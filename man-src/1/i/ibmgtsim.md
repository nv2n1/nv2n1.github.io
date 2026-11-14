---
title: "ibmgtsim(1)"
name: "ibmgtsim"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibmgtsim/"
description: "IBMgtSim – Infiniband Management Simulator"
---

<p><code>IBMgtSim</code> &#8211; Infiniband Management Simulator</p>
<h2>Synopsys</h2>
<p>IBMgtSim [-h] [-V mod-verb-pair-list] [-l log-file] [-p server-port]<br />
&nbsp;<wbr>&nbsp;<wbr>[-w num-threads]&nbsp;<wbr>[-f flow-tcl-file]&nbsp;<wbr>[-s seed]&nbsp;<wbr>-t topology</p>
<h2>Description</h2>
<p>Simulates the Fabric as defined by the given topology file and start a server to handle <font SIZE="-1">MAD</font> requests from clients like OpenSM.</p>
<h2>Arguments</h2>
<dl>
<dt>-t topology</p>
<dd>A topology file describing the fabric to be simulated (see <code>ibdm-topo-file</code>)</dl>
<h2>Options</h2>
<dl>
<dt>-s seed</p>
<dd>The seed to be used for random number generation.</p>
<dt>-f flow-tcl-file</p>
<dd>A tcl file to be sourced after the fabric is setup.</p>
<dt>-l log-file</p>
<dd>Set the log file of the simulator (default is /var/cache/ibutils/ibsim.log)</p>
<dt>-p server-port</p>
<dd>Set the port number the server attaches to (default 46517)</p>
<dt>-w num-threads</p>
<dd>The number of threads processing the mads</p>
<dt>-V &lt;module-verbosity-pair-list&gt;</p>
<dd>Provides a fine grain control over the log file verbosity. Given list of pairs of simulator software module names and their verbosity levels &#8211; every module is separatly controlled. The first value (missing module name) is controlling the default verbosity for all un-explicitly set modules. </p>
<dl>
<dd>Current Verbosity Levels: </p>
<pre> MsgShowFatal = 0x01;
 MsgShowError = 0x02;
 MsgShowWarning= 0x04;
 MsgShowInfo = 0x08;
 MsgShowVerbose= 0x10;
 MsgShowContext= 0x20;
 MsgShowSource = 0x40;
 MsgShowTime = 0x80;
 MsgShowModule = 0x100;
 MsgShowMads = 0x200;
 MsgShowFrames = 0x400;
 MsgShowAll = 0xffff;
 MsgDefault = 0x62f;</pre>
<p>Software Modules: </p>
<p> client, server, dispatcher, node, sma, lftMad, mftMad, vlArbMad, pKeyMad, portInfoMad </p>
<p> Examples -V flag values might be: </p>
<pre> -V 0xffff = Full verbosity on all modules</pre>
<pre> -V '0x3 server 0x6f2 sma 0xffff' = Only fatal and error for all modules
 full verbosity for the SMA module and default verbosity for the
 Server module.</pre>
</dl>
<dt>-h</p>
<dd>This help message</dl>
<h2>Author</h2>
<p>Eitan Zahavi, Mellanox Technologies <font SIZE="-1">LTD</font>, eitan [at] mellanox.co.il</p>
