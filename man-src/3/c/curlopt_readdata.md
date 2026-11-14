---
title: "curlopt_readdata(3)"
name: "curlopt_readdata"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_readdata/"
description: "CURLOPT_READDATA – custom pointer passed to the read callback"
---

<p>CURLOPT_READDATA &#8211; custom pointer passed to the read callback</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_READDATA, void *pointer);</p>
<h2>Description</h2>
<p>Data <i>pointer</i> to pass to the file read function. If you use the <i><a href="/docs/linux/man/3-curlopt_readfunction/">CURLOPT_READFUNCTION</a>(3)</i> option, this is the pointer you&#8217;ll get as input in the 4th argument to the callback. </p>
<p> If you don&#8217;t specify a read callback but instead rely on the default internal read function, this data must be a valid readable FILE * (cast to &#8216;void *&#8217;). </p>
<p> If you&#8217;re using libcurl as a win32 DLL, you MUST use a <i><a href="/docs/linux/man/3-curlopt_readfunction/">CURLOPT_READFUNCTION</a>(3)</i> if you set this option.</p>
<h2>Default</h2>
<p>By default, this is a FILE * to stdin.</p>
<h2>Protocols</h2>
<p>This is used for all protocols when sending data.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>This option was once known by the older name <i>CURLOPT_INFILE</i>, the name <i>CURLOPT_READDATA</i> was introduced in 7.9.7.</p>
<h2>Return Value</h2>
<p>This will return CURLE_OK.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_readfunction/">CURLOPT_READFUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_writedata/">CURLOPT_WRITEDATA</a></code>(3),</p>
