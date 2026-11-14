---
title: "pmreconnectcontext(3)"
name: "pmreconnectcontext"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmreconnectcontext/"
description: "pmReconnectContext – reconnect to a PMAPI context"
---

<p><code>pmReconnectContext</code> &#8211; reconnect to a PMAPI context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmReconnectContext(int </code><i>handle</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>As a consequence of network, host or Performance Metrics Collector Daemon (PMCD) failures, an application&#8217;s connection to a PMCD may be established and then subsequently lost. </p>
<p> The routine <code>pmReconnectContext</code> allows an application to request that the context identified by <i>handle</i> should be re-established, provided the associated metrics source is accessible. </p>
<p> When the source of metrics associated with the context <i>handle</i> is <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), then to avoid flooding the system with reconnect requests, <code>pmReconnectContext</code> will only attempt a reconnection after a suitable delay from the previous unsuccessful attempt to reconnect this context. This imposed restriction on the reconnect re-try time interval uses an exponential back-off so that the initial delay is 5 seconds after the first unsuccessful attempt, then 10 seconds, then 20 seconds, then 40 seconds and then 80 seconds thereafter. </p>
<p> The environment variable <code>PMCD_RECONNECT_TIMEOUT</code> may be used to redefine the back-off intervals, see <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3). </p>
<p> Calling <code>pmReconnectContext</code> with a handle identifying a currently connected <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) context will cause the connection to be broken before any reconnection is attempted. </p>
<p> If <i>handle</i> identifies a context associated with an archive source of metrics, <code>pmReconnectContext</code> returns without delay. </p>
<p> If the reconnection succeeds, <code>pmReconnectContext</code> returns <i>handle</i>. </p>
<p> As a side-effect of reconnecting, any derived metrics that have previously been defined using <code><a href="/docs/linux/man/3-pmregisterderived/">pmRegisterDerived</a></code>(3), <code><a href="/docs/linux/man/3-pmregisterderivedmetric/">pmRegisterDerivedMetric</a></code>(3) or <code><a href="/docs/linux/man/3-pmloadderivedconfig/">pmLoadDerivedConfig</a></code>(3) will be re-processed and re-bound to the available metrics from the reconnected source. The support of dynamic definition for derived metrics provides one use case where <code>pmReconnectContext</code> may be called even if the connection to the metrics source has not been lost. </p>
<p> Note that even in the case of a successful reconnection, <code>pmReconnectContext</code> does not change the current Performance Metrics Application Programming Interface (PMAPI) context, so <i>handle</i> remains valid. </p>
<p> When attempting to connect to a remote <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on a machine that is booting, <code>pmReconnectContext</code> could potentially block for a long time until the remote machine finishes its initialization. <code>pmReconnectContext</code> will abort and return an error if the connection has not been established after some specified interval has elapsed. The default interval is 5 seconds. This may be modified by setting <code>PMCD_CONNECT_TIMEOUT</code> in the environment to a real number of seconds for the desired timeout. This is most useful in cases where the remote host is at the end of a slow network, requiring longer latencies to establish the connection correctly.</p>
<h2>Environment</h2>
<dl>
<dt><code>PMCD_CONNECT_TIMEOUT</code></p>
<dd>Timeout period (in seconds) for <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) connection attempts.</p>
<dt><code>PMCD_RECONNECT_TIMEOUT</code></p>
<dd>Redefines the back-off intervals &#8211; refer to <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmloadderivedconfig/">pmLoadDerivedConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3), <code><a href="/docs/linux/man/3-pmregisterderived/">pmRegisterDerived</a></code>(3), <code><a href="/docs/linux/man/3-pmregisterderivedmetric/">pmRegisterDerivedMetric</a></code>(3) and <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3).</p>
<h2>Diagnostics</h2>
<p><code>PM_ERR_NOCONTEXT</code></p>
<dl>
<dd><i>handle</i> does not identify a valid PMAPI context</dl>
<p> <code>-ETIMEDOUT</code></p>
<dl>
<dd>The re-try time has not elapsed, or the reconnection is attempted and fails.</dl>
<h2>Caveat</h2>
<p>Applications that use <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) should exercise caution because the static fields in <i>struct hostent</i> may not be preserved across some <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) calls. In particular, <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) and <code><a href="/docs/linux/man/3-pmreconnectcontext/">pmReconnectContext</a></code>(3) both may call <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) internally.</p>
