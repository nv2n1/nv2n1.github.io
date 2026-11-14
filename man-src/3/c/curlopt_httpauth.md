---
title: "curlopt_httpauth(3)"
name: "curlopt_httpauth"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_httpauth/"
description: "CURLOPT_HTTPAUTH – set HTTP server authentication methods to try"
---

<p>CURLOPT_HTTPAUTH &#8211; set HTTP server authentication methods to try</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HTTPAUTH, long bitmask);</pre>
<h2>Description</h2>
<p>Pass a long as parameter, which is set to a bitmask, to tell libcurl which authentication method(s) you want it to use speaking to the remote server. </p>
<p> The available bits are listed below. If more than one bit is set, libcurl will first query the site to see which authentication methods it supports and then pick the best one you allow it to use. For some methods, this will induce an extra network round-trip. Set the actual name and password with the <i><a href="/docs/linux/man/3-curlopt_userpwd/">CURLOPT_USERPWD</a>(3)</i> option or with the <i><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a>(3)</i> and the <i><a href="/docs/linux/man/3-curlopt_password/">CURLOPT_PASSWORD</a>(3)</i> options. </p>
<p> For authentication with a proxy, see <i><a href="/docs/linux/man/3-curlopt_proxyauth/">CURLOPT_PROXYAUTH</a>(3)</i>. </p>
<dl COMPACT>
<dt>CURLAUTH_BASIC</p>
<dd>HTTP Basic authentication. This is the default choice, and the only method that is in wide-spread use and supported virtually everywhere. This sends the user name and password over the network in plain text, easily captured by others.</p>
<dt>CURLAUTH_DIGEST</p>
<dd>HTTP Digest authentication. Digest authentication is defined in RFC2617 and is a more secure way to do authentication over public networks than the regular old-fashioned Basic method.</p>
<dt>CURLAUTH_DIGEST_IE</p>
<dd>HTTP Digest authentication with an IE flavor. Digest authentication is defined in RFC2617 and is a more secure way to do authentication over public networks than the regular old-fashioned Basic method. The IE flavor is simply that libcurl will use a special &quot;quirk&quot; that IE is known to have used before version 7 and that some servers require the client to use.</p>
<dt>CURLAUTH_NEGOTIATE</p>
<dd>HTTP Negotiate (SPNEGO) authentication. Negotiate authentication is defined in RFC 4559 and is the most secure way to perform authentication over HTTP. </p>
<p> You need to build libcurl with a suitable GSS-API library or SSPI on Windows for this to work.</p>
<dt>CURLAUTH_NTLM</p>
<dd>HTTP NTLM authentication. A proprietary protocol invented and used by Microsoft. It uses a challenge-response and hash concept similar to Digest, to prevent the password from being eavesdropped. </p>
<p> You need to build libcurl with either OpenSSL, GnuTLS or NSS support for this option to work, or build libcurl on Windows with SSPI support.</p>
<dt>CURLAUTH_NTLM_WB</p>
<dd>NTLM delegating to winbind helper. Authentication is performed by a separate binary application that is executed when needed. The name of the application is specified at compile time but is typically /usr/bin/ntlm_auth </p>
<p> Note that libcurl will fork when necessary to run the winbind application and kill it when complete, calling waitpid() to await its exit when done. On POSIX operating systems, killing the process will cause a SIGCHLD signal to be raised (regardless of whether <i><a href="/docs/linux/man/3-curlopt_nosignal/">CURLOPT_NOSIGNAL</a>(3)</i> is set), which must be handled intelligently by the application. In particular, the application must not unconditionally call wait() in its SIGCHLD signal handler to avoid being subject to a race condition. This behavior is subject to change in future versions of libcurl.</p>
<dt>CURLAUTH_ANY</p>
<dd>This is a convenience macro that sets all bits and thus makes libcurl pick any it finds suitable. libcurl will automatically select the one it finds most secure.</p>
<dt>CURLAUTH_ANYSAFE</p>
<dd>This is a convenience macro that sets all bits except Basic and thus makes libcurl pick any it finds suitable. libcurl will automatically select the one it finds most secure.</p>
<dt>CURLAUTH_ONLY</p>
<dd>This is a meta symbol. OR this value together with a single specific auth value to force libcurl to probe for un-restricted auth and if not, only that single auth algorithm is acceptable.</dl>
<h2>Default</h2>
<p>CURLAUTH_BASIC</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Option Added in 7.10.6. </p>
<p> CURLAUTH_DIGEST_IE was added added in 7.19.3 </p>
<p> CURLAUTH_ONLY was added in 7.21.3 </p>
<p> CURLAUTH_NTLM_WB was added in 7.22.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_NOT_BUILT_IN if the bitmask specified no supported authentication methods.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_proxyauth/">CURLOPT_PROXYAUTH</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_userpwd/">CURLOPT_USERPWD</a></code>(3),</p>
