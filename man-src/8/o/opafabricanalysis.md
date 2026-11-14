---
title: "opafabricanalysis(8)"
name: "opafabricanalysis"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opafabricanalysis/"
description: "opafabricanalysis"
---

<p>opafabricanalysis </p>
<p> <code>(All)</code> Performs analysis of the fabric.</p>
<h2>Syntax</h2>
<p>opafabricanalysis [-b|-e] [-s] [-d <i>dir</i>] [-c <i>file</i>] [-t <i>portsfile</i>] [-p <i>ports</i>] [-T <i>topology_input</i>]</p>
<h2>Options</h2>
<dl>
<dt>&#8212; help</p>
<dd>Produce full help text.</p>
<dt>-b</p>
<dd>Baseline mode, default is compare/check mode.</p>
<dt>-e</p>
<dd>Evaluate health only, default is compare/check mode.</p>
<dt>-s</p>
<dd>Save history of failures (errors/differences).</p>
<dt>-d dir</p>
<dd>Top-level directory for saving baseline and history of failed checks. Default = /var/lib/opa-ff/analysis</p>
<dt>-c file</p>
<dd>Error thresholds config file. Default = /etc/sysconfig/opa/opamon.conf</p>
<dt>-t portsfile</p>
<dd>File with list of local HFI ports used to access fabric(s) for analysis. Default = /etc/sysconfig/opa/ports</p>
<dt>-p ports</p>
<dd>List of local HFI ports used to access fabric(s) for analysis. Default is the first active port. Specified as HFI:port as follows:</p>
<dl>
<dd>
<dl>
<dd>0:0 First active port in system</dl>
</dl>
<dl>
<dd>
<dl>
<dd>0: <i>y</i> Port <i>y</i> within system</dl>
</dl>
<dl>
<dd>
<dl>
<dd>&nbsp;<wbr><i>x</i>:0&nbsp;<wbr> First active port on HFI <i>x</i></dl>
</dl>
<dl>
<dd>
<dl>
<dd>&nbsp;<wbr><i>x</i>:&nbsp;<wbr><i>y</i>&nbsp;<wbr> HFI <i>x</i>, port <i>y</i></dl>
</dl>
<dt>-T <i>topology_input</i></p>
<dd>Name of topology input file to use. Any %P markers in this filename are replaced with the HFI:port being operated on (such as 0:0 or 1:2). Default = /etc/sysconfig/opa/topology.%P.xml. If -T NONE is specified, no topology input file is used. See <i>opareport</i> for more information.</dl>
<h2>Example</h2>
<p>opafabricanalysis<br />
 opafabricanalysis -p &#8216;1:1 1:2 2:1 2:2&#8217; The fabric analysis tool checks the following:</p>
