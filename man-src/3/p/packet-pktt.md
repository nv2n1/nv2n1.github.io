---
title: "packet-pktt(3)"
name: "packet-pktt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-pktt/"
description: "packet.pktt – Packet trace module"
---

<p>packet.pktt &#8211; Packet trace module</p>
<h2>Description</h2>
<p>The Packet trace module is a python module that takes a trace file created by tcpdump and unpacks the contents of each packet. You can decode one packet at a time, or do a search for specific packets. The main difference between these modules and other tools used to decode trace files is that you can use this module to completely automate your tests. </p>
<p> How does it work? It opens the trace file and reads one record at a time keeping track where each record starts. This way, very large trace files can be opened without having to wait for the file to load and avoid loading the whole file into memory. </p>
<p> Packet layers supported:<br />
&nbsp;<wbr>&#8211; ETHERNET II&nbsp;<wbr>(RFC 894)<br />
&nbsp;<wbr>&#8211; IP layer&nbsp;<wbr>(supports IPv4 and IPv6)<br />
&nbsp;<wbr>&#8211; UDP layer<br />
&nbsp;<wbr>&#8211; TCP layer<br />
&nbsp;<wbr>&#8211; RPC layer<br />
&nbsp;<wbr>&#8211; NFS v4.0<br />
&nbsp;<wbr>&#8211; NFS v4.1 including pNFS file layouts<br />
&nbsp;<wbr>&#8211; NFS v4.2<br />
&nbsp;<wbr>&#8211; PORTMAP v2<br />
&nbsp;<wbr>&#8211; MOUNT v3<br />
&nbsp;<wbr>&#8211; NLM v4</p>
<h2>Classes</h2>
<h3>class Header(baseobj.BaseObj)</h3>
<pre><code>Methods defined here:</code>
---------------------
<code>__init__(self, pktt)</code></pre>
<h3>class Pktt(baseobj.BaseObj, packet.unpack.Unpack)</h3>
<pre>Packet trace object
Usage:
 from packet.pktt import Pktt
 x = Pktt(&quot;/traces/tracefile.cap&quot;)
 # Iterate over all packets found in the trace file
 for pkt in x:
 print pkt
<code>Methods defined here:</code>
---------------------
<code>__contains__(self, expr)</code>
Implement membership test operator.
Return true if expr matches a packet in the trace file,
false otherwise.
The packet is also stored in the object attribute pkt.
Examples:
 # Find the next READ request
 if (&quot;NFS.argop == 25&quot; in x):
 print x.pkt.nfs
See match() method for more information
<code>__del__(self)</code>
Destructor
Gracefully close the tcpdump trace file if it is opened.
<code>__getitem__(self, index)</code>
Get the packet from the trace file given by the index
or raise IndexError.
The packet is also stored in the object attribute pkt.
Examples:
 pkt = x[index]
<code>__init__(self, tfile, live=False, state=True)</code>
Constructor
Initialize object's private data, note that this will not check the
file for existence nor will open the file to verify if it is a valid
tcpdump file. The tcpdump trace file will be opened the first time a
packet is retrieved.
<dl><dt><dd><dl><dt><code>tracefile:</code>
<dd>Name of tcpdump trace file or a list of trace file names
(little or big endian format)
<dt><code>live:</code>
<dd>If set to True, methods will not return if encountered &lt;EOF&gt;,
they will keep on trying until more data is available in the
file. This is useful when running tcpdump in parallel,
especially when tcpdump is run with the '-C' option, in which
case when &lt;EOF&gt; is encountered the next trace file created by
tcpdump will be opened and the object will be re-initialized,
all private data referencing the previous file is lost.
</dl></dl>
<code>__iter__(self)</code>
Make this object iterable.
<code>clear_xid_list(self)</code>
Clear list of outstanding xids
<code>match(self, expr, maxindex=None, rewind=True, reply=False)</code>
Return the packet that matches the given expression, also the packet
index points to the next packet after the matched packet.
Returns None if packet is not found and the packet index points
to the packet at the beginning of the search.
<dl><dt><dd><dl><dt><code>expr:</code>
<dd>String of expressions to be evaluated
<dt><code>maxindex:</code>
<dd>The match fails if packet index hits this limit
<dt><code>rewind:</code>
<dd>Rewind to index where matching started if match fails
<dt><code>reply:</code>
<dd>Match RPC replies of previously matched calls as well
</dl></dl><dl><dt><dd>Examples:
 # Find the packet with both the ACK and SYN TCP flags set to 1
 pkt = x.match(&quot;TCP.flags.ACK == 1 and TCP.flags.SYN == 1&quot;)
 # Find the next NFS EXCHANGE_ID request
 pkt = x.match(&quot;NFS.argop == 42&quot;)
 # Find the next NFS EXCHANGE_ID or CREATE_SESSION request
 pkt = x.match(&quot;NFS.argop in [42,43]&quot;)
 # Find the next NFS OPEN request or reply
 pkt = x.match(&quot;NFS.op == 18&quot;)
 # Find all packets coming from subnet 192.168.1.0/24 using
 # a regular expression
 while x.match(r&quot;IP.src == re('192.168.1.*')&quot;):
 print x.pkt.tcp
 # Find packet having a GETATTR asking for FATTR4_FS_LAYOUT_TYPES(bit 62)
 pkt_call = x.match(&quot;NFS.attr_request &amp; 0x4000000000000000L != 0&quot;)
 if pkt_call:
 # Find GETATTR reply
 xid = pkt_call.rpc.xid
 # Find reply where the number 62 is in the array NFS.attributes
 pkt_reply = x.match(&quot;RPC.xid == %d and 62 in NFS.attributes&quot; % xid)
 # Find the next WRITE request
 pkt = x.match(&quot;NFS.argop == 38&quot;)
 if pkt:
 print pkt.nfs
 # Same as above, but using membership test operator instead
 if (&quot;NFS.argop == 38&quot; in x):
 print x.pkt.nfs
