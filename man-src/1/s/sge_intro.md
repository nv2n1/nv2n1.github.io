---
title: "sge_intro(1)"
name: "sge_intro"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sge_intro/"
---

<h2 class="name">NAME</h2>
 

 sge_intro - xxQS_NAMExx, a facility for executing jobs on remote machines 

<h2>DESCRIPTION</h2>

 xxQS_NAMExx is a facility for executing Unix-like batch jobs (shell scripts or binaries) on a pool of cooperating CPUs. Jobs are queued and executed remotely according to defined policies. The CPUs may be in desktop systems, with jobs run on them at times when they would otherwise be idle or only lightly loaded. The work load may be distributed according to the (generalized) load situation of each machine and the resource requirements of the jobs. 

 User level checkpointing programs are supported and a transparent checkpointing mechanism is provided (see Checkpointing jobs migrate from system to system without user intervention on load demand. In addition to simple batch jobs, interactive jobs and parallel jobs can also be submitted to xxQS_NAMExx. 

<h2>USER INTERFACE</h2>

 The xxQS_NAMExx user interface consists of several programs which are described separately.
<dl>
<dt>
<dd> <i>qacct</i> extracts arbitrary accounting information from the cluster logfile.
<dt>
<dd> <i>qalter</i> changes the characteristics of already submitted jobs.
<dt>
<dd> <i>qconf</i> provides the user interface for configuring, modifying, deleting and querying queues and the cluster configuration.
<dt>
<dd> <i>qdel</i> provides the means for a user/operator/manager to cancel jobs.
<dt>
<dd> <i>qevent</i> provides a means of watching xxQS_NAMExx events and acting on jobs finishing.
<dt>
<dd> <i>qhold</i> holds back submitted jobs from execution.
<dt>
<dd> <i>qhost</i> displays status information about xxQS_NAMExx execution hosts.
<dt>
<dd> <i>qlogin</i> initiates a telnet or similar login session with automatic selection of a suitable host.
<dt>
<dd> <i>qmake</i> is a replacement for the standard Unix <i>make</i> facility. It extends make with an ability to distribute independent make steps across a cluster of suitable machines.
<dt>
<dd> <i>qmod</i> allows the owner(s) of a queue to suspend and enable queues, e.g. all queues associated with his machine (all currently active processes in this queue are also signaled) or to suspend and enable jobs executing in the queues.
<dt>
<dd> <i>qmon</i> provides a Motif command interface to all xxQS_NAMExx functions. The status of all, or a private selection of, the configured queues is displayed on-line by changing colors at corresponding queue icons.
<dt>
<dd> <i>qping</i> can be used to check the status of xxQS_NAMExx daemons.
<dt>
<dd> <i>qquota</i> provides a status listing of all currently used resource quotas (see
<dt>
<dd> <i>qresub</i> creates new jobs by copying currently running or pending jobs.
<dt>
<dd> <i>qrls</i> releases holds from jobs previously assigned to them e.g. via (see above).
<dt>
<dd> <i>qrdel</i> provides the means to cancel advance reservations.
<dt>
<dd> <i>qrsh</i> can be used for various purposes such as providing remote execution of interactive applications via xxQS_NAMExx comparable to the standard Unix facility rsh, to allow for the submission of batch jobs which, upon execution, support terminal I/O (standard/error output and standard input) and terminal control, to provide a batch job submission client which remains active until the job has finished or to allow for the xxQS_NAMExx-controlled remote execution of the tasks of parallel jobs.
<dt>
<dd> <i>qrstat</i> provides a status listing of all advance reservations in the cluster.
<dt>
<dd> <i>qrsub</i> is the user interface for submitting an advance reservation to xxQS_NAMExx.
<dt>
<dd> <i>qselect</i> prints a list of queue names corresponding to specified selection criteria. The output of <i>qselect</i> is usually fed into other xxQS_NAMExx commands to apply actions on a selected set of queues.
<dt>
<dd> <i>qsh</i> opens an interactive shell (in an on a low loaded host. Any kind of interactive job can be run in this shell.
<dt>
<dd> <i>qstat</i> provides a status listing of all jobs and queues associated with the cluster.
<dt>
<dd> <i>qtcsh</i> is a fully compatible replacement for the widely known and used Unix C-Shell (<i>csh</i>) derivative <i>tcsh</i>. It provides a command-shell with the extension of transparently distributing execution of designated applications to suitable and lightly loaded hosts via xxQS_NAMExx.
<dt>
<dd> <i>qsub</i> is the user interface for submitting a job to xxQS_NAMExx.</dl>

<h2>SEE ALSO</h2>

<h2>COPYRIGHT</h2>

 Copyright: 2008 by Sun Microsystems, Inc. Parts of the manual page texts are Copyright 2011 Univa Corporation, and various dates by other contributors. The manual pages are licensed under the Sun Industry Standards Source License, like the source, except where noted in some files by other contributors, which are under other free licences noted in their source. 

<h2>Index</h2>


