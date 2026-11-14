---
title: "ibtracert(8)"
name: "ibtracert"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibtracert/"
description: "IBTRACERT –"
---

<p>IBTRACERT &#8211;</p>
<h2>Trace Infiniband Path</h2>
<h3>Synopsis</h3>
<p>ibtracert [options] [&lt;lid|guid&gt; [&lt;startlid&gt; [&lt;endlid&gt;]]]</p>
<h3>Description</h3>
<p>ibtracert uses SMPs to trace the path from a source GID/LID to a destination GID/LID. Each hop along the path is displayed until the destination is reached or a hop does not respond. By using the -m option, multicast path tracing can be performed between source and destination nodes.</p>
<h3>Options</h3>
<dl>
<dt><code>-n, &#8211;no_info</code></p>
<dd>simple format; don&#8217;t show additional information</p>
<dt><code>-m</code></p>
<dd>show the multicast trace of the specified mlid</p>
<dt><code>-f, &#8211;force</code></p>
<dd>force route to destination port</dl>
<h3>Addressing Flags</h3>
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
<p>Unicast examples</p>
<dl>
<dt><code>::</code></p>
<dd>ibtracert 4 16 # show path between lids 4 and 16 ibtracert -n 4 16 # same, but using simple output format ibtracert -G 0x8f1040396522d 0x002c9000100d051 # use guid addresses </p>
<p> Multicast example</p>
<dt><code>::</code></p>
<dd>ibtracert -m 0xc000 4 16 # show multicast path of mlid 0xc000 between lids 4 and 16</dl>
<h3>See Also</h3>
<p>ibroute (8)</p>
<h3>Author</h3>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt;<i>hal.rosenstock [at] gmail.com</i>&gt;</p>
<dt><code>Ira Weiny</code></p>
<dd>&lt; <i>ira.weiny [at] intel.com</i> &gt; </p>
</dl>
