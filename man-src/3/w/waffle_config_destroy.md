---
title: "waffle_config_destroy(3)"
name: "waffle_config_destroy"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_config_destroy/"
description: "waffle_config, waffle_config_choose, waffle_config_destroy, waffle_config_get_native – class waffle_config"
---

<p>waffle_config, waffle_config_choose, waffle_config_destroy, waffle_config_get_native &#8211; class waffle_config</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

struct waffle_config;

struct waffle_config *waffle_config_choose(struct waffle_display *display, const int32_t attrib_list[]);

bool waffle_config_destroy(struct waffle_config *self);

union waffle_native_config *waffle_config_get_native(struct waffle_config *self);</code></pre>
<h2>Description</h2>
<p><code>struct waffle_config</code></p>
<dl>
<dd>
<dd>An opaque type.</dl>
<p> <code>waffle_config_choose()</code></p>
<dl>
<dd>Choose a config on <i>display</i> that satifisfies the set of attributes specified by <i>attrib_list</i>. The config can later be used to create surfaces and contexts with <code><a href="/docs/linux/man/3-waffle_window_create/">waffle_window_create</a></code>(3) and <code><a href="/docs/linux/man/3-waffle_context_create/">waffle_context_create</a></code>(3). <i>attrib_list</i> consists of a zero-terminated sequence of name/value pairs. If an attribute is absent from <i>attrib_list</i>, then it assumes its default value. If <i>attrib_list</i> is null, then it is intrepreted the same as the empty list, which is the list that contains only the terminal zero. See the section called &#8220;ATTRIBUTES&#8221; below for details on the set of attributes that may appear in <i>attrib_list</i>.  <code>waffle_config_destroy()</code></p>
<dl>
<dd>Destroy the config and release its memory.</dl>
<p> <code>waffle_config_get_native()</code></p>
<dl>
<dd>Get the config&#8217;s underlying native objects. Use <code><a href="/docs/linux/man/3-free/">free</a></code>(3) to deallocate the returned pointer. See <code><a href="/docs/linux/man/3-waffle_native/">waffle_native</a></code>(3) for the definition of <code>union waffle_native_config</code>.</dl>
<h2>Discussion</h2>
<p>The context attributes (<code>WAFFLE_CONTEXT_*</code>) have quirks that are specific to the native platform. Waffle attempts to accomdate those quirks in a platform-neutral way as much as possible, but not all quirks can be eliminated through a platform abstraction layer. The quirks are documented below in detail. </p>
<p> For example, one quirk that Waffle is able to accommodate is that some platforms require specification of context attributes at different times. GLX requires that the context attributes be specified at time of context creation [<code><a href="/docs/linux/man/3-glxcreatecontextattribsarb/">glXCreateContextAttribsARB</a></code>(3)] but MacOS requires the attributes to be specified when choosing a config [<code>CGLChoosePixelFormat</code>]. Therefore, Waffle is constrained by MacOS to require the attributes at time of <code>waffle_config_choose()</code>. </p>
<p> For additional documentation on the behavior of context attributes on each platform, refer to the following:</p>
<dl>
<dd>For GLX, refer to the m[blue]<code>GLX 1.4 Specification</code>m[]<font SIZE="-2">[1]</font> and the specifications for extensions m[blue]<code>GLX_ARB_create_context_profile</code>m[]<font SIZE="-2">[2]</font> and m[blue]<code>GLX_EXT_create_context_es2_profile</code>m[]<font SIZE="-2">[3]</font>.</dl>
<dl>
<dd>For EGL, refer to the m[blue]<code>EGL 1.4 Specification</code>m[]<font SIZE="-2">[4]</font> and the specifications for extension m[blue]<code>EGL_KHR_create_context</code>m[]<font SIZE="-2">[5]</font>.</dl>
<dl>
<dd>For CGL, refer to the documentation of <code>kCGLPFAOpenGLProfile</code> in the m[blue]<code>CGL Reference</code>m[]<font SIZE="-2">[6]</font>.</dl>
<h2>Attributes</h2>
<p><code>WAFFLE_CONTEXT_API</code></p>
<dl>
<dd>This is a required attribute; it has no default value. It must be one of:</p>
<dl>
<dd><code>WAFFLE_CONTEXT_OPENGL</code></dl>
<dl>
<dd><code>WAFFLE_CONTEXT_OPENGL_ES1</code></dl>
<dl>
<dd><code>WAFFLE_CONTEXT_OPENGL_ES2</code></dl>
<dl>
<dd><code>WAFFLE_CONTEXT_OPENGL_ES3</code></dl>
<p> The actual set of supported values depends on the native platform. To check if the system supports a given API, use <code><a href="/docs/linux/man/3-waffle_display_supports_context_api/">waffle_display_supports_context_api</a></code>(3). Invariants and expectations for each platform are discussed below. </p>
<p> On Android, <code>WAFFLE_CONTEXT_OPENGL_ES1</code> is always supported. Beginning with Ice Cream Sandwich (that is, Android 4.0), <code>WAFFLE_CONTEXT_OPENGL_ES2</code> is also supported. Use <code><a href="/docs/linux/man/3-waffle_display_supports_context_api/">waffle_display_supports_context_api</a></code>(3) to check if additional APIs are supported. </p>
<p> On GLX, <code>WAFFLE_CONTEXT_OPENGL</code> is always supported. The system may optionally support additional APIs. </p>
<p> On EGL platforms other than Android, no API is guaranteed to be supported. One must use <code><a href="/docs/linux/man/3-waffle_display_supports_context_api/">waffle_display_supports_context_api</a></code>(3) to check for supported APIs. </p>
<p> On MacOS, only <code>WAFFLE_CONTEXT_OPENGL</code> is supported. This may change in the future if Apple adds support for additional APIs.</dl>
<p> <code>WAFFLE_CONTEXT_MAJOR_VERSION</code><br />
 <code>WAFFLE_CONTEXT_MINOR_VERSION</code></p>
