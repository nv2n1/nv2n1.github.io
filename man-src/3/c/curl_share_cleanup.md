---
title: "curl_share_cleanup(3)"
name: "curl_share_cleanup"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_share_cleanup/"
description: "curl_share_cleanup – Clean up a shared object"
---

<h2>NAME</h2>
<p> curl_share_cleanup &#8211; Clean up a shared object</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>CURLSHcode curl_share_cleanup(CURLSH *</code><i>share_handle</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> This function deletes a shared object. The share handle cannot be used anymore when this function has been called. </p>
<h2>RETURN VALUE</h2>
<p> CURLSHE_OK (zero) means that the option was set properly, non-zero means an error occurred as <i>&lt;curl/curl.h&gt;</i> defines. See the <i>libcurl-errors.3</i> man page for the full list with descriptions. If an error occurs, then the share object will not be deleted.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_share_init/">curl_share_init</a></code>(3), <code><a href="/docs/linux/man/3-curl_share_setopt/">curl_share_setopt</a></code>(3) </p>
<h2>Index</h2>
