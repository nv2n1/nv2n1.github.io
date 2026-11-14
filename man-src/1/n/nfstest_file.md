---
title: "nfstest_file(1)"
name: "nfstest_file"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfstest_file/"
description: "nfstest_file – Find all packets for a specific file"
---

<h2>NAME</h2>
<p> nfstest_file &#8211; Find all packets for a specific file</p>
<h2>SYNOPSIS</h2>
<p> nfstest_file [options] -p &lt;filepath&gt; &lt;trace1.cap&gt; [&lt;trace2.cap&gt; &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Display all NFS packets for the specified path. It takes a relative path, where it searches for each of the directory entries given in the path until it gets the file handle for the directory where the file is located. Once the directory file handle is found, a LOOKUP or OPEN/CREATE is searched for the given file name. If the file lookup or creation is found, all file handles and state ids associated with that file are searched and all packets found, including their respective replies are displayed. </p>
<p> There are three levels of verbosity in which they are specified using a bitmap, where the most significant bit gives a more verbose output. Verbose level 1 is used as a default where each packet is displayed condensed to one line using the last layer of the packet as the main output. </p>
<p> The packet trace files are processed either serially or in parallel. The packets are displayed using their timestamps so they are always displayed in the correct order even if the files given are out of order. If the packet traces were captured one after the other the packets are displayed serially, first the packets of the first file according to their timestamps, then the second and so forth. If the packet traces were captured at the same time on multiple clients the packets are displayed in parallel, packets are interleaved from all the files when displayed again according to their timestamps. </p>
<p> Note: A packet call can be displayed out of order if the call is not matched by any of the file handles, state ids or names but its reply is matched so its corresponding call is displayed right before the reply. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;version</p>
<dd> show program&#8217;s version number and exit</p>
<dt>-h, &#8211;help</p>
<dd> show this help message and exit</p>
<dt>-p PATH, &#8211;path=PATH</p>
<dd> Path relative to the mount point, the path can be specified by its file handle &#8216;FH:0xc3f001b4&#8217;. Also the relative path could start with a directory file handle &#8216;DH:0x0c35bb58/file_name&#8217;</p>
<dt>&#8211;stid=STID</p>
<dd> State id to include in the search</p>
<dt>-v VERBOSE, &#8211;verbose=VERBOSE</p>
<dd> Verbose level bitmask [default: 1]. bitmap 0x01: one line per packet. bitmap 0x02: one line per layer. bitmap 0x04: real verbose.</p>
<dt>-s START, &#8211;start=START</p>
<dd> Start index [default: 0]</p>
<dt>-e END, &#8211;end=END</p>
<dd> End index [default: 0]</p>
<dt>-z TZ, &#8211;tz=TZ</p>
<dd> Time zone to use to display timestamps </p>
</dl>
<h3>Packet display:</h3>
<dl>
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
<p> # Find all packets for relative path: nfstest_file -p data/name_d_1/name_d_2/name_f_13 nested_dir_v3.cap </p>
<p> # Find all packets for relative path, starting with a directory file handle: nfstest_file -p DH:0x34ac5f28/name_d_1/name_d_2/name_f_13 nested_dir_v3.cap </p>
<p> # Find all packets for file, starting with a directory file handle: nfstest_file -p DH:0x0c35bb58/name_f_13 nested_dir_v3.cap </p>
<p> # Find all packets for file handle nfstest_file -p FH:0xc3f001b4 /tmp/trace.cap </p>
<p> # Find all packets for file, including all operations for the given state id nfstest_file -p f00000001 &#8211;stid 0x0fd4 /tmp/trace.cap </p>
<p> # Display all packets for file (one line per layer) nfstest_file -p f00000001 -v 2 /tmp/trace.cap </p>
<p> # Display all packets for file<br />
 # (real verbose, all items in each layer are displayed) nfstest_file -p f00000001 -v 4 /tmp/trace.cap </p>
<p> # Display all packets for file (display both verbose level 1 and 2) nfstest_file -p f00000001 -v 3 /tmp/trace.cap </p>
<p> # Display packets for file between packets 100 through 199<br />
 $ nfstest_file -p f00000001 -s 100 -e 200 /tmp/trace.cap </p>
<p> # Display all packets truncating all strings to 100 bytes<br />
 # This is useful when some packets are very large and there<br />
 # is no need to display all the data<br />
 $ nfstest_file -p f00000001 &#8211;strsize 100 -v 2 /tmp/trace.cap </p>
<p> # Display packets using India time zone<br />
 $ nfstest_file -p f00000001 &#8211;tz &quot;UTC-5:30&quot; /tmp/trace.cap<br />
 $ nfstest_file -p f00000001 &#8211;tz &quot;Asia/Kolkata&quot; /tmp/trace.cap </p>
<p> # Display all packets for file found in all trace files given<br />
 # The packets are displayed in order using their timestamps<br />
 $ nfstest_file -p f00000001 trace1.cap trace2.cap trace3.cap</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-formatstr/">formatstr</a>(3),</code> <code><a href="/docs/linux/man/1-nfstest_alloc/">nfstest_alloc</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_cache/">nfstest_cache</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_delegation/">nfstest_delegation</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_dio/">nfstest_dio</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_interop/">nfstest_interop</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_io/">nfstest_io</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_lock/">nfstest_lock</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pkt/">nfstest_pkt</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pnfs/">nfstest_pnfs</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_posix/">nfstest_posix</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_sparse/">nfstest_sparse</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_xid/">nfstest_xid</a>(1),</code> <code><a href="/docs/linux/man/3-packet-nfs-nfs3_const/">packet.nfs.nfs3_const</a>(3),</code> <code><a href="/docs/linux/man/3-packet-nfs-nfs4_const/">packet.nfs.nfs4_const</a>(3),</code> <code><a href="/docs/linux/man/3-packet-pktt/">packet.pktt</a>(3),</code> <code><a href="/docs/linux/man/3-packet-utils/">packet.utils</a>(3)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
