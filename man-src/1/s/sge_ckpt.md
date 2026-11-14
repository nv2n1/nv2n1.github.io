---
title: "sge_ckpt(1)"
name: "sge_ckpt"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sge_ckpt/"
description: "Grid Engine Checkpointing – the Grid Engine checkpointing mechanism and checkpointing support"
---

<h2 class="name">NAME</h2>
<p> Grid Engine Checkpointing &#8211; the Grid Engine checkpointing mechanism and checkpointing support </p>
<h2>DESCRIPTION</h2>
<p> Grid Engine supports two levels of checkpointing: the user level and a operating system provided transparent level. User level checkpointing refers to applications, which do their own checkpointing by writing restart files at certain times or algorithmic steps and by properly processing these restart files when restarted. </p>
<p> Transparent checkpointing has to be provided by the operating system and is usually integrated in the operating system kernel. An example for a kernel integrated checkpointing facility is the Hibernator package from Softway for SGI IRIX platforms. </p>
<p> Checkpointing jobs need to be identified to the Grid Engine system by using the <i>-ckpt</i> option of the command. The argument to this flag refers to a so called checkpointing environment, which defines the attributes of the checkpointing method to be used (see for details). Checkpointing environments are setup by the options <i>-ackpt</i>, <i>-dckpt</i>, <i>-mckpt</i> and <i>-sckpt</i>. The option <i>-c</i> can be used to overwrite the <i>when</i> attribute for the referenced checkpointing environment. </p>
<p> If a queue is of the type CHECKPOINTING, jobs need to have the checkpointing attribute flagged (see the <code>-ckpt</code> option to to be permitted to run in such a queue. As opposed to the behavior for regular batch jobs, checkpointing jobs are aborted under conditions, for which batch or interactive jobs are suspended or even stay unaffected. These conditions are:</p>
<dl>
<dt>*</p>
<dd> Explicit suspension of the queue or job via by the cluster administration or a queue owner if the <i>x</i> occasion specifier (see <i>-c</i> and was assigned to the job.</p>
<dt>*</p>
<dd> A load average value exceeding the migration threshold as configured for the corresponding queues (see</p>
<dt>*</p>
<dd> Shutdown of the Grid Engine execution daemon being responsible for the checkpointing job.</dl>
<p> After abortion, the jobs will migrate to other queues unless they were submitted to one specific queue by an explicit user request. The migration of jobs leads to a dynamic load balancing. <code>Note:</code> The abortion of checkpointed jobs will free all resources (memory, swap space) which the job occupies at that time. This is opposed to the situation for suspended regular jobs, which still cover swap space. </p>
<h2>RESTRICTIONS</h2>
<p> When a job migrates to a queue on another machine at present no files are transferred automatically to that machine. This means that all files which are used throughout the entire job including restart files, executables and scratch files must be visible or transferred explicitly (e.g. at the beginning of the job script). </p>
<p> There are also some practical limitations regarding use of disk space for transparently checkpointing jobs. Checkpoints of a transparently checkpointed application are usually stored in a checkpoint file or directory by the operating system. The file or directory contains all the text, data, and stack space for the process, along with some additional control information. This means jobs which use a very large virtual address space will generate very large checkpoint files. Also the workstations on which the jobs will actually execute may have little free disk space. Thus it is not always possible to transfer a transparent checkpointing job to a machine, even though that machine is idle. Since large virtual memory jobs must wait for a machine that is both idle, and has a sufficient amount of free disk space, such jobs may suffer long turnaround times.</p>
<h2>SEE ALSO</h2>
<p> <i>Grid Engine Installation and Administration Guide,</i> <i>Grid Engine User&#8217;s Guide</i></p>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
