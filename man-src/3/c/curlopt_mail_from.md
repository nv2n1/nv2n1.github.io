---
title: "curlopt_mail_from(3)"
name: "curlopt_mail_from"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_mail_from/"
description: "CURLOPT_MAIL_FROM – SMTP sender address"
---

<p>CURLOPT_MAIL_FROM &#8211; SMTP sender address</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_MAIL_FROM, char *from);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. This should be used to specify the sender&#8217;s email address when sending SMTP mail with libcurl. </p>
<p> An originator email address should be specified with angled brackets (&lt;&gt;) around it, which if not specified will be added automatically. </p>
<p> If this parameter is not specified then an empty address will be sent to the mail server which may cause the email to be rejected.</p>
<h2>Default</h2>
<p>blank</p>
<h2>Protocols</h2>
<p>SMTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.20.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_mail_rcpt/">CURLOPT_MAIL_RCPT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_mail_auth/">CURLOPT_MAIL_AUTH</a></code>(3),</p>
