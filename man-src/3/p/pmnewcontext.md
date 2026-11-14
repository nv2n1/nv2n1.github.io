---
title: "pmnewcontext(3)"
name: "pmnewcontext"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pmnewcontext/"
description: "pmNewContext – establish a new PMAPI context"
---

<p><code>pmNewContext</code> &#8211; establish a new PMAPI context</p>
<h2>C Synopsis</h2>
<p><code> #include &lt;pcp/pmapi.h&gt; </p>
<p> int pmNewContext(int </code><i>type</i>, const char *<i>name</i>); </p>
<p> cc &#8230; -lpcp</p>
<h2>Description</h2>
<p>An application using the Performance Metrics Application Programming Interface (PMAPI) may manipulate several concurrent contexts, each associated with a source of performance metrics, e.g. <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on some host, or a set of archive logs of performance metrics as created by <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), or a standalone connection on the local host that does not involve <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). </p>
<p> <code>pmNewContext</code> may be used to establish a new context. The source of the metrics is identified by <i>name</i>, and may be either a host name (<i>type</i> is <code>PM_CONTEXT_HOST</code>), or a comma-separated list of names referring to a set of archive logs (<i>type</i> is <code>PM_CONTEXT_ARCHIVE</code>). Each element of the list may either be the base name common to all of the physical files of an archive log or the name of a directory containing archive logs. </p>
<p> For a <i>type</i> of <code>PM_CONTEXT_HOST</code>, in addition to identifying a host the <i>name</i> may also be used to encode additional optional information in the form of a <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) port number, a <code><a href="/docs/linux/man/1-pmproxy/">pmproxy</a></code>(1) hostname and a proxy port number. For example the <i>name</i> &quot;app23:14321,4321 [at] firewall.example.com:11111&quot; specifies a connection on port <i>14321</i> (or port <i>4321</i> if <i>14321</i> is unavailable) to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on the host <i>app23</i> via port <i>11111</i> to <code><a href="/docs/linux/man/1-pmproxy/">pmproxy</a></code>(1) on the host <i>firewall.example.com</i>. </p>
<p> For a <i>type</i> of <code>PM_CONTEXT_ARCHIVE</code>, each element of the list of names in <i>name</i> may also be the name of any of the physical files of an archive, e.g. <i>myarchive</i><code>.meta</code> (the metadata file) or <i>myarchive</i><code>.index</code> (the temporal index) or <i>myarchive</i><code>.0</code> (the first data volume of the archive) or <i>myarchive</i><code>.0.bz2</code> or <i>myarchive</i><code>.0.bz</code> (the first data volume compressed with <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1)) or <i>myarchive</i><code>.0.gz</code> or <i>myarchive</i><code>.0.Z</code> or <i>myarchive</i><code>.0.z</code> (the first data volume compressed with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1)), <i>myarchive</i><code>.1</code> or <i>myarchive</i><code>.3.bz2</code> or <i>myarchive</i><code>.42.gz</code> etc. </p>
<p> If more than one archive is specified for a <i>type</i> of <code>PM_CONTEXT_ARCHIVE</code>, there are some restrictions on the archives within the set:</p>
<dl>
<dt>&bull;</p>
<dd>The archives must all have been generated on the same host.</p>
<dt>&bull;</p>
<dd>The archives must not overlap in time.</p>
<dt>&bull;</p>
<dd>The archives must all have been created using the same time zone.</p>
<dt>&bull;</p>
<dd>The <i>PMID</i> of each metric should be the same in all of the archives. Multiple <i>PMID</i>s are currently tolerated by using the first <i>PMID</i> defined for each metric and ignoring subsequent <i>PMID</i>s.</p>
<dt>&bull;</p>
<dd>The type of each metric must be the same in all of the archives.</p>
<dt>&bull;</p>
<dd>The semantics of each metric must be the same in all of the archives.</p>
<dt>&bull;</p>
<dd>The units of each metric must be the same in all of the archives.</p>
<dt>&bull;</p>
<dd>The instance domain of each metric must be the same in all of the archives.</dl>
<p> In the case where <i>type</i> is <code>PM_CONTEXT_LOCAL</code>, <i>name</i> is ignored, and the context uses a standalone connection to the PMDA methods used by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). When this type of context is used, the range of accessible performance metrics is constrained to those from the operating system, and optionally the &#8220;proc&#8221;, &#8220;sample&#8221; and &#8220;ib&#8221; PMDAs. </p>
<p> In the case where <i>type</i> is <code>PM_CONTEXT_HOST</code>, additional flags can be added to the <i>type</i> to indicate if the connection to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) should be encrypted (<code>PM_CTXFLAG_SECURE</code>), deferred (<code>PM_CTXFLAG_SHALLOW</code>) and if the file descriptor used to communicate with <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), should not be shared across contexts (<code>PM_CTXFLAG_EXCLUSIVE</code>). The <code>PM_CTXFLAG_SHALLOW</code> flag is now deprecated and ignored. </p>
<p> The initial instance profile is set up to select all instances in all instance domains. In the case of a set of archives, the initial collection time is also set to zero, so that an initial <code><a href="/docs/linux/man/3-pmfetch/">pmFetch</a></code>(3) will result in the earliest set of metrics being returned from the set of archives. </p>
<p> Once established, the association between a context and a source of metrics is fixed for the life of the context, however routines are provided to independently manipulate both the instance profile (see <code><a href="/docs/linux/man/3-pmaddprofile/">pmAddProfile</a></code>(3) and <code><a href="/docs/linux/man/3-pmdelprofile/">pmDelProfile</a></code>(3)) and the collection time for archives (see <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3)). </p>
<p> <code>pmNewContext</code> returns a handle that may be used with subsequent calls to <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3). </p>
<p> The new context remains the current PMAPI context for all subsequent calls across the PMAPI, until another call to <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) is made, or the context is explicitly changed with a call to <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3) or <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3), or destroyed using <code><a href="/docs/linux/man/3-pmdestroycontext/">pmDestroyContext</a></code>(3). </p>
<p> When attempting to connect to a remote <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) on a machine that is booting, <code>pmNewContext</code> could potentially block for a long time until the remote machine finishes its initialization. <code>pmNewContext</code> will abort and return an error if the connection has not been established after some specified interval has elapsed. The default interval is 5 seconds. This may be modified by setting <code>PMCD_CONNECT_TIMEOUT</code> in the environment to a real number of seconds for the desired timeout. This is most useful in cases where the remote host is at the end of a slow network, requiring longer latencies to establish the connection correctly.</p>
<h2>Environment</h2>
<dl>
<dt><code>PMCD_CONNECT_TIMEOUT</code></p>
<dd>Timeout period (in seconds) for <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) connection attempts.</p>
<dt><code>PMCD_PORT</code></p>
<dd>TCP/IP port(s) for connecting to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), historically was 4321 and more recently the officially registered port 44321; in the current release, <code>pmcd</code> listens on both these ports as a transitional arrangement. If used, should be set to a comma-separated list of numerical port numbers.</p>
<dt><code>PMDA_PATH</code></p>
<dd>When searching for PMDAs to be loaded when <i>type</i> is <code>PM_CONTEXT_LOCAL</code>, the <code>PMDA_PATH</code> environment variable may be used to define a search path of directories to be used to locate the PMDA executables. The default search path is <code>$PCP_SHARE_DIR/lib:/usr/pcp/lib</code>.</dl>
<h2>Caveats</h2>
<p>When using a <i>type</i> of <code>PM_CONTEXT_LOCAL</code>, the operating system PMDA may export data structures directly from the kernel, which means that the <code>pmNewContext</code> caller should be an executable program compiled for the same object code format as the booted kernel. </p>
<p> In addition, applications using a <code>PM_CONTEXT_LOCAL</code> context must be single-threaded because the various DSO PMDAs may not be thread-safe. This restriction is enforced at the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), where routines may return the error code <code>PM_ERR_THREAD</code> if the library detects calls from more than one thread. </p>
<p> Applications that use <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) should exercise caution because the static fields in <i>struct hostent</i> may not be preserved across some <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) calls. In particular, <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a></code>(3) and <code><a href="/docs/linux/man/3-pmreconnectcontext/">pmReconnectContext</a></code>(3) both may call <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3) internally.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmproxy/">pmproxy</a></code>(1), <code><a href="/docs/linux/man/3-pmaddprofile/">pmAddProfile</a></code>(3), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/3-pmdelprofile/">pmDelProfile</a></code>(3), <code><a href="/docs/linux/man/3-pmdestroycontext/">pmDestroyContext</a></code>(3), <code><a href="/docs/linux/man/3-pmdupcontext/">pmDupContext</a></code>(3), <code><a href="/docs/linux/man/3-pmgetconfig/">pmGetConfig</a></code>(3), <code><a href="/docs/linux/man/3-pmreconnectcontext/">pmReconnectContext</a></code>(3), <code><a href="/docs/linux/man/3-pmsetmode/">pmSetMode</a></code>(3), <code><a href="/docs/linux/man/3-pmusecontext/">pmUseContext</a></code>(3), <code><a href="/docs/linux/man/3-pmwhichcontext/">pmWhichContext</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>Diagnostics</h2>
<p><code>PM_ERR_PERMISSION</code></p>
<dl>
<dd>No permission to perform requested operation</dl>
<p> <code>PM_ERR_CONNLIMIT</code></p>
<dl>
<dd>PMCD connection limit for this host exceeded</dl>
<p> <code>PM_ERR_NOCONTEXT</code></p>
<dl>
<dd>Requested context type was not <code>PM_CONTEXT_LOCAL</code>, <code>PM_CONTEXT_HOST </code> or <code>PM_CONTEXT_ARCHIVE</code>.</dl>
<p> <code>PM_ERR_LOGOVERLAP</code></p>
<dl>
<dd>Archives overlap in time</dl>
<p> <code>PM_ERR_LOGHOST</code></p>
<dl>
<dd>Archives differ by host</dl>
<p> <code>PM_ERR_LOGTIMEZONE</code></p>
<dl>
<dd>Archives differ by time zone.</dl>
<p> <code>PM_ERR_LOGCHANGETYPE</code></p>
<dl>
<dd>The type of a metric differs among archives</dl>
<p> <code>PM_ERR_LOGCHANGESEM</code></p>
<dl>
<dd>The semantics of a metric differs among archives</dl>
<p> <code>PM_ERR_LOGCHANGEINDOM</code></p>
<dl>
<dd>The instance domain of a metric differs among archives</dl>
<p> <code>PM_ERR_LOGCHANGEUNITS</code></p>
<dl>
<dd>The units of a metric differs among archives </p>
</dl>
