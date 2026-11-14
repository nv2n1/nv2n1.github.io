---
title: "apt-transport-http(1)"
name: "apt-transport-http"
section: "1"
letter: "a"
url: "/docs/linux/man/1-apt-transport-http/"
description: "apt-transport-http – APT transport for downloading via the Hypertext Transfer Protocol (HTTP)"
---

<h2 class="name">NAME</h2>
<p> apt-transport-http &#8211; APT transport for downloading via the Hypertext Transfer Protocol (HTTP) </p>
<h2>DESCRIPTION</h2>
<p> This APT transport allows the use of repositories accessed via the Hypertext Transfer Protocol (HTTP). It is available by default and probably the most used of all transports. Note that a transport is never called directly by a user but used by APT tools based on user configuration. </p>
<p> HTTP is an unencrypted transport protocol meaning that the whole communication with the remote server (or proxy) can be observed by a sufficiently capable attacker commonly referred to as a &quot;man in the middle&quot; (MITM). However, such an attacker can <i>not</i> modify the communication to compromise the security of your system, as APT&#8217;s data security model is independent of the chosen transport method. This is explained in detail in <code><a href="/docs/linux/man/8-apt-secure/">apt-secure</a></code>(8). An overview of available transport methods is given in <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5).</p>
<h2>OPTIONS</h2>
<p> Various options can be set in an <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) file to modify its behavior, ranging from proxy configuration to workarounds for specific server limitations.</p>
<h3>Proxy Configuration</h3>
<p> The environment variable <code>http_proxy</code> is supported for system wide configuration. Proxies specific to APT can be configured via the option Acquire::http::Proxy. Proxies which should be used only for certain hosts can be specified via Acquire::http::Proxy::<i>host</i>. Even more fine-grained control can be achieved via proxy autodetection, detailed further below. All these options use the URI format <i>scheme</i>://[[<i>user</i>][:<i>pass</i>]@]<i>host</i>[:<i>port</i>]/. Supported URI schemes are socks5h (SOCKS5 with remote DNS resolution), http and https. Authentication details can be supplied via <code><a href="/docs/linux/man/5-apt_auth-conf/">apt_auth.conf</a></code>(5) instead of including it in the URI directly. </p>
<p> The various APT configuration options support the special value DIRECT meaning that no proxy should be used. The environment variable <code>no_proxy</code> is also supported for the same purpose. </p>
<p> Furthermore, there are three settings provided for cache control with HTTP/1.1 compliant proxy caches: Acquire::http::No-Cache tells the proxy not to use its cached response under any circumstances. Acquire::http::Max-Age sets the allowed maximum age (in seconds) of an index file in the cache of the proxy. Acquire::http::No-Store specifies that the proxy should not store the requested archive files in its cache, which can be used to prevent the proxy from polluting its cache with (big) .deb files.</p>
<h3>Automatic Proxy Configuration</h3>
<p> Acquire::http::Proxy-Auto-Detect can be used to specify an external command to discover the HTTP proxy to use. The first and only parameter is a URI denoting the host to be contacted, to allow for host-specific configuration. APT expects the command to output the proxy on stdout as a single line in the previously specified URI format or the word DIRECT if no proxy should be used. No output indicates that the generic proxy settings should be used. </p>
<p> Note that auto-detection will not be used for a host if a host-specific proxy configuration is already set via Acquire::http::Proxy::<i>host</i>. </p>
<p> See the <code><a href="/docs/linux/man/1-squid-deb-proxy-client/">squid-deb-proxy-client</a></code>(1) and <code><a href="/docs/linux/man/1-auto-apt-proxy/">auto-apt-proxy</a></code>(1) packages for example implementations. </p>
<p> This option takes precedence over the legacy option name Acquire::http::ProxyAutoDetect.</p>
<h3>Connection Configuration</h3>
<p> The option Acquire::http::Timeout sets the timeout timer used by the method; this value applies to the connection as well as the data timeout. </p>
<p> The used bandwidth can be limited with Acquire::http::Dl-Limit which accepts integer values in kilobytes per second. The default value is 0 which deactivates the limit and tries to use all available bandwidth. Note that this option implicitly disables downloading from multiple servers at the same time. </p>
<p> The setting Acquire::http::Pipeline-Depth can be used to enable HTTP pipelining (RFC 2616 section 8.1.2.2) which can be beneficial e.g. on high-latency connections. It specifies how many requests are sent in a pipeline. APT tries to detect and work around misbehaving webservers and proxies at runtime, but if you know that yours does not conform to the HTTP/1.1 specification, pipelining can be disabled by setting the value to 0. It is enabled by default with the value 10. </p>
<p> Acquire::http::AllowRedirect controls whether APT will follow redirects, which is enabled by default. </p>
<p> Acquire::http::User-Agent can be used to set a different User-Agent for the http download method as some proxies allow access for clients only if the client uses a known identifier. </p>
<p> Acquire::http::SendAccept is enabled by default and sends an Accept: text/* header field to the server for requests without file extensions to prevent the server from attempting content negotiation.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre><code>
Acquire::http
{
    Proxy::example.org "DIRECT";
    Proxy "socks5h://apt:pass [at] 127.0.0.1:9050";
    Proxy - Auto - Detect "/usr/local/bin/apt-http-proxy-auto-detect";
    No - Cache "true";
    Max - Age "3600";
    No - Store "true";
    Timeout "10";
    Dl - Limit "42";
    Pipeline - Depth "0";
    AllowRedirect "false";
    User - Agent "My APT-HTTP";
    SendAccept "false";
};
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-apt-conf/">apt.conf</a></code>(5) <code><a href="/docs/linux/man/5-apt_auth-conf/">apt_auth.conf</a></code>(5) <code><a href="/docs/linux/man/5-sources-list/">sources.list</a></code>(5)</p>
<h2>BUGS</h2>
<p> m[blue]<code>APT bug page</code>m[]<font SIZE="-2">[1]</font>. If you wish to report a bug in APT, please see /usr/share/doc/debian/bug-reporting.txt or the <code><a href="/docs/linux/man/1-reportbug/">reportbug</a></code>(1) command.</p>
<h2>AUTHOR</h2>
<p> <code>APT team</code></p>
<dl>
<dt>
<dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> APT bug page</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://bugs.debian.org/src:apt">http://bugs.debian.org/src:apt</a></dl>
</dl>
<h2>Index</h2>
