---
title: "waffle_dl_sym(3)"
name: "waffle_dl_sym"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_dl_sym/"
description: "waffle_dl, waffle_dl_can_open, waffle_dl_sym – platform-independent interface to dynamic libraries"
---

<p>waffle_dl, waffle_dl_can_open, waffle_dl_sym &#8211; platform-independent interface to dynamic libraries</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

bool waffle_dl_can_open(int32_t dl);

void *waffle_dl_sym(int32_t dl, const char *symbol);</code></pre>
<h2>Description</h2>
<dd>The waffle_dl functions provide a platform-independent interface for dynamic OpenGL libraries. For each function, the parameter <i>dl</i> must be one of:</p>
<dl>
<dd><code>WAFFLE_DL_OPENGL</code></dl>
<dl>
<dd><code>WAFFLE_DL_OPENGL_ES1</code></dl>
<dl>
<dd><code>WAFFLE_DL_OPENGL_ES2</code></dl>
<dl>
<dd><code>WAFFLE_DL_OPENGL_ES3</code></dl>
<p> For example, on Linux, the <code>WAFFLE_DL_*</code> enums map to libGL.so.1, libGLESv1_CM.so, libGLESv2.so, and libGLESv2.so, respectively. </p>
<p> <code>waffle_dl_can_open()</code></p>
<dl>
<dd>Test if a dynamic library can be opened.</dl>
<p> <code>waffle_dl_sym()</code></p>
<dl>
<dd>Get a <i>symbol</i> from a dynamic library.</dl>
<h2>Return Value</h2>
<p>Functions whose return type is <code>bool</code> return true on success and false on failure. Functions whose return type is a pointer return <code>NULL</code> on failure. Use <code><a href="/docs/linux/man/3-waffle_error_get_info/">waffle_error_get_info</a></code>(3) to get information about any errors.</p>
<h2>Errors</h2>
<p>If waffle fails to find the requested library on the system, then <code>WAFFLE_ERROR_UNSUPPORTED_ON_PLATFORM</code> is emitted. </p>
<p> See <code><a href="/docs/linux/man/3-waffle_error/">waffle_error</a></code>(3) for the complete list of waffle&#8217;s error codes.</p>
<h2>Issues</h2>
<p>Please report bugs or and feature requests to m[blue]<code><a rel="nofollow" href="https://github.com/waffle-gl/waffle/issues">https://github.com/waffle-gl/waffle/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-waffle/">waffle</a></code>(7), <code><a href="/docs/linux/man/3-waffle_get_proc_address/">waffle_get_proc_address</a></code>(3)</p>
<h2>Author</h2>
<p><code>Chad Versace</code> &lt;chad.versace [at] linux.intel.com&gt;</p>
<dl>
<dd>Maintainer</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Intel </p>
<p> This manual page is licensed under the Creative Commons Attribution-ShareAlike 3.0 United States License (CC BY-SA 3.0). To view a copy of this license, visit m[blue]<code><a rel="nofollow" href="http://creativecommons.org.license/by-sa/3.0/us">http://creativecommons.org.license/by-sa/3.0/us</a></code>m[].</p>
