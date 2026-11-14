---
title: "waffle_error(3)"
name: "waffle_error"
section: "3"
letter: "w"
url: "/docs/linux/man/3-waffle_error/"
description: "waffle_error, waffle_error_get_info, waffle_error_get_code, waffle_error_to_string – Thread-local error state"
---

<p>waffle_error, waffle_error_get_info, waffle_error_get_code, waffle_error_to_string &#8211; Thread-local error state</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;waffle.h&gt;

enum waffle_error {... };

struct waffle_error_info {
    enum waffle_error code;
    const char *message;
    size_t message_length;
};

const struct waffle_error_info *waffle_error_get_info(void);

enum waffle_error waffle_error_get_code(void);

const char *waffle_error_to_string(enum waffle_errore);</code></pre>
<h2>Description</h2>
<dd>Waffle functions usually return either a <code>bool</code>, in which false indicates failure, or a pointer, in which null indicates failure. In addition to returning a flag indicating failure, most functions also clear and then set some thread-local error state. The only functions that do not alter waffle&#8217;s error state are listed here and are explicitly documented as such. All functions listed here can be called before waffle has been successfully initialized with <code><a href="/docs/linux/man/3-waffle_init/">waffle_init</a></code>(3) <code>struct waffle_error_info</code></p>
<dl>
<dd>This struct contains the user-visible portion of waffle&#8217;s thread-local error state. <i>code</i> may be any token from <code>enum waffle_error</code>. <i>message</i> often contains a descriptive message about the error. It is never null, though it may be the empty string. <i>message_length</i> is the length of <i>message</i> according to <code><a href="/docs/linux/man/3-strlen/">strlen</a></code>(3).</dl>
<p> <code>waffle_error_to_string()</code></p>
<dl>
<dd>Convert a <code>waffle_error</code> token to a string. For example, convert <code>WAFFLE_ERROR_UNKNOWN</code> to &quot;WAFFLE_ERROR_UNKNOWN&quot;. Return null if the token is not a valid error token. This function always sets the error code to <code>WAFFLE_ERROR_NONE</code>.</dl>
<p> <code>waffle_error_get_info()</code></p>
<dl>
<dd>Get information about the current thread&#8217;s error state. This function never returns null. The returned pointer becomes invalid when the thread-local error state changes. This function does not alter waffle&#8217;s error state.</dl>
<p> <code>waffle_error_get_code()</code></p>
<dl>
<dd>Get the current thread&#8217;s error code. Calling this function is equivalent to obtaining the error code with waffle_error_get_info()-&gt;code. This function does not alter waffle&#8217;s error state.</dl>
<p> <code>enum waffle_error</code></p>
<dl>
<dd>For reference, below is the complete list of waffle&#8217;s error codes. <code>WAFFLE_NO_ERROR</code> = 0x00</p>
<dl>
<dd>The function succeeded.</dl>
<p> <code>WAFFLE_ERROR_FATAL</code> = 0x01</p>
<dl>
<dd>Waffle encountered a fatal error. All future waffle calls result in undefined behavior.</dl>
<p> <code>WAFFLE_ERROR_UNKNOWN</code> = 0x02</p>
<dl>
<dd>Waffle encountered an error for which it lacks an error code. This is usually produced when an underlying native call, such as <code><a href="/docs/linux/man/3-xopendisplay/">XOpenDisplay</a></code>(3), fails for an unknown reason.</dl>
<p> <code>WAFFLE_ERROR_INTERNAL</code> = 0x03</p>
<dl>
<dd>You found a bug in waffle. Please report it. The error message, obtained by <code>waffle_error_get_info()</code>, should contain a description of the bug.</dl>
<p> <code>WAFFLE_ERROR_BAD_ALLOC</code> = 0x04</p>
<dl>
<dd>Waffle failed to allocate memory.</dl>
<p> <code>WAFFLE_ERROR_NOT_INITIALIZED</code> = 0x05</p>
<dl>
<dd>The failed function requires waffle to be initialized with <code><a href="/docs/linux/man/3-waffle_init/">waffle_init</a></code>(3).</dl>
<p> <code>WAFFLE_ERROR_ALREADY_INITIALIZED</code> = 0x06</p>
<dl>
<dd>If waffle has already been initialized by a successful call to <code><a href="/docs/linux/man/3-waffle_init/">waffle_init</a></code>(3), then subsequent calls to <code>waffle_init()</code> produce this error.</dl>
<p> <code>WAFFLE_ERROR_BAD_ATTRIBUTE</code> = 0x08</p>
<dl>
<dd>An unrecognized attribute name or attribute value was passed in an attribute list.</dl>
<p> <code>WAFFLE_ERROR_BAD_PARAMETER</code> = 0x10</p>
<dl>
<dd>The failed function was passed an invalid argument.</dl>
<p> <code>WAFFLE_ERROR_BAD_DISPLAY_MATCH</code> = 0x11</p>
<dl>
<dd>The waffle objects passed to the failed function belong to different displays.</dl>
<p> <code>WAFFLE_ERROR_UNSUPPORTED_ON_PLATFORM</code> = 0x12</p>
<dl>
<dd>The requested action is unsupported on the current system or platform, but is otherwise valid. For example, attempting to choose a <code>waffle_config</code> whose API is OpenGL ES1 on a system that doesn&#8217;t OpenGL ES1 will produce this error.</dl>
<p> <code>WAFFLE_ERROR_BUILT_WITHOUT_SUPPORT</code> = 0x13</p>
<dl>
<dd>Waffle was built without support for the requested action. For example, if waffle was built without support for GBM, then calling waffle_init() with attribute WAFFLE_PLATFORM=WAFFLE_PLATFORM_GBM will produce this error.</dl>
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
