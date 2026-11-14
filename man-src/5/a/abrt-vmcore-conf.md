---
title: "abrt-vmcore-conf(5)"
name: "abrt-vmcore-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-abrt-vmcore-conf/"
---

abrt-vmcore.conf - Configuration file for Configuration file for ABRT's VMCore addon

<h2>Description</h2>

The configuration file consists of items in the format &quot;Option = Value&quot;. Currently, only one item exists: 

 CopyVMcore = <i>yes</i> / <i>no</i>
<dl><dd>Set to <i>no</i> if you want vmcore to be moved, not copied, from /var/crash to ABRT's main problem directory. Default is to copy vmcore.</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-abrt-harvest-vmcore/">abrt-harvest-vmcore</a>(1) <a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>Authors</h2>

<dl><dd>&bull; ABRT team</dl>
