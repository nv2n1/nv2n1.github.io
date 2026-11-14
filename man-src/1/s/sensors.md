---
title: "sensors(1)"
name: "sensors"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sensors/"
description: "sensors – print sensors information"
---

<h2 class="name">NAME</h2>
<p> sensors &#8211; print sensors information </p>
<h2>SYNOPSIS</h2>
<p> <code>sensors [</code> <i>options</i> <code>] [</code> <i>chips</i> <code>]</code><br />
 <code>sensors -s [</code> <i>chips</i> <code>]</code><br />
 <code>sensors &#8211;bus-list</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>sensors</code> is used to show the current readings of all sensor chips.<br />
 <code>sensors -s</code> is used to set all limits as specified in the configuration file.<br />
 <code>sensors &#8211;bus-list</code> is used to generate bus statements suitable for the configuration file. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-c, &#8211;config-file config-file</p>
<dd> Specify a configuration file. If no file is specified, the libsensors default configuration file is used. Use `-c /dev/null&#8217; to temporarily disable this default configuration file.</p>
<dt>-h, &#8211;help</p>
<dd> Print a help text and exit.</p>
<dt>-s, &#8211;set</p>
<dd> Evaluate all `set&#8217; statements in the configuration file and exit. You must be `root&#8217; to do this. If this parameter is not specified, no `set&#8217; statement is evaluated.</p>
<dt>-A, &#8211;no-adapter</p>
<dd> Do not show the adapter for each chip.</p>
<dt>-u</p>
<dd> Raw output. This mode is suitable for debugging and for post-processing of the output by scripts. It is also useful when writing a configuration file because it shows the raw input names which must be referenced in the configuration file.</p>
<dt>-j</p>
<dd> Json output. This mode is suitable for post-processing of the output by scripts.</p>
<dt>-v, &#8211;version</p>
<dd> Print the program version and exit.</p>
<dt>-f, &#8211;fahrenheit</p>
<dd> Print the temperatures in degrees Fahrenheit instead of Celsius.</p>
<dt>&#8211;bus-list</p>
<dd> Generate bus statements suitable for using in sensors.conf. Such bus statements are only needed if you have several chips sharing the same address on different buses of the same type. As bus numbers are usually not guaranteed to be stable over reboots, these statements let you refer to each bus by its name rather than numbers.</dl>
<h2>FILES</h2>
<p> <i>/etc/sensors3.conf</i><br />
 <i>/etc/sensors.conf</i></p>
<dl>
<dt>
<dd> The system wide configuration file. See <code><a href="/docs/linux/man/5-sensors-conf/">sensors.conf</a></code>(5) for further details.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-sensors-conf/">sensors.conf</a>(5), <a href="/docs/linux/man/8-sensors-detect/">sensors-detect</a>(8). </p>
<h2>AUTHOR</h2>
<p> Frodo Looijaard and the lm_sensors group <a rel="nofollow" href="https://hwmon.wiki.kernel.org/lm_sensors">https://hwmon.wiki.kernel.org/lm_sensors</a> </p>
<h2>Index</h2>
