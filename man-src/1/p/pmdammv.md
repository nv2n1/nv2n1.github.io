---
title: "pmdammv(1)"
name: "pmdammv"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdammv/"
description: "pmdammv – memory mapped values performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdammv</code> &#8211; memory mapped values performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/mmv/pmdammv</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdammv</code> is a Performance Metrics Domain Agent (PMDA) which exports application level performance metrics using memory mapped files. It offers an extremely low overhead instrumentation facility that is well-suited to long running, mission critical applications where it is desirable to have performance metrics and availability information permanently enabled. </p>
<p> The <code>mmv</code> PMDA exports instrumentation that has been added to an application using the MMV APIs (refer to <code><a href="/docs/linux/man/3-mmv_stats_init/">mmv_stats_init</a></code>(3) and <code><a href="/docs/linux/man/5-mmv/">mmv</a></code>(5) for further details). These APIs can be called from several languages, including C, C++, Perl, Python and Java (via the separate &#8220;Parfait&#8221; class library). </p>
<p> A brief description of the <code>pmdammv</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>mmv.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdammv</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<h2>INSTALLATION</h2>
<p> If you want access to the names, help text and values for the mmv performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/mmv
# ./Install
</pre>
<p> Note that the default mechanism for sharing memory mapped values between instrumented applications and the <code>mmv</code> PMDA involves the creation of a world-writeable <i>$PCP_TMP_DIR/mmv</i> directory with the sticky-bit set (similar to <i>/tmp</i> and <i>/var/tmp</i>, for example). This suffices to allow any application, running under any user account, to communicate with the PMDA (which runs under the &quot;pcp&quot; account by default). This may not be desirable for every environment, and one should consider the security implications of any directory setup like this (similar classes of issues exist as those that affect the system temporary file directories). </p>
<p> The installation process will not overwrite any existing <i>$PCP_TMP_DIR/mmv</i> directory. Thus it is possible to implement an alternate permissions strategy with no world-writable directory for sharing files &#8211; any directory readable by user or group &quot;pcp&quot; will suffice. </p>
<p> If you want to undo the installation, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/mmv
# ./Remove
</pre>
<p> <code>pmdammv</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdammv</code></p>
<dt><code>$PCP_TMP_DIR/mmv</code></p>
<dd> directory housing memory mapped value files</p>
<dt><code>$PCP_PMDAS_DIR/mmv/help</code></p>
<dd> default help text file for the mmv metrics</p>
<dt><code>$PCP_PMDAS_DIR/mmv/Install</code></p>
<dd> installation script for the <code>pmdammv</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/mmv/Remove</code></p>
<dd> undo installation script for the <code>pmdammv</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/mmv.log</code></p>
<dd> default log file for error messages and other information from <code>pmdammv</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/3-mmv_stats_init/">mmv_stats_init</a></code>(3), <code><a href="/docs/linux/man/5-mmv/">mmv</a></code>(5), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
