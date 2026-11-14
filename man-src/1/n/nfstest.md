---
title: "nfstest(1)"
name: "nfstest"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfstest/"
description: "NFStest – NFS Test Suite"
---

<h2>NAME</h2>
<p> NFStest &#8211; NFS Test Suite</p>
<h2>DESCRIPTION</h2>
<p> Provides a set of tools for testing either the NFS client or the NFS server, included tests focused mainly on testing the client. These tools include the following:.SS Test utilities package (nfstest) Provides a set of tools for testing either the NFS client or the NFS server, most of the functionality is focused mainly on testing the client. These tools include the following: </p>
<p>&nbsp;<wbr>&#8211; Process command line arguments<br />
&nbsp;<wbr>&#8211; Provide functionality for PASS/FAIL<br />
&nbsp;<wbr>&#8211; Provide test grouping functionality<br />
&nbsp;<wbr>&#8211; Provide multiple client support<br />
&nbsp;<wbr>&#8211; Logging mechanism<br />
&nbsp;<wbr>&#8211; Debug info control<br />
&nbsp;<wbr>&#8211; Mount/Unmount control<br />
&nbsp;<wbr>&#8211; Create files/directories<br />
&nbsp;<wbr>&#8211; Provide mechanism to start a packet trace<br />
&nbsp;<wbr>&#8211; Provide mechanism to simulate a network partition<br />
&nbsp;<wbr>&#8211; Support for pNFS testing </p>
<h3>Packet trace package (packet)</h3>
<p> Testing NFS has mostly been done using test tools like connectathon test suite, filebench, iozone and others. But mostly using the connectathon test suite. These are good tools for testing, but they are outdated and they also cannot be used for testing pNFS thoroughly. </p>
<p> For example, you can run the connectathon test suite on pNFS, it runs, it passes all the tests &#8212; but how can we make sure that pNFS worked properly. How can we verify that a layout is granted, but not only that a layout is granted, what type of layout was granted (read, rw). Did the client sent IO to the data servers or to the metadata server. </p>
<p> The Packet trace module takes a trace file created by tcpdump and unpacks the contents of each packet. You can decode one packet at a time, or do a search for specific packets. The main difference between this modules and other tools used to decode trace files is that you can use this module to completely automate your tests. </p>
<p> How does it work? It opens the trace file and reads one record at a time keeping track where each record starts. This way, very large trace files can be opened without having to wait for the file to load and avoid loading the whole file into memory. </p>
<p> Packet layers supported:<br />
&nbsp;<wbr>&#8211; ETHERNET II&nbsp;<wbr>(RFC 894)<br />
&nbsp;<wbr>&#8211; IP layer&nbsp;<wbr>(supports IPv4 and IPv6)<br />
&nbsp;<wbr>&#8211; TCP layer<br />
&nbsp;<wbr>&#8211; UDP layer<br />
&nbsp;<wbr>&#8211; RPC layer<br />
&nbsp;<wbr>&#8211; NFS v4.0<br />
&nbsp;<wbr>&#8211; NFS v4.1 including pNFS file layouts<br />
&nbsp;<wbr>&#8211; NFS v4.2<br />
&nbsp;<wbr>&#8211; PORTMAP v2<br />
&nbsp;<wbr>&#8211; MOUNT v3<br />
&nbsp;<wbr>&#8211; NLM v4</p>
<h2>REQUIREMENTS AND LIMITATIONS</h2>
<p> In order to run the included tests, the user id in all the client hosts must have access to run commands as root using the &#8216;sudo&#8217; command without the need for a password, this includes the host where the test is being executed. This is used to run commands like &#8216;mount&#8217; and &#8216;umount&#8217;. Furthermore, the user id must be able to ssh to remote hosts without the need for a password if test requires the use of multiple clients. </p>
<p> Network partition is simulated by the use of &#8216;iptables&#8217;, please be advised that after every test is run the iptables is flushed and reset so any rules previously setup will be lost. Currently, there is no mechanism to restore the iptables rules to their original state.</p>
<h2>TESTS</h2>
<h3>nfstest_alloc</h3>
<pre><code>
Verify correct functionality of space reservations so applications are
able to reserve or unreserve space for a file. The system call fallocate
is used to manipulate the allocated disk space for a file, either to
preallocate or deallocate it. For filesystems which support the fallocate
system call, preallocation is done quickly by allocating blocks and
marking them as uninitialized, requiring no I/O to the data blocks.
This is much faster than creating a file and filling it with zeros.
Basic allocate tests verify the disk space is actually preallocated or
reserved for the given range by filling up the device after the allocation
and make sure data can be written to the allocated range without any
problems. Also, any data written outside the allocated range will fail
with NFS4ERR_NOSPC when there is no more space left on the device.
On the other hand, deallocating space will give the disk space back
so it can be used by either the same file on regions not already
preallocated or by different files without the risk of getting
a no space error.
Valid for NFSv4.2 and beyond
</code></pre>
<h3>nfstest_cache</h3>
<pre>
Verify consistency of attribute caching by varying acregmin, acregmax,
acdirmin, acdirmax and actimo. Verify consistency of data caching by varying
acregmin, acregmax, acdirmin, acdirmax and actimo.
Valid for any version of NFS
</pre>
<h3>nfstest_delegation</h3>
<pre>
Basic delegation tests verify that a correct delegation is granted when
opening a file for reading or writing. Also, another OPEN should not be
sent for the same file when the client is holding a delegation. Verify
that the stateid of all I/O operations should be the delegation stateid.
Reads from a different process on the same file should not cause the client
to send additional READ packets when the client is holding a read delegation.
Furthermore, a LOCK packet should not be sent to the server when the client
is holding a delegation.
Recall delegation tests verify the delegation is recalled when a conflicting
operation is sent to the server from a different client. Conflicting operations
are reading, writing and changing the permissions on the same file. Note, that
reading a file from a different client can only recall a read delegation.
Also, verify that a delegation is not recalled when a different client is
granted a read delegation. After a delegation is recalled, the client should
send an OPEN with CLAIM_DELEGATE_CUR before returning the delegation and the
stateid should be the same as the original OPEN stateid. Also, a delegation
should not be granted when re-opening the file right before returning
the delegation. Verify client flushes all written data before returning
the WRITE delegation. The LOCK should be sent as well right before returning
a delegation which has been recalled. A delegation should not be granted
on the second client who cause the delegation recall on the first client.
Valid for any version of NFS granting delegations
</pre>
<h3>nfstest_dio</h3>
<pre>
Functional direct I/O tests verify that every READ/WRITE is sent to the server
instead of the client caching the requests. Client bypasses read ahead by
sending the READ with only the requested bytes. Verify the client correctly
handles eof marker when reading the whole file. Verify client ignores delegation
while writing a file.
Direct I/O on pNFS tests verify the client sends the READ/WRITE to the correct
DS or the MDS if using a PAGESIZE aligned buffer or not, respectively.
Direct I/O data correctness tests verify that a file written with buffered I/O
is read correctly with direct I/O. Verify that a file written with direct I/O
is read correctly with buffered I/O.
Vectored I/O tests verify coalescence of multiple vectors into one READ/WRITE
packet when all vectors are PAGESIZE aligned. Vectors with different alignments
are sent on separate packets.
Valid for NFSv4.0 and NFSv4.1 including pNFS
</pre>
<h3>nfstest_interop</h3>
<pre>
Basic interoperability tests verify that a file written with different
versions of NFS is written correctly. The contents of the file are verified
by reading the file back using one of the NFS versions.
The tests append different data from different versions of NFS one at a
time then reads the contents of the file to verify it was written
correctly. This is done twice for each test.
</pre>
<h3>nfstest_lock</h3>
<p>Basic locking tests verify that a lock is granted using various arguments<br />
to fcntl. These include blocking and non-blocking locks, read or write locks,<br />
where the file is opened either for reading, writing or both. It also checks<br />
different ranges including limit conditions.<br />
Non-overlapping tests verity that locks are granted on both the client under<br />
test and a second process or a remote client when locking the same file.<br />
Overlapping tests verity that a lock is granted on the client under test<br />
and a second process or a remote client trying to lock the same file will<br />
be denied if a non-blocking lock is issue or will be blocked if a blocking<br />
lock is issue on the second process or remote client.<br />
Valid for any version of NFS</p>
<h3>nfstest_pnfs</h3>
<pre><code>
Verify basic pNFS functionality for file (both READ and WRITE), including
opening a second file within the same mount and having a lock on the file.
Also, verify basic pNFS functionality for a file opened for both READ and
WRITE while reading the file first and then writing to it or the other way
around by writing to the file fist and then reading the file. These tests
verify proper functionality of pNFS and NFSv4.1 as well:
    - Verify EXCHANGE_ID is sent to MDS
    - Verify CREATE_SESSION is sent to MDS
    - Verify LAYOUTGET is sent to MDS (check layout type, iomode, layout range)
    - Verify GETDEVICEINFO is sent to MDS
    - Verify EXCHANGE_ID is sent to the correct DS
    - Verify CREATE_SESSION is sent to DS
    - Verify READ/WRITE is sent to DS (check correct stateid, correct offset and size)
    - Verify no GETATTR is sent to DS
