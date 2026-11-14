---
title: "cgi_vredirect(3)"
name: "cgi_vredirect"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgi_vredirect/"
description: "cgi_vredirect – send an HTTP 302 redirect response"
---

<h2 class="name">NAME</h2>
<p> cgi_vredirect &#8211; send an HTTP 302 redirect response </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgi.h&gt;
</code></pre>
<pre><code>
void cgi_vredirect(CGI *cgi, int uri, const char *fmt, va_list ap);
</code></pre>
<h2>ARGUMENTS</h2>
<p> cgi &#8211; cgi struct<br />
 uri &#8211; whether the URL is full (1) or path only (0)<br />
 fmt &#8211; printf format string<br />
 ap &#8211; stdarg va_list </p>
<h2>DESCRIPTION</h2>
<p> cgi_vredirect is mostly used internally, but can be used if you need a varargs version of the function. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgi_debug_init/">cgi_debug_init</a></code>(3), <a href="/docs/linux/man/3-cgi_parse/">cgi_parse</a><code>(3), <a href="/docs/linux/man/3-cgi_destroy/">cgi_destroy</a></code>(3), <a href="/docs/linux/man/3-cgi_js_escape/">cgi_js_escape</a><code>(3), <a href="/docs/linux/man/3-cgi_html_escape_strfunc/">cgi_html_escape_strfunc</a></code>(3), <a href="/docs/linux/man/3-cgi_register_strfuncs/">cgi_register_strfuncs</a><code>(3), <a href="/docs/linux/man/3-cgi_output/">cgi_output</a></code>(3), <a href="/docs/linux/man/3-parse_rfc2388/">parse_rfc2388</a><code>(3), <a href="/docs/linux/man/3-cgi_url_validate/">cgi_url_validate</a></code>(3), <a href="/docs/linux/man/3-open_upload/">open_upload</a><code>(3), <a href="/docs/linux/man/3-cgi_cs_init/">cgi_cs_init</a></code>(3), <a href="/docs/linux/man/3-cgi_url_escape_more/">cgi_url_escape_more</a><code>(3), <a href="/docs/linux/man/3-cgi_html_strip_strfunc/">cgi_html_strip_strfunc</a></code>(3), <a href="/docs/linux/man/3-cgi_neo_error/">cgi_neo_error</a><code>(3), <a href="/docs/linux/man/3-cgi_redirect/">cgi_redirect</a></code>(3), <a href="/docs/linux/man/3-cgi_filehandle/">cgi_filehandle</a><code>(3), <a href="/docs/linux/man/3-cgi_register_parse_cb/">cgi_register_parse_cb</a></code>(3), <a href="/docs/linux/man/3-cgi_url_escape/">cgi_url_escape</a><code>(3), <a href="/docs/linux/man/3-cgi_init/">cgi_init</a></code>(3), <a href="/docs/linux/man/3-cgi_redirect_uri/">cgi_redirect_uri</a><code>(3), <a href="/docs/linux/man/3-cgi_cookie_clear/">cgi_cookie_clear</a></code>(3), <a href="/docs/linux/man/3-cgi_url_unescape/">cgi_url_unescape</a><code>(3), <a href="/docs/linux/man/3-cgi_vredirect/">cgi_vredirect</a></code>(3), <a href="/docs/linux/man/3-cgi_display/">cgi_display</a><code>(3), <a href="/docs/linux/man/3-cgi_html_ws_strip/">cgi_html_ws_strip</a></code>(3), <a href="/docs/linux/man/3-cgi_error/">cgi_error</a><code>(3), <a href="/docs/linux/man/3-cgi_cookie_set/">cgi_cookie_set</a></code>(3), <a href="/docs/linux/man/3-cgi_text_html_strfunc/">cgi_text_html_strfunc</a><code>(3), cgi_cookie_authority</code> </p>
<h2>Index</h2>
