---
title: "curlopt_writefunction(3)"
name: "curlopt_writefunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_writefunction/"
description: "CURLOPT_WRITEFUNCTION – set callback for writing received data"
---

<p>CURLOPT_WRITEFUNCTION &#8211; set callback for writing received data</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
size_t write_callback(char *ptr, size_t size, size_t nmemb, void *userdata);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_WRITEFUNCTION, write_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This callback function gets called by libcurl as soon as there is data received that needs to be saved. <i>ptr</i> points to the delivered data, and the size of that data is <i>size</i> multiplied with <i>nmemb</i>. </p>
<p> The callback function will be passed as much data as possible in all invokes, but you must not make any assumptions. It may be one byte, it may be thousands. The maximum amount of body data that will be passed to the write callback is defined in the curl.h header file: <i>CURL_MAX_WRITE_SIZE</i> (the usual default is 16K). If <i><a href="/docs/linux/man/3-curlopt_header/">CURLOPT_HEADER</a>(3)</i> is enabled, which makes header data get passed to the write callback, you can get up to <i>CURL_MAX_HTTP_HEADER</i> bytes of header data passed into it. This usually means 100K. </p>
<p> This function may be called with zero bytes data if the transferred file is empty. </p>
<p> The data passed to this function will not be zero terminated! </p>
<p> Set the <i>userdata</i> argument with the <i><a href="/docs/linux/man/3-curlopt_writedata/">CURLOPT_WRITEDATA</a>(3)</i> option. </p>
<p> Your callback should return the number of bytes actually taken care of. If that amount differs from the amount passed to your callback function, it&#8217;ll signal an error condition to the library. This will cause the transfer to get aborted and the libcurl function used will return <i>CURLE_WRITE_ERROR</i>. </p>
<p> If your callback function returns CURL_WRITEFUNC_PAUSE it will cause this transfer to become paused. See <i><a href="/docs/linux/man/3-curl_easy_pause/">curl_easy_pause</a>(3)</i> for further details. </p>
<p> Set this option to NULL to get the internal default function used instead of your callback. The internal default function will write the data to the FILE * given with <i><a href="/docs/linux/man/3-curlopt_writedata/">CURLOPT_WRITEDATA</a>(3)</i>.</p>
<h2>Default</h2>
<p>libcurl will use &#8216;fwrite&#8217; as a callback by default.</p>
<h2>Protocols</h2>
<p>For all protocols</p>
<h2>Availability</h2>
<p>Support for the CURL_WRITEFUNC_PAUSE return code was added in version 7.18.0.</p>
<h2>Return Value</h2>
<p>This will return CURLE_OK.</p>
<h2>Example</h2>
<p>A common technique is to use this callback to store the incoming data into a dynamically growing allocated buffer. Like in the getinmemory example: <a rel="nofollow" href="http://curl.haxx.se/libcurl/c/getinmemory.html">http://curl.haxx.se/libcurl/c/getinmemory.html</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_writedata/">CURLOPT_WRITEDATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_readfunction/">CURLOPT_READFUNCTION</a></code>(3),</p>
