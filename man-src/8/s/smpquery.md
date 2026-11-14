---
title: "smpquery(8)"
name: "smpquery"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smpquery/"
description: "SMPQUERY –"
---

<p>SMPQUERY &#8211;</p>
<h2>Query Infiniband Subnet Management Attributes</h2>
<h3>Synopsis</h3>
<p>smpquery [options] &lt;op&gt; &lt;dest dr_path|lid|guid&gt; [op params]</p>
<h3>Description</h3>
<p>smpquery allows a basic subset of standard SMP queries including the following: node info, node description, switch info, port info. Fields are displayed in human readable format.</p>
<h3>Options</h3>
<p>Current supported operations (case insensitive) and their parameters: </p>
<pre>Nodeinfo (NI) &lt;addr&gt;
Nodedesc (ND) &lt;addr&gt;
Portinfo (PI) &lt;addr&gt; [&lt;portnum&gt;] # default port is zero
PortInfoExtended (PIE) &lt;addr&gt; [&lt;portnum&gt;]
Switchinfo (SI) &lt;addr&gt;
PKeyTable (PKeys) &lt;addr&gt; [&lt;portnum&gt;]
SL2VLTable (SL2VL) &lt;addr&gt; [&lt;portnum&gt;]
VLArbitration (VLArb) &lt;addr&gt; [&lt;portnum&gt;]
GUIDInfo (GI) &lt;addr&gt;
MlnxExtPortInfo (MEPI) &lt;addr&gt; [&lt;portnum&gt;] # default port is zero</pre>
<dl>
<dt><code>-c, &#8211;combined</code></p>
<dd>Use Combined route address argument <code>&lt;lid&gt; &lt;DR_Path&gt;</code></p>
<dt><code>-x, &#8211;extended</code></p>
<dd>Set SMSupportsExtendedSpeeds bit 31 in AttributeModifier (only impacts PortInfo queries).</p>
<dt><code>-K, &#8211;show_keys</code></p>
<dd>show security keys (mkey, smkey, etc.) associated with the request.</dl>
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
<p><code>-t, &#8211;timeout &lt;timeout_ms&gt;</code> override the default timeout for the solicited mads. </p>
<p> <code>&#8211;node-name-map &lt;node-name-map&gt;</code> Specify a node name map. This file maps GUIDs to more user friendly names. See FILES section.</p>
<dl>
<dt><code>-y, &#8211;m_key &lt;key&gt;</code></p>
<dd>use the specified M_key for requests. If non-numeric value (like &#8216;x&#8217;) is specified then a value will be prompted for. </p>
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
<dl>
<dt><code>::</code></p>
<dd>smpquery portinfo 3 1 # portinfo by lid, with port modifier smpquery -G switchinfo 0x2C9000100D051 1 # switchinfo by guid smpquery -D nodeinfo 0 # nodeinfo by direct route smpquery -c nodeinfo 6 0,12 # nodeinfo by combined route</dl>
<h3>See Also</h3>
<p>smpdump (8)</p>
<h3>Author</h3>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>hal [at] mellanox.com</i> &gt; </p>
</dl>
