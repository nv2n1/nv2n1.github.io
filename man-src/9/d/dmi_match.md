---
title: "dmi_match(9)"
name: "dmi_match"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dmi_match/"
description: "dmi_match – compare a string to the dmi field (if exists)"
---

<p>dmi_match &#8211; compare a string to the dmi field (if exists)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool dmi_match(enum dmi_field&nbsp;<wbr></code><i>f</i><code>, const char&nbsp;<wbr>*&nbsp;<wbr></code><i>str</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>f</i></p>
<dl>
<dd>
<dd>DMI field identifier</dl>
<p> <i>str</i></p>
<dl>
<dd>string to compare the DMI field to</dl>
<h2>Description</h2>
<p>Returns true if the requested field equals to the str (including NULL).</p>
<h2>Copyright</h2>
