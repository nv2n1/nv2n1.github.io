---
title: "curlopt_ssl_ctx_function(3)"
name: "curlopt_ssl_ctx_function"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssl_ctx_function/"
description: "CURLOPT_SSL_CTX_FUNCTION – openssl specific callback to do SSL magic"
---

<p>CURLOPT_SSL_CTX_FUNCTION &#8211; openssl specific callback to do SSL magic</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode ssl_ctx_callback(CURL *curl, void *ssl_ctx, void *userptr);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSL_CTX_FUNCTION,
 ssl_ctx_callback);</pre>
<h2>Description</h2>
<p>This option only works for libcurl powered by OpenSSL. If libcurl was built against another SSL library, this functionality is absent. </p>
<p> Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This callback function gets called by libcurl just before the initialization of a SSL connection after having processed all other SSL related options to give a last chance to an application to modify the behaviour of openssl&#8217;s ssl initialization. The <i>sslctx</i> parameter is actually a pointer to an openssl <i>SSL_CTX</i>. If an error is returned from the callback, no attempt to establish a connection is made and the perform operation will return the error code. Set the <i>userptr</i> argument with the <i><a href="/docs/linux/man/3-curlopt_ssl_ctx_data/">CURLOPT_SSL_CTX_DATA</a>(3)</i> option. </p>
<p> This function will get called on all new connections made to a server, during the SSL negotiation. The SSL_CTX pointer will be a new one every time. </p>
<p> To use this properly, a non-trivial amount of knowledge of the openssl libraries is necessary. For example, using this function allows you to use openssl callbacks to add additional validation code for certificates, and even to change the actual URI of a HTTPS request (example used in the lib509 test case). See also the example section for a replacement of the key, certificate and trust file settings.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All TLS based protocols: HTTPS, FTPS, IMAPS, POP3, SMTPS etc.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.11.0. Only supported when built with OpenSSL.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssl_ctx_data/">CURLOPT_SSL_CTX_DATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssl_verifypeer/">CURLOPT_SSL_VERIFYPEER</a></code>(3),</p>
