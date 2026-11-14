---
title: "abrt-xorg(5)"
name: "abrt-xorg"
section: "5"
letter: "a"
url: "/docs/linux/man/5-abrt-xorg/"
---

abrt-xorg.conf - Configuration file for abrt-action-analyze-xorg

<h2>Description</h2>

The <i>abrt-action-analyze-xorg</i> tool processes Xorg crash problem data and generates deduplication hashes for it. 

 The configuration file consists of items in the format &quot;Option = Value&quot;. Currently, only one item exists: 

 BlacklistedXorgModules = <i>moduleName</i>, <i>moduleName</i> ...
<dl><dd>Xorg crash will be ignored if any of the listed Xorg modules were loaded at the time of the crash. Module names should be without &quot;_drv.so&quot; suffix: use <i>buggymodule</i>, not <i>buggymodule_drv</i> or <i>buggymodule_drv.so</i>.</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-abrt-action-analyze-xorg/">abrt-action-analyze-xorg</a>(1) <a HREF="/docs/linux/man/5-abrt-conf/">abrt.conf</a>(5)

<h2>Authors</h2>

<dl><dd>&bull; ABRT team</dl>
