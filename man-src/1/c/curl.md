---
title: "curl(1)"
name: "curl"
section: "1"
letter: "c"
url: "/docs/linux/man/1-curl/"
description: "curl – transfer a URL"
---

<h2 class="name">NAME</h2>
<p> curl &#8211; transfer a URL </p>
<h2>SYNOPSIS</h2>
<p> <code>curl [options / URLs]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>curl</code> is a tool for transferring data from or to a server. It supports these protocols: DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, RTMP, RTMPS, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET or TFTP. The command is designed to work without user interaction. </p>
<p> curl offers a busload of useful tricks like proxy support, user authentication, FTP upload, HTTP post, SSL connections, cookies, file transfer resume and more. As you will see below, the number of features will make your head spin. </p>
<p> curl is powered by libcurl for all transfer-related features. See <i><a href="/docs/linux/man/3-libcurl/">libcurl</a>(3)</i> for details.</p>
<h2>URL</h2>
<p> The URL syntax is protocol-dependent. You find a detailed description in RFC 3986. </p>
<p> You can specify multiple URLs or parts of URLs by writing part sets within braces and quoting the URL as in: </p>
<pre>
  &quot;<a rel="nofollow" href="http://site.{one,two,three}.com">http://site.{one,two,three}.com</a>&quot;
</pre>
<p> or you can get sequences of alphanumeric series by using [] as in: </p>
<pre>
  &quot;<a href="ftp://ftp.example.com/file[1-100].txt">ftp://ftp.example.com/file[1-100].txt</a>&quot;
</pre>
<pre>
  &quot;<a href="ftp://ftp.example.com/file[001-100].txt">ftp://ftp.example.com/file[001-100].txt</a>&quot;    (with leading zeros)
</pre>
<pre>
  &quot;<a href="ftp://ftp.example.com/file[a-z].txt">ftp://ftp.example.com/file[a-z].txt</a>&quot;
</pre>
<p> Nested sequences are not supported, but you can use several ones next to each other: </p>
<pre><code>
"http://example.com/archive[1996-1999]/vol[1-4]/part{a,b,c}.html"
</code></pre>
<p> You can specify any amount of URLs on the command line. They will be fetched in a sequential manner in the specified order. You can specify command line options and URLs mixed and in any order on the command line. </p>
<p> You can specify a step counter for the ranges to get every Nth number or letter: </p>
<pre>
  &quot;<a rel="nofollow" href="http://example.com/file[1-100:10].txt">http://example.com/file[1-100:10].txt</a>&quot;
</pre>
<pre>
  &quot;<a rel="nofollow" href="http://example.com/file[a-z:2].txt">http://example.com/file[a-z:2].txt</a>&quot;
</pre>
<p> When using [] or {} sequences when invoked from a command line prompt, you probably have to put the full URL within double quotes to avoid the shell from interfering with it. This also goes for other characters treated special, like for example &#8216;&amp;&#8217;, &#8216;?&#8217; and &#8216;*&#8217;. </p>
<p> Provide the IPv6 zone index in the URL with an escaped percentage sign and the interface name. Like in </p>
<pre>
  &quot;<a rel="nofollow" href="http://[fe80::3%25eth0]/">http://[fe80::3%25eth0]/</a>&quot;
</pre>
<p> If you specify URL without protocol:// prefix, curl will attempt to guess what protocol you might want. It will then default to HTTP but try other protocols based on often-used host name prefixes. For example, for host names starting with &quot;ftp.&quot; curl will assume you want to speak FTP. </p>
<p> curl will do its best to use what you pass to it as a URL. It is not trying to validate it as a syntactically correct URL by any means but is fairly liberal with what it accepts. </p>
<p> curl will attempt to re-use connections for multiple file transfers, so that getting many files from the same server will not do multiple connects / handshakes. This improves speed. Of course this is only done on files specified on a single command line and cannot be used between separate curl invocations.</p>
<h2>OUTPUT</h2>
<p> If not told otherwise, curl writes the received data to stdout. It can be instructed to instead save that data into a local file, using the <i>-o, &#8211;output</i> or <i>-O, &#8211;remote-name</i> options. If curl is given multiple URLs to transfer on the command line, it similarly needs multiple options for where to save them. </p>
<p> curl does not parse or otherwise &quot;understand&quot; the content it gets or writes as output. It does no encoding or decoding, unless explicitly asked to with dedicated command line options.</p>
<h2>PROTOCOLS</h2>
<p> curl supports numerous protocols, or put in URL terms: schemes. Your particular build may not support them all.</p>
<dl>
<dt>DICT</p>
<dd> Lets you lookup words using online dictionaries.</p>
<dt>FILE</p>
<dd> Read or write local files. curl does not support accessing file:// URL remotely, but when running on Microsoft Windows using the native UNC approach will work.</p>
<dt>FTP(S)</p>
<dd> curl supports the File Transfer Protocol with a lot of tweaks and levers. With or without using TLS.</p>
<dt>GOPHER(S)</p>
<dd> Retrieve files.</p>
<dt>HTTP(S)</p>
<dd> curl supports HTTP with numerous options and variations. It can speak HTTP version 0.9, 1.0, 1.1, 2 and 3 depending on build options and the correct command line options.</p>
<dt>IMAP(S)</p>
<dd> Using the mail reading protocol, curl can &quot;download&quot; emails for you. With or without using TLS.</p>
<dt>LDAP(S)</p>
<dd> curl can do directory lookups for you, with or without TLS.</p>
<dt>MQTT</p>
<dd> curl supports MQTT version 3. Downloading over MQTT equals &quot;subscribe&quot; to a topic while uploading/posting equals &quot;publish&quot; on a topic. MQTT over TLS is not supported (yet).</p>
<dt>POP3(S)</p>
<dd> Downloading from a pop3 server means getting a mail. With or without using TLS.</p>
<dt>RTMP(S)</p>
<dd> The Realtime Messaging Protocol is primarily used to server streaming media and curl can download it.</p>
<dt>RTSP</p>
<dd> curl supports RTSP 1.0 downloads.</p>
<dt>SCP</p>
<dd> curl supports SSH version 2 scp transfers.</p>
<dt>SFTP</p>
<dd> curl supports SFTP (draft 5) done over SSH version 2.</p>
<dt>SMB(S)</p>
<dd> curl supports SMB version 1 for upload and download.</p>
<dt>SMTP(S)</p>
<dd> Uploading contents to an SMTP server means sending an email. With or without TLS.</p>
<dt>TELNET</p>
<dd> Telling curl to fetch a telnet URL starts an interactive session where it sends what it reads on stdin and outputs what the server sends it.</p>
<dt>TFTP</p>
<dd> curl can do TFTP downloads and uploads.</dl>
<h2>PROGRESS METER</h2>
<p> curl normally displays a progress meter during operations, indicating the amount of transferred data, transfer speeds and estimated time left, etc. The progress meter displays number of bytes and the speeds are in bytes per second. The suffixes (k, M, G, T, P) are 1024 based. For example 1k is 1024 bytes. 1M is 1048576 bytes. </p>
<p> curl displays this data to the terminal by default, so if you invoke curl to do an operation and it is about to write data to the terminal, it <i>disables</i> the progress meter as otherwise it would mess up the output mixing progress meter and response data. </p>
<p> If you want a progress meter for HTTP POST or PUT requests, you need to redirect the response output to a file, using shell redirect (&gt;), <i>-o, &#8211;output</i> or similar. </p>
<p> This does not apply to FTP upload as that operation does not spit out any response data to the terminal. </p>
<p> If you prefer a progress &quot;bar&quot; instead of the regular meter, <i>-#, &#8211;progress-bar</i> is your friend. You can also disable the progress meter completely with the <i>-s, &#8211;silent</i> option.</p>
<h2>OPTIONS</h2>
<p> Options start with one or two dashes. Many of the options require an additional value next to them. </p>
<p> The short &quot;single-dash&quot; form of the options, -d for example, may be used with or without a space between it and its value, although a space is a recommended separator. The long &quot;double-dash&quot; form, <i>-d, &#8211;data</i> for example, requires a space between it and its value. </p>
<p> Short version options that do not need any additional values can be used immediately next to each other, like for example you can specify all the options -O, -L and -v at once as -OLv. </p>
<p> In general, all boolean options are enabled with &#8212;<code>option</code> and yet again disabled with &#8212;<code>no-</code>option. That is, you use the same option name but prefix it with &quot;no-&quot;. However, in this list we mostly only list and show the &#8211;option version of them.</p>
<dl>
<dt>&#8211;abstract-unix-socket &lt;path&gt;</p>
<dd> (HTTP) Connect through an abstract Unix domain socket, instead of using the network. Note: netstat shows the path of an abstract socket prefixed with &#8216;@&#8217;, however the &lt;path&gt; argument should not have this leading character. </p>
<p> Example: </p>
<pre>
 curl --abstract-unix-socket socketpath <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;unix-socket</i>. Added in 7.53.0.</p>
<dt>&#8211;alt-svc &lt;file name&gt;</p>
<dd> (HTTPS) This option enables the alt-svc parser in curl. If the file name points to an existing alt-svc cache file, that will be used. After a completed transfer, the cache will be saved to the file name again if it has been modified. </p>
<p> Specify a &quot;&quot; file name (zero length) to avoid loading/saving and make curl just handle the cache in memory. </p>
<p> If this option is used several times, curl will load contents from all the files but the last one will be used for saving. </p>
<p> Example: </p>
<pre>
 curl --alt-svc svc.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;resolve</i> and <i>&#8211;connect-to</i>. Added in 7.64.1.</p>
<dt>&#8211;anyauth</p>
<dd> (HTTP) Tells curl to figure out authentication method by itself, and use the most secure one the remote site claims to support. This is done by first doing a request and checking the response-headers, thus possibly inducing an extra network round-trip. This is used instead of setting a specific authentication method, which you can do with <i>&#8211;basic</i>, <i>&#8211;digest</i>, <i>&#8211;ntlm</i>, and <i>&#8211;negotiate</i>. </p>
<p> Using <i>&#8211;anyauth</i> is not recommended if you do uploads from stdin, since it may require data to be sent twice and then the client must be able to rewind. If the need should arise when uploading from stdin, the upload operation will fail. </p>
<p> Used together with <i>-u, &#8211;user</i>. </p>
<p> Example: </p>
<pre>
 curl --anyauth --user me:pwd <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-anyauth</i>, <i>&#8211;basic</i> and <i>&#8211;digest</i>.</p>
<dt>-a, &#8211;append</p>
<dd> (FTP SFTP) When used in an upload, this makes curl append to the target file instead of overwriting it. If the remote file does not exist, it will be created. Note that this flag is ignored by some SFTP servers (including OpenSSH). </p>
<p> Example: </p>
<pre>
 curl --upload-file local --append <a href="ftp://example.com/">ftp://example.com/</a>
</pre>
<p> See also <i>-r, &#8211;range</i> and <i>-C, &#8211;continue-at</i>.</p>
<dt>&#8211;aws-sigv4 &lt;provider1[:provider2[:region[:service]]]&gt;</p>
<dd> Use AWS V4 signature authentication in the transfer. </p>
<p> The provider argument is a string that is used by the algorithm when creating outgoing authentication headers. </p>
<p> The region argument is a string that points to a geographic area of a resources collection (region-code) when the region name is omitted from the endpoint. </p>
<p> The service argument is a string that points to a function provided by a cloud (service-code) when the service name is omitted from the endpoint. </p>
<p> Example: </p>
<pre>
 curl --aws-sigv4 &quot;aws:amz:east-2:es&quot; --user &quot;key:secret&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;basic</i> and <i>-u, &#8211;user</i>. Added in 7.75.0.</p>
<dt>&#8211;basic</p>
<dd> (HTTP) Tells curl to use HTTP Basic authentication with the remote host. This is the default and this option is usually pointless, unless you use it to override a previously set option that sets a different authentication method (such as <i>&#8211;ntlm</i>, <i>&#8211;digest</i>, or <i>&#8211;negotiate</i>). </p>
<p> Used together with <i>-u, &#8211;user</i>. </p>
<p> Example: </p>
<pre>
 curl -u name:password --basic <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-basic</i>.</p>
<dt>&#8211;cacert &lt;file&gt;</p>
<dd> (TLS) Tells curl to use the specified certificate file to verify the peer. The file may contain multiple CA certificates. The certificate(s) must be in PEM format. Normally curl is built to use a default file for this, so this option is typically used to alter that default file. </p>
<p> curl recognizes the environment variable named &#8216;CURL_CA_BUNDLE&#8217; if it is set, and uses the given path as a path to a CA cert bundle. This option overrides that variable. </p>
<p> The windows version of curl will automatically look for a CA certs file named &#8216;curl-ca-bundle.crt&#8217;, either in the same directory as curl.exe, or in the Current Working Directory, or in any folder along your PATH. </p>
<p> If curl is built against the NSS SSL library, the NSS PEM PKCS#11 module (libnsspem.so) needs to be available for this option to work properly. </p>
<p> (iOS and macOS only) If curl is built against Secure Transport, then this option is supported for backward compatibility with other SSL engines, but it should not be set. If the option is not set, then curl will use the certificates in the system and user Keychain to verify the peer, which is the preferred method of verifying the peer&#8217;s certificate chain. </p>
<p> (Schannel only) This option is supported for Schannel in Windows 7 or later with libcurl 7.60 or later. This option is supported for backward compatibility with other SSL engines; instead it is recommended to use Windows&#8217; store of root certificates (the default for Schannel). </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --cacert CA-file.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;capath</i> and <i>-k, &#8211;insecure</i>.</p>
<dt>&#8211;capath &lt;dir&gt;</p>
<dd> (TLS) Tells curl to use the specified certificate directory to verify the peer. Multiple paths can be provided by separating them with &quot;:&quot; (e.g. &quot;path1:path2:path3&quot;). The certificates must be in PEM format, and if curl is built against OpenSSL, the directory must have been processed using the c_rehash utility supplied with OpenSSL. Using <i>&#8211;capath</i> can allow OpenSSL-powered curl to make SSL-connections much more efficiently than using <i>&#8211;cacert</i> if the &#8211;cacert file contains many CA certificates. </p>
<p> If this option is set, the default capath value will be ignored, and if it is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --capath /local/directory <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;cacert</i> and <i>-k, &#8211;insecure</i>.</p>
<dt>&#8211;cert-status</p>
<dd> (TLS) Tells curl to verify the status of the server certificate by using the Certificate Status Request (aka. OCSP stapling) TLS extension. </p>
<p> If this option is enabled and the server sends an invalid (e.g. expired) response, if the response suggests that the server certificate has been revoked, or no response at all is received, the verification fails. </p>
<p> This is currently only implemented in the OpenSSL, GnuTLS and NSS backends. </p>
<p> Example: </p>
<pre>
 curl --cert-status <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;pinnedpubkey</i>. Added in 7.41.0.</p>
<dt>&#8211;cert-type &lt;type&gt;</p>
<dd> (TLS) Tells curl what type the provided client certificate is using. PEM, DER, ENG and P12 are recognized types. If not specified, PEM is assumed. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --cert-type PEM --cert file <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-E, &#8211;cert</i>, <i>&#8211;key</i> and <i>&#8211;key-type</i>.</p>
<dt>-E, &#8211;cert &lt;certificate[:password]&gt;</p>
<dd> (TLS) Tells curl to use the specified client certificate file when getting a file with HTTPS, FTPS or another SSL-based protocol. The certificate must be in PKCS#12 format if using Secure Transport, or PEM format if using any other engine. If the optional password is not specified, it will be queried for on the terminal. Note that this option assumes a &quot;certificate&quot; file that is the private key and the client certificate concatenated! See <i>-E, &#8211;cert</i> and <i>&#8211;key</i> to specify them independently. </p>
<p> If curl is built against the NSS SSL library then this option can tell curl the nickname of the certificate to use within the NSS database defined by the environment variable SSL_DIR (or by default /etc/pki/nssdb). If the NSS PEM PKCS#11 module (libnsspem.so) is available then PEM files may be loaded. If you want to use a file from the current directory, please precede it with &quot;./&quot; prefix, in order to avoid confusion with a nickname. If the nickname contains &quot;:&quot;, it needs to be preceded by &quot;\&quot; so that it is not recognized as password delimiter. If the nickname contains &quot;\&quot;, it needs to be escaped as &quot;\&quot; so that it is not recognized as an escape character. </p>
<p> If curl is built against OpenSSL library, and the engine pkcs11 is available, then a PKCS#11 URI (RFC 7512) can be used to specify a certificate located in a PKCS#11 device. A string beginning with &quot;pkcs11:&quot; will be interpreted as a PKCS#11 URI. If a PKCS#11 URI is provided, then the <i>&#8211;engine</i> option will be set as &quot;pkcs11&quot; if none was provided and the <i>&#8211;cert-type</i> option will be set as &quot;ENG&quot; if none was provided. </p>
<p> (iOS and macOS only) If curl is built against Secure Transport, then the certificate string can either be the name of a certificate/private key in the system or user keychain, or the path to a PKCS#12-encoded certificate and private key. If you want to use a file from the current directory, please precede it with &quot;./&quot; prefix, in order to avoid confusion with a nickname. </p>
<p> (Schannel only) Client certificates must be specified by a path expression to a certificate store. (Loading PFX is not supported; you can import it to a store first). You can use &quot;&lt;store location&gt;\&lt;store name&gt;\&lt;thumbprint&gt;&quot; to refer to a certificate in the system certificates store, for example, &quot;CurrentUser\MY\934a7ac6f8a5d579285a74fa61e19f23ddfe8d7a&quot;. Thumbprint is usually a SHA-1 hex string which you can see in certificate details. Following store locations are supported: CurrentUser, LocalMachine, CurrentService, Services, CurrentUserGroupPolicy, LocalMachineGroupPolicy, LocalMachineEnterprise. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --cert certfile --key keyfile <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;cert-type</i>, <i>&#8211;key</i> and <i>&#8211;key-type</i>.</p>
<dt>&#8211;ciphers &lt;list of ciphers&gt;</p>
<dd> (TLS) Specifies which ciphers to use in the connection. The list of ciphers must specify valid ciphers. Read up on SSL cipher list details on this URL: </p>
<pre>
 <a rel="nofollow" href="https://curl.se/docs/ssl-ciphers.html">https://curl.se/docs/ssl-ciphers.html</a>
</pre>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --ciphers ECDHE-ECDSA-AES256-CCM8 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;tlsv1.3</i>.</p>
<dt>&#8211;compressed-ssh</p>
<dd> (SCP SFTP) Enables built-in SSH compression. This is a request, not an order; the server may or may not do it. </p>
<p> Example: </p>
<pre>
 curl --compressed-ssh <a href="sftp://example.com/">sftp://example.com/</a>
</pre>
<p> See also <i>&#8211;compressed</i>. Added in 7.56.0.</p>
<dt>&#8211;compressed</p>
<dd> (HTTP) Request a compressed response using one of the algorithms curl supports, and automatically decompress the content. Headers are not modified. </p>
<p> If this option is used and the server sends an unsupported encoding, curl will report an error. This is a request, not an order; the server may or may not deliver data compressed. </p>
<p> Example: </p>
<pre>
 curl --compressed <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;compressed-ssh</i>.</p>
<dt>-K, &#8211;config &lt;file&gt;</p>
<dd> Specify a text file to read curl arguments from. The command line arguments found in the text file will be used as if they were provided on the command line. </p>
<p> Options and their parameters must be specified on the same line in the file, separated by whitespace, colon, or the equals sign. Long option names can optionally be given in the config file without the initial double dashes and if so, the colon or equals characters can be used as separators. If the option is specified with one or two dashes, there can be no colon or equals character between the option and its parameter. </p>
<p> If the parameter contains whitespace (or starts with : or =), the parameter must be enclosed within quotes. Within double quotes, the following escape sequences are available: \, \&quot;, 	, 
,  and . A backslash preceding any other letter is ignored. </p>
<p> If the first column of a config line is a &#8216;#&#8217; character, the rest of the line will be treated as a comment. </p>
<p> Only write one option per physical line in the config file. </p>
<p> Specify the filename to <i>-K, &#8211;config</i> as &#8216;-&#8216; to make curl read the file from stdin. </p>
<p> Note that to be able to specify a URL in the config file, you need to specify it using the <i>&#8211;url</i> option, and not by simply writing the URL on its own line. So, it could look similar to this: </p>
<p> url = &quot;<a rel="nofollow" href="https://curl.se/docs/">https://curl.se/docs/</a>&quot; </p>
<pre>
 # --- Example file ---
 # this is a comment
 url = &quot;example.com&quot;
 output = &quot;curlhere.html&quot;
 user-agent = &quot;superagent/1.0&quot;
</pre>
<pre>
 # and fetch another URL too
 url = &quot;example.com/docs/manpage.html&quot;
 -O
 referer = &quot;<a rel="nofollow" href="http://nowhereatall.example.com/">http://nowhereatall.example.com/</a>&quot;
 # --- End of example file ---
</pre>
<p> When curl is invoked, it (unless <i>-q, &#8211;disable</i> is used) checks for a default config file and uses it if found, even when <i>-K, &#8211;config</i> is used. The default config file is checked for in the following places in this order: </p>
<p> 1) &quot;$CURL_HOME/.curlrc&quot; </p>
<p> 2) &quot;$XDG_CONFIG_HOME/.curlrc&quot; (Added in 7.73.0) </p>
<p> 3) &quot;$HOME/.curlrc&quot; </p>
<p> 4) Windows: &quot;%USERPROFILE%\.curlrc&quot; </p>
<p> 5) Windows: &quot;%APPDATA%\.curlrc&quot; </p>
<p> 6) Windows: &quot;%USERPROFILE%\Application Data\.curlrc&quot; </p>
<p> 7) Non-windows: use getpwuid to find the home directory </p>
<p> 8) On windows, if it finds no .curlrc file in the sequence described above, it checks for one in the same dir the curl executable is placed. </p>
<p> This option can be used multiple times to load multiple config files. </p>
<p> Example: </p>
<pre>
 curl --config file.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-q, &#8211;disable</i>.</p>
