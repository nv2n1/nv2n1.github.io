---
title: "abrt-harvest-vmcore(1)"
name: "abrt-harvest-vmcore"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-harvest-vmcore/"
---

<h2 class="name">NAME</h2>
 

 abrt-harvest-vmcore - Converts VMCores to ABRT problems 

<h2>SYNOPSIS</h2>

 

 <i>abrt-harvest-vmcore</i>

<h2>DESCRIPTION</h2>

 

 This script is meant to be run once at system startup after abrtd is up and running. It moves all vmcore directories in /var/crash (which are presumably created by kdump) to abrtd spool directory. 

 The goal is to let abrtd notice and process them as new problem data dirs.

<h2>FILES</h2>

 

 /etc/abrt/plugins/vmcore.conf
<dl>
<dt>
<dd> Configuration file where user can enable copying or moving VMcore to ABRT problem directory</dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-abrt-vmcore-conf/">abrt-vmcore.conf</a>(5) <a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
<dd> &bull; ABRT team</dl>
 

<h2>Index</h2>


