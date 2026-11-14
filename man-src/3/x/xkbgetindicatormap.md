---
title: "xkbgetindicatormap(3)"
name: "xkbgetindicatormap"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xkbgetindicatormap/"
description: "XkbGetIndicatorMap – Gets the map for one or more indicators, using a mask to specify the indicators"
---

<p>XkbGetIndicatorMap &#8211; Gets the map for one or more indicators, using a mask to specify the indicators </p>
<h2>Synopsis</h2>
<dl COMPACT>
<dt> <code>Status XkbGetIndicatorMap</code> <code>(Display *</code><i>dpy</i><code>,</code> <code>unsigned int </code><i>which</i><code>,</code> <code>XkbDescPtr </code><i>desc</i><code>);</code><br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</dl>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>&#8211; dpy</i></p>
<dd>
<dd>connection to the X server</p>
<dt><i>&#8211; which</i></p>
<dd>mask of indicators for which maps should be returned</p>
<dt><i>&#8211; desc</i></p>
<dd>keyboard description to be updated</dl>
<h2>Description</h2>
<p>Xkb allows applications to obtain information about indicators using two different methods. The first method, which is similar to the core X implementation, uses a mask to specify the indicators. The second method, which is more suitable for applications concerned with interoperability, uses indicator names. The correspondence between the indicator name and the bit position in masks is as follows: one of the parameters returned from <i>XkbGetNamedIndicators </i> is an index that is the bit position to use in any function call that requires a mask of indicator bits, as well as the indicator&#8217;s index into the XkbIndicatorRec array of indicator maps. </p>
<p> <i>XkbGetIndicatorMap </i> obtains the maps from the server for only those indicators specified by the <i>which </i> mask and copies the values into the keyboard description specified by <i>desc. </i> If the <i>indicators </i> field of the <i>desc </i> parameter is NULL, <i>XkbGetIndicatorMap </i> allocates and initializes it. </p>
<p> To free the indicator maps, use <i>XkbFreeIndicatorMaps.</i></p>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt><code>BadAlloc</code></p>
<dd>Unable to allocate storage</p>
<dt><code>BadMatch</code></p>
<dd>A compatible version of Xkb was not available in the server or an argument has correct type and range, but is otherwise invalid</p>
<dt><code>BadImplementation</code></p>
<dd>Invalid reply from server</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xkbfreeindicatormaps/">XkbFreeIndicatorMaps</a></code>(3), <code><a href="/docs/linux/man/3-xkbgetnamedindicators/">XkbGetNamedIndicators</a></code>(3)</p>
