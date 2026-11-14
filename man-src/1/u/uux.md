---
title: "uux(1)"
name: "uux"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uux/"
description: "uux – Remote command execution over UUCP"
---

<h2>NAME</h2>
<p> uux &#8211; Remote command execution over UUCP</p>
<h2>SYNOPSIS</h2>
<p> <code>uux</code> [ options ] command</p>
<h2>DESCRIPTION</h2>
<p> The <i>uux</i> command is used to execute a command on a remote system, or to execute a command on the local system using files from remote systems. The command is not executed immediately; the request is queued until the <i>uucico</i> (8) daemon calls the system and executes it. The daemon is started automatically unless one of the <code>-r</code> or <code>&#8211;nouucico</code> options is given. </p>
<p> The actual command execution is done by the <i>uuxqt</i> (8) daemon. </p>
<p> File arguments can be gathered from remote systems to the execution system, as can standard input. Standard output may be directed to a file on a remote system. </p>
<p> The command name may be preceded by a system name followed by an exclamation point if it is to be executed on a remote system. An empty system name is taken as the local system. </p>
<p> Each argument that contains an exclamation point is treated as naming a file. The system which the file is on is before the exclamation point, and the pathname on that system follows it. An empty system name is taken as the local system; this must be used to transfer a file to a command being executed on a remote system. If the path is not absolute, it will be appended to the current working directory on the local system; the result may not be meaningful on the remote system. A pathname may begin with ~/, in which case it is relative to the UUCP public directory (usually /usr/spool/uucppublic or /var/spool/uucppublic) on the appropriate system. A pathname may begin with ~name/, in which case it is relative to the home directory of the named user on the appropriate system. </p>
<p> Standard input and output may be redirected as usual; the pathnames used may contain exclamation points to indicate that they are on remote systems. Note that the redirection characters must be quoted so that they are passed to <i>uux</i> rather than interpreted by the shell. Append redirection (&gt;&gt;) does not work. </p>
<p> All specified files are gathered together into a single directory before execution of the command begins. This means that each file must have a distinct base name. For example, </p>
<pre>
uux 'sys1!diff sys2!~user1/foo sys3!~user2/foo &gt;!foo.diff'
</pre>
<p> will fail because both files will be copied to sys1 and stored under the name foo. </p>
<p> Arguments may be quoted by parentheses to avoid interpretation of exclamation points. This is useful when executing the <i>uucp</i> command on a remote system. </p>
<p> A request to execute an empty command (e.g., <i>uux sys!)</i> will create a poll file for the specified system. </p>
<p> The exit status of <i>uux</i> is one of the codes found in the header file <code>sysexits.h.</code> In particular, <code>EX_OK</code> ( <code>0</code> ) indicates success, and <code>EX_TEMPFAIL</code> ( <code>75</code> ) indicates a temporary failure.</p>
<h2>OPTIONS</h2>
<p> The following options may be given to <i>uux.</i></p>
<dl>
<dt><code>-, -p, &#8211;stdin</code></p>
<dd> Read standard input and use it as the standard input for the command to be executed.</p>
<dt><code>-c, &#8211;nocopy</code></p>
<dd> Do not copy local files to the spool directory. This is the default. If they are removed before being processed by the <i>uucico</i> (8) daemon, the copy will fail. The files must be readable by the <i>uucico</i> (8) daemon, as well as the by the invoker of <i>uux.</i></p>
<dt><code>-C, &#8211;copy</code></p>
<dd> Copy local files to the spool directory.</p>
<dt><code>-l, &#8211;link</code></p>
<dd> Link local files into the spool directory. If a file can not be linked because it is on a different device, it will be copied unless one of the <code>-c</code> or <code>&#8211;nocopy</code> options also appears (in other words, use of <code>&#8211;link</code> switches the default from <code>&#8211;nocopy</code> to <code>&#8211;copy).</code> If the files are changed before being processed by the <i>uucico</i> (8) daemon, the changed versions will be used. The files must be readable by the <i>uucico</i> (8) daemon, as well as by the invoker of <i>uux.</i></p>
<dt><code>-g grade, &#8211;grade grade</code></p>
<dd> Set the grade of the file transfer command. Jobs of a higher grade are executed first. Grades run 0 &#8230; 9 A &#8230; Z a &#8230; z from high to low.</p>
<dt><code>-n, &#8211;notification=no</code></p>
<dd> Do not send mail about the status of the job, even if it fails.</p>
<dt><code>-z, &#8211;notification=error</code></p>
<dd> Send mail about the status of the job if an error occurs. For many <i>uuxqt</i> daemons, including the Taylor UUCP <i>uuxqt,</i> this is the default action; for those, <code>&#8211;notification=error</code> will have no effect. However, some <i>uuxqt</i> daemons will send mail if the job succeeds unless the <code>&#8211;notification=error</code> option is used, and some other <i>uuxqt</i> daemons will not send mail if the job fails unless the <code>&#8211;notification=error</code> option is used.</p>
<dt><code>-r, &#8211;nouucico</code></p>
<dd> Do not start the <i>uucico</i> (8) daemon immediately; merely queue up the execution request for later processing.</p>
<dt><code>-j, &#8211;jobid</code></p>
<dd> Print jobids on standard output. A jobid will be generated for each file copy operation required to perform the operation. These file copies may be cancelled by passing the jobid to the <code>&#8211;kill</code> switch of <i>uustat</i> (1), which will make the execution impossible to complete.</p>
<dt><code>-a address, &#8211;requestor address</code></p>
<dd> Report job status to the specified e-mail address.</p>
<dt><code>-x type, &#8211;debug type</code></p>
<dd> Turn on particular debugging types. The following types are recognized: abnormal, chat, handshake, uucp-proto, proto, port, config, spooldir, execute, incoming, outgoing. Only abnormal, config, spooldir and execute are meaningful for <i>uux.</i> </p>
<p> Multiple types may be given, separated by commas, and the <code>&#8211;debug</code> option may appear multiple times. A number may also be given, which will turn on that many types from the foregoing list; for example, <code>&#8211;debug 2</code> is equivalent to <code>&#8211;debug abnormal,chat.</code></p>
<dt><code>-I file, &#8211;config file</code></p>
<dd> Set configuration file to use. This option may not be available, depending upon how <i>uux</i> was compiled.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Report version information and exit.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a help message and exit.</dl>
<h2>EXAMPLES</h2>
<pre>
uux -z - sys1!rmail user1
</pre>
<p> Execute the command &#8220;rmail user1&#8221; on the system sys1, giving it as standard input whatever is given to <i>uux</i> as standard input. If a failure occurs, send a message using <i>mail</i> (1). </p>
<pre>
uux 'diff -c sys1!~user1/file1 sys2!~user2/file2 &gt;!file.diff'
</pre>
<p> Fetch the two named files from system sys1 and system sys2 and execute <i>diff</i> putting the result in file.diff in the current directory. The current directory must be writable by the <i>uuxqt</i> (8) daemon for this to work. </p>
<pre>
uux 'sys1!uucp ~user1/file1 (sys2!~user2/file2)'
</pre>
<p> Execute <i>uucp</i> on the system sys1 copying file1 (on system sys1) to sys2. This illustrates the use of parentheses for quoting.</p>
<h2>RESTRICTIONS</h2>
<p> The remote system may not permit you to execute certain commands. Many remote systems only permit the execution of <i>rmail</i> and <i>rnews.</i> </p>
<p> Some of the options are dependent on the capabilities of the <i>uuxqt</i> (8) daemon on the remote system.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mail/">mail</a>(1), <a href="/docs/linux/man/1-uustat/">uustat</a>(1), <a href="/docs/linux/man/1-uucp/">uucp</a>(1), <a href="/docs/linux/man/8-uucico/">uucico</a>(8), <a href="/docs/linux/man/8-uuxqt/">uuxqt</a>(8)</p>
<h2>BUGS</h2>
<p> Files can not be referenced across multiple systems. </p>
<p> Too many jobids are output by <code>&#8211;jobid,</code> and there is no good way to cancel a local execution requiring remote files.</p>
<h2>AUTHOR</h2>
<p> Ian Lance Taylor (ian [at] airs.com) </p>
<h2>Index</h2>
