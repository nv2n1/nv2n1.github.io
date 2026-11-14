---
title: "dmi_get_system_info(9)"
name: "dmi_get_system_info"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dmi_get_system_info/"
---

dmi_get_system_info - return DMI data value

<h2>Synopsis</h2>

<pre><code>const char *dmi_get_system_info(int field);</code></pre>

<h2>Arguments</h2>

<i>field</i>
<dl><dd><dd>data index (see enum dmi_field)</dl>

<h2>Description</h2>

Returns one DMI data value, can be used to perform complex DMI data checks.

<h2>Copyright</h2>


