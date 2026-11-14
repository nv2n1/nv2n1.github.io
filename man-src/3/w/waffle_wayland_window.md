---
title: "waffle_wayland_window(3)"
name: "waffle_wayland_window"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_wayland_window/"
description: "waffle_wayland, waffle_wayland_display, waffle_wayland_config, waffle_wayland_context, waffle_wayland_window – Containers for underlying native Wayland objects"
---

<p>waffle_wayland, waffle_wayland_display, waffle_wayland_config, waffle_wayland_context, waffle_wayland_window &#8211; Containers for underlying native Wayland objects</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle_wayland.h&gt;

struct waffle_wayland_display {
    struct wl_display *wl_display;
    struct wl_compositor *wl_compositor;
    struct wl_shell *wl_shell;
    EGLDisplay egl_display;
};

struct waffle_wayland_config {
    struct waffle_wayland_display display;
    EGLConfig egl_config;
};

struct waffle_wayland_context {
    struct waffle_wayland_display display;
    EGLContext egl_context;
};

struct waffle_wayland_window {
    struct waffle_wayland_display display;
    struct wl_surface *wl_surface;
    struct wl_shell_surface *wl_shell_surface;
    struct wl_egl_window *wl_window;
    EGLSurface egl_surface;
};</code></pre>
<h2>Issues</h2>
<p>Please report bugs or and feature requests to m[blue]<code><a rel="nofollow" href="https://github.com/waffle-gl/waffle/issues">https://github.com/waffle-gl/waffle/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-waffle/">waffle</a></code>(7), <code><a href="/docs/linux/man/3-waffle_native/">waffle_native</a></code>(3)</p>
<h2>Author</h2>
<p><code>Chad Versace</code> &lt;chad.versace [at] linux.intel.com&gt;</p>
<dl>
<dd>Maintainer</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Intel </p>
<p> This manual page is licensed under the Creative Commons Attribution-ShareAlike 3.0 United States License (CC BY-SA 3.0). To view a copy of this license, visit m[blue]<code><a rel="nofollow" href="http://creativecommons.org.license/by-sa/3.0/us">http://creativecommons.org.license/by-sa/3.0/us</a></code>m[].</p>
