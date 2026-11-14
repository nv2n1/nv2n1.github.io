---
title: "curlopt_infilesize(3)"
name: "curlopt_infilesize"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_infilesize/"
description: "CURLOPT_INFILESIZE – set size of the input file to send off"
---

<p>CURLOPT_INFILESIZE &#8211; set size of the input file to send off</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_INFILESIZE, long filesize);</p>
<h2>Description</h2>
<p>When uploading a file to a remote site, <i>filesize</i> should be used to tell libcurl what the expected size of the input file is. This value must be passed as a long. See also <i><a href="/docs/linux/man/3-curlopt_infilesize_large/">CURLOPT_INFILESIZE_LARGE</a>(3)</i> for sending files larger than 2GB. </p>
<p> For uploading using SCP, this option or <i><a href="/docs/linux/man/3-curlopt_infilesize_large/">CURLOPT_INFILESIZE_LARGE</a>(3)</i> is mandatory. </p>
<p> To unset this value again, set it to -1. </p>
<p> When sending emails using SMTP, this command can be used to specify the optional SIZE parameter for the MAIL FROM command. </p>
<p> This option does not limit how much data libcurl will actually send, as that is controlled entirely by what the read callback returns, but telling one value and sending a different amount may lead to errors.</p>
<h2>Default</h2>
<p>Unset</p>
<h2>Protocols</h2>
<p>Many</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>SMTP support added in 7.23.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_infilesize_large/">CURLOPT_INFILESIZE_LARGE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_upload/">CURLOPT_UPLOAD</a></code>(3),</p>
