---
title: "curlopt_url(3)"
name: "curlopt_url"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_url/"
description: "CURLOPT_URL – provide the URL to use in the request"
---

<p>CURLOPT_URL &#8211; provide the URL to use in the request</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_URL, char *URL);</p>
<h2>Description</h2>
<p>Pass in a pointer to the <i>URL</i> to work with. The parameter should be a char * to a zero terminated string which must be URL-encoded in the following format: </p>
<p> <a href="scheme://host:port/path">scheme://host:port/path</a> </p>
<p> For a greater explanation of the format please see RFC3986. </p>
<p> libcurl doesn&#8217;t validate the syntax or use this variable until the transfer is issued. Even if you set a crazy value here, <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> will still return <i>CURLE_OK</i>. </p>
<p> If the given URL lacks the scheme (such as &quot;http://&quot; or &quot;ftp://&quot; etc) then libcurl will attempt to resolve the protocol based on one of the following given host names: HTTP, FTP, DICT, LDAP, IMAP, POP3 or SMTP </p>
<p> Should the protocol, either that specified by the scheme or deduced by libcurl from the host name, not be supported by libcurl then <i>CURLE_UNSUPPORTED_PROTOCOL</i> will be returned from either the <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> or <i><a href="/docs/linux/man/3-curl_multi_perform/">curl_multi_perform</a>(3)</i> functions when you call them. Use <i><a href="/docs/linux/man/3-curl_version_info/">curl_version_info</a>(3)</i> for detailed information of which protocols are supported by the build of libcurl you are using. </p>
<p> <i><a href="/docs/linux/man/3-curlopt_protocols/">CURLOPT_PROTOCOLS</a>(3)</i> can be used to limit what protocols libcurl will use for this transfer, independent of what libcurl has been compiled to support. That may be useful if you accept the URL from an external source and want to limit the accessibility. </p>
<p> <i><a href="/docs/linux/man/3-curlopt_url/">CURLOPT_URL</a>(3)</i> is the only option that <code>must</code> be set before a transfer is started. </p>
<p> The host part of the URL contains the address of the server that you want to connect to. This can be the fully qualified domain name of the server, the local network name of the machine on your network or the IP address of the server or machine represented by either an IPv4 or IPv6 address. For example: </p>
<p> <a rel="nofollow" href="http://www.example.com/">http://www.example.com/</a> </p>
<p> <a rel="nofollow" href="http://hostname/">http://hostname/</a> </p>
<p> <a rel="nofollow" href="http://192.168.0.1/">http://192.168.0.1/</a> </p>
<p> <a rel="nofollow" href="http://[2001:1890:1112:1::20]/">http://[2001:1890:1112:1::20]/</a> </p>
<p> It is also possible to specify the user name, password and any supported login options as part of the host, for the following protocols, when connecting to servers that require authentication: </p>
<p> <a rel="nofollow" href="http://user:password@www.example.com">http://user:password@www.example.com</a> </p>
<p> <a href="ftp://user:password@ftp.example.com">ftp://user:password@ftp.example.com</a> </p>
<p> <a href="smb://domain%2fuser:password@server.example.com">smb://domain%2fuser:password@server.example.com</a> </p>
<p> <a href="imap://user:password;options@mail.example.com">imap://user:password;options@mail.example.com</a> </p>
<p> pop3://user:password;options [at] mail.example.com </p>
<p> <a href="smtp://user:password;options@mail.example.com">smtp://user:password;options@mail.example.com</a> </p>
<p> At present only IMAP, POP3 and SMTP support login options as part of the host. For more information about the login options in URL syntax please see RFC2384, RFC5092 and IETF draft draft-earhart-url-smtp-00.txt (Added in 7.31.0). </p>
<p> The port is optional and when not specified libcurl will use the default port based on the determined or specified protocol: 80 for HTTP, 21 for FTP and 25 for SMTP, etc. The following examples show how to specify the port: </p>
<p> <a rel="nofollow" href="http://www.example.com:8080/">http://www.example.com:8080/</a> &#8211; This will connect to a web server using port 8080 rather than 80. </p>
<p> <a href="smtp://mail.example.com:587/">smtp://mail.example.com:587/</a> &#8211; This will connect to a SMTP server on the alternative mail port. </p>
<p> The path part of the URL is protocol specific and whilst some examples are given below this list is not conclusive: </p>
<dl COMPACT>
<dt>HTTP</p>
<dd>The path part of a HTTP request specifies the file to retrieve and from what directory. If the directory is not specified then the web server&#8217;s root directory is used. If the file is omitted then the default document will be retrieved for either the directory specified or the root directory. The exact resource returned for each URL is entirely dependent on the server&#8217;s configuration. </p>
<p> <a rel="nofollow" href="http://www.example.com">http://www.example.com</a> &#8211; This gets the main page from the web server. </p>
<p> <a rel="nofollow" href="http://www.example.com/index.html">http://www.example.com/index.html</a> &#8211; This returns the main page by explicitly requesting it. </p>
<p> <a rel="nofollow" href="http://www.example.com/contactus/">http://www.example.com/contactus/</a> &#8211; This returns the default document from the contactus directory. </p>
<dt>FTP</p>
<dd>The path part of an FTP request specifies the file to retrieve and from what directory. If the file part is omitted then libcurl downloads the directory listing for the directory specified. If the directory is omitted then the directory listing for the root / home directory will be returned. </p>
<p> <a href="ftp://ftp.example.com">ftp://ftp.example.com</a> &#8211; This retrieves the directory listing for the root directory. </p>
<p> <a href="ftp://ftp.example.com/readme.txt">ftp://ftp.example.com/readme.txt</a> &#8211; This downloads the file readme.txt from the root directory. </p>
<p> <a href="ftp://ftp.example.com/libcurl/readme.txt">ftp://ftp.example.com/libcurl/readme.txt</a> &#8211; This downloads readme.txt from the libcurl directory. </p>
<p> <a href="ftp://user:password@ftp.example.com/readme.txt">ftp://user:password@ftp.example.com/readme.txt</a> &#8211; This retrieves the readme.txt file from the user&#8217;s home directory. When a username and password is specified, everything that is specified in the path part is relative to the user&#8217;s home directory. To retrieve files from the root directory or a directory underneath the root directory then the absolute path must be specified by prepending an additional forward slash to the beginning of the path. </p>
<p> <a href="ftp://user:password@ftp.example.com//readme.txt">ftp://user:password@ftp.example.com//readme.txt</a> &#8211; This retrieves the readme.txt from the root directory when logging in as a specified user. </p>
<dt>SMTP</p>
<dd>The path part of a SMTP request specifies the host name to present during communication with the mail server. If the path is omitted then libcurl will attempt to resolve the local computer&#8217;s host name. However, this may not return the fully qualified domain name that is required by some mail servers and specifying this path allows you to set an alternative name, such as your machine&#8217;s fully qualified domain name, which you might have obtained from an external function such as gethostname or getaddrinfo. </p>
<p> <a href="smtp://mail.example.com">smtp://mail.example.com</a> &#8211; This connects to the mail server at example.com and sends your local computer&#8217;s host name in the HELO / EHLO command. </p>
<p> <a href="smtp://mail.example.com/client.example.com">smtp://mail.example.com/client.example.com</a> &#8211; This will send client.example.com in the HELO / EHLO command to the mail server at example.com. </p>
<dt>POP3</p>
<dd>The path part of a POP3 request specifies the message ID to retrieve. If the ID is not specified then a list of waiting messages is returned instead. </p>
<p> pop3://user:password [at] mail.example.com &#8211; This lists the available messages for the user </p>
<p> pop3://user:password [at] mail.example.com/1 &#8211; This retrieves the first message for the user </p>
<dt>IMAP</p>
<dd>The path part of an IMAP request not only specifies the mailbox to list (Added in 7.30.0) or select, but can also be used to check the UIDVALIDITY of the mailbox, to specify the UID, SECTION (Added in 7.30.0) and PARTIAL octets (Added in 7.37.0) of the message to fetch and to specify what messages to search for (Added in 7.37.0). </p>
<p> <a href="imap://user:password@mail.example.com">imap://user:password@mail.example.com</a> &#8211; Performs a top level folder list </p>
<p> <a href="imap://user:password@mail.example.com/INBOX">imap://user:password@mail.example.com/INBOX</a> &#8211; Performs a folder list on the user&#8217;s inbox </p>
<p> <a href="imap://user:password@mail.example.com/INBOX/;UID=1">imap://user:password@mail.example.com/INBOX/;UID=1</a> &#8211; Selects the user&#8217;s inbox and fetches message 1 </p>
<p> <a href="imap://user:password@mail.example.com/INBOX;UIDVALIDITY=50/;UID=2">imap://user:password@mail.example.com/INBOX;UIDVALIDITY=50/;UID=2</a> &#8211; Selects the user&#8217;s inbox, checks the UIDVALIDITY of the mailbox is 50 and fetches message 2 if it is </p>
<p> <a href="imap://user:password@mail.example.com/INBOX/;UID=3/;SECTION=TEXT">imap://user:password@mail.example.com/INBOX/;UID=3/;SECTION=TEXT</a> &#8211; Selects the user&#8217;s inbox and fetches the text portion of message 3 </p>
<p> <a href="imap://user:password@mail.example.com/INBOX/;UID=4/;PARTIAL=0.1024">imap://user:password@mail.example.com/INBOX/;UID=4/;PARTIAL=0.1024</a> &#8211; Selects the user&#8217;s inbox and fetches the first 1024 octets of message 4 </p>
<p> <a href="imap://user:password@mail.example.com/INBOX?NEW">imap://user:password@mail.example.com/INBOX?NEW</a> &#8211; Selects the user&#8217;s inbox and checks for NEW messages </p>
<p> <a href="imap://user:password@mail.example.com/INBOX?SUBJECT%20shadows">imap://user:password@mail.example.com/INBOX?SUBJECT%20shadows</a> &#8211; Selects the user&#8217;s inbox and searches for messages containing &quot;shadows&quot; in the subject line </p>
<p> For more information about the individual components of an IMAP URL please see RFC5092. </p>
<dt>SCP</p>
<dd>The path part of a SCP request specifies the file to retrieve and from what directory. The file part may not be omitted. The file is taken as an absolute path from the root directory on the server. To specify a path relative to the user&#8217;s home directory on the server, prepend ~/ to the path portion. If the user name is not embedded in the URL, it can be set with the <i><a href="/docs/linux/man/3-curlopt_userpwd/">CURLOPT_USERPWD</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a>(3)</i> option. </p>
<p> <a href="scp://user@example.com/etc/issue">scp://user@example.com/etc/issue</a> &#8211; This specifies the file /etc/issue </p>
<p> <a href="scp://example.com/~/my-file">scp://example.com/~/my-file</a> &#8211; This specifies the file my-file in the user&#8217;s home directory on the server </p>
<dt>SFTP</p>
<dd>The path part of a SFTP request specifies the file to retrieve and from what directory. If the file part is omitted then libcurl downloads the directory listing for the directory specified. If the path ends in a / then a directory listing is returned instead of a file. If the path is omitted entirely then the directory listing for the root / home directory will be returned. If the user name is not embedded in the URL, it can be set with the <i><a href="/docs/linux/man/3-curlopt_userpwd/">CURLOPT_USERPWD</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a>(3)</i> option. </p>
<p> <a href="sftp://user:password@example.com/etc/issue">sftp://user:password@example.com/etc/issue</a> &#8211; This specifies the file /etc/issue </p>
<p> <a href="sftp://user@example.com/~/my-file">sftp://user@example.com/~/my-file</a> &#8211; This specifies the file my-file in the user&#8217;s home directory </p>
<p> <a href="sftp://ssh.example.com/~/Documents/">sftp://ssh.example.com/~/Documents/</a> &#8211; This requests a directory listing of the Documents directory under the user&#8217;s home directory </p>
<dt>SMB</p>
<dd>The path part of a SMB request specifies the file to retrieve and from what share and directory or the share to upload to and as such, may not be omitted. If the user name is not embedded in the URL, it can be set with the <i><a href="/docs/linux/man/3-curlopt_userpwd/">CURLOPT_USERPWD</a>(3)</i> or <i><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a>(3)</i> option. If the user name is embedded in the URL then it must contain the domain name and as such, the backslash must be URL encoded as %2f. </p>
<p> <a href="smb://server.example.com/files/issue">smb://server.example.com/files/issue</a> &#8211; This specifies the file &quot;issue&quot; located in the root of the &quot;files&quot; share </p>
<p> <a href="smb://server.example.com/files/">smb://server.example.com/files/</a> -T issue &#8211; This specifies the file &quot;issue&quot; will be uploaded to the root of the &quot;files&quot; share. </p>
<dt>LDAP</p>
<dd>The path part of a LDAP request can be used to specify the: Distinguished Name, Attributes, Scope, Filter and Extension for a LDAP search. Each field is separated by a question mark and when that field is not required an empty string with the question mark separator should be included. </p>
<p> <a href="ldap://ldap.example.com/o=My%20Organisation">ldap://ldap.example.com/o=My%20Organisation</a> &#8211; This will perform a LDAP search with the DN as My Organisation. </p>
<p> <a href="ldap://ldap.example.com/o=My%20Organisation?postalAddress">ldap://ldap.example.com/o=My%20Organisation?postalAddress</a> &#8211; This will perform the same search but will only return postalAddress attributes. </p>
<p> <a href="ldap://ldap.example.com/?rootDomainNamingContext">ldap://ldap.example.com/?rootDomainNamingContext</a> &#8211; This specifies an empty DN and requests information about the rootDomainNamingContext attribute for an Active Directory server. </p>
<p> For more information about the individual components of a LDAP URL please see RFC4516.</p>
<dt>RTMP</p>
<dd>There&#8217;s no official URL spec for RTMP so libcurl uses the URL syntax supported by the underlying librtmp library. It has a syntax where it wants a traditional URL, followed by a space and a series of space-separated name=value pairs. </p>
<p> While space is not typically a &quot;legal&quot; letter, libcurl accepts them. When a user wants to pass in a &#8216;#&#8217; (hash) character it will be treated as a fragment and get cut off by libcurl if provided literally. You will instead have to escape it by providing it as backslash and its ASCII value in hexadecimal: &quot;\23&quot;.</dl>
<h2>Default</h2>
<p>There is no default URL. If this option isn&#8217;t set, no transfer can be performed.</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<pre>CURL *curl = curl_easy_init();
if(curl) {
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com">http://example.com</a>&quot;);
 curl_easy_perform(curl);
}</pre>
<h2>Availability</h2>
<p>POP3 and SMTP were added in 7.31.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK on success or CURLE_OUT_OF_MEMORY if there was insufficient heap space. </p>
<p> Note that <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> won&#8217;t actually parse the given string so given a bad URL, it will not be detected until <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> or similar is called.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_verbose/">CURLOPT_VERBOSE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_protocols/">CURLOPT_PROTOCOLS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_forbid_reuse/">CURLOPT_FORBID_REUSE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_fresh_connect/">CURLOPT_FRESH_CONNECT</a></code>(3), <code><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a></code>(3)</p>
