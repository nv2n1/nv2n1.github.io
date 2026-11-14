---
title: "curlopt_xferinfofunction(3)"
name: "curlopt_xferinfofunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_xferinfofunction/"
description: "CURLOPT_XFERINFOFUNCTION – callback to progress meter function"
---

<p>CURLOPT_XFERINFOFUNCTION &#8211; callback to progress meter function</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> int progress_callback(void *clientp,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>curl_off_t dltotal,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>curl_off_t dlnow,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>curl_off_t ultotal,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>curl_off_t ulnow); </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_XFERINFOFUNCTION, progress_callback);</p>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This function gets called by libcurl instead of its internal equivalent with a frequent interval. While data is being transferred it will be called very frequently, and during slow periods like when nothing is being transferred it can slow down to about one call per second. </p>
<p> <i>clientp</i> is the pointer set with <i><a href="/docs/linux/man/3-curlopt_xferinfodata/">CURLOPT_XFERINFODATA</a>(3)</i>, it is not used by libcurl but is only passed along from the application to the callback. </p>
<p> The callback gets told how much data libcurl will transfer and has transferred, in number of bytes. <i>dltotal</i> is the total number of bytes libcurl expects to download in this transfer. <i>dlnow</i> is the number of bytes downloaded so far. <i>ultotal</i> is the total number of bytes libcurl expects to upload in this transfer. <i>ulnow</i> is the number of bytes uploaded so far. </p>
<p> Unknown/unused argument values passed to the callback will be set to zero (like if you only download data, the upload size will remain 0). Many times the callback will be called one or more times first, before it knows the data sizes so a program must be made to handle that. </p>
<p> Returning a non-zero value from this callback will cause libcurl to abort the transfer and return <i>CURLE_ABORTED_BY_CALLBACK</i>. </p>
<p> If you transfer data with the multi interface, this function will not be called during periods of idleness unless you call the appropriate libcurl function that performs transfers. </p>
<p> <i><a href="/docs/linux/man/3-curlopt_noprogress/">CURLOPT_NOPROGRESS</a>(3)</i> must be set to 0 to make this function actually get called.</p>
<h2>Default</h2>
<p>By default, libcurl has an internal progress meter. That&#8217;s rarely wanted by users.</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<p><a rel="nofollow" href="http://curl.haxx.se/libcurl/c/progressfunc.html">http://curl.haxx.se/libcurl/c/progressfunc.html</a></p>
<h2>Availability</h2>
<p>Added in 7.32.0. This callback replaces <i><a href="/docs/linux/man/3-curlopt_progressfunction/">CURLOPT_PROGRESSFUNCTION</a>(3)</i></p>
<h2>Return Value</h2>
<p>Returns CURLE_OK.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_xferinfodata/">CURLOPT_XFERINFODATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_noprogress/">CURLOPT_NOPROGRESS</a></code>(3),</p>
