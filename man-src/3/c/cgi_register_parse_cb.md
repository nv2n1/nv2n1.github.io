---
title: "cgi_register_parse_cb(3)"
name: "cgi_register_parse_cb"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgi_register_parse_cb/"
description: "cgi_register_parse_cb – Register a parse callback"
---

<h2 class="name">NAME</h2>
<p> cgi_register_parse_cb &#8211; Register a parse callback </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;cgi/cgi.h&gt;
</code></pre>
<pre><code>
NEOERR *cgi_register_parse_cb(CGI *cgi, const char *method, const char *ctype,
                              void *rock, CGI_PARSE_CB parse_cb);
</code></pre>
<h2>ARGUMENTS</h2>
<p> cgi &#8211; a CGI struct<br />
 method &#8211; the HTTP method you want to handle, or * for all<br />
 ctype &#8211; the HTTP Content-Type you want to handle, or * for all<br />
 rock &#8211; opaque data that we&#8217;ll pass to your call back </p>
<h2>DESCRIPTION</h2>
<p> The ClearSilver CGI Kit has built-in functionality to handle the following methods: GET -&gt; doesn&#8217;t have any data except query string, which is processed for all methods POST w/ application/x-www-form-urlencoded POST w/ multipart/form-data processed as RFC2388 data into files and HDF (see cgi_filehandle()) PUT (any type) The entire data chunk is stored as a file, with meta data in HDF (similar to single files in RFC2388). The data is accessible via cgi_filehandle with NULL for name. To handle other methods/content types, you have to register your own parse function. This isn&#8217;t necessary if you aren&#8217;t expecting any data, and technically HTTP only allows data on PUT/POST requests (and presumably user defined methods). In particular, if you want to implement XML-RPC or SOAP, you&#8217;ll have to register a callback here to grab the XML data chunk. Usually you&#8217;ll want to register POST w/ application/xml or POST w/ text/xml (you either need to register both or register POST w/ * and check the ctype yourself, remember to nerr_raise(CGIParseNotHandled) if you aren&#8217;t handling the POST). In general, your callback should: Find out how much data is available: l = hdf_get_value (cgi-&gt;hdf, &quot;CGI.ContentLength&quot;, NULL); len = <a href="/docs/linux/man/l-atoi/">atoi</a>(l); And read/handle all of the data using cgiwrap_read. See the builtin handlers for how this is done. Note that cgiwrap_read is not guarunteed to return all of the data you request (just like <a href="/docs/linux/man/3-fread/">fread</a>(3)) since it might be reading of a socket. Sorry. You should be careful when reading the data to watch for short reads (ie, end of file) and cases where the client sends you data ad infinitum. </p>
<h2>RETURN VALUE</h2>
<p> None </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cgi_debug_init/">cgi_debug_init</a></code>(3), <a href="/docs/linux/man/3-cgi_parse/">cgi_parse</a><code>(3), <a href="/docs/linux/man/3-cgi_destroy/">cgi_destroy</a></code>(3), <a href="/docs/linux/man/3-cgi_js_escape/">cgi_js_escape</a><code>(3), <a href="/docs/linux/man/3-cgi_html_escape_strfunc/">cgi_html_escape_strfunc</a></code>(3), <a href="/docs/linux/man/3-cgi_register_strfuncs/">cgi_register_strfuncs</a><code>(3), <a href="/docs/linux/man/3-cgi_output/">cgi_output</a></code>(3), <a href="/docs/linux/man/3-parse_rfc2388/">parse_rfc2388</a><code>(3), <a href="/docs/linux/man/3-cgi_url_validate/">cgi_url_validate</a></code>(3), <a href="/docs/linux/man/3-open_upload/">open_upload</a><code>(3), <a href="/docs/linux/man/3-cgi_cs_init/">cgi_cs_init</a></code>(3), <a href="/docs/linux/man/3-cgi_url_escape_more/">cgi_url_escape_more</a><code>(3), <a href="/docs/linux/man/3-cgi_html_strip_strfunc/">cgi_html_strip_strfunc</a></code>(3), <a href="/docs/linux/man/3-cgi_neo_error/">cgi_neo_error</a><code>(3), <a href="/docs/linux/man/3-cgi_redirect/">cgi_redirect</a></code>(3), <a href="/docs/linux/man/3-cgi_filehandle/">cgi_filehandle</a><code>(3), <a href="/docs/linux/man/3-cgi_register_parse_cb/">cgi_register_parse_cb</a></code>(3), <a href="/docs/linux/man/3-cgi_url_escape/">cgi_url_escape</a><code>(3), <a href="/docs/linux/man/3-cgi_init/">cgi_init</a></code>(3), <a href="/docs/linux/man/3-cgi_redirect_uri/">cgi_redirect_uri</a><code>(3), <a href="/docs/linux/man/3-cgi_cookie_clear/">cgi_cookie_clear</a></code>(3), <a href="/docs/linux/man/3-cgi_url_unescape/">cgi_url_unescape</a><code>(3), <a href="/docs/linux/man/3-cgi_vredirect/">cgi_vredirect</a></code>(3), <a href="/docs/linux/man/3-cgi_display/">cgi_display</a><code>(3), <a href="/docs/linux/man/3-cgi_html_ws_strip/">cgi_html_ws_strip</a></code>(3), <a href="/docs/linux/man/3-cgi_error/">cgi_error</a><code>(3), <a href="/docs/linux/man/3-cgi_cookie_set/">cgi_cookie_set</a></code>(3), <a href="/docs/linux/man/3-cgi_text_html_strfunc/">cgi_text_html_strfunc</a><code>(3), cgi_cookie_authority</code> </p>
<h2>Index</h2>
