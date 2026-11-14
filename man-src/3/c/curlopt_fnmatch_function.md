---
title: "curlopt_fnmatch_function(3)"
name: "curlopt_fnmatch_function"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_fnmatch_function/"
description: "CURLOPT_FNMATCH_FUNCTION – wildcard matching function callback"
---

<p>CURLOPT_FNMATCH_FUNCTION &#8211; wildcard matching function callback</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
int fnmatch_callback(void *ptr,
 const char *pattern,
 const char *string);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FNMATCH_FUNCTION,
 fnmatch_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This callback s used for wildcard matching. </p>
<p> Return <i>CURL_FNMATCHFUNC_MATCH</i> if pattern matches the string, <i>CURL_FNMATCHFUNC_NOMATCH</i> if not or <i>CURL_FNMATCHFUNC_FAIL</i> if an error occurred.</p>
<h2>Default</h2>
<p>NULL == an internal function for wildcard matching.</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.21.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_fnmatch_data/">CURLOPT_FNMATCH_DATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a></code>(3),</p>
