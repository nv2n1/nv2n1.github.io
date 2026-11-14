---
title: "curl_multi_assign(3)"
name: "curl_multi_assign"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_multi_assign/"
description: "curl_multi_assign – set data to association with an internal socket"
---

<h2>NAME</h2>
<p> curl_multi_assign &#8211; set data to association with an internal socket</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_assign(CURLM *multi_handle, curl_socket_t sockfd,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>void&nbsp;<wbr>*sockptr);</p>
<h2>DESCRIPTION</h2>
<p> This function assigns an association in the multi handle between the given socket and a private pointer of the application. This is (only) useful for <i><a href="/docs/linux/man/3-curl_multi_socket/">curl_multi_socket</a>(3)</i> uses. </p>
<p> When set, the <i>sockptr</i> pointer will be passed to all future socket callbacks for the specific <i>sockfd</i> socket. </p>
<p> If the given <i>sockfd</i> isn&#8217;t already in use by libcurl, this function will return an error. </p>
<p> libcurl only keeps one single pointer associated with a socket, so calling this function several times for the same socket will make the last set pointer get used. </p>
<p> The idea here being that this association (socket to private pointer) is something that just about every application that uses this API will need and then libcurl can just as well do it since it already has an internal hash table lookup for this.</p>
<h2>RETURN VALUE</h2>
<p> The standard CURLMcode for multi interface error codes.</p>
<h2>TYPICAL USAGE</h2>
<p> In a typical application you allocate a struct or at least use some kind of semi-dynamic data for each socket that we must wait for action on when using the <i><a href="/docs/linux/man/3-curl_multi_socket/">curl_multi_socket</a>(3)</i> approach. </p>
<p> When our socket-callback gets called by libcurl and we get to know about yet another socket to wait for, we can use <i><a href="/docs/linux/man/3-curl_multi_assign/">curl_multi_assign</a>(3)</i> to point out the particular data so that when we get updates about this same socket again, we don&#8217;t have to find the struct associated with this socket by ourselves.</p>
<h2>AVAILABILITY</h2>
<p> This function was added in libcurl 7.15.5, although not deemed stable yet.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_multi_setopt/">curl_multi_setopt</a></code>(3), <code><a href="/docs/linux/man/3-curl_multi_socket/">curl_multi_socket</a></code>(3) </p>
<h2>Index</h2>
