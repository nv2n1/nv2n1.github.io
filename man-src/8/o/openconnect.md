---
title: "openconnect(8)"
name: "openconnect"
section: "8"
letter: "o"
url: "/docs/linux/man/8-openconnect/"
description: "openconnect – Connect to Cisco AnyConnect VPN"
---

<p>openconnect &#8211; Connect to Cisco AnyConnect VPN</p>
<h2>Synopsis</h2>
<p>[ <code>&#8211;config </code><i>configfile</i> ] [ <code>-b,&#8211;background</code> ] [ <code>&#8211;pid-file </code><i>pidfile</i> ] [ <code>-c,&#8211;certificate </code><i>cert</i> ] [ <code>-e,&#8211;cert-expire-warning </code><i>days</i> ] [ <code>-k,&#8211;sslkey </code><i>key</i> ] [ <code>-C,&#8211;cookie </code><i>cookie</i> ] [ <code>&#8211;cookie-on-stdin</code> ] [ <code>&#8211;compression </code><i>MODE</i> ] [ <code>-d,&#8211;deflate</code> ] [ <code>-D,&#8211;no-deflate</code> ] [ <code>&#8211;force-dpd </code><i>interval</i> ] [ <code>-g,&#8211;usergroup </code><i>group</i> ] [ <code>-h,&#8211;help</code> ] [ <code>&#8211;http-auth </code><i>methods</i> ] [ <code>-i,&#8211;interface </code><i>ifname</i> ] [ <code>-l,&#8211;syslog</code> ] [ <code>&#8211;timestamp</code> ] [ <code>-U,&#8211;setuid </code><i>user</i> ] [ <code>&#8211;csd-user </code><i>user</i> ] [ <code>-m,&#8211;mtu </code><i>mtu</i> ] [ <code>&#8211;basemtu </code><i>mtu</i> ] [ <code>-p,&#8211;key-password </code><i>pass</i> ] [ <code>-P,&#8211;proxy </code><i>proxyurl</i> ] [ <code>&#8211;proxy-auth </code><i>methods</i> ] [ <code>&#8211;no-proxy</code> ] [ <code>&#8211;libproxy</code> ] [ <code>&#8211;key-password-from-fsid</code> ] [ <code>-q,&#8211;quiet</code> ] [ <code>-Q,&#8211;queue-len </code><i>len</i> ] [ <code>-s,&#8211;script </code><i>vpnc-script</i> ] [ <code>-S,&#8211;script-tun</code> ] [ <code>-u,&#8211;user </code><i>name</i> ] [ <code>-V,&#8211;version</code> ] [ <code>-v,&#8211;verbose</code> ] [ <code>-x,&#8211;xmlconfig </code><i>config</i> ] [ <code>&#8211;authgroup </code><i>group</i> ] [ <code>&#8211;authenticate</code> ] [ <code>&#8211;cookieonly</code> ] [ <code>&#8211;printcookie</code> ] [ <code>&#8211;cafile </code><i>file</i> ] [ <code>&#8211;disable-ipv6</code> ] [ <code>&#8211;dtls-ciphers </code><i>list</i> ] [ <code>&#8211;dtls-local-port </code><i>port</i> ] [ <code>&#8211;dump-http-traffic</code> ] [ <code>&#8211;no-cert-check</code> ] [ <code>&#8211;no-system-trust</code> ] [ <code>&#8211;pfs</code> ] [ <code>&#8211;no-dtls</code> ] [ <code>&#8211;no-http-keepalive</code> ] [ <code>&#8211;no-passwd</code> ] [ <code>&#8211;no-xmlpost</code> ] [ <code>&#8211;non-inter</code> ] [ <code>&#8211;passwd-on-stdin</code> ] [ <code>&#8211;token-mode </code><i>mode</i> ] [ <code>&#8211;token-secret </code><i>{secret</i>[<i>,counter</i>]|@<i>file</i>} ] [ <code>&#8211;reconnect-timeout</code> ] [ <code>&#8211;servercert </code><i>sha1</i> ] [ <code>&#8211;useragent </code><i>string</i> ] [ <code>&#8211;os </code><i>string</i> ] <code>[<a rel="nofollow" href="https://]">https://]</a></code><i>server</i><code>[:</code><i>port</i><code>][/</code><i>group</i><code>]</code> </p>
<h2>Description</h2>
<p>The program <code>openconnect</code> connects to Cisco &quot;AnyConnect&quot; VPN servers, which use standard TLS and DTLS protocols for data transport. The connection happens in two phases. First there is a simple HTTPS connection over which the user authenticates somehow &#8211; by using a certificate, or password or SecurID, etc. Having authenticated, the user is rewarded with an HTTP cookie which can be used to make the real VPN connection. The second phase uses that cookie in an HTTPS <i>CONNECT</i> request, and data packets can be passed over the resulting connection. In auxiliary headers exchanged with the <i>CONNECT</i> request, a Session-ID and Master Secret for a DTLS connection are also exchanged, which allows data transport over UDP to occur. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;config=CONFIGFILE</code></p>
<dd>Read further options from <i>CONFIGFILE</i> before continuing to process options from the command line. The file should contain long-format options as would be accepted on the command line, but without the two leading &#8212; dashes. Empty lines, or lines where the first non-space character is a # character, are ignored. </p>
<p> Any option except the <code>config</code> option may be specified in the file.</p>
<dt><code>-b,&#8211;background</code></p>
<dd>Continue in background after startup</p>
<dt><code>&#8211;pid-file=PIDFILE</code></p>
<dd>Save the pid to <i>PIDFILE</i> when backgrounding</p>
<dt><code>-c,&#8211;certificate=CERT</code></p>
<dd>Use SSL client certificate <i>CERT</i> which may be either a file name or, if OpenConnect has been built with an appropriate version of GnuTLS, a PKCS#11 URL.</p>
<dt><code>-e,&#8211;cert-expire-warning=DAYS</code></p>
<dd>Give a warning when SSL client certificate has <i>DAYS</i> left before expiry</p>
<dt><code>-k,&#8211;sslkey=KEY</code></p>
<dd>Use SSL private key <i>KEY</i> which may be either a file name or, if OpenConnect has been built with an appropriate version of GnuTLS, a PKCS#11 URL.</p>
<dt><code>-C,&#8211;cookie=COOKIE</code></p>
<dd>Use WebVPN cookie. <i>COOKIE</i></p>
<dt><code>&#8211;cookie-on-stdin</code></p>
<dd>Read cookie from standard input.</p>
<dt><code>-d,&#8211;deflate</code></p>
<dd>Enable all compression, including stateful modes. By default, only stateless compression algorithms are enabled.</p>
<dt><code>-D,&#8211;no-deflate</code></p>
<dd>Disable all compression.</p>
<dt><code>&#8211;compression=MODE</code></p>
<dd>Set compression mode, where <i>MODE</i> is one of <i>stateless</i> , <i>none</i> , or <i>all.</i> </p>
<p> By default, only stateless compression algorithms which do not maintain state from one packet to the next (and which can be used on UDP transports) are enabled. By setting the mode to <i>all</i> stateful algorithms (currently only zlib deflate) can be enabled. Or all compression can be disabled by setting the mode to <i>none.</i> </p>
<p> <code>&#8211;force-dpd=INTERVAL</code> Use <i>INTERVAL</i> as minimum Dead Peer Detection interval for CSTP and DTLS, forcing use of DPD even when the server doesn&#8217;t request it.</p>
<dt><code>-g,&#8211;usergroup=GROUP</code></p>
<dd>Use <i>GROUP</i> as login UserGroup</p>
<dt><code>-h,&#8211;help</code></p>
<dd>Display help text</p>
<dt><code>&#8211;http-auth=METHODS</code></p>
<dd>Use only the specified methods for HTTP authentication to a server. By default, only Negotiate, NTLM and Digest authentication are enabled. Basic authentication is also supported but because it is insecure it must be explicitly enabled. The argument is a comma-separated list of methods to be enabled. Note that the order does not matter: OpenConnect will use Negotiate, NTLM, Digest and Basic authentication in that order, if each is enabled, regardless of the order specified in the METHODS string.</p>
<dt><code>-i,&#8211;interface=IFNAME</code></p>
<dd>Use <i>IFNAME</i> for tunnel interface</p>
<dt><code>-l,&#8211;syslog</code></p>
<dd>Use syslog for progress messages</p>
<dt><code>&#8211;timestamp</code></p>
<dd>Prepend a timestamp to each progress message</p>
<dt><code>-U,&#8211;setuid=USER</code></p>
<dd>Drop privileges after connecting, to become user <i>USER</i></p>
<dt><code>&#8211;csd-user=USER</code></p>
<dd>Drop privileges during CSD (Cisco Secure Desktop) script execution.</p>
<dt><code>&#8211;csd-wrapper=SCRIPT</code></p>
<dd>Run <i>SCRIPT</i> instead of the CSD (Cisco Secure Desktop) script.</p>
<dt><code>-m,&#8211;mtu=MTU</code></p>
<dd>Request <i>MTU</i> from server as the MTU of the tunnel.</p>
<dt><code>&#8211;basemtu=MTU</code></p>
<dd>Indicate <i>MTU</i> as the path MTU between client and server on the unencrypted network. Newer servers will automatically calculate the MTU to be used on the tunnel from this value.</p>
<dt><code>-p,&#8211;key-password=PASS</code></p>
<dd>Provide passphrase for certificate file, or SRK (System Root Key) PIN for TPM</p>
<dt><code>-P,&#8211;proxy=PROXYURL</code></p>
<dd>Use HTTP or SOCKS proxy for connection. A username and password can be provided in the given URL, and will be used for authentication. If authentication is required but no credentials are given, GSSAPI and automatic NTLM authentication using Samba&#8217;s ntlm_auth helper tool may be attempted.</p>
<dt><code>&#8211;proxy-auth=METHODS</code></p>
<dd>Use only the specified methods for HTTP authentication to a proxy. By default, only Negotiate, NTLM and Digest authentication are enabled. Basic authentication is also supported but because it is insecure it must be explicitly enabled. The argument is a comma-separated list of methods to be enabled. Note that the order does not matter: OpenConnect will use Negotiate, NTLM, Digest and Basic authentication in that order, if each is enabled, regardless of the order specified in the METHODS string.</p>
<dt><code>&#8211;no-proxy</code></p>
<dd>Disable use of proxy</p>
<dt><code>&#8211;libproxy</code></p>
<dd>Use libproxy to configure proxy automatically (when built with libproxy support)</p>
<dt><code>&#8211;key-password-from-fsid</code></p>
<dd>Passphrase for certificate file is automatically generated from the <i>fsid</i> of the file system on which it is stored. The <i>fsid</i> is obtained from the <code><a href="/docs/linux/man/2-statvfs/">statvfs</a></code>(2) or <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2) system call, depending on the operating system. On a Linux or similar system with GNU coreutils, the <i>fsid</i> used by this option should be equal to the output of the command: stat &#8211;file-system &#8211;printf=%i\n $CERTIFICATE It is not the same as the 128-bit UUID of the file system.</p>
<dt><code>-q,&#8211;quiet</code></p>
<dd>Less output</p>
<dt><code>-Q,&#8211;queue-len=LEN</code></p>
<dd>Set packet queue limit to <i>LEN</i> pkts</p>
<dt><code>-s,&#8211;script=SCRIPT</code></p>
<dd>Invoke <i>SCRIPT</i> to configure the network after connection. Without this, routing and name service are unlikely to work correctly. The script is expected to be compatible with the <code>vpnc-script</code> which is shipped with the &quot;vpnc&quot; VPN client. See <i><a rel="nofollow" href="http://www.infradead.org/openconnect/vpnc-script.html">http://www.infradead.org/openconnect/vpnc-script.html</a></i> for more information. This version of OpenConnect is configured to use <code>/etc/vpnc/vpnc-script</code> by default. </p>
<p> On Windows, a relative directory for the default script will be handled as starting from the directory that the openconnect executable is running from, rather than the current directory. The script will be invoked with the command-based script host <code>cscript.exe</code>.</p>
<dt><code>-S,&#8211;script-tun</code></p>
<dd>Pass traffic to &#8216;script&#8217; program over a UNIX socket, instead of to a kernel tun/tap device. This allows the VPN IP traffic to be handled entirely in userspace, for example by a program which uses lwIP to provide SOCKS access into the VPN.</p>
<dt><code>-u,&#8211;user=NAME</code></p>
<dd>Set login username to <i>NAME</i></p>
<dt><code>-V,&#8211;version</code></p>
<dd>Report version number</p>
<dt><code>-v,&#8211;verbose</code></p>
<dd>More output (may be specified multiple times for additional output)</p>
<dt><code>-x,&#8211;xmlconfig=CONFIG</code></p>
<dd>XML config file</p>
<dt><code>&#8211;authgroup=GROUP</code></p>
<dd>Choose authentication login selection</p>
<dt><code>&#8211;authenticate</code></p>
<dd>Authenticate only, and output the information needed to make the connection a form which can be used to set shell environment variables. When invoked with this option, openconnect will not make the connection, but if successful will output something like the following to stdout: </p>
<pre><code>COOKIE=3311180634 [at] 13561856@1339425499 [at] B315A0E29D16C6FD92EE...</code>
<code>HOST=10.0.0.1</code>
<code>FINGERPRINT=469bb424ec8835944d30bc77c77e8fc1d8e23a42</code></pre>
<p>Thus, you can invoke openconnect as a non-privileged user <i>(with access to the user&#8217;s PKCS#11 tokens, etc.)</i> for authentication, and then invoke openconnect separately to make the actual connection as root: </p>
<pre><code>eval `openconnect --authenticate <a rel="nofollow" href="https://vpnserver.example.com`;">https://vpnserver.example.com`;</a></code>
<code>[ -n $COOKIE ] &amp;&amp; echo $COOKIE |</code>
<code>&nbsp;<wbr>&nbsp;<wbr>sudo openconnect --cookie-on-stdin $HOST --servercert $FINGERPRINT</code></pre>
<dt><code>&#8211;cookieonly</code></p>
<dd>Fetch webvpn cookie only; don&#8217;t connect</p>
<dt><code>&#8211;printcookie</code></p>
<dd>Print webvpn cookie before connecting</p>
<dt><code>&#8211;cafile=FILE</code></p>
<dd>Cert file for server verification</p>
<dt><code>&#8211;disable-ipv6</code></p>
<dd>Do not advertise IPv6 capability to server</p>
<dt><code>&#8211;dtls-ciphers=LIST</code></p>
<dd>Set OpenSSL ciphers to support for DTLS</p>
<dt><code>&#8211;dtls-local-port=PORT</code></p>
<dd>Use <i>PORT</i> as the local port for DTLS datagrams</p>
<dt><code>&#8211;dump-http-traffic</code></p>
<dd>Enable verbose output of all HTTP requests and the bodies of all responses received from the server.</p>
<dt><code>&#8211;no-cert-check</code></p>
<dd>Do not require server SSL certificate to be valid. Checks will still happen and failures will cause a warning message, but the connection will continue anyway. You should not need to use this option &#8211; if your servers have SSL certificates which are not signed by a trusted Certificate Authority, you can still add them (or your private CA) to a local file and use that file with the <code>&#8211;cafile</code> option.</p>
<dt><code>&#8211;no-system-trust</code></p>
<dd>Do not trust the system default certificate authorities. If this option is given, only certificate authorities given with the <code>&#8211;cafile</code> option, if any, will be trusted automatically. </p>
<dt><code>&#8211;pfs</code></p>
<dd>Enforces Perfect Forward Secrecy (PFS). That ensures that if the server&#8217;s long-term key is compromised, any session keys established before the compromise will be unaffected. If this option is provided and the server does not support PFS in the TLS channel the connection will fail. </p>
<p> PFS is available in Cisco ASA releases <a href="/docs/linux/man/2-9-1/">9.1</a>(2) and higher; a suitable cipher suite may need to be manually enabled by the administrator using the <code>ssl encryption</code> setting. </p>
<dt><code>&#8211;no-dtls</code></p>
<dd>Disable DTLS</p>
<dt><code>&#8211;no-http-keepalive</code></p>
<dd>Version 8.2.2.5 of the Cisco ASA software has a bug where it will forget the client&#8217;s SSL certificate when HTTP connections are being re-used for multiple requests. So far, this has only been seen on the initial connection, where the server gives an HTTP/1.0 redirect response with an explicit <code>Connection: Keep-Alive</code> directive. OpenConnect as of v2.22 has an unconditional workaround for this, which is never to obey that directive after an HTTP/1.0 response. </p>
<p> However, Cisco&#8217;s support team has failed to give any competent response to the bug report and we don&#8217;t know under what other circumstances their bug might manifest itself. So this option exists to disable ALL re-use of HTTP sessions and cause a new connection to be made for each request. If your server seems not to be recognising your certificate, try this option. If it makes a difference, please report this information to the <code>openconnect-devel [at] lists.infradead.org</code> mailing list.</p>
<dt><code>&#8211;no-passwd</code></p>
<dd>Never attempt password (or SecurID) authentication.</p>
<dt><code>&#8211;no-xmlpost</code></p>
<dd>Do not attempt to post an XML authentication/configuration request to the server; use the old style GET method which was used by older clients and servers instead. </p>
<p> This option is a temporary safety net, to work around potential compatibility issues with the code which falls back to the old method automatically. It causes OpenConnect to behave more like older versions (4.08 and below) did. If you find that you need to use this option, then you have found a bug in OpenConnect. Please see <a rel="nofollow" href="http://www.infradead.org/openconnect/mail.html">http://www.infradead.org/openconnect/mail.html</a> and report this to the developers.</p>
<dt><code>&#8211;non-inter</code></p>
<dd>Do not expect user input; exit if it is required.</p>
<dt><code>&#8211;passwd-on-stdin</code></p>
<dd>Read password from standard input</p>
<dt><code>&#8211;token-mode=MODE</code></p>
<dd>Enable one-time password generation using the <i>MODE</i> algorithm. <code>&#8211;token-mode=rsa</code> will call libstoken to generate an RSA SecurID tokencode, <code>&#8211;token-mode=totp</code> will call liboath to generate an RFC 6238 time-based password, and <code>&#8211;token-mode=hotp</code> will call liboath to generate an RFC 4226 HMAC-based password. Yubikey tokens which generate OATH codes in hardware are supported with <code>&#8211;token-mode=yubioath</code></p>
<dt><code>&#8211;token-secret={ SECRET[,COUNTER] | @FILENAME }</code></p>
<dd>The secret to use when generating one-time passwords/verification codes. Base 32-encoded TOTP/HOTP secrets can be used by specifying &quot;base32:&quot; at the beginning of the secret, and for HOTP secrets the token counter can be specified following a comma. </p>
<p> RSA SecurID secrets can be specified as an Android/iPhone URI or a raw numeric CTF string (with or without dashes). </p>
<p> For Yubikey OATH the token secret specifies the name of the credential to be used. If not provided, the first OATH credential found on the device will be used. </p>
<p> <i>FILENAME</i>, if specified, can contain any of the above strings. Or, it can contain a SecurID XML (SDTID) seed. </p>
<p> If this option is omitted, and &#8211;token-mode is &quot;rsa&quot;, libstoken will try to use the software token seed saved in <code>~/.stokenrc</code> by the &quot;stoken import&quot; command.</p>
<dt><code>&#8211;reconnect-timeout</code></p>
<dd>Keep reconnect attempts until so much seconds are elapsed. The default timeout is 300 seconds, which means that openconnect can recover VPN connection after a temporary network down time of 300 seconds.</p>
<dt><code>&#8211;servercert=SHA1</code></p>
<dd>Accept server&#8217;s SSL certificate only if its fingerprint matches <i>SHA1</i>.</p>
<dt><code>&#8211;useragent=STRING</code></p>
<dd>Use <i>STRING</i> as &#8216;User-Agent:&#8217; field value in HTTP header. (e.g. &#8211;useragent &#8216;Cisco AnyConnect VPN Agent for Windows 2.2.0133&#8217;)</p>
<dt><code>&#8211;os=STRING</code></p>
<dd>OS type to report to gateway. Recognized values are: <code>linux</code>, <code>linux-64</code>, <code>win</code>, <code>mac-intel</code>, <code>android</code>, <code>apple-ios</code>. Reporting a different OS type may affect the dynamic access policy (DAP) applied to the VPN session. If the gateway requires CSD, it will also cause the corresponding CSD trojan binary to be downloaded, so you may need to use <code>&#8211;csd-wrapper</code> if this code is not executable on the local machine.</dl>
<h2>Signals</h2>
<p>In the data phase of the connection, the following signals are handled:</p>
<dl>
<dt><code>SIGINT</code></p>
<dd>performs a clean shutdown by logging the session off, disconnecting from the gateway, and running the vpnc-script to restore the network configuration.</p>
<dt><code>SIGHUP</code></p>
<dd>disconnects from the gateway and runs the vpnc-script, but does not log the session off; this allows for reconnection later using <code>&#8211;cookie</code>.</p>
<dt><code>SIGUSR2</code></p>
<dd>forces an immediate disconnection and reconnection; this can be used to quickly recover from LAN IP address changes.</p>
<dt><code>SIGTERM</code></p>
<dd>exits immediately without logging off or running vpnc-script.</dl>
<h2>Limitations</h2>
<p>Note that although IPv6 has been tested on all platforms on which <code>openconnect</code> is known to run, it depends on a suitable <code>vpnc-script</code> to configure the network. The standard <code>vpnc-script</code> shipped with vpnc 0.5.3 is not capable of setting up IPv6 routes; the one from <code><a href="git://git.infradead.org/users/dwmw2/vpnc-scripts.git">git://git.infradead.org/users/dwmw2/vpnc-scripts.git</a></code> will be required.</p>
<h2>Authors</h2>
<p>David Woodhouse &lt;dwmw2 [at] infradead.org&gt;</p>
