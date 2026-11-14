---
title: "nfstest_dio(1)"
name: "nfstest_dio"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfstest_dio/"
description: "nfstest_dio – Direct I/O tests"
---

<h2>NAME</h2>
<p> nfstest_dio &#8211; Direct I/O tests</p>
<h2>SYNOPSIS</h2>
<p> nfstest_dio &#8211;server &lt;server&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> Functional direct I/O tests verify that every READ/WRITE is sent to the server instead of the client caching the requests. Client bypasses read ahead by sending the READ with only the requested bytes. Verify the client correctly handles eof marker when reading the whole file. Verify client ignores delegation while writing a file. </p>
<p> Direct I/O on pNFS tests verify the client sends the READ/WRITE to the correct DS or the MDS if using a PAGESIZE aligned buffer or not, respectively. </p>
<p> Direct I/O data correctness tests verify that a file written with buffered I/O is read correctly with direct I/O. Verify that a file written with direct I/O is read correctly with buffered I/O. </p>
<p> Vectored I/O tests verify coalescence of multiple vectors into one READ/WRITE packet when all vectors are PAGESIZE aligned. Vectors with different alignments are sent on separate packets. </p>
<p> Valid for NFSv4.0 and NFSv4.1 including pNFS. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;version</p>
<dd> show program&#8217;s version number and exit</p>
<dt>-h, &#8211;help</p>
<dd> show this help message and exit</p>
<dt>-f FILE, &#8211;file=FILE</p>
<dd> File where options are specified besides the system wide file /etc/nfstest, user wide file $HOME/.nfstest or in the current directory .nfstest file </p>
</dl>
<h3>NFS specific options:</h3>
<dl>
<dt>-s SERVER, &#8211;server=SERVER</p>
<dd> Server name or IP address</p>
<dt>-e EXPORT, &#8211;export=EXPORT</p>
<dd> Exported file system to mount [default: &#8216;/&#8217;]</p>
<dt>&#8211;nfsversion=NFSVERSION</p>
<dd> NFS version, e.g., 3, 4, 4.1, etc. [default: 4.1]</p>
<dt>-m MTPOINT, &#8211;mtpoint=MTPOINT</p>
<dd> Mount point [default: &#8216;/mnt/t&#8217;]</p>
<dt>-p PORT, &#8211;port=PORT</p>
<dd> NFS server port [default: 2049]</p>
<dt>&#8211;proto=PROTO</p>
<dd> NFS protocol name [default: &#8216;tcp&#8217;]</p>
<dt>&#8211;sec=SEC</p>
<dd> Security flavor [default: &#8216;sys&#8217;]</p>
<dt>-o MTOPTS, &#8211;mtopts=MTOPTS</p>
<dd> Mount options [default: &#8216;hard,intr&#8217;]</p>
<dt>&#8211;datadir=DATADIR</p>
<dd> Data directory where files are created, directory is created on the mount point [default: &#8221;] </p>
</dl>
<h3>Logging options:</h3>
<dl>
<dt>-v VERBOSE, &#8211;verbose=VERBOSE</p>
<dd> Verbose level for debug messages [default: &#8216;none&#8217;]</p>
<dt>&#8211;tverbose=TVERBOSE</p>
<dd> Verbose level for test messages [default: &#8216;1&#8217;]</p>
<dt>&#8211;createlog</p>
<dd> Create log file</p>
<dt>&#8211;warnings</p>
<dd> Display warnings</p>
<dt>&#8211;tag=TAG</p>
<dd> Informational tag, it is displayed as an INFO message [default: &#8221;] </p>
</dl>
<h3>Packet trace options:</h3>
<dl>
<dt>&#8211;createtraces</p>
<dd> Create a packet trace for each test</p>
<dt>&#8211;tbsize=TBSIZE</p>
<dd> Capture buffer size for tcpdump [default: &#8216;50000&#8217;]</p>
<dt>&#8211;trcdelay=TRCDELAY</p>
<dd> Seconds to delay before stopping packet trace [default: 0.0]</p>
<dt>&#8211;keeptraces</p>
<dd> Do not remove any trace files [default: remove trace files if no errors]</p>
<dt>&#8211;rmtraces</p>
<dd> Remove trace files [default: remove trace files if no errors]</p>
<dt>-i INTERFACE, &#8211;interface=INTERFACE</p>
<dd> Device interface [default: automatically selected] </p>
</dl>
<h3>File options:</h3>
<dl>
<dt>&#8211;nfiles=NFILES</p>
<dd> Number of files to create [default: 2]</p>
<dt>&#8211;filesize=FILESIZE</p>
<dd> File size to use for test files [default: 262144]</p>
<dt>&#8211;rsize=RSIZE</p>
<dd> Read size to use when reading files [default: 4096]</p>
<dt>&#8211;wsize=WSIZE</p>
<dd> Write size to use when writing files [default: 4096]</p>
<dt>&#8211;iodelay=IODELAY</p>
<dd> Seconds to delay I/O operations [default: 0.1]</p>
<dt>&#8211;offset-delta=OFFSET_DELTA</p>
<dd> Read/Write offset delta [default: 4096] </p>
</dl>
<h3>Path options:</h3>
<dl>
<dt>&#8211;sudo=SUDO</p>
<dd> Full path of binary for sudo [default: &#8216;/usr/bin/sudo&#8217;]</p>
<dt>&#8211;tcpdump=TCPDUMP</p>
<dd> Full path of binary for tcpdump [default: &#8216;/usr/sbin/tcpdump&#8217;]</p>
<dt>&#8211;iptables=IPTABLES</p>
<dd> Full path of binary for iptables [default: &#8216;/sbin/iptables&#8217;]</p>
<dt>&#8211;messages=MESSAGES</p>
<dd> Full path of log messages file [default: &#8216;/var/log/messages&#8217;]</p>
<dt>&#8211;tmpdir=TMPDIR</p>
<dd> Temporary directory [default: &#8216;/tmp&#8217;] </p>
</dl>
<h3>Debug options:</h3>
<dl>
<dt>&#8211;nocleanup</p>
<dd> Do not cleanup created files</p>
<dt>&#8211;bugmsgs=BUGMSGS</p>
<dd> File containing test messages to mark as bugs if they failed</p>
<dt>&#8211;ignore</p>
<dd> Ignore all bugs given by bugmsgs</p>
<dt>&#8211;nomount</p>
<dd> Do not mount server and run the tests on local disk space</p>
<dt>&#8211;basename=BASENAME</p>
<dd> Base name for all files and logs [default: automatically generated]</p>
<dt>&#8211;nfsdebug=NFSDEBUG</p>
<dd> Set NFS kernel debug flags and save log messages [default: &#8221;]</p>
<dt>&#8211;rpcdebug=RPCDEBUG</p>
<dd> Set RPC kernel debug flags and save log messages [default: &#8221;] </p>
</dl>
<h3>Test options:</h3>
<dl>
<dt>&#8211;runtest=RUNTEST</p>
<dd> Comma separated list of tests to run, if list starts with a &#8216;^&#8217; then all tests are run except the ones listed [default: &#8216;all&#8217;]</p>
<dt>&#8211;iotype=IOTYPE</p>
<dd> List of I/O types to test [default: &#8216;read,write&#8217;]</p>
<dt>&#8211;biotype=BIOTYPE</p>
<dd> List of buffered I/O types to test [default: &#8216;none,read,write&#8217;]</p>
<dt>&#8211;withdeleg=WITHDELEG</p>
<dd> Use delegation on tests [default: both without and with delegation]</dl>
<h2>TESTS</h2>
<h3>eof</h3>
<pre>
Verify eof marker is handled correctly when reading the end
of the file.
</pre>
<h3>correctness</h3>
<pre>
Verify data correctness when reading/writing using direct I/O.
File created with buffered I/O is read correctly with direct I/O.
File created with direct I/O is read correctly with buffered I/O.
</pre>
<h3>fstat</h3>
<pre>
Verify fstat() gets correct file size after writing.
</pre>
<h3>read</h3>
<pre>
Verify READ is sent after writing when the file is open for
both read and write.
</pre>
<h3>read_ahead</h3>
<pre>
Verify READ is sent with only the requested bytes bypassing
read ahead.
</pre>
<h3>basic</h3>
<pre>
Verify a packet is sent for each I/O request.
</pre>
<h3>rsize</h3>
<pre>
Verify multiple READ packets are sent for each read request
having request size &gt; rsize.
</pre>
<h3>wsize</h3>
<pre>
Verify multiple WRITE packets are sent for each write request
having request size &gt; wsize
</pre>
<h3>aligned</h3>
<pre>
Verify packet is sent to correct DS server when using a memory
which is PAGESIZE aligned.
</pre>
<h3>nonaligned</h3>
<pre>
Verify packet is sent to the MDS when using a memory which
is not PAGESIZE aligned.
</pre>
<h3>diffalign</h3>
<pre>
Verify packets are sent to both the MDS and correct DS on same open
using buffers with different alignments.
</pre>
<h3>stripesize</h3>
<pre>
Verify multiple packets are sent for each request having the
request size greater than stripe size.
</pre>
<h3>vectored_io</h3>
<pre>
Verify vectored I/O functionality.
</pre>
<h2>EXAMPLES</h2>
<p> The only required option is &#8211;server<br />
 $ nfstest_dio &#8211;server 192.168.0.11</p>
<h2>NOTES</h2>
<p> The user id in the local host must have access to run commands as root using the &#8216;sudo&#8217; command without the need for a password.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-nfstest-test_util/">nfstest.test_util</a>(3),</code> <code><a href="/docs/linux/man/1-nfstest_alloc/">nfstest_alloc</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_cache/">nfstest_cache</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_delegation/">nfstest_delegation</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_file/">nfstest_file</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_interop/">nfstest_interop</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_io/">nfstest_io</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_lock/">nfstest_lock</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pkt/">nfstest_pkt</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pnfs/">nfstest_pnfs</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_posix/">nfstest_posix</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_sparse/">nfstest_sparse</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_xid/">nfstest_xid</a>(1),</code> <code><a href="/docs/linux/man/3-packet-nfs-nfs4_const/">packet.nfs.nfs4_const</a>(3)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
