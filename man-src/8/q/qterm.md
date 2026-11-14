---
title: "qterm(8)"
name: "qterm"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qterm/"
description: "qterm – terminate processing by a PBS batch server"
---

<p>qterm &#8211; terminate processing by a PBS batch server</p>
<h2>Synopsis</h2>
<p>qterm [-t type] [server&#8230;]</p>
<h2>Description</h2>
<p>The <code>qterm </code> command terminates a PBS batch server. When a server receives a terminate command, the server will go into a <i>terminating</i> state. While in this state, the server will not allow new jobs to be started or enqueued. By default, qterm will request a &quot;quick&quot; shutdown of the PBS server. Other ways of shutting down the server (specified with the -t argument), and their impact on running jobs, are described below. The qterm command will not exit until the server has completed its shutdown procedure. </p>
<p> In order to execute qterm, the user must have PBS Operation or Manager privilege.</p>
<h2>Options</h2>
<dl>
<dt>-t type</p>
<dd>Specifies the type of shut down. The types are:</p>
<dl>
<dd>
<dl>
<dt>immediate</p>
<dd>All running jobs are to immediately stop execution.</p>
<dd>If checkpoint is supported, running jobs that were submitted with &quot;-c shutdown&quot; are checkpointed, terminated, and requeued. If checkpoint is not supported or the job cannot be checkpointed, running jobs are requeued if the <i> </i><font SIZE="-1"><i> attribute is true. Otherwise, jobs are killed.</p>
<dd>Normally the server will not shutdown until there are no jobs in the running state. If the server is unable to contact the MOM of running job, the job is still listed as running. The server may be forced down by a second qterm -t immediate command.</p>
<dt>delay&nbsp;<wbr></p>
<dd>If checkpoint is supported, running jobs that were submitted with &quot;-c shutdown&quot; are checkpointed, terminated, and requeued. If a job cannot be checkpointed, but can be rerun, the job is terminated and requeued. Otherwise, running jobs are allowed to continue to run. Note, the operator or administrator may use the qrerun and qdel commands to remove running jobs.</p>
<dt>quick&nbsp;<wbr></p>
<dd>This option is used when you wish that running jobs be left running when the server shuts down. The server will cleanly shutdown and can be restarted when desired. Upon restart of the server, jobs that continue to run are shown as running; jobs that terminated during the server&#8217;s absence will be placed into the exiting state.</dl>
</dl>
</dl>
<p> </i></font></p>
<h2>Operands</h2>
<p>The <i> operand specifies which servers are to shutdown. If no servers are given, then the default server will be terminated. </i></p>
<h2>Standard Error</h2>
<p>The qterm command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>Exit Status</h2>
<p>Upon successful processing of all the operands presented to the qterm command, the exit status will be a value of zero. </p>
<p> If the qterm command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>See Also</h2>
<p><a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B), <a href="//www.systutorials.com/docs/linux/man/1B-qmgr/">qmgr</a>(1B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_aix4/">pbs_resources_aix4</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_irix5/">pbs_resources_irix5</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_sp2/">pbs_resources_sp2</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_sunos4/">pbs_resources_sunos4</a>(7B), and <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_unicos8/">pbs_resources_unicos8</a>(7B) </p>
