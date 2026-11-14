---
title: "nfstest_lock(1)"
name: "nfstest_lock"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfstest_lock/"
description: "nfstest_lock – Locking tests"
---

<h2>NAME</h2>
<p> nfstest_lock &#8211; Locking tests</p>
<h2>SYNOPSIS</h2>
<p> nfstest_lock &#8211;server &lt;server&gt; [&#8211;client &lt;client&gt;] [options]</p>
<h2>DESCRIPTION</h2>
<p> Basic locking tests verify that a lock is granted using various arguments to fcntl. These include blocking and non-blocking locks, read or write locks, where the file is opened either for reading, writing or both. It also checks different ranges including limit conditions. </p>
<p> Non-overlapping tests verity that locks are granted on both the client under test and a second process or a remote client when locking the same file. </p>
<p> Overlapping tests verity that a lock is granted on the client under test and a second process or a remote client trying to lock the same file will be denied if a non-blocking lock is issue or will be blocked if a blocking lock is issue on the second process or remote client. </p>
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
<dd> Device interface [default: automatically selected]</p>
<dt>&#8211;subtraces</p>
<dd> Create a packet trace for each sub-test. Use it with caution since it will create a lot of packet traces. Use &#8211;createtraces instead unless trying to get a packet trace for a specific sub-test. Best if it is used in combination with the &#8211;runtest option. </p>
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
<dt>&#8211;client=CLIENT</p>
<dd> Remote NFS client used for conflicting lock tests</p>
<dt>&#8211;offset=OFFSET</p>
<dd> Offset of first lock granted [default: 4096]</p>
<dt>&#8211;length=LENGTH</p>
<dd> Length of first lock granted [default: 4096]</p>
<dt>&#8211;unlock-delay=UNLOCK_DELAY</p>
<dd> Time in seconds to unlock first lock [default: 2.0]</p>
<dt>&#8211;lockw-timeout=LOCKW_TIMEOUT</p>
<dd> Time in seconds to wait for blocked lock after conflicting lock has been released [default: 30]</p>
<dt>&#8211;opentype=OPENTYPE</p>
<dd> List of open types to test [default: read,write,rdwr]</p>
<dt>&#8211;locktype=LOCKTYPE</p>
<dd> List of lock types to test [default: read,write]</p>
<dt>&#8211;opentype2=OPENTYPE2</p>
<dd> List of open types to test on remote client [default: read,write,rdwr]</p>
<dt>&#8211;locktype2=LOCKTYPE2</p>
<dd> List of lock types to test on remote client [default: read,write]</p>
<dt>&#8211;setlock=SETLOCK</p>
<dd> List of set lock types to test [default: immediate,block]</dl>
<h2>TESTS</h2>
<h3>btest01</h3>
<pre>
Basic locking tests
These tests verify that a lock is granted using various arguments
to fcntl. These include blocking and non-blocking locks, read or
write locks, where the file is opened either for reading, writing
or both. It also checks different ranges including limit conditions.
</pre>
<h3>noverlap</h3>
<pre>
Run all non-overlapping locking tests: nptest01, nptest02, nptest03,
nptest04, nctest01, nctest02, nctest03, nctest04
</pre>
<h3>nptest</h3>
<pre>
Run all non-overlapping locking tests using a second process: nptest01,
nptest02, nptest03, nptest04
</pre>
<h3>nptest01</h3>
<pre><code>
Locking non - overlapping range from a second process where end2 &lt; start1
                                                                       process1 : |
                                                                                  -- -- -- -- -- -- -- -- -- |
                                                                                  process2 : | -- -- -- -- |
</code></pre>
<h3>nptest02</h3>
<p>Locking non &#8211; overlapping range from a second process where end2 == start1 &#8211; 1 process1 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                                          process2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>nptest03</h3>
<p>Locking non &#8211; overlapping range from a second process where start2 &gt; end1<br />
                                                                         process1 : |<br />
                                                                                    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                                    process2 : | &#8212; &#8212; &#8212; &#8212; |</p>
<h3>nptest04</h3>
<p>Locking non &#8211; overlapping range from a second process where start2 == end1 + 1 process1 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                                          process2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>nctest</h3>
<pre>
Run all non-overlapping locking tests using a second client: nctest01,
nctest02, nctest03, nctest04
</pre>
<h3>nctest01</h3>
<p>Locking non &#8211; overlapping range from a second client where end2 &lt; start1<br />
                                                                      client1 : |<br />
                                                                                &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                                client2 : | &#8212; &#8212; &#8212; &#8212; |</p>
