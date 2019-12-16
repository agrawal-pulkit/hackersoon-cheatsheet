---
title: "Consul_vault"
date: 2019-12-12T02:12:50+05:30
 
weight: 999
---

{{% children depth="3" sort="weight" %}}


### This tutorial is to setup consul and vault in mac.
Install consul using homebrew:

    brew install consul

Install vault using homebrew:

    brew install vault

Run consul and vault in your system:

    Consul agent — dev
    Vault server -dev

#### Consul: key/value
Create a key/value in consul.

    consul kv put test/data/key value

This command will create hierarchy test=>data=> {key: value}
Get a key/value from the consul.

    consul kv get test/data/key value

#### Vault: key/value
Vault Authentication after installation
Unseal vault using master keys these keys created for the first time. please contact an administrator for getting keys.

    vault operator unseal

Login in the vault using the root token.

    vault login

Enable key-value in vault this is for the first time enable.

    vault secrets enable -path=kv kv-v2

Create a key value in the vault.

    vault kv put kv-v2/hello key=value  

output: 

    Key              Value 
    ---              -----
    created_time     2019-07-10T07:52:26.062739464Z 
    deletion_time    n/a 
    destroyed        false 
    version          1

get a key-value from the vault.

    vault kv get kv-v2/hello  

output: 

    Key              Value 
    ---              ----- 
    created_time     2019-07-10T07:52:26.062739464Z 
    deletion_time    n/a 
    destroyed        false 
    version          1  
    === Data === 
    Key    Value 
    ---    ----- 
    key    value

{{% notice warning %}}
Don't share your vault token with anybody.
{{% /notice%}}