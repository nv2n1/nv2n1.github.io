---
title: "pmdatrace(1)"
name: "pmdatrace"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdatrace/"
description: "pmdatrace – application-level transaction performance metrics domain agent"
---

<h2>NAME</h2>
<p> <code>pmdatrace</code> &#8211; application-level transaction performance metrics domain agent</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/trace/pmdatrace</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-A</code> <i>access</i>] [<code>-I</code> <i>port</i>] [<code>-M</code> <i>username</i>] [<code>-N</code> <i>buckets</i>] [<code>-T</code> <i>period</i>] [<code>-U</code> <i>units</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>pmdatrace</code> is a Performance Metrics Domain Agent (PMDA) which exports transaction performance metrics from application processes which use the <i>pcp_trace</i> library described in <code><a href="/docs/linux/man/3-pmdatrace/">pmdatrace</a></code>(3). </p>
<p> A brief description of the <code>pmdatrace</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>trace.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdatrace</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-A</code></p>
<dd> Host-based access control for <code>pmdatrace</code>. <i>access</i> must be either an allow or deny specification, using either allow:hostspec:maxconns or disallow:hostspec, where `allow&#8217; and `disallow&#8217; are keywords, `hostspec&#8217; is a host specification conforming to the format used by both <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), and `maxconns&#8217; is the maximum number of connections allowed from a given `hostspec&#8217;. Using a maximum connections of zero specifies an unlimited number of connections for the accompanying `hostspec&#8217;.</p>
<dt><code>-I</code></p>
<dd> Communicate with <i>pcp_trace</i> clients via the given Internet <i>port</i>. This can alternatively be specified by setting <code>$PCP_TRACE_PORT</code> in the environment to some valid port number (use of the <code>-I</code> option overrides this). The default port number is 4323.</p>
<dt><code>-T</code></p>
<dd> <i>period</i> defines the aggregation period used to compute the recent averages and extrema. Specified as a time interval using the syntax described in <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for the common <code>-t</code> PCP argument, e.g. <code>30 seconds</code> or <code>1 min</code>. The default is 60 seconds.</p>
<dt><code>-M</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</p>
<dt><code>-N</code></p>
<dd> Internally, the aggregation <i>period</i> is divided into <i>bucket</i> divisions, and the rolling average is recomputed every <i>period</i>/<i>bucket</i> seconds. For example, the defaults correspond to -T 60 and -N 12, which means the average is recomputed every five seconds for a period covering the prior 60 seconds.</p>
<dt><code>-U</code></p>
<dd> This option allows the dimension and scale associated with the observation value metric to be configured. <i>units</i> is a comma-separated string of six integer values, which are the space dimension, time dimension, count dimension, space scale, time scale, and count scale, respectively. The default dimension and scale is &#8220;none&#8221;, which is equivalent to presenting &#8220;0,0,0,0,0,0&#8221; as the argument to -U. The units associated with a metric are most easily viewed using the -d (metric description) option to <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1). The Install script described below steps through this option quite explicitly, so it is recommended that the Install script be used for building up the <i>units</i> specification.</dl>
<p> Essentially, the exported metrics provide statistics on the time for completion of each transaction, and an average count of transactions completed and watch points passed over a given time <i>period</i>. </p>
<h2>INSTALLATION</h2>
<p> In order for a host to export the names, help text and values for the Trace performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/trace
# ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/trace
# ./Remove
</pre>
<p> <code>pmdatrace</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdatrace</code></p>
<dt><code>$PCP_PMDAS_DIR/trace/help</code></p>
<dd> default help text file for the trace metrics</p>
<dt><code>$PCP_DEMOS_DIR/trace/*</code></p>
<dd> example programs which use the <i>pcp_trace</i> library</p>
<dt><code>$PCP_PMDAS_DIR/trace/Install</code></p>
<dd> installation script for the <code>pmdatrace</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/trace/Remove</code></p>
<dd> undo installation script for <code>pmdatrace</code></p>
<dt><code>$PCP_LOG_DIR/pmcd/trace.log</code></p>
<dd> default log file for error messages and other information from <code>pmdatrace</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmtrace/">pmtrace</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) and <code><a href="/docs/linux/man/3-pmdatrace/">pmdatrace</a></code>(3). </p>
<h2>Index</h2>
