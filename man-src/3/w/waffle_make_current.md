---
title: "waffle_make_current(3)"
name: "waffle_make_current"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_make_current/"
description: "waffle_make_current – Bind a context for rendering"
---

<p>waffle_make_current &#8211; Bind a context for rendering</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

bool waffle_make_current(struct waffle_display *display, struct waffle_window *window, struct waffle_context *context);</code></pre>
<h2>Description</h2>
<p><code>waffle_make_current()</code></p>
<dl>
<dd>
<dd>Bind the given <i>window</i> and <i>context</i> for rendering on the current thread. <i>window</i> and <i>context</i> must both have been created on the given <i>display</i>. To unbind the current context without binding a new one, set <i>window</i> and <i>context</i> to <code>NULL</code>. </p>
<p> This function is analogous to <code><a href="/docs/linux/man/3-glxmakecurrent/">glXMakeCurrent</a></code>(3), <code><a href="/docs/linux/man/3-eglmakecurrent/">eglMakeCurrent</a></code>(3), and <code>[NSOpenGLContext makeCurrentContext]</code>.</dl>
<h2>Return Value</h2>
<p>Functions whose return type is <code>bool</code> return true on success and false on failure. Functions whose return type is a pointer return <code>NULL</code> on failure. Use <code><a href="/docs/linux/man/3-waffle_error_get_info/">waffle_error_get_info</a></code>(3) to get information about any errors.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/3-waffle_error/">waffle_error</a></code>(3) for the complete list of waffle&#8217;s error codes. </p>
<p> No errors are specific to any functions listed in this manual page.</p>
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
