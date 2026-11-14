---
title: "infiniband-diags(8)"
name: "infiniband-diags"
section: "8"
letter: "i"
url: "/docs/linux/man/8-infiniband-diags/"
description: "INFINIBAND-DIAGS –"
---

<p>INFINIBAND-DIAGS &#8211;</p>
<h2>Diagnostics For Infiniband Fabrics</h2>
<h3>Description</h3>
<p>infiniband-diags is a set of utilities designed to help configure, debug, and maintain infiniband fabrics. Many tools and utilities are provided. Some with similar functionality. </p>
<p> The base utilities use directed route MAD&#8217;s to perform their operations. They may therefore work even in unconfigured subnets. Other, higher level utilities, require LID routed MAD&#8217;s and to some extent SA/SM access.</p>
<h3>THE USE OF SMPs (QP0)</h3>
<p>Many of the tools in this package rely on the use of SMPs via QP0 to acquire data directly from the SMA. While this mode of operation is not technically in compliance with the InfiniBand specification, practical experience has found that this level of diagnostics is valuable when working with a fabric which is broken or only partially configured. For this reason many of these tools may require the use of an MKey or operation from Virtual Machines may be restricted for security reasons.</p>
<h3>Common Options</h3>
<p>Most OpenIB diagnostics take some of the following common flags. The exact list of supported flags per utility can be found in the documentation for those commands.</p>
<h3>Addressing Flags</h3>
<p>The -D and -G option have two forms: </p>
<p> <code>-D, &#8211;Direct</code> The address specified is a directed route </p>
<pre>Examples:
 [options] -D [options] &quot;0&quot; # self port
 [options] -D [options] &quot;0,1,2,1,4&quot; # out via port 1, then 2, ...
 (Note the second number in the path specified must match the port being
 used. This can be specified using the port selection flag '-P' or the
 port found through the automatic selection process.)</pre>
<p><code>-D, &#8211;Direct &lt;dr_path&gt;</code> The address specified is a directed route </p>
<pre>Examples:
 -D &quot;0&quot; # self port
 -D &quot;0,1,2,1,4&quot; # out via port 1, then 2, ...
 (Note the second number in the path specified must match the port being
 used. This can be specified using the port selection flag '-P' or the
 port found through the automatic selection process.)</pre>
