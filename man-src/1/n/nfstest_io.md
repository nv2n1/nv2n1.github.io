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
<dt>&#8211;version</dt>
<dd> show program&#8217;s version number and exit</dd>
<dt>-h, &#8211;help</dt>
<dd> show this help message and exit</dd>
<dt>-d DATADIR, &#8211;datadir=DATADIR</dt>
<dd> Top level directory where files will be created, it will be created if it does not exist</dd>
<dt>-s SEED, &#8211;seed=SEED</dt>
<dd> Seed to initialized the random number generator [default: automatically generated]</dd>
<dt>-n NPROCS, &#8211;nprocs=NPROCS</dt>
<dd> Number of processes to use [default: 1]</dd>
<dt>-r RUNTIME, &#8211;runtime=RUNTIME</dt>
<dd> Run time [default: &#8216;0&#8217;]</dd>
<dt>-v VERBOSE, &#8211;verbose=VERBOSE</dt>
<dd> Verbose level: none|info|debug|dbg1-7|all [default: &#8216;none&#8217;]</dd>
<dt>-e, &#8211;exiterr</dt>
<dd> Exit on first error </dd>
</dl>
<h3>Read and write:</h3>
<dl>
<dt>&#8211;read=READ</dt>
<dd> Read file percentage [default: 40]</dd>
<dt>&#8211;write=WRITE</dt>
<dd> Write file percentage [default: 40]</dd>
<dt>&#8211;rdwr=RDWR</dt>
<dd> Read/write file percentage [default: 20]</dd>
<dt>&#8211;randio=RANDIO</dt>
<dd> Random file access percentage [default: 50]</dd>
<dt>&#8211;iodelay=IODELAY</dt>
<dd> Seconds to delay I/O operations [default: 0.0]</dd>
<dt>&#8211;direct</dt>
<dd> Use direct I/O</dd>
<dt>&#8211;rdwronly</dt>
<dd> Use read and write only, no rename, remove, etc. </dd>
</dl>
<h3>File operations:</h3>
<dl>
<dt>&#8211;create=CREATE</dt>
<dd> Create file percentage [default: 5]</dd>
<dt>&#8211;odgrade=ODGRADE</dt>
<dd> Open downgrade percentage [default: 10]</dd>
<dt>&#8211;osync=OSYNC</dt>
<dd> Open file with O_SYNC [default: 20]</dd>
<dt>&#8211;fsync=FSYNC</dt>
<dd> Percentage of fsync after write [default: 5]</dd>
<dt>&#8211;rename=RENAME</dt>
<dd> Rename file percentage [default: 5]</dd>
<dt>&#8211;remove=REMOVE</dt>
<dd> Remove file percentage [default: 5]</dd>
<dt>&#8211;trunc=TRUNC</dt>
<dd> Truncate file percentage [default: 5]</dd>
<dt>&#8211;ftrunc=FTRUNC</dt>
<dd> Truncate opened file percentage [default: 5]</dd>
<dt>&#8211;link=LINK</dt>
<dd> Create hard link percentage [default: 2]</dd>
<dt>&#8211;slink=SLINK</dt>
<dd> Create symbolic link percentage [default: 1]</dd>
<dt>&#8211;readdir=READDIR</dt>
<dd> List contents of directory percentage [default: 1]</dd>
<dt>&#8211;lock=LOCK</dt>
<dd> Lock file percentage [default: 20]</dd>
<dt>&#8211;unlock=UNLOCK</dt>
<dd> Unlock file percentage [default: 80]</dd>
<dt>&#8211;tlock=TLOCK</dt>
<dd> Lock test percentage [default: 50]</dd>
<dt>&#8211;lockfull=LOCKFULL</dt>
<dd> Lock full file percentage [default: 50]</dd>
<dt>&#8211;minfiles=MINFILES</dt>
<dd> Mininum number of files to create before any file operation is executed [default: 10] </dd>
</dl>
<h3>File size options:</h3>
<dl>
<dt>&#8211;fsizeavg=FSIZEAVG</dt>
<dd> File size average [default: 1m]</dd>
<dt>&#8211;fsizedev=FSIZEDEV</dt>
<dd> File size standard deviation [default: 256k]</dd>
<dt>&#8211;rsize=RSIZE</dt>
<dd> Read block size [default: 64k]</dd>
<dt>&#8211;rsizedev=RSIZEDEV</dt>
<dd> Read block size standard deviation [default: 8k]</dd>
<dt>&#8211;wsize=WSIZE</dt>
<dd> Write block size [default: 64k]</dd>
<dt>&#8211;wsizedev=WSIZEDEV</dt>
<dd> Write block size standard deviation [default: 8k]</dd>
<dt>&#8211;sizemult=SIZEMULT</dt>
<dd> Size multiplier [default: 1] </dd>
</dl>
<h3>Logging options:</h3>
<dl>
<dt>&#8211;createlog</dt>
<dd> Create log file</dd>
<dt>&#8211;createlogs</dt>
<dd> Create a log file for each process</dd>
<dt>&#8211;logdir=LOGDIR</dt>
<dd> Log directory [default: &#8216;/tmp&#8217;]</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-nfstest-file_io/">nfstest.file_io</a>(3),</code> <code><a href="/docs/linux/man/1-nfstest_alloc/">nfstest_alloc</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_cache/">nfstest_cache</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_delegation/">nfstest_delegation</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_dio/">nfstest_dio</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_file/">nfstest_file</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_interop/">nfstest_interop</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_lock/">nfstest_lock</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pkt/">nfstest_pkt</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_pnfs/">nfstest_pnfs</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_posix/">nfstest_posix</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_sparse/">nfstest_sparse</a>(1),</code> <code><a href="/docs/linux/man/1-nfstest_xid/">nfstest_xid</a>(1)</code> </p>
<h2>BUGS</h2>
<p> No known bugs.</p>
<h2>AUTHOR</h2>
<p> Jorge Mora (mora [at] netapp.com) </p>
<h2>Index</h2>
