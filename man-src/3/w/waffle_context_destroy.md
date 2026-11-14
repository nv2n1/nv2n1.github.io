---
title: "waffle_context_destroy(3)"
name: "waffle_context_destroy"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_context_destroy/"
description: "waffle_context, waffle_context_create, waffle_context_destroy, waffle_context_get_native – class waffle_context"
---

<p>waffle_context, waffle_context_create, waffle_context_destroy, waffle_context_get_native &#8211; class waffle_context</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

struct waffle_context;

struct waffle_context *waffle_context_create(struct waffle_config *config, struct waffle_context *shared_ctx);

bool waffle_context_destroy(struct waffle_context *self);

union waffle_native_context *waffle_context_get_native(struct waffle_context *self);</code></pre>
<h2>Description</h2>
<p><code>struct waffle_context</code></p>
<dl>
<dd>
<dd>An opaque type.</dl>
<p> <code>waffle_context_create()</code></p>
<dl>
<dd>Create a context for OpenGL rendering with the properties specified by <i>config</i>. </p>
<p> The returned context&#8217;s actual properties may differ from, but are guaranteed to be compatible with, the properties specified by <i>config</i>. See the section called &#8220;VERSION PROMOTION&#8221; below for details. </p>
<p> If <i>share_ctx</i> is not null, then the newly created context is added to the share group of <i>share_ctx</i>. Some data, such as display lists, are shared among all contexts that belong to the same share group. For details on what data is shared, see the specification for the relevant native platform: the m[blue]<code>GLX 1.4 Specification</code>m[]<font SIZE="-2">[1]</font>, the m[blue]<code>EGL 1.4 Specification</code>m[]<font SIZE="-2">[2]</font>, or the m[blue]<code>CGL Reference</code>m[]<font SIZE="-2">[3]</font>.</dl>
<p> <code>waffle_context_destroy()</code></p>
<dl>
<dd>Destroy the context and release its memory.</dl>
<p> <code>waffle_context_get_native()</code></p>
<dl>
<dd>Get the context&#8217;s underlying native objects. Use <code><a href="/docs/linux/man/3-free/">free</a></code>(3) to deallocate the returned pointer. See <code><a href="/docs/linux/man/3-waffle_native/">waffle_native</a></code>(3) for the definition of <code>union waffle_native_context</code>.</dl>
<h2>Version Promotion</h2>
<p>The context&#8217;s requested version and profile is given by the config attributes <code>WAFFLE_CONTEXT_MAJOR_VERSION</code>, <code>WAFFLE_CONTEXT_MINOR_VERSION</code>, <code>WAFFLE_CONTEXT_PROFILE</code>. The context returned by <code>waffle_context_create</code> may implement any version and profile that is backwards compatible with that requested, as described below. </p>
<dl>
<dd>&bull; If the chosen API is <code>WAFFLE_OPENGL_ES1</code>, <code>WAFFLE_OPENGL_ES2</code>, or <code>WAFFLE_OPENGL_ES3</code>, then the returned context may implement any of:</p>
<dl>
<dd>* The requested version.</dl>
<dl>
<dd>* Any later version, so long as no features have been from that later version.</dl>
</dl>
<dl>
<dd>&bull; If the chosen API is <code>WAFFLE_CONTEXT_OPENGL</code> and version 3.0 or less is requested, then the returned context may implement any of:</p>
<dl>
<dd>* Any version no less than that requested and no greater than 3.0.</dl>
<dl>
<dd>* Version 3.1, if the GL_ARB_compatibility extension is also implemented.</dl>
<dl>
<dd>* The compatibility profile of version 3.2 or greater.</dl>
</dl>
<dl>
<dd>&bull; If the chosen API is <code>WAFFLE_CONTEXT_OPENGL</code> and version 3.1 is requested, then the returned context may implement any of:</p>
<dl>
<dd>* Version 3.1, with or without the GL_ARB_compatibility extension.</dl>
<dl>
<dd>* The core profile of version 3.2 or greater.</dl>
</dl>
<dl>
<dd>&bull; If the chosen API is <code>WAFFLE_CONTEXT_OPENGL</code> and version 3.2 or greater is requested, then the returned context may implement any of:</p>
<dl>
<dd>* The requested profile and version.</dl>
<dl>
<dd>* The requested profile of any later version, so long as no features have been from that later version and profile.</dl>
</dl>
<h2>Return Value</h2>
<p>Functions whose return type is <code>bool</code> return true on success and false on failure. Functions whose return type is a pointer return <code>NULL</code> on failure. Use <code><a href="/docs/linux/man/3-waffle_error_get_info/">waffle_error_get_info</a></code>(3) to get information about any errors.</p>
<h2>Errors</h2>
<p>See <code><a href="/docs/linux/man/3-waffle_error/">waffle_error</a></code>(3) for the complete list of waffle&#8217;s error codes. </p>
<p> No errors are specific to the <code>waffle_context</code> functions.</p>
<h2>Issues</h2>
<p>Please report bugs or and feature requests to m[blue]<code><a rel="nofollow" href="https://github.com/waffle-gl/waffle/issues">https://github.com/waffle-gl/waffle/issues</a></code>m[].</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-waffle/">waffle</a></code>(7)<code><a href="/docs/linux/man/3-waffle_config_choose/">waffle_config_choose</a></code>(3)</p>
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