Only valid using NFSv4.1 with pNFS enabled and file layout type
</code></pre>
<h3>nfstest_posix</h3>
<pre>
Verify POSIX file system level access over the specified path using
positive and negative testing.
Valid for any version of NFS
</pre>
<h3>nfstest_sparse</h3>
<pre>
Verify correct functionality of sparse files. These are files which
have unallocated or uninitialized data blocks as holes. The new NFSv4.2
operation SEEK is used to search for the next hole or data segment
in a file.
Basic tests verify the SEEK operation returns the correct offset of the
next hole or data with respect to the starting offset given to the seek
system call. Verify the SEEK operation is sent to the server with the
correct stateid as a READ call. All files have a virtual hole at the
end of the file so when searching for the next hole, even if the file
does not have a hole, it returns the size of the file.
Valid for NFSv4.2 and beyond
</pre>
<h2>TOOLS</h2>
<h3>nfstest_io</h3>
<pre>
This I/O tool is used to create and manipulate files of different types.
The arguments allow running for a specified period of time as well as running
multiple processes. Each process modifies a single file at a time and the
file name space is different for each process so there are no collisions
between two different processes modifying the same file.
</pre>
<h3>nfstest_pkt</h3>
<pre>
Decode and display all packets in the packet trace file(s) given.
The match option gives the ability to search for specific packets within
the packet trace file. Other options allow displaying of their corresponding
call or reply when only one or the other is matched. Only a range of packets
can be displayed if the start and/or end options are used.
</pre>
<h3>nfstest_file</h3>
<pre>
Display all NFS packets for the specified path. It takes a relative path,
where it searches for each of the directory entries given in the path until
it gets the file handle for the directory where the file is located. Once the
directory file handle is found, a LOOKUP or OPEN/CREATE is searched for the
given file name. If the file lookup or creation is found, all file handles
and state ids associated with that file are searched and all packets found,
including their respective replies are displayed.
</pre>
<h3>nfstest_xid</h3>
<pre>
Search all the packet traces given for XID inconsistencies. Verify all
operations in the NFSv4.x COMPOUND reply are the same as the operations
given in the call.
Valid for packet traces with NFSv4 and above
</pre>
<h2>INSTALLATION</h2>
<p> 1. Install package using one of the following methods:<br />
a. Install the rpm as root:<br />
#&nbsp;<wbr>rpm -i NFStest-2.1-1.noarch.rpm </p>
<p>All manual pages are available<br />
$&nbsp;<wbr>man nfstest </p>
<p>Run tests:<br />
$&nbsp;<wbr>nfstest_pnfs &#8211;help </p>
<p>b. Untar the tarball:<br />
Get the latest tarball from&nbsp;<wbr><a rel="nofollow" href="http://wiki.linux-nfs.org/wiki/index.php/NFStest">http://wiki.linux-nfs.org/wiki/index.php/NFStest</a> </p>
<p>$&nbsp;<wbr>tar -zxvf NFStest-2.1.tar.gz </p>
<p>The tests can run without installation, just set the python path<br />
environment variable:<br />
$&nbsp;<wbr>cd NFStest-2.1<br />
$&nbsp;<wbr>export PYTHONPATH=$PWD<br />
$&nbsp;<wbr>cd test<br />
$&nbsp;<wbr>./nfstest_pnfs &#8211;help </p>
<p>Or install to standard python site-packages and executable directories:<br />
$&nbsp;<wbr>cd&nbsp;<wbr>~/NFStest-2.1<br />
$&nbsp;<wbr>sudo python setup.py install </p>
<p>All manual pages are available<br />
$&nbsp;<wbr>man nfstest </p>
<p>Run tests:<br />
$&nbsp;<wbr>nfstest_pnfs &#8211;help </p>
<p>c. Clone the git repository:<br />
$&nbsp;<wbr>cd&nbsp;<wbr>~<br />
$&nbsp;<wbr>git clone&nbsp;<wbr><a href="git://git.linux-nfs.org/projects/mora/nfstest.git">git://git.linux-nfs.org/projects/mora/nfstest.git</a> </p>
<p>The tests can run without installation, just set the python path<br />
environment variable:<br />
$&nbsp;<wbr>cd nfstest<br />
$&nbsp;<wbr>export PYTHONPATH=$PWD<br />
$&nbsp;<wbr>cd test<br />
$&nbsp;<wbr>./nfstest_pnfs &#8211;help </p>
<p>Or install to standard python site-packages and executable directories:<br />
$&nbsp;<wbr>cd&nbsp;<wbr>~/nfstest<br />
$&nbsp;<wbr>sudo python setup.py install </p>
<p>All manual pages are available<br />
$&nbsp;<wbr>man nfstest </p>
<p>Run tests:<br />
$&nbsp;<wbr>nfstest_pnfs &#8211;help </p>
<p> 2. Make sure user running the tests can run commands using &#8216;sudo&#8217; without<br />
the need for a password. </p>
<p> 3. Make sure user running the tests can run commands remotely using &#8216;ssh&#8217;<br />
without the need for a password. This is only needed for tests which<br />
require multiple clients. </p>
<p> 4. Create the mount point specified by the &#8211;mtpoint (default: /mnt/t) option<br />
on all the clients.<br />
$&nbsp;<wbr>sudo mkdir&nbsp;<wbr>/mnt/t<br />
$&nbsp;<wbr>sudo chmod 777&nbsp;<wbr>/mnt/t</p>
<h2>EXAMPLES</h2>
<p> The only required option is &#8211;server<br />
 $ nfstest_pnfs &#8211;server 192.168.0.11 </p>