<dt>&#8211;connect-timeout &lt;fractional seconds&gt;</p>
<dd> Maximum time in seconds that you allow curl&#8217;s connection to take. This only limits the connection phase, so if curl connects within the given period it will continue &#8211; if not it will exit. Since version 7.32.0, this option accepts decimal values. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Examples: </p>
<pre>
 curl --connect-timeout 20 <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl --connect-timeout 3.14 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-m, &#8211;max-time</i>.</p>
<dt>&#8211;connect-to &lt;HOST1:PORT1:HOST2:PORT2&gt;</p>
<dd>
<p> For a request to the given HOST1:PORT1 pair, connect to HOST2:PORT2 instead. This option is suitable to direct requests at a specific server, e.g. at a specific cluster node in a cluster of servers. This option is only used to establish the network connection. It does NOT affect the hostname/port that is used for TLS/SSL (e.g. SNI, certificate verification) or for the application protocols. &quot;HOST1&quot; and &quot;PORT1&quot; may be the empty string, meaning &quot;any host/port&quot;. &quot;HOST2&quot; and &quot;PORT2&quot; may also be the empty string, meaning &quot;use the request&#8217;s original host/port&quot;. </p>
<p> A &quot;host&quot; specified to this option is compared as a string, so it needs to match the name used in request URL. It can be either numerical such as &quot;127.0.0.1&quot; or the full host name such as &quot;example.org&quot;. </p>
<p> This option can be used many times to add many connect rules. </p>
<p> Example: </p>
<pre>
 curl --connect-to example.com:443:example.net:8443 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;resolve</i> and <i>-H, &#8211;header</i>. Added in 7.49.0.</p>
<dt>-C, &#8211;continue-at &lt;offset&gt;</p>
<dd> Continue/Resume a previous file transfer at the given offset. The given offset is the exact number of bytes that will be skipped, counting from the beginning of the source file before it is transferred to the destination. If used with uploads, the FTP server command SIZE will not be used by curl. </p>
<p> Use &quot;-C -&quot; to tell curl to automatically find out where/how to resume the transfer. It then uses the given output/input files to figure that out. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Examples: </p>
<pre>
 curl -C - <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl -C 400 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-r, &#8211;range</i>.</p>
<dt>-c, &#8211;cookie-jar &lt;filename&gt;</p>
<dd> (HTTP) Specify to which file you want curl to write all cookies after a completed operation. Curl writes all cookies from its in-memory cookie storage to the given file at the end of operations. If no cookies are known, no data will be written. The file will be written using the Netscape cookie file format. If you set the file name to a single dash, &quot;-&quot;, the cookies will be written to stdout. </p>
<p> This command line option will activate the cookie engine that makes curl record and use cookies. Another way to activate it is to use the <i>-b, &#8211;cookie</i> option. </p>
<p> If the cookie jar cannot be created or written to, the whole curl operation will not fail or even report an error clearly. Using <i>-v, &#8211;verbose</i> will get a warning displayed, but that is the only visible feedback you get about this possibly lethal situation. </p>
<p> If this option is used several times, the last specified file name will be used. </p>
<p> Examples: </p>
<pre>
 curl -c store-here.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl -c store-here.txt -b read-these <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-b, &#8211;cookie</i>.</p>
<dt>-b, &#8211;cookie &lt;data|filename&gt;</p>
<dd> (HTTP) Pass the data to the HTTP server in the Cookie header. It is supposedly the data previously received from the server in a &quot;Set-Cookie:&quot; line. The data should be in the format &quot;NAME1=VALUE1; NAME2=VALUE2&quot;. </p>
<p> If no &#8216;=&#8217; symbol is used in the argument, it is instead treated as a filename to read previously stored cookie from. This option also activates the cookie engine which will make curl record incoming cookies, which may be handy if you are using this in combination with the <i>-L, &#8211;location</i> option or do multiple URL transfers on the same invoke. If the file name is exactly a minus (&quot;-&quot;), curl will instead read the contents from stdin. </p>
<p> The file format of the file to read cookies from should be plain HTTP headers (Set-Cookie style) or the Netscape/Mozilla cookie file format. </p>
<p> The file specified with <i>-b, &#8211;cookie</i> is only used as input. No cookies will be written to the file. To store cookies, use the <i>-c, &#8211;cookie-jar</i> option. </p>
<p> If you use the Set-Cookie file format and do not specify a domain then the cookie is not sent since the domain will never match. To address this, set a domain in Set-Cookie line (doing that will include sub-domains) or preferably: use the Netscape format. </p>
<p> This option can be used multiple times. </p>
<p> Users often want to both read cookies from a file and write updated cookies back to a file, so using both <i>-b, &#8211;cookie</i> and <i>-c, &#8211;cookie-jar</i> in the same command line is common. </p>
<p> Examples: </p>
<pre>
 curl -b cookiefile <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl -b cookiefile -c cookiefile <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-c, &#8211;cookie-jar</i> and <i>-j, &#8211;junk-session-cookies</i>.</p>
<dt>&#8211;create-dirs</p>
<dd> When used in conjunction with the <i>-o, &#8211;output</i> option, curl will create the necessary local directory hierarchy as needed. This option creates the directories mentioned with the <i>-o, &#8211;output</i> option, nothing else. If the &#8211;output file name uses no directory, or if the directories it mentions already exist, no directories will be created. </p>
<p> Created dirs are made with mode 0750 on unix style file systems. </p>
<p> To create remote directories when using FTP or SFTP, try <i>&#8211;ftp-create-dirs</i>. </p>
<p> Example: </p>
<pre>
 curl --create-dirs --output local/dir/file <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;ftp-create-dirs</i> and <i>&#8211;output-dir</i>.</p>
<dt>&#8211;create-file-mode &lt;mode&gt;</p>
<dd> (SFTP SCP FILE) When curl is used to create files remotely using one of the supported protocols, this option allows the user to set which &#8216;mode&#8217; to set on the file at creation time, instead of the default 0644. </p>
<p> This option takes an octal number as argument. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --create-file-mode 0777 -T localfile <a href="sftp://example.com/new">sftp://example.com/new</a>
</pre>
<p> See also <i>&#8211;ftp-create-dirs</i>. Added in 7.75.0.</p>
<dt>&#8211;crlf</p>
<dd> (FTP SMTP) Convert LF to CRLF in upload. Useful for MVS (OS/390). </p>
<p> (SMTP added in 7.40.0) </p>
<p> Example: </p>
<pre>
 curl --crlf -T file <a href="ftp://example.com/">ftp://example.com/</a>
</pre>
<p> See also <i>-B, &#8211;use-ascii</i>.</p>
<dt>&#8211;crlfile &lt;file&gt;</p>
<dd> (TLS) Provide a file using PEM format with a Certificate Revocation List that may specify peer certificates that are to be considered revoked. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --crlfile rejects.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;cacert</i> and <i>&#8211;capath</i>.</p>
<dt>&#8211;curves &lt;algorithm list&gt;</p>
<dd> (TLS) Tells curl to request specific curves to use during SSL session establishment according to RFC 8422, 5.1. Multiple algorithms can be provided by separating them with &quot;:&quot; (e.g. &quot;X25519:P-521&quot;). The parameter is available identically in the &quot;openssl s_client/s_server&quot; utilities. </p>
<p> <i>&#8211;curves</i> allows a OpenSSL powered curl to make SSL-connections with exactly the (EC) curve requested by the client, avoiding nontransparent client/server negotiations. </p>
<p> If this option is set, the default curves list built into openssl will be ignored. </p>
<p> Example: </p>
<pre>
 curl --curves X25519 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;ciphers</i>. Added in 7.73.0.</p>
<dt>&#8211;data-ascii &lt;data&gt;</p>
<dd> (HTTP) This is just an alias for <i>-d, &#8211;data</i>. </p>
<p> Example: </p>
<pre>
 curl --data-ascii @file <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;data-binary</i>, <i>&#8211;data-raw</i> and <i>&#8211;data-urlencode</i>.</p>
<dt>&#8211;data-binary &lt;data&gt;</p>
<dd> (HTTP) This posts data exactly as specified with no extra processing whatsoever. </p>
<p> If you start the data with the letter @, the rest should be a filename. Data is posted in a similar manner as <i>-d, &#8211;data</i> does, except that newlines and carriage returns are preserved and conversions are never done. </p>
<p> Like <i>-d, &#8211;data</i> the default content-type sent to the server is application/x-www-form-urlencoded. If you want the data to be treated as arbitrary binary data by the server then set the content-type to octet-stream: -H &quot;Content-Type: application/octet-stream&quot;. </p>
<p> If this option is used several times, the ones following the first will append data as described in <i>-d, &#8211;data</i>. </p>
<p> Example: </p>
<pre>
 curl --data-binary @filename <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;data-ascii</i>.</p>
<dt>&#8211;data-raw &lt;data&gt;</p>
<dd> (HTTP) This posts data similarly to <i>-d, &#8211;data</i> but without the special interpretation of the @ character. </p>
<p> Examples: </p>
<pre>
 curl --data-raw &quot;hello&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl --data-raw &quot;@at@at@&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-d, &#8211;data</i>. Added in 7.43.0.</p>
<dt>&#8211;data-urlencode &lt;data&gt;</p>
<dd> (HTTP) This posts data, similar to the other <i>-d, &#8211;data</i> options with the exception that this performs URL-encoding. </p>
<p> To be CGI-compliant, the &lt;data&gt; part should begin with a <i>name</i> followed by a separator and a content specification. The &lt;data&gt; part can be passed to curl using one of the following syntaxes:</p>
<dl>
<dt>
<dd>
<dl>
<dt>content</p>
<dd> This will make curl URL-encode the content and pass that on. Just be careful so that the content does not contain any = or @ symbols, as that will then make the syntax match one of the other cases below!</p>
<dt>=content</p>
<dd> This will make curl URL-encode the content and pass that on. The preceding = symbol is not included in the data.</p>
<dt>name=content</p>
<dd> This will make curl URL-encode the content part and pass that on. Note that the name part is expected to be URL-encoded already.</p>
<dt>@filename</p>
<dd> This will make curl load data from the given file (including any newlines), URL-encode that data and pass it on in the POST.</p>
<dt>name [at] filename</p>
<dd> This will make curl load data from the given file (including any newlines), URL-encode that data and pass it on in the POST. The name part gets an equal sign appended, resulting in <i>name=urlencoded-file-content</i>. Note that the name is expected to be URL-encoded already.</dl>
</dl>
<p> Examples:<br />
curl&#8211; data &#8211; urlencode name = val https : // example.com<br />
                                           curl&#8211; data &#8211;<br />
                                           urlencode = encodethis https : // example.com<br />
                                                                          curl&#8211; data &#8211;<br />
                                                                          urlencode name[at] file https : // example.com<br />
                                                                                                          curl&#8211; data &#8211;<br />
                                                                                                          urlencode @fileonly https: // example.com</p>
<p> See also <i>-d, &#8211;data</i> and <i>&#8211;data-raw</i>.</p>
<dt>-d, &#8211;data &lt;data&gt;</p>
<dd> (HTTP MQTT) Sends the specified data in a POST request to the HTTP server, in the same way that a browser does when a user has filled in an HTML form and presses the submit button. This will cause curl to pass the data to the server using the content-type application/x-www-form-urlencoded. Compare to <i>-F, &#8211;form</i>. </p>
<p> <i>&#8211;data-raw</i> is almost the same but does not have a special interpretation of the @ character. To post data purely binary, you should instead use the <i>&#8211;data-binary</i> option. To URL-encode the value of a form field you may use <i>&#8211;data-urlencode</i>. </p>
<p> If any of these options is used more than once on the same command line, the data pieces specified will be merged with a separating &amp;-symbol. Thus, using &#8216;-d name=daniel -d skill=lousy&#8217; would generate a post chunk that looks like &#8216;name=daniel&amp;skill=lousy&#8217;. </p>
<p> If you start the data with the letter @, the rest should be a file name to read the data from, or &#8211; if you want curl to read the data from stdin. Posting data from a file named &#8216;foobar&#8217; would thus be done with <i>-d, &#8211;data</i> @foobar. When <i>-d, &#8211;data</i> is told to read from a file like that, carriage returns and newlines will be stripped out. If you do not want the @ character to have a special interpretation use <i>&#8211;data-raw</i> instead. </p>
<p> Examples: </p>
<pre>
 curl -d &quot;name=curl&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl -d &quot;name=curl&quot; -d &quot;tool=cmdline&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl -d @filename <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;data-binary</i>, <i>&#8211;data-urlencode</i> and <i>&#8211;data-raw</i>. This option overrides <i>-F, &#8211;form</i> and <i>-I, &#8211;head</i> and <i>-T, &#8211;upload-file</i>.</p>
<dt>&#8211;delegation &lt;LEVEL&gt;</p>
<dd> (GSS/kerberos) Set LEVEL to tell the server what it is allowed to delegate when it comes to user credentials.</p>
<dl>
<dt>
<dd>
<dl>
<dt>none</p>
<dd> Do not allow any delegation.</p>
<dt>policy</p>
<dd> Delegates if and only if the OK-AS-DELEGATE flag is set in the Kerberos service ticket, which is a matter of realm policy.</p>
<dt>always</p>
<dd> Unconditionally allow the server to delegate.</dl>
</dl>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --delegation &quot;none&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-k, &#8211;insecure</i> and <i>&#8211;ssl</i>.</p>
<dt>&#8211;digest</p>
<dd> (HTTP) Enables HTTP Digest authentication. This is an authentication scheme that prevents the password from being sent over the wire in clear text. Use this in combination with the normal <i>-u, &#8211;user</i> option to set user name and password. </p>
<p> If this option is used several times, only the first one is used. </p>
<p> Example: </p>
<pre>
 curl -u name:password --digest <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-u, &#8211;user</i>, <i>&#8211;proxy-digest</i> and <i>&#8211;anyauth</i>. This option overrides <i>&#8211;basic</i> and <i>&#8211;ntlm</i> and <i>&#8211;negotiate</i>.</p>
<dt>&#8211;disable-eprt</p>
<dd> (FTP) Tell curl to disable the use of the EPRT and LPRT commands when doing active FTP transfers. Curl will normally always first attempt to use EPRT, then LPRT before using PORT, but with this option, it will use PORT right away. EPRT and LPRT are extensions to the original FTP protocol, and may not work on all servers, but they enable more functionality in a better way than the traditional PORT command. </p>
<p> &#8211;eprt can be used to explicitly enable EPRT again and &#8211;no-eprt is an alias for <i>&#8211;disable-eprt</i>. </p>
<p> If the server is accessed using IPv6, this option will have no effect as EPRT is necessary then. </p>
<p> Disabling EPRT only changes the active behavior. If you want to switch to passive mode you need to not use <i>-P, &#8211;ftp-port</i> or force it with <i>&#8211;ftp-pasv</i>. </p>
<p> Example: </p>
<pre>
 curl --disable-eprt <a href="ftp://example.com/">ftp://example.com/</a>
</pre>
<p> See also <i>&#8211;disable-epsv</i> and <i>-P, &#8211;ftp-port</i>.</p>
<dt>&#8211;disable-epsv</p>
<dd> (FTP) Tell curl to disable the use of the EPSV command when doing passive FTP transfers. Curl will normally always first attempt to use EPSV before PASV, but with this option, it will not try using EPSV. </p>
<p> &#8211;epsv can be used to explicitly enable EPSV again and &#8211;no-epsv is an alias for <i>&#8211;disable-epsv</i>. </p>
<p> If the server is an IPv6 host, this option will have no effect as EPSV is necessary then. </p>
<p> Disabling EPSV only changes the passive behavior. If you want to switch to active mode you need to use <i>-P, &#8211;ftp-port</i>. </p>
<p> Example: </p>
<pre>
 curl --disable-epsv <a href="ftp://example.com/">ftp://example.com/</a>
</pre>
<p> See also <i>&#8211;disable-eprt</i> and <i>-P, &#8211;ftp-port</i>.</p>
<dt>-q, &#8211;disable</p>
<dd> If used as the first parameter on the command line, the <i>curlrc</i> config file will not be read and used. See the <i>-K, &#8211;config</i> for details on the default config file search path. </p>
<p> Example: </p>
<pre>
 curl -q <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-K, &#8211;config</i>.</p>
<dt>&#8211;disallow-username-in-url</p>
<dd> (HTTP) This tells curl to exit if passed a url containing a username. This is probably most useful when the URL is being provided at run-time or similar. </p>
<p> Example: </p>
<pre>
 curl --disallow-username-in-url <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proto</i>. Added in 7.61.0.</p>
<dt>&#8211;dns-interface &lt;interface&gt;</p>
<dd> (DNS) Tell curl to send outgoing DNS requests through &lt;interface&gt;. This option is a counterpart to <i>&#8211;interface</i> (which does not affect DNS). The supplied string must be an interface name (not an address). </p>
<p> Example: </p>
<pre>
 curl --dns-interface eth0 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;dns-ipv4-addr</i> and <i>&#8211;dns-ipv6-addr</i>. <i>&#8211;dns-interface</i> requires that the underlying libcurl was built to support c-ares. Added in 7.33.0.</p>
<dt>&#8211;dns-ipv4-addr &lt;address&gt;</p>
<dd> (DNS) Tell curl to bind to &lt;ip-address&gt; when making IPv4 DNS requests, so that the DNS requests originate from this address. The argument should be a single IPv4 address. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --dns-ipv4-addr 10.1.2.3 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;dns-interface</i> and <i>&#8211;dns-ipv6-addr</i>. <i>&#8211;dns-ipv4-addr</i> requires that the underlying libcurl was built to support c-ares. Added in 7.33.0.</p>
<dt>&#8211;dns-ipv6-addr &lt;address&gt;</p>
<dd> (DNS) Tell curl to bind to &lt;ip-address&gt; when making IPv6 DNS requests, so that the DNS requests originate from this address. The argument should be a single IPv6 address. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --dns-ipv6-addr 2a04:4e42::561 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;dns-interface</i> and <i>&#8211;dns-ipv4-addr</i>. <i>&#8211;dns-ipv6-addr</i> requires that the underlying libcurl was built to support c-ares. Added in 7.33.0.</p>
<dt>&#8211;dns-servers &lt;addresses&gt;</p>
<dd> Set the list of DNS servers to be used instead of the system default. The list of IP addresses should be separated with commas. Port numbers may also optionally be given as <i>:&lt;port-number&gt;</i> after each IP address. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --dns-servers 192.168.0.1,192.168.0.2 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;dns-interface</i> and <i>&#8211;dns-ipv4-addr</i>. <i>&#8211;dns-servers</i> requires that the underlying libcurl was built to support c-ares. Added in 7.33.0.</p>
<dt>&#8211;doh-cert-status</p>
<dd> Same as <i>&#8211;cert-status</i> but used for DoH (DNS-over-HTTPS). </p>
<p> Example: </p>
<pre>
 curl --doh-cert-status --doh-url <a rel="nofollow" href="https://doh.example">https://doh.example</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;doh-insecure</i>. Added in 7.76.0.</p>
<dt>&#8211;doh-insecure</p>
<dd> Same as <i>-k, &#8211;insecure</i> but used for DoH (DNS-over-HTTPS). </p>
<p> Example: </p>
<pre>
 curl --doh-insecure --doh-url <a rel="nofollow" href="https://doh.example">https://doh.example</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;doh-url</i>. Added in 7.76.0.</p>
<dt>&#8211;doh-url &lt;URL&gt;</p>
<dd> Specifies which DNS-over-HTTPS (DoH) server to use to resolve hostnames, instead of using the default name resolver mechanism. The URL must be HTTPS. </p>
<p> Some SSL options that you set for your transfer will apply to DoH since the name lookups take place over SSL. However, the certificate verification settings are not inherited and can be controlled separately via <i>&#8211;doh-insecure</i> and <i>&#8211;doh-cert-status</i>. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --doh-url <a rel="nofollow" href="https://doh.example">https://doh.example</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;doh-insecure</i>. Added in 7.62.0.</p>
<dt>-D, &#8211;dump-header &lt;filename&gt;</p>
<dd> (HTTP FTP) Write the received protocol headers to the specified file. If no headers are received, the use of this option will create an empty file. </p>
<p> When used in FTP, the FTP server response lines are considered being &quot;headers&quot; and thus are saved there. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --dump-header store.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-o, &#8211;output</i>.</p>
<dt>&#8211;egd-file &lt;file&gt;</p>
<dd> (TLS) Specify the path name to the Entropy Gathering Daemon socket. The socket is used to seed the random engine for SSL connections. </p>
<p> Example: </p>
<pre>
 curl --egd-file /random/here <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;random-file</i>.</p>
<dt>&#8211;engine &lt;name&gt;</p>
<dd> (TLS) Select the OpenSSL crypto engine to use for cipher operations. Use <i>&#8211;engine</i> list to print a list of build-time supported engines. Note that not all (and possibly none) of the engines may be available at run-time. </p>
<p> Example: </p>
<pre>
 curl --engine flavor <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;ciphers</i> and <i>&#8211;curves</i>.</p>
