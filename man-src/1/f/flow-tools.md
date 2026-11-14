---
title: "flow-tools(1)"
name: "flow-tools"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-tools/"
description: "flow-tools – Tool set for working with NetFlow data."
---

<h2>NAME</h2>
<p> flow-tools &#8211; Tool set for working with NetFlow data.</p>
<h2>DESCRIPTION</h2>
<p> Flow-tools is library and a collection of programs used to collect, send, process, and generate reports from NetFlow data. The tools can be used together on a single server or distributed to multiple servers for large deployments. The flow-toools library provides an API for development of custom applications for NetFlow export versions 1,5,6 and the 14 currently defined version 8 subversions. A Perl and Python interface have been contributed and are included in the distribution. </p>
<p> Flow data is collected and stored by default in host byte order, yet the files are portable across big and little endian architectures. </p>
<p> Commands that utilize the network use a localip/remoteip/port designation for communication. &quot;localip&quot; is the IP address the host will use as a source for sending or bind to when receiving NetFlow PDU&#8217;s (ie the destination address of the exporter. Configuring the &quot;localip&quot; to 0 will force the kernel to decide what IP address to use for sending and listen on all IP addresses for receiving. &quot;remoteip&quot; is the destination IP address used for sending or the expected address of the source when receiving. If the &quot;remoteip&quot; is 0 then the application will accept flows from any source address. The &quot;port&quot; is the UDP port number used for sending or receiving. When using multicast addresses the localip/remoteip/port is used to represent the source, group, and port respectively. </p>
<p> Flows are exported from a router in a number of different configurable versions. A flow is a collection of key fields and additional data. The flow key is {srcaddr, dstaddr, input, output, srcport, dstport, prot, ToS}. Flow-tools supports one export version per file. </p>
<p> Export versions 1, 5, 6, and 7 all maintain {nexthop, dPkts, dOctets, First, Last, flags}, ie the next-hop IP address, number of packets, number of octets (bytes), start time, end time, and flags such as the TCP header bits. Version 5 adds the additional fields {src_as, dst_as, src_mask, dst_mask}, ie source AS, destination AS, source network mask, and destination network mask. Version 7 which is specific to the Catalyst switches adds in addition to the version 5 fields {router_sc}, which is the Router IP address which populates the flow cache shortcut in the Supervisor. Version 6 which is not officially supported by Cisco adds in addition to the version 5 fields {in_encaps, out_encaps, peer_nexthop}, ie the input and output interface encapsulation size, and the IP address of the next hop within the peer. Version 1 exports do not contain a sequence number and therefore should be avoided, although it is safe to store the data as version 1 if the additional fields are not used. </p>
<p> Version 8 IOS NetFlow is a second level flow cache that reduces the data exported from the router. There are currently 11 formats, all of which provide {dFlows, dOctets, dPkts, First, Last} for the key fields. </p>
<pre>
  8.1 -  Source and Destination AS, Input and Output interface
  8.2 -  Protocol and Port
  8.3 -  Source Prefix and Input interface
  8.4 -  Destination Prefix and Output interface
  8.5 -  Source/Destination Prefix and Input/Output interface
  8.9 -  8.1 + ToS
  8.10 - 8.2 + ToS
  8.11 - 8.3 + ToS
  8.12 - 8.5 + ToS
  8.13 - 8.2 + ToS
  8.14 - 8.3 + ports + ToS
</pre>
<p> Version 8 CatIOS NetFlow appears to be a less fine grained first level flow cache. </p>
<pre>
  8.6 - Destination IP, ToS, Marked ToS, 
  8.7 - Source/Destination IP, Input/Output interface, ToS, Marked ToS, 
  8.8 - Source/Destination IP, Source/Destination Port,
        Input/Output interface, ToS, Marked ToS, 
