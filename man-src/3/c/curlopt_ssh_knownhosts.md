---
title: "curlopt_ssh_knownhosts(3)"
name: "curlopt_ssh_knownhosts"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssh_knownhosts/"
description: "CURLOPT_SSH_KNOWNHOSTS – file name holding the SSH known hosts"
---

<p>CURLOPT_SSH_KNOWNHOSTS &#8211; file name holding the SSH known hosts</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSH_KNOWNHOSTS, char *fname);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string holding the file name of the known_host file to use. The known_hosts file should use the OpenSSH file format as supported by libssh2. If this file is specified, libcurl will only accept connections with hosts that are known and present in that file, with a matching public key. Use <i><a href="/docs/linux/man/3-curlopt_ssh_keyfunction/">CURLOPT_SSH_KEYFUNCTION</a>(3)</i> to alter the default behavior on host and key (mis)matching.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>SFTP and SCP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.19.6</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssh_auth_types/">CURLOPT_SSH_AUTH_TYPES</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssh_host_public_key_md5/">CURLOPT_SSH_HOST_PUBLIC_KEY_MD5</a></code>(3),</p>
