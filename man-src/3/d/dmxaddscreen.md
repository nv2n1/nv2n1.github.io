---
title: "dmxaddscreen(3)"
name: "dmxaddscreen"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dmxaddscreen/"
description: "DMXAddScreen – attach a new back-end screen"
---

<p>DMXAddScreen &#8211; attach a new back-end screen</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/X11/extensions/dmxext.h">X11/extensions/dmxext.h</a>&gt;</code> </p>
<pre><code>Bool DMXAddScreen(Display </code><i>*dpy</i><code>,</code>
<code> const char </code><i>*displayName</i><code>,</code>
<code> unsigned int </code><i>mask</i><code>,</code>
<code> DMXScreenAttributes </code><i>*attr</i><code>,</code>
<code> int </code><i>*screen</i><code>);</code></pre>
<h2>Description</h2>
<p><code>DMXAddScreen()</code> attaches a back-end screen to the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) server, in place of the previously detached back-end server specified by <i>screen</i>. </p>
<p> <i>displayName</i> is the name of the new back-end display, <i>mask</i> specifies the field in <i>attr</i> that are active, and <i>screen</i> returns the new <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) screen number for the attached screen. </p>
<p> The information stored in <i>mask and attr</i> is identical to that used by the <code><a href="/docs/linux/man/3-dmxchangescreenattributes/">DMXChangeScreenAttributes</a></code>(3) and <code><a href="/docs/linux/man/3-dmxgetscreenattribues/">DMXGetScreenAttribues</a></code>(3) functions.</p>
<h2>Return Value</h2>
<p><code>DMXAddScreen()</code> will return <code>True</code> if the screen was successfully attached, and <code>False</code> otherwise. <code>False</code> will be returned if the <i>-addremovescreens</i> command line option was not specified on the <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1) command line, the input value of <i>screen</i> is out of range, <i>screen</i> is not currently detached, <i>displayName</i> cannot be opened, has unexpected visuals, or has characteristics that do not match the previously detached screen. </p>
<p> <code>DMXAddScreen()</code> can generate <code>BadLength</code>, <code>BadAlloc</code>, and <code>BadValue</code> errors.</p>
<h2>Notes</h2>
<p>Attributes that are not specified will default to 0. This may lead to unintended results. </p>
<p> Unlike other functions in the <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3) API, this function uses <i>screen</i> for both input and output.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-dmxremovescreen/">DMXRemoveScreen</a></code>(3), <code><a href="/docs/linux/man/3-dmxchangescreenattributes/">DMXChangeScreenAttributes</a></code>(3), <code><a href="/docs/linux/man/3-dmxgetscreenattributes/">DMXGetScreenAttributes</a></code>(3), <code><a href="/docs/linux/man/3-dmx/">DMX</a></code>(3), <code><a href="/docs/linux/man/1-xdmx/">Xdmx</a></code>(1)</p>
