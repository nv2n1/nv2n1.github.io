---
title: "dmxchangescreensattributes(3)"
name: "dmxchangescreensattributes"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxchangescreensattributes/"
description: "DMXChangeScreensAttributes – change back-end screen attributes"
---

<p>DMXChangeScreensAttributes &#8211; change back-end screen attributes</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>int DMXChangeScreensAttributes(Display </code><i>*dpy</i><code>,</code>
<code> int </code><i>screen_count</i><code>,</code>
<code> int </code><i>*screens</i><code>,</code>
<code> int </code><i>mask_count</i><code>,</code>
<code> unsigned int </code><i>*masks</i><code>,</code>
<code> DMXScreenAttributes </code><i>*attr</i><code>,</code>
<code> int *</code><i>error_screen</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXChangeScreensAttributes()</code> changes the geometries and positions of the DMX screen and DMX root windows on the back-end X servers. <i>screen_count</i> specifies the number of screens to be changed. For each screen, the screen number is placed in <i>screens</i>, an attribute mask is placed in <i>masks</i>, and a <i>DMXScreenAttributes</i> structure is included in <i>attr</i>. </p>
<p> An explanation of the <i>DMXScreenAttributes</i> structure is given in <code><a href="/docs/linux/man/3-dmxgetscreenattributes/">DMXGetScreenAttributes</a></code>(3). </p>
<p> The values that are used to compute each value in <i>masks</i> are as follows </p>
<pre>DMXScreenWindowWidth
DMXScreenWindowHeight
DMXScreenWindowXoffset
DMXScreenWindowYoffset
DMXRootWindowWidth
DMXRootWindowHeight
DMXRootWindowXoffset
DMXRootWindowYoffset
DMXRootWindowXorigin
DMXRootWindowYorigin</pre>
<p>In general, <i>mask_count</i> should be equal to <i>screen_count</i>. However, as a convenience, <i>mask_count</i> may be less than <i>screen_count</i>, and the last entry in <i>masks</i> will then be used for all of the remaining screens. For example, this allows identical changes to be made to several screens using only one mask.</p>
<h2>Return Value</h2>
<p>On success, 0 is returned. Otherwise, <i>error_screen</i> is set to the value of the first screen in the list that caused the error and a non-zero value is returned. If <i>screen_count</i> or <i>mask_count</i> is less than 1, or if any of the attribute values are not within the appropriate bounding boxes, <code>DmxBadValue</code> is returned. If a protocol error occurs, <code>DmxBadReply</code> is returned. </p>
<p> <code>DMXChangeScreensAttributes()</code> can generate <code>BadLength</code> (if the data provided does not match the data implicitly required by the <i>screen_count</i> and <i>mask_count</i> values), <code>BadValue</code> (if the values in <i>screens</i> are not valid), and <code>BadAlloc</code> errors.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxgetscreencount/">DMXGetScreenCount</a></code>(3), <code><a href="/docs/linux/man/3-dmxgetscreenattributes/">DMXGetScreenAttributes</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
