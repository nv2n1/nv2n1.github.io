---
title: "ibfindnodesusing(8)"
name: "ibfindnodesusing"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibfindnodesusing/"
description: "IBFINDNODESUSING –"
---

<p>IBFINDNODESUSING &#8211;</p>
<h2>Find A List Of End Nodes Which Are Routed Through The Specified Switch And Port</h2>
<h3>Synopsis</h3>
<p>ibfindnodesusing.pl [options] &lt;switch_guid|switch_name&gt; &lt;port&gt;</p>
<h3>Description</h3>
<p>ibfindnodesusing.pl uses ibroute and detects the current nodes which are routed through both directions of the link specified. The link is specified by one switch port end; the script finds the remote end automatically.</p>
<h3>Options</h3>
<dl>
<dt><code>-h</code></p>
<dd>show help</p>
<dt><code>-R</code></p>
<dd>Recalculate the ibnetdiscover information, ie do not use the cached information. This option is slower but should be used if the diag tools have not been used for some time or if there are other reasons to believe that the fabric has changed. </p>
<p> <code>-C &lt;ca_name&gt;</code> use the specified ca_name. </p>
<p> <code>-P &lt;ca_port&gt;</code> use the specified ca_port.</dl>
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
<h3>Author</h3>
<dl>
<dt><code>Ira Weiny</code></p>
<dd>&lt; <i>ira.weiny [at] intel.com</i> &gt; </p>
</dl>
