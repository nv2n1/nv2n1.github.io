---
title: "pbsdsh(1)"
name: "pbsdsh"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pbsdsh/"
description: "pbsdsh – distribute task to nodes under pbs"
---

<h2 class="name">NAME</h2>
<p> pbsdsh &#8211; distribute task to nodes under pbs </p>
<h2>SYNOPSIS</h2>
<p> pbsdsh [-c copies] [-o] [-s] [-u] [-v] program [args]<br />
 pbsdsh [-n node] [-o] [-s] [-u] [-v] program [args]<br />
 pbsdsh [-h nodename] [-o] [-v] program [args]</p>
<h2>DESCRIPTION</h2>
<p> Executes (spawns) a normal Unix program on one or more nodes under control of the Portable Batch System, PBS. Pbsdsh uses the Task Manager API, see <a href="/docs/linux/man/3-tm_spawn/">tm_spawn</a>(3), to distribute the program on the allocated nodes. </p>
<p> When run without the -c or the -n option, pbsdsh will spawn the program on all nodes allocated to the PBS job. The spawns take place concurrently &#8211; all execute at (about) the same time. </p>
<p> Users will find the <code>PBS_TASKNUM</code> , <code>PBS_NODENUM</code> , and the <code>PBS_VNODENUM</code> environmental variables useful. They contain the TM task id, the node identifier, and the cpu (virtual node) identifier.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-c copies</p>
<dd> The program is spawned on the first <i> nodes allocated. This option is mutual exclusive with -n.</p>
<dt>-n node</p>
<dd> The program is spawned on one node which is the node allocted. This option is mutual exclusive with -c.</p>
<dt>-h hostname</p>
<dd> The program is spawned on the node specified.</p>
<dt>-o</p>
<dd> Capture stdout of the spawned program. Normally stdout goes to the job&#8217;s output.</p>
<dt>-s</p>
<dd> If this option is given, the program is run in turn on each node, one after the other.</p>
<dt>-u</p>
<dd> The program is run once on each node (unique). This ignores the number of allocated processers on a given node.</p>
<dt>-v</p>
<dd> Verbose output about error conditions and task exit status is produced.</dl>
<p> </i></p>
<h2>OPERANDS</h2>
<p> The first operand, <i> is the program to execute. </p>
<p> Additional operands, are passed as arguments to the program. </i></p>
<h2>STANDARD ERROR</h2>
<p> The pbsdsh command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the command, the exit status will be a value of zero. </p>
<p> If the pbsdsh command fails to process any operand, or fails to contact the MOM daemon on the localhost the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-tm_spawn/">tm_spawn</a>(3B) </p>
<h2>Index</h2>
