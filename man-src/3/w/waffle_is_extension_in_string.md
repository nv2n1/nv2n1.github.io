---
title: "waffle_is_extension_in_string(3)"
name: "waffle_is_extension_in_string"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_is_extension_in_string/"
description: "waffle_is_extension_in_string – Check if a name appears in an OpenGL-style extension string"
---

<p>waffle_is_extension_in_string &#8211; Check if a name appears in an OpenGL-style extension string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

bool waffle_is_extension_in_string(const char *extension_string, const char *extension_name);</code></pre>
<h2>Description</h2>
<p><code>waffle_is_extension_in_string()</code></p>
<dl>
<dd>
<dd>Check if an extension name appears in an OpenGL-style extension string. </p>
<p> The <i>extension_string</i> must be in the format returned by glGetString(GL_EXTENSIONS). Note that this function is not restricted to the OpenGL extension string; it can also be used on the WGL, GLX and EGL extension strings. </p>
<p> This function can be called before waffle has been successfully initialized with <code><a href="/docs/linux/man/3-waffle_init/">waffle_init</a></code>(3).</dl>
<h2>Errors</h2>
<p>This function sets the error code to <code>WAFFLE_NO_ERROR</code>.</p>
<h2>Issues</h2>
<p>Please report bugs or and feature requests to m[blue]<code><a rel="nofollow" href="https://github.com/waffle-gl/waffle/issues">https://github.com/waffle-gl/waffle/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-waffle/">waffle</a></code>(7)</p>
<h2>Author</h2>
<p><code>Chad Versace</code> &lt;chad.versace [at] linux.intel.com&gt;</p>
<dl>
<dd>Maintainer</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Intel </p>
<p> This manual page is licensed under the Creative Commons Attribution-ShareAlike 3.0 United States License (CC BY-SA 3.0). To view a copy of this license, visit m[blue]<code><a rel="nofollow" href="http://creativecommons.org.license/by-sa/3.0/us">http://creativecommons.org.license/by-sa/3.0/us</a></code>m[].</p>
