---
title: "snmp-bridge-mib(1)"
name: "snmp-bridge-mib"
section: "1"
letter: "s"
url: "/docs/linux/man/1-snmp-bridge-mib/"
description: "snmp-bridge-mib – provide Linux bridge information via SNMP"
---

<h2 class="name">NAME</h2>
<p> snmp-bridge-mib &#8211; provide Linux bridge information via SNMP </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>snmp-bridge-mib</code> {bridge}</dl>
<h2>ARGUMENTS</h2>
<dd>The following arguments are required: </p>
<p> <code>bridge</code></p>
<dl>
<dt>
<dd> The name of the Linux bridge for which you want to provide information via SNMP, e.g. br0.</dl>
<h2>DESCRIPTION</h2>
<p> The snmp-bridge-mib is an extension to net-snmp. It collects information about a bridge in a Linux system and exports them for query from other (remote) systems for management purposes.</p>
<h2>CONFIGURATION:</h2>
<p> The preferred method of snmp-bridge-mib to attach to net-snmp is agentx. For this to work, you will have to add the following line to /etc/snmp/snmpd.conf, </p>
<dl>
<dt>
<dd>
<pre>
    master agentx
    
</pre>
</dl>
<p> restart snmpd and start snmp-bridge-mib. snmp-bridge-mib will then connect to the running snmpd daemon. </p>
<p> Another way of attaching snmp-bridge-mib to is to run it as an embedded perl module. You have to add </p>
<dl>
<dt>
<dd>
<pre>
    perl do &quot;path to location of snmp-bridge-mib&quot;
    
</pre>
</dl>
<p> and restart snmpd.</p>
<h2>EXAMPLE:</h2>
<p> Follow the instructions in this manpage and type </p>
<dl>
<dt>
<dd>
<pre>
    perl /usr/bin/snmp-bridge-mib br0
    
</pre>
</dl>
<p> You&#8217;ll get the following output: </p>
<dl>
<dt>
<dd>
<pre>
     registering at .1.3.6.1.2.1.17
     running as a subagent.
     dot1qbridge agent started.
     NET-SNMP version 5.4.2.1 AgentX subagent connected
     
</pre>
</dl>
<p> Now it&#8217;s time for a first test: </p>
<dl>
<dt>
<dd>
<pre>
    $ export MIBS=+BRIDGE-MIB
    $ snmpwalk localhost .1.3.6.1.2.1.17
    
