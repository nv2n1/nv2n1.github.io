---
title: "curlopt_mail_rcpt(3)"
name: "curlopt_mail_rcpt"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_mail_rcpt/"
description: "CURLOPT_MAIL_RCPT – list of SMTP mail recipients"
---

<p>CURLOPT_MAIL_RCPT &#8211; list of SMTP mail recipients</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_MAIL_RCPT,
 struct curl_slist *rcpts);</pre>
<h2>Description</h2>
<p>Pass a pointer to a linked list of recipients to pass to the server in your SMTP mail request. The linked list should be a fully valid list of <code>struct curl_slist</code> structs properly filled in. Use <i><a href="/docs/linux/man/3-curl_slist_append/">curl_slist_append</a>(3)</i> to create the list and <i><a href="/docs/linux/man/3-curl_slist_free_all/">curl_slist_free_all</a>(3)</i> to clean up an entire list. </p>
<p> When performing a mail transfer, each recipient should be specified within a pair of angled brackets (&lt;&gt;), however, should you not use an angled bracket as the first character libcurl will assume you provided a single email address and enclose that address within brackets for you. </p>
<p> When performing an address verification (VRFY command), each recipient should be specified as the user name or user name and domain (as per Section 3.5 of RFC5321). </p>
<p> When performing a mailing list expand (EXPN command), each recipient should be specified using the mailing list name, such as &quot;Friends&quot; or &quot;London-Office&quot;.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>SMTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.20.0. The VRFY and EXPN logic was added in 7.34.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_mail_from/">CURLOPT_MAIL_FROM</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_mail_auth/">CURLOPT_MAIL_AUTH</a></code>(3),</p>
