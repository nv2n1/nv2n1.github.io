---
title: "nghttpd(1)"
name: "nghttpd"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nghttpd/"
description: "nghttpd – HTTP/2 server"
---

<h2>NAME</h2>
<p> nghttpd &#8211; HTTP/2 server</p>
<h2>SYNOPSIS</h2>
<p> <code>nghttpd</code> [OPTION]&#8230; &lt;PORT&gt; [&lt;PRIVATE_KEY&gt; &lt;CERT&gt;]</p>
<h2>DESCRIPTION</h2>
<p> HTTP/2 server</p>
<dl>
<dt><code>&lt;PORT&gt;</code></p>
<dd> Specify listening port number.</p>
<dt><code>&lt;PRIVATE_KEY&gt;</code></p>
<dd> Set path to server&#8217;s private key. Required unless <i>&#8211;no-tls</i> is specified.</p>
<dt><code>&lt;CERT&gt;</code></p>
<dd> Set path to server&#8217;s certificate. Required unless <i>&#8211;no-tls</i> is specified.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a, &#8211;address=&lt;ADDR&gt;</code></p>
<dd> The address to bind to. If not specified the default IP address determined by getaddrinfo is used.</p>
<dt><code>-D, &#8211;daemon</code></p>
<dd> Run in a background. If <i>-D</i> is used, the current working directory is changed to &#8216;<i>/</i>&#8216;. Therefore if this option is used, <i>-d</i> option must be specified.</p>
<dt><code>-V, &#8211;verify-client</code></p>
<dd> The server sends a client certificate request. If the client did not return a certificate, the handshake is terminated. Currently, this option just requests a client certificate and does not verify it.</p>
<dt><code>-d, &#8211;htdocs=&lt;PATH&gt;</code></p>
<dd> Specify document root. If this option is not specified, the document root is the current working directory.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Print debug information such as reception/ transmission of frames and name/value pairs.</p>
<dt><code>&#8211;no-tls</code></p>
<dd> Disable SSL/TLS.</p>
<dt><code>-c, &#8211;header-table-size=&lt;SIZE&gt;</code></p>
<dd> Specify decoder header table size.</p>
<dt><code>&#8211;color</code></p>
<dd> Force colored log output.</p>
<dt><code>-p, &#8211;push=&lt;PATH&gt;=&lt;PUSH_PATH,&#8230;&gt;</code></p>
<dd> Push resources &lt;PUSH_PATH&gt;s when &lt;PATH&gt; is requested. This option can be used repeatedly to specify multiple push configurations. &lt;PATH&gt; and &lt;PUSH_PATH&gt;s are relative to document root. See <i>&#8211;htdocs</i> option. Example: <i>-p</i>/=/foo.png <i>-p</i>/doc=/bar.css</p>
<dt><code>-b, &#8211;padding=&lt;N&gt;</code></p>
<dd> Add at most &lt;N&gt; bytes to a frame payload as padding. Specify 0 to disable padding.</p>
<dt><code>-m, &#8211;max-concurrent-streams=&lt;N&gt;</code></p>
<dd> Set the maximum number of the concurrent streams in one HTTP/2 session. </p>
<p> Default: <code>100</code></p>
<dt><code>-n, &#8211;workers=&lt;N&gt;</code></p>
<dd> Set the number of worker threads. </p>
<p> Default: <code>1</code></p>
<dt><code>-e, &#8211;error-gzip</code></p>
<dd> Make error response gzipped.</p>
<dt><code>&#8211;dh-param-file=&lt;PATH&gt;</code></p>
<dd> Path to file that contains DH parameters in PEM format. Without this option, DHE cipher suites are not available.</p>
<dt><code>&#8211;early-response</code></p>
<dd> Start sending response when request HEADERS is received, rather than complete request is received.</p>
<dt><code>&#8211;trailer=&lt;HEADER&gt;</code></p>
<dd> Add a trailer header to a response. &lt;HEADER&gt; must not include pseudo header field (header field name starting with &#8216;:&#8217;). The trailer is sent only if a response has body part. Example: <i>&#8211;trailer</i> &#8216;foo: bar&#8217;.</p>
<dt><code>&#8211;hexdump</code></p>
<dd> Display the incoming traffic in hexadecimal (Canonical hex+ASCII display). If SSL/TLS is used, decrypted data are used.</p>
<dt><code>&#8211;echo-upload</code></p>
<dd> Send back uploaded content if method is POST or PUT.</p>
<dt><code>&#8211;mime-types-file=&lt;PATH&gt;</code></p>
<dd> Path to file that contains MIME media types and the extensions that represent them. </p>
<p> Default: <code>/etc/mime.types</code></p>
<dt><code>&#8211;no-content-length</code></p>
<dd> Don&#8217;t send content-length header field.</p>
<dt><code>&#8211;version</code></p>
<dd> Display version information and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display this help and exit. </p>
<p> The &lt;SIZE&gt; argument is an integer and an optional unit (e.g., 10K is 10 * 1024). Units are K, M and G (powers of 1024).</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-nghttp/">nghttp</a>(1)</i>, <i><a href="/docs/linux/man/1-nghttpx/">nghttpx</a>(1)</i>, <i><a href="/docs/linux/man/1-h2load/">h2load</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Tatsuhiro Tsujikawa</p>
<h2>COPYRIGHT</h2>
<p> 2012, 2015, 2016, Tatsuhiro Tsujikawa </p>
<h2>Index</h2>
