---
title: "pmdaib(1)"
name: "pmdaib"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmdaib/"
description: "pmdaib – Infiniband performance metrics domain agent (PMDA)"
---

<h2>NAME</h2>
<p> <code>pmdaib</code> &#8211; Infiniband performance metrics domain agent (PMDA)</p>
<h2>SYNOPSYS</h2>
<p> <code>$PCP_PMDAS_DIR/infiniband/pmdaib</code> [<code>-c</code> <i>configFile</i>] [<code>-D</code> <i>debug</i>] [<code>-d</code> <i>domain</i>] [<code>-l</code> <i>logfile</i>] [<code>-w</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmdaib</code> is a Performance Metrics Domain Agent (PMDA) which exports information and performance metrics about local Infiniband HCAs and local or remote Infiniband GUIDs. </p>
<p> A brief description of the <code>pmdaib</code> command line options follows:</p>
<dl>
<dt><code>-c</code></p>
<dd> Location of the config file. By default, the config file is named <code>$PCP_PMDAS_DIR/infiniband/config.</code> See <code>CONFIG FILE</code> for more information.</p>
<dt><code>-D</code></p>
<dd> A debug values, as specified by <code>pmdbg (1)</code></p>
<dt><code>-d</code></p>
<dd> Specify an alternate performance metrics <i>domain</i> number. Almost never necessary.</p>
<dt><code>-l</code></p>
<dd> Location of the log file. By default, a log file named <i>ib.log</i> is written to <code>$PCP_LOG_DIR/pmcd</code>. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-w</code></p>
<dd> Write out the default config file to <code>$PCP_PMDAS_DIRS/infiniband</code> and exit immediately. The written config file will contain the local HCA ports. It will not overwrite an existing file. This argument should only be used to create the template config file and should never appear in <i>pmcd.conf.</i> See <code>CONFIG FILE</code> for more information on the file format and on monitoring remote GUIDs.</dl>
<h2>CONFIG FILE</h2>
<p> By default, the PMDA will operate without using a config file. In this mode of operation the local HCA ports will be monitored. Note that if a new HCA is added to the machine that instance domain naming may change because it will always be based on the kernel&#8217;s naming. </p>
<p> In cases where this is not acceptable, or in the case where monitoring remote Infiniband ports is required, a config file must be created. A &quot;template&quot; file can be created by running the <code>pmdaib</code> daemon with the <code>-w</code> argument. This will create a config file with the local ports and GUIDs. </p>
<p> If the config file is <i>executable</i> then it will be run and the output will be used as the config file. </p>
<p> The config file is composed of line-based records. Blank lines and everything after the <i>hash (#)</i> character are ignored. Each line has 6 fields: </p>
<p> [<code>instName</code>] [<code>portGUID</code>] [<code>portNum</code>] via [<code>localPortName</code>]:[<code>localPortNum</code>] </p>
<p> The first field is used to give a static instance name to the Infiniband port that has a specific GUID. All of the other fields must be properly specified in order to monitor a particular port. </p>
<p> For example, to monitor port 1 of the local HCA called &#8216;mthca0&#8217; a possible config file line would be: </p>
<p> myPort1 0xdeadbeef01234567 1 via mthca0:1 </p>
<p> Remote ports can be easily monitored by specifying the GUID of the HCA or switch and specifying the remote port number. The <code>localPortName</code>:<code>localPortNum</code> tuple specifies which local HCA and port to use as the &quot;first hop&quot; in contacting the remote GUID. E.g., to monitor port 13 of a remote switch which is connected to the fabric on the first port of the second HCA: </p>
<p> switch13 0xfeeffeefabcdabcd 13 via mthca1:1</p>
<h2>LOCAL CONTEXT</h2>
<p> The Infiniband pmda also supports accessing the metrics via <code>PM_CONTEXT_LOCAL</code> when using the PMAPI interface. In order to use the Infiniband pmda in this way, set the environment variable <code>PMDA_LOCAL_IB</code> prior to calling <code><a href="/docs/linux/man/3-pmnewcontext/">pmNewContext</a>(3).</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a>(1),</code> <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a>(3),</code> <code><a href="/docs/linux/man/3-pmcontextnew/">pmContextNew</a>(3),</code> <code><a href="/docs/linux/man/8-ibnetdiscover/">ibnetdiscover</a>(8).</code> </p>
<h2>Index</h2>
