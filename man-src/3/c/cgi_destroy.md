---
title: "cgi_destroy(3)"
name: "cgi_destroy"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgi_destroy/"
description: "cgi_destroy – deallocate the data associated with a CGI"
---

<h2 class="name">NAME</h2>
<p> cgi_destroy &#8211; deallocate the data associated with a CGI </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgi.h&gt;
</code></pre>
<pre><code>
void cgi_destroy(CGI **cgi);
</code></pre>
<h2>ARGUMENTS</h2>
<p> cgi &#8211; a pointer to a pointer to a CGI struct </p>
<h2>DESCRIPTION</h2>
<p> cgi_destroy will destroy all the data associated with a CGI, which mostly means the associated HDF and removal of any files that were uploaded via multipart/form-data. (Note that even in the event of a crash, these files will be deleted, as they were unlinked on creation and only exist because of the open file pointer) </p>
<h2>RETURN VALUE</h2>
<p> cgi &#8211; NULL on output </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgi_debug_init/">cgi_debug_init</a></code>(3), <a href="/docs/linux/man/3-cgi_parse/">cgi_parse</a><code>(3), <a href="/docs/linux/man/3-cgi_destroy/">cgi_destroy</a></code>(3), <a href="/docs/linux/man/3-cgi_js_escape/">cgi_js_escape</a><code>(3), <a href="/docs/linux/man/3-cgi_html_escape_strfunc/">cgi_html_escape_strfunc</a></code>(3), <a href="/docs/linux/man/3-cgi_register_strfuncs/">cgi_register_strfuncs</a><code>(3), <a href="/docs/linux/man/3-cgi_output/">cgi_output</a></code>(3), <a href="/docs/linux/man/3-parse_rfc2388/">parse_rfc2388</a><code>(3), <a href="/docs/linux/man/3-cgi_url_validate/">cgi_url_validate</a></code>(3), <a href="/docs/linux/man/3-open_upload/">open_upload</a><code>(3), <a href="/docs/linux/man/3-cgi_cs_init/">cgi_cs_init</a></code>(3), <a href="/docs/linux/man/3-cgi_url_escape_more/">cgi_url_escape_more</a><code>(3), <a href="/docs/linux/man/3-cgi_html_strip_strfunc/">cgi_html_strip_strfunc</a></code>(3), <a href="/docs/linux/man/3-cgi_neo_error/">cgi_neo_error</a><code>(3), <a href="/docs/linux/man/3-cgi_redirect/">cgi_redirect</a></code>(3), <a href="/docs/linux/man/3-cgi_filehandle/">cgi_filehandle</a><code>(3), <a href="/docs/linux/man/3-cgi_register_parse_cb/">cgi_register_parse_cb</a></code>(3), <a href="/docs/linux/man/3-cgi_url_escape/">cgi_url_escape</a><code>(3), <a href="/docs/linux/man/3-cgi_init/">cgi_init</a></code>(3), <a href="/docs/linux/man/3-cgi_redirect_uri/">cgi_redirect_uri</a><code>(3), <a href="/docs/linux/man/3-cgi_cookie_clear/">cgi_cookie_clear</a></code>(3), <a href="/docs/linux/man/3-cgi_url_unescape/">cgi_url_unescape</a><code>(3), <a href="/docs/linux/man/3-cgi_vredirect/">cgi_vredirect</a></code>(3), <a href="/docs/linux/man/3-cgi_display/">cgi_display</a><code>(3), <a href="/docs/linux/man/3-cgi_html_ws_strip/">cgi_html_ws_strip</a></code>(3), <a href="/docs/linux/man/3-cgi_error/">cgi_error</a><code>(3), <a href="/docs/linux/man/3-cgi_cookie_set/">cgi_cookie_set</a></code>(3), <a href="/docs/linux/man/3-cgi_text_html_strfunc/">cgi_text_html_strfunc</a><code>(3), cgi_cookie_authority</code> </p>
<h2>Index</h2>
