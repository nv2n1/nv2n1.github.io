---
title: "nfstest_xid(1)"
name: "nfstest_xid"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfstest_xid/"
description: "nfstest_xid – Verify packets are matched correctly by their XID"
---

<h2>NAME</h2>
<p> nfstest_xid &#8211; Verify packets are matched correctly by their XID</p>
<h2>SYNOPSIS</h2>
<p> nfstest_xid &lt;trace1&gt; [&lt;trace2&gt; &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Search all the packet traces given for XID inconsistencies. Verify all operations in the NFSv4.x COMPOUND reply are the same as the operations given in the call. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;version</p>
<dd> show program&#8217;s version number and exit</p>
<dt>-h, &#8211;help</p>
<dd> show this help message and exit </p>
</dl>
<h3>Packet display:</h3>
<dl>
<dt>&#8211;load-body=LOAD_BODY</p>
<dd> Display RPC payload body [default: False] </p>
</dl>
<h3>Debug:</h3>
<dl>
<dt>&#8211;enum-check=ENUM_CHECK</p>
<dd> If set to True, enums are strictly enforced [default: True]</p>
<dt>&#8211;debug-level=DEBUG_LEVEL</p>
<dd> Set debug level messages</p>
<dt>&#8211;unpack-error=UNPACK_ERROR</p>
<dd> Raise unpack error when True</p>
<dt>&#8211;error</p>
<dd> Exit on first error</dl>
<h2>EXAMPLES</h2>
<p> $ nfstest_xid /tmp/trace1.pcap</p>
<h2>NOTES</h2>
<p> Valid for packet traces with NFSv4 and above</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nfstest_alloc/">nfstest_alloc</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_cache/">nfstest_cache</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_delegation/">nfstest_delegation</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_dio/">nfstest_dio</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_file/">nfstest_file</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_interop/">nfstest_interop</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_io/">nfstest_io</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_lock/">nfstest_lock</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pkt/">nfstest_pkt</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pnfs/">nfstest_pnfs</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_posix/">nfstest_posix</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_sparse/">nfstest_sparse</a>(1),</code> <code><a href="/docs/linux/man/3-packet-pktt/">packet.pktt</a>(3),</code> <code><a href="/docs/linux/man/3-packet-unpack/">packet.unpack</a>(3),</code> <code><a href="/docs/linux/man/3-packet-utils/">packet.utils</a>(3)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
