---
title: "xkballocindicatormaps(3)"
name: "xkballocindicatormaps"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkballocindicatormaps/"
description: "XkbAllocIndicatorMaps – Allocates, directly, the indicators member of the keyboard description record"
---

<p>XkbAllocIndicatorMaps &#8211; Allocates, directly, the <i>indicators </i> member of the keyboard description record </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbAllocIndicatorMaps</code> <code>(variable_type *</code><i>xkb</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; xkb</i></p>
<dd>
<dd>keyboard description structure</dl>
<h2>Description</h2>
<p>The <i>xkb </i> parameter must point to a valid keyboard description. If it doesn&#8217;t, <i>XkbAllocIndicatorMaps </i> returns a BadMatch error. Otherwise, <i>XkbAllocIndicatorMaps </i> allocates and initializes the <i>indicators </i> member of the keyboard description record and returns Success. If <i>XkbAllocIndicatorMaps </i> was unable to allocate the indicators record, it reports a BadAlloc error.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>Success</p>
<dd>The <i>XkbAllocIndicatorMaps </i> function returns Success if it is successful in allocating and initializing the <i>indicators </i> member of the keyboard description record.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</p>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage </p>
</dl>