See also:
 match_ethernet(), match_ip(), match_tcp(), match_rpc(), match_nfs()
</dl>
<code>match_nfs(self, uargs)</code>
Match NFS values on current packet.
In NFSv4, there is a single compound procedure with multiple
operations, matching becomes a little bit tricky in order to make
the matching expression easy to use. The NFS object's name space
gets converted into a flat name space for the sole purpose of
matching. In other words, all operation objects in array are
treated as being part of the NFS object's top level attributes.
Consider the following NFS object:
 nfsobj = COMPOUND4res(
 status=NFS4_OK,
 tag='NFSv4_tag',
 array = [
 nfs_resop4(
 resop=OP_SEQUENCE,
 opsequence=SEQUENCE4res(
 status=NFS4_OK,
 resok=SEQUENCE4resok(
 sessionid='sessionid',
 sequenceid=29,
 slotid=0,
 highest_slotid=179,
 target_highest_slotid=179,
 status_flags=0,
 ),
 ),
 ),
 nfs_resop4(
 resop=OP_PUTFH,
 opputfh = PUTFH4res(
 status=NFS4_OK,
 ),
 ),
 ...
 ]
 ),
The result for operation PUTFH is the second in the list:
 putfh = nfsobj.array[1]
From this putfh object the status operation can be accessed as:
 status = putfh.opputfh.status
or simply as (this is how the NFS object works):
 status = putfh.status
In this example, the following match expression 'NFS.status == 0'
could match the top level status of the compound (nfsobj.status)
or the putfh status (nfsobj.array[1].status)
The following match expression 'NFS.sequenceid == 25' will also
match this packet as well, even though the actual expression should
be 'nfsobj.array[0].opsequence.resok.sequenceid == 25' or
simply 'nfsobj.array[0].sequenceid == 25'.
This approach makes the match expressions simpler at the expense of
having some ambiguities on where the actual matched occurred. If a
match is desired on a specific operation, a more qualified name can
be given. In the above example, in order to match the status of the
PUTFH operation the match expression 'NFS.opputfh.status == 0' can
be used. On the other hand, consider a compound having multiple
PUTFH results the above match expression will always match the first
occurrence of PUTFH where the status is 0. There is no way to tell
the match engine to match the second or Nth occurrence of an
operation.
<code>next(self)</code>
Get the next packet from the trace file or raise StopIteration.
The packet is also stored in the object attribute pkt.
Examples:
 # Iterate over all packets found in the trace file using
 # the iterable properties of the object
 for pkt in x:
 print pkt
 # Iterate over all packets found in the trace file using it
 # as a method and using the object variable as the packet
 # Must use the try statement to catch StopIteration exception
 try:
 while (x.next()):
 print x.pkt
 except StopIteration:
 pass
 # Iterate over all packets found in the trace file using it
 # as a method and using the return value as the packet
 # Must use the try statement to catch StopIteration exception
 while True:
 try:
 print x.next()
 except StopIteration:
 break
NOTE:
 Supports only single active iteration
<code>rewind(self, index=0)</code>
Rewind the trace file by setting the file pointer to the start of
the given packet index. Returns False if unable to rewind the file,
e.g., when the given index is greater than the maximum number
of packets processed so far.
<code>Static methods defined here:</code>
----------------------------
<code>escape(data)</code>
Escape special characters.
Examples:
 # Call as an instance
 escaped_data = x.escape(data)
 # Call as a class
 escaped_data = Pktt.escape(data)
<code>ip_tcp_dst_expr(ipaddr, port)</code>
Return a match expression to find a packet going to ipaddr:port.
Examples:
 # Call as an instance
 expr = x.ip_tcp_dst_expr('192.168.1.50', 2049)
 # Call as a class
 expr = Pktt.ip_tcp_dst_expr('192.168.1.50', 2049)
 # Returns &quot;IP.dst == '192.168.1.50' and TCP.dst_port == 2049&quot;
 # Expression ready for x.match()
 pkt = x.match(expr)
<code>ip_tcp_src_expr(ipaddr, port)</code>
Return a match expression to find a packet coming from ipaddr:port.
Examples:
 # Call as an instance
 expr = x.ip_tcp_src_expr('192.168.1.50', 2049)
 # Call as a class
 expr = Pktt.ip_tcp_src_expr('192.168.1.50', 2049)
 # Returns &quot;IP.src == '192.168.1.50' and TCP.src_port == 2049&quot;
 # Expression ready for x.match()
 pkt = x.match(expr)</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-formatstr/">formatstr</a>(3),</code> <code><a href="/docs/linux/man/3-packet-link-ethernet/">packet.link.ethernet</a>(3),</code> <code><a href="/docs/linux/man/3-packet-pkt/">packet.pkt</a>(3),</code> <code><a href="/docs/linux/man/3-packet-record/">packet.record</a>(3),</code> <code><a href="/docs/linux/man/3-packet-unpack/">packet.unpack</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
