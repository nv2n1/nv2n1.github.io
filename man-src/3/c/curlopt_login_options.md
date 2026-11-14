---
title: "curlopt_login_options(3)"
name: "curlopt_login_options"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_login_options/"
description: "CURLOPT_LOGIN_OPTIONS – set login options"
---

<p>CURLOPT_LOGIN_OPTIONS &#8211; set login options</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_LOGIN_OPTIONS, char *options);</p>
<h2>Description</h2>
<p>Pass a char * as parameter, which should be pointing to the zero terminated <i>options</i> string to use for the transfer. </p>
<p> For more information about the login options please see RFC2384, RFC5092 and IETF draft draft-earhart-url-smtp-00.txt </p>
<p> <code><a href="/docs/linux/man/3-curlopt_login_options/">CURLOPT_LOGIN_OPTIONS</a>(3)</code> can be used to set protocol specific login options, such as the preferred authentication mechanism via &quot;AUTH=NTLM&quot; or &quot;AUTH=*&quot;, and should be used in conjunction with the <i><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a>(3)</i> option.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>Only IMAP, POP3 and SMTP support login options.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.34.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_password/">CURLOPT_PASSWORD</a></code>(3),</p>
