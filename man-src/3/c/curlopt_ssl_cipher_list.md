---
title: "curlopt_ssl_cipher_list(3)"
name: "curlopt_ssl_cipher_list"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssl_cipher_list/"
description: "CURLOPT_SSL_CIPHER_LIST – specify ciphers to use for TLS"
---

<p>CURLOPT_SSL_CIPHER_LIST &#8211; specify ciphers to use for TLS</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSL_CIPHER_LIST, char *list);</p>
<h2>Description</h2>
<p>Pass a char *, pointing to a zero terminated string holding the list of ciphers to use for the SSL connection. The list must be syntactically correct, it consists of one or more cipher strings separated by colons. Commas or spaces are also acceptable separators but colons are normally used, !, &#8211; and + can be used as operators. </p>
<p> For OpenSSL and GnuTLS valid examples of cipher lists include &#8216;RC4-SHA&#8217;, &#8216;SHA1+DES&#8217;, &#8216;TLSv1&#8217; and &#8216;DEFAULT&#8217;. The default list is normally set when you compile OpenSSL. </p>
<p> You&#8217;ll find more details about cipher lists on this URL: </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://www.openssl.org/docs/apps/ciphers.html">http://www.openssl.org/docs/apps/ciphers.html</a> </p>
<p> For NSS, valid examples of cipher lists include &#8216;rsa_rc4_128_md5&#8217;, &#8216;rsa_aes_128_sha&#8217;, etc. With NSS you don&#8217;t add/remove ciphers. If one uses this option then all known ciphers are disabled and only those passed in are enabled. </p>
<p> You&#8217;ll find more details about the NSS cipher lists on this URL: </p>
<p>&nbsp;<wbr><a rel="nofollow" href="http://git.fedorahosted.org/cgit/mod_nss.git/plain/docs/mod_nss.html#Directives">http://git.fedorahosted.org/cgit/mod_nss.git/plain/docs/mod_nss.html#Directives</a></p>
<h2>Default</h2>
<p>NULL, use internal default</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>If built TLS enabled.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if TLS is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_sslversion/">CURLOPT_SSLVERSION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_use_ssl/">CURLOPT_USE_SSL</a></code>(3),</p>
