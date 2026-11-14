---
title: "curl_easy_setopt(3)"
name: "curl_easy_setopt"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_easy_setopt/"
description: "curl_easy_setopt – set options for a curl easy handle"
---

<h2>NAME</h2>
<p> curl_easy_setopt &#8211; set options for a curl easy handle</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLoption option, parameter);</p>
<h2>DESCRIPTION</h2>
<p> curl_easy_setopt() is used to tell libcurl how to behave. By using the appropriate options to <i>curl_easy_setopt</i>, you can change libcurl&#8217;s behavior. All options are set with the <i>option</i> followed by a <i>parameter</i>. That parameter can be a <code>long</code>, a <code>function pointer</code>, an <code>object pointer</code> or a <code>curl_off_t</code>, depending on what the specific option expects. Read this manual carefully as bad input values may cause libcurl to behave badly! You can only set one option in each function call. A typical application uses many curl_easy_setopt() calls in the setup phase. </p>
<p> Options set with this function call are valid for all forthcoming transfers performed using this <i>handle</i>. The options are not in any way reset between transfers, so if you want subsequent transfers with different options, you must change them between the transfers. You can optionally reset all options back to internal default with <i><a href="/docs/linux/man/3-curl_easy_reset/">curl_easy_reset</a>(3)</i>. </p>
<p> Strings passed to libcurl as &#8216;char *&#8217; arguments, are copied by the library; thus the string storage associated to the pointer argument may be overwritten after curl_easy_setopt() returns. Exceptions to this rule are described in the option details below. </p>
<p> Before version 7.17.0, strings were not copied. Instead the user was forced keep them available until libcurl no longer needed them. </p>
<p> The <i>handle</i> is the return code from a <i><a href="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a>(3)</i> or <i><a href="/docs/linux/man/3-curl_easy_duphandle/">curl_easy_duphandle</a>(3)</i> call.</p>
<h2>BEHAVIOR OPTIONS</h2>
<dl>
<dt>CURLOPT_VERBOSE</p>
<dd> Set the parameter to 1 to get the library to display a lot of verbose information about its operations. Very useful for libcurl and/or protocol debugging and understanding. The verbose information will be sent to stderr, or the stream set with <i>CURLOPT_STDERR</i>. </p>
<p> You hardly ever want this set in production use, you will almost always want this when you debug/report problems. Another neat option for debugging is the <i>CURLOPT_DEBUGFUNCTION</i>.</p>
<dt>CURLOPT_HEADER</p>
<dd> A parameter set to 1 tells the library to include the header in the body output. This is only relevant for protocols that actually have headers preceding the data (like HTTP).</p>
<dt>CURLOPT_NOPROGRESS</p>
<dd> Pass a long. If set to 1, it tells the library to shut off the progress meter completely. It will also prevent the <i>CURLOPT_PROGRESSFUNCTION</i> from getting called. </p>
<p> Future versions of libcurl are likely to not have any built-in progress meter at all.</p>
<dt>CURLOPT_NOSIGNAL</p>
<dd> Pass a long. If it is 1, libcurl will not use any functions that install signal handlers or any functions that cause signals to be sent to the process. This option is mainly here to allow multi-threaded unix applications to still set/use all timeout options etc, without risking getting signals. (Added in 7.10) </p>
<p> If this option is set and libcurl has been built with the standard name resolver, timeouts will not occur while the name resolve takes place. Consider building libcurl with c-ares support to enable asynchronous DNS lookups, which enables nice timeouts for name resolves without signals. </p>
<p> Setting <i>CURLOPT_NOSIGNAL</i> to 1 makes libcurl NOT ask the system to ignore SIGPIPE signals, which otherwise are sent by the system when trying to send data to a socket which is closed in the other end. libcurl makes an effort to never cause such SIGPIPEs to trigger, but some operating systems have no way to avoid them and even on those that have there are some corner cases when they may still happen, contrary to our desire. In addition, using <i>CURLAUTH_NTLM_WB</i> authentication could cause a SIGCHLD signal to be raised.</p>
<dt>CURLOPT_WILDCARDMATCH</p>
<dd> Set this option to 1 if you want to transfer multiple files according to a file name pattern. The pattern can be specified as part of the <i>CURLOPT_URL</i> option, using an fnmatch-like pattern (Shell Pattern Matching) in the last part of URL (file name). </p>
<p> By default, libcurl uses its internal wildcard matching implementation. You can provide your own matching function by the <i>CURLOPT_FNMATCH_FUNCTION</i> option. </p>
<p> This feature is only supported by the FTP download for now. </p>
<p> A brief introduction of its syntax follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>* &#8211; ASTERISK</p>
<dd> <a href="ftp://example.com/some/path/">ftp://example.com/some/path/</a><code>*.txt</code> (for all txt&#8217;s from the root directory)</dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>? &#8211; QUESTION MARK</p>
<dd> Question mark matches any (exactly one) character. </p>
<p> <a href="ftp://example.com/some/path/">ftp://example.com/some/path/</a><code>photo?.jpeg</code></dl>
</dl>
<dl>
<dt>
<dd>
<dl>
<dt>[ &#8211; BRACKET EXPRESSION</p>
<dd> The left bracket opens a bracket expression. The question mark and asterisk have no special meaning in a bracket expression. Each bracket expression ends by the right bracket and matches exactly one character. Some examples follow: </p>
<p> <code>[a-zA-Z0-9]</code> or <code>[f-gF-G]</code> &#8211; character interval </p>
<p> <code>[abc]</code> &#8211; character enumeration </p>
<p> <code>[^abc]</code> or <code>[!abc]</code> &#8211; negation </p>
<p> <code>[[:</code><i>name</i><code>:]]</code> class expression. Supported classes are <code>alnum</code>,<code>lower</code>, <code>space</code>, <code>alpha</code>, <code>digit</code>, <code>print</code>, <code>upper</code>, <code>blank</code>, <code>graph</code>, <code>xdigit</code>. </p>
<p> <code>[][-!^]</code> &#8211; special case &#8211; matches only &#8216;-&#8216;, &#8216;]&#8217;, &#8216;[&#8216;, &#8216;!&#8217; or &#8216;^&#8217;. These characters have no special purpose. </p>
<p> <code>[\[\]\]</code> &#8211; escape syntax. Matches &#8216;[&#8216;, &#8216;]&#8217; or &#8216;\&#8217;. </p>
<p> Using the rules above, a file name pattern can be constructed: </p>
<p> <a href="ftp://example.com/some/path/">ftp://example.com/some/path/</a><code>[a-z[:upper:]\].jpeg</code></dl>
</dl>
</dl>
<p> (This was added in 7.21.0)</p>
<h2>CALLBACK OPTIONS</h2>
<dl>
<dt>CURLOPT_WRITEFUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>size_t function( char *ptr, size_t size, size_t nmemb, void *userdata);</code> This function gets called by libcurl as soon as there is data received that needs to be saved. The size of the data pointed to by <i>ptr</i> is <i>size</i> multiplied with <i>nmemb</i>, it will not be zero terminated. Return the number of bytes actually taken care of. If that amount differs from the amount passed to your function, it&#8217;ll signal an error to the library. This will abort the transfer and return <i>CURLE_WRITE_ERROR</i>. </p>
<p> From 7.18.0, the function can return CURL_WRITEFUNC_PAUSE which then will cause writing to this connection to become paused. See <i><a href="/docs/linux/man/3-curl_easy_pause/">curl_easy_pause</a>(3)</i> for further details. </p>
<p> This function may be called with zero bytes data if the transferred file is empty. </p>
<p> Set this option to NULL to get the internal default function. The internal default function will write the data to the FILE * given with <i>CURLOPT_WRITEDATA</i>. </p>
<p> Set the <i>userdata</i> argument with the <i>CURLOPT_WRITEDATA</i> option. </p>
<p> The callback function will be passed as much data as possible in all invokes, but you cannot possibly make any assumptions. It may be one byte, it may be thousands. The maximum amount of body data that can be passed to the write callback is defined in the curl.h header file: CURL_MAX_WRITE_SIZE (the usual default is 16K). If you however have <i>CURLOPT_HEADER</i> set, which sends header data to the write callback, you can get up to <i>CURL_MAX_HTTP_HEADER</i> bytes of header data passed into it. This usually means 100K.</p>
<dt>CURLOPT_WRITEDATA</p>
<dd> Data pointer to pass to the file write function. If you use the <i>CURLOPT_WRITEFUNCTION</i> option, this is the pointer you&#8217;ll get as input. If you don&#8217;t use a callback, you must pass a &#8216;FILE *&#8217; as libcurl will pass this to fwrite() when writing data. </p>
<p> The internal <i>CURLOPT_WRITEFUNCTION</i> will write the data to the FILE * given with this option, or to stdout if this option hasn&#8217;t been set. </p>
<p> If you&#8217;re using libcurl as a win32 DLL, you <code>MUST</code> use the <i>CURLOPT_WRITEFUNCTION</i> if you set this option or you will experience crashes. </p>
<p> This option is also known with the older name <i>CURLOPT_FILE</i>, the name <i>CURLOPT_WRITEDATA</i> was introduced in 7.9.7.</p>
<dt>CURLOPT_READFUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>size_t function( void *ptr, size_t size, size_t nmemb, void *userdata);</code> This function gets called by libcurl as soon as it needs to read data in order to send it to the peer. The data area pointed at by the pointer <i>ptr</i> may be filled with at most <i>size</i> multiplied with <i>nmemb</i> number of bytes. Your function must return the actual number of bytes that you stored in that memory area. Returning 0 will signal end-of-file to the library and cause it to stop the current transfer. </p>
<p> If you stop the current transfer by returning 0 &quot;pre-maturely&quot; (i.e before the server expected it, like when you&#8217;ve said you will upload N bytes and you upload less than N bytes), you may experience that the server &quot;hangs&quot; waiting for the rest of the data that won&#8217;t come. </p>
<p> The read callback may return <i>CURL_READFUNC_ABORT</i> to stop the current operation immediately, resulting in a <i>CURLE_ABORTED_BY_CALLBACK</i> error code from the transfer (Added in 7.12.1) </p>
<p> From 7.18.0, the function can return CURL_READFUNC_PAUSE which then will cause reading from this connection to become paused. See <i><a href="/docs/linux/man/3-curl_easy_pause/">curl_easy_pause</a>(3)</i> for further details. </p>
<p> <code>Bugs</code>: when doing TFTP uploads, you must return the exact amount of data that the callback wants, or it will be considered the final packet by the server end and the transfer will end there. </p>
<p> If you set this callback pointer to NULL, or don&#8217;t set it at all, the default internal read function will be used. It is doing an fread() on the FILE * userdata set with <i>CURLOPT_READDATA</i>.</p>
<dt>CURLOPT_READDATA</p>
<dd> Data pointer to pass to the file read function. If you use the <i>CURLOPT_READFUNCTION</i> option, this is the pointer you&#8217;ll get as input. If you don&#8217;t specify a read callback but instead rely on the default internal read function, this data must be a valid readable FILE *. </p>
<p> If you&#8217;re using libcurl as a win32 DLL, you MUST use a <i>CURLOPT_READFUNCTION</i> if you set this option. </p>
<p> This option was also known by the older name <i>CURLOPT_INFILE</i>, the name <i>CURLOPT_READDATA</i> was introduced in 7.9.7.</p>
<dt>CURLOPT_IOCTLFUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>curlioerr function(CURL *handle, int cmd, void *clientp);</code>. This function gets called by libcurl when something special I/O-related needs to be done that the library can&#8217;t do by itself. For now, rewinding the read data stream is the only action it can request. The rewinding of the read data stream may be necessary when doing a HTTP PUT or POST with a multi-pass authentication method. (Option added in 7.12.3). </p>
<p> Use <i>CURLOPT_SEEKFUNCTION</i> instead to provide seeking!</p>
<dt>CURLOPT_IOCTLDATA</p>
<dd> Pass a pointer that will be untouched by libcurl and passed as the 3rd argument in the ioctl callback set with <i>CURLOPT_IOCTLFUNCTION</i>. (Option added in 7.12.3)</p>
<dt>CURLOPT_SEEKFUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>int function(void *instream, curl_off_t offset, int origin);</code> This function gets called by libcurl to seek to a certain position in the input stream and can be used to fast forward a file in a resumed upload (instead of reading all uploaded bytes with the normal read function/callback). It is also called to rewind a stream when doing a HTTP PUT or POST with a multi-pass authentication method. The function shall work like &quot;fseek&quot; or &quot;lseek&quot; and accepted SEEK_SET, SEEK_CUR and SEEK_END as argument for origin, although (in 7.18.0) libcurl only passes SEEK_SET. The callback must return 0 (CURL_SEEKFUNC_OK) on success, 1 (CURL_SEEKFUNC_FAIL) to cause the upload operation to fail or 2 (CURL_SEEKFUNC_CANTSEEK) to indicate that while the seek failed, libcurl is free to work around the problem if possible. The latter can sometimes be done by instead reading from the input or similar. </p>
<p> If you forward the input arguments directly to &quot;fseek&quot; or &quot;lseek&quot;, note that the data type for <i>offset</i> is not the same as defined for curl_off_t on many systems! (Option added in 7.18.0)</p>
<dt>CURLOPT_SEEKDATA</p>
<dd> Data pointer to pass to the file seek function. If you use the <i>CURLOPT_SEEKFUNCTION</i> option, this is the pointer you&#8217;ll get as input. If you don&#8217;t specify a seek callback, NULL is passed. (Option added in 7.18.0)</p>
<dt>CURLOPT_SOCKOPTFUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>int function(void *clientp, curl_socket_t curlfd, curlsocktype purpose);</code>. This function gets called by libcurl after the socket() call but before the connect() call. The callback&#8217;s <i>purpose</i> argument identifies the exact purpose for this particular socket: </p>
<p> <i>CURLSOCKTYPE_IPCXN</i> for actively created connections or since 7.28.0 <i>CURLSOCKTYPE_ACCEPT</i> for FTP when the connection was setup with PORT/EPSV (in earlier versions these sockets weren&#8217;t passed to this callback). </p>
<p> Future versions of libcurl may support more purposes. It passes the newly created socket descriptor so additional setsockopt() calls can be done at the user&#8217;s discretion. Return 0 (zero) from the callback on success. Return 1 from the callback function to signal an unrecoverable error to the library and it will close the socket and return <i>CURLE_COULDNT_CONNECT</i>. (Option added in 7.16.0) </p>
<p> Added in 7.21.5, the callback function may return <i>CURL_SOCKOPT_ALREADY_CONNECTED</i>, which tells libcurl that the socket is in fact already connected and then libcurl will not attempt to connect it.</p>
<dt>CURLOPT_SOCKOPTDATA</p>
<dd> Pass a pointer that will be untouched by libcurl and passed as the first argument in the sockopt callback set with <i>CURLOPT_SOCKOPTFUNCTION</i>. (Option added in 7.16.0)</p>
<dt>CURLOPT_OPENSOCKETFUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>curl_socket_t function(void *clientp, curlsocktype purpose, struct curl_sockaddr *address);</code>. This function gets called by libcurl instead of the <i><a href="/docs/linux/man/2-socket/">socket</a>(2)</i> call. The callback&#8217;s <i>purpose</i> argument identifies the exact purpose for this particular socket: <i>CURLSOCKTYPE_IPCXN</i> is for IP based connections. Future versions of libcurl may support more purposes. It passes the resolved peer address as a <i>address</i> argument so the callback can modify the address or refuse to connect at all. The callback function should return the socket or <i>CURL_SOCKET_BAD</i> in case no connection could be established or another error was detected. Any additional <i><a href="/docs/linux/man/2-setsockopt/">setsockopt</a>(2)</i> calls can be done on the socket at the user&#8217;s discretion. <i>CURL_SOCKET_BAD</i> return value from the callback function will signal an unrecoverable error to the library and it will return <i>CURLE_COULDNT_CONNECT</i>. This return code can be used for IP address blacklisting. The default behavior is: </p>
<pre><code>
return socket(addr-&gt;family, addr-&gt;socktype, addr-&gt;protocol);
</code></pre>
<p> (Option added in 7.17.1.)</p>
<dt>CURLOPT_OPENSOCKETDATA</p>
<dd> Pass a pointer that will be untouched by libcurl and passed as the first argument in the opensocket callback set with <i>CURLOPT_OPENSOCKETFUNCTION</i>. (Option added in 7.17.1.)</p>
<dt>CURLOPT_CLOSESOCKETFUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>int function(void *clientp, curl_socket_t item);</code>. This function gets called by libcurl instead of the <i><a href="/docs/linux/man/3-close/">close</a>(3)</i> or <i><a href="/docs/linux/man/3-closesocket/">closesocket</a>(3)</i> call when sockets are closed (not for any other file descriptors). This is pretty much the reverse to the <i>CURLOPT_OPENSOCKETFUNCTION</i> option. Return 0 to signal success and 1 if there was an error. (Option added in 7.21.7)</p>
<dt>CURLOPT_CLOSESOCKETDATA</p>
<dd> Pass a pointer that will be untouched by libcurl and passed as the first argument in the closesocket callback set with <i>CURLOPT_CLOSESOCKETFUNCTION</i>. (Option added in 7.21.7)</p>
<dt>CURLOPT_PROGRESSFUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>int function(void *clientp, double dltotal, double dlnow, double ultotal, double ulnow); </code>. This function gets called by libcurl instead of its internal equivalent with a frequent interval during operation (roughly once per second or sooner) no matter if data is being transferred or not. Unknown/unused argument values passed to the callback will be set to zero (like if you only download data, the upload size will remain 0). Returning a non-zero value from this callback will cause libcurl to abort the transfer and return <i>CURLE_ABORTED_BY_CALLBACK</i>. </p>
<p> If you transfer data with the multi interface, this function will not be called during periods of idleness unless you call the appropriate libcurl function that performs transfers. </p>
<p> <i>CURLOPT_NOPROGRESS</i> must be set to 0 to make this function actually get called.</p>
<dt>CURLOPT_PROGRESSDATA</p>
<dd> Pass a pointer that will be untouched by libcurl and passed as the first argument in the progress callback set with <i>CURLOPT_PROGRESSFUNCTION</i>.</p>
<dt>CURLOPT_HEADERFUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>size_t function( void *ptr, size_t size, size_t nmemb, void *userdata);</code>. This function gets called by libcurl as soon as it has received header data. The header callback will be called once for each header and only complete header lines are passed on to the callback. Parsing headers is very easy using this. The size of the data pointed to by <i>ptr</i> is <i>size</i> multiplied with <i>nmemb</i>. Do not assume that the header line is zero terminated! The pointer named <i>userdata</i> is the one you set with the <i>CURLOPT_WRITEHEADER</i> option. The callback function must return the number of bytes actually taken care of. If that amount differs from the amount passed to your function, it&#8217;ll signal an error to the library. This will abort the transfer and return <i>CURL_WRITE_ERROR</i>. </p>
<p> A complete HTTP header that is passed to this function can be up to <i>CURL_MAX_HTTP_HEADER</i> (100K) bytes. </p>
<p> If this option is not set, or if it is set to NULL, but <i>CURLOPT_HEADERDATA</i> (<i>CURLOPT_WRITEHEADER</i>) is set to anything but NULL, the function used to accept response data will be used instead. That is, it will be the function specified with <i>CURLOPT_WRITEFUNCTION</i>, or if it is not specified or NULL &#8211; the default, stream-writing function. </p>
<p> It&#8217;s important to note that the callback will be invoked for the headers of all responses received after initiating a request and not just the final response. This includes all responses which occur during authentication negotiation. If you need to operate on only the headers from the final response, you will need to collect headers in the callback yourself and use HTTP status lines, for example, to delimit response boundaries. </p>
<p> When a server sends a chunked encoded transfer, it may contain a trailer. That trailer is identical to a HTTP header and if such a trailer is received it is passed to the application using this callback as well. There are several ways to detect it being a trailer and not an ordinary header: 1) it comes after the response-body. 2) it comes after the final header line (CR LF) 3) a Trailer: header among the regular response-headers mention what header(s) to expect in the trailer. </p>
<p> For non-HTTP protocols like FTP, POP3, IMAP and SMTP this function will get called with the server responses to the commands that libcurl sends.</p>
<dt>CURLOPT_WRITEHEADER</p>
<dd> (This option is also known as <code>CURLOPT_HEADERDATA</code>) Pass a pointer to be used to write the header part of the received data to. If you don&#8217;t use <i>CURLOPT_WRITEFUNCTION</i> or <i>CURLOPT_HEADERFUNCTION</i> to take care of the writing, this must be a valid FILE * as the internal default will then be a plain fwrite(). See also the <i>CURLOPT_HEADERFUNCTION</i> option above on how to set a custom get-all-headers callback.</p>
<dt>CURLOPT_DEBUGFUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>int curl_debug_callback (CURL *, curl_infotype, char *, size_t, void *);</code> <i>CURLOPT_DEBUGFUNCTION</i> replaces the standard debug function used when <i>CURLOPT_VERBOSE </i> is in effect. This callback receives debug information, as specified with the <code>curl_infotype</code> argument. This function must return 0. The data pointed to by the char * passed to this function WILL NOT be zero terminated, but will be exactly of the size as told by the size_t argument. </p>
<p> Available curl_infotype values:</p>
<dl>
<dt>
<dd>
<dl>
<dt>CURLINFO_TEXT</p>
<dd> The data is informational text.</p>
<dt>CURLINFO_HEADER_IN</p>
<dd> The data is header (or header-like) data received from the peer.</p>
<dt>CURLINFO_HEADER_OUT</p>
<dd> The data is header (or header-like) data sent to the peer.</p>
<dt>CURLINFO_DATA_IN</p>
<dd> The data is protocol data received from the peer.</p>
<dt>CURLINFO_DATA_OUT</p>
<dd> The data is protocol data sent to the peer.</dl>
</dl>
<dt>CURLOPT_DEBUGDATA</p>
<dd> Pass a pointer to whatever you want passed in to your <i>CURLOPT_DEBUGFUNCTION</i> in the last void * argument. This pointer is not used by libcurl, it is only passed to the callback.</p>
<dt>CURLOPT_SSL_CTX_FUNCTION</p>
<dd> This option does only function for libcurl powered by OpenSSL. If libcurl was built against another SSL library, this functionality is absent. </p>
<p> Pass a pointer to a function that matches the following prototype: <code>CURLcode sslctxfun(CURL *curl, void *sslctx, void *parm);</code> This function gets called by libcurl just before the initialization of a SSL connection after having processed all other SSL related options to give a last chance to an application to modify the behaviour of openssl&#8217;s ssl initialization. The <i>sslctx</i> parameter is actually a pointer to an openssl <i>SSL_CTX</i>. If an error is returned no attempt to establish a connection is made and the perform operation will return the error code from this callback function. Set the <i>parm</i> argument with the <i>CURLOPT_SSL_CTX_DATA</i> option. This option was introduced in 7.11.0. </p>
<p> This function will get called on all new connections made to a server, during the SSL negotiation. The SSL_CTX pointer will be a new one every time. </p>
<p> To use this properly, a non-trivial amount of knowledge of the openssl libraries is necessary. For example, using this function allows you to use openssl callbacks to add additional validation code for certificates, and even to change the actual URI of a HTTPS request (example used in the lib509 test case). See also the example section for a replacement of the key, certificate and trust file settings.</p>
<dt>CURLOPT_SSL_CTX_DATA</p>
<dd> Data pointer to pass to the ssl context callback set by the option <i>CURLOPT_SSL_CTX_FUNCTION</i>, this is the pointer you&#8217;ll get as third parameter, otherwise <code>NULL</code>. (Added in 7.11.0)</p>
<dt>CURLOPT_CONV_TO_NETWORK_FUNCTION</p>
<dd>
<dt>CURLOPT_CONV_FROM_NETWORK_FUNCTION</p>
<dd>
<dt>CURLOPT_CONV_FROM_UTF8_FUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>CURLcode function(char *ptr, size_t length);</code> </p>
<p> These three options apply to non-ASCII platforms only. They are available only if <code>CURL_DOES_CONVERSIONS</code> was defined when libcurl was built. When this is the case, <i><a href="/docs/linux/man/3-curl_version_info/">curl_version_info</a>(3)</i> will return the CURL_VERSION_CONV feature bit set. </p>
<p> The data to be converted is in a buffer pointed to by the ptr parameter. The amount of data to convert is indicated by the length parameter. The converted data overlays the input data in the buffer pointed to by the ptr parameter. CURLE_OK should be returned upon successful conversion. A CURLcode return value defined by curl.h, such as CURLE_CONV_FAILED, should be returned if an error was encountered. </p>
<p> <code>CURLOPT_CONV_TO_NETWORK_FUNCTION</code> and <code>CURLOPT_CONV_FROM_NETWORK_FUNCTION</code> convert between the host encoding and the network encoding. They are used when commands or ASCII data are sent/received over the network. </p>
<p> <code>CURLOPT_CONV_FROM_UTF8_FUNCTION</code> is called to convert from UTF8 into the host encoding. It is required only for SSL processing. </p>
<p> If you set a callback pointer to NULL, or don&#8217;t set it at all, the built-in libcurl iconv functions will be used. If HAVE_ICONV was not defined when libcurl was built, and no callback has been established, conversion will return the CURLE_CONV_REQD error code. </p>
<p> If HAVE_ICONV is defined, CURL_ICONV_CODESET_OF_HOST must also be defined. For example: </p>
<p>&nbsp;<wbr>#define CURL_ICONV_CODESET_OF_HOST&nbsp;<wbr>&quot;IBM-1047&quot; </p>
<p> The iconv code in libcurl will default the network and UTF8 codeset names as follows: </p>
<p>&nbsp;<wbr>#define CURL_ICONV_CODESET_OF_NETWORK&nbsp;<wbr>&quot;ISO8859-1&quot; </p>
<p>&nbsp;<wbr>#define CURL_ICONV_CODESET_FOR_UTF8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;UTF-8&quot; </p>
<p> You will need to override these definitions if they are different on your system.</p>
<dt>CURLOPT_INTERLEAVEFUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>size_t function( void *ptr, size_t size, size_t nmemb, void *userdata)</code>. This function gets called by libcurl as soon as it has received interleaved RTP data. This function gets called for each $ block and therefore contains exactly one upper-layer protocol unit (e.g. one RTP packet). Curl writes the interleaved header as well as the included data for each call. The first byte is always an ASCII dollar sign. The dollar sign is followed by a one byte channel identifier and then a 2 byte integer length in network byte order. See <i>RFC2326 Section 10.12</i> for more information on how RTP interleaving behaves. If unset or set to NULL, curl will use the default write function. </p>
<p> Interleaved RTP poses some challenges for the client application. Since the stream data is sharing the RTSP control connection, it is critical to service the RTP in a timely fashion. If the RTP data is not handled quickly, subsequent response processing may become unreasonably delayed and the connection may close. The application may use <i>CURL_RTSPREQ_RECEIVE</i> to service RTP data when no requests are desired. If the application makes a request, (e.g. <i>CURL_RTSPREQ_PAUSE</i>) then the response handler will process any pending RTP data before marking the request as finished. (Added in 7.20.0)</p>
<dt>CURLOPT_INTERLEAVEDATA</p>
<dd> This is the userdata pointer that will be passed to <i>CURLOPT_INTERLEAVEFUNCTION</i> when interleaved RTP data is received. (Added in 7.20.0)</p>
<dt>CURLOPT_CHUNK_BGN_FUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>long function (const void *transfer_info, void *ptr, int remains)</code>. This function gets called by libcurl before a part of the stream is going to be transferred (if the transfer supports chunks). </p>
<p> This callback makes sense only when using the <i>CURLOPT_WILDCARDMATCH</i> option for now. </p>
<p> The target of transfer_info parameter is a &quot;feature depended&quot; structure. For the FTP wildcard download, the target is curl_fileinfo structure (see <i>curl/curl.h</i>). The parameter ptr is a pointer given by <i>CURLOPT_CHUNK_DATA</i>. The parameter remains contains number of chunks remaining per the transfer. If the feature is not available, the parameter has zero value. </p>
<p> Return <i>CURL_CHUNK_BGN_FUNC_OK</i> if everything is fine, <i>CURL_CHUNK_BGN_FUNC_SKIP</i> if you want to skip the concrete chunk or <i>CURL_CHUNK_BGN_FUNC_FAIL</i> to tell libcurl to stop if some error occurred. (This was added in 7.21.0)</p>
<dt>CURLOPT_CHUNK_END_FUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>long function(void *ptr)</code>. This function gets called by libcurl as soon as a part of the stream has been transferred (or skipped). </p>
<p> Return <i>CURL_CHUNK_END_FUNC_OK</i> if everything is fine or <code>CURL_CHUNK_END_FUNC_FAIL</code> to tell the lib to stop if some error occurred. (This was added in 7.21.0)</p>
<dt>CURLOPT_CHUNK_DATA</p>
<dd> Pass a pointer that will be untouched by libcurl and passed as the ptr argument to the <i>CURL_CHUNK_BGN_FUNTION</i> and <i>CURL_CHUNK_END_FUNTION</i>. (This was added in 7.21.0)</p>
<dt>CURLOPT_FNMATCH_FUNCTION</p>
<dd> Pass a pointer to a function that matches the following prototype: <code>int function(void *ptr, const char *pattern, const char *string)</code> prototype (see <i>curl/curl.h</i>). It is used internally for the wildcard matching feature. </p>
<p> Return <i>CURL_FNMATCHFUNC_MATCH</i> if pattern matches the string, <i>CURL_FNMATCHFUNC_NOMATCH</i> if not or <i>CURL_FNMATCHFUNC_FAIL</i> if an error occurred. (This was added in 7.21.0)</p>
<dt>CURLOPT_FNMATCH_DATA</p>
<dd> Pass a pointer that will be untouched by libcurl and passed as the ptr argument to the <i>CURL_FNMATCH_FUNCTION</i>. (This was added in 7.21.0)</dl>
<h2>ERROR OPTIONS</h2>
<dl>
<dt>CURLOPT_ERRORBUFFER</p>
<dd> Pass a char * to a buffer that the libcurl may store human readable error messages in. This may be more helpful than just the return code from <i>curl_easy_perform</i>. The buffer must be at least CURL_ERROR_SIZE big. Although this argument is a &#8216;char *&#8217;, it does not describe an input string. Therefore the (probably undefined) contents of the buffer is NOT copied by the library. You must keep the associated storage available until libcurl no longer needs it. Failing to do so will cause very odd behavior or even crashes. libcurl will need it until you call <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> or you set the same option again to use a different pointer. </p>
<p> Use <i>CURLOPT_VERBOSE</i> and <i>CURLOPT_DEBUGFUNCTION</i> to better debug/trace why errors happen. </p>
<p> If the library does not return an error, the buffer may not have been touched. Do not rely on the contents in those cases. </p>
<dt>CURLOPT_STDERR</p>
<dd> Pass a FILE * as parameter. Tell libcurl to use this stream instead of stderr when showing the progress meter and displaying <i>CURLOPT_VERBOSE</i> data.</p>
<dt>CURLOPT_FAILONERROR</p>
<dd> A parameter set to 1 tells the library to fail silently if the HTTP code returned is equal to or larger than 400. The default action would be to return the page normally, ignoring that code. </p>
<p> This method is not fail-safe and there are occasions where non-successful response codes will slip through, especially when authentication is involved (response codes 401 and 407). </p>
<p> You might get some amounts of headers transferred before this situation is detected, like when a &quot;100-continue&quot; is received as a response to a POST/PUT and a 401 or 407 is received immediately afterwards.</dl>
<h2>NETWORK OPTIONS</h2>
<dl>
<dt>CURLOPT_URL</p>
<dd> Pass in a pointer to the actual URL to deal with. The parameter should be a char * to a zero terminated string which must be URL-encoded in the following format: </p>
<p> <a href="scheme://host:port/path">scheme://host:port/path</a> </p>
<p> For a greater explanation of the format please see RFC3986. </p>
<p> If the given URL lacks the scheme, or protocol, part (&quot;http://&quot; or &quot;ftp://&quot; etc), libcurl will attempt to resolve which protocol to use based on the given host mame. If the protocol is not supported, libcurl will return (<i>CURLE_UNSUPPORTED_PROTOCOL</i>) when you call <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> or <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i>. Use <i><a href="/docs/linux/man/3-curl_version_info/">curl_version_info</a>(3)</i> for detailed information on which protocols are supported. </p>
<p> The host part of the URL contains the address of the server that you want to connect to. This can be the fully qualified domain name of the server, the local network name of the machine on your network or the IP address of the server or machine represented by either an IPv4 or IPv6 address. For example: </p>
<p> <a rel="nofollow" href="http://www.example.com/">http://www.example.com/</a> </p>
<p> <a rel="nofollow" href="http://hostname/">http://hostname/</a> </p>
<p> <a rel="nofollow" href="http://192.168.0.1/">http://192.168.0.1/</a> </p>
<p> <a rel="nofollow" href="http://[2001:1890:1112:1::20]/">http://[2001:1890:1112:1::20]/</a> </p>
<p> It is also possible to specify the user name and password as part of the host, for some protocols, when connecting to servers that require authentication. </p>
<p> For example the following types of authentication support this: </p>
<p> <a rel="nofollow" href="http://user:password@www.example.com">http://user:password@www.example.com</a> </p>
<p> <a href="ftp://user:password@ftp.example.com">ftp://user:password@ftp.example.com</a> </p>
<p> pop3://user:password [at] mail.example.com </p>
<p> The port is optional and when not specified libcurl will use the default port based on the determined or specified protocol: 80 for HTTP, 21 for FTP and 25 for SMTP, etc. The following examples show how to specify the port: </p>
<p> <a rel="nofollow" href="http://www.example.com:8080/">http://www.example.com:8080/</a> &#8211; This will connect to a web server using port 8080 rather than 80. </p>
<p> <a href="smtp://mail.example.com:587/">smtp://mail.example.com:587/</a> &#8211; This will connect to a SMTP server on the alternative mail port. </p>
<p> The path part of the URL is protocol specific and whilst some examples are given below this list is not conclusive: </p>
<p> <code>HTTP</code> </p>
<p> The path part of a HTTP request specifies the file to retrieve and from what directory. If the directory is not specified then the web server&#8217;s root directory is used. If the file is omitted then the default document will be retrieved for either the directory specified or the root directory. The exact resource returned for each URL is entirely dependent on the server&#8217;s configuration. </p>
<p> <a rel="nofollow" href="http://www.example.com">http://www.example.com</a> &#8211; This gets the main page from the web server. </p>
<p> <a rel="nofollow" href="http://www.example.com/index.html">http://www.example.com/index.html</a> &#8211; This returns the main page by explicitly requesting it. </p>
<p> <a rel="nofollow" href="http://www.example.com/contactus/">http://www.example.com/contactus/</a> &#8211; This returns the default document from the contactus directory. </p>
<p> <code>FTP</code> </p>
<p> The path part of an FTP request specifies the file to retrieve and from what directory. If the file part is omitted then libcurl downloads the directory listing for the directory specified. If the directory is omitted then the directory listing for the root / home directory will be returned. </p>
<p> <a href="ftp://ftp.example.com">ftp://ftp.example.com</a> &#8211; This retrieves the directory listing for the root directory. </p>
<p> <a href="ftp://ftp.example.com/readme.txt">ftp://ftp.example.com/readme.txt</a> &#8211; This downloads the file readme.txt from the root directory. </p>
<p> <a href="ftp://ftp.example.com/libcurl/readme.txt">ftp://ftp.example.com/libcurl/readme.txt</a> &#8211; This downloads readme.txt from the libcurl directory. </p>
<p> <a href="ftp://user:password@ftp.example.com/readme.txt">ftp://user:password@ftp.example.com/readme.txt</a> &#8211; This retrieves the readme.txt file from the user&#8217;s home directory. When a username and password is specified, everything that is specified in the path part is relative to the user&#8217;s home directory. To retrieve files from the root directory or a directory underneath the root directory then the absolute path must be specified by prepending an additional forward slash to the beginning of the path. </p>
<p> <a href="ftp://user:password@ftp.example.com//readme.txt">ftp://user:password@ftp.example.com//readme.txt</a> &#8211; This retrieves the readme.txt from the root directory when logging in as a specified user. </p>
<p> <code>SMTP</code> </p>
<p> The path part of a SMTP request specifies the host name to present during communication with the mail server. If the path is omitted then libcurl will attempt to resolve the local computer&#8217;s host name. However, this may not return the fully qualified domain name that is required by some mail servers and specifying this path allows you to set an alternative name, such as your machine&#8217;s fully qualified domain name, which you might have obtained from an external function such as gethostname or getaddrinfo. </p>
<p> <a href="smtp://mail.example.com">smtp://mail.example.com</a> &#8211; This connects to the mail server at example.com and sends your local computer&#8217;s host name in the HELO / EHLO command. </p>
<p> <a href="smtp://mail.example.com/client.example.com">smtp://mail.example.com/client.example.com</a> &#8211; This will send client.example.com in the HELO / EHLO command to the mail server at example.com. </p>
<p> <code>POP3</code> </p>
<p> The path part of a POP3 request specifies the mailbox (message) to retrieve. If the mailbox is not specified then a list of waiting messages is returned instead. </p>
<p> pop3://user:password [at] mail.example.com &#8211; This lists the available messages pop3://user:password [at] mail.example.com/1 &#8211; This retrieves the first message </p>
<p> <code>SCP</code> </p>
<p> The path part of a SCP request specifies the file to retrieve and from what directory. The file part may not be omitted. The file is taken as an absolute path from the root directory on the server. To specify a path relative to the user&#8217;s home directory on the server, prepend ~/ to the path portion. If the user name is not embedded in the URL, it can be set with the <i>CURLOPT_USERPWD</i> or <code>CURLOPT_USERNAME</code> option. </p>
<p> <a href="scp://user@example.com/etc/issue">scp://user@example.com/etc/issue</a> &#8211; This specifies the file /etc/issue </p>
<p> <a href="scp://example.com/~/my-file">scp://example.com/~/my-file</a> &#8211; This specifies the file my-file in the user&#8217;s home directory on the server </p>
<p> <code>SFTP</code> </p>
<p> The path part of a SFTP request specifies the file to retrieve and from what directory. If the file part is omitted then libcurl downloads the directory listing for the directory specified. If the path ends in a / then a directory listing is returned instead of a file. If the path is omitted entirely then the directory listing for the root / home directory will be returned. If the user name is not embedded in the URL, it can be set with the <i>CURLOPT_USERPWD</i> or <code>CURLOPT_USERNAME</code> option. </p>
<p> <a href="sftp://user:password@example.com/etc/issue">sftp://user:password@example.com/etc/issue</a> &#8211; This specifies the file /etc/issue </p>
<p> <a href="sftp://user@example.com/~/my-file">sftp://user@example.com/~/my-file</a> &#8211; This specifies the file my-file in the user&#8217;s home directory </p>
<p> <a href="sftp://ssh.example.com/~/Documents/">sftp://ssh.example.com/~/Documents/</a> &#8211; This requests a directory listing of the Documents directory under the user&#8217;s home directory </p>
<p> <code>LDAP</code> </p>
<p> The path part of a LDAP request can be used to specify the: Distinguished Name, Attributes, Scope, Filter and Extension for a LDAP search. Each field is separated by a question mark and when that field is not required an empty string with the question mark separator should be included. </p>
<p> <a href="ldap://ldap.example.com/o=My%20Organisation">ldap://ldap.example.com/o=My%20Organisation</a> &#8211; This will perform a LDAP search with the DN as My Organisation. </p>
<p> <a href="ldap://ldap.example.com/o=My%20Organisation?postalAddress">ldap://ldap.example.com/o=My%20Organisation?postalAddress</a> &#8211; This will perform the same search but will only return postalAddress attributes. </p>
<p> <a href="ldap://ldap.example.com/?rootDomainNamingContext">ldap://ldap.example.com/?rootDomainNamingContext</a> &#8211; This specifies an empty DN and requests information about the rootDomainNamingContext attribute for an Active Directory server. </p>
<p> For more information about the individual components of a LDAP URL please see RFC4516. </p>
<p> <code>NOTES</code> </p>
<p> Starting with version 7.20.0, the fragment part of the URI will not be sent as part of the path, which was previously the case. </p>
<p> <i>CURLOPT_URL</i> is the only option that <code>must</code> be set before <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> is called. </p>
<p> <i>CURLOPT_PROTOCOLS</i> can be used to limit what protocols libcurl will use for this transfer, independent of what libcurl has been compiled to support. That may be useful if you accept the URL from an external source and want to limit the accessibility.</p>
<dt>CURLOPT_PROTOCOLS</p>
<dd> Pass a long that holds a bitmask of CURLPROTO_* defines. If used, this bitmask limits what protocols libcurl may use in the transfer. This allows you to have a libcurl built to support a wide range of protocols but still limit specific transfers to only be allowed to use a subset of them. By default libcurl will accept all protocols it supports. See also <i>CURLOPT_REDIR_PROTOCOLS</i>. (Added in 7.19.4)</p>
<dt>CURLOPT_REDIR_PROTOCOLS</p>
<dd> Pass a long that holds a bitmask of CURLPROTO_* defines. If used, this bitmask limits what protocols libcurl may use in a transfer that it follows to in a redirect when <i>CURLOPT_FOLLOWLOCATION</i> is enabled. This allows you to limit specific transfers to only be allowed to use a subset of protocols in redirections. By default libcurl will allow all protocols except for FILE and SCP. This is a difference compared to pre-7.19.4 versions which unconditionally would follow to all protocols supported. (Added in 7.19.4)</p>
<dt>CURLOPT_PROXY</p>
<dd> Set HTTP proxy to use. The parameter should be a char * to a zero terminated string holding the host name or dotted IP address. To specify port number in this string, append :[port] to the end of the host name. The proxy string may be prefixed with [protocol]:// since any such prefix will be ignored. The proxy&#8217;s port number may optionally be specified with the separate option. If not specified, libcurl will default to using port 1080 for proxies. <i>CURLOPT_PROXYPORT</i>. </p>
<p> When you tell the library to use a HTTP proxy, libcurl will transparently convert operations to HTTP even if you specify an FTP URL etc. This may have an impact on what other features of the library you can use, such as <i>CURLOPT_QUOTE</i> and similar FTP specifics that don&#8217;t work unless you tunnel through the HTTP proxy. Such tunneling is activated with <i>CURLOPT_HTTPPROXYTUNNEL</i>. </p>
<p> libcurl respects the environment variables <code>http_proxy</code>, <code>ftp_proxy</code>, <code>all_proxy</code> etc, if any of those are set. The <i>CURLOPT_PROXY</i> option does however override any possibly set environment variables. </p>
<p> Setting the proxy string to &quot;&quot; (an empty string) will explicitly disable the use of a proxy, even if there is an environment variable set for it. </p>
<p> Since 7.14.1, the proxy host string given in environment variables can be specified the exact same way as the proxy can be set with <i>CURLOPT_PROXY</i>, include protocol prefix (<a rel="nofollow" href="http://)">http://)</a> and embedded user + password. </p>
<p> Since 7.21.7, the proxy string may be specified with a protocol:// prefix to specify alternative proxy protocols. Use socks4://, socks4a://, socks5:// or socks5h:// (the last one to enable socks5 and asking the proxy to do the resolving, also known as CURLPROXY_SOCKS5_HOSTNAME type) to request the specific SOCKS version to be used. No protocol specified, http:// and all others will be treated as HTTP proxies.</p>
<dt>CURLOPT_PROXYPORT</p>
<dd> Pass a long with this option to set the proxy port to connect to unless it is specified in the proxy string <i>CURLOPT_PROXY</i>.</p>
<dt>CURLOPT_PROXYTYPE</p>
<dd> Pass a long with this option to set type of the proxy. Available options for this are <i>CURLPROXY_HTTP</i>, <i>CURLPROXY_HTTP_1_0</i> (added in 7.19.4), <i>CURLPROXY_SOCKS4</i> (added in 7.10), <i>CURLPROXY_SOCKS5</i>, <i>CURLPROXY_SOCKS4A</i> (added in 7.18.0) and <i>CURLPROXY_SOCKS5_HOSTNAME</i> (added in 7.18.0). The HTTP type is default. (Added in 7.10) </p>
<p> If you set <code>CURLOPT_PROXYTYPE</code> to <i>CURLPROXY_HTTP_1_0</i>, it will only affect how libcurl speaks to a proxy when CONNECT is used. The HTTP version used for &quot;regular&quot; HTTP requests is instead controlled with <i>CURLOPT_HTTP_VERSION</i>.</p>
<dt>CURLOPT_NOPROXY</p>
<dd> Pass a pointer to a zero terminated string. The string consists of a comma separated list of host names that do not require a proxy to get reached, even if one is specified. The only wildcard available is a single * character, which matches all hosts, and effectively disables the proxy. Each name in this list is matched as either a domain which contains the hostname, or the hostname itself. For example, example.com would match example.com, example.com:80, and <a rel="nofollow" href="http://www.example.com">www.example.com</a>, but not <a href="http://www.notanexample.com">www.notanexample.com</a>. (Added in 7.19.4)</p>
<dt>CURLOPT_HTTPPROXYTUNNEL</p>
<dd> Set the parameter to 1 to make the library tunnel all operations through a given HTTP proxy. There is a big difference between using a proxy and to tunnel through it. If you don&#8217;t know what this means, you probably don&#8217;t want this tunneling option.</p>
<dt>CURLOPT_SOCKS5_GSSAPI_SERVICE</p>
<dd> Pass a char * as parameter to a string holding the name of the service. The default service name for a SOCKS5 server is rcmd/server-fqdn. This option allows you to change it. (Added in 7.19.4)</p>
<dt>CURLOPT_SOCKS5_GSSAPI_NEC</p>
<dd> Pass a long set to 1 to enable or 0 to disable. As part of the gssapi negotiation a protection mode is negotiated. The RFC1961 says in section 4.3/4.4 it should be protected, but the NEC reference implementation does not. If enabled, this option allows the unprotected exchange of the protection mode negotiation. (Added in 7.19.4).</p>
<dt>CURLOPT_INTERFACE</p>
<dd> Pass a char * as parameter. This sets the interface name to use as outgoing network interface. The name can be an interface name, an IP address, or a host name. </p>
<p> Starting with 7.24.0: If the parameter starts with &quot;if!&quot; then it is treated as only as interface name and no attempt will ever be named to do treat it as an IP address or to do name resolution on it. If the parameter starts with &quot;host!&quot; it is treated as either an IP address or a hostname. Hostnames are resolved synchronously. Using the if! format is highly recommended when using the multi interfaces to avoid allowing the code to block. If &quot;if!&quot; is specified but the parameter does not match an existing interface, CURLE_INTERFACE_FAILED is returned.</p>
<dt>CURLOPT_LOCALPORT</p>
<dd> Pass a long. This sets the local port number of the socket used for connection. This can be used in combination with <i>CURLOPT_INTERFACE</i> and you are recommended to use <i>CURLOPT_LOCALPORTRANGE</i> as well when this is set. Valid port numbers are 1 &#8211; 65535. (Added in 7.15.2)</p>
<dt>CURLOPT_LOCALPORTRANGE</p>
<dd> Pass a long. This is the number of attempts libcurl will make to find a working local port number. It starts with the given <i>CURLOPT_LOCALPORT</i> and adds one to the number for each retry. Setting this to 1 or below will make libcurl do only one try for the exact port number. Port numbers by nature are scarce resources that will be busy at times so setting this value to something too low might cause unnecessary connection setup failures. (Added in 7.15.2)</p>
<dt>CURLOPT_DNS_CACHE_TIMEOUT</p>
<dd> Pass a long, this sets the timeout in seconds. Name resolves will be kept in memory for this number of seconds. Set to zero to completely disable caching, or set to -1 to make the cached entries remain forever. By default, libcurl caches this info for 60 seconds. </p>
<p> The name resolve functions of various libc implementations don&#8217;t re-read name server information unless explicitly told so (for example, by calling <i><a href="/docs/linux/man/3-res_init/">res_init</a>(3)</i>). This may cause libcurl to keep using the older server even if DHCP has updated the server info, and this may look like a DNS cache issue to the casual libcurl-app user.</p>
<dt>CURLOPT_DNS_USE_GLOBAL_CACHE</p>
<dd> Pass a long. If the value is 1, it tells curl to use a global DNS cache that will survive between easy handle creations and deletions. This is not thread-safe and this will use a global variable. </p>
<p> <code>WARNING:</code> this option is considered obsolete. Stop using it. Switch over to using the share interface instead! See <i>CURLOPT_SHARE</i> and <i><a href="/docs/linux/man/3-curl_share_init/">curl_share_init</a>(3)</i>.</p>
<dt>CURLOPT_BUFFERSIZE</p>
<dd> Pass a long specifying your preferred size (in bytes) for the receive buffer in libcurl. The main point of this would be that the write callback gets called more often and with smaller chunks. This is just treated as a request, not an order. You cannot be guaranteed to actually get the given size. (Added in 7.10) </p>
<p> This size is by default set as big as possible (CURL_MAX_WRITE_SIZE), so it only makes sense to use this option if you want it smaller.</p>
<dt>CURLOPT_PORT</p>
<dd> Pass a long specifying what remote port number to connect to, instead of the one specified in the URL or the default port for the used protocol.</p>
<dt>CURLOPT_TCP_NODELAY</p>
<dd> Pass a long specifying whether the TCP_NODELAY option is to be set or cleared (1 = set, 0 = clear). The option is cleared by default. This will have no effect after the connection has been established. </p>
<p> Setting this option will disable TCP&#8217;s Nagle algorithm. The purpose of this algorithm is to try to minimize the number of small packets on the network (where &quot;small packets&quot; means TCP segments less than the Maximum Segment Size (MSS) for the network). </p>
<p> Maximizing the amount of data sent per TCP segment is good because it amortizes the overhead of the send. However, in some cases (most notably telnet or rlogin) small segments may need to be sent without delay. This is less efficient than sending larger amounts of data at a time, and can contribute to congestion on the network if overdone.</p>
<dt>CURLOPT_ADDRESS_SCOPE</p>
<dd> Pass a long specifying the scope_id value to use when connecting to IPv6 link-local or site-local addresses. (Added in 7.19.0)</p>
<dt>CURLOPT_TCP_KEEPALIVE</p>
<dd> Pass a long. If set to 1, TCP keepalive probes will be sent. The delay and frequency of these probes can be controlled by the <i>CURLOPT_TCP_KEEPIDLE</i> and <i>CURLOPT_TCP_KEEPINTVL</i> options, provided the operating system supports them. Set to 0 (default behavior) to disable keepalive probes (Added in 7.25.0).</p>
<dt>CURLOPT_TCP_KEEPIDLE</p>
<dd> Pass a long. Sets the delay, in seconds, that the operating system will wait while the connection is idle before sending keepalive probes. Not all operating systems support this option. (Added in 7.25.0)</p>
<dt>CURLOPT_TCP_KEEPINTVL</p>
<dd> Pass a long. Sets the interval, in seconds, that the operating system will wait between sending keepalive probes. Not all operating systems support this option. (Added in 7.25.0)</p>
<dt>CURLOPT_UNIX_SOCKET_PATH</p>
<dd> Pass a <i>path</i> to a UNIX domain socket. This enables the use of UNIX domain sockets as connection end point and sets the path to <i>path</i>. If <i>path</i> is NULL, then UNIX domain sockets are disabled. An empty string will result in an error at some point. </p>
<p> When enabled, cURL will connect to the UNIX domain socket instead of establishing a TCP connection to a host. Since no TCP connection is established, cURL does not need to resolve the DNS hostname in the URL. </p>
<p> The maximum path length on Cygwin, Linux and Solaris is 107. On other platforms might be even less.</dl>
<h2>NAMES and PASSWORDS OPTIONS (Authentication)</h2>
<dl>
<dt>CURLOPT_NETRC</p>
<dd> This parameter controls the preference of libcurl between using user names and passwords from your <i>~/.netrc</i> file, relative to user names and passwords in the URL supplied with <i>CURLOPT_URL</i>. </p>
<p> libcurl uses a user name (and supplied or prompted password) supplied with <i>CURLOPT_USERPWD</i> in preference to any of the options controlled by this parameter. </p>
<p> Pass a long, set to one of the values described below.</p>
<dl>
<dt>
<dd>
<dl>
<dt>CURL_NETRC_OPTIONAL</p>
<dd> The use of your <i>~/.netrc</i> file is optional, and information in the URL is to be preferred. The file will be scanned for the host and user name (to find the password only) or for the host only, to find the first user name and password after that <i>machine</i>, which ever information is not specified in the URL. </p>
<p> Undefined values of the option will have this effect.</p>
<dt>CURL_NETRC_IGNORED</p>
<dd> The library will ignore the file and use only the information in the URL. </p>
<p> This is the default.</p>
<dt>CURL_NETRC_REQUIRED</p>
<dd> This value tells the library that use of the file is required, to ignore the information in the URL, and to search the file for the host only.</dl>
</dl>
<p> Only machine name, user name and password are taken into account (init macros and similar things aren&#8217;t supported). </p>
<p> libcurl does not verify that the file has the correct properties set (as the standard Unix ftp client does). It should only be readable by user.</p>
<dt>CURLOPT_NETRC_FILE</p>
<dd> Pass a char * as parameter, pointing to a zero terminated string containing the full path name to the file you want libcurl to use as .netrc file. If this option is omitted, and <i>CURLOPT_NETRC</i> is set, libcurl will attempt to find a .netrc file in the current user&#8217;s home directory. (Added in 7.10.9)</p>
<dt>CURLOPT_USERPWD</p>
<dd> Pass a char * as parameter, which should be [user name]:[password] to use for the connection. Use <i>CURLOPT_HTTPAUTH</i> to decide the authentication method. </p>
<p> When using NTLM, you can set the domain by prepending it to the user name and separating the domain and name with a forward (/) or backward slash (\). Like this: &quot;domain/user:password&quot; or &quot;domain
