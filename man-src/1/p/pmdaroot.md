---
title: "pmdaroot(1)"
name: "pmdaroot"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdaroot/"
description: "pmdaroot – a privileged PMCD helper performance metrics domain agent"
---

<h2>NAME</h2>
<p> <code>pmdaroot</code> &#8211; a privileged PMCD helper performance metrics domain agent</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/root/pmdaroot</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-s</code> <i>sockname</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdaroot</code> is a special Performance Metrics Domain Agent (PMDA) which cooperates closely with <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and other PMDAs to provide limited privileged services to these unprivileged processes. </p>
<p> In this role it is used to discover operating system containers running on the local host. It also enables access to performance data from within those containers by other PMDAs running on the bare-metal host, using the <code><a href="/docs/linux/man/3-pmdarootconnect/">pmdaRootConnect</a></code>(3) and the associated namespace interfaces. </p>
<p> Like all other PMDAs, it also exports performance metrics from the domain it controls. Currently, this is limited to information about the containers on the local system, and currently only Docker containers can be detected.</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>root.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdaroot</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-s</code></p>
<dd> Location of the <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7) domain socket for communication with clients seeking privileged operations. By default, a socket file named <code>$PCP_TMP_DIR/pmcd/root.socket</code> is used.</dl>
<h2>INSTALLATION</h2>
<p> Access to the names, help text and values for the kernel performance metrics is available by default &#8211; unlike most other agents, no action is required to enable them and they should not be removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/root/help</code></p>
<dd> default help text file for metrics exported by the root PMDA.</p>
<dt><code>$PCP_LOG_DIR/pmcd/root.log</code></p>
<dd> default log file for error messages and other information from the root PMDA.</p>
<dt><code>$PCP_TMP_DIR/pmcd/root.socket</code></p>
<dd> default socket file for communication with root PMDA clients.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/3-pmda/">PMDA</a></code>(3), <code><a href="/docs/linux/man/3-pmdarootconnect/">pmdaRootConnect</a></code>(3), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7). </p>
<h2>Index</h2>
