---
title: "curlopt_xoauth2_bearer(3)"
name: "curlopt_xoauth2_bearer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_xoauth2_bearer/"
description: "CURLOPT_XOAUTH2_BEARER – specify OAuth 2.0 access token"
---

<p>CURLOPT_XOAUTH2_BEARER &#8211; specify OAuth 2.0 access token</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_XOAUTH2_BEARER, char *token);</p>
<h2>Description</h2>
<p>Pass a char * as parameter, which should point to the zero terminated OAuth 2.0 Bearer Access Token for use with IMAP, POP3 and SMTP servers that support the OAuth 2.0 Authorization Framework. </p>
<p> Note: The user name used to generate the Bearer Token should be supplied via the <i><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a>(3)</i> option.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>IMAP, POP3 and SMTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.33.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_mail_auth/">CURLOPT_MAIL_AUTH</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a></code>(3),</p>
