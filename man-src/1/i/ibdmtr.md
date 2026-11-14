---
title: "ibdmtr(1)"
name: "ibdmtr"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibdmtr/"
description: "ibdmtr – Fabric Trace Route"
---

<h2>NAME</h2>
<p> <code>ibdmtr</code> &#8211; Fabric Trace Route</p>
<h2>SYNOPSYS</h2>
<p> ibdmtr [-v][-h] {-c &lt;cbaling file&gt;|-t &lt;topo file&gt;} -s &lt;sm node name&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-p&nbsp;<wbr>&lt;sm port num&gt;&nbsp;<wbr>-d&nbsp;<wbr>&lt;comma-sep-dr-path&gt;</p>
<h2>DESCRIPTION</h2>
<p> This utility parses a cabling list or topology file describing the systems connections that make a fabric. Then it start following the direct route provided and print out the systems and nodes on the route.</p>
<h2>ARGUMENTS Required arguments description.</h2>
<dl>
<dt>-t|&#8211;topology &lt;file&gt;</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>Topology file describing the network. See man ibdm-topology-file.</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>-c|&#8211;cables &lt;file&gt;</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>Cabling list file. Following the line format:</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> &lt;Sys1Type&gt; &lt;Sys1Name&gt; &lt;Port1Name&gt; &lt;Sys2Type&gt; &lt;Sys2Name&gt; &lt;Port2Name&gt;</dl>
<dt>-s|&#8211;sm-node &lt;name&gt;</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>The name of the <font SIZE="-1">SM</font> node (not system). E.g. <font SIZE="-1">OSM/U1</font>.</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>-p|&#8211;port-num &lt;num&gt;</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>The number of the <font SIZE="-1">SM</font> node port the <font SIZE="-1">SM</font> is attached to</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>-d|&#8211;dr-path &lt;comm-sep-dr-path&gt;</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>A list of ports to go out through</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-v|&#8211;verbose</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>verbsoe mode</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>-h|&#8211;help</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>provide this help message</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>AUTHOR</h2>
<p> Eitan Zahavi, Mellanox Technologies <font SIZE="-1">LTD</font>, eitan [at] mellanox.co.il </p>
<h2>Index</h2>
