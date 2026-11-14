---
title: "nghttpx(1)"
name: "nghttpx"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nghttpx/"
description: "nghttpx – HTTP/2 proxy"
---

<h2>NAME</h2>
<p> nghttpx &#8211; HTTP/2 proxy</p>
<h2>SYNOPSIS</h2>
<p> <code>nghttpx</code> [OPTIONS]&#8230; [&lt;PRIVATE_KEY&gt; &lt;CERT&gt;]</p>
<h2>DESCRIPTION</h2>
<p> A reverse proxy for HTTP/2, HTTP/1 and SPDY.</p>
<dl>
<dt><code>&lt;PRIVATE_KEY&gt;</code></p>
<dd> Set path to server&#8217;s private key. Required unless <i>-p</i>, <i>&#8211;client</i> or <i>&#8211;frontend-no-tls</i> are given.</p>
<dt><code>&lt;CERT&gt;</code></p>
<dd> Set path to server&#8217;s certificate. Required unless <i>-p</i>, <i>&#8211;client</i> or <i>&#8211;frontend-no-tls</i> are given. To make OCSP stapling work, this must be absolute path.</dl>
<h2>OPTIONS</h2>
<p> The options are categorized into several groups.</p>
<h3>Connections</h3>
<dl>
<dt><code>-b, &#8211;backend=(&lt;HOST&gt;,&lt;PORT&gt;|unix:&lt;PATH&gt;)[;&lt;PATTERN&gt;[:&#8230;]]</code></p>
<dd> Set backend host and port. The multiple backend addresses are accepted by repeating this option. UNIX domain socket can be specified by prefixing path name with &quot;unix:&quot; (e.g., unix:/var/run/backend.sock). </p>
<p> Optionally, if &lt;PATTERN&gt;s are given, the backend address is only used if request matches the pattern. If <i>-s</i> or <i>-p</i> is used, &lt;PATTERN&gt;s are ignored. The pattern matching is closely designed to ServeMux in net/http package of Go programming language. &lt;PATTERN&gt; consists of path, host + path or just host. The path must start with &quot;<i>/</i>&quot;. If it ends with &quot;<i>/</i>&quot;, it matches all request path in its subtree. To deal with the request to the directory without trailing slash, the path which ends with &quot;<i>/</i>&quot; also matches the request path which only lacks trailing &#8216;<i>/</i>&#8216; (e.g., path &quot;<i>/foo/</i>&quot; matches request path &quot;<i>/foo</i>&quot;). If it does not end with &quot;<i>/</i>&quot;, it performs exact match against the request path. If host is given, it performs exact match against the request host. If host alone is given, &quot;<i>/</i>&quot; is appended to it, so that it matches all request paths under the host (e.g., specifying &quot;nghttp2.org&quot; equals to &quot;nghttp2.org/&quot;). </p>
<p> Patterns with host take precedence over patterns with just path. Then, longer patterns take precedence over shorter ones, breaking a tie by the order of the appearance in the configuration. </p>
<p> If &lt;PATTERN&gt; is omitted, &quot;<i>/</i>&quot; is used as pattern, which matches all request paths (catch-all pattern). The catch-all backend must be given. </p>
<p> When doing a match, nghttpx made some normalization to pattern, request host and path. For host part, they are converted to lower case. For path part, percent-encoded unreserved characters defined in RFC 3986 are decoded, and any dot-segments (&quot;..&quot; and &quot;.&quot;) are resolved and removed. </p>
<p> For example, <i>-b</i>&#8216;127.0.0.1,8080;nghttp2.org/httpbin/&#8217; matches the request host &quot;nghttp2.org&quot; and the request path &quot;<i>/httpbin/get</i>&quot;, but does not match the request host &quot;nghttp2.org&quot; and the request path &quot;<i>/index.html</i>&quot;. </p>
<p> The multiple &lt;PATTERN&gt;s can be specified, delimiting them by &quot;:&quot;. Specifying <i>-b</i>&#8216;127.0.0.1,8080;nghttp2.org:<a rel="nofollow" href="http://www.nghttp2.org">www.nghttp2.org</a>&#8216; has the same effect to specify <i>-b</i>&#8216;127.0.0.1,8080;nghttp2.org&#8217; and <i>-b</i>&#8216;127.0.0.1,8080;<a rel="nofollow" href="http://www.nghttp2.org">www.nghttp2.org</a>&#8216;. </p>
<p> The backend addresses sharing same &lt;PATTERN&gt; are grouped together forming load balancing group. </p>
<p> Since &quot;;&quot; and &quot;:&quot; are used as delimiter, &lt;PATTERN&gt; must not contain these characters. Since &quot;;&quot; has special meaning in shell, the option value must be quoted. </p>
<p> Default: <code>127.0.0.1,80</code></p>
<dt><code>-f, &#8211;frontend=(&lt;HOST&gt;,&lt;PORT&gt;|unix:&lt;PATH&gt;)</code></p>
<dd> Set frontend host and port. If &lt;HOST&gt; is &#8216;*&#8217;, it assumes all addresses including both IPv4 and IPv6. UNIX domain socket can be specified by prefixing path name with &quot;unix:&quot; (e.g., unix:/var/run/nghttpx.sock) </p>
<p> Default: <code>*,3000</code></p>
<dt><code>&#8211;backlog=&lt;N&gt;</code></p>
<dd> Set listen backlog size. </p>
<p> Default: <code>512</code></p>
<dt><code>&#8211;backend-ipv4</code></p>
<dd> Resolve backend hostname to IPv4 address only.</p>
<dt><code>&#8211;backend-ipv6</code></p>
<dd> Resolve backend hostname to IPv6 address only.</p>
<dt><code>&#8211;backend-http-proxy-uri=&lt;URI&gt;</code></p>
<dd> Specify proxy URI in the form <i>http:/</i>/[&lt;USER&gt;:&lt;PASS&gt;@]&lt;PROXY&gt;:&lt;PORT&gt;. If a proxy requires authentication, specify &lt;USER&gt; and &lt;PASS&gt;. Note that they must be properly percent-encoded. This proxy is used when the backend connection is HTTP/2. First, make a CONNECT request to the proxy and it connects to the backend on behalf of nghttpx. This forms tunnel. After that, nghttpx performs SSL/TLS handshake with the downstream through the tunnel. The timeouts when connecting and making CONNECT request can be specified by <i>&#8211;backend-read-timeout</i> and <i>&#8211;backend-write-timeout</i> options.</p>
<dt><code>&#8211;accept-proxy-protocol</code></p>
<dd> Accept PROXY protocol version 1 on frontend connection.</dl>
<h3>Performance</h3>
<dl>
<dt><code>-n, &#8211;workers=&lt;N&gt;</code></p>
<dd> Set the number of worker threads. </p>
<p> Default: <code>1</code></p>
<dt><code>&#8211;read-rate=&lt;SIZE&gt;</code></p>
<dd> Set maximum average read rate on frontend connection. Setting 0 to this option means read rate is unlimited. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;read-burst=&lt;SIZE&gt;</code></p>
<dd> Set maximum read burst size on frontend connection. Setting 0 to this option means read burst size is unlimited. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;write-rate=&lt;SIZE&gt;</code></p>
<dd> Set maximum average write rate on frontend connection. Setting 0 to this option means write rate is unlimited. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;write-burst=&lt;SIZE&gt;</code></p>
<dd> Set maximum write burst size on frontend connection. Setting 0 to this option means write burst size is unlimited. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;worker-read-rate=&lt;SIZE&gt;</code></p>
<dd> Set maximum average read rate on frontend connection per worker. Setting 0 to this option means read rate is unlimited. Not implemented yet. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;worker-read-burst=&lt;SIZE&gt;</code></p>
<dd> Set maximum read burst size on frontend connection per worker. Setting 0 to this option means read burst size is unlimited. Not implemented yet. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;worker-write-rate=&lt;SIZE&gt;</code></p>
<dd> Set maximum average write rate on frontend connection per worker. Setting 0 to this option means write rate is unlimited. Not implemented yet. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;worker-write-burst=&lt;SIZE&gt;</code></p>
<dd> Set maximum write burst size on frontend connection per worker. Setting 0 to this option means write burst size is unlimited. Not implemented yet. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;worker-frontend-connections=&lt;N&gt;</code></p>
<dd> Set maximum number of simultaneous connections frontend accepts. Setting 0 means unlimited. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;backend-http2-connections-per-worker=&lt;N&gt;</code></p>
<dd> Set maximum number of backend HTTP/2 physical connections per worker. If pattern is used in <i>-b</i> option, this limit is applied to each pattern group (in other words, each pattern group can have maximum &lt;N&gt; HTTP/2 connections). The default value is 0, which means that the value is adjusted to the number of backend addresses. If pattern is used, this adjustment is done for each pattern group.</p>
<dt><code>&#8211;backend-http1-connections-per-host=&lt;N&gt;</code></p>
<dd> Set maximum number of backend concurrent HTTP/1 connections per origin host. This option is meaningful when <i>-s</i> option is used. The origin host is determined by authority portion of request URI (or :authority header field for HTTP/2). To limit the number of connections per frontend for default mode, use <i>&#8211;backend-http1-connections-per-frontend</i>. </p>
<p> Default: <code>8</code></p>
<dt><code>&#8211;backend-http1-connections-per-frontend=&lt;N&gt;</code></p>
<dd> Set maximum number of backend concurrent HTTP/1 connections per frontend. This option is only used for default mode. 0 means unlimited. To limit the number of connections per host for HTTP/2 or SPDY proxy mode (-s option), use <i>&#8211;backend-http1-connections-per-host</i>. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;rlimit-nofile=&lt;N&gt;</code></p>
<dd> Set maximum number of open files (RLIMIT_NOFILE) to &lt;N&gt;. If 0 is given, nghttpx does not set the limit. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;backend-request-buffer=&lt;SIZE&gt;</code></p>
<dd> Set buffer size used to store backend request. </p>
<p> Default: <code>16K</code></p>
<dt><code>&#8211;backend-response-buffer=&lt;SIZE&gt;</code></p>
<dd> Set buffer size used to store backend response. </p>
<p> Default: <code>128K</code></p>
<dt><code>&#8211;fastopen=&lt;N&gt;</code></p>
<dd> Enables &quot;TCP Fast Open&quot; for the listening socket and limits the maximum length for the queue of connections that have not yet completed the three-way handshake. If value is 0 then fast open is disabled. </p>
<p> Default: <code>0</code></dl>
<h3>Timeout</h3>
<dl>
<dt><code>&#8211;frontend-http2-read-timeout=&lt;DURATION&gt;</code></p>
<dd> Specify read timeout for HTTP/2 and SPDY frontend connection. </p>
<p> Default: <code>3m</code></p>
<dt><code>&#8211;frontend-read-timeout=&lt;DURATION&gt;</code></p>
<dd> Specify read timeout for HTTP/1.1 frontend connection. </p>
<p> Default: <code>1m</code></p>
<dt><code>&#8211;frontend-write-timeout=&lt;DURATION&gt;</code></p>
<dd> Specify write timeout for all frontend connections. </p>
<p> Default: <code>30s</code></p>
<dt><code>&#8211;stream-read-timeout=&lt;DURATION&gt;</code></p>
<dd> Specify read timeout for HTTP/2 and SPDY streams. 0 means no timeout. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;stream-write-timeout=&lt;DURATION&gt;</code></p>
<dd> Specify write timeout for HTTP/2 and SPDY streams. 0 means no timeout. </p>
<p> Default: <code>0</code></p>
<dt><code>&#8211;backend-read-timeout=&lt;DURATION&gt;</code></p>
<dd> Specify read timeout for backend connection. </p>
<p> Default: <code>1m</code></p>
<dt><code>&#8211;backend-write-timeout=&lt;DURATION&gt;</code></p>
<dd> Specify write timeout for backend connection. </p>
<p> Default: <code>30s</code></p>
<dt><code>&#8211;backend-keep-alive-timeout=&lt;DURATION&gt;</code></p>
<dd> Specify keep-alive timeout for backend connection. </p>
<p> Default: <code>2s</code></p>
<dt><code>&#8211;listener-disable-timeout=&lt;DURATION&gt;</code></p>
<dd> After accepting connection failed, connection listener is disabled for a given amount of time. Specifying 0 disables this feature. </p>
<p> Default: <code>30s</code></dl>
<h3>SSL/TLS</h3>
<dl>
<dt><code>&#8211;ciphers=&lt;SUITE&gt;</code></p>
<dd> Set allowed cipher list. The format of the string is described in OpenSSL <a href="/docs/linux/man/1-ciphers/">ciphers</a>(1).</p>
<dt><code>-k, &#8211;insecure</code></p>
<dd> Don&#8217;t verify backend server&#8217;s certificate if <i>-p</i>, <i>&#8211;client</i> or <i>&#8211;http2-bridge</i> are given and <i>&#8211;backend-no-tls</i> is not given.</p>
<dt><code>&#8211;cacert=&lt;PATH&gt;</code></p>
<dd> Set path to trusted CA certificate file if <i>-p</i>, <i>&#8211;client</i> or <i>&#8211;http2-bridge</i> are given and <i>&#8211;backend-no-tls</i> is not given. The file must be in PEM format. It can contain multiple certificates. If the linked OpenSSL is configured to load system wide certificates, they are loaded at startup regardless of this option.</p>
<dt><code>&#8211;private-key-passwd-file=&lt;PATH&gt;</code></p>
<dd> Path to file that contains password for the server&#8217;s private key. If none is given and the private key is password protected it&#8217;ll be requested interactively.</p>
<dt><code>&#8211;subcert=&lt;KEYPATH&gt;:&lt;CERTPATH&gt;</code></p>
<dd> Specify additional certificate and private key file. nghttpx will choose certificates based on the hostname indicated by client using TLS SNI extension. This option can be used multiple times. To make OCSP stapling work, &lt;CERTPATH&gt; must be absolute path.</p>
<dt><code>&#8211;backend-tls-sni-field=&lt;HOST&gt;</code></p>
<dd> Explicitly set the content of the TLS SNI extension. This will default to the backend HOST name.</p>
<dt><code>&#8211;dh-param-file=&lt;PATH&gt;</code></p>
<dd> Path to file that contains DH parameters in PEM format. Without this option, DHE cipher suites are not available.</p>
<dt><code>&#8211;npn-list=&lt;LIST&gt;</code></p>
<dd> Comma delimited list of ALPN protocol identifier sorted in the order of preference. That means most desirable protocol comes first. This is used in both ALPN and NPN. The parameter must be delimited by a single comma only and any white spaces are treated as a part of protocol string. </p>
<p> Default: <code>h2,h2-16,h2-14,spdy/3.1,http/1.1</code></p>
<dt><code>&#8211;verify-client</code></p>
<dd> Require and verify client certificate.</p>
<dt><code>&#8211;verify-client-cacert=&lt;PATH&gt;</code></p>
<dd> Path to file that contains CA certificates to verify client certificate. The file must be in PEM format. It can contain multiple certificates.</p>
<dt><code>&#8211;client-private-key-file=&lt;PATH&gt;</code></p>
<dd> Path to file that contains client private key used in backend client authentication.</p>
<dt><code>&#8211;client-cert-file=&lt;PATH&gt;</code></p>
<dd> Path to file that contains client certificate used in backend client authentication.</p>
<dt><code>&#8211;tls-proto-list=&lt;LIST&gt;</code></p>
<dd> Comma delimited list of SSL/TLS protocol to be enabled. The following protocols are available: TLSv1.2, TLSv1.1 and TLSv1.0. The name matching is done in case-insensitive manner. The parameter must be delimited by a single comma only and any white spaces are treated as a part of protocol string. If the protocol list advertised by client does not overlap this list, you will receive the error message &quot;unknown protocol&quot;. </p>
<p> Default: <code>TLSv1.2,TLSv1.1</code></p>
<dt><code>&#8211;tls-ticket-key-file=&lt;PATH&gt;</code></p>
<dd> Path to file that contains random data to construct TLS session ticket parameters. If aes-128-cbc is given in <i>&#8211;tls-ticket-key-cipher</i>, the file must contain exactly 48 bytes. If aes-256-cbc is given in <i>&#8211;tls-ticket-key-cipher</i>, the file must contain exactly 80 bytes. This options can be used repeatedly to specify multiple ticket parameters. If several files are given, only the first key is used to encrypt TLS session tickets. Other keys are accepted but server will issue new session ticket with first key. This allows session key rotation. Please note that key rotation does not occur automatically. User should rearrange files or change options values and restart nghttpx gracefully. If opening or reading given file fails, all loaded keys are discarded and it is treated as if none of this option is given. If this option is not given or an error occurred while opening or reading a file, key is generated every 1 hour internally and they are valid for 12 hours. This is recommended if ticket key sharing between nghttpx instances is not required.</p>
<dt><code>&#8211;tls-ticket-key-memcached=&lt;HOST&gt;,&lt;PORT&gt;</code></p>
<dd> Specify address of memcached server to store session cache. This enables shared TLS ticket key between multiple nghttpx instances. nghttpx does not set TLS ticket key to memcached. The external ticket key generator is required. nghttpx just gets TLS ticket keys from memcached, and use them, possibly replacing current set of keys. It is up to extern TLS ticket key generator to rotate keys frequently. See &quot;TLS SESSION TICKET RESUMPTION&quot; section in manual page to know the data format in memcached entry.</p>
<dt><code>&#8211;tls-ticket-key-memcached-interval=&lt;DURATION&gt;</code></p>
<dd> Set interval to get TLS ticket keys from memcached. </p>
<p> Default: <code>10m</code></p>
<dt><code>&#8211;tls-ticket-key-memcached-max-retry=&lt;N&gt;</code></p>
<dd> Set maximum number of consecutive retries before abandoning TLS ticket key retrieval. If this number is reached, the attempt is considered as failure, and &quot;failure&quot; count is incremented by 1, which contributed to the value controlled <i>&#8211;tls-ticket-key-memcached-max-fail</i> option. </p>
<p> Default: <code>3</code></p>
<dt><code>&#8211;tls-ticket-key-memcached-max-fail=&lt;N&gt;</code></p>
<dd> Set maximum number of consecutive failure before disabling TLS ticket until next scheduled key retrieval. </p>
<p> Default: <code>2</code></p>
<dt><code>&#8211;tls-ticket-key-cipher=&lt;CIPHER&gt;</code></p>
<dd> Specify cipher to encrypt TLS session ticket. Specify either aes-128-cbc or aes-256-cbc. By default, aes-128-cbc is used.</p>
<dt><code>&#8211;fetch-ocsp-response-file=&lt;PATH&gt;</code></p>
<dd> Path to fetch-ocsp-response script file. It should be absolute path. </p>
<p> Default: <code>/usr/local/share/nghttp2/fetch-ocsp-response</code></p>
<dt><code>&#8211;ocsp-update-interval=&lt;DURATION&gt;</code></p>
<dd> Set interval to update OCSP response cache. </p>
<p> Default: <code>4h</code></p>
<dt><code>&#8211;no-ocsp</code></p>
<dd> Disable OCSP stapling.</p>
<dt><code>&#8211;tls-session-cache-memcached=&lt;HOST&gt;,&lt;PORT&gt;</code></p>
<dd> Specify address of memcached server to store session cache. This enables shared session cache between multiple nghttpx instances.</p>
<dt><code>&#8211;tls-dyn-rec-warmup-threshold=&lt;SIZE&gt;</code></p>
<dd> Specify the threshold size for TLS dynamic record size behaviour. During a TLS session, after the threshold number of bytes have been written, the TLS record size will be increased to the maximum allowed (16K). The max record size will continue to be used on the active TLS session. After <i>&#8211;tls-dyn-rec-idle-timeout</i> has elapsed, the record size is reduced to 1300 bytes. Specify 0 to always use the maximum record size, regardless of idle period. This behaviour applies to all TLS based frontends, and TLS HTTP/2 backends. </p>
<p> Default: <code>1M</code></p>
<dt><code>&#8211;tls-dyn-rec-idle-timeout=&lt;DURATION&gt;</code></p>
<dd> Specify TLS dynamic record size behaviour timeout. See <i>&#8211;tls-dyn-rec-warmup-threshold</i> for more information. This behaviour applies to all TLS based frontends, and TLS HTTP/2 backends. </p>
<p> Default: <code>1s</code></dl>
<h3>HTTP/2 and SPDY</h3>
<dl>
<dt><code>-c, &#8211;http2-max-concurrent-streams=&lt;N&gt;</code></p>
<dd> Set the maximum number of the concurrent streams in one HTTP/2 and SPDY session. </p>
<p> Default: <code>100</code></p>
<dt><code>&#8211;frontend-http2-window-bits=&lt;N&gt;</code></p>
<dd> Sets the per-stream initial window size of HTTP/2 SPDY frontend connection. For HTTP/2, the size is 2**&lt;N&gt;-1. For SPDY, the size is 2**&lt;N&gt;. </p>
<p> Default: <code>16</code></p>
<dt><code>&#8211;frontend-http2-connection-window-bits=&lt;N&gt;</code></p>
<dd> Sets the per-connection window size of HTTP/2 and SPDY frontend connection. For HTTP/2, the size is 2**&lt;N&gt;-1. For SPDY, the size is 2**&lt;N&gt;. </p>
<p> Default: <code>16</code></p>
<dt><code>&#8211;frontend-no-tls</code></p>
<dd> Disable SSL/TLS on frontend connections.</p>
<dt><code>&#8211;backend-http2-window-bits=&lt;N&gt;</code></p>
<dd> Sets the initial window size of HTTP/2 backend connection to 2**&lt;N&gt;-1. </p>
<p> Default: <code>16</code></p>
<dt><code>&#8211;backend-http2-connection-window-bits=&lt;N&gt;</code></p>
<dd> Sets the per-connection window size of HTTP/2 backend connection to 2**&lt;N&gt;-1. </p>
<p> Default: <code>16</code></p>
<dt><code>&#8211;backend-no-tls</code></p>
<dd> Disable SSL/TLS on backend connections.</p>
<dt><code>&#8211;http2-no-cookie-crumbling</code></p>
<dd> Don&#8217;t crumble cookie header field.</p>
<dt><code>&#8211;padding=&lt;N&gt;</code></p>
<dd> Add at most &lt;N&gt; bytes to a HTTP/2 frame payload as padding. Specify 0 to disable padding. This option is meant for debugging purpose and not intended to enhance protocol security.</p>
<dt><code>&#8211;no-server-push</code></p>
<dd> Disable HTTP/2 server push. Server push is supported by default mode and HTTP/2 frontend via Link header field. It is also supported if both frontend and backend are HTTP/2 (which implies <i>&#8211;http2-bridge</i> or <i>&#8211;client</i> mode). In this case, server push from backend session is relayed to frontend, and server push via Link header field is also supported. HTTP SPDY frontend does not support server push.</dl>
<h3>Mode</h3>
<dl>
<dt><code>(default mode)</code></p>
<dd> Accept HTTP/2, SPDY and HTTP/1.1 over SSL/TLS. If <i>&#8211;frontend-no-tls</i> is used, accept HTTP/2 and HTTP/1.1. The incoming HTTP/1.1 connection can be upgraded to HTTP/2 through HTTP Upgrade. The protocol to the backend is HTTP/1.1.</p>
<dt><code>-s, &#8211;http2-proxy</code></p>
<dd> Like default mode, but enable secure proxy mode.</p>
<dt><code>&#8211;http2-bridge</code></p>
<dd> Like default mode, but communicate with the backend in HTTP/2 over SSL/TLS. Thus the incoming all connections are converted to HTTP/2 connection and relayed to the backend. See <i>&#8211;backend-http-proxy-uri</i> option if you are behind the proxy and want to connect to the outside HTTP/2 proxy.</p>
<dt><code>&#8211;client</code></p>
<dd> Accept HTTP/2 and HTTP/1.1 without SSL/TLS. The incoming HTTP/1.1 connection can be upgraded to HTTP/2 connection through HTTP Upgrade. The protocol to the backend is HTTP/2. To use nghttpx as a forward proxy, use <i>-p</i> option instead.</p>
<dt><code>-p, &#8211;client-proxy</code></p>
<dd> Like <i>&#8211;client</i> option, but it also requires the request path from frontend must be an absolute URI, suitable for use as a forward proxy.</dl>
<h3>Logging</h3>
<dl>
<dt><code>-L, &#8211;log-level=&lt;LEVEL&gt;</code></p>
<dd> Set the severity level of log output. &lt;LEVEL&gt; must be one of INFO, NOTICE, WARN, ERROR and FATAL. </p>
<p> Default: <code>NOTICE</code></p>
<dt><code>&#8211;accesslog-file=&lt;PATH&gt;</code></p>
<dd> Set path to write access log. To reopen file, send USR1 signal to nghttpx.</p>
<dt><code>&#8211;accesslog-syslog</code></p>
<dd> Send access log to syslog. If this option is used, <i>&#8211;accesslog-file</i> option is ignored.</p>
<dt><code>&#8211;accesslog-format=&lt;FORMAT&gt;</code></p>
<dd> Specify format string for access log. The default format is combined format. The following variables are available:</p>
<dt>&bull;</p>
<dd> $remote_addr: client IP address.</p>
<dt>&bull;</p>
<dd> $time_local: local time in Common Log format.</p>
<dt>&bull;</p>
<dd> $time_iso8601: local time in ISO 8601 format.</p>
<dt>&bull;</p>
<dd> $request: HTTP request line.</p>
<dt>&bull;</p>
<dd> $status: HTTP response status code.</p>
<dt>&bull;</p>
<dd> $body_bytes_sent: the number of bytes sent to client as response body.</p>
<dt>&bull;</p>
<dd> $http_&lt;VAR&gt;: value of HTTP request header &lt;VAR&gt; where &#8216;_&#8217; in &lt;VAR&gt; is replaced with &#8216;-&#8216;.</p>
<dt>&bull;</p>
<dd> $remote_port: client port.</p>
<dt>&bull;</p>
<dd> $server_port: server port.</p>
<dt>&bull;</p>
<dd> $request_time: request processing time in seconds with milliseconds resolution.</p>
<dt>&bull;</p>
<dd> $pid: PID of the running process.</p>
<dt>&bull;</p>
<dd> $alpn: ALPN identifier of the protocol which generates the response. For HTTP/1, ALPN is always http/1.1, regardless of minor version.</p>
<dt>&bull;</p>
<dd> $ssl_cipher: cipher used for SSL/TLS connection.</p>
<dt>&bull;</p>
<dd> $ssl_protocol: protocol for SSL/TLS connection.</p>
<dt>&bull;</p>
<dd> $ssl_session_id: session ID for SSL/TLS connection.</p>
<dt>&bull;</p>
<dd> $ssl_session_reused: &quot;r&quot; if SSL/TLS session was reused. Otherwise, &quot;.&quot; </p>
<p> The variable can be enclosed by &quot;{&quot; and &quot;}&quot; for disambiguation (e.g., ${remote_addr}). </p>
<p> Default: <code>$remote_addr &#8211; &#8211; [$time_local] &quot;$request&quot; $status $body_bytes_sent &quot;$http_referer&quot; &quot;$http_user_agent&quot;</code></p>
<dt><code>&#8211;errorlog-file=&lt;PATH&gt;</code></p>
<dd> Set path to write error log. To reopen file, send USR1 signal to nghttpx. stderr will be redirected to the error log file unless <i>&#8211;errorlog-syslog</i> is used. </p>
<p> Default: <code>/dev/stderr</code></p>
<dt><code>&#8211;errorlog-syslog</code></p>
<dd> Send error log to syslog. If this option is used, <i>&#8211;errorlog-file</i> option is ignored.</p>
<dt><code>&#8211;syslog-facility=&lt;FACILITY&gt;</code></p>
<dd> Set syslog facility to &lt;FACILITY&gt;. </p>
<p> Default: <code>daemon</code></dl>
<h3>HTTP</h3>
<dl>
<dt><code>&#8211;add-x-forwarded-for</code></p>
<dd> Append X-Forwarded-For header field to the downstream request.</p>
<dt><code>&#8211;strip-incoming-x-forwarded-for</code></p>
<dd> Strip X-Forwarded-For header field from inbound client requests.</p>
<dt><code>&#8211;add-forwarded=&lt;LIST&gt;</code></p>
<dd> Append RFC 7239 Forwarded header field with parameters specified in comma delimited list &lt;LIST&gt;. The supported parameters are &quot;by&quot;, &quot;for&quot;, &quot;host&quot;, and &quot;proto&quot;. By default, the value of &quot;by&quot; and &quot;for&quot; parameters are obfuscated string. See <i>&#8211;forwarded-by</i> and <i>&#8211;forwarded-for</i> options respectively. Note that nghttpx does not translate non-standard X-Forwarded-* header fields into Forwarded header field, and vice versa.</p>
<dt><code>&#8211;strip-incoming-forwarded</code></p>
<dd> Strip Forwarded header field from inbound client requests.</p>
<dt><code>&#8211;forwarded-by=(obfuscated|ip|&lt;VALUE&gt;)</code></p>
<dd> Specify the parameter value sent out with &quot;by&quot; parameter of Forwarded header field. If &quot;obfuscated&quot; is given, the string is randomly generated at startup. If &quot;ip&quot; is given, the interface address of the connection, including port number, is sent with &quot;by&quot; parameter. User can also specify the static obfuscated string. The limitation is that it must start with &quot;_&quot;, and only consists of character set [A-Za-z0-9._-], as described in RFC 7239. </p>
<p> Default: <code>obfuscated</code></p>
<dt><code>&#8211;forwarded-for=(obfuscated|ip)</code></p>
<dd> Specify the parameter value sent out with &quot;for&quot; parameter of Forwarded header field. If &quot;obfuscated&quot; is given, the string is randomly generated for each client connection. If &quot;ip&quot; is given, the remote client address of the connection, without port number, is sent with &quot;for&quot; parameter. </p>
<p> Default: <code>obfuscated</code></p>
<dt><code>&#8211;no-via</code></p>
<dd> Don&#8217;t append to Via header field. If Via header field is received, it is left unaltered.</p>
<dt><code>&#8211;no-location-rewrite</code></p>
<dd> Don&#8217;t rewrite location header field on <i>&#8211;http2-bridge</i>, <i>&#8211;client</i> and default mode. For <i>&#8211;http2-proxy</i> and <i>&#8211;client-proxy</i> mode, location header field will not be altered regardless of this option.</p>
<dt><code>&#8211;host-rewrite</code></p>
<dd> Rewrite host and :authority header fields on <i>&#8211;http2-bridge</i>, <i>&#8211;client</i> and default mode. For <i>&#8211;http2-proxy</i> and <i>&#8211;client-proxy</i> mode, these headers will not be altered regardless of this option.</p>
<dt><code>&#8211;altsvc=&lt;PROTOID,PORT[,HOST,[ORIGIN]]&gt;</code></p>
<dd> Specify protocol ID, port, host and origin of alternative service. &lt;HOST&gt; and &lt;ORIGIN&gt; are optional. They are advertised in alt-svc header field only in HTTP/1.1 frontend. This option can be used multiple times to specify multiple alternative services. Example: <i>&#8211;altsvc</i>=h2,443</p>
<dt><code>&#8211;add-request-header=&lt;HEADER&gt;</code></p>
<dd> Specify additional header field to add to request header set. This option just appends header field and won&#8217;t replace anything already set. This option can be used several times to specify multiple header fields. Example: <i>&#8211;add-request-header</i>=&quot;foo: bar&quot;</p>
<dt><code>&#8211;add-response-header=&lt;HEADER&gt;</code></p>
<dd> Specify additional header field to add to response header set. This option just appends header field and won&#8217;t replace anything already set. This option can be used several times to specify multiple header fields. Example: <i>&#8211;add-response-header</i>=&quot;foo: bar&quot;</p>
<dt><code>&#8211;header-field-buffer=&lt;SIZE&gt;</code></p>
<dd> Set maximum buffer size for incoming HTTP request header field list. This is the sum of header name and value in bytes. </p>
<p> Default: <code>64K</code></p>
<dt><code>&#8211;max-header-fields=&lt;N&gt;</code></p>
<dd> Set maximum number of incoming HTTP request header fields, which appear in one request or response header field list. </p>
<p> Default: <code>100</code></dl>
<h3>Debug</h3>
<dl>
<dt><code>&#8211;frontend-http2-dump-request-header=&lt;PATH&gt;</code></p>
<dd> Dumps request headers received by HTTP/2 frontend to the file denoted in &lt;PATH&gt;. The output is done in HTTP/1 header field format and each header block is followed by an empty line. This option is not thread safe and MUST NOT be used with option <i>-n</i>&lt;N&gt;, where &lt;N&gt; &gt;= 2.</p>
<dt><code>&#8211;frontend-http2-dump-response-header=&lt;PATH&gt;</code></p>
<dd> Dumps response headers sent from HTTP/2 frontend to the file denoted in &lt;PATH&gt;. The output is done in HTTP/1 header field format and each header block is followed by an empty line. This option is not thread safe and MUST NOT be used with option <i>-n</i>&lt;N&gt;, where &lt;N&gt; &gt;= 2.</p>
<dt><code>-o, &#8211;frontend-frame-debug</code></p>
<dd> Print HTTP/2 frames in frontend to stderr. This option is not thread safe and MUST NOT be used with option <i>-n</i>=N, where N &gt;= 2.</dl>
<h3>Process</h3>
<dl>
<dt><code>-D, &#8211;daemon</code></p>
<dd> Run in a background. If <i>-D</i> is used, the current working directory is changed to &#8216;<i>/</i>&#8216;.</p>
<dt><code>&#8211;pid-file=&lt;PATH&gt;</code></p>
<dd> Set path to save PID of this program.</p>
<dt><code>&#8211;user=&lt;USER&gt;</code></p>
<dd> Run this program as &lt;USER&gt;. This option is intended to be used to drop root privileges.</dl>
<h3>Scripting</h3>
<dl>
<dt><code>&#8211;mruby-file=&lt;PATH&gt;</code></p>
<dd> Set mruby script file</dl>
<h3>Misc</h3>
<dl>
<dt><code>&#8211;conf=&lt;PATH&gt;</code></p>
<dd> Load configuration from &lt;PATH&gt;. </p>
<p> Default: <code>/etc/nghttpx/nghttpx.conf</code></p>
<dt><code>&#8211;include=&lt;PATH&gt;</code></p>
<dd> Load additional configurations from &lt;PATH&gt;. File &lt;PATH&gt; is read when configuration parser encountered this option. This option can be used multiple times, or even recursively.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print version and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this help and exit. </p>
<p> The &lt;SIZE&gt; argument is an integer and an optional unit (e.g., 10K is 10 * 1024). Units are K, M and G (powers of 1024). </p>
<p> The &lt;DURATION&gt; argument is an integer and an optional unit (e.g., 1s is 1 second and 500ms is 500 milliseconds). Units are h, m, s or ms (hours, minutes, seconds and milliseconds, respectively). If a unit is omitted, a second is used as unit.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/etc/nghttpx/nghttpx.conf</i></p>
<dd> The default configuration file path nghttpx searches at startup. The configuration file path can be changed using <i>&#8211;conf</i> option. </p>
<p> Those lines which are staring <code>#</code> are treated as comment. </p>
<p> The option name in the configuration file is the long command-line option name with leading <code>&#8212;</code> stripped (e.g., <code>frontend</code>). Put <code>=</code> between option name and value. Don&#8217;t put extra leading or trailing spaces. </p>
<p> When specifying arguments including characters which have special meaning to a shell, we usually use quotes so that shell does not interpret them. When writing this configuration file, quotes for this purpose must not be used. For example, specify additional request header field, do this: </p>
<pre>
add-request-header=foo: bar
</pre>
<p> instead of: </p>
<pre>
add-request-header=&quot;foo: bar&quot;
</pre>
<p> The options which do not take argument in the command-line <i>take</i> argument in the configuration file. Specify <code>yes</code> as an argument (e.g., <code>http2-proxy=yes</code>). If other string is given, it is ignored. </p>
<p> To specify private key and certificate file which are given as positional arguments in command-line, use <code>private-key-file</code> and <code>certificate-file</code>. </p>
<p> <i>&#8211;conf</i> option cannot be used in the configuration file and will be ignored if specified.</dl>
<h2>SIGNALS</h2>
<dl>
<dt><code>SIGQUIT</code></p>
<dd> Shutdown gracefully. First accept pending connections and stop accepting connection. After all connections are handled, nghttpx exits.</p>
<dt><code>SIGUSR1</code></p>
<dd> Reopen log files.</p>
<dt><code>SIGUSR2</code></p>
<dd> Fork and execute nghttpx. It will execute the binary in the same path with same command-line arguments and environment variables. After new process comes up, sending SIGQUIT to the original process to perform hot swapping. </p>
<p> <code>NOTE:</code> nghttpx consists of multiple processes: one process for processing these signals, and another one for processing requests. The former spawns the latter. The former is called master process, and the latter is called worker process. If neverbleed is enabled, the worker process spawns neverbleed daemon process which does RSA key processing. The above signal must be sent to the master process. If the other processes received one of them, it is ignored. This behaviour of these processes may change in the future release. In other words, in the future release, the processes other than master process may terminate upon the reception of these signals. Therefore these signals should not be sent to the processes other than master process.</dl>
<h2>SERVER PUSH</h2>
<p> nghttpx supports HTTP/2 server push in default mode with Link header field. nghttpx looks for Link header field (<i>RFC 5988</i>) in response headers from backend server and extracts URI-reference with parameter <code>rel=preload</code> (see <i>preload</i>) and pushes those URIs to the frontend client. Here is a sample Link header field to initiate server push: </p>
<pre>
Link: &lt;/fonts/font.woff&gt;; rel=preload
Link: &lt;/css/theme.css&gt;; rel=preload
</pre>
<p> Currently, the following restriction is applied for server push:</p>
<dl>
<dt>1.</p>
<dd> The associated stream must have method &quot;GET&quot; or &quot;POST&quot;. The associated stream&#8217;s status code must be 200. </p>
<p> This limitation may be loosened in the future release. </p>
<p> nghttpx also supports server push if both frontend and backend are HTTP/2 (which implies <i>&#8211;http2-bridge</i> or <i>&#8211;client</i>). In this case, in addition to server push via Link header field, server push from backend is relayed to frontend HTTP/2 session. </p>
<p> HTTP/2 server push will be disabled if <i>&#8211;http2-proxy</i> or <i>&#8211;client-proxy</i> is used.</dl>
<h2>UNIX DOMAIN SOCKET</h2>
<p> nghttpx supports UNIX domain socket with a filename for both frontend and backend connections. </p>
<p> Please note that current nghttpx implementation does not delete a socket with a filename. And on start up, if nghttpx detects that the specified socket already exists in the file system, nghttpx first deletes it. However, if SIGUSR2 is used to execute new binary and both old and new configurations use same filename, new binary does not delete the socket and continues to use it.</p>
<h2>OCSP STAPLING</h2>
<p> OCSP query is done using external Python script <code>fetch-ocsp-response</code>, which has been originally developed in Perl as part of h2o project (<i><a rel="nofollow" href="https://github.com/h2o/h2o">https://github.com/h2o/h2o</a></i>), and was translated into Python. </p>
<p> The script file is usually installed under <code>$(prefix)/share/nghttp2/</code> directory. The actual path to script can be customized using <i>&#8211;fetch-ocsp-response-file</i> option. </p>
<p> If OCSP query is failed, previous OCSP response, if any, is continued to be used.</p>
<h2>TLS SESSION RESUMPTION</h2>
<p> nghttpx supports TLS session resumption through both session ID and session ticket.</p>
<h3>SESSION ID RESUMPTION</h3>
<p> By default, session ID is shared by all worker threads. </p>
<p> If <i>&#8211;tls-session-cache-memcached</i> is given, nghttpx will insert serialized session data to memcached with <code>nghttpx:tls-session-cache:</code> + lowercased hex string of session ID as a memcached entry key, with expiry time 12 hours. Session timeout is set to 12 hours.</p>
<h3>TLS SESSION TICKET RESUMPTION</h3>
<p> By default, session ticket is shared by all worker threads. The automatic key rotation is also enabled by default. Every an hour, new encryption key is generated, and previous encryption key becomes decryption only key. We set session timeout to 12 hours, and thus we keep at most 12 keys. </p>
<p> If <i>&#8211;tls-ticket-key-memcached</i> is given, encryption keys are retrieved from memcached. nghttpx just reads keys from memcached; one has to deploy key generator program to update keys frequently (e.g., every 1 hour). The example key generator tlsticketupdate.go is available under contrib directory in nghttp2 archive. The memcached entry key is <code>nghttpx:tls-ticket-key</code>. The data format stored in memcached is the binary format described below: </p>
<pre><code>
+ -- -- -- -- -- -- --+-- -- -- -+-- -- -- -- -- -- -- --+ | VERSION(4) | LEN(2) | KEY(48 or 80)... + -- -- -- -- -- -- --+-- -- -- -+-- -- -- -- -- -- -- --+^ |
    | |
    +-- -- -- -- -- -- -- -- -- -- -- --+(LEN, KEY)pair can be repeated
</code></pre>
<p> All numbers in the above figure is bytes. All integer fields are network byte order. </p>
<p> First 4 bytes integer VERSION field, which must be 1. The 2 bytes integer LEN field gives the length of following KEY field, which contains key. If <i>&#8211;tls-ticket-key-cipher</i>=aes-128-cbc is used, LEN must be 48. If <i>&#8211;tls-ticket-key-cipher</i>=aes-256-cbc is used, LEN must be 80. LEN and KEY pair can be repeated multiple times to store multiple keys. The key appeared first is used as encryption key. All the remaining keys are used as decryption only. </p>
<p> If <i>&#8211;tls-ticket-key-file</i> is given, encryption key is read from the given file. In this case, nghttpx does not rotate key automatically. To rotate key, one has to restart nghttpx (see SIGNALS).</p>
<h2>MRUBY SCRIPTING</h2>
<p> <code>WARNING:</code> The current mruby extension API is experimental and not frozen. The API is subject to change in the future release. </p>
<p> nghttpx allows users to extend its capability using mruby scripts. nghttpx has 2 hook points to execute mruby script: request phase and response phase. The request phase hook is invoked after all request header fields are received from client. The response phase hook is invoked after all response header fields are received from backend server. These hooks allows users to modify header fields, or common HTTP variables, like authority or request path, and even return custom response without forwarding request to backend servers. </p>
<p> To specify mruby script file, use <i>&#8211;mruby-file</i> option. The script will be evaluated once per thread on startup, and it must instantiate object and evaluate it as the return value (e.g., <code>App.new</code>). This object is called app object. If app object defines <code>on_req</code> method, it is called with <i>Nghttpx::Env</i> object on request hook. Similarly, if app object defines <code>on_resp</code> method, it is called with <i>Nghttpx::Env</i> object on response hook. For each method invocation, user can can access <i>Nghttpx::Request</i> and <i>Nghttpx::Response</i> objects via <i>Nghttpx::Env#req</i> and <i>Nghttpx::Env#resp</i> respectively.</p>
<dl>
<dt><code>Nghttpx::REQUEST_PHASE</code></p>
<dd> Constant to represent request phase.</p>
<dt><code>Nghttpx::RESPONSE_PHASE</code></p>
<dd> Constant to represent response phase.</p>
<dt><code>class Nghttpx::Env</code></p>
<dd> Object to represent current request specific context.</p>
<dt><code>attribute [R] req</code></p>
<dd> Return <i>Request</i> object.</p>
<dt><code>attribute [R] resp</code></p>
<dd> Return <i>Response</i> object.</p>
<dt><code>attribute [R] ctx</code></p>
<dd> Return Ruby hash object. It persists until request finishes. So values set in request phase hoo can be retrieved in response phase hook.</p>
<dt><code>attribute [R] phase</code></p>
<dd> Return the current phase.</p>
<dt><code>attribute [R] remote_addr</code></p>
<dd> Return IP address of a remote client.</p>
<dt><code>class Nghttpx::Request</code></p>
<dd> Object to represent request from client. The modification to Request object is allowed only in request phase hook.</p>
<dt><code>attribute [R] http_version_major</code></p>
<dd> Return HTTP major version.</p>
<dt><code>attribute [R] http_version_minor</code></p>
<dd> Return HTTP minor version.</p>
<dt><code>attribute [R/W] method</code></p>
<dd> HTTP method. On assignment, copy of given value is assigned. We don&#8217;t accept arbitrary method name. We will document them later, but well known methods, like GET, PUT and POST, are all supported.</p>
<dt><code>attribute [R/W] authority</code></p>
<dd> Authority (i.e., example.org), including optional port component . On assignment, copy of given value is assigned.</p>
<dt><code>attribute [R/W] scheme</code></p>
<dd> Scheme (i.e., http, https). On assignment, copy of given value is assigned.</p>
<dt><code>attribute [R/W] path</code></p>
<dd> Request path, including query component (i.e., /index.html). On assignment, copy of given value is assigned. The path does not include authority component of URI.</p>
<dt><code>attribute [R] headers</code></p>
<dd> Return Ruby hash containing copy of request header fields. Changing values in returned hash does not change request header fields actually used in request processing. Use <i>Nghttpx::Request#add_header</i> or <i>Nghttpx::Request#set_header</i> to change request header fields.</p>
<dt><code>add_header(key, value)</code></p>
<dd> Add header entry associated with key. The value can be single string or array of string. It does not replace any existing values associated with key.</p>
<dt><code>set_header(key, value)</code></p>
<dd> Set header entry associated with key. The value can be single string or array of string. It replaces any existing values associated with key.</p>
<dt><code>clear_headers()</code></p>
<dd> Clear all existing request header fields.</p>
<dt><code>push uri</code></p>
<dd> Initiate to push resource identified by <i>uri</i>. Only HTTP/2 protocol supports this feature. For the other protocols, this method is noop. <i>uri</i> can be absolute URI, absolute path or relative path to the current request. For absolute or relative path, scheme and authority are inherited from the current request. Currently, method is always GET. nghttpx will issue request to backend servers to fulfill this request. The request and response phase hooks will be called for pushed resource as well.</p>
<dt><code>class Nghttpx::Response</code></p>
<dd> Object to represent response from backend server.</p>
<dt><code>attribute [R] http_version_major</code></p>
<dd> Return HTTP major version.</p>
<dt><code>attribute [R] http_version_minor</code></p>
<dd> Return HTTP minor version.</p>
<dt><code>attribute [R/W] status</code></p>
<dd> HTTP status code. It must be in the range [200, 999], inclusive. The non-final status code is not supported in mruby scripting at the moment.</p>
<dt><code>attribute [R] headers</code></p>
<dd> Return Ruby hash containing copy of response header fields. Changing values in returned hash does not change response header fields actually used in response processing. Use <i>Nghttpx::Response#add_header</i> or <i>Nghttpx::Response#set_header</i> to change response header fields.</p>
<dt><code>add_header(key, value)</code></p>
<dd> Add header entry associated with key. The value can be single string or array of string. It does not replace any existing values associated with key.</p>
<dt><code>set_header(key, value)</code></p>
<dd> Set header entry associated with key. The value can be single string or array of string. It replaces any existing values associated with key.</p>
<dt><code>clear_headers()</code></p>
<dd> Clear all existing response header fields.</p>
<dt><code>return(body)</code></p>
<dd> Return custom response <i>body</i> to a client. When this method is called in request phase hook, the request is not forwarded to the backend, and response phase hook for this request will not be invoked. When this method is called in response phase hook, response from backend server is canceled and discarded. The status code and response header fields should be set before using this method. To set status code, use :rb:meth To set response header fields, use <i>Nghttpx::Response#status</i>. If status code is not set, 200 is used. <i>Nghttpx::Response#add_header</i> and <i>Nghttpx::Response#set_header</i>. When this method is invoked in response phase hook, the response headers are filled with the ones received from backend server. To send completely custom header fields, first call <i>Nghttpx::Response#clear_headers</i> to erase all existing header fields, and then add required header fields. It is an error to call this method twice for a given request.</dl>
<h3>MRUBY EXAMPLES</h3>
<p> Modify request path: </p>
<pre>
class App
  def on_req(env)
    env.req.path = &quot;/apps#{env.req.path}&quot;
  end
end
App.new
</pre>
<p> Don&#8217;t forget to instantiate and evaluate object at the last line. </p>
<p> Restrict permission of viewing a content to a specific client addresses: </p>
<pre><code>
class App
    def
    on_req(env)
        allowed_clients = [ "127.0.0.1", "::1" ] if env.req.path.start_with
    ? ("/log/") &amp;&amp;
          !allowed_clients.include
    ? (env.remote_addr)then
      env.resp.status = 404 env.resp.return "permission denied" end
                        end
                        end
                        App.new
</code></pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-nghttp/">nghttp</a>(1)</i>, <i><a href="/docs/linux/man/1-nghttpd/">nghttpd</a>(1)</i>, <i><a href="/docs/linux/man/1-h2load/">h2load</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Tatsuhiro Tsujikawa</p>
<h2>COPYRIGHT</h2>
<p> 2012, 2015, 2016, Tatsuhiro Tsujikawa </p>
<h2>Index</h2>
