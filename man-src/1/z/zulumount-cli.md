---
title: "zulumount-cli(1)"
name: "zulumount-cli"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zulumount-cli/"
---

zuluMount-cli - command line tool that manages encrypted and unencrypted volumes
<h2>Description</h2>zuluMount-cli is a tool that has a primary mission of opening and closing encrypted volumes as well as mounting and unmounting unecrypted volumes and opened encrypted ones.Its primary purpose is to do what tools like udisks does. 
 

<h2>Usage</h2>usage: see examples below 

 
 options: 
 -m -- mount a volume : arguments: -d volume_path -z mount_point -e mode(rw/ro) 
-- additional arguments for crypto_LUKS,crypto_PLAIN,crypto_TCRYPT volumes, -p passphrase/-f keyfile 
 -z -- mount point component to append to &quot;/run/media/private/$USER/&quot; 
 -u -- unmount a volume: arguments: -d volume_path 
 -s -- print properties of an encrypted volume: arguments: -d volume_path 
 -o -- offset in sectors on where the volume starts in the volume.The volume is assumed to be plain type with this option 
and the option must be given when -u or -s arguments are used with a volume opened with this option 
 -M -- this option will create a mount point in &quot;/run/media/private/$USER/&quot; and a publicly accessible &quot;mirror&quot; in &quot;/run/media/public/' 
 -l -- print expanded list of all volumes 
 -Y -- file system options 
 -e -- mount options 
 -t -- volume type to assume when unlocking a volume.Use &quot;vera&quot; when unlocking a VeraCrypt volume. 
 -L -- must be used with -d,print properties of a volume specified by d option 
 -P -- print a list of all volumes 
 -A -- print a list of all volumes 
 -S -- print a list of system volumes 
 -N -- print a list of non system volumes 
 -E -- print a list of mounted volumes 
 -D -- get a device node address from its mapper path( mapper paths are usually located in /dev/mapper ). Required argument: -d 
 -F -- path to truecrypt multiple keyfiles.Keyfiles are separated by &quot;\011&quot; character sequence 
 examples: 
 mount a volume : zuluMount-cli -m -d /dev/sdc1 
 unmount a volume: zuluMount-cli -u -d /dev/sdc1 
 mount and encrypted volume with a key &quot;xyz&quot; : zuluMount-cli -m -d /dev/sdc2 -p xyz 
 

<h2>Copyright</h2>Copyright (c) 2011-2015 
 name : Francis Banyikwa 
 email: mhogomchungu [at] gmail.com 
 
 

 This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see &lt;<a rel="nofollow" HREF="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. 
 

<h2>Last Edit</h2>Last change: Fri Mar 13 01:12:21 EAT 2015
