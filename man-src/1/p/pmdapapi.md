---
title: "pmdapapi(1)"
name: "pmdapapi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdapapi/"
description: "pmdapapi – papi performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdapapi</code> &#8211; papi performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/pmdapapi</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdapapi</code> is a papi Performance Metrics Domain Agent (PMDA) which exposes hardware performance counters via the library Performance API (PAPI). </p>
<p> The metrics exported by the papi PMDA report values gathered from the hardware counters and metrics available, as reported by papi. Currently, only root users may access such metrics. </p>
<p> A brief description of the <code>pmdapapi</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>papi.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdapapi</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</dl>
<p> Performance counters are activated automatically as they are fetched cyclically (such as via <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1) or <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1)). This automatic activation is temporary, and lasts only a number of seconds governed by the <code>papi.control.auto_enable</code> control value (default 120). In the case automatic activation is undesirable, one may disable it by setting the <code>papi.control.auto_enable</code> metric to 0. </p>
<p> Alternately, the <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1) command can be used to permanently enable tracking particular metrics, or stop them on demand. Using the <code>papi.control.enable</code> and <code>papi.control.disable</code> metrics, one may set the metrics you wish to track using a space or comma separated list. Writing to the <code>papi.control.reset</code> metric disables all counters immediately. This may be useful if the system performance counters are needed for another profiling task. </p>
<pre>
# pmstore papi.control.enable &quot;TOT_CYC TOT_INS&quot;
papi.control.enable old value=&quot;&quot; new value=&quot;TOT_CYC TOT_INS&quot;
# pmval papi.system.TOT_CYC
            8.371E+04
# pmval papi.system.TOT_INS
            2.712E+04
# pmstore papi.control.disable &quot;TOT_CYC,TOT_INS&quot;
papi.control.disable old value=&quot;&quot; new value=&quot;TOT_CYC,TOT_INS&quot;
</pre>
<p> Fetching the <code>papi.control.status</code> metric provides an overview of all active counters. </p>
<p> By default, PAPI multiplexing, which allows support for collecting more metrics than supported by the hardware concurrently, is enabled. One may modify the <code>papi.control.multiplex</code> metric to disable multiplexing by setting it to 0. </p>
<p> Where possible, <code>pmdapapi</code> will expose available native perf and uncore events on the current hardware. It is not possible to count some native metrics and preset metrics concurrently. </p>
<pre>
# true -- automatically-enabled counters
# pmval -s3 papi.system.perf.BRANCH.LOADS
metric:    papi.system.perf.BRANCH.LOADS
host:      HOSTNAME
semantics: cumulative counter (converting to rate)
units:     count (converting to count / sec)
samples:   3
interval:  1.00 sec
            7530.    
            7539.    
            7543. 
# pmval -s3 papi.system.perf.BRANCH.MISSES
metric:    papi.system.perf.BRANCH.MISSES
host:      HOSTNAME
semantics: cumulative counter (converting to rate)
units:     count (converting to count / sec)
samples:   3
interval:  1.00 sec
             696.8   
             590.8   
             651.8
# true -- quick overview
# pminfo -f papi.control.status
papi.control.status
    value &quot;Papi is running, has multiplexing enabled, perf.BRANCH.MISSES(114): 8960, perf.BRANCH.LOADS(110): 158400&quot;
# true -- optional instant disable
# pmstore papi.control.disable &quot;perf.BRANCH.LOADS,perf.BRANCH.MISSES&quot;  
papi.control.disable old value=&quot;&quot; new value=&quot;perf.BRANCH.LOADS,perf.BRANCH.MISSES&quot;
</pre>
<h2>INSTALLATION</h2>
<p> If you want access to the names, help text and values for the papi performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/papi
# ./Install
</pre>
<p> If you want to undo the installation (and remove both PMDAs), do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/papi
# ./Remove
</pre>
<p> <code>pmdapapi</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdapapi</code></p>
<dt><code>$PCP_PMDAS_DIR/papi/help</code></p>
<dd> default help text file for the papi metrics</p>
<dt><code>$PCP_PMDAS_DIR/papi/Install</code></p>
<dd> installation script for the <code>pmdapapi</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/papi/Remove</code></p>
<dd> undo installation script for the <code>pmdapapi</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/sample.log</code></p>
<dd> default log file for error messages and other information from <code>pmdapapi</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
