---
title: "waffle_window_show(3)"
name: "waffle_window_show"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_window_show/"
description: "waffle_window, waffle_window_create, waffle_window_destroy, waffle_window_show, waffle_window_swap_buffers, waffle_window_get_native – class waffle_window"
---

<p>waffle_window, waffle_window_create, waffle_window_destroy, waffle_window_show, waffle_window_swap_buffers, waffle_window_get_native &#8211; class waffle_window</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

struct waffle_window;

struct waffle_window *waffle_window_create(struct waffle_window *config, int32_t width, int32_t height);

bool waffle_window_destroy(struct waffle_window *self);

bool waffle_window_show(struct waffle_window *self);

bool waffle_window_swap_buffers(struct waffle_window *self);

union waffle_native_window *waffle_window_get_native(struct waffle_window *self);</code></pre>
<h2>Description</h2>
<p><code>struct waffle_window</code></p>
<dl>
<dd>
<dd>An opaque type.</dl>
<p> <code>waffle_window_create()</code></p>
<dl>
<dd>Create a window with the properties specified by <i>config</i>. </p>
<p> If the platform allows, the window is not displayed onto the screen after creation. To display the window, call <code>waffle_window_show()</code>.</dl>
<p> <code>waffle_window_destroy()</code></p>
<dl>
<dd>Destroy the window and release its memory.</dl>
<p> <code>waffle_window_show()</code></p>
<dl>
<dd>Show the window on the display. If the window is already shown, or if the native platform does not support showing windows (such as GBM), then do nothing and returns true.</dl>
<p> <code>waffle_window_swap_buffers()</code></p>
<dl>
<dd>If the window is double-buffered, then implicitly call <code>glFlush()</code> and post the contents of the back buffer to the front buffer. If the window is front-buffered, then do nothing. For platform-specific details of swap semantics, see the specification for the relevant native platform: the m[blue]<code>GLX 1.4 Specification</code>m[]<font SIZE="-2">[1]</font>, the m[blue]<code>EGL 1.4 Specification</code>m[]<font SIZE="-2">[2]</font>, or the m[blue]<code>CGL Reference</code>m[]<font SIZE="-2">[3]</font>.</dl>
<p> <code>waffle_window_get_native()</code></p>
<dl>
<dd>Get the window&#8217;s underlying native objects. Use <code><a href="/docs/linux/man/3-free/">free</a></code>(3) to deallocate the returned pointer. See <code><a href="/docs/linux/man/3-waffle_native/">waffle_native</a></code>(3) for the definition of <code>union waffle_native_window</code>.</dl>
<h2>Return Value</h2>
<p>Functions whose return type is <code>bool</code> return true on success and false on failure. Functions whose return type is a pointer return <code>NULL</code> on failure. Use <code><a href="/docs/linux/man/3-waffle_error_get_info/">waffle_error_get_info</a></code>(3) to get information about any errors.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/3-waffle_error/">waffle_error</a></code>(3) for the complete list of waffle&#8217;s error codes. </p>
<p> No errors are specific to the <code>waffle_window</code> functions.</p>
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
<dd>CGL Reference</p>
<dl>
<dd><a rel="nofollow" href="https://developer.apple.com/library/mac/#documentation/graphicsimaging/reference/CGL_OpenGL/Reference/reference.html">https://developer.apple.com/library/mac/#documentation/graphicsimaging/reference/CGL_OpenGL/Reference/reference.html</a></dl>
