---
title: "abrt-python-conf(5)"
name: "abrt-python-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-abrt-python-conf/"
---

abrt-python.conf - Configuration file for ABRT's python crash hook

<h2>Description</h2>

Currently, only one item exists: 

 RequireAbsolutePath = <i>yes</i> / <i>no</i> ...
<dl><dd>If set to <i>no</i>, unhandled python exceptions will be caught and saved even in scripts which are run without full path in sys.argv[0]. Default is <i>yes</i>: do not save them.</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>Authors</h2>

<dl><dd>&bull; ABRT team</dl>
