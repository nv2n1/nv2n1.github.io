---
title: "pmdaperfevent(1)"
name: "pmdaperfevent"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdaperfevent/"
description: "pmdaperfevent – hardware performance counter performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdaperfevent</code> &#8211; hardware performance counter performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/perfevent/pmdaperfevent</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>] [<code>-i</code> <i>port</i>] [<code>-p</code>] [<code>-u</code> <i>socket</i>] [<code>-6</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdaperfevent</code> is a Performance Metrics Domain Agent (PMDA) that configures and reads the hardware performance counters using the Linux kernel perf_event API. </p>
<p> The <code>perfevent</code> PMDA exports metrics for hardware performance counters that are configurable from the Linux kernel perf_event API. The PMDA uses the libpfm4 library to access the hardware performance counters so any counters that are supported in libpfm4 should be available. Also included is the ability to read the Intel RAPL counters via direct MSR access. The PMDA supports automatically loading different counters for each hardware architecture. A single configuration file is used to specify the desired counters for each hardware performance monitoring unit (PMU). The configuration file allows different counters to be programmed on different CPUs and supports round-robin assignment of uncore counters needed for some AMD chips. </p>
<p> The PMDA configures the counters to count events in both user and kernel mode. This means that the hardware counters are unavailable to use by normal unprivileged user applications when they are in use by the PMDA. The PMDA provides a mechanism to temporarily disable the system-wide counters in order to allow normal users to be able to use the counters if they wish. See <code><a href="/docs/linux/man/1-perfalloc/">perfalloc</a></code>(1) for details. </p>
<p> Note that <code>pmdaperfevent</code> is affected by the value of the <i>kernel.perf_event_paranoid</i> setting, which can be adjusted by <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8). </p>
<p> A brief description of the <code>pmdaperfevent</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>perfevent.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdaperfevent</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the privileged &quot;root&quot; account.</p>
<dt><code>-i</code></p>
<dd> listen on given port number for connection from <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1)</p>
<dt><code>-p</code></p>
<dd> communicate with <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) via stdin/stdout</p>
<dt><code>-u</code></p>
<dd> expect <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) to connect on given unix domain socket</p>
<dt><code>-6</code></p>
<dd> expect <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) to connect on given ipv6 port (number or name)</dl>
<h2>INSTALLATION</h2>
<p> The <code>perfevent</code> PMDA is not activated by default To install the PMDA, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/perfevent
# ./Install
</pre>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/perfevent
# ./Remove
</pre>
<p> <code>pmdaperfevent</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdaperfevent</code></p>
<dt><code>$PCP_PMDAS_DIR/perfevent/perfevent.conf</code></p>
<dd> default configuration file for the PMDA. See <code><a href="/docs/linux/man/5-perfevent-conf/">perfevent.conf</a></code>(5) for detailed information.</p>
<dt><code>$PCP_PMDAS_DIR/perfevent/help</code></p>
<dd> default help text file for the perfevent metrics</p>
<dt><code>$PCP_PMDAS_DIR/perfevent/Install</code></p>
<dd> installation script for the <code>pmdaperfevent</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/perfevent/Remove</code></p>
<dd> undo installation script for the <code>pmdaperfevent</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/perfevent.log</code></p>
<dd> default log file for error messages and other information from <code>pmdaperfevent</code></dl>
<h2>UPGRADING</h2>
<p> Some metric names have changed starting in version 3.10.8 to better conform to PMNS conventions. <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1) can be used to update old archives. A helper utility, <code>$PCP_PMDAS_DIR/perfevent/perfevent-makerewrite.pl</code> will generate a config file that is suitable for use with <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1) to update the metric names in existing archives.</p>
<h2>BUGS</h2>
<p> Each event is placed in its own group and there is no way to group related events together so they are guaranteed to be simultaneously active. A workaround for this is to ensure that the number of configured events is less than or equal to the number of available hardware counters. This means that the events will not be time-multiplexed by the kernel and will be simultaneously active.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-perfalloc/">perfalloc</a></code>(1), <code><a href="/docs/linux/man/5-perfevent-conf/">perfevent.conf</a></code>(5), <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmlogrewrite/">pmlogrewrite</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5), <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5) and <code><a href="/docs/linux/man/8-sysctl/">sysctl</a></code>(8). </p>
<h2>Index</h2>
