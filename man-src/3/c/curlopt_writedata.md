---
title: "curlopt_writedata(3)"
name: "curlopt_writedata"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_writedata/"
description: "CURLOPT_WRITEDATA – custom pointer passed to the write callback"
---

<p>CURLOPT_WRITEDATA &#8211; custom pointer passed to the write callback</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_WRITEDATA, void *pointer);</p>
<h2>Description</h2>
<p>A data <i>pointer</i> to pass to the write callback. If you use the <i><a href="/docs/linux/man/3-curlopt_writefunction/">CURLOPT_WRITEFUNCTION</a>(3)</i> option, this is the pointer you&#8217;ll get in that callback&#8217;s 4th argument. If you don&#8217;t use a write callback, you must make <i>pointer</i> a &#8216;FILE *&#8217; (cast to &#8216;void *&#8217;) as libcurl will pass this to <i><a href="/docs/linux/man/3-fwrite/">fwrite</a>(3)</i> when writing data. </p>
<p> The internal <i><a href="/docs/linux/man/3-curlopt_writefunction/">CURLOPT_WRITEFUNCTION</a>(3)</i> will write the data to the FILE * given with this option, or to stdout if this option hasn&#8217;t been set. </p>
<p> If you&#8217;re using libcurl as a win32 DLL, you <code>MUST</code> use the <i><a href="/docs/linux/man/3-curlopt_writefunction/">CURLOPT_WRITEFUNCTION</a>(3)</i> if you set this option or you will experience crashes.</p>
<h2>Default</h2>
<p>By default, this is a FILE * to stdout.</p>
<h2>Protocols</h2>
<p>Used for all protocols.</p>
<h2>Example</h2>
<p>A common technique is to use the write callback to store the incoming data into a dynamically growing allocated buffer, and then this CURLOPT_WRITEDATA is used to point to a struct or the buffer to store data in. Like in the getinmemory example: <a rel="nofollow" href="http://curl.haxx.se/libcurl/c/getinmemory.html">http://curl.haxx.se/libcurl/c/getinmemory.html</a></p>
<h2>Availability</h2>
<p>Available in all libcurl versions. This option was formerly known as <i>CURLOPT_FILE</i>, the name <i>CURLOPT_WRITEDATA</i> was introduced in 7.9.7.</p>
<h2>Return Value</h2>
<p>This will return CURLE_OK.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_writefunction/">CURLOPT_WRITEFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_readdata/">CURLOPT_READDATA</a></code>(3),</p>
