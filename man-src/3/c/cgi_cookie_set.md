---
title: "cgi_cookie_set(3)"
name: "cgi_cookie_set"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgi_cookie_set/"
description: "cgi_cookie_set – Set a browser Cookie"
---

<h2 class="name">NAME</h2>
<p> cgi_cookie_set &#8211; Set a browser Cookie </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgi.h&gt;
</code></pre>
<pre><code>
NEOERR *cgi_cookie_set(CGI *cgi, const char *name, const char *value,
                       const char *path, const char *domain,
                       const char *time_str, int persistent, int secure);
</code></pre>
<h2>ARGUMENTS</h2>
<p> cgi &#8211; a CGI struct<br />
 name &#8211; the name of the cookie<br />
 value &#8211; the value to set the cookie to.<br />
 path &#8211; optional path for which the cookie is valid. Default<br />
 is /<br />
 domain &#8211; optional domain for which the cookie is valid. You<br />
 can use cgi_cookie_authority to determine this<br />
 domain. Default is none, which is interpreted by<br />
 the browser as the sending domain only.<br />
 time_str &#8211; expiration time string in the following format </p>
<h2>DESCRIPTION</h2>
<p> cgi_cookie_set will issue a Set-Cookie header that should cause a browser to return a cookie when required. Note this function does no escaping of anything, you have to take care of that first. </p>
<p> HH:MM: SS GMT. Only used if persistent. Default is one year from time of call. persistent &#8211; cookie will be stored by the browser between sessions secure &#8211; cookie will only be sent over secure connections </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgi_debug_init/">cgi_debug_init</a></code>(3), <a href="/docs/linux/man/3-cgi_parse/">cgi_parse</a><code>(3), <a href="/docs/linux/man/3-cgi_destroy/">cgi_destroy</a></code>(3), <a href="/docs/linux/man/3-cgi_js_escape/">cgi_js_escape</a><code>(3), <a href="/docs/linux/man/3-cgi_html_escape_strfunc/">cgi_html_escape_strfunc</a></code>(3), <a href="/docs/linux/man/3-cgi_register_strfuncs/">cgi_register_strfuncs</a><code>(3), <a href="/docs/linux/man/3-cgi_output/">cgi_output</a></code>(3), <a href="/docs/linux/man/3-parse_rfc2388/">parse_rfc2388</a><code>(3), <a href="/docs/linux/man/3-cgi_url_validate/">cgi_url_validate</a></code>(3), <a href="/docs/linux/man/3-open_upload/">open_upload</a><code>(3), <a href="/docs/linux/man/3-cgi_cs_init/">cgi_cs_init</a></code>(3), <a href="/docs/linux/man/3-cgi_url_escape_more/">cgi_url_escape_more</a><code>(3), <a href="/docs/linux/man/3-cgi_html_strip_strfunc/">cgi_html_strip_strfunc</a></code>(3), <a href="/docs/linux/man/3-cgi_neo_error/">cgi_neo_error</a><code>(3), <a href="/docs/linux/man/3-cgi_redirect/">cgi_redirect</a></code>(3), <a href="/docs/linux/man/3-cgi_filehandle/">cgi_filehandle</a><code>(3), <a href="/docs/linux/man/3-cgi_register_parse_cb/">cgi_register_parse_cb</a></code>(3), <a href="/docs/linux/man/3-cgi_url_escape/">cgi_url_escape</a><code>(3), <a href="/docs/linux/man/3-cgi_init/">cgi_init</a></code>(3), <a href="/docs/linux/man/3-cgi_redirect_uri/">cgi_redirect_uri</a><code>(3), <a href="/docs/linux/man/3-cgi_cookie_clear/">cgi_cookie_clear</a></code>(3), <a href="/docs/linux/man/3-cgi_url_unescape/">cgi_url_unescape</a><code>(3), <a href="/docs/linux/man/3-cgi_vredirect/">cgi_vredirect</a></code>(3), <a href="/docs/linux/man/3-cgi_display/">cgi_display</a><code>(3), <a href="/docs/linux/man/3-cgi_html_ws_strip/">cgi_html_ws_strip</a></code>(3), <a href="/docs/linux/man/3-cgi_error/">cgi_error</a><code>(3), <a href="/docs/linux/man/3-cgi_cookie_set/">cgi_cookie_set</a></code>(3), <a href="/docs/linux/man/3-cgi_text_html_strfunc/">cgi_text_html_strfunc</a><code>(3), cgi_cookie_authority</code> </p>
<h2>Index</h2>
