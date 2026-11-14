---
title: "waffle_glx(3)"
name: "waffle_glx"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_glx/"
description: "waffle_glx, waffle_glx_display, waffle_glx_config, waffle_glx_context, waffle_glx_window – Containers for underlying native GLX objects"
---

<p>waffle_glx, waffle_glx_display, waffle_glx_config, waffle_glx_context, waffle_glx_window &#8211; Containers for underlying native GLX objects</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle_glx.h&gt;

struct waffle_glx_display {
    Display *xlib_display;
};

struct waffle_glx_config {
    Display *xlib_display;
    GLXFBConfig glx_fbconfig;
};

struct waffle_glx_context {
    Display *xlib_display;
    GLXContext glx_context;
};

struct waffle_glx_window {
    Display *xlib_display;
    XID xlib_window;
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
