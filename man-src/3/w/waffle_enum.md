---
title: "waffle_enum(3)"
name: "waffle_enum"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_enum/"
description: "waffle_enum, waffle_enum_to_string – Listing of non-error enums and associated utility functions"
---

<p>waffle_enum, waffle_enum_to_string &#8211; Listing of non-error enums and associated utility functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

enum waffle_enum {... };

const char *waffle_enum_to_string(int32_t e);</code></pre>
<h2>Description</h2>
<p><code>waffle_enum_to_string()</code></p>
<dl>
<dd>
<dd>Convert an <code>waffle_enum</code> token to a string. For example, convert <code>WAFFLE_DONT_CARE</code> to &quot;WAFFLE_DONT_CARE&quot;. Return null if the token is not a valid <code>waffle_enum</code>. This function always sets the error code to <code>WAFFLE_NO_ERROR</code>. It can be called before waffle has been successfully initialized with <code><a href="/docs/linux/man/3-waffle_init/">waffle_init</a></code>(3)</dl>
<p> <code>enum waffle_enum</code></p>
<dl>
<dd>For reference, below is the complete list of waffle&#8217;s non-error enums. </p>
<pre><code>enum waffle_enum {
    // ------------------------------------------------------------------
    // Generic
    // ------------------------------------------------------------------

    WAFFLE_DONT_CARE                                            = -1,
    WAFFLE_NONE                                                 =  0,

    // ------------------------------------------------------------------
    // For waffle_init()
    // ------------------------------------------------------------------

    WAFFLE_PLATFORM                                             = 0x0010,
    WAFFLE_PLATFORM_ANDROID                                 = 0x0011,
    WAFFLE_PLATFORM_CGL                                     = 0x0012,
    WAFFLE_PLATFORM_GLX                                     = 0x0013,
    WAFFLE_PLATFORM_WAYLAND                                 = 0x0014,
    WAFFLE_PLATFORM_X11_EGL                                 = 0x0015,
    WAFFLE_PLATFORM_GBM                                     = 0x0016,
    WAFFLE_PLATFORM_WGL                                     = 0x0017,

    // ------------------------------------------------------------------
    // For waffle_config_choose()
    // ------------------------------------------------------------------

    WAFFLE_CONTEXT_API                                          = 0x020a,
    WAFFLE_CONTEXT_OPENGL                                   = 0x020b,
    WAFFLE_CONTEXT_OPENGL_ES1                               = 0x020c,
    WAFFLE_CONTEXT_OPENGL_ES2                               = 0x020d,
    WAFFLE_CONTEXT_OPENGL_ES3                               = 0x0214,

    WAFFLE_CONTEXT_MAJOR_VERSION                                = 0x020e,
    WAFFLE_CONTEXT_MINOR_VERSION                                = 0x020f,

    WAFFLE_CONTEXT_PROFILE                                      = 0x0210,
    WAFFLE_CONTEXT_CORE_PROFILE                             = 0x0211,
    WAFFLE_CONTEXT_COMPATIBILITY_PROFILE                    = 0x0212,

    WAFFLE_RED_SIZE                                             = 0x0201,
    WAFFLE_GREEN_SIZE                                           = 0x0202,
    WAFFLE_BLUE_SIZE                                            = 0x0203,
    WAFFLE_ALPHA_SIZE                                           = 0x0204,

    WAFFLE_DEPTH_SIZE                                           = 0x0205,
    WAFFLE_STENCIL_SIZE                                         = 0x0206,

    WAFFLE_SAMPLE_BUFFERS                                       = 0x0207,
    WAFFLE_SAMPLES                                              = 0x0208,

    WAFFLE_DOUBLE_BUFFERED                                      = 0x0209,

    WAFFLE_ACCUM_BUFFER                                         = 0x0213,

    // ------------------------------------------------------------------
    // For waffle_dl_sym()
    // ------------------------------------------------------------------

    WAFFLE_DL_OPENGL                                            = 0x0301,
    WAFFLE_DL_OPENGL_ES1                                        = 0x0302,
    WAFFLE_DL_OPENGL_ES2                                        = 0x0303,
};
</code></pre>
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
