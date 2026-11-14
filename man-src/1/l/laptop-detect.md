---
title: "laptop-detect(1)"
name: "laptop-detect"
section: "1"
letter: "l"
url: "/docs/linux/man/1-laptop-detect/"
description: "laptop-detect – attempt to detect a laptop"
---

<h2 class="name">NAME</h2>
<p> laptop-detect &#8211; attempt to detect a laptop </p>
<h2>SYNOPSIS</h2>
<p> laptop-detect [<i>-h</i>|<i>&#8211;help</i>|<i>-v</i>|<i>&#8211;verbose</i>|<i>-V</i>|<i>&#8211;version</i>|<i>-D</i>|<i>&#8211;debug</i>]</p>
<h2>DESCRIPTION</h2>
<p> Laptop-detect attempts to determine whether it is being run on a laptop or a desktop and appraises its caller of this.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> Output help information and exit.</p>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd> be verbose (messages go to STDOUT)</p>
<dt><code>-V</code> <code>&#8211;version</code></p>
<dd> Output version information and exit.</p>
<dt><code>-D</code> <code>&#8211;debug</code></p>
<dd> Debug mode.</dl>
<h2>EXIT STATUS</h2>
<pre>
<code>0</code>       most likely running on a laptop
<code>1</code>       most likely NOT running on a laptop
<code>2</code>       usage error (arguments supplied)
</pre>
<h2>FILES</h2>
<p> <i>/proc/acpi/battery</i><br />
 <i>/proc/pmu/info</i><br />
 <i>/dev/mem</i><br />
 <i>/sys/devices/virtual/dmi/id/chassis_type</i><br />
 <i>/sys/class/power_supply/*/type</i><br />
 <i>/proc/apm</i></p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-dmidecode/">dmidecode</a>(8) </p>
<h2>Index</h2>
