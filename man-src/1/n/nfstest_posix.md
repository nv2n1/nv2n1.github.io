---
title: "nfstest_posix(1)"
name: "nfstest_posix"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfstest_posix/"
description: "nfstest_posix – POSIX file system level access tests"
---

<h2>NAME</h2>
<p> nfstest_posix &#8211; POSIX file system level access tests</p>
<h2>SYNOPSIS</h2>
<p> nfstest_posix &#8211;server &lt;server&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> Verify POSIX file system level access over the specified path using positive and negative testing. </p>
<p> Valid for any version of NFS. </p>
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
<h3>access</h3>
<pre>
Verify POSIX API access() on files with different modes.
</pre>
<h3>chdir</h3>
<pre>
Verify POSIX API chdir() by changing to a newly created directory
and then by changing back to the original directory.
</pre>
<h3>close</h3>
<pre>
Verify POSIX API close() works and that writing to a closed file
descriptor returns an error.
</pre>
<h3>closedir</h3>
<pre>
Verify POSIX API closedir() works and that reading to a closed file
descriptor returns an error.
</pre>
<h3>creat</h3>
<pre>
Verify POSIX API creat(path, mode) is equivalent to
open(path, O_WRONLY|O_CREAT|O_TRUNC, mode). First test with a path
that does not exist to verify the file was created and then test
with a path that does exist to verify that the file is truncated.
</pre>
<h3>fcntl</h3>
<pre>
Verify the POSIX API fcntl() commands F_DUPFD, F_GETFD, F_SETFD,
F_GETFL, F_SETFL, and FD_CLOEXEC. The F_DUPFD command is tested
by performing operations on the original and dupped file descriptor
to ensure they behave correctly. The F_GETFD and F_SETFD commands
are tested by setting the FD_CLOEXEC flag and making sure it gets set.
The F_GETFL and F_SETFL commands are tested by setting the O_APPEND
flag and making sure it gets set.
Run the test for both 'read' and 'write'.
</pre>
<h3>fdatasync</h3>
<pre>
Verify POSIX API fdatasync().
</pre>
<h3>fstat</h3>
<pre>
Verify POSIX API fstat() by checking the mode on a file and that
it returns the expected structure members. Create a symlink and
verify that fstat returns information about the link.
</pre>
<h3>fstatvfs</h3>
<pre>
Verify POSIX API fstatvfs() by making sure all the members of the
structure are returned.
</pre>
<h3>fsync</h3>
<pre>
Verify POSIX API fsync().
</pre>
<h3>link</h3>
<pre>
Verify POSIX API link(src, dst) creates a link and updates
st_ctime field for the file. Verify that link updates the
st_ctime and st_mtime for the directory. Verify st_link count
incremented by 1 for the file.
</pre>
<h3>lseek</h3>
<pre>
Verify POSIX API lseek() with different offsets and whence
values including seeking past the end of the file.
</pre>
<h3>lstat</h3>
<pre>
Verify POSIX API lstat() by checking the mode on a file and that
it returns the expected structure members. Create a symlink and
verify that lstat returns information about the link.
</pre>
<h3>mkdir</h3>
<pre>
Verify POSIX API mkdir(). Verify that mkdir with a path of a symbolic
link fails. Verify that the st_ctime and st_mtime fields of the
parent directory are updated.
</pre>
<h3>mmap</h3>
<pre>
Verify POSIX API mmap() by mapping a file and verifying I/O
operations. Verify mmap followed by memory read of existing
file works. Verify mmap followed by memory write to file works.
</pre>
<h3>munmap</h3>
<pre>
Verify POSIX API munmap() by mapping a file and then unmapping
the file.
</pre>
<h3>opendir</h3>
<pre>
Verify POSIX API opendir() on a directory.
</pre>
<h3>read</h3>
<pre>
Verify POSIX API read() by reading data from a file. Verify that
the st_atime of the file is updated after the read. Verify a read
of 0 bytes returns 0.
</pre>
<h3>readdir</h3>
<pre>
Verify POSIX API readdir() on a directory.
</pre>
<h3>readlink</h3>
<pre>
Verify Test POSIX API readlink() by reading a symbolic link.
</pre>
<h3>rename</h3>
<pre>
Verify POSIX API rename() by renaming a file, directory, and a
symbolic link. Verify that a rename from a file to a symbolic
link will cause the symbolic link to be removed.
</pre>
<h3>rewinddir</h3>
<pre>
Verify POSIX API rewinddir() on a directory.
</pre>
<h3>rmdir</h3>
<pre>
Verify POSIX API rmdir() by removing a directory. Verify that the
parent's st_ctime and st_mtime are updated.
</pre>
<h3>seekdir</h3>
<pre>
Verify POSIX API seekdir() on a directory.
</pre>
<h3>stat</h3>
<pre>
Verify POSIX API stat() by checking the mode on a file and that
it returns the expected structure members. Create a symlink and
verify that stat returns information about the file.
</pre>
<h3>statvfs</h3>
<pre>
Verify POSIX API statvfs() by making sure all the members of the
structure are returned.
</pre>
<h3>symlink</h3>
<pre>
Verify POSIX API symlink() by creating a symbolic link and verify
that the file type is slnk.
</pre>
<h3>sync</h3>
<pre>
Verify POSIX API sync().
</pre>
<h3>telldir</h3>
<pre>
Verify POSIX API telldir() on a directory.
</pre>
<h3>unlink</h3>
<pre>
Verify POSIX API unlink() by unlinking a file and verify that it
was removed. Verify that the st_ctime and st_mtime fields of the
parent directory were updated. Then unlink a symbolic link and
verify that the symbolic link was removed but not the referenced
file. Then remove an opened file and verify that I/O still occurs
to the file after the unlink and that the file gets removed when
the file is closed. Create a file and then hard link to it so the
link count is greater than 1. Unlink the hard file and verify that
st_ctime field is updated.
</pre>
<h3>write</h3>
<pre>
Verify POSIX API write() by writing 0 bytes and verifying 0
is returned. Write a pattern the file, seek +N, write another
pattern, and close the file. Open the file and read in both
written patterns and verify that it is the correct pattern.
Read in the data from the hole in the file and verify that it is 0.
</pre>
<h3>open</h3>
<pre>
Verify POSIX API open() on a file. Verify file creation using
the O_CREAT flag and verifying the file mode is set to the
specified value. Verify the st_ctime and st_mtime are updated
on the parent directory after the file was created. Verify open
on existing file fails with the O_EXCL flag set. Verify write
succeeds and read fails if file was open with O_WRONLY. Verify
read succeeds and write fails if file was open with O_RDONLY.
Verify that all writes with O_APPEND set are to the end of the file.
Use O_DSYNC, O_RSYNC, and O_SYNC flags in open calls.
Verify file open with O_CREAT and O_TRUNC set will truncate an
existing file. Verify that it updates the file st_ctime and st_mtime.
</pre>
<h3>chmod</h3>
<pre>
Verify POSIX API chmod() on a file and directory by trying all valid
combinations of modes. Verify that the st_ctime files is updated
for both the file and directory.
</pre>
<h2>EXAMPLES</h2>
<p> The only required option is &#8211;server<br />
 $ nfstest_posix &#8211;server 192.168.0.11</p>
<h2>NOTES</h2>
<p> The user id in the local host must have access to run commands as root using the &#8216;sudo&#8217; command without the need for a password.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-nfstest-test_util/">nfstest.test_util</a>(3),</code> <code><a href="/docs/linux/man/1-nfstest_alloc/">nfstest_alloc</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_cache/">nfstest_cache</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_delegation/">nfstest_delegation</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_dio/">nfstest_dio</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_file/">nfstest_file</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_interop/">nfstest_interop</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_io/">nfstest_io</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_lock/">nfstest_lock</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pkt/">nfstest_pkt</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pnfs/">nfstest_pnfs</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_sparse/">nfstest_sparse</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_xid/">nfstest_xid</a>(1)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
