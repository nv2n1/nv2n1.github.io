---
title: "ec2meta(1)"
name: "ec2meta"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ec2meta/"
---

<h2 class="name">NAME</h2>
 

 ec2meta - get the metadata for this particular ec2 instance 

<h2>SYNOPSIS</h2>

 ec2meta -h --help [type]

<h2>ARGUMENTS</h2>

 With a <font SIZE="-1">TYPE</font> reports just that <font SIZE="-1">TYPE</font> of meta data. With out one reports on all meta data available. (except the keys, which are listed by name, not value) 

 The -h flag displays this help message. 

 types: 

 <pre>
 ami_id             The AMI ID used to launch the instance. 1.0
 ami_manifest_path  The manifest path of the AMI with which the instance was launched.  1.0
 ami_launch_index   The index of this instance in the reservation (per AMI).    1.0
 ancestor_ami_ids   The AMI IDs of any instances that were rebundled to create this AMI.    2007_10_10
 instance_id        The ID of this instance.    1.0
 instance_type      The type of instance to launch. For more information, see Selecting Instance Types. 2007_08_29
 local_hostname     The local hostname of the instance. 2007_01_19
 public_hostname    The public hostname of the instance.    2007_01_19
 local_ipv4         Public IP address if launched with direct addressing; private IP address if launched with public addressing.    1.0
 public_ipv4        NATted public IP Address    2007_01_19
 public_keys/       Public keys. Only available if supplied at instance launch time 1.0
 reservation_id     ID of the reservation.  1.0
 security_groups    Names of the security groups the instance is launched in. Only available if supplied at instance launch time    1.0
 product_codes      Product codes associated with this instance.    2007_03_01
 user_data          User supplied data at instance launch
</pre> 

<h2>Index</h2>


