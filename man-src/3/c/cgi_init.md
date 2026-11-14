---
title: "cgi_init(3)"
name: "cgi_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgi_init/"
description: "cgi_init – Initialize ClearSilver CGI environment"
---

<h2 class="name">NAME</h2>
<p> cgi_init &#8211; Initialize ClearSilver CGI environment </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgi.h&gt;
</code></pre>
<pre>
NEOERR *cgi_init (CGI **cgi, HDF *hdf);
</pre>
<h2>ARGUMENTS</h2>
<p> cgi &#8211; a pointer to a CGI pointer<br />
 hdf_file &#8211; the path to an HDF data set file that will also be<br />
 loaded into the dataset. This will likely have to<br />
 a be a full path, as the HDF search paths are not<br />
 yet set up. Certain things, like </p>
<h2>DESCRIPTION</h2>
<p> cgi_init initializes the ClearSilver CGI environment, including creating the HDF data set. It will then import the standard CGI environment variables into that dataset, will parse the QUERY_STRING into the data set, and parse the HTTP_COOKIE into the data set. Note that if the var xdisplay is in the form data, cgi_init will attempt to validate the value and launch the configured debugger on the CGI program. These variables have to be specified in the hdf_file pointed to by hdf_file. The default settings do not allow debugger launching for security reasons. </p>
<h2>RETURN VALUE</h2>
<p> cgi &#8211; an allocated CGI struct, including </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgi_debug_init/">cgi_debug_init</a></code>(3), <a href="/docs/linux/man/3-cgi_parse/">cgi_parse</a><code>(3), <a href="/docs/linux/man/3-cgi_destroy/">cgi_destroy</a></code>(3), <a href="/docs/linux/man/3-cgi_js_escape/">cgi_js_escape</a><code>(3), <a href="/docs/linux/man/3-cgi_html_escape_strfunc/">cgi_html_escape_strfunc</a></code>(3), <a href="/docs/linux/man/3-cgi_register_strfuncs/">cgi_register_strfuncs</a><code>(3), <a href="/docs/linux/man/3-cgi_output/">cgi_output</a></code>(3), <a href="/docs/linux/man/3-parse_rfc2388/">parse_rfc2388</a><code>(3), <a href="/docs/linux/man/3-cgi_url_validate/">cgi_url_validate</a></code>(3), <a href="/docs/linux/man/3-open_upload/">open_upload</a><code>(3), <a href="/docs/linux/man/3-cgi_cs_init/">cgi_cs_init</a></code>(3), <a href="/docs/linux/man/3-cgi_url_escape_more/">cgi_url_escape_more</a><code>(3), <a href="/docs/linux/man/3-cgi_html_strip_strfunc/">cgi_html_strip_strfunc</a></code>(3), <a href="/docs/linux/man/3-cgi_neo_error/">cgi_neo_error</a><code>(3), <a href="/docs/linux/man/3-cgi_redirect/">cgi_redirect</a></code>(3), <a href="/docs/linux/man/3-cgi_filehandle/">cgi_filehandle</a><code>(3), <a href="/docs/linux/man/3-cgi_register_parse_cb/">cgi_register_parse_cb</a></code>(3), <a href="/docs/linux/man/3-cgi_url_escape/">cgi_url_escape</a><code>(3), <a href="/docs/linux/man/3-cgi_init/">cgi_init</a></code>(3), <a href="/docs/linux/man/3-cgi_redirect_uri/">cgi_redirect_uri</a><code>(3), <a href="/docs/linux/man/3-cgi_cookie_clear/">cgi_cookie_clear</a></code>(3), <a href="/docs/linux/man/3-cgi_url_unescape/">cgi_url_unescape</a><code>(3), <a href="/docs/linux/man/3-cgi_vredirect/">cgi_vredirect</a></code>(3), <a href="/docs/linux/man/3-cgi_display/">cgi_display</a><code>(3), <a href="/docs/linux/man/3-cgi_html_ws_strip/">cgi_html_ws_strip</a></code>(3), <a href="/docs/linux/man/3-cgi_error/">cgi_error</a><code>(3), <a href="/docs/linux/man/3-cgi_cookie_set/">cgi_cookie_set</a></code>(3), <a href="/docs/linux/man/3-cgi_text_html_strfunc/">cgi_text_html_strfunc</a><code>(3), cgi_cookie_authority</code> </p>
<h2>Index</h2>