</pre>
<p> The following programs are included in the flow-tools distribution. </p>
<p> <code>flow-capture</code> &#8211; Collect, compress, store, and manage disk space for exported flows from a router. </p>
<p> <code>flow-cat</code> &#8211; Concatenate flow files. Typically flow files will contain a small window of 5 or 15 minutes of exports. Flow-cat can be used to append files for generating reports that span longer time periods. </p>
<p> <code>flow-fanout</code> &#8211; Replicate NetFlow datagrams to unicast or multicast destinations. Flow-fanout is used to facilitate multiple collectors attached to a single router. </p>
<p> <code>flow-report</code> &#8211; Generate reports for NetFlow data sets. Reports include source/destination IP pairs, source/destination AS, and top talkers. Over 50 reports are currently supported. </p>
<p> <code>flow-tag</code> &#8211; Tag flows based on IP address or AS #. Flow-tag is used to group flows by customer network. The tags can later be used with flow-fanout or flow-report to generate customer based traffic reports. </p>
<p> <code>flow-filter</code> &#8211; Filter flows based on any of the export fields. Flow-filter is used in-line with other programs to generate reports based on flows matching filter expressions. </p>
<p> <code>flow-import</code> &#8211; Import data from ASCII or cflowd format. </p>
<p> <code>flow-export</code> &#8211; Export data to ASCII or cflowd format. </p>
<p> <code>flow-send</code> &#8211; Send data over the network using the NetFlow protocol. </p>
<p> <code>flow-receive</code> &#8211; Receive exports using the NetFlow protocol without storing to disk like flow-capture. </p>
<p> <code>flow-gen</code> &#8211; Generate test data. </p>
<p> <code>flow-dscan</code> &#8211; Simple tool for detecting some types of network scanning and Denial of Service attacks. </p>
<p> <code>flow-merge</code> &#8211; Merge flow files in chronoligical order. </p>
<p> <code>flow-xlate</code> &#8211; Perform translations on some flow fields. </p>
<p> <code>flow-expire</code> &#8211; Expire flows using the same policy of flow-capture. </p>
<p> <code>flow-header</code> &#8211; Display meta information in flow file. </p>
<p> <code>flow-split</code> &#8211; Split flow files into smaller files based on size, time, or tags.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt; </p>
<p> <code>flow-merge</code> by Larry Lidz &lt;ellidz [at] eridu.uchicago.edu&gt; </p>
<p> Patches and other contribitions by a list too long to mention here. </p>
<p> <code>flow-tools</code> is avalable at<br />
&nbsp;<wbr>&lt;URL:<a rel="nofollow" href="http://www.splintered.net/sw/flow-tools">http://www.splintered.net/sw/flow-tools</a>&gt;. </p>
<p> A mailing list is maintained at &lt;flow-tools [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-capture/">flow-capture</a></code>(1) <code><a href="/docs/linux/man/1-flow-cat/">flow-cat</a></code>(1) <code><a href="/docs/linux/man/1-flow-dscan/">flow-dscan</a></code>(1) <code><a href="/docs/linux/man/1-flow-expire/">flow-expire</a></code>(1) <code><a href="/docs/linux/man/1-flow-export/">flow-export</a></code>(1) <code><a href="/docs/linux/man/1-flow-fanout/">flow-fanout</a></code>(1) <code><a href="/docs/linux/man/1-flow-filter/">flow-filter</a></code>(1) <code><a href="/docs/linux/man/1-flow-nfilter/">flow-nfilter</a></code>(1) <code><a href="/docs/linux/man/1-flow-gen/">flow-gen</a></code>(1) <code><a href="/docs/linux/man/1-flow-header/">flow-header</a></code>(1) <code><a href="/docs/linux/man/1-flow-import/">flow-import</a></code>(1) <code><a href="/docs/linux/man/1-flow-merge/">flow-merge</a></code>(1) <code><a href="/docs/linux/man/1-flow-print/">flow-print</a></code>(1) <code><a href="/docs/linux/man/1-flow-receive/">flow-receive</a></code>(1) <code><a href="/docs/linux/man/1-flow-report/">flow-report</a></code>(1) <code><a href="/docs/linux/man/1-flow-send/">flow-send</a></code>(1) <code><a href="/docs/linux/man/1-flow-split/">flow-split</a></code>(1) <code><a href="/docs/linux/man/1-flow-stat/">flow-stat</a></code>(1) <code><a href="/docs/linux/man/1-flow-tag/">flow-tag</a></code>(1) <code><a href="/docs/linux/man/1-flow-xlate/">flow-xlate</a></code>(1) </p>
<h2>Index</h2>
