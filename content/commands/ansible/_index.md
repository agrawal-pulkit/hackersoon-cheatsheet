---
title: "Ansible"
date: 2019-12-13T02:40:30+05:30
 
weight: 999
---

{{% children depth="3" sort="weight" %}}

* list ansible dynamic inventory
```
    ansible-inventory -i <inventory-path> --list
```

* run ansible playbook
```
    anible-playbook -i <inventory-path> <playbook>.yml -t tag --user=<user>
```