---
title: "curlopt_proxy(3)"
name: "curlopt_proxy"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_proxy/"
description: "CURLOPT_PROXY – set proxy to use"
---

<p>CURLOPT_PROXY &#8211; set proxy to use</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_PROXY, char *proxy);</p>
<h2>Description</h2>
<p>Set the <i>proxy</i> to use for the upcoming request. The parameter should be a char * to a zero terminated string holding the host name or dotted IP address. </p>
<p> To specify port number in this string, append :[port] to the end of the host name. The proxy&#8217;s port number may optionally be specified with the separate option <i><a href="/docs/linux/man/3-curlopt_proxyport/">CURLOPT_PROXYPORT</a>(3)</i>. If not specified, libcurl will default to using port 1080 for proxies. </p>
<p> The proxy string may be prefixed with [scheme]:// to specify which kind of proxy is used. Use socks4://, socks4a://, socks5:// or socks5h:// (the last one to enable socks5 and asking the proxy to do the resolving, also known as <i>CURLPROXY_SOCKS5_HOSTNAME</i> type) to request the specific SOCKS version to be used. No protocol specified, http:// and all others will be treated as HTTP proxies. </p>
<p> Without a scheme prefix, <i><a href="/docs/linux/man/3-curlopt_proxytype/">CURLOPT_PROXYTYPE</a>(3)</i> can be used to specify which kind of proxy the string identifies. </p>
<p> When you tell the library to use a HTTP proxy, libcurl will transparently convert operations to HTTP even if you specify an FTP URL etc. This may have an impact on what other features of the library you can use, such as <i><a href="/docs/linux/man/3-curlopt_quote/">CURLOPT_QUOTE</a>(3)</i> and similar FTP specifics that don&#8217;t work unless you tunnel through the HTTP proxy. Such tunneling is activated with <i><a href="/docs/linux/man/3-curlopt_httpproxytunnel/">CURLOPT_HTTPPROXYTUNNEL</a>(3)</i>. </p>
<p> libcurl respects the environment variables <code>http_proxy</code>, <code>ftp_proxy</code>, <code>all_proxy</code> etc, if any of those are set. The <i><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a>(3)</i> option does however override any possibly set environment variables. </p>
<p> Setting the proxy string to &quot;&quot; (an empty string) will explicitly disable the use of a proxy, even if there is an environment variable set for it. </p>
<p> A proxy host string given in an environment variable can also include protocol scheme (<a rel="nofollow" href="http://)">http://)</a> and embedded user + password.</p>
<h2>Default</h2>
<p>Default is NULL, meaning no proxy is used. </p>
<p> When you set a host name to use, do not assume that there&#8217;s any particular single port number used widely for proxies. Specify it!</p>
<h2>Protocols</h2>
<p>All except file://. Note that some protocols don&#8217;t do very well over proxy.</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Since 7.14.1 the proxy environment variable names can include the protocol scheme. </p>
<p> Since 7.21.7 the proxy string supports the socks protocols as &quot;schemes&quot;.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if proxies are supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_proxyport/">CURLOPT_PROXYPORT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_httpproxytunnel/">CURLOPT_HTTPPROXYTUNNEL</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_proxytype/">CURLOPT_PROXYTYPE</a></code>(3)</p>