<dt>&#8211;etag-compare &lt;file&gt;</p>
<dd> (HTTP) This option makes a conditional HTTP request for the specific ETag read from the given file by sending a custom If-None-Match header using the stored ETag. </p>
<p> For correct results, make sure that the specified file contains only a single line with the desired ETag. An empty file is parsed as an empty ETag. </p>
<p> Use the option <i>&#8211;etag-save</i> to first save the ETag from a response, and then use this option to compare against the saved ETag in a subsequent request. </p>
<p> Example: </p>
<pre>
 curl --etag-compare etag.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;etag-save</i> and <i>-z, &#8211;time-cond</i>. Added in 7.68.0.</p>
<dt>&#8211;etag-save &lt;file&gt;</p>
<dd> (HTTP) This option saves an HTTP ETag to the specified file. An ETag is a caching related header, usually returned in a response. </p>
<p> If no ETag is sent by the server, an empty file is created. </p>
<p> Example: </p>
<pre>
 curl --etag-save storetag.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;etag-compare</i>. Added in 7.68.0.</p>
<dt>&#8211;expect100-timeout &lt;seconds&gt;</p>
<dd> (HTTP) Maximum time in seconds that you allow curl to wait for a 100-continue response when curl emits an Expects: 100-continue header in its request. By default curl will wait one second. This option accepts decimal values! When curl stops waiting, it will continue as if the response has been received. </p>
<p> Example: </p>
<pre>
 curl --expect100-timeout 2.5 -T file <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;connect-timeout</i>. Added in 7.47.0.</p>
<dt>&#8211;fail-early</p>
<dd> Fail and exit on the first detected transfer error. </p>
<p> When curl is used to do multiple transfers on the command line, it will attempt to operate on each given URL, one by one. By default, it will ignore errors if there are more URLs given and the last URL&#8217;s success will determine the error code curl returns. So early failures will be &quot;hidden&quot; by subsequent successful transfers. </p>
<p> Using this option, curl will instead return an error on the first transfer that fails, independent of the amount of URLs that are given on the command line. This way, no transfer failures go undetected by scripts and similar. </p>
<p> This option is global and does not need to be specified for each use of <i>-:, &#8211;next</i>. </p>
<p> This option does not imply <i>-f, &#8211;fail</i>, which causes transfers to fail due to the server&#8217;s HTTP status code. You can combine the two options, however note <i>-f, &#8211;fail</i> is not global and is therefore contained by <i>-:, &#8211;next</i>. </p>
<p> Example: </p>
<pre>
 curl --fail-early <a rel="nofollow" href="https://example.com">https://example.com</a> <a rel="nofollow" href="https://two.example">https://two.example</a>
</pre>
<p> See also <i>-f, &#8211;fail</i> and <i>&#8211;fail-with-body</i>. Added in 7.52.0.</p>
<dt>&#8211;fail-with-body</p>
<dd> (HTTP) Return an error on server errors where the HTTP response code is 400 or greater). In normal cases when an HTTP server fails to deliver a document, it returns an HTML document stating so (which often also describes why and more). This flag will still allow curl to output and save that content but also to return error 22. </p>
<p> This is an alternative option to <i>-f, &#8211;fail</i> which makes curl fail for the same circumstances but without saving the content. </p>
<p> Example: </p>
<pre>
 curl --fail-with-body <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-f, &#8211;fail</i>. Added in 7.76.0.</p>
<dt>-f, &#8211;fail</p>
<dd> (HTTP) Fail silently (no output at all) on server errors. This is mostly done to enable scripts etc to better deal with failed attempts. In normal cases when an HTTP server fails to deliver a document, it returns an HTML document stating so (which often also describes why and more). This flag will prevent curl from outputting that and return error 22. </p>
<p> This method is not fail-safe and there are occasions where non-successful response codes will slip through, especially when authentication is involved (response codes 401 and 407). </p>
<p> Example: </p>
<pre>
 curl --fail <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;fail-with-body</i>.</p>
<dt>&#8211;false-start</p>
<dd> (TLS) Tells curl to use false start during the TLS handshake. False start is a mode where a TLS client will start sending application data before verifying the server&#8217;s Finished message, thus saving a round trip when performing a full handshake. </p>
<p> This is currently only implemented in the NSS and Secure Transport (on iOS 7.0 or later, or OS X 10.9 or later) backends. </p>
<p> Example: </p>
<pre>
 curl --false-start <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;tcp-fastopen</i>. Added in 7.42.0.</p>
<dt>&#8211;form-escape</p>
<dd> (HTTP) Tells curl to pass on names of multipart form fields and files using backslash-escaping instead of percent-encoding. </p>
<p> Example: </p>
<pre>
 curl --form-escape --form 'field
ame=curl' 'file=@load&quot;this' <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-F, &#8211;form</i>. Added in 7.81.0.</p>
<dt>&#8211;form-string &lt;name=string&gt;</p>
<dd> (HTTP SMTP IMAP) Similar to <i>-F, &#8211;form</i> except that the value string for the named parameter is used literally. Leading &#8216;@&#8217; and &#8216;&lt;&#8216; characters, and the &#8216;;type=&#8217; string in the value have no special meaning. Use this in preference to <i>-F, &#8211;form</i> if there&#8217;s any possibility that the string value may accidentally trigger the &#8216;@&#8217; or &#8216;&lt;&#8216; features of <i>-F, &#8211;form</i>. </p>
<p> Example: </p>
<pre>
 curl --form-string &quot;data&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-F, &#8211;form</i>.</p>
<dt>-F, &#8211;form &lt;name=content&gt;</p>
<dd> (HTTP SMTP IMAP) For HTTP protocol family, this lets curl emulate a filled-in form in which a user has pressed the submit button. This causes curl to POST data using the Content-Type multipart/form-data according to RFC 2388. </p>
<p> For SMTP and IMAP protocols, this is the means to compose a multipart mail message to transmit. </p>
<p> This enables uploading of binary files etc. To force the &#8216;content&#8217; part to be a file, prefix the file name with an @ sign. To just get the content part from a file, prefix the file name with the symbol &lt;. The difference between @ and &lt; is then that @ makes a file get attached in the post as a file upload, while the &lt; makes a text field and just get the contents for that text field from a file. </p>
<p> Tell curl to read content from stdin instead of a file by using &#8211; as filename. This goes for both @ and &lt; constructs. When stdin is used, the contents is buffered in memory first by curl to determine its size and allow a possible resend. Defining a part&#8217;s data from a named non-regular file (such as a named pipe or similar) is unfortunately not subject to buffering and will be effectively read at transmission time; since the full size is unknown before the transfer starts, such data is sent as chunks by HTTP and rejected by IMAP. </p>
<p> Example: send an image to an HTTP server, where &#8216;profile&#8217; is the name of the form-field to which the file portrait.jpg will be the input: </p>
<pre>
 curl -F profile=@portrait.jpg <a rel="nofollow" href="https://example.com/upload.cgi">https://example.com/upload.cgi</a>
</pre>
<p> Example: send your name and shoe size in two text fields to the server: </p>
<pre>
 curl -F name=John -F shoesize=11 <a rel="nofollow" href="https://example.com/">https://example.com/</a>
</pre>
<p> Example: send your essay in a text field to the server. Send it as a plain text field, but get the contents for it from a local file: </p>
<pre>
 curl -F &quot;story=&lt;hugefile.txt&quot; <a rel="nofollow" href="https://example.com/">https://example.com/</a>
</pre>
<p> You can also tell curl what Content-Type to use by using &#8216;type=&#8217;, in a manner similar to: </p>
<pre>
 curl -F &quot;web=@index.html;type=text/html&quot; example.com
</pre>
<p> or </p>
<pre>
 curl -F &quot;name=daniel;type=text/foo&quot; example.com
</pre>
<p> You can also explicitly change the name field of a file upload part by setting filename=, like this: </p>
<pre>
 curl -F &quot;file=@localfile;filename=nameinpost&quot; example.com
</pre>
<p> If filename/path contains &#8216;,&#8217; or &#8216;;&#8217;, it must be quoted by double-quotes like: </p>
<pre>
 curl -F &quot;file=@\&quot;local,file\&quot;;filename=\&quot;name;in;post\&quot;&quot; example.com
</pre>
<p> or </p>
<pre>
 curl -F 'file=@&quot;local,file&quot;;filename=&quot;name;in;post&quot;' example.com
</pre>
<p> Note that if a filename/path is quoted by double-quotes, any double-quote or backslash within the filename must be escaped by backslash. </p>
<p> Quoting must also be applied to non-file data if it contains semicolons, leading/trailing spaces or leading double quotes: </p>
<pre>
 curl -F 'colors=&quot;red; green; blue&quot;;type=text/x-myapp' example.com
</pre>
<p> You can add custom headers to the field by setting headers=, like </p>
<pre>
  curl -F &quot;submit=OK;headers=\&quot;X-submit-type: OK\&quot;&quot; example.com
</pre>
<p> or </p>
<pre>
  curl -F &quot;submit=OK;headers=@headerfile&quot; example.com
</pre>
<p> The headers= keyword may appear more that once and above notes about quoting apply. When headers are read from a file, Empty lines and lines starting with &#8216;#&#8217; are comments and ignored; each header can be folded by splitting between two words and starting the continuation line with a space; embedded carriage-returns and trailing spaces are stripped. Here is an example of a header file contents: </p>
<pre>
  # This file contain two headers.
  X-header-1: this is a header
</pre>
<pre>
  # The following header is folded.
  X-header-2: this is
   another header
</pre>
<p> To support sending multipart mail messages, the syntax is extended as follows:<br />
 &#8211; name can be omitted: the equal sign is the first character of the argument,<br />
 &#8211; if data starts with &#8216;(&#8216;, this signals to start a new multipart: it can be followed by a content type specification.<br />
 &#8211; a multipart can be terminated with a &#8216;=)&#8217; argument. </p>
<p> Example: the following command sends an SMTP mime email consisting in an inline part in two alternative formats: plain text and HTML. It attaches a text file: </p>
<pre>
 curl -F '=(;type=multipart/alternative' \
      -F '=plain text message' \
      -F '= &lt;body&gt;HTML message&lt;/body&gt;;type=text/html' \
      -F '=)' -F '=@textfile.txt' ...  <a href="smtp://example.com">smtp://example.com</a>
</pre>
<p> Data can be encoded for transfer using encoder=. Available encodings are <i>binary</i> and <i>8bit</i> that do nothing else than adding the corresponding Content-Transfer-Encoding header, <i>7bit</i> that only rejects 8-bit characters with a transfer error, <i>quoted-printable</i> and <i>base64</i> that encodes data according to the corresponding schemes, limiting lines length to 76 characters. </p>
<p> Example: send multipart mail with a quoted-printable text message and a base64 attached file: </p>
<pre>
 curl -F '=text message;encoder=quoted-printable' \
      -F '=@localfile;encoder=base64' ... <a href="smtp://example.com">smtp://example.com</a>
</pre>
<p> See further examples and details in the MANUAL. </p>
<p> This option can be used multiple times. </p>
<p> Example: </p>
<pre>
 curl --form &quot;name=curl&quot; --form &quot;file=@loadthis&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-d, &#8211;data</i>, <i>&#8211;form-string</i> and <i>&#8211;form-escape</i>. This option overrides <i>-d, &#8211;data</i> and <i>-I, &#8211;head</i> and <i>-T, &#8211;upload-file</i>.</p>
<dt>&#8211;ftp-account &lt;data&gt;</p>
<dd> (FTP) When an FTP server asks for &quot;account data&quot; after user name and password has been provided, this data is sent off using the ACCT command. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --ftp-account &quot;mr.robot&quot; <a href="ftp://example.com/">ftp://example.com/</a>
</pre>
<p> See also <i>-u, &#8211;user</i>.</p>
<dt>&#8211;ftp-alternative-to-user &lt;command&gt;</p>
<dd> (FTP) If authenticating with the USER and PASS commands fails, send this command. When connecting to Tumbleweed&#8217;s Secure Transport server over FTPS using a client certificate, using &quot;SITE AUTH&quot; will tell the server to retrieve the username from the certificate. </p>
<p> Example: </p>
<pre>
 curl --ftp-alternative-to-user &quot;U53r&quot; <a href="ftp://example.com">ftp://example.com</a>
</pre>
<p> See also <i>&#8211;ftp-account</i> and <i>-u, &#8211;user</i>.</p>
<dt>&#8211;ftp-create-dirs</p>
<dd> (FTP SFTP) When an FTP or SFTP URL/operation uses a path that does not currently exist on the server, the standard behavior of curl is to fail. Using this option, curl will instead attempt to create missing directories. </p>
<p> Example: </p>
<pre>
 curl --ftp-create-dirs -T file <a href="ftp://example.com/remote/path/file">ftp://example.com/remote/path/file</a>
</pre>
<p> See also <i>&#8211;create-dirs</i>.</p>
<dt>&#8211;ftp-method &lt;method&gt;</p>
<dd> (FTP) Control what method curl should use to reach a file on an FTP(S) server. The method argument should be one of the following alternatives:</p>
<dl>
<dt>
<dd>
<dl>
<dt>multicwd</p>
<dd> curl does a single CWD operation for each path part in the given URL. For deep hierarchies this means many commands. This is how RFC 1738 says it should be done. This is the default but the slowest behavior.</p>
<dt>nocwd</p>
<dd> curl does no CWD at all. curl will do SIZE, RETR, STOR etc and give a full path to the server for all these commands. This is the fastest behavior.</p>
<dt>singlecwd</p>
<dd> curl does one CWD with the full target directory and then operates on the file &quot;normally&quot; (like in the multicwd case). This is somewhat more standards compliant than &#8216;nocwd&#8217; but without the full penalty of &#8216;multicwd&#8217;.</dl>
</dl>
<p> Examples: </p>
<pre>
 curl --ftp-method multicwd <a href="ftp://example.com/dir1/dir2/file">ftp://example.com/dir1/dir2/file</a>
 curl --ftp-method nocwd <a href="ftp://example.com/dir1/dir2/file">ftp://example.com/dir1/dir2/file</a>
 curl --ftp-method singlecwd <a href="ftp://example.com/dir1/dir2/file">ftp://example.com/dir1/dir2/file</a>
</pre>
<p> See also <i>-l, &#8211;list-only</i>.</p>
<dt>&#8211;ftp-pasv</p>
<dd> (FTP) Use passive mode for the data connection. Passive is the internal default behavior, but using this option can be used to override a previous <i>-P, &#8211;ftp-port</i> option. </p>
<p> If this option is used several times, only the first one is used. Undoing an enforced passive really is not doable but you must then instead enforce the correct <i>-P, &#8211;ftp-port</i> again. </p>
<p> Passive mode means that curl will try the EPSV command first and then PASV, unless <i>&#8211;disable-epsv</i> is used. </p>
<p> Example: </p>
<pre>
 curl --ftp-pasv <a href="ftp://example.com/">ftp://example.com/</a>
</pre>
<p> See also <i>&#8211;disable-epsv</i>.</p>
<dt>-P, &#8211;ftp-port &lt;address&gt;</p>
<dd> (FTP) Reverses the default initiator/listener roles when connecting with FTP. This option makes curl use active mode. curl then tells the server to connect back to the client&#8217;s specified address and port, while passive mode asks the server to setup an IP address and port for it to connect to. &lt;address&gt; should be one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt>interface</p>
<dd> e.g. &quot;eth0&quot; to specify which interface&#8217;s IP address you want to use (Unix only)</p>
<dt>IP address</p>
<dd> e.g. &quot;192.168.10.1&quot; to specify the exact IP address</p>
<dt>host name</p>
<dd> e.g. &quot;my.host.domain&quot; to specify the machine</p>
<dt>&#8211;</p>
<dd> make curl pick the same IP address that is already used for the control connection</dl>
</dl>
<p> If this option is used several times, the last one will be used. Disable the use of PORT with <i>&#8211;ftp-pasv</i>. Disable the attempt to use the EPRT command instead of PORT by using <i>&#8211;disable-eprt</i>. EPRT is really PORT++. </p>
<p> You can also append &quot;:[start]-[end]&quot; to the right of the address, to tell curl what TCP port range to use. That means you specify a port range, from a lower to a higher number. A single number works as well, but do note that it increases the risk of failure since the port may not be available. </p>
<p> Examples: </p>
<pre>
 curl -P - ftp:/example.com
 curl -P eth0 ftp:/example.com
 curl -P 192.168.0.2 ftp:/example.com
</pre>
<p> See also <i>&#8211;ftp-pasv</i> and <i>&#8211;disable-eprt</i>.</p>
<dt>&#8211;ftp-pret</p>
<dd> (FTP) Tell curl to send a PRET command before PASV (and EPSV). Certain FTP servers, mainly drftpd, require this non-standard command for directory listings as well as up and downloads in PASV mode. </p>
<p> Example: </p>
<pre>
 curl --ftp-pret <a href="ftp://example.com/">ftp://example.com/</a>
</pre>
<p> See also <i>-P, &#8211;ftp-port</i> and <i>&#8211;ftp-pasv</i>.</p>
<dt>&#8211;ftp-skip-pasv-ip</p>
<dd> (FTP) Tell curl to not use the IP address the server suggests in its response to curl&#8217;s PASV command when curl connects the data connection. Instead curl will re-use the same IP address it already uses for the control connection. </p>
<p> Since curl 7.74.0 this option is enabled by default. </p>
<p> This option has no effect if PORT, EPRT or EPSV is used instead of PASV. </p>
<p> Example: </p>
<pre>
 curl --ftp-skip-pasv-ip <a href="ftp://example.com/">ftp://example.com/</a>
</pre>
<p> See also <i>&#8211;ftp-pasv</i>.</p>
<dt>&#8211;ftp-ssl-ccc-mode &lt;active/passive&gt;</p>
<dd> (FTP) Sets the CCC mode. The passive mode will not initiate the shutdown, but instead wait for the server to do it, and will not reply to the shutdown from the server. The active mode initiates the shutdown and waits for a reply from the server. </p>
<p> Example: </p>
<pre>
 curl --ftp-ssl-ccc-mode active --ftp-ssl-ccc <a href="ftps://example.com/">ftps://example.com/</a>
</pre>
<p> See also <i>&#8211;ftp-ssl-ccc</i>.</p>
<dt>&#8211;ftp-ssl-ccc</p>
<dd> (FTP) Use CCC (Clear Command Channel) Shuts down the SSL/TLS layer after authenticating. The rest of the control channel communication will be unencrypted. This allows NAT routers to follow the FTP transaction. The default mode is passive. </p>
<p> Example: </p>
<pre>
 curl --ftp-ssl-ccc <a href="ftps://example.com/">ftps://example.com/</a>
</pre>
<p> See also <i>&#8211;ssl</i> and <i>&#8211;ftp-ssl-ccc-mode</i>.</p>
<dt>&#8211;ftp-ssl-control</p>
<dd> (FTP) Require SSL/TLS for the FTP login, clear for transfer. Allows secure authentication, but non-encrypted data transfers for efficiency. Fails the transfer if the server does not support SSL/TLS. </p>
<p> Example: </p>
<pre>
 curl --ftp-ssl-control <a href="ftp://example.com">ftp://example.com</a>
</pre>
<p> See also <i>&#8211;ssl</i>.</p>
<dt>-G, &#8211;get</p>
<dd> When used, this option will make all data specified with <i>-d, &#8211;data</i>, <i>&#8211;data-binary</i> or <i>&#8211;data-urlencode</i> to be used in an HTTP GET request instead of the POST request that otherwise would be used. The data will be appended to the URL with a &#8216;?&#8217; separator. </p>
<p> If used in combination with <i>-I, &#8211;head</i>, the POST data will instead be appended to the URL with a HEAD request. </p>
<p> If this option is used several times, only the first one is used. This is because undoing a GET does not make sense, but you should then instead enforce the alternative method you prefer. </p>
<p> Examples: </p>
<pre>
 curl --get <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl --get -d &quot;tool=curl&quot; -d &quot;age=old&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl --get -I -d &quot;tool=curl&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-d, &#8211;data</i> and <i>-X, &#8211;request</i>.</p>
<dt>-g, &#8211;globoff</p>
<dd> This option switches off the &quot;URL globbing parser&quot;. When you set this option, you can specify URLs that contain the letters {}[] without having curl itself interpret them. Note that these letters are not normal legal URL contents but they should be encoded according to the URI standard. </p>
<p> Example:<br />
curl &#8211; g &#8220;https://example.com/{[]}}}}&#8221;</p>
<p> See also <i>-K, &#8211;config</i> and <i>-q, &#8211;disable</i>.</p>
<dt>&#8211;happy-eyeballs-timeout-ms &lt;milliseconds&gt;</p>
<dd> Happy Eyeballs is an algorithm that attempts to connect to both IPv4 and IPv6 addresses for dual-stack hosts, giving IPv6 a head-start of the specified number of milliseconds. If the IPv6 address cannot be connected to within that time, then a connection attempt is made to the IPv4 address in parallel. The first connection to be established is the one that is used. </p>
<p> The range of suggested useful values is limited. Happy Eyeballs RFC 6555 says &quot;It is RECOMMENDED that connection attempts be paced 150-250 ms apart to balance human factors against network load.&quot; libcurl currently defaults to 200 ms. Firefox and Chrome currently default to 300 ms. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --happy-eyeballs-timeout-ms 500 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-m, &#8211;max-time</i> and <i>&#8211;connect-timeout</i>. Added in 7.59.0.</p>
<dt>&#8211;haproxy-protocol</p>
<dd> (HTTP) Send a HAProxy PROXY protocol v1 header at the beginning of the connection. This is used by some load balancers and reverse proxies to indicate the client&#8217;s true IP address and port. </p>
<p> This option is primarily useful when sending test requests to a service that expects this header. </p>
<p> Example: </p>
<pre>
 curl --haproxy-protocol <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i>. Added in 7.60.0.</p>