<p><code>-G, &#8211;Guid</code> The address specified is a Port GUID </p>
<p> <code>&#8211;port-guid, -G &lt;port_guid&gt;</code> Specify a port_guid </p>
<p> <code>-L, &#8211;Lid</code> The address specified is a LID </p>
<p> <code>-s, &#8211;sm_port &lt;smlid&gt;</code> use &#8216;smlid&#8217; as the target lid for SA queries.</p>
<h3>Port Selection flags</h3>
<p><code>-C, &#8211;Ca &lt;ca_name&gt;</code> use the specified ca_name. </p>
<p> <code>-P, &#8211;Port &lt;ca_port&gt;</code> use the specified ca_port.</p>
<h3>Local port Selection</h3>
<p>Multiple port/Multiple CA support: when no IB device or port is specified (see the &quot;local umad parameters&quot; below), the libibumad library selects the port to use by the following criteria:</p>
<dl>
<dt>1.</p>
<dd>the first port that is ACTIVE.</p>
<dt>2.</p>
<dd>if not found, the first port that is UP (physical link up). </p>
<p> If a port and/or CA name is specified, the libibumad library attempts to fulfill the user request, and will fail if it is not possible. </p>
<p> For example: </p>
<pre>ibaddr # use the first port (criteria #1 above)
ibaddr -C mthca1 # pick the best port from &quot;mthca1&quot; only.
ibaddr -P 2 # use the second (active/up) port from the first available IB device.
ibaddr -C mthca0 -P 2 # use the specified port only.</pre>
</dl>
<h3>Debugging flags</h3>
<dl>
<dt><code>-d</code></p>
<dd>raise the IB debugging level. May be used several times (-ddd or -d -d -d).</p>
<dt><code>-e</code></p>
<dd>show send and receive errors (timeouts and others) </p>
<p> <code>-h, &#8211;help</code> show the usage message</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>increase the application verbosity level. May be used several times (-vv or -v -v -v) </p>
<p> <code>-V, &#8211;version</code> show the version info.</dl>
<h3>Configuration flags</h3>
<p><code>-t, &#8211;timeout &lt;timeout_ms&gt;</code> override the default timeout for the solicited mads.</p>
<dl>
<dt><code>&#8211;outstanding_smps, -o &lt;val&gt;</code></p>
<dd>Specify the number of outstanding SMP&#8217;s which should be issued during the scan </p>
<p> Default: 2 </p>
<p> <code>&#8211;node-name-map &lt;node-name-map&gt;</code> Specify a node name map. This file maps GUIDs to more user friendly names. See FILES section. </p>
<p> <code>&#8211;config, -z &lt;config_file&gt;</code> Specify alternate config file. Default: /etc/infiniband-diags/ibdiag.conf</dl>
<h3>Common Files</h3>
<p>The following config files are common amongst many of the utilities.</p>
<h3>Config File</h3>
<p>/etc/infiniband-diags/ibdiag.conf </p>
<p> A global config file is provided to set some of the common options for all tools. See supplied config file for details.</p>
<h3>Node Name Map File Format</h3>
<p>The node name map is used to specify user friendly names for nodes in the output. GUIDs are used to perform the lookup. </p>
<p> This functionality is provided by the opensm-libs package. See <code><a href="/docs/linux/man/8-opensm/">opensm</a>(8)</code> for the file location for your installation. </p>
<p> <code>Generically:</code> </p>
<pre># comment
&lt;guid&gt; &quot;&lt;name&gt;&quot;</pre>
<p><code>Example:</code> </p>
<pre># IB1
# Line cards
0x0008f104003f125c &quot;IB1 (Rack 11 slot 1 ) ISR9288/ISR9096 Voltaire sLB-24D&quot;
0x0008f104003f125d &quot;IB1 (Rack 11 slot 1 ) ISR9288/ISR9096 Voltaire sLB-24D&quot;
0x0008f104003f10d2 &quot;IB1 (Rack 11 slot 2 ) ISR9288/ISR9096 Voltaire sLB-24D&quot;
0x0008f104003f10d3 &quot;IB1 (Rack 11 slot 2 ) ISR9288/ISR9096 Voltaire sLB-24D&quot;
0x0008f104003f10bf &quot;IB1 (Rack 11 slot 12 ) ISR9288/ISR9096 Voltaire sLB-24D&quot;
# Spines
0x0008f10400400e2d &quot;IB1 (Rack 11 spine 1 ) ISR9288 Voltaire sFB-12D&quot;
0x0008f10400400e2e &quot;IB1 (Rack 11 spine 1 ) ISR9288 Voltaire sFB-12D&quot;
0x0008f10400400e2f &quot;IB1 (Rack 11 spine 1 ) ISR9288 Voltaire sFB-12D&quot;
0x0008f10400400e31 &quot;IB1 (Rack 11 spine 2 ) ISR9288 Voltaire sFB-12D&quot;
0x0008f10400400e32 &quot;IB1 (Rack 11 spine 2 ) ISR9288 Voltaire sFB-12D&quot;
# GUID Node Name
0x0008f10400411a08 &quot;SW1 (Rack 3) ISR9024 Voltaire 9024D&quot;
0x0008f10400411a28 &quot;SW2 (Rack 3) ISR9024 Voltaire 9024D&quot;
0x0008f10400411a34 &quot;SW3 (Rack 3) ISR9024 Voltaire 9024D&quot;
0x0008f104004119d0 &quot;SW4 (Rack 3) ISR9024 Voltaire 9024D&quot;</pre>
<h3>Topology File Format</h3>
<p>The topology file format is human readable and largely intuitive. Most identifiers are given textual names like vendor ID (vendid), device ID (device ID), GUIDs of various types (sysimgguid, caguid, switchguid, etc.). PortGUIDs are shown in parentheses (). For switches, this is shown on the switchguid line. For CA and router ports, it is shown on the connectivity lines. The IB node is identified followed by the number of ports and a quoted the node GUID. On the right of this line is a comment (#) followed by the NodeDescription in quotes. If the node is a switch, this line also contains whether switch port 0 is base or enhanced, and the LID and LMC of port 0. Subsequent lines pertaining to this node show the connectivity. On the left is the port number of the current node. On the right is the peer node (node at other end of link). It is identified in quotes with nodetype followed by &#8211; followed by NodeGUID with the port number in square brackets. Further on the right is a comment (#). What follows the comment is dependent on the node type. If it it a switch node, it is followed by the NodeDescription in quotes and the LID of the peer node. If it is a CA or router node, it is followed by the local LID and LMC and then followed by the NodeDescription in quotes and the LID of the peer node. The active link width and speed are then appended to the end of this output line. </p>
<p> An example of this is: </p>
<pre>#
# Topology file: generated on Tue Jun 5 14:15:10 2007
#
# Max of 3 hops discovered
# Initiated from node 0008f10403960558 port 0008f10403960559
Non-Chassis Nodes
vendid=0x8f1
devid=0x5a06
sysimgguid=0x5442ba00003000
switchguid=0x5442ba00003080(5442ba00003080)
Switch 24 &quot;S-005442ba00003080&quot; # &quot;ISR9024 Voltaire&quot; base port 0 lid 6 lmc 0
[22] &quot;H-0008f10403961354&quot;[1](8f10403961355) # &quot;MT23108 InfiniHost Mellanox Technologies&quot; lid 4 4xSDR
[10] &quot;S-0008f10400410015&quot;[1] # &quot;SW-6IB4 Voltaire&quot; lid 3 4xSDR
[8] &quot;H-0008f10403960558&quot;[2](8f1040396055a) # &quot;MT23108 InfiniHost Mellanox Technologies&quot; lid 14 4xSDR
[6] &quot;S-0008f10400410015&quot;[3] # &quot;SW-6IB4 Voltaire&quot; lid 3 4xSDR
[12] &quot;H-0008f10403960558&quot;[1](8f10403960559) # &quot;MT23108 InfiniHost Mellanox Technologies&quot; lid 10 4xSDR
vendid=0x8f1
devid=0x5a05
switchguid=0x8f10400410015(8f10400410015)
Switch 8 &quot;S-0008f10400410015&quot; # &quot;SW-6IB4 Voltaire&quot; base port 0 lid 3 lmc 0
[6] &quot;H-0008f10403960984&quot;[1](8f10403960985) # &quot;MT23108 InfiniHost Mellanox Technologies&quot; lid 16 4xSDR
[4] &quot;H-005442b100004900&quot;[1](5442b100004901) # &quot;MT23108 InfiniHost Mellanox Technologies&quot; lid 12 4xSDR
[1] &quot;S-005442ba00003080&quot;[10] # &quot;ISR9024 Voltaire&quot; lid 6 1xSDR
[3] &quot;S-005442ba00003080&quot;[6] # &quot;ISR9024 Voltaire&quot; lid 6 4xSDR
vendid=0x2c9
devid=0x5a44
caguid=0x8f10403960984
Ca 2 &quot;H-0008f10403960984&quot; # &quot;MT23108 InfiniHost Mellanox Technologies&quot;
[1](8f10403960985) &quot;S-0008f10400410015&quot;[6] # lid 16 lmc 1 &quot;SW-6IB4 Voltaire&quot; lid 3 4xSDR
vendid=0x2c9
devid=0x5a44
caguid=0x5442b100004900
Ca 2 &quot;H-005442b100004900&quot; # &quot;MT23108 InfiniHost Mellanox Technologies&quot;
[1](5442b100004901) &quot;S-0008f10400410015&quot;[4] # lid 12 lmc 1 &quot;SW-6IB4 Voltaire&quot; lid 3 4xSDR
vendid=0x2c9
devid=0x5a44
caguid=0x8f10403961354
Ca 2 &quot;H-0008f10403961354&quot; # &quot;MT23108 InfiniHost Mellanox Technologies&quot;
[1](8f10403961355) &quot;S-005442ba00003080&quot;[22] # lid 4 lmc 1 &quot;ISR9024 Voltaire&quot; lid 6 4xSDR
vendid=0x2c9
devid=0x5a44
caguid=0x8f10403960558
Ca 2 &quot;H-0008f10403960558&quot; # &quot;MT23108 InfiniHost Mellanox Technologies&quot;
[2](8f1040396055a) &quot;S-005442ba00003080&quot;[8] # lid 14 lmc 1 &quot;ISR9024 Voltaire&quot; lid 6 4xSDR
[1](8f10403960559) &quot;S-005442ba00003080&quot;[12] # lid 10 lmc 1 &quot;ISR9024 Voltaire&quot; lid 6 1xSDR</pre>
<p>When grouping is used, IB nodes are organized into chassis which are numbered. Nodes which cannot be determined to be in a chassis are displayed as &quot;Non-Chassis Nodes&quot;. External ports are also shown on the connectivity lines.</p>
<h3>Utilities list</h3>
<h3>Basic fabric conectivity</h3>
<p>See: ibnetdiscover, iblinkinfo</p>
<h3>Node information</h3>
<p>See: ibnodes, ibswitches, ibhosts, ibrouters</p>
<h3>Port information</h3>
<p>See: ibportstate, ibaddr</p>
<h3>Switch Forwarding Table info</h3>
<p>See: ibtracert, ibroute, dump_lfts, dump_mfts, check_lft_balance, ibfindnodesusing</p>
<h3>Peformance counters</h3>
<p>See: ibqueryerrors, perfquery</p>
<h3>Local HCA info</h3>
<p>See: ibstat, ibstatus</p>
<h3>Connectivity check</h3>
<p>See: ibping, ibsysstat</p>
<h3>Low level query tools</h3>
<p>See: smpquery, smpdump, saquery, sminfo</p>
<h3>Fabric verification tools</h3>
<p>See: ibidsverify</p>
<h3>Backwards compatibility scripts</h3>
<p>The following scripts have been identified as redundant and/or lower performing as compared to the above scripts. They are provided as legacy scripts when &#8211;enable-compat-utils is specified at build time. </p>
<p> ibcheckerrors, ibclearcounters, ibclearerrors, ibdatacounters ibchecknet, ibchecknode, ibcheckport, ibcheckportstate, ibcheckportwidth, ibcheckstate, ibcheckwidth, ibswportwatch, ibprintca, ibprintrt, ibprintswitch, set_nodedesc.sh</p>
<h3>Authors</h3>
<dl>
<dt><code>Ira Weiny</code></p>
<dd>&lt; <i>ira.weiny [at] intel.com</i> &gt; </p>
</dl>
