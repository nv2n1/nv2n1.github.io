---
title: "iblinkinfo(8)"
name: "iblinkinfo"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iblinkinfo/"
description: "IBLINKINFO – report link info for all links in the fabric"
---

<p>IBLINKINFO &#8211; report link info for all links in the fabric</p>
<h2>Synopsis</h2>
<p>iblinkinfo &lt;options&gt;</p>
<h2>Description</h2>
<p>iblinkinfo reports link info for each port in an IB fabric, node by node. Optionally, iblinkinfo can do partial scans and limit its output to parts of a fabric.</p>
<h2>Options</h2>
<p><code>&#8211;down, -d</code> Print only nodes which have a port in the &quot;Down&quot; state. </p>
<p> <code>&#8211;line, -l</code> Print all information for each link on one line. Default is to print a header with the node information and then a list for each port (useful for grep&#8217;ing output). </p>
<p> <code>&#8211;additional, -p</code> Print additional port settings (&lt;LifeTime&gt;,&lt;HoqLife&gt;,&lt;VLStallCount&gt;) </p>
<p> <code>&#8211;switches-only</code> Show only switches in output. </p>
<p> <code>&#8211;cas-only</code> Show only CAs in output.</p>
<h3>Partial Scan flags</h3>
<p>The node to start a partial scan can be specified with the following addresses. </p>
<p> <code>&#8211;port-guid, -G &lt;port_guid&gt;</code> Specify a port_guid </p>
<p> <code>-D, &#8211;Direct &lt;dr_path&gt;</code> The address specified is a directed route </p>
<pre>Examples:
 -D &quot;0&quot; # self port
 -D &quot;0,1,2,1,4&quot; # out via port 1, then 2, ...
 (Note the second number in the path specified must match the port being
 used. This can be specified using the port selection flag '-P' or the
 port found through the automatic selection process.)</pre>
<p><code>Note:</code> For switches results are printed for all ports not just switch port 0. </p>
<p> <code>&#8211;switch, -S &lt;port_guid&gt;</code> same as &quot;-G&quot;. (provided only for backward compatibility) </p>
<p> How much of the scan to be printed can be controled with the following. </p>
<p> <code>&#8211;all, -a</code> Print all nodes found in a partial fabric scan. Normally a partial fabric scan will return only the node specified. This option will print the other nodes found as well. </p>
<p> <code>&#8211;hops, -n &lt;hops&gt;</code> Specify the number of hops away from a specified node to scan. This is useful to expand a partial fabric scan beyond the node specified.</p>
<h3>Cache File flags</h3>
<p><code>&#8211;load-cache &lt;filename&gt;</code> Load and use the cached ibnetdiscover data stored in the specified filename. May be useful for outputting and learning about other fabrics or a previous state of a fabric. </p>
<p> <code>&#8211;diff &lt;filename&gt;</code> Load cached ibnetdiscover data and do a diff comparison to the current network or another cache. A special diff output for ibnetdiscover output will be displayed showing differences between the old and current fabric. By default, the following are compared for differences: switches, channel adapters, routers, and port connections. </p>
<p> <code>&#8211;diffcheck &lt;key(s)&gt;</code> Specify what diff checks should be done in the <code>&#8211;diff</code> option above. Comma separate multiple diff check key(s). The available diff checks are: <code>sw = switches</code>, <code>ca = channel adapters</code>, <code>router</code> = routers, <code>port</code> = port connections, <code>lid</code> = lids, <code>nodedesc</code> = node descriptions. Note that <code>port</code>, <code>lid</code>, and <code>nodedesc</code> are checked only for the node types that are specified (e.g. <code>sw</code>, <code>ca</code>, <code>router</code>). If <code>port</code> is specified alongside <code>lid</code> or <code>nodedesc</code>, remote port lids and node descriptions will also be compared. </p>
<p> <code>&#8211;filterdownports &lt;filename&gt;</code> Filter downports indicated in a ibnetdiscover cache. If a port was previously indicated as down in the specified cache, and is still down, do not output it in the resulting output. This option may be particularly useful for environments where switches are not fully populated, thus much of the default iblinkinfo info is considered unuseful. See <code>ibnetdiscover</code> for information on caching ibnetdiscover output.</p>
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
<dt><code>-e</code></p>
<dd>show send and receive errors (timeouts and others) </p>
<p> <code>-h, &#8211;help</code> show the usage message</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>increase the application verbosity level. May be used several times (-vv or -v -v -v) </p>
<p> <code>-V, &#8211;version</code> show the version info.</dl>
<h2>Exit Status</h2>
<p>0 on success, -1 on failure to scan the fabric, 1 if check mode is used and inconsistencies are found.</p>
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
<h2>Author</h2>
<dl>
<dt><code>Ira Weiny</code></p>
<dd>&lt; <i>ira.weiny [at] intel.com</i> &gt; </p>
</dl>
