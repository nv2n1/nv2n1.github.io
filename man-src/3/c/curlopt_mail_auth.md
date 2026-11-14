---
title: "curlopt_mail_auth(3)"
name: "curlopt_mail_auth"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_mail_auth/"
description: "CURLOPT_MAIL_AUTH – SMTP authentication address"
---

<p>CURLOPT_MAIL_AUTH &#8211; SMTP authentication address</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_MAIL_AUTH, char *auth);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. This will be used to specify the authentication address (identity) of a submitted message that is being relayed to another server. </p>
<p> This optional parameter allows co-operating agents in a trusted environment to communicate the authentication of individual messages and should only be used by the application program, using libcurl, if the application is itself a mail server acting in such an environment. If the application is operating as such and the AUTH address is not known or is invalid, then an empty string should be used for this parameter. </p>
<p> Unlike <i><a href="/docs/linux/man/3-curlopt_mail_from/">CURLOPT_MAIL_FROM</a>(3)</i> and <i><a href="/docs/linux/man/3-curlopt_mail_rcpt/">CURLOPT_MAIL_RCPT</a>(3)</i>, the address should not be specified within a pair of angled brackets (&lt;&gt;). However, if an empty string is used then a pair of brackets will be sent by libcurl as required by RFC2554.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>SMTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.25.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_mail_from/">CURLOPT_MAIL_FROM</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_mail_rcpt/">CURLOPT_MAIL_RCPT</a></code>(3),</p>
