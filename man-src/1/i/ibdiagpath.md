---
title: "ibdiagpath(1)"
name: "ibdiagpath"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibdiagpath/"
description: "ibdiagpath – IB diagnostic path"
---

<h2 class="name">NAME</h2>
<p> ibdiagpath &#8211; IB diagnostic path </p>
<h2>SYNOPSYS</h2>
<p> ibdiagpath<br />
&nbsp;<wbr>&nbsp;<wbr>{-n&nbsp;<wbr>&lt;[src-name,]dst-name&gt;|-l&nbsp;<wbr>&lt;[src-lid,]dst-lid&gt;|-d&nbsp;<wbr>&lt;p1,p2,p3,&#8230;&gt;}<br />
&nbsp;<wbr>&nbsp;<wbr>[-c&nbsp;<wbr>&lt;count&gt;]&nbsp;<wbr>[-v]&nbsp;<wbr>[-t&nbsp;<wbr>&lt;topo-file&gt;]&nbsp;<wbr>[-s&nbsp;<wbr>&lt;sys-name&gt;]&nbsp;<wbr>[-i&nbsp;<wbr>&lt;dev-index&gt;]<br />
&nbsp;<wbr>&nbsp;<wbr>[-p&nbsp;<wbr>&lt;port-num&gt;]&nbsp;<wbr>[-o&nbsp;<wbr>&lt;out-dir&gt;]&nbsp;<wbr>[-lw&nbsp;<wbr>&lt;1x|4x|12x&gt;]&nbsp;<wbr>[-ls&nbsp;<wbr>&lt;2.5|5|10&gt;]&nbsp;<wbr>[-pm]<br />
&nbsp;<wbr>&nbsp;<wbr>[-pc]&nbsp;<wbr>[-P&nbsp;<wbr>&lt;&lt;<font SIZE="-1">PM</font>&nbsp;<wbr>counter&gt;=&lt;Trash Limit&gt;&gt;]</p>
<h2>DESCRIPTION</h2>
<p> ibdiagpath traces a path between two end-points and provides information regarding the nodes and ports traversed along the path. It utilizes device specific health queries for the different devices along the traversed path. The way ibdiagpath operates depends on the addressing mode used on the command line. If directed route adressing is used, the local node is the source node and the route to the destination port is known apriori. On the other hand, if <font SIZE="-1">LID</font> route (or by-name) addressing is imployed, then the source and destination ports of a route are specified by their LIDs (or by the names defined in the topology file). In this case, the actual path from the local port to the source port, and from the source port to the destination port, is defined by means of Subnet Management Linear Forwarding Table queries of the switch nodes along those paths. Therefore, the path cannot be predicted as it may change. The tool allows omitting the source node, in which case the local port on the machine running the tool is assumed to be the source. Note: When ibdiagpath queries for the performance counters along the path between the source and destination ports, it always traverses the <font SIZE="-1">LID</font> route, even if a directed route is specified. If along the <font SIZE="-1">LID</font> route one or more links are not in the <font SIZE="-1">ACTIVE</font> state, ibdiagpath reports an error. Checks for path validity from partitions, IPoIB and QoS perspectives are also provided.</p>
<dl>
<dt><i>ibdiagpath.log</i> &#8211;</p>
<dd> A dump of all the application reports generate according to the provided flags</p>
<dt><i>ibdiagnet.pm</i> &#8211;</p>
<dd> A dump of the pm Counters values, of the fabric links</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n &lt;[src-name,]dst-name</code>&gt; :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Names of the source and destination ports (as defined in the topology file; source may be omitted -&gt; local port is assumed to be the source)</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-l &lt;[src-lid,]dst-lid</code>&gt; :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Source and destination LIDs (source may be omitted -&gt; local port is assumed to be the source)</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-d &lt;p1,p2,p3,&#8230;</code>&gt; :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> directed route from the local node (which is the source) and the destination node</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-c &lt;count</code>&gt; :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> The minimal number of packets to be sent across each link (default = 100)</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-v</code> :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Enable verbose mode</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-t &lt;topo-file</code>&gt; :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Specifies the topology file name</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-s &lt;sys-name</code>&gt; :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Specifies the local system name. Meaningful only if a topology file is specified</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-i &lt;dev-index</code>&gt; :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Specifies the index of the device of the port used to connect to the <font SIZE="-1">IB</font> fabric (in case of multiple devices on the local system)</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-p &lt;port-num</code>&gt; :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Specifies the local device&#8217;s port number used to connect to the <font SIZE="-1">IB</font> fabric</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-o &lt;out-dir</code>&gt; :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Specifies the directory where the output files will be placed (default = /var/cache/ibutils)</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-lw &lt;1x|4x|12x</code>&gt; :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Specifies the expected link width</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-ls &lt;2.5|5|10</code>&gt; :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Specifies the expected link speed</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-pm</code> :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Dump all the fabric links, pm Counters into ibdiagnet.pm</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-pc</code> :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Reset all the fabric links pmCounters</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-P</code> &lt;PM=&lt;Trash&gt;&gt; :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> If any of the provided pm is greater then its provided value, print it to screen</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-h|&#8211;help</code> :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Prints the help page information</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-V|&#8211;version</code> :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Prints the version of the tool</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;vars</code> :</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt> Prints the tool&#8217;s environment variables and their values</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>ERROR CODES</h2>
<dl>
<dt>1 &#8211; The path traced is un-healthy</p>
<dd>
<dt>2 &#8211; Failed to parse command line options</p>
<dd>
<dt>3 &#8211; More then 64 hops are required for traversing the local port to the &quot;Source&quot; port and then to the &quot;Destination&quot; port.</p>
<dd>
<dt>4 &#8211; Unable to traverse the <font SIZE="-1">LFT</font> data from source to destination</p>
<dd>
<dt>5 &#8211; Failed to use Topology File</p>
<dd>
<dt>6 &#8211; Failed to load required Package</p>
<dd>
</dl>
<h2>Index</h2>
