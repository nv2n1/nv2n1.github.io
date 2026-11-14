---
title: "status(8)"
name: "status"
section: "8"
letter: "s"
url: "/docs/linux/man/8-status/"
description: "initctl – init daemon control utility"
---

<p>initctl &#8211; init daemon control utility</p>
<h2>Synopsis</h2>
<p><code>initctl</code> [<i>OPTION</i>]&#8230; <i>COMMAND</i> [<i>OPTION</i>]&#8230; <i>ARG</i>&#8230;</p>
<h2>Description</h2>
<p><code>initctl</code> allows a system administrator to communication with the <code><a href="/docs/linux/man/8-init/">init</a></code>(8) daemon and perform various actions depending on <i>COMMAND</i>. </p>
<p> Normally it is invoked directly with the command specified as the first non-option argument; however, symbolic or hard links may be used so that it is invoked as the name of a command, in which case it behaves accordingly.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;show-ids</code></p>
<dd>Usually a job&#8217;s name is sufficient to identify it, except for instance jobs which may have multiple running instances with the same name. To query or stop a specific instance, its unique id is necessary. </p>
<p> This option causes all commands to output the unique id of jobs and events, in addition to their name.</p>
<dt><code>&#8211;by-id</code></p>
<dd>Applies to the <code>start</code>, <code>stop</code> and <code>status</code> commands. </p>
<p> Normally these accept the job name as arguments; with this option they expect job ids instead.</p>
<dt><code>&#8211;no-wait</code></p>
<dd>Applies to the <code>start</code>, <code>stop</code> and <code>emit</code> commands. </p>
<p> Normally these commands wait for the named jobs or events to be started, stopped or finished respectively. This option causes them to return without waiting once the request has been confirmed.</p>
<dt><code>&#8211;quiet</code></p>
<dd>Reduces output of all commands to errors only.</dl>
<h2>Commands</h2>
<dl>
<dt><code>start </code><i>JOB</i>&#8230;</p>
<dd>Requests that the named jobs be started. The status of the jobs will be output to standard output until they are succesfully running, or in the case of tasks, until they have completed. </p>
<p> See <code>status</code> for a description of the output format.</p>
<dt><code>stop </code><i>JOB</i>&#8230;</p>
<dd>Requests that the named jobs be stopped. The status of the jobs will be output to standard output until they are successfully stopped. </p>
<p> When called with an instance job, all instances will be stopped. </p>
<p> See <code>status</code> for a description of the output format.</p>
<dt><code>status </code><i>JOB</i>&#8230;</p>
<dd>Requests the status of the named jobs. For each job on the command-line, a line like the following is output. </p>
<pre> job (start) running, process 1234</pre>
<p>The job name is given first; the goal of the job, either <i>start</i> or <i>stop</i> is then given in parens followed by the current state of the job. If there is an associated process, the pid is given. </p>
<p> Some job states may have multiple processes associated, for example when the job is in the <i>post-start</i> or <i>pre-stop</i> states. The extra processes follow on consecutive lines, indented by a tab. </p>
<pre> job (start) post-start, process 1347
 main process 1234</pre>
<p>If no <i>post-start</i> or <i>pre-stop</i> process exists, only one line is output. If there&#8217;s a <i>main</i> process running, that is included on the same line preceeded by <i>(main)</i>. </p>
<pre> job (stop) pre-stop, (main) process 1234</pre>
<p>Instance jobs are output with the first line giving the name of the job, and consecutive lines giving the state of each instance indented by four spaces. </p>
<pre> job (instance)
 (start) running, process 1234
 (start) post-start, process 2358
 main process 2345
 (stop) pre-stop, (main) process 3456</pre>
<dt><code>list</code> [<i>PATTERN</i>]</p>
<dd>Requests a list of the known jobs and their statuses. The optional pattern may contain the usual shell wildcard and glob characters, if omitted all known jobs are returned. </p>
<p> See <code>status</code> for a description of the output format.</p>
<dt><code>emit </code><i>EVENT</i></p>
<dd>Requests that the named event be emitted, potentially causing jobs to be started and stopped. The event information is output once handling begins followed by each job status changed caused by the event until handling is finished. </p>
<pre> fstab-device-added hda1
 FSTAB_FSNAME=/dev/hda1
 FSTAB_DIR=/
 FSTAB_TYPE=ext3
 FSTAB_OPTS=default</pre>
<p>The event name is given first followed by each argument to the event separated by a space. Consecutive lines are indented and give the environment variables passed to any job changed by the event. </p>
<p> See <code>status</code> for a description of the output format for the job status changes.</p>
<dt><code>jobs</code></p>
<dd>Requests notification of all job state changes be sent to the process, which remains in the foreground until terminated. </p>
<p> See <code>status</code> for a description of the output format.</p>
<dt><code>events</code></p>
<dd>Requests notification of all generated events be sent to the process, which remains in the foreground until terminated. </p>
<p> See <code>emit</code> for a description of the output format of the event messages.</p>
<dt><code>version</code></p>
<dd>Requests and outputs the version of the running init daemon.</p>
<dt><code>log-priority </code><i>PRIORITY</i></p>
<dd>Changes the minimum priority of messages logged by the init daemon. </p>
<p> <i>PRIORITY</i> may be one of <i>debug</i>, <i>info</i>, <i>message</i>, <i>warn</i>, <i>error</i> or <i>fatal</i>.</dl>
<h2>Author</h2>
<p>Written by Scott James Remnant.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs at <a rel="nofollow" href="https://launchpad.net/products/upstart/+bugs">https://launchpad.net/products/upstart/+bugs</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2007 Canonical Ltd.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-init/">init</a></code>(8) <code><a href="/docs/linux/man/8-telinit/">telinit</a></code>(8) </p>
