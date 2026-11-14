---
title: "abrt-ccpp(5)"
name: "abrt-ccpp"
section: "5"
letter: "a"
url: "/docs/linux/man/5-abrt-ccpp/"
---

abrt-CCpp.conf - Configuration file for ABRT's core dump crash hook

<h2>Description</h2>

The configuration file consists of items in the format &quot;Option = Value&quot;. Ithe following items are recognized: 

 MakeCompatCore = <i>yes</i> / <i>no</i> ...
<dl><dd>If you also want to dump file named &quot;core&quot; in crashed process' current dir, set to &quot;yes&quot;.</dl>
 

 SaveBinaryImage = <i>yes</i> / <i>no</i> ...
<dl><dd>Do you want a copy of crashed binary be saved? Useful, for example, when <i>deleted binary</i> segfaults. Default is <i>no</i>.</dl>
 

 VerboseLog = NUM
<dl><dd>Used to make the hook more verbose</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>Authors</h2>

<dl><dd>&bull; ABRT team</dl>
