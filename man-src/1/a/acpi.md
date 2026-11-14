---
title: "acpi(1)"
name: "acpi"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acpi/"
description: "acpi – Shows battery status and other ACPI information"
---

<h2>NAME</h2>
<p> acpi &#8211; Shows battery status and other ACPI information</p>
<h2>SYNOPSIS</h2>
<p> <code>acpi</code> [<code>options</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>acpi</code> Shows information from the /proc or the /sys filesystem, such as battery status or thermal information.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b | &#8211;battery</code></p>
<dd> show battery information</p>
<dt><code>-a | &#8211;ac-adapter</code></p>
<dd> show ac adapter information</p>
<dt><code>-t | &#8211;thermal</code></p>
<dd> show thermal information</p>
<dt><code>-c | &#8211;cooling</code></p>
<dd> show cooling device information</p>
<dt><code>-V | &#8211;everything</code></p>
<dd> show every device, overrides above options</p>
<dt><code>-s | &#8211;show-empty</code></p>
<dd> show non-operational devices</p>
<dt><code>-i | &#8211;details</code></p>
<dd> show additional details if available:</p>
<dt>
<dd> * battery capacity information</p>
<dt>
<dd> * temperature trip points</p>
<dt><code>-f | &#8211;fahrenheit</code></p>
<dd> use fahrenheit as the temperature unit instead of default celsius</p>
<dt><code>-k | &#8211;kelvin</code></p>
<dd> use kelvin as the temperature unit instead of default celsius</p>
<dt><code>-p | &#8211;proc</code></p>
<dd> use the old /proc interface, default is the new /sys one</p>
<dt><code>-d | &#8211;directory &lt;dir&gt;</code></p>
<dd> path to ACPI info (either /proc/acpi or /sys/class)</p>
<dt><code>-h | &#8211;help</code></p>
<dd> display help and exit</p>
<dt><code>-v | &#8211;version</code></p>
<dd> output version information and exit </p>
</dl>
<h2>AUTHOR</h2>
<p> The original version of this manual page was written by Paul Telford &lt;pxt [at] debian.org&gt; for the <code>Debian</code> system. Newer additions were done my Michael Meskes &lt;meskes [at] debian.org&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU GPL. </p>
<h2>Index</h2>
