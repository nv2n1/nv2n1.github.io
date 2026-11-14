---
title: "opareport(8)"
name: "opareport"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opareport/"
description: "opareport"
---

<p>opareport </p>
<p> <code>(All)</code> Provides powerful fabric analysis and reporting capabilities. Must be run on a host connected to the Intel(R) Omni-Path Fabric with the Intel(R) Omni-Path Fabric Suite FastFabric Toolset installed.</p>
<h2>Syntax</h2>
<p>opareport [-v][-q] [-h <i>hfi</i>] [-p <i>port</i>]<br />
 [-o <i>report</i>] [-d <i>detail</i>] [-P|-H] [-N] [-x]<br />
 [-X <i>snapshot_input</i>] [-T <i>topology_input</i>] [-s] [-r] [-V]<br />
 [-i#8217#160; <i>seconds</i>] [-C] [-a] [-m] [-K <i>mkey</i>] [-M] [-A] [-c <i>file</i>] [-L]<br />
 [-F <i>point</i>] [-S <i>point</i>] [-D <i>point</i>] [-Q]</p>
<h2>Options</h2>
<dl>
<dt>&#8211;help</p>
<dd>Produces full help text. </p>
<dt>-v/&#8211;verbose</p>
<dd>Returns verbose output. </p>
<dt>-q/&#8211;quiet</p>
<dd>Disables progress reports. </p>
<dt>-h/&#8211;hfi <i>hfi</i></p>
<dd>HFI, numbered 1..n. Using 0 specifies that the -p <i>port</i> port is a system-wide port number. Default is 0. </p>
<dt>-p/&#8211;port <i>port</i></p>
<dd>Port, numbered 1..n. If -h <i>hfi</i> is 0 then <i>port</i> is a system-wide port number. Default is 1. </p>
<dt>-o/&#8211;output <i>report</i></p>
<dd>Report type for output. Refer to <i>Report Types</i> for details. </p>
<dt>-d/&#8211;detail <i>detail</i></p>
<dd>Level of detail 0-n for output. Default is 2. </p>
<dt>-P/&#8211;persist</p>
<dd>Includes data persistent across reboots. </p>
<dt>-H/&#8211;hard</p>
<dd>Includes permanent hardware data. </p>
<dt>-N/&#8211;noname</p>
<dd>Omits node and IOC names. </p>
<dt>-x/&#8211;xml</p>
<dd>Produces output in XML. </p>
<dt>-X/&#8211;infile <i>snapshot_input</i></p>
<dd>Generates a report using the data in the snapshot_input file. snapshot_input must have been generated during a previous -o <i>snapshot</i> run. When used, the -s, -i, -C, and -a options are ignored. Not permitted with -o <i>route</i> and -F <i>route</i>. &#8216;-&#8216; may be used as the snapshot_input to specify stdin. </p>
<dt>-T/&#8211;topology <i>topology_input</i></p>
<dd>Uses topology_input file to augment and verify fabric information. When used, various reports can be augmented with information not available electronically (such as cable labels and lengths). &#8216;-&#8216; may be used to specify stdin. </p>
<dt>-s/&#8211;stats</p>
<dd>Gets performance statistics for all ports. </p>
<dt>-i/&#8211;interval <i>seconds</i></p>
<dd>Obtains performance statistics over interval <i>seconds</i>, clears all statistics, waits interval <i>seconds</i>, then generates report. Implies -s option. </p>
<dt>-C/&#8211;clear</p>
<dd>Clears performance statistics for all ports. Only statistics with error thresholds are cleared. A clear occurs after generating the report. </p>
<dt>-a/&#8211;clearall</p>
<dd>Clears all performance statistics for all ports. </p>
<dt>-m/&#8211;smadirect</p>
<dd>Accesses fabric information directly from SMA. </p>
<dt>-K/&#8211;mkey <i>mkey</i></p>
<dd>SMA M_Key for direct SMA query. Default is 0. </p>
<dt>-M/&#8211;pmadirect</p>
<dd>Accesses performance statistics using direct PMA. </p>
<dt>-A/&#8211;allports</p>
<dd>Gets PortInfo for down switch ports. Uses direct SMA to get this data. If used with -M, also gets PMA stats for down-switch ports. </p>
<dt>-c/&#8211;config <i>file</i></p>
<dd>Error thresholds configuration file. Default is /etc/sysconfig/opa/opamon.conf file. </p>
<dt>-L/&#8211;limit</p>
<dd>Limits operation to exact specified focus with -F for port error counters check (-o <i>errors</i>) and port counters clear (-C or -i). Normally, the neighbor of each selected port is also checked/cleared. Does not affect other reports. </p>
<dt>-F/&#8211;focus <i>point</i></p>
<dd>Focus area for report. Used for all reports except route to limit scope of report. Refer to <i>Point Syntax</i> for details. </p>
<dt>-S/&#8211;src <i>point</i></p>
<dd>Source for trace route, default is local port. Refer to <i>Point Syntax</i> for details. </p>
<dt>-D/&#8211;dest <i>point</i></p>
<dd>Destination for trace route. Refer to <i>Point Syntax</i> for details. </p>
<dt>-Q/&#8211;quietfocus</p>
<dd>Excludes focus description from report. </p>
</dl>
<h2>-h and -p options permit a variety of selections:</h2>
<dl>
<dt>-h 0</p>
<dd>First active port in system (default). </p>
<dt>-h 0 -p 0</p>
<dd>First active port in system. </p>
<dt>-h <i>x</i></p>
<dd>First active port on HFI <i>x</i>. </p>
<dt>-h <i>x</i>#8217#160;-p 0</p>
<dd>First active port on HFI <i>x</i>. </p>
<dt>-h 0 -p <i>y</i></p>
<dd>Port <i>y</i>#8217#160;within system (no matter which ports are active). </p>
<dt>-h <i>x</i>#8217#160;-p <i>y</i></p>
<dd>HFI <i>x</i>, port <i>y</i>. </p>
</dl>
<h2>Snapshot-Specific Options</h2>
<dl>
<dt>-r/&#8211;routes</p>
<dd>Gets routing tables for all switches. </p>
<dt>-V/&#8211;vltables</p>
<dd>Gets QOS VL-related tables for all ports. </p>
</dl>
<h2>Report Types</h2>
<dl>
<dt>comps</p>
<dd>Summary of all systems and SMs in fabric. </p>
<dt>brcomps</p>
<dd>Brief summary of all systems and SMs in fabric. </p>
<dt>nodes</p>
<dd>Summary of all node types and SMs in fabric. </p>
<dt>brnodes</p>
<dd>Brief summary of all node types and SMs in fabric. </p>
<dt>ious</p>
<dd>Summary of all IO units in the fabric. </p>
<dt>lids</p>
<dd>Summary of all LIDs in the fabric. </p>
<dt>links</p>
<dd>Summary of all links. </p>
<dt>extlinks</p>
<dd>Summary of links external to systems. </p>
<dt>slowlinks</p>
<dd>Summary of links running slower than expected. </p>
<dt>slowconfiglinks</p>
<dd>Summary of links configured to run slower than supported, includes slowlinks. </p>
<dt>slowconnlinks</p>
<dd>Summary of links connected with mismatched speed potential, includes slowconfiglinks. </p>
<dt>misconfiglinks</p>
<dd>Summary of links configured to run slower than supported. </p>
<dt>misconnlinks</p>
<dd>Summary of links connected with mismatched speed potential. </p>
<dt>errors</p>
<dd>Summary of links whose errors exceed counts in the configuration file. </p>
<dt>otherports</p>
<dd>Summary of ports not connected to the fabric. </p>
<dt>linear</p>
<dd>Summary of linear forwarding data base (FDB) for each switch. </p>
<dt>mcast</p>
<dd>Summary of multicast FDB for each switch in the fabric. </p>
<dt>portusage</p>
<dd>Summary of ports referenced in linear FDB for each switch, broken down by NodeType of DLID. </p>
<dt>pathusage</p>
<dd>Summary of number of FI to FI paths routed through each switch port. </p>
<dt>treepathusage</p>
<dd>Analysis of number of FI to FI paths routed through each switch port for a FAT tree. </p>
<dt>portgroups</p>
<dd>Summary of adaptive routing port groups for each switch. </p>
<dt>quarantinednodes</p>
<dd>Summary of quarantined nodes. </p>
<dt>validateroutes</p>
<dd>Validates all routes in the fabric. </p>
<dt>validatepgs</p>
<dd>Validates all port groups in the fabric. </p>
<dt>validatecreditloops</p>
<dd>Validates topology configuration of the fabric to identify any existing credit loops. </p>
<dt>vfinfo</p>
<dd>Summary of virtual fabric (vFabric) information. </p>
<dt>vfmember</p>
<dd>Summary of vFabric membership information. </p>
<dt>verifyfis</p>
<dd>Compares fabric (or snapshot) FIs to supplied topology and identifies differences and omissions. </p>
<dt>verifysws</p>
<dd>Compares fabric (or snapshot) switches to supplied topology and identifies differences and omissions. </p>
<dt>verifynodes</p>
<dd>Returns verifyfis and verifysws reports. </p>
<dt>verifysms</p>
<dd>Compares fabric (or snapshot) SMs to supplied topology and identifies differences and omissions. </p>
<dt>verifylinks</p>
<dd>Compares fabric (or snapshot) links to supplied topology and identifies differences and omissions. </p>
<dt>verifyextlinks</p>
<dd>Compares fabric (or snapshot) links to supplied topology and identifies differences and omissions. Limits analysis to links external to systems. </p>
<dt>verifyall</p>
<dd>Returns verifyfis, verifysws, verifysms, and verifylinks reports. </p>
<dt>all</p>
<dd>Returns comps, nodes, ious, links, extlinks, slowconnlinks, and errors reports. </p>
<dt>route</p>
<dd>Traces route between -S and -D points. </p>
<dt>bfrctrl</p>
<dd>Reports Buffer Control Tables for all ports. </p>
<dt>snapshot</p>
<dd>Outputs snapshot of the fabric state for later use as <i>snapshot_input</i>. This implies -x. May not be combined with other reports. When selected, -F, -P, -H, and -N options are ignored. </p>
<dt>topology</p>
<dd>Outputs the topology of the fabric for later use as <i>topology_input</i>. This implies -x. May not be combined with other reports.</p>
<dt>none</p>
<dd>No report, useful to clear statistics. </p>
</dl>
<h2>Point Syntax</h2>
<dl>
<dt>gid: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is numeric port GID of form: subnet:guid. </p>
<dt>lid: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is numeric LID. </p>
<dt>lid: <i>value</i>:node</p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is numeric LID, selects entire node with given LID. </p>
<dt>lid: <i>value</i>:port: <i>value2</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is numeric LID of node,&nbsp;<wbr>&nbsp;<wbr><i>value2</i>&nbsp;<wbr>is port number. </p>
<dt>portguid: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is numeric port GUID. </p>
<dt>nodeguid: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is numeric node GUID. </p>
<dt>nodeguid: <i>value1</i>: <i>port</i>: <i>value2</i></p>
<dd>&nbsp;<wbr><i>value1</i>&nbsp;<wbr>is numeric node GUID,&nbsp;<wbr>&nbsp;<wbr><i>value2</i>&nbsp;<wbr>is port number. </p>
<dt>iocguid: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is numeric IOC GUID. </p>
<dt>iocguid: <i>value1</i>:port: <i>value2</i></p>
<dd>&nbsp;<wbr><i>value1</i>&nbsp;<wbr>is numeric IOC GUID,&nbsp;<wbr>&nbsp;<wbr><i>value2</i>&nbsp;<wbr>is port number. </p>
<dt>systemguid: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is numeric system image GUID. </p>
<dt>systemguid: <i>value1</i>:port: <i>value2</i></p>
<dd>&nbsp;<wbr><i>value1</i>&nbsp;<wbr>is the numeric system image GUID,&nbsp;<wbr>&nbsp;<wbr><i>value2</i>&nbsp;<wbr>is port number. </p>
<dt>ioc: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is IOC Profile ID String&nbsp;<wbr>(IOC Name). </p>
<dt>ioc: <i>value1</i>:port: <i>value2</i></p>
<dd>&nbsp;<wbr><i>value1</i>&nbsp;<wbr>is IOC Profile ID String&nbsp;<wbr>(IOC Name),&nbsp;<wbr>&nbsp;<wbr><i>value2</i>&nbsp;<wbr>is port number. </p>
<dt>iocpat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for IOC Profile ID String&nbsp;<wbr>(IOC Name). </p>
<dt>iocpat: <i>value1</i>:port: <i>value2</i></p>
<dd>&nbsp;<wbr><i>value1</i>&nbsp;<wbr>is glob pattern for IOC Profile ID String&nbsp;<wbr>(IOC Name),&nbsp;<wbr>&nbsp;<wbr><i>value2</i>&nbsp;<wbr>is port number. </p>
<dt>ioctype: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is IOC type&nbsp;<wbr>(VNIC or SRP). </p>
<dt>ioctype: <i>value1</i>:port: <i>value2</i></p>
<dd>&nbsp;<wbr><i>value1</i>&nbsp;<wbr>is IOC type&nbsp;<wbr>(VNIC or SRP),&nbsp;<wbr>&nbsp;<wbr><i>value2</i>&nbsp;<wbr>is port number. </p>
<dt>node: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is node description&nbsp;<wbr>(node name). </p>
<dt>node: <i>value1</i>:port: <i>value2</i></p>
<dd>&nbsp;<wbr><i>value1</i>&nbsp;<wbr>is node description&nbsp;<wbr>(node name),&nbsp;<wbr>&nbsp;<wbr><i>value2</i>&nbsp;<wbr>is port number. </p>
<dt>nodepat: <i>value</i></p>
<dd>&nbsp;<wbr><i>#8217gt;value</i>&nbsp;<wbr>is glob pattern for node description&nbsp;<wbr>(node name). </p>
<dt>nodepat: <i>value1</i>:port: <i>value2</i></p>
<dd>&nbsp;<wbr><i>value1</i>&nbsp;<wbr>is the glob pattern for the node description&nbsp;<wbr>(node name),&nbsp;<wbr>&nbsp;<wbr><i>value2</i>&nbsp;<wbr>is port number. </p>
<dt>nodedetpat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for node details. </p>
<dt>nodedetpat: <i>value1</i>:port: <i>value2</i></p>
<dd>&nbsp;<wbr><i>value1</i>&nbsp;<wbr>is the glob pattern for the node details,&nbsp;<wbr>&nbsp;<wbr><i>value2</i>&nbsp;<wbr>is port number. </p>
<dt>nodetype: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is node type&nbsp;<wbr>(SW, FI, or RT). </p>
<dt>nodetype: <i>value1</i>:port: <i>value2</i></p>
<dd>&nbsp;<wbr><i>value1</i>&nbsp;<wbr>is node type&nbsp;<wbr>(SW, FI, or RT),&nbsp;<wbr>&nbsp;<wbr><i>value2</i>&nbsp;<wbr>is port number. </p>
<dt>rate: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is string for rate&nbsp;<wbr>(25g, 50g, 75g, 100g), omits switch mgmt port 0. </p>
<dt>portstate: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is a string for state&nbsp;<wbr>(init, armed, active). </p>
<dt>portphysstate: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is a string for PHYs state&nbsp;<wbr>(polling, disabled, training, linkup, recovery, offline, test) </p>
<dt>mtucap: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is MTU size&nbsp;<wbr>(2048, 4096, 8192, 10240), omits switch mgmt port 0. </p>
<dt>labelpat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for cable label. </p>
<dt>lengthpat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for cable length. </p>
<dt>cabledetpat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for cable details. </p>
<dt>cabinflenpat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for cable info length. </p>
<dt>cabinfvendnamepat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for cable info vendor name. </p>
<dt>cabinfvendpnpat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for cable info vendor part number. </p>
<dt>cabinfvendrevpat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for cable info vendor revision. </p>
<dt>cabinftype: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is either optical, passive_copper, active_copper, or unknown. </p>
<dt>cabinfvendsnpat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for cable info vendor serial number. </p>
<dt>linkdetpat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for link details. </p>
<dt>portdetpat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for port details. </p>
<dt>sm</p>
<dd>Master subnet manager (SM). </p>
<dt>smdetpat: <i>value</i></p>
<dd>&nbsp;<wbr><i>value</i>&nbsp;<wbr>is glob pattern for SM details. </p>
<dt>route: <i>point1</i>: <i>point2</i></p>
<dd>All ports along the routes between the two given points. </p>
<dt>linkqual: <i>value</i></p>
<dd>Ports with a link quality equal to <i>value</i>. </p>
<dt>linkqualLE: <i>value</i></p>
<dd>Ports with a link quality less than or equal to <i>value</i>. </p>
<dt>linkqualGE: <i>value</i></p>
<dd>Ports with a link quality greater than or equal to <i>value</i>. </p>
</dl>
<h2>Examples</h2>
<p>opareport can generate hundreds of different reports. Commonly generated reports include the following:opareport -o comps -d 3<br />
 opareport -o errors -o slowlinks<br />
 opareport -o nodes -F portguid:0x00117500a000447b<br />
 opareport -o nodes -F nodeguid:0x001175009800447b:port:1<br />
 opareport -o nodes -F nodeguid:0x001175009800447b<br />
 opareport -o nodes -F &#8216;node:duster hfi1_0&#8217;<br />
 opareport -o nodes -F &#8216;node:duster hfi1_0:port:1&#8217;<br />
 opareport -o nodes -F &#8216;nodepat:d*&#8217;<br />
 opareport -o nodes -F &#8216;nodepat:d*:port:1&#8217;<br />
 opareport -o nodes -F &#8216;nodedetpat:compute*&#8217;<br />
 opareport -o nodes -F &#8216;nodedetpat:compute*:port:1&#8217;<br />
 opareport -o nodes -F nodetype:FI<br />
 opareport -o nodes -F nodetype:FI:port:1<br />
 opareport -o nodes -F lid:1<br />
 opareport -o nodes -F lid:1:node<br />
 opareport -o nodes -F lid:1:port:2<br />
 opareport -o nodes -F gid:0xfe80000000000000:0x00117500a000447b<br />
 opareport -o nodes -F systemguid:0x001175009800447b<br />
 opareport -o nodes -F systemguid:0x001175009800447b:port:1<br />
 opareport -o nodes -F iocguid:0x00117501300001e0<br />
 opareport -o nodes -F iocguid:0x00117501300001e0:port:2<br />
 opareport -o nodes -F &#8216;ioc:Chassis 0x001175005000010C, Slot 2, IOC 1&#8217;<br />
 opareport -o nodes -F &#8216;ioc:Chassis 0x001175005000010C, Slot 2, IOC 1:port:2&#8217;<br />
 opareport -o nodes -F &#8216;iocpat:*Slot 2*&#8217;<br />
 opareport -o nodes -F &#8216;iocpat:*Slot 2*:port:2&#8217;<br />
 opareport -o nodes -F ioctype:VNIC<br />
 opareport -o nodes -F ioctype:VNIC:port:2<br />
 opareport -o extlinks -F rate:5g<br />
 opareport -o extlinks -F portstate:armed<br />
 opareport -o extlinks -F portphysstate:linkup<br />
 opareport -o extlinks -F &#8216;labelpat:S1345*&#8217;<br />
 opareport -o extlinks -F &#8216;lengthpat:11m&#8217;<br />
 opareport -o extlinks -F &#8216;cabledetpat:*gore*&#8217;<br />
 opareport -o extlinks -F &#8216;linkdetpat:*core ISL*&#8217;<br />
 opareport -o extlinks -F &#8216;portdetpat:*mgmt*&#8217;<br />
 opareport -o links -F mtucap:2048<br />
 opareport -o nodes -F sm<br />
 opareport -o nodes -F &#8216;smdetpat:primary*&#8217;<br />
 opareport -o nodes -F &#8216;route:node:duster hfi1_0:node:cuda hfi1_0&#8217;<br />
 opareport -o nodes -F &#8216;route:node:duster hfi1_0:port:1:node:cuda hfi1_0:port:2&#8217;<br />
 opareport -s -o snapshot #8217gt; file<br />
 opareport -o topology #8217gt; topology.xml<br />
 opareport -o errors -X file </p>
<h2>Other Information</h2>
<p>opareport also supports operation with the Fabric Manager Performance Manager (PM)/Performance Manager Agent (PMA). When opareport detects the presence of a PMA, it automatically issues any required PortCounter queries and clears to the PMA to access the PMs running totals. If a PMA is not detected, then opareport directly accesses the PMAs on all the nodes. The -M option can force access to the PMA even if a PMA is present. </p>
<p> opareport takes advantage of these interfaces to obtain extensive information about the fabric from the subnet manager and the end nodes. Using this information, opareport is able to cross-reference it and produce analysis greatly beyond what any single subnet manager request could provide. As such, it exceeds the capabilities previously available in tools such as opasaquery and opafabricinfo. </p>
<p> opareport obtains and displays 64-bit data movement counters from the Fabric Manager PM/PA or directly from the fabric using the -M option. Snapshots generated by this version of opareport, in conjunction with the -s option, may report value out of range errors when used as input to older versions of opareport. However, the thresholds specified in opamon.conf and other input configuration files continue to only support 32-bit values for data movement counter thresholds. </p>
<p> opareport internally cross-references all this information so its output can be in user-friendly form. Reports include GUIDs, LIDs, and names for components. Obviously, these reports are easiest to read if the end user has taken the time to provide unique names for all the components in the fabric (node names and IOC names). All Intel components support this capability. For hosts, the node names are automatically assigned based on the network host name of the server. For switches and line cards, the names can be assigned using the element managers for each component. </p>
<p> Each run of opareport obtains up-to-date information from the fabric. At the start of the run opareport takes a few seconds to obtain all the fabric data, then it is output to stdout. The reports are sorted by GUIDs and other permanent information so they can be rerun in the future and produce output in the same order even if components have been rebooted. This is useful for comparison using simple tools like diff. opareport permits multiple reports to be requested for a single run (for example, one of each report type). </p>
<p> By default, opareport uses the first active port on the local system. However, if the Management Node is connected to more than one fabric (for example, a subnet), the Intel(R) Omni-Path Host Fabric Interface (HFI) and port may be specified to select the fabric to analyze.</p>