<dl>
<dd>This pair of attributes is optional. They specify the context version that <code><a href="/docs/linux/man/3-waffle_context_create/">waffle_context_create</a></code>(3) will request. </p>
<p> The pair&#8217;s default value and set of accepted values depend on the value of <code>WAFFLE_CONTEXT_API</code> and the native platform. Below is described in detail the rules by which waffle filters the set of accepted values according to the value of <code>WAFFLE_CONTEXT_API</code>. Even if <code>waffle_config_choose()</code> accepts the requested version and successfully returns a config, the native platform may later reject the requested version when <code><a href="/docs/linux/man/3-waffle_context_create/">waffle_context_create</a></code>(3) is called. </p>
<p> If the requested API is <code>WAFFLE_CONTEXT_OPENGL_ES1</code>, then the default value is 1.0. The only accepted values are 1.0 and 1.1. </p>
<p> If the requested API is <code>WAFFLE_CONTEXT_OPENGL_ES2</code>, then the default value is 2.0. Waffle accepts any value that is at least 2.0 and strictly less than 3.0. </p>
<p> If the requested API is <code>WAFFLE_CONTEXT_OPENGL_ES3</code>, then the default value is 3.0. Waffle accepts any value that is at least 3.0 and strictly less than 4.0. </p>
<p> If the requested API is <code>WAFFLE_CONTEXT_OPENGL</code>, then the default and minimum accepted value is 1.0.</dl>
<p> <code>WAFFLE_CONTEXT_PROFILE</code></p>
<dl>
<dd>This attributes is optional. It specifies the context profile that <code><a href="/docs/linux/man/3-waffle_context_create/">waffle_context_create</a></code>(3) will request. </p>
<p> The attribute&#8217;s default value and set of accepted values depend on the values of <code>WAFFLE_CONTEXT_API</code>, <code>WAFFLE_CONTEXT_MAJOR_VERSION</code>, <code>WAFFLE_CONTEXT_MINOR_VERSION</code>, and the native platform. Below is described in detail the rules by which waffle decides the default value and the set of accepted values. Even if <code>waffle_config_choose()</code> accepts the requested profile and successfully returns a config, the native platform may later reject the requested profile when <code><a href="/docs/linux/man/3-waffle_context_create/">waffle_context_create</a></code>(3) is called. </p>
<p> If the requested API is <code>WAFFLE_CONTEXT_OPENGL_ES1</code>, <code>WAFFLE_CONTEXT_OPENGL_ES2</code>, or <code>WAFFLE_CONTEXT_OPENGL_ES3</code>, then the default and only accepted value is <code>WAFFLE_NONE</code>. </p>
<p> If the requested API is <code>WAFFLE_CONTEXT_OPENGL</code> and the requested version is less than 3.2, then the default and only accepted value is <code>WAFFLE_NONE</code>. </p>
<p> If the requested API is <code>WAFFLE_CONTEXT_OPENGL</code> and the requested version is at least 3.2, then default value is <code>WAFFLE_CONTEXT_CORE_PROFILE</code>. The set of accepted values is <code>WAFFLE_CONTEXT_PROFILE_CORE</code> and <code>WAFFLE_CONTEXT_PROFILE_COMPATIBILITY</code>.</dl>
<p> <code>WAFFLE_CONTEXT_FORWARD_COMPATIBLE</code></p>
<dl>
<dd>Feature test macro: WAFFLE_API_VERSION &gt;= 0x0103. (See <code><a href="/docs/linux/man/7-waffle_feature_test_macros/">waffle_feature_test_macros</a></code>(7)). </p>
<p> This attribute, if true, instructs <code><a href="/docs/linux/man/3-waffle_context_create/">waffle_context_create</a></code>(3) to create a forward-compatible context. However, even if <code>waffle_config_choose()</code> successfully returns a config for a forward-compatible context, the native platform may later reject it when <code><a href="/docs/linux/man/3-waffle_context_create/">waffle_context_create</a></code>(3) is called. </p>
<p> Forward-compatible contexts do not support functionality marked as deprecated by that version of the API. A non-forward-compatible context supports all functionality in that version, deprecated or not. </p>
<p> This attribute is optional and its default value is false(0). Valid values are <a href="/docs/linux/man/1-true/">true</a>(1), false(0), and <code>WAFFLE_DONT_CARE</code>. However, <a href="/docs/linux/man/1-true/">true</a>(1) is valid only if the requested context API is <code>WAFFLE_CONTEXT_OPENGL</code> and its version is at least 3.0.</dl>
<p> <code>WAFFLE_CONTEXT_DEBUG</code></p>
<dl>
<dd>Feature test macro: WAFFLE_API_VERSION &gt;= 0x0103. (See <code><a href="/docs/linux/man/7-waffle_feature_test_macros/">waffle_feature_test_macros</a></code>(7)). </p>
<p> This attribute, if true, instructs <code><a href="/docs/linux/man/3-waffle_context_create/">waffle_context_create</a></code>(3) to create a debug context. However, even if <code>waffle_config_choose()</code> successfully returns a config for a debug context, the native platform may later reject it when <code><a href="/docs/linux/man/3-waffle_context_create/">waffle_context_create</a></code>(3) is called. </p>
<p> Debug contexts are intended for use during application development, to provide additional runtime checking, validation, and logging functionality while possibly incurring performance penalties. The additional functionality provided by debug contexts may vary according to the implementation. In some cases a debug context may be identical to a non-debug context. </p>
<p> This attribute is optional and its default value is false(0). Valid values are <a href="/docs/linux/man/1-true/">true</a>(1), false(0), and <code>WAFFLE_DONT_CARE</code>.</dl>
<p> <code>WAFFLE_RED_SIZE</code><br />
 <code>WAFFLE_GREEN_SIZE</code><br />
 <code>WAFFLE_BLUE_SIZE</code><br />
 <code>WAFFLE_ALPHA_SIZE</code><br />
 <code>WAFFLE_DEPTH_SIZE</code><br />
 <code>WAFFLE_STENCIL_SIZE</code></p>
