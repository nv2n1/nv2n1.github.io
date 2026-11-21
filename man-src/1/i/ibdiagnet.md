---
title: "ibdiagnet(1)"
name: "ibdiagnet"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibdiagnet/"
description: "ibdiagnet – IB diagnostic net"
---

<h2 class="name">NAME</h2>
<p> ibdiagnet &#8211; IB diagnostic net </p>
<h2>SYNOPSYS</h2>
<p> ibdiagnet [-c &lt;count&gt;] [-v] [-r] [-vlr] [-u] [-o &lt;out-dir&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[-t&nbsp;<wbr>&lt;topo-file&gt;]&nbsp;<wbr>[-s&nbsp;<wbr>&lt;sys-name&gt;]&nbsp;<wbr>[-i&nbsp;<wbr>&lt;dev-index&gt;]&nbsp;<wbr>[-p&nbsp;<wbr>&lt;port-num&gt;]&nbsp;<wbr>[-wt]<br />
&nbsp;<wbr>&nbsp;<wbr>[-pm]&nbsp;<wbr>[-pc]&nbsp;<wbr>[-P&nbsp;<wbr>&lt;&lt;<font SIZE="-1">PM</font>&gt;=&lt;Value&gt;&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[-lw&nbsp;<wbr>&lt;1x|4x|12x&gt;]&nbsp;<wbr>[-ls&nbsp;<wbr>&lt;2.5|5|10&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[-skip&nbsp;<wbr>&lt;ibdiag_check/s&gt;]&nbsp;<wbr>[-load_db&nbsp;<wbr>&lt;db_file&gt;]</p>
<h2>DESCRIPTION</h2>
<p> ibdiagnet scans the fabric using directed route packets and extracts all the available information regarding its connectivity and devices. It then produces the following files in the output directory (which defined by the -o option (see below)).</p>
<h2>FILES</h2>
<dl>
<dt><i>ibdiagnet.log</i> &#8211;</dt>
<dd> A dump of all the application reports generate according to the provided flags</dd>
<dt><i>ibdiagnet.lst</i> &#8211;</dt>
<dd> List of all the nodes, ports and links in the fabric</dd>
<dt><i>ibdiagnet.fdbs</i> &#8211;</dt>
<dd> A dump of the unicast forwarding tables of the fabric switches</dd>
<dt><i>ibdiagnet.mcfdbs</i> &#8211;</dt>
<dd> A dump of the multicast forwarding tables of the fabric switches</dd>
<dt><i>ibdiagnet.masks</i> &#8211;</dt>
<dd> In case of duplicate port/node Guids, these file include the map between masked Guid and real Guids</dd>
<dt><i>ibdiagnet.sm</i> &#8211;</dt>
<dd> List of all the <font SIZE="-1">SM </font>(state and priority) in the fabric</dd>
<dt><i>ibdiagnet.pm</i> &#8211;</dt>
<dd> A dump of the pm Counters values, of the fabric links</dd>
<dt><i>ibdiagnet.pkey</i> &#8211;</dt>
<dd> A dump of the the existing partitions and their member host ports</dd>
<dt><i>ibdiagnet.mcgs</i> &#8211;</dt>
<dd> A dump of the multicast groups, their properties and member host ports</dd>
<dt><i>ibdiagnet.psl</i> &#8211;</dt>
<dd> A dump of the path record <font SIZE="-1">SL</font> of each possible source node guid and <font SIZE="-1">DLID</font> pairs. Created only if -vlr option is provided</dd>
<dt><i>ibdiagnet.slvl</i> &#8211;</dt>
<dd> A dump of the <font SIZE="-1">SL2VL</font> Tables from all the switches. Created only if -vlr option is provided</dd>
<dt><i>ibdiagnet.db</i> &#8211;</dt>
<dd> A dump of the internal subnet database. This file can be loaded in later runs using the -load_db option</dd></dl>
<p> In addition to generating the files above, the discovery phase also checks for duplicate node/port GUIDs in the <font SIZE="-1">IB</font> fabric. If such an error is detected, it is displayed on the standard output. After the discovery phase is completed, directed route packets are sent multiple times (according to the -c option) to detect possible problematic paths on which packets may be lost. Such paths are explored, and a report of the suspected bad links is displayed on the standard output. </p>
<p> After scanning the fabric, if the -r option is provided, a full report of the fabric qualities is displayed. This report includes:</p>
<dl>
<dt>&bull;</dt>
<dd> <font SIZE="-1"><code>SM</code></font><code> report</code></dd>
<dt>&bull;</dt>
<dd> <code>Number of nodes and systems</code></dd>
<dt>&bull;</dt>
<dd> <code>Hop-count information</code></dd>
<dl>
<dl>
<dt> maximal hop-count, an example path, and a hop-count histogram</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt>&bull;</dt>
<dd> <code>All CA-to-CA paths traced</code></dd>
<dt>&bull;</dt>
<dd> <code>Credit loop report</code></dd>
<dt>&bull;</dt>
<dd> <code>mgid-mlid-HCAs multicast group and report</code></dd>
<dt>&bull;</dt>
<dd> <code>Partitions report</code></dd>
<dt>&bull;</dt>
<dd> <code>IPoIB report</code></dd></dl>
<p> Note: In case the <font SIZE="-1">IB</font> fabric includes only one <font SIZE="-1">CA,</font> then CA-to-CA paths are not reported. Furthermore, if a topology file is provided, ibdiagnet uses the names defined in it for the output reports.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c &lt;count</code>&gt; :</dt>
<dd>
</dd><dl>
<dl>
<dt> Min number of packets to be sent across each link (default = 10)</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-v</code> :</dt>
<dd>
</dd><dl>
<dl>
<dt> Enable verbose mode</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-r</code> :</dt>
<dd>
</dd><dl>
<dl>
<dt> Provides a report of the fabric qualities</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-u</code> :</dt>
<dd>
</dd><dl>
<dl>
<dt> Credit loop check based on UpDown rules</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-t &lt;topo-file</code>&gt; :</dt>
<dd>
</dd><dl>
<dl>
<dt> Specifies the topology file name</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-s &lt;sys-name</code>&gt; :</dt>
<dd>
</dd><dl>
<dl>
<dt> Specifies the local system name. Meaningful only if a topology file is specified</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-i &lt;dev-index</code>&gt; :</dt>
<dd>
</dd><dl>
<dl>
<dt> Specifies the index of the device of the port used to connect to the <font SIZE="-1">IB</font> fabric (in case of multiple devices on the local system)</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-p &lt;port-num</code>&gt; :</dt>
<dd>
</dd><dl>
<dl>
<dt> Specifies the local device&#8217;s port num used to connect to the <font SIZE="-1">IB</font> fabric</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-o &lt;out-dir</code>&gt; :</dt>
<dd>
</dd><dl>
<dl>
<dt> Specifies the directory where the output files will be placed (default = /var/cache/ibutils)</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-lw &lt;1x|4x|12x</code>&gt; :</dt>
<dd>
</dd><dl>
<dl>
<dt> Specifies the expected link width</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-ls &lt;2.5|5|10</code>&gt; :</dt>
<dd>
</dd><dl>
<dl>
<dt> Specifies the expected link speed</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-pm</code> :</dt>
<dd>
</dd><dl>
<dl>
<dt> Dump all the fabric links, pm Counters into ibdiagnet.pm</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-pc</code> :</dt>
<dd>
</dd><dl>
<dl>
<dt> Reset all the fabric links pmCounters</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-P</code> &lt;PM=&lt;Trash&gt;&gt; :</dt>
<dd>
</dd><dl>
<dl>
<dt> If any of the provided pm is greater then its provided value, print it to screen</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-skip &lt;skip-option(s)</code>&gt; :</dt>
<dd>
</dd><dl>
<dl>
<dt> Skip the executions of the selected checks. Skip options (one or more can be specified) : dup_guids zero_guids pm logical_state part ipoib all</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-wt</code> &lt;file-name&gt;&gt; :</dt>
<dd>
</dd><dl>
<dl>
<dt> Write out the discovered topology into the given file. This flag is useful if you later want to check for changes from the current state of the fabric. A directory named ibdiag_ibnl is also created by this option, and holds the <font SIZE="-1">IBNL</font> files required to load this topology. To use these files you will need to set the environment variable named <font SIZE="-1">IBDM_IBNL_PATH</font> to that directory. The directory is located in /var/cache/ibutils or in the output directory provided by the -o flag.</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-load_db</code> &lt;file-name&gt;&gt; :</dt>
<dd>
</dd><dl>
<dl>
<dt> Load subnet data from the given .db file, and skip subnet discovery stage. Note: Some of the checks require actual subnet discovery, and therefore would not run when load_db is specified. These checks are : Duplicated/zero guids, link state, SMs status.</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-vlr</code> :</dt>
<dd>
</dd><dl>
<dl>
<dt> <font SIZE="-1">VL</font> based Routing &#8211; provide this option to create the paths <font SIZE="-1">SL</font> file (psl), <font SIZE="-1">SL2VL</font> file (slvl) and use them in credit loops check (if -r option is provided).</dt>
<dd> <font SIZE="-1">NOTE:</font> Since number of paths is N^2 extracting the <font SIZE="-1">PSL</font> file may take some time.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-h|&#8211;help</code> :</dt>
<dd>
</dd><dl>
<dl>
<dt> Prints the help page information</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>-V|&#8211;version</code> :</dt>
<dd>
</dd><dl>
<dl>
<dt> Prints the version of the tool</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
<dt><code>&#8211;vars</code> :</dt>
<dd>
</dd><dl>
<dl>
<dt> Prints the tool&#8217;s environment variables and their values</dt>
<dd></dd></dl>
</dl>
<dl>
</dl>
</dl>
<h2>ERROR CODES</h2>
<dl>
<dt>1 &#8211; Failed to fully discover the fabric</dt>
<dd>
</dd><dt>2 &#8211; Failed to parse command line options</dt>
<dd>
</dd><dt>3 &#8211; Failed to intract with <font SIZE="-1">IB</font> fabric</dt>
<dd>
</dd><dt>4 &#8211; Failed to use local device or local port</dt>
<dd>
</dd><dt>5 &#8211; Failed to use Topology File</dt>
<dd>
</dd><dt>6 &#8211; Failed to load requierd Package</dt>
<dd>
</dd></dl>
