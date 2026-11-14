---
title: "curlopt_ssh_auth_types(3)"
name: "curlopt_ssh_auth_types"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssh_auth_types/"
description: "CURLOPT_SSH_AUTH_TYPES – set desired auth types for SFTP and SCP"
---

<p>CURLOPT_SSH_AUTH_TYPES &#8211; set desired auth types for SFTP and SCP</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSH_AUTH_TYPES, long bitmask);</p>
<h2>Description</h2>
<p>Pass a long set to a bitmask consisting of one or more of CURLSSH_AUTH_PUBLICKEY, CURLSSH_AUTH_PASSWORD, CURLSSH_AUTH_HOST, CURLSSH_AUTH_KEYBOARD and CURLSSH_AUTH_AGENT. </p>
<p> Set <i>CURLSSH_AUTH_ANY</i> to let libcurl pick a suitable one. Currently CURLSSH_AUTH_HOST has no effect. If CURLSSH_AUTH_AGENT is used, libcurl attempts to connect to ssh-agent or pageant and let the agent attempt the authentication.</p>
<h2>Default</h2>
<p>None</p>
<h2>Protocols</h2>
<p>SFTP and SCP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>CURLSSH_AUTH_HOST was added in 7.16.1, CURLSSH_AUTH_AGENT was added in 7.28.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssh_host_public_key_md5/">CURLOPT_SSH_HOST_PUBLIC_KEY_MD5</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssh_public_keyfile/">CURLOPT_SSH_PUBLIC_KEYFILE</a></code>(3),</p>
