---

title: "cgi_url_escape_more(3)"
name: "cgi_url_escape_more"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgi_url_escape_more/"
description: "cgi_url_escape_more – url escape a string"
---

<pre><code>
#include &lt;cgi/cgi.h&gt;
</code></pre>
<pre><code>
NEOERR *cgi_url_escape_more(const char *buf, char **esc, const char *other);
</code></pre>
<h2>ARGUMENTS</h2>
<p> buf &#8211; a 0 terminated string<br />
 other &#8211; a 0 terminated string of characters to escape </p>
<p> cgi_url_escape_more will do URL escaping on the passed in string, and return a newly allocated string that is escaped. Characters which are escaped include control characters, %, ?, +, space, =, &amp;, /, and &quot; and any characters in other </p>
<h2>RETURN VALUE</h2>
<p> esc &#8211; a newly allocated string </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgi_debug_init/">cgi_debug_init</a></code>(3), <a href="/docs/linux/man/3-cgi_parse/">cgi_parse</a><code>(3), <a href="/docs/linux/man/3-cgi_destroy/">cgi_destroy</a></code>(3), cgi_js_escape<code>(3), cgi_html_escape_strfunc</code>(3), cgi_register_strfuncs<code>(3), <a href="/docs/linux/man/3-cgi_output/">cgi_output</a></code>(3), parse_rfc2388<code>(3), <a href="/docs/linux/man/3-cgi_url_validate/">cgi_url_validate</a></code>(3), open_upload<code>(3), <a href="/docs/linux/man/3-cgi_cs_init/">cgi_cs_init</a></code>(3), <a href="/docs/linux/man/3-cgi_url_escape_more/">cgi_url_escape_more</a><code>(3), cgi_html_strip_strfunc</code>(3), <a href="/docs/linux/man/3-cgi_neo_error/">cgi_neo_error</a><code>(3), <a href="/docs/linux/man/3-cgi_redirect/">cgi_redirect</a></code>(3), <a href="/docs/linux/man/3-cgi_filehandle/">cgi_filehandle</a><code>(3), <a href="/docs/linux/man/3-cgi_register_parse_cb/">cgi_register_parse_cb</a></code>(3), <a href="/docs/linux/man/3-cgi_url_escape/">cgi_url_escape</a><code>(3), <a href="/docs/linux/man/3-cgi_init/">cgi_init</a></code>(3), <a href="/docs/linux/man/3-cgi_redirect_uri/">cgi_redirect_uri</a><code>(3), <a href="/docs/linux/man/3-cgi_cookie_clear/">cgi_cookie_clear</a></code>(3), <a href="/docs/linux/man/3-cgi_url_unescape/">cgi_url_unescape</a><code>(3), <a href="/docs/linux/man/3-cgi_vredirect/">cgi_vredirect</a></code>(3), <a href="/docs/linux/man/3-cgi_display/">cgi_display</a><code>(3), cgi_html_ws_strip</code>(3), <a href="/docs/linux/man/3-cgi_error/">cgi_error</a><code>(3), <a href="/docs/linux/man/3-cgi_cookie_set/">cgi_cookie_set</a></code>(3), cgi_text_html_strfunc<code>(3), cgi_cookie_authority</code> </p>
