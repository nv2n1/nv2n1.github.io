---
title: "curlopt_netrc(3)"
name: "curlopt_netrc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_netrc/"
description: "CURLOPT_NETRC – request that .netrc is used"
---

<p>CURLOPT_NETRC &#8211; request that .netrc is used</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_NETRC, long level);</p>
<h2>Description</h2>
<p>This parameter controls the preference <i>level</i> of libcurl between using user names and passwords from your <i>~/.netrc</i> file, relative to user names and passwords in the URL supplied with <i><a href="/docs/linux/man/3-curlopt_url/">CURLOPT_URL</a>(3)</i>. </p>
<p> libcurl uses a user name (and supplied or prompted password) supplied with <i><a href="/docs/linux/man/3-curlopt_userpwd/">CURLOPT_USERPWD</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a>(3)</i> in preference to any of the options controlled by this parameter. </p>
<p> Only machine name, user name and password are taken into account (init macros and similar things aren&#8217;t supported). </p>
<p> libcurl does not verify that the file has the correct properties set (as the standard Unix ftp client does). It should only be readable by user. </p>
<p> <i>level</i> should be set to one of the values described below. </p>
<dl COMPACT>
<dt>CURL_NETRC_OPTIONAL</p>
<dd>The use of your <i>~/.netrc</i> file is optional, and information in the URL is to be preferred. The file will be scanned for the host and user name (to find the password only) or for the host only, to find the first user name and password after that <i>machine</i>, which ever information is not specified in the URL. </p>
<p> Undefined values of the option will have this effect.</p>
<dt>CURL_NETRC_IGNORED</p>
<dd>The library will ignore the file and use only the information in the URL. </p>
<p> This is the default.</p>
<dt>CURL_NETRC_REQUIRED</p>
<dd>This value tells the library that use of the file is required, to ignore the information in the URL, and to search the file for the host only.</dl>
<h2>Default</h2>
<p>CURL_NETRC_IGNORED</p>
<h2>Protocols</h2>
<p>Most</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_userpwd/">CURLOPT_USERPWD</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a></code>(3),</p>