<h3>nctest02</h3>
<p>Locking non &#8211; overlapping range from a second client where end2 == start1 &#8211; 1 client1 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                                        client2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>nctest03</h3>
<p>Locking non &#8211; overlapping range from a second client where start2 &gt; end1<br />
                                                                        client1 : |<br />
                                                                                  &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                                  client2 : | &#8212; &#8212; &#8212; &#8212; |</p>
<h3>nctest04</h3>
<p>Locking non &#8211; overlapping range from a second client where start2 == end1 + 1 client1 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                                        client2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>overlap</h3>
<pre>
Run all overlapping locking tests: optest01, optest02, optest03,
optest04, optest05, optest06, optest07, optest08, octest01, octest02,
octest03, octest04, octest05, octest06, octest07, octest08
</pre>
<h3>optest</h3>
<pre>
Run all overlapping locking tests using a second process: optest01,
optest02, optest03, optest04, optest05, optest06, optest07, optest08
</pre>
<h3>optest01</h3>
<p>Locking same range from a second process<br />
        process1 : |<br />
                   &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                   process2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>optest02</h3>
<p>Locking overlapping range from a second process where start2 &lt; start1<br />
                                                                   process1 : |<br />
                                                                              &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                              process2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>optest03</h3>
<p>Locking overlapping range from a second process where end2 &gt; end1<br />
                                                                 process1 : |<br />
                                                                            &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                            process2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>optest04</h3>
<p>Locking overlapping range from a second process where range2 is entirely within range1<br />
        process1 : |<br />
                   &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                   process2 : | &#8212; &#8212; &#8212; &#8212; |</p>
<h3>optest05</h3>
<p>Locking overlapping range from a second process where range1 is entirely within range2<br />
        process1 : |<br />
                   &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                   process2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>optest06</h3>
<pre>
Locking full file range from a second process
</pre>
<h3>optest07</h3>
<p>Locking overlapping range from a second process where end2 == start1<br />
                                                                  process1 : |<br />
                                                                             &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                             process2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>optest08</h3>
<p>Locking overlapping range from a second process where start2 == end1<br />
                                                                    process1 : |<br />
                                                                               &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                               process2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>octest</h3>
<pre>
Run all overlapping locking tests using a second client: octest01,
octest02, octest03, octest04, octest05, octest06, octest07, octest08
</pre>
<h3>octest01</h3>
<p>Locking same range from a second client<br />
        client1 : |<br />
                  &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                  client2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>octest02</h3>
<p>Locking overlapping range from a second client where start2 &lt; start1<br />
                                                                  client1 : |<br />
                                                                            &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                            client2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>octest03</h3>
<p>Locking overlapping range from a second client where end2 &gt; end1<br />
                                                                client1 : |<br />
                                                                          &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                          client2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>octest04</h3>
<p>Locking overlapping range from a second client where range2 is entirely within range1<br />
        client1 : |<br />
                  &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                  client2 : | &#8212; &#8212; &#8212; &#8212; |</p>
<h3>octest05</h3>
<p>Locking overlapping range from a second client where range1 is entirely within range2<br />
        client1 : |<br />
                  &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                  client2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>octest06</h3>
<pre>
Locking full file range from a second client
</pre>
<h3>octest07</h3>
<p>Locking overlapping range from a second client where end2 == start1<br />
                                                                 client1 : |<br />
                                                                           &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |<br />
                                                                           client2 : | &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; |</p>
<h3>octest08</h3>
<pre><code>
Locking overlapping range from a second client where start2 == end1
                                                                   client1 : |
                                                                             -- -- -- -- -- -- -- -- -- |
                                                                             client2 : | -- -- -- -- -- -- -- -- -- |
</code></pre>
<h2>NOTES</h2>
<p> The user id in the local host and the host specified by &#8211;client must have access to run commands as root using the &#8216;sudo&#8217; command without the need for a password. </p>
<p> The user id must be able to &#8216;ssh&#8217; to remote host without the need for a password.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-nfstest-rexec/">nfstest.rexec</a>(3),</code> <code><a href="/docs/linux/man/3-nfstest-test_util/">nfstest.test_util</a>(3),</code> <code><a href="/docs/linux/man/1-nfstest_alloc/">nfstest_alloc</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_cache/">nfstest_cache</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_delegation/">nfstest_delegation</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_dio/">nfstest_dio</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_file/">nfstest_file</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_interop/">nfstest_interop</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_io/">nfstest_io</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pkt/">nfstest_pkt</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pnfs/">nfstest_pnfs</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_posix/">nfstest_posix</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_sparse/">nfstest_sparse</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_xid/">nfstest_xid</a>(1)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
