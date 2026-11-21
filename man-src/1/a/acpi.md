---

title: "acpi(1)"
name: "acpi"
section: "1"
letter: "a"
url: "/docs/linux/man/1-acpi/"
description: "acpi – Shows battery status and other ACPI information"
---

<p> acpi &#8211; Shows battery status and other ACPI information</p>
<h2>SYNOPSIS</h2>
<p> <code>acpi</code> [<code>options</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>acpi</code> Shows information from the /proc or the /sys filesystem, such as battery status or thermal information.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b | &#8211;battery</code></dt>
<dd> show battery information</dd>
<dt><code>-a | &#8211;ac-adapter</code></dt>
<dd> show ac adapter information</dd>
<dt><code>-t | &#8211;thermal</code></dt>
<dd> show thermal information</dd>
<dt><code>-c | &#8211;cooling</code></dt>
<dd> show cooling device information</dd>
<dt><code>-V | &#8211;everything</code></dt>
<dd> show every device, overrides above options</dd>
<dt><code>-s | &#8211;show-empty</code></dt>
<dd> show non-operational devices</dd>
<dt><code>-i | &#8211;details</code></dt>
<dd> show additional details if available:</dd>
<dt>
</dt><dd> * battery capacity information</dd>
<dt>
</dt><dd> * temperature trip points</dd>
<dt><code>-f | &#8211;fahrenheit</code></dt>
<dd> use fahrenheit as the temperature unit instead of default celsius</dd>
<dt><code>-k | &#8211;kelvin</code></dt>
<dd> use kelvin as the temperature unit instead of default celsius</dd>
<dt><code>-p | &#8211;proc</code></dt>
<dd> use the old /proc interface, default is the new /sys one</dd>
<dt><code>-d | &#8211;directory &lt;dir&gt;</code></dt>
<dd> path to ACPI info (either /proc/acpi or /sys/class)</dd>
<dt><code>-h | &#8211;help</code></dt>
<dd> display help and exit</dd>
<dt><code>-v | &#8211;version</code></dt>
<dd> output version information and exit </dd>
</dl>
<h2>AUTHOR</h2>
<p> The original version of this manual page was written by Paul Telford &lt;pxt [at] debian.org&gt; for the <code>Debian</code> system. Newer additions were done my Michael Meskes &lt;meskes [at] debian.org&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU GPL. </p>