<dt>-I, &#8211;head</p>
<dd> (HTTP FTP FILE) Fetch the headers only! HTTP-servers feature the command HEAD which this uses to get nothing but the header of a document. When used on an FTP or FILE file, curl displays the file size and last modification time only. </p>
<p> Example: </p>
<pre>
 curl -I <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-G, &#8211;get</i>, <i>-v, &#8211;verbose</i> and <i>&#8211;trace-ascii</i>.</p>
<dt>-H, &#8211;header &lt;header/@file&gt;</p>
<dd> (HTTP) Extra header to include in the request when sending HTTP to a server. You may specify any number of extra headers. Note that if you should add a custom header that has the same name as one of the internal ones curl would use, your externally set header will be used instead of the internal one. This allows you to make even trickier stuff than curl would normally do. You should not replace internally set headers without knowing perfectly well what you are doing. Remove an internal header by giving a replacement without content on the right side of the colon, as in: -H &quot;Host:&quot;. If you send the custom header with no-value then its header must be terminated with a semicolon, such as -H &quot;X-Custom-Header;&quot; to send &quot;X-Custom-Header:&quot;. </p>
<p> curl will make sure that each header you add/replace is sent with the proper end-of-line marker, you should thus <code>not</code> add that as a part of the header content: do not add newlines or carriage returns, they will only mess things up for you. </p>
<p> This option can take an argument in @filename style, which then adds a header for each line in the input file. Using @- will make curl read the header file from stdin. Added in 7.55.0. </p>
<p> You need <i>&#8211;proxy-header</i> to send custom headers intended for a HTTP proxy. Added in 7.37.0. </p>
<p> Passing on a &quot;Transfer-Encoding: chunked&quot; header when doing a HTTP request with a request body, will make curl send the data using chunked encoding. </p>
<p> <code>WARNING</code>: headers set with this option will be set in all requests &#8211; even after redirects are followed, like when told with <i>-L, &#8211;location</i>. This can lead to the header being sent to other hosts than the original host, so sensitive headers should be used with caution combined with following redirects. </p>
<p> This option can be used multiple times to add/replace/remove multiple headers. </p>
<p> Examples: </p>
<pre>
 curl -H &quot;X-First-Name: Joe&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl -H &quot;User-Agent: yes-please/2000&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl -H &quot;Host:&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-A, &#8211;user-agent</i> and <i>-e, &#8211;referer</i>.</p>
<dt>-h, &#8211;help &lt;category&gt;</p>
<dd> Usage help. This lists all commands of the &lt;category&gt;. If no arg was provided, curl will display the most important command line arguments. If the argument &quot;all&quot; was provided, curl will display all options available. If the argument &quot;category&quot; was provided, curl will display all categories and their meanings. </p>
<p> Example: </p>
<pre>
 curl --help all
</pre>
<p> See also <i>-v, &#8211;verbose</i>.</p>
<dt>&#8211;hostpubmd5 &lt;md5&gt;</p>
<dd> (SFTP SCP) Pass a string containing 32 hexadecimal digits. The string should be the 128 bit MD5 checksum of the remote host&#8217;s public key, curl will refuse the connection with the host unless the md5sums match. </p>
<p> Example: </p>
<pre>
 curl --hostpubmd5 e5c1c49020640a5ab0f2034854c321a8 <a href="sftp://example.com/">sftp://example.com/</a>
</pre>
<p> See also <i>&#8211;hostpubsha256</i>.</p>
<dt>&#8211;hostpubsha256 &lt;sha256&gt;</p>
<dd> (SFTP SCP) Pass a string containing a Base64-encoded SHA256 hash of the remote host&#8217;s public key. Curl will refuse the connection with the host unless the hashes match. </p>
<p> Example: </p>
<pre>
 curl --hostpubsha256 NDVkMTQxMGQ1ODdmMjQ3MjczYjAyOTY5MmRkMjVmNDQ= <a href="sftp://example.com/">sftp://example.com/</a>
</pre>
<p> See also <i>&#8211;hostpubmd5</i>. Added in 7.80.0.</p>
<dt>&#8211;hsts &lt;file name&gt;</p>
<dd> (HTTPS) This option enables HSTS for the transfer. If the file name points to an existing HSTS cache file, that will be used. After a completed transfer, the cache will be saved to the file name again if it has been modified. </p>
<p> Specify a &quot;&quot; file name (zero length) to avoid loading/saving and make curl just handle HSTS in memory. </p>
<p> If this option is used several times, curl will load contents from all the files but the last one will be used for saving. </p>
<p> Example: </p>
<pre>
 curl --hsts cache.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proto</i>. Added in 7.74.0.</p>
<dt>&#8211;http0.9</p>
<dd> (HTTP) Tells curl to be fine with HTTP version 0.9 response. </p>
<p> HTTP/0.9 is a completely headerless response and therefore you can also connect with this to non-HTTP servers and still get a response since curl will simply transparently downgrade &#8211; if allowed. </p>
<p> Since curl 7.66.0, HTTP/0.9 is disabled by default. </p>
<p> Example: </p>
<pre>
 curl --http0.9 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;http1.1</i>, <i>&#8211;http2</i> and <i>&#8211;http3</i>. Added in 7.64.0.</p>
<dt>-0, &#8211;http1.0</p>
<dd> (HTTP) Tells curl to use HTTP version 1.0 instead of using its internally preferred HTTP version. </p>
<p> Example: </p>
<pre>
 curl --http1.0 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;http0.9</i> and <i>&#8211;http1.1</i>. This option overrides <i>&#8211;http1.1</i> and <i>&#8211;http2</i>.</p>
<dt>&#8211;http1.1</p>
<dd> (HTTP) Tells curl to use HTTP version 1.1. </p>
<p> Example: </p>
<pre>
 curl --http1.1 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;http1.1</i> and <i>&#8211;http0.9</i>. This option overrides <i>-0, &#8211;http1.0</i> and <i>&#8211;http2</i>. Added in 7.33.0.</p>
<dt>&#8211;http2-prior-knowledge</p>
<dd> (HTTP) Tells curl to issue its non-TLS HTTP requests using HTTP/2 without HTTP/1.1 Upgrade. It requires prior knowledge that the server supports HTTP/2 straight away. HTTPS requests will still do HTTP/2 the standard way with negotiated protocol version in the TLS handshake. </p>
<p> Example: </p>
<pre>
 curl --http2-prior-knowledge <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;http2</i> and <i>&#8211;http3</i>. <i>&#8211;http2-prior-knowledge</i> requires that the underlying libcurl was built to support HTTP/2. This option overrides <i>&#8211;http1.1</i> and <i>-0, &#8211;http1.0</i> and <i>&#8211;http2</i>. Added in 7.49.0.</p>
<dt>&#8211;http2</p>
<dd> (HTTP) Tells curl to use HTTP version 2. </p>
<p> For HTTPS, this means curl will attempt to negotiate HTTP/2 in the TLS handshake. curl does this by default. </p>
<p> For HTTP, this means curl will attempt to upgrade the request to HTTP/2 using the Upgrade: request header. </p>
<p> Example: </p>
<pre>
 curl --http2 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;http1.1</i> and <i>&#8211;http3</i>. <i>&#8211;http2</i> requires that the underlying libcurl was built to support HTTP/2. This option overrides <i>&#8211;http1.1</i> and <i>-0, &#8211;http1.0</i> and <i>&#8211;http2-prior-knowledge</i>. Added in 7.33.0.</p>
<dt>&#8211;http3</p>
<dd> (HTTP) <code>WARNING</code>: this option is experimental. Do not use in production. </p>
<p> Tells curl to use HTTP version 3 directly to the host and port number used in the URL. A normal HTTP/3 transaction will be done to a host and then get redirected via Alt-Svc, but this option allows a user to circumvent that when you know that the target speaks HTTP/3 on the given host and port. </p>
<p> This option will make curl fail if a QUIC connection cannot be established, it cannot fall back to a lower HTTP version on its own. </p>
<p> Example: </p>
<pre>
 curl --http3 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;http1.1</i> and <i>&#8211;http2</i>. <i>&#8211;http3</i> requires that the underlying libcurl was built to support HTTP/3. This option overrides <i>&#8211;http1.1</i> and <i>-0, &#8211;http1.0</i> and <i>&#8211;http2</i> and <i>&#8211;http2-prior-knowledge</i>. Added in 7.66.0.</p>
<dt>&#8211;ignore-content-length</p>
<dd> (FTP HTTP) For HTTP, Ignore the Content-Length header. This is particularly useful for servers running Apache 1.x, which will report incorrect Content-Length for files larger than 2 gigabytes. </p>
<p> For FTP (since 7.46.0), skip the RETR command to figure out the size before downloading a file. </p>
<p> This option does not work for HTTP if libcurl was built to use hyper. </p>
<p> Example: </p>
<pre>
 curl --ignore-content-length <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;ftp-skip-pasv-ip</i>.</p>
<dt>-i, &#8211;include</p>
<dd> Include the HTTP response headers in the output. The HTTP response headers can include things like server name, cookies, date of the document, HTTP version and more&#8230; </p>
<p> To view the request headers, consider the <i>-v, &#8211;verbose</i> option. </p>
<p> Example: </p>
<pre>
 curl -i <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-v, &#8211;verbose</i>.</p>
<dt>-k, &#8211;insecure</p>
<dd> (TLS SFTP SCP) By default, every secure connection curl makes is verified to be secure before the transfer takes place. This option makes curl skip the verification step and proceed without checking. </p>
<p> When this option is not used for protocols using TLS, curl verifies the server&#8217;s TLS certificate before it continues: that the certificate contains the right name which matches the host name used in the URL and that the certificate has been signed by a CA certificate present in the cert store. See this online resource for further details: </p>
<pre>
 <a rel="nofollow" href="https://curl.se/docs/sslcerts.html">https://curl.se/docs/sslcerts.html</a>
</pre>
<p> For SFTP and SCP, this option makes curl skip the <i>known_hosts</i> verification. <i>known_hosts</i> is a file normally stored in the user&#8217;s home directory in the .ssh subdirectory, which contains host names and their public keys. </p>
<p> <code>WARNING</code>: using this option makes the transfer insecure. </p>
<p> Example: </p>
<pre>
 curl --insecure <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-insecure</i>, <i>&#8211;cacert</i> and <i>&#8211;capath</i>.</p>
<dt>&#8211;interface &lt;name&gt;</p>
<dd> Perform an operation using a specified interface. You can enter interface name, IP address or host name. An example could look like: </p>
<pre>
 curl --interface eth0:1 <a rel="nofollow" href="https://www.example.com/">https://www.example.com/</a>
</pre>
<p> If this option is used several times, the last one will be used. </p>
<p> On Linux it can be used to specify a VRF, but the binary needs to either have CAP_NET_RAW or to be run as root. More information about Linux VRF: <a rel="nofollow" href="https://www.kernel.org/doc/Documentation/networking/vrf.txt">https://www.kernel.org/doc/Documentation/networking/vrf.txt</a> </p>
<p> Example: </p>
<pre>
 curl --interface eth0 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;dns-interface</i>.</p>
<dt>-4, &#8211;ipv4</p>
<dd> This option tells curl to resolve names to IPv4 addresses only, and not for example try IPv6. </p>
<p> Example: </p>
<pre>
 curl --ipv4 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;http1.1</i> and <i>&#8211;http2</i>. This option overrides <i>-6, &#8211;ipv6</i>.</p>
<dt>-6, &#8211;ipv6</p>
<dd> This option tells curl to resolve names to IPv6 addresses only, and not for example try IPv4. </p>
<p> Example: </p>
<pre>
 curl --ipv6 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;http1.1</i> and <i>&#8211;http2</i>. This option overrides <i>-4, &#8211;ipv4</i>.</p>
<dt>-j, &#8211;junk-session-cookies</p>
<dd> (HTTP) When curl is told to read cookies from a given file, this option will make it discard all &quot;session cookies&quot;. This will basically have the same effect as if a new session is started. Typical browsers always discard session cookies when they are closed down. </p>
<p> Example: </p>
<pre>
 curl --junk-session-cookies -b cookies.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-b, &#8211;cookie</i> and <i>-c, &#8211;cookie-jar</i>.</p>
<dt>&#8211;keepalive-time &lt;seconds&gt;</p>
<dd> This option sets the time a connection needs to remain idle before sending keepalive probes and the time between individual keepalive probes. It is currently effective on operating systems offering the TCP_KEEPIDLE and TCP_KEEPINTVL socket options (meaning Linux, recent AIX, HP-UX and more). This option has no effect if <i>&#8211;no-keepalive</i> is used. </p>
<p> If this option is used several times, the last one will be used. If unspecified, the option defaults to 60 seconds. </p>
<p> Example: </p>
<pre>
 curl --keepalive-time 20 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;no-keepalive</i> and <i>-m, &#8211;max-time</i>.</p>
<dt>&#8211;key-type &lt;type&gt;</p>
<dd> (TLS) Private key file type. Specify which type your <i>&#8211;key</i> provided private key is. DER, PEM, and ENG are supported. If not specified, PEM is assumed. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --key-type DER --key here <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;key</i>.</p>
<dt>&#8211;key &lt;key&gt;</p>
<dd> (TLS SSH) Private key file name. Allows you to provide your private key in this separate file. For SSH, if not specified, curl tries the following candidates in order: &#8216;~/.ssh/id_rsa&#8217;, &#8216;~/.ssh/id_dsa&#8217;, &#8216;./id_rsa&#8217;, &#8216;./id_dsa&#8217;. </p>
<p> If curl is built against OpenSSL library, and the engine pkcs11 is available, then a PKCS#11 URI (RFC 7512) can be used to specify a private key located in a PKCS#11 device. A string beginning with &quot;pkcs11:&quot; will be interpreted as a PKCS#11 URI. If a PKCS#11 URI is provided, then the <i>&#8211;engine</i> option will be set as &quot;pkcs11&quot; if none was provided and the <i>&#8211;key-type</i> option will be set as &quot;ENG&quot; if none was provided. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --cert certificate --key here <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;key-type</i> and <i>-E, &#8211;cert</i>.</p>
<dt>&#8211;krb &lt;level&gt;</p>
<dd> (FTP) Enable Kerberos authentication and use. The level must be entered and should be one of &#8216;clear&#8217;, &#8216;safe&#8217;, &#8216;confidential&#8217;, or &#8216;private&#8217;. Should you use a level that is not one of these, &#8216;private&#8217; will instead be used. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --krb clear <a href="ftp://example.com/">ftp://example.com/</a>
</pre>
<p> See also <i>&#8211;delegation</i> and <i>&#8211;ssl</i>. <i>&#8211;krb</i> requires that the underlying libcurl was built to support Kerberos.</p>
<dt>&#8211;libcurl &lt;file&gt;</p>
<dd> Append this option to any ordinary curl command line, and you will get libcurl-using C source code written to the file that does the equivalent of what your command-line operation does! </p>
<p> This option is global and does not need to be specified for each use of <i>-:, &#8211;next</i>. </p>
<p> If this option is used several times, the last given file name will be used. </p>
<p> Example: </p>
<pre>
 curl --libcurl client.c <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-v, &#8211;verbose</i>.</p>
<dt>&#8211;limit-rate &lt;speed&gt;</p>
<dd> Specify the maximum transfer rate you want curl to use &#8211; for both downloads and uploads. This feature is useful if you have a limited pipe and you would like your transfer not to use your entire bandwidth. To make it slower than it otherwise would be. </p>
<p> The given speed is measured in bytes/second, unless a suffix is appended. Appending &#8216;k&#8217; or &#8216;K&#8217; will count the number as kilobytes, &#8216;m&#8217; or &#8216;M&#8217; makes it megabytes, while &#8216;g&#8217; or &#8216;G&#8217; makes it gigabytes. The suffixes (k, M, G, T, P) are 1024 based. For example 1k is 1024. Examples: 200K, 3m and 1G. </p>
<p> The rate limiting logic works on averaging the transfer speed to no more than the set threshold over a period of multiple seconds. </p>
<p> If you also use the <i>-Y, &#8211;speed-limit</i> option, that option will take precedence and might cripple the rate-limiting slightly, to help keeping the speed-limit logic working. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Examples: </p>
<pre>
 curl --limit-rate 100K <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl --limit-rate 1000 <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl --limit-rate 10M <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-Y, &#8211;speed-limit</i> and <i>-y, &#8211;speed-time</i>.</p>
<dt>-l, &#8211;list-only</p>
<dd> (FTP POP3) (FTP) When listing an FTP directory, this switch forces a name-only view. This is especially useful if the user wants to machine-parse the contents of an FTP directory since the normal directory view does not use a standard look or format. When used like this, the option causes an NLST command to be sent to the server instead of LIST. </p>
<p> Note: Some FTP servers list only files in their response to NLST; they do not include sub-directories and symbolic links. </p>
<p> (POP3) When retrieving a specific email from POP3, this switch forces a LIST command to be performed instead of RETR. This is particularly useful if the user wants to see if a specific message-id exists on the server and what size it is. </p>
<p> Note: When combined with <i>-X, &#8211;request</i>, this option can be used to send a UIDL command instead, so the user may use the email&#8217;s unique identifier rather than its message-id to make the request. </p>
<p> Example: </p>
<pre>
 curl --list-only <a href="ftp://example.com/dir/">ftp://example.com/dir/</a>
</pre>
<p> See also <i>-Q, &#8211;quote</i> and <i>-X, &#8211;request</i>.</p>
<dt>&#8211;local-port &lt;num/range&gt;</p>
<dd> Set a preferred single number or range (FROM-TO) of local port numbers to use for the connection(s). Note that port numbers by nature are a scarce resource that will be busy at times so setting this range to something too narrow might cause unnecessary connection setup failures. </p>
<p> Example: </p>
<pre>
 curl --local-port 1000-3000 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-g, &#8211;globoff</i>.</p>
<dt>&#8211;location-trusted</p>
<dd> (HTTP) Like <i>-L, &#8211;location</i>, but will allow sending the name + password to all hosts that the site may redirect to. This may or may not introduce a security breach if the site redirects you to a site to which you will send your authentication info (which is plaintext in the case of HTTP Basic authentication). </p>
<p> Example: </p>
<pre>
 curl --location-trusted -u user:password <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-u, &#8211;user</i>.</p>
<dt>-L, &#8211;location</p>
<dd> (HTTP) If the server reports that the requested page has moved to a different location (indicated with a Location: header and a 3XX response code), this option will make curl redo the request on the new place. If used together with <i>-i, &#8211;include</i> or <i>-I, &#8211;head</i>, headers from all requested pages will be shown. When authentication is used, curl only sends its credentials to the initial host. If a redirect takes curl to a different host, it will not be able to intercept the user+password. See also <i>&#8211;location-trusted</i> on how to change this. You can limit the amount of redirects to follow by using the <i>&#8211;max-redirs</i> option. </p>
<p> When curl follows a redirect and if the request is a POST, it will send the following request with a GET if the HTTP response was 301, 302, or 303. If the response code was any other 3xx code, curl will re-send the following request using the same unmodified method. </p>
<p> You can tell curl to not change POST requests to GET after a 30x response by using the dedicated options for that: <i>&#8211;post301</i>, <i>&#8211;post302</i> and <i>&#8211;post303</i>. </p>
<p> The method set with <i>-X, &#8211;request</i> overrides the method curl would otherwise select to use. </p>
<p> Example: </p>
<pre>
 curl -L <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;resolve</i> and <i>&#8211;alt-svc</i>.</p>
<dt>&#8211;login-options &lt;options&gt;</p>
<dd> (IMAP POP3 SMTP) Specify the login options to use during server authentication. </p>
<p> You can use login options to specify protocol specific options that may be used during authentication. At present only IMAP, POP3 and SMTP support login options. For more information about login options please see RFC 2384, RFC 5092 and IETF draft draft-earhart-url-smtp-00.txt </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --login-options 'AUTH=*' <a href="imap://example.com">imap://example.com</a>
</pre>
<p> See also <i>-u, &#8211;user</i>. Added in 7.34.0.</p>
<dt>&#8211;mail-auth &lt;address&gt;</p>
<dd> (SMTP) Specify a single address. This will be used to specify the authentication address (identity) of a submitted message that is being relayed to another server. </p>
<p> Example: </p>
<pre>
 curl --mail-auth user [at] example.come -T mail <a href="smtp://example.com/">smtp://example.com/</a>
</pre>
<p> See also <i>&#8211;mail-rcpt</i> and <i>&#8211;mail-from</i>.</p>
<dt>&#8211;mail-from &lt;address&gt;</p>
<dd> (SMTP) Specify a single address that the given mail should get sent from. </p>
<p> Example: </p>
<pre>
 curl --mail-from user [at] example.com -T mail <a href="smtp://example.com/">smtp://example.com/</a>
</pre>
<p> See also <i>&#8211;mail-rcpt</i> and <i>&#8211;mail-auth</i>.</p>
<dt>&#8211;mail-rcpt-allowfails</p>
<dd> (SMTP) When sending data to multiple recipients, by default curl will abort SMTP conversation if at least one of the recipients causes RCPT TO command to return an error. </p>
<p> The default behavior can be changed by passing <i>&#8211;mail-rcpt-allowfails</i> command-line option which will make curl ignore errors and proceed with the remaining valid recipients. </p>
<p> If all recipients trigger RCPT TO failures and this flag is specified, curl will still abort the SMTP conversation and return the error received from to the last RCPT TO command. </p>
<p> Example:<br />
curl&#8211; mail &#8211; rcpt &#8211; allowfails&#8211; mail &#8211; rcpt dest[at] example.com smtp: // example.com</p>
<p> See also <i>&#8211;mail-rcpt</i>. Added in 7.69.0.</p>
<dt>&#8211;mail-rcpt &lt;address&gt;</p>
<dd> (SMTP) Specify a single email address, user name or mailing list name. Repeat this option several times to send to multiple recipients. </p>
<p> When performing an address verification (VRFY command), the recipient should be specified as the user name or user name and domain (as per Section 3.5 of RFC5321). (Added in 7.34.0) </p>
<p> When performing a mailing list expand (EXPN command), the recipient should be specified using the mailing list name, such as &quot;Friends&quot; or &quot;London-Office&quot;. (Added in 7.34.0) </p>
<p> Example: </p>
<pre>
 curl --mail-rcpt user [at] example.net <a href="smtp://example.com">smtp://example.com</a>
