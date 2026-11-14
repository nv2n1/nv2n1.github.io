---
title: "curlopt_ssh_private_keyfile(3)"
name: "curlopt_ssh_private_keyfile"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssh_private_keyfile/"
description: "CURLOPT_SSH_PRIVATE_KEYFILE – set private key file for SSH auth"
---

<p>CURLOPT_SSH_PRIVATE_KEYFILE &#8211; set private key file for SSH auth</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSH_PRIVATE_KEYFILE,
 char *filename);</pre>
<h2>Description</h2>
<p>Pass a char * pointing to a <i>filename</i> for your private key. If not used, libcurl defaults to <code>$HOME/.ssh/id_dsa</code> if the HOME environment variable is set, and just &quot;id_dsa&quot; in the current directory if HOME is not set. </p>
<p> If the file is password-protected, set the password with <i><a href="/docs/linux/man/3-curlopt_keypasswd/">CURLOPT_KEYPASSWD</a>(3)</i>.</p>
<h2>Default</h2>
<p>As explained above</p>
<h2>Protocols</h2>
<p>SFTP and SCP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.16.1</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssh_public_keyfile/">CURLOPT_SSH_PUBLIC_KEYFILE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssh_auth_types/">CURLOPT_SSH_AUTH_TYPES</a></code>(3),</p>
