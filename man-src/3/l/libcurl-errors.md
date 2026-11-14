---
title: "libcurl-errors(3)"
name: "libcurl-errors"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libcurl-errors/"
---

<h2>NAME</h2>

 libcurl-errors - error codes in libcurl

<h2>DESCRIPTION</h2>

 This man page includes most, if not all, available error codes in libcurl. Why they occur and possibly what you can do to fix the problem are also included.

<h2>CURLcode</h2>

 Almost all &quot;easy&quot; interface functions return a CURLcode error code. No matter what, using the <i><a HREF="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> option <i>CURLOPT_ERRORBUFFER</i> is a good idea as it will give you a human readable error string that may offer more details about the cause of the error than just the error code. <i><a HREF="/docs/linux/man/3-curl_easy_strerror/">curl_easy_strerror</a>(3)</i> can be called to get an error string from a given CURLcode number. 

 CURLcode is one of the following:
<dl>
<dt>CURLE_OK (0)
<dd> All fine. Proceed as usual.
<dt>CURLE_UNSUPPORTED_PROTOCOL (1)
<dd> The URL you passed to libcurl used a protocol that this libcurl does not support. The support might be a compile-time option that you didn't use, it can be a misspelled protocol string or just a protocol libcurl has no code for.
<dt>CURLE_FAILED_INIT (2)
<dd> Very early initialization code failed. This is likely to be an internal error or problem, or a resource problem where something fundamental couldn't get done at init time.
<dt>CURLE_URL_MALFORMAT (3)
<dd> The URL was not properly formatted.
<dt>CURLE_NOT_BUILT_IN (4)
<dd> A requested feature, protocol or option was not found built-in in this libcurl due to a build-time decision. This means that a feature or option was not enabled or explicitly disabled when libcurl was built and in order to get it to function you have to get a rebuilt libcurl.
<dt>CURLE_COULDNT_RESOLVE_PROXY (5)
<dd> Couldn't resolve proxy. The given proxy host could not be resolved.
<dt>CURLE_COULDNT_RESOLVE_HOST (6)
<dd> Couldn't resolve host. The given remote host was not resolved.
<dt>CURLE_COULDNT_CONNECT (7)
<dd> Failed to connect() to host or proxy.
<dt>CURLE_FTP_WEIRD_SERVER_REPLY (8)
<dd> After connecting to a FTP server, libcurl expects to get a certain reply back. This error code implies that it got a strange or bad reply. The given remote server is probably not an OK FTP server.
<dt>CURLE_REMOTE_ACCESS_DENIED (9)
<dd> We were denied access to the resource given in the URL. For FTP, this occurs while trying to change to the remote directory.
<dt>CURLE_FTP_ACCEPT_FAILED (10)
<dd> While waiting for the server to connect back when an active FTP session is used, an error code was sent over the control connection or similar.
<dt>CURLE_FTP_WEIRD_PASS_REPLY (11)
<dd> After having sent the FTP password to the server, libcurl expects a proper reply. This error code indicates that an unexpected code was returned.
<dt>CURLE_FTP_ACCEPT_TIMEOUT (12)
<dd> During an active FTP session while waiting for the server to connect, the <i>CURLOPT_ACCEPTTIMOUT_MS</i> (or the internal default) timeout expired.
<dt>CURLE_FTP_WEIRD_PASV_REPLY (13)
<dd> libcurl failed to get a sensible result back from the server as a response to either a PASV or a EPSV command. The server is flawed.
<dt>CURLE_FTP_WEIRD_227_FORMAT (14)
<dd> FTP servers return a 227-line as a response to a PASV command. If libcurl fails to parse that line, this return code is passed back.
<dt>CURLE_FTP_CANT_GET_HOST (15)
<dd> An internal failure to lookup the host used for the new connection.
<dt>CURLE_FTP_COULDNT_SET_TYPE (17)
<dd> Received an error when trying to set the transfer mode to binary or ASCII.
<dt>CURLE_PARTIAL_FILE (18)
<dd> A file transfer was shorter or larger than expected. This happens when the server first reports an expected transfer size, and then delivers data that doesn't match the previously given size.
<dt>CURLE_FTP_COULDNT_RETR_FILE (19)
<dd> This was either a weird reply to a 'RETR' command or a zero byte transfer complete.
<dt>CURLE_QUOTE_ERROR (21)
<dd> When sending custom &quot;QUOTE&quot; commands to the remote server, one of the commands returned an error code that was 400 or higher (for FTP) or otherwise indicated unsuccessful completion of the command.
<dt>CURLE_HTTP_RETURNED_ERROR (22)
<dd> This is returned if CURLOPT_FAILONERROR is set TRUE and the HTTP server returns an error code that is &gt;= 400.
<dt>CURLE_WRITE_ERROR (23)
<dd> An error occurred when writing received data to a local file, or an error was returned to libcurl from a write callback.
<dt>CURLE_UPLOAD_FAILED (25)
<dd> Failed starting the upload. For FTP, the server typically denied the STOR command. The error buffer usually contains the server's explanation for this.
<dt>CURLE_READ_ERROR (26)
<dd> There was a problem reading a local file or an error returned by the read callback.
<dt>CURLE_OUT_OF_MEMORY (27)
<dd> A memory allocation request failed. This is serious badness and things are severely screwed up if this ever occurs.
<dt>CURLE_OPERATION_TIMEDOUT (28)
<dd> Operation timeout. The specified time-out period was reached according to the conditions.
<dt>CURLE_FTP_PORT_FAILED (30)
<dd> The FTP PORT command returned error. This mostly happens when you haven't specified a good enough address for libcurl to use. See <i>CURLOPT_FTPPORT</i>.
<dt>CURLE_FTP_COULDNT_USE_REST (31)
<dd> The FTP REST command returned error. This should never happen if the server is sane.
<dt>CURLE_RANGE_ERROR (33)
<dd> The server does not support or accept range requests.
<dt>CURLE_HTTP_POST_ERROR (34)
<dd> This is an odd error that mainly occurs due to internal confusion.
<dt>CURLE_SSL_CONNECT_ERROR (35)
<dd> A problem occurred somewhere in the SSL/TLS handshake. You really want the error buffer and read the message there as it pinpoints the problem slightly more. Could be certificates (file formats, paths, permissions), passwords, and others.
<dt>CURLE_BAD_DOWNLOAD_RESUME (36)
<dd> The download could not be resumed because the specified offset was out of the file boundary.
<dt>CURLE_FILE_COULDNT_READ_FILE (37)
<dd> A file given with FILE:// couldn't be opened. Most likely because the file path doesn't identify an existing file. Did you check file permissions?
<dt>CURLE_LDAP_CANNOT_BIND (38)
<dd> LDAP cannot bind. LDAP bind operation failed.
<dt>CURLE_LDAP_SEARCH_FAILED (39)
<dd> LDAP search failed.
<dt>CURLE_FUNCTION_NOT_FOUND (41)
<dd> Function not found. A required zlib function was not found.
<dt>CURLE_ABORTED_BY_CALLBACK (42)
<dd> Aborted by callback. A callback returned &quot;abort&quot; to libcurl.
<dt>CURLE_BAD_FUNCTION_ARGUMENT (43)
<dd> Internal error. A function was called with a bad parameter.
<dt>CURLE_INTERFACE_FAILED (45)
<dd> Interface error. A specified outgoing interface could not be used. Set which interface to use for outgoing connections' source IP address with CURLOPT_INTERFACE.
<dt>CURLE_TOO_MANY_REDIRECTS (47)
<dd> Too many redirects. When following redirects, libcurl hit the maximum amount. Set your limit with CURLOPT_MAXREDIRS.
<dt>CURLE_UNKNOWN_OPTION (48)
<dd> An option passed to libcurl is not recognized/known. Refer to the appropriate documentation. This is most likely a problem in the program that uses libcurl. The error buffer might contain more specific information about which exact option it concerns.
<dt>CURLE_TELNET_OPTION_SYNTAX (49)
<dd> A telnet option string was Illegally formatted.
<dt>CURLE_PEER_FAILED_VERIFICATION (51)
<dd> The remote server's SSL certificate or SSH md5 fingerprint was deemed not OK.
<dt>CURLE_GOT_NOTHING (52)
<dd> Nothing was returned from the server, and under the circumstances, getting nothing is considered an error.
<dt>CURLE_SSL_ENGINE_NOTFOUND (53)
<dd> The specified crypto engine wasn't found.
<dt>CURLE_SSL_ENGINE_SETFAILED (54)
<dd> Failed setting the selected SSL crypto engine as default!
<dt>CURLE_SEND_ERROR (55)
<dd> Failed sending network data.
<dt>CURLE_RECV_ERROR (56)
<dd> Failure with receiving network data.
<dt>CURLE_SSL_CERTPROBLEM (58)
<dd> problem with the local client certificate.
<dt>CURLE_SSL_CIPHER (59)
<dd> Couldn't use specified cipher.
<dt>CURLE_SSL_CACERT (60)
<dd> Peer certificate cannot be authenticated with known CA certificates.
<dt>CURLE_BAD_CONTENT_ENCODING (61)
<dd> Unrecognized transfer encoding.
<dt>CURLE_LDAP_INVALID_URL (62)
<dd> Invalid LDAP URL.
<dt>CURLE_FILESIZE_EXCEEDED (63)
<dd> Maximum file size exceeded.
<dt>CURLE_USE_SSL_FAILED (64)
<dd> Requested FTP SSL level failed.
<dt>CURLE_SEND_FAIL_REWIND (65)
<dd> When doing a send operation curl had to rewind the data to retransmit, but the rewinding operation failed.
<dt>CURLE_SSL_ENGINE_INITFAILED (66)
<dd> Initiating the SSL Engine failed.
<dt>CURLE_LOGIN_DENIED (67)
<dd> The remote server denied curl to login (Added in 7.13.1)
<dt>CURLE_TFTP_NOTFOUND (68)
<dd> File not found on TFTP server.
<dt>CURLE_TFTP_PERM (69)
<dd> Permission problem on TFTP server.
<dt>CURLE_REMOTE_DISK_FULL (70)
<dd> Out of disk space on the server.
<dt>CURLE_TFTP_ILLEGAL (71)
<dd> Illegal TFTP operation.
<dt>CURLE_TFTP_UNKNOWNID (72)
<dd> Unknown TFTP transfer ID.
<dt>CURLE_REMOTE_FILE_EXISTS (73)
<dd> File already exists and will not be overwritten.
<dt>CURLE_TFTP_NOSUCHUSER (74)
<dd> This error should never be returned by a properly functioning TFTP server.
<dt>CURLE_CONV_FAILED (75)
<dd> Character conversion failed.
<dt>CURLE_CONV_REQD (76)
<dd> Caller must register conversion callbacks.
<dt>CURLE_SSL_CACERT_BADFILE (77)
<dd> Problem with reading the SSL CA cert (path? access rights?)
<dt>CURLE_REMOTE_FILE_NOT_FOUND (78)
<dd> The resource referenced in the URL does not exist.
<dt>CURLE_SSH (79)
<dd> An unspecified error occurred during the SSH session.
<dt>CURLE_SSL_SHUTDOWN_FAILED (80)
<dd> Failed to shut down the SSL connection.
<dt>CURLE_AGAIN (81)
<dd> Socket is not ready for send/recv wait till it's ready and try again. This return code is only returned from <i><a HREF="/docs/linux/man/3-curl_easy_recv/">curl_easy_recv</a>(3)</i> and <i><a HREF="/docs/linux/man/3-curl_easy_send/">curl_easy_send</a>(3)</i> (Added in 7.18.2)
<dt>CURLE_SSL_CRL_BADFILE (82)
<dd> Failed to load CRL file (Added in 7.19.0)
<dt>CURLE_SSL_ISSUER_ERROR (83)
<dd> Issuer check failed (Added in 7.19.0)
<dt>CURLE_FTP_PRET_FAILED (84)
<dd> The FTP server does not understand the PRET command at all or does not support the given argument. Be careful when using <i>CURLOPT_CUSTOMREQUEST</i>, a custom LIST command will be sent with PRET CMD before PASV as well. (Added in 7.20.0)
<dt>CURLE_RTSP_CSEQ_ERROR (85)
<dd> Mismatch of RTSP CSeq numbers.
<dt>CURLE_RTSP_SESSION_ERROR (86)
<dd> Mismatch of RTSP Session Identifiers.
<dt>CURLE_FTP_BAD_FILE_LIST (87)
<dd> Unable to parse FTP file list (during FTP wildcard downloading).
<dt>CURLE_CHUNK_FAILED (88)
<dd> Chunk callback reported error.
<dt>CURLE_OBSOLETE*
<dd> These error codes will never be returned. They were used in an old libcurl version and are currently unused.</dl>

