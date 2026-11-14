---
title: "xinerama(3)"
name: "xinerama"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xinerama/"
description: "Xinerama – API for Xinerama extension to X11 Protocol"
---

<p>Xinerama &#8211; API for Xinerama extension to X11 Protocol </p>
<h2>Synopsis</h2>
<p>#include &lt;X11/extensions/Xinerama.h&gt; </p>
<pre>Bool XineramaQueryExtension (Display *<i>dpy</i>,
 int *<i>event_base_return</i>, int *<i>error_base_return</i>);
Status XineramaQueryVersion (Display *<i>dpy</i>,
 int *<i>major_version_return</i>,
 int *<i>minor_version_return</i>);
Bool XineramaIsActive (Display *<i>dpy</i>);
XineramaScreenInfo * XineramaQueryScreens (Display *<i>dpy</i>,
 int *<i>number</i>);</pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>display</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>event_base_return</i></p>
<dd>Specifies the return location for the assigned base event code</p>
<dt><i>error_base_return</i></p>
<dd>Specifies the return location for the assigned base error code</p>
<dt><i>major_version_return</i></p>
<dd>Returns the major version supported by the server</p>
<dt><i>minor_version_return</i></p>
<dd>Returns the minor version supported by the server</p>
<dt><i>number</i></p>
<dd>Returns the number of entries in the returned XineramaScreenInfo array.</dl>
<h2>Description</h2>
<p><code>Xinerama</code> is a simple library designed to interface the Xinerama Extension for retrieving information about physical output devices which may be combined into a single logical X screen. </p>
<h2>Functions</h2>
<h3><code>XineramaQueryExtension()</code></h3>
<p>The XineramaQueryExtension function queries the Xserver to determine the availability of the Xinerama Extension. If the extension is available, the return value is True, and event_base_return and error_base_return are set to the base event number and base error number for the extension, respectively. Otherwise, the return value is False, and the values of event_base_return and error_base_return are undefined. </p>
<h3><code>XineramaQueryVersion()</code></h3>
<p>The XineramaQueryVersion function returns the version of the Xinerama extension implemented by the Xserver. The version is returned in major_version_return and minor_version_return. The major version will be incremented for protocol incompatible changes, and the minor version will be incremented for small, upwardly compatible changes. </p>
<p> If the Xinerama library is compatible with the version returned by the server, it returns nonzero. If the server does not support the XINERAMA extension, or if there was an error during communications with the server, or if the server and library protocol versions are incompatible, it returns zero. </p>
<h3><code>XineramaIsActive()</code></h3>
<p>The XineramaIsActive function returns a Boolean operator used to determine if Xinerama is activated on the screen. Returns True for active and False for not active. </p>
<h3><code>XineramaQueryScreens()</code></h3>
<p>The <code>XineramaQueryScreens()</code> function returns info about each individual output device within the Xinerama Screen. The integer pointed to by the <i>number</i> argument is updated to the number of output devices listed in the returned array of <i>XineramaScreenInfo</i> structures. <code>XineramaQueryScreens()</code> returns NULL and sets <i>number</i> to 0 if Xinerama is not active. </p>
<p> The pointer returned should be released with <a href="/docs/linux/man/3-xfree/">XFree</a>(3) when no longer needed. </p>
<h2>Note</h2>
<p>The original API provided for interacting with the XINERAMA extension used function names beginning with <i>XPanoramiX</i>. That API is now deprecated and this API should be used instead in new software.</p>
