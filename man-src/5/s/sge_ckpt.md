---
title: "sge_ckpt(5)"
name: "sge_ckpt"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sge_ckpt/"
description: "xxqs_name_sxx_ckpt – the xxQS_NAMExx checkpointing mechanism and checkpointing support"
---

<p>xxqs_name_sxx_ckpt &#8211; the xxQS_NAMExx checkpointing mechanism and checkpointing support</p>
<h2>Description</h2>
<p>xxQS_NAMExx supports two levels of checkpointing: the user level and an operating system-provided transparent level. User level checkpointing refers to applications which do their own checkpointing by writing restart files at certain times or algorithmic steps and by properly processing these restart files when restarted. Transparent checkpointing has to be provided by the operating system and is usually integrated in the operating system kernel. Checkpointing jobs need to be identified to the xxQS_NAMExx system by using the <i>-ckpt</i> option of the command. The argument to this flag refers to a so called checkpointing environment, which defines the attributes of the checkpointing method to be used (see for details). Checkpointing environments are setup by the options <i>-ackpt</i>, <i>-dckpt</i>, <i>-mckpt</i> and <i>-sckpt</i>. The option <i>-c</i> can be used to overwrite the <i>when</i> attribute for the referenced checkpointing environment. As opposed to the behavior for regular batch jobs, checkpointing jobs (see the <code>-ckpt</code> option to are aborted under conditions for which batch or interactive jobs are suspended or even stay unaffected. These conditions are:</p>
<dl>
<dt>&bull;</p>
<dd>Explicit suspension of the queue or job via by the cluster administration or a queue owner if the <i>x</i> occasion specifier (see <i>-c</i> and was assigned to the job.</p>
<dt>&bull;</p>
<dd>A load average value exceeding the suspend threshold as configured for the corresponding queues (see</p>
<dt>&bull;</p>
<dd>Shutdown of the xxQS_NAMExx execution daemon being responsible for the checkpointing job.</dl>
<p> After they are aborted, jobs will migrate to other hosts, and possibly other cluster queues, unless they were submitted to a specific one by an explicit user request. The migration of jobs leads to a dynamic load balancing. <code>Note:</code> Aborting checkpointed jobs will free all resources (memory, swap space) which the job occupies at that time. This is opposed to the situation for suspended regular jobs, which still use virtual memory and other consumable resources. </p>
<h2>Restrictions</h2>
<p>When a job migrates to another machine, at present no files are transferred automatically to that machine. This means that all files which are used throughout the entire job, including restart files, executables, and scratch files, must be visible or transferred explicitly (e.g. at the beginning of the job script). </p>
<p> There are also some practical limitations regarding use of disk space for transparently checkpointing jobs. Checkpoints of a transparently checkpointed application are usually stored in a checkpoint file or directory by the operating system. The file or directory contains all the text, data, and stack space for the process, along with some additional control information. This means jobs which use a very large virtual address space will generate very large checkpoint files. Also the workstations on which the jobs will actually execute may have little free disk space. Thus it is not always possible to transfer a transparent checkpointing job to a machine, even though that machine is idle. Since large virtual memory jobs must wait for a machine that is both idle, and has a sufficient amount of free disk space, such jobs may suffer long turnaround times. </p>
<p> There is currently no mechanism for restarting jobs with the same resources they were granted originally. That might be important if they were submitted with a choice or range of resources and start running in a particular way with what they&#8217;re given. </p>
<p> Similarly, with heterogeneous execution hosts, jobs may need to restart on a host which supports a superset of the instruction set where the job originally ran if the checkpoint mechanism (e.g. BLCR or DMTCP) dumps an image of the running process. Runtime libraries, in particular, may initialize themselves depending on details of the architecture they start up on &#8211; say to use a specific type of vector unit. Then, they may fail if moved to an older host of similar architecture which lacks that feature, even if they were compiled for a common instruction set.</p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
