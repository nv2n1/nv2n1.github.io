---
title: "fcweightfromopentypedouble(3)"
name: "fcweightfromopentypedouble"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcweightfromopentypedouble/"
description: "FcWeightFromOpenTypeDouble – Convert from OpenType weight values to fontconfig ones"
---

<p>FcWeightFromOpenTypeDouble &#8211; Convert from OpenType weight values to fontconfig ones </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> double FcWeightFromOpenTypeDouble (double</code><i>ot_weight</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcWeightFromOpenTypeDouble</code> returns an double value to use with FC_WEIGHT, from an double in the 1..1000 range, resembling the numbers from OpenType specification&#8217;s OS/2 usWeight numbers, which are also similar to CSS font-weight numbers. If input is negative, zero, or greater than 1000, returns -1. This function linearly doubleerpolates between various FC_WEIGHT_* constants. As such, the returned value does not necessarily match any of the predefined constants.</p>
<h2>Since</h2>
<p>version 2.12.92</p>
