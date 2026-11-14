---
title: "uucp(1)"
name: "uucp"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uucp/"
description: "uucp – Unix to Unix copy"
---

<h2>NAME</h2>
<p> uucp &#8211; Unix to Unix copy</p>
<h2>SYNOPSIS</h2>
<p> <code>uucp</code> [ options ] source-file destination-file </p>
<p> <code>uucp</code> [ options ] source-file&#8230; destination-directory</p>
<h2>DESCRIPTION</h2>
<p> The <i>uucp</i> command copies files between systems. Each <i>file</i> argument is either a pathname on the local machine or is of the form</p>
<dl>
<dt>
<dd> system!path</dl>
<p> which is interpreted as being on a remote system. In the first form, the contents of the first file are copied to the second. In the second form, each source file is copied into the destination directory. </p>
<p> A file be transferred to or from <i>system2</i> via <i>system1</i> by using</p>
<dl>
<dt>
<dd> system1!system2!path.</dl>
<p> Any pathname that does not begin with / or ~ will be appended to the current directory (unless the <code>-W</code> or <code>&#8211;noexpand</code> option is used); this resulting path will not necessarily exist on a remote system. A pathname beginning with a simple ~ starts at the UUCP public directory; a pathname beginning with ~name starts at the home directory of the named user. The ~ is interpreted on the appropriate system. Note that some shells will interpret a simple ~ to the local home directory before <i>uucp</i> sees it; to avoid this the ~ must be quoted. </p>
<p> Shell metacharacters ? * [ ] are interpreted on the appropriate system, assuming they are quoted to prevent the shell from interpreting them first. </p>
<p> The copy does not take place immediately, but is queued up for the <i>uucico</i> (8) daemon; the daemon is started immediately unless the <code>-r</code> or <code>&#8211;nouucico</code> switch is given. In any case, the next time the remote system is called the file(s) will be copied.</p>
<h2>OPTIONS</h2>
<p> The following options may be given to <i>uucp.</i></p>
<dl>
<dt><code>-c, &#8211;nocopy</code></p>
<dd> Do not copy local source files to the spool directory. If they are removed before being processed by the <i>uucico</i> (8) daemon, the copy will fail. The files must be readable by the <i>uucico</i> (8) daemon, and by the invoking user.</p>
<dt><code>-C, &#8211;copy</code></p>
<dd> Copy local source files to the spool directory. This is the default.</p>
<dt><code>-d, &#8211;directories</code></p>
<dd> Create all necessary directories when doing the copy. This is the default.</p>
<dt><code>-f, &#8211;nodirectories</code></p>
<dd> If any necessary directories do not exist for the destination path, abort the copy.</p>
<dt><code>-R, &#8211;recursive</code></p>
<dd> If any of the source file names are directories, copy their contents recursively to the destination (which must itself be a directory).</p>
<dt><code>-g grade, &#8211;grade grade</code></p>
<dd> Set the grade of the file transfer command. Jobs of a higher grade are executed first. Grades run 0 &#8230; 9 A &#8230; Z a &#8230; z from high to low.</p>
<dt><code>-m, &#8211;mail</code></p>
<dd> Report completion or failure of the file transfer by <i>mail</i> (1).</p>
<dt><code>-n user, &#8211;notify user</code></p>
<dd> Report completion or failure of the file transfer by <i>mail</i> (1) to the named user on the remote system.</p>
<dt><code>-r, &#8211;nouucico</code></p>
<dd> Do not start <i>uucico</i> (8) daemon immediately; merely queue up the file transfer for later execution.</p>
<dt><code>-j, &#8211;jobid</code></p>
<dd> Print jobid on standard output. The job may be later cancelled by passing the jobid to the <code>-k</code> switch of <i>uustat</i> (1). It is possible for some complex operations to produce more than one jobid, in which case each will be printed on a separate line. For example </p>
<pre>
uucp sys1!~user1/file1 sys2!~user2/file2 ~user3
</pre>
<p> will generate two separate jobs, one for the system <i>sys1</i> and one for the system <i>sys2.</i></p>
<dt><code>-W, &#8211;noexpand</code></p>
<dd> Do not prepend remote relative path names with the current directory.</p>
<dt><code>-t, &#8211;uuto</code></p>
<dd> This option is used by the <i>uuto</i> shell script. It causes <i>uucp</i> to interpret the final argument as <i>system!user.</i> The file(s) are sent to <i>~/receive/USER/LOCAL</i> on the remote system, where <i>USER</i> is from the final argument and <i>LOCAL</i> is the local UUCP system name. Also, <i>uucp</i> will act as though <i>&#8211;notify user</i> were specified.</p>
<dt><code>-x type, &#8211;debug type</code></p>
<dd> Turn on particular debugging types. The following types are recognized: abnormal, chat, handshake, uucp-proto, proto, port, config, spooldir, execute, incoming, outgoing. Only abnormal, config, spooldir and execute are meaningful for <i>uucp.</i> </p>
<p> Multiple types may be given, separated by commas, and the <code>&#8211;debug</code> option may appear multiple times. A number may also be given, which will turn on that many types from the foregoing list; for example, <code>&#8211;debug 2</code> is equivalent to <code>&#8211;debug abnormal,chat.</code></p>
<dt><code>-I file, &#8211;config file</code></p>
<dd> Set configuration file to use. This option may not be available, depending upon how <i>uucp</i> was compiled.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Report version information and exit.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a help message and exit.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mail/">mail</a>(1), <a href="/docs/linux/man/1-uux/">uux</a>(1), <a href="/docs/linux/man/1-uustat/">uustat</a>(1), <a href="/docs/linux/man/8-uucico/">uucico</a>(8)</p>
<h2>BUGS</h2>
<p> Some of the options are dependent on the capabilities of the <i>uucico</i> (8) daemon on the remote system. </p>
<p> The <i>-n</i> and <i>-m</i> switches do not work when transferring a file from one remote system to another. </p>
<p> File modes are not preserved, except for the execute bit. The resulting file is owned by the uucp user.</p>
<h2>AUTHOR</h2>
<p> Ian Lance Taylor &lt;ian [at] airs.com&gt; </p>
<h2>Index</h2>
