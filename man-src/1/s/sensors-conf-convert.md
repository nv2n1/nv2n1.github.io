---
title: "sensors-conf-convert(1)"
name: "sensors-conf-convert"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sensors-conf-convert/"
description: "sensors-conf-convert – convert sensors.conf from lm-sensors 2 format to lm-sensors 3 format"
---

<h2>SYNOPSIS</h2>
<p> <code>sensors-conf-convert</code> <i>&lt; /etc/sensors.conf &gt; /etc/sensors3.conf</i></p>
<h2>DESCRIPTION</h2>
<p> <code>sensors-conf-convert</code> converts a sensors.conf file from the old (Linux 2.4, lm-sensors 2) symbol names to the new (Linux 2.6, lm-sensors 3) symbol names. </p>
<p> Implemented conversions:</p>
<dl>
<dt>&#8211; The &quot;algorithm name&quot; part of bus statements is removed.</dt>
<dd>
</dd><dt>&#8211; Bus statements for the ISA bus are removed.</dt>
<dd>
</dd><dt>&#8211; Chip names containing dashes are removed.</dt>
<dd>
</dd><dt>&#8211; Label, ignore, set and compute statements referencing features</dt>
<dd> which are not part of the new interface are removed.</dd>
<dt>&#8211; Label, ignore, set and compute statements referencing features</dt>
<dd> which have been renamed are updated. This includes both general feature name changes and chip-specific feature name changes.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-sensors-conf/">sensors.conf</a>(5)</p>
<h2>AUTHOR</h2>
<p> Jean Delvare. </p>
