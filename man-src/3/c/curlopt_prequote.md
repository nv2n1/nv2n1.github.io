---
title: "curlopt_prequote(3)"
name: "curlopt_prequote"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_prequote/"
description: "CURLOPT_PREQUOTE – commands to run before FTP or SFTP transfer"
---

<p>CURLOPT_PREQUOTE &#8211; commands to run before FTP or SFTP transfer</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PREQUOTE, char *cmds);</p>
<h2>Description</h2>
<p>Pass a pointer to a linked list of FTP or SFTP commands to pass to the server after the transfer type is set. The linked list should be a fully valid list of struct curl_slist structs properly filled in as described for <i><a href="/docs/linux/man/3-curlopt_quote/">CURLOPT_QUOTE</a>(3)</i>. Disable this operation again by setting a NULL to this option.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>FTP and SFTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Along with the protocol support</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_quote/">CURLOPT_QUOTE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_postquote/">CURLOPT_POSTQUOTE</a></code>(3),</p>