<p> Required options are &#8211;server and &#8211;client<br />
 $ nfstest_cache &#8211;server 192.168.0.11 &#8211;client 192.168.0.20 </p>
<p> Testing with different values of &#8211;acmin and &#8211;acmax (this takes a long time)<br />
 $ nfstest_cache &#8211;server 192.168.0.11 &#8211;client 192.168.0.20 &#8211;acmin 10,20 &#8211;acmax 20,30,60,80 </p>
<p> The only required option is &#8211;server but only the basic delegation tests will be run. In order to run the recall tests the &#8211;client option must be used<br />
 $ nfstest_delegation &#8211;server 192.168.0.11 &#8211;client 192.168.0.20 </p>
<p> The only required option is &#8211;server<br />
 $ nfstest_dio &#8211;server 192.168.0.11 </p>
<p> The only required option is &#8211;server<br />
 $ nfstest_interop &#8211;server 192.168.0.11 </p>
<p> The only required option is &#8211;server but use the &#8211;client option to run the conflicting lock tests<br />
 $ nfstest_lock &#8211;server 192.168.0.11 &#8211;client 192.168.0.20 </p>
<p> The only required option is &#8211;server<br />
 $ nfstest_posix &#8211;server 192.168.0.11 </p>
<p> The only required option is &#8211;server<br />
 $ nfstest_alloc &#8211;server 192.168.0.11 </p>
