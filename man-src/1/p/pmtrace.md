---
title: "pmtrace(1)"
name: "pmtrace"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmtrace/"
description: "pmtrace – command line performance instrumentation"
---

<h2>NAME</h2>
<p> <code>pmtrace</code> &#8211; command line performance instrumentation</p>
<h2>SYNOPSIS</h2>
<p> <code>pmtrace</code> [<code>-q</code>] [<code>-c</code> <i>value</i> | <code>-e</code> <i>command</i> | <code>-v</code> <i>value</i>] [<code>-h</code> <i>host</i>] [<code>-S</code> <i>state</i>] <i>tag</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pmtrace</code> provides a simple command line interface to the trace Performance Metrics Domain Agent (PMDA) and the associated <i>pcp_trace</i> library. </p>
<p> The default <code>pmtrace</code> behavior is to provide point trace data to the trace PMDA, using the <i>tag</i> argument as the identifying name associated with each trace point. The <i>tag</i> then becomes an instance identifier within the set of trace.point metrics. </p>
<p> The <code>-e</code> option allows an arbitrary <i>command</i> to be executed. This <i>command</i> will be measured as a transaction since it has well defined start and end points. The information is made available through the trace.transact metrics. </p>
<p> Trace data can be sent to the trace PMDA running on <i>host</i>, rather than the localhost, using the <code>-h</code> option. This overrides use of the environment variable <code>PCP_TRACE_HOST</code>. </p>
<p> The <code>-q</code> option suppresses messages from a successful trace, so that <code>pmtrace</code> runs quietly. </p>
<p> The <code>-c</code> option allows an arbitrary counter <i>value</i> to be exported through the trace.count metrics, while the <code>-v</code> option allows an arbitrary floating point <i>value</i> to be exported through the trace.observe metrics </p>
<p> The <code>-S</code> option enables internal debugging and tracing. The value of <i>state</i> is a bit-wise combination of debug flags as defined in <code><a href="/docs/linux/man/3-pmtracestate/">pmtracestate</a></code>(3), and may be specified using the decimal or hexadecimal syntax prescribed by <code><a href="/docs/linux/man/3-strtol/">strtol</a></code>(3). </p>
<h2>ENVIRONMENT</h2>
<p> Since <code>pmtrace</code> uses the <i>libpcp_trace</i> library routines, the environment variables <code>PCP_TRACE_HOST</code>, <code>PCP_TRACE_PORT</code>, and <code>PCP_TRACE_TIMEOUT</code> are all honored. Refer to <code><a href="/docs/linux/man/3-pmdatrace/">pmdatrace</a></code>(3) for a detailed description of the semantics of each.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_DEMOS_DIR/trace/pmtrace.c</code></p>
<dd> source code for <code>pmtrace</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdatrace/">pmdatrace</a></code>(1), <code><a href="/docs/linux/man/1-pmprobe/">pmprobe</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), and <code><a href="/docs/linux/man/3-pmdatrace/">pmdatrace</a></code>(3).</p>
<h2>DIAGNOSTICS</h2>
<p> All are generated on standard error and are intended to be self-explanatory. </p>
<p> The <code>pmtrace</code> exit status is always zero except when the <code>-e</code> option is in use, in which case the exit status of <i>command</i> is returned. </p>
<h2>Index</h2>
