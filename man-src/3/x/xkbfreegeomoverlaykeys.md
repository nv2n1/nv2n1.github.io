---
title: "xkbfreegeomoverlaykeys(3)"
name: "xkbfreegeomoverlaykeys"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbfreegeomoverlaykeys/"
description: "XkbFreeGeomOverlayKeys – Free keys in an overlay row"
---

<p>XkbFreeGeomOverlayKeys &#8211; Free keys in an overlay row </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>void XkbFreeGeomOverlayKeys</code> <code>(XkbRowPtr </code><i>row</i><code>,</code> <code>int </code><i>first</i><code>,</code> <code>int </code><i>count</i><code>,</code> <code>Bool </code><i>free_all</i><code>);</code><br />
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
<p>Xkb provides a number of functions to allocate and free subcomponents of a keyboard geometry. Use these functions to create or modify keyboard geometries. Note that these functions merely allocate space for the new element(s), and it is up to you to fill in the values explicitly in your code. These allocation functions increase <i>sz_* </i> but never touch <i>num_* </i> (unless there is an allocation failure, in which case they reset both <i>sz_* </i> and <i>num_* </i> to zero). These functions return Success if they succeed, BadAlloc if they are not able to allocate space, or BadValue if a parameter is not as expected. </p>
<p> If <i>free_all </i> is True, all keys are freed regardless of the value of <i>first </i> and <i>count. </i> Otherwise, the number of keys specified by <i>count </i> are freed, beginning with the key specified by <i>first </i> in the specified row.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>Success</p>
<dd>The XkbFreeGeomOverlayKeys function returns Success if there are no allocation or argument errors.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadValue</code></p>
<dd>An argument is out of range </p>
</dl>
