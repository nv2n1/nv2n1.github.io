---

title: "libcurl-errors(3)"
name: "libcurl-errors"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libcurl-errors/"
---

libcurl-errors - error codes in libcurl

<h2>DESCRIPTION</h2>

 This man page includes most, if not all, available error codes in libcurl. Why they occur and possibly what you can do to fix the problem are also included.

<h2>CURLcode</h2>

 Almost all &quot;easy&quot; interface functions return a CURLcode error code. No matter what, using the <i><a HREF="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> option <i>CURLOPT_ERRORBUFFER</i> is a good idea as it will give you a human readable error string that may offer more details about the cause of the error than just the error code. <i><a HREF="/docs/linux/man/3-curl_easy_strerror/">curl_easy_strerror</a>(3)</i> can be called to get an error string from a given CURLcode number. 

 CURLcode is one of the following:
<dl>
<dt>CURLE_OK (0)
</dt><dd> All fine. Proceed as usual.
</dd><dt>CURLE_UNSUPPORTED_PROTOCOL (1)
</dt><dd> The URL you passed to libcurl used a protocol that this libcurl does not support. The support might be a compile-time option that you didn't use, it can be a misspelled protocol string or just a protocol libcurl has no code for.
</dd><dt>CURLE_FAILED_INIT (2)
</dt><dd> Very early initialization code failed. This is likely to be an internal error or problem, or a resource problem where something fundamental couldn't get done at init time.
</dd><dt>CURLE_URL_MALFORMAT (3)
</dt><dd> The URL was not properly formatted.
</dd><dt>CURLE_NOT_BUILT_IN (4)
</dt><dd> A requested feature, protocol or option was not found built-in in this libcurl due to a build-time decision. This means that a feature or option was not enabled or explicitly disabled when libcurl was built and in order to get it to function you have to get a rebuilt libcurl.
</dd><dt>CURLE_COULDNT_RESOLVE_PROXY (5)
</dt><dd> Couldn't resolve proxy. The given proxy host could not be resolved.
</dd><dt>CURLE_COULDNT_RESOLVE_HOST (6)
</dt><dd> Couldn't resolve host. The given remote host was not resolved.
</dd><dt>CURLE_COULDNT_CONNECT (7)
</dt><dd> Failed to connect() to host or proxy.
</dd><dt>CURLE_FTP_WEIRD_SERVER_REPLY (8)
</dt><dd> After connecting to a FTP server, libcurl expects to get a certain reply back. This error code implies that it got a strange or bad reply. The given remote server is probably not an OK FTP server.
</dd><dt>CURLE_REMOTE_ACCESS_DENIED (9)
</dt><dd> We were denied access to the resource given in the URL. For FTP, this occurs while trying to change to the remote directory.
</dd><dt>CURLE_FTP_ACCEPT_FAILED (10)
</dt><dd> While waiting for the server to connect back when an active FTP session is used, an error code was sent over the control connection or similar.
</dd><dt>CURLE_FTP_WEIRD_PASS_REPLY (11)
</dt><dd> After having sent the FTP password to the server, libcurl expects a proper reply. This error code indicates that an unexpected code was returned.
</dd><dt>CURLE_FTP_ACCEPT_TIMEOUT (12)
</dt><dd> During an active FTP session while waiting for the server to connect, the <i>CURLOPT_ACCEPTTIMOUT_MS</i> (or the internal default) timeout expired.
</dd><dt>CURLE_FTP_WEIRD_PASV_REPLY (13)
</dt><dd> libcurl failed to get a sensible result back from the server as a response to either a PASV or a EPSV command. The server is flawed.
</dd><dt>CURLE_FTP_WEIRD_227_FORMAT (14)
</dt><dd> FTP servers return a 227-line as a response to a PASV command. If libcurl fails to parse that line, this return code is passed back.
</dd><dt>CURLE_FTP_CANT_GET_HOST (15)
</dt><dd> An internal failure to lookup the host used for the new connection.
</dd><dt>CURLE_FTP_COULDNT_SET_TYPE (17)
</dt><dd> Received an error when trying to set the transfer mode to binary or ASCII.
</dd><dt>CURLE_PARTIAL_FILE (18)
</dt><dd> A file transfer was shorter or larger than expected. This happens when the server first reports an expected transfer size, and then delivers data that doesn't match the previously given size.
</dd><dt>CURLE_FTP_COULDNT_RETR_FILE (19)
</dt><dd> This was either a weird reply to a 'RETR' command or a zero byte transfer complete.
</dd><dt>CURLE_QUOTE_ERROR (21)
</dt><dd> When sending custom &quot;QUOTE&quot; commands to the remote server, one of the commands returned an error code that was 400 or higher (for FTP) or otherwise indicated unsuccessful completion of the command.
</dd><dt>CURLE_HTTP_RETURNED_ERROR (22)
</dt><dd> This is returned if CURLOPT_FAILONERROR is set TRUE and the HTTP server returns an error code that is &gt;= 400.
</dd><dt>CURLE_WRITE_ERROR (23)
</dt><dd> An error occurred when writing received data to a local file, or an error was returned to libcurl from a write callback.
</dd><dt>CURLE_UPLOAD_FAILED (25)
</dt><dd> Failed starting the upload. For FTP, the server typically denied the STOR command. The error buffer usually contains the server's explanation for this.
</dd><dt>CURLE_READ_ERROR (26)
</dt><dd> There was a problem reading a local file or an error returned by the read callback.
</dd><dt>CURLE_OUT_OF_MEMORY (27)
</dt><dd> A memory allocation request failed. This is serious badness and things are severely screwed up if this ever occurs.
</dd><dt>CURLE_OPERATION_TIMEDOUT (28)
</dt><dd> Operation timeout. The specified time-out period was reached according to the conditions.
</dd><dt>CURLE_FTP_PORT_FAILED (30)
</dt><dd> The FTP PORT command returned error. This mostly happens when you haven't specified a good enough address for libcurl to use. See <i>CURLOPT_FTPPORT</i>.
</dd><dt>CURLE_FTP_COULDNT_USE_REST (31)
</dt><dd> The FTP REST command returned error. This should never happen if the server is sane.
</dd><dt>CURLE_RANGE_ERROR (33)
</dt><dd> The server does not support or accept range requests.
</dd><dt>CURLE_HTTP_POST_ERROR (34)
</dt><dd> This is an odd error that mainly occurs due to internal confusion.
</dd><dt>CURLE_SSL_CONNECT_ERROR (35)
</dt><dd> A problem occurred somewhere in the SSL/TLS handshake. You really want the error buffer and read the message there as it pinpoints the problem slightly more. Could be certificates (file formats, paths, permissions), passwords, and others.
</dd><dt>CURLE_BAD_DOWNLOAD_RESUME (36)
</dt><dd> The download could not be resumed because the specified offset was out of the file boundary.
</dd><dt>CURLE_FILE_COULDNT_READ_FILE (37)
</dt><dd> A file given with FILE:// couldn't be opened. Most likely because the file path doesn't identify an existing file. Did you check file permissions?
</dd><dt>CURLE_LDAP_CANNOT_BIND (38)
</dt><dd> LDAP cannot bind. LDAP bind operation failed.
</dd><dt>CURLE_LDAP_SEARCH_FAILED (39)
</dt><dd> LDAP search failed.
</dd><dt>CURLE_FUNCTION_NOT_FOUND (41)
</dt><dd> Function not found. A required zlib function was not found.
</dd><dt>CURLE_ABORTED_BY_CALLBACK (42)
</dt><dd> Aborted by callback. A callback returned &quot;abort&quot; to libcurl.
</dd><dt>CURLE_BAD_FUNCTION_ARGUMENT (43)
</dt><dd> Internal error. A function was called with a bad parameter.
</dd><dt>CURLE_INTERFACE_FAILED (45)
</dt><dd> Interface error. A specified outgoing interface could not be used. Set which interface to use for outgoing connections' source IP address with CURLOPT_INTERFACE.
</dd><dt>CURLE_TOO_MANY_REDIRECTS (47)
</dt><dd> Too many redirects. When following redirects, libcurl hit the maximum amount. Set your limit with CURLOPT_MAXREDIRS.
</dd><dt>CURLE_UNKNOWN_OPTION (48)
</dt><dd> An option passed to libcurl is not recognized/known. Refer to the appropriate documentation. This is most likely a problem in the program that uses libcurl. The error buffer might contain more specific information about which exact option it concerns.
</dd><dt>CURLE_TELNET_OPTION_SYNTAX (49)
</dt><dd> A telnet option string was Illegally formatted.
</dd><dt>CURLE_PEER_FAILED_VERIFICATION (51)
</dt><dd> The remote server's SSL certificate or SSH md5 fingerprint was deemed not OK.
</dd><dt>CURLE_GOT_NOTHING (52)
</dt><dd> Nothing was returned from the server, and under the circumstances, getting nothing is considered an error.
</dd><dt>CURLE_SSL_ENGINE_NOTFOUND (53)
</dt><dd> The specified crypto engine wasn't found.
</dd><dt>CURLE_SSL_ENGINE_SETFAILED (54)
</dt><dd> Failed setting the selected SSL crypto engine as default!
</dd><dt>CURLE_SEND_ERROR (55)
</dt><dd> Failed sending network data.
</dd><dt>CURLE_RECV_ERROR (56)
</dt><dd> Failure with receiving network data.
</dd><dt>CURLE_SSL_CERTPROBLEM (58)
</dt><dd> problem with the local client certificate.
</dd><dt>CURLE_SSL_CIPHER (59)
</dt><dd> Couldn't use specified cipher.
</dd><dt>CURLE_SSL_CACERT (60)
</dt><dd> Peer certificate cannot be authenticated with known CA certificates.
</dd><dt>CURLE_BAD_CONTENT_ENCODING (61)
</dt><dd> Unrecognized transfer encoding.
</dd><dt>CURLE_LDAP_INVALID_URL (62)
</dt><dd> Invalid LDAP URL.
</dd><dt>CURLE_FILESIZE_EXCEEDED (63)
</dt><dd> Maximum file size exceeded.
</dd><dt>CURLE_USE_SSL_FAILED (64)
</dt><dd> Requested FTP SSL level failed.
</dd><dt>CURLE_SEND_FAIL_REWIND (65)
</dt><dd> When doing a send operation curl had to rewind the data to retransmit, but the rewinding operation failed.
</dd><dt>CURLE_SSL_ENGINE_INITFAILED (66)
</dt><dd> Initiating the SSL Engine failed.
</dd><dt>CURLE_LOGIN_DENIED (67)
</dt><dd> The remote server denied curl to login (Added in 7.13.1)
</dd><dt>CURLE_TFTP_NOTFOUND (68)
</dt><dd> File not found on TFTP server.
</dd><dt>CURLE_TFTP_PERM (69)
</dt><dd> Permission problem on TFTP server.
</dd><dt>CURLE_REMOTE_DISK_FULL (70)
</dt><dd> Out of disk space on the server.
</dd><dt>CURLE_TFTP_ILLEGAL (71)
</dt><dd> Illegal TFTP operation.
</dd><dt>CURLE_TFTP_UNKNOWNID (72)
</dt><dd> Unknown TFTP transfer ID.
</dd><dt>CURLE_REMOTE_FILE_EXISTS (73)
</dt><dd> File already exists and will not be overwritten.
</dd><dt>CURLE_TFTP_NOSUCHUSER (74)
</dt><dd> This error should never be returned by a properly functioning TFTP server.
</dd><dt>CURLE_CONV_FAILED (75)
</dt><dd> Character conversion failed.
</dd><dt>CURLE_CONV_REQD (76)
</dt><dd> Caller must register conversion callbacks.
</dd><dt>CURLE_SSL_CACERT_BADFILE (77)
</dt><dd> Problem with reading the SSL CA cert (path? access rights?)
</dd><dt>CURLE_REMOTE_FILE_NOT_FOUND (78)
</dt><dd> The resource referenced in the URL does not exist.
</dd><dt>CURLE_SSH (79)
</dt><dd> An unspecified error occurred during the SSH session.
</dd><dt>CURLE_SSL_SHUTDOWN_FAILED (80)
</dt><dd> Failed to shut down the SSL connection.
</dd><dt>CURLE_AGAIN (81)
</dt><dd> Socket is not ready for send/recv wait till it's ready and try again. This return code is only returned from <i><a HREF="/docs/linux/man/3-curl_easy_recv/">curl_easy_recv</a>(3)</i> and <i><a HREF="/docs/linux/man/3-curl_easy_send/">curl_easy_send</a>(3)</i> (Added in 7.18.2)
</dd><dt>CURLE_SSL_CRL_BADFILE (82)
</dt><dd> Failed to load CRL file (Added in 7.19.0)
</dd><dt>CURLE_SSL_ISSUER_ERROR (83)
</dt><dd> Issuer check failed (Added in 7.19.0)
</dd><dt>CURLE_FTP_PRET_FAILED (84)
</dt><dd> The FTP server does not understand the PRET command at all or does not support the given argument. Be careful when using <i>CURLOPT_CUSTOMREQUEST</i>, a custom LIST command will be sent with PRET CMD before PASV as well. (Added in 7.20.0)
</dd><dt>CURLE_RTSP_CSEQ_ERROR (85)
</dt><dd> Mismatch of RTSP CSeq numbers.
</dd><dt>CURLE_RTSP_SESSION_ERROR (86)
</dt><dd> Mismatch of RTSP Session Identifiers.
</dd><dt>CURLE_FTP_BAD_FILE_LIST (87)
</dt><dd> Unable to parse FTP file list (during FTP wildcard downloading).
</dd><dt>CURLE_CHUNK_FAILED (88)
</dt><dd> Chunk callback reported error.
</dd><dt>CURLE_OBSOLETE*
</dt><dd> These error codes will never be returned. They were used in an old libcurl version and are currently unused.</dd></dl>

