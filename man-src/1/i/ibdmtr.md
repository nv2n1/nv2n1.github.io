---

title: "ibdmtr(1)"
name: "ibdmtr"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibdmtr/"
description: "ibdmtr – Fabric Trace Route"
---

<p> <code>ibdmtr</code> &#8211; Fabric Trace Route</p>
<h2>SYNOPSYS</h2>
<p> ibdmtr [-v][-h] {-c &lt;cbaling file&gt;|-t &lt;topo file&gt;} -s &lt;sm node name&gt;<br/>
&nbsp;<wbr>&nbsp;<wbr>-p&nbsp;<wbr>&lt;sm port num&gt;&nbsp;<wbr>-d&nbsp;<wbr>&lt;comma-sep-dr-path&gt;</p>
<h2>DESCRIPTION</h2>
<p> This utility parses a cabling list or topology file describing the systems connections that make a fabric. Then it start following the direct route provided and print out the systems and nodes on the route.</p>
<h2>ARGUMENTS Required arguments description.</h2>
<dl>
<dt>-t|&#8211;topology &lt;file&gt;</dt>
<dd>
</dd><dl>
<dl>
<dt>Topology file describing the network. See man ibdm-topology-file.</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt>-c|&#8211;cables &lt;file&gt;</dt>
<dd>
</dd><dl>
<dl>
<dt>Cabling list file. Following the line format:</dt>
<dd></dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> &lt;Sys1Type&gt; &lt;Sys1Name&gt; &lt;Port1Name&gt; &lt;Sys2Type&gt; &lt;Sys2Name&gt; &lt;Port2Name&gt;</dd></dl>
<dt>-s|&#8211;sm-node &lt;name&gt;</dt>
<dd>
</dd><dl>
<dl>
<dt>The name of the SM node (not system). E.g. OSM/U1.</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt>-p|&#8211;port-num &lt;num&gt;</dt>
<dd>
</dd><dl>
<dl>
<dt>The number of the SM node port the SM is attached to</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt>-d|&#8211;dr-path &lt;comm-sep-dr-path&gt;</dt>
<dd>
</dd><dl>
<dl>
<dt>A list of ports to go out through</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-v|&#8211;verbose</dt>
<dd>
</dd><dl>
<dl>
<dt>verbsoe mode</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt>-h|&#8211;help</dt>
<dd>
</dd><dl>
<dl>
<dt>provide this help message</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
</dl>
<h2>AUTHOR</h2>
<p> Eitan Zahavi, Mellanox Technologies LTD, eitan [at] mellanox.co.il </p>
