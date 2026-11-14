---
title: "curlopt_copypostfields(3)"
name: "curlopt_copypostfields"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_copypostfields/"
description: "CURLOPT_COPYPOSTFIELDS – have libcurl copy data to POST"
---

<p>CURLOPT_COPYPOSTFIELDS &#8211; have libcurl copy data to POST</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_COPYPOSTFIELDS, char *data);</p>
<h2>Description</h2>
<p>Pass a char * as parameter, which should be the full <i>data</i> to post in a HTTP POST operation. It behaves as the <i><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a>(3)</i> option, but the original data is instead copied by the library, allowing the application to overwrite the original data after setting this option. </p>
<p> Because data are copied, care must be taken when using this option in conjunction with <i><a href="/docs/linux/man/3-curlopt_postfieldsize/">CURLOPT_POSTFIELDSIZE</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_postfieldsize_large/">CURLOPT_POSTFIELDSIZE_LARGE</a>(3)</i>: If the size has not been set prior to <i><a href="/docs/linux/man/3-curlopt_copypostfields/">CURLOPT_COPYPOSTFIELDS</a>(3)</i>, the data is assumed to be a zero terminated string; else the stored size informs the library about the byte count to copy. In any case, the size must not be changed after <i><a href="/docs/linux/man/3-curlopt_copypostfields/">CURLOPT_COPYPOSTFIELDS</a>(3)</i>, unless another <i><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_copypostfields/">CURLOPT_COPYPOSTFIELDS</a>(3)</i> option is issued.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP(S)</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 char local_buffer[1024]=&quot;data to send&quot;;
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 /* size of the data to copy from the buffer and send in the request */
 curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, 12L);
 /* send data from the local stack */
 curl_easy_setopt(curl, CURLOPT_COPYPOSTFIELDS, local_buffer);
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Added in 7.17.1</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_postfieldsize/">CURLOPT_POSTFIELDSIZE</a></code>(3),</p>
