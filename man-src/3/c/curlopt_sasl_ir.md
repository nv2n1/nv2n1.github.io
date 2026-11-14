---
title: "curlopt_sasl_ir(3)"
name: "curlopt_sasl_ir"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_sasl_ir/"
description: "CURLOPT_SASL_IR – enable sending initial response in first packet"
---

<p>CURLOPT_SASL_IR &#8211; enable sending initial response in first packet</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SASL_IR, long enable);</p>
<h2>Description</h2>
<p>Pass a long. If the value is 1, curl will send the initial response to the server in the first authentication packet in order to reduce the number of ping pong requests. Only applicable to the following supporting SASL authentication mechanisms: </p>
<p> * Login * Plain * GSSAPI * NTLM * OAuth 2.0 </p>
<p> Note: Whilst IMAP supports this option there is no need to explicitly set it, as libcurl can determine the feature itself when the server supports the SASL-IR CAPABILITY.</p>
<h2>Default</h2>
<p>0</p>
<h2>Protocols</h2>
<p>IMAP, POP3 and SMTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.31.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_mail_auth/">CURLOPT_MAIL_AUTH</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_mail_from/">CURLOPT_MAIL_FROM</a></code>(3),</p>
