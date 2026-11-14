---
title: "hitch(8)"
name: "hitch"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hitch/"
description: "Hitch – high performance TLS proxy"
---

<p>Hitch &#8211; high performance TLS proxy</p>
<h2>Synopsis</h2>
<p>hitch [OPTIONS] [PEM]</p>
<h2>Description</h2>
<p>Hitch is a network proxy that terminates TLS/SSL connections and forwards the unencrypted traffic to some backend. It&#8217;s designed to handle 10s of thousands of connections efficiently on multicore machines. </p>
<p> Hitch has very few features &#8212; it&#8217;s designed to be paired with an intelligent backend like Varnish Cache. It maintains a strict 1:1 connection pattern with this backend handler so that the backend can dictate throttling behavior, maximum connection behavior, availability of service, etc. </p>
<p> The only required argument is a path to a PEM file that contains the certificate (or a chain of certificates) and private key. It should also contain DH parameter if you wish to use Diffie-Hellman cipher suites.</p>
<h2>Command Line Arguments</h2>
<dl>
<dt><code>&#8211;config=</code><i>FILE</i></p>
<dd>Load configuration from specified file. See <i><a href="/docs/linux/man/5-hitch-conf/">hitch.conf</a>(5)</i> for details.</p>
<dt><code>&#8211;tls</code></p>
<dd>All TLS versions, no SSLv3 (deprecated). See config file setting <code>tls-protos</code>.</p>
<dt><code>&#8211;ssl</code></p>
<dd>enable SSLv3 (deprecated). See config file setting <code>tls-protos</code>.</p>
<dt><code>-c</code></p>
<dd>
<dt><code>&#8211;ciphers=</code><i>SUITE</i></p>
<dd>Sets allowed ciphers (Default: &quot;&quot;)</p>
<dt><code>-e</code></p>
<dd>
<dt><code>&#8211;ssl-engine=</code><i>NAME</i></p>
<dd>Sets OpenSSL engine (Default: &quot;&quot;)</p>
<dt><code>-O</code></p>
<dd>
<dt><code>&#8211;prefer-server-ciphers</code></p>
<dd>Prefer server list order</p>
<dt><code>&#8211;client</code></p>
<dd>Enable client proxy mode</p>
<dt><code>-b</code></p>
<dd>&#8211;backend=[HOST]:PORT Backend [connect] (default is &quot;[127.0.0.1]:8000&quot;)</p>
<dt><code>-f</code></p>
<dd>&#8211;frontend=[HOST]:PORT[+CERT] Frontend [bind] (default is &quot;[*]:8443&quot;) (Note: brackets are mandatory in endpoint specifiers.)</p>
<dt><code>-n</code></p>
<dd>
<dt><code>&#8211;workers=</code><i>NUM</i></p>
<dd>Number of worker processes (Default: 1)</p>
<dt><code>-B</code></p>
<dd>
<dt><code>&#8211;backlog=</code><i>NUM</i></p>
<dd>Set listen backlog size (Default: 100)</p>
<dt><code>-k</code></p>
<dd>
<dt><code>&#8211;keepalive=</code><i>SECS</i></p>
<dd>TCP keepalive on client socket (Default: 3600)</p>
<dt><code>-r</code></p>
<dd>
<dt><code>&#8211;chroot=</code><i>DIR</i></p>
<dd>Sets chroot directory (Default: &quot;&quot;)</p>
<dt><code>-u</code></p>
<dd>
<dt><code>&#8211;user=</code><i>USER</i></p>
<dd>Set uid/gid after binding the socket (Default: &quot;&quot;)</p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;group=</code><i>GROUP</i></p>
<dd>Set gid after binding the socket (Default: &quot;&quot;)</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd>Be quiet; emit only error messages</p>
<dt><code>-s</code></p>
<dd>
<dt><code>&#8211;syslog</code></p>
<dd>Send log message to syslog in addition to stderr/stdout</p>
<dt><code>&#8211;syslog-facility=</code><i>FACILITY</i></p>
<dd>Syslog facility to use (Default: &quot;daemon&quot;)</p>
<dt><code>&#8211;daemon</code></p>
<dd>Fork into background and become a daemon; this also sets the &#8211;quiet option (Default: off)</p>
<dt><code>&#8211;write-ip</code></p>
<dd>Write 1 octet with the IP family followed by the IP address in 4 (IPv4) or 16 (IPv6) octets little-endian to backend before the actual data (Default: off)</p>
<dt><code>&#8211;write-proxy-v1</code></p>
<dd>Write HaProxy&#8217;s PROXY v1 (IPv4 or IPv6) protocol line before actual data (Default: off)</p>
<dt><code>&#8211;write-proxy-v2</code></p>
<dd>Write HaProxy&#8217;s PROXY v2 binary (IPv4 or IPv6) protocol line before actual data (Default: off)</p>
<dt><code>&#8211;write-proxy</code></p>
<dd>Equivalent to &#8211;write-proxy-v2. For PROXY version 1 use &#8211;write-proxy-v1 explicitly</p>
<dt><code>&#8211;proxy-proxy</code></p>
<dd>Proxy HaProxy&#8217;s PROXY (IPv4 or IPv6) protocol line before actual data (PROXY v1 only) (Default: off)</p>
<dt><code>&#8211;alpn-protos=</code><i>LIST</i></p>
<dd>Sets the protocols for ALPN/NPN negotiation, given by a comma separated list. If this is not set explicitly, ALPN/NPN will not be used. Requires OpenSSL 1.0.1 for NPN and OpenSSL 1.0.2 for ALPN.</p>
<dt><code>&#8211;sni-nomatch-abort</code></p>
<dd>Abort handshake when client submits an unrecognized SNI server name (Default: off)</p>
<dt><code>&#8211;ocsp-dir=</code><i>DIR</i></p>
<dd>Set OCSP staple cache directory This enables automated retrieval and stapling of OCSP responses (Default: &quot;&quot;)</p>
<dt><code>-t</code></p>
<dd>
<dt><code>&#8211;test</code></p>
<dd>Test configuration and exit</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;pidfile=</code><i>FILE</i></p>
<dd>PID file</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Print program version and exit</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd>This help message</dl>
<h2>History</h2>
<p>Hitch was originally called stud and was written by Jamie Turner at Bump.com.</p>
