---
title: "sslsplit(1)"
name: "sslsplit"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sslsplit/"
description: "sslsplit — transparent SSL/TLS interception"
---

<h2>NAME</h2>
<p> sslsplit &#8212; transparent SSL/TLS interception</p>
<h2>SYNOPSIS</h2>
<p> <code>sslsplit</code> [<code>-kCKwWOPZdDgGsrReumjplLSFi</code>] <code>-c</code> <i>pem</i> <i>proxyspecs</i> [&#8230;]<br />
 <code>sslsplit</code> [<code>-kCKwWOPZdDgGsrReumjplLSFi</code>] <code>-c</code> <i>pem</i> <code>-t</code> <i>dir</i> <i>proxyspecs</i> [&#8230;]<br />
 <code>sslsplit</code> [<code>-OPZwWdDgGsrReumjplLSFi</code>] <code>-t</code> <i>dir</i> <i>proxyspecs</i> [&#8230;]<br />
 <code>sslsplit -E</code><br />
 <code>sslsplit -V</code><br />
 <code>sslsplit -h</code> </p>
<h2>DESCRIPTION</h2>
<p> SSLsplit is a tool for man-in-the-middle attacks against SSL/TLS encrypted network connections. It is intended to be useful for network forensics, application security analysis and penetration testing. </p>
<p> SSLsplit is designed to transparently terminate connections that are redirected to it using a network address translation engine. SSLsplit then terminates SSL/TLS and initiates a new SSL/TLS connection to the original destination address, while logging all data transmitted. Besides NAT based operation, SSLsplit also supports static destinations and using the server name indicated by SNI as upstream destination. SSLsplit is purely a transparent proxy and cannot act as a HTTP or SOCKS proxy configured in a browser. See NAT ENGINES and PROXY SPECIFICATIONS below for specifics on the different modes of operation. </p>
<p> SSLsplit supports plain TCP, plain SSL, HTTP and HTTPS connections over both IPv4 and IPv6. SSLsplit fully supports Server Name Indication (SNI) and is able to work with RSA, DSA and ECDSA keys and DHE and ECDHE cipher suites. Depending on the version of OpenSSL, SSLsplit supports SSL 3.0, TLS 1.0, TLS 1.1 and TLS 1.2, and optionally SSL 2.0 as well. </p>
<p> For SSL and HTTPS connections, SSLsplit generates and signs forged X509v3 certificates on-the-fly, mimicking the original server certificate&#8217;s subject DN, subjectAltName extension and other characteristics. SSLsplit has the ability to use existing certificates of which the private key is available, instead of generating forged ones. SSLsplit supports NULL-prefix CN certificates but otherwise does not implement exploits against specific certificate verification vulnerabilities in SSL/TLS stacks. </p>
<p> SSLsplit implements a number of defences against mechanisms which would normally prevent MitM attacks or make them more difficult. SSLsplit can deny OCSP requests in a generic way. For HTTP and HTTPS connections, SSLsplit removes response headers for HPKP in order to prevent public key pinning, for HSTS to allow the user to accept untrusted certificates, and Alternate Protocols to prevent switching to QUIC/SPDY. HTTP compression, encodings and keep-alive are disabled to make the logs more readable. </p>
<p> As an experimental feature, SSLsplit supports STARTTLS and similar mechanisms, where a protocol starts on a plain text TCP connection and is later upgraded to SSL/TLS through protocol-specific means, such as the STARTTLS command in SMTP. SSLsplit supports generic upgrading of TCP connections to SSL. </p>
<p> SSLsplit does not automagically redirect any network traffic. To actually implement an attack, you also need to redirect the traffic to the system running <code>sslsplit</code>. Your options include running <code>sslsplit</code> on a legitimate router, ARP spoofing, ND spoofing, DNS poisoning, deploying a rogue access point (e.g. using hostap mode), physical recabling, malicious VLAN reconfiguration or route injection, /etc/hosts modification and so on.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c </code><i>pemfile</i></p>
<dd> Use CA certificate from <i>pemfile</i> to sign certificates forged on-the-fly. If <i>pemfile</i> also contains the matching CA private key, it is also loaded, otherwise it must be provided with <code>-k</code>. If <i>pemfile</i> also contains Diffie-Hellman group parameters, they are also loaded, otherwise they can be provided with <code>-g</code>. If <code>-t</code> is also given, SSLsplit will only forge a certificate if there is no matching certificate in the provided certificate directory.</p>
<dt><code>-C </code><i>pemfile</i></p>
<dd> Use CA certificates from <i>pemfile</i> as extra certificates in the certificate chain. This is needed if the CA given with <code>-k</code> and <code>-c</code> is a sub-CA, in which case any intermediate CA certificates and the root CA certificate must be included in the certificate chain.</p>
<dt><code>-d</code></p>
<dd> Detach from TTY and run as a daemon, logging error messages to syslog instead of standard error.</p>
<dt><code>-D</code></p>
<dd> Run in debug mode, log lots of debugging information to standard error. This also forces foreground mode and cannot be used with <code>-d</code>.</p>
<dt><code>-e </code><i>engine</i></p>
<dd> Use <i>engine</i> as the default NAT engine for <i>proxyspecs</i> without explicit NAT engine, static destination address or SNI mode. <i>engine</i> can be any of the NAT engines supported by the system, as returned by <code>-E</code>.</p>
<dt><code>-E</code></p>
<dd> List all supported NAT engines available on the system and exit. See NAT ENGINES for a list of NAT engines currently supported by SSLsplit.</p>
<dt><code>-F </code><i>logspec</i></p>
<dd> Log connection content to separate log files with the given path specification (see LOG SPECIFICATIONS below). For each connection, a log file will be written, which will contain both directions of data as transmitted. Information about the connection will be contained in the filename only.</p>
<dt><code>-g </code><i>pemfile</i></p>
<dd> Use Diffie-Hellman group parameters from <i>pemfile</i> for Ephemereal Diffie-Hellman (EDH/DHE) cipher suites. If <code>-g</code> is not given, SSLsplit first tries to load DH parameters from the PEM files given by <code>-K</code>, <code>-k</code> or <code>-c</code>. If no DH parameters are found in the key files, built-in group parameters are automatically used. The <code>-g</code> option is only available if SSLsplit was built against a version of OpenSSL which supports Diffie-Hellman cipher suites.</p>
<dt><code>-G </code><i>curve</i></p>
<dd> Use the named <i>curve</i> for Ephemereal Elliptic Curve Diffie-Hellman (ECDHE) cipher suites. If <code>-G</code> is not given, a default curve (<code>prime256v1</code>) is used automatically. The <code>-G</code> option is only available if SSLsplit was built against a version of OpenSSL which supports Elliptic Curve Diffie-Hellman cipher suites.</p>
<dt><code>-h</code></p>
<dd> Display help on usage and exit.</p>
<dt><code>-i</code></p>
<dd> For each connection, find the local process owning the connection. This makes process information such as pid, owner:group and executable path for connections originating on the same system as SSLsplit available to the connect log and enables the respective <code>-F</code> path specification directives. <code>-i</code> is available on Mac OS X and FreeBSD; support for other platforms has not been implemented yet.</p>
<dt><code>-j </code><i>jaildir</i></p>
<dd> Change the root directory to <i>jaildir</i> using <a href="/docs/linux/man/2-chroot/">chroot</a>(2) after opening files. Note that this has implications for <code>sni</code> <i>proxyspecs</i>. Depending on your operating system, you will need to copy files such as <code>/etc/resolv.conf</code> to <i>jaildir</i> in order for name resolution to work. Using <code>sni</code> proxyspecs depends on name resolution. Some operating systems require special device nodes such as <code>/dev/null</code> to be present within the jail. Check your system&#8217;s documentation for details.</p>
<dt><code>-k </code><i>pemfile</i></p>
<dd> Use CA private key from <i>pemfile</i> to sign certificates forged on-the-fly. If <i>pemfile</i> also contains the matching CA certificate, it is also loaded, otherwise it must be provided with <code>-c</code>. If <i>pemfile</i> also contains Diffie-Hellman group parameters, they are also loaded, otherwise they can be provided with <code>-g</code>. If <code>-t</code> is also given, SSLsplit will only forge a certificate if there is no matching certificate in the provided certificate directory.</p>
<dt><code>-K </code><i>pemfile</i></p>
<dd> Use private key from <i>pemfile</i> for the leaf certificates forged on-the-fly. If <code>-K</code> is not given, SSLsplit will generate a random 1024-bit RSA key.</p>
<dt><code>-l </code><i>logfile</i></p>
<dd> Log connections to <i>logfile</i> in a single line per connection format, including addresses and ports and some HTTP and SSL information, if available. SIGUSR1 will cause <i>logfile</i> to be re-opened.</p>
<dt><code>-L </code><i>logfile</i></p>
<dd> Log connection content to <i>logfile</i>. The content log will contain a parsable log format with transmitted data, prepended with headers identifying the connection and the data length of each logged segment. SIGUSR1 will cause <i>logfile</i> to be re-opened.</p>
<dt><code>-m</code></p>
<dd> When dropping privileges using <code>-u</code>, override the target primary group to be set to <i>group</i>.</p>
<dt><code>-O</code></p>
<dd> Deny all Online Certificate Status Protocol (OCSP) requests on all <i>proxyspecs</i> and for all OCSP servers with an OCSP response of <code>tryLater</code>, causing OCSP clients to temporarily accept even revoked certificates. HTTP requests are being treated as OCSP requests if the method is <code>GET</code> and the URI contains a syntactically valid OCSPRequest ASN.1 structure parsable by OpenSSL, or if the method is <code>POST</code> and the <code>Content-Type</code> is <code>application/ocsp-request</code>. For this to be effective, SSLsplit must be handling traffic destined to the port used by the OCSP server. In particular, SSLsplit must be configured to receive traffic to all ports used by OCSP servers of targetted certificates within the <i>certdir</i> specified by <code>-t</code>.</p>
<dt><code>-p </code><i>pidfile</i></p>
<dd> Write the process ID to <i>pidfile</i> and refuse to run if the <i>pidfile</i> is already in use by another process.</p>
<dt><code>-P</code></p>
<dd> Passthrough SSL/TLS connections which cannot be split instead of dropping them. Connections cannot be split if <code>-c</code> and <code>-k</code> are not given and the site does not match any certificate loaded using <code>-t</code>, or if the connection to the original server gives SSL/TLS errors. Specifically, this happens if the site requests a client certificate. In these situations, passthrough with <code>-P</code> results in uninterrupted service for the clients, while dropping is the more secure alternative if unmonitored connections must be prevented. Passthrough mode currently does not apply to SSL/TLS errors in the connection from the client, since the connection from the client cannot easily be retried. Specifically, <code>-P</code> does not currently work for clients that do not accept forged certificates.</p>
<dt><code>-r </code><i>proto</i></p>
<dd> Force SSL/TLS protocol version on both client and server side to <i>proto</i> by selecting the respective OpenSSL method constructor instead of the default SSLv23_method() which supports all protocol versions. This is useful when analyzing traffic to a server that only supports a specific version of SSL/TLS and does not implement proper protocol negotiation. Depending on build options and the version of OpenSSL that is used, the following values for <i>proto</i> are accepted: <code>ssl2</code>, <code>ssl3</code>, <code>tls10</code>, <code>tls11</code> and <code>tls12</code>. Note that SSL 2.0 support is not built in by default because some servers don&#8217;t handle SSL 2.0 Client Hello messages gracefully.</p>
<dt><code>-R </code><i>proto</i></p>
<dd> Disable the SSL/TLS protocol version <i>proto</i> on both client and server side by disabling the respective protocols in OpenSSL. To disable multiple protocol versions, <code>-R</code> can be given multiple times. If <i>-r</i> is also given, there will be no effect in disabling other protocol versions. Disabling protocol versions is useful when analyzing traffic to a server that does not handle some protocol versions well, or to test behaviour with different protocol versions. Depending on build options and the version of OpenSSL that is used, the following values for <i>proto</i> are accepted: <code>ssl2</code>, <code>ssl3</code>, <code>tls10</code>, <code>tls11</code> and <code>tls12</code>. Note that SSL 2.0 support is not built in by default because some servers don&#8217;t handle SSL 2.0 Client Hello messages gracefully.</p>
<dt><code>-s </code><i>ciphers</i></p>
<dd> Use OpenSSL <i>ciphers</i> specification for both server and client SSL/TLS connections. If <code>-s</code> is not given, a cipher list of <code>ALL:-aNULL</code> is used. Normally, SSL/TLS implementations choose the most secure cipher suites, not the fastest ones. By specifying an appropriate OpenSSL cipher list, the set of cipher suites can be limited to fast algorithms, or <code>eNULL</code> cipher suites can be added. Note that for connections to be successful, the SSLsplit cipher suites must include at least one cipher suite supported by both the client and the server of each connection. See <a href="/docs/linux/man/1-ciphers/">ciphers</a>(1) for details on how to construct OpenSSL cipher lists.</p>
<dt><code>-S </code><i>logdir</i></p>
<dd> Log connection content to separate log files under <i>logdir</i>. For each connection, a log file will be written, which will contain both directions of data as transmitted. Information about the connection will be contained in the filename only.</p>
<dt><code>-t </code><i>certdir</i></p>
<dd> Use private key, certificate and certificate chain from PEM files in <i>certdir</i> for connections to hostnames matching the respective certificates, instead of using certificates forged on-the-fly. A single PEM file must contain a single private key, a single certificate and optionally intermediate and root CA certificates to use as certificate chain. When using <code>-t</code>, SSLsplit will first attempt to use a matching certificate loaded from <i>certdir</i>. If <code>-c</code> and <code>-k</code> are also given, certificates will be forged on-the-fly for sites matching none of the common names in the certificates loaded from <i>certdir</i>. Otherwise, connections matching no certificate will be dropped, or if <code>-P</code> is given, passed through without splitting SSL/TLS.</p>
<dt><code>-u</code></p>
<dd> Drop privileges after opening sockets and files by setting the real, effective and stored user IDs to <i>user</i> and loading the appropriate primary and ancillary groups. If <code>-u</code> is not given, SSLsplit will drop privileges to the stored UID if EUID != UID (setuid bit scenario), or to <code>nobody</code> if running with full <code>root</code> privileges (EUID == UID == 0). Due to an Apple bug, <code>-u</code> cannot be used with <code>pf</code> proxyspecs on Mac OS X.</p>
<dt><code>-V</code></p>
<dd> Display version and compiled features information and exit.</p>
<dt><code>-w </code><i>gendir</i></p>
<dd> Write generated keys and certificates to individual files in <i>gendir</i>. For keys, the key identifier is used as filename, which consists of the SHA-1 hash of the ASN.1 bit string of the public key, as referenced by the subjectKeyIdentifier extension in certificates. For certificates, the SHA-1 fingerprints of the original and the used (forged) certificate are combined to form the filename. Note that only newly generated certificates are written to disk.</p>
<dt><code>-W </code><i>gendir</i></p>
<dd> Same as <code>-w</code>, but also write original certificates and certificates not newly generated, such as those loaded from <code>-t</code>.</p>
<dt><code>-Z</code></p>
<dd> Disable SSL/TLS compression on all connections. This is useful if your limiting factor is CPU, not network bandwidth. The <code>-Z</code> option is only available if SSLsplit was built against a version of OpenSSL which supports disabling compression.</dl>
<h2>PROXY SPECIFICATIONS</h2>
<p> Proxy specifications (<i>proxyspecs</i>) consist of the connection type, listen address and static forward address or address resolution mechanism (NAT engine, SNI DNS lookup): </p>
<p> <code>https</code> <i>listenaddr port</i> [<i>nat-engine</i>|<i>fwdaddr port</i>|<code>sni</code> <i>port</i>]<br />
 <code>ssl</code> <i>listenaddr port</i> [<i>nat-engine</i>|<i>fwdaddr port</i>|<code>sni</code> <i>port</i>]<br />
 <code>http</code> <i>listenaddr port</i> [<i>nat-engine</i>|<i>fwdaddr port</i>]<br />
 <code>tcp</code> <i>listenaddr port</i> [<i>nat-engine</i>|<i>fwdaddr port</i>]<br />
 <code>autossl</code> <i>listenaddr port</i> [<i>nat-engine</i>|<i>fwdaddr port</i>]</p>
<dl>
<dt><code>https</code></p>
<dd> SSL/TLS interception with HTTP protocol decoding, including the removal of HPKP, HSTS and Alternate Protocol response headers.</p>
<dt><code>ssl</code></p>
<dd> SSL/TLS interception without any lower level protocol decoding; decrypted connection content is treated as opaque stream of bytes and not modified.</p>
<dt><code>http</code></p>
<dd> Plain TCP connection without SSL/TLS, with HTTP protocol decoding, including the removal of HPKP, HSTS and Alternate Protocol response headers.</p>
<dt><code>tcp</code></p>
<dd> Plain TCP connection without SSL/TLS and without any lower level protocol decoding; decrypted connection content is treated as opaque stream of bytes and not modified.</p>
<dt><code>autossl</code></p>
<dd> Plain TCP connection until a Client Hello SSL/TLS message appears in the byte stream, then automatic upgrade to SSL/TLS interception. This is generic, protocol-independent STARTTLS support, that may erroneously trigger on byte sequences that look like Client Hello messages even though there was no actual STARTTLS command issued. This is an experimental feature and may in its current state miss some Client Hello messages depending on circumstances. YMMV. Testing and patches highly welcome.</p>
<dt><i>listenaddr port</i></p>
<dd> IPv4 or IPv6 address and port or service name to listen on. This is the address and port where the NAT engine should redirect connections to.</p>
<dt><i>nat-engine</i></p>
<dd> NAT engine to query for determining the original destination address and port of transparently redirected connections. If no engine is given, the default engine is used, unless overridden with <code>-e</code>. When using a NAT engine, <code>sslsplit</code> needs to run on the same system as the NAT rules redirecting the traffic to <code>sslsplit</code>. See NAT ENGINES for a list of supported NAT engines.</p>
<dt><i>fwdaddr port</i></p>
<dd> Static destination address, IPv4 or IPv6, with port or service name. When this is used, connections are forwarded to the given server address and port. If <i>fwdaddr</i> is a hostname, it will be resolved to an IP address.</p>
<dt><code>sni</code> <i>port</i></p>
<dd> Use the Server Name Indication (SNI) hostname sent by the client in the Client Hello SSL/TLS message to determine the IP address of the server to connect to. This only works for <code>ssl</code> and <code>https</code> <i>proxyspecs</i> and needs a port or service name as an argument. Because this requires DNS lookups, it is preferrable to use NAT engine lookups (see above), except when that is not possible, such as when there is no supported NAT engine or when running <code>sslsplit</code> on a different system than the NAT rules redirecting the actual connections. Note that when using <code>-j</code> with <code>sni</code>, you may need to prepare <i>jaildir</i> to make name resolution work from within the chroot directory.</dl>
<h2>SIGNALS</h2>
<p> A running <code>sslsplit</code> accepts SIGINT and SIGQUIT for a clean shutdown and SIGUSR1 to re-open the long-living log files (<code>-l</code> and <code>-L</code>). Per-connection log files (<code>-S</code> and <code>-F</code>) are not re-opened because their filename is specific to the connection.</p>
<h2>LOG SPECIFICATIONS</h2>
<p> Log specifications are composed of zero or more printf-style directives; ordinary characters are included directly in the output path. SSLsplit current supports the following directives:</p>
<dl>
<dt><i>%T</i></p>
<dd> The initial connection time as an ISO 8601 UTC timestamp.</p>
<dt><i>%d</i></p>
<dd> The destination host and port, separated by a comma, IPv6 addresses using underscore instead of colon.</p>
<dt><i>%D</i></p>
<dd> The destination host, IPv6 addresses using underscore instead of colon.</p>
<dt><i>%p</i></p>
<dd> The destination port.</p>
<dt><i>%s</i></p>
<dd> The source host and port, separated by a comma, IPv6 addresses using underscore instead of colon.</p>
<dt><i>%S</i></p>
<dd> The source host, IPv6 addresses using underscore instead of colon.</p>
<dt><i>%q</i></p>
<dd> The source port.</p>
<dt><i>%x</i></p>
<dd> The name of the local process. Requires <code>-i</code> to be used. If process information is unavailable, this directive will be omitted from the output path.</p>
<dt><i>%X</i></p>
<dd> The full path of the local process. Requires <code>-i</code> to be used. If process information is unavailable, this directive will be omitted from the output path.</p>
<dt><i>%u</i></p>
<dd> The username or numeric uid of the local process. Requires <code>-i</code> to be used. If process information is unavailable, this directive will be omitted from the output path.</p>
<dt><i>%g</i></p>
<dd> The group name or numeric gid of the local process. Requires <code>-i</code> to be used. If process information is unavailable, this directive will be omitted from the output path.</p>
<dt><i>%%</i></p>
<dd> A literal &#8216;%&#8217; character.</dl>
<h2>NAT ENGINES</h2>
<p> SSLsplit currently supports the following NAT engines:</p>
<dl>
<dt><code>pf</code></p>
<dd> OpenBSD packet filter (pf) <code>rdr</code>/<code>rdr-to</code> NAT redirects, also available on FreeBSD, NetBSD and Mac OS X. Fully supported, including IPv6. Note that SSLsplit needs permission to open <code>/dev/pf</code> for reading, which by default means that it needs to run under <code>root</code> privileges. Assuming inbound interface <code>em0</code>, first in old (FreeBSD, Mac OS X), then in new (OpenBSD 4.7+) syntax:</dl>
<dl>
<dt>
<dd>
<pre><code>
rdr pass on em0 proto tcp from 2001 : db8:: / 64 to any port 80-&gt;::1 port 10080 rdr pass on em0 proto tcp from 2001 : db8:: / 64 to any port 443-&gt;::1 port 10443 rdr pass on em0 proto tcp from 192.0.2.0 / 24 to any port 80-&gt;127.0.0.1 port 10080 rdr pass on em0 proto tcp from 192.0.2.0 / 24 to any port 443-&gt;127.0.0.1 port 10443
</code></pre>
</dl>
<dl>
<dt>
<dd>
<pre>
<code>pass in quick on em0 proto tcp from 2001:db8::/64 to any \
         port  80 rdr-to       ::1 port 10080</code>
<code>pass in quick on em0 proto tcp from 2001:db8::/64 to any \
         port 443 rdr-to       ::1 port 10443</code>
<code>pass in quick on em0 proto tcp from  192.0.2.0/24 to any \
         port  80 rdr-to 127.0.0.1 port 10080</code>
<code>pass in quick on em0 proto tcp from  192.0.2.0/24 to any \
         port 443 rdr-to 127.0.0.1 port 10443</code>
</pre>
</dl>
<dl>
<dt><code>ipfw</code></p>
<dd> FreeBSD IP firewall (IPFW) divert sockets, also available on Mac OS X. Available on FreeBSD and OpenBSD using pf <code>divert-to</code>. Fully supported on FreeBSD and OpenBSD, including IPv6. Only supports IPv4 on Mac OS X due to the ancient version of IPFW included. First in IPFW, then in pf <code>divert-to</code> syntax:</dl>
<dl>
<dt>
<dd>
<pre>
<code>ipfw add fwd       ::1,10080 tcp from 2001:db8::/64 to any  80</code>
<code>ipfw add fwd       ::1,10443 tcp from 2001:db8::/64 to any 443</code>
<code>ipfw add fwd 127.0.0.1,10080 tcp from 192.0.2.0/24  to any  80</code>
<code>ipfw add fwd 127.0.0.1,10443 tcp from 192.0.2.0/24  to any 443</code>
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
<code>pass in quick on em0 proto tcp from 2001:db8::/64 to any \
         port  80 divert-to       ::1 port 10080</code>
<code>pass in quick on em0 proto tcp from 2001:db8::/64 to any \
         port 443 divert-to       ::1 port 10443</code>
<code>pass in quick on em0 proto tcp from  192.0.2.0/24 to any \
         port  80 divert-to 127.0.0.1 port 10080</code>
<code>pass in quick on em0 proto tcp from  192.0.2.0/24 to any \
         port 443 divert-to 127.0.0.1 port 10443</code>
</pre>
</dl>
<dl>
<dt><code>ipfilter</code></p>
<dd> IPFilter (ipfilter, ipf), available on many systems, including FreeBSD, NetBSD, Linux and Solaris. Note that SSLsplit needs permission to open <code>/dev/ipnat</code> for reading, which by default means that it needs to run under <code>root</code> privileges. Only supports IPv4 due to limitations in the SIOCGNATL <a href="/docs/linux/man/2-ioctl/">ioctl</a>(2) interface. Assuming inbound interface <code>bge0</code>:</dl>
<dl>
<dt>
<dd>
<pre>
<code>rdr bge0 0.0.0.0/0 port  80 -&gt; 127.0.0.1 port 10080</code>
<code>rdr bge0 0.0.0.0/0 port 443 -&gt; 127.0.0.1 port 10443</code>
</pre>
</dl>
<dl>
<dt><code>netfilter</code></p>
<dd> Linux netfilter using the iptables REDIRECT target. Only supports IPv4 due to limitations in the SO_ORIGINAL_DST <a href="/docs/linux/man/2-getsockopt/">getsockopt</a>(2) interface.</dl>
<dl>
<dt>
<dd>
iptables &#8211; t nat &#8211; A PREROUTING &#8211; s 192.0.2.0 / 24 &#8211; p tcp&#8211; dport 80 &#8211; j REDIRECT&#8211; to &#8211; ports 10080 iptables &#8211; t nat &#8211; A PREROUTING &#8211; s 192.0.2.0 / 24 &#8211; p tcp&#8211; dport 443 &#8211; j REDIRECT&#8211; to &#8211; ports 10443</p>
<p> Note that SSLsplit is only able to accept incoming connections if it binds to the correct IP address (e.g. 192.0.2.1) or on all interfaces (0.0.0.0). REDIRECT uses the local interface address of the incoming interface as target IP address, or 127.0.0.1 for locally generated packets.</dl>
<dl>
<dt><code>tproxy</code></p>
<dd> Linux netfilter using the iptables TPROXY target together with routing table magic to allow non-local traffic to originate on local sockets. Fully supported, including IPv6.</dl>
<dl>
<dt>
<dd>
ip &#8211; f inet6 rule add fwmark 1 lookup 100 ip &#8211; f inet6 route add local default dev lo table 100 ip6tables &#8211; t mangle &#8211; N DIVERT ip6tables &#8211; t mangle &#8211; A DIVERT &#8211; j MARK&#8211; set &#8211; mark 1 ip6tables &#8211; t mangle &#8211; A DIVERT &#8211; j ACCEPT ip6tables &#8211; t mangle &#8211; A PREROUTING &#8211; p tcp &#8211; m socket &#8211; j DIVERT ip6tables &#8211; t mangle &#8211; A PREROUTING &#8211; s 2001 : db8:: / 64 &#8211; p tcp&#8211; dport 80 &#8211; j TPROXY&#8211; tproxy &#8211; mark 0x1 / 0x1 &#8211;on &#8211; port 10080 ip6tables &#8211; t mangle &#8211; A PREROUTING &#8211; s 2001 : db8:: / 64 &#8211; p tcp&#8211; dport 443 &#8211; j TPROXY&#8211; tproxy &#8211; mark 0x1 / 0x1 &#8211;on &#8211; port 10443 ip &#8211; f inet rule add fwmark 1 lookup 100 ip &#8211; f inet route add local default dev lo table 100 iptables &#8211; t mangle &#8211; N DIVERT iptables &#8211; t mangle &#8211; A DIVERT &#8211; j MARK&#8211; set &#8211; mark 1 iptables &#8211; t mangle &#8211; A DIVERT &#8211; j ACCEPT iptables &#8211; t mangle &#8211; A PREROUTING &#8211; p tcp &#8211; m socket &#8211; j DIVERT iptables &#8211; t mangle &#8211; A PREROUTING &#8211; s 192.0.2.0 / 24 &#8211; p tcp&#8211; dport 80 &#8211; j TPROXY&#8211; tproxy &#8211; mark 0x1 / 0x1 &#8211;on &#8211; port 10080 iptables &#8211; t mangle &#8211; A PREROUTING &#8211; s 192.0.2.0 / 24 &#8211; p tcp&#8211; dport 443 &#8211; j TPROXY&#8211; tproxy &#8211; mark 0x1 / 0x1 &#8211;on &#8211; port 10443</p>
<p> Note that return path filtering (rp_filter) also needs to be disabled on interfaces which handle TPROXY redirected traffic.</dl>
<h2>EXAMPLES</h2>
<p> Matching the above NAT engine configuration samples, intercept HTTP and HTTPS over IPv4 and IPv6 using forged certificates with CA private key <code>ca.key</code> and certificate <code>ca.crt</code>, logging connections to <code>connect.log</code> and connection data into separate files under <code>/tmp</code> (add <code>-e</code> <i>nat-engine</i> to select the appropriate engine if multiple engines are available on your system): </p>
<pre>
<code>sslsplit -k ca.key -c ca.crt -l connect.log -L /tmp \
         https ::1 10443  https 127.0.0.1 10443 \
         http  ::1 10080  http  127.0.0.1 10080</code>
</pre>
<p> If the Linux netfilter engine is used with the iptables REDIRECT target, it is important to listen to the correct IP address (e.g. 192.0.2.1) or on all interfaces (0.0.0.0), otherwise SSLsplit is not able to accept incoming connections. </p>
<p> Intercepting IMAP/IMAPS using the same settings: </p>
<pre>
<code>sslsplit -k ca.key -c ca.crt -l connect.log -L /tmp \
         ssl ::1 10993  ssl 127.0.0.1 10993 \
         tcp ::1 10143  tcp 127.0.0.1 10143</code>
</pre>
<p> A more targetted setup, HTTPS only, using certificate/chain/key files from <code>/path/to/cert.d</code> and statically redirecting to <code><a rel="nofollow" href="http://www.example.org">www.example.org</a></code> instead of querying a NAT engine: </p>
<pre>
<code>sslsplit -t /path/to/cert.d -l connect.log -L /tmp \
         https ::1       10443 <a rel="nofollow" href="http://www.example.org">www.example.org</a> 443 \
         https 127.0.0.1 10443 <a rel="nofollow" href="http://www.example.org">www.example.org</a> 443</code>
</pre>
<p> The original example, but using SSL options optimized for speed by disabling compression and selecting only fast cipher cipher suites and using a precomputed private key <code>leaf.key</code> for the forged certificates. Most significant speed increase is gained by choosing fast algorithms and small keysizes for the CA and leaf private keys. Check <code>openssl speed</code> for algorithm performance on your system. Note that clients may not support all algorithms and key sizes. Also, some clients warn their users about cipher suites they consider weak. </p>
<pre>
<code>sslsplit -Z -s NULL:RC4:AES128:-DHE -K leaf.key \
         -k ca.key -c ca.crt -l connect.log -L /tmp \
         https ::1 10443  https 127.0.0.1 10443 \
         http  ::1 10080  http  127.0.0.1 10080</code>
</pre>
<p> The original example, but running as a daemon under user <code>sslsplit</code> and writing a PID file: </p>
<pre>
<code>sslsplit -d -p /var/run/sslsplit.pid -u sslsplit \
         -k ca.key -c ca.crt -l connect.log -L /tmp \
         https ::1 10443  https 127.0.0.1 10443 \
         http  ::1 10080  http  127.0.0.1 10080</code>
</pre>
<p> To generate a CA private key <code>ca.key</code> and certificate <code>ca.crt</code> using OpenSSL: </p>
<pre><code>
cat &gt; x509v3ca.cnf &lt;&lt; 'EOF'
              [req] distinguished_name = reqdn
    [reqdn]
    [v3_ca] basicConstraints = CA : TRUE
                                        subjectKeyIdentifier = hash
                                            authorityKeyIdentifier = keyid : always,
                    issuer : always
                                 EOF
                                     openssl genrsa -
                             out ca.key 2048 openssl req - new - nodes - x509 - sha256 - out ca.crt - key ca.key - config x509v3ca.cnf - extensions v3_ca - subj '/O=SSLsplit Root CA/CN=SSLsplit Root CA/' - set_serial 0 - days 3650
</code></pre>
<h2>NOTES</h2>
<p> SSLsplit is able to handle a relatively high number of listeners and connections due to a multithreaded, event based architecture based on libevent, taking advantage of platform specific select() replacements such as kqueue. The main thread handles the listeners and signalling, while a number of worker threads equal to twice the number of CPU cores is used for handling the actual connections in separate event bases, including the CPU-intensive SSL/TLS handling. </p>
<p> Care has been taken to choose well-performing data structures for caching certificates and SSL sessions. Logging is implemented in separate disk writer threads to ensure that socket event handling threads don&#8217;t have to block on disk I/O. DNS lookups are performed asynchroniously. SSLsplit uses SSL session caching on both ends to minimize the amount of full SSL handshakes, but even then, the limiting factor in handling SSL connections are the actual bignum computations.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-openssl/">openssl</a>(1), <a href="/docs/linux/man/1-ciphers/">ciphers</a>(1), <a href="/docs/linux/man/1-speed/">speed</a>(1), <a href="/docs/linux/man/4-pf/">pf</a>(4), <a href="/docs/linux/man/8-ipfw/">ipfw</a>(8), <a href="/docs/linux/man/8-iptables/">iptables</a>(8), <a href="/docs/linux/man/8-ip6tables/">ip6tables</a>(8), <a href="/docs/linux/man/8-ip/">ip</a>(8), <a href="/docs/linux/man/8-hostapd/">hostapd</a>(8), <a href="/docs/linux/man/8-arpspoof/">arpspoof</a>(8), <a href="/docs/linux/man/8-parasite6/">parasite6</a>(8), <a href="/docs/linux/man/8-yersinia/">yersinia</a>(8), <i><a rel="nofollow" href="https://www.roe.ch/SSLsplit">https://www.roe.ch/SSLsplit</a></i></p>
<h2>AUTHORS</h2>
<p> SSLsplit was written by Daniel Roethlisberger &lt;daniel [at] roe.ch&gt;. </p>
<p> The following individuals have contributed code or documentation, in chronological order of their first contribution: Steve Wills, Landon Fuller, Wayne Jensen, Rory McNamara, Alexander Neumann, Adam Jacob Muller and Richard Poole.</p>
<h2>BUGS</h2>
<p> Use Github for submission of bug reports or patches: </p>
<dl>
<dt>
<dd> <i><a rel="nofollow" href="https://github.com/droe/sslsplit">https://github.com/droe/sslsplit</a></i></dl>
<h2>Index</h2>
