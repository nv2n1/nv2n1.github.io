---
title: "curl_easy_getinfo(3)"
name: "curl_easy_getinfo"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_easy_getinfo/"
description: "curl_easy_getinfo – extract information from a curl handle"
---

<h2>NAME</h2>
<p> curl_easy_getinfo &#8211; extract information from a curl handle</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>CURLcode curl_easy_getinfo(CURL *curl, CURLINFO info, &#8230; );</code> </p>
<h2>DESCRIPTION</h2>
<p> Request internal information from the curl session with this function. The third argument <code>MUST</code> be a pointer to a long, a pointer to a char *, a pointer to a struct curl_slist * or a pointer to a double (as this documentation describes further down). The data pointed-to will be filled in accordingly and can be relied upon only if the function returns CURLE_OK. Use this function AFTER a performed transfer if you want to get transfer- oriented data. </p>
<p> You should not free the memory returned by this function unless it is explicitly mentioned below.</p>
<h2>AVAILABLE INFORMATION</h2>
<p> The following information can be extracted:</p>
<dl>
<dt>CURLINFO_EFFECTIVE_URL</p>
<dd> Pass a pointer to a char pointer to receive the last used effective URL.</p>
<dt>CURLINFO_RESPONSE_CODE</p>
<dd> Pass a pointer to a long to receive the last received HTTP, FTP or SMTP response code. This option was previously known as CURLINFO_HTTP_CODE in libcurl 7.10.7 and earlier. The value will be zero if no server response code has been received. Note that a proxy&#8217;s CONNECT response should be read with <i>CURLINFO_HTTP_CONNECTCODE</i> and not this. </p>
<p> Support for SMTP responses added in 7.25.0.</p>
<dt>CURLINFO_HTTP_CONNECTCODE</p>
<dd> Pass a pointer to a long to receive the last received proxy response code to a CONNECT request.</p>
<dt>CURLINFO_FILETIME</p>
<dd> Pass a pointer to a long to receive the remote time of the retrieved document (in number of seconds since 1 jan 1970 in the GMT/UTC time zone). If you get -1, it can be because of many reasons (unknown, the server hides it or the server doesn&#8217;t support the command that tells document time etc) and the time of the document is unknown. Note that you must tell the server to collect this information before the transfer is made, by using the CURLOPT_FILETIME option to <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> or you will unconditionally get a -1 back. (Added in 7.5)</p>
<dt>CURLINFO_TOTAL_TIME</p>
<dd> Pass a pointer to a double to receive the total time in seconds for the previous transfer, including name resolving, TCP connect etc.</p>
<dt>CURLINFO_NAMELOOKUP_TIME</p>
<dd> Pass a pointer to a double to receive the time, in seconds, it took from the start until the name resolving was completed.</p>
<dt>CURLINFO_CONNECT_TIME</p>
<dd> Pass a pointer to a double to receive the time, in seconds, it took from the start until the connect to the remote host (or proxy) was completed.</p>
<dt>CURLINFO_APPCONNECT_TIME</p>
<dd> Pass a pointer to a double to receive the time, in seconds, it took from the start until the SSL/SSH connect/handshake to the remote host was completed. This time is most often very near to the PRETRANSFER time, except for cases such as HTTP pippelining where the pretransfer time can be delayed due to waits in line for the pipeline and more. (Added in 7.19.0)</p>
<dt>CURLINFO_PRETRANSFER_TIME</p>
<dd> Pass a pointer to a double to receive the time, in seconds, it took from the start until the file transfer is just about to begin. This includes all pre-transfer commands and negotiations that are specific to the particular protocol(s) involved. It does <i>not</i> involve the sending of the protocol- specific request that triggers a transfer.</p>
<dt>CURLINFO_STARTTRANSFER_TIME</p>
<dd> Pass a pointer to a double to receive the time, in seconds, it took from the start until the first byte is received by libcurl. This includes CURLINFO_PRETRANSFER_TIME and also the time the server needs to calculate the result.</p>
<dt>CURLINFO_REDIRECT_TIME</p>
<dd> Pass a pointer to a double to receive the total time, in seconds, it took for all redirection steps include name lookup, connect, pretransfer and transfer before final transaction was started. CURLINFO_REDIRECT_TIME contains the complete execution time for multiple redirections. (Added in 7.9.7)</p>
<dt>CURLINFO_REDIRECT_COUNT</p>
<dd> Pass a pointer to a long to receive the total number of redirections that were actually followed. (Added in 7.9.7)</p>
<dt>CURLINFO_REDIRECT_URL</p>
<dd> Pass a pointer to a char pointer to receive the URL a redirect <i>would</i> take you to if you would enable CURLOPT_FOLLOWLOCATION. This can come very handy if you think using the built-in libcurl redirect logic isn&#8217;t good enough for you but you would still prefer to avoid implementing all the magic of figuring out the new URL. (Added in 7.18.2)</p>
<dt>CURLINFO_SIZE_UPLOAD</p>
<dd> Pass a pointer to a double to receive the total amount of bytes that were uploaded.</p>
<dt>CURLINFO_SIZE_DOWNLOAD</p>
<dd> Pass a pointer to a double to receive the total amount of bytes that were downloaded. The amount is only for the latest transfer and will be reset again for each new transfer.</p>
<dt>CURLINFO_SPEED_DOWNLOAD</p>
<dd> Pass a pointer to a double to receive the average download speed that curl measured for the complete download. Measured in bytes/second.</p>
<dt>CURLINFO_SPEED_UPLOAD</p>
<dd> Pass a pointer to a double to receive the average upload speed that curl measured for the complete upload. Measured in bytes/second.</p>
<dt>CURLINFO_HEADER_SIZE</p>
<dd> Pass a pointer to a long to receive the total size of all the headers received. Measured in number of bytes.</p>
<dt>CURLINFO_REQUEST_SIZE</p>
<dd> Pass a pointer to a long to receive the total size of the issued requests. This is so far only for HTTP requests. Note that this may be more than one request if FOLLOWLOCATION is true.</p>
<dt>CURLINFO_SSL_VERIFYRESULT</p>
<dd> Pass a pointer to a long to receive the result of the certification verification that was requested (using the CURLOPT_SSL_VERIFYPEER option to <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i>).</p>
<dt>CURLINFO_SSL_ENGINES</p>
<dd> Pass the address of a &#8216;struct curl_slist *&#8217; to receive a linked-list of OpenSSL crypto-engines supported. Note that engines are normally implemented in separate dynamic libraries. Hence not all the returned engines may be available at run-time. <code>NOTE:</code> you must call <i><a href="/docs/linux/man/3-curl_slist_free_all/">curl_slist_free_all</a>(3)</i> on the list pointer once you&#8217;re done with it, as libcurl will not free the data for you. (Added in 7.12.3)</p>
<dt>CURLINFO_CONTENT_LENGTH_DOWNLOAD</p>
<dd> Pass a pointer to a double to receive the content-length of the download. This is the value read from the Content-Length: field. Since 7.19.4, this returns -1 if the size isn&#8217;t known.</p>
<dt>CURLINFO_CONTENT_LENGTH_UPLOAD</p>
<dd> Pass a pointer to a double to receive the specified size of the upload. Since 7.19.4, this returns -1 if the size isn&#8217;t known.</p>
<dt>CURLINFO_CONTENT_TYPE</p>
<dd> Pass a pointer to a char pointer to receive the content-type of the downloaded object. This is the value read from the Content-Type: field. If you get NULL, it means that the server didn&#8217;t send a valid Content-Type header or that the protocol used doesn&#8217;t support this.</p>
<dt>CURLINFO_PRIVATE</p>
<dd> Pass a pointer to a char pointer to receive the pointer to the private data associated with the curl handle (set with the CURLOPT_PRIVATE option to <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i>). Please note that for internal reasons, the value is returned as a char pointer, although effectively being a &#8216;void *&#8217;. (Added in 7.10.3)</p>
<dt>CURLINFO_HTTPAUTH_AVAIL</p>
<dd> Pass a pointer to a long to receive a bitmask indicating the authentication method(s) available. The meaning of the bits is explained in the CURLOPT_HTTPAUTH option for <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i>. (Added in 7.10.8)</p>
<dt>CURLINFO_PROXYAUTH_AVAIL</p>
<dd> Pass a pointer to a long to receive a bitmask indicating the authentication method(s) available for your proxy authentication. (Added in 7.10.8)</p>
<dt>CURLINFO_OS_ERRNO</p>
<dd> Pass a pointer to a long to receive the errno variable from a connect failure. Note that the value is only set on failure, it is not reset upon a successful operation. (Added in 7.12.2)</p>
<dt>CURLINFO_NUM_CONNECTS</p>
<dd> Pass a pointer to a long to receive how many new connections libcurl had to create to achieve the previous transfer (only the successful connects are counted). Combined with <i>CURLINFO_REDIRECT_COUNT</i> you are able to know how many times libcurl successfully reused existing connection(s) or not. See the Connection Options of <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> to see how libcurl tries to make persistent connections to save time. (Added in 7.12.3)</p>
<dt>CURLINFO_PRIMARY_IP</p>
<dd> Pass a pointer to a char pointer to receive the pointer to a zero-terminated string holding the IP address of the most recent connection done with this <code>curl</code> handle. This string may be IPv6 if that&#8217;s enabled. Note that you get a pointer to a memory area that will be re-used at next request so you need to copy the string if you want to keep the information. (Added in 7.19.0)</p>
<dt>CURLINFO_PRIMARY_PORT</p>
<dd> Pass a pointer to a long to receive the destination port of the most recent connection done with this <code>curl</code> handle. (Added in 7.21.0)</p>
<dt>CURLINFO_LOCAL_IP</p>
<dd> Pass a pointer to a char pointer to receive the pointer to a zero-terminated string holding the local (source) IP address of the most recent connection done with this <code>curl</code> handle. This string may be IPv6 if that&#8217;s enabled. The same restrictions apply as to <i>CURLINFO_PRIMARY_IP</i>. (Added in 7.21.0)</p>
<dt>CURLINFO_LOCAL_PORT</p>
<dd> Pass a pointer to a long to receive the local (source) port of the most recent connection done with this <code>curl</code> handle. (Added in 7.21.0)</p>
<dt>CURLINFO_COOKIELIST</p>
<dd> Pass a pointer to a &#8216;struct curl_slist *&#8217; to receive a linked-list of all cookies cURL knows (expired ones, too). Don&#8217;t forget to <i><a href="/docs/linux/man/3-curl_slist_free_all/">curl_slist_free_all</a>(3)</i> the list after it has been used. If there are no cookies (cookies for the handle have not been enabled or simply none have been received) &#8216;struct curl_slist *&#8217; will be set to point to NULL. (Added in 7.14.1)</p>
<dt>CURLINFO_LASTSOCKET</p>
<dd> Pass a pointer to a long to receive the last socket used by this curl session. If the socket is no longer valid, -1 is returned. When you finish working with the socket, you must call curl_easy_cleanup() as usual and let libcurl close the socket and cleanup other resources associated with the handle. This is typically used in combination with <i>CURLOPT_CONNECT_ONLY</i>. (Added in 7.15.2) </p>
<p> NOTE: this API is not really working on win64, since the SOCKET type on win64 is 64 bit large while its &#8216;long&#8217; is only 32 bits.</p>
<dt>CURLINFO_FTP_ENTRY_PATH</p>
<dd> Pass a pointer to a char pointer to receive a pointer to a string holding the path of the entry path. That is the initial path libcurl ended up in when logging on to the remote FTP server. This stores a NULL as pointer if something is wrong. (Added in 7.15.4) </p>
<p> Also works for SFTP since 7.21.4</p>
<dt>CURLINFO_CERTINFO</p>
<dd> Pass a pointer to a &#8216;struct curl_certinfo *&#8217; and you&#8217;ll get it set to point to struct that holds a number of linked lists with info about the certificate chain, assuming you had CURLOPT_CERTINFO enabled when the previous request was done. The struct reports how many certs it found and then you can extract info for each of those certs by following the linked lists. The info chain is provided in a series of data in the format &quot;name:content&quot; where the content is for the specific named data. See also the certinfo.c example. NOTE: this option is only available in libcurl built with OpenSSL support. (Added in 7.19.1)</p>
<dt>CURLINFO_CONDITION_UNMET</p>
<dd> Pass a pointer to a long to receive the number 1 if the condition provided in the previous request didn&#8217;t match (see <i>CURLOPT_TIMECONDITION</i>). Alas, if this returns a 1 you know that the reason you didn&#8217;t get data in return is because it didn&#8217;t fulfill the condition. The long ths argument points to will get a zero stored if the condition instead was met. (Added in 7.19.4)</p>
<dt>CURLINFO_RTSP_SESSION_ID</p>
<dd> Pass a pointer to a char pointer to receive a pointer to a string holding the most recent RTSP Session ID. </p>
<p> Applications wishing to resume an RTSP session on another connection should retreive this info before closing the active connection.</p>
<dt>CURLINFO_RTSP_CLIENT_CSEQ</p>
<dd> Pass a pointer to a long to receive the next CSeq that will be used by the application.</p>
<dt>CURLINFO_RTSP_SERVER_CSEQ</p>
<dd> Pass a pointer to a long to receive the next server CSeq that will be expected by the application. </p>
<p> <i>(NOTE: listening for server initiated requests is currently unimplemented).</i> </p>
<p> Applications wishing to resume an RTSP session on another connection should retreive this info before closing the active connection.</p>
<dt>CURLINFO_RTSP_CSEQ_RECV</p>
<dd> Pass a pointer to a long to receive the most recently received CSeq from the server. If your application encounters a <i>CURLE_RTSP_CSEQ_ERROR</i> then you may wish to troubleshoot and/or fix the CSeq mismatch by peeking at this value.</dl>
<h2>TIMES</h2>
<pre><code>
An overview of the six time values available from curl_easy_getinfo()
        curl_easy_perform() |
    | --NAMELOOKUP
    | -- | --CONNECT
    | -- | -- | --APPCONNECT
    | -- | -- | -- | --PRETRANSFER
    | -- | -- | -- | -- | --STARTTRANSFER
    | -- | -- | -- | -- | -- | --TOTAL
    | -- | -- | -- | -- | -- | --REDIRECT
</code></pre>
<dl>
<dt>NAMELOOKUP</p>
<dd> <i>CURLINFO_NAMELOOKUP_TIME</i>. The time it took from the start until the name resolving was completed.</p>
<dt>CONNECT</p>
<dd> <i>CURLINFO_CONNECT_TIME</i>. The time it took from the start until the connect to the remote host (or proxy) was completed.</p>
<dt>APPCONNECT</p>
<dd> <i>CURLINFO_APPCONNECT_TIME</i>. The time it took from the start until the SSL connect/handshake with the remote host was completed. (Added in in 7.19.0)</p>
<dt>PRETRANSFER</p>
<dd> <i>CURLINFO_PRETRANSFER_TIME</i>. The time it took from the start until the file transfer is just about to begin. This includes all pre-transfer commands and negotiations that are specific to the particular protocol(s) involved.</p>
<dt>STARTTRANSFER</p>
<dd> <i>CURLINFO_STARTTRANSFER_TIME</i>. The time it took from the start until the first byte is received by libcurl.</p>
<dt>TOTAL</p>
<dd> <i>CURLINFO_TOTAL_TIME</i>. Total time of the previous request.</p>
<dt>REDIRECT</p>
<dd> <i>CURLINFO_REDIRECT_TIME</i>. The time it took for all redirection steps include name lookup, connect, pretransfer and transfer before final transaction was started. So, this is zero if no redirection took place.</dl>
<h2>RETURN VALUE</h2>
<p> If the operation was successful, CURLE_OK is returned. Otherwise an appropriate error code will be returned.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a></code>(3) </p>
<h2>Index</h2>
