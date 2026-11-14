---
title: "xkbfreegeomkeys(3)"
name: "xkbfreegeomkeys"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreegeomkeys/"
description: "XkbFreeGeomKeys – Free geometry keys"
---

<p>XkbFreeGeomKeys &#8211; Free geometry keys </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeGeomKeys</code> <code>(XkbRowPtr </code><i>row</i><code>,</code> <code>int </code><i>first</i><code>,</code> <code>int </code><i>count</i><code>,</code> <code>Bool </code><i>free_all</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; row</i></p>
<dd>
<dd>row in which keys should be freed</p>
<dt><i>&#8211; first</i></p>
<dd>first key to be freed</p>
<dt><i>&#8211; count</i></p>
<dd>number of keys to be freed</p>
<dt><i>&#8211; free_all</i></p>
<dd>True =&gt; all keys are freed</dl>
<h2>Description</h2>
<p>If <i>free_all </i> is True, all keys are freed regardless of the value of <i>first </i> or <i>count. </i> Otherwise, <i>count </i> keys are freed beginning with the one specified by <i>first.</i></p>
