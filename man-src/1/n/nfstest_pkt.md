---
title: "nfstest_pkt(1)"
name: "nfstest_pkt"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfstest_pkt/"
description: "nfstest_pkt – Packet trace decoder"
---

<h2>NAME</h2>
<p> nfstest_pkt &#8211; Packet trace decoder</p>
<h2>SYNOPSIS</h2>
<p> nfstest_pkt [options] &lt;trace1.cap&gt; [&lt;trace2.cap&gt; &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Decode and display all packets in the packet trace file(s) given. The match option gives the ability to search for specific packets within the packet trace file. Other options allow displaying of their corresponding call or reply when only one or the other is matched. Only a range of packets can be displayed if the start and/or end options are used. </p>
<p> There are three levels of verbosity in which they are specified using a bitmap, where the most significant bit gives a more verbose output. Verbose level 1 is used as a default where each packet is displayed condensed to one line using the last layer of the packet as the main output. By default only the NFS packets (NFS, MOUNT, NLM, etc.) are displayed. </p>
<p> The packet trace files are processed either serially or in parallel. The packets are displayed using their timestamps so they are always displayed in the correct order even if the files given are out of order. If the packet traces were captured one after the other the packets are displayed serially, first the packets of the first file according to their timestamps, then the second and so forth. If the packet traces were captured at the same time on multiple clients the packets are displayed in parallel, packets are interleaved from all the files when displayed again according to their timestamps. </p>
<p> Note: When using the &#8211;call option, a packet call can be displayed out of order if the call is not matched explicitly but its reply is matched so its corresponding call is displayed right before the reply. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;version</p>
<dd> show program&#8217;s version number and exit</p>
<dt>-h, &#8211;help</p>
<dd> show this help message and exit</p>
<dt>-v VERBOSE, &#8211;verbose=VERBOSE</p>
<dd> Verbose level bitmask [default: 1]. bitmap 0x01: one line per packet. bitmap 0x02: one line per layer. bitmap 0x04: real verbose.</p>
<dt>-l LAYERS, &#8211;layers=LAYERS</p>
<dd> Layers to display [default: &#8216;nfs,nlm,mount,portmap&#8217;]. Valid layers: ethernet, ip, tcp, udp, rpc, nfs, nlm, mount, portmap</p>
<dt>-s START, &#8211;start=START</p>
<dd> Start index [default: 0]</p>
<dt>-e END, &#8211;end=END</p>
<dd> End index [default: 0]</p>
<dt>-m MATCH, &#8211;match=MATCH</p>
<dd> Match string [default: True]</p>
<dt>-c, &#8211;call</p>
<dd> If matching a reply packet, include its coresponding call in the output</p>
<dt>-r, &#8211;reply</p>
<dd> If matching a call packet, include its coresponding reply in the output</p>
<dt>-d DISPLAY, &#8211;display=DISPLAY</p>
<dd> Print specific packet or part of a packet [default: pkt]</p>
<dt>-z TZ, &#8211;tz=TZ</p>
<dd> Time zone to use to display timestamps </p>
</dl>
<h3>RPC display:</h3>
<dl>
<dt>&#8211;rpc-type=RPC_TYPE</p>
<dd> Display RPC type [default: True]</p>
<dt>&#8211;rpc-load=RPC_LOAD</p>
<dd> Display RPC load type (NFS, NLM, etc.) [default: True]</p>
<dt>&#8211;rpc-ver=RPC_VER</p>
<dd> Display RPC load version [default: True]</p>
<dt>&#8211;rpc-xid=RPC_XID</p>
<dd> Display RPC xid [default: True] </p>
</dl>
<h3>Packet display:</h3>
<dl>
<dt>&#8211;nfs-mainop=NFS_MAINOP</p>
<dd> Display NFSv4 main operation only [default: False]</p>
<dt>&#8211;load-body=LOAD_BODY</p>
<dd> Display RPC payload body [default: True]</p>
<dt>&#8211;crc16=CRC16</p>
<dd> Display CRC16 encoded strings [default: True]</p>
<dt>&#8211;crc32=CRC32</p>
<dd> Display CRC32 encoded strings [default: True]</p>
<dt>&#8211;strsize=STRSIZE</p>
<dd> Truncate all strings to this size [default: 0] </p>
</dl>
<h3>Debug:</h3>
<dl>
<dt>&#8211;enum-check=ENUM_CHECK</p>
<dd> If set to True, enums are strictly enforced [default: True]</p>
<dt>&#8211;debug-level=DEBUG_LEVEL</p>
<dd> Set debug level messages</dl>
<h2>EXAMPLES</h2>
<p> # Display all NFS packets (one line per packet)<br />
 # Display only the NFS packets by default.<br />
 # Default for &#8211;verbose option is 1 &#8212; one line per packet<br />
 $ nfstest_pkt /tmp/trace.cap </p>
<p> # Display all NFS packets (one line per layer)<br />
 $ nfstest_pkt -v 2 /tmp/trace.cap </p>
<p> # Display all NFS packets (real verbose, all items in each layer are displayed)<br />
 $ nfstest_pkt -v 4 /tmp/trace.cap </p>
<p> # Display all NFS packets (display both verbose level 1 and 2)<br />
 $ nfstest_pkt -v 3 /tmp/trace.cap </p>
<p> # Display all TCP packets (this will display all RPC and NFS packets as well)<br />
 $ nfstest_pkt -l tcp /tmp/trace.cap </p>
<p> # Display all packets<br />
 $ nfstest_pkt -l all /tmp/trace.cap </p>
<p> # Display all NFS, NLM, MOUNT and PORTMAP packets<br />
 $ nfstest_pkt -l nfs,nlm,mount,portmap /tmp/trace.cap </p>
<p> # Display packets 100 through 199<br />
 $ nfstest_pkt -s 100 -e 200 -l all /tmp/trace.cap </p>
<p> # Display all NFS packets with non-zero status<br />
 $ nfstest_pkt -m &quot;nfs.status != 0&quot; /tmp/trace.cap </p>
<p> # Display all NFSv4 WRITE packets<br />
 $ nfstest_pkt -m &quot;rpc.version == 4 and nfs.op == 38&quot; /tmp/trace.cap </p>
<p> # Display all NFSv4 WRITE calls<br />
 $ nfstest_pkt -m &quot;rpc.version == 4 and nfs.argop == 38&quot; /tmp/trace.cap </p>
<p> # Display all NFS packets having a file name as f00000001 (OPEN, LOOKUP, etc.)<br />
 # including their replies<br />
 $ nfstest_pkt -r -m &quot;nfs.name == &#8216;f00000001&#8217;&quot; /tmp/trace.cap </p>
<p> # Display all NFS packets with non-zero status including their respective calls<br />
 $ nfstest_pkt -c -m &quot;nfs.status != 0&quot; /tmp/trace.cap<br />
 $ nfstest_pkt -d &quot;pkt_call,pkt&quot; -m &quot;nfs.status != 0&quot; /tmp/trace.cap </p>
<p> # Display all TCP packets (just the TCP layer)<br />
 $ nfstest_pkt -d &quot;pkt.tcp&quot; -l tcp /tmp/trace.cap </p>
<p> # Display all NFS file handles<br />
 $ nfstest_pkt -d &quot;pkt.NFSop.fh&quot; -m &quot;len(nfs.fh) &gt; 0&quot; /tmp/trace.cap </p>
<p> # Display all RPC packets including the record infomation (packet number, timestamp, etc.)<br />
 # For verbose level 1 (default) the &quot;,&quot; separator will be converted to a<br />
 # space if all items are only pkt(.*)? or pkt_call(.*)?<br />
 $ nfstest_pkt -d &quot;pkt.record,pkt.rpc&quot; -l rpc /tmp/trace.cap </p>
<p> # Display all RPC packets including the record infomation (packet number, timestamp, etc.)<br />
 # For verbose level 2 the &quot;,&quot; separator will be converted to a new line if<br />
 # all items are only pkt(.*)? or pkt_call(.*)?<br />
 $ nfstest_pkt -v 2 -d &quot;pkt.record,pkt.rpc&quot; -l rpc /tmp/trace.cap </p>
<p> # Display all RPC packets including the record infomation (packet number, timestamp, etc.)<br />
 # using the given display format<br />
 $ nfstest_pkt -d &quot;&gt;&gt;&gt; record: pkt.record &gt;&gt;&gt; rpc: pkt.rpc&quot; -l rpc /tmp/trace.cap </p>
<p> # Display all packets truncating all strings to 100 bytes<br />
 # This is useful when some packets are very large and there<br />
 # is no need to display all the data<br />
 $ nfstest_pkt &#8211;strsize 100 -v 2 -l all /tmp/trace.cap </p>
<p> # Display all NFSv4 packets displaying the main operation of the compound<br />
 # e.g., display &quot;WRITE&quot; instead of &quot;SEQUENCE;PUTFH;WRITE&quot;<br />
 $ nfstest_pkt &#8211;nfs-mainop 1 -l nfs /tmp/trace.cap </p>
<p> # Have all CRC16 strings displayed as plain strings<br />
 # e.g., display unformatted state ids<br />
 $ nfstest_pkt &#8211;crc16 0 /tmp/trace.cap </p>
<p> # Have all CRC32 strings displayed as plain strings<br />
 # e.g., display unformatted file handles<br />
 $ nfstest_pkt &#8211;crc32 0 /tmp/trace.cap </p>
<p> # Display packets using India time zone<br />
 $ nfstest_pkt &#8211;tz &quot;UTC-5:30&quot; /tmp/trace.cap<br />
 $ nfstest_pkt &#8211;tz &quot;Asia/Kolkata&quot; /tmp/trace.cap </p>
<p> # Display all packets for all trace files given<br />
 # The packets are displayed in order using their timestamps<br />
 $ nfstest_pkt trace1.cap trace2.cap trace3.cap</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-formatstr/">formatstr</a>(3),</code> <code><a href="/docs/linux/man/1-nfstest_alloc/">nfstest_alloc</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_cache/">nfstest_cache</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_delegation/">nfstest_delegation</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_dio/">nfstest_dio</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_file/">nfstest_file</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_interop/">nfstest_interop</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_io/">nfstest_io</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_lock/">nfstest_lock</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pnfs/">nfstest_pnfs</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_posix/">nfstest_posix</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_sparse/">nfstest_sparse</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_xid/">nfstest_xid</a>(1),</code> <code><a href="/docs/linux/man/3-packet-pktt/">packet.pktt</a>(3),</code> <code><a href="/docs/linux/man/3-packet-utils/">packet.utils</a>(3)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
