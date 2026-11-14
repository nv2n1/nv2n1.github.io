---
title: "nfstest_pnfs(1)"
name: "nfstest_pnfs"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfstest_pnfs/"
description: "nfstest_pnfs – Basic pNFS functional tests"
---

<h2>NAME</h2>
<p> nfstest_pnfs &#8211; Basic pNFS functional tests</p>
<h2>SYNOPSIS</h2>
<p> nfstest_pnfs &#8211;server &lt;server&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> Verify basic pNFS functionality for file (both READ and WRITE), including opening a second file within the same mount and having a lock on the file. Also, verify basic pNFS functionality for a file opened for both READ and WRITE while reading the file first and then writing to it or the other way around by writing to the file fist and then reading the file. These tests verify proper functionality of pNFS and NFSv4.1 as well. </p>
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
<dd> Comma separated list of tests to run, if list starts with a &#8216;^&#8217; then all tests are run except the ones listed [default: &#8216;all&#8217;]</dl>
<h2>TESTS</h2>
<h3>read</h3>
<pre>
Verify basic pNFS functionality on a couple of files opened for
reading within the same mount.
</pre>
<h3>write</h3>
<pre>
Verify basic pNFS functionality on a couple of files opened for
writing and then re-opening the first file for writing within
the same mount.
</pre>
<h3>write_read</h3>
<pre>
Verify basic pNFS functionality on a couple of files opened for
writing and then re-opening the first file for reading within
the same mount.
</pre>
<h3>read_lock</h3>
<pre>
Verify traffic for locked file opened for reading using pNFS.
</pre>
<h3>write_lock</h3>
<pre>
Verify traffic for locked file opened for writing using pNFS.
</pre>
<h3>setattr</h3>
<pre>
Verify setattr traffic for file using pNFS.
</pre>
<h3>setattr_lock</h3>
<pre>
Verify setattr traffic for locked file using pNFS.
</pre>
<h3>rw_read</h3>
<pre>
Verify traffic for file opened for read and write: reading file first.
</pre>
<h3>rw_write</h3>
<pre>
Verify traffic for file opened for read and write: writing file first.
</pre>
<h3>one_ds</h3>
<pre>
Verify client only connects to the DS with I/O.
</pre>
<h3>rsize</h3>
<pre>
Verify traffic for file using pNFS when mount option rsize &lt; 4096.
</pre>
<h3>wsize</h3>
<pre>
Verify traffic for file using pNFS when mount option wsize &lt; 4096.
</pre>
<h3>rwsize</h3>
<pre>
Verify traffic for file using pNFS when mount option rsize &lt; 4096 and wsize &lt; 4096.
</pre>
<h3>nfsvers</h3>
<pre>
Verify file created with pNFS is read correctly from different versions
of NFS. Also, verify files created with different versions of NFS are
read correctly from pNFS
</pre>
<h2>EXAMPLES</h2>
<p> The only required option is &#8211;server<br />
 $ nfstest_pnfs &#8211;server 192.168.0.11</p>
<h2>NOTES</h2>
<p> The user id in the local host must have access to run commands as root using the &#8216;sudo&#8217; command without the need for a password.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-nfstest-test_util/">nfstest.test_util</a>(3),</code> <code><a href="/docs/linux/man/1-nfstest_alloc/">nfstest_alloc</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_cache/">nfstest_cache</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_delegation/">nfstest_delegation</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_dio/">nfstest_dio</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_file/">nfstest_file</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_interop/">nfstest_interop</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_io/">nfstest_io</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_lock/">nfstest_lock</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pkt/">nfstest_pkt</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_posix/">nfstest_posix</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_sparse/">nfstest_sparse</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_xid/">nfstest_xid</a>(1),</code> <code><a href="/docs/linux/man/3-packet-nfs-nfs4_const/">packet.nfs.nfs4_const</a>(3)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
