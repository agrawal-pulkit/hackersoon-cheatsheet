---
title: "Vault Acl"
date: 2019-12-12T02:12:50+05:30
 
weight: 999
---


{{% children depth="3" sort="weight" %}}


## **Authenticatin Methods**

Different types of authentication methods:

- Internal Authentication
- External Authentication
- Multiple Authentication

## **Commands for create authentication methods**

### **Enable an auth method**

    vault auth enable [method]

### **Write Config to an auth method**

    vault write auth/[method]/config

### **Add a role to the auth method**

    vault write auth/[method]/role/[rolename]

### **Disable an auth method**

    vault auth disable [method]

## **Enable userpass method**

### **Add envirnmont variables**

    export VAULT_ADDR='http://127.0.0.1:8200/'
    export VAULT_TOKEN=<token>

### **Check auth list**

    vault auth list

### **Enable userpass auth method**

- Using vault cli
```
    vault auth enable userpass
```
- using curl api
```
    cutl --header "x-Vault-Token: $VAULT_TOKEN" --request POST \ --data '{"type":"userpass"}' $VAULT_ADDR/v1/sys/auth/userpass
```
### **Add a user to the userpass auth method**

### **create a user with password**

    vault write auth/userpass/users/<username> password=<****>

### **get users from userpass methos**

    vault list auth/userpass/users
    
### **login in vault with new userpass user credential**

- login in new user
```
    vault login -method=userpass username=<username>
```
- set vault token as new token
```
    export VAULT_TOKEN=<new token>
    vault token lookup
```
### **Remove account**

    vault delete auth/username/users/<username>

## **Vault Policies**

- Wallet policies use for provide the role based access.
- Who, What and How?
- we can use hcl or json templates for writing the policy files(mostly HCL)
- variables for identity

`Sample Plolicy document`

    path "path_of_secret_data/[*]" {
        capabilities = ["create", "read", "update", "list", "delete"]
        required_parameters = ["param_names"]
        allowed_parameters = {
            param_name = ["any"]
        }
        denied_parameter = {
            param_name = ["any"]
        }
    }

### **Useful commands for vault policies**

### **list policies**

    vault policy list

### **create a policy**

    vault policy write [policy] [policy_file.hcl]

### **update a policy**

    vault write sys/policy/[policy] policy=[policy_file.hcl]

### **delete a policy**

    vault delete sys/policy/[policy]

### **Create a sample policy**

- create a sample policy file
```
    cat > sample_policy.hcl
    path "kv-v2/*" {
        capabilities = ["create", "read", "update", "list", "delete"]
    }
    
    path "kv-v2/appId*" {
        capabilities = ["create", "read", "update", "list", "delete"]
    
        allowed_parameters = {
            "api-key"= []
            "environment" = ["dev", "staging"]
            "description" = []
        }
    }
    
    path "secret/data/{{identity.entity.id}}/*" {
        capabilities = ["create", "read", "update", "delete"]
    }
    
    path "secret/metadata/{{identity.entity.id}}/*" {
        capabilities = ["list"]
    }
```
- run create policy command
```
    vault policy write dev1 sample-policy.hcl
```
- create a userpass with policy
```
    vault write auth/userpass/users/<username> password=<****> pol
```