---
title: "dmi_get_date(9)"
name: "dmi_get_date"
section: "9"
letter: "d"
url: "/docs/linux/man/9-dmi_get_date/"
description: "dmi_get_date – parse a DMI date"
---

<p>dmi_get_date &#8211; parse a DMI date</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>bool dmi_get_date(int&nbsp;<wbr></code><i>field</i><code>, int&nbsp;<wbr>*&nbsp;<wbr></code><i>yearp</i><code>, int&nbsp;<wbr>*&nbsp;<wbr></code><i>monthp</i><code>, int&nbsp;<wbr>*&nbsp;<wbr></code><i>dayp</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>field</i></p>
<dl>
<dd>
<dd>data index (see enum dmi_field)</dl>
<p> <i>yearp</i></p>
<dl>
<dd>optional out parameter for the year</dl>
<p> <i>monthp</i></p>
<dl>
<dd>optional out parameter for the month</dl>
<p> <i>dayp</i></p>
<dl>
<dd>optional out parameter for the day</dl>
<h2>Description</h2>
<p>The date field is assumed to be in the form resembling [mm[/dd]]/yy[yy] and the result is stored in the out parameters any or all of which can be omitted. </p>
<p> If the field doesn&#8217;t exist, all out parameters are set to zero and false is returned. Otherwise, true is returned with any invalid part of date set to zero. </p>
<p> On return, year, month and day are guaranteed to be in the range of [0,9999], [0,12] and [0,31] respectively.</p>
<h2>Copyright</h2>