<dl>
<dd>The default value for each size attribute is <code>0</code>. Valid values are the non-negative integers and <code>WAFFLE_DONT_CARE</code>. If the requested size for a channel is 0, then any surface created with the config will lack that channel. If the requested size for a channel is positive, then the number of bits in that channel for any surface created with the config will be at least the requested size.</dl>
<p> <code>WAFFLE_SAMPLE_BUFFERS</code><br />
 <code>WAFFLE_SAMPLES</code></p>
<dl>
<dd>The default value of <code>WAFFLE_SAMPLE_BUFFERS</code> is false(0). Valid values are <a href="/docs/linux/man/1-true/">true</a>(1), false(0), and <code>WAFFLE_DONT_CARE</code>. The attribute specifies if a surface created with this config is double-buffered. If false, then any surface created with the config will not be multisampled. If true, the any surface created with the config will be multisampled, where the number of samples will be at least <code>WAFFLE_SAMPLES</code>. </p>
<p> The default value of <code>WAFFLE_SAMPLES</code> is <code>0</code>. Valid values are the non-negative integers and <code>WAFFLE_DONT_CARE</code>.</dl>
<p> <code>WAFFLE_DOUBLE_BUFFERED</code></p>
<dl>
<dd>The default value is <a href="/docs/linux/man/1-true/">true</a>(1). Valid values are <a href="/docs/linux/man/1-true/">true</a>(1), false(0), and <code>WAFFLE_DONT_CARE</code>. This attribute specifies if a surface created with this config is double-buffered.</dl>
<p> <code>WAFFLE_ACCUM_BUFFER</code></p>
<dl>
<dd>The default value is false(0). Valid values are <a href="/docs/linux/man/1-true/">true</a>(1), false(0), and <code>WAFFLE_DONT_CARE</code>. This attribute specifies if a surface created with this config possesses an accumulation buffer.</dl>
<h2>Return Value</h2>
<p>Functions whose return type is <code>bool</code> return true on success and false on failure. Functions whose return type is a pointer return <code>NULL</code> on failure. Use <code><a href="/docs/linux/man/3-waffle_error_get_info/">waffle_error_get_info</a></code>(3) to get information about any errors.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/3-waffle_error/">waffle_error</a></code>(3) for the complete list of waffle&#8217;s error codes. Listed below are the errors specific to the <code>waffle_config</code> functions. <code>waffle_config_choose()</code></p>
<dl>
<dd><code>WAFFLE_ERROR_BAD_ATTRIBUTE</code></p>
<dl>
<dd>An item in <i>attrib_list</i> is unrecognized or has an invalid value, or a required attribute is missing.</dl>
<p> <code>WAFFLE_ERROR_UNSUPPORTED_ON_PLATFORM</code></p>
<dl>
<dd>If the native platform does not expose the necessary functionality to create a context with the properties specified by config or if waffle can predetermine that the native platform will reject the config at context creation, but otherwise the requested attributes are valid, then <code>WAFFLE_ERROR_UNSUPPORTED_ON_PLATFORM</code> is emitted. For example,</p>
<dl>
<dd>&bull; GLX supports creation of an OpenGL ES2 context only if libGLESv2.so is installed and if GLX_EXT_create_context_es2_profile is exposed as both a server and client extension.</dl>
<dl>
<dd>&bull; MacOS does not support the OpenGL 3.2 Compatibility Profile, and it supports the OpenGL 3.2 Core Profile only for MacOS &gt;= 10.7 on select GPU&#8217;s.</dl>
<h2>Examples</h2>
<h3>Example 1</h3>
<p>Choose a config for an OpenGL legacy context that has at least 8 bits in each of the RGBA channels. #include &lt;stdlib.h&gt;<br />
#include &lt;waffle.h&gt;</p>
<p>static const int32_t init_attrib_list[] = {<br />
    WAFFLE_PLATFORM,<br />
    WAFFLE_PLATFORM_GLX,<br />
    0,<br />
};</p>
<p>static const int32_t config_attrib_list[] = {<br />
    WAFFLE_CONTEXT_API,<br />
    WAFFLE_CONTEXT_OPENGL,</p>
<p>    WAFFLE_RED_SIZE,<br />
    8,<br />
    WAFFLE_GREEN_SIZE,<br />
    8,<br />
    WAFFLE_BLUE_SIZE,<br />
    8,<br />
    WAFFLE_ALPHA_SIZE,<br />
    8,</p>
<p>    0,<br />
};</p>
<p>int main()<br />
{<br />
    struct waffle_display *display;<br />
    struct waffle_config *config;<br />
    bool ok;</p>
<p>    ok = waffle_init(init_attrib_list);<br />
    if (!ok)<br />
        exit(EXIT_FAILURE);</p>
<p>    display = waffle_display_connect(NULL);<br />
    if (!display)<br />
        exit(EXIT_FAILURE);</p>
<p>    config = waffle_config_choose(config_attrib_list);<br />
    if (!config)<br />
        exit(EXIT_FAILURE);</p>
<p>    // Now clean up.<br />
    waffle_config_destroy(config);<br />
    waffle_display_disconnect(display);<br />
    return EXIT_SUCCESS;<br />
}</p>
<h3>Example 2</h3>
<p>An attribute list for creating an OpenGL 3.2 Core Profile context that has depth and stencil buffers and some non-zero number of bits in each of the RGB channels. Since the default value of <code>WAFFLE_ALPHA_SIZE</code> is <code>WAFFLE_DONT_CARE</code>, the config may not have an alpha channel. </p>
<pre><code>const int32_t attrib_list[] = {
    WAFFLE_CONTEXT_API,
    WAFFLE_CONTEXT_OPENGL,
    WAFFLE_CONTEXT_MAJOR_VERSION,
    3,
    WAFFLE_CONTEXT_MINOR_VERSION,
    2,
    WAFFLE_CONTEXT_PROFILE,
    WAFFLE_CONTEXT_CORE_PROFILE,

    WAFFLE_RED_SIZE,
    1,
    WAFFLE_GREEN_SIZE,
    1,
    WAFFLE_BLUE_SIZE,
    1,

    WAFFLE_DEPTH_SIZE,
    24,
    WAFFLE_STENCIL_SIZE,
    8,

    0,
};
</code></pre>
<h2>Issues</h2>
<p>Please report bugs or and feature requests to m[blue]<code><a rel="nofollow" href="https://github.com/waffle-gl/waffle/issues">https://github.com/waffle-gl/waffle/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-waffle/">waffle</a></code>(7)<code><a href="/docs/linux/man/3-waffle_context_create/">waffle_context_create</a></code>(3)<code><a href="/docs/linux/man/3-waffle_window_create/">waffle_window_create</a></code>(3)</p>
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
<dd>GLX_ARB_create_context_profile</p>
<dl>
<dd><a rel="nofollow" href="http://www.opengl.org/registry/specs/ARB/glx_create_context.txt">http://www.opengl.org/registry/specs/ARB/glx_create_context.txt</a></dl>
<dt> 3.</p>
<dd>GLX_EXT_create_context_es2_profile</p>
<dl>
<dd><a rel="nofollow" href="http://www.opengl.org/registry/specs/EXT/glx_create_context_es2_profile.txt">http://www.opengl.org/registry/specs/EXT/glx_create_context_es2_profile.txt</a></dl>
<dt> 4.</p>
<dd>EGL 1.4 Specification</p>
<dl>
<dd><a rel="nofollow" href="http://www.khronos.org/registry/egl/specs/eglspec.1.4.20110406.pdf">http://www.khronos.org/registry/egl/specs/eglspec.1.4.20110406.pdf</a></dl>
<dt> 5.</p>
<dd>EGL_KHR_create_context</p>
<dl>
<dd><a rel="nofollow" href="http://www.khronos.org/registry/egl/extensions/KHR/EGL_KHR_create_context.txt">http://www.khronos.org/registry/egl/extensions/KHR/EGL_KHR_create_context.txt</a></dl>
<dt> 6.</p>
<dd>CGL Reference</p>
<dl>
<dd><a rel="nofollow" href="https://developer.apple.com/library/mac/#documentation/graphicsimaging/reference/CGL_OpenGL/Reference/reference.html">https://developer.apple.com/library/mac/#documentation/graphicsimaging/reference/CGL_OpenGL/Reference/reference.html</a></dl>
