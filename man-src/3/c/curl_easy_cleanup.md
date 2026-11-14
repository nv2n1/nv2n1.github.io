---
title: "curl_easy_cleanup(3)"
name: "curl_easy_cleanup"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_easy_cleanup/"
description: "curl_easy_cleanup – End a libcurl easy session"
---

<h2>NAME</h2>
<p> curl_easy_cleanup &#8211; End a libcurl easy session</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>void curl_easy_cleanup(CURL *</code><i>handle</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> This function must be the last function to call for an easy session. It is the opposite of the <i><a href="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a>(3)</i> function and must be called with the same <i>handle</i> as input that the curl_easy_init call returned. </p>
<p> This will effectively close all connections this handle has used and possibly has kept open until now. Don&#8217;t call this function if you intend to transfer more files. </p>
<p> Occasionally you may get your progress callback or header callback called from within <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> (if previously set for the handle using <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i>). Like if libcurl decides to shut down the connection and the protocol is of a kind that requires a command/response sequence before disconnect. Examples of such protocols are FTP, POP3 and IMAP. </p>
<p> Any uses of the <code>handle</code> after this function has been called and have returned, are illegal. This kills the handle and all memory associated with it! </p>
<p> With libcurl versions prior to 7.17.: when you&#8217;ve called this, you can safely remove all the strings you&#8217;ve previously told libcurl to use, as it won&#8217;t use them anymore now.</p>
<h2>RETURN VALUE</h2>
<p> None</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a></code>(3), </p>
<h2>Index</h2>
