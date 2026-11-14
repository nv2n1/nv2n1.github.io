---
title: "orte-dvm(1)"
name: "orte-dvm"
section: "1"
letter: "o"
url: "/docs/linux/man/1-orte-dvm/"
description: "orte-dvm, ompi_dvm – Establish a Distributed Virtual Machine (DVM)."
---

<h2 class="name">NAME</h2>
<p> orte-dvm, ompi_dvm &#8211; Establish a Distributed Virtual Machine (DVM). </p>
<p> <code>Note:</code> <i>orte-dvm</i> and <i>ompi-dvm</i> are synonyms for each other. Using either of the names will produce the same behavior. </p>
<h2>SYNOPSIS</h2>
<p> <code>orte-dvm</code> [ options ] </p>
<p> Invoking <i>orte-dvm</i> via an absolute path name is equivalent to specifying the <i>&#8211;prefix</i> option with a <i>&lt;dir&gt;</i> value equivalent to the directory where <i>orte-dvm</i> resides, minus its last subdirectory. For example: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;/usr/local/bin/orte-dvm &#8230; </p>
<p> is equivalent to </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;orte-dvm &#8211;prefix&nbsp;/usr/local </p>
<h2>QUICK SUMMARY</h2>
<p> <i>orte-dvm</i> will establish a DVM that can be used to execute subsequent applications. Use of <i>orte-dvm</i> can be advantageous, for example, when you want to execute a number of short-lived tasks. In such cases, the time required to start the ORTE DVM can be a significant fraction of the time to execute the overall application. Thus, creating a persistent DVM can speed the overall execution. In addition, a persistent DVM will support executing multiple parallel applications while maintaining separation between their respective cores.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, &#8211;help</p>
<dd> Display help for this command</p>
<dt><code>-V</code>, &#8211;version</p>
<dd> Print version number. If no other arguments are given, this will also cause orte-dvm to exit.</dl>
<p> Use one of the following options to specify which hosts (nodes) of the cluster to use for the DVM.</p>
<dl>
<dt><code>-H</code>, -host, &#8211;host &lt;host1,host2,&#8230;,hostN&gt;</p>
<dd> List of hosts for the DVM.</p>
<dt><code>-hostfile</code>, &#8211;hostfile &lt;hostfile&gt;</p>
<dd> Provide a hostfile to use.</p>
<dt><code>-machinefile</code>, &#8211;machinefile &lt;machinefile&gt;</p>
<dd> Synonym for <i>-hostfile</i>.</p>
<dt><code>&#8211;prefix </code>&lt;dir&gt;</p>
<dd> Prefix directory that will be used to set the <i>PATH</i> and <i>LD_LIBRARY_PATH</i> on the remote node before invoking the ORTE daemon.</dl>
<p> Setting MCA parameters:</p>
<dl>
<dt><code>-gmca</code>, &#8211;gmca &lt;key&gt; &lt;value&gt;</p>
<dd> Pass global MCA parameters that are applicable to all contexts. <i>&lt;key&gt;</i> is the parameter name; <i>&lt;value&gt;</i> is the parameter value.</p>
<dt><code>-mca</code>, &#8211;mca &lt;key&gt; &lt;value&gt;</p>
<dd> Send arguments to various MCA modules. See the &quot;MCA&quot; section, below.</p>
<dt><code>-report-uri</code>, &#8211;report-uri &lt;channel&gt;</p>
<dd> Print out orte-dvm&#8217;s URI during startup. The channel must be either a &#8216;-&#8216; to indicate that the URI is to be output to stdout, a &#8216;+&#8217; to indicate that the URI is to be output to stderr, or a filename to which the URI is to be written.</dl>
<p> The following options are useful for developers; they are not generally useful to most ORTE and/or MPI users:</p>
<dl>
<dt><code>-d</code>, &#8211;debug-devel</p>
<dd> Enable debugging of the ORTE layer.</p>
<dt><code>&#8211;debug-daemons-file</code></p>
<dd> Enable debugging of the ORTE daemons in the DVM, storing output in files.</dl>
<p> There may be other options listed with <i>orte-dvm &#8211;help</i>.</p>
<h2>DESCRIPTION</h2>
<p> <i>orte-dvm</i> starts a Distributed Virtual Machine (DVM) by launching a daemon on each node of the allocation, as modified or specified by the <i>-host</i> and <i>-hostfile</i> options. Applications can subsequently be executed using the <i>orte-submit</i> command. The DVM remains in operation until receiving the <i>orte-submit -terminate</i> command.</p>
<h3>Specifying Host Nodes</h3>
<p> Host nodes can be identified on the <i>orte-dvm</i> command line with the <i>-host</i> option or in a hostfile. </p>
<p> For example,</p>
<dl>
<dt>orte-dvm -H aa,aa,bb ./a.out</p>
<dd> launches two processes on node aa and one on bb.</dl>
<p> Or, consider the hostfile </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>%</code>&nbsp;cat myhostfile<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;aa slots=2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;bb slots=2<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;cc slots=2 </p>
<p> Here, we list both the host names (aa, bb, and cc) but also how many &quot;slots&quot; there are for each. Slots indicate how many processes can potentially execute on a node. For best performance, the number of slots may be chosen to be the number of cores on the node or the number of processor sockets. If the hostfile does not provide slots information, a default of 1 is assumed. When running under resource managers (e.g., SLURM, Torque, etc.), Open MPI will obtain both the hostnames and the number of slots directly from the resource manger. </p>
<h2>Index</h2>
