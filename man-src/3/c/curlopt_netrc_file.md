---
title: "curlopt_netrc_file(3)"
name: "curlopt_netrc_file"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_netrc_file/"
description: "CURLOPT_NETRC_FILE – file name to read .netrc info from"
---

<p>CURLOPT_NETRC_FILE &#8211; file name to read .netrc info from</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_NETRC_FILE, char *file);</p>
<h2>Description</h2>
<p>Pass a char * as parameter, pointing to a zero terminated string containing the full path name to the <i>file</i> you want libcurl to use as .netrc file. If this option is omitted, and <i><a href="/docs/linux/man/3-curlopt_netrc/">CURLOPT_NETRC</a>(3)</i> is set, libcurl will attempt to find a .netrc file in the current user&#8217;s home directory.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.10.9</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_netrc/">CURLOPT_NETRC</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a></code>(3),</p>