<p> The only required option is &#8211;server<br />
 $ nfstest_sparse &#8211;server 192.168.0.11 </p>
<p> The only required option is &#8211;datadir (-d)<br />
 $ nfstest_io -d /mnt/t/data -v all -n 10 -r 3600 </p>
<p> Display all the NFS packets in the trace file<br />
 $ nfstest_pkt /tmp/trace.cap </p>
<p> Display all packets for the file name given The only required option is &#8211;path (-p)<br />
 $ nfstest_file -p f00000001 /tmp/trace.cap </p>
<p> Search the packet trace for XID inconsistencies<br />
 $ nfstest_xid /tmp/trace.cap</p>
<h2>USEFUL OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd> All tests have this option to display usage information and options available</p>
<dt>&#8211;createlog</p>
<dd> Create log file when specified</p>
<dt>&#8211;keeptraces</p>
<dd> Do not remove any trace files at the end of execution</p>
<dt>-v, &#8211;verbose &lt;none|opts|info|debug|all|intbitmask&gt;</p>
<dd> Verbose level for info/debug messages </p>
<p> Example:<br />
&nbsp;<wbr>$&nbsp;<wbr>nfstest_posix &#8211;server 192.168.0.11 &#8211;verbose all<br />
&nbsp;<wbr>$&nbsp;<wbr>nfstest_posix &#8211;server 192.168.0.11 &#8211;verbose 0x0F</p>
<dt>&#8211;runtest &lt;[^]testname1[,testname2[,&#8230;]]&gt;</p>
<dd> Comma separated list of tests to run, if the first character on the list is &#8216;^&#8217; then run all the tests except the ones listed. </p>
<p> Example:<br />
&nbsp;<wbr>Run only the access, chdir, creat and fcntl tests<br />
&nbsp;<wbr>$&nbsp;<wbr>nfstest_posix &#8211;server 192.168.0.11 &#8211;runtest access,chdir,creat,fcntl </p>
<p>&nbsp;<wbr>Run all the tests except for open and chmod<br />
&nbsp;<wbr>$&nbsp;<wbr>nfstest_posix &#8211;server 192.168.0.11 &#8211;runtest&nbsp;<wbr>^open,chmod</p>
<dt>&#8211;tverbose &lt;group|normal|verbose&gt;</p>
<dd> Verbose level for test messages (default: normal) When tverbose=group, only the test groups are displayed as PASS if all the tests in the group passed, otherwise it will FAIL. In some of the tests tverbose could be &#8216;verbose&#8217; for a greater level of verbosity in which a particular test have many sub-tests (&gt;100) </p>
<p> Example:<br />
&nbsp;<wbr>$&nbsp;<wbr>nfstest_posix &#8211;server 192.168.0.11<br />
&nbsp;<wbr>***&nbsp;<wbr>Verify POSIX API access()&nbsp;<wbr>on NFSv4<br />
&nbsp;<wbr>&nbsp;<wbr>PASS: access &#8211; file access allowed with mode F_OK<br />
&nbsp;<wbr>&nbsp;<wbr>PASS: access &#8211; file access not allowed with mode F_OK for a non-existent file<br />
&nbsp;<wbr>&nbsp;<wbr>PASS: access &#8211; file access allowed with mode R_OK for file with permissions 0777<br />
&nbsp;<wbr>&nbsp;<wbr>PASS: access &#8211; file access allowed with mode W_OK for file with permissions 0777<br />
&nbsp;<wbr>&nbsp;<wbr>PASS: access &#8211; file access allowed with mode X_OK for file with permissions 0777<br />
&nbsp;<wbr>&nbsp;<wbr>&#8230; </p>
<p>&nbsp;<wbr>$&nbsp;<wbr>nfstest_posix &#8211;server 192.168.0.11 &#8211;tverbose group<br />
&nbsp;<wbr>&nbsp;<wbr>PASS: Verify POSIX API access()&nbsp;<wbr>on NFSv4&nbsp;<wbr>(58 passed, 0 failed)</p>
<dt>&#8211;bugmsgs &lt;filename&gt;</p>
<dd> File containing test messages to mark as bugs if they failed. When at least one of the tests fails the exit code is set to 1. When this option is specified, all known bugs are not counted as failures so the whole test execution is not failed. If the known bugs actually passed, using this option will fail the test to let the user know that the bug has been fixed.</p>
<dt>&#8211;ignore</p>
<dd> Ignore all bugs given by bugmsgs. If this option is specified all failures given by bugmsgs are ignored. On the other hand, if a test passes which is marked as a bug, using this option the test will not failed as when using the bugmsgs option alone.</p>
<dt>&#8211;nfsdebug &lt;flags&gt;</p>
<dd> Set NFS kernel debug flags and save log messages. Use any of the valid flags given for module &#8216;nfs&#8217; on command &#8216;rpcdebug&#8217;.</p>
<dt>&#8211;rpcdebug &lt;flags&gt;</p>
<dd> Set RPC kernel debug flags and save log messages. Use any of the valid flags given for module &#8216;rpc&#8217; on command &#8216;rpcdebug&#8217;.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nfstest_alloc/">nfstest_alloc</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_cache/">nfstest_cache</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_delegation/">nfstest_delegation</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_dio/">nfstest_dio</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_file/">nfstest_file</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_interop/">nfstest_interop</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_io/">nfstest_io</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_lock/">nfstest_lock</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pkt/">nfstest_pkt</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pnfs/">nfstest_pnfs</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_posix/">nfstest_posix</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_sparse/">nfstest_sparse</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_xid/">nfstest_xid</a>(1)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
