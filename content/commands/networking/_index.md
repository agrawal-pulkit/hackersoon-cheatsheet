---
title: "Networking"
date: 2019-12-11T11:41:10+05:30
 
weight: 70
---

{{% children depth="3" sort="weight" %}}

#### nc

    # Listener: 
    nc -l 1234 > out.file

    # Producer: 
    nc -w 3 <ip> 1234 < out.file

#### find which service is running and process info

    netstat -nltp

    #porcess
    ps -ef
    pas aux

#### change the boot disk size of instance without restart 

    lsblk
    growpart /dev/sda 1
    resize2fs /dev/sda1
    df -h

#### check disk size

    df -h
    du -csh *