</pre>
<p> See also <i>&#8211;mail-rcpt-allowfails</i>.</p>
<dt>-M, &#8211;manual</p>
<dd> Manual. Display the huge help text. </p>
<p> Example: </p>
<pre>
 curl --manual
</pre>
<p> See also <i>-v, &#8211;verbose</i>, <i>&#8211;libcurl</i> and <i>&#8211;trace</i>.</p>
<dt>&#8211;max-filesize &lt;bytes&gt;</p>
<dd> (FTP HTTP MQTT) Specify the maximum size (in bytes) of a file to download. If the file requested is larger than this value, the transfer will not start and curl will return with exit code 63. </p>
<p> A size modifier may be used. For example, Appending &#8216;k&#8217; or &#8216;K&#8217; will count the number as kilobytes, &#8216;m&#8217; or &#8216;M&#8217; makes it megabytes, while &#8216;g&#8217; or &#8216;G&#8217; makes it gigabytes. Examples: 200K, 3m and 1G. (Added in 7.58.0) </p>
<p> <code>NOTE</code>: The file size is not always known prior to download, and for such files this option has no effect even if the file transfer ends up being larger than this given limit. Example: </p>
<pre>
 curl --max-filesize 100K <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;limit-rate</i>.</p>
<dt>&#8211;max-redirs &lt;num&gt;</p>
<dd> (HTTP) Set maximum number of redirections to follow. When <i>-L, &#8211;location</i> is used, to prevent curl from following too many redirects, by default, the limit is set to 50 redirects. Set this option to -1 to make it unlimited. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --max-redirs 3 --location <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-L, &#8211;location</i>.</p>
<dt>-m, &#8211;max-time &lt;fractional seconds&gt;</p>
<dd> Maximum time in seconds that you allow the whole operation to take. This is useful for preventing your batch jobs from hanging for hours due to slow networks or links going down. Since 7.32.0, this option accepts decimal values, but the actual timeout will decrease in accuracy as the specified timeout increases in decimal precision. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Examples: </p>
<pre>
 curl --max-time 10 <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl --max-time 2.92 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;connect-timeout</i>.</p>
<dt>&#8211;metalink</p>
<dd> This option was previously used to specify a metalink resource. Metalink support has been disabled in curl since 7.78.0 for security reasons. </p>
<p> Example: </p>
<pre>
 curl --metalink file <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-Z, &#8211;parallel</i>.</p>
<dt>&#8211;negotiate</p>
<dd> (HTTP) Enables Negotiate (SPNEGO) authentication. </p>
<p> This option requires a library built with GSS-API or SSPI support. Use <i>-V, &#8211;version</i> to see if your curl supports GSS-API/SSPI or SPNEGO. </p>
<p> When using this option, you must also provide a fake <i>-u, &#8211;user</i> option to activate the authentication code properly. Sending a &#8216;-u :&#8217; is enough as the user name and password from the <i>-u, &#8211;user</i> option are not actually used. </p>
<p> If this option is used several times, only the first one is used. </p>
<p> Example: </p>
<pre>
 curl --negotiate -u : <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;basic</i>, <i>&#8211;ntlm</i>, <i>&#8211;anyauth</i> and <i>&#8211;proxy-negotiate</i>.</p>
<dt>&#8211;netrc-file &lt;filename&gt;</p>
<dd> This option is similar to <i>-n, &#8211;netrc</i>, except that you provide the path (absolute or relative) to the netrc file that curl should use. You can only specify one netrc file per invocation. If several <i>&#8211;netrc-file</i> options are provided, the last one will be used. </p>
<p> It will abide by <i>&#8211;netrc-optional</i> if specified. </p>
<p> Example: </p>
<pre>
 curl --netrc-file netrc <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-n, &#8211;netrc</i>, <i>-u, &#8211;user</i> and <i>-K, &#8211;config</i>. This option overrides <i>-n, &#8211;netrc</i>.</p>
<dt>&#8211;netrc-optional</p>
<dd> Similar to <i>-n, &#8211;netrc</i>, but this option makes the .netrc usage <code>optional</code> and not mandatory as the <i>-n, &#8211;netrc</i> option does. </p>
<p> Example: </p>
<pre>
 curl --netrc-optional <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;netrc-file</i>. This option overrides <i>-n, &#8211;netrc</i>.</p>
<dt>-n, &#8211;netrc</p>
<dd> Makes curl scan the <i>.netrc</i> (<i>_netrc</i> on Windows) file in the user&#8217;s home directory for login name and password. This is typically used for FTP on Unix. If used with HTTP, curl will enable user authentication. See <i><a href="/docs/linux/man/5-netrc/">netrc</a>(5)</i> and <i><a href="/docs/linux/man/1-ftp/">ftp</a>(1)</i> for details on the file format. Curl will not complain if that file does not have the right permissions (it should be neither world- nor group-readable). The environment variable &quot;HOME&quot; is used to find the home directory. </p>
<p> A quick and simple example of how to setup a <i>.netrc</i> to allow curl to FTP to the machine host.domain.com with user name &#8216;myself&#8217; and password &#8216;secret&#8217; could look similar to: </p>
<pre>
 machine host.domain.com
 login myself
 password secret&quot;
Example:
 curl --netrc <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;netrc-file</i>, <i>-K, &#8211;config</i> and <i>-u, &#8211;user</i>.</p>
<dt>-:, &#8211;next</p>
<dd> Tells curl to use a separate operation for the following URL and associated options. This allows you to send several URL requests, each with their own specific options, for example, such as different user names or custom requests for each. </p>
<p> <i>-:, &#8211;next</i> will reset all local options and only global ones will have their values survive over to the operation following the <i>-:, &#8211;next</i> instruction. Global options include <i>-v, &#8211;verbose</i>, <i>&#8211;trace</i>, <i>&#8211;trace-ascii</i> and <i>&#8211;fail-early</i>. </p>
<p> For example, you can do both a GET and a POST in a single command line: </p>
<pre>
 curl www1.example.com --next -d postthis www2.example.com
</pre>
<p> Examples: </p>
<pre>
 curl <a rel="nofollow" href="https://example.com">https://example.com</a> --next -d postthis www2.example.com
 curl -I <a rel="nofollow" href="https://example.com">https://example.com</a> --next <a rel="nofollow" href="https://example.net/">https://example.net/</a>
</pre>
<p> See also <i>-Z, &#8211;parallel</i> and <i>-K, &#8211;config</i>. Added in 7.36.0.</p>
<dt>&#8211;no-alpn</p>
<dd> (HTTPS) Disable the ALPN TLS extension. ALPN is enabled by default if libcurl was built with an SSL library that supports ALPN. ALPN is used by a libcurl that supports HTTP/2 to negotiate HTTP/2 support with the server during https sessions. </p>
<p> Example: </p>
<pre>
 curl --no-alpn <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;no-npn</i> and <i>&#8211;http2</i>. <i>&#8211;no-alpn</i> requires that the underlying libcurl was built to support TLS. Added in 7.36.0.</p>
<dt>-N, &#8211;no-buffer</p>
<dd> Disables the buffering of the output stream. In normal work situations, curl will use a standard buffered output stream that will have the effect that it will output the data in chunks, not necessarily exactly when the data arrives. Using this option will disable that buffering. </p>
<p> Note that this is the negated option name documented. You can thus use &#8211;buffer to enforce the buffering. </p>
<p> Example: </p>
<pre>
 curl --no-buffer <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-#, &#8211;progress-bar</i>.</p>
<dt>&#8211;no-keepalive</p>
<dd> Disables the use of keepalive messages on the TCP connection. curl otherwise enables them by default. </p>
<p> Note that this is the negated option name documented. You can thus use &#8211;keepalive to enforce keepalive. </p>
<p> Example: </p>
<pre>
 curl --no-keepalive <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;keepalive-time</i>.</p>
<dt>&#8211;no-npn</p>
<dd> (HTTPS) Disable the NPN TLS extension. NPN is enabled by default if libcurl was built with an SSL library that supports NPN. NPN is used by a libcurl that supports HTTP/2 to negotiate HTTP/2 support with the server during https sessions. </p>
<p> Example: </p>
<pre>
 curl --no-npn <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;no-alpn</i> and <i>&#8211;http2</i>. <i>&#8211;no-npn</i> requires that the underlying libcurl was built to support TLS. Added in 7.36.0.</p>
<dt>&#8211;no-progress-meter</p>
<dd> Option to switch off the progress meter output without muting or otherwise affecting warning and informational messages like <i>-s, &#8211;silent</i> does. </p>
<p> Note that this is the negated option name documented. You can thus use &#8211;progress-meter to enable the progress meter again. </p>
<p> Example: </p>
<pre>
 curl --no-progress-meter -o store <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-v, &#8211;verbose</i> and <i>-s, &#8211;silent</i>. Added in 7.67.0.</p>
<dt>&#8211;no-sessionid</p>
<dd> (TLS) Disable curl&#8217;s use of SSL session-ID caching. By default all transfers are done using the cache. Note that while nothing should ever get hurt by attempting to reuse SSL session-IDs, there seem to be broken SSL implementations in the wild that may require you to disable this in order for you to succeed. </p>
<p> Note that this is the negated option name documented. You can thus use &#8211;sessionid to enforce session-ID caching. </p>
<p> Example: </p>
<pre>
 curl --no-sessionid <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-k, &#8211;insecure</i>.</p>
