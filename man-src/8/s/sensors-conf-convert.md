---
title: "sensors-conf-convert(8)"
name: "sensors-conf-convert"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sensors-conf-convert/"
description: "sensors-conf-convert – sensors configuration conversion"
---

<p>sensors-conf-convert &#8211; sensors configuration conversion</p>
<h2>Synopsis</h2>
<p><code>sensors-conf-convert</code> &lt; <i>/etc/sensors.conf</i> &gt; <i>/etc/sensors3.conf</i> </p>
<h2>Description</h2>
<p>The purpose of the <code>sensors-conf-convert</code> tool is to convert <i>sensors.conf</i> from the lm_sensors version 2 format to the lm_sensors version 3 format. The old configuration file is read from the standard input and the new one is written to the standard output. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-sensors/">sensors</a>(1), <a href="/docs/linux/man/3-libsensors/">libsensors</a>(3) </p>
<h2>Author</h2>
<p>Jean Delvare</p>
