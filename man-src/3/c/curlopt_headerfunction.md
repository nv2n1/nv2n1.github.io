---
title: "curlopt_headerfunction(3)"
name: "curlopt_headerfunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_headerfunction/"
description: "CURLOPT_HEADERFUNCTION – callback that receives header data"
---

<p>CURLOPT_HEADERFUNCTION &#8211; callback that receives header data</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> size_t header_callback(char *buffer,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>size_t size,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>size_t nitems,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>void&nbsp;<wbr>*userdata); </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HEADERFUNCTION, header_callback);</p>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This function gets called by libcurl as soon as it has received header data. The header callback will be called once for each header and only complete header lines are passed on to the callback. Parsing headers is very easy using this. The size of the data pointed to by <i>ptr</i> is <i>size</i> multiplied with <i>nmemb</i>. Do not assume that the header line is zero terminated! The pointer named <i>userdata</i> is the one you set with the <i><a href="/docs/linux/man/3-curlopt_headerdata/">CURLOPT_HEADERDATA</a>(3)</i> option. This callback function must return the number of bytes actually taken care of. If that amount differs from the amount passed in to your function, it&#8217;ll signal an error to the library. This will cause the transfer to get aborted and the libcurl function in progress will return <i>CURL_WRITE_ERROR</i>. </p>
<p> A complete HTTP header that is passed to this function can be up to <i>CURL_MAX_HTTP_HEADER</i> (100K) bytes. </p>
<p> If this option is not set, or if it is set to NULL, but <i><a href="/docs/linux/man/3-curlopt_headerdata/">CURLOPT_HEADERDATA</a>(3)</i> is set to anything but NULL, the function used to accept response data will be used instead. That is, it will be the function specified with <i><a href="/docs/linux/man/3-curlopt_writefunction/">CURLOPT_WRITEFUNCTION</a>(3)</i>, or if it is not specified or NULL &#8211; the default, stream-writing function. </p>
<p> It&#8217;s important to note that the callback will be invoked for the headers of all responses received after initiating a request and not just the final response. This includes all responses which occur during authentication negotiation. If you need to operate on only the headers from the final response, you will need to collect headers in the callback yourself and use HTTP status lines, for example, to delimit response boundaries. </p>
<p> When a server sends a chunked encoded transfer, it may contain a trailer. That trailer is identical to a HTTP header and if such a trailer is received it is passed to the application using this callback as well. There are several ways to detect it being a trailer and not an ordinary header: 1) it comes after the response-body. 2) it comes after the final header line (CR LF) 3) a Trailer: header among the regular response-headers mention what header(s) to expect in the trailer. </p>
<p> For non-HTTP protocols like FTP, POP3, IMAP and SMTP this function will get called with the server responses to the commands that libcurl sends.</p>
<h2>Default</h2>
<p>Nothing.</p>
<h2>Protocols</h2>
<p>Used for all protocols with headers or meta-data concept: HTTP, FTP, POP3, IMAP, SMTP and more.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_headerdata/">CURLOPT_HEADERDATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_writefunction/">CURLOPT_WRITEFUNCTION</a></code>(3),</p>
