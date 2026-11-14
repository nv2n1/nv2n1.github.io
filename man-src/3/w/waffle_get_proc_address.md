---
title: "waffle_get_proc_address(3)"
name: "waffle_get_proc_address"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_get_proc_address/"
description: "waffle_get_proc_address – Query address of OpenGL functions"
---

<p>waffle_get_proc_address &#8211; Query address of OpenGL functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

void *waffle_get_proc_address(const char *name);</code></pre>
<h2>Description</h2>
<p><code>waffle_get_proc_address()</code></p>
<dl>
<dd>
<dd>On GLX, this redirects to <code><a href="/docs/linux/man/3-glxgetprocaddress/">glXGetProcAddress</a></code>(3). On EGL, this redirects to <code><a href="/docs/linux/man/3-eglgetprocaddress/">eglGetProcAddress</a></code>(3). On CGL, this function returns <code>NULL</code> because there exists no <code>CGLGetProcAdress()</code>. On WGL, this redirects to <code><a href="/docs/linux/man/3-wglgetprocaddress/">wglGetProcAddress</a></code>(3). </p>
<p> Some aspects of this function&#8217;s behavior are platform-specific and non-intuitive. For example, </p>
<dl>
<dd>&bull; If the queried function is not available, <code>waffle_get_proc_address()</code> may return a non-null pointer.</dl>
<dl>
<dd>&bull; If the queried function is statically exposed by the OpenGL library of a given API, then <code>waffle_get_proc_address()</code> may return a <code>NULL</code>.</dl>
<dl>
<dd>&bull; Under Windows (WGL) a current context must be available before executing the function. Otherwise <code>waffle_get_proc_address()</code> may return a <code>NULL</code>.</dl>
<p> For details on this function&#8217;s behavior, see the specification for the relevant platform: the m[blue]<code>GLX 1.4 Specification</code>m[]<font SIZE="-2">[1]</font> the m[blue]<code>EGL 1.4 Specification</code>m[]<font SIZE="-2">[2]</font> or the m[blue]<code>MSDN article</code>m[]<font SIZE="-2">[3]</font>.</dl>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/3-waffle_error/">waffle_error</a></code>(3) for the complete list of waffle&#8217;s error codes. </p>
<p> No errors are specific to any functions listed in this manual page.</p>
<h2>Issues</h2>
<p>Please report bugs or and feature requests to m[blue]<code><a rel="nofollow" href="https://github.com/waffle-gl/waffle/issues">https://github.com/waffle-gl/waffle/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-waffle/">waffle</a></code>(7), <code><a href="/docs/linux/man/3-waffle_dl_sym/">waffle_dl_sym</a></code>(3)</p>
<h2>Author</h2>
<p><code>Chad Versace</code> &lt;chad.versace [at] linux.intel.com&gt;</p>
<dl>
<dd>Maintainer</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Intel </p>
<p> This manual page is licensed under the Creative Commons Attribution-ShareAlike 3.0 United States License (CC BY-SA 3.0). To view a copy of this license, visit m[blue]<code><a rel="nofollow" href="http://creativecommons.org.license/by-sa/3.0/us">http://creativecommons.org.license/by-sa/3.0/us</a></code>m[].</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>GLX 1.4 Specification</p>
<dl>
<dd><a rel="nofollow" href="http://www.opengl.org/registry/doc/glx1.4.pdf">http://www.opengl.org/registry/doc/glx1.4.pdf</a></dl>
<dt> 2.</p>
<dd>EGL 1.4 Specification</p>
<dl>
<dd><a rel="nofollow" href="http://www.khronos.org/registry/egl/specs/eglspec.1.4.20110406.pdf">http://www.khronos.org/registry/egl/specs/eglspec.1.4.20110406.pdf</a></dl>
<dt> 3.</p>
<dd>MSDN article</p>
<dl>
<dd><a rel="nofollow" href="http://msdn.microsoft.com/en-gb/library/windows/desktop/dd374386(v=vs.85).aspx">http://msdn.microsoft.com/en-gb/library/windows/desktop/dd374386(v=vs.85).aspx</a></dl>
