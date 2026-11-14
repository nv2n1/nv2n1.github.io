---
title: "curlopt_localportrange(3)"
name: "curlopt_localportrange"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_localportrange/"
description: "CURLOPT_LOCALPORTRANGE – number of additional local ports to try"
---

<p>CURLOPT_LOCALPORTRANGE &#8211; number of additional local ports to try</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_LOCALPORTRANGE,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>long range);</p>
<h2>Description</h2>
<p>Pass a long. The <i>range</i> argument is the number of attempts libcurl will make to find a working local port number. It starts with the given <i><a href="/docs/linux/man/3-curlopt_localport/">CURLOPT_LOCALPORT</a>(3)</i> and adds one to the number for each retry. Setting this option to 1 or below will make libcurl do only one try for the exact port number. Port numbers by nature are scarce resources that will be busy at times so setting this value to something too low might cause unnecessary connection setup failures.</p>
<h2>Default</h2>
<p>1</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.15.2</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_localport/">CURLOPT_LOCALPORT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_interface/">CURLOPT_INTERFACE</a></code>(3),</p>
