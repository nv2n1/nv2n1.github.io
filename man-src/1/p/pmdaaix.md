---
title: "pmdaaix(1)"
name: "pmdaaix"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdaaix/"
description: "pmdaaix, pmdadarwin, pmdafreebsd, pmdalinux, pmdanetbsd, pmdasolaris, pmdawindows – operating system kernel performance metrics domain agents"
---

<h2>NAME</h2>
<p> <code>pmdaaix</code>, <code>pmdadarwin</code>, <code>pmdafreebsd</code>, <code>pmdalinux</code>, <code>pmdanetbsd</code>, <code>pmdasolaris</code>, <code>pmdawindows</code> &#8211; operating system kernel performance metrics domain agents</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/aix/pmdaaix</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>]<br />
 <code>$PCP_PMDAS_DIR/darwin/pmdadarwin</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>]<br />
 <code>$PCP_PMDAS_DIR/freebsd/pmdafreebsd</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>]<br />
 <code>$PCP_PMDAS_DIR/linux/pmdalinux</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>]<br />
 <code>$PCP_PMDAS_DIR/netbsd/pmdanetbsd</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>]<br />
 <code>$PCP_PMDAS_DIR/solaris/pmdasolaris</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>]<br />
 <code>$PCP_PMDAS_DIR/windows/pmdawindows</code> [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-U</code> <i>username</i>]</p>
<h2>DESCRIPTION</h2>
<p> Each supported platform has a kernel Performance Metrics Domain Agent (PMDA) which extracts performance metrics from the kernel of that platfrom. A variety of platform-specific metrics are available, with an equally varied set of access mechanisms &#8211; typically this involves special system calls, or reading from files in kernel virtual filesystems such as the Linux <i>sysfs</i> and <i>procfs</i> filesystems. </p>
<p> The platform kernel PMDA is one of the most critical components of the PCP installation, and must be as efficient and reliable as possible. In all installations the default kernel PMDA will be installed as a shared library and thus executes directly within the <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) process. This slightly reduces overheads associated with querying the metadata and values associated with these metrics (no message passing is required). </p>
<p> Unlike many other PMDAs, the kernel PMDA exports a number of metric namespace subtrees, such as kernel, network, swap, mem, ipc, filesys, nfs, disk and hinv (hardware inventory). </p>
<p> Despite usually running as shared libraries, most installations also include a stand-alone executable for the kernel PMDA. This is to aid profiling and debugging activities, with <code><a href="/docs/linux/man/1-dbpmda/">dbpmda</a></code>(1) for example. In this case (but not for shared libraries), the following command line options are available:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>[platform].log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmda[platform]</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<h2>INSTALLATION</h2>
<p> Access to the names, help text and values for the kernel performance metrics is available by default &#8211; unlike most other agents, no action is required to enable them and they should not be removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMDAS_DIR/[platform]/help</code></p>
<dd> default help text file for the the kernel metrics</p>
<dt><code>$PCP_LOG_DIR/pmcd/[platform].log</code></p>
<dd> default log file for error messages and other information from the kernel PMDA.</dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <i>/etc/pcp.conf</i> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-dbpmda/">dbpmda</a></code>(1) <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