<h2>CURLMcode</h2>

 This is the generic return code used by functions in the libcurl multi interface. Also consider <i><a HREF="/docs/linux/man/3-curl_multi_strerror/">curl_multi_strerror</a>(3)</i>.
<dl>
<dt>CURLM_CALL_MULTI_PERFORM (-1)
<dd> This is not really an error. It means you should call <i><a HREF="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i> again without doing select() or similar in between. Before version 7.20.0 this could be returned by <i><a HREF="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i>, but in later versions this return code is never used.
<dt>CURLM_OK (0)
<dd> Things are fine.
<dt>CURLM_BAD_HANDLE (1)
<dd> The passed-in handle is not a valid CURLM handle.
<dt>CURLM_BAD_EASY_HANDLE (2)
<dd> An easy handle was not good/valid. It could mean that it isn't an easy handle at all, or possibly that the handle already is in used by this or another multi handle.
<dt>CURLM_OUT_OF_MEMORY (3)
<dd> You are doomed.
<dt>CURLM_INTERNAL_ERROR (4)
<dd> This can only be returned if libcurl bugs. Please report it to us!
<dt>CURLM_BAD_SOCKET (5)
<dd> The passed-in socket is not a valid one that libcurl already knows about. (Added in 7.15.4)
<dt>CURLM_UNKNOWN_OPTION (6)
<dd> curl_multi_setopt() with unsupported option (Added in 7.15.4)</dl>

<h2>CURLSHcode</h2>

 The &quot;share&quot; interface will return a CURLSHcode to indicate when an error has occurred. Also consider <i><a HREF="/docs/linux/man/3-curl_share_strerror/">curl_share_strerror</a>(3)</i>.
<dl>
<dt>CURLSHE_OK (0)
<dd> All fine. Proceed as usual.
<dt>CURLSHE_BAD_OPTION (1)
<dd> An invalid option was passed to the function.
<dt>CURLSHE_IN_USE (2)
<dd> The share object is currently in use.
<dt>CURLSHE_INVALID (3)
<dd> An invalid share object was passed to the function.
<dt>CURLSHE_NOMEM (4)
<dd> Not enough memory was available. (Added in 7.12.0)
<dt>CURLSHE_NOT_BUILT_IN (5)
<dd> The requested sharing could not be done because the library you use don't have that particular feature enabled. (Added in 7.23.0) 

</dl>

<h2>Index</h2>


