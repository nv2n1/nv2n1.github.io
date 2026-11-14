---
title: "pmdiscoverservices(3)"
name: "pmdiscoverservices"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmdiscoverservices/"
description: "pmDiscoverServices – discover PCP services on the network"
---

<p><code>pmDiscoverServices</code> &#8211; discover PCP services on the network</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> </code></p>
<pre>int pmDiscoverServices(const char *<i>service</i>, const char *<i>mechanism</i>, char ***<i>urls</i>);</pre>
<p>#include &lt;pcp/impl.h&gt; </p>
<pre>int __pmDiscoverServicesWithOptions(const char *<i>service</i>, const char *<i>mechanism</i>, const char *<i>optionsString</i>, const volatile unsigned *<i>flags</i>, char ***<i>urls</i>);</pre>
<p>cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>Given a PCP service name, as identified by <i>service</i>, and using the type of discovery optionally specified in <i>mechanism</i>, <code>pmDiscoverServices</code> returns, via <i>urls</i>, a list of URLs representing the services discovered on the network. </p>
<p> The internal function <code>__pmDiscoverServicesWithOptions</code> performs the same function and adds arguments for global options and a mechanism for interrupting the discovery process. </p>
<p> The <code><a href="/docs/linux/man/1-pmfind/">pmfind</a></code>(1) utility provides command line access to both of these interfaces. </p>
<p> Calling </p>
<p> pmDiscoverServices(<i>service</i>, <i>mechanism</i>, <i>urls</i>) </p>
<p> is equivalent to calling </p>
<p> __pmDiscoverServicesWithOptions(<i>service</i>, <i>mechanism</i>, NULL, NULL, <i>urls</i>); </p>
<p> <i>service</i> specifies the PCP service to be discovered. Currently supported services are <code>PM_SERVER_SERVICE_SPEC,</code> <code>PM_PROXY_SERVICE_SPEC</code> and <code>PM_WEBD_SERVICE_SPEC,</code> which search for <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmproxy/">pmproxy</a></code>(1), and <code><a href="/docs/linux/man/1-pmwebd/">pmwebd</a></code>(1), servers respectively. </p>
<p> <i>mechanism</i> specifies the style of discovery to be used. </p>
<p> The currently supported mechanisms are:</p>
<dl>
<dt><code>avahi</code></p>
<dd>This searches for services which are broadcasting using mDNS via <code><a href="/docs/linux/man/8-avahi-daemon/">avahi-daemon</a></code>(8). An optional suffix <code>&quot;,timeout=N&quot;</code> may be added to specify the discovery timeout in floating-point multiples of one second. The default timeout is 0.5 seconds, which may be overridden by the <code>AVAHI_DISCOVERY_TIMEOUT</code> environment variable, also specified in floating-point multiples of one second. If both are specified, then the value specified in the environment variable takes precedence.</p>
<dt><code>probe=&lt;net-address&gt;/&lt;mask-bits&gt;</code></p>
<dd>Actively probes the given subnet for the requested PCP service(s). &lt;net-address&gt; is an inet or ipv6 network address and &lt;mask-bits&gt; is the number of bits used to define the subnet. For example, 192.168.1.0/24 defines an 8 bit subnet consisting of the addresses 192.168.1.0 through 192.168.1.255. An optional suffix <code>&quot;,maxThreads=N&quot;</code> may be added to limit the number of threads used while probing. The default is no fixed limit, which is to say that the process&#8217; rlimits for the number of threads and open file descriptors will be respected. An optional suffix <code>&quot;,timeout=N&quot;</code> may be added to specify the timeout for each connection attempt in floating-point multiples of one second. The default timeout is 20 milliseconds.</dl>
<p> <i>mechanism</i> may also be NULL, which means to use all available discovery mechanisms. </p>
<p> For <code>__pmDiscoverServicesWithOptions,</code> <i>optionsString</i> specifies global options to be applied to the discovery process. Options are comma-separated and may be one or more of the following:</p>
<dl>
<dt><code>resolve</code></p>
<dd>This requests that DNS name resolution be attempted for the addresses of any discovered services.</p>
<dt><code>timeout=N</code></p>
<dd>This specifies a timeout period after which the discovery process will be interrupted. N is a floating point number representing the number of seconds before timing out.</dl>
<p> <i>optionsString</i> may also be NULL, which means that no global options are specified. </p>
<p> For <code>__pmDiscoverServicesWithOptions,</code> <i>flags</i> specifies a pointer to an object of type <i>unsigned</i> which is a bit mask of options/status flags for the discovery process. The supported flags are:</p>
<dl>
<dt><code>PM_SERVICE_DISCOVERY_RESOLVE</code></p>
<dd>Specifying this flag is equivalent to specifying <i>resolve</i> in the <i>optionsString</i></p>
<dt><code>PM_SERVICE_DISCOVERY_INTERRUPTED</code></p>
<dd>This flag must be unset when calling <code>__pmDiscoverServicesWithOptions</code> but may be set asynchronously (by an interrupt handler, for example) in order to interrupt the service discovery process.</dl>
<p> <i>flags</i> may also be NULL, which indicates that no flags are set. </p>
<p> <code>pmDiscoverServices</code> and <code>__pmDiscoverServicesWithOptions</code> will return the number of services discovered, else a value less than zero for an error. The value zero indicates that no services were discovered. </p>
<p> The resulting list of pointers, <i>urls</i>, <code>and</code> the values (the URLs) that the pointers reference will have been allocated by <code>pmDiscoverServices</code> or <code>__pmDiscoverServicesWithOptions</code> with a single call to <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), and it is the responsibility of the <code>pmDiscoverServices</code> or <code>__pmDiscoverServicesWithOptions</code> caller to <code>free</code>(<i>urls</i>) to release the space when it is no longer required. </p>
<p> When an error occurs, or no services are discovered, <i>urls</i> is undefined (no space will have been allocated, and so calling <code><a href="/docs/linux/man/3-free/">free</a></code>(3) is a singularly bad idea).</p>
<h2>Pcp Environment</h2>
<p>Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5). Values for these variables may be obtained programmatically using the <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3) function.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmproxy/">pmproxy</a></code>(1), <code><a href="/docs/linux/man/1-pmwebd/">pmwebd</a></code>(1), <code><a href="/docs/linux/man/1-pmfind/">pmfind</a></code>(1), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/8-avahi-daemon/">avahi-daemon</a></code>(8).</p>
<h2>Diagnostics</h2>
<dl>
<dt><code>-EINVAL</code></p>
<dd>An invalid argument has been specified.</p>
<dt><code>-ENOMEM</code></p>
<dd>Unable to allocate memory required to process the request.</p>
<dt><code>-EOPNOTSUPP</code></p>
<dd>The specified <i>mechanism</i> is not supported. </p>
</dl>
