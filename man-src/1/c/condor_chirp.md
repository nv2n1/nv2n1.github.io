---
title: "condor_chirp(1)"
name: "condor_chirp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_chirp/"
description: "condor_chirp Access files or job ClassAd from an executing job"
---

<h2>Name</h2>
<p> <i>condor_chirp</i> Access files or job ClassAd from an executing job </p>
<h2>Synopsis</h2>
<p> <i>condor_chirp</i> <code>&lt;Chirp-Command&gt;</code> </p>
<h2>Description</h2>
<p> <i>condor_chirp</i> is not intended for use as a command-line tool. It is most often invoked by an HTCondor job, while the job is executing. It accesses files or job ClassAd attributes on the submit machine. Files can be read, written or removed. Job attributes can be read, and most attributes can be updated. </p>
<p> When invoked by an HTCondor job, the command-line arguments describe the operation to be performed. Each of these arguments is described below within the section on Chirp Commands. Descriptions using the terms <i>local</i> and <i>remote</i> are given from the point of view of the executing job. </p>
<p> If the input file name for <code>put</code> or <code>write</code> is a dash, <i>condor_chirp</i> uses standard input as the source. If the output file name for <code>fetch</code> is a dash, <i>condor_chirp</i> writes to standard output instead of a local file. </p>
<p> Jobs that use <i>condor_chirp</i> must have the attribute WantIOProxy set to True in the job ClassAd. To do this, place </p>
<p> +WantIOProxy = true </p>
<p> in the submit description file of the job. </p>
<p> <i>condor_chirp</i> only works for jobs run in the vanilla, parallel and java universes. </p>
<h2>Chirp Commands</h2>
<p> <code>fetch </code> <i>RemoteFileName LocalFileName</i></p>
<dl>
<dt>
<dd> Copy the <i>RemoteFileName</i> from the submit machine to the execute machine, naming it <i>LocalFileName</i> .</p>
<dt>
<dd></dl>
<p> <code>put</code> [ <code>-mode </code> <i>mode</i> ] [ <code>-perm </code> <i>UnixPerm</i> ] <i>LocalFileName</i> <i>RemoteFileName</i></p>
<dl>
<dt>
<dd> Copy the <i>LocalFileName</i> from the execute machine to the submit machine, naming it <i>RemoteFileName</i> . The optional <code>-perm </code> <i>UnixPerm</i> argument describes the file access permissions in a Unix format; 660 is an example Unix format.</p>
<dt>
<dd> The optional <code>-mode </code> <i>mode</i> argument is one or more of the following characters describing the <i>RemoteFileName</i> file: w , open for writing; a , force all writes to append; t , truncate before use; c , create the file, if it does not exist; x , fail if c is given and the file already exists.</p>
<dt>
<dd></dl>
<p> <code>remove </code> <i>RemoteFileName</i></p>
<dl>
<dt>
<dd> Remove the <i>RemoteFileName</i> file from the submit machine.</p>
<dt>
<dd></dl>
<p> <code>get_job_attr </code> <i>JobAttributeName</i></p>
<dl>
<dt>
<dd> Prints the named job ClassAd attribute to standard output.</p>
<dt>
<dd></dl>
<p> <code>set_job_attr </code> <i>JobAttributeName AttributeValue</i></p>
<dl>
<dt>
<dd> Sets the named job ClassAd attribute with the given attribute value.</p>
<dt>
<dd></dl>
<p> <code>get_job_attr_delayed </code> <i>JobAttributeName</i></p>
<dl>
<dt>
<dd> Prints the named job ClassAd attribute to standard output, potentially reading the cached value from a recent set_job_attr_delayed.</p>
<dt>
<dd></dl>
<p> <code>set_job_attr_delayed </code> <i>JobAttributeName AttributeValue</i></p>
<dl>
<dt>
<dd> Sets the named job ClassAd attribute with the given attribute value, but does not immediately synchronize the value with the submit side. It can take 15 minutes before the synchronization occurs. This has much less overhead than the non delayed version. With this option, jobs do <i>not</i> need ClassAd attribute WantIOProxy set. With this option, job attribute names are restricted to begin with the case sensitive substring Chirp .</p>
<dt>
<dd></dl>
<p> <code>ulog </code> <i>Message</i></p>
<dl>
<dt>
<dd> Appends <i>Message</i> to the job event log.</p>
<dt>
<dd></dl>
<p> <code>read</code> [ <code>-offset </code> <i>offset</i> ] [ <code>-stride </code> <i>length skip</i> ] <i>RemoteFileName</i> <i>Length</i></p>
<dl>
<dt>
<dd> Read <i>Length</i> bytes from <i>RemoteFileName</i> . Optionally, implement a stride by starting the read at <i>offset</i> and reading <i>length</i> bytes with a stride of <i>skip</i> bytes.</p>
<dt>
<dd></dl>
<p> <code>write</code> [ <code>-offset </code> <i>offset</i> ] [ <code>-stride </code> <i>length skip</i> ] <i>RemoteFileName</i> <i>LocalFileName</i> [ <i>numbytes</i> ]</p>
<dl>
<dt>
<dd> Write the contents of <i>LocalFileName</i> to <i>RemoteFileName</i> . Optionally, start writing to the remote file at <i>offset</i> and write <i>length</i> bytes with a stride of <i>skip</i> bytes. If the optional <i>numbytes</i> follows <i>LocalFileName</i> , then the write will halt after <i>numbytes</i> input bytes have been written. Otherwise, the entire contents of <i>LocalFileName</i> will be written.</p>
<dt>
<dd></dl>
<p> <code>rmdir</code> [ <code>-r</code> ] <i>RemotePath</i></p>
<dl>
<dt>
<dd> Delete the directory specified by <i>RemotePath</i> . If the optional <code>-r</code> is specified, recursively delete the entire directory.</p>
<dt>
<dd></dl>
<p> <code>getdir</code> [ <code>-l</code> ] <i>RemotePath</i></p>
<dl>
<dt>
<dd> List the contents of the directory specified by <i>RemotePath</i> . If <i>-l</i> is specified, list all metadata as well.</p>
<dt>
<dd></dl>
<p> <code>whoami</code></p>
<dl>
<dt>
<dd> Get the user&#8217;s current identity.</p>
<dt>
<dd></dl>
<p> <code>whoareyou </code> <i>RemoteHost</i></p>
<dl>
<dt>
<dd> Get the identity of <i>RemoteHost</i> .</p>
<dt>
<dd></dl>
<p> <code>link</code> [ <code>-s</code> ] <i>OldRemotePath</i> <i>NewRemotePath</i></p>
<dl>
<dt>
<dd> Create a hard link from <i>OldRemotePath</i> to <i>NewRemotePath</i> . If the optional <i>-s</i> is specified, create a symbolic link instead.</p>
<dt>
<dd></dl>
<p> <code>readlink </code> <i>RemoteFileName</i></p>
<dl>
<dt>
<dd> Read the contents of the file defined by the symbolic link <i>RemoteFileName</i> .</p>
<dt>
<dd></dl>
<p> <code>stat </code> <i>RemotePath</i></p>
<dl>
<dt>
<dd> Get metadata for <i>RemotePath</i> . Examines the target, if it is a symbolic link.</p>
<dt>
<dd></dl>
<p> <code>lstat </code> <i>RemotePath</i></p>
<dl>
<dt>
<dd> Get metadata for <i>RemotePath</i> . Examines the file, if it is a symbolic link.</p>
<dt>
<dd></dl>
<p> <code>statfs </code> <i>RemotePath</i></p>
<dl>
<dt>
<dd> Get file system metadata for <i>RemotePath</i> .</p>
<dt>
<dd></dl>
<p> <code>access </code> <i>RemotePath Mode</i></p>
<dl>
<dt>
<dd> Check access permissions for <i>RemotePath</i> . <i>Mode</i> is one or more of the characters r , w , x , or f , representing read, write, execute, and existence, respectively.</p>
<dt>
<dd></dl>
<p> <code>chmod </code> <i>RemotePath UnixPerm</i></p>
<dl>
<dt>
<dd> Change the permissions of <i>RemotePath</i> to <i>UnixPerm</i> . <i>UnixPerm</i> describes the file access permissions in a Unix format; 660 is an example Unix format.</p>
<dt>
<dd></dl>
<p> <code>chown </code> <i>RemotePath UID GID</i></p>
<dl>
<dt>
<dd> Change the ownership of <i>RemotePath</i> to <i>UID</i> and <i>GID</i> . Changes the target of <i>RemotePath</i> , if it is a symbolic link.</p>
<dt>
<dd></dl>
<p> <code>chown </code> <i>RemotePath UID GID</i></p>
<dl>
<dt>
<dd> Change the ownership of <i>RemotePath</i> to <i>UID</i> and <i>GID</i> . Changes the link, if <i>RemotePath</i> is a symbolic link.</p>
<dt>
<dd></dl>
<p> <code>truncate </code> <i>RemoteFileName Length</i></p>
<dl>
<dt>
<dd> Truncates <i>RemoteFileName</i> to <i>Length</i> bytes.</p>
<dt>
<dd></dl>
<p> <code>utime </code> <i>RemotePath AccessTime ModifyTime</i></p>
<dl>
<dt>
<dd> Change the access to <i>AccessTime</i> and modification time to <i>ModifyTime</i> of <i>RemotePath</i> .</p>
<dt>
<dd></dl>
<h2>Examples</h2>
<p> To copy a file from the submit machine to the execute machine while the user job is running, run </p>
<p>&nbsp;<wbr>&nbsp;<wbr>condor_chirp fetch remotefile localfile </p>
<p> To print to standard output the value of the Requirements expression from within a running job, run </p>
<p>&nbsp;<wbr>&nbsp;<wbr>condor_chirp get_job_attr Requirements </p>
<p> Note that the remote (submit-side) directory path is relative to the submit directory, and the local (execute-side) directory is relative to the current directory of the running program. </p>
<p> To append the word &quot;foo&quot; to a file called RemoteFile on the submit machine, run </p>
<p>&nbsp;<wbr>&nbsp;<wbr>echo foo | condor_chirp put -mode wa &#8211; RemoteFile </p>
<p> To append the message &quot;Hello World&quot; to the job event log, run </p>
<p>&nbsp;<wbr>&nbsp;<wbr>condor_chirp ulog&nbsp;<wbr>&quot;Hello World&quot; </p>
<h2>Exit Status</h2>
<p> <i>condor_chirp</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
