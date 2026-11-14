---
title: "pmdasample(1)"
name: "pmdasample"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdasample/"
description: "pmdasample – sample performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdasample</code> &#8211; sample performance metrics domain agent (PMDA)</p>
<h2>SYNOPSIS</h2>
<p> <code>$PCP_PMDAS_DIR/pmdasample</code> [<code>-d</code> <i>domain</i>] [<code>-i</code> <i>port</i>] [<code>-l</code> <i>logfile</i>] [<code>-p</code>] [<code>-u</code> <i>socket</i>] [<code>-U</code> <i>username</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdasample</code> is a sample Performance Metrics Domain Agent (PMDA) which exports a variety of synthetic performance metrics. </p>
<p> This PMDA was developed as part of the quality assurance testing for the PCP product, but has other uses, most notably in the development of new PCP clients. </p>
<p> The metrics exported by the sample PMDA cover the full range of data types, data semantics, value cardinality, instance domain stability and error conditions found in real PMDAs. </p>
<p> A brief description of the <code>pmdasample</code> command line options follows:</p>
<dl>
<dt><code>-d</code></p>
<dd> It is absolutely crucial that the performance metrics <i>domain</i> number specified here is unique and consistent. That is, <i>domain</i> should be different for every PMDA on the one host, and the same <i>domain</i> number should be used for the same PMDA on all hosts.</p>
<dt><code>-i</code></p>
<dd> Expect PMCD to connect to <code>pmdasample</code> on the specified TCP/IP port. <i>port</i> may be a port number or port name.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>sample.log</i> is written in the current directory of <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when <code>pmdasample</code> is started, i.e. <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-p</code></p>
<dd> Expect PMCD to create a pipe and the connection to <code>pmdasample</code> is via standard input and standard output. This is the default connection mode.</p>
<dt><code>-u</code></p>
<dd> Expect PMCD to connect to <code>pmdasample</code> on the Unix domain socket named <i>socket</i>.</p>
<dt><code>-U</code></p>
<dd> User account under which to run the agent. The default is the unprivileged &quot;pcp&quot; account in current versions of PCP, but in older versions the superuser account (&quot;root&quot;) was used by default.</dl>
<p> At most one of the options <code>-i</code>, <code>-p</code> and <code>-u</code> may be specified.</p>
<h2>INSTALLATION</h2>
<p> If you want access to the names, help text and values for the sample performance metrics, do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/sample
# ./Install
</pre>
<p> Note that the installation script also installs the DSO version of the sample PMDA, so there are in fact two PMDAs installed, and two sets of performance metrics, namely <code>sample.*</code> and <code>sampledso.*</code>. </p>
<p> If you want to undo the installation (and remove both PMDAs), do the following as root: </p>
<pre>
# cd $PCP_PMDAS_DIR/sample
# ./Remove
</pre>
<p> <code>pmdasample</code> is launched by <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) and should never be executed directly. The Install and Remove scripts notify <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) when the agent is installed or removed.</p>
<h2>FILES</h2>
<dl>
<dt><code>$PCP_PMCDCONF_PATH</code></p>
<dd> command line options used to launch <code>pmdasample</code></p>
<dt><code>$PCP_PMDAS_DIR/sample/help</code></p>
<dd> default help text file for the sample metrics</p>
<dt><code>$PCP_PMDAS_DIR/sample/Install</code></p>
<dd> installation script for the <code>pmdasample</code> agent</p>
<dt><code>$PCP_PMDAS_DIR/sample/Remove</code></p>
<dd> undo installation script for the <code>pmdasample</code> agent</p>
<dt><code>$PCP_LOG_DIR/pmcd/sample.log</code></p>
<dd> default log file for error messages and other information from <code>pmdasample</code></dl>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>$PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdasimple/">pmdasimple</a></code>(1), <code><a href="/docs/linux/man/1-pmdatrivial/">pmdatrivial</a></code>(1), <code><a href="/docs/linux/man/1-pmdatxmon/">pmdatxmon</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5). </p>
<h2>Index</h2>
