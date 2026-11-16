---
title: "runsimtest(1)"
name: "runsimtest"
section: "1"
letter: "r"
url: "/docs/linux/man/1-runsimtest/"
description: "RunSimTest – Run a test over the IB management simulator"
---

<p><code>RunSimTest</code> &#8211; Run a test over the IB management simulator</p>
<h2>Synopsys</h2>
<p>RunSimTest [-h] [-o osm-path][-f flow-file][-c checker-file]<br />
-t topology&nbsp;<wbr>[-n osm-node-name][-p osm-port-num][-s seed][-V verbosity-list] </p>
<p> This command starts the simulator and runs the the given test flow on top of it. Then it runs the checker flow. The default test flow starts OpenSM and wait for Subnet-Up event. User given flow can make use of the provided facilities for starting OpenSM and tracking it events.</p>
<h2>Arguments</h2>
<dl>
<dt>-t topology</dt>
<dd>A topology file describing the fabric (see <code>ibdm-topo-file</code>)</dd></dl>
<h2>Options</h2>
<dl>
<dt>-f flow-file</dt>
<dd>A tcl file sourced by the sim after the fabric is setup. See following discussion about the provided <font SIZE="-1">API</font> and global variables that are available for the flow.</dd>
<dt>-c checker-file</dt>
<dd>A tcl file defining when osm completed and what checks are requierd to validate it&#8217;s outputs. The procedure named &#8216;checker&#8217; is invoked by the test flow to start the checking flow. The default flow waits for OpenSM to complete setup the fabric and run ibdmchk.</dd>
<dt>-o osm-path</dt>
<dd>Full path to OpenSM (/usr/local/ofed/osm-sim/bin/opensm). <font SIZE="-1">NOTE</font> OpenSM should be compiled with &#8211;with-osmv=sim to be able to connect to the simulator.</dd>
<dt>-n osm-node</dt>
<dd>Topology file node name the <font SIZE="-1">SM</font> runs on (default H-1/U1)</dd>
<dt>-p port-num</dt>
<dd>Port number the <font SIZE="-1">SM</font> attaches to (default 1).</dd>
<dt>-s seed</dt>
<dd>Random seed to be used.</dd>
<dt>-V verbosity-list</dt>
<dd>Module verbosity list. The first should be the global verbosity. See IBMgtSim for full list of modules. Examples: </dd>
<pre> -V 0xffff = Full verbosity on all modules
 -V '&quot;0x3 server 0x6f2 sma 0xffff&quot;' = Only fatal and error
 for all modules full verbosity for the SMA module and default
 verbosity for the Server module.</pre>
<dt>-h</dt>
<dd>This help message</dd></dl>
<h2>Author</h2>
<p>Eitan Zahavi, Mellanox Technologies <font SIZE="-1">LTD</font>, eitan [at] mellanox.co.il</p>
