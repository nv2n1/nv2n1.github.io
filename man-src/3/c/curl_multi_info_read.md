---
title: "curl_multi_info_read(3)"
name: "curl_multi_info_read"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_info_read/"
description: "curl_multi_info_read – read multi stack informationals"
---

<h2>NAME</h2>
<p> curl_multi_info_read &#8211; read multi stack informationals</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;curl/curl.h&gt; </p>
<p> CURLMsg *curl_multi_info_read( CURLM *multi_handle,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>int&nbsp;<wbr>*msgs_in_queue);</p>
<h2>DESCRIPTION</h2>
<p> Ask the multi handle if there are any messages/informationals from the individual transfers. Messages may include informationals such as an error code from the transfer or just the fact that a transfer is completed. More details on these should be written down as well. </p>
<p> Repeated calls to this function will return a new struct each time, until a NULL is returned as a signal that there is no more to get at this point. The integer pointed to with <i>msgs_in_queue</i> will contain the number of remaining messages after this function was called. </p>
<p> When you fetch a message using this function, it is removed from the internal queue so calling this function again will not return the same message again. It will instead return new messages at each new invoke until the queue is emptied. </p>
<p> <code>WARNING:</code> The data the returned pointer points to will not survive calling <i><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a>(3)</i>, <i><a href="/docs/linux/man/3-curl_multi_remove_handle/">curl_multi_remove_handle</a>(3)</i> or <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i>. </p>
<p> The &#8216;CURLMsg&#8217; struct is very simple and only contains very basic information. If more involved information is wanted, the particular &quot;easy handle&quot; in present in that struct and can thus be used in subsequent regular <i><a href="/docs/linux/man/3-curl_easy_getinfo/">curl_easy_getinfo</a>(3)</i> calls (or similar): </p>
<pre><code>
struct CURLMsg {
    CURLMSG msg;       /* what this message means */
    CURL *easy_handle; /* the handle it concerns */
    union {
        void *whatever;  /* message-specific data */
        CURLcode result; /* return code for transfer */
    } data;
};
</code></pre>
<p> When <code>msg</code> is <i>CURLMSG_DONE</i>, the message identifies a transfer that is done, and then <code>result</code> contains the return code for the easy handle that just completed. </p>
<p> At this point, there are no other <code>msg</code> types defined.</p>
<h2>RETURN VALUE</h2>
<p> A pointer to a filled-in struct, or NULL if it failed or ran out of structs. It also writes the number of messages left in the queue (after this read) in the integer the second argument points to.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_multi_cleanup/">curl_multi_cleanup</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_init/">curl_multi_init</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a></code>(3) </p>
<h2>Index</h2>
