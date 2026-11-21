---

title: "nfstest_dio(1)"
name: "nfstest_dio"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfstest_dio/"
description: "nfstest_dio – Direct I/O tests"
---

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
<dt>&#8211;version</dt>
<dd> show program&#8217;s version number and exit</dd>
<dt>-h, &#8211;help</dt>
<dd> show this help message and exit</dd>
<dt>-f FILE, &#8211;file=FILE</dt>
<dd> File where options are specified besides the system wide file /etc/nfstest, user wide file $HOME/.nfstest or in the current directory .nfstest file </dd>
</dl>
<h3>NFS specific options:</h3>
<dl>
<dt>-s SERVER, &#8211;server=SERVER</dt>
<dd> Server name or IP address</dd>
<dt>-e EXPORT, &#8211;export=EXPORT</dt>
<dd> Exported file system to mount [default: &#8216;/&#8217;]</dd>
<dt>&#8211;nfsversion=NFSVERSION</dt>
<dd> NFS version, e.g., 3, 4, 4.1, etc. [default: 4.1]</dd>
<dt>-m MTPOINT, &#8211;mtpoint=MTPOINT</dt>
<dd> Mount point [default: &#8216;/mnt/t&#8217;]</dd>
<dt>-p PORT, &#8211;port=PORT</dt>
<dd> NFS server port [default: 2049]</dd>
<dt>&#8211;proto=PROTO</dt>
<dd> NFS protocol name [default: &#8216;tcp&#8217;]</dd>
<dt>&#8211;sec=SEC</dt>
<dd> Security flavor [default: &#8216;sys&#8217;]</dd>
<dt>-o MTOPTS, &#8211;mtopts=MTOPTS</dt>
<dd> Mount options [default: &#8216;hard,intr&#8217;]</dd>
<dt>&#8211;datadir=DATADIR</dt>
<dd> Data directory where files are created, directory is created on the mount point [default: &#8221;] </dd>
</dl>
<h3>Logging options:</h3>
<dl>
<dt>-v VERBOSE, &#8211;verbose=VERBOSE</dt>
<dd> Verbose level for debug messages [default: &#8216;none&#8217;]</dd>
<dt>&#8211;tverbose=TVERBOSE</dt>
<dd> Verbose level for test messages [default: &#8216;1&#8217;]</dd>
<dt>&#8211;createlog</dt>
<dd> Create log file</dd>
<dt>&#8211;warnings</dt>
<dd> Display warnings</dd>
<dt>&#8211;tag=TAG</dt>
<dd> Informational tag, it is displayed as an INFO message [default: &#8221;] </dd>
</dl>
<h3>Packet trace options:</h3>
<dl>
<dt>&#8211;createtraces</dt>
<dd> Create a packet trace for each test</dd>
<dt>&#8211;tbsize=TBSIZE</dt>
<dd> Capture buffer size for tcpdump [default: &#8216;50000&#8217;]</dd>
<dt>&#8211;trcdelay=TRCDELAY</dt>
<dd> Seconds to delay before stopping packet trace [default: 0.0]</dd>
<dt>&#8211;keeptraces</dt>
<dd> Do not remove any trace files [default: remove trace files if no errors]</dd>
<dt>&#8211;rmtraces</dt>
<dd> Remove trace files [default: remove trace files if no errors]</dd>
<dt>-i INTERFACE, &#8211;interface=INTERFACE</dt>
<dd> Device interface [default: automatically selected] </dd>
</dl>
<h3>File options:</h3>
<dl>
<dt>&#8211;nfiles=NFILES</dt>
<dd> Number of files to create [default: 2]</dd>
<dt>&#8211;filesize=FILESIZE</dt>
<dd> File size to use for test files [default: 262144]</dd>
<dt>&#8211;rsize=RSIZE</dt>
<dd> Read size to use when reading files [default: 4096]</dd>
<dt>&#8211;wsize=WSIZE</dt>
<dd> Write size to use when writing files [default: 4096]</dd>
<dt>&#8211;iodelay=IODELAY</dt>
<dd> Seconds to delay I/O operations [default: 0.1]</dd>
<dt>&#8211;offset-delta=OFFSET_DELTA</dt>
<dd> Read/Write offset delta [default: 4096] </dd>
</dl>
<h3>Path options:</h3>
<dl>
<dt>&#8211;sudo=SUDO</dt>
<dd> Full path of binary for sudo [default: &#8216;/usr/bin/sudo&#8217;]</dd>
<dt>&#8211;tcpdump=TCPDUMP</dt>
<dd> Full path of binary for tcpdump [default: &#8216;/usr/sbin/tcpdump&#8217;]</dd>
<dt>&#8211;iptables=IPTABLES</dt>
<dd> Full path of binary for iptables [default: &#8216;/sbin/iptables&#8217;]</dd>
<dt>&#8211;messages=MESSAGES</dt>
<dd> Full path of log messages file [default: &#8216;/var/log/messages&#8217;]</dd>
<dt>&#8211;tmpdir=TMPDIR</dt>
<dd> Temporary directory [default: &#8216;/tmp&#8217;] </dd>
</dl>
<h3>Debug options:</h3>
<dl>
<dt>&#8211;nocleanup</dt>
<dd> Do not cleanup created files</dd>
<dt>&#8211;bugmsgs=BUGMSGS</dt>
<dd> File containing test messages to mark as bugs if they failed</dd>
<dt>&#8211;ignore</dt>
<dd> Ignore all bugs given by bugmsgs</dd>
<dt>&#8211;nomount</dt>
<dd> Do not mount server and run the tests on local disk space</dd>
<dt>&#8211;basename=BASENAME</dt>
<dd> Base name for all files and logs [default: automatically generated]</dd>
<dt>&#8211;nfsdebug=NFSDEBUG</dt>
<dd> Set NFS kernel debug flags and save log messages [default: &#8221;]</dd>
<dt>&#8211;rpcdebug=RPCDEBUG</dt>
<dd> Set RPC kernel debug flags and save log messages [default: &#8221;] </dd>
</dl>
<h3>Test options:</h3>
<dl>
<dt>&#8211;runtest=RUNTEST</dt>
<dd> Comma separated list of tests to run, if list starts with a &#8216;^&#8217; then all tests are run except the ones listed [default: &#8216;all&#8217;]</dd>
<dt>&#8211;iotype=IOTYPE</dt>
<dd> List of I/O types to test [default: &#8216;read,write&#8217;]</dd>
<dt>&#8211;biotype=BIOTYPE</dt>
<dd> List of buffered I/O types to test [default: &#8216;none,read,write&#8217;]</dd>
<dt>&#8211;withdeleg=WITHDELEG</dt>
<dd> Use delegation on tests [default: both without and with delegation]</dd></dl>
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
