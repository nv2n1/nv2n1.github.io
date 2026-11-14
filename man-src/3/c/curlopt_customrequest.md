---
title: "curlopt_customrequest(3)"
name: "curlopt_customrequest"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_customrequest/"
description: "CURLOPT_CUSTOMREQUEST – custom string for request"
---

<p>CURLOPT_CUSTOMREQUEST &#8211; custom string for request</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CUSTOMREQUEST, char *request);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. </p>
<p> When you change the request method by setting <code><a href="/docs/linux/man/3-curlopt_customrequest/">CURLOPT_CUSTOMREQUEST</a>(3)</code> to something, you don&#8217;t actually change how libcurl behaves or acts in regards to the particular request method, it will only change the actual string sent in the request. </p>
<p> Restore to the internal default by setting this to NULL. </p>
<p> This option can be used to specify the request:</p>
<dl COMPACT>
<dt>HTTP</p>
<dd>Instead of GET or HEAD when performing HTTP based requests. This is particularly useful, for example, for performing a HTTP DELETE request. </p>
<p> For example: </p>
<p> When you tell libcurl to do a HEAD request, but then specify a GET though a custom request libcurl will still act as if it sent a HEAD. To switch to a proper HEAD use <i><a href="/docs/linux/man/3-curlopt_nobody/">CURLOPT_NOBODY</a>(3)</i>, to switch to a proper POST use <i><a href="/docs/linux/man/3-curlopt_post/">CURLOPT_POST</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a>(3)</i> and to switch to a proper GET use <i><a href="/docs/linux/man/3-curlopt_httpget/">CURLOPT_HTTPGET</a>(3)</i>. </p>
<p> Many people have wrongly used this option to replace the entire request with their own, including multiple headers and POST contents. While that might work in many cases, it will cause libcurl to send invalid requests and it could possibly confuse the remote server badly. Use <i><a href="/docs/linux/man/3-curlopt_post/">CURLOPT_POST</a>(3)</i> and <i><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a>(3)</i> to set POST data. Use <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i> to replace or extend the set of headers sent by libcurl. Use <i><a href="/docs/linux/man/3-curlopt_http_version/">CURLOPT_HTTP_VERSION</a>(3)</i> to change HTTP version. </p>
<dt>FTP</p>
<dd>Instead of LIST and NLST when performing FTP directory listings.</p>
<dt>IMAP</p>
<dd>Instead of LIST when issuing IMAP based requests.</p>
<dt>POP3</p>
<dd>Instead of LIST and RETR when issuing POP3 based requests. </p>
<p> For example: </p>
<p> When you tell libcurl to use a custom request it will behave like a LIST or RETR command was sent where it expects data to be returned by the server. As such <i><a href="/docs/linux/man/3-curlopt_nobody/">CURLOPT_NOBODY</a>(3)</i> should be used when specifying commands such as DELE and NOOP for example.</p>
<dt>SMTP</p>
<dd>Instead of a HELP or VRFY when issuing SMTP based requests. </p>
<p> For example: </p>
<p> Normally a multiline response is returned which can be used, in conjunction with <i><a href="/docs/linux/man/3-curlopt_mail_rcpt/">CURLOPT_MAIL_RCPT</a>(3)</i>, to specify an EXPN request. If the <i><a href="/docs/linux/man/3-curlopt_nobody/">CURLOPT_NOBODY</a>(3)</i> option is specified then the request can be used to issue NOOP and RSET commands.</dl>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP, FTP, IMAP, POP3 and SMTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>IMAP is supported since 7.30.0, POP3 since 7.26.0 and SMTP since 7.34.0.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_nobody/">CURLOPT_NOBODY</a></code>(3),</p>
