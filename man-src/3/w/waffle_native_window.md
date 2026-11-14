---
title: "waffle_native_window(3)"
name: "waffle_native_window"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_native_window/"
description: "waffle_native, waffle_native_display, waffle_native_config, waffle_native_context, waffle_native_window – Containers for underlying native objects"
---

<p>waffle_native, waffle_native_display, waffle_native_config, waffle_native_context, waffle_native_window &#8211; Containers for underlying native objects</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

union waffle_native_display {
    struct waffle_gbm_display *gbm;
    struct waffle_glx_display *glx;
    struct waffle_wayland_display *wayland;
    struct waffle_x11_egl_display *x11_egl;
};

union waffle_native_config {
    struct waffle_gbm_config *gbm;
    struct waffle_glx_config *glx;
    struct waffle_wayland_config *wayland;
    struct waffle_x11_egl_config *x11_egl;
};

union waffle_native_context {
    struct waffle_gbm_context *gbm;
    struct waffle_glx_context *glx;
    struct waffle_wayland_context *wayland;
    struct waffle_x11_egl_context *x11_egl;
};

union waffle_native_window {
    struct waffle_gbm_window *gbm;
    struct waffle_glx_window *glx;
    struct waffle_wayland_window *wayland;
    struct waffle_x11_egl_window *x11_egl;
};</code></pre>
<h2>Description</h2>
<p>Each of the <code>waffle_${obj}_get_native()</code> functions returns a correspondingly named <code>union waffle_native_${obj}*</code>. For example, <code>waffle_window_get_native()</code> returns <code>union waffle_native_window*</code> </p>
<p> For each platform, the header &lt;waffle_${platform}.h&gt; defines the native container structs. For example, &lt;waffle_glx.h&gt; defines the structs <code>waffle_glx_${obj}</code>. </p>
<p> Observerve that native container structs are not defined for all platforms that waffle supports. In particular, waffle supports Android (<code>WAFFLE_PLATFORM_ANDROID</code>) and MacOS via CGL (<code>WAFFLE_PLATFORM_CGL</code>), but no container structs are defined for those platforms. Presently, waffle does not expose the native objects for those platforms due to implementation difficulties.</p>
<h2>Issues</h2>
<p>Please report bugs or and feature requests to m[blue]<code><a rel="nofollow" href="https://github.com/waffle-gl/waffle/issues">https://github.com/waffle-gl/waffle/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-waffle/">waffle</a></code>(7), <code><a href="/docs/linux/man/3-waffle_gbm/">waffle_gbm</a></code>(3), <code><a href="/docs/linux/man/3-waffle_glx/">waffle_glx</a></code>(3), <code><a href="/docs/linux/man/3-waffle_wayland/">waffle_wayland</a></code>(3), <code><a href="/docs/linux/man/3-waffle_x11_egl/">waffle_x11_egl</a></code>(3)</p>
<h2>Author</h2>
<p><code>Chad Versace</code> &lt;chad.versace [at] linux.intel.com&gt;</p>
<dl>
<dd>Maintainer</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Intel </p>
<p> This manual page is licensed under the Creative Commons Attribution-ShareAlike 3.0 United States License (CC BY-SA 3.0). To view a copy of this license, visit m[blue]<code><a rel="nofollow" href="http://creativecommons.org.license/by-sa/3.0/us">http://creativecommons.org.license/by-sa/3.0/us</a></code>m[].</p>
