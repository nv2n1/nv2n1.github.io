---
title: "dev_valid_name(9)"
name: "dev_valid_name"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dev_valid_name/"
description: "dev_valid_name – check if name is okay for network device"
---

<p>dev_valid_name &#8211; check if name is okay for network device</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool dev_valid_name(const char&nbsp;<wbr>*&nbsp;<wbr></code><i>name</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>name</i></p>
<dl>
<dd>
<dd>name string</dl>
<h2>Description</h2>
<p>Network device names need to be valid file names to to allow sysfs to work. We also disallow any kind of whitespace.</p>
<h2>Copyright</h2>