<dt>&#8211;noproxy &lt;no-proxy-list&gt;</p>
<dd> Comma-separated list of hosts for which not to use a proxy, if one is specified. The only wildcard is a single * character, which matches all hosts, and effectively disables the proxy. Each name in this list is matched as either a domain which contains the hostname, or the hostname itself. For example, local.com would match local.com, local.com:80, and <a rel="nofollow" href="http://www.local.com">www.local.com</a>, but not <a rel="nofollow" href="http://www.notlocal.com">www.notlocal.com</a>. </p>
<p> Since 7.53.0, This option overrides the environment variables that disable the proxy (&#8216;no_proxy&#8217; and &#8216;NO_PROXY&#8217;). If there&#8217;s an environment variable disabling a proxy, you can set the noproxy list to &quot;&quot; to override it. </p>
<p> Example: </p>
<pre>
 curl --noproxy &quot;<a rel="nofollow" href="http://www.example">www.example</a>&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i>.</p>
<dt>&#8211;ntlm-wb</p>
<dd> (HTTP) Enables NTLM much in the style <i>&#8211;ntlm</i> does, but hand over the authentication to the separate binary ntlmauth application that is executed when needed. </p>
<p> Example: </p>
<pre>
 curl --ntlm-wb -u user:password <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;ntlm</i> and <i>&#8211;proxy-ntlm</i>.</p>
<dt>&#8211;ntlm</p>
<dd> (HTTP) Enables NTLM authentication. The NTLM authentication method was designed by Microsoft and is used by IIS web servers. It is a proprietary protocol, reverse-engineered by clever people and implemented in curl based on their efforts. This kind of behavior should not be endorsed, you should encourage everyone who uses NTLM to switch to a public and documented authentication method instead, such as Digest. </p>
<p> If you want to enable NTLM for your proxy authentication, then use <i>&#8211;proxy-ntlm</i>. </p>
<p> If this option is used several times, only the first one is used. </p>
<p> Example: </p>
<pre>
 curl --ntlm -u user:password <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-ntlm</i>. <i>&#8211;ntlm</i> requires that the underlying libcurl was built to support TLS. This option overrides <i>&#8211;basic</i> and <i>&#8211;negotiate</i> and <i>&#8211;digest</i> and <i>&#8211;anyauth</i>.</p>
<dt>&#8211;oauth2-bearer &lt;token&gt;</p>
<dd> (IMAP POP3 SMTP HTTP) Specify the Bearer Token for OAUTH 2.0 server authentication. The Bearer Token is used in conjunction with the user name which can be specified as part of the <i>&#8211;url</i> or <i>-u, &#8211;user</i> options. </p>
<p> The Bearer Token and user name are formatted according to RFC 6750. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --oauth2-bearer &quot;mF_9.B5f-4.1JqM&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;basic</i>, <i>&#8211;ntlm</i> and <i>&#8211;digest</i>. Added in 7.33.0.</p>
<dt>&#8211;output-dir &lt;dir&gt;</p>
<dd>
<p> This option specifies the directory in which files should be stored, when <i>-O, &#8211;remote-name</i> or <i>-o, &#8211;output</i> are used. </p>
<p> The given output directory is used for all URLs and output options on the command line, up until the first <i>-:, &#8211;next</i>. </p>
<p> If the specified target directory does not exist, the operation will fail unless <i>&#8211;create-dirs</i> is also used. </p>
<p> If this option is used multiple times, the last specified directory will be used. </p>
<p> Example: </p>
<pre>
 curl --output-dir &quot;tmp&quot; -O <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-O, &#8211;remote-name</i> and <i>-J, &#8211;remote-header-name</i>. Added in 7.73.0.</p>
<dt>-o, &#8211;output &lt;file&gt;</p>
<dd> Write output to &lt;file&gt; instead of stdout. If you are using {} or [] to fetch multiple documents, you should quote the URL and you can use &#8216;#&#8217; followed by a number in the &lt;file&gt; specifier. That variable will be replaced with the current string for the URL being fetched. Like in: </p>
<pre>
 curl &quot;<a rel="nofollow" href="http://{one,two}.example.com">http://{one,two}.example.com</a>&quot; -o &quot;file_#1.txt&quot;
</pre>
<p> or use several variables like: </p>
<p>curl &#8220;http://{site,host}.host[1-5].com&#8221; &#8211; o &#8220;#1_#2&#8221;</p>
<p> You may use this option as many times as the number of URLs you have. For example, if you specify two URLs on the same command line, you can use it like this: </p>
<pre>
  curl -o aa example.com -o bb example.net
</pre>
<p> and the order of the -o options and the URLs does not matter, just that the first -o is for the first URL and so on, so the above command line can also be written as </p>
<pre>
  curl example.com example.net -o aa -o bb
</pre>
<p> See also the <i>&#8211;create-dirs</i> option to create the local directories dynamically. Specifying the output as &#8216;-&#8216; (a single dash) will force the output to be done to stdout. </p>
<p> To suppress response bodies, you can redirect output to /dev/null: </p>
<pre>
  curl example.com -o /dev/null
</pre>
<p> Or for Windows use nul: </p>
<p>curl example.com &#8211; o nul Examples : curl &#8211; o file https : // example.com<br />
                                                          curl &#8220;http://{one,two}.example.com&#8221; &#8211;<br />
                                                          o &#8220;file_#1.txt&#8221; curl &#8220;http://{site,host}.host[1-5].com&#8221; &#8211; o &#8220;#1_#2&#8221; curl &#8211; o file https: // example.com -o file2 https://example.net</p>
<p> See also <i>-O, &#8211;remote-name</i>, <i>&#8211;remote-name-all</i> and <i>-J, &#8211;remote-header-name</i>.</p>
<dt>&#8211;parallel-immediate</p>
<dd> When doing parallel transfers, this option will instruct curl that it should rather prefer opening up more connections in parallel at once rather than waiting to see if new transfers can be added as multiplexed streams on another connection. </p>
<p> This option is global and does not need to be specified for each use of <i>-:, &#8211;next</i>. </p>
<p> Example: </p>
<pre>
 curl --parallel-immediate -Z <a rel="nofollow" href="https://example.com">https://example.com</a> -o file1 <a rel="nofollow" href="https://example.com">https://example.com</a> -o file2
</pre>
<p> See also <i>-Z, &#8211;parallel</i> and <i>&#8211;parallel-max</i>. Added in 7.68.0.</p>
<dt>&#8211;parallel-max &lt;num&gt;</p>
<dd> When asked to do parallel transfers, using <i>-Z, &#8211;parallel</i>, this option controls the maximum amount of transfers to do simultaneously. </p>
<p> This option is global and does not need to be specified for each use of <i>-:, &#8211;next</i>. </p>
<p> The default is 50. </p>
<p> Example: </p>
<pre>
 curl --parallel-max 100 -Z <a rel="nofollow" href="https://example.com">https://example.com</a> <a href="ftp://example.com/">ftp://example.com/</a>
</pre>
<p> See also <i>-Z, &#8211;parallel</i>. Added in 7.66.0.</p>
<dt>-Z, &#8211;parallel</p>
<dd> Makes curl perform its transfers in parallel as compared to the regular serial manner. </p>
<p> This option is global and does not need to be specified for each use of <i>-:, &#8211;next</i>. </p>
<p> Example: </p>
<pre>
 curl --parallel <a rel="nofollow" href="https://example.com">https://example.com</a> -o file1 <a rel="nofollow" href="https://example.com">https://example.com</a> -o file2
</pre>
<p> See also <i>-:, &#8211;next</i> and <i>-v, &#8211;verbose</i>. Added in 7.66.0.</p>
<dt>&#8211;pass &lt;phrase&gt;</p>
<dd> (SSH TLS) Passphrase for the private key. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --pass secret --key file <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;key</i> and <i>-u, &#8211;user</i>.</p>
<dt>&#8211;path-as-is</p>
<dd> Tell curl to not handle sequences of /../ or /./ in the given URL path. Normally curl will squash or merge them according to standards but with this option set you tell it not to do that. </p>
<p> Example: </p>
<pre>
 curl --path-as-is <a rel="nofollow" href="https://example.com/../../etc/passwd">https://example.com/../../etc/passwd</a>
</pre>
<p> See also <i>&#8211;request-target</i>. Added in 7.42.0.</p>
<dt>&#8211;pinnedpubkey &lt;hashes&gt;</p>
<dd> (TLS) Tells curl to use the specified public key file (or hashes) to verify the peer. This can be a path to a file which contains a single public key in PEM or DER format, or any number of base64 encoded sha256 hashes preceded by &#8216;sha256//&#8217; and separated by &#8216;;&#8217;. </p>
<p> When negotiating a TLS or SSL connection, the server sends a certificate indicating its identity. A public key is extracted from this certificate and if it does not exactly match the public key provided to this option, curl will abort the connection before sending or receiving any data. </p>
<p> PEM/DER support: </p>
<p> 7.39.0: OpenSSL, GnuTLS and GSKit </p>
<p> 7.43.0: NSS and wolfSSL </p>
<p> 7.47.0: mbedtls </p>
<p> sha256 support: </p>
<p> 7.44.0: OpenSSL, GnuTLS, NSS and wolfSSL </p>
<p> 7.47.0: mbedtls </p>
<p> Other SSL backends not supported. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Examples: </p>
<pre>
 curl --pinnedpubkey keyfile <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl --pinnedpubkey 'sha256//ce118b51897f4452dc' <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;hostpubsha256</i>. Added in 7.39.0.</p>
<dt>&#8211;post301</p>
<dd> (HTTP) Tells curl to respect RFC 7231/6.4.2 and not convert POST requests into GET requests when following a 301 redirection. The non-RFC behavior is ubiquitous in web browsers, so curl does the conversion by default to maintain consistency. However, a server may require a POST to remain a POST after such a redirection. This option is meaningful only when using <i>-L, &#8211;location</i>. </p>
<p> Example: </p>
<pre>
 curl --post301 --location -d &quot;data&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;post302</i>, <i>&#8211;post303</i> and <i>-L, &#8211;location</i>.</p>
<dt>&#8211;post302</p>
<dd> (HTTP) Tells curl to respect RFC 7231/6.4.3 and not convert POST requests into GET requests when following a 302 redirection. The non-RFC behavior is ubiquitous in web browsers, so curl does the conversion by default to maintain consistency. However, a server may require a POST to remain a POST after such a redirection. This option is meaningful only when using <i>-L, &#8211;location</i>. </p>
<p> Example: </p>
<pre>
 curl --post302 --location -d &quot;data&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;post301</i>, <i>&#8211;post303</i> and <i>-L, &#8211;location</i>.</p>
<dt>&#8211;post303</p>
<dd> (HTTP) Tells curl to violate RFC 7231/6.4.4 and not convert POST requests into GET requests when following 303 redirections. A server may require a POST to remain a POST after a 303 redirection. This option is meaningful only when using <i>-L, &#8211;location</i>. </p>
<p> Example: </p>
<pre>
 curl --post303 --location -d &quot;data&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;post302</i>, <i>&#8211;post301</i> and <i>-L, &#8211;location</i>.</p>
<dt>&#8211;preproxy [protocol://]host[:port]</p>
<dd> Use the specified SOCKS proxy before connecting to an HTTP or HTTPS <i>-x, &#8211;proxy</i>. In such a case curl first connects to the SOCKS proxy and then connects (through SOCKS) to the HTTP or HTTPS proxy. Hence pre proxy. </p>
<p> The pre proxy string should be specified with a protocol:// prefix to specify alternative proxy protocols. Use socks4://, socks4a://, socks5:// or socks5h:// to request the specific SOCKS version to be used. No protocol specified will make curl default to SOCKS4. </p>
<p> If the port number is not specified in the proxy string, it is assumed to be 1080. </p>
<p> User and password that might be provided in the proxy string are URL decoded by curl. This allows you to pass in special characters such as @ by using %40 or pass in a colon with %3a. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --preproxy socks5://proxy.example -x <a rel="nofollow" href="http://http.example">http://http.example</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i> and <i>&#8211;socks5</i>. Added in 7.52.0.</p>
<dt>-#, &#8211;progress-bar</p>
<dd> Make curl display transfer progress as a simple progress bar instead of the standard, more informational, meter. </p>
<p> This progress bar draws a single line of &#8216;#&#8217; characters across the screen and shows a percentage if the transfer size is known. For transfers without a known size, there will be space ship (-=o=-) that moves back and forth but only while data is being transferred, with a set of flying hash sign symbols on top. </p>
<p> This option is global and does not need to be specified for each use of <i>-:, &#8211;next</i>. </p>
<p> Example: </p>
<pre>
 curl -# -O <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;styled-output</i>.</p>
<dt>&#8211;proto-default &lt;protocol&gt;</p>
<dd> Tells curl to use <i>protocol</i> for any URL missing a scheme name. </p>
<p> An unknown or unsupported protocol causes error <i>CURLE_UNSUPPORTED_PROTOCOL</i> (1). </p>
<p> This option does not change the default proxy protocol (http). </p>
<p> Without this option set, curl guesses protocol based on the host name, see <i>&#8211;url</i> for details. </p>
<p> Example: </p>
<pre>
 curl --proto-default https <a href="ftp://ftp.example.com">ftp.example.com</a>
</pre>
<p> See also <i>&#8211;proto</i> and <i>&#8211;proto-redir</i>. Added in 7.45.0.</p>
<dt>&#8211;proto-redir &lt;protocols&gt;</p>
<dd> Tells curl to limit what protocols it may use on redirect. Protocols denied by <i>&#8211;proto</i> are not overridden by this option. See &#8211;proto for how protocols are represented. </p>
<p> Example, allow only HTTP and HTTPS on redirect: </p>
<pre>
 curl --proto-redir -all,http,https <a rel="nofollow" href="http://example.com">http://example.com</a>
</pre>
<p> By default curl will only allow HTTP, HTTPS, FTP and FTPS on redirect (since 7.65.2). Specifying <i>all</i> or <i>+all</i> enables all protocols on redirects, which is not good for security. </p>
<p> Example: </p>
<pre>
 curl --proto-redir =http,https <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proto</i>.</p>
<dt>&#8211;proto &lt;protocols&gt;</p>
<dd> Tells curl to limit what protocols it may use for transfers. Protocols are evaluated left to right, are comma separated, and are each a protocol name or &#8216;all&#8217;, optionally prefixed by zero or more modifiers. Available modifiers are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>+</code></p>
<dd> Permit this protocol in addition to protocols already permitted (this is the default if no modifier is used).</p>
<dt><code>&#8211;</code></p>
<dd> Deny this protocol, removing it from the list of protocols already permitted.</p>
<dt><code>=</code></p>
<dd> Permit only this protocol (ignoring the list already permitted), though subject to later modification by subsequent entries in the comma separated list.</dl>
</dl>
<dt>
<dd> For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>&#8211;proto</i> -ftps</p>
<dd> uses the default protocols, but disables ftps</p>
<dt><i>&#8211;proto</i> -all,https,+http</p>
<dd> only enables http and https</p>
<dt><i>&#8211;proto</i> =http,https</p>
<dd> also only enables http and https</dl>
</dl>
<dt>
<dd> Unknown protocols produce a warning. This allows scripts to safely rely on being able to disable potentially dangerous protocols, without relying upon support for that protocol being built into curl to avoid an error. </p>
<p> This option can be used multiple times, in which case the effect is the same as concatenating the protocols into one instance of the option. </p>
<p> Example: </p>
<pre>
 curl --proto =http,https,sftp <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proto-redir</i> and <i>&#8211;proto-default</i>.</p>
<dt>&#8211;proxy-anyauth</p>
<dd> Tells curl to pick a suitable authentication method when communicating with the given HTTP proxy. This might cause an extra request/response round-trip. </p>
<p> Example: </p>
<pre>
 curl --proxy-anyauth --proxy-user user:passwd -x proxy <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i>, <i>&#8211;proxy-basic</i> and <i>&#8211;proxy-digest</i>.</p>
<dt>&#8211;proxy-basic</p>
<dd> Tells curl to use HTTP Basic authentication when communicating with the given proxy. Use <i>&#8211;basic</i> for enabling HTTP Basic with a remote host. Basic is the default authentication method curl uses with proxies. </p>
<p> Example: </p>
<pre>
 curl --proxy-basic --proxy-user user:passwd -x proxy <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i>, <i>&#8211;proxy-anyauth</i> and <i>&#8211;proxy-digest</i>.</p>
<dt>&#8211;proxy-cacert &lt;file&gt;</p>
<dd> Same as <i>&#8211;cacert</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-cacert CA-file.txt -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-capath</i>, <i>&#8211;cacert</i>, <i>&#8211;capath</i> and <i>-x, &#8211;proxy</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-capath &lt;dir&gt;</p>
<dd> Same as <i>&#8211;capath</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-capath /local/directory -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-cacert</i>, <i>-x, &#8211;proxy</i> and <i>&#8211;capath</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-cert-type &lt;type&gt;</p>
<dd> Same as <i>&#8211;cert-type</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-cert-type PEM --proxy-cert file -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-cert</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-cert &lt;cert[:passwd]&gt;</p>
<dd> Same as <i>-E, &#8211;cert</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-cert file -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-cert-type</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-ciphers &lt;list&gt;</p>
<dd> Same as <i>&#8211;ciphers</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-ciphers ECDHE-ECDSA-AES256-CCM8 -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;ciphers</i>, <i>&#8211;curves</i> and <i>-x, &#8211;proxy</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-crlfile &lt;file&gt;</p>
<dd> Same as <i>&#8211;crlfile</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-crlfile rejects.txt -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;crlfile</i> and <i>-x, &#8211;proxy</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-digest</p>
<dd> Tells curl to use HTTP Digest authentication when communicating with the given proxy. Use <i>&#8211;digest</i> for enabling HTTP Digest with a remote host. </p>
<p> Example: </p>
<pre>
 curl --proxy-digest --proxy-user user:passwd -x proxy <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i>, <i>&#8211;proxy-anyauth</i> and <i>&#8211;proxy-basic</i>.</p>
<dt>&#8211;proxy-header &lt;header/@file&gt;</p>
<dd> (HTTP) Extra header to include in the request when sending HTTP to a proxy. You may specify any number of extra headers. This is the equivalent option to <i>-H, &#8211;header</i> but is for proxy communication only like in CONNECT requests when you want a separate header sent to the proxy to what is sent to the actual remote host. </p>
<p> curl will make sure that each header you add/replace is sent with the proper end-of-line marker, you should thus <code>not</code> add that as a part of the header content: do not add newlines or carriage returns, they will only mess things up for you. </p>
<p> Headers specified with this option will not be included in requests that curl knows will not be sent to a proxy. </p>
<p> Starting in 7.55.0, this option can take an argument in @filename style, which then adds a header for each line in the input file. Using @- will make curl read the header file from stdin. </p>
<p> This option can be used multiple times to add/replace/remove multiple headers. </p>
<p> Examples: </p>
<pre>
 curl --proxy-header &quot;X-First-Name: Joe&quot; -x <a rel="nofollow" href="http://proxy">http://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl --proxy-header &quot;User-Agent: surprise&quot; -x <a rel="nofollow" href="http://proxy">http://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl --proxy-header &quot;Host:&quot; -x <a rel="nofollow" href="http://proxy">http://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i>. Added in 7.37.0.</p>
<dt>&#8211;proxy-insecure</p>
<dd> Same as <i>-k, &#8211;insecure</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-insecure -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i> and <i>-k, &#8211;insecure</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-key-type &lt;type&gt;</p>
<dd> Same as <i>&#8211;key-type</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-key-type DER --proxy-key here -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-key</i> and <i>-x, &#8211;proxy</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-key &lt;key&gt;</p>
<dd> Same as <i>&#8211;key</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-key here -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-key-type</i> and <i>-x, &#8211;proxy</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-negotiate</p>
<dd> Tells curl to use HTTP Negotiate (SPNEGO) authentication when communicating with the given proxy. Use <i>&#8211;negotiate</i> for enabling HTTP Negotiate (SPNEGO) with a remote host. </p>
<p> Example: </p>
<pre>
 curl --proxy-negotiate --proxy-user user:passwd -x proxy <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-anyauth</i> and <i>&#8211;proxy-basic</i>.</p>
<dt>&#8211;proxy-ntlm</p>
<dd> Tells curl to use HTTP NTLM authentication when communicating with the given proxy. Use <i>&#8211;ntlm</i> for enabling NTLM with a remote host. </p>
<p> Example: </p>
<pre>
 curl --proxy-ntlm --proxy-user user:passwd -x <a rel="nofollow" href="http://proxy">http://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-negotiate</i> and <i>&#8211;proxy-anyauth</i>.</p>
<dt>&#8211;proxy-pass &lt;phrase&gt;</p>
<dd> Same as <i>&#8211;pass</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-pass secret --proxy-key here -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i> and <i>&#8211;proxy-key</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-pinnedpubkey &lt;hashes&gt;</p>
<dd> (TLS) Tells curl to use the specified public key file (or hashes) to verify the proxy. This can be a path to a file which contains a single public key in PEM or DER format, or any number of base64 encoded sha256 hashes preceded by &#8216;sha256//&#8217; and separated by &#8216;;&#8217;. </p>
<p> When negotiating a TLS or SSL connection, the server sends a certificate indicating its identity. A public key is extracted from this certificate and if it does not exactly match the public key provided to this option, curl will abort the connection before sending or receiving any data. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Examples: </p>
<pre>
 curl --proxy-pinnedpubkey keyfile <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl --proxy-pinnedpubkey 'sha256//ce118b51897f4452dc' <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;pinnedpubkey</i> and <i>-x, &#8211;proxy</i>. Added in 7.59.0.</p>
<dt>&#8211;proxy-service-name &lt;name&gt;</p>
<dd> This option allows you to change the service name for proxy negotiation. </p>
<p> Example: </p>
<pre>
 curl --proxy-service-name &quot;shrubbery&quot; -x proxy <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;service-name</i> and <i>-x, &#8211;proxy</i>. Added in 7.43.0.</p>
<dt>&#8211;proxy-ssl-allow-beast</p>
<dd> Same as <i>&#8211;ssl-allow-beast</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-ssl-allow-beast -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;ssl-allow-beast</i> and <i>-x, &#8211;proxy</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-ssl-auto-client-cert</p>
<dd> Same as <i>&#8211;ssl-auto-client-cert</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-ssl-auto-client-cert -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;ssl-auto-client-cert</i> and <i>-x, &#8211;proxy</i>. Added in 7.77.0.</p>
<dt>&#8211;proxy-tls13-ciphers &lt;ciphersuite list&gt;</p>
<dd> (TLS) Specifies which cipher suites to use in the connection to your HTTPS proxy when it negotiates TLS 1.3. The list of ciphers suites must specify valid ciphers. Read up on TLS 1.3 cipher suite details on this URL: </p>
<pre>
 <a rel="nofollow" href="https://curl.se/docs/ssl-ciphers.html">https://curl.se/docs/ssl-ciphers.html</a>
</pre>
<p> This option is currently used only when curl is built to use OpenSSL 1.1.1 or later. If you are using a different SSL backend you can try setting TLS 1.3 cipher suites by using the <i>&#8211;proxy-ciphers</i> option. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --proxy-tls13-ciphers TLS_AES_128_GCM_SHA256 -x proxy <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;tls13-ciphers</i> and <i>&#8211;curves</i>. Added in 7.61.0.</p>
<dt>&#8211;proxy-tlsauthtype &lt;type&gt;</p>
<dd> Same as <i>&#8211;tlsauthtype</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-tlsauthtype SRP -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i> and <i>&#8211;proxy-tlsuser</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-tlspassword &lt;string&gt;</p>
<dd> Same as <i>&#8211;tlspassword</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-tlspassword passwd -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i> and <i>&#8211;proxy-tlsuser</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-tlsuser &lt;name&gt;</p>
<dd> Same as <i>&#8211;tlsuser</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-tlsuser smith -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i> and <i>&#8211;proxy-tlspassword</i>. Added in 7.52.0.</p>
<dt>&#8211;proxy-tlsv1</p>
<dd> Same as <i>-1, &#8211;tlsv1</i> but used in HTTPS proxy context. </p>
<p> Example: </p>
<pre>
 curl --proxy-tlsv1 -x <a rel="nofollow" href="https://proxy">https://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i>. Added in 7.52.0.</p>
<dt>-U, &#8211;proxy-user &lt;user:password&gt;</p>
<dd> Specify the user name and password to use for proxy authentication. </p>
<p> If you use a Windows SSPI-enabled curl binary and do either Negotiate or NTLM authentication then you can tell curl to select the user name and password from your environment by specifying a single colon with this option: &quot;-U :&quot;. </p>
<p> On systems where it works, curl will hide the given option argument from process listings. This is not enough to protect credentials from possibly getting seen by other users on the same system as they will still be visible for a moment before cleared. Such sensitive data should be retrieved from a file instead or similar and never used in clear text in a command line. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --proxy-user name:pwd -x proxy <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-pass</i>.</p>
<dt>-x, &#8211;proxy [protocol://]host[:port]</p>
<dd> Use the specified proxy. </p>
<p> The proxy string can be specified with a protocol:// prefix. No protocol specified or http:// will be treated as HTTP proxy. Use socks4://, socks4a://, socks5:// or socks5h:// to request a specific SOCKS version to be used. </p>
<p> HTTPS proxy support via https:// protocol prefix was added in 7.52.0 for OpenSSL, GnuTLS and NSS. </p>
<p> Unrecognized and unsupported proxy protocols cause an error since 7.52.0. Prior versions may ignore the protocol and use http:// instead. </p>
<p> If the port number is not specified in the proxy string, it is assumed to be 1080. </p>
<p> This option overrides existing environment variables that set the proxy to use. If there&#8217;s an environment variable setting a proxy, you can set proxy to &quot;&quot; to override it. </p>
<p> All operations that are performed over an HTTP proxy will transparently be converted to HTTP. It means that certain protocol specific operations might not be available. This is not the case if you can tunnel through the proxy, as one with the <i>-p, &#8211;proxytunnel</i> option. </p>
<p> User and password that might be provided in the proxy string are URL decoded by curl. This allows you to pass in special characters such as @ by using %40 or pass in a colon with %3a. </p>
<p> The proxy host can be specified the same way as the proxy environment variables, including the protocol prefix (<a rel="nofollow" href="http://)">http://)</a> and the embedded user + password. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --proxy <a rel="nofollow" href="http://proxy.example">http://proxy.example</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;socks5</i> and <i>&#8211;proxy-basic</i>.</p>
<dt>&#8211;proxy1.0 &lt;host[:port]&gt;</p>
<dd> Use the specified HTTP 1.0 proxy. If the port number is not specified, it is assumed at port 1080. </p>
<p> The only difference between this and the HTTP proxy option <i>-x, &#8211;proxy</i>, is that attempts to use CONNECT through the proxy will specify an HTTP 1.0 protocol instead of the default HTTP 1.1. </p>
<p> Example: </p>
<pre>
 curl --proxy1.0 -x <a rel="nofollow" href="http://proxy">http://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i>, <i>&#8211;socks5</i> and <i>&#8211;preproxy</i>.</p>
<dt>-p, &#8211;proxytunnel</p>
<dd> When an HTTP proxy is used <i>-x, &#8211;proxy</i>, this option will make curl tunnel through the proxy. The tunnel approach is made with the HTTP proxy CONNECT request and requires that the proxy allows direct connect to the remote port number curl wants to tunnel through to. </p>
<p> To suppress proxy CONNECT response headers when curl is set to output headers use <i>&#8211;suppress-connect-headers</i>. </p>
<p> Example: </p>
<pre>
 curl --proxytunnel -x <a rel="nofollow" href="http://proxy">http://proxy</a> <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-x, &#8211;proxy</i>.</p>
<dt>&#8211;pubkey &lt;key&gt;</p>
<dd> (SFTP SCP) Public key file name. Allows you to provide your public key in this separate file. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> (As of 7.39.0, curl attempts to automatically extract the public key from the private key file, so passing this option is generally not required. Note that this public key extraction requires libcurl to be linked against a copy of libssh2 1.2.8 or higher that is itself linked against OpenSSL.) </p>
<p> Example: </p>
<pre>
 curl --pubkey file.pub <a href="sftp://example.com/">sftp://example.com/</a>
</pre>
<p> See also <i>&#8211;pass</i>.</p>
<dt>-Q, &#8211;quote &lt;command&gt;</p>
<dd> (FTP SFTP) Send an arbitrary command to the remote FTP or SFTP server. Quote commands are sent BEFORE the transfer takes place (just after the initial PWD command in an FTP transfer, to be exact). To make commands take place after a successful transfer, prefix them with a dash &#8216;-&#8216;. To make commands be sent after curl has changed the working directory, just before the transfer command(s), prefix the command with a &#8216;+&#8217; (this is only supported for FTP). You may specify any number of commands. </p>
<p> By default curl will stop at first failure. To make curl continue even if the command fails, prefix the command with an asterisk (*). Otherwise, if the server returns failure for one of the commands, the entire operation will be aborted. </p>
<p> You must send syntactically correct FTP commands as RFC 959 defines to FTP servers, or one of the commands listed below to SFTP servers. </p>
<p> This option can be used multiple times. </p>
<p> SFTP is a binary protocol. Unlike for FTP, curl interprets SFTP quote commands itself before sending them to the server. File names may be quoted shell-style to embed spaces or special characters. Following is the list of all supported SFTP quote commands:</p>
<dl>
<dt>
<dd>
<dl>
<dt>atime date file</p>
<dd> The atime command sets the last access time of the file named by the file operand. The &lt;date expression&gt; can be all sorts of date strings, see the <i><a href="/docs/linux/man/3-curl_getdate/">curl_getdate</a>(3)</i> man page for date expression details. (Added in 7.73.0)</p>
<dt>chgrp group file</p>
<dd> The chgrp command sets the group ID of the file named by the file operand to the group ID specified by the group operand. The group operand is a decimal integer group ID.</p>
<dt>chmod mode file</p>
<dd> The chmod command modifies the file mode bits of the specified file. The mode operand is an octal integer mode number.</p>
<dt>chown user file</p>
<dd> The chown command sets the owner of the file named by the file operand to the user ID specified by the user operand. The user operand is a decimal integer user ID.</p>
<dt>ln source_file target_file</p>
<dd> The ln and symlink commands create a symbolic link at the target_file location pointing to the source_file location.</p>
<dt>mkdir directory_name</p>
<dd> The mkdir command creates the directory named by the directory_name operand.</p>
<dt>mtime date file</p>
<dd> The mtime command sets the last modification time of the file named by the file operand. The &lt;date expression&gt; can be all sorts of date strings, see the <i><a href="/docs/linux/man/3-curl_getdate/">curl_getdate</a>(3)</i> man page for date expression details. (Added in 7.73.0)</p>
<dt>pwd</p>
<dd> The pwd command returns the absolute pathname of the current working directory.</p>
<dt>rename source target</p>
<dd> The rename command renames the file or directory named by the source operand to the destination path named by the target operand.</p>
<dt>rm file</p>
<dd> The rm command removes the file specified by the file operand.</p>
<dt>rmdir directory</p>
<dd> The rmdir command removes the directory entry specified by the directory operand, provided it is empty.</p>
<dt>symlink source_file target_file</p>
<dd> See ln.</dl>
</dl>
<p> Example: </p>
<pre>
 curl --quote &quot;DELE file&quot; <a href="ftp://example.com/foo">ftp://example.com/foo</a>
</pre>
<p> See also <i>-X, &#8211;request</i>.</p>
<dt>&#8211;random-file &lt;file&gt;</p>
<dd> Specify the path name to file containing what will be considered as random data. The data may be used to seed the random engine for SSL connections. See also the <i>&#8211;egd-file</i> option. </p>
<p> Example: </p>
<pre>
 curl --random-file rubbish <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;egd-file</i>.</p>
<dt>-r, &#8211;range &lt;range&gt;</p>
<dd> (HTTP FTP SFTP FILE) Retrieve a byte range (i.e. a partial document) from an HTTP/1.1, FTP or SFTP server or a local FILE. Ranges can be specified in a number of ways.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0-499</code></p>
<dd> specifies the first 500 bytes</p>
<dt><code>500-999</code></p>
<dd> specifies the second 500 bytes</p>
<dt><code>-500</code></p>
<dd> specifies the last 500 bytes</p>
<dt><code>9500-</code></p>
<dd> specifies the bytes from offset 9500 and forward</p>
<dt><code>0-0,-1</code></p>
<dd> specifies the first and last byte only(*)(HTTP)</p>
<dt><code>100-199,500-599</code></p>
<dd> specifies two separate 100-byte ranges(*) (HTTP)</dl>
</dl>
<dt>
<dd> (*) = NOTE that this will cause the server to reply with a multipart response, which will be returned as-is by curl! Parsing or otherwise transforming this response is the responsibility of the caller. </p>
<p> Only digit characters (0-9) are valid in the &#8216;start&#8217; and &#8216;stop&#8217; fields of the &#8216;start-stop&#8217; range syntax. If a non-digit character is given in the range, the server&#8217;s response will be unspecified, depending on the server&#8217;s configuration. </p>
<p> You should also be aware that many HTTP/1.1 servers do not have this feature enabled, so that when you attempt to get a range, you will instead get the whole document. </p>
<p> FTP and SFTP range downloads only support the simple &#8216;start-stop&#8217; syntax (optionally with one of the numbers omitted). FTP use depends on the extended FTP command SIZE. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --range 22-44 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-C, &#8211;continue-at</i> and <i>-a, &#8211;append</i>.</p>
<dt>&#8211;raw</p>
<dd> (HTTP) When used, it disables all internal HTTP decoding of content or transfer encodings and instead makes them passed on unaltered, raw. </p>
<p> Example: </p>
<pre>
 curl --raw <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;tr-encoding</i>.</p>
<dt>-e, &#8211;referer &lt;URL&gt;</p>
<dd> (HTTP) Sends the &quot;Referrer Page&quot; information to the HTTP server. This can also be set with the <i>-H, &#8211;header</i> flag of course. When used with <i>-L, &#8211;location</i> you can append &quot;;auto&quot; to the <i>-e, &#8211;referer</i> URL to make curl automatically set the previous URL when it follows a Location: header. The &quot;;auto&quot; string can be used alone, even if you do not set an initial <i>-e, &#8211;referer</i>. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Examples:<br />
curl&#8211; referer &#8220;https://fake.example&#8221; https : // example.com<br />
                                              curl&#8211; referer &#8220;https://fake.example;auto&#8221; &#8211;<br />
                                              L https : // example.com<br />
                                                        curl&#8211; referer &#8220;;auto&#8221; &#8211;<br />
                                                        L https: // example.com</p>
<p> See also <i>-A, &#8211;user-agent</i> and <i>-H, &#8211;header</i>.</p>
<dt>-J, &#8211;remote-header-name</p>
<dd> (HTTP) This option tells the <i>-O, &#8211;remote-name</i> option to use the server-specified Content-Disposition filename instead of extracting a filename from the URL. </p>
<p> If the server specifies a file name and a file with that name already exists in the current working directory it will not be overwritten and an error will occur. If the server does not specify a file name then this option has no effect. </p>
<p> There&#8217;s no attempt to decode %-sequences (yet) in the provided file name, so this option may provide you with rather unexpected file names. </p>
<p> <code>WARNING</code>: Exercise judicious use of this option, especially on Windows. A rogue server could send you the name of a DLL or other file that could be loaded automatically by Windows or some third party software. </p>
<p> Example: </p>
<pre>
 curl -OJ <a rel="nofollow" href="https://example.com/file">https://example.com/file</a>
</pre>
<p> See also <i>-O, &#8211;remote-name</i>.</p>
<dt>&#8211;remote-name-all</p>
<dd> This option changes the default action for all given URLs to be dealt with as if <i>-O, &#8211;remote-name</i> were used for each one. So if you want to disable that for a specific URL after <i>&#8211;remote-name-all</i> has been used, you must use &quot;-o -&quot; or &#8211;no-remote-name. </p>
<p> Example: </p>
<pre>
 curl --remote-name-all <a href="ftp://example.com/file1">ftp://example.com/file1</a> <a href="ftp://example.com/file2">ftp://example.com/file2</a>
</pre>
<p> See also <i>-O, &#8211;remote-name</i>.</p>
<dt>-O, &#8211;remote-name</p>
<dd> Write output to a local file named like the remote file we get. (Only the file part of the remote file is used, the path is cut off.) </p>
<p> The file will be saved in the current working directory. If you want the file saved in a different directory, make sure you change the current working directory before invoking curl with this option. </p>
<p> The remote file name to use for saving is extracted from the given URL, nothing else, and if it already exists it will be overwritten. If you want the server to be able to choose the file name refer to <i>-J, &#8211;remote-header-name</i> which can be used in addition to this option. If the server chooses a file name and that name already exists it will not be overwritten. </p>
<p> There is no URL decoding done on the file name. If it has %20 or other URL encoded parts of the name, they will end up as-is as file name. </p>
<p> You may use this option as many times as the number of URLs you have. </p>
<p> Example: </p>
<pre>
 curl -O <a rel="nofollow" href="https://example.com/filename">https://example.com/filename</a>
</pre>
<p> See also <i>&#8211;remote-name-all</i>.</p>
<dt>-R, &#8211;remote-time</p>
<dd> When used, this will make curl attempt to figure out the timestamp of the remote file, and if that is available make the local file get that same timestamp. </p>
<p> Example: </p>
<pre>
 curl --remote-time -o foo <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-O, &#8211;remote-name</i> and <i>-z, &#8211;time-cond</i>.</p>
<dt>&#8211;request-target &lt;path&gt;</p>
<dd> (HTTP) Tells curl to use an alternative &quot;target&quot; (path) instead of using the path as provided in the URL. Particularly useful when wanting to issue HTTP requests without leading slash or other data that does not follow the regular URL pattern, like &quot;OPTIONS *&quot;. </p>
<p> Example: </p>
<pre>
 curl --request-target &quot;*&quot; -X OPTIONS <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-X, &#8211;request</i>. Added in 7.55.0.</p>
<dt>-X, &#8211;request &lt;method&gt;</p>
<dd> (HTTP) Specifies a custom request method to use when communicating with the HTTP server. The specified request method will be used instead of the method otherwise used (which defaults to GET). Read the HTTP 1.1 specification for details and explanations. Common additional HTTP requests include PUT and DELETE, but related technologies like WebDAV offers PROPFIND, COPY, MOVE and more. </p>
<p> Normally you do not need this option. All sorts of GET, HEAD, POST and PUT requests are rather invoked by using dedicated command line options. </p>
<p> This option only changes the actual word used in the HTTP request, it does not alter the way curl behaves. So for example if you want to make a proper HEAD request, using -X HEAD will not suffice. You need to use the <i>-I, &#8211;head</i> option. </p>
<p> The method string you set with <i>-X, &#8211;request</i> will be used for all requests, which if you for example use <i>-L, &#8211;location</i> may cause unintended side-effects when curl does not change request method according to the HTTP 30x response codes &#8211; and similar. </p>
<p> (FTP) Specifies a custom FTP command to use instead of LIST when doing file lists with FTP. </p>
<p> (POP3) Specifies a custom POP3 command to use instead of LIST or RETR. </p>
<p> (IMAP) Specifies a custom IMAP command to use instead of LIST. (Added in 7.30.0) </p>
<p> (SMTP) Specifies a custom SMTP command to use instead of HELP or VRFY. (Added in 7.34.0) </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Examples: </p>
<pre>
 curl -X &quot;DELETE&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl -X NLST <a href="ftp://example.com/">ftp://example.com/</a>
</pre>
<p> See also <i>&#8211;request-target</i>.</p>
<dt>&#8211;resolve &lt;[+]host:port:addr[,addr]&#8230;&gt;</p>
<dd> Provide a custom address for a specific host and port pair. Using this, you can make the curl requests(s) use a specified address and prevent the otherwise normally resolved address to be used. Consider it a sort of /etc/hosts alternative provided on the command line. The port number should be the number used for the specific protocol the host will be used for. It means you need several entries if you want to provide address for the same host but different ports. </p>
<p> By specifying &#8216;*&#8217; as host you can tell curl to resolve any host and specific port pair to the specified address. Wildcard is resolved last so any <i>&#8211;resolve</i> with a specific host and port will be used first. </p>
<p> The provided address set by this option will be used even if <i>-4, &#8211;ipv4</i> or <i>-6, &#8211;ipv6</i> is set to make curl use another IP version. </p>
<p> By prefixing the host with a &#8216;+&#8217; you can make the entry time out after curl&#8217;s default timeout (1 minute). Note that this will only make sense for long running parallel transfers with a lot of files. In such cases, if this option is used curl will try to resolve the host as it normally would once the timeout has expired. </p>
<p> Support for providing the IP address within [brackets] was added in 7.57.0. </p>
<p> Support for providing multiple IP addresses per entry was added in 7.59.0. </p>
<p> Support for resolving with wildcard was added in 7.64.0. </p>
<p> Support for the &#8216;+&#8217; prefix was was added in 7.75.0. </p>
<p> This option can be used many times to add many host names to resolve. </p>
<p> Example: </p>
<pre>
 curl --resolve example.com:443:127.0.0.1 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;connect-to</i> and <i>&#8211;alt-svc</i>.</p>
<dt>&#8211;retry-all-errors</p>
<dd> Retry on any error. This option is used together with <i>&#8211;retry</i>. </p>
<p> This option is the &quot;sledgehammer&quot; of retrying. Do not use this option by default (eg in curlrc), there may be unintended consequences such as sending or receiving duplicate data. Do not use with redirected input or output. You&#8217;d be much better off handling your unique problems in shell script. Please read the example below. </p>
<p> <code>WARNING</code>: For server compatibility curl attempts to retry failed flaky transfers as close as possible to how they were started, but this is not possible with redirected input or output. For example, before retrying it removes output data from a failed partial transfer that was written to an output file. However this is not true of data redirected to a | pipe or &gt; file, which are not reset. We strongly suggest you do not parse or record output via redirect in combination with this option, since you may receive duplicate data. </p>
<p> By default curl will not error on an HTTP response code that indicates an HTTP error, if the transfer was successful. For example, if a server replies 404 Not Found and the reply is fully received then that is not an error. When <i>&#8211;retry</i> is used then curl will retry on some HTTP response codes that indicate transient HTTP errors, but that does not include most 4xx response codes such as 404. If you want to retry on all response codes that indicate HTTP errors (4xx and 5xx) then combine with <i>-f, &#8211;fail</i>. </p>
<p> Example: </p>
<pre>
 curl --retry 5 --retry-all-errors <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;retry</i>. Added in 7.71.0.</p>
<dt>&#8211;retry-connrefused</p>
<dd> In addition to the other conditions, consider ECONNREFUSED as a transient error too for <i>&#8211;retry</i>. This option is used together with &#8211;retry. </p>
<p> Example: </p>
<pre>
 curl --retry-connrefused --retry <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;retry</i> and <i>&#8211;retry-all-errors</i>. Added in 7.52.0.</p>
<dt>&#8211;retry-delay &lt;seconds&gt;</p>
<dd> Make curl sleep this amount of time before each retry when a transfer has failed with a transient error (it changes the default backoff time algorithm between retries). This option is only interesting if <i>&#8211;retry</i> is also used. Setting this delay to zero will make curl use the default backoff time. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --retry-delay 5 --retry <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;retry</i>.</p>
<dt>&#8211;retry-max-time &lt;seconds&gt;</p>
<dd> The retry timer is reset before the first transfer attempt. Retries will be done as usual (see <i>&#8211;retry</i>) as long as the timer has not reached this given limit. Notice that if the timer has not reached the limit, the request will be made and while performing, it may take longer than this given time period. To limit a single request&#8217;s maximum time, use <i>-m, &#8211;max-time</i>. Set this option to zero to not timeout retries. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --retry-max-time 30 --retry 10 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;retry</i>.</p>
<dt>&#8211;retry &lt;num&gt;</p>
<dd> If a transient error is returned when curl tries to perform a transfer, it will retry this number of times before giving up. Setting the number to 0 makes curl do no retries (which is the default). Transient error means either: a timeout, an FTP 4xx response code or an HTTP 408, 429, 500, 502, 503 or 504 response code. </p>
<p> When curl is about to retry a transfer, it will first wait one second and then for all forthcoming retries it will double the waiting time until it reaches 10 minutes which then will be the delay between the rest of the retries. By using <i>&#8211;retry-delay</i> you disable this exponential backoff algorithm. See also <i>&#8211;retry-max-time</i> to limit the total time allowed for retries. </p>
<p> Since curl 7.66.0, curl will comply with the Retry-After: response header if one was present to know when to issue the next retry. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --retry 7 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;retry-max-time</i>.</p>
<dt>&#8211;sasl-authzid &lt;identity&gt;</p>
<dd> Use this authorisation identity (authzid), during SASL PLAIN authentication, in addition to the authentication identity (authcid) as specified by <i>-u, &#8211;user</i>. </p>
<p> If the option is not specified, the server will derive the authzid from the authcid, but if specified, and depending on the server implementation, it may be used to access another user&#8217;s inbox, that the user has been granted access to, or a shared mailbox for example. </p>
<p> Example: </p>
<pre>
 curl --sasl-authzid zid <a href="imap://example.com/">imap://example.com/</a>
</pre>
<p> See also <i>&#8211;login-options</i>. Added in 7.66.0.</p>
<dt>&#8211;sasl-ir</p>
<dd> Enable initial response in SASL authentication. </p>
<p> Example: </p>
<pre>
 curl --sasl-ir <a href="imap://example.com/">imap://example.com/</a>
</pre>
<p> See also <i>&#8211;sasl-authzid</i>. Added in 7.31.0.</p>
<dt>&#8211;service-name &lt;name&gt;</p>
<dd> This option allows you to change the service name for SPNEGO. </p>
<p> Examples: <i>&#8211;negotiate</i> <i>&#8211;service-name</i> sockd would use sockd/server-name. </p>
<p> Example: </p>
<pre>
 curl --service-name sockd/server <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;negotiate</i> and <i>&#8211;proxy-service-name</i>. Added in 7.43.0.</p>
<dt>-S, &#8211;show-error</p>
<dd> When used with <i>-s, &#8211;silent</i>, it makes curl show an error message if it fails. </p>
<p> This option is global and does not need to be specified for each use of <i>-:, &#8211;next</i>. </p>
<p> Example: </p>
<pre>
 curl --show-error --silent <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;no-progress-meter</i>.</p>
<dt>-s, &#8211;silent</p>
<dd> Silent or quiet mode. Do not show progress meter or error messages. Makes Curl mute. It will still output the data you ask for, potentially even to the terminal/stdout unless you redirect it. </p>
<p> Use <i>-S, &#8211;show-error</i> in addition to this option to disable progress meter but still show error messages. </p>
<p> Example: </p>
<pre>
 curl -s <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-v, &#8211;verbose</i>, <i>&#8211;stderr</i> and <i>&#8211;no-progress-meter</i>.</p>
<dt>&#8211;socks4 &lt;host[:port]&gt;</p>
<dd> Use the specified SOCKS4 proxy. If the port number is not specified, it is assumed at port 1080. Using this socket type make curl resolve the host name and passing the address on to the proxy. </p>
<p> This option overrides any previous use of <i>-x, &#8211;proxy</i>, as they are mutually exclusive. </p>
<p> This option is superfluous since you can specify a socks4 proxy with <i>-x, &#8211;proxy</i> using a socks4:// protocol prefix. </p>
<p> Since 7.52.0, <i>&#8211;preproxy</i> can be used to specify a SOCKS proxy at the same time <i>-x, &#8211;proxy</i> is used with an HTTP/HTTPS proxy. In such a case curl first connects to the SOCKS proxy and then connects (through SOCKS) to the HTTP or HTTPS proxy. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --socks4 hostname:4096 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;socks4a</i>, <i>&#8211;socks5</i> and <i>&#8211;socks5-hostname</i>.</p>
<dt>&#8211;socks4a &lt;host[:port]&gt;</p>
<dd> Use the specified SOCKS4a proxy. If the port number is not specified, it is assumed at port 1080. This asks the proxy to resolve the host name. </p>
<p> This option overrides any previous use of <i>-x, &#8211;proxy</i>, as they are mutually exclusive. </p>
<p> This option is superfluous since you can specify a socks4a proxy with <i>-x, &#8211;proxy</i> using a socks4a:// protocol prefix. </p>
<p> Since 7.52.0, <i>&#8211;preproxy</i> can be used to specify a SOCKS proxy at the same time <i>-x, &#8211;proxy</i> is used with an HTTP/HTTPS proxy. In such a case curl first connects to the SOCKS proxy and then connects (through SOCKS) to the HTTP or HTTPS proxy. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --socks4a hostname:4096 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;socks4</i>, <i>&#8211;socks5</i> and <i>&#8211;socks5-hostname</i>.</p>
<dt>&#8211;socks5-basic</p>
<dd> Tells curl to use username/password authentication when connecting to a SOCKS5 proxy. The username/password authentication is enabled by default. Use <i>&#8211;socks5-gssapi</i> to force GSS-API authentication to SOCKS5 proxies. </p>
<p> Example: </p>
<pre>
 curl --socks5-basic --socks5 hostname:4096 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;socks5</i>. Added in 7.55.0.</p>
<dt>&#8211;socks5-gssapi-nec</p>
<dd> As part of the GSS-API negotiation a protection mode is negotiated. RFC 1961 says in section 4.3/4.4 it should be protected, but the NEC reference implementation does not. The option <i>&#8211;socks5-gssapi-nec</i> allows the unprotected exchange of the protection mode negotiation. </p>
<p> Example: </p>
<pre>
 curl --socks5-gssapi-nec --socks5 hostname:4096 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;socks5</i>.</p>
<dt>&#8211;socks5-gssapi-service &lt;name&gt;</p>
<dd> The default service name for a socks server is rcmd/server-fqdn. This option allows you to change it. </p>
<p> Examples: <i>&#8211;socks5</i> proxy-name <i>&#8211;socks5-gssapi-service</i> sockd would use sockd/proxy-name <i>&#8211;socks5</i> proxy-name <i>&#8211;socks5-gssapi-service</i> sockd/real-name would use sockd/real-name for cases where the proxy-name does not match the principal name. </p>
<p> Example: </p>
<pre>
 curl --socks5-gssapi-service sockd --socks5 hostname:4096 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;socks5</i>.</p>
<dt>&#8211;socks5-gssapi</p>
<dd> Tells curl to use GSS-API authentication when connecting to a SOCKS5 proxy. The GSS-API authentication is enabled by default (if curl is compiled with GSS-API support). Use <i>&#8211;socks5-basic</i> to force username/password authentication to SOCKS5 proxies. </p>
<p> Example: </p>
<pre>
 curl --socks5-gssapi --socks5 hostname:4096 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;socks5</i>. Added in 7.55.0.</p>
<dt>&#8211;socks5-hostname &lt;host[:port]&gt;</p>
<dd> Use the specified SOCKS5 proxy (and let the proxy resolve the host name). If the port number is not specified, it is assumed at port 1080. </p>
<p> This option overrides any previous use of <i>-x, &#8211;proxy</i>, as they are mutually exclusive. </p>
<p> This option is superfluous since you can specify a socks5 hostname proxy with <i>-x, &#8211;proxy</i> using a socks5h:// protocol prefix. </p>
<p> Since 7.52.0, <i>&#8211;preproxy</i> can be used to specify a SOCKS proxy at the same time <i>-x, &#8211;proxy</i> is used with an HTTP/HTTPS proxy. In such a case curl first connects to the SOCKS proxy and then connects (through SOCKS) to the HTTP or HTTPS proxy. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --socks5-hostname proxy.example:7000 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;socks5</i> and <i>&#8211;socks4a</i>.</p>
<dt>&#8211;socks5 &lt;host[:port]&gt;</p>
<dd> Use the specified SOCKS5 proxy &#8211; but resolve the host name locally. If the port number is not specified, it is assumed at port 1080. </p>
<p> This option overrides any previous use of <i>-x, &#8211;proxy</i>, as they are mutually exclusive. </p>
<p> This option is superfluous since you can specify a socks5 proxy with <i>-x, &#8211;proxy</i> using a socks5:// protocol prefix. </p>
<p> Since 7.52.0, <i>&#8211;preproxy</i> can be used to specify a SOCKS proxy at the same time <i>-x, &#8211;proxy</i> is used with an HTTP/HTTPS proxy. In such a case curl first connects to the SOCKS proxy and then connects (through SOCKS) to the HTTP or HTTPS proxy. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> This option (as well as <i>&#8211;socks4</i>) does not work with IPV6, FTPS or LDAP. </p>
<p> Example: </p>
<pre>
 curl --socks5 proxy.example:7000 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;socks5-hostname</i> and <i>&#8211;socks4a</i>.</p>
<dt>-Y, &#8211;speed-limit &lt;speed&gt;</p>
<dd> If a download is slower than this given speed (in bytes per second) for speed-time seconds it gets aborted. speed-time is set with <i>-y, &#8211;speed-time</i> and is 30 if not set. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --speed-limit 300 --speed-time 10 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-y, &#8211;speed-time</i>, <i>&#8211;limit-rate</i> and <i>-m, &#8211;max-time</i>.</p>
<dt>-y, &#8211;speed-time &lt;seconds&gt;</p>
<dd> If a download is slower than speed-limit bytes per second during a speed-time period, the download gets aborted. If speed-time is used, the default speed-limit will be 1 unless set with <i>-Y, &#8211;speed-limit</i>. </p>
<p> This option controls transfers and thus will not affect slow connects etc. If this is a concern for you, try the <i>&#8211;connect-timeout</i> option. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --speed-limit 300 --speed-time 10 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-Y, &#8211;speed-limit</i> and <i>&#8211;limit-rate</i>.</p>
<dt>&#8211;ssl-allow-beast</p>
<dd> This option tells curl to not work around a security flaw in the SSL3 and TLS1.0 protocols known as BEAST. If this option is not used, the SSL layer may use workarounds known to cause interoperability problems with some older SSL implementations. </p>
<p> <code>WARNING</code>: this option loosens the SSL security, and by using this flag you ask for exactly that. </p>
<p> Example: </p>
<pre>
 curl --ssl-allow-beast <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-ssl-allow-beast</i> and <i>-k, &#8211;insecure</i>.</p>
<dt>&#8211;ssl-auto-client-cert</p>
<dd> Tell libcurl to automatically locate and use a client certificate for authentication, when requested by the server. This option is only supported for Schannel (the native Windows SSL library). Prior to 7.77.0 this was the default behavior in libcurl with Schannel. Since the server can request any certificate that supports client authentication in the OS certificate store it could be a privacy violation and unexpected. </p>
<p> Example: </p>
<pre>
 curl --ssl-auto-client-cert <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;proxy-ssl-auto-client-cert</i>. Added in 7.77.0.</p>
<dt>&#8211;ssl-no-revoke</p>
<dd> (Schannel) This option tells curl to disable certificate revocation checks. WARNING: this option loosens the SSL security, and by using this flag you ask for exactly that. </p>
<p> Example: </p>
<pre>
 curl --ssl-no-revoke <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;crlfile</i>. Added in 7.44.0.</p>
<dt>&#8211;ssl-reqd</p>
<dd> (FTP IMAP POP3 SMTP LDAP) Require SSL/TLS for the connection. Terminates the connection if the server does not support SSL/TLS. </p>
<p> This option is handled in LDAP since version 7.81.0. It is fully supported by the openldap backend and rejected by the generic ldap backend if explicit TLS is required. </p>
<p> This option was formerly known as &#8211;ftp-ssl-reqd. </p>
<p> Example: </p>
<pre>
 curl --ssl-reqd <a href="ftp://example.com">ftp://example.com</a>
</pre>
<p> See also <i>&#8211;ssl</i> and <i>-k, &#8211;insecure</i>.</p>
<dt>&#8211;ssl-revoke-best-effort</p>
<dd> (Schannel) This option tells curl to ignore certificate revocation checks when they failed due to missing/offline distribution points for the revocation check lists. </p>
<p> Example: </p>
<pre>
 curl --ssl-revoke-best-effort <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;crlfile</i> and <i>-k, &#8211;insecure</i>. Added in 7.70.0.</p>
<dt>&#8211;ssl</p>
<dd> (FTP IMAP POP3 SMTP LDAP) Try to use SSL/TLS for the connection. Reverts to a non-secure connection if the server does not support SSL/TLS. See also <i>&#8211;ftp-ssl-control</i> and <i>&#8211;ssl-reqd</i> for different levels of encryption required. </p>
<p> This option is handled in LDAP since version 7.81.0. It is fully supported by the openldap backend and ignored by the generic ldap backend. </p>
<p> Please note that a server may close the connection if the negotiation does not succeed. </p>
<p> This option was formerly known as &#8211;ftp-ssl. That option name can still be used but will be removed in a future version. </p>
<p> Example: </p>
<pre>
 curl --ssl pop3://example.com/
</pre>
<p> See also <i>-k, &#8211;insecure</i> and <i>&#8211;ciphers</i>.</p>
<dt>-2, &#8211;sslv2</p>
<dd> (SSL) This option previously asked curl to use SSLv2, but starting in curl 7.77.0 this instruction is ignored. SSLv2 is widely considered insecure (see RFC 6176). </p>
<p> Example: </p>
<pre>
 curl --sslv2 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;http1.1</i> and <i>&#8211;http2</i>. <i>-2, &#8211;sslv2</i> requires that the underlying libcurl was built to support TLS. This option overrides <i>-3, &#8211;sslv3</i> and <i>-1, &#8211;tlsv1</i> and <i>&#8211;tlsv1.1</i> and <i>&#8211;tlsv1.2</i>.</p>
<dt>-3, &#8211;sslv3</p>
<dd> (SSL) This option previously asked curl to use SSLv3, but starting in curl 7.77.0 this instruction is ignored. SSLv3 is widely considered insecure (see RFC 7568). </p>
<p> Example: </p>
<pre>
 curl --sslv3 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;http1.1</i> and <i>&#8211;http2</i>. <i>-3, &#8211;sslv3</i> requires that the underlying libcurl was built to support TLS. This option overrides <i>-2, &#8211;sslv2</i> and <i>-1, &#8211;tlsv1</i> and <i>&#8211;tlsv1.1</i> and <i>&#8211;tlsv1.2</i>.</p>
<dt>&#8211;stderr &lt;file&gt;</p>
<dd> Redirect all writes to stderr to the specified file instead. If the file name is a plain &#8216;-&#8216;, it is instead written to stdout. </p>
<p> This option is global and does not need to be specified for each use of <i>-:, &#8211;next</i>. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --stderr output.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-v, &#8211;verbose</i> and <i>-s, &#8211;silent</i>.</p>
<dt>&#8211;styled-output</p>
<dd> Enables the automatic use of bold font styles when writing HTTP headers to the terminal. Use &#8211;no-styled-output to switch them off. </p>
<p> This option is global and does not need to be specified for each use of <i>-:, &#8211;next</i>. </p>
<p> Example: </p>
<pre>
 curl --styled-output -I <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-I, &#8211;head</i> and <i>-v, &#8211;verbose</i>. Added in 7.61.0.</p>
<dt>&#8211;suppress-connect-headers</p>
<dd> When <i>-p, &#8211;proxytunnel</i> is used and a CONNECT request is made do not output proxy CONNECT response headers. This option is meant to be used with <i>-D, &#8211;dump-header</i> or <i>-i, &#8211;include</i> which are used to show protocol headers in the output. It has no effect on debug options such as <i>-v, &#8211;verbose</i> or <i>&#8211;trace</i>, or any statistics. </p>
<p> Example: </p>
<pre>
 curl --suppress-connect-headers --include -x proxy <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-D, &#8211;dump-header</i>, <i>-i, &#8211;include</i> and <i>-p, &#8211;proxytunnel</i>. Added in 7.54.0.</p>
<dt>&#8211;tcp-fastopen</p>
<dd> Enable use of TCP Fast Open (RFC7413). </p>
<p> Example: </p>
<pre>
 curl --tcp-fastopen <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;false-start</i>. Added in 7.49.0.</p>
<dt>&#8211;tcp-nodelay</p>
<dd> Turn on the TCP_NODELAY option. See the <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> man page for details about this option. </p>
<p> Since 7.50.2, curl sets this option by default and you need to explicitly switch it off if you do not want it on. </p>
<p> Example: </p>
<pre>
 curl --tcp-nodelay <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-N, &#8211;no-buffer</i>.</p>
<dt>-t, &#8211;telnet-option &lt;opt=val&gt;</p>
<dd> Pass options to the telnet protocol. Supported options are: </p>
<p> TTYPE=&lt;term&gt; Sets the terminal type. </p>
<p> XDISPLOC=&lt;X display&gt; Sets the X display location. </p>
<p> NEW_ENV=&lt;var,val&gt; Sets an environment variable. </p>
<p> Example: </p>
<pre>
 curl -t TTYPE=vt100 <a href="telnet://example.com/">telnet://example.com/</a>
</pre>
<p> See also <i>-K, &#8211;config</i>.</p>
<dt>&#8211;tftp-blksize &lt;value&gt;</p>
<dd> (TFTP) Set TFTP BLKSIZE option (must be &gt;512). This is the block size that curl will try to use when transferring data to or from a TFTP server. By default 512 bytes will be used. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --tftp-blksize 1024 <a href="tftp://example.com/file">tftp://example.com/file</a>
</pre>
<p> See also <i>&#8211;tftp-no-options</i>.</p>
<dt>&#8211;tftp-no-options</p>
<dd> (TFTP) Tells curl not to send TFTP options requests. </p>
<p> This option improves interop with some legacy servers that do not acknowledge or properly implement TFTP options. When this option is used <i>&#8211;tftp-blksize</i> is ignored. </p>
<p> Example: </p>
<pre>
 curl --tftp-no-options <a href="tftp://192.168.0.1/">tftp://192.168.0.1/</a>
</pre>
<p> See also <i>&#8211;tftp-blksize</i>. Added in 7.48.0.</p>
<dt>-z, &#8211;time-cond &lt;time&gt;</p>
<dd> (HTTP FTP) Request a file that has been modified later than the given time and date, or one that has been modified before that time. The &lt;date expression&gt; can be all sorts of date strings or if it does not match any internal ones, it is taken as a filename and tries to get the modification date (mtime) from &lt;file&gt; instead. See the <i><a href="/docs/linux/man/3-curl_getdate/">curl_getdate</a>(3)</i> man pages for date expression details. </p>
<p> Start the date expression with a dash (-) to make it request for a document that is older than the given date/time, default is a document that is newer than the specified date/time. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Examples: </p>
<pre>
 curl -z &quot;Wed 01 Sep 2021 12:18:00&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl -z &quot;-Wed 01 Sep 2021 12:18:00&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl -z file <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;etag-compare</i> and <i>-R, &#8211;remote-time</i>.</p>
<dt>&#8211;tls-max &lt;VERSION&gt;</p>
<dd> (SSL) VERSION defines maximum supported TLS version. The minimum acceptable version is set by tlsv1.0, tlsv1.1, tlsv1.2 or tlsv1.3. </p>
<p> If the connection is done without TLS, this option has no effect. This includes QUIC-using (HTTP/3) transfers. </p>
<dl>
<dt>
<dd>
<dl>
<dt>default</p>
<dd> Use up to recommended TLS version.</p>
<dt>1.0</p>
<dd> Use up to TLSv1.0.</p>
<dt>1.1</p>
<dd> Use up to TLSv1.1.</p>
<dt>1.2</p>
<dd> Use up to TLSv1.2.</p>
<dt>1.3</p>
<dd> Use up to TLSv1.3.</dl>
</dl>
<p> Examples: </p>
<pre>
 curl --tls-max 1.2 <a rel="nofollow" href="https://example.com">https://example.com</a>
 curl --tls-max 1.3 --tlsv1.2 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;tlsv1.0</i>, <i>&#8211;tlsv1.1</i>, <i>&#8211;tlsv1.2</i> and <i>&#8211;tlsv1.3</i>. <i>&#8211;tls-max</i> requires that the underlying libcurl was built to support TLS. Added in 7.54.0.</p>
<dt>&#8211;tls13-ciphers &lt;ciphersuite list&gt;</p>
<dd> (TLS) Specifies which cipher suites to use in the connection if it negotiates TLS 1.3. The list of ciphers suites must specify valid ciphers. Read up on TLS 1.3 cipher suite details on this URL: </p>
<pre>
 <a rel="nofollow" href="https://curl.se/docs/ssl-ciphers.html">https://curl.se/docs/ssl-ciphers.html</a>
</pre>
<p> This option is currently used only when curl is built to use OpenSSL 1.1.1 or later. If you are using a different SSL backend you can try setting TLS 1.3 cipher suites by using the <i>&#8211;ciphers</i> option. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --tls13-ciphers TLS_AES_128_GCM_SHA256 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;ciphers</i> and <i>&#8211;curves</i>. Added in 7.61.0.</p>
<dt>&#8211;tlsauthtype &lt;type&gt;</p>
<dd> Set TLS authentication type. Currently, the only supported option is &quot;SRP&quot;, for TLS-SRP (RFC 5054). If <i>&#8211;tlsuser</i> and <i>&#8211;tlspassword</i> are specified but <i>&#8211;tlsauthtype</i> is not, then this option defaults to &quot;SRP&quot;. This option works only if the underlying libcurl is built with TLS-SRP support, which requires OpenSSL or GnuTLS with TLS-SRP support. </p>
<p> Example: </p>
<pre>
 curl --tlsauthtype SRP <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;tlsuser</i>.</p>
<dt>&#8211;tlspassword &lt;string&gt;</p>
<dd> Set password for use with the TLS authentication method specified with <i>&#8211;tlsauthtype</i>. Requires that <i>&#8211;tlsuser</i> also be set. </p>
<p> This option does not work with TLS 1.3. </p>
<p> Example: </p>
<pre>
 curl --tlspassword pwd --tlsuser user <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;tlsuser</i>.</p>
<dt>&#8211;tlsuser &lt;name&gt;</p>
<dd> Set username for use with the TLS authentication method specified with <i>&#8211;tlsauthtype</i>. Requires that <i>&#8211;tlspassword</i> also is set. </p>
<p> This option does not work with TLS 1.3. </p>
<p> Example: </p>
<pre>
 curl --tlspassword pwd --tlsuser user <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;tlspassword</i>.</p>
<dt>&#8211;tlsv1.0</p>
<dd> (TLS) Forces curl to use TLS version 1.0 or later when connecting to a remote TLS server. </p>
<p> In old versions of curl this option was documented to allow _only_ TLS 1.0. That behavior was inconsistent depending on the TLS library. Use <i>&#8211;tls-max</i> if you want to set a maximum TLS version. </p>
<p> Example: </p>
<pre>
 curl --tlsv1.0 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;tlsv1.3</i>. Added in 7.34.0.</p>
<dt>&#8211;tlsv1.1</p>
<dd> (TLS) Forces curl to use TLS version 1.1 or later when connecting to a remote TLS server. </p>
<p> In old versions of curl this option was documented to allow _only_ TLS 1.1. That behavior was inconsistent depending on the TLS library. Use <i>&#8211;tls-max</i> if you want to set a maximum TLS version. </p>
<p> Example: </p>
<pre>
 curl --tlsv1.1 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;tlsv1.3</i>. Added in 7.34.0.</p>
<dt>&#8211;tlsv1.2</p>
<dd> (TLS) Forces curl to use TLS version 1.2 or later when connecting to a remote TLS server. </p>
<p> In old versions of curl this option was documented to allow _only_ TLS 1.2. That behavior was inconsistent depending on the TLS library. Use <i>&#8211;tls-max</i> if you want to set a maximum TLS version. </p>
<p> Example: </p>
<pre>
 curl --tlsv1.2 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;tlsv1.3</i>. Added in 7.34.0.</p>
<dt>&#8211;tlsv1.3</p>
<dd> (TLS) Forces curl to use TLS version 1.3 or later when connecting to a remote TLS server. </p>
<p> If the connection is done without TLS, this option has no effect. This includes QUIC-using (HTTP/3) transfers. </p>
<p> Note that TLS 1.3 is not supported by all TLS backends. </p>
<p> Example: </p>
<pre>
 curl --tlsv1.3 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;tlsv1.2</i>. Added in 7.52.0.</p>
<dt>-1, &#8211;tlsv1</p>
<dd> (SSL) Tells curl to use at least TLS version 1.x when negotiating with a remote TLS server. That means TLS version 1.0 or higher </p>
<p> Example: </p>
<pre>
 curl --tlsv1 <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;http1.1</i> and <i>&#8211;http2</i>. <i>-1, &#8211;tlsv1</i> requires that the underlying libcurl was built to support TLS. This option overrides <i>&#8211;tlsv1.1</i> and <i>&#8211;tlsv1.2</i> and <i>&#8211;tlsv1.3</i>.</p>
<dt>&#8211;tr-encoding</p>
<dd> (HTTP) Request a compressed Transfer-Encoding response using one of the algorithms curl supports, and uncompress the data while receiving it. </p>
<p> Example: </p>
<pre>
 curl --tr-encoding <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;compressed</i>.</p>
<dt>&#8211;trace-ascii &lt;file&gt;</p>
<dd> Enables a full trace dump of all incoming and outgoing data, including descriptive information, to the given output file. Use &quot;-&quot; as filename to have the output sent to stdout. </p>
<p> This is similar to <i>&#8211;trace</i>, but leaves out the hex part and only shows the ASCII part of the dump. It makes smaller output that might be easier to read for untrained humans. </p>
<p> This option is global and does not need to be specified for each use of <i>-:, &#8211;next</i>. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --trace-ascii log.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-v, &#8211;verbose</i> and <i>&#8211;trace</i>. This option overrides <i>&#8211;trace</i> and <i>-v, &#8211;verbose</i>.</p>
<dt>&#8211;trace-time</p>
<dd> Prepends a time stamp to each trace or verbose line that curl displays. </p>
<p> This option is global and does not need to be specified for each use of <i>-:, &#8211;next</i>. </p>
<p> Example: </p>
<pre>
 curl --trace-time --trace-ascii output <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;trace</i> and <i>-v, &#8211;verbose</i>.</p>
<dt>&#8211;trace &lt;file&gt;</p>
<dd> Enables a full trace dump of all incoming and outgoing data, including descriptive information, to the given output file. Use &quot;-&quot; as filename to have the output sent to stdout. Use &quot;%&quot; as filename to have the output sent to stderr. </p>
<p> This option is global and does not need to be specified for each use of <i>-:, &#8211;next</i>. </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl --trace log.txt <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;trace-ascii</i> and <i>&#8211;trace-time</i>. This option overrides <i>-v, &#8211;verbose</i> and <i>&#8211;trace-ascii</i>.</p>
<dt>&#8211;unix-socket &lt;path&gt;</p>
<dd> (HTTP) Connect through this Unix domain socket, instead of using the network. </p>
<p> Example: </p>
<pre>
 curl --unix-socket socket-path <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>&#8211;abstract-unix-socket</i>. Added in 7.40.0.</p>
<dt>-T, &#8211;upload-file &lt;file&gt;</p>
<dd> This transfers the specified local file to the remote URL. If there is no file part in the specified URL, curl will append the local file name. NOTE that you must use a trailing / on the last directory to really prove to Curl that there is no file name or curl will think that your last directory name is the remote file name to use. That will most likely cause the upload operation to fail. If this is used on an HTTP(S) server, the PUT command will be used. </p>
<p> Use the file name &quot;-&quot; (a single dash) to use stdin instead of a given file. Alternately, the file name &quot;.&quot; (a single period) may be specified instead of &quot;-&quot; to use stdin in non-blocking mode to allow reading server output while stdin is being uploaded. </p>
<p> You can specify one <i>-T, &#8211;upload-file</i> for each URL on the command line. Each <i>-T, &#8211;upload-file</i> + URL pair specifies what to upload and to where. curl also supports &quot;globbing&quot; of the <i>-T, &#8211;upload-file</i> argument, meaning that you can upload multiple files to a single URL by using the same URL globbing style supported in the URL. </p>
<p> When uploading to an SMTP server: the uploaded data is assumed to be RFC 5322 formatted. It has to feature the necessary set of headers and mail body formatted correctly by the user as curl will not transcode nor encode it further in any way. </p>
<p> Examples: </p>
<pre><code>
curl - T file https : // example.com
                      curl -
                      T "img[1-1000].png" ftp : // ftp.example.com/
                                                curl-- upload -
                                                file "{file1,file2}" https: // example.com
</code></pre>
<p> See also <i>-G, &#8211;get</i> and <i>-I, &#8211;head</i>.</p>
<dt>&#8211;url &lt;url&gt;</p>
<dd> Specify a URL to fetch. This option is mostly handy when you want to specify URL(s) in a config file. </p>
<p> If the given URL is missing a scheme name (such as &quot;http://&quot; or &quot;ftp://&quot; etc) then curl will make a guess based on the host. If the outermost sub-domain name matches DICT, FTP, IMAP, LDAP, POP3 or SMTP then that protocol will be used, otherwise HTTP will be used. Since 7.45.0 guessing can be disabled by setting a default protocol, see <i>&#8211;proto-default</i> for details. </p>
<p> This option may be used any number of times. To control where this URL is written, use the <i>-o, &#8211;output</i> or the <i>-O, &#8211;remote-name</i> options. </p>
<p> <code>WARNING</code>: On Windows, particular file:// accesses can be converted to network accesses by the operating system. Beware! </p>
<p> Example: </p>
<pre>
 curl --url <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-:, &#8211;next</i> and <i>-K, &#8211;config</i>.</p>
<dt>-B, &#8211;use-ascii</p>
<dd> (FTP LDAP) Enable ASCII transfer. For FTP, this can also be enforced by using a URL that ends with &quot;;type=A&quot;. This option causes data sent to stdout to be in text mode for win32 systems. </p>
<p> Example: </p>
<pre>
 curl -B <a href="ftp://example.com/README">ftp://example.com/README</a>
</pre>
<p> See also <i>&#8211;crlf</i> and <i>&#8211;data-ascii</i>.</p>
<dt>-A, &#8211;user-agent &lt;name&gt;</p>
<dd> (HTTP) Specify the User-Agent string to send to the HTTP server. To encode blanks in the string, surround the string with single quote marks. This header can also be set with the <i>-H, &#8211;header</i> or the <i>&#8211;proxy-header</i> options. </p>
<p> If you give an empty argument to <i>-A, &#8211;user-agent</i> (&quot;&quot;), it will remove the header completely from the request. If you prefer a blank header, you can set it to a single space (&quot; &quot;). </p>
<p> If this option is used several times, the last one will be used. </p>
<p> Example: </p>
<pre>
 curl -A &quot;Agent 007&quot; <a rel="nofollow" href="https://example.com">https://example.com</a>
</pre>
<p> See also <i>-H, &#8211;header</i> and <i>&#8211;proxy-header</i>.</p>
<dt>-u, &#8211;user &lt;user:password&gt;</p>
<dd> Specify the user name and password to use for server authentication. Overrides <i>-n, &#8211;netrc</i> and <i>&#8211;netrc-optional</i>. </p>
<p> If you simply specify the user name, curl will prompt for a password. </p>
<p> The user name and passwords are split up on the first colon, which makes it impossible to use a colon in the user name with this option. The password can, still. </p>
<p> On systems where it works, curl will hide the given option argument from process listings. This is not enough to protect credentials from possibly getting seen by other users on the same system as they will still be visible for a moment before cleared. Such sensitive data should be retrieved from a file instead or similar and never used in clear text in a command line. </p>
<p> When using Kerberos V5 with a Windows based server you should include the Windows domain name in the user name, in order for the server to successfully obtain a Kerberos Ticket. If you do not, then the initial authentication handshake may fail. </p>
<p> When using NTLM, the user name can be specified simply as the user name, without the domain, if there is a single domain and forest in your setup for example. </p>
<p> To specify the domain name use either Down-Level Logon Name or UPN (User Principal Name) formats. For example, EXAMPLE
