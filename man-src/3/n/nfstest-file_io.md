---
title: "nfstest-file_io(3)"
name: "nfstest-file_io"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nfstest-file_io/"
description: "nfstest.file_io – File I/O module"
---

<p>nfstest.file_io &#8211; File I/O module</p>
<h2>Description</h2>
<p>Provides an interface to create and manipulate files of different types. The arguments allow running for a specified period of time as well as running multiple processes. Each process modifies a single file at a time and the file name space is different for each process so there are no collisions between two different processes modifying the same file. </p>
<p> File types:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Regular file<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Hard link<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Symbolic link </p>
<p> File operations:<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Open&nbsp;<wbr>(create or re-open)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Open downgrade<br />
&nbsp;<wbr>This is done by opening the file for read and write, then the file is<br />
&nbsp;<wbr>opened again as read only and finally closing the read and write file<br />
&nbsp;<wbr>descriptor<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Read&nbsp;<wbr>(sequential or random access)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Write&nbsp;<wbr>(sequential or random access)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Remove<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Rename<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Truncate&nbsp;<wbr>(path or file descriptor)<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Readdir<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Lock<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Unlock<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211; Tlock</p>
<h2>Classes</h2>
<h3>class FileIO(baseobj.BaseObj)</h3>
<pre>FileIO object
Usage:
 from nfstest.file_io import FileIO
 # Instantiate FileIO object given top level directory
 x = FileIO(datadir=&quot;/tmp/data&quot;)
 # Run workload creating the top level directory if necessary
 x.run()
<code>Methods defined here:</code>
---------------------
<code>__del__(self)</code>
Destructor
<code>__init__(self, **kwargs)</code>
Constructor
Initialize object's private data
<dl><dt><dd><dl><dt><code>datadir:</code>
<dd>Top level directory where files will be created,
it will be created if it does not exist
<dt><code>seed:</code>
<dd>Seed to initialized the random number generator
[default: automatically generated]
<dt><code>nprocs:</code>
<dd>Number of processes to use [default: 1]
<dt><code>runtime:</code>
<dd>Run time [default: 0 (indefinitely)]
<dt><code>verbose:</code>
<dd>Verbose level: none|info|debug|dbg1-7|all [default: 'none']
<dt><code>exiterr:</code>
<dd>Exit on first error [default: False]
<dt><code>read:</code>
<dd>Read file percentage [default: 40]
<dt><code>write:</code>
<dd>Write file percentage [default: 40]
<dt><code>rdwr:</code>
<dd>Read/write file percentage [default: 20]
<dt><code>randio:</code>
<dd>Random file access percentage [default: 50]
<dt><code>iodelay:</code>
<dd>Seconds to delay I/O operations [default: 0.0]
<dt><code>direct:</code>
<dd>Use direct I/O [default: False]
<dt><code>rdwronly:</code>
<dd>Use read and write only, no rename, remove, etc. [default: False]
<dt><code>create:</code>
<dd>Create file percentage [default: 5]
<dt><code>odgrade:</code>
<dd>Open downgrade percentage [default: 10]
<dt><code>osync:</code>
<dd>Open file with O_SYNC [default: 20]
<dt><code>fsync:</code>
<dd>Percentage of fsync after write [default: 5]
<dt><code>rename:</code>
<dd>Rename file percentage [default: 5]
<dt><code>remove:</code>
<dd>Remove file percentage [default: 5]
<dt><code>trunc:</code>
<dd>Truncate file percentage [default: 5]
<dt><code>ftrunc:</code>
<dd>Truncate opened file percentage [default: 5]
<dt><code>link:</code>
<dd>Create hard link percentage [default: 2]
<dt><code>slink:</code>
<dd>Create symbolic link percentage [default: 1]
<dt><code>readdir:</code>
<dd>List contents of directory percentage [default: 1]
<dt><code>lock:</code>
<dd>Lock file percentage [default: 20]
<dt><code>unlock:</code>
<dd>Unlock file percentage [default: 80]
<dt><code>tlock:</code>
<dd>Lock test percentage [default: 50]
<dt><code>lockfull:</code>
<dd>Lock full file percentage [default: 50]
<dt><code>minfiles:</code>
<dd>Mininum number of files to create before any file operation
is executed [default: 10]
<dt><code>fsizeavg:</code>
<dd>File size average [default: 1m]
<dt><code>fsizedev:</code>
<dd>File size standard deviation [default: 256k]
<dt><code>rsize:</code>
<dd>Read block size [default: 64k]
<dt><code>rsizedev:</code>
<dd>Read block size standard deviation [default: 8k]
<dt><code>wsize:</code>
<dd>Write block size [default: 64k]
<dt><code>wsizedev:</code>
<dd>Write block size standard deviation [default: 8k]
<dt><code>sizemult:</code>
<dd>Size multiplier [default: 1]
<dt><code>createlog:</code>
<dd>Create log file [default: False]
<dt><code>createlogs:</code>
<dd>Create a log file for each process [default: False]
<dt><code>logdir:</code>
<dd>Log directory [default: '/tmp']
</dl></dl>
<code>run(self)</code>
Main function where all processes are started
<code>run_process(self, tid=0)</code>
Main loop for each process</pre>
<h3>class FileObj(baseobj.BaseObj)</h3>
<pre># File object</pre>
<h3>class TermSignal(exceptions.Exception)</h3>
<pre>Exception to be raised on SIGTERM signal</pre>
<h2>Functions</h2>
<h3>stop_handler(signum, frame)</h3>
<p>Signal handler to catch SIGTERM and allow for gracefull termination of subprocesses</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-formatstr/">formatstr</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
