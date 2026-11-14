---
title: "curlopt_ssh_keydata(3)"
name: "curlopt_ssh_keydata"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssh_keydata/"
description: "CURLOPT_SSH_KEYDATA – pointer to pass to the SSH key callback"
---

<p>CURLOPT_SSH_KEYDATA &#8211; pointer to pass to the SSH key callback</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSH_KEYDATA, void *pointer);</p>
<h2>Description</h2>
<p>Pass a void * as parameter. This <i>pointer</i> will be passed along verbatim to the callback set with <i><a href="/docs/linux/man/3-curlopt_ssh_keyfunction/">CURLOPT_SSH_KEYFUNCTION</a>(3)</i>.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>SFTP and SCP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.19.6</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssh_keydata/">CURLOPT_SSH_KEYDATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssh_knownhosts/">CURLOPT_SSH_KNOWNHOSTS</a></code>(3),</p>