<h2>CURLMcode</h2>

 This is the generic return code used by functions in the libcurl multi interface. Also consider <i><a HREF="/docs/linux/man/3-curl_multi_strerror/">curl_multi_strerror</a>(3)</i>.
<dl>
<dt>CURLM_CALL_MULTI_PERFORM (-1)
</dt><dd> This is not really an error. It means you should call <i><a HREF="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i> again without doing select() or similar in between. Before version 7.20.0 this could be returned by <i><a HREF="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i>, but in later versions this return code is never used.
</dd><dt>CURLM_OK (0)
</dt><dd> Things are fine.
</dd><dt>CURLM_BAD_HANDLE (1)
</dt><dd> The passed-in handle is not a valid CURLM handle.
</dd><dt>CURLM_BAD_EASY_HANDLE (2)
</dt><dd> An easy handle was not good/valid. It could mean that it isn't an easy handle at all, or possibly that the handle already is in used by this or another multi handle.
</dd><dt>CURLM_OUT_OF_MEMORY (3)
</dt><dd> You are doomed.
</dd><dt>CURLM_INTERNAL_ERROR (4)
</dt><dd> This can only be returned if libcurl bugs. Please report it to us!
</dd><dt>CURLM_BAD_SOCKET (5)
</dt><dd> The passed-in socket is not a valid one that libcurl already knows about. (Added in 7.15.4)
</dd><dt>CURLM_UNKNOWN_OPTION (6)
</dt><dd> curl_multi_setopt() with unsupported option (Added in 7.15.4)</dd></dl>

<h2>CURLSHcode</h2>

 The &quot;share&quot; interface will return a CURLSHcode to indicate when an error has occurred. Also consider <i><a HREF="/docs/linux/man/3-curl_share_strerror/">curl_share_strerror</a>(3)</i>.
<dl>
<dt>CURLSHE_OK (0)
</dt><dd> All fine. Proceed as usual.
</dd><dt>CURLSHE_BAD_OPTION (1)
</dt><dd> An invalid option was passed to the function.
</dd><dt>CURLSHE_IN_USE (2)
</dt><dd> The share object is currently in use.
</dd><dt>CURLSHE_INVALID (3)
</dt><dd> An invalid share object was passed to the function.
</dd><dt>CURLSHE_NOMEM (4)
</dt><dd> Not enough memory was available. (Added in 7.12.0)
</dd><dt>CURLSHE_NOT_BUILT_IN (5)
</dt><dd> The requested sharing could not be done because the library you use don't have that particular feature enabled. (Added in 7.23.0) 
</dd></dl>
