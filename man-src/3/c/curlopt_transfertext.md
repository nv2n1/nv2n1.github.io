---
title: "curlopt_transfertext(3)"
name: "curlopt_transfertext"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_transfertext/"
description: "CURLOPT_TRANSFERTEXT – request a text based transfer for FTP"
---

<p>CURLOPT_TRANSFERTEXT &#8211; request a text based transfer for FTP</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TRANSFERTEXT, long text);</p>
<h2>Description</h2>
<p>A parameter set to 1 tells the library to use ASCII mode for FTP transfers, instead of the default binary transfer. For win32 systems it does not set the stdout to binary mode. This option can be usable when transferring text data between systems with different views on certain characters, such as newlines or similar. </p>
<p> libcurl does not do a complete ASCII conversion when doing ASCII transfers over FTP. This is a known limitation/flaw that nobody has rectified. libcurl simply sets the mode to ASCII and performs a standard transfer.</p>
<h2>Default</h2>
<p>0, disabled</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Along with FTP</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if FTP is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_crlf/">CURLOPT_CRLF</a></code>(3),</p>