</pre>
</dl>
<p> The output produced should look like </p>
<dl>
<dt>
<dd>
<pre>
    BRIDGE-MIB::dot1dStpBridgeHelloTime = INTEGER: 199 centi-seconds
    BRIDGE-MIB::dot1dStpBridgeForwardDelay = INTEGER: 1499 centi-seconds
    BRIDGE-MIB::dot1dStpPort.1 = INTEGER: 1
    BRIDGE-MIB::dot1dStpPort.3 = INTEGER: 3
    BRIDGE-MIB::dot1dStpPortPriority.1 = INTEGER: 32
    BRIDGE-MIB::dot1dStpPortPriority.3 = INTEGER: 32
    BRIDGE-MIB::dot1dStpPortState.1 = INTEGER: <a href="//www.systutorials.com/docs/linux/man/1-disabled/">disabled</a>(1)
    BRIDGE-MIB::dot1dStpPortState.3 = INTEGER: <a href="//www.systutorials.com/docs/linux/man/1-disabled/">disabled</a>(1)
    BRIDGE-MIB::dot1dStpPortEnable.1 = INTEGER: <a href="//www.systutorials.com/docs/linux/man/2-disabled/">disabled</a>(2)
    BRIDGE-MIB::dot1dStpPortEnable.3 = INTEGER: <a href="//www.systutorials.com/docs/linux/man/2-disabled/">disabled</a>(2)
    BRIDGE-MIB::dot1dStpPortPathCost.1 = INTEGER: 2
    BRIDGE-MIB::dot1dStpPortPathCost.3 = INTEGER: 4
    BRIDGE-MIB::dot1dStpPortDesignatedRoot.1 = STRING: &quot;8000.001018382c78&quot;
    BRIDGE-MIB::dot1dStpPortDesignatedRoot.3 = STRING: &quot;8000.001018382c78&quot;
    BRIDGE-MIB::dot1dStpPortDesignatedCost.1 = INTEGER: 0
    BRIDGE-MIB::dot1dStpPortDesignatedCost.3 = INTEGER: 0
    BRIDGE-MIB::dot1dStpPortDesignatedBridge.1 = STRING: &quot;8000.001018382c78&quot;
    BRIDGE-MIB::dot1dStpPortDesignatedBridge.3 = STRING: &quot;8000.001018382c78&quot;
    BRIDGE-MIB::dot1dStpPortDesignatedPort.1 = STRING: &quot;32769&quot;
    BRIDGE-MIB::dot1dStpPortDesignatedPort.3 = STRING: &quot;32770&quot;
    BRIDGE-MIB::dot1dStpPortPathCost32.1 = INTEGER: 2
    BRIDGE-MIB::dot1dStpPortPathCost32.3 = INTEGER: 4
    BRIDGE-MIB::dot1dTpLearnedEntryDiscards = Counter32: 0
    BRIDGE-MIB::dot1dTpAgingTime = INTEGER: 300 seconds
    BRIDGE-MIB::dot1dTpFdbAddress.'...8,x' = STRING: 0:10:18:38:2c:78
    BRIDGE-MIB::dot1dTpFdbAddress.'.!^/B|' = STRING: 0:21:5e:2f:42:7c
    BRIDGE-MIB::dot1dTpFdbPort.'...8,x' = INTEGER: 1
    BRIDGE-MIB::dot1dTpFdbPort.'.!^/B|' = INTEGER: 3
    BRIDGE-MIB::dot1dTpFdbStatus.'...8,x' = INTEGER: <a href="//www.systutorials.com/docs/linux/man/3-learned/">learned</a>(3)
    BRIDGE-MIB::dot1dTpFdbStatus.'.!^/B|' = INTEGER: <a href="//www.systutorials.com/docs/linux/man/3-learned/">learned</a>(3)
    BRIDGE-MIB::dot1dTpPort.1 = INTEGER: 1
    BRIDGE-MIB::dot1dTpPort.3 = INTEGER: 3
    BRIDGE-MIB::dot1dTpPortMaxInfo.1 = INTEGER: 1500 bytes
    BRIDGE-MIB::dot1dTpPortMaxInfo.3 = INTEGER: 1500 bytes
    BRIDGE-MIB::dot1dTpPortInFrames.1 = Counter32: 18082 frames
    BRIDGE-MIB::dot1dTpPortInFrames.3 = Counter32: 1546072 frames
    BRIDGE-MIB::dot1dTpPortOutFrames.1 = Counter32: 11601 frames
    BRIDGE-MIB::dot1dTpPortOutFrames.3 = Counter32: 10988 frames
    BRIDGE-MIB::dot1dTpPortInDiscards.1 = Counter32: 0 frames
    BRIDGE-MIB::dot1dTpPortInDiscards.3 = Counter32: 0 frames
    
</pre>
</dl>
<h2>BUGS</h2>
<dl>
<dt>
<dd> 1. snmp-bridge-mib currently only supports one bridge which has to be specified on the commandline.</dl>
<dl>
<dt>
<dd> 2. Not all elements of RFC 4188 because they are either not available in sysfs or difficult to extract from the existing data.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-snmpd-conf/">snmpd.conf</a></code>(5), <code><a href="/docs/linux/man/3-net--snmp/">Net::SNMP</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> <code>Jens Osterkamp</code> &lt;jens [at] linux.vnet.ibm.com&gt;</p>
<dl>
<dt>
<dd> Developer</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009, 2010 IBM Corp., All Rights Reserved </p>
<p> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: </p>
<p> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. </p>
<p> THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. </p>
<h2>Index</h2>
