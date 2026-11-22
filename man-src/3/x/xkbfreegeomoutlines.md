---
title: "xkbfreegeomoutlines(3)"
name: "xkbfreegeomoutlines"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreegeomoutlines/"
description: "XkbFreeGeomOutlines – Free geometry outlines"
---

<p>XkbFreeGeomOutlines &#8211; Free geometry outlines </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeGeomOutlines</code> <code>(XkbShapePtr </code><i>shape</i><code>,</code> <code>int </code><i>first</i><code>,</code> <code>int </code><i>count</i><code>,</code> <code>Bool </code><i>free_all</i><code>);</code><br/>
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dt></dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; shape</i></dt>
<dd>
</dd><dd>shape in which outlines should be freed</dd>
<dt><i>&#8211; first</i></dt>
<dd>first outline to be freed</dd>
<dt><i>&#8211; count</i></dt>
<dd>number of outlines to be freed</dd>
<dt><i>&#8211; free_all</i></dt>
<dd>True =&gt; all outlines are freed</dd></dl>
<h2>Description</h2>
<p>If <i>free_all </i> is True, all outlines are freed regardless of the value of <i>first </i> or <i>count. </i> Otherwise, <i>count </i> outlines are freed beginning with the one specified by <i>first.</i></p>
