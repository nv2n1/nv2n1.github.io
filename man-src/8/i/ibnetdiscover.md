---
title: "ibnetdiscover(8)"
name: "ibnetdiscover"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibnetdiscover/"
description: "IBNETDISCOVER – discover InfiniBand topology"
---

<p>IBNETDISCOVER &#8211; discover InfiniBand topology</p>
<h2>Synopsis</h2>
<p>ibnetdiscover [options] [&lt;topology-file&gt;]</p>
<h2>Description</h2>
<p>ibnetdiscover performs IB subnet discovery and outputs a human readable topology file. GUIDs, node types, and port numbers are displayed as well as port LIDs and NodeDescriptions. All nodes (and links) are displayed (full topology). Optionally, this utility can be used to list the current connected nodes by nodetype. The output is printed to standard output unless a topology file is specified.</p>
<h2>Options</h2>
<p><code>-l, &#8211;list</code> List of connected nodes </p>
<p> <code>-g, &#8211;grouping</code> Show grouping. Grouping correlates IB nodes by different vendor specific schemes. It may also show the switch external ports correspondence. </p>
<p> <code>-H, &#8211;Hca_list</code> List of connected CAs </p>
<p> <code>-S, &#8211;Switch_list</code> List of connected switches </p>
<p> <code>-R, &#8211;Router_list</code> List of connected routers </p>
<p> <code>-s, &#8211;show</code> Show progress information during discovery. </p>
<p> <code>-f, &#8211;full</code> Show full information (ports&#8217; speed and width, vlcap) </p>
<p> <code>-p, &#8211;ports</code> Obtain a ports report which is a list of connected ports with relevant information (like LID, portnum, GUID, width, speed, and NodeDescription). </p>
<p> <code>-m, &#8211;max_hops</code> Report max hops discovered.</p>
<dl>
<dt><code>&#8211;outstanding_smps, -o &lt;val&gt;</code></p>
<dd>Specify the number of outstanding SMP&#8217;s which should be issued during the scan </p>
<p> Default: 2</dl>
<h3>Cache File flags</h3>
<p><code>&#8211;cache &lt;filename&gt;</code> Cache the ibnetdiscover network data in the specified filename. This cache may be used by other tools for later analysis. </p>
<p> <code>&#8211;load-cache &lt;filename&gt;</code> Load and use the cached ibnetdiscover data stored in the specified filename. May be useful for outputting and learning about other fabrics or a previous state of a fabric. </p>
<p> <code>&#8211;diff &lt;filename&gt;</code> Load cached ibnetdiscover data and do a diff comparison to the current network or another cache. A special diff output for ibnetdiscover output will be displayed showing differences between the old and current fabric. By default, the following are compared for differences: switches, channel adapters, routers, and port connections. </p>
<p> <code>&#8211;diffcheck &lt;key(s)&gt;</code> Specify what diff checks should be done in the <code>&#8211;diff</code> option above. Comma separate multiple diff check key(s). The available diff checks are: <code>sw = switches</code>, <code>ca = channel adapters</code>, <code>router</code> = routers, <code>port</code> = port connections, <code>lid</code> = lids, <code>nodedesc</code> = node descriptions. Note that <code>port</code>, <code>lid</code>, and <code>nodedesc</code> are checked only for the node types that are specified (e.g. <code>sw</code>, <code>ca</code>, <code>router</code>). If <code>port</code> is specified alongside <code>lid</code> or <code>nodedesc</code>, remote port lids and node descriptions will also be compared.</p>
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
<h3>Configuration flags</h3>
<p><code>&#8211;config, -z &lt;config_file&gt;</code> Specify alternate config file. Default: /etc/infiniband-diags/ibdiag.conf</p>
<dl>
<dt><code>&#8211;outstanding_smps, -o &lt;val&gt;</code></p>
<dd>Specify the number of outstanding SMP&#8217;s which should be issued during the scan </p>
<p> Default: 2 </p>
<p> <code>&#8211;node-name-map &lt;node-name-map&gt;</code> Specify a node name map. This file maps GUIDs to more user friendly names. See FILES section. </p>
<p> <code>-t, &#8211;timeout &lt;timeout_ms&gt;</code> override the default timeout for the solicited mads.</p>
<dt><code>-y, &#8211;m_key &lt;key&gt;</code></p>
<dd>use the specified M_key for requests. If non-numeric value (like &#8216;x&#8217;) is specified then a value will be prompted for.</dl>
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
<h2>Files</h2>
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
<h2>Authors</h2>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>halr [at] voltaire.com</i> &gt;</p>
<dt><code>Ira Weiny</code></p>
<dd>&lt; <i>ira.weiny [at] intel.com</i> &gt; </p>
</dl>
