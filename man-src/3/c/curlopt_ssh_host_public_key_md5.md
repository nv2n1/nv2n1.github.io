---
title: "curlopt_ssh_host_public_key_md5(3)"
name: "curlopt_ssh_host_public_key_md5"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssh_host_public_key_md5/"
description: "CURLOPT_SSH_HOST_PUBLIC_KEY_MD5 – checksum of SSH server public key"
---

<p>CURLOPT_SSH_HOST_PUBLIC_KEY_MD5 &#8211; checksum of SSH server public key</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSH_HOST_PUBLIC_KEY_MD5,
 char *md5);</pre>
<h2>Description</h2>
<p>Pass a char * pointing to a string containing 32 hexadecimal digits. The string should be the 128 bit MD5 checksum of the remote host&#8217;s public key, and libcurl will reject the connection to the host unless the md5sums match.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>SCP and SFTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.17.1</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssh_public_keyfile/">CURLOPT_SSH_PUBLIC_KEYFILE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssh_auth_types/">CURLOPT_SSH_AUTH_TYPES</a></code>(3),</p>
