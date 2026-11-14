---
title: "xvqueryextension(3)"
name: "xvqueryextension"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xvqueryextension/"
description: "XvQueryExtension – return version and release of extension"
---

<p>XvQueryExtension &#8211; return version and release of extension</p>
<h2>Synopsis</h2>
<p><code>#include &lt;X11/extensions/Xvlib.h&gt;</code> </p>
<pre><code>int XvQueryExtension(Display *</code><i>dpy</i><code>, unsigned int *</code><i>p_version</i><code>,</code>
<code> unsigned int *</code><i>p_revision</i><code>,</code>
<code> unsigned int *</code><i>p_request_base</i><code>,</code>
<code> unsigned int *</code><i>p_event_base</i><code>,</code>
<code> unsigned int *</code><i>p_error_base</i><code>);</code></pre>
<h2>Arguments</h2>
<dl COMPACT>
<dt><i>dpy</i></p>
<dd>Specifies the connection to the X server.</p>
<dt><i>p_version</i></p>
<dd>Pointer to where the current version number of the <i>Xv</i> video extension is written.</p>
<dt><i>p_revision</i></p>
<dd>Pointer to where the revision number of the <i>Xv</i> video extension is written.</p>
<dt><i>p_request_base</i></p>
<dd>Pointer to where the extension major request number is returned</p>
<dt><i>p_event_base</i></p>
<dd>Pointer to where the extension event base is returned</p>
<dt><i>p_error_base</i></p>
<dd>Pointer to where the extension error base is returned</dl>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/3-xvqueryextension/">XvQueryExtension</a></code>(3) returns the version and release numbers for the Xv video extension currently loaded on the system. The extension major request number, event base, and error base are also returned.</p>
<h2>Return Values</h2>
<dl COMPACT>
<dt>[Success]</p>
<dd>Returned if <code><a href="/docs/linux/man/3-xvqueryextension/">XvQueryExtension</a></code>(3) completed successfully.</p>
<dt>[XvBadExtension]</p>
<dd>Returned if the Xv video extension is not available for the named display.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-xv/">Xv</a></code>(3)</p>
