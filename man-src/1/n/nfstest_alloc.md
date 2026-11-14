---
title: "nfstest_alloc(1)"
name: "nfstest_alloc"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfstest_alloc/"
description: "nfstest_alloc – Space reservation tests"
---

<h2>NAME</h2>
<p> nfstest_alloc &#8211; Space reservation tests</p>
<h2>SYNOPSIS</h2>
<p> nfstest_alloc &#8211;server &lt;server&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> Verify correct functionality of space reservations so applications are able to reserve or unreserve space for a file. The system call fallocate is used to manipulate the allocated disk space for a file, either to preallocate or deallocate it. For filesystems which support the fallocate system call, preallocation is done quickly by allocating blocks and marking them as uninitialized, requiring no I/O to the data blocks. This is much faster than creating a file and filling it with zeros. </p>
<p> Basic allocate tests verify the disk space is actually preallocated or reserved for the given range by filling up the device after the allocation and make sure data can be written to the allocated range without any problems. Also, any data written outside the allocated range will fail with NFS4ERR_NOSPC when there is no more space left on the device. On the other hand, deallocating space will give the disk space back so it can be used by either the same file on regions not already preallocated or by different files without the risk of getting a no space error. </p>
<p> Performance testing using ALLOCATE versus initializing a file to all zeros is also included. The performance comparison is done with different file sizes. </p>
<p> Some tests include testing at the protocol level by taking a packet trace and inspecting the actual packets sent to the server or servers. </p>
<p> Negative testing is included whenever possible since some testing cannot be done at the protocol level because the fallocate system call does some error checking of its own and the NFS client won&#8217;t even send an ALLOCATE or DEALLOCATE operation to the server letting the server deal with the error. Negative tests include trying to allocate an invalid range, having an invalid value for either the offset or the length, trying to allocate or deallocate a region on a file opened as read only or the file is a non-regular file type. </p>
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
<dd> NFS version, e.g., 3, 4, 4.1, etc. [default: 4.2]</p>
<dt>-m MTPOINT, &#8211;mtpoint=MTPOINT</p>
<dd> Mount point [default: &#8216;/mnt/t&#8217;]</p>
<dt>-p PORT, &#8211;port=PORT</p>
<dd> NFS server port [default: 2049]</p>
<dt>&#8211;proto=PROTO</p>
<dd> NFS protocol name [default: &#8216;tcp&#8217;]</p>
<dt>&#8211;sec=SEC</p>
<dd> Security flavor [default: &#8216;sys&#8217;]</p>
<dt>-o MTOPTS, &#8211;mtopts=MTOPTS</p>
<dd> Mount options [default: &#8216;hard,rsize=4096,wsize=4096&#8217;]</p>
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
<dd> File size to use for test files [default: 65536]</p>
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
<dt>&#8211;perf-fsize=PERF_FSIZE</p>
<dd> Starting file size for the perf01 test [default: 1MB]</p>
<dt>&#8211;perf-mult=PERF_MULT</p>
<dd> File size multiplier for the perf01 test, the tests are performed for a file size which is a multiple of the previous test file size [default: 4]</p>
<dt>&#8211;perf-time=PERF_TIME</p>
<dd> Run the performance test perf01 until the sub-test for the current file size executes for more than this time [default: 15]</dl>
<h2>TESTS</h2>
<h3>alloc</h3>
<pre>
Run all ALLOCATE tests: alloc01, alloc02, alloc03, alloc04, alloc05,
alloc06
</pre>
<h3>alloc01</h3>
<pre>
Verify ALLOCATE succeeds on files opened as write only
</pre>
<h3>alloc02</h3>
<pre>
Verify ALLOCATE succeeds on files opened as read and write
</pre>
<h3>alloc03</h3>
<pre>
Verify ALLOCATE fails on files opened as read only
</pre>
<h3>alloc04</h3>
<pre>
Verify ALLOCATE fails with EINVAL for invalid offset or length
</pre>
<h3>alloc05</h3>
<pre>
Verify ALLOCATE fails with ESPIPE when using a named pipe file handle
</pre>
<h3>alloc06</h3>
<pre>
Verify ALLOCATE reserves the disk space
</pre>
<h3>dealloc</h3>
<pre>
Run all DEALLOCATE tests: dealloc01, dealloc02, dealloc03, dealloc04,
dealloc05, dealloc06
</pre>
<h3>dealloc01</h3>
<pre>
Verify DEALLOCATE succeeds on files opened as write only
</pre>
<h3>dealloc02</h3>
<pre>
Verify DEALLOCATE succeeds on files opened as read and write
</pre>
<h3>dealloc03</h3>
<pre>
Verify DEALLOCATE fails on files opened as read only
</pre>
<h3>dealloc04</h3>
<pre>
Verify DEALLOCATE fails with EINVAL for invalid offset or length
</pre>
<h3>dealloc05</h3>
<pre>
Verify DEALLOCATE fails with ESPIPE when using a named pipe file handle
</pre>
<h3>dealloc06</h3>
<pre>
Verify DEALLOCATE unreserves the disk space
</pre>
<h3>perf01</h3>
<pre>
Verify ALLOCATE outperforms initializing the file to all zeros
</pre>
<h2>EXAMPLES</h2>
<p> The only required option is &#8211;server<br />
 $ nfstest_alloc &#8211;server 192.168.0.11</p>
<h2>NOTES</h2>
<p> The user id in the local host must have access to run commands as root using the &#8216;sudo&#8217; command without the need for a password. </p>
<p> Tests which require filling up all the disk space on the mounted device should have exclusive access to the device. </p>
<p> Valid only for NFS version 4.2 and above.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-formatstr/">formatstr</a>(3),</code> <code><a href="/docs/linux/man/3-nfstest-test_util/">nfstest.test_util</a>(3),</code> <code><a href="/docs/linux/man/3-nfstest-utils/">nfstest.utils</a>(3),</code> <code><a href="/docs/linux/man/1-nfstest_cache/">nfstest_cache</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_delegation/">nfstest_delegation</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_dio/">nfstest_dio</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_file/">nfstest_file</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_interop/">nfstest_interop</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_io/">nfstest_io</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_lock/">nfstest_lock</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pkt/">nfstest_pkt</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pnfs/">nfstest_pnfs</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_posix/">nfstest_posix</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_sparse/">nfstest_sparse</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_xid/">nfstest_xid</a>(1),</code> <code><a href="/docs/linux/man/3-packet-nfs-nfs4_const/">packet.nfs.nfs4_const</a>(3)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
