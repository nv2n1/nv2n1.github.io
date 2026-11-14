---
title: "curlopt_readfunction(3)"
name: "curlopt_readfunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_readfunction/"
description: "CURLOPT_READFUNCTION – read callback for data uploads"
---

<p>CURLOPT_READFUNCTION &#8211; read callback for data uploads</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> size_t read_callback(char *buffer, size_t size, size_t nitems, void *instream); </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_READFUNCTION, read_callback); </p>
<h2>Description</h2>
<p>Pass a pointer to your callback function, as the prototype shows above. </p>
<p> This callback function gets called by libcurl as soon as it needs to read data in order to send it to the peer. The data area pointed at by the pointer <i>buffer</i> should be filled up with at most <i>size</i> multiplied with <i>nmemb</i> number of bytes by your function. </p>
<p> Your function must then return the actual number of bytes that it stored in that memory area. Returning 0 will signal end-of-file to the library and cause it to stop the current transfer. </p>
<p> If you stop the current transfer by returning 0 &quot;pre-maturely&quot; (i.e before the server expected it, like when you&#8217;ve said you will upload N bytes and you upload less than N bytes), you may experience that the server &quot;hangs&quot; waiting for the rest of the data that won&#8217;t come. </p>
<p> The read callback may return <i>CURL_READFUNC_ABORT</i> to stop the current operation immediately, resulting in a <i>CURLE_ABORTED_BY_CALLBACK</i> error code from the transfer. </p>
<p> The callback can return <i>CURL_READFUNC_PAUSE</i> to cause reading from this connection to pause. See <i><a href="/docs/linux/man/3-curl_easy_pause/">curl_easy_pause</a>(3)</i> for further details. </p>
<p> <code>Bugs</code>: when doing TFTP uploads, you must return the exact amount of data that the callback wants, or it will be considered the final packet by the server end and the transfer will end there. </p>
<p> If you set this callback pointer to NULL, or don&#8217;t set it at all, the default internal read function will be used. It is doing an fread() on the FILE * userdata set with <i><a href="/docs/linux/man/3-curlopt_readdata/">CURLOPT_READDATA</a>(3)</i>.</p>
<h2>Default</h2>
<p>The default internal read callback is fread().</p>
<h2>Protocols</h2>
<p>This is used for all protocols when doing uploads.</p>
<h2>Example</h2>
<p>Here&#8217;s an example setting a read callback for reading that to upload to an FTP site: <a rel="nofollow" href="http://curl.haxx.se/libcurl/c/ftpupload.html">http://curl.haxx.se/libcurl/c/ftpupload.html</a></p>
<h2>Availability</h2>
<p>CURL_READFUNC_PAUSE return code was added in 7.18.0 and CURL_READFUNC_ABORT was added in 7.12.1.</p>
<h2>Return Value</h2>
<p>This will return CURLE_OK.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_readdata/">CURLOPT_READDATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_writefunction/">CURLOPT_WRITEFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_seekfunction/">CURLOPT_SEEKFUNCTION</a></code>(3),</p>
