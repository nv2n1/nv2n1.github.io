---
title: "xkbfreegeomproperties(3)"
name: "xkbfreegeomproperties"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreegeomproperties/"
description: "XkbFreeGeomProperties – Free geometry properties"
---

<p>XkbFreeGeomProperties &#8211; Free geometry properties </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeGeomProperties</code> <code>(XkbGeometryPtr </code><i>geom</i><code>,</code> <code>int </code><i>first</i><code>,</code> <code>int </code><i>count</i><code>,</code> <code>Bool *</code><i>free_all</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; geom</i></p>
<dd>
<dd>geometry in which properties should be freed</p>
<dt><i>&#8211; first</i></p>
<dd>first property to be freed</p>
<dt><i>&#8211; count</i></p>
<dd>number of properties to be freed</p>
<dt><i>&#8211; free_all</i></p>
<dd>True =&gt; all properties are freed</dl>
<h2>Description</h2>
<p>Xkb provides a number of functions to allocate and free subcomponents of a keyboard geometry. Use these functions to create or modify keyboard geometries. Note that these functions merely allocate space for the new element(s), and it is up to you to fill in the values explicitly in your code. These allocation functions increase <i>sz_* </i> but never touch <i>num_* </i> (unless there is an allocation failure, in which case they reset both <i>sz_* </i> and <i>num_* </i> to zero). These functions return Success if they succeed, BadAlloc if they are not able to allocate space, or BadValue if a parameter is not as expected. </p>
<p> If <i>free_all </i> is True, all properties are freed regardless of the value of <i>first </i> or <i>count. </i> Otherwise, <i>count </i> properties are freed beginning with the one specified by <i>first.</i></p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>Success</p>
<dd>The XkbFreeGeomProperties function returns Success when there are no allocation or argument errors.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>
