---

title: "abrt-harvest-vmcore(1)"
name: "abrt-harvest-vmcore"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abrt-harvest-vmcore/"
---

abrt-harvest-vmcore - Converts VMCores to ABRT problems 

<i>abrt-harvest-vmcore</i>

This script is meant to be run once at system startup after abrtd is up and running. It moves all vmcore directories in /var/crash (which are presumably created by kdump) to abrtd spool directory. 

 The goal is to let abrtd notice and process them as new problem data dirs.

<h2>FILES</h2>

 

 /etc/abrt/plugins/vmcore.conf
<dl>
<dt>
</dt><dd> Configuration file where user can enable copying or moving VMcore to ABRT problem directory</dd></dl>

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/5-abrt-vmcore-conf/">abrt-vmcore.conf</a>(5) <a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>AUTHORS</h2>

 

<dl>
<dt>
</dt><dd> &bull; ABRT team</dd></dl>
