---
title: "ibroute(8)"
name: "ibroute"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibroute/"
description: "IBROUTE –"
---

<p>IBROUTE &#8211;</p>
<h2>Query Infiniband Switch Forwarding Tables</h2>
<h3>Synopsis</h3>
<p>ibroute [options] [&lt;dest dr_path|lid|guid&gt; [&lt;startlid&gt; [&lt;endlid&gt;]]]</p>
<h3>Description</h3>
<p>ibroute uses SMPs to display the forwarding tables (unicast (LinearForwardingTable or LFT) or multicast (MulticastForwardingTable or MFT)) for the specified switch LID and the optional lid (mlid) range. The default range is all valid entries in the range 1&#8230;FDBTop.</p>
<h3>Options</h3>
<dl>
<dt><code>-a, &#8211;all</code></p>
<dd>show all lids in range, even invalid entries</p>
<dt><code>-n, &#8211;no_dests</code></p>
<dd>do not try to resolve destinations</p>
<dt><code>-M, &#8211;Multicast</code></p>
<dd>show multicast forwarding tables In this case, the range parameters are specifying the mlid range.</dl>
<h3>Addressing Flags</h3>
<p><code>-D, &#8211;Direct</code> The address specified is a directed route </p>
<pre>Examples:
 [options] -D [options] &quot;0&quot; # self port
 [options] -D [options] &quot;0,1,2,1,4&quot; # out via port 1, then 2, ...
 (Note the second number in the path specified must match the port being
 used. This can be specified using the port selection flag '-P' or the
 port found through the automatic selection process.)</pre>
<p><code>-G, &#8211;Guid</code> The address specified is a Port GUID </p>
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
<dt><code>-y, &#8211;m_key &lt;key&gt;</code></p>
<dd>use the specified M_key for requests. If non-numeric value (like &#8216;x&#8217;) is specified then a value will be prompted for. </p>
<p> <code>&#8211;node-name-map &lt;node-name-map&gt;</code> Specify a node name map. This file maps GUIDs to more user friendly names. See FILES section. </p>
<p> <code>&#8211;config, -z &lt;config_file&gt;</code> Specify alternate config file. Default: /etc/infiniband-diags/ibdiag.conf</dl>
<h3>Files</h3>
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
<h3>Examples</h3>
<p>Unicast examples</p>
<dl>
<dt><code>::</code></p>
<dd>ibroute 4 # dump all lids with valid out ports of switch with lid 4 ibroute -a 4 # same, but dump all lids, even with invalid out ports ibroute -n 4 # simple dump format &#8211; no destination resolution ibroute 4 10 # dump lids starting from 10 (up to FDBTop) ibroute 4 0x10 0x20 # dump lid range ibroute -G 0x08f1040023 # resolve switch by GUID ibroute -D 0,1 # resolve switch by direct path </p>
<p> Multicast examples</p>
<dt><code>::</code></p>
<dd>ibroute -M 4 # dump all non empty mlids of switch with lid 4 ibroute -M 4 0xc010 0xc020 # same, but with range ibroute -M -n 4 # simple dump format</dl>
<h3>See Also</h3>
<p>ibtracert (8)</p>
<h3>Author</h3>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>halr [at] voltaire.com</i> &gt; </p>
</dl>
