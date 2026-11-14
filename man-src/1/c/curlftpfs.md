---
title: "curlftpfs(1)"
name: "curlftpfs"
section: "1"
letter: "c"
url: "/docs/linux/man/1-curlftpfs/"
description: "curlftpfs – mount a ftp host as a local directory"
---

<h2 class="name">NAME</h2>
<p> curlftpfs &#8211; mount a ftp host as a local directory </p>
<h2>SYNOPSIS</h2>
<p> <code>curlftpfs [options]</code> <i>host path</i></p>
<h2>DESCRIPTION</h2>
<p> The program <code>curlftpfs</code> is a tool to mount remote ftp hosts as local directories. It connects to the <i>host</i> FTP server and maps its directory structure to the <i>path</i> directory. </p>
<p> curlftpfs is powered by libcurl for all transfer-related features. See <code><a href="/docs/linux/man/3-libcurl/">libcurl</a></code>(3) for details. The filesystem part is implemented on top of FUSE. See <code><a rel="nofollow" href="http://fuse.sourceforge.net/">http://fuse.sourceforge.net/</a></code> for details.</p>
<h2>FTP OPTIONS</h2>
<dl>
<dt><code>-h/&#8211;help</code></p>
<dd> Print help options.</p>
<dt><code>-v/&#8211;verbose</code></p>
<dd> Make libcurl print verbose debug output.</p>
<dt><code>-V/&#8211;version</code></p>
<dd> Print curlftpfs, libcurl and fuse versions.</p>
<dt><code>-o</code></p>
<dd> Options are specified with a <code>-o</code> flag followed by a comma separated string of options.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cacert=&lt;file&gt;</code></p>
<dd> (SSL) Pass a string naming a file holding one or more certificates to verify the peer with. </p>
<p> Note that option is by default set to the system path where libcurl&#8217;s cacert bundle is assumed to be stored, as established at build time.</p>
<dt><code>capath=&lt;directory&gt;</code></p>
<dd> (SSL) Tells curlftpfs to use the specified certificate directory to verify the peer. The certificates must be in PEM format, and the directory must have been processed using the c_rehash utility supplied with openssl. Using <code>capath</code> can allow curlftpfs to make connections much more efficiently than using <code>cacert</code> if the <code>cacert</code> file contains many CA certificates.</p>
<dt><code>cert=&lt;certificate&gt;</code></p>
<dd> (SSL) Tells curlftpfs to use the specified certificate file. The default format is &quot;PEM&quot; and can be changed with <code>cert_type</code>.</p>
<dt><code>cert_type=&lt;type&gt;</code></p>
<dd> (SSL) Tells curlftpfs what certificate type the provided certificate is in. PEM, DER and ENG are recognized types.</p>
<dt><code>ciphers=&lt;list of ciphers&gt;</code></p>
<dd> (SSL) Specifies which ciphers to use in the connection. The list must be syntactically correct, it consists of one or more cipher strings separated by colons. Commas or spaces are also acceptable separators but colons are normally used, , &#8211; and + can be used as operators. Valid examples of cipher lists include &#8216;RC4-SHA&#8217;, &#8216;SHA1+DES&#8217;, &#8216;TLSv1&#8217; and &#8216;DEFAULT&#8217;. The default list is normally set when you compile OpenSSL. </p>
<p> Read up on SSL cipher list details on this URL: <i><a rel="nofollow" href="http://www.openssl.org/docs/apps/ciphers.html">http://www.openssl.org/docs/apps/ciphers.html</a></i></p>
<dt><code>codepage=&lt;name&gt;</code></p>
<dd> Sets the encoding the ftp server uses to encode file names.</p>
<dt><code>connect_timeout=&lt;seconds&gt;</code></p>
<dd> Maximum time in seconds that you allow the connection to the server to take. This only limits the connection phase, once curlftpfs has connected this option is of no more use.</p>
<dt><code>custom_list=&lt;command&gt;</code></p>
<dd> Command used by curlftpfs to list files. The default is &quot;LIST -a&quot; but some servers might require extra options, e.g. &quot;LIST -la&quot;.</p>
<dt><code>disable_eprt</code></p>
<dd> Tell curlftpfs to disable the use of the EPRT and LPRT commands when doing active FTP transfers. Curlftpfs will normally always first attempt to use EPRT, then LPRT before using PORT, but with this option, it will use PORT right away. EPRT and LPRT are extensions to the original FTP protocol, may not work on all servers but enable more functionality in a better way than the traditional PORT command.</p>
<dt><code>disable_epsv</code></p>
<dd> Tell curlftpfs to disable the use of the EPSV command when doing passive FTP transfers. This is the default.</p>
<dt><code>enable_epsv</code></p>
<dd> Tell curlftpfs to enable the use of the EPSV command when doing passive FTP transfers. Curlftpfs will first attempt to use EPSV before PASV.</p>
<dt><code>engine=&lt;name&gt;</code></p>
<dd> Select the OpenSSL crypto engine to use for cipher operations. Use:<br />
 <code>curl &#8211;engine list</code><br />
 to print a list of build-time supported engines. Note that not all (or none) of the engines may be available at run-time.</p>
