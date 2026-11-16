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
<dt><code>&#8211;config=</code><i>FILE</i></dt>
<dd>Load configuration from specified file. See <i><a href="/docs/linux/man/5-hitch-conf/">hitch.conf</a>(5)</i> for details.</dd>
<dt><code>&#8211;tls</code></dt>
<dd>All TLS versions, no SSLv3 (deprecated). See config file setting <code>tls-protos</code>.</dd>
<dt><code>&#8211;ssl</code></dt>
<dd>enable SSLv3 (deprecated). See config file setting <code>tls-protos</code>.</dd>
<dt><code>-c</code></dt>
<dd>
</dd><dt><code>&#8211;ciphers=</code><i>SUITE</i></dt>
<dd>Sets allowed ciphers (Default: &quot;&quot;)</dd>
<dt><code>-e</code></dt>
<dd>
</dd><dt><code>&#8211;ssl-engine=</code><i>NAME</i></dt>
<dd>Sets OpenSSL engine (Default: &quot;&quot;)</dd>
<dt><code>-O</code></dt>
<dd>
</dd><dt><code>&#8211;prefer-server-ciphers</code></dt>
<dd>Prefer server list order</dd>
<dt><code>&#8211;client</code></dt>
<dd>Enable client proxy mode</dd>
<dt><code>-b</code></dt>
<dd>&#8211;backend=[HOST]:PORT Backend [connect] (default is &quot;[127.0.0.1]:8000&quot;)</dd>
<dt><code>-f</code></dt>
<dd>&#8211;frontend=[HOST]:PORT[+CERT] Frontend [bind] (default is &quot;[*]:8443&quot;) (Note: brackets are mandatory in endpoint specifiers.)</dd>
<dt><code>-n</code></dt>
<dd>
</dd><dt><code>&#8211;workers=</code><i>NUM</i></dt>
<dd>Number of worker processes (Default: 1)</dd>
<dt><code>-B</code></dt>
<dd>
</dd><dt><code>&#8211;backlog=</code><i>NUM</i></dt>
<dd>Set listen backlog size (Default: 100)</dd>
<dt><code>-k</code></dt>
<dd>
</dd><dt><code>&#8211;keepalive=</code><i>SECS</i></dt>
<dd>TCP keepalive on client socket (Default: 3600)</dd>
<dt><code>-r</code></dt>
<dd>
</dd><dt><code>&#8211;chroot=</code><i>DIR</i></dt>
<dd>Sets chroot directory (Default: &quot;&quot;)</dd>
<dt><code>-u</code></dt>
<dd>
</dd><dt><code>&#8211;user=</code><i>USER</i></dt>
<dd>Set uid/gid after binding the socket (Default: &quot;&quot;)</dd>
<dt><code>-g</code></dt>
<dd>
</dd><dt><code>&#8211;group=</code><i>GROUP</i></dt>
<dd>Set gid after binding the socket (Default: &quot;&quot;)</dd>
<dt><code>-q</code></dt>
<dd>
</dd><dt><code>&#8211;quiet</code></dt>
<dd>Be quiet; emit only error messages</dd>
<dt><code>-s</code></dt>
<dd>
</dd><dt><code>&#8211;syslog</code></dt>
<dd>Send log message to syslog in addition to stderr/stdout</dd>
<dt><code>&#8211;syslog-facility=</code><i>FACILITY</i></dt>
<dd>Syslog facility to use (Default: &quot;daemon&quot;)</dd>
<dt><code>&#8211;daemon</code></dt>
<dd>Fork into background and become a daemon; this also sets the &#8211;quiet option (Default: off)</dd>
<dt><code>&#8211;write-ip</code></dt>
<dd>Write 1 octet with the IP family followed by the IP address in 4 (IPv4) or 16 (IPv6) octets little-endian to backend before the actual data (Default: off)</dd>
<dt><code>&#8211;write-proxy-v1</code></dt>
<dd>Write HaProxy&#8217;s PROXY v1 (IPv4 or IPv6) protocol line before actual data (Default: off)</dd>
<dt><code>&#8211;write-proxy-v2</code></dt>
<dd>Write HaProxy&#8217;s PROXY v2 binary (IPv4 or IPv6) protocol line before actual data (Default: off)</dd>
<dt><code>&#8211;write-proxy</code></dt>
<dd>Equivalent to &#8211;write-proxy-v2. For PROXY version 1 use &#8211;write-proxy-v1 explicitly</dd>
<dt><code>&#8211;proxy-proxy</code></dt>
<dd>Proxy HaProxy&#8217;s PROXY (IPv4 or IPv6) protocol line before actual data (PROXY v1 only) (Default: off)</dd>
<dt><code>&#8211;alpn-protos=</code><i>LIST</i></dt>
<dd>Sets the protocols for ALPN/NPN negotiation, given by a comma separated list. If this is not set explicitly, ALPN/NPN will not be used. Requires OpenSSL 1.0.1 for NPN and OpenSSL 1.0.2 for ALPN.</dd>
<dt><code>&#8211;sni-nomatch-abort</code></dt>
<dd>Abort handshake when client submits an unrecognized SNI server name (Default: off)</dd>
<dt><code>&#8211;ocsp-dir=</code><i>DIR</i></dt>
<dd>Set OCSP staple cache directory This enables automated retrieval and stapling of OCSP responses (Default: &quot;&quot;)</dd>
<dt><code>-t</code></dt>
<dd>
</dd><dt><code>&#8211;test</code></dt>
<dd>Test configuration and exit</dd>
<dt><code>-p</code></dt>
<dd>
</dd><dt><code>&#8211;pidfile=</code><i>FILE</i></dt>
<dd>PID file</dd>
<dt><code>-V</code></dt>
<dd>
</dd><dt><code>&#8211;version</code></dt>
<dd>Print program version and exit</dd>
<dt><code>-h</code></dt>
<dd>
</dd><dt><code>&#8211;help</code></dt>
<dd>This help message</dd></dl>
<h2>History</h2>
<p>Hitch was originally called stud and was written by Jamie Turner at Bump.com.</p>
