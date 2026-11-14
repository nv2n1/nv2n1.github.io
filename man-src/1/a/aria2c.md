---
title: "aria2c(1)"
name: "aria2c"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aria2c/"
description: "aria2c – The ultra fast download utility"
---

<h2 class="name">NAME</h2>
<p> aria2c &#8211; The ultra fast download utility </p>
<h2>SYNOPSIS</h2>
<p> <code>aria2c</code> [&lt;OPTIONS&gt;] [&lt;URI&gt;|&lt;MAGNET&gt;|&lt;TORRENT_FILE&gt;|&lt;METALINK_FILE&gt;] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> aria2 is a utility for downloading files. The supported protocols are HTTP(S), FTP, SFTP, BitTorrent, and Metalink. aria2 can download a file from multiple sources/protocols and tries to utilize your maximum download bandwidth. It supports downloading a file from HTTP(S)/FTP /SFTP and BitTorrent at the same time, while the data downloaded from HTTP(S)/FTP/SFTP is uploaded to the BitTorrent swarm. Using Metalink chunk checksums, aria2 automatically validates chunks of data while downloading a file.</p>
<h2>OPTIONS</h2>
<p> <code>NOTE:</code> Most FTP related options are applicable to SFTP as well. Some options are not effective against SFTP (e.g., <i>&#8211;ftp-pasv</i>)</p>
<h3>Basic Options</h3>
<dl>
<dt><code>-d, &#8211;dir=&lt;DIR&gt;</code></p>
<dd> The directory to store the downloaded file.</p>
<dt><code>-i, &#8211;input-file=&lt;FILE&gt;</code></p>
<dd> Downloads the URIs listed in <code>FILE</code>. You can specify multiple sources for a single entity by putting multiple URIs on a single line separated by the <code>TAB</code> character. Additionally, options can be specified after each URI line. Option lines must start with one or more white space characters (<code>SPACE</code> or <code>TAB</code>) and must only contain one option per line. Input files can use gzip compression. When <code>FILE</code> is specified as <code>&#8211;</code>, aria2 will read the input from <code>stdin</code>. See the <i>Input File</i> subsection for details. See also the <i>&#8211;deferred-input</i> option. See also the <i>&#8211;save-session</i> option.</p>
<dt><code>-l, &#8211;log=&lt;LOG&gt;</code></p>
<dd> The file name of the log file. If <code>&#8211;</code> is specified, log is written to <code>stdout</code>. If empty string(&quot;&quot;) is specified, or this option is omitted, no log is written to disk at all.</p>
<dt><code>-j, &#8211;max-concurrent-downloads=&lt;N&gt;</code></p>
<dd> Set the maximum number of parallel downloads for every queue item. See also the <i>&#8211;split</i> option. Default: <code>5</code> </p>
<p> <code>NOTE:</code> <i>&#8211;max-concurrent-downloads</i> limits the number of items which are downloaded concurrently. <i>&#8211;split</i> and <i>&#8211;min-split-size</i> affect the number of connections inside each item. Imagine that you have an input file (see <i>&#8211;input-file</i> option) like this: </p>
<pre>
<a rel="nofollow" href="http://example.com/foo">http://example.com/foo</a>
<a rel="nofollow" href="http://example.com/bar">http://example.com/bar</a>
</pre>
<p> Here is 2 download items. aria2 can download these items concurrently if the value more than or equal 2 is given to <i>&#8211;max-concurrent-downloads</i>. In each download item, you can configure the number of connections using <i>&#8211;split</i> and/or <i>&#8211;min-split-size</i>, etc.</p>
<dt><code>-V, &#8211;check-integrity [true|false]</code></p>
<dd> Check file integrity by validating piece hashes or a hash of entire file. This option has effect only in BitTorrent, Metalink downloads with checksums or HTTP(S)/FTP downloads with <i>&#8211;checksum</i> option. If piece hashes are provided, this option can detect damaged portions of a file and re-download them. If a hash of entire file is provided, hash check is only done when file has been already download. This is determined by file length. If hash check fails, file is re-downloaded from scratch. If both piece hashes and a hash of entire file are provided, only piece hashes are used. Default: <code>false</code></p>
<dt><code>-c, &#8211;continue [true|false]</code></p>
<dd> Continue downloading a partially downloaded file. Use this option to resume a download started by a web browser or another program which downloads files sequentially from the beginning. Currently this option is only applicable to HTTP(S)/FTP downloads.</p>
<dt><code>-h, &#8211;help[=&lt;TAG&gt;|&lt;KEYWORD&gt;]</code></p>
<dd> The help messages are classified with tags. A tag starts with <code>#</code>. For example, type <code>&#8211;help=#http</code> to get the usage for the options tagged with <code>#http</code>. If non-tag word is given, print the usage for the options whose name includes that word. Available Values: <code>#basic</code>, <code>#advanced</code>, <code>#http</code>, <code>#https</code>, <code>#ftp</code>, <code>#metalink</code>, <code>#bittorrent</code>, <code>#cookie</code>, <code>#hook</code>, <code>#file</code>, <code>#rpc</code>, <code>#checksum</code>, <code>#experimental</code>, <code>#deprecated</code>, <code>#help</code>, <code>#all</code> Default: <code>#basic</code></dl>
<h3>HTTP/FTP/SFTP Options</h3>
<dl>
<dt><code>&#8211;all-proxy=&lt;PROXY&gt;</code></p>
<dd> Use a proxy server for all protocols. To override a previously defined proxy, use &quot;&quot;. You also can override this setting and specify a proxy server for a particular protocol using <i>&#8211;http-proxy</i>, <i>&#8211;https-proxy</i> and <i>&#8211;ftp-proxy</i> options. This affects all downloads. The format of PROXY is <code>[<a rel="nofollow" href="http://][USER:PASSWORD@]HOST[:PORT]">http://][USER:PASSWORD@]HOST[:PORT]</a></code>. See also <i>ENVIRONMENT</i> section. </p>
<p> <code>NOTE:</code> If user and password are embedded in proxy URI and they are also specified by <i>&#8211;{http,https,ftp,all}-proxy-{user,passwd}</i> options, those specified later override prior options. For example, if you specified <code>http-proxy-user=myname</code>, <code>http-proxy-passwd=mypass</code> in aria2.conf and you specified <code>&#8211;http-proxy=&quot;<a rel="nofollow" href="http://proxy">http://proxy</a>&quot;</code> on the command-line, then you&#8217;d get HTTP proxy <code><a rel="nofollow" href="http://proxy">http://proxy</a></code> with user <code>myname</code> and password <code>mypass</code>. </p>
<p> Another example: if you specified on the command-line <code>&#8211;http-proxy=&quot;<a rel="nofollow" href="http://user:pass@proxy">http://user:pass@proxy</a>&quot; &#8211;http-proxy-user=&quot;myname&quot; &#8211;http-proxy-passwd=&quot;mypass&quot;</code>, then you&#8217;d get HTTP proxy <code><a rel="nofollow" href="http://proxy">http://proxy</a></code> with user <code>myname</code> and password <code>mypass</code>. </p>
<p> One more example: if you specified in command-line <code>&#8211;http-proxy-user=&quot;myname&quot; &#8211;http-proxy-passwd=&quot;mypass&quot; &#8211;http-proxy=&quot;<a rel="nofollow" href="http://user:pass@proxy">http://user:pass@proxy</a>&quot;</code>, then you&#8217;d get HTTP proxy <code><a rel="nofollow" href="http://proxy">http://proxy</a></code> with user <code>user</code> and password <code>pass</code>.</p>
<dt><code>&#8211;all-proxy-passwd=&lt;PASSWD&gt;</code></p>
<dd> Set password for <i>&#8211;all-proxy</i> option.</p>
<dt><code>&#8211;all-proxy-user=&lt;USER&gt;</code></p>
<dd> Set user for <i>&#8211;all-proxy</i> option.</p>
<dt><code>&#8211;checksum=&lt;TYPE&gt;=&lt;DIGEST&gt;</code></p>
<dd> Set checksum. TYPE is hash type. The supported hash type is listed in <code>Hash Algorithms</code> in <code>aria2c -v</code>. DIGEST is hex digest. For example, setting sha-1 digest looks like this: <code>sha-1=0192ba11326fe2298c8cb4de616f4d4140213838</code> This option applies only to HTTP(S)/FTP downloads.</p>
<dt><code>&#8211;connect-timeout=&lt;SEC&gt;</code></p>
<dd> Set the connect timeout in seconds to establish connection to HTTP/FTP/proxy server. After the connection is established, this option makes no effect and <i>&#8211;timeout</i> option is used instead. Default: <code>60</code></p>
<dt><code>&#8211;dry-run [true|false]</code></p>
<dd> If <code>true</code> is given, aria2 just checks whether the remote file is available and doesn&#8217;t download data. This option has effect on HTTP/FTP download. BitTorrent downloads are canceled if <code>true</code> is specified. Default: <code>false</code></p>
<dt><code>&#8211;lowest-speed-limit=&lt;SPEED&gt;</code></p>
<dd> Close connection if download speed is lower than or equal to this value(bytes per sec). <code>0</code> means aria2 does not have a lowest speed limit. You can append <code>K</code> or <code>M</code> (1K = 1024, 1M = 1024K). This option does not affect BitTorrent downloads. Default: <code>0</code></p>
<dt><code>-x, &#8211;max-connection-per-server=&lt;NUM&gt;</code></p>
<dd> The maximum number of connections to one server for each download. Default: <code>1</code></p>
<dt><code>&#8211;max-file-not-found=&lt;NUM&gt;</code></p>
<dd> If aria2 receives &quot;file not found&quot; status from the remote HTTP/FTP servers NUM times without getting a single byte, then force the download to fail. Specify <code>0</code> to disable this option. This options is effective only when using HTTP/FTP servers. The number of retry attempt is counted toward <i>&#8211;max-tries</i>, so it should be configured too. </p>
<p> Default: <code>0</code></p>
<dt><code>-m, &#8211;max-tries=&lt;N&gt;</code></p>
<dd> Set number of tries. <code>0</code> means unlimited. See also <i>&#8211;retry-wait</i>. Default: <code>5</code></p>
<dt><code>-k, &#8211;min-split-size=&lt;SIZE&gt;</code></p>
<dd> aria2 does not split less than 2*SIZE byte range. For example, let&#8217;s consider downloading 20MiB file. If SIZE is 10M, aria2 can split file into 2 range [0-10MiB) and [10MiB-20MiB) and download it using 2 sources(if <i>&#8211;split</i> &gt;= 2, of course). If SIZE is 15M, since 2*15M &gt; 20MiB, aria2 does not split file and download it using 1 source. You can append <code>K</code> or <code>M</code> (1K = 1024, 1M = 1024K). Possible Values: <code>1M</code> &#8211;<code>1024M</code> Default: <code>20M</code></p>
<dt><code>&#8211;netrc-path=&lt;FILE&gt;</code></p>
<dd> Specify the path to the netrc file. Default: <code>$(HOME)/.netrc</code> </p>
<p> <code>NOTE:</code> Permission of the .netrc file must be 600. Otherwise, the file will be ignored.</p>
<dt><code>-n, &#8211;no-netrc [true|false]</code></p>
<dd> Disables netrc support. netrc support is enabled by default. </p>
<p> <code>NOTE:</code> netrc file is only read at the startup if <i>&#8211;no-netrc</i> is <code>false</code>. So if <i>&#8211;no-netrc</i> is <code>true</code> at the startup, no netrc is available throughout the session. You cannot get netrc enabled even if you send <i>&#8211;no-netrc=false</i> using <i>aria2.changeGlobalOption()</i>.</p>
<dt><code>&#8211;no-proxy=&lt;DOMAINS&gt;</code></p>
<dd> Specify a comma separated list of host names, domains and network addresses with or without a subnet mask where no proxy should be used. </p>
<p> <code>NOTE:</code> For network addresses with a subnet mask, both IPv4 and IPv6 addresses work. The current implementation does not resolve the host name in an URI to compare network addresses specified in <i>&#8211;no-proxy</i>. So it is only effective if URI has numeric IP addresses.</p>
<dt><code>-o, &#8211;out=&lt;FILE&gt;</code></p>
<dd> The file name of the downloaded file. It is always relative to the directory given in <i>&#8211;dir</i> option. When the <i>&#8211;force-sequential</i> option is used, this option is ignored. </p>
<p> <code>NOTE:</code> You cannot specify a file name for Metalink or BitTorrent downloads. The file name specified here is only used when the URIs fed to aria2 are given on the command line directly, but not when using <i>&#8211;input-file</i>, <i>&#8211;force-sequential</i> option. </p>
<p> Example: </p>
<pre>
$ aria2c -o myfile.zip &quot;<a rel="nofollow" href="http://mirror1/file.zip">http://mirror1/file.zip</a>&quot; &quot;<a rel="nofollow" href="http://mirror2/file.zip">http://mirror2/file.zip</a>&quot;
</pre>
<dt><code>&#8211;proxy-method=&lt;METHOD&gt;</code></p>
<dd> Set the method to use in proxy request. METHOD is either <code>get</code> or <code>tunnel</code>. HTTPS downloads always use <code>tunnel</code> regardless of this option. Default: <code>get</code></p>
<dt><code>-R, &#8211;remote-time [true|false]</code></p>
<dd> Retrieve timestamp of the remote file from the remote HTTP/FTP server and if it is available, apply it to the local file. Default: <code>false</code></p>
<dt><code>&#8211;reuse-uri [true|false]</code></p>
<dd> Reuse already used URIs if no unused URIs are left. Default: <code>true</code></p>
<dt><code>&#8211;retry-wait=&lt;SEC&gt;</code></p>
<dd> Set the seconds to wait between retries. When <code>SEC &gt; 0</code>, aria2 will retry downloads when the HTTP server returns a 503 response. Default: <code>0</code></p>
<dt><code>&#8211;server-stat-of=&lt;FILE&gt;</code></p>
<dd> Specify the file name to which performance profile of the servers is saved. You can load saved data using <i>&#8211;server-stat-if</i> option. See <i>Server Performance Profile</i> subsection below for file format.</p>
<dt><code>&#8211;server-stat-if=&lt;FILE&gt;</code></p>
<dd> Specify the file name to load performance profile of the servers. The loaded data will be used in some URI selector such as <code>feedback</code>. See also <i>&#8211;uri-selector</i> option. See <i>Server Performance Profile</i> subsection below for file format.</p>
<dt><code>&#8211;server-stat-timeout=&lt;SEC&gt;</code></p>
<dd> Specifies timeout in seconds to invalidate performance profile of the servers since the last contact to them. Default: <code>86400</code> (24hours)</p>
<dt><code>-s, &#8211;split=&lt;N&gt;</code></p>
<dd> Download a file using N connections. If more than N URIs are given, first N URIs are used and remaining URIs are used for backup. If less than N URIs are given, those URIs are used more than once so that N connections total are made simultaneously. The number of connections to the same host is restricted by the <i>&#8211;max-connection-per-server</i> option. See also the <i>&#8211;min-split-size</i> option. Default: <code>5</code> </p>
<p> <code>NOTE:</code> Some Metalinks regulate the number of servers to connect. aria2 strictly respects them. This means that if Metalink defines the <code>maxconnections</code> attribute lower than N, then aria2 uses the value of this lower value instead of N.</p>
<dt><code>&#8211;stream-piece-selector=&lt;SELECTOR&gt;</code></p>
<dd> Specify piece selection algorithm used in HTTP/FTP download. Piece means fixed length segment which is downloaded in parallel in segmented download. If <code>default</code> is given, aria2 selects piece so that it reduces the number of establishing connection. This is reasonable default behavior because establishing connection is an expensive operation. If <code>inorder</code> is given, aria2 selects piece which has minimum index. Index=0 means first of the file. This will be useful to view movie while downloading it. <i>&#8211;enable-http-pipelining</i> option may be useful to reduce re-connection overhead. Please note that aria2 honors <i>&#8211;min-split-size</i> option, so it will be necessary to specify a reasonable value to <i>&#8211;min-split-size</i> option. If <code>random</code> is given, aria2 selects piece randomly. Like <code>inorder</code>, <i>&#8211;min-split-size</i> option is honored. If <code>geom</code> is given, at the beginning aria2 selects piece which has minimum index like <code>inorder</code>, but it exponentially increasingly keeps space from previously selected piece. This will reduce the number of establishing connection and at the same time it will download the beginning part of the file first. This will be useful to view movie while downloading it. Default: <code>default</code></p>
<dt><code>-t, &#8211;timeout=&lt;SEC&gt;</code></p>
<dd> Set timeout in seconds. Default: <code>60</code></p>
<dt><code>&#8211;uri-selector=&lt;SELECTOR&gt;</code></p>
<dd> Specify URI selection algorithm. The possible values are <code>inorder</code>, <code>feedback</code> and <code>adaptive</code>. If <code>inorder</code> is given, URI is tried in the order appeared in the URI list. If <code>feedback</code> is given, aria2 uses download speed observed in the previous downloads and choose fastest server in the URI list. This also effectively skips dead mirrors. The observed download speed is a part of performance profile of servers mentioned in <i>&#8211;server-stat-of</i> and <i>&#8211;server-stat-if</i> options. If <code>adaptive</code> is given, selects one of the best mirrors for the first and reserved connections. For supplementary ones, it returns mirrors which has not been tested yet, and if each of them has already been tested, returns mirrors which has to be tested again. Otherwise, it doesn&#8217;t select anymore mirrors. Like <code>feedback</code>, it uses a performance profile of servers. Default: <code>feedback</code></dl>
<h3>HTTP Specific Options</h3>
<dl>
<dt><code>&#8211;ca-certificate=&lt;FILE&gt;</code></p>
<dd> Use the certificate authorities in FILE to verify the peers. The certificate file must be in PEM format and can contain multiple CA certificates. Use <i>&#8211;check-certificate</i> option to enable verification. </p>
<p> <code>NOTE:</code> If you build with OpenSSL or the recent version of GnuTLS which has <code>gnutls_certificate_set_x509_system_trust()</code> function and the library is properly configured to locate the system-wide CA certificates store, aria2 will automatically load those certificates at the startup. </p>
<p> <code>NOTE:</code> <i>WinTLS</i> and <i>AppleTLS</i> do not support this option. Instead you will have to import the certificate into the OS trust store.</p>
<dt><code>&#8211;certificate=&lt;FILE&gt;</code></p>
<dd> Use the client certificate in FILE. The certificate must be either in PKCS12 (.p12, .pfx) or in PEM format. </p>
<p> PKCS12 files must contain the certificate, a key and optionally a chain of additional certificates. Only PKCS12 files with a blank import password can be opened! </p>
<p> When using PEM, you have to specify the private key via <i>&#8211;private-key</i> as well. </p>
<p> <code>NOTE:</code> <i>WinTLS</i> does not support PEM files at the moment. Users have to use PKCS12 files. </p>
<p> <code>NOTE:</code> <i>AppleTLS</i> users should use the KeyChain Access utility to import the client certificate and get the SHA-1 fingerprint from the Information dialog corresponding to that certificate. To start aria2c use <i>&#8211;certificate=&lt;SHA-1&gt;</i>. Alternatively PKCS12 files are also supported. PEM files, however, are not supported.</p>
<dt><code>&#8211;check-certificate [true|false]</code></p>
<dd> Verify the peer using certificates specified in <i>&#8211;ca-certificate</i> option. Default: <code>true</code></p>
<dt><code>&#8211;http-accept-gzip [true|false]</code></p>
<dd> Send <code>Accept: deflate, gzip</code> request header and inflate response if remote server responds with <code>Content-Encoding: gzip</code> or <code>Content-Encoding: deflate</code>. Default: <code>false</code> </p>
<p> <code>NOTE:</code> Some server responds with <code>Content-Encoding: gzip</code> for files which itself is gzipped file. aria2 inflates them anyway because of the response header.</p>
<dt><code>&#8211;http-auth-challenge [true|false]</code></p>
<dd> Send HTTP authorization header only when it is requested by the server. If <code>false</code> is set, then authorization header is always sent to the server. There is an exception: if user name and password are embedded in URI, authorization header is always sent to the server regardless of this option. Default: <code>false</code></p>
<dt><code>&#8211;http-no-cache [true|false]</code></p>
<dd> Send <code>Cache-Control: no-cache</code> and <code>Pragma: no-cache</code> header to avoid cached content. If <code>false</code> is given, these headers are not sent and you can add Cache-Control header with a directive you like using <i>&#8211;header</i> option. Default: <code>false</code></p>
<dt><code>&#8211;http-user=&lt;USER&gt;</code></p>
<dd> Set HTTP user. This affects all URIs.</p>
<dt><code>&#8211;http-passwd=&lt;PASSWD&gt;</code></p>
<dd> Set HTTP password. This affects all URIs.</p>
<dt><code>&#8211;http-proxy=&lt;PROXY&gt;</code></p>
<dd> Use a proxy server for HTTP. To override a previously defined proxy, use &quot;&quot;. See also the <i>&#8211;all-proxy</i> option. This affects all http downloads. The format of PROXY is <code>[<a rel="nofollow" href="http://][USER:PASSWORD@]HOST[:PORT]">http://][USER:PASSWORD@]HOST[:PORT]</a></code></p>
<dt><code>&#8211;http-proxy-passwd=&lt;PASSWD&gt;</code></p>
<dd> Set password for <i>&#8211;http-proxy</i>.</p>
<dt><code>&#8211;http-proxy-user=&lt;USER&gt;</code></p>
<dd> Set user for <i>&#8211;http-proxy</i>.</p>
<dt><code>&#8211;https-proxy=&lt;PROXY&gt;</code></p>
<dd> Use a proxy server for HTTPS. To override a previously defined proxy, use &quot;&quot;. See also the <i>&#8211;all-proxy</i> option. This affects all https download. The format of PROXY is <code>[<a rel="nofollow" href="http://][USER:PASSWORD@]HOST[:PORT]">http://][USER:PASSWORD@]HOST[:PORT]</a></code></p>
<dt><code>&#8211;https-proxy-passwd=&lt;PASSWD&gt;</code></p>
<dd> Set password for <i>&#8211;https-proxy</i>.</p>
<dt><code>&#8211;https-proxy-user=&lt;USER&gt;</code></p>
<dd> Set user for <i>&#8211;https-proxy</i>.</p>
<dt><code>&#8211;private-key=&lt;FILE&gt;</code></p>
<dd> Use the private key in FILE. The private key must be decrypted and in PEM format. The behavior when encrypted one is given is undefined. See also <i>&#8211;certificate</i> option.</p>
<dt><code>&#8211;referer=&lt;REFERER&gt;</code></p>
<dd> Set an http referrer (Referer). This affects all http/https downloads. If <code>*</code> is given, the download URI is also used as the referrer. This may be useful when used together with the <i>&#8211;parameterized-uri</i> option.</p>
<dt><code>&#8211;enable-http-keep-alive [true|false]</code></p>
<dd> Enable HTTP/1.1 persistent connection. Default: <code>true</code></p>
<dt><code>&#8211;enable-http-pipelining [true|false]</code></p>
<dd> Enable HTTP/1.1 pipelining. Default: <code>false</code> </p>
<p> <code>NOTE:</code> In performance perspective, there is usually no advantage to enable this option.</p>
<dt><code>&#8211;header=&lt;HEADER&gt;</code></p>
<dd> Append HEADER to HTTP request header. You can use this option repeatedly to specify more than one header: </p>
<pre>
$ aria2c --header=&quot;X-A: b78&quot; --header=&quot;X-B: 9J1&quot; &quot;<a rel="nofollow" href="http://host/file">http://host/file</a>&quot;
</pre>
<dt><code>&#8211;load-cookies=&lt;FILE&gt;</code></p>
<dd> Load Cookies from FILE using the Firefox3 format (SQLite3), Chromium/Google Chrome (SQLite3) and the Mozilla/Firefox(1.x/2.x)/Netscape format. </p>
<p> <code>NOTE:</code> If aria2 is built without libsqlite3, then it doesn&#8217;t support Firefox3 and Chromium/Google Chrome cookie format.</p>
<dt><code>&#8211;save-cookies=&lt;FILE&gt;</code></p>
<dd> Save Cookies to FILE in Mozilla/Firefox(1.x/2.x)/ Netscape format. If FILE already exists, it is overwritten. Session Cookies are also saved and their expiry values are treated as 0. Possible Values: <code>/path/to/file</code></p>
<dt><code>&#8211;use-head [true|false]</code></p>
<dd> Use HEAD method for the first request to the HTTP server. Default: <code>false</code></p>
<dt><code>-U, &#8211;user-agent=&lt;USER_AGENT&gt;</code></p>
<dd> Set user agent for HTTP(S) downloads. Default: <code>aria2/$VERSION</code>, $VERSION is replaced by package version.</dl>
<h3>FTP/SFTP Specific Options</h3>
<dl>
<dt><code>&#8211;ftp-user=&lt;USER&gt;</code></p>
<dd> Set FTP user. This affects all URIs. Default: <code>anonymous</code></p>
<dt><code>&#8211;ftp-passwd=&lt;PASSWD&gt;</code></p>
<dd> Set FTP password. This affects all URIs. If user name is embedded but password is missing in URI, aria2 tries to resolve password using .netrc. If password is found in .netrc, then use it as password. If not, use the password specified in this option. Default: <code>ARIA2USER@</code></p>
<dt><code>-p, &#8211;ftp-pasv [true|false]</code></p>
<dd> Use the passive mode in FTP. If <code>false</code> is given, the active mode will be used. Default: <code>true</code> </p>
<p> <code>NOTE:</code> This option is ignored for SFTP transfer.</p>
<dt><code>&#8211;ftp-proxy=&lt;PROXY&gt;</code></p>
<dd> Use a proxy server for FTP. To override a previously defined proxy, use &quot;&quot;. See also the <i>&#8211;all-proxy</i> option. This affects all ftp downloads. The format of PROXY is <code>[<a rel="nofollow" href="http://][USER:PASSWORD@]HOST[:PORT]">http://][USER:PASSWORD@]HOST[:PORT]</a></code></p>
<dt><code>&#8211;ftp-proxy-passwd=&lt;PASSWD&gt;</code></p>
<dd> Set password for <i>&#8211;ftp-proxy</i> option.</p>
<dt><code>&#8211;ftp-proxy-user=&lt;USER&gt;</code></p>
<dd> Set user for <i>&#8211;ftp-proxy</i> option.</p>
<dt><code>&#8211;ftp-type=&lt;TYPE&gt;</code></p>
<dd> Set FTP transfer type. TYPE is either <code>binary</code> or <code>ascii</code>. Default: <code>binary</code> </p>
<p> <code>NOTE:</code> This option is ignored for SFTP transfer.</p>
<dt><code>&#8211;ftp-reuse-connection [true|false]</code></p>
<dd> Reuse connection in FTP. Default: <code>true</code></p>
<dt><code>&#8211;ssh-host-key-md=&lt;TYPE&gt;=&lt;DIGEST&gt;</code></p>
<dd> Set checksum for SSH host public key. TYPE is hash type. The supported hash type is <code>sha-1</code> or <code>md5</code>. DIGEST is hex digest. For example: <code>sha-1=b030503d4de4539dc7885e6f0f5e256704edf4c3</code>. This option can be used to validate server&#8217;s public key when SFTP is used. If this option is not set, which is default, no validation takes place.</dl>
<h3>BitTorrent/Metalink Options</h3>
<dl>
<dt><code>&#8211;select-file=&lt;INDEX&gt;&#8230;</code></p>
<dd> Set file to download by specifying its index. You can find the file index using the <i>&#8211;show-files</i> option. Multiple indexes can be specified by using <code>,</code>, for example: <code>3,6</code>. You can also use <code>&#8211;</code> to specify a range: <code>1-5</code>. <code>,</code> and <code>&#8211;</code> can be used together: <code>1-5,8,9</code>. When used with the -M option, index may vary depending on the query (see <i>&#8211;metalink-*</i> options). </p>
<p> <code>NOTE:</code> In multi file torrent, the adjacent files specified by this option may also be downloaded. This is by design, not a bug. A single piece may include several files or part of files, and aria2 writes the piece to the appropriate files.</p>
<dt><code>-S, &#8211;show-files [true|false]</code></p>
<dd> Print file listing of &quot;.torrent&quot;, &quot;.meta4&quot; and &quot;.metalink&quot; file and exit. In case of &quot;.torrent&quot; file, additional information (infohash, piece length, etc) is also printed.</dl>
<h3>BitTorrent Specific Options</h3>
<dl>
<dt><code>&#8211;bt-detach-seed-only [true|false]</code></p>
<dd> Exclude seed only downloads when counting concurrent active downloads (See <i>-j</i> option). This means that if <code>-j3</code> is given and this option is turned on and 3 downloads are active and one of those enters seed mode, then it is excluded from active download count (thus it becomes 2), and the next download waiting in queue gets started. But be aware that seeding item is still recognized as active download in RPC method. Default: <code>false</code></p>
<dt><code>&#8211;bt-enable-hook-after-hash-check [true|false]</code></p>
<dd> Allow hook command invocation after hash check (see <i>-V</i> option) in BitTorrent download. By default, when hash check succeeds, the command given by <i>&#8211;on-bt-download-complete</i> is executed. To disable this action, give <code>false</code> to this option. Default: <code>true</code></p>
<dt><code>&#8211;bt-enable-lpd [true|false]</code></p>
<dd> Enable Local Peer Discovery. If a private flag is set in a torrent, aria2 doesn&#8217;t use this feature for that download even if <code>true</code> is given. Default: <code>false</code></p>
<dt><code>&#8211;bt-exclude-tracker=&lt;URI&gt;[,&#8230;]</code></p>
<dd> Comma separated list of BitTorrent tracker&#8217;s announce URI to remove. You can use special value <code>*</code> which matches all URIs, thus removes all announce URIs. When specifying <code>*</code> in shell command-line, don&#8217;t forget to escape or quote it. See also <i>&#8211;bt-tracker</i> option.</p>
<dt><code>&#8211;bt-external-ip=&lt;IPADDRESS&gt;</code></p>
<dd> Specify the external IP address to use in BitTorrent download and DHT. It may be sent to BitTorrent tracker. For DHT, this option should be set to report that local node is downloading a particular torrent. This is critical to use DHT in a private network. Although this function is named <code>external</code>, it can accept any kind of IP addresses.</p>
<dt><code>&#8211;bt-force-encryption [true|false]</code></p>
<dd> Requires BitTorrent message payload encryption with arc4. This is a shorthand of <i>&#8211;bt-require-crypto</i> <i>&#8211;bt-min-crypto-level</i>=arc4. This option does not change the option value of those options. If <code>true</code> is given, deny legacy BitTorrent handshake and only use Obfuscation handshake and always encrypt message payload. Default: <code>false</code></p>
<dt><code>&#8211;bt-hash-check-seed [true|false]</code></p>
<dd> If <code>true</code> is given, after hash check using <i>&#8211;check-integrity</i> option and file is complete, continue to seed file. If you want to check file and download it only when it is damaged or incomplete, set this option to <code>false</code>. This option has effect only on BitTorrent download. Default: <code>true</code></p>
<dt><code>&#8211;bt-load-saved-metadata [true|false]</code></p>
<dd> Before getting torrent metadata from DHT when downloading with magnet link, first try to read file saved by <i>&#8211;bt-save-metadata</i> option. If it is successful, then skip downloading metadata from DHT. Default: <code>false</code></p>
<dt><code>&#8211;bt-lpd-interface=&lt;INTERFACE&gt;</code></p>
<dd> Use given interface for Local Peer Discovery. If this option is not specified, the default interface is chosen. You can specify interface name and IP address. Possible Values: interface, IP address</p>
<dt><code>&#8211;bt-max-open-files=&lt;NUM&gt;</code></p>
<dd> Specify maximum number of files to open in multi-file BitTorrent/Metalink download globally. Default: <code>100</code></p>
<dt><code>&#8211;bt-max-peers=&lt;NUM&gt;</code></p>
<dd> Specify the maximum number of peers per torrent. <code>0</code> means unlimited. See also <i>&#8211;bt-request-peer-speed-limit</i> option. Default: <code>55</code></p>
<dt><code>&#8211;bt-metadata-only [true|false]</code></p>
<dd> Download meta data only. The file(s) described in meta data will not be downloaded. This option has effect only when BitTorrent Magnet URI is used. See also <i>&#8211;bt-save-metadata</i> option. Default: <code>false</code></p>
<dt><code>&#8211;bt-min-crypto-level=plain|arc4</code></p>
<dd> Set minimum level of encryption method. If several encryption methods are provided by a peer, aria2 chooses the lowest one which satisfies the given level. Default: <code>plain</code></p>
<dt><code>&#8211;bt-prioritize-piece=head[=&lt;SIZE&gt;],tail[=&lt;SIZE&gt;]</code></p>
<dd> Try to download first and last pieces of each file first. This is useful for previewing files. The argument can contain 2 keywords: <code>head</code> and <code>tail</code>. To include both keywords, they must be separated by comma. These keywords can take one parameter, SIZE. For example, if <code>head=&lt;SIZE&gt;</code> is specified, pieces in the range of first SIZE bytes of each file get higher priority. <code>tail=&lt;SIZE&gt;</code> means the range of last SIZE bytes of each file. SIZE can include <code>K</code> or <code>M</code> (1K = 1024, 1M = 1024K). If SIZE is omitted, SIZE=1M is used.</p>
<dt><code>&#8211;bt-remove-unselected-file [true|false]</code></p>
<dd> Removes the unselected files when download is completed in BitTorrent. To select files, use <i>&#8211;select-file</i> option. If it is not used, all files are assumed to be selected. Please use this option with care because it will actually remove files from your disk. Default: <code>false</code></p>
<dt><code>&#8211;bt-require-crypto [true|false]</code></p>
<dd> If <code>true</code> is given, aria2 doesn&#8217;t accept and establish connection with legacy BitTorrent handshake(\19BitTorrent protocol). Thus aria2 always uses Obfuscation handshake. Default: <code>false</code></p>
<dt><code>&#8211;bt-request-peer-speed-limit=&lt;SPEED&gt;</code></p>
<dd> If the whole download speed of every torrent is lower than SPEED, aria2 temporarily increases the number of peers to try for more download speed. Configuring this option with your preferred download speed can increase your download speed in some cases. You can append <code>K</code> or <code>M</code> (1K = 1024, 1M = 1024K). Default: <code>50K</code></p>
<dt><code>&#8211;bt-save-metadata [true|false]</code></p>
<dd> Save meta data as &quot;.torrent&quot; file. This option has effect only when BitTorrent Magnet URI is used. The file name is hex encoded info hash with suffix &quot;.torrent&quot;. The directory to be saved is the same directory where download file is saved. If the same file already exists, meta data is not saved. See also <i>&#8211;bt-metadata-only</i> option. Default: <code>false</code></p>
<dt><code>&#8211;bt-seed-unverified [true|false]</code></p>
<dd> Seed previously downloaded files without verifying piece hashes. Default: <code>false</code></p>
<dt><code>&#8211;bt-stop-timeout=&lt;SEC&gt;</code></p>
<dd> Stop BitTorrent download if download speed is 0 in consecutive SEC seconds. If <code>0</code> is given, this feature is disabled. Default: <code>0</code></p>
<dt><code>&#8211;bt-tracker=&lt;URI&gt;[,&#8230;]</code></p>
<dd> Comma separated list of additional BitTorrent tracker&#8217;s announce URI. These URIs are not affected by <i>&#8211;bt-exclude-tracker</i> option because they are added after URIs in <i>&#8211;bt-exclude-tracker</i> option are removed.</p>
<dt><code>&#8211;bt-tracker-connect-timeout=&lt;SEC&gt;</code></p>
<dd> Set the connect timeout in seconds to establish connection to tracker. After the connection is established, this option makes no effect and <i>&#8211;bt-tracker-timeout</i> option is used instead. Default: <code>60</code></p>
<dt><code>&#8211;bt-tracker-interval=&lt;SEC&gt;</code></p>
<dd> Set the interval in seconds between tracker requests. This completely overrides interval value and aria2 just uses this value and ignores the min interval and interval value in the response of tracker. If <code>0</code> is set, aria2 determines interval based on the response of tracker and the download progress. Default: <code>0</code></p>
<dt><code>&#8211;bt-tracker-timeout=&lt;SEC&gt;</code></p>
<dd> Set timeout in seconds. Default: <code>60</code></p>
<dt><code>&#8211;dht-entry-point=&lt;HOST&gt;:&lt;PORT&gt;</code></p>
<dd> Set host and port as an entry point to IPv4 DHT network.</p>
<dt><code>&#8211;dht-entry-point6=&lt;HOST&gt;:&lt;PORT&gt;</code></p>
<dd> Set host and port as an entry point to IPv6 DHT network.</p>
<dt><code>&#8211;dht-file-path=&lt;PATH&gt;</code></p>
<dd> Change the IPv4 DHT routing table file to PATH. Default: <code>$HOME/.aria2/dht.dat</code> if present, otherwise <code>$XDG_CACHE_HOME/aria2/dht.dat</code>.</p>
<dt><code>&#8211;dht-file-path6=&lt;PATH&gt;</code></p>
<dd> Change the IPv6 DHT routing table file to PATH. Default: <code>$HOME/.aria2/dht6.dat</code> if present, otherwise <code>$XDG_CACHE_HOME/aria2/dht6.dat</code>.</p>
<dt><code>&#8211;dht-listen-addr6=&lt;ADDR&gt;</code></p>
<dd> Specify address to bind socket for IPv6 DHT. It should be a global unicast IPv6 address of the host.</p>
<dt><code>&#8211;dht-listen-port=&lt;PORT&gt;&#8230;</code></p>
<dd> Set UDP listening port used by DHT(IPv4, IPv6) and UDP tracker. Multiple ports can be specified by using <code>,</code>, for example: <code>6881,6885</code>. You can also use <code>&#8211;</code> to specify a range: <code>6881-6999</code>. <code>,</code> and <code>&#8211;</code> can be used together. Default: <code>6881-6999</code> </p>
<p> <code>NOTE:</code> Make sure that the specified ports are open for incoming UDP traffic.</p>
<dt><code>&#8211;dht-message-timeout=&lt;SEC&gt;</code></p>
<dd> Set timeout in seconds. Default: <code>10</code></p>
<dt><code>&#8211;enable-dht [true|false]</code></p>
<dd> Enable IPv4 DHT functionality. It also enables UDP tracker support. If a private flag is set in a torrent, aria2 doesn&#8217;t use DHT for that download even if <code>true</code> is given. Default: <code>true</code></p>
<dt><code>&#8211;enable-dht6 [true|false]</code></p>
<dd> Enable IPv6 DHT functionality. If a private flag is set in a torrent, aria2 doesn&#8217;t use DHT for that download even if <code>true</code> is given. Use <i>&#8211;dht-listen-port</i> option to specify port number to listen on. See also <i>&#8211;dht-listen-addr6</i> option.</p>
<dt><code>&#8211;enable-peer-exchange [true|false]</code></p>
<dd> Enable Peer Exchange extension. If a private flag is set in a torrent, this feature is disabled for that download even if <code>true</code> is given. Default: <code>true</code></p>
<dt><code>&#8211;follow-torrent=true|false|mem</code></p>
<dd> If <code>true</code> or <code>mem</code> is specified, when a file whose suffix is <code>.torrent</code> or content type is <code>application/x-bittorrent</code> is downloaded, aria2 parses it as a torrent file and downloads files mentioned in it. If <code>mem</code> is specified, a torrent file is not written to the disk, but is just kept in memory. If <code>false</code> is specified, the <code>.torrent</code> file is downloaded to the disk, but is not parsed as a torrent and its contents are not downloaded. Default: <code>true</code></p>
<dt><code>-O, &#8211;index-out=&lt;INDEX&gt;=&lt;PATH&gt;</code></p>
<dd> Set file path for file with index=INDEX. You can find the file index using the <i>&#8211;show-files</i> option. PATH is a relative path to the path specified in <i>&#8211;dir</i> option. You can use this option multiple times. Using this option, you can specify the output file names of BitTorrent downloads.</p>
<dt><code>&#8211;listen-port=&lt;PORT&gt;&#8230;</code></p>
<dd> Set TCP port number for BitTorrent downloads. Multiple ports can be specified by using <code>,</code>, for example: <code>6881,6885</code>. You can also use <code>&#8211;</code> to specify a range: <code>6881-6999</code>. <code>,</code> and <code>&#8211;</code> can be used together: <code>6881-6889,6999</code>. Default: <code>6881-6999</code> </p>
<p> <code>NOTE:</code> Make sure that the specified ports are open for incoming TCP traffic.</p>
<dt><code>&#8211;max-overall-upload-limit=&lt;SPEED&gt;</code></p>
<dd> Set max overall upload speed in bytes/sec. <code>0</code> means unrestricted. You can append <code>K</code> or <code>M</code> (1K = 1024, 1M = 1024K). To limit the upload speed per torrent, use <i>&#8211;max-upload-limit</i> option. Default: <code>0</code></p>
<dt><code>-u, &#8211;max-upload-limit=&lt;SPEED&gt;</code></p>
<dd> Set max upload speed per each torrent in bytes/sec. <code>0</code> means unrestricted. You can append <code>K</code> or <code>M</code> (1K = 1024, 1M = 1024K). To limit the overall upload speed, use <i>&#8211;max-overall-upload-limit</i> option. Default: <code>0</code></p>
<dt><code>&#8211;peer-id-prefix=&lt;PEER_ID_PREFIX&gt;</code></p>
<dd> Specify the prefix of peer ID. The peer ID in BitTorrent is 20 byte length. If more than 20 bytes are specified, only first 20 bytes are used. If less than 20 bytes are specified, random byte data are added to make its length 20 bytes. </p>
<p> Default: <code>A2-$MAJOR-$MINOR-$PATCH-</code>, $MAJOR, $MINOR and $PATCH are replaced by major, minor and patch version number respectively. For instance, aria2 version 1.18.8 has prefix ID <code>A2-1-18-8-</code>.</p>
<dt><code>&#8211;peer-agent=&lt;PEER_AGENT&gt;</code></p>
<dd> Specify the string used during the bitorrent extended handshake for the peer&#8217;s client version. </p>
<p> Default: <code>aria2/$MAJOR.$MINOR.$PATCH</code>, $MAJOR, $MINOR and $PATCH are replaced by major, minor and patch version number respectively. For instance, aria2 version 1.18.8 has peer agent <code>aria2/1.18.8</code>.</p>
<dt><code>&#8211;seed-ratio=&lt;RATIO&gt;</code></p>
<dd> Specify share ratio. Seed completed torrents until share ratio reaches RATIO. You are strongly encouraged to specify equals or more than <code>1.0</code> here. Specify <code>0.0</code> if you intend to do seeding regardless of share ratio. If <i>&#8211;seed-time</i> option is specified along with this option, seeding ends when at least one of the conditions is satisfied. Default: <code>1.0</code></p>
<dt><code>&#8211;seed-time=&lt;MINUTES&gt;</code></p>
<dd> Specify seeding time in (fractional) minutes. Also see the <i>&#8211;seed-ratio</i> option. </p>
<p> <code>NOTE:</code> Specifying <i>&#8211;seed-time=0</i> disables seeding after download completed.</p>
<dt><code>-T, &#8211;torrent-file=&lt;TORRENT_FILE&gt;</code></p>
<dd> The path to the &quot;.torrent&quot; file. You are not required to use this option because you can specify &quot;.torrent&quot; files without <i>&#8211;torrent-file</i>.</dl>
<h3>Metalink Specific Options</h3>
<dl>
<dt><code>&#8211;follow-metalink=true|false|mem</code></p>
<dd> If <code>true</code> or <code>mem</code> is specified, when a file whose suffix is <code>.meta4</code> or <code>.metalink</code> or content type of <code>application/metalink4+xml</code> or <code>application/metalink+xml</code> is downloaded, aria2 parses it as a metalink file and downloads files mentioned in it. If <code>mem</code> is specified, a metalink file is not written to the disk, but is just kept in memory. If <code>false</code> is specified, the <code>.metalink</code> file is downloaded to the disk, but is not parsed as a metalink file and its contents are not downloaded. Default: <code>true</code></p>
<dt><code>&#8211;metalink-base-uri=&lt;URI&gt;</code></p>
<dd> Specify base URI to resolve relative URI in metalink:url and metalink:metaurl element in a metalink file stored in local disk. If URI points to a directory, URI must end with <code>/</code>.</p>
<dt><code>-M, &#8211;metalink-file=&lt;METALINK_FILE&gt;</code></p>
<dd> The file path to &quot;.meta4&quot; and &quot;.metalink&quot; file. Reads input from <code>stdin</code> when <code>&#8211;</code> is specified. You are not required to use this option because you can specify &quot;.metalink&quot; files without <i>&#8211;metalink-file</i>.</p>
<dt><code>&#8211;metalink-language=&lt;LANGUAGE&gt;</code></p>
<dd> The language of the file to download.</p>
<dt><code>&#8211;metalink-location=&lt;LOCATION&gt;[,&#8230;]</code></p>
<dd> The location of the preferred server. A comma-delimited list of locations is acceptable, for example, <code>jp,us</code>.</p>
<dt><code>&#8211;metalink-os=&lt;OS&gt;</code></p>
<dd> The operating system of the file to download.</p>
<dt><code>&#8211;metalink-version=&lt;VERSION&gt;</code></p>
<dd> The version of the file to download.</p>
<dt><code>&#8211;metalink-preferred-protocol=&lt;PROTO&gt;</code></p>
<dd> Specify preferred protocol. The possible values are <code>http</code>, <code>https</code>, <code>ftp</code> and <code>none</code>. Specify <code>none</code> to disable this feature. Default: <code>none</code></p>
<dt><code>&#8211;metalink-enable-unique-protocol [true|false]</code></p>
<dd> If <code>true</code> is given and several protocols are available for a mirror in a metalink file, aria2 uses one of them. Use <i>&#8211;metalink-preferred-protocol</i> option to specify the preference of protocol. Default: <code>true</code></dl>
<h3>RPC Options</h3>
<dl>
<dt><code>&#8211;enable-rpc [true|false]</code></p>
<dd> Enable JSON-RPC/XML-RPC server. It is strongly recommended to set secret authorization token using <i>&#8211;rpc-secret</i> option. See also <i>&#8211;rpc-listen-port</i> option. Default: <code>false</code></p>
<dt><code>&#8211;pause [true|false]</code></p>
<dd> Pause download after added. This option is effective only when <i>&#8211;enable-rpc=true</i> is given. Default: <code>false</code></p>
<dt><code>&#8211;pause-metadata [true|false]</code></p>
<dd> Pause downloads created as a result of metadata download. There are 3 types of metadata downloads in aria2: (1) downloading .torrent file. (2) downloading torrent metadata using magnet link. (3) downloading metalink file. These metadata downloads will generate downloads using their metadata. This option pauses these subsequent downloads. This option is effective only when <i>&#8211;enable-rpc=true</i> is given. Default: <code>false</code></p>
<dt><code>&#8211;rpc-allow-origin-all [true|false]</code></p>
<dd> Add Access-Control-Allow-Origin header field with value <code>*</code> to the RPC response. Default: <code>false</code></p>
<dt><code>&#8211;rpc-certificate=&lt;FILE&gt;</code></p>
<dd> Use the certificate in FILE for RPC server. The certificate must be either in PKCS12 (.p12, .pfx) or in PEM format. </p>
<p> PKCS12 files must contain the certificate, a key and optionally a chain of additional certificates. Only PKCS12 files with a blank import password can be opened! </p>
<p> When using PEM, you have to specify the private key via <i>&#8211;rpc-private-key</i> as well. Use <i>&#8211;rpc-secure</i> option to enable encryption. </p>
<p> <code>NOTE:</code> <i>WinTLS</i> does not support PEM files at the moment. Users have to use PKCS12 files. </p>
<p> <code>NOTE:</code> <i>AppleTLS</i> users should use the KeyChain Access utility to first generate a self-signed SSL-Server certificate, e.g. using the wizard, and get the SHA-1 fingerprint from the Information dialog corresponding to that new certificate. To start aria2c with <i>&#8211;rpc-secure</i> use <i>&#8211;rpc-certificate=&lt;SHA-1&gt;</i>. Alternatively PKCS12 files are also supported. PEM files, however, are not supported.</p>
<dt><code>&#8211;rpc-listen-all [true|false]</code></p>
<dd> Listen incoming JSON-RPC/XML-RPC requests on all network interfaces. If false is given, listen only on local loopback interface. Default: <code>false</code></p>
<dt><code>&#8211;rpc-listen-port=&lt;PORT&gt;</code></p>
<dd> Specify a port number for JSON-RPC/XML-RPC server to listen to. Possible Values: <code>1024</code> &#8211;<code>65535</code> Default: <code>6800</code></p>
<dt><code>&#8211;rpc-max-request-size=&lt;SIZE&gt;</code></p>
<dd> Set max size of JSON-RPC/XML-RPC request. If aria2 detects the request is more than SIZE bytes, it drops connection. Default: <code>2M</code></p>
<dt><code>&#8211;rpc-passwd=&lt;PASSWD&gt;</code></p>
<dd> Set JSON-RPC/XML-RPC password. </p>
<p> <code>WARNING:</code> <i>&#8211;rpc-passwd</i> option will be deprecated in the future release. Migrate to <i>&#8211;rpc-secret</i> option as soon as possible.</p>
<dt><code>&#8211;rpc-private-key=&lt;FILE&gt;</code></p>
<dd> Use the private key in FILE for RPC server. The private key must be decrypted and in PEM format. Use <i>&#8211;rpc-secure</i> option to enable encryption. See also <i>&#8211;rpc-certificate</i> option.</p>
<dt><code>&#8211;rpc-save-upload-metadata [true|false]</code></p>
<dd> Save the uploaded torrent or metalink meta data in the directory specified by <i>&#8211;dir</i> option. The file name consists of SHA-1 hash hex string of meta data plus extension. For torrent, the extension is &#8216;.torrent&#8217;. For metalink, it is &#8216;.meta4&#8217;. If false is given to this option, the downloads added by <i>aria2.addTorrent()</i> or <i>aria2.addMetalink()</i> will not be saved by <i>&#8211;save-session</i> option. Default: <code>true</code></p>
<dt><code>&#8211;rpc-secret=&lt;TOKEN&gt;</code></p>
<dd> Set RPC secret authorization token. Read <i>RPC authorization secret token</i> to know how this option value is used.</p>
<dt><code>&#8211;rpc-secure [true|false]</code></p>
<dd> RPC transport will be encrypted by SSL/TLS. The RPC clients must use https scheme to access the server. For WebSocket client, use wss scheme. Use <i>&#8211;rpc-certificate</i> and <i>&#8211;rpc-private-key</i> options to specify the server certificate and private key.</p>
<dt><code>&#8211;rpc-user=&lt;USER&gt;</code></p>
<dd> Set JSON-RPC/XML-RPC user. </p>
<p> <code>WARNING:</code> <i>&#8211;rpc-user</i> option will be deprecated in the future release. Migrate to <i>&#8211;rpc-secret</i> option as soon as possible.</dl>
<h3>Advanced Options</h3>
<dl>
<dt><code>&#8211;allow-overwrite [true|false]</code></p>
<dd> Restart download from scratch if the corresponding control file doesn&#8217;t exist. See also <i>&#8211;auto-file-renaming</i> option. Default: <code>false</code></p>
<dt><code>&#8211;allow-piece-length-change [true|false]</code></p>
<dd> If false is given, aria2 aborts download when a piece length is different from one in a control file. If true is given, you can proceed but some download progress will be lost. Default: <code>false</code></p>
<dt><code>&#8211;always-resume [true|false]</code></p>
<dd> Always resume download. If <code>true</code> is given, aria2 always tries to resume download and if resume is not possible, aborts download. If <code>false</code> is given, when all given URIs do not support resume or aria2 encounters <code>N</code> URIs which does not support resume (<code>N</code> is the value specified using <i>&#8211;max-resume-failure-tries</i> option), aria2 downloads file from scratch. See <i>&#8211;max-resume-failure-tries</i> option. Default: <code>true</code></p>
<dt><code>&#8211;async-dns [true|false]</code></p>
<dd> Enable asynchronous DNS. Default: <code>true</code></p>
<dt><code>&#8211;async-dns-server=&lt;IPADDRESS&gt;[,&#8230;]</code></p>
<dd> Comma separated list of DNS server address used in asynchronous DNS resolver. Usually asynchronous DNS resolver reads DNS server addresses from <code>/etc/resolv.conf</code>. When this option is used, it uses DNS servers specified in this option instead of ones in <code>/etc/resolv.conf</code>. You can specify both IPv4 and IPv6 address. This option is useful when the system does not have <code>/etc/resolv.conf</code> and user does not have the permission to create it.</p>
<dt><code>&#8211;auto-file-renaming [true|false]</code></p>
<dd> Rename file name if the same file already exists. This option works only in HTTP(S)/FTP download. The new file name has a dot and a number(1..9999) appended after the name, but before the file extension, if any. Default: <code>true</code></p>
<dt><code>&#8211;auto-save-interval=&lt;SEC&gt;</code></p>
<dd> Save a control file(*.aria2) every SEC seconds. If <code>0</code> is given, a control file is not saved during download. aria2 saves a control file when it stops regardless of the value. The possible values are between <code>0</code> to <code>600</code>. Default: <code>60</code></p>
<dt><code>&#8211;conditional-get [true|false]</code></p>
<dd> Download file only when the local file is older than remote file. This function only works with HTTP(S) downloads only. It does not work if file size is specified in Metalink. It also ignores Content-Disposition header. If a control file exists, this option will be ignored. This function uses If-Modified-Since header to get only newer file conditionally. When getting modification time of local file, it uses user supplied file name (see <i>&#8211;out</i> option) or file name part in URI if <i>&#8211;out</i> is not specified. To overwrite existing file, <i>&#8211;allow-overwrite</i> is required. Default: <code>false</code></p>
<dt><code>&#8211;conf-path=&lt;PATH&gt;</code></p>
<dd> Change the configuration file path to PATH. Default: <code>$HOME/.aria2/aria2.conf</code> if present, otherwise <code>$XDG_CONFIG_HOME/aria2/aria2.conf</code>.</p>
<dt><code>&#8211;console-log-level=&lt;LEVEL&gt;</code></p>
<dd> Set log level to output to console. LEVEL is either <code>debug</code>, <code>info</code>, <code>notice</code>, <code>warn</code> or <code>error</code>. Default: <code>notice</code></p>
<dt><code>&#8211;content-disposition-default-utf8 [true|false]</code></p>
<dd> Handle quoted string in Content-Disposition header as UTF-8 instead of ISO-8859-1, for example, the filename parameter, but not the extended version filename*. Default: <code>false</code></p>
<dt><code>-D, &#8211;daemon [true|false]</code></p>
<dd> Run as daemon. The current working directory will be changed to <code>/</code> and standard input, standard output and standard error will be redirected to <code>/dev/null</code>. Default: <code>false</code></p>
<dt><code>&#8211;deferred-input [true|false]</code></p>
<dd> If <code>true</code> is given, aria2 does not read all URIs and options from file specified by <i>&#8211;input-file</i> option at startup, but it reads one by one when it needs later. This may reduce memory usage if input file contains a lot of URIs to download. If <code>false</code> is given, aria2 reads all URIs and options at startup. Default: <code>false</code> </p>
<p> <code>WARNING:</code> <i>&#8211;deferred-input</i> option will be disabled when <i>&#8211;save-session</i> is used together.</p>
<dt><code>&#8211;disable-ipv6 [true|false]</code></p>
<dd> Disable IPv6. This is useful if you have to use broken DNS and want to avoid terribly slow AAAA record lookup. Default: <code>false</code></p>
<dt><code>&#8211;disk-cache=&lt;SIZE&gt;</code></p>
<dd> Enable disk cache. If SIZE is <code>0</code>, the disk cache is disabled. This feature caches the downloaded data in memory, which grows to at most SIZE bytes. The cache storage is created for aria2 instance and shared by all downloads. The one advantage of the disk cache is reduce the disk I/O because the data are written in larger unit and it is reordered by the offset of the file. If hash checking is involved and the data are cached in memory, we don&#8217;t need to read them from the disk. SIZE can include <code>K</code> or <code>M</code> (1K = 1024, 1M = 1024K). Default: <code>16M</code></p>
<dt><code>&#8211;download-result=&lt;OPT&gt;</code></p>
<dd> This option changes the way <code>Download Results</code> is formatted. If OPT is <code>default</code>, print GID, status, average download speed and path/URI. If multiple files are involved, path/URI of first requested file is printed and remaining ones are omitted. If OPT is <code>full</code>, print GID, status, average download speed, percentage of progress and path/URI. The percentage of progress and path/URI are printed for each requested file in each row. If OPT is <code>hide</code>, <code>Download Results</code> is hidden. Default: <code>default</code></p>
<dt><code>&#8211;dscp=&lt;DSCP&gt;</code></p>
<dd> Set DSCP value in outgoing IP packets of BitTorrent traffic for QoS. This parameter sets only DSCP bits in TOS field of IP packets, not the whole field. If you take values from <i>/usr/include/netinet/ip.h</i> divide them by 4 (otherwise values would be incorrect, e.g. your <code>CS1</code> class would turn into <code>CS4</code>). If you take commonly used values from RFC, network vendors&#8217; documentation, Wikipedia or any other source, use them as they are.</p>
<dt><code>&#8211;rlimit-nofile=&lt;NUM&gt;</code></p>
<dd> Set the soft limit of open file descriptors. This open will only have effect when:</p>
<dt>a.</p>
<dd> The system supports it (posix)</p>
<dt>b.</p>
<dd> The limit does not exceed the hard limit.</p>
<dt>c.</p>
<dd> The specified limit is larger than the current soft limit. </p>
<p> This is equivalent to setting nofile via ulimit, except that it will never decrease the limit. </p>
<p> This option is only available on systems supporting the rlimit API.</p>
<dt><code>&#8211;enable-color [true|false]</code></p>
<dd> Enable color output for a terminal. Default: <code>true</code></p>
<dt><code>&#8211;enable-mmap [true|false]</code></p>
<dd> Map files into memory. This option may not work if the file space is not pre-allocated. See <i>&#8211;file-allocation</i>. </p>
<p> Default: <code>false</code></p>
<dt><code>&#8211;event-poll=&lt;POLL&gt;</code></p>
<dd> Specify the method for polling events. The possible values are <code>epoll</code>, <code>kqueue</code>, <code>port</code>, <code>poll</code> and <code>select</code>. For each <code>epoll</code>, <code>kqueue</code>, <code>port</code> and <code>poll</code>, it is available if system supports it. <code>epoll</code> is available on recent Linux. <code>kqueue</code> is available on various *BSD systems including Mac OS X. <code>port</code> is available on Open Solaris. The default value may vary depending on the system you use.</p>
<dt><code>&#8211;file-allocation=&lt;METHOD&gt;</code></p>
<dd> Specify file allocation method. <code>none</code> doesn&#8217;t pre-allocate file space. <code>prealloc</code> pre-allocates file space before download begins. This may take some time depending on the size of the file. If you are using newer file systems such as ext4 (with extents support), btrfs, xfs or NTFS(MinGW build only), <code>falloc</code> is your best choice. It allocates large(few GiB) files almost instantly. Don&#8217;t use <code>falloc</code> with legacy file systems such as ext3 and FAT32 because it takes almost same time as <code>prealloc</code> and it blocks aria2 entirely until allocation finishes. <code>falloc</code> may not be available if your system doesn&#8217;t have <code><a href="/docs/linux/man/3-posix_fallocate/">posix_fallocate</a>(3)</code> function. <code>trunc</code> uses <code><a href="/docs/linux/man/2-ftruncate/">ftruncate</a>(2)</code> system call or platform-specific counterpart to truncate a file to a specified length. </p>
<p> Possible Values: <code>none</code>, <code>prealloc</code>, <code>trunc</code>, <code>falloc</code> Default: <code>prealloc</code> </p>
<p> <code>WARNING:</code> Using <code>trunc</code> seemingly allocates disk space very quickly, but what it actually does is that it sets file length metadata in file system, and does not allocate disk space at all. This means that it does not help avoiding fragmentation. </p>
<p> <code>NOTE:</code> In multi file torrent downloads, the files adjacent forward to the specified files are also allocated if they share the same piece.</p>
<dt><code>&#8211;force-save [true|false]</code></p>
<dd> Save download with <i>&#8211;save-session</i> option even if the download is completed or removed. This option also saves control file in that situations. This may be useful to save BitTorrent seeding which is recognized as completed state. Default: <code>false</code></p>
<dt><code>&#8211;save-not-found [true|false]</code></p>
<dd> Save download with <i>&#8211;save-session</i> option even if the file was not found on the server. This option also saves control file in that situations. Default: <code>true</code></p>
<dt><code>&#8211;gid=&lt;GID&gt;</code></p>
<dd> Set GID manually. aria2 identifies each download by the ID called GID. The GID must be hex string of 16 characters, thus [0-9a-fA-F] are allowed and leading zeros must not be stripped. The GID all 0 is reserved and must not be used. The GID must be unique, otherwise error is reported and the download is not added. This option is useful when restoring the sessions saved using <i>&#8211;save-session</i> option. If this option is not used, new GID is generated by aria2.</p>
<dt><code>&#8211;hash-check-only [true|false]</code></p>
<dd> If <code>true</code> is given, after hash check using <i>&#8211;check-integrity</i> option, abort download whether or not download is complete. Default: <code>false</code></p>
<dt><code>&#8211;human-readable [true|false]</code></p>
<dd> Print sizes and speed in human readable format (e.g., 1.2Ki, 3.4Mi) in the console readout. Default: <code>true</code></p>
<dt><code>&#8211;interface=&lt;INTERFACE&gt;</code></p>
<dd> Bind sockets to given interface. You can specify interface name, IP address and host name. Possible Values: interface, IP address, host name </p>
<p> <code>NOTE:</code> If an interface has multiple addresses, it is highly recommended to specify IP address explicitly. See also <i>&#8211;disable-ipv6</i>. If your system doesn&#8217;t have <code><a href="/docs/linux/man/3-getifaddrs/">getifaddrs</a>(3)</code>, this option doesn&#8217;t accept interface name.</p>
<dt><code>&#8211;keep-unfinished-download-result [true|false]</code></p>
<dd> Keep unfinished download results even if doing so exceeds <i>&#8211;max-download-result</i>. This is useful if all unfinished downloads must be saved in session file (see <i>&#8211;save-session</i> option). Please keep in mind that there is no upper bound to the number of unfinished download result to keep. If that is undesirable, turn this option off. Default: <code>true</code></p>
<dt><code>&#8211;max-download-result=&lt;NUM&gt;</code></p>
<dd> Set maximum number of download result kept in memory. The download results are completed/error/removed downloads. The download results are stored in FIFO queue and it can store at most NUM download results. When queue is full and new download result is created, oldest download result is removed from the front of the queue and new one is pushed to the back. Setting big number in this option may result high memory consumption after thousands of downloads. Specifying 0 means no download result is kept. Note that unfinished downloads are kept in memory regardless of this option value. See <i>&#8211;keep-unfinished-download-result</i> option. Default: <code>1000</code></p>
<dt><code>&#8211;max-mmap-limit=&lt;SIZE&gt;</code></p>
<dd> Set the maximum file size to enable mmap (see <i>&#8211;enable-mmap</i> option). The file size is determined by the sum of all files contained in one download. For example, if a download contains 5 files, then file size is the total size of those files. If file size is strictly greater than the size specified in this option, mmap will be disabled. Default: <code>9223372036854775807</code></p>
<dt><code>&#8211;max-resume-failure-tries=&lt;N&gt;</code></p>
<dd> When used with <i>&#8211;always-resume=false,</i> aria2 downloads file from scratch when aria2 detects N number of URIs that does not support resume. If N is <code>0</code>, aria2 downloads file from scratch when all given URIs do not support resume. See <i>&#8211;always-resume</i> option. Default: <code>0</code></p>
<dt><code>&#8211;min-tls-version=&lt;VERSION&gt;</code></p>
<dd> Specify minimum SSL/TLS version to enable. Possible Values: <code>TLSv1.1</code>, <code>TLSv1.2</code>, <code>TLSv1.3</code> Default: <code>TLSv1.2</code></p>
<dt><code>&#8211;multiple-interface=&lt;INTERFACES&gt;</code></p>
<dd> Comma separated list of interfaces to bind sockets to. Requests will be splited among the interfaces to achieve link aggregation. You can specify interface name, IP address and hostname. If <i>&#8211;interface</i> is used, this option will be ignored. Possible Values: interface, IP address, hostname</p>
<dt><code>&#8211;log-level=&lt;LEVEL&gt;</code></p>
<dd> Set log level to output. LEVEL is either <code>debug</code>, <code>info</code>, <code>notice</code>, <code>warn</code> or <code>error</code>. Default: <code>debug</code></p>
<dt><code>&#8211;on-bt-download-complete=&lt;COMMAND&gt;</code></p>
<dd> For BitTorrent, a command specified in <i>&#8211;on-download-complete</i> is called after download completed and seeding is over. On the other hand, this option set the command to be executed after download completed but before seeding. See <i>Event Hook</i> for more details about COMMAND. Possible Values: <code>/path/to/command</code></p>
<dt><code>&#8211;on-download-complete=&lt;COMMAND&gt;</code></p>
<dd> Set the command to be executed after download completed. See <i>Event Hook</i> for more details about COMMAND. See also <i>&#8211;on-download-stop</i> option. Possible Values: <code>/path/to/command</code></p>
<dt><code>&#8211;on-download-error=&lt;COMMAND&gt;</code></p>
<dd> Set the command to be executed after download aborted due to error. See <i>Event Hook</i> for more details about COMMAND. See also <i>&#8211;on-download-stop</i> option. Possible Values: <code>/path/to/command</code></p>
<dt><code>&#8211;on-download-pause=&lt;COMMAND&gt;</code></p>
<dd> Set the command to be executed after download was paused. See <i>Event Hook</i> for more details about COMMAND. Possible Values: <code>/path/to/command</code></p>
<dt><code>&#8211;on-download-start=&lt;COMMAND&gt;</code></p>
<dd> Set the command to be executed after download got started. See <i>Event Hook</i> for more details about COMMAND. Possible Values: <code>/path/to/command</code></p>
<dt><code>&#8211;on-download-stop=&lt;COMMAND&gt;</code></p>
<dd> Set the command to be executed after download stopped. You can override the command to be executed for particular download result using <i>&#8211;on-download-complete</i> and <i>&#8211;on-download-error</i>. If they are specified, command specified in this option is not executed. See <i>Event Hook</i> for more details about COMMAND. Possible Values: <code>/path/to/command</code></p>
<dt><code>&#8211;optimize-concurrent-downloads [true|false|&lt;A&gt;:&lt;B&gt;]</code></p>
<dd> Optimizes the number of concurrent downloads according to the bandwidth available. aria2 uses the download speed observed in the previous downloads to adapt the number of downloads launched in parallel according to the rule N = A + B Log10(speed in Mbps). The coefficients A and B can be customized in the option arguments with A and B separated by a colon. The default values (A=5, B=25) lead to using typically 5 parallel downloads on 1Mbps networks and above 50 on 100Mbps networks. The number of parallel downloads remains constrained under the maximum defined by the <i>&#8211;max-concurrent-downloads</i> parameter. Default: <code>false</code></p>
<dt><code>&#8211;piece-length=&lt;LENGTH&gt;</code></p>
<dd> Set a piece length for HTTP/FTP downloads. This is the boundary when aria2 splits a file. All splits occur at multiple of this length. This option will be ignored in BitTorrent downloads. It will be also ignored if Metalink file contains piece hashes. Default: <code>1M</code> </p>
<p> <code>NOTE:</code> The possible use case of <i>&#8211;piece-length</i> option is change the request range in one HTTP pipelined request. To enable HTTP pipelining use <i>&#8211;enable-http-pipelining</i>.</p>
<dt><code>&#8211;show-console-readout [true|false]</code></p>
<dd> Show console readout. Default: <code>true</code></p>
<dt><code>&#8211;stderr [true|false]</code></p>
<dd> Redirect all console output that would be otherwise printed in stdout to stderr. Default: <code>false</code></p>
<dt><code>&#8211;summary-interval=&lt;SEC&gt;</code></p>
<dd> Set interval in seconds to output download progress summary. Setting <code>0</code> suppresses the output. Default: <code>60</code></p>
<dt><code>-Z, &#8211;force-sequential [true|false]</code></p>
<dd> Fetch URIs in the command-line sequentially and download each URI in a separate session, like the usual command-line download utilities. Default: <code>false</code></p>
<dt><code>&#8211;max-overall-download-limit=&lt;SPEED&gt;</code></p>
<dd> Set max overall download speed in bytes/sec. <code>0</code> means unrestricted. You can append <code>K</code> or <code>M</code> (1K = 1024, 1M = 1024K). To limit the download speed per download, use <i>&#8211;max-download-limit</i> option. Default: <code>0</code></p>
<dt><code>&#8211;max-download-limit=&lt;SPEED&gt;</code></p>
<dd> Set max download speed per each download in bytes/sec. <code>0</code> means unrestricted. You can append <code>K</code> or <code>M</code> (1K = 1024, 1M = 1024K). To limit the overall download speed, use <i>&#8211;max-overall-download-limit</i> option. Default: <code>0</code></p>
<dt><code>&#8211;no-conf [true|false]</code></p>
<dd> Disable loading aria2.conf file.</p>
<dt><code>&#8211;no-file-allocation-limit=&lt;SIZE&gt;</code></p>
<dd> No file allocation is made for files whose size is smaller than SIZE. You can append <code>K</code> or <code>M</code> (1K = 1024, 1M = 1024K). Default: <code>5M</code></p>
<dt><code>-P, &#8211;parameterized-uri [true|false]</code></p>
<dd> Enable parameterized URI support. You can specify set of parts: <code><a rel="nofollow" href="http://{sv1,sv2,sv3}/foo.iso">http://{sv1,sv2,sv3}/foo.iso</a></code>. Also you can specify numeric sequences with step counter: <code><a rel="nofollow" href="http://host/image[000-100:2].img">http://host/image[000-100:2].img</a></code>. A step counter can be omitted. If all URIs do not point to the same file, such as the second example above, -Z option is required. Default: <code>false</code></p>
<dt><code>-q, &#8211;quiet [true|false]</code></p>
<dd> Make aria2 quiet (no console output). Default: <code>false</code></p>
<dt><code>&#8211;realtime-chunk-checksum [true|false]</code></p>
<dd> Validate chunk of data by calculating checksum while downloading a file if chunk checksums are provided. Default: <code>true</code></p>
<dt><code>&#8211;remove-control-file [true|false]</code></p>
<dd> Remove control file before download. Using with <i>&#8211;allow-overwrite=true,</i> download always starts from scratch. This will be useful for users behind proxy server which disables resume.</p>
<dt><code>&#8211;save-session=&lt;FILE&gt;</code></p>
<dd> Save error/unfinished downloads to FILE on exit. You can pass this output file to aria2c with <i>&#8211;input-file</i> option on restart. If you like the output to be gzipped append a .gz extension to the file name. Please note that downloads added by <i>aria2.addTorrent()</i> and <i>aria2.addMetalink()</i> RPC method and whose meta data could not be saved as a file are not saved. Downloads removed using <i>aria2.remove()</i> and <i>aria2.forceRemove()</i> will not be saved. GID is also saved with <i>gid</i>, but there are some restrictions, see below. </p>
<p> <code>NOTE:</code> Normally, GID of the download itself is saved. But some downloads use meta data (e.g., BitTorrent and Metalink). In this case, there are some restrictions.</p>
<dt><code>magnet URI, and followed by torrent download</code></p>
<dd> GID of BitTorrent meta data download is saved.</p>
<dt><code>URI to torrent file, and followed by torrent download</code></p>
<dd> GID of torrent file download is saved.</p>
<dt><code>URI to metalink file, and followed by file downloads described in metalink file</code></p>
<dd> GID of metalink file download is saved.</p>
<dt><code>local torrent file</code></p>
<dd> GID of torrent download is saved.</p>
<dt><code>local metalink file</code></p>
<dd> Any meaningful GID is not saved.</p>
<dt><code>&#8211;save-session-interval=&lt;SEC&gt;</code></p>
<dd> Save error/unfinished downloads to a file specified by <i>&#8211;save-session</i> option every SEC seconds. If <code>0</code> is given, file will be saved only when aria2 exits. Default: <code>0</code></p>
<dt><code>&#8211;socket-recv-buffer-size=&lt;SIZE&gt;</code></p>
<dd> Set the maximum socket receive buffer in bytes. Specifying <code>0</code> will disable this option. This value will be set to socket file descriptor using <code>SO_RCVBUF</code> socket option with <code>setsockopt()</code> call. Default: <code>0</code></p>
<dt><code>&#8211;stop=&lt;SEC&gt;</code></p>
<dd> Stop application after SEC seconds has passed. If <code>0</code> is given, this feature is disabled. Default: <code>0</code></p>
<dt><code>&#8211;stop-with-process=&lt;PID&gt;</code></p>
<dd> Stop application when process PID is not running. This is useful if aria2 process is forked from a parent process. The parent process can fork aria2 with its own pid and when parent process exits for some reason, aria2 can detect it and shutdown itself.</p>
<dt><code>&#8211;truncate-console-readout [true|false]</code></p>
<dd> Truncate console readout to fit in a single line. Default: <code>true</code></p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print the version number, copyright and the configuration information and exit.</dl>
<h3>Notes for Options</h3>
<h3>Optional arguments</h3>
<p> The options that have its argument surrounded by square brackets([]) take an optional argument. Usually omitting the argument is evaluated to <code>true</code>. If you use short form of these options(such as <code>-V</code>) and give an argument, then the option name and its argument should be concatenated(e.g. <code>-Vfalse</code>). If any spaces are inserted between the option name and the argument, the argument will be treated as URI and usually this is not what you expect.</p>
<h3>Units (K and M)</h3>
<p> Some options takes <code>K</code> and <code>M</code> to conveniently represent 1024 and 1048576 respectively. aria2 detects these characters in case-insensitive way. In other words, <code>k</code> and <code>m</code> can be used as well as <code>K</code> and <code>M</code> respectively.</p>
<h3>URI, MAGNET, TORRENT_FILE, METALINK_FILE</h3>
<p> You can specify multiple URIs in command-line. Unless you specify <i>&#8211;force-sequential</i> option, all URIs must point to the same file or downloading will fail. </p>
<p> You can specify arbitrary number of BitTorrent Magnet URI. Please note that they are always treated as a separate download. Both hex encoded 40 characters Info Hash and Base32 encoded 32 characters Info Hash are supported. The multiple <code>tr</code> parameters are supported. Because BitTorrent Magnet URI is likely to contain <code>&amp;</code> character, it is highly recommended to always quote URI with single(<code>&#8216;</code>) or double(<code>&quot;</code>) quotation. It is strongly recommended to enable DHT especially when <code>tr</code> parameter is missing. See <i><a rel="nofollow" href="http://www.bittorrent.org/beps/bep_0009.html">http://www.bittorrent.org/beps/bep_0009.html</a></i> for more details about BitTorrent Magnet URI. </p>
<p> You can also specify arbitrary number of torrent files and Metalink documents stored on a local drive. Please note that they are always treated as a separate download. Both Metalink4 and Metalink version 3.0 are supported. </p>
<p> You can specify both torrent file with -T option and URIs. By doing this, you can download a file from both torrent swarm and HTTP(S)/FTP/SFTP server at the same time, while the data from HTTP(S)/FTP/SFTP are uploaded to the torrent swarm. For single file torrents, URI can be a complete URI pointing to the resource or if URI ends with /, name in torrent file in torrent is added. For multi-file torrents, name and path are added to form a URI for each file. </p>
<p> <code>NOTE:</code> Make sure that URI is quoted with single(<code>&#8216;</code>) or double(<code>&quot;</code>) quotation if it contains <code>&amp;</code> or any characters that have special meaning in shell.</p>
<h3>Resuming Download</h3>
<p> Usually, you can resume transfer by just issuing same command (aria2c URI) if the previous transfer is made by aria2. </p>
<p> If the previous transfer is made by a browser or wget like sequential download manager, then use <i>&#8211;continue</i> option to continue the transfer.</p>
<h3>Event Hook</h3>
<p> aria2 provides options to specify arbitrary command after specific event occurred. Currently following options are available: <i>&#8211;on-bt-download-complete</i>, <i>&#8211;on-download-pause</i>, <i>&#8211;on-download-complete</i>. <i>&#8211;on-download-start</i>, <i>&#8211;on-download-error</i>, <i>&#8211;on-download-stop</i>. </p>
<p> aria2 passes 3 arguments to specified command when it is executed. These arguments are: GID, the number of files and file path. For HTTP, FTP, and SFTP downloads, usually the number of files is 1. BitTorrent download can contain multiple files. If number of files is more than one, file path is first one. In other words, this is the value of path key of first struct whose selected key is true in the response of <i>aria2.getFiles()</i> RPC method. If you want to get all file paths, consider to use JSON-RPC/XML-RPC. Please note that file path may change during download in HTTP because of redirection or Content-Disposition header. </p>
<p> Let&#8217;s see an example of how arguments are passed to command: </p>
<pre><code>
$ cat hook.sh
#!/ bin / sh
        echo "Called with [$1] [$2] [$3]" $ aria2c-- on -
    download - complete hook.sh http : // example.org/file.iso
                                       Called with[1][1][/ path / to / file.iso]
</code></pre>
<h2>EXIT STATUS</h2>
<p> Because aria2 can handle multiple downloads at once, it encounters lots of errors in a session. aria2 returns the following exit status based on the last error encountered.</p>
<dl>
<dt><code>0</code></p>
<dd> If all downloads were successful.</p>
<dt><code>1</code></p>
<dd> If an unknown error occurred.</p>
<dt><code>2</code></p>
<dd> If time out occurred.</p>
<dt><code>3</code></p>
<dd> If a resource was not found.</p>
<dt><code>4</code></p>
<dd> If aria2 saw the specified number of &quot;resource not found&quot; error. See <i>&#8211;max-file-not-found</i> option.</p>
<dt><code>5</code></p>
<dd> If a download aborted because download speed was too slow. See <i>&#8211;lowest-speed-limit</i> option.</p>
<dt><code>6</code></p>
<dd> If network problem occurred.</p>
<dt><code>7</code></p>
<dd> If there were unfinished downloads. This error is only reported if all finished downloads were successful and there were unfinished downloads in a queue when aria2 exited by pressing <code>Ctrl-C</code> by an user or sending TERM or INT signal.</p>
<dt><code>8</code></p>
<dd> If remote server did not support resume when resume was required to complete download.</p>
<dt><code>9</code></p>
<dd> If there was not enough disk space available.</p>
<dt><code>10</code></p>
<dd> If piece length was different from one in .aria2 control file. See <i>&#8211;allow-piece-length-change</i> option.</p>
<dt><code>11</code></p>
<dd> If aria2 was downloading same file at that moment.</p>
<dt><code>12</code></p>
<dd> If aria2 was downloading same info hash torrent at that moment.</p>
<dt><code>13</code></p>
<dd> If file already existed. See <i>&#8211;allow-overwrite</i> option.</p>
<dt><code>14</code></p>
<dd> If renaming file failed. See <i>&#8211;auto-file-renaming</i> option.</p>
<dt><code>15</code></p>
<dd> If aria2 could not open existing file.</p>
<dt><code>16</code></p>
<dd> If aria2 could not create new file or truncate existing file.</p>
<dt><code>17</code></p>
<dd> If file I/O error occurred.</p>
<dt><code>18</code></p>
<dd> If aria2 could not create directory.</p>
<dt><code>19</code></p>
<dd> If name resolution failed.</p>
<dt><code>20</code></p>
<dd> If aria2 could not parse Metalink document.</p>
<dt><code>21</code></p>
<dd> If FTP command failed.</p>
<dt><code>22</code></p>
<dd> If HTTP response header was bad or unexpected.</p>
<dt><code>23</code></p>
<dd> If too many redirects occurred.</p>
<dt><code>24</code></p>
<dd> If HTTP authorization failed.</p>
<dt><code>25</code></p>
<dd> If aria2 could not parse bencoded file (usually &quot;.torrent&quot; file).</p>
<dt><code>26</code></p>
<dd> If &quot;.torrent&quot; file was corrupted or missing information that aria2 needed.</p>
<dt><code>27</code></p>
<dd> If Magnet URI was bad.</p>
<dt><code>28</code></p>
<dd> If bad/unrecognized option was given or unexpected option argument was given.</p>
<dt><code>29</code></p>
<dd> If the remote server was unable to handle the request due to a temporary overloading or maintenance.</p>
<dt><code>30</code></p>
<dd> If aria2 could not parse JSON-RPC request.</p>
<dt><code>31</code></p>
<dd> Reserved. Not used.</p>
<dt><code>32</code></p>
<dd> If checksum validation failed. </p>
<p> <code>NOTE:</code> An error occurred in a finished download will not be reported as exit status.</dl>
<h2>ENVIRONMENT</h2>
<p> aria2 recognizes the following environment variables.</p>
<dl>
<dt><code>http_proxy [<a rel="nofollow" href="http://][USER:PASSWORD@]HOST[:PORT]">http://][USER:PASSWORD@]HOST[:PORT]</a></code></p>
<dd> Specify proxy server for use in HTTP. Overrides http-proxy value in configuration file. The command-line option <i>&#8211;http-proxy</i> overrides this value.</p>
<dt><code>https_proxy [<a rel="nofollow" href="http://][USER:PASSWORD@]HOST[:PORT]">http://][USER:PASSWORD@]HOST[:PORT]</a></code></p>
<dd> Specify proxy server for use in HTTPS. Overrides https-proxy value in configuration file. The command-line option <i>&#8211;https-proxy</i> overrides this value.</p>
<dt><code>ftp_proxy [<a rel="nofollow" href="http://][USER:PASSWORD@]HOST[:PORT]">http://][USER:PASSWORD@]HOST[:PORT]</a></code></p>
<dd> Specify proxy server for use in FTP. Overrides ftp-proxy value in configuration file. The command-line option <i>&#8211;ftp-proxy</i> overrides this value.</p>
<dt><code>all_proxy [<a rel="nofollow" href="http://][USER:PASSWORD@]HOST[:PORT]">http://][USER:PASSWORD@]HOST[:PORT]</a></code></p>
<dd> Specify proxy server for use if no protocol-specific proxy is specified. Overrides all-proxy value in configuration file. The command-line option <i>&#8211;all-proxy</i> overrides this value. </p>
<p> <code>NOTE:</code> Although aria2 accepts <code>ftp://</code> and <code>https://</code> scheme in proxy URI, it simply assumes that <code>http://</code> is specified and does not change its behavior based on the specified scheme.</p>
<dt><code>no_proxy [DOMAIN,&#8230;]</code></p>
<dd> Specify a comma-separated list of host names, domains and network addresses with or without a subnet mask where no proxy should be used. Overrides the <i>no-proxy</i> value in configuration file. The command-line option <i>&#8211;no-proxy</i> overrides this value.</dl>
<h2>FILES</h2>
<h3>aria2.conf</h3>
<p> By default, aria2 checks whether the legacy path <code>$HOME/.aria2/aria2.conf</code> is present, otherwise it parses <code>$XDG_CONFIG_HOME/aria2/aria2.conf</code> as its configuration file. You can specify the path to configuration file using <i>&#8211;conf-path</i> option. If you don&#8217;t want to use the configuration file, use <i>&#8211;no-conf</i> option. </p>
<p> The configuration file is a text file and has 1 option per each line. In each line, you can specify name-value pair in the format: <code>NAME=VALUE</code>, where name is the long command-line option name without <code>&#8212;</code> prefix. You can use same syntax for the command-line option. The lines beginning <code>#</code> are treated as comments: </p>
<pre>
# sample configuration file for aria2c
listen-port=60000
dht-listen-port=60000
seed-ratio=1.0
max-upload-limit=50K
ftp-pasv=true
</pre>
<p> <code>NOTE:</code> The confidential information such as user/password might be included in the configuration file. It is recommended to change file mode bits of the configuration file (e.g., <code>chmod 600 aria2.conf</code>), so that other user cannot see the contents of the file. </p>
<p> The environment variables, such as <code>${HOME}</code>, are expanded by shell. This means that those variables used in configuration file are not expanded. However, it is useful to <code>${HOME}</code> to refer user&#8217;s home directory in configuration file to specify file paths. Therefore, aria2 expands <code>${HOME}</code> found in the following option values to user&#8217;s home directory:</p>
<dl>
<dt>&bull;</p>
<dd> <i>ca-certificate</i></p>
<dt>&bull;</p>
<dd> <i>certificate</i></p>
<dt>&bull;</p>
<dd> <i>dht-file-path</i></p>
<dt>&bull;</p>
<dd> <i>dht-file-path6</i></p>
<dt>&bull;</p>
<dd> <i>dir</i></p>
<dt>&bull;</p>
<dd> <i>input-file</i></p>
<dt>&bull;</p>
<dd> <i>load-cookies</i></p>
<dt>&bull;</p>
<dd> <i>log</i></p>
<dt>&bull;</p>
<dd> <i>metalink-file</i></p>
<dt>&bull;</p>
<dd> <i>netrc-path</i></p>
<dt>&bull;</p>
<dd> <i>on-bt-download-complete</i></p>
<dt>&bull;</p>
<dd> <i>on-download-complete</i></p>
<dt>&bull;</p>
<dd> <i>on-download-error</i></p>
<dt>&bull;</p>
<dd> <i>on-download-start</i></p>
<dt>&bull;</p>
<dd> <i>on-download-stop</i></p>
<dt>&bull;</p>
<dd> <i>on-download-pause</i></p>
<dt>&bull;</p>
<dd> <i>out</i></p>
<dt>&bull;</p>
<dd> <i>private-key</i></p>
<dt>&bull;</p>
<dd> <i>rpc-certificate</i></p>
<dt>&bull;</p>
<dd> <i>rpc-private-key</i></p>
<dt>&bull;</p>
<dd> <i>save-cookies</i></p>
<dt>&bull;</p>
<dd> <i>save-session</i></p>
<dt>&bull;</p>
<dd> <i>server-stat-if</i></p>
<dt>&bull;</p>
<dd> <i>server-stat-of</i></p>
<dt>&bull;</p>
<dd> <i>torrent-file</i> </p>
<p> Note that this expansion occurs even if the above options are used in the command-line. This means that expansion may occur 2 times: first, shell and then aria2c.</dl>
<h3>dht.dat</h3>
<p> Unless the legacy file paths <code>$HOME/.aria2/dht.dat</code> and <code>$HOME/.aria2/dht6.dat</code> are pointing to existing files, the routing table of IPv4 DHT is saved to the path <code>$XDG_CACHE_HOME/aria2/dht.dat</code> and the routing table of IPv6 DHT is saved to the path <code>$XDG_CACHE_HOME/aria2/dht6.dat</code>.</p>
<h3>Netrc</h3>
<p> Netrc support is enabled by default for HTTP(S)/FTP/SFTP. To disable netrc support, specify <i>&#8211;no-netrc</i> option. Your .netrc file should have correct permissions(600). </p>
<p> If machine name starts <code>.</code>, aria2 performs domain-match instead of exact match. This is an extension of aria2. For example of domain match, imagine the following .netrc entry: </p>
<pre>
machine .example.org login myid password mypasswd
</pre>
<p> <code>aria2.example.org</code> domain-matches <code>.example.org</code> and uses <code>myid</code> and <code>mypasswd</code>. </p>
<p> Some domain-match example follow: <code>example.net</code> does not domain-match <code>.example.org</code>. <code>example.org</code> does not domain-match <code>.example.org</code> because of preceding <code>.</code>. If you want to match <code>example.org</code>, specify <code>example.org</code>.</p>
<h3>Control File</h3>
<p> aria2 uses a control file to track the progress of a download. A control file is placed in the same directory as the downloading file and its file name is the file name of downloading file with <code>.aria2</code> appended. For example, if you are downloading file.zip, then the control file should be file.zip.aria2. (There is a exception for this naming convention. If you are downloading a multi torrent, its control file is the &quot;top directory&quot; name of the torrent with <code>.aria2</code> appended. The &quot;top directory&quot; name is a value of &quot;name&quot; key in &quot;info&quot; directory in a torrent file.) </p>
<p> Usually a control file is deleted once download completed. If aria2 decides that download cannot be resumed(for example, when downloading a file from a HTTP server which doesn&#8217;t support resume), a control file is not created. </p>
<p> Normally if you lose a control file, you cannot resume download. But if you have a torrent or metalink with chunk checksums for the file, you can resume the download without a control file by giving -V option to aria2c in command-line.</p>
<h3>Input File</h3>
<p> The input file can contain a list of URIs for aria2 to download. You can specify multiple URIs for a single entity: separate URIs on a single line using the TAB character. </p>
<p> Each line is treated as if it is provided in command-line argument. Therefore they are affected by <i>&#8211;force-sequential</i> and <i>&#8211;parameterized-uri</i> options. </p>
<p> Since URIs in the input file are directly read by aria2, they must not be quoted with single(<code>&#8216;</code>) or double(<code>&quot;</code>) quotation. </p>
<p> Lines starting with <code>#</code> are treated as comments and skipped. </p>
<p> Additionally, the following options can be specified after each line of URIs. These optional lines must start with white space(s).</p>
<dl>
<dt>&bull;</p>
<dd> <i>all-proxy</i></p>
<dt>&bull;</p>
<dd> <i>all-proxy-passwd</i></p>
<dt>&bull;</p>
<dd> <i>all-proxy-user</i></p>
<dt>&bull;</p>
<dd> <i>allow-overwrite</i></p>
<dt>&bull;</p>
<dd> <i>allow-piece-length-change</i></p>
<dt>&bull;</p>
<dd> <i>always-resume</i></p>
<dt>&bull;</p>
<dd> <i>async-dns</i></p>
<dt>&bull;</p>
<dd> <i>auto-file-renaming</i></p>
<dt>&bull;</p>
<dd> <i>bt-enable-hook-after-hash-check</i></p>
<dt>&bull;</p>
<dd> <i>bt-enable-lpd</i></p>
<dt>&bull;</p>
<dd> <i>bt-exclude-tracker</i></p>
<dt>&bull;</p>
<dd> <i>bt-external-ip</i></p>
<dt>&bull;</p>
<dd> <i>bt-force-encryption</i></p>
<dt>&bull;</p>
<dd> <i>bt-hash-check-seed</i></p>
<dt>&bull;</p>
<dd> <i>bt-load-saved-metadata</i></p>
<dt>&bull;</p>
<dd> <i>bt-max-peers</i></p>
<dt>&bull;</p>
<dd> <i>bt-metadata-only</i></p>
<dt>&bull;</p>
<dd> <i>bt-min-crypto-level</i></p>
<dt>&bull;</p>
<dd> <i>bt-prioritize-piece</i></p>
<dt>&bull;</p>
<dd> <i>bt-remove-unselected-file</i></p>
<dt>&bull;</p>
<dd> <i>bt-request-peer-speed-limit</i></p>
<dt>&bull;</p>
<dd> <i>bt-require-crypto</i></p>
<dt>&bull;</p>
<dd> <i>bt-save-metadata</i></p>
<dt>&bull;</p>
<dd> <i>bt-seed-unverified</i></p>
<dt>&bull;</p>
<dd> <i>bt-stop-timeout</i></p>
<dt>&bull;</p>
<dd> <i>bt-tracker</i></p>
<dt>&bull;</p>
<dd> <i>bt-tracker-connect-timeout</i></p>
<dt>&bull;</p>
<dd> <i>bt-tracker-interval</i></p>
<dt>&bull;</p>
<dd> <i>bt-tracker-timeout</i></p>
<dt>&bull;</p>
<dd> <i>check-integrity</i></p>
<dt>&bull;</p>
<dd> <i>checksum</i></p>
<dt>&bull;</p>
<dd> <i>conditional-get</i></p>
<dt>&bull;</p>
<dd> <i>connect-timeout</i></p>
<dt>&bull;</p>
<dd> <i>content-disposition-default-utf8</i></p>
<dt>&bull;</p>
<dd> <i>continue</i></p>
<dt>&bull;</p>
<dd> <i>dir</i></p>
<dt>&bull;</p>
<dd> <i>dry-run</i></p>
<dt>&bull;</p>
<dd> <i>enable-http-keep-alive</i></p>
<dt>&bull;</p>
<dd> <i>enable-http-pipelining</i></p>
<dt>&bull;</p>
<dd> <i>enable-mmap</i></p>
<dt>&bull;</p>
<dd> <i>enable-peer-exchange</i></p>
<dt>&bull;</p>
<dd> <i>file-allocation</i></p>
<dt>&bull;</p>
<dd> <i>follow-metalink</i></p>
<dt>&bull;</p>
<dd> <i>follow-torrent</i></p>
<dt>&bull;</p>
<dd> <i>force-save</i></p>
<dt>&bull;</p>
<dd> <i>ftp-passwd</i></p>
<dt>&bull;</p>
<dd> <i>ftp-pasv</i></p>
<dt>&bull;</p>
<dd> <i>ftp-proxy</i></p>
<dt>&bull;</p>
<dd> <i>ftp-proxy-passwd</i></p>
<dt>&bull;</p>
<dd> <i>ftp-proxy-user</i></p>
<dt>&bull;</p>
<dd> <i>ftp-reuse-connection</i></p>
<dt>&bull;</p>
<dd> <i>ftp-type</i></p>
<dt>&bull;</p>
<dd> <i>ftp-user</i></p>
<dt>&bull;</p>
<dd> <i>gid</i></p>
<dt>&bull;</p>
<dd> <i>hash-check-only</i></p>
<dt>&bull;</p>
<dd> <i>header</i></p>
<dt>&bull;</p>
<dd> <i>http-accept-gzip</i></p>
<dt>&bull;</p>
<dd> <i>http-auth-challenge</i></p>
<dt>&bull;</p>
<dd> <i>http-no-cache</i></p>
<dt>&bull;</p>
<dd> <i>http-passwd</i></p>
<dt>&bull;</p>
<dd> <i>http-proxy</i></p>
<dt>&bull;</p>
<dd> <i>http-proxy-passwd</i></p>
<dt>&bull;</p>
<dd> <i>http-proxy-user</i></p>
<dt>&bull;</p>
<dd> <i>http-user</i></p>
<dt>&bull;</p>
<dd> <i>https-proxy</i></p>
<dt>&bull;</p>
<dd> <i>https-proxy-passwd</i></p>
<dt>&bull;</p>
<dd> <i>https-proxy-user</i></p>
<dt>&bull;</p>
<dd> <i>index-out</i></p>
<dt>&bull;</p>
<dd> <i>lowest-speed-limit</i></p>
<dt>&bull;</p>
<dd> <i>max-connection-per-server</i></p>
<dt>&bull;</p>
<dd> <i>max-download-limit</i></p>
<dt>&bull;</p>
<dd> <i>max-file-not-found</i></p>
<dt>&bull;</p>
<dd> <i>max-mmap-limit</i></p>
<dt>&bull;</p>
<dd> <i>max-resume-failure-tries</i></p>
<dt>&bull;</p>
<dd> <i>max-tries</i></p>
<dt>&bull;</p>
<dd> <i>max-upload-limit</i></p>
<dt>&bull;</p>
<dd> <i>metalink-base-uri</i></p>
<dt>&bull;</p>
<dd> <i>metalink-enable-unique-protocol</i></p>
<dt>&bull;</p>
<dd> <i>metalink-language</i></p>
<dt>&bull;</p>
<dd> <i>metalink-location</i></p>
<dt>&bull;</p>
<dd> <i>metalink-os</i></p>
<dt>&bull;</p>
<dd> <i>metalink-preferred-protocol</i></p>
<dt>&bull;</p>
<dd> <i>metalink-version</i></p>
<dt>&bull;</p>
<dd> <i>min-split-size</i></p>
<dt>&bull;</p>
<dd> <i>no-file-allocation-limit</i></p>
<dt>&bull;</p>
<dd> <i>no-netrc</i></p>
<dt>&bull;</p>
<dd> <i>no-proxy</i></p>
<dt>&bull;</p>
<dd> <i>out</i></p>
<dt>&bull;</p>
<dd> <i>parameterized-uri</i></p>
<dt>&bull;</p>
<dd> <i>pause</i></p>
<dt>&bull;</p>
<dd> <i>pause-metadata</i></p>
<dt>&bull;</p>
<dd> <i>piece-length</i></p>
<dt>&bull;</p>
<dd> <i>proxy-method</i></p>
<dt>&bull;</p>
<dd> <i>realtime-chunk-checksum</i></p>
<dt>&bull;</p>
<dd> <i>referer</i></p>
<dt>&bull;</p>
<dd> <i>remote-time</i></p>
<dt>&bull;</p>
<dd> <i>remove-control-file</i></p>
<dt>&bull;</p>
<dd> <i>retry-wait</i></p>
<dt>&bull;</p>
<dd> <i>reuse-uri</i></p>
<dt>&bull;</p>
<dd> <i>rpc-save-upload-metadata</i></p>
<dt>&bull;</p>
<dd> <i>seed-ratio</i></p>
<dt>&bull;</p>
<dd> <i>seed-time</i></p>
<dt>&bull;</p>
<dd> <i>select-file</i></p>
<dt>&bull;</p>
<dd> <i>split</i></p>
<dt>&bull;</p>
<dd> <i>ssh-host-key-md</i></p>
<dt>&bull;</p>
<dd> <i>stream-piece-selector</i></p>
<dt>&bull;</p>
<dd> <i>timeout</i></p>
<dt>&bull;</p>
<dd> <i>uri-selector</i></p>
<dt>&bull;</p>
<dd> <i>use-head</i></p>
<dt>&bull;</p>
<dd> <i>user-agent</i> </p>
<p> These options have exactly same meaning of the ones in the command-line options, but it just applies to the URIs it belongs to. Please note that for options in input file <code>&#8212;</code> prefix must be stripped. </p>
<p> For example, the content of uri.txt is: </p>
<pre>
<a rel="nofollow" href="http://server/file.iso">http://server/file.iso</a> <a rel="nofollow" href="http://mirror/file.iso">http://mirror/file.iso</a>
  dir=/iso_images
  out=file.img
<a rel="nofollow" href="http://foo/bar">http://foo/bar</a>
</pre>
<p> If aria2 is executed with <code>-i uri.txt -d /tmp</code> options, then <code>file.iso</code> is saved as <code>/iso_images/file.img</code> and it is downloaded from <code><a rel="nofollow" href="http://server/file.iso">http://server/file.iso</a></code> and <code><a rel="nofollow" href="http://mirror/file.iso">http://mirror/file.iso</a></code>. The file <code>bar</code> is downloaded from <code><a rel="nofollow" href="http://foo/bar">http://foo/bar</a></code> and saved as <code>/tmp/bar</code>. </p>
<p> In some cases, <i>out</i> parameter has no effect. See note of <i>&#8211;out</i> option for the restrictions.</dl>
<h3>Server Performance Profile</h3>
<p> This section describes the format of server performance profile. The file is plain text and each line has several <code>NAME=VALUE</code> pair, delimited by comma. Currently following NAMEs are recognized:</p>
<dl>
<dt><code>host</code></p>
<dd> Host name of the server. Required.</p>
<dt><code>protocol</code></p>
<dd> Protocol for this profile, such as ftp, http. Required.</p>
<dt><code>dl_speed</code></p>
<dd> The average download speed observed in the previous download in bytes per sec. Required.</p>
<dt><code>sc_avg_speed</code></p>
<dd> The average download speed observed in the previous download in bytes per sec. This value is only updated if the download is done in single connection environment and only used by AdaptiveURISelector. Optional.</p>
<dt><code>mc_avg_speed</code></p>
<dd> The average download speed observed in the previous download in bytes per sec. This value is only updated if the download is done in multi connection environment and only used by AdaptiveURISelector. Optional.</p>
<dt><code>counter</code></p>
<dd> How many times the server is used. Currently this value is only used by AdaptiveURISelector. Optional.</p>
<dt><code>last_updated</code></p>
<dd> Last contact time in GMT with this server, specified in the seconds since the Epoch(00:00:00 on January 1, 1970, UTC). Required.</p>
<dt><code>status</code></p>
<dd> ERROR is set when server cannot be reached or out-of-service or timeout occurred. Otherwise, OK is set. </p>
<p> Those fields must exist in one line. The order of the fields is not significant. You can put pairs other than the above; they are simply ignored. </p>
<p> An example follows: </p>
<pre>
host=localhost, protocol=http, dl_speed=32000, last_updated=1222491640, status=OK
host=localhost, protocol=ftp, dl_speed=0, last_updated=1222491632, status=ERROR
</pre>
</dl>
<h2>RPC INTERFACE</h2>
<p> aria2 provides JSON-RPC over HTTP and XML-RPC over HTTP interfaces that offer basically the same functionality. aria2 also provides JSON-RPC over WebSocket. JSON-RPC over WebSocket uses the same method signatures and response format as JSON-RPC over HTTP, but additionally provides server-initiated notifications. See <i>JSON-RPC over WebSocket</i> section for more information. </p>
<p> The request path of the JSON-RPC interface (for both over HTTP and over WebSocket) is <code>/jsonrpc</code>. The request path of the XML-RPC interface is <code>/rpc</code>. </p>
<p> The WebSocket URI for JSON-RPC over WebSocket is <code>ws://HOST:PORT/jsonrpc</code>. If you enabled SSL/TLS encryption, use <code><a href="wss://HOST:PORT/jsonrpc">wss://HOST:PORT/jsonrpc</a></code> instead. </p>
<p> The implemented JSON-RPC is based on JSON-RPC 2.0 &lt;<i><a rel="nofollow" href="http://jsonrpc.org/specification">http://jsonrpc.org/specification</a></i>&gt;, and supports HTTP POST and GET (JSONP). The WebSocket transport is an aria2 extension. </p>
<p> The JSON-RPC interface does not support notifications over HTTP, but the RPC server will send notifications over WebSocket. It also does not support floating point numbers. The character encoding must be UTF-8. </p>
<p> When reading the following documentation for JSON-RPC, interpret structs as JSON objects.</p>
<h3>Terminology</h3>
<p> GID The GID (or gid) is a key to manage each download. Each download will be assigned a unique GID. The GID is stored as 64-bit binary value in aria2. For RPC access, it is represented as a hex string of 16 characters (e.g., <code>2089b05ecca3d829</code>). Normally, aria2 generates this GID for each download, but the user can specify GIDs manually using the <i>&#8211;gid</i> option. When querying downloads by GID, you can specify only the prefix of a GID as long as it is unique among others.</p>
<h3>RPC authorization secret token</h3>
<p> As of 1.18.4, in addition to HTTP basic authorization, aria2 provides RPC method-level authorization. In a future release, HTTP basic authorization will be removed and RPC method-level authorization will become mandatory. </p>
<p> To use RPC method-level authorization, the user has to specify an RPC secret authorization token using the <i>&#8211;rpc-secret</i> option. For each RPC method call, the caller has to include the token prefixed with <code>token:</code>. Even when the <i>&#8211;rpc-secret</i> option is not used, if the first parameter in the RPC method is a string and starts with <code>token:</code>, it will removed from the parameter list before the request is being processed. </p>
<p> For example, if the RPC secret authorization token is <code>$$secret$$</code>, calling <i>aria2.addUri</i> RPC method would have to look like this: </p>
<pre>
aria2.addUri(&quot;token:$$secret$$&quot;, [&quot;<a rel="nofollow" href="http://example.org/file">http://example.org/file</a>&quot;])
</pre>
<p> The <i>system.multicall</i> RPC method is treated specially. Since the XML-RPC specification only allows a single array as a parameter for this method, we don&#8217;t specify the token in the call. Instead, each nested method call has to provide the token as the first parameter as described above. </p>
<p> <code>NOTE:</code> The secret token validation in aria2 is designed to take at least a certain amount of time to mitigate brute-force/dictionary attacks against the RPC interface. Therefore it is recommended to prefer Batch or <i>system.multicall</i> requests when appropriate. </p>
<p> <i>system.listMethods</i> and <i>system.listNotifications</i> can be executed without token. Since they just return available methods/notifications, they do not alter anything, they&#8217;re safe without secret token.</p>
<h3>Methods</h3>
<p> All code examples are compatible with the Python 2.7 interpreter. For information on the <i>secret</i> parameter, see <i>RPC authorization secret token</i>.</p>
<dl>
<dt><code>aria2.addUri([secret], uris[, options[, position]])</code></p>
<dd> This method adds a new download. <i>uris</i> is an array of HTTP/FTP/SFTP/BitTorrent URIs (strings) pointing to the same resource. If you mix URIs pointing to different resources, then the download may fail or be corrupted without aria2 complaining. When adding BitTorrent Magnet URIs, <i>uris</i> must have only one element and it should be BitTorrent Magnet URI. <i>options</i> is a struct and its members are pairs of option name and value. See <i>Options</i> below for more details. If <i>position</i> is given, it must be an integer starting from 0. The new download will be inserted at <i>position</i> in the waiting queue. If <i>position</i> is omitted or <i>position</i> is larger than the current size of the queue, the new download is appended to the end of the queue. This method returns the GID of the newly registered download. </p>
<p> <code>JSON-RPC Example</code> </p>
<p> The following example adds <code><a rel="nofollow" href="http://example.org/file">http://example.org/file</a></code>: </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.addUri&#8217;, &#8230; &#8216;params&#8217; : [[&#8216;http://example.org/file&#8217;]]}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; c.read() &#8216;{&#8220;id&#8221;:&#8221;qwer&#8221;,&#8221;jsonrpc&#8221;:&#8221;2.0&#8243;,&#8221;result&#8221;:&#8221;2089b05ecca3d829&#8243;}&#8217;</p>
<p> <code>XML-RPC Example</code> </p>
<p> The following example adds <code><a rel="nofollow" href="http://example.org/file">http://example.org/file</a></code>: </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; s.aria2.addUri(['<a rel="nofollow" href="http://example.org/file'])">http://example.org/file'])</a>
'2089b05ecca3d829'
</pre>
<p> The following example adds a new download with two sources and some options: </p>
<pre>
&gt;&gt;&gt; s.aria2.addUri(['<a rel="nofollow" href="http://example.org/file',">http://example.org/file',</a> '<a rel="nofollow" href="http://mirror/file'],">http://mirror/file'],</a>
                    dict(dir=&quot;/tmp&quot;))
'd2703803b52216d1'
</pre>
<p> The following example adds a download and inserts it to the front of the queue: </p>
<p>&gt;&gt;&gt; s.aria2.addUri([&#8216;http://example.org/file&#8217;], {}, 0) &#8216;ca3d829cee549a4d&#8217;</p>
<dt><code>aria2.addTorrent([secret], torrent[, uris[, options[, position]]])</code></p>
<dd> This method adds a BitTorrent download by uploading a &quot;.torrent&quot; file. If you want to add a BitTorrent Magnet URI, use the <i>aria2.addUri()</i> method instead. <i>torrent</i> must be a base64-encoded string containing the contents of the &quot;.torrent&quot; file. <i>uris</i> is an array of URIs (string). <i>uris</i> is used for Web-seeding. For single file torrents, the URI can be a complete URI pointing to the resource; if URI ends with /, name in torrent file is added. For multi-file torrents, name and path in torrent are added to form a URI for each file. <i>options</i> is a struct and its members are pairs of option name and value. See <i>Options</i> below for more details. If <i>position</i> is given, it must be an integer starting from 0. The new download will be inserted at <i>position</i> in the waiting queue. If <i>position</i> is omitted or <i>position</i> is larger than the current size of the queue, the new download is appended to the end of the queue. This method returns the GID of the newly registered download. If <i>&#8211;rpc-save-upload-metadata</i> is <code>true</code>, the uploaded data is saved as a file named as the hex string of SHA-1 hash of data plus &quot;.torrent&quot; in the directory specified by <i>&#8211;dir</i> option. E.g. a file name might be <code>0a3893293e27ac0490424c06de4d09242215f0a6.torrent</code>. If a file with the same name already exists, it is overwritten! If the file cannot be saved successfully or <i>&#8211;rpc-save-upload-metadata</i> is <code>false</code>, the downloads added by this method are not saved by <i>&#8211;save-session</i>. </p>
<p> The following examples add local file <code>file.torrent</code>. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json, base64 &gt;&gt;&gt; torrent = base64.b64encode(open(&#8216;file.torrent&#8217;).read()) &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;asdf&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.addTorrent&#8217;, &#8216;params&#8217; : [torrent]}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; c.read() &#8216;{&#8220;id&#8221;:&#8221;asdf&#8221;,&#8221;jsonrpc&#8221;:&#8221;2.0&#8243;,&#8221;result&#8221;:&#8221;2089b05ecca3d829&#8243;}&#8217;</p>
<p> <code>XML-RPC Example</code> </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; s.aria2.addTorrent(xmlrpclib.Binary(open('file.torrent', mode='rb').read()))
'2089b05ecca3d829'
</pre>
<dt><code>aria2.addMetalink([secret], metalink[, options[, position]])</code></p>
<dd> This method adds a Metalink download by uploading a &quot;.metalink&quot; file. <i>metalink</i> is a base64-encoded string which contains the contents of the &quot;.metalink&quot; file. <i>options</i> is a struct and its members are pairs of option name and value. See <i>Options</i> below for more details. If <i>position</i> is given, it must be an integer starting from 0. The new download will be inserted at <i>position</i> in the waiting queue. If <i>position</i> is omitted or <i>position</i> is larger than the current size of the queue, the new download is appended to the end of the queue. This method returns an array of GIDs of newly registered downloads. If <i>&#8211;rpc-save-upload-metadata</i> is <code>true</code>, the uploaded data is saved as a file named hex string of SHA-1 hash of data plus &quot;.metalink&quot; in the directory specified by <i>&#8211;dir</i> option. E.g. a file name might be <code>0a3893293e27ac0490424c06de4d09242215f0a6.metalink</code>. If a file with the same name already exists, it is overwritten! If the file cannot be saved successfully or <i>&#8211;rpc-save-upload-metadata</i> is <code>false</code>, the downloads added by this method are not saved by <i>&#8211;save-session</i>. </p>
<p> The following examples add local file file.meta4. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json, base64 &gt;&gt;&gt; metalink = base64.b64encode(open(&#8216;file.meta4&#8217;).read()) &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.addMetalink&#8217;, &#8230; &#8216;params&#8217; : [metalink]}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; c.read() &#8216;{&#8220;id&#8221;:&#8221;qwer&#8221;,&#8221;jsonrpc&#8221;:&#8221;2.0&#8243;,&#8221;result&#8221;:[&#8220;2089b05ecca3d829&#8221;]}&#8217;</p>
<p> <code>XML-RPC Example</code> </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; s.aria2.addMetalink(xmlrpclib.Binary(open('file.meta4', mode='rb').read()))
['2089b05ecca3d829']
</pre>
<dt><code>aria2.remove([secret], gid)</code></p>
<dd> This method removes the download denoted by <i>gid</i> (string). If the specified download is in progress, it is first stopped. The status of the removed download becomes <code>removed</code>. This method returns GID of removed download. </p>
<p> The following examples remove a download with GID#2089b05ecca3d829. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.remove&#8217;, &#8230; &#8216;params&#8217; : [&#8216;2089b05ecca3d829&#8217;]}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; c.read() &#8216;{&#8220;id&#8221;:&#8221;qwer&#8221;,&#8221;jsonrpc&#8221;:&#8221;2.0&#8243;,&#8221;result&#8221;:&#8221;2089b05ecca3d829&#8243;}&#8217;</p>
<p> <code>XML-RPC Example</code> </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; s.aria2.remove('2089b05ecca3d829')
'2089b05ecca3d829'
</pre>
<dt><code>aria2.forceRemove([secret], gid)</code></p>
<dd> This method removes the download denoted by <i>gid</i>. This method behaves just like <i>aria2.remove()</i> except that this method removes the download without performing any actions which take time, such as contacting BitTorrent trackers to unregister the download first.</p>
<dt><code>aria2.pause([secret], gid)</code></p>
<dd> This method pauses the download denoted by <i>gid</i> (string). The status of paused download becomes <code>paused</code>. If the download was active, the download is placed in the front of waiting queue. While the status is <code>paused</code>, the download is not started. To change status to <code>waiting</code>, use the <i>aria2.unpause()</i> method. This method returns GID of paused download.</p>
<dt><code>aria2.pauseAll([secret])</code></p>
<dd> This method is equal to calling <i>aria2.pause()</i> for every active/waiting download. This methods returns <code>OK</code>.</p>
<dt><code>aria2.forcePause([secret], gid)</code></p>
<dd> This method pauses the download denoted by <i>gid</i>. This method behaves just like <i>aria2.pause()</i> except that this method pauses downloads without performing any actions which take time, such as contacting BitTorrent trackers to unregister the download first.</p>
<dt><code>aria2.forcePauseAll([secret])</code></p>
<dd> This method is equal to calling <i>aria2.forcePause()</i> for every active/waiting download. This methods returns <code>OK</code>.</p>
<dt><code>aria2.unpause([secret], gid)</code></p>
<dd> This method changes the status of the download denoted by <i>gid</i> (string) from <code>paused</code> to <code>waiting</code>, making the download eligible to be restarted. This method returns the GID of the unpaused download.</p>
<dt><code>aria2.unpauseAll([secret])</code></p>
<dd> This method is equal to calling <i>aria2.unpause()</i> for every paused download. This methods returns <code>OK</code>.</p>
<dt><code>aria2.tellStatus([secret], gid[, keys])</code></p>
<dd> This method returns the progress of the download denoted by <i>gid</i> (string). <i>keys</i> is an array of strings. If specified, the response contains only keys in the <i>keys</i> array. If <i>keys</i> is empty or omitted, the response contains all keys. This is useful when you just want specific keys and avoid unnecessary transfers. For example, <code>aria2.tellStatus(&quot;2089b05ecca3d829&quot;, [&quot;gid&quot;, &quot;status&quot;])</code> returns the <i>gid</i> and <i>status</i> keys only. The response is a struct and contains following keys. Values are strings.</p>
<dt><code>gid</code></p>
<dd> GID of the download.</p>
<dt><code>status</code></p>
<dd> <code>active</code> for currently downloading/seeding downloads. <code>waiting</code> for downloads in the queue; download is not started. <code>paused</code> for paused downloads. <code>error</code> for downloads that were stopped because of error. <code>complete</code> for stopped and completed downloads. <code>removed</code> for the downloads removed by user.</p>
<dt><code>totalLength</code></p>
<dd> Total length of the download in bytes.</p>
<dt><code>completedLength</code></p>
<dd> Completed length of the download in bytes.</p>
<dt><code>uploadLength</code></p>
<dd> Uploaded length of the download in bytes.</p>
<dt><code>bitfield</code></p>
<dd> Hexadecimal representation of the download progress. The highest bit corresponds to the piece at index 0. Any set bits indicate loaded pieces, while unset bits indicate not yet loaded and/or missing pieces. Any overflow bits at the end are set to zero. When the download was not started yet, this key will not be included in the response.</p>
<dt><code>downloadSpeed</code></p>
<dd> Download speed of this download measured in bytes/sec.</p>
<dt><code>uploadSpeed</code></p>
<dd> Upload speed of this download measured in bytes/sec.</p>
<dt><code>infoHash</code></p>
<dd> InfoHash. BitTorrent only.</p>
<dt><code>numSeeders</code></p>
<dd> The number of seeders aria2 has connected to. BitTorrent only.</p>
<dt><code>seeder</code></p>
<dd> <code>true</code> if the local endpoint is a seeder. Otherwise <code>false</code>. BitTorrent only.</p>
<dt><code>pieceLength</code></p>
<dd> Piece length in bytes.</p>
<dt><code>numPieces</code></p>
<dd> The number of pieces.</p>
<dt><code>connections</code></p>
<dd> The number of peers/servers aria2 has connected to.</p>
<dt><code>errorCode</code></p>
<dd> The code of the last error for this item, if any. The value is a string. The error codes are defined in the <i>EXIT STATUS</i> section. This value is only available for stopped/completed downloads.</p>
<dt><code>errorMessage</code></p>
<dd> The (hopefully) human readable error message associated to <code>errorCode</code>.</p>
<dt><code>followedBy</code></p>
<dd> List of GIDs which are generated as the result of this download. For example, when aria2 downloads a Metalink file, it generates downloads described in the Metalink (see the <i>&#8211;follow-metalink</i> option). This value is useful to track auto-generated downloads. If there are no such downloads, this key will not be included in the response.</p>
<dt><code>following</code></p>
<dd> The reverse link for <code>followedBy</code>. A download included in <code>followedBy</code> has this object&#8217;s GID in its <code>following</code> value.</p>
<dt><code>belongsTo</code></p>
<dd> GID of a parent download. Some downloads are a part of another download. For example, if a file in a Metalink has BitTorrent resources, the downloads of &quot;.torrent&quot; files are parts of that parent. If this download has no parent, this key will not be included in the response.</p>
<dt><code>dir</code></p>
<dd> Directory to save files.</p>
<dt><code>files</code></p>
<dd> Returns the list of files. The elements of this list are the same structs used in <i>aria2.getFiles()</i> method.</p>
<dt><code>bittorrent</code></p>
<dd> Struct which contains information retrieved from the .torrent (file). BitTorrent only. It contains following keys.</p>
<dt><code>announceList</code></p>
<dd> List of lists of announce URIs. If the torrent contains <code>announce</code> and no <code>announce-list</code>, <code>announce</code> is converted to the <code>announce-list</code> format.</p>
<dt><code>comment</code></p>
<dd> The comment of the torrent. <code>comment.utf-8</code> is used if available.</p>
<dt><code>creationDate</code></p>
<dd> The creation time of the torrent. The value is an integer since the epoch, measured in seconds.</p>
<dt><code>mode</code></p>
<dd> File mode of the torrent. The value is either <code>single</code> or <code>multi</code>.</p>
<dt><code>info</code></p>
<dd> Struct which contains data from Info dictionary. It contains following keys.</p>
<dt><code>name</code></p>
<dd> name in info dictionary. <code>name.utf-8</code> is used if available.</p>
<dt><code>verifiedLength</code></p>
<dd> The number of verified number of bytes while the files are being hash checked. This key exists only when this download is being hash checked.</p>
<dt><code>verifyIntegrityPending</code></p>
<dd> <code>true</code> if this download is waiting for the hash check in a queue. This key exists only when this download is in the queue. </p>
<p> <code>JSON-RPC Example</code> </p>
<p> The following example gets information about a download with GID#2089b05ecca3d829: </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.tellStatus&#8217;, &#8230; &#8216;params&#8217; : [&#8216;2089b05ecca3d829&#8217;]}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;,<br />
            u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;,<br />
                         u&#8217;result&#8217;:<br />
    {<br />
        u&#8217;bitfield&#8217; : u&#8217;0000000000&#8242;,<br />
                      u&#8217;completedLength&#8217; : u&#8217;901120&#8242;,<br />
                                           u&#8217;connections&#8217; : u&#8217;1&#8242;,<br />
                                                            u&#8217;dir&#8217; : u&#8217;/downloads&#8217;,<br />
                                                                     u&#8217;downloadSpeed&#8217; : u&#8217;15158&#8242;,<br />
                                                                                        u&#8217;files&#8217; : [ {u&#8217;index&#8217; : u&#8217;1&#8242;,<br />
                                                                                                      u&#8217;length&#8217; : u&#8217;34896138&#8242;,<br />
                                                                                                      u&#8217;completedLength&#8217; : u&#8217;34896138&#8242;,<br />
                                                                                                      u&#8217;path&#8217; : u&#8217;/downloads/file&#8217;,<br />
                                                                                                      u&#8217;selected&#8217; : u&#8217;true&#8217;,<br />
                                                                                                      u&#8217;uris&#8217; : [ {u&#8217;status&#8217; : u&#8217;used&#8217;,<br />
                                                                                                                   u&#8217;uri&#8217; : u&#8217;http://example.org/file&#8217;} ]} ],<br />
                                                                                                   u&#8217;gid&#8217; : u&#8217;2089b05ecca3d829&#8242;,<br />
                                                                                                            u&#8217;numPieces&#8217; : u&#8217;34&#8217;,<br />
                                                                                                                           u&#8217;pieceLength&#8217; : u&#8217;1048576&#8242;,<br />
                                                                                                                                            u&#8217;status&#8217; : u&#8217;active&#8217;,<br />
                                                                                                                                                        u&#8217;totalLength&#8217; : u&#8217;34896138&#8242;,<br />
                                                                                                                                                                         u&#8217;uploadLength&#8217; : u&#8217;0&#8242;,<br />
                                                                                                                                                                                           u&#8217;uploadSpeed&#8217; : u&#8217;0&#8242;<br />
    }<br />
}</p>
<p> The following example gets only specific keys: </p>
<p>&gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.tellStatus&#8217;, &#8230; &#8216;params&#8217; : [ &#8216;2089b05ecca3d829&#8217;,<br />
                                                                                                                &#8230;[&#8216;gid&#8217;,<br />
                                                                                                                    &#8230; &#8216;totalLength&#8217;,<br />
                                                                                                                    &#8230; &#8216;completedLength&#8217;] ]}) &gt;&gt;&gt;<br />
              c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;,<br />
            u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;,<br />
                         u&#8217;result&#8217;:<br />
    {<br />
        u&#8217;completedLength&#8217; : u&#8217;5701632&#8242;,<br />
                             u&#8217;gid&#8217; : u&#8217;2089b05ecca3d829&#8242;,<br />
                                      u&#8217;totalLength&#8217; : u&#8217;34896138&#8242;<br />
    }<br />
}</p>
<p> <code>XML-RPC Example</code> </p>
<p> The following example gets information about a download with GID#2089b05ecca3d829: </p>
<p>&gt;&gt;&gt; import xmlrpclib &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; s = xmlrpclib.ServerProxy(&#8216;http://localhost:6800/rpc&#8217;) &gt;&gt;&gt; r = s.aria2.tellStatus(&#8216;2089b05ecca3d829&#8217;) &gt;&gt;&gt; pprint(r)<br />
{<br />
    &#8216;bitfield&#8217; : &#8216;ffff80&#8217;,<br />
                 &#8216;completedLength&#8217; : &#8216;34896138&#8217;,<br />
                                     &#8216;connections&#8217; : &#8216;0&#8217;,<br />
                                                     &#8216;dir&#8217; : &#8216;/downloads&#8217;,<br />
                                                             &#8216;downloadSpeed&#8217; : &#8216;0&#8217;,<br />
                                                                               &#8216;errorCode&#8217; : &#8216;0&#8217;,<br />
                                                                                             &#8216;files&#8217; : [ {&#8216;index&#8217; : &#8216;1&#8217;,<br />
                                                                                                          &#8216;length&#8217; : &#8216;34896138&#8217;,<br />
                                                                                                          &#8216;completedLength&#8217; : &#8216;34896138&#8217;,<br />
                                                                                                          &#8216;path&#8217; : &#8216;/downloads/file&#8217;,<br />
                                                                                                          &#8216;selected&#8217; : &#8216;true&#8217;,<br />
                                                                                                          &#8216;uris&#8217; : [ {&#8216;status&#8217; : &#8216;used&#8217;,<br />
                                                                                                                      &#8216;uri&#8217; : &#8216;http://example.org/file&#8217;} ]} ],<br />
                                                                                                       &#8216;gid&#8217; : &#8216;2089b05ecca3d829&#8217;,<br />
                                                                                                               &#8216;numPieces&#8217; : &#8217;17&#8217;,<br />
                                                                                                                             &#8216;pieceLength&#8217; : &#8216;2097152&#8217;,<br />
                                                                                                                                             &#8216;status&#8217; : &#8216;complete&#8217;,<br />
                                                                                                                                                        &#8216;totalLength&#8217; : &#8216;34896138&#8217;,<br />
                                                                                                                                                                        &#8216;uploadLength&#8217; : &#8216;0&#8217;,<br />
                                                                                                                                                                                         &#8216;uploadSpeed&#8217; : &#8216;0&#8217;<br />
}</p>
<p> The following example gets only specific keys: </p>
<p>&gt;&gt;&gt; r = s.aria2.tellStatus(&#8216;2089b05ecca3d829&#8217;, [ &#8216;gid&#8217;, &#8216;totalLength&#8217;, &#8216;completedLength&#8217; ]) &gt;&gt;&gt; pprint(r)<br />
{<br />
    &#8216;completedLength&#8217; : &#8216;34896138&#8217;, &#8216;gid&#8217; : &#8216;2089b05ecca3d829&#8217;, &#8216;totalLength&#8217; : &#8216;34896138&#8217;<br />
}</p>
<dt><code>aria2.getUris([secret], gid)</code></p>
<dd> This method returns the URIs used in the download denoted by <i>gid</i> (string). The response is an array of structs and it contains following keys. Values are string.</p>
<dt><code>uri</code></p>
<dd> URI</p>
<dt><code>status</code></p>
<dd> &#8216;used&#8217; if the URI is in use. &#8216;waiting&#8217; if the URI is still waiting in the queue. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.getUris&#8217;, &#8230; &#8216;params&#8217; : [&#8216;2089b05ecca3d829&#8217;]}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;,<br />
            u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;,<br />
                         u&#8217;result&#8217; : [ {u&#8217;status&#8217; : u&#8217;used&#8217;,<br />
                                        u&#8217;uri&#8217; : u&#8217;http://example.org/file&#8217;} ]<br />
}</p>
<p> <code>XML-RPC Example</code> </p>
<p>&gt;&gt;&gt; import xmlrpclib &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; s = xmlrpclib.ServerProxy(&#8216;http://localhost:6800/rpc&#8217;) &gt;&gt;&gt; r = s.aria2.getUris(&#8216;2089b05ecca3d829&#8217;) &gt;&gt;&gt; pprint(r)<br />
                                                                                                                                                                  [{&#8216;status&#8217; : &#8216;used&#8217;, &#8216;uri&#8217; : &#8216;http://example.org/file&#8217;}]</p>
<dt><code>aria2.getFiles([secret], gid)</code></p>
<dd> This method returns the file list of the download denoted by <i>gid</i> (string). The response is an array of structs which contain following keys. Values are strings.</p>
<dt><code>index</code></p>
<dd> Index of the file, starting at 1, in the same order as files appear in the multi-file torrent.</p>
<dt><code>path</code></p>
<dd> File path.</p>
<dt><code>length</code></p>
<dd> File size in bytes.</p>
<dt><code>completedLength</code></p>
<dd> Completed length of this file in bytes. Please note that it is possible that sum of <code>completedLength</code> is less than the <code>completedLength</code> returned by the <i>aria2.tellStatus()</i> method. This is because <code>completedLength</code> in <i>aria2.getFiles()</i> only includes completed pieces. On the other hand, <code>completedLength</code> in <i>aria2.tellStatus()</i> also includes partially completed pieces.</p>
<dt><code>selected</code></p>
<dd> <code>true</code> if this file is selected by <i>&#8211;select-file</i> option. If <i>&#8211;select-file</i> is not specified or this is single-file torrent or not a torrent download at all, this value is always <code>true</code>. Otherwise <code>false</code>.</p>
<dt><code>uris</code></p>
<dd> Returns a list of URIs for this file. The element type is the same struct used in the <i>aria2.getUris()</i> method. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.getFiles&#8217;, &#8230; &#8216;params&#8217; : [&#8216;2089b05ecca3d829&#8217;]}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;,<br />
            u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;,<br />
                         u&#8217;result&#8217; : [ {u&#8217;index&#8217; : u&#8217;1&#8242;,<br />
                                        u&#8217;length&#8217; : u&#8217;34896138&#8242;,<br />
                                        u&#8217;completedLength&#8217; : u&#8217;34896138&#8242;,<br />
                                        u&#8217;path&#8217; : u&#8217;/downloads/file&#8217;,<br />
                                        u&#8217;selected&#8217; : u&#8217;true&#8217;,<br />
                                        u&#8217;uris&#8217; : [ {u&#8217;status&#8217; : u&#8217;used&#8217;,<br />
                                                     u&#8217;uri&#8217; : u&#8217;http://example.org/file&#8217;} ]} ]<br />
}</p>
<p> <code>XML-RPC Example</code> </p>
<p>&gt;&gt;&gt; import xmlrpclib &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; s = xmlrpclib.ServerProxy(&#8216;http://localhost:6800/rpc&#8217;) &gt;&gt;&gt; r = s.aria2.getFiles(&#8216;2089b05ecca3d829&#8217;) &gt;&gt;&gt; pprint(r)<br />
                                                                                                                                                                   [{&#8216;index&#8217; : &#8216;1&#8217;,<br />
                                                                                                                                                                     &#8216;length&#8217; : &#8216;34896138&#8217;,<br />
                                                                                                                                                                     &#8216;completedLength&#8217; : &#8216;34896138&#8217;,<br />
                                                                                                                                                                     &#8216;path&#8217; : &#8216;/downloads/file&#8217;,<br />
                                                                                                                                                                     &#8216;selected&#8217; : &#8216;true&#8217;,<br />
                                                                                                                                                                     &#8216;uris&#8217; : [ {&#8216;status&#8217; : &#8216;used&#8217;,<br />
                                                                                                                                                                                 &#8216;uri&#8217; : &#8216;http://example.org/file&#8217;} ]}]</p>
<dt><code>aria2.getPeers([secret], gid)</code></p>
<dd> This method returns a list peers of the download denoted by <i>gid</i> (string). This method is for BitTorrent only. The response is an array of structs and contains the following keys. Values are strings.</p>
<dt><code>peerId</code></p>
<dd> Percent-encoded peer ID.</p>
<dt><code>ip</code></p>
<dd> IP address of the peer.</p>
<dt><code>port</code></p>
<dd> Port number of the peer.</p>
<dt><code>bitfield</code></p>
<dd> Hexadecimal representation of the download progress of the peer. The highest bit corresponds to the piece at index 0. Set bits indicate the piece is available and unset bits indicate the piece is missing. Any spare bits at the end are set to zero.</p>
<dt><code>amChoking</code></p>
<dd> <code>true</code> if aria2 is choking the peer. Otherwise <code>false</code>.</p>
<dt><code>peerChoking</code></p>
<dd> <code>true</code> if the peer is choking aria2. Otherwise <code>false</code>.</p>
<dt><code>downloadSpeed</code></p>
<dd> Download speed (byte/sec) that this client obtains from the peer.</p>
<dt><code>uploadSpeed</code></p>
<dd> Upload speed(byte/sec) that this client uploads to the peer.</p>
<dt><code>seeder</code></p>
<dd> <code>true</code> if this peer is a seeder. Otherwise <code>false</code>. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.getPeers&#8217;, &#8230; &#8216;params&#8217; : [&#8216;2089b05ecca3d829&#8217;]}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;,<br />
            u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;,<br />
                         u&#8217;result&#8217; : [ {u&#8217;amChoking&#8217; : u&#8217;true&#8217;,<br />
                                        u&#8217;bitfield&#8217; : u&#8217;ffffffffffffffffffffffffffffffffffffffff&#8217;,<br />
                                        u&#8217;downloadSpeed&#8217; : u&#8217;10602&#8242;,<br />
                                        u&#8217;ip&#8217; : u&#8217;10.0.0.9&#8242;,<br />
                                        u&#8217;peerChoking&#8217; : u&#8217;false&#8217;,<br />
                                        u&#8217;peerId&#8217; : u&#8217;aria2%2F1%2E10%2E5%2D%87%2A%EDz%2F%F7%E6&#8242;,<br />
                                        u&#8217;port&#8217; : u&#8217;6881&#8242;,<br />
                                        u&#8217;seeder&#8217; : u&#8217;true&#8217;,<br />
                                        u&#8217;uploadSpeed&#8217; : u&#8217;0&#8242;},<br />
                                       {u&#8217;amChoking&#8217; : u&#8217;false&#8217;,<br />
                                        u&#8217;bitfield&#8217; : u&#8217;ffffeff0fffffffbfffffff9fffffcfff7f4ffff&#8217;,<br />
                                        u&#8217;downloadSpeed&#8217; : u&#8217;8654&#8242;,<br />
                                        u&#8217;ip&#8217; : u&#8217;10.0.0.30&#8242;,<br />
                                        u&#8217;peerChoking&#8217; : u&#8217;false&#8217;,<br />
                                        u&#8217;peerId&#8217; : u&#8217;bittorrent client758&#8242;,<br />
                                        u&#8217;port&#8217; : u&#8217;37842&#8242;,<br />
                                        u&#8217;seeder&#8217; : u&#8217;false&#8217;,<br />
                                        u&#8217;uploadSpeed&#8217; : u&#8217;6890&#8242;} ]<br />
}</p>
<p> <code>XML-RPC Example</code> </p>
<p>&gt;&gt;&gt; import xmlrpclib &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; s = xmlrpclib.ServerProxy(&#8216;http://localhost:6800/rpc&#8217;) &gt;&gt;&gt; r = s.aria2.getPeers(&#8216;2089b05ecca3d829&#8217;) &gt;&gt;&gt; pprint(r)<br />
                                                                                                                                                                   [{&#8216;amChoking&#8217; : &#8216;true&#8217;,<br />
                                                                                                                                                                     &#8216;bitfield&#8217; : &#8216;ffffffffffffffffffffffffffffffffffffffff&#8217;,<br />
                                                                                                                                                                     &#8216;downloadSpeed&#8217; : &#8216;10602&#8217;,<br />
                                                                                                                                                                     &#8216;ip&#8217; : &#8216;10.0.0.9&#8217;,<br />
                                                                                                                                                                     &#8216;peerChoking&#8217; : &#8216;false&#8217;,<br />
                                                                                                                                                                     &#8216;peerId&#8217; : &#8216;aria2%2F1%2E10%2E5%2D%87%2A%EDz%2F%F7%E6&#8217;,<br />
                                                                                                                                                                     &#8216;port&#8217; : &#8216;6881&#8217;,<br />
                                                                                                                                                                     &#8216;seeder&#8217; : &#8216;true&#8217;,<br />
                                                                                                                                                                     &#8216;uploadSpeed&#8217; : &#8216;0&#8217;},<br />
                                                                                                                                                                    {&#8216;amChoking&#8217; : &#8216;false&#8217;,<br />
                                                                                                                                                                     &#8216;bitfield&#8217; : &#8216;ffffeff0fffffffbfffffff9fffffcfff7f4ffff&#8217;,<br />
                                                                                                                                                                     &#8216;downloadSpeed&#8217; : &#8216;8654&#8217;,<br />
                                                                                                                                                                     &#8216;ip&#8217; : &#8216;10.0.0.30&#8217;,<br />
                                                                                                                                                                     &#8216;peerChoking&#8217; : &#8216;false&#8217;,<br />
                                                                                                                                                                     &#8216;peerId&#8217; : &#8216;bittorrent client758&#8217;,<br />
                                                                                                                                                                     &#8216;port&#8217; : &#8216;37842&#8217;,<br />
                                                                                                                                                                     &#8216;seeder&#8217; : &#8216;false, &#8216;uploadSpeed&#8217; : &#8216;6890&#8217;}]</p>
<dt><code>aria2.getServers([secret], gid)</code></p>
<dd> This method returns currently connected HTTP(S)/FTP/SFTP servers of the download denoted by <i>gid</i> (string). The response is an array of structs and contains the following keys. Values are strings.</p>
<dt><code>index</code></p>
<dd> Index of the file, starting at 1, in the same order as files appear in the multi-file metalink.</p>
<dt><code>servers</code></p>
<dd> A list of structs which contain the following keys.</p>
<dt><code>uri</code></p>
<dd> Original URI.</p>
<dt><code>currentUri</code></p>
<dd> This is the URI currently used for downloading. If redirection is involved, currentUri and uri may differ.</p>
<dt><code>downloadSpeed</code></p>
<dd> Download speed (byte/sec) </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.getServers&#8217;, &#8230; &#8216;params&#8217; : [&#8216;2089b05ecca3d829&#8217;]}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;,<br />
            u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;,<br />
                         u&#8217;result&#8217; : [ {u&#8217;index&#8217; : u&#8217;1&#8242;,<br />
                                        u&#8217;servers&#8217; : [ {u&#8217;currentUri&#8217; : u&#8217;http://example.org/file&#8217;,<br />
                                                        u&#8217;downloadSpeed&#8217; : u&#8217;10467&#8242;,<br />
                                                        u&#8217;uri&#8217; : u&#8217;http://example.org/file&#8217;} ]} ]<br />
}</p>
<p> <code>XML-RPC Example</code> </p>
<p>&gt;&gt;&gt; import xmlrpclib &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; s = xmlrpclib.ServerProxy(&#8216;http://localhost:6800/rpc&#8217;) &gt;&gt;&gt; r = s.aria2.getServers(&#8216;2089b05ecca3d829&#8217;) &gt;&gt;&gt; pprint(r)<br />
                                                                                                                                                                     [{&#8216;index&#8217; : &#8216;1&#8217;,<br />
                                                                                                                                                                       &#8216;servers&#8217; : [ {&#8216;currentUri&#8217; : &#8216;http://example.org/dl/file&#8217;,<br />
                                                                                                                                                                                      &#8216;downloadSpeed&#8217; : &#8216;20285&#8217;,<br />
                                                                                                                                                                                      &#8216;uri&#8217; : &#8216;http://example.org/file&#8217;} ]}]</p>
<dt><code>aria2.tellActive([secret][, keys])</code></p>
<dd> This method returns a list of active downloads. The response is an array of the same structs as returned by the <i>aria2.tellStatus()</i> method. For the <i>keys</i> parameter, please refer to the <i>aria2.tellStatus()</i> method.</p>
<dt><code>aria2.tellWaiting([secret], offset, num[, keys])</code></p>
<dd> This method returns a list of waiting downloads, including paused ones. <i>offset</i> is an integer and specifies the offset from the download waiting at the front. <i>num</i> is an integer and specifies the max. number of downloads to be returned. For the <i>keys</i> parameter, please refer to the <i>aria2.tellStatus()</i> method. </p>
<p> If <i>offset</i> is a positive integer, this method returns downloads in the range of [<i>offset</i>, <i>offset</i> + <i>num</i>). </p>
<p> <i>offset</i> can be a negative integer. <i>offset</i> == -1 points last download in the waiting queue and <i>offset</i> == -2 points the download before the last download, and so on. Downloads in the response are in reversed order then. </p>
<p> For example, imagine three downloads &quot;A&quot;,&quot;B&quot; and &quot;C&quot; are waiting in this order. <code>aria2.tellWaiting(0, 1)</code> returns <code>[&quot;A&quot;]</code>. <code>aria2.tellWaiting(1, 2)</code> returns <code>[&quot;B&quot;, &quot;C&quot;]</code>. <code>aria2.tellWaiting(-1, 2)</code> returns <code>[&quot;C&quot;, &quot;B&quot;]</code>. </p>
<p> The response is an array of the same structs as returned by <i>aria2.tellStatus()</i> method.</p>
<dt><code>aria2.tellStopped([secret], offset, num[, keys])</code></p>
<dd> This method returns a list of stopped downloads. <i>offset</i> is an integer and specifies the offset from the least recently stopped download. <i>num</i> is an integer and specifies the max. number of downloads to be returned. For the <i>keys</i> parameter, please refer to the <i>aria2.tellStatus()</i> method. </p>
<p> <i>offset</i> and <i>num</i> have the same semantics as described in the <i>aria2.tellWaiting()</i> method. </p>
<p> The response is an array of the same structs as returned by the <i>aria2.tellStatus()</i> method.</p>
<dt><code>aria2.changePosition([secret], gid, pos, how)</code></p>
<dd> This method changes the position of the download denoted by <i>gid</i> in the queue. <i>pos</i> is an integer. <i>how</i> is a string. If <i>how</i> is <code>POS_SET</code>, it moves the download to a position relative to the beginning of the queue. If <i>how</i> is <code>POS_CUR</code>, it moves the download to a position relative to the current position. If <i>how</i> is <code>POS_END</code>, it moves the download to a position relative to the end of the queue. If the destination position is less than 0 or beyond the end of the queue, it moves the download to the beginning or the end of the queue respectively. The response is an integer denoting the resulting position. </p>
<p> For example, if GID#2089b05ecca3d829 is currently in position 3, <code>aria2.changePosition(&#8216;2089b05ecca3d829&#8217;, -1, &#8216;POS_CUR&#8217;)</code> will change its position to 2. Additionally <code>aria2.changePosition(&#8216;2089b05ecca3d829&#8217;, 0, &#8216;POS_SET&#8217;)</code> will change its position to 0 (the beginning of the queue). </p>
<p> The following examples move the download GID#2089b05ecca3d829 to the front of the queue. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.changePosition&#8217;, &#8230; &#8216;params&#8217; : [ &#8216;2089b05ecca3d829&#8217;, 0, &#8216;POS_SET&#8217; ]}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;, u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;, u&#8217;result&#8217; : 0<br />
}</p>
<p> <code>XML-RPC Example</code> </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; s.aria2.changePosition('2089b05ecca3d829', 0, 'POS_SET')
0
</pre>
<dt><code>aria2.changeUri([secret], gid, fileIndex, delUris, addUris[, position])</code></p>
<dd> This method removes the URIs in <i>delUris</i> from and appends the URIs in <i>addUris</i> to download denoted by <i>gid</i>. <i>delUris</i> and <i>addUris</i> are lists of strings. A download can contain multiple files and URIs are attached to each file. <i>fileIndex</i> is used to select which file to remove/attach given URIs. <i>fileIndex</i> is 1-based. <i>position</i> is used to specify where URIs are inserted in the existing waiting URI list. <i>position</i> is 0-based. When <i>position</i> is omitted, URIs are appended to the back of the list. This method first executes the removal and then the addition. <i>position</i> is the position after URIs are removed, not the position when this method is called. When removing an URI, if the same URIs exist in download, only one of them is removed for each URI in <i>delUris</i>. In other words, if there are three URIs <code><a rel="nofollow" href="http://example.org/aria2">http://example.org/aria2</a></code> and you want remove them all, you have to specify (at least) 3 <code><a rel="nofollow" href="http://example.org/aria2">http://example.org/aria2</a></code> in <i>delUris</i>. This method returns a list which contains two integers. The first integer is the number of URIs deleted. The second integer is the number of URIs added. </p>
<p> The following examples add the URI <code><a rel="nofollow" href="http://example.org/file">http://example.org/file</a></code> to the file whose index is <code>1</code> and belongs to the download GID#2089b05ecca3d829. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.changeUri&#8217;, &#8230; &#8216;params&#8217; : [ &#8216;2089b05ecca3d829&#8217;, 1, [],<br />
                                                                                                                                                                      [&#8216;http://example.org/file&#8217;] ]}) &gt;&gt;&gt;<br />
                                                                     c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;, u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;, u&#8217;result&#8217; : [ 0, 1 ]<br />
}</p>
<p> <code>XML-RPC Example</code> </p>
<p>&gt;&gt;&gt; import xmlrpclib &gt;&gt;&gt; s = xmlrpclib.ServerProxy(&#8216;http://localhost:6800/rpc&#8217;) &gt;&gt;&gt; s.aria2.changeUri(&#8216;2089b05ecca3d829&#8217;, 1, [],<br />
                                                                                                      [&#8216;http://example.org/file&#8217;])<br />
                                                                                        [0, 1]</p>
<dt><code>aria2.getOption([secret], gid)</code></p>
<dd> This method returns options of the download denoted by <i>gid</i>. The response is a struct where keys are the names of options. The values are strings. Note that this method does not return options which have no default value and have not been set on the command-line, in configuration files or RPC methods. </p>
<p> The following examples get options of the download GID#2089b05ecca3d829. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.getOption&#8217;, &#8230; &#8216;params&#8217; : [&#8216;2089b05ecca3d829&#8217;]}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;,<br />
            u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;,<br />
                         u&#8217;result&#8217;:<br />
    {<br />
        u&#8217;allow-overwrite&#8217; : u&#8217;false&#8217;,<br />
                             u&#8217;allow-piece-length-change&#8217; : u&#8217;false&#8217;,<br />
                                                            u&#8217;always-resume&#8217; : u&#8217;true&#8217;,<br />
                                                                               u&#8217;async-dns&#8217; : u&#8217;true&#8217;,<br />
                                                                                              &#8230;</p>
<p> <code>XML-RPC Example</code> </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; from pprint import pprint
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; r = s.aria2.getOption('2089b05ecca3d829')
&gt;&gt;&gt; pprint(r)
{'allow-overwrite': 'false',
 'allow-piece-length-change': 'false',
 'always-resume': 'true',
 'async-dns': 'true',
 ....
</pre>
<dt><code>aria2.changeOption([secret], gid, options)</code></p>
<dd> This method changes options of the download denoted by <i>gid</i> (string) dynamically. <i>options</i> is a struct. The options listed in <i>Input File</i> subsection are available, <code>except</code> for following options:</p>
<dt>&bull;</p>
<dd> <i>dry-run</i></p>
<dt>&bull;</p>
<dd> <i>metalink-base-uri</i></p>
<dt>&bull;</p>
<dd> <i>parameterized-uri</i></p>
<dt>&bull;</p>
<dd> <i>pause</i></p>
<dt>&bull;</p>
<dd> <i>piece-length</i></p>
<dt>&bull;</p>
<dd> <i>rpc-save-upload-metadata</i> </p>
<p> Except for the following options, changing the other options of active download makes it restart (restart itself is managed by aria2, and no user intervention is required):</p>
<dt>&bull;</p>
<dd> <i>bt-max-peers</i></p>
<dt>&bull;</p>
<dd> <i>bt-request-peer-speed-limit</i></p>
<dt>&bull;</p>
<dd> <i>bt-remove-unselected-file</i></p>
<dt>&bull;</p>
<dd> <i>force-save</i></p>
<dt>&bull;</p>
<dd> <i>max-download-limit</i></p>
<dt>&bull;</p>
<dd> <i>max-upload-limit</i> </p>
<p> This method returns <code>OK</code> for success. </p>
<p> The following examples set the <i>max-download-limit</i> option to <code>20K</code> for the download GID#2089b05ecca3d829. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.changeOption&#8217;, &#8230; &#8216;params&#8217; : [ &#8216;2089b05ecca3d829&#8217;,<br />
                                                                                                                                                                         &#8230; {&#8216;max-download-limit&#8217; : &#8217;10K&#8217;} ]}) &gt;&gt;&gt;<br />
                                                                     c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;, u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;, u&#8217;result&#8217; : u&#8217;OK&#8217;<br />
}</p>
<p> <code>XML-RPC Example</code> </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; s.aria2.changeOption('2089b05ecca3d829', {'max-download-limit':'20K'})
'OK'
</pre>
<dt><code>aria2.getGlobalOption([secret])</code></p>
<dd> This method returns the global options. The response is a struct. Its keys are the names of options. Values are strings. Note that this method does not return options which have no default value and have not been set on the command-line, in configuration files or RPC methods. Because global options are used as a template for the options of newly added downloads, the response contains keys returned by the <i>aria2.getOption()</i> method.</p>
<dt><code>aria2.changeGlobalOption([secret], options)</code></p>
<dd> This method changes global options dynamically. <i>options</i> is a struct. The following options are available:</p>
<dt>&bull;</p>
<dd> <i>bt-max-open-files</i></p>
<dt>&bull;</p>
<dd> <i>download-result</i></p>
<dt>&bull;</p>
<dd> <i>keep-unfinished-download-result</i></p>
<dt>&bull;</p>
<dd> <i>log</i></p>
<dt>&bull;</p>
<dd> <i>log-level</i></p>
<dt>&bull;</p>
<dd> <i>max-concurrent-downloads</i></p>
<dt>&bull;</p>
<dd> <i>max-download-result</i></p>
<dt>&bull;</p>
<dd> <i>max-overall-download-limit</i></p>
<dt>&bull;</p>
<dd> <i>max-overall-upload-limit</i></p>
<dt>&bull;</p>
<dd> <i>optimize-concurrent-downloads</i></p>
<dt>&bull;</p>
<dd> <i>save-cookies</i></p>
<dt>&bull;</p>
<dd> <i>save-session</i></p>
<dt>&bull;</p>
<dd> <i>server-stat-of</i> </p>
<p> In addition, options listed in the <i>Input File</i> subsection are available, <code>except</code> for following options: <i>checksum</i>, <i>index-out</i>, <i>out</i>, <i>pause</i> and <i>select-file</i>. </p>
<p> With the <i>log</i> option, you can dynamically start logging or change log file. To stop logging, specify an empty string(&quot;&quot;) as the parameter value. Note that log file is always opened in append mode. This method returns <code>OK</code> for success.</p>
<dt><code>aria2.getGlobalStat([secret])</code></p>
<dd> This method returns global statistics such as the overall download and upload speeds. The response is a struct and contains the following keys. Values are strings.</p>
<dt><code>downloadSpeed</code></p>
<dd> Overall download speed (byte/sec).</p>
<dt><code>uploadSpeed</code></p>
<dd> Overall upload speed(byte/sec).</p>
<dt><code>numActive</code></p>
<dd> The number of active downloads.</p>
<dt><code>numWaiting</code></p>
<dd> The number of waiting downloads.</p>
<dt><code>numStopped</code></p>
<dd> The number of stopped downloads in the current session. This value is capped by the <i>&#8211;max-download-result</i> option.</p>
<dt><code>numStoppedTotal</code></p>
<dd> The number of stopped downloads in the current session and <i>not</i> capped by the <i>&#8211;max-download-result</i> option. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.getGlobalStat&#8217;}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;,<br />
            u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;,<br />
                         u&#8217;result&#8217;:<br />
    {<br />
        u&#8217;downloadSpeed&#8217; : u&#8217;21846&#8242;,<br />
                           u&#8217;numActive&#8217; : u&#8217;2&#8242;,<br />
                                          u&#8217;numStopped&#8217; : u&#8217;0&#8242;,<br />
                                                          u&#8217;numWaiting&#8217; : u&#8217;0&#8242;,<br />
                                                                          u&#8217;uploadSpeed&#8217; : u&#8217;0&#8242;<br />
    }<br />
}</p>
<p> <code>XML-RPC Example</code> </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; from pprint import pprint
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; r = s.aria2.getGlobalStat()
&gt;&gt;&gt; pprint(r)
{'downloadSpeed': '23136',
 'numActive': '2',
 'numStopped': '0',
 'numWaiting': '0',
 'uploadSpeed': '0'}
</pre>
<dt><code>aria2.purgeDownloadResult([secret])</code></p>
<dd> This method purges completed/error/removed downloads to free memory. This method returns <code>OK</code>.</p>
<dt><code>aria2.removeDownloadResult([secret], gid)</code></p>
<dd> This method removes a completed/error/removed download denoted by <i>gid</i> from memory. This method returns <code>OK</code> for success. </p>
<p> The following examples remove the download result of the download GID#2089b05ecca3d829. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.removeDownloadResult&#8217;, &#8230; &#8216;params&#8217; : [&#8216;2089b05ecca3d829&#8217;]}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;, u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;, u&#8217;result&#8217; : u&#8217;OK&#8217;<br />
}</p>
<p> <code>XML-RPC Example</code> </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; s.aria2.removeDownloadResult('2089b05ecca3d829')
'OK'
</pre>
<dt><code>aria2.getVersion([secret])</code></p>
<dd> This method returns the version of aria2 and the list of enabled features. The response is a struct and contains following keys.</p>
<dt><code>version</code></p>
<dd> Version number of aria2 as a string.</p>
<dt><code>enabledFeatures</code></p>
<dd> List of enabled features. Each feature is given as a string. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.getVersion&#8217;}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;,<br />
            u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;,<br />
                         u&#8217;result&#8217;:<br />
    {<br />
        u&#8217;enabledFeatures&#8217; : [ u&#8217;Async DNS&#8217;,<br />
                               u&#8217;BitTorrent&#8217;,<br />
                               u&#8217;Firefox3 Cookie&#8217;,<br />
                               u&#8217;GZip&#8217;,<br />
                               u&#8217;HTTPS&#8217;,<br />
                               u&#8217;Message Digest&#8217;,<br />
                               u&#8217;Metalink&#8217;,<br />
                               u&#8217;XML-RPC&#8217; ],<br />
                             u&#8217;version&#8217; : u&#8217;1.11.0&#8242;<br />
    }<br />
}</p>
<p> <code>XML-RPC Example</code> </p>
<p>&gt;&gt;&gt; import xmlrpclib &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; s = xmlrpclib.ServerProxy(&#8216;http://localhost:6800/rpc&#8217;) &gt;&gt;&gt; r = s.aria2.getVersion() &gt;&gt;&gt; pprint(r)<br />
{<br />
    &#8216;enabledFeatures&#8217; : [ &#8216;Async DNS&#8217;,<br />
                          &#8216;BitTorrent&#8217;,<br />
                          &#8216;Firefox3 Cookie&#8217;,<br />
                          &#8216;GZip&#8217;,<br />
                          &#8216;HTTPS&#8217;,<br />
                          &#8216;Message Digest&#8217;,<br />
                          &#8216;Metalink&#8217;,<br />
                          &#8216;XML-RPC&#8217; ],<br />
                        &#8216;version&#8217; : &#8216;1.11.0&#8217;<br />
}</p>
<dt><code>aria2.getSessionInfo([secret])</code></p>
<dd> This method returns session information. The response is a struct and contains following key.</p>
<dt><code>sessionId</code></p>
<dd> Session ID, which is generated each time when aria2 is invoked. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.getSessionInfo&#8217;}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;,<br />
            u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;,<br />
                         u&#8217;result&#8217;:<br />
    {<br />
        u&#8217;sessionId&#8217; : u&#8217;cd6a3bc6a1de28eb5bfa181e5f6b916d44af31a9&#8242;<br />
    }<br />
}</p>
<p> <code>XML-RPC Example</code> </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; s.aria2.getSessionInfo()
{'sessionId': 'cd6a3bc6a1de28eb5bfa181e5f6b916d44af31a9'}
</pre>
<dt><code>aria2.shutdown([secret])</code></p>
<dd> This method shuts down aria2. This method returns <code>OK</code>.</p>
<dt><code>aria2.forceShutdown([secret])</code></p>
<dd> This method shuts down <code>aria2()</code>. This method behaves like :func:&#8217;aria2.shutdown` without performing any actions which take time, such as contacting BitTorrent trackers to unregister downloads first. This method returns <code>OK</code>.</p>
<dt><code>aria2.saveSession([secret])</code></p>
<dd> This method saves the current session to a file specified by the <i>&#8211;save-session</i> option. This method returns <code>OK</code> if it succeeds.</p>
<dt><code>system.multicall(methods)</code></p>
<dd> This methods encapsulates multiple method calls in a single request. <i>methods</i> is an array of structs. The structs contain two keys: <code>methodName</code> and <code>params</code>. <code>methodName</code> is the method name to call and <code>params</code> is array containing parameters to the method call. This method returns an array of responses. The elements will be either a one-item array containing the return value of the method call or a struct of fault element if an encapsulated method call fails. </p>
<p> In the following examples, we add 2 downloads. The first one is <code><a rel="nofollow" href="http://example.org/file">http://example.org/file</a></code> and the second one is <code>file.torrent</code>. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json, base64 &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;system.multicall&#8217;, &#8230; &#8216;params&#8217; : [[ {&#8216;methodName&#8217; : &#8216;aria2.addUri&#8217;,<br />
                                                                                                                                                                                 &#8230; &#8216;params&#8217; : [[&#8216;http://example.org&#8217;]]},<br />
                                                                                                                                                                                &#8230; {&#8216;methodName&#8217; : &#8216;aria2.addTorrent&#8217;,<br />
                                                                                                                                                                                     &#8230; &#8216;params&#8217; : [base64.b64encode(open(&#8216;file.torrent&#8217;).read())]} ]]}) &gt;&gt;&gt;<br />
                                                                             c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{<br />
    u&#8217;id&#8217; : u&#8217;qwer&#8217;, u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;, u&#8217;result&#8217; : [ [u&#8217;2089b05ecca3d829&#8242;], [u&#8217;d2703803b52216d1&#8242;] ]<br />
}</p>
<p> JSON-RPC additionally supports Batch requests as described in the JSON-RPC 2.0 Specification: </p>
<p>&gt;&gt;&gt; jsonreq = json.dumps([ {&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.addUri&#8217;, &#8230; &#8216;params&#8217; : [[&#8216;http://example.org&#8217;]]},<br />
                           &#8230; {&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;asdf&#8217;, &#8230; &#8216;method&#8217; : &#8216;aria2.addTorrent&#8217;, &#8230; &#8216;params&#8217; : [base64.b64encode(open(&#8216;file.torrent&#8217;).read())]} ]) &gt;&gt;&gt;<br />
              c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
                                                                                    [{u&#8217;id&#8217; : u&#8217;qwer&#8217;, u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;, u&#8217;result&#8217; : u&#8217;2089b05ecca3d829&#8242;},<br />
                                                                                     {u&#8217;id&#8217; : u&#8217;asdf&#8217;, u&#8217;jsonrpc&#8217; : u&#8217;2.0&#8242;, u&#8217;result&#8217; : u&#8217;d2703803b52216d1&#8242;}]</p>
<p> <code>XML-RPC Example</code> </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; mc = xmlrpclib.MultiCall(s)
&gt;&gt;&gt; mc.aria2.addUri(['<a rel="nofollow" href="http://example.org/file'])">http://example.org/file'])</a>
&gt;&gt;&gt; mc.aria2.addTorrent(xmlrpclib.Binary(open('file.torrent', mode='rb').read()))
&gt;&gt;&gt; r = mc()
&gt;&gt;&gt; tuple(r)
('2089b05ecca3d829', 'd2703803b52216d1')
</pre>
<dt><code>system.listMethods()</code></p>
<dd> This method returns all the available RPC methods in an array of string. Unlike other methods, this method does not require secret token. This is safe because this method just returns the available method names. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;system.listMethods&#8217;}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{u&#8217;id&#8217;: u&#8217;qwer&#8217;,<br />
 u&#8217;jsonrpc&#8217;: u&#8217;2.0&#8242;,<br />
 u&#8217;result&#8217;: [u&#8217;aria2.addUri&#8217;,<br />
             u&#8217;aria2.addTorrent&#8217;,<br />
&#8230;</p>
<p> <code>XML-RPC Example</code> </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; s.system.listMethods()
['aria2.addUri', 'aria2.addTorrent', ...
</pre>
<dt><code>system.listNotifications()</code></p>
<dd> This method returns all the available RPC notifications in an array of string. Unlike other methods, this method does not require secret token. This is safe because this method just returns the available notifications names. </p>
<p> <code>JSON-RPC Example</code> </p>
<p>&gt;&gt;&gt; import urllib2, json &gt;&gt;&gt; from pprint import pprint &gt;&gt;&gt; jsonreq = json.dumps({&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8230; &#8216;method&#8217; : &#8216;system.listNotifications&#8217;}) &gt;&gt;&gt; c = urllib2.urlopen(&#8216;http://localhost:6800/jsonrpc&#8217;, jsonreq) &gt;&gt;&gt; pprint(json.loads(c.read()))<br />
{u&#8217;id&#8217;: u&#8217;qwer&#8217;,<br />
 u&#8217;jsonrpc&#8217;: u&#8217;2.0&#8242;,<br />
 u&#8217;result&#8217;: [u&#8217;aria2.onDownloadStart&#8217;,<br />
             u&#8217;aria2.onDownloadPause&#8217;,<br />
&#8230;</p>
<p> <code>XML-RPC Example</code> </p>
<pre>
&gt;&gt;&gt; import xmlrpclib
&gt;&gt;&gt; s = xmlrpclib.ServerProxy('<a rel="nofollow" href="http://localhost:6800/rpc')">http://localhost:6800/rpc')</a>
&gt;&gt;&gt; s.system.listNotifications()
['aria2.onDownloadStart', 'aria2.onDownloadPause', ...
</pre>
</dl>
<h3>Error Handling</h3>
<p> Over JSON-RPC, aria2 returns a JSON object which contains an error code in <code>code</code> and the error message in <code>message</code>. </p>
<p> Over XML-RPC, aria2 returns <code>faultCode=1</code> and the error message in <code>faultString</code>.</p>
<h3>Options</h3>
<p> The same options as for <i>&#8211;input-file</i> are available. See the <i>Input File</i> subsection for a complete list of options. </p>
<p> In the option struct, the name element is the option name (without the preceding <code>&#8212;</code>) and the value element is the argument as a string.</p>
<h3>JSON-RPC Example</h3>
<pre>
{'split':'1', 'http-proxy':'<a rel="nofollow" href="http://proxy/'}">http://proxy/'}</a>
</pre>
<h3>XML-RPC Example</h3>
<pre>
&lt;struct&gt;
  &lt;member&gt;
    &lt;name&gt;split&lt;/name&gt;
    &lt;value&gt;&lt;string&gt;1&lt;/string&gt;&lt;/value&gt;
  &lt;/member&gt;
  &lt;member&gt;
    &lt;name&gt;http-proxy&lt;/name&gt;
    &lt;value&gt;&lt;string&gt;<a rel="nofollow" href="http://proxy/">http://proxy/</a>&lt;/string&gt;&lt;/value&gt;
  &lt;/member&gt;
&lt;/struct&gt;
</pre>
<p> The <i>header</i> and <i>index-out</i> options are allowed multiple times on the command-line. Since the name should be unique in a struct (many XML-RPC library implementations use a hash or dict for struct), a single string is not enough. To overcome this limitation, you may use an array as the value as well as a string.</p>
<h3>JSON-RPC Example</h3>
<p>{<br />
    &#8216;header&#8217; : [ &#8216;Accept-Language: ja&#8217;, &#8216;Accept-Charset: utf-8&#8217; ]<br />
}</p>
<h3>XML-RPC Example</h3>
<pre>
&lt;struct&gt;
  &lt;member&gt;
    &lt;name&gt;header&lt;/name&gt;
    &lt;value&gt;
      &lt;array&gt;
        &lt;data&gt;
          &lt;value&gt;&lt;string&gt;Accept-Language: ja&lt;/string&gt;&lt;/value&gt;
          &lt;value&gt;&lt;string&gt;Accept-Charset: utf-8&lt;/string&gt;&lt;/value&gt;
        &lt;/data&gt;
      &lt;/array&gt;
    &lt;/value&gt;
  &lt;/member&gt;
&lt;/struct&gt;
</pre>
<p> The following example adds a download with two options: <code>dir</code> and <code>header</code>. The <code>header</code> option requires two values, so it uses a list: </p>
<p>&gt;&gt;&gt; import xmlrpclib &gt;&gt;&gt; s = xmlrpclib.ServerProxy(&#8216;http://localhost:6800/rpc&#8217;) &gt;&gt;&gt; opts = dict(dir = &#8216;/tmp&#8217;,<br />
                                                                                                &#8230; header = [ &#8216;Accept-Language: ja&#8217;,<br />
                                                                                                               &#8230; &#8216;Accept-Charset: utf-8&#8217; ]) &gt;&gt;&gt;<br />
                                                                                           s.aria2.addUri([&#8216;http://example.org/file&#8217;], opts) &#8216;1&#8217;</p>
<h3>JSON-RPC using HTTP GET</h3>
<p> The JSON-RPC interface also supports requests via HTTP GET. The encoding scheme in GET parameters is based on JSON-RPC over HTTP Specification [2008-1-15(RC1)]. The encoding of GET parameters are follows: </p>
<pre>
/jsonrpc?method=METHOD_NAME&amp;id=ID&amp;params=BASE64_ENCODED_PARAMS
</pre>
<p> The <code>method</code> and <code>id</code> are always treated as JSON string and their encoding must be UTF-8. </p>
<p> For example, The encoded string of <code>aria2.tellStatus(&#8216;2089b05ecca3d829&#8217;)</code> with <code>id=&#8217;foo&#8217;</code> looks like this: </p>
<pre>
/jsonrpc?method=aria2.tellStatus&amp;id=foo&amp;params=WyIyMDg5YjA1ZWNjYTNkODI5Il0%3D
</pre>
<p> The <code>params</code> parameter is Base64-encoded JSON array which usually appears in <code>params</code> attribute in JSON-RPC request object. In the above example, the params is <code>[&quot;2089b05ecca3d829&quot;]</code>, therefore: </p>
<p>[&#8220;2089b05ecca3d829&#8221;]&#8211;(Base64)&#8211; &gt; WyIyMDg5YjA1ZWNjYTNkODI5Il0 =<br />
    &#8211;(Percent Encode)&#8211; &gt; WyIyMDg5YjA1ZWNjYTNkODI5Il0 % 3D</p>
<p> The JSON-RPC interface also supports JSONP. You can specify the callback function in the <code>jsoncallback</code> parameter: </p>
<pre>
/jsonrpc?method=aria2.tellStatus&amp;id=foo&amp;params=WyIyMDg5YjA1ZWNjYTNkODI5Il0%3D&amp;jsoncallback=cb
</pre>
<p> For Batch requests, the <code>method</code> and <code>id</code> parameters must not be specified. The whole request must be specified in the <code>params</code> parameter. For example, a Batch request: </p>
<p>[{&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;qwer&#8217;, &#8216;method&#8217; : &#8216;aria2.getVersion&#8217;},<br />
 {&#8216;jsonrpc&#8217; : &#8216;2.0&#8217;, &#8216;id&#8217; : &#8216;asdf&#8217;, &#8216;method&#8217; : &#8216;aria2.tellActive&#8217;}]</p>
<p> must be encoded like this: </p>
<pre>
/jsonrpc?params=W3sianNvbnJwYyI6ICIyLjAiLCAiaWQiOiAicXdlciIsICJtZXRob2QiOiAiYXJpYTIuZ2V0VmVyc2lvbiJ9LCB7Impzb25ycGMiOiAiMi4wIiwgImlkIjogImFzZGYiLCAibWV0aG9kIjogImFyaWEyLnRlbGxBY3RpdmUifV0%3D
</pre>
<h3>JSON-RPC over WebSocket</h3>
<p> JSON-RPC over WebSocket uses same method signatures and response format as JSON-RPC over HTTP. The supported WebSocket version is 13 which is detailed in <i>RFC 6455</i>. </p>
<p> To send a RPC request to the RPC server, send a serialized JSON string in a Text frame. The response from the RPC server is delivered also in a Text frame.</p>
<h3>Notifications</h3>
<p> The RPC server might send notifications to the client. Notifications is unidirectional, therefore the client which receives the notification must not respond to it. The method signature of a notification is much like a normal method request but lacks the id key. The value of the params key is the data which this notification carries. The format of the value varies depending on the notification method. Following notification methods are defined.</p>
<dl>
<dt><code>aria2.onDownloadStart(event)</code></p>
<dd> This notification will be sent when a download is started. The <i>event</i> is of type struct and it contains following keys. The value type is string.</p>
<dt><code>gid</code></p>
<dd> GID of the download.</p>
<dt><code>aria2.onDownloadPause(event)</code></p>
<dd> This notification will be sent when a download is paused. The <i>event</i> is the same struct as the <i>event</i> argument of <i>aria2.onDownloadStart()</i> method.</p>
<dt><code>aria2.onDownloadStop(event)</code></p>
<dd> This notification will be sent when a download is stopped by the user. The <i>event</i> is the same struct as the <i>event</i> argument of <i>aria2.onDownloadStart()</i> method.</p>
<dt><code>aria2.onDownloadComplete(event)</code></p>
<dd> This notification will be sent when a download is complete. For BitTorrent downloads, this notification is sent when the download is complete and seeding is over. The <i>event</i> is the same struct of the <i>event</i> argument of <i>aria2.onDownloadStart()</i> method.</p>
<dt><code>aria2.onDownloadError(event)</code></p>
<dd> This notification will be sent when a download is stopped due to an error. The <i>event</i> is the same struct as the <i>event</i> argument of <i>aria2.onDownloadStart()</i> method.</p>
<dt><code>aria2.onBtDownloadComplete(event)</code></p>
<dd> This notification will be sent when a torrent download is complete but seeding is still going on. The <i>event</i> is the same struct as the <i>event</i> argument of <i>aria2.onDownloadStart()</i> method.</dl>
<h3>Sample XML-RPC Client Code</h3>
<p> The following Ruby script adds <code><a rel="nofollow" href="http://localhost/aria2.tar.bz2">http://localhost/aria2.tar.bz2</a></code> to aria2c (running on localhost) with option <i>&#8211;dir=/downloads</i> and prints the RPC response: </p>
<p>#!/ usr / bin / env ruby<br />
require &#8216;xmlrpc/client&#8217; require &#8216;pp&#8217; client = XMLRPC::Client.new2(&#8220;http://localhost:6800/rpc&#8221;)<br />
                                                  options = {&#8220;dir&#8221; = &gt; &#8220;/downloads&#8221;} result = client.call(&#8220;aria2.addUri&#8221;, [&#8220;http://localhost/aria2.tar.bz2&#8221;], options)<br />
                                                                                                  pp result</p>
<p> If you are a Python lover, you can use xmlrpclib (Python3 uses xmlrpc.client instead) to interact with aria2: </p>
<p>import xmlrpclib from pprint import pprint s = xmlrpclib.ServerProxy(&#8220;http://localhost:6800/rpc&#8221;)<br />
                                                                         r = s.aria2.addUri([&#8220;http://localhost/aria2.tar.bz2&#8221;], {&#8220;dir&#8221; : &#8220;/downloads&#8221; })<br />
                                                                                                pprint(r)</p>
<h2>MISC</h2>
<h3>Console Readout</h3>
<p> While downloading files, aria2 prints a readout to the console to show the progress of the downloads. The console readout looks like this: </p>
<pre>
[#2089b0 400.0KiB/33.2MiB(1%) CN:1 DL:115.7KiB ETA:4m51s]
</pre>
<p> This section describes what these numbers and strings mean.</p>
<dl>
<dt><code>#NNNNNN</code></p>
<dd> The first 6 characters of the GID as a hex string. The GID is an unique ID for each download, internal to aria2. The GID is particularly useful when interacting with aria2 using the RPC interface.</p>
<dt><code>X/Y(Z%)</code></p>
<dd> Completed length, the total file length and its progress. If <i>&#8211;select-file</i> is used, this is the sum of selected files.</p>
<dt><code>SEED</code></p>
<dd> Share ratio when the aria2 is seeding a finished torrent.</p>
<dt><code>CN</code></p>
<dd> The number of connections aria2 has established.</p>
<dt><code>SD</code></p>
<dd> The number of seeders aria2 is connected to.</p>
<dt><code>DL</code></p>
<dd> Download speed (bytes per second).</p>
<dt><code>UL</code></p>
<dd> Upload speed (bytes per second) and the number of uploaded bytes.</p>
<dt><code>ETA</code></p>
<dd> Expected time to finish the download. </p>
<p> When more than one download is in progress, some of the information described above will be omitted in order to show information for several downloads. And the overall download and upload speeds are shown at the beginning of the line. </p>
<p> When aria2 is allocating file space or validating checksums, it additionally prints the progress of these operations:</p>
<dt><code>FileAlloc</code></p>
<dd> GID, already allocated length and total length in bytes.</p>
<dt><code>Checksum</code></p>
<dd> GID, already validated length and total length in bytes.</dl>
<h2>EXAMPLE</h2>
<h3>HTTP/FTP Segmented Downloads</h3>
<h3>Download a file</h3>
<pre>
$ aria2c &quot;<a rel="nofollow" href="http://host/file.zip">http://host/file.zip</a>&quot;
</pre>
<p> <code>NOTE:</code> To stop a download, press <code>Ctrl-C</code>. You can resume the transfer by running aria2c with the same argument in the same directory. You can change URIs as long as they are pointing to the same file.</p>
<h3>Download a file from two different HTTP servers</h3>
<pre>
$ aria2c &quot;<a rel="nofollow" href="http://host/file.zip">http://host/file.zip</a>&quot; &quot;<a rel="nofollow" href="http://mirror/file.zip">http://mirror/file.zip</a>&quot;
</pre>
<h3>Download a file from one host using multiple connections</h3>
<pre>
$ aria2c -x2 -k1M &quot;<a rel="nofollow" href="http://host/file.zip">http://host/file.zip</a>&quot;
</pre>
<p> <code>NOTE:</code> The -x option specified the number of allowed connections, while the -k option specified the size of chunks.</p>
<h3>Download a file from HTTP and FTP servers at the same time</h3>
<pre>
$ aria2c &quot;<a rel="nofollow" href="http://host1/file.zip">http://host1/file.zip</a>&quot; &quot;<a href="ftp://host2/file.zip">ftp://host2/file.zip</a>&quot;
</pre>
<h3>Download files listed in a text file concurrently</h3>
<pre>
$ aria2c -ifiles.txt -j2
</pre>
<p> <code>NOTE:</code> -j option specifies the number of parallel downloads.</p>
<h3>Using a proxy</h3>
<p> For HTTP: </p>
<pre>
$ aria2c --http-proxy=&quot;<a rel="nofollow" href="http://proxy:8080">http://proxy:8080</a>&quot; &quot;<a rel="nofollow" href="http://host/file">http://host/file</a>&quot;
</pre>
<pre>
$ aria2c --http-proxy=&quot;<a rel="nofollow" href="http://proxy:8080">http://proxy:8080</a>&quot; --no-proxy=&quot;localhost,127.0.0.1,192.168.0.0/16&quot; &quot;<a rel="nofollow" href="http://host/file">http://host/file</a>&quot;
</pre>
<p> For FTP: </p>
<pre>
$ aria2c --ftp-proxy=&quot;<a rel="nofollow" href="http://proxy:8080">http://proxy:8080</a>&quot; &quot;<a href="ftp://host/file">ftp://host/file</a>&quot;
</pre>
<p> <code>NOTE:</code> See <i>&#8211;http-proxy</i>, <i>&#8211;https-proxy</i>, <i>&#8211;ftp-proxy</i>, <i>&#8211;all-proxy</i> and <i>&#8211;no-proxy</i> for details. You can specify proxy in the environment variables. See <i>ENVIRONMENT</i> section.</p>
<h3>Using a Proxy with authorization</h3>
<pre>
$ aria2c --http-proxy=&quot;<a rel="nofollow" href="http://username:password@proxy:8080">http://username:password@proxy:8080</a>&quot; &quot;<a rel="nofollow" href="http://host/file">http://host/file</a>&quot;
</pre>
<pre>
$ aria2c --http-proxy=&quot;<a rel="nofollow" href="http://proxy:8080">http://proxy:8080</a>&quot; --http-proxy-user=&quot;username&quot; --http-proxy-passwd=&quot;password&quot; &quot;<a rel="nofollow" href="http://host/file">http://host/file</a>&quot;
</pre>
<h3>Metalink Download</h3>
<h3>Download files with remote Metalink</h3>
<pre>
$ aria2c --follow-metalink=mem &quot;<a rel="nofollow" href="http://host/file.metalink">http://host/file.metalink</a>&quot;
</pre>
<h3>Download using a local metalink file</h3>
<pre>
$ aria2c -p --lowest-speed-limit=4000 file.metalink
</pre>
<p> <code>NOTE:</code> To stop a download, press <code>Ctrl-C</code>. You can resume the transfer by running aria2c with the same argument in the same directory.</p>
<h3>Download several local metalink files</h3>
<pre>
$ aria2c -j2 file1.metalink file2.metalink
</pre>
<h3>Download only selected files</h3>
<pre>
$ aria2c --select-file=1-4,8 file.metalink
</pre>
<p> <code>NOTE:</code> The index is printed to the console using -S option.</p>
<h3>Download a file using a local metalink file with user preference</h3>
<pre>
$ aria2c --metalink-location=jp,us --metalink-version=1.1 --metalink-language=en-US file.metalink
</pre>
<h3>BitTorrent Download</h3>
<h3>Download files using a remote BitTorrent file</h3>
<pre>
$ aria2c --follow-torrent=mem &quot;<a rel="nofollow" href="http://host/file.torrent">http://host/file.torrent</a>&quot;
</pre>
<h3>Download using a local torrent file</h3>
<pre>
$ aria2c --max-upload-limit=40K file.torrent
</pre>
<p> <code>NOTE:</code> &#8211;max-upload-limit specifies the max of upload rate. </p>
<p> <code>NOTE:</code> To stop a download, press <code>Ctrl-C</code>. You can resume the transfer later by running aria2c with the same argument in the same directory.</p>
<h3>Download using BitTorrent Magnet URI</h3>
<pre>
$ aria2c &quot;magnet:?xt=urn:btih:248D0A1CD08284299DE78D5C1ED359BB46717D8C&amp;dn=aria2&quot;
</pre>
<p> <code>NOTE:</code> Don&#8217;t forget to quote BitTorrent Magnet URIs which include <code>&amp;</code> characters with single(<code>&#8216;</code>) or double(<code>&quot;</code>) quotes when specifying URIs on the command-line.</p>
<h3>Download 2 torrents</h3>
<pre>
$ aria2c -j2 file1.torrent file2.torrent
</pre>
<h3>Download a file via torrent and HTTP/FTP server in parallel</h3>
<pre>
$ aria2c -Ttest.torrent &quot;<a rel="nofollow" href="http://host1/file">http://host1/file</a>&quot; &quot;<a href="ftp://host2/file">ftp://host2/file</a>&quot;
</pre>
<h3>Only download specific files (usually called selected download)</h3>
<pre>
$ aria2c --select-file=1-4,8 file.torrent
</pre>
<p> <code>NOTE:</code> The index is printed to the console using -S option.</p>
<h3>Download a .torrent file, but do not download the torrent</h3>
<pre>
$ aria2c --follow-torrent=false &quot;<a rel="nofollow" href="http://host/file.torrent">http://host/file.torrent</a>&quot;
</pre>
<h3>Specify the output file name</h3>
<p> To specify the output file name for BitTorrent downloads, you need to know the index of file in the torrent (see <i>&#8211;show-files</i>). For example, the output looks like this: </p>
<p>idx | path / length == = += == == == == == == == == == == =<br />
                                                              1 | dist / base &#8211; 2.6.18.iso | 99.9MiB &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;2 | dist / driver &#8211; 2.6.18.iso | 169.0MiB &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;</p>
<p> To save &#8216;dist/base-2.6.18.iso&#8217; in &#8216;/tmp/mydir/base.iso&#8217; and &#8216;dist/driver-2.6.18.iso&#8217; in &#8216;/tmp/dir/driver.iso&#8217;, use the following command: </p>
<pre>
$ aria2c --dir=/tmp --index-out=1=mydir/base.iso --index-out=2=dir/driver.iso file.torrent
</pre>
<h3>Change the listening ports for incoming peer connections</h3>
<pre>
$ aria2c --listen-port=7000-7001,8000 file.torrent
</pre>
<p> <code>NOTE:</code> Since aria2 doesn&#8217;t configure firewalls or routers for port forwarding, it&#8217;s up to you to do so manually.</p>
<h3>Specify conditions to stop seeding after torrent downloads finish</h3>
<pre>
$ aria2c --seed-time=120 --seed-ratio=1.0 file.torrent
</pre>
<p> <code>NOTE:</code> In the above example, the program stops seeding after 120 minutes since download completed or seed ratio reaches 1.0.</p>
<h3>Throttle upload speed</h3>
<pre>
$ aria2c --max-upload-limit=100K file.torrent
</pre>
<h3>Enable IPv4 DHT</h3>
<pre>
$ aria2c --enable-dht --dht-listen-port=6881 file.torrent
</pre>
<p> <code>NOTE:</code> DHT uses UDP. Since aria2 doesn&#8217;t configure firewalls or routers for port forwarding, it&#8217;s up to you to do it manually.</p>
<h3>Enable IPv6 DHT</h3>
<pre>
$ aria2c --enable-dht6 --dht-listen-port=6881 --dht-listen-addr6=YOUR_GLOBAL_UNICAST_IPV6_ADDR
</pre>
<p> <code>NOTE:</code> aria2 uses the same ports as IPv4 for IPv6.</p>
<h3>Add and remove tracker URIs</h3>
<p> Ignore all tracker announce URIs defined in file.torrent and use <code><a rel="nofollow" href="http://tracker1/announce">http://tracker1/announce</a></code> and <code><a rel="nofollow" href="http://tracker2/announce">http://tracker2/announce</a></code> instead: </p>
<pre>
$ aria2c --bt-exclude-tracker=&quot;*&quot; --bt-tracker=&quot;<a rel="nofollow" href="http://tracker1/announce,http://tracker2/announce">http://tracker1/announce,http://tracker2/announce</a>&quot; file.torrent
</pre>
<h3>More advanced HTTP features</h3>
<h3>Load cookies</h3>
<pre>
$ aria2c --load-cookies=cookies.txt &quot;<a rel="nofollow" href="http://host/file.zip">http://host/file.zip</a>&quot;
</pre>
<p> <code>NOTE:</code> You can use Firefox/Mozilla/Chromium&#8217;s cookie files without modification.</p>
<h3>Resume download started by web browsers or other programs</h3>
<pre>
$ aria2c -c -s2 &quot;<a rel="nofollow" href="http://host/partiallydownloadedfile.zip">http://host/partiallydownloadedfile.zip</a>&quot;
</pre>
<p> <code>NOTE:</code> This will only work when the initial download was not multi-segmented.</p>
<h3>Client certificate authorization for SSL/TLS</h3>
<p> Specify a PKCS12 file as follows: </p>
<pre>
$ aria2c --certificate=/path/to/mycert.p12
</pre>
<p> <code>NOTE:</code> The file specified in <i>&#8211;certificate</i> must be contain one PKCS12 encoded certificate and key. The password must be blank. </p>
<p> Alternatively, if PEM files are supported, use a command like the following: </p>
<pre>
$ aria2c --certificate=/path/to/mycert.pem --private-key=/path/to/mykey.pem <a rel="nofollow" href="https://host/file">https://host/file</a>
</pre>
<p> <code>NOTE:</code> The file specified in <i>&#8211;private-key</i> must be decrypted. The behavior when encrypted one is given is undefined.</p>
<h3>Verify SSL/TLS servers using given CA certificates</h3>
<pre>
$ aria2c --ca-certificate=/path/to/ca-certificates.crt --check-certificate <a rel="nofollow" href="https://host/file">https://host/file</a>
</pre>
<p> <code>NOTE:</code> This option is only available when aria2 was compiled against GnuTLS or OpenSSL. WinTLS and AppleTLS will always use the system certificate store. Instead of <code>`&#8211;ca-certificate</code> install the certificate in that store.</p>
<h3>RPC</h3>
<h3>Encrypt RPC traffic with SSL/TLS</h3>
<p> Specify a server PKC12 file: </p>
<pre>
$ aria2c --enable-rpc --rpc-certificate=/path/to/server.p12 --rpc-secure
</pre>
<p> <code>NOTE:</code> The file specified in <i>&#8211;rpc-certificate</i> must be contain one PKCS12 encoded certificate and key. The password must be blank. </p>
<p> Alternatively, when PEM files are supported (GnuTLS and OpenSSL), specify the server certificate file and private key file as follows: </p>
<pre><code>
$ aria2c-- enable - rpc-- rpc - certificate = / path / to / server.crt-- rpc - private - key = / path / to / server.key-- rpc - secure
</code></pre>
<h3>And more advanced features</h3>
<h3>Throttle the download speed</h3>
<p> Per-download: </p>
<pre>
$ aria2c --max-download-limit=100K file.metalink
</pre>
<p> Overall: </p>
<pre>
$ aria2c --max-overall-download-limit=100K file.metalink
</pre>
<h3>Repair a damaged download</h3>
<pre>
$ aria2c -V file.metalink
</pre>
<p> <code>NOTE:</code> Repairing damaged downloads can be done efficiently when used with BitTorrent or Metalink with chunk checksums.</p>
<h3>Drop connections if download speed is lower than a specified limit</h3>
<pre>
$ aria2c --lowest-speed-limit=10K file.metalink
</pre>
<h3>Parameterized URI support</h3>
<p> You can specify set of parts: </p>
<pre>
$ aria2c -P &quot;<a rel="nofollow" href="http://{host1,host2,host3}/file.iso">http://{host1,host2,host3}/file.iso</a>&quot;
</pre>
<p> You can specify numeric sequence: </p>
<pre>
$ aria2c -Z -P &quot;<a rel="nofollow" href="http://host/image[000-100].png">http://host/image[000-100].png</a>&quot;
</pre>
<p> <code>NOTE:</code> The -Z option is required if the URIs don&#8217;t point to the same file, such as in the above example. </p>
<p> You can specify step counter: </p>
<pre>
$ aria2c -Z -P &quot;<a rel="nofollow" href="http://host/image[A-Z:2].png">http://host/image[A-Z:2].png</a>&quot;
</pre>
<h3>Verifying checksums</h3>
<pre>
$ aria2c --checksum=sha-1=0192ba11326fe2298c8cb4de616f4d4140213837 <a rel="nofollow" href="http://example.org/file">http://example.org/file</a>
</pre>
<h3>Parallel downloads of an arbitrary number of URIs, metalink, torrent</h3>
<pre>
$ aria2c -j3 -Z &quot;<a rel="nofollow" href="http://host/file1">http://host/file1</a>&quot; file2.torrent file3.metalink
</pre>
<h3>BitTorrent Encryption</h3>
<p> Encrypt the whole payload using ARC4 (obfuscation): </p>
<pre>
$ aria2c --bt-min-crypto-level=arc4 --bt-require-crypto=true file.torrent
</pre>
<h2>SEE ALSO</h2>
<p> Project Web Site: <i><a rel="nofollow" href="https://aria2.github.io/">https://aria2.github.io/</a></i> </p>
<p> Metalink Homepage: <i><a rel="nofollow" href="http://www.metalinker.org/">http://www.metalinker.org/</a></i> </p>
<p> The Metalink Download Description Format: <i>RFC 5854</i></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2006, 2015 Tatsuhiro Tsujikawa </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA </p>
<p> In addition, as a special exception, the copyright holders give permission to link the code of portions of this program with the OpenSSL library under certain conditions as described in each individual source file, and distribute linked combinations including the two. You must obey the GNU General Public License in all respects for all of the code used other than OpenSSL. If you modify file(s) with this exception, you may extend this exception to your version of the file(s), but you are not obligated to do so. If you do not wish to do so, delete this exception statement from your version. If you delete this exception statement from all source files in the program, then also delete it here. </p>
<h2>Index</h2>
