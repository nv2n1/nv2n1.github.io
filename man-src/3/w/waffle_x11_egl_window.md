---
title: "waffle_x11_egl_window(3)"
name: "waffle_x11_egl_window"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_x11_egl_window/"
description: "waffle_x11_egl, waffle_x11_egl_display, waffle_x11_egl_config, waffle_x11_egl_context, waffle_x11_egl_window – Containers for underlying native X11/EGL objects"
---

<p>waffle_x11_egl, waffle_x11_egl_display, waffle_x11_egl_config, waffle_x11_egl_context, waffle_x11_egl_window &#8211; Containers for underlying native X11/EGL objects</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle_x11_egl.h&gt;

struct waffle_x11_egl_display {
    Display *xlib_display;
    EGLDisplay egl_display;
};

struct waffle_x11_egl_config {
    struct waffle_x11_egl_display display;
    EGLConfig egl_config;
};

struct waffle_x11_egl_context {
    struct waffle_x11_egl_display display;
    EGLContext egl_context;
};

struct waffle_x11_egl_window {
    struct waffle_x11_egl_display display;
    XID xlib_window;
    EGLSurface egl_surface;
};</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-waffle/">waffle</a></code>(7), <code><a href="/docs/linux/man/3-waffle_native/">waffle_native</a></code>(3)</p>
<h2>Author</h2>
<p><code>Chad Versace</code> &lt;chad.versace [at] linux.intel.com&gt;</p>
<dl>
<dd>Maintainer</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Intel </p>
<p> This manual page is licensed under the Creative Commons Attribution-ShareAlike 3.0 United States License (CC BY-SA 3.0). To view a copy of this license, visit m[blue]<code><a rel="nofollow" href="http://creativecommons.org.license/by-sa/3.0/us">http://creativecommons.org.license/by-sa/3.0/us</a></code>m[].</p>
