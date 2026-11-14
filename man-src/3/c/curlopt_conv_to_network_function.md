---
title: "curlopt_conv_to_network_function(3)"
name: "curlopt_conv_to_network_function"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_conv_to_network_function/"
description: "CURLOPT_CONV_TO_NETWORK_FUNCTION – convert data to network from host encoding"
---

<p>CURLOPT_CONV_TO_NETWORK_FUNCTION &#8211; convert data to network from host encoding</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode conv_callback(char *ptr, size_t length);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_CONV_TO_NETWORK_FUNCTION,
 conv_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> Applies to non-ASCII platforms. <i><a href="/docs/linux/man/3-curl_version_info/">curl_version_info</a>(3)</i> will return the CURL_VERSION_CONV feature bit set if this option is provided. </p>
<p> The data to be converted is in a buffer pointed to by the <i>ptr</i> parameter. The amount of data to convert is indicated by the <i>length</i> parameter. The converted data overlays the input data in the buffer pointed to by the ptr parameter. <i>CURLE_OK</i> must be returned upon successful conversion. A CURLcode return value defined by curl.h, such as <i>CURLE_CONV_FAILED</i>, should be returned if an error was encountered. </p>
<p> <code>CURLOPT_CONV_TO_NETWORK_FUNCTION</code> converts from host encoding to the network encoding. It is used when commands or ASCII data are sent over the network. </p>
<p> If you set a callback pointer to NULL, or don&#8217;t set it at all, the built-in libcurl iconv functions will be used. If HAVE_ICONV was not defined when libcurl was built, and no callback has been established, conversion will return the CURLE_CONV_REQD error code. </p>
<p> If HAVE_ICONV is defined, CURL_ICONV_CODESET_OF_HOST must also be defined. For example: </p>
<p>&nbsp;<wbr>#define CURL_ICONV_CODESET_OF_HOST&nbsp;<wbr>&quot;IBM-1047&quot; </p>
<p> The iconv code in libcurl will default the network and UTF8 codeset names as follows: </p>
<p>&nbsp;<wbr>#define CURL_ICONV_CODESET_OF_NETWORK&nbsp;<wbr>&quot;ISO8859-1&quot; </p>
<p>&nbsp;<wbr>#define CURL_ICONV_CODESET_FOR_UTF8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;UTF-8&quot; </p>
<p> You will need to override these definitions if they are different on your system.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>FTP, SMTP, IMAP, POP3</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Available only if <code>CURL_DOES_CONVERSIONS</code> was defined when libcurl was built.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_conv_from_network_function/">CURLOPT_CONV_FROM_NETWORK_FUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_conv_to_utf8_function/">CURLOPT_CONV_TO_UTF8_FUNCTION</a></code>(3),</p>
