---
title: "nfstest_io(1)"
name: "nfstest_io"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfstest_io/"
description: "nfstest_io – I/O tool"
---

<h2>NAME</h2>
<p> nfstest_io &#8211; I/O tool</p>
<h2>SYNOPSIS</h2>
<p> nfstest_io -d &lt;datadir&gt; [options]</p>
<h2>DESCRIPTION</h2>
<p> This I/O tool is used to create and manipulate files of different types. The arguments allow running for a specified period of time as well as running multiple processes. Each process modifies a single file at a time and the file name space is different for each process so there are no collisions between two different processes modifying the same file. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;version</p>
<dd> show program&#8217;s version number and exit</p>
<dt>-h, &#8211;help</p>
<dd> show this help message and exit</p>
<dt>-d DATADIR, &#8211;datadir=DATADIR</p>
<dd> Top level directory where files will be created, it will be created if it does not exist</p>
<dt>-s SEED, &#8211;seed=SEED</p>
<dd> Seed to initialized the random number generator [default: automatically generated]</p>
<dt>-n NPROCS, &#8211;nprocs=NPROCS</p>
<dd> Number of processes to use [default: 1]</p>
<dt>-r RUNTIME, &#8211;runtime=RUNTIME</p>
<dd> Run time [default: &#8216;0&#8217;]</p>
<dt>-v VERBOSE, &#8211;verbose=VERBOSE</p>
<dd> Verbose level: none|info|debug|dbg1-7|all [default: &#8216;none&#8217;]</p>
<dt>-e, &#8211;exiterr</p>
<dd> Exit on first error </p>
</dl>
<h3>Read and write:</h3>
<dl>
<dt>&#8211;read=READ</p>
<dd> Read file percentage [default: 40]</p>
<dt>&#8211;write=WRITE</p>
<dd> Write file percentage [default: 40]</p>
<dt>&#8211;rdwr=RDWR</p>
<dd> Read/write file percentage [default: 20]</p>
<dt>&#8211;randio=RANDIO</p>
<dd> Random file access percentage [default: 50]</p>
<dt>&#8211;iodelay=IODELAY</p>
<dd> Seconds to delay I/O operations [default: 0.0]</p>
<dt>&#8211;direct</p>
<dd> Use direct I/O</p>
<dt>&#8211;rdwronly</p>
<dd> Use read and write only, no rename, remove, etc. </p>
</dl>
<h3>File operations:</h3>
<dl>
<dt>&#8211;create=CREATE</p>
<dd> Create file percentage [default: 5]</p>
<dt>&#8211;odgrade=ODGRADE</p>
<dd> Open downgrade percentage [default: 10]</p>
<dt>&#8211;osync=OSYNC</p>
<dd> Open file with O_SYNC [default: 20]</p>
<dt>&#8211;fsync=FSYNC</p>
<dd> Percentage of fsync after write [default: 5]</p>
<dt>&#8211;rename=RENAME</p>
<dd> Rename file percentage [default: 5]</p>
<dt>&#8211;remove=REMOVE</p>
<dd> Remove file percentage [default: 5]</p>
<dt>&#8211;trunc=TRUNC</p>
<dd> Truncate file percentage [default: 5]</p>
<dt>&#8211;ftrunc=FTRUNC</p>
<dd> Truncate opened file percentage [default: 5]</p>
<dt>&#8211;link=LINK</p>
<dd> Create hard link percentage [default: 2]</p>
<dt>&#8211;slink=SLINK</p>
<dd> Create symbolic link percentage [default: 1]</p>
<dt>&#8211;readdir=READDIR</p>
<dd> List contents of directory percentage [default: 1]</p>
<dt>&#8211;lock=LOCK</p>
<dd> Lock file percentage [default: 20]</p>
<dt>&#8211;unlock=UNLOCK</p>
<dd> Unlock file percentage [default: 80]</p>
<dt>&#8211;tlock=TLOCK</p>
<dd> Lock test percentage [default: 50]</p>
<dt>&#8211;lockfull=LOCKFULL</p>
<dd> Lock full file percentage [default: 50]</p>
<dt>&#8211;minfiles=MINFILES</p>
<dd> Mininum number of files to create before any file operation is executed [default: 10] </p>
</dl>
<h3>File size options:</h3>
<dl>
<dt>&#8211;fsizeavg=FSIZEAVG</p>
<dd> File size average [default: 1m]</p>
<dt>&#8211;fsizedev=FSIZEDEV</p>
<dd> File size standard deviation [default: 256k]</p>
<dt>&#8211;rsize=RSIZE</p>
<dd> Read block size [default: 64k]</p>
<dt>&#8211;rsizedev=RSIZEDEV</p>
<dd> Read block size standard deviation [default: 8k]</p>
<dt>&#8211;wsize=WSIZE</p>
<dd> Write block size [default: 64k]</p>
<dt>&#8211;wsizedev=WSIZEDEV</p>
<dd> Write block size standard deviation [default: 8k]</p>
<dt>&#8211;sizemult=SIZEMULT</p>
<dd> Size multiplier [default: 1] </p>
</dl>
<h3>Logging options:</h3>
<dl>
<dt>&#8211;createlog</p>
<dd> Create log file</p>
<dt>&#8211;createlogs</p>
<dd> Create a log file for each process</p>
<dt>&#8211;logdir=LOGDIR</p>
<dd> Log directory [default: &#8216;/tmp&#8217;]</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-nfstest-file_io/">nfstest.file_io</a>(3),</code> <code><a href="/docs/linux/man/1-nfstest_alloc/">nfstest_alloc</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_cache/">nfstest_cache</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_delegation/">nfstest_delegation</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_dio/">nfstest_dio</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_file/">nfstest_file</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_interop/">nfstest_interop</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_lock/">nfstest_lock</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pkt/">nfstest_pkt</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pnfs/">nfstest_pnfs</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_posix/">nfstest_posix</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_sparse/">nfstest_sparse</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_xid/">nfstest_xid</a>(1)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
