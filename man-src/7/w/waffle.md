---
title: "waffle(7)"
name: "waffle"
section: "7"
letter: "w"
url: "/docs/linux/man/7-waffle/"
description: "waffle – a library for selecting an OpenGL API and window system at runtime"
---

<p>waffle &#8211; a library for selecting an OpenGL API and window system at runtime</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

Link with -lwaffle-1.</code></pre>
<h2>Description</h2>
<p>Waffle is a cross-platform library that allows one to defer selection of an OpenGL API and of window system until runtime. For example, on Linux, Waffle enables an application to select X11/EGL with an OpenGL 3.3 core profile, Wayland with OpenGL ES2, and other window system / API combinations. </p>
<p> Waffle&#8217;s immediate goal is to enable m[blue]<code>Piglit</code>m[]<font SIZE="-2">[1]</font>, m[blue]<code>Mesa</code>m[]<font SIZE="-2">[2]</font>&#8216;s OpenGL test suite, to test multiple OpenGL flavors in a cross-platform way, and to allow each Piglit test to choose its OpenGL API and window system at runtime. A future goal is to enable the ability to record, with another tool such as m[blue]<code>APITrace</code>m[]<font SIZE="-2">[3]</font>, an application&#8217;s OpenGL calls on one operating system or window system, and then replay that trace on a different system. </p>
<p> m[blue]<code>waffle</code>m[]<font SIZE="-2">[4]</font>&#8216;s website.</p>
<h2>Examples</h2>
<p>Your distribution should have installed example source code that demonstrates how to use waffle at /usr/share/doc/waffle-${version}/examples. You can also find m[blue]<code>examples</code>m[]<font SIZE="-2">[5]</font> in Waffle&#8217;s source repository.</p>
<h2>Issues</h2>
<p>Please report bugs or and feature requests to m[blue]<code><a rel="nofollow" href="https://github.com/waffle-gl/waffle/issues">https://github.com/waffle-gl/waffle/issues</a></code>m[].</p>
<h2>See Also</h2>
<dl>
<dd>Website: <a rel="nofollow" href="http://www.waffle-gl.org">http://www.waffle-gl.org</a></dl>
<dl>
<dd>Source: <a href="git://github.com/waffle-gl/waffle">git://github.com/waffle-gl/waffle</a></dl>
<dl>
<dd><code><a href="/docs/linux/man/7-waffle_feature_test_macros/">waffle_feature_test_macros</a></code>(7)</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_attrib_list/">waffle_attrib_list</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_config/">waffle_config</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_context/">waffle_context</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_display/">waffle_display</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_dl/">waffle_dl</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_enum/">waffle_enum</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_error/">waffle_error</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_gbm/">waffle_gbm</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_get_proc_address/">waffle_get_proc_address</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_glx/">waffle_glx</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_init/">waffle_init</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_is_extension_in_string/">waffle_is_extension_in_string</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_make_current/">waffle_make_current</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_native/">waffle_native</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_wayland/">waffle_wayland</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_window/">waffle_window</a></code>(3),</dl>
<dl>
<dd><code><a href="/docs/linux/man/3-waffle_x11_egl/">waffle_x11_egl</a></code>(3)</dl>
<dl>
<dd><code><a href="/docs/linux/man/1-wflinfo/">wflinfo</a></code>(1),</dl>
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
<dd>Piglit</p>
<dl>
<dd><a rel="nofollow" href="http://piglit.freedesktop.org">http://piglit.freedesktop.org</a></dl>
<dt> 2.</p>
<dd>Mesa</p>
<dl>
<dd><a rel="nofollow" href="http://mesa3d.org">http://mesa3d.org</a></dl>
<dt> 3.</p>
<dd>APITrace</p>
<dl>
<dd><a rel="nofollow" href="http://github.com/apitrace/apitrace#readme">http://github.com/apitrace/apitrace#readme</a></dl>
<dt> 4.</p>
<dd>waffle</p>
<dl>
<dd><a rel="nofollow" href="http://www.waffle-gl.org">http://www.waffle-gl.org</a></dl>
<dt> 5.</p>
<dd>examples</p>
<dl>
<dd><a rel="nofollow" href="https://github.com/waffle-gl/waffle/tree/master/examples">https://github.com/waffle-gl/waffle/tree/master/examples</a></dl>
