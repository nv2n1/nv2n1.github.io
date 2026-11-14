---
title: "ibdmchk(1)"
name: "ibdmchk"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibdmchk/"
description: "IBDM – Network Checker and Attributes Analyzer"
---

<h2>NAME</h2>
<p> <code>IBDM &#8211; Network Checker and Attributes Analyzer</code></p>
<h2>SYNOPSYS</h2>
<p> ibdmchk has two operation modes: design and verification. </p>
<p> <font SIZE="-1">DESIGN:</font> </p>
<p> ibdmchk [-v][-h][-u][-r &lt;roots file&gt;] -t &lt;topology file&gt; -n &lt;<font SIZE="-1">SM</font> Node&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>-p&nbsp;<wbr>&lt;<font SIZE="-1">SM</font>&nbsp;<wbr>Port&gt;&nbsp;<wbr>[-e]&nbsp;<wbr>[-l&nbsp;<wbr>&lt;lmc&gt;] </p>
<p> <font SIZE="-1">VERIFICATION:</font> </p>
<p> ibdmchk [-v][-h][-r &lt;roots file&gt;] [-s &lt;subnet file&gt;] [-f &lt;fdb file&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[-m&nbsp;<wbr>&lt;mcfdbs file&gt;&nbsp;<wbr>[-l&nbsp;<wbr>&lt;lmc&gt;]&nbsp;<wbr>[-u]&nbsp;<wbr>[-M]&nbsp;<wbr>[-a]<br />
&nbsp;<wbr>&nbsp;<wbr>[-c&nbsp;<wbr>&lt;path sl file&gt;]&nbsp;<wbr>[-d&nbsp;<wbr>&lt;sl2vl tables file&gt;]</p>
<h2>DESIGN MODE DESCRIPTION</h2>
<p> The Design mode is intended to be used before the cluster is built. It provides basic checks of the specified network as described by a topology file. After simulating the <font SIZE="-1">SM</font> <font SIZE="-1">LID</font> assignment and routing algorithms it provides reports of the (H)CA to (H)CA paths depth histogram and credit deadlock potential in the resulting routing scheme.</p>
<h2>ARGUMENTS:</h2>
<dl>
<dt>-t|&#8211;topo &lt;topo file&gt;</p>
<dd> The <code>topology file</code> specifying the network. See man <code>ibdm-topology-file</code></p>
<dt>-n|&#8211;node &lt;<font SIZE="-1">SM</font> Node&gt;</p>
<dd> The name of the Subnet Manager node (syntax: &lt;Topo-File-System&gt;/U1)</p>
<dt>-p|&#8211;port &lt;<font SIZE="-1">SM</font> Port&gt;</p>
<dd> The port number by which the <font SIZE="-1">SM</font> nodes is attached to the fabric.</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-v|&#8211;verbose</p>
<dd> Verbsoe mode</p>
<dt>-h|&#8211;help</p>
<dd> Provides this help message</p>
<dt>-l|&#8211;lmc &lt;lmc&gt;</p>
<dd> <font SIZE="-1">LMC</font> value &gt; 0 means assigning 2^lmc lids to each port.</p>
<dt>-e|&#8211;enh</p>
<dd> Use enhanced routing algorithm when <font SIZE="-1">LMC</font> &gt; 0 and report the resulting paths correlation (using same system/node) histogram</p>
<dt>-r|&#8211;roots &lt;roots file&gt; A file with all the roots node names (one on each line).</p>
<dd></dl>
<h2>VERIFICATION MODE DESCRIPTION</h2>
<p> After the cluster is built and OpenSM is run (using flag -D 0x43) it reports the subnet and <font SIZE="-1">FDB</font> tables into the files osm-subnet.lst, osm.fdbs and osm.fdbs in /var/log/ (or subnet.lst, osm.fdbs and osm.mcfdbs into /var/cache/ibutils in older OpenSM versions). ibdiagnet is also producing the same files in its output directory. Based on these files the utility checks all <font SIZE="-1">CA</font> to <font SIZE="-1">CA</font> connectivity. Further analysis for credit deadlock potential is performed and reported. In case of an <font SIZE="-1">LMC</font> &gt; 0 it reports histograms for how many systems and nodes are common between the different paths for the same port pairs.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-l|&#8211;lmc &lt;lmc&gt;</p>
<dd> The <font SIZE="-1">LMC</font> value used while running OpenSM. Mandatory if not the default 0.</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-v|&#8211;verbose</p>
<dd> Verbsoe mode</p>
<dt>-h|&#8211;help</p>
<dd> Provides this help message</p>
<dt>-s|&#8211;subnet &lt;file&gt;</p>
<dd> OpenSM subnet.lst file (default is /var/log/osm-subnet.lst or /var/cache/ibutils/subnet.lst)</p>
<dt>-f|&#8211;fdb &lt;file&gt;</p>
<dd> OpenSM dump of Ucast <font SIZE="-1">LFDB</font>. Use -D 0x41 to generate it (default is /var/log/osm.fdbs or /var/cache/ibutils/osm.fdbs).</p>
<dt>-m|&#8211;mcfdb &lt;file&gt;</p>
<dd> OpenSM dump of Multicast <font SIZE="-1">LFDB</font>. Use -D 0x41 to generate it (default is /var/log/osm.mcfdbs or /var/cache/ibutils/osm.mcfdbs).</p>
<dt>-c|&#8211;psl &lt;file&gt;</p>
<dd> Source Guid to <font SIZE="-1">DLID</font> -&gt; Path <font SIZE="-1">SL</font> mapping. Each line holds: src_node_guid dlid sl. Used by the credit loop check to accuartly model <font SIZE="-1">SL/VL</font> based routing.</p>
<dt>-d|&#8211;slvl &lt;file&gt;</p>
<dd> <font SIZE="-1">SL2VL</font> mapping of all switces. Each line holds: swguid iport oport 0x(sl0)(sl1) 0x(sl2)(sl3)&#8230; Used by the credit loop check to accuartly model <font SIZE="-1">SL/VL</font> based routing.</p>
<dt>-r|&#8211;roots &lt;roots file&gt;</p>
<dd> A file holding all root nodes guids (one per line).</p>
<dt>-u|&#8211;updn</p>
<dd> Use Up/Down based credit loop check algorithm instead of the generic one.</p>
<dt>-M|&#8211;MFT</p>
<dd> Include multicast routing in credit loops analysis.</p>
<dt>-a|&#8211;all</p>
<dd> Verify not only CA-CA paths but also <font SIZE="-1">SW-SW</font>, CA-SW and <font SIZE="-1">SW-CA</font>. Both check for <font SIZE="-1">FDB</font> path connectivity and also for credit loops.</dl>
<h2>AUTHOR</h2>
<p> Eitan Zahavi, Mellanox Technologies <font SIZE="-1">LTD</font>, eitan [at] mellanox.co.il </p>
<h2>Index</h2>