<dt><code>ftpfs_debug</code></p>
<dd> Make curlftpfs print lots of debug information. Useful only in conjunction with the <code>-d</code> option.</p>
<dt><code>ftp_method=&lt;method&gt;</code></p>
<dd> Control what method curlftpfs should use to reach a file on the server. The method argument should be one of the following alternatives:</p>
<dl>
<dt>
<dd>
<dl>
<dt>multicwd</p>
<dd> curlftpfs does a single CWD operation for each path part in the given URL. For deep hierarchies this means very many commands. This is how RFC1738 says it should be done. This is the default but the slowest behavior.</p>
<dt>singlecwd</p>
<dd> curlftpfs does one CWD with the full target directory and then operates on the file &quot;normally&quot; (like in the multicwd case).</dl>
</dl>
<dt><code>ftp_port=&lt;address&gt;</code></p>
<dd> Reverses the initiator/listener roles when connecting with ftp. This switch makes curlftpfs use the PORT command instead of PASV. In practice, PORT tells the server to connect to the client&#8217;s specified address and port, while PASV asks the server for an ip address and port to connect to. &lt;address&gt; should be one of:</p>
<dl>
<dt>
<dd>
<dl>
<dt>interface</p>
<dd> i.e &quot;eth0&quot; to specify which interface&#8217;s IP address you want to use</p>
<dt>IP address</p>
<dd> i.e &quot;192.168.10.1&quot; to specify exact IP number</p>
<dt>host name</p>
<dd> i.e &quot;my.host.domain&quot; to specify machine</p>
<dt>&#8211;</p>
<dd> make curlftpfs pick the same IP address that is already used for the control connection</dl>
</dl>
<dl>
<dt>
<dd>
<p> Disable the attempt to use the EPRT command instead of PORT by using <i>disable_eprt</i>. EPRT is really PORT++.</dl>
<dt><code>httpproxy</code></p>
<dd> Set the proxy type to HTTP. This is the default type.</p>
<dt><code>interface=&lt;name&gt;</code></p>
<dd> Pass a string as parameter. This set the interface name to use as outgoing network interface. The name can be an interface name, an IP address or a host name.</p>
<dt><code>iocharset=&lt;name&gt;</code></p>
<dd> Sets the charset used by the client side for codepage to charset translation. Default: UTF8.</p>
<dt><code>ipv4</code></p>
<dd> If libcurl is capable of resolving an address to multiple IP versions (which it is if it is ipv6-capable), this option tells libcurl to resolve names to IPv4 addresses only.</p>
<dt><code>ipv6</code></p>
<dd> If libcurl is capable of resolving an address to multiple IP versions (which it is if it is ipv6-capable), this option tells libcurl to resolve names to IPv6 addresses only.</p>
<dt><code>key=&lt;key&gt;</code></p>
<dd> (SSL) Private key file name. Allows you to provide your private key in this separate file. The default format is &quot;PEM&quot; and can be changed with <code>key_type</code>.</p>
<dt><code>key_type=&lt;type&gt;</code></p>
<dd> (SSL) Pass a string in the format of your private key. Supported formats are &quot;PEM&quot;, &quot;DER&quot; and &quot;ENG&quot;. </p>
<p> The format &quot;ENG&quot; enables you to load the private key from a crypto engine. In this case <code>key</code> is used as an identifier passed to the engine. You have to set the crypto engine with <code>engine</code> option. &quot;DER&quot; format key file currently does not work because of a bug in OpenSSL.</p>
<dt><code>krb4=&lt;level&gt;</code></p>
<dd> Enable kerberos4 authentication and use. The level must be entered and should be one of &#8216;clear&#8217;, &#8216;safe&#8217;, &#8216;confidential&#8217; or &#8216;private&#8217;. Should you use a level that is not one of these, &#8216;private&#8217; will instead be used. </p>
<p> This option requires that the libcurl library was built with kerberos4 support. This is not very common.</p>
<dt><code>no_verify_hostname</code></p>
<dd> (SSL) Curlftpfs will not verify the hostname when connecting to a SSL enabled server.</p>
<dt><code>no_verify_peer</code></p>
<dd> (SSL) Curlftpfs will not verify the certificate when connecting to a SSL enabled server.</p>
<dt><code>pass=&lt;password&gt;</code></p>
<dd> (SSL) Pass phrase for the private key.</p>
<dt><code>proxy=&lt;host[:port]&gt;</code></p>
<dd> Use specified HTTP proxy. If the port number is not specified, it is assumed at port 1080. </p>
<p> This option overrides existing environment variables that sets proxy to use. If there&#8217;s an environment variable setting a proxy, you can set proxy to &quot;&quot; to override it. </p>
<p> This options implies the <code>proxytunnel</code> option. </p>
<p> Starting with libcurl version 7.14.1, the proxy host can be specified the exact same way as the proxy environment variables, including protocol prefix (<a rel="nofollow" href="http://)">http://)</a> and embedded user + password.</p>
<dt><code>proxytunnel</code></p>
<dd> Tells curlftpfs to use a tunnel proxy. This option is implied by the <code>proxy</code> option but you need to set it manually if you use the <i>proxy</i> environment variable.</p>
<dt><code>proxy_anyauth</code></p>
<dd> Tells curl to pick a suitable authentication method when communicating with the given proxy. This will cause an extra request/response round-trip.</p>
<dt><code>proxy_basic</code></p>
<dd> Tells curlftpfs to use HTTP Basic authentication when communicating with the given proxy. Basic is the default authentication method curlftpfs is used with proxies.</p>
<dt><code>proxy_digest</code></p>
<dd> Tells curlftpfs to use HTTP Digest authentication when communicating with the given proxy.</p>
<dt><code>proxy_ntlm</code></p>
<dd> Tells curlftpfs to use HTTP NTLM authentication when communicating with the given proxy.</p>
<dt><code>proxy_user=&lt;user:password&gt;</code></p>
<dd> Specify user and password to use for proxy authentication.</p>
<dt><code>skip_pasv_ip</code></p>
<dd> Tell curlftpfs to not use the IP address the server suggests in its response to curlftpfs&#8217;s PASV command when curlftpfs connects the data connection. Instead curlftpfs will re-use the same IP address it already uses for the control connection.</p>
<dt><code>socks4</code></p>
<dd> Set the proxy type to SOCKS4.</p>
<dt><code>socks5</code></p>
<dd> Set the proxy type to SOCKS5.</p>
<dt><code>ssl</code></p>
<dd> Make curlftpfs use SSL/TLS for both control and data connections.</p>
<dt><code>sslv3</code></p>
<dd> Forces curlftpfs to use SSL version 3 when negotiating with a remote SSL server.</p>
<dt><code>ssl_control</code></p>
<dd> Make curlftpfs use SSL/TLS only for the control connection.</p>
<dt><code>ssl_try</code></p>
<dd> Curlftpfs will try to use SSL/TLS for both the control and data connections but if the server doesn&#8217;t support it, it will still connect unencrypted.</p>
<dt><code>tcp_nodelay</code></p>
<dd> Turn on the TCP_NODELAY option. See the <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> man page for details about this option.</p>
<dt><code>tlsv1</code></p>
<dd> (SSL) Forces curlftpfs to use TLS version 1 when negotiating with a remote TLS server.</p>
<dt><code>transform_symlinks</code></p>
<dd> Append <i>path</i> to the absolute symlinks so that they still point inside the ftp directory structure. Otherwise those links will very probably be broken.</p>
<dt><code>user=&lt;user:password&gt;</code></p>
<dd> Specify user and password to use for server authentication. Overrides netrc configuration.</p>
<dt><code>utf8</code></p>
<dd> Try to transfer file list with UTF-8 encoding. Send OPTS UTF8 ON at the beginning of file list transfer.</dl>
</dl>
</dl>
<h2>FUSE OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> Enable FUSE debug output. Implies <code>-f</code>.</p>
<dt><code>-f</code></p>
<dd> Run curlftpfs in foreground mode.</p>
<dt><code>-r</code></p>
<dd> Mount read-only.</p>
<dt><code>-s</code></p>
<dd> Disable multi-threaded operation.</p>
<dt><code>-o</code></p>
<dd> Options are specified with a <code>-o</code> flag followed by a comma separated string of options.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>allow_other</code></p>
<dd> Allow access to other users. By default the mount point is only accessible to the user that mounted it and not even to root.</p>
<dt><code>allow_root</code></p>
<dd> Allow access to root user. By default the mount point is only accessible to the user that mounted it and not even to root.</p>
<dt><code>debug</code></p>
<dd> enable debug output</p>
<dt><code>direct_io</code></p>
<dd> use direct I/O</p>
<dt><code>fsname=NAME</code></p>
<dd> set filesystem name in mtab</p>
<dt><code>gid=N</code></p>
<dd> set file group</p>
<dt><code>hard_remove</code></p>
<dd> immediate removal (don&#8217;t hide files)</p>
<dt><code>kernel_cache</code></p>
<dd> Let the kernel VFS do some caching of the files.</p>
<dt><code>large_read</code></p>
<dd> issue large read requests (2.4 only)</p>
<dt><code>max_read=N</code></p>
<dd> set maximum size of read requests</p>
<dt><code>nonempty</code></p>
<dd> allow mounts over non-empty file/dir</p>
<dt><code>readdir_ino</code></p>
<dd> try to fill in d_ino in readdir</p>
<dt><code>uid=N</code></p>
<dd> set file owner</p>
<dt><code>umask=M</code></p>
<dd> set file permissions (octal)</p>
<dt><code>use_ino</code></p>
<dd> let filesystem set inode numbers</dl>
</dl>
</dl>
<h2>AUTHORS</h2>
<p> Robson Braga Araujo is the author and maintainer of CurlFtpFS.</p>
<h2>WWW</h2>
<p> <a rel="nofollow" href="http://curlftpfs.sourceforge.net">http://curlftpfs.sourceforge.net</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) </p>
<h2>Index</h2>
