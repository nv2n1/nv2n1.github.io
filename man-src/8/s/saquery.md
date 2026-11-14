---
title: "saquery(8)"
name: "saquery"
section: "8"
letter: "s"
url: "/docs/linux/man/8-saquery/"
description: "SAQUERY –"
---

<p>SAQUERY &#8211;</p>
<h2>Query Infiniband Subnet Administration Attributes</h2>
<h3>Synopsis</h3>
<p>saquery [options] [&lt;name&gt; | &lt;lid&gt; | &lt;guid&gt;]</p>
<h3>Description</h3>
<p>saquery issues the selected SA query. Node records are queried by default.</p>
<h3>Options</h3>
<dl>
<dt><code>-p</code></p>
<dd>get PathRecord info</p>
<dt><code>-N</code></p>
<dd>get NodeRecord info</p>
<dt><code>-D, &#8211;list</code></p>
<dd>get NodeDescriptions of CAs only</p>
<dt><code>-S</code></p>
<dd>get ServiceRecord info</p>
<dt><code>-I</code></p>
<dd>get InformInfoRecord (subscription) info</p>
<dt><code>-L</code></p>
<dd>return the Lids of the name specified</p>
<dt><code>-l</code></p>
<dd>return the unique Lid of the name specified</p>
<dt><code>-G</code></p>
<dd>return the Guids of the name specified</p>
<dt><code>-O</code></p>
<dd>return the name for the Lid specified</p>
<dt><code>-U</code></p>
<dd>return the name for the Guid specified</p>
<dt><code>-c</code></p>
<dd>get the SA&#8217;s class port info</p>
<dt><code>-s</code></p>
<dd>return the PortInfoRecords with isSM or isSMdisabled capability mask bit on</p>
<dt><code>-g</code></p>
<dd>get multicast group info</p>
<dt><code>-m</code></p>
<dd>get multicast member info. If a group is specified, limit the output to the group specified and print one line containing only the GUID and node description for each entry. Example: saquery -m 0xc000</p>
<dt><code>-x</code></p>
<dd>get LinkRecord info</p>
<dt><code>&#8211;src-to-dst &lt;src:dst&gt;</code></p>
<dd>get a PathRecord for &lt;src:dst&gt; where src and dst are either node names or LIDs</p>
<dt><code>&#8211;sgid-to-dgid &lt;sgid:dgid&gt;</code></p>
<dd>get a PathRecord for <code>sgid</code> to <code>dgid</code> where both GIDs are in an IPv6 format acceptable to <code>inet_pton (3)</code></p>
<dt><code>&#8211;smkey &lt;val&gt;</code></p>
<dd>use SM_Key value for the query. Will be used only with &quot;trusted&quot; queries. If non-numeric value (like &#8216;x&#8217;) is specified then saquery will prompt for a value. Default (when not specified here or in /etc/infiniband-diags/ibdiag.conf) is to use SM_Key == 0 (or &quot;untrusted&quot;)</p>
<dt><code>-K, &#8211;show_keys</code></p>
<dd>show security keys (mkey, smkey, etc.) associated with the request. </p>
<p> <code>&#8211;slid &lt;lid&gt;</code> Source LID (PathRecord) </p>
<p> <code>&#8211;dlid &lt;lid&gt;</code> Destination LID (PathRecord) </p>
<p> <code>&#8211;mlid &lt;lid&gt;</code> Multicast LID (MCMemberRecord) </p>
<p> <code>&#8211;sgid &lt;gid&gt;</code> Source GID (IPv6 format) (PathRecord) </p>
<p> <code>&#8211;dgid &lt;gid&gt;</code> Destination GID (IPv6 format) (PathRecord) </p>
<p> <code>&#8211;gid &lt;gid&gt;</code> Port GID (MCMemberRecord) </p>
<p> <code>&#8211;mgid &lt;gid&gt;</code> Multicast GID (MCMemberRecord) </p>
<p> <code>&#8211;reversible</code> Reversible path (PathRecord) </p>
<p> <code>&#8211;numb_path</code> Number of paths (PathRecord)</p>
<dt><code>&#8211;pkey</code> P_Key (PathRecord, MCMemberRecord). If non-numeric value (like &#8216;x&#8217;)</p>
<dd>is specified then saquery will prompt for a value </p>
<p> <code>&#8211;qos_class</code> QoS Class (PathRecord) </p>
<p> <code>&#8211;sl</code> Service level (PathRecord, MCMemberRecord) </p>
<p> <code>&#8211;mtu</code> MTU and selector (PathRecord, MCMemberRecord) </p>
<p> <code>&#8211;rate</code> Rate and selector (PathRecord, MCMemberRecord) </p>
<p> <code>&#8211;pkt_lifetime</code> Packet lifetime and selector (PathRecord, MCMemberRecord)</p>
<dt><code>&#8211;qkey</code> Q_Key (MCMemberRecord). If non-numeric value (like &#8216;x&#8217;) is specified</p>
<dd>then saquery will prompt for a value </p>
<p> <code>&#8211;tclass</code> Traffic Class (PathRecord, MCMemberRecord) </p>
<p> <code>&#8211;flow_label</code> Flow Label (PathRecord, MCMemberRecord) </p>
<p> <code>&#8211;hop_limit</code> Hop limit (PathRecord, MCMemberRecord) </p>
<p> <code>&#8211;scope</code> Scope (MCMemberRecord) </p>
<p> <code>&#8211;join_state</code> Join state (MCMemberRecord) </p>
<p> <code>&#8211;proxy_join</code> Proxy join (MCMemberRecord) </p>
<p> <code>&#8211;service_id</code> ServiceID (PathRecord) </p>
<p> Supported query names (and aliases): </p>
<pre>ClassPortInfo (CPI)
NodeRecord (NR) [lid]
PortInfoRecord (PIR) [[lid]/[port]/[options]]
SL2VLTableRecord (SL2VL) [[lid]/[in_port]/[out_port]]
PKeyTableRecord (PKTR) [[lid]/[port]/[block]]
VLArbitrationTableRecord (VLAR) [[lid]/[port]/[block]]
InformInfoRecord (IIR)
LinkRecord (LR) [[from_lid]/[from_port]] [[to_lid]/[to_port]]
ServiceRecord (SR)
PathRecord (PR)
MCMemberRecord (MCMR)
LFTRecord (LFTR) [[lid]/[block]]
MFTRecord (MFTR) [[mlid]/[position]/[block]]
GUIDInfoRecord (GIR) [[lid]/[block]]
SwitchInfoRecord (SWIR) [lid]
SMInfoRecord (SMIR) [lid]</pre>
</dl>
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
<h3>Dependencies</h3>
<p>OpenSM (or other running SM/SA), libosmcomp, libibumad, libibmad</p>
<h3>Authors</h3>
<dl>
<dt><code>Ira Weiny</code></p>
<dd>&lt; <i>ira.weiny [at] intel.com</i> &gt;</p>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>halr [at] mellanox.com</i> &gt; </p>
</dl>
