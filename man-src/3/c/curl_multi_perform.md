---
title: "curl_multi_perform(3)"
name: "curl_multi_perform"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_perform/"
description: "curl_multi_perform – reads/writes available data from each easy handle"
---

<h2>NAME</h2>
<p> curl_multi_perform &#8211; reads/writes available data from each easy handle</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_perform(CURLM *multi_handle, int *running_handles);</p>
<h2>DESCRIPTION</h2>
<p> This function handles transfers on all the added handles that need attention in an non-blocking fashion. </p>
<p> When an application has found out there&#8217;s data available for the multi_handle or a timeout has elapsed, the application should call this function to read/write whatever there is to read or write right now etc. curl_multi_perform() returns as soon as the reads/writes are done. This function does not require that there actually is any data available for reading or that data can be written, it can be called just in case. It will write the number of handles that still transfer data in the second argument&#8217;s integer-pointer. </p>
<p> If the amount of <i>running_handles</i> is changed from the previous call (or is less than the amount of easy handles you&#8217;ve added to the multi handle), you know that there is one or more transfers less &quot;running&quot;. You can then call <i><a href="/docs/linux/man/3-curl_multi_info_read/">curl_multi_info_read</a>(3)</i> to get information about each individual completed transfer, and that returned info includes CURLcode and more. If an added handle fails very quickly, it may never be counted as a running_handle. </p>
<p> When <i>running_handles</i> is set to zero (0) on the return of this function, there is no longer any transfers in progress.</p>
<h2>RETURN VALUE</h2>
<p> CURLMcode type, general libcurl multi interface error code. </p>
<p> Before version 7.20.0: If you receive <i>CURLM_CALL_MULTI_PERFORM</i>, this basically means that you should call <i>curl_multi_perform</i> again, before you select() on more actions. You don&#8217;t have to do it immediately, but the return code means that libcurl may have more data available to return or that there may be more data to send off before it is &quot;satisfied&quot;. Do note that <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i> will return <i>CURLM_CALL_MULTI_PERFORM</i> only when it wants to be called again <code>immediately</code>. When things are fine and there is nothing immediate it wants done, it&#8217;ll return <i>CURLM_OK</i> and you need to wait for &quot;action&quot; and then call this function again. </p>
<p> This function only returns errors etc regarding the whole multi stack. Problems still might have occurred on individual transfers even when this function returns <i>CURLM_OK</i>. Use <i><a href="/docs/linux/man/3-curl_multi_info_read/">curl_multi_info_read</a>(3)</i> to figure out how individual transfers did.</p>
<h2>TYPICAL USAGE</h2>
<p> Most applications will use <i><a href="/docs/linux/man/3-curl_multi_fdset/">curl_multi_fdset</a>(3)</i> to get the multi_handle&#8217;s file descriptors, and <i><a href="/docs/linux/man/3-curl_multi_timeout/">curl_multi_timeout</a>(3)</i> to get a suitable timeout period, then it&#8217;ll wait for action on the file descriptors using <code><a href="/docs/linux/man/3-select/">select</a>(3)</code>. As soon as one or more file descriptor is ready, <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i> gets called.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_init/">curl_multi_init</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_fdset/">curl_multi_fdset</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_info_read/">curl_multi_info_read</a></code>(3), <code><a href="/docs/linux/man/3-libcurl-errors/">libcurl-errors</a></code>(3) </p>
<h2>Index</h2>
