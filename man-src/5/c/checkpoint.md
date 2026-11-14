---
title: "checkpoint(5)"
name: "checkpoint"
section: "5"
letter: "c"
url: "/docs/linux/man/5-checkpoint/"
description: "checkpoint – xxQS_NAMExx checkpointing environment configuration file format"
---

<p>checkpoint &#8211; xxQS_NAMExx checkpointing environment configuration file format</p>
<h2>Description</h2>
<p>Checkpointing is a facility to save the complete status of an executing program or job and to restore and restart from this so-called checkpoint at a later point of time if the original program or job was halted, e.g. through a system crash. </p>
<p> xxQS_NAMExx provides various levels of checkpointing support (see The checkpointing environment described here is a means to configure the different types of checkpointing in use for your xxQS_NAMExx cluster or parts thereof. For that purpose you can define the operations which have to be executed in initiating a checkpoint generation, a migration of a checkpoint to another host, or a restart of a checkpointed application. </p>
<p> Supporting different operating systems may easily force xxQS_NAMExx to introduce operating system dependencies for the configuration of the checkpointing configuration file and updates of the supported operating system versions may lead to frequently changing implementation details. Please refer to the &lt;xxqs_name_sxx_root&gt;/ckpt directory for more information. </p>
<p> Please use the <i>-ackpt</i>, <i>-dckpt</i>, <i>-mckpt</i> or <i>-sckpt</i> options to the command to manipulate checkpointing environments from the command-line or use the corresponding dialogue for X-Windows based interactive configuration. </p>
<p> Note, xxQS_NAMExx allows backslashes (\) be used to escape newline characters. The backslash and the newline are replaced with a space character before any interpretation.</p>
<h2>Format</h2>
<p>The format of a <i>checkpoint</i> file is defined as follows:</p>
<h3><code>ckpt_name</code></h3>
<p>The name of the checkpointing environment in the format for <i>ckpt_name</i> in To be used in the <code>-ckpt</code> switch or for the options mentioned above.</p>
<h3><code>interface</code></h3>
<p>The type of checkpointing to be used. Currently, the following types are valid:</p>
<dl>
<dt><i>hibernator</i></p>
<dd>The Hibernator kernel level checkpointing is interfaced.</p>
<dt><i>cpr</i></p>
<dd>The SGI kernel level checkpointing is used.</p>
<dt><i>transparent</i></p>
<dd>xxQS_NAMExx assumes that the jobs submitted with reference to this checkpointing interface use a checkpointing library such as provided by the free package <i>Condor</i>.</p>
<dt><i>userdefined</i></p>
<dd>xxQS_NAMExx assumes that the jobs submitted with reference to this checkpointing interface perform their private checkpointing method.</p>
<dt><i>application-level</i></p>
<dd>Uses all of the interface commands configured in the checkpointing object like in the case of one of the kernel level checkpointing interfaces (<i>cpr</i>, etc.) except for the <code>restart_command</code> (see below), which is not used (even if it is configured) but the job script is invoked in case of a restart instead.</dl>
<h3><code>ckpt_command</code></h3>
<p>A command-line type command string to be executed by xxQS_NAMExx in order to initiate a checkpoint. The following pseudo-variables are available to be substituted in the value:</p>
<dl>
<dt><code>$host</code></p>
<dd>The name of the host on which the command is executed.</p>
<dt><code>$ja_task_id</code></p>
<dd>The array job task index (0 if not an array job).</p>
<dt><code>$job_owner</code></p>
<dd>The user name of the job owner.</p>
<dt><code>$job_id</code></p>
<dd>xxQS_NAMExx&#8217;s unique job identification number.</p>
<dt><code>$job_name</code></p>
<dd>The name of the job.</p>
<dt><code>$queue</code></p>
<dd>The cluster queue name of the master queue instance, on which the command is started.</p>
<dt><code>$job_pid</code></p>
<dd>The process id of the job/task to checkpoint.</p>
<dt><code>$ckpt_dir</code></p>
<dd>See <code>ckpt_dir</code> below.</p>
<dt><code>$ckpt_signal</code></p>
<dd>See <code>signal</code> below.</p>
<dt><code>$sge_cell</code></p>
<dd>The SGE_CELL environment variable (useful for locating files).</p>
<dt><code>$sge_root</code></p>
<dd>The SGE_ROOT environment variable (useful for locating files).</dl>
<h3><code>migr_command</code></h3>
<p>A command-line type command string to be executed by xxQS_NAMExx during a migration of a checkpointing job from one host to another. The same pseudo-variables are available as for <code>ckpt_command</code>. Note that the command is expected to create a checkpoint itself &#8211; the checkpointing command isn&#8217;t called automatically on migration.</p>
<h3><code>restart_command</code></h3>
<p>A command-line type command string to be executed by xxQS_NAMExx when restarting a previously checkpointed application. The same pseudo-variables are available as for <code>ckpt_command</code>.</p>
<h3><code>clean_command</code></h3>
<p>A command-line type command string to be executed by xxQS_NAMExx in order to cleanup after a checkpointed application has finished. The same pseudo-variables are available as for <code>ckpt_command</code>.</p>
<h3><code>ckpt_dir</code></h3>
<p>A file system location to which checkpoints of potentially considerable size should be stored.</p>
<h3><code>signal</code></h3>
<p>A Unix signal to be sent to a job by xxQS_NAMExx to initiate checkpoint generation. The value for this field can either be a symbolic name from the list produced by the <i>-l</i> option of the <i><a href="/docs/linux/man/1-kill/">kill</a></i>(1) command or an integer number which must be a valid signal on the systems used for checkpointing.</p>
<h3><code>when</code></h3>
<p>The points of time when checkpoints are expected to be generated. Valid values for this parameter are composed from the letters <i>s</i>, <i>m</i>, <i>x</i>, <i>r</i>, and any combinations thereof without any separating character in between. The same letters are allowed for the <i>-c</i> option of the command which will overwrite the definitions in the checkpointing environment used. The meaning of the letters is as follows:</p>
<dl>
<dt><i>s</i></p>
<dd>A job is checkpointed, aborted and, if possible, migrated if the corresponding is shut down on the job&#8217;s host. This operation is handled by the specified <code>migr_command</code>.</p>
<dt><i>m</i></p>
<dd>checkpoints are generated periodically at the <i>min_cpu_interval</i> interval defined by the queue (see in which a job executes.</p>
<dt><i>x</i></p>
<dd>A job is checkpointed, aborted and, if possible, migrated as soon as the job gets suspended (manually as well as automatically). This operation is handled by the specified <code>migr_command</code>.</p>
<dt><i>r</i></p>
<dd>A job will be rescheduled (not checkpointed) when the host on which the job currently runs goes into the &quot;unknown&quot; state and the time interval <i>reschedule_unknown</i> (see defined in the global/local cluster configuration is exceeded.</dl>
<h2>Environment Variables</h2>
<p><code>xxQS_NAME_Sxx_BINDING</code> and <code>xxQS_NAME_Sxx_CKPT_DIR</code> may be specified on job submission. See</p>
<h2>Restrictions</h2>
<p><code>Note</code> that the functionality of any checkpointing, migration or restart procedures provided by default with the xxQS_NAMExx distribution, as well as the way how they are invoked in the <i>ckpt_command</i>, <i>migr_command</i> or <i>restart_command</i> parameters of any default checkpointing environments, should not be changed; otherwise the functionality remains the full responsibility of the administrator configuring the checkpointing environment. xxQS_NAMExx will just invoke these procedures and evaluate their exit status. If the procedures do not perform their tasks properly, or are not invoked in a proper fashion, the checkpointing mechanism may behave unexpectedly; xxQS_NAMExx has no means to detect this &#8211; all exit codes are treated as successful operation except for the case of kernel checkpointing. </p>
<p> See also the restrictions in</p>
<h2>See Also</h2>
<h2>Copyright</h2>
<p>See for a full statement of rights and permissions.</p>
