---
title: "curl_easy_pause(3)"
name: "curl_easy_pause"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_easy_pause/"
description: "curl_easy_pause – pause and unpause a connection"
---

<h2>NAME</h2>
<p> curl_easy_pause &#8211; pause and unpause a connection</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>CURLcode curl_easy_pause(CURL *handle</code><i>, int bitmask</i><code> );</code> </p>
<h2>DESCRIPTION</h2>
<p> Using this function, you can explicitly mark a running connection to get paused, and you can unpause a connection that was previously paused. </p>
<p> A connection can be paused by using this function or by letting the read or the write callbacks return the proper magic return code (<i>CURL_READFUNC_PAUSE</i> and <i>CURL_WRITEFUNC_PAUSE</i>). A write callback that returns pause signals to the library that it couldn&#8217;t take care of any data at all, and that data will then be delivered again to the callback when the writing is later unpaused. </p>
<p> NOTE: while it may feel tempting, take care and notice that you cannot call this function from another thread. </p>
<p> When this function is called to unpause reading, the chance is high that you will get your write callback called before this function returns. </p>
<p> The <code>handle</code> argument is of course identifying the handle that operates on the connection you want to pause or unpause. </p>
<p> The <code>bitmask</code> argument is a set of bits that sets the new state of the connection. The following bits can be used:</p>
<dl>
<dt>CURLPAUSE_RECV</p>
<dd> Pause receiving data. There will be no data received on this connection until this function is called again without this bit set. Thus, the write callback (<i>CURLOPT_WRITEFUNCTION</i>) won&#8217;t be called.</p>
<dt>CURLPAUSE_SEND</p>
<dd> Pause sending data. There will be no data sent on this connection until this function is called again without this bit set. Thus, the read callback (<i>CURLOPT_READFUNCTION</i>) won&#8217;t be called.</p>
<dt>CURLPAUSE_ALL</p>
<dd> Convenience define that pauses both directions.</p>
<dt>CURLPAUSE_CONT</p>
<dd> Convenience define that unpauses both directions</dl>
<h2>RETURN VALUE</h2>
<p> CURLE_OK (zero) means that the option was set properly, and a non-zero return code means something wrong occurred after the new state was set. See the <i><a href="/docs/linux/man/3-libcurl-errors/">libcurl-errors</a>(3)</i> man page for the full list with descriptions.</p>
<h2>AVAILABILITY</h2>
<p> This function was added in libcurl 7.18.0. Before this version, there was no explicit support for pausing transfers.</p>
<h2>MEMORY USE</h2>
<p> When pausing a read by returning the magic return code from a write callback, the read data is already in libcurl&#8217;s internal buffers so it&#8217;ll have to keep it in an allocated buffer until the reading is again unpaused using this function. </p>
<p> If the downloaded data is compressed and is asked to get uncompressed automatically on download, libcurl will continue to uncompress the entire downloaded chunk and it will cache the data uncompressed. This has the side- effect that if you download something that is compressed a lot, it can result in a very large data amount needing to be allocated to save the data during the pause. This said, you should probably consider not using paused reading if you allow libcurl to uncompress data automatically.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a></code>(3), <code><a href="/docs/linux/man/3-curl_easy_reset/">curl_easy_reset</a></code>(3) </p>
<h2>Index</h2>
