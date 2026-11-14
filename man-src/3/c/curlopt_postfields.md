---
title: "curlopt_postfields(3)"
name: "curlopt_postfields"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_postfields/"
description: "CURLOPT_POSTFIELDS – specify data to POST to server"
---

<p>CURLOPT_POSTFIELDS &#8211; specify data to POST to server</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_POSTFIELDS, char *postdata);</p>
<h2>Description</h2>
<p>Pass a char * as parameter, pointing to the full data to send in a HTTP POST operation. You must make sure that the data is formatted the way you want the server to receive it. libcurl will not convert or encode it for you in any way. For example, the web server may assume that this data is url-encoded. </p>
<p> The data pointed to is NOT copied by the library: as a consequence, it must be preserved by the calling application until the associated transfer finishes. This behaviour can be changed (so libcurl does copy the data) by setting the <i><a href="/docs/linux/man/3-curlopt_copypostfields/">CURLOPT_COPYPOSTFIELDS</a>(3)</i> option. </p>
<p> This POST is a normal application/x-www-form-urlencoded kind (and libcurl will set that Content-Type by default when this option is used), which is commonly used by HTML forms. Change Content-Type with <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i>. </p>
<p> Using <i><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a>(3)</i> implies <i><a href="/docs/linux/man/3-curlopt_post/">CURLOPT_POST</a>(3)</i>. </p>
<p> If you want to do a zero-byte POST, you need to set <i><a href="/docs/linux/man/3-curlopt_postfieldsize/">CURLOPT_POSTFIELDSIZE</a>(3)</i> explicitly to zero, as simply setting <i><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a>(3)</i> to NULL or &quot;&quot; just effectively disables the sending of the specified string. libcurl will instead assume that you&#8217;ll send the POST data using the read callback! </p>
<p> Using POST with HTTP 1.1 implies the use of a &quot;Expect: 100-continue&quot; header. You can disable this header with <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i> as usual. </p>
<p> To make multipart/formdata posts (aka RFC2388-posts), check out the <i><a href="/docs/linux/man/3-curlopt_httppost/">CURLOPT_HTTPPOST</a>(3)</i> option combined with <i><a href="/docs/linux/man/3-curl_formadd/">curl_formadd</a>(3)</i>.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 const char *data = &quot;data to send&quot;;
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 /* size of the POST data */
 curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, 12L);
 /* pass in a pointer to the data - libcurl will not copy */
 curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_postfieldsize/">CURLOPT_POSTFIELDSIZE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_readfunction/">CURLOPT_READFUNCTION</a></code>(3),</p>
