---
title: "fcweighttoopentypedouble(3)"
name: "fcweighttoopentypedouble"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcweighttoopentypedouble/"
description: "FcWeightToOpenTypeDouble – Convert from fontconfig weight values to OpenType ones"
---

<p>FcWeightToOpenTypeDouble &#8211; Convert from fontconfig weight values to OpenType ones </p>
<h2>Synopsis</h2>
<p><code>#include &lt;fontconfig/fontconfig.h&gt; </p>
<p> double FcWeightToOpenTypeDouble (double</code><i>ot_weight</i><code>); </code></p>
<h2>Description</h2>
<p><code>FcWeightToOpenTypeDouble</code> is the inverse of <code>FcWeightFromOpenType</code>. If the input is less than FC_WEIGHT_THIN or greater than FC_WEIGHT_EXTRABLACK, returns -1. Otherwise returns a number in the range 1 to 1000.</p>
<h2>Since</h2>
<p>version 2.12.92</p>
