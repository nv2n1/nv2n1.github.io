---
title: "curlopt_keypasswd(3)"
name: "curlopt_keypasswd"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_keypasswd/"
description: "CURLOPT_KEYPASSWD – set passphrase to private key"
---

<p>CURLOPT_KEYPASSWD &#8211; set passphrase to private key</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_KEYPASSWD, char *pwd);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. It will be used as the password required to use the <i><a href="/docs/linux/man/3-curlopt_sslkey/">CURLOPT_SSLKEY</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_ssh_private_keyfile/">CURLOPT_SSH_PRIVATE_KEYFILE</a>(3)</i> private key. You never needed a pass phrase to load a certificate but you need one to load your private key.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>This option was known as CURLOPT_SSLKEYPASSWD up to 7.16.4 and CURLOPT_SSLCERTPASSWD up to 7.9.2.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if TLS enabled, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sslkey/">CURLOPT_SSLKEY</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssh_private_keyfile/">CURLOPT_SSH_PRIVATE_KEYFILE</a></code>(3),</p>
