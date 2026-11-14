---
title: "curlopt_postquote(3)"
name: "curlopt_postquote"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_postquote/"
description: "CURLOPT_POSTQUOTE – (S)FTP commands to run after the transfer"
---

<p>CURLOPT_POSTQUOTE &#8211; (S)FTP commands to run after the transfer</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_POSTQUOTE, struct curl_slist *cmds);</p>
<h2>Description</h2>
<p>Pass a pointer to a linked list of FTP or SFTP commands to pass to the server after your FTP transfer request. The commands will only be run if no error occurred. The linked list should be a fully valid list of struct curl_slist structs properly filled in as described for <i><a href="/docs/linux/man/3-curlopt_quote/">CURLOPT_QUOTE</a>(3)</i>. </p>
<p> Disable this operation again by setting a NULL to this option.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>SFTP and FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If support for the protocols are built-in.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_quote/">CURLOPT_QUOTE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_prequote/">CURLOPT_PREQUOTE</a></code>(3),</p>
