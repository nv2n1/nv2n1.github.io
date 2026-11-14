---
title: "sas_disk_blink(8)"
name: "sas_disk_blink"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sas_disk_blink/"
description: "sas_disk_blink – blink the LED on a SAS disk"
---

<p>sas_disk_blink &#8211; blink the LED on a SAS disk</p>
<h2>Synopsis</h2>
<p><code>sas_disk_blink</code> [<i>&#8211;help</i>] [<i>&#8211;set NUM</i>] [<i>&#8211;verbose</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This bash shell script attempts to blink the LED on the SAS disk referred to by <i>DEVICE</i>. By default the LED will blink for 30 seconds. This is meant to help identify which disk corresponds to a given <i>DEVICE</i>. </p>
<p> The script use the sdparm utility and manipulates the &quot;Ready LED Meaning&quot; (RLM) field in the Protocol specific port mode page in order to blink the LED.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-s</code>, <code>&#8211;set</code> <i>NUM</i></p>
<dd>when <i>NUM</i> is 0 then the RLM field is cleared. When <i>NUM</i> is 1 then the RLM field is set. When <i>NUM</i> &gt; 1 then the SAS disk LED is made to blink for <i>NUM</i> seconds. If this option is not given then the SAS disk LED is made to blink for 30 seconds.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level or verbosity.</dl>
<h2>Exit Status</h2>
<p>The exit status of this script is 0 when it is successful. Otherwise the exit status is that of the last sdparm utility called. See the <a href="/docs/linux/man/8-sdparm/">sdparm</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by D. Gilbert</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sdparm (sdparm)</code> </p>
