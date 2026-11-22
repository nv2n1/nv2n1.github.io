---

title: "ibdmchk(1)"
name: "ibdmchk"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibdmchk/"
description: "IBDM – Network Checker and Attributes Analyzer"
---

<p> <code>IBDM &#8211; Network Checker and Attributes Analyzer</code></p>
<h2>SYNOPSYS</h2>
<p> ibdmchk has two operation modes: design and verification. </p>
<p> DESIGN: </p>
<p> ibdmchk [-v][-h][-u][-r &lt;roots file&gt;] -t &lt;topology file&gt; -n &lt;SM Node&gt;<br/>
&nbsp;<wbr>&nbsp;<wbr>-p&nbsp;<wbr>&lt;SM&nbsp;<wbr>Port&gt;&nbsp;<wbr>[-e]&nbsp;<wbr>[-l&nbsp;<wbr>&lt;lmc&gt;] </p>
<p> VERIFICATION: </p>
<p> ibdmchk [-v][-h][-r &lt;roots file&gt;] [-s &lt;subnet file&gt;] [-f &lt;fdb file&gt;]<br/>
&nbsp;<wbr>&nbsp;<wbr>[-m&nbsp;<wbr>&lt;mcfdbs file&gt;&nbsp;<wbr>[-l&nbsp;<wbr>&lt;lmc&gt;]&nbsp;<wbr>[-u]&nbsp;<wbr>[-M]&nbsp;<wbr>[-a]<br/>
&nbsp;<wbr>&nbsp;<wbr>[-c&nbsp;<wbr>&lt;path sl file&gt;]&nbsp;<wbr>[-d&nbsp;<wbr>&lt;sl2vl tables file&gt;]</p>
<h2>DESIGN MODE DESCRIPTION</h2>
<p> The Design mode is intended to be used before the cluster is built. It provides basic checks of the specified network as described by a topology file. After simulating the SM LID assignment and routing algorithms it provides reports of the (H)CA to (H)CA paths depth histogram and credit deadlock potential in the resulting routing scheme.</p>
<h2>ARGUMENTS:</h2>
<dl>
<dt>-t|&#8211;topo &lt;topo file&gt;</dt>
<dd> The <code>topology file</code> specifying the network. See man <code>ibdm-topology-file</code></dd>
<dt>-n|&#8211;node &lt;SM Node&gt;</dt>
<dd> The name of the Subnet Manager node (syntax: &lt;Topo-File-System&gt;/U1)</dd>
<dt>-p|&#8211;port &lt;SM Port&gt;</dt>
<dd> The port number by which the SM nodes is attached to the fabric.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt>-v|&#8211;verbose</dt>
<dd> Verbsoe mode</dd>
<dt>-h|&#8211;help</dt>
<dd> Provides this help message</dd>
<dt>-l|&#8211;lmc &lt;lmc&gt;</dt>
<dd> LMC value &gt; 0 means assigning 2^lmc lids to each port.</dd>
<dt>-e|&#8211;enh</dt>
<dd> Use enhanced routing algorithm when LMC &gt; 0 and report the resulting paths correlation (using same system/node) histogram</dd>
<dt>-r|&#8211;roots &lt;roots file&gt; A file with all the roots node names (one on each line).</dt>
<dd></dd></dl>
<h2>VERIFICATION MODE DESCRIPTION</h2>
<p> After the cluster is built and OpenSM is run (using flag -D 0x43) it reports the subnet and FDB tables into the files osm-subnet.lst, osm.fdbs and osm.fdbs in /var/log/ (or subnet.lst, osm.fdbs and osm.mcfdbs into /var/cache/ibutils in older OpenSM versions). ibdiagnet is also producing the same files in its output directory. Based on these files the utility checks all CA to CA connectivity. Further analysis for credit deadlock potential is performed and reported. In case of an LMC &gt; 0 it reports histograms for how many systems and nodes are common between the different paths for the same port pairs.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-l|&#8211;lmc &lt;lmc&gt;</dt>
<dd> The LMC value used while running OpenSM. Mandatory if not the default 0.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt>-v|&#8211;verbose</dt>
<dd> Verbsoe mode</dd>
<dt>-h|&#8211;help</dt>
<dd> Provides this help message</dd>
<dt>-s|&#8211;subnet &lt;file&gt;</dt>
<dd> OpenSM subnet.lst file (default is /var/log/osm-subnet.lst or /var/cache/ibutils/subnet.lst)</dd>
<dt>-f|&#8211;fdb &lt;file&gt;</dt>
<dd> OpenSM dump of Ucast LFDB. Use -D 0x41 to generate it (default is /var/log/osm.fdbs or /var/cache/ibutils/osm.fdbs).</dd>
<dt>-m|&#8211;mcfdb &lt;file&gt;</dt>
<dd> OpenSM dump of Multicast LFDB. Use -D 0x41 to generate it (default is /var/log/osm.mcfdbs or /var/cache/ibutils/osm.mcfdbs).</dd>
<dt>-c|&#8211;psl &lt;file&gt;</dt>
<dd> Source Guid to DLID -&gt; Path SL mapping. Each line holds: src_node_guid dlid sl. Used by the credit loop check to accuartly model SL/VL based routing.</dd>
<dt>-d|&#8211;slvl &lt;file&gt;</dt>
<dd> SL2VL mapping of all switces. Each line holds: swguid iport oport 0x(sl0)(sl1) 0x(sl2)(sl3)&#8230; Used by the credit loop check to accuartly model SL/VL based routing.</dd>
<dt>-r|&#8211;roots &lt;roots file&gt;</dt>
<dd> A file holding all root nodes guids (one per line).</dd>
<dt>-u|&#8211;updn</dt>
<dd> Use Up/Down based credit loop check algorithm instead of the generic one.</dd>
<dt>-M|&#8211;MFT</dt>
<dd> Include multicast routing in credit loops analysis.</dd>
<dt>-a|&#8211;all</dt>
<dd> Verify not only CA-CA paths but also SW-SW, CA-SW and SW-CA. Both check for FDB path connectivity and also for credit loops.</dd></dl>
<h2>AUTHOR</h2>
<p> Eitan Zahavi, Mellanox Technologies LTD, eitan [at] mellanox.co.il </p>
