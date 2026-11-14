---
title: "pmdaproc(1)"
name: "pmdaproc"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdaproc/"
description: "pmdaproc – process performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdaproc</code> &#8211; process performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/proc/pmdaproc</code> [<code>-AL</code>] [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-r</code> <i>cgroup</i>] [<code>-U</code> <i>username</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdaproc</code> is a Performance Metrics Domain Agent (PMDA) which extracts performance metrics describing the state of the individual processes running on a Linux system. </p>
<p> The <code>proc</code> PMDA exports metrics that measure the memory, processor and other resource use of each process, as well as summary information collated across all of the running processes. The PMDA uses credentials passed from the <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) monitoring tool identifying the user requesting the information, to ensure that only values the user is allowed to access are returned by the PMDA. This involves the PMDA temporarily changing its effective user and group identifiers for the duration of requests for instances and values. In other words, system calls to extract information are performed as the user originating the request and not as a privileged user. The mechanisms available for transfer of user credentials are described further in the <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) page. </p>
<p> A brief description of the <code>pmdaproc</code> command line options follows:</p>
<dl>
<dt><code>-A</code></p>
<dd> Disables use of the credentials provided by <code>PMAPI</code> client tools, and simply runs everything under the &quot;root&quot; account.</p>
<dt><code>-L</code></p>
<dd> Changes the per-process instance domain used by most <code>pmdaproc</code> metrics to include threads as well.</p>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>proc.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdaproc</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-r</code></p>
<dd> Restrict the set of processes exported in the per-process instance domain to only those processes that are contained by the specified <i>cgroup</i> resource container. This option provides an optional finer granularity to the monitoring, and can also be used to reduce the resources consumed by <i>pmdaproc</i> during requests for instances and values.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the privileged &quot;root&quot; account, with seteuid (2) and setegid (2) switching for accessing most information.</dl>
<h2>HOTPROC OVERVIEW</h2>
<p> The <code>pmdaproc</code> Performance Metrics Domain Agent (PMDA) includes an additional set of per-process metrics with an instance domain of processes restricted to an &quot;interesting&quot; or &quot;hot&quot; set. Unlike the stock metrics exported by the <code>proc</code> PMDA, which have an instance domain equal to the current processes, <code>hot</code> metrics have an instance domain which is a subset of this. This <code>hotproc</code> instance domain is determined by a configurable predicate evaluated over some refresh interval. </p>
<p> As well as the equivalent per-process <code>proc</code> metrics, <code>hotproc</code> provides a <code>cpuburn</code> metric which specifies the CPU utilization of the process over the refresh interval, <code>total</code> metrics which indicate how much of the available CPU time the &quot;interesting&quot; processes account for, <code>predicate</code> metrics which show the values of the reserved variables (see below) that are being used in the hotproc predicate, and <code>control</code> metrics for controlling the agent. </p>
<h2>HOTPROC CONFIGURATION</h2>
<p> The configuration file consists of one predicate used to determine if a process should be in the interesting set or not. </p>
<p> An example configuration file may be found at <code>$PCP_PMDAS_DIR/proc/samplehotproc.conf</code> </p>
<p> This file with any modifications can be copied to <code>$PCP_PMDAS_DIR/proc/hotproc.conf</code> in order to configure the <code>hot</code> metrics. The <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1) and <code><a href="/docs/linux/man/3-pmstore/">pmStore</a></code>(3) interfaces can be used as well (described below). </p>
<p> The predicate is described using the language specified below. The symbols are based on those used by the <code><a href="/docs/linux/man/1-c/">C</a></code>(1) and <code><a href="/docs/linux/man/1-awk/">awk</a></code>(1) languages.</p>
<dl>
<dt>Boolean Connectives</p>
<dd> <code>&amp;&amp;</code> (and), <code>||</code> (or), <code>!</code> (not), <code>()</code> (precedence overriding)</p>
<dt>Number comparators</p>
<dd> <code>&lt;</code> , <code>&lt;=</code> , <code>&gt;</code> , <code>&gt;=</code> , <code>==</code> , <code>!=</code></p>
<dt>String comparators</p>
<dd> <code>==</code> , <code>!=</code></p>
<dt>String/Pattern comparators</p>
<dd> <code>~</code> (string matches pattern) , <code>!~</code> (string does not match pattern)</p>
<dt>Reserved variables</p>
<dd> <code>uid</code> (user id; type integer) <code>uname</code> (user name; type string), <code>gid</code> (group id; type integer) <code>gname</code> (group name; type string), <code>fname</code> (process file name; type string), <code>psargs</code> (process file name with args; type string), <code>cpuburn</code> (cpu utilization; type float), <code>iodemand</code> (I/O demand &#8211; Kbytes read/written per second; type float), <code>ctxswitch</code> (number of context switches per second; type float), <code>syscalls</code> (number of system calls per second; type float), <code>virtualsize</code> (virtual size in Kbytes; type float), <code>residentsize</code> (resident size in Kbytes; type float), <code>iowait</code> (blocked and raw io wait in secs/sec; type float), <code>schedwait</code> (time waiting in run queue in secs/sec; type float).</p>
<dt>Literal values</p>
<dd> <code>1234</code> (positive integer), <code>0.35</code> (positive float), <code>&quot;foobar&quot;</code> (string; delimited by <code>&quot;</code>), <code>/[fF](o)+bar/</code> (pattern; delimited by <code>/</code>), <code>true</code> (boolean), <code>false</code> (boolean)</p>
<dt>Comments</p>
<dd> <code>#this is a comment</code> (from <code>#</code> to the end of the line).</p>
<dt>Examples</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>cpuburn&nbsp;<wbr>&gt;&nbsp;<wbr>0.2&nbsp;<wbr>#&nbsp;<wbr>cpu utilization of more than 20%<br />
&nbsp;<wbr>&nbsp;<wbr>cpuburn&nbsp;<wbr>&gt;&nbsp;<wbr>0.2&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>uname&nbsp;<wbr>==&nbsp;<wbr>&quot;root&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>cpuburn&nbsp;<wbr>&gt;&nbsp;<wbr>0.2&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>(uname&nbsp;<wbr>==&nbsp;<wbr>&quot;root&quot;&nbsp;<wbr>|| uname&nbsp;<wbr>==&nbsp;<wbr>&quot;hot&quot;)<br />
&nbsp;<wbr>&nbsp;<wbr>psargs&nbsp;<wbr>~&nbsp;<wbr>/pmda/&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>cpuburn&nbsp;<wbr>&gt;&nbsp;<wbr>0.4 </p>
</dl>
<p> The <code>hotproc.predicate</code> metrics may be used to see what the values of the reserved variables are that were used by the predicate at the last refresh. They do not cover the reserved variables which are already exported elsewhere. A <code>hotproc.predicate</code> metric may not have a value if it is not referenced in the configuration predicate. </p>
<h2>DYNAMIC CONFIGURATION</h2>
<p> The <code>hot</code> metrics can also be configured at runtime through the <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1) interface (and, implicitly, the <code><a href="/docs/linux/man/3-pmstore/">pmStore</a></code>(3) API)</p>
<dl>
<dt>Examples</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>pmstore hotproc.control.config&nbsp;<wbr>&#8216;fname&nbsp;<wbr>==&nbsp;<wbr>&quot;mingetty&quot;&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>pmstore hotproc.control.config&nbsp;<wbr>&#8216;uid&nbsp;<wbr>==&nbsp;<wbr>0&#8242;</p>
<dt>To force the config file to be reloaded:</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>pmstore hotproc.control.reload_config&nbsp;<wbr>&quot;1&quot;</dl>
<h2>INSTALLATION</h2>
<p> The <code>proc</code> PMDA is installed and available by default. If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/proc
# ./Remove
</pre>
<p> If you want to establish access to the names, help text and values for the proc performance metrics once more, after removal, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/proc
# ./Install
</pre>
<p> <code>pmdaproc</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdaproc</code></p>
<dt><code>$PCP_PMDAS_DIR/proc/help</code></p>
<dd> default help text file for the proc metrics</p>
<dt><code>$PCP_PMDAS_DIR/proc/Install</code></p>
<dd> installation script for the <code>pmdaproc</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/proc/Remove</code></p>
<dd> undo installation script for the <code>pmdaproc</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/proc.log</code></p>
<dd> default log file for error messages and other information from <code>pmdaproc</code></p>
<dt><code>$PCP_PMDAS_DIR/proc/samplehotproc.conf</code></p>
<dd> simple sample hotproc configuration</p>
<dt><code>$PCP_PMDAS_DIR/proc/hotproc.conf</code></p>
<dd> default hotproc configuration file</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmstore/">pmstore</a></code>(1), <code><a href="/docs/linux/man/2-seteuid/">seteuid</a></code>(2), <code><a href="/docs/linux/man/2-setegid/">setegid</a></code>(2), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
