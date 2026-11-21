---
title: "nfstest_cache(1)"
name: "nfstest_cache"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfstest_cache/"
description: "nfstest_cache – NFS client side caching tests"
---

<h2>NAME</h2>
<p> nfstest_cache &#8211; NFS client side caching tests</p>
<h2>SYNOPSIS</h2>
<p> nfstest_cache &#8211;server &lt;server&gt; &#8211;client &lt;client&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> Verify consistency of attribute caching by varying acregmin, acregmax, acdirmin, acdirmax and actimo. Verify consistency of data caching by varying acregmin, acregmax, acdirmin, acdirmax and actimo. </p>
<p> Valid for any version of NFS. </p>
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
<dd> Mount options [default: &#8216;hard,rsize=4096,wsize=4096&#8217;]</dd>
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
<dd> File size to use for test files [default: 32]</dd>
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
<dt>&#8211;client=CLIENT</dt>
<dd> Remote NFS client</dd>
<dt>&#8211;justbefore=JUSTBEFORE</dt>
<dd> Time in seconds to test a condition just before it is expected to come true [default: 2]</dd>
<dt>&#8211;acmin=ACMIN</dt>
<dd> Comma separated values to use for acregmin/acdirmin/actimeo [default: 10]</dd>
<dt>&#8211;acmax=ACMAX</dt>
<dd> Comma separated values to use for acregmax/acdirmax, first value of acmin will be used as acregmin/acdirmin [default: 20]</dd></dl>
<h2>TESTS</h2>
<h3>acregmin_attr</h3>
<pre>
Verify consistency of attribute caching by varying the
acregmin NFS option.
The cached information is assumed to be valid for attrtimeo
which starts at acregmin.
</pre>
<h3>acregmax_attr</h3>
<pre>
Verify consistency of attribute caching by varying the
acregmax NFS option.
The cached information is assumed to be valid for attrtimeo which
starts at acregmin. An attribute revalidation to the server
that shows no attribute change doubles attrtimeo up to acregmax.
An attribute revalidation to the server that shows a change has
occurred resets it to acregmin.
</pre>
<h3>acdirmin_attr</h3>
<pre>
Verify consistency of attribute caching by varying the
acdirmin NFS option.
The cached information is assumed to be valid for attrtimeo
which starts at acdirmin. Test that this is so.
</pre>
<h3>acdirmax_attr</h3>
<pre>
Verify consistency of attribute caching by varying the
acdirmax NFS option.
The cached information is assumed to be valid for attrtimeo which
starts at acdirmin. An attribute revalidation to the server
that shows no attribute change doubles attrtimeo up to acdirmax.
An attribute revalidation to the server that shows a change has
occurred resets it to acdirmin.
</pre>
<h3>actimeo_attr</h3>
<pre>
Verify consistency of attribute caching by varying the
actimeo NFS option.
The cached information is assumed to be valid for attrtimeo
which starts and ends at actimeo.
</pre>
<h3>acregmin_data</h3>
<pre>
Verify consistency of data caching by varying the
acregmin NFS option.
</pre>
<h3>acregmax_data</h3>
<pre>
Verify consistency of data caching by varying the
acregmax NFS option.
The cached information is assumed to be valid for attrtimeo which
starts at acregmin. An attribute revalidation to the server
that shows no attribute change doubles attrtimeo up to acregmax.
An attribute revalidation to the server that shows a change has
occurred resets it to acregmin.
</pre>
<h3>acdirmin_data</h3>
<pre>
Verify consistency of data caching by varying the
acdirmin NFS option.
The cached information is assumed to be valid for attrtimeo
which starts at acdirmin. Test that this is so.
</pre>
<h3>acdirmax_data</h3>
<pre>
Verify consistency of data caching by varying the
acdirmax NFS option.
The cached information is assumed to be valid for attrtimeo which
starts at acdirmin. An attribute revalidation to the server
that shows no attribute change doubles attrtimeo up to acdirmax.
An attribute revalidation to the server that shows a change has
occurred resets it to acdirmin.
</pre>
<h3>actimeo_data</h3>
<pre>
Verify consistency of data caching by varying the
actimeo NFS option.
The cached information is assumed to be valid for attrtimeo
which starts and ends at actimeo.
</pre>
<h2>EXAMPLES</h2>
<p> Required options are &#8211;server and &#8211;client<br />
 $ nfstest_cache &#8211;server 192.168.0.11 &#8211;client 192.168.0.20 </p>
<p> Testing with different values of &#8211;acmin and &#8211;acmax (this takes a long time)<br />
 $ nfstest_cache &#8211;server 192.168.0.11 &#8211;client 192.168.0.20 &#8211;acmin 10,20 &#8211;acmax 20,30,60,80</p>
<h2>NOTES</h2>
<p> The user id in the local host and the host specified by &#8211;client must have access to run commands as root using the &#8216;sudo&#8217; command without the need for a password. </p>
<p> The user id must be able to &#8216;ssh&#8217; to remote host without the need for a password.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-nfstest-test_util/">nfstest.test_util</a>(3),</code> <code><a href="/docs/linux/man/1-nfstest_alloc/">nfstest_alloc</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_delegation/">nfstest_delegation</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_dio/">nfstest_dio</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_file/">nfstest_file</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_interop/">nfstest_interop</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_io/">nfstest_io</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_lock/">nfstest_lock</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pkt/">nfstest_pkt</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pnfs/">nfstest_pnfs</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_posix/">nfstest_posix</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_sparse/">nfstest_sparse</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_xid/">nfstest_xid</a>(1)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