<dl>
<dt>&bull;</p>
<dd>Fabric links (both internal to switch chassis and external cables)</p>
<dt>&bull;</p>
<dd>Fabric components (nodes, links, SMs, systems, and their SMA configuration)</p>
<dt>&bull;</p>
<dd>Fabric PMA error counters and link speed mismatches</dl>
<p> <code>NOTE:</code> The comparison includes components on the fabric. Therefore, operations such as shutting down a server cause the server to no longer appear on the fabric and are flagged as a fabric change or failure by opafabricanalysis. </p>
<h2>Environment Variables</h2>
<p>The following environment variables are also used by this command:</p>
<dl>
<dt><code>PORTS</code></p>
<dd>List of ports, used in absence of -t and -p.</p>
<dt><code>PORTS_FILE</code></p>
<dd>File containing list of ports, used in absence of -t and -p.</p>
<dt><code>FF_TOPOLOGY_FILE</code></p>
<dd>File containing topology_input (may have %P marker in filename), used in absence of -T.</p>
<dt><code>FF_ANALYSIS_DIR</code></p>
<dd>Top level directory for baselines and failed health checks.</dl>
<h2>Details</h2>
<p>For simple fabrics, the Intel(R) Omni-Path Fabric Suite FastFabric Toolset host is connected to a single fabric. By default, the first active port on the FastFabric Toolset host is used to analyze the fabric. However, in more complex fabrics, the FastFabric Toolset host may be connected to more than one fabric or subnet. In this case, you can specify the ports or HFIs to use with one of the following methods:</p>
<dl>
<dt>&bull;</p>
<dd>On the command line using the -p option.</p>
<dt>&bull;</p>
<dd>In a file specified using the -t option.</p>
<dt>&bull;</p>
<dd>Through the environment variables <code>PORTS</code> or <code>PORTS_FILE</code>.</p>
<dt>&bull;</p>
<dd>Using the <code>PORTS_FILE</code> configuration option in opafastfabric.conf.</dl>
<p> If the specified port does not exist or is empty, the first active port on the local system is used. In more complex configurations, you must specify the exact ports to use for all fabrics to be analyzed. For more information, refer to. </p>
<p> You can specify the topology_input file to be used with one of the following methods:</p>
<dl>
<dt>&bull;</p>
<dd>On the command line using the -T option.</p>
<dt>&bull;</p>
<dd>In a file specified through the environment variable <code>FF_TOPOLOGY_FILE</code>.</p>
<dt>&bull;</p>
<dd>Using the ff_topology_file configuration option in opafastfabric.conf.</dl>
<p> If the specified file does not exist, no topology_input file is used. Alternately the filename can be specified as NONE to prevent use of an input file. </p>
<p> For more information, refer to <i>opareport</i> </p>
<p> By default, the error analysis includes PMA counters and slow links (that is, links running below enabled speeds). You can change this using the <code>FF_FABRIC_HEALTH</code> configuration parameter in opafastfabric.conf. This parameter specifies the opareport options and reports to be used for the health analysis. It also can specify the PMA counter clearing behavior (-I <i>seconds</i>, -C, or none at all). See <i>Appendix#8217#160;A</i> in the <i>Intel(R) Omni-Path Fabric Suite FastFabric User Guide</i> </p>
<p> for more information. </p>
<p> When a topology_input file is used, it can also be useful to extend <code>FF_FABRIC_HEALTH</code> to include fabric topology verification options such as -o verifylinks. </p>
<p> The thresholds for PMA counter analysis default to /etc/sysconfig/opa/opamon.conf. However, you can specify an alternate configuration file for thresholds using the -c option. The opamon.si.conf file can also be used to check for any non-zero values for signal integrity (SI) counters. </p>
<p> All files generated by opafabricanalysis start with fabric in their file name. This is followed by the port selection option identifying the port used for the analysis. Default is 0:0. </p>
<p> The opafabricanalysis tool generates files such as the following within FF_ANALYSIS_DIR : </p>
<p> <code>Health Check</code> </p>
<dl>
<dt>&bull;</p>
<dd>latest/fabric.0:0.errors stdout of opareport for errors encountered during fabric error analysis. </p>
<dt>&bull;</p>
<dd>latest/fabric.0.0.errors.stderr stderr of opareport during fabric error analysis. </p>
</dl>
<p> <code>Baseline</code> </p>
<p> During a baseline run, the following files are also created in FF_ANALYSIS_DIR/latest.</p>
<dl>
<dt>&bull;</p>
<dd>baseline/fabric.0:0.snapshot.xml opareport snapshot of complete fabric components and SMA configuration. </p>
<dt>&bull;</p>
<dd>baseline/fabric.0:0.comps opareport summary of fabric components and basic SMA configuration. </p>
<dt>&bull;</p>
<dd>baseline/fabric.0.0.links opareport summary of internal and external links. </p>
</dl>
<p> <code>Full Analysis</code> </p>
<dl>
<dt>&bull;</p>
<dd>latest/fabric.0:0.snapshot.xml opareport snapshot of complete fabric components and SMA configuration. </p>
<dt>&bull;</p>
<dd>latest/fabric.0:0.snapshot.stderr stderr of opareport during snapshot. </p>
<dt>&bull;</p>
<dd>latest/fabric.0:0.errors stdout of opareport for errors encountered during fabric error analysis. </p>
<dt>&bull;</p>
<dd>latest/fabric.0.0.errors.stderr stderr of opareport during fabric error analysis. </p>
<dt>&bull;</p>
<dd>latest/fabric.0:0.comps stdout of opareport for fabric components and SMA configuration. </p>
<dt>&bull;</p>
<dd>latest/fabric.0:0.comps.stderr stderr of opareport for fabric components. </p>
<dt>&bull;</p>
<dd>latest/fabric.0:0.comps.diff diff of baseline and latest fabric components. </p>
<dt>&bull;</p>
<dd>latest/fabric.0:0.links stdout of opareport summary of internal and external links. </p>
<dt>&bull;</p>
<dd>latest/fabric.0:0.links.stderr stderr of opareport summary of internal and external links. </p>
<dt>&bull;</p>
<dd>latest/fabric.0:0.links.diff diff of baseline and latest fabric internal and external links. </p>
<dt>&bull;</p>
<dd>latest/fabric.0:0.links.changes.stderr stderr of opareport comparison of links. </p>
<dt>&bull;</p>
<dd>latest/fabric.0:0.links.changes opareport comparison of links against baseline. This is typically easier to read than the links.diff file and contains the same information. </p>
<dt>&bull;</p>
<dd>latest/fabric.0:0.comps.changes.stderr stderr of opareport comparison of components. </p>
<dt>&bull;</p>
<dd>latest/fabric.0:0.comps.changes opareport comparison of components against baseline. This is typically easier to read than the comps.diff file and contains the same information. </p>
</dl>
<p> The .diff and .changes files are only created if differences are detected. </p>
<p> If the -s option is used and failures are detected, files related to the checks that failed are also copied to the time-stamped directory name under FF_ANALYSIS_DIR.</p>
<h2>Fabric Items Checked Against the Baseline</h2>
<p>Based on opareport -o links :</p>
<dl>
<dt>&bull;</p>
<dd>Unconnected/down/missing cables</p>
<dt>&bull;</p>
<dd>Added/moved cables</p>
<dt>&bull;</p>
<dd>Changes in link width and speed</p>
<dt>&bull;</p>
<dd>Changes to Node GUIDs in fabric (replacement of HFI or Switch hardware)</p>
<dt>&bull;</p>
<dd>Adding/Removing Nodes [FI, Virtual FIs, Virtual Switches, Physical Switches, Physical Switch internal switching cards (leaf/spine)]</p>
<dt>&bull;</p>
<dd>Changes to server or switch names</dl>
<p> Based on opareport -o comps :</p>
<dl>
<dt>&bull;</p>
<dd>Overlap with items from links report</p>
<dt>&bull;</p>
<dd>Changes in port MTU, LMC, number of VLs</p>
<dt>&bull;</p>
<dd>Changes in port speed/width enabled or supported</p>
<dt>&bull;</p>
<dd>Changes in HFI or switch device IDs/revisions/VendorID (for example, ASIC HW changes)</p>
<dt>&bull;</p>
<dd>Changes in port Capability mask (which features/agents run on port/server)</p>
<dt>&bull;</p>
<dd>Changes to ErrorLimits and PKey enforcement per port</p>
<dt>&bull;</p>
<dd>Changes to IOUs/IOCs/IOC Services provided </p>
</dl>
<p> Location (port, node) and number of SMs in fabric. Includes:</p>
<dl>
<dt>&bull;</p>
<dd>Primary and backups</p>
<dt>&bull;</p>
<dd>Configured priority for SM</dl>
<h2>Fabric Items Also Checked During Health Check</h2>
<p>Based on opareport -s -C -o errors -o slowlinks :</p>
<dl>
<dt>&bull;</p>
<dd>PMA error counters on all Intel(R) Omni-Path Fabric ports (HFI, switch external and switch internal) checked against configurable thresholds.</p>
<dt>&bull;</p>
<dd>Counters are cleared each time a health check is run. Each health check reflects a counter delta since last health check.</p>
<dt>&bull;</p>
<dd>Typically identifies potential fabric errors, such as symbol errors.</p>
<dt>&bull;</p>
<dd>May also identify transient congestion, depending on the counters that are monitored.</p>
<dt>&bull;</p>
<dd>Link active speed/width as compared to Enabled speed.</p>
<dt>&bull;</p>
<dd>Identifies links whose active speed/width is #8217lt; min (enabled speed/width on each side of link).</p>
<dt>&bull;</p>
<dd>This typically reflects bad cables or bad ports or poor connections.</p>
<dt>&bull;</p>
<dd>Side effect is the verification of SA health. </p>
</dl>
