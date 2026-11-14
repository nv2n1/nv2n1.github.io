---
title: "waffle_display_supports_context_api(3)"
name: "waffle_display_supports_context_api"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_display_supports_context_api/"
description: "waffle_display, waffle_display_connect, waffle_display_disconnect, waffle_display_supports_context_api, waffle_display_get_native – class waffle_display"
---

<p>waffle_display, waffle_display_connect, waffle_display_disconnect, waffle_display_supports_context_api, waffle_display_get_native &#8211; class waffle_display</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

struct waffle_display;

struct waffle_display *waffle_display_connect(const char *name);

bool waffle_display_disconnect(struct waffle_display *self);

bool waffle_display_supports_context_api(struct waffle_display *self, int32_t context_api);

union waffle_native_display *waffle_display_get_native(struct waffle_display *self);</code></pre>
<h2>Description</h2>
<p><code>struct waffle_display</code></p>
<dl>
<dd>
<dd>An opaque type.</dl>
<p> <code>waffle_display_connect()</code></p>
<dl>
<dd>Connect to a display. The interpretation of <i>name</i> differs according to the platform given to <code><a href="/docs/linux/man/3-waffle_init/">waffle_init</a></code>(3). </p>
<p> On Android, CGL and WGL <i>name</i> is ignored. </p>
<p> On the X11 platforms, GLX and X11/EGL, the function connects to the X11 display with the given <i>name</i>. If <i>name</i> is null, then it uses the value of the environment variable <code>DISPLAY</code>. </p>
<p> On Wayland, the function connects to the Wayland display with the given name. If <i>name</i> is null, then it uses the value of the environment variable <code>WAYLAND_DISPLAY</code>. </p>
<p> On GBM, the function opens the device at the filepath <i>name</i>. If <i>name</i> is null, then it iterates using udev through the set of card devices in the drm subsystem, which are usually located in /dev/dri, and attempts to open each in turn with open(O_RDWR | O_CLOEXEC) until successful.</dl>
<p> <code>waffle_display_disconnect()</code></p>
<dl>
<dd>Disconnect from the <code>waffle_display</code> and release it&#8217;s memory. All pointers to waffle objects that were created with the display become invalid.</dl>
<p> <code>waffle_display_supports_context_api()</code></p>
<dl>
<dd>Check if the display is capable of creating a <code><a href="/docs/linux/man/3-waffle_context/">waffle_context</a></code>(3) with the given <i>context_api</i>. See <code><a href="/docs/linux/man/3-waffle_config/">waffle_config</a></code>(3) for choices of <i>context_api</i> and expectations for each platform.</dl>
<p> <code>waffle_display_get_native()</code></p>
<dl>
<dd>Get the display&#8217;s underlying native objects. Use <code><a href="/docs/linux/man/3-free/">free</a></code>(3) to deallocate the returned pointer. See <code><a href="/docs/linux/man/3-waffle_native/">waffle_native</a></code>(3) for the definition of <code>union waffle_native_display</code>.</dl>
<h2>Return Value</h2>
<p>Functions whose return type is <code>bool</code> return true on success and false on failure. Functions whose return type is a pointer return <code>NULL</code> on failure. Use <code><a href="/docs/linux/man/3-waffle_error_get_info/">waffle_error_get_info</a></code>(3) to get information about any errors.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/3-waffle_error/">waffle_error</a></code>(3) for the complete list of waffle&#8217;s error codes. </p>
<p> No errors are specific to any of the <code>waffle_display</code> functions.</p>
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
