---
title: "waffle_init(3)"
name: "waffle_init"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_init/"
description: "waffle_init – Initialize waffle’s per-process global state"
---

<p>waffle_init &#8211; Initialize waffle&#8217;s per-process global state</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

bool waffle_init(const int32_t attrib_list[]);</code></pre>
<h2>Description</h2>
<p><code>waffle_init()</code></p>
<dd>initializes the per-process global state of the waffle library with the attributes specified in <i>attrib_list</i>. The set of attributes is documented below. <i>attrib_list</i> consists of a zero-terminated sequence of name/value pairs. </p>
<p> Most waffle functions emit an error if called when waffle is unitialized. The small set of functions that can be successfully called before initialization are explicitly documented as such. </p>
<p> If a call to <code>waffle_init()</code> fails, no global state is initialized and the caller may safely attempt to call <code>waffle_init()</code> again. If waffle has already been initialized by a successful call to <code>waffle_init()</code>, then calling <code>waffle_init()</code> again emits the error <code>WAFFLE_ERROR_ALREADY_INITIALIZED</code>.</p>
<h2>Attributes</h2>
<p><code>WAFFLE_PLATFORM</code></p>
<dl>
<dd>This attribute is required. Possible values are: <code>WAFFLE_PLATFORM_ANDROID</code></p>
<dl>
<dd>[Android] Use EGL on Android.</dl>
<p> <code>WAFFLE_PLATFORM_GBM</code></p>
<dl>
<dd>[Linux] Use EGL with GBM, the &quot;Generic Buffer Manager&quot; provided by libgbm. This platform is capable of OpenGL rendering without a display manager.</dl>
<p> <code>WAFFLE_PLATFORM_CGL</code></p>
<dl>
<dd>[MacOS] Use CGL to create the <code><a href="/docs/linux/man/3-waffle_config/">waffle_config</a></code>(3) and <code><a href="/docs/linux/man/3-waffle_context/">waffle_context</a></code>(3). Use Cocoa to create the <code><a href="/docs/linux/man/3-waffle_window/">waffle_window</a></code>(3).</dl>
<p> <code>WAFFLE_PLATFORM_GLX</code></p>
<dl>
<dd>[Linux only, MacOS not yet supported]</dl>
<p> <code>WAFFLE_PLATFORM_WAYLAND</code></p>
<dl>
<dd>[Linux] Use EGL with the Wayland display server.</dl>
<p> <code>WAFFLE_PLATFORM_WGL</code></p>
<dl>
<dd>[Windows] Use WGL on Windows.</dl>
<p> <code>WAFFLE_PLATFORM_X11_EGL</code></p>
<dl>
<dd>[Linux] Use EGL with the X11 display server.</dl>
<h2>Return Value</h2>
<p>Functions whose return type is <code>bool</code> return true on success and false on failure. Functions whose return type is a pointer return <code>NULL</code> on failure. Use <code><a href="/docs/linux/man/3-waffle_error_get_info/">waffle_error_get_info</a></code>(3) to get information about any errors.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/3-waffle_error/">waffle_error</a></code>(3) for the complete list of waffle&#8217;s error codes. </p>
<p> Listed are the errors specific to <code>waffle_init()</code>. </p>
<p> <code>WAFFLE_ERROR_ALREADY_INITIALIZED</code></p>
<dl>
<dd>Waffle has already been initialized with a successfull call to <code>waffle_init()</code>.</dl>
<p> <code>WAFFLE_ERROR_BAD_ATTRIBUTE</code></p>
<dl>
<dd>An item in <i>attrib_list</i> is unrecognized or has an invalid value, or a required attribute is missing.</dl>
<p> <code>WAFFLE_ERROR_BUILT_WITHOUT_SUPPORT</code></p>
<dl>
<dd>Waffle was built without support for the requested attribute.</dl>
<h2>Example</h2>
<p>Initialize waffle for X11/EGL. </p>
<pre><code>#include &lt;waffle.h&gt;

static const int32_t init_attrib_list[] = {
    WAFFLE_PLATFORM,
    WAFFLE_PLATFORM_X11_EGL,
    0,
};

int main()
{
    bool ok = waffle_init(init_attrib_list);
    if (ok)
        return EXIT_SUCCESS;
    else
        return EXIT_FAILURE;
}</code></pre>
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
