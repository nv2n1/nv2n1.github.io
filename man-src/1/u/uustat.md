---
title: "uustat(1)"
name: "uustat"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uustat/"
description: "uustat – UUCP status inquiry and control"
---

<h2>NAME</h2>
<p> uustat &#8211; UUCP status inquiry and control</p>
<h2>SYNOPSIS</h2>
<p> <code>uustat -a</code> </p>
<p> <code>uustat &#8211;all</code> </p>
<p> <code>uustat</code> [ <code>-eKRiMNQ ] [</code> <code>-sS</code> system ] [ <code>-uU</code> user ] [ <code>-cC</code> command ] [ <code>-oy</code> hours ] [ <code>-B</code> lines ] [ <code>&#8211;executions</code> ] [ <code>&#8211;kill-all</code> ] [ <code>&#8211;rejuvenate-all</code> ] [ <code>&#8211;prompt</code> ] [ <code>&#8211;mail</code> ] [ <code>&#8211;notify</code> ] [ <code>&#8211;no-list</code> ] [ <code>&#8211;system</code> system ] [ <code>&#8211;not-system</code> system ] [ <code>&#8211;user</code> user ] [ <code>&#8211;not-user</code> user ] [ <code>&#8211;command</code> command ] [ <code>&#8211;not-command</code> command ] [ <code>&#8211;older-than</code> hours ] [ <code>&#8211;younger-than</code> hours ] [ <code>&#8211;mail-lines</code> lines ] </p>
<p> <code>uustat</code> [ <code>-kr</code> jobid ] [ <code>&#8211;kill</code> jobid ] [ <code>&#8211;rejuvenate</code> jobid ] </p>
<p> <code>uustat -q [</code> <code>-sS</code> system ] [ <code>-oy</code> hours ] [ <code>&#8211;system</code> system ] [ <code>&#8211;not-system</code> system ] [ <code>&#8211;older-than</code> hours ] [ <code>&#8211;younger-than</code> hours ] </p>
<p> <code>uustat &#8211;list [</code> <code>-sS</code> system ] [ <code>-oy</code> hours ] [ <code>&#8211;system</code> system ] [ <code>&#8211;not-system</code> system ] [ <code>&#8211;older-than</code> hours ] [ <code>&#8211;younger-than</code> hours ] </p>
<p> <code>uustat -m</code> </p>
<p> <code>uustat &#8211;status</code> </p>
<p> <code>uustat -p</code> </p>
<p> <code>uustat &#8211;ps</code></p>
<h2>DESCRIPTION</h2>
<p> The <i>uustat</i> command can display various types of status information about the UUCP system. It can also be used to cancel or rejuvenate requests made by <i>uucp</i> (1) or <i>uux</i> (1). </p>
<p> By default <i>uustat</i> displays all jobs queued up for the invoking user, as if given the <code>&#8211;user</code> option with the appropriate argument. </p>
<p> If any of the <code>-a,</code> <code>&#8211;all,</code> <code>-e,</code> <code>&#8211;executions,</code> <code>-s,</code> <code>&#8211;system,</code> <code>-S,</code> <code>&#8211;not-system,</code> <code>-u,</code> <code>&#8211;user,</code> <code>-U,</code> <code>&#8211;not-user,</code> <code>-c,</code> <code>&#8211;command,</code> <code>-C,</code> <code>&#8211;not-command,</code> <code>-o,</code> <code>&#8211;older-than,</code> <code>-y,</code> <code>&#8211;younger-than</code> options are given, then all jobs which match the combined specifications are displayed. </p>
<p> The <code>-K</code> or <code>&#8211;kill-all</code> option may be used to kill off a selected group of jobs, such as all jobs more than 7 days old.</p>
<h2>OPTIONS</h2>
<p> The following options may be given to <i>uustat.</i></p>
<dl>
<dt><code>-a, &#8211;all</code></p>
<dd> List all queued file transfer requests.</p>
<dt><code>-e, &#8211;executions</code></p>
<dd> List queued execution requests rather than queued file transfer requests. Queued execution requests are processed by <i>uuxqt</i> (8) rather than <i>uucico</i> (8). Queued execution requests may be waiting for some file to be transferred from a remote system. They are created by an invocation of <i>uux</i> (1).</p>
<dt><code>-s system, &#8211;system system</code></p>
<dd> List all jobs queued up for the named system. These options may be specified multiple times, in which case all jobs for all the systems will be listed. If used with <code>&#8211;list</code> only the systems named will be listed.</p>
<dt><code>-S system, &#8211;not-system system</code></p>
<dd> List all jobs queued for systems other than the one named. These options may be specified multiple times, in which case no jobs from any of the specified systems will be listed. If used with <code>&#8211;list</code> only the systems not named will be listed. These options may not be used with <code>-s</code> or <code>&#8211;system.</code></p>
<dt><code>-u user, &#8211;user user</code></p>
<dd> List all jobs queued up for the named user. These options may be specified multiple times, in which case all jobs for all the users will be listed.</p>
<dt><code>-U user, &#8211;not-user user</code></p>
<dd> List all jobs queued up for users other than the one named. These options may be specified multiple times, in which case no jobs from any of the specified users will be listed. These options may not be used with <code>-u</code> or <code>&#8211;user.</code></p>
<dt><code>-c command, &#8211;command command</code></p>
<dd> List all jobs requesting the execution of the named command. If <code>command</code> is <i>ALL</i> this will list all jobs requesting the execution of some command (as opposed to simply requesting a file transfer). These options may be specified multiple times, in which case all jobs requesting any of the commands will be listed.</p>
<dt><code>-C command, &#8211;not-command command</code></p>
<dd> List all jobs requesting execution of some command other than the named command, or, if <code>command</code> is <i>ALL,</i> list all jobs that simply request a file transfer (as opposed to requesting the execution of some command). These options may be specified multiple times, in which case no job requesting one of the specified commands will be listed. These options may not be used with <code>-c</code> or <code>&#8211;command.</code></p>
<dt><code>-o hours, &#8211;older-than hours</code></p>
<dd> List all queued jobs older than the given number of hours. If used with <code>&#8211;list</code> only systems whose oldest job is older than the given number of hours will be listed.</p>
<dt><code>-y hours, &#8211;younger-than hours</code></p>
<dd> List all queued jobs younger than the given number of hours. If used with <code>&#8211;list</code> only systems whose oldest job is younger than the given number of hours will be listed.</p>
<dt><code>-k jobid, &#8211;kill jobid</code></p>
<dd> Kill the named job. The job id is shown by the default output format, as well as by the <code>-j</code> or <code>&#8211;jobid</code> option to <i>uucp</i> (1) or <i>uux</i> (1). A job may only be killed by the user who created the job, or by the UUCP administrator or the superuser. The <code>-k</code> or <code>&#8211;kill</code> options may be used multiple times on the command line to kill several jobs.</p>
<dt><code>-r jobid, &#8211;rejuvenate jobid</code></p>
<dd> Rejuvenate the named job. This will mark it as having been invoked at the current time, affecting the output of the <code>-o,</code> <code>&#8211;older-than,</code> <code>-y,</code> or <code>&#8211;younger-than</code> options and preserving it from any automated cleanup daemon. The job id is shown by the default output format, as well as by the <code>-j</code> or <code>&#8211;jobid</code> options to <i>uucp</i> (1) or <i>uux</i> (1). A job may only be rejuvenated by the user who created the job, or by the UUCP administrator or the superuser. The <code>-r</code> or <code>&#8211;rejuvenate</code> options may be used multiple times on the command line to rejuvenate several jobs.</p>
<dt><code>-q, &#8211;list</code></p>
<dd> Display the status of commands, executions and conversations for all remote systems for which commands or executions are queued. The <code>-s,</code> <code>&#8211;system,</code> <code>-S,</code> <code>&#8211;not-system,</code> <code>-o,</code> <code>&#8211;older-than,</code> <code>-y,</code> and <code>&#8211;younger-than</code> options may be used to restrict the systems which are listed. Systems for which no commands or executions are queued will never be listed.</p>
<dt><code>-m, &#8211;status</code></p>
<dd> Display the status of conversations for all remote systems.</p>
<dt><code>-p, &#8211;ps</code></p>
<dd> Display the status of all processes holding UUCP locks on systems or ports.</p>
<dt><code>-i, &#8211;prompt</code></p>
<dd> For each listed job, prompt whether to kill the job or not. If the first character of the input line is <i>y</i> or <i>Y</i> the job will be killed.</p>
<dt><code>-K, &#8211;kill-all</code></p>
<dd> Automatically kill each listed job. This can be useful for automatic cleanup scripts, in conjunction with the <code>&#8211;mail</code> and <code>&#8211;notify</code> options.</p>
<dt><code>-R, &#8211;rejuvenate-all</code></p>
<dd> Automatically rejuvenate each listed job. This may not be used with <code>&#8211;kill-all.</code></p>
<dt><code>-M, &#8211;mail</code></p>
<dd> For each listed job, send mail to the UUCP administrator. If the job is killed (due to <code>&#8211;kill-all</code> or <code>&#8211;prompt</code> with an affirmative response) the mail will indicate that. A comment specified by the <code>&#8211;comment</code> option may be included. If the job is an execution, the initial portion of its standard input will be included in the mail message; the number of lines to include may be set with the <code>&#8211;mail-lines</code> option (the default is 100). If the standard input contains null characters, it is assumed to be a binary file and is not included.</p>
<dt><code>-N, &#8211;notify</code></p>
<dd> For each listed job, send mail to the user who requested the job. The mail is identical to that sent by the <code>-M</code> or <code>&#8211;mail</code> options.</p>
<dt><code>-W comment, &#8211;comment comment</code></p>
<dd> Specify a comment to be included in mail sent with the <code>-M,</code> <code>&#8211;mail,</code> <code>-N,</code> or <code>&#8211;notify</code> options.</p>
<dt><code>-B lines, &#8211;mail-lines lines</code></p>
<dd> When the <code>-M,</code> <code>&#8211;mail,</code> <code>-N,</code> or <code>&#8211;notify</code> options are used to send mail about an execution with standard input, this option controls the number of lines of standard input to include in the message. The default is 100.</p>
<dt><code>-Q, &#8211;no-list</code></p>
<dd> Do not actually list the job, but only take any actions indicated by the <code>-i,</code> <code>&#8211;prompt,</code> <code>-K,</code> <code>&#8211;kill-all,</code> <code>-M,</code> <code>&#8211;mail,</code> <code>-N</code> or <code>&#8211;notify</code> options.</p>
<dt><code>-x type, &#8211;debug type</code></p>
<dd> Turn on particular debugging types. The following types are recognized: abnormal, chat, handshake, uucp-proto, proto, port, config, spooldir, execute, incoming, outgoing. Only abnormal, config, spooldir and execute are meaningful for <i>uustat.</i> </p>
<p> Multiple types may be given, separated by commas, and the <code>&#8211;debug</code> option may appear multiple times. A number may also be given, which will turn on that many types from the foregoing list; for example, <code>&#8211;debug 2</code> is equivalent to <code>&#8211;debug abnormal,chat.</code></p>
<dt><code>-I file, &#8211;config file</code></p>
<dd> Set configuration file to use. This option may not be available, depending upon how <i>uustat</i> was compiled.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Report version information and exit.</p>
<dt><code>&#8211;help</code></p>
<dd> Print a help message and exit.</dl>
<h2>EXAMPLES</h2>
<pre>
uustat --all
</pre>
<p> Display status of all jobs. A sample output line is as follows: </p>
<pre>
bugsA027h bugs ian 04-01 13:50 Executing rmail ian [at] airs.com (sending 1283 bytes)
</pre>
<p> The format is </p>
<pre>
jobid system user queue-date command (size)
</pre>
<p> The jobid may be passed to the <code>&#8211;kill</code> or <code>&#8211;rejuvenate</code> options. The size indicates how much data is to be transferred to the remote system, and is absent for a file receive request. The <code>&#8211;system,</code> <code>&#8211;not-system,</code> <code>&#8211;user,</code> <code>&#8211;not-user,</code> <code>&#8211;command,</code> <code>&#8211;not-command,</code> <code>&#8211;older-than,</code> and <code>&#8211;younger-than</code> options may be used to control which jobs are listed. </p>
<pre>
uustat --executions
</pre>
<p> Display status of queued up execution requests. A sample output line is as follows: </p>
<pre>
bugs bugs!ian 05-20 12:51 rmail ian
</pre>
<p> The format is </p>
<pre>
system requestor queue-date command
</pre>
<p> The <code>&#8211;system,</code> <code>&#8211;not-system,</code> <code>&#8211;user,</code> <code>&#8211;not-user,</code> <code>&#8211;command,</code> <code>&#8211;not-command,</code> <code>&#8211;older-than,</code> and <code>&#8211;younger-than</code> options may be used to control which requests are listed. </p>
<pre>
uustat --list
</pre>
<p> Display status for all systems with queued up commands. A sample output line is as follows: </p>
<pre>
bugs            4C (1 hour)   0X (0 secs) 04-01 14:45 Dial failed
</pre>
<p> This indicates the system, the number of queued commands, the age of the oldest queued command, the number of queued local executions, the age of the oldest queued execution, the date of the last conversation, and the status of that conversation. </p>
<pre>
uustat --status
</pre>
<p> Display conversation status for all remote systems. A sample output line is as follows: </p>
<pre>
bugs           04-01 15:51 Conversation complete
</pre>
<p> This indicates the system, the date of the last conversation, and the status of that conversation. If the last conversation failed, <i>uustat</i> will indicate how many attempts have been made to call the system. If the retry period is currently preventing calls to that system, <i>uustat</i> also displays the time when the next call will be permitted. </p>
<pre>
uustat --ps
</pre>
<p> Display the status of all processes holding UUCP locks. The output format is system dependent, as <i>uustat</i> simply invokes <i>ps</i> (1) on each process holding a lock. </p>
<pre><code>
uustat-- command rmail-- older - than 168 --kill - all-- no - list-- mail-- notify-- comment "Queued for over 1 week"
</code></pre>
<p> This will kill all <i>rmail</i> commands that have been queued up waiting for delivery for over 1 week (168 hours). For each such command, mail will be sent both to the UUCP administrator and to the user who requested the rmail execution. The mail message sent will include the string given by the <code>&#8211;comment</code> option. The <code>&#8211;no-list</code> option prevents any of the jobs from being listed on the terminal, so any output from the program will be error messages.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ps/">ps</a>(1), <a href="/docs/linux/man/1-rmail/">rmail</a>(1), <a href="/docs/linux/man/1-uucp/">uucp</a>(1), <a href="/docs/linux/man/1-uux/">uux</a>(1), <a href="/docs/linux/man/8-uucico/">uucico</a>(8), <a href="/docs/linux/man/8-uuxqt/">uuxqt</a>(8)</p>
<h2>AUTHOR</h2>
<p> Ian Lance Taylor (ian [at] airs.com) </p>
<h2>Index</h2>
