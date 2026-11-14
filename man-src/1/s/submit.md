---
title: "submit(1)"
name: "submit"
section: "1"
letter: "s"
url: "/docs/linux/man/1-submit/"
description: "qsub, qsh, qlogin, qrsh, qalter, qresub – submit jobs to xxQS_NAMExx"
---

<h2 class="name">NAME</h2>
<p> qsub, qsh, qlogin, qrsh, qalter, qresub &#8211; submit jobs to xxQS_NAMExx</p>
<h2>SYNTAX</h2>
<p> <code>qsub</code> [<i>options</i>] [<i>command</i> [<i>command_args</i>] | <code>&#8212;</code> [<i>command_args</i>]] </p>
<p> <code>qsh</code> [<i>options</i>] [<code>&#8212;</code> <i>xterm_args</i>] </p>
<p> <code>qlogin</code> [<i>options</i>] </p>
<p> <code>qrsh</code> [<i>options</i>] [<i>command</i> [<i>command_args</i>]] </p>
<p> <code>qalter</code> [<i>options</i>] <i>wc_job_range_list</i> [<code>&#8212;</code> [<i>command_args</i>]] </p>
<p> <code>qalter</code> [<i>options</i>] <code>-u </code> <i>user_list</i> | <code>-u *</code> [<code>&#8212;</code> [<i>command_args</i>]] </p>
<p> <code>qresub</code> [<i>options</i>] <i>job_id_list</i></p>
<h2>DESCRIPTION</h2>
<p> <i>Qsub</i> submits batch jobs to the xxQS_NAMExx queuing system. xxQS_NAMExx supports single- and multiple-node jobs. <i>command</i> can be a path to a binary or a script (see <code>-b</code> below) which contains the commands to be run by the job using a shell (for example, or Arguments to the command are given as <i>command_args</i> to <i>qsub</i>. If <i>command</i> is handled as a script then it is possible to embed flags in the script. If the first two characters of a script line either match &#8216;#$&#8217; or are equal to the prefix string defined with the <code>-C</code> option described below, the line is parsed for embedded command flags. </p>
<p> <i>Qsh</i> submits an interactive X-windows session to xxQS_NAMExx. An is brought up from the executing machine with the display directed either to the X-server indicated by the DISPLAY environment variable or as specified with the <code>-display</code> option of <i>qsh</i>. Interactive jobs are not spooled if no resource is available to execute them. They are either dispatched to a suitable machine for execution immediately or the user submitting the job is notified by <i>qsh</i> that appropriate resources to execute the job are not available. <i>xterm_args</i> are passed to the executable. Note, however, that the <i>-e</i> and <i>-ls</i> xterm options do not work with <i>qsh</i>. </p>
<p> <i>Qlogin</i> is similar to <i>qsh</i> in that it submits an interactive job to the queuing system. It does not open an window on the X display, but uses the current terminal for user I/O. It establishes a connection with the remote host, using the configured mechanisms described in <i>Qlogin</i> is invoked exactly like <i>qsh</i> and its jobs can only run on INTERACTIVE queues. <i>Qlogin</i> jobs can only be used if the is running under the root account. </p>
<p> <i>Qrsh</i> is similar to <i>qlogin</i> in that it submits an interactive job to the queuing system. It uses the current terminal for user I/O. With a command, it establishes a connection with the remote host. If no command is given to <i>qrsh</i>, an session is established. It uses the configured mechanisms described in <i>Qrsh</i> jobs can only run in INTERACTIVE queues unless the option <code>-now no</code> is used (see below). They can also only be run if the is running under the root account. </p>
<p> <i>Qrsh</i> provides an additional useful feature for integrating with interactive tools providing a specific command shell. If the environment variable <code>QRSH_WRAPPER</code> is set when <i>qrsh</i> is invoked, the executable it names will be executed to run <i>qrsh</i> commands instead of the user&#8217;s login shell or any shell specified in the <i>qrsh</i> command-line; it is passed the command line arguments, not <code>-c</code> and a string as for shell invocation. The options <code>-cwd</code>, <code>-v</code>, <code>-V</code>, and <code>-display</code> only apply to batch jobs. </p>
<p> <i>Qalter</i> can be used to change the attributes of pending jobs. For array jobs with a mix of running and pending tasks (see the <code>-t</code> option below), modification with <i>qalter</i> only affects the pending tasks. <i>Qalter</i> can change most of the characteristics of a job (see the corresponding statements in the OPTIONS section below), including those which were defined as embedded flags in the script file (see above). An option specified with <i>qalter</i> completely replaces any parameters previously specified for the job by that option, e.g. if the job has a resource requirement corresponding to <code>-l h_rt=3600,h_vmem=2G</code>, then after a <code>qalter -l h_rt=7200</code>, the resource requirement is simply <code>h_rt=7200</code>; it is not currently possible to override one or more values. </p>
<p> Some submit options, such as the job script, cannot be changed with <i>qalter</i>. If parameters are set with <i>qalter</i>, the output from <code>qstat -j</code> acquires an additional field, <code>version</code>, which is incremented each time. </p>
<p> If a server JSV is defined, modifications are forbidden unless they are explicitly allowed by the parameter <code>jsv_allowed_mod</code>. (See also </p>
<p> <i>Qresub</i> allows the user to create jobs as copies of existing pending or running jobs. The copied jobs will have exactly the same attributes as the ones from which they were copied, except with a new job ID and with a cleared hold state. The only modification to the copied jobs supported by <i>qresub</i> is assignment of a new hold state with the <code>-h</code> option. This option can be used to first copy a job and then change its attributes via <i>qalter</i>. </p>
<p> Only a manager can use <i>qresub</i> on jobs submitted by another user. Regular users can only use <i>qresub</i> on their own jobs. </p>
<p> See for the significance of exit codes returned by the submitted job. </p>
<p> For <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, and <i>qlogin</i> the administrator and the user may define default request files (see which can contain any of the options described below. If an option in a default request file is understood by <i>qsub</i> and <i>qlogin</i> but not by <i>qsh</i> the option is silently ignored if <i>qsh</i> is invoked. Thus you can maintain shared default request files for both <i>qsub</i> and <i>qsh</i>. </p>
<p> A cluster-wide default request file may be placed under <i>$xxQS_NAME_Sxx_ROOT/$xxQS_NAME_Sxx_CELL/common/xxqs_name_sxx_request</i>. User private default request files are processed under the locations <i>$HOME/.xxqs_name_sxx_request</i> and <i>$cwd/.xxqs_name_sxx_request</i>. The working directory local default request file has the highest precedence, then the home directory file and then the cluster global file. The option arguments, the embedded script flags and the options in the default request files are processed in the following order: </p>
<dl>
<dt>
<dd>
<pre>
left to right in the script line,
left to right in the default request files,
from top to bottom of the script file (<i>qsub</i> only),
from top to bottom of default request files,
from left to right of the command line.
</pre>
</dl>
<p> In other words, the command line can be used to override the embedded flags and the default request settings. The embedded flags, however, will override the default settings. </p>
<p> <code>Note</code>, that the <code>-clear</code> option can be used to discard any previous settings at any time in a default request file, in the embedded script flags, or in a command-line option. It is, however, not available with <i>qalter</i>. </p>
<p> The request options described below can be requested either hard or soft. By default, all requests are considered hard until the <code>-soft</code> option (see below) is encountered. The hard/soft status remains in effect until its counterpart is encountered again. If all the hard requests for a job cannot be met, the job will not be scheduled. Jobs which cannot be run at the present time remain spooled.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-@</code> <i>optionfile</i></p>
<dd> Forces <i>qsub</i>, <i>qrsh</i>, <i>qsh</i>, or <i>qlogin</i> to use the options contained in <i>optionfile</i>. The indicated file may contain all valid options. Comment lines must start with a &quot;#&quot; sign.</p>
<dt><code>-a</code> <i>date_time</i></p>
<dd> Available for <i>qsub</i> and <i>qalter</i> only. </p>
<p> Defines or redefines the time and date at which a job is eligible for execution. <i>date_time</i> is of the form [[<i>CC</i>]<i>YY</i>]<i>MMDDhhmm</i>[<code>.</code><i>SS</i>]; for the details, please see <code>date_time</code> in </p>
<p> If this option is used with <i>qsub</i> or if a corresponding value is specified in <i>qmon</i> then a parameter named <code>a</code> and the value in the format CCYYMMDDhhmm.SS will be passed to the defined JSV instances. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-ac</code> <i>variable</i>[<code>=</code><i>value</i>]<code>,</code>&#8230;</p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Adds the given name/value pair(s) to the job&#8217;s context. <i>value</i> may be omitted. xxQS_NAMExx appends the given argument to the list of context variables for the job. Multiple <code>-ac</code>, <code>-dc</code>, and <code>-sc</code> options may be given. The order is important here. </p>
<p> The outcome of the evaluation of all <code>-ac</code>, <code>-dc</code>, and <code>-sc</code> options or corresponding values in <i>qmon</i> is passed to defined JSV instances as parameter with the name <code>ac</code>. (See <code>-jsv</code> option below or find more information concerning JSV in </p>
<p> <i>Qalter</i> allows changing this option even while the job executes.</p>
<dt><code>-ar</code> <i>ar_id</i></p>
<dd> Available for <i>qsub</i>, <i>qalter</i>, <i>qrsh</i>, <i>qsh</i>, or <i>qlogin</i> only. </p>
<p> Assigns the submitted job to be a part of an existing Advance Reservation with id <i>ar_id</i>. The complete list of existing Advance Reservations can be obtained using the command. </p>
<p> Note that the <code>-ar</code> option implicitly adds the <code>-w e</code> option if not otherwise requested. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job however. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>ar</code>. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-A</code> <i>account_string</i></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Identifies the account to which the resource consumption of the job should be charged. The <i>account_string</i> should conform to the <i>account_name</i> definition in In the absence of this parameter xxQS_NAMExx will place the default account string &quot;xxqs_name_sxx&quot; in the accounting record of the job. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>A</code>. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-b y</code>[<code>es</code>]|<code>n</code>[<code>o</code>]</p>
<dd> Available for <i>qsub</i>, <i>qrsh</i> only. <i>Qalter</i> does not allow changing this option. This option cannot be embedded in the script file itself. </p>
<p> Gives the user the possibility to indicate explicitly whether <i>command</i> should be treated as binary or script. If the argument of <code>-b</code> is &#8216;y&#8217;, then <i>command</i> may be a binary or script. The <i>command</i> might not be accessible from the submission host. Nothing except the path of the <i>command</i> will be transferred from the submission host to the execution host. Path aliasing will be applied to the path of <i>command</i> before it is executed. </p>
<p> If the argument of <code>-b</code> is &#8216;n&#8217; then <i>command</i> needs to be a script, and it will be handled as such. The script file has to be accessible by the submission host. It will be transferred to the execution host. <i>qsub</i>/<i>qrsh</i> will search directive prefixes within scripts. </p>
<p> <i>qsub</i> will implicitly use <code>-b n</code>, whereas <i>qrsh</i> will apply the <code>-b y</code> option if nothing else is specified. </p>
<p> The value specified with this option or the corresponding value specified in <i>qmon</i> will only be passed to defined JSV instances if the value is <i>yes</i>. The name of the parameter will be <code>b</code>. The value will be <code>y</code> also when the long form <code>yes</code> was specified during submission. (See <code>-jsv</code> option below or find more information concerning JSV in </p>
<p> Please note that submission of <i>command</i> as a script (<code>-b n</code>) can have a significant performance impact, especially for short running jobs and big job scripts. Script submission adds a number of operations to the submission process: The job script needs to be </p>
<pre>
- parsed at client side (for special comments)
- transferred from submit client to qmaster
- spooled in qmaster
- transferred to execd at job execution
- spooled in execd
- removed from spooling both in execd and qmaster once the job is done
</pre>
<p> If job scripts are available on the execution nodes, e.g. via NFS, binary submission can be the better choice.</p>
<dt><code>-binding</code> [<i>binding_instance</i>] <i>binding_strategy</i></p>
<dd> A job can request a specific processor core binding (processor affinity) with this parameter. This request is neither a hard nor a soft request, it is a hint for the execution host to do this if possible. Please note that the requested binding strategy is not used for resource selection within xxQS_NAMExx. As a result an execution host might be selected where xxQS_NAMExx does not even know the hardware topology and therefore is not able to apply the requested binding. (The binding facility depends on the platform, and on xxQS_NAMExx being compiled with appropriate support.) </p>
<p> To make xxQS_NAMExx select hardware on which the binding can be applied, please use the <code>-l</code> switch in combination with the complex attribute <code>m_topology</code>. </p>
<p> <i>binding_instance</i> is an optional parameter. It might either be <code>env</code>, <code>pe</code> or <code>set</code> depending on which instance should accomplish the job to core binding. If the value for <i>binding_instance</i> is not specified then <code>set</code> will be used. </p>
<p> <code>env</code> means that only the environment variable <code>xxQS_NAME_Sxx_BINDING</code> will be exported to the job environment of the job. This variable contains the selected operating system internal processor numbers. In presence of SMT or CMT it may contain more than the number of cores selected, because each core could be represented by multiple processor identifiers. The processor numbers are space-separated. </p>
<p> <code>pe</code> means that the information about the selected cores appears in the fourth column of the <code>pe_hostfile</code>. Here the logical core and socket numbers are printed (they start at 0 and have no holes) in colon-separated pairs (e.g. &quot;0,0:1,0&quot;, which means core 0 on socket 0 and core 0 on socket 1). For more information about the $pe_hostfile check In addition, <code>xxQS_NAME_Sxx_BINDING</code> is set as for <code>env</code> binding. </p>
<p> <code>set</code> (the default if nothing else is specified) means that the binding strategy is applied by xxQS_NAMExx. Each shepherd (on the master host, or those connected to with qrsh -inherit) is bound to the relevant cores. The binding is inherited by the task that is started, so that processes or threads it spawns are bound to those cores, but it is up to the task to make any more specific bindings of its sub-tasks within the set of bound cores it inherits. How xxQS_NAMExx does this depends on the underlying hardware architecture of the execution host where the submitted job will be started. In addition, <code>xxQS_NAME_Sxx_BINDING</code> is set as for <code>env</code> binding. </p>
<p> Binding will be done to restrict the job to run exclusively on the selected cores, if possible on the platform; otherwise bound processes may still be able to use other cores. The operating system will probably allow other unbound processes to use these cores. Note that if all cores on a node are specified to be bound by one job, that is probably equivalent to no binding, with the task free to use all the cores. </p>
<p> The <i>loadcheck</i> tool in the <i>utilbin</i> directory can be used to check the host&#8217;s capabilities. You can also use <code>-sep</code> in combination with <code>-cb</code> of to find whether xxQS_NAMExx is able to recognize the hardware topology. <i><a href="/docs/linux/man/1-hwloc-ps/">hwloc-ps</a></i>(1) can be used to check the bindings in force on a host. </p>
<p> Possible values for <i>binding_strategy</i> are as follows: </p>
<pre><code>
linear : [number[:socket, core]] striding : number : n[:socket, core] explicit : socket, core[:socket, core]...
</code></pre>
<p> For the binding strategies &quot;linear&quot; and &quot;striding&quot; there is an optional socket and core pair attached. These denote the mandatory starting point for the first core to bind on. Logical socket and core numbers are used, per <i><a href="/docs/linux/man/7-hwloc/">hwloc</a></i>(7). </p>
<p> <code>linear</code> means that xxQS_NAMExx tries to bind the job on <i>number</i> successive cores. If <i>socket</i> and <i>core</i> are omitted then xxQS_NAMExx first allocates successive cores on the first empty socket found. (&quot;Empty&quot; means that there are no jobs bound to the socket by xxQS_NAMExx.) If this is not possible, or is not sufficient, xxQS_NAMExx tries to find (further) cores on the socket with the most unbound cores, and so on. If <i>socket</i> and <i>core</i> are specified, then xxQS_NAMExx tries to find empty cores with this starting point. If the binding request cannot be satisfied, then binding is not done on the host concerned. <i>number</i> may be omitted or specified as <code>slots</code>. In that case it will be taken as the number of slots assigned to the job on a per-host basis, on the assumption that one slot per core is used. That allows binding to work when parallel jobs run across nodes with variable slot counts per node. Multiple processing units (hardware threads) per core are currently not taken into account in this, but systems running such parallel jobs will typically have only a single thread per core. <code>-binding linear</code> is a reasonable overall default for in many cases. </p>
<p> <code>striding</code> means that xxQS_NAMExx tries to find cores with a certain offset. It will select <i>number</i> of empty cores with an offset of <code>n</code>-1 cores in between. Start point for the search algorithm is socket 0 core 0. As soon as <i>number</i> cores are found they will be used to do the job binding. If there are not enough empty cores, or if the correct offset cannot be achieved, then no binding will be done on the host concerned. </p>
<p> <code>explicit</code> binds the specified sockets and cores that are mentioned in the provided socket/core list. Each socket/core pair has to be specified only once. If a socket/core pair is already in use by a different job, the whole binding request will be ignored. </p>
<p> Note that a binding like &quot;<code>pe linear:</code><i>number</i>&#8230;&quot; is only useful if the job has exclusive access to its multiple compute nodes, they all have the same topology, and the PE has a fixed allocation rule (<code>allocation_rule</code> <i>n</i>). (The $pe_hostfile content is created on the job&#8217;s master host, with the same &lt;socket,core&gt; specification for each.) This method can&#8217;t be used for job isolation. Similarly, <code>set</code> requires a fixed allocation per host for distributed parallel jobs. </p>
<p> <code>Qalter</code> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> If this option, or a corresponding value in qmon, is specified then these values will be passed to defined JSV instances as parameters with the names <code>binding_strategy</code>, <code>binding_type</code>, <code>binding_amount</code>, <code>binding_step</code>, <code>binding_socket</code>, <code>binding_core</code>, <code>binding_exp_n</code>, <code>binding_exp_socket</code><i>id</i>, <code>binding_exp_core</code><i>id</i>. </p>
<p> Please note that the length of the socket/core value list of the explicit binding is reported as <code>binding_exp_n</code>. <i>id</i> will be replaced by the position of the socket/core pair within the explicit list (0 &lt;= <i>id</i> &lt; <code>binding_exp_n</code>). The first socket/core pair of the explicit binding will be reported with the parameter names <code>binding_exp_socket0</code> and <code>binding_exp_core0</code>. </p>
<p> Values that do not apply for the specified binding will not be reported to JSV. E.g. <code>binding_step</code> will only be reported for the striding binding and all <code>binding_exp_*</code> values will passed to JSV if explicit binding was specified. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-c</code> <i>occasion_specifier</i></p>
<dd> Available for <i>qsub</i> and <i>qalter</i> only. </p>
<p> Defines or redefines whether the job should be checkpointed, and if so, under what circumstances. The specification of the checkpointing occasions with this option overwrites the definitions of the <i>when</i> parameter in the checkpointing environment (see referenced by the <code>qsub -ckpt</code> switch. Possible values for <i>occasion_specifier</i> are</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>n</code></p>
<dd> No checkpoint is performed;</p>
<dt><code>s</code></p>
<dd> Checkpoint when batch server is shut down;</p>
<dt><code>m</code></p>
<dd> Checkpoint at minimum CPU interval;</p>
<dt><code>x</code></p>
<dd> Checkpoint when job gets suspended;</p>
<dt><code>r</code></p>
<dd> Reschedule when execution host goes into the &quot;unknown&quot; state;</p>
<dt><i>interval</i></p>
<dd> Checkpoint in the specified interval (a <code>time_specifier</code> per</dl>
</dl>
<dt>
<dd> The minimum CPU interval is defined in the queue configuration (see for details). If <i>interval</i> is specified, the maximum of that and the queue&#8217;s minimum CPU interval is used (to ensure that a machine is not overloaded by checkpoints being generated too frequently). </p>
<p> The value specified with this option or the corresponding value specified in <i>qmon</i> will be passed to defined JSV instances. The <i>interval</i> will be available as parameter with the name <code>c_interval</code>. The character sequence specified will be available as parameter with the name <code>c_occasion</code>. Please note that if you change <code>c_occasion</code> via JSV, then the last setting of <code>c_interval</code> will be overwritten, and vice versa. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-ckpt</code> <i>ckpt_name</i></p>
<dd> Available for <i>qsub</i> and <i>qalter</i> only. </p>
<p> Selects the checkpointing environment (see to be used for checkpointing the job. Also declares the job to be a checkpointing job. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>ckpt</code>. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-clear</code></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, and <i>qlogin</i> only. </p>
<p> Causes all elements of the job to be reset to the initial default status prior to applying any modifications (if any) appearing in this specific command.</p>
<dt><code>-cwd</code></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i> and <i>qalter</i> only. </p>
<p> Execute the job from the current working directory. This switch will activate xxQS_NAMExx&#8217;s path aliasing facility, if the corresponding configuration files are present (see </p>
<p> In the case of <i>qalter</i>, the previous definition of the current working directory will be overwritten if <i>qalter</i> is executed from a different directory than the preceding <i>qsub</i> or <i>qalter</i>. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>cwd</code>. The value of this parameter will be the absolute path to the current working directory. JSV scripts can remove the path from jobs during the verification process by setting the value of this parameter to an empty string. As a result the job behaves as if <code>-cwd</code> was not specified during job submission. (See <code>-jsv</code> option below or find more information concerning JSV in </p>
<dt><code>-C</code> <i>prefix_string</i></p>
<dd> Available for <i>qsub</i> and <i>qrsh</i> with script submission (<code>-b n</code>). </p>
<p> <i>Prefix_string</i> defines the prefix that declares a directive in the job&#8217;s command. The prefix is not a job attribute, but affects the behavior of <i>qsub</i> and <i>qrsh</i>. If <i>prefix</i> is a null string, the command will not be scanned for embedded directives.<br />
 The directive prefix consists of two ASCII characters which, when appearing in the first two bytes of a script line, indicate that what follows is an xxQS_NAMExx command. The default is &quot;#$&quot;.<br />
 The user should be aware that changing the first delimiting character can produce unforeseen side effects. If the script file contains anything other than a &quot;#&quot; character in the first byte position of the line, the shell processor for the job will reject the line and may exit the job prematurely.<br />
 If the -C option is present in the script file, it is ignored.</p>
<dt><code>-dc</code> <i>variable</i>,&#8230;</p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Removes the given variable(s) from the job&#8217;s context. Multiple <code>-ac</code>, <code>-dc</code>, and <code>-sc</code> options may be given. The order is important. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. </p>
<p> The outcome of the evaluation of all <code>-ac</code>, <code>-dc</code>, and <code>-sc</code> options or corresponding values in <i>qmon</i> is passed to defined JSV instances as parameter with the name <code>ac</code>. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-display</code> <i>display_specifier</i></p>
<dd> Available for <i>qsh</i> and <i>qrsh</i> with a command. </p>
<p> Directs to use <i>display_specifier</i> in order to contact the X server. The <i>display_specifier</i> has to contain the hostname part of the display name (e.g. myhost:1). Local display names (e.g. :0) cannot be used in grid environments. Values set with the <code>-display</code> option overwrite settings from the submission environment and from <code>-v</code> command line options. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>display</code>. This value will also be available in the job environment which might optionally be passed to JSV scripts. The variable name will be <code>DISPLAY</code>. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-dl</code> <i>date_time</i></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Specifies the deadline initiation time in [[<i>CC</i>]<i>YY</i>]<i>MMDDhhmm</i>[<code>.</code><i>SS</i>] format (see <code>-a</code> option above). The deadline initiation time is the time at which a deadline job has to reach top priority to be able to complete within a given deadline. Before the deadline initiation time the priority of a deadline job will be raised steadily until it reaches the maximum as configured by the xxQS_NAMExx administrator. </p>
<p> This option is applicable only for users allowed to submit deadline jobs. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>dl</code>. The format for the date_time value is CCYYMMDDhhmm.SS. (See <code>-jsv</code> option below or find more information concerning JSV in </p>
<dt><code>-e</code> [[<i>hostname</i>]<code>:</code>]<i>path</i>&#8230;</p>
<dd> Available for <i>qsub</i> and <i>qalter</i> only, but currently silently ignored by <i>qsh</i>, <i>qrsh</i>, and <i>qlogin</i>. </p>
<p> Defines or redefines the path used for the standard error stream of the job. For <i>qsh</i>, <i>qrsh</i> and <i>qlogin</i> only the standard error stream of prolog and epilog is redirected. If the <i>path</i> constitutes an absolute path name, the error-path attribute of the job is set to <i>path</i>, including the <i>hostname</i>. If the path name is relative, xxQS_NAMExx expands <i>path</i>, either relative to the current working directory (if the <code>-cwd</code> switch &#8211; see above &#8211; is also specified) or to the home directory. If <i>hostname</i> is present, the standard error stream will be placed in the corresponding location only if the job runs on the specified host. If the path contains a &quot;:&quot; without a <i>hostname</i>, a leading &quot;:&quot; has to be specified. </p>
<p> By default the file name for interactive jobs is <i>/dev/null</i>. For batch jobs the default file name has the form <i>job_name</i><code>.e</code><i>job_id</i> and <i>job_name</i><code>.e</code><i>job_id</i><code>.</code><i>task_id</i> for array job tasks (see <code>-t</code> option below). </p>
<p> If <i>path</i> is a directory, the standard error stream of the job will be put in this directory under the default file name. If the pathname contains certain pseudo environment variables, their value will be expanded at runtime of the job and will be used to constitute the standard error stream path name. The following pseudo environment variables are supported currently; note the lack of an <code>xxQS_NAMExx_</code> prefix in this context: </p>
<pre>
$HOME       home directory on execution machine
$USER       user ID of job owner
$JOB_ID     current job ID
$JOB_NAME   current job name (see <code>-N</code> option)
$HOSTNAME   name of the execution host
$TASK_ID    array job task index number
</pre>
<p> The tilde sign &quot;~&quot; can be used as an alternative to $HOME, as in or Note that the &quot;~&quot; sign also works in combination with user names, so that &quot;~<i>user</i>&quot; expands to the home directory of <i>user</i>. Using another user ID than that of the job owner requires corresponding permissions, of course. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>e</code>. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-hard</code></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Signifies that all <code>-q</code> and <code>-l</code> resource requirements following in the command line will be hard requirements and must be satisfied in full before a job can be scheduled.<br />
 As xxQS_NAMExx scans the command line and script file for xxQS_NAMExx options and parameters it builds a list of resources required by a job. All such resource requests are normally considered as absolutely essential for the job to commence. However, if the <code>-soft</code> option (see below) is encountered during the scan then all following resources are designated as &quot;soft requirements&quot; for execution, or &quot;nice-to-have, but not essential&quot;. If the <code>-hard</code> flag is encountered at a later stage of the scan, all resource requests following it once again become essential. The <code>-hard</code> and <code>-soft</code> options in effect act as toggles during the scan. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then the corresponding <code>-q</code> and <code>-l</code> resource requirements will be passed to defined JSV instances as parameter with the names <code>q_hard</code> and <code>l_hard</code>. Find for information in the sections describing <code>-q</code> and <code>-l</code>. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-h</code> | <code>-h</code> {<code>u</code>|<code>s</code>|<code>o</code>|<code>n</code>|<code>U</code>|<code>O</code>|<code>S</code>}&#8230;</p>
<dd> Available for <i>qsub</i> (only <code>-h</code>), <i>qrsh</i>, <i>qalter</i> and <i>qresub</i> (hold state is removed when not set explicitly). </p>
<p> List of holds to place on a job, a task or some tasks of a job. </p>
<pre>
`u'  denotes a user hold.
`s'  denotes a system hold.
`o'  denotes a operator hold.
`n'  denotes no hold (requires manager privileges).
</pre>
<p> As long as any hold other than `n&#8217; is assigned to the job the job is not eligible for execution. Holds can be released via <i>qalter</i> and In case of <i>qalter</i> this is supported by the following additional option specifiers for the <code>-h</code> switch: </p>
<pre>
`U'  removes a user hold.
`S'  removes a system hold.
`O'  removes a operator hold.
</pre>
<p> xxQS_NAMExx managers can assign and remove all hold types, xxQS_NAMExx operators can assign and remove user and operator holds, and users can only assign or remove user holds. </p>
<p> In the case of <i>qsub</i> only user holds can be placed on a job and thus only the first form of the option with the <code>-h</code> switch alone is allowed. As opposed to this, <i>qalter</i> requires the second form described above. </p>
<p> An alternate means to assign a hold is provided by the facility. </p>
<p> If the job is an array job (see the <code>-t</code> option below), all tasks specified via <code>-t</code> are affected by the <code>-h</code> operation simultaneously. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> If this option is specified with <i>qsub</i> or during the submission of a job in <i>qmon</i> then the parameter <code>h</code> with the value <code>u</code> will be passed to the defined JSV instances indicating that the job will be in user hold after the submission finishes. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-hold_jid</code> <i>wc_job_list</i></p>
<dd> Available for <i>qsub</i>, <i>qrsh</i>, and <i>qalter</i> only. See For the definition of <i>wc_job_list</i>. </p>
<p> Defines or redefines the job dependency list of the submitted job. A reference by job name or pattern is only accepted if the referenced job is owned by the same user as the referring job. The submitted job is not eligible for execution unless all jobs referenced in the comma-separated job id and/or job name list have completed. If any of the referenced jobs exits with exit code 100, the submitted job will remain ineligible for execution. </p>
<p> With the help of job names or regular patterns, one can specify a job dependency on multiple jobs satisfying the regular pattern, or on all jobs with the requested name. The name dependencies are resolved at submit time and can only be changed via qalter. New jobs or name changes of other jobs will not be taken into account. To remove a job dependency list with <i>qalter</i>, use a null <i>wc_job_list</i>, i.e. use<br />
 <code> qalter -hold_jid &#8221; &#8230;</code> </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>hold_jid</code>. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-hold_jid_ad</code> <i>wc_job_list</i></p>
<dd> Available for <i>qsub</i>, <i>qrsh</i>, and <i>qalter</i> only. See for the definition of <i>wc_job_list</i>. </p>
<p> Defines or redefines the job array dependency list of the submitted job. A reference by job name or pattern is only accepted if the referenced job is owned by the same user as the referring job. Each sub-task of the submitted job is not eligible for execution unless the corresponding sub-tasks of all jobs referenced in the comma-separated job id and/or job name list have completed. If dependent jobs have a different array stride to referenced jobs, the dependency may be many-to-one or one-to-many, e.g. if an array is submitted with <code>-t 1:50:2</code>, depending on one submitted with <code>-t 1:50</code>, then task <i>n</i> of the dependent depends on task <i>n</i>+1 of the other. </p>
<p> If any array task of the referenced jobs exits with exit code 100, the dependent tasks of the submitted job will remain ineligible for execution. </p>
<p> With the help of job names or regular patterns, one can specify a job dependency on multiple jobs satisfying the regular pattern, or on all jobs with the requested name. The name dependencies are resolved at submit time and can only be changed via qalter. New jobs or name changes of other jobs will not be taken into account. </p>
<p> If either the submitted job or any job in <i>wc_job_list</i> are not array jobs with the same range of sub-tasks (see <code>-t</code> option below), the request list will be rejected and the job create or modify operation will return an error. </p>
<p> <i>qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified, then this value will be passed to defined JSV instances as a parameter with the name <code>hold_jid_ad</code>. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-i</code> [[<i>hostname</i>]<code>:</code>]<i>path</i><code>,</code>&#8230;</p>
<dd> Available for <i>qsub</i>, and <i>qalter</i> only. </p>
<p> Defines or redefines the path used for the standard input stream of the job. The <i>path</i> is handled as described in the <code>-e</code> option for the standard error stream. </p>
<p> By default <i>/dev/null</i> is the input stream for the job. </p>
<p> It is possible to use certain pseudo variables, whose values will be expanded at runtime of the job and will be used to express the standard input stream as described in the <i>-e</i> option for the standard error stream. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>i</code>. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-inherit</code></p>
<dd> Available only for <i>qrsh</i> and </p>
<p> <i>qrsh </i> allows the user to start a task in an already scheduled parallel job. The option <code>-inherit</code> tells <i>qrsh</i> to read a job id from the environment variable JOB_ID and start the specified command as a task in this job. Please note that in this case, the hostname of the host where the command will be executed must precede the command to execute; the syntax changes to </p>
<p> <code>qrsh -inherit</code> [<i>other options</i>] <i>hostname command</i> [<i>command_args</i>] </p>
<p> Note also, that in combination with <code>-inherit</code>, most other command line options will be ignored. Only the options <code>-verbose</code>, <code>-v</code> and <code>-V</code> will be interpreted. As a replacement to option <code>-cwd</code> please use <code>-v PWD</code>. </p>
<p> Usually a task should have the same environment (including the current working directory) as the corresponding job, so specifying the option <code>-V</code> should be suitable for most applications. </p>
<p> <i>Note:</i> If in your system the qmaster tcp port is not configured as a service, but rather via the environment variable xxQS_NAME_Sxx_QMASTER_PORT, make sure that this variable is set in the environment when calling <i>qrsh</i> or <i>qmake</i> with the <code>-inherit</code> option. If you call <i>qrsh</i> or <i>qmake</i> with the <code>-inherit</code> option from within a job script, export xxQS_NAME_Sxx_QMASTER_PORT with the option &quot;-v xxQS_NAME_Sxx_QMASTER_PORT&quot; either as a command argument or an embedded directive. </p>
<p> This parameter is not available in the JSV context. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-j</code> <code>y</code>[<code>es</code>]|<code>n</code>[<code>o</code>]</p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Specifies whether or not the standard error stream of the job is merged into the standard output stream.<br />
 If both the <code>-j y</code> and the <code>-e</code> options are present, xxQS_NAMExx sets, but ignores, the error-path attribute. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> The value specified with this option or the corresponding value specified in <i>qmon</i> will only be passed to defined JSV instances if the value is <code>yes</code>. The name of the parameter will be <code>j</code>. The value will be <code>y</code> also when the long form <code>yes</code> was specified during submission. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-js</code> <i>job_share</i></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Defines or redefines the job share of the job relative to other jobs. Job share is an unsigned integer value. The default job share value for jobs is 0. </p>
<p> The job share influences the Share Tree Policy and the Functional Policy. It has no effect on the Urgency and Override Policies (see for further information on the resource management policies supported by xxQS_NAMExx). </p>
<p> In case of the Share Tree Policy, users can distribute the tickets to which they are currently entitled among their jobs using different shares assigned via <code>-js</code>. If all jobs have the same job share value, the tickets are distributed evenly. Otherwise, jobs receive tickets relative to the different job shares. Job shares are treated like an additional level in the share tree in the latter case. </p>
<p> In connection with the Functional Policy, the job share can be used to weight jobs within the functional job category. Tickets are distributed relative to any uneven job share distribution treated as a virtual share distribution level underneath the functional job category. </p>
<p> If both the Share Tree and the Functional Policy are active, the job shares will have an effect in both policies, and the tickets independently derived in each of them are added to the total number of tickets for each job. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>js</code>. (See <code>-jsv</code> option below or find more information concerning JSV in</p>
<dt><code>-jsv</code> <i>jsv_url</i></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i> and <i>qlogin</i> only. </p>
<p> Defines a client JSV instance which will be executed to verify the job specification before the job is sent to qmaster. </p>
<p> In contrast to other options this switch will not be overwritten if it is also used in xxqs_name_sxx_request files. Instead all specified JSV instances will be executed to verify the job to be submitted. </p>
<p> The JSV instance which is directly passed with the command line of a client is executed first to verify the job specification. After that the JSV instance which might have been defined in various xxqs_name_sxx_request files will be triggered to check the job. Find more details in man page and </p>
<p> The syntax of the <code>jsv_url</code> is specified in</p>
<dt><code>-l</code> <i>resource</i><code>=</code><i>expression</i><code>,</code>&#8230;</p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Launch the job in a xxQS_NAMExx queue meeting the given resource request list. In case of <i>qalter</i> the previous definition is replaced by the specified one. </p>
<p> describes how a list of available resources and their associated valid value specifiers can be obtained, and section &quot;MATCHING TYPES&quot; in describes the possible forms of the expression for the requested resources. </p>
<p> There may be multiple <code>-l</code> switches in a single command. You may request multiple <code>-l</code> options to be soft or hard both in the same command line. In case of a serial job multiple <code>-l</code> switches refine the definition for the sought queue. </p>
<p> <i>Qalter</i> allows changing the value of this option even while the job is running, but only if no change is made to requests for resources marked as consumable. However the modification will only be effective after a restart or migration of the job. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified the these hard and soft resource requirements will be passed to defined JSV instances as parameter with the names <code>l_hard</code> and <code>l_soft</code>. If regular expressions will be used for resource requests, then these expressions will be passed as they are. Also shortcut names will not be expanded. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-m</code> <code>b</code>|<code>e</code>|<code>a</code>|<code>s</code>|<code>n,</code>&#8230;</p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Defines or redefines under which circumstances mail is to be sent to the job owner or to the users defined with the <code>-M</code> option described below. The option arguments have the following meaning: </p>
<pre>
`b'     Mail is sent at the beginning of the job.
`e'     Mail is sent at the end of the job.
`a'     Mail is sent when the job is aborted or 
        rescheduled.
`s'     Mail is sent when the job is suspended.
`n'     No mail is sent.
</pre>
<p> Currently no mail is sent when a job is suspended. </p>
<p> <i>Qalter</i> allows changing the &quot;b&quot;, &quot;e&quot;, and &quot;a&quot; option arguments even while the job executes. The modification of the option arguments will only be in effect after a restart or migration of the job, however. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>m</code>. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-M</code> <i>user</i>[<code>@</code><i>host</i>]<code>,</code>&#8230;</p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Defines or redefines the list of users to which the server that executes the job has to send mail, if the server sends mail about the job. Default is the job owner at the originating host. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modification will only be in effect after a restart or migration of the job, however. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>M</code>. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-masterq</code> <i>wc_queue_list</i></p>
<dd> Available for <i>qsub</i>, <i>qrsh</i>, <i>qsh</i>, <i>qlogin</i> and <i>qalter</i>. Only meaningful for parallel jobs, i.e. together with the -pe option. </p>
<p> Defines or redefines a list of cluster queues, queue domains and queue instances which may be used to become the so called <i>master queue</i> of this parallel job. A more detailed description of <i>wc_queue_list</i> can be found in The <i>master queue</i> is defined as the queue where the parallel job is started. The other queues to which the parallel job spawns tasks are called <i>slave queues</i>. A parallel job only has one <i>master queue</i>. </p>
<p> This parameter has all the properties of a resource request and will be merged with requirements derived from the <code>-l</code> option described above. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> If this option, or a corresponding value in <i>qmon</i>, is specified, this hard resource requirement will be passed to defined JSV instances as a parameter with the name <code>masterq</code>. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-notify</code></p>
<dd> Available for <i>qsub</i>, <i>qrsh</i> (with command) and <i>qalter</i> only. </p>
<p> This flag, when set, causes xxQS_NAMExx to send &quot;warning&quot; signals to a running job prior to sending the signals themselves. If a SIGSTOP is pending, the job will receive a SIGUSR1 several seconds before the SIGSTOP. If a SIGKILL is pending, the job will receive a SIGUSR2 several seconds before the SIGKILL. This option provides the running job a configured time interval to do cleanup operations before receiving the SIGSTOP or SIGKILL. The amount of time delay is controlled by the <code>notify</code> parameter in each queue configuration (see </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. </p>
<p> Only if this option is used the parameter named <code>notify</code> with the value <code>y</code> will be passed to defined JSV instances. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-now</code> <code>y</code>[<code>es</code>]|<code>n</code>[<code>o</code>]</p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qlogin</i> and <i>qrsh</i>. </p>
<p> <code>-now y</code> tries to start the job immediately or not at all. The command returns 0 on success, or 1 on failure (also if the job could not be scheduled immediately). For array jobs submitted with the <code>-now</code> option, if all tasks cannot be immediately scheduled, no tasks are scheduled. </p>
<p> Jobs submitted with <code>-now y</code> option, can <i>only</i> run on INTERACTIVE queues. <code>-now y</code> is default for <i>qsh</i>, <i>qlogin</i> and <i>qrsh</i> </p>
<p> With the <code>-now n</code> option, the job will be put into the pending queue if it cannot be executed immediately. <code>-now n</code> is default for <i>qsub</i>.</p>
<dt><code>-N name</code></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> The name of the job. The name should follow the &quot;<code>name</code>&quot; definition in Invalid job names will be denied at submit time. </p>
<p> If the <code>-N</code> option is not present, xxQS_NAMExx assigns the name of the job script to the job after any directory pathname has been removed from the script name. If the script is read from standard input, the job name defaults to STDIN. </p>
<p> In the case of <i>qsh</i> or <i>qlogin</i> with the <code>-N</code> option is absent, the name &quot;INTERACTIVE&quot; or &quot;QLOGIN&quot; respectively is assigned to the job. </p>
<p> In the case of <i>qrsh</i> if the <code>-N</code> option is absent, the resulting job name is determined from the qrsh command line by using the argument string up to the first occurrence of a semicolon or whitespace and removing the directory pathname. With no command, &quot;QRLOGIN&quot; is used. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. </p>
<p> The value specified with this option or the corresponding value specified in <i>qmon</i> will be passed to defined JSV instances as parameter with the name <code>N</code>. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-noshell</code></p>
<dd> Available only for <i>qrsh</i> with a command line. </p>
<p> Do not start the command line given to <i>qrsh</i> in the user&#8217;s login shell, i.e. execute it without the wrapping shell. </p>
<p> This option can be used to speed up execution as some overhead, like the shell startup and sourcing the shell resource files, is avoided. </p>
<p> This option can only be used if no shell-specific command line parsing is required. If the command line contains shell syntax like environment variable substitution or (back) quoting, a shell must be started. In this case, either do not use the <code>-noshell</code> option or include the shell call in the command line. </p>
<p> Example:<br />
 qrsh echo &#8216;$HOSTNAME&#8217;<br />
 Alternative call with the <code>-noshell</code> option<br />
 qrsh -noshell /bin/tcsh -f -c &#8216;echo $HOSTNAME&#8217;</p>
<dt><code>-nostdin</code></p>
<dd> Available only for <i>qrsh</i>. </p>
<p> Suppress the input stream STDIN &#8211; <i>qrsh</i> will pass the option <code>-n</code> to the command. This is especially useful, if multiple tasks are executed in parallel using <i>qrsh</i>, e.g. in a process it would be undefined which process would get the input.</p>
<dt><code>-o</code> [[<i>hostname</i>]<code>:</code>]<i>path</i><code>,</code>&#8230;</p>
<dd> Available for <i>qsub</i> and <i>qalter</i> only, but currently silently ignored by <i>qsh</i>, <i>qrsh</i>, and <i>qlogin</i>. </p>
<p> Specify the path used for the standard output stream of the job. <i>path</i> is handled as described in the <code>-e</code> option for the standard error stream. </p>
<p> By default the file name for standard output has the form <i>job_name</i><code>.o</code><i>job_id</i>, or <i>job_name</i><code>.o</code><i>job_id</i><code>.</code><i>task_id</i> for array job tasks (see <code>-t</code> option below). </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>o</code>. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-ot</code> <i>override_tickets</i></p>
<dd> Available for <i>qalter</i> only. </p>
<p> Changes the number of override tickets for the specified job. Requires manager/operator privileges.</p>
<dt><code>-P</code> <i>project_name</i></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Specifies the project to which this job is assigned. The administrator needs to give permission to individual users to submit jobs to a specific project (see <code>-aprj</code> option to </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>P</code>. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-p</code> <i>priority</i></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Defines or redefines the priority of the job relative to other jobs. <i>priority</i> is an integer in the range -1023 to 1024. The default priority value for jobs is 0. </p>
<p> Users may only decrease the priority of their jobs. xxQS_NAMExx managers and administrators may also increase the priority associated with jobs. If a pending job has higher priority, it is eligible for being dispatched earlier by the xxQS_NAMExx scheduler. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified and the priority is not 0 then this value will be passed to defined JSV instances as parameter with the name <code>p</code>. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-pe</code> <i>parallel_environment n</i>[<code>&#8211;</code>[<i>m</i>]]|[<code>&#8211;</code>]<i>m</i><code>,</code>&#8230;</p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Parallel programming environment (PE) to instantiate. For more detail about PEs, please see <code>parallel_env</code> in </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then the parameters <code>pe_name</code>, <code>pe_min</code> and <code>pe_max</code> will be passed to configured JSV instances where <code>pe_name</code> will be the name of the parallel environment and the values <code>pe_min</code> and <code>pe_max</code> represent the values <i>n</i> and <i>m</i> which have been provided with the <code>-pe</code> option. A missing specification of <i>m</i> will be expanded as value 9999999 in JSV scripts and it represents the value infinity. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-pty y</code>[<code>es</code>]|<code>n</code>[<code>o</code>]</p>
<dd> Available for <i>qrsh</i>, <i>qsub</i> and <i>qlogin</i> only, and normally only effective for interactive jobs with the <code>builtin</code> remote startup method (see </p>
<p> <code>-pty yes</code> starts the job in a pseudo terminal (pty). If no pty is available, the job start fails. <code>-pty no</code> starts the job without a pty. By default, <i>qrsh without a command</i> and <i>qlogin</i> start the job in a pty, and <i>qrsh</i> or <i>qsub</i> with a command starts the job without a pty. </p>
<p> This parameter is not available in the JSV context. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-q</code> <i>wc_queue_list</i></p>
<dd> Available for <i>qsub</i>, <i>qrsh</i>, <i>qsh</i>, <i>qlogin</i> and <i>qalter</i>. </p>
<p> Defines or redefines a list of cluster queues, queue domains or queue instances which may be used to execute this job. Please find a description of <i>wc_queue_list</i> in This parameter has all the properties of a resource request and will be merged with requirements derived from the <code>-l</code> option described above. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then these hard and soft resource requirements will be passed to defined JSV instances as parameters with the names <code>q_hard</code> and <code>q_soft</code>. If regular expressions will be used for resource requests, then these expressions will be passed as they are. Also shortcut names will not be expanded. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-R</code> <code>y</code>[<code>es</code>]|<code>n</code>[<code>o</code>]</p>
<dd> Available for <i>qsub</i>, <i>qrsh</i>, <i>qsh</i>, <i>qlogin</i> and <i>qalter</i>. </p>
<p> Indicates whether a reservation for this job should be done. Reservation is never done for immediate jobs, i.e. jobs submitted using the <code>-now yes</code> option. Please note that regardless of the reservation request, job reservation might be disabled using <code>max_reservation</code> in and is limited to that number of the highest priority jobs. </p>
<p> By default jobs are submitted with <code>-R n</code>. </p>
<p> The value specified with this option or the corresponding value specified in <i>qmon</i> will only be passed to defined JSV instances if the value is <i>yes</i>. The name of the parameter will be <code>R</code>. The value will be <code>y</code> also when the long form <code>yes</code> was specified during submission. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-r y</code>[<code>es</code>]|<code>n</code>[<code>o</code>]</p>
<dd> Available for <i>qsub</i> and <i>qalter</i> only. </p>
<p> Specifies whether a job can be rerun or not. If the value of <code>-r</code> is &#8216;yes&#8217;, the job will be rerun if it gets aborted without leaving a consistent exit state. (This is typically the case if the node on which the job is running crashes). If <code>-r</code> is &#8216;no&#8217; (the default), the job will not be rerun under such circumstances. It will still be rerun if it finishes with exit code 99 unless <code>FORBID_RESCHEDULE</code> is set in <code>qmaster_params</code> in </p>
<p> Interactive jobs submitted with <i>qsh</i>, <i>qrsh</i>, or <i>qlogin</i> are not rerunnable. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. </p>
<p> The value specified with this option or the corresponding value specified in <i>qmon</i> will only be passed to defined JSV instances if the value is <i>yes</i>. The name of the parameter will be <code>r</code>. The value will be <code>y</code> also when the long form <code>yes</code> was specified during submission. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-sc</code> <i>variable</i>[<code>=</code><i>value</i>]<code>,</code>&#8230;</p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Sets the given name/value pairs as the job&#8217;s context. <i>value</i> may be omitted. xxQS_NAMExx replaces the job&#8217;s previously defined context with the one given as the argument. Multiple <code>-ac</code>, <code>-dc</code>, and <code>-sc</code> options may be given. The order is important. </p>
<p> Contexts provide a way to dynamically attach and remove meta-information to and from a job. The context variables are <code>not</code> passed to the job&#8217;s execution context in its environment, but are available in its spool area. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. </p>
<p> The outcome of the evaluation of all <code>-ac</code>, <code>-dc</code>, and <code>-sc</code> options or corresponding values in <i>qmon</i> is passed to defined JSV instances as parameter with the name <code>ac</code>. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-shell y</code>[<code>es</code>]|<code>n</code>[<code>o</code>]</p>
<dd> Available only for <i>qsub</i>. </p>
<p> <code>-shell n</code> causes qsub to execute the command line directly, as if by No command shell will be executed for the job. This option only applies when <code>-b y</code> is also used. Without <code>-b y</code>, <code>-shell n</code> has no effect. </p>
<p> This option can be used to speed up execution, as some overhead, like the shell startup and sourcing the shell resource files, is avoided. </p>
<p> This option can only be used if no shell-specific command line parsing is required. If the command line contains shell syntax, like environment variable substitution or (back) quoting, a shell must be started. In this case either do not use the <code>-shell n</code> option or execute the shell as the command line and pass the path to the executable as a parameter. </p>
<p> If a job executed with the <code>-shell n</code> option fails due to a user error, such as an invalid path to the executable, the job will enter the error state. </p>
<p> <code>-shell y</code> cancels the effect of a previous <code>-shell n</code>. Otherwise, it has no effect. </p>
<p> See <code>-b</code> and <code>-noshell</code> for more information. </p>
<p> The value specified with this option or the corresponding value specified in <i>qmon</i> will only be passed to defined JSV instances if the value is <i>yes</i>. The name of the parameter will be <code>shell</code>. The value will be <code>y</code> also when the long form <code>yes</code> was specified during submission. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-soft</code></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i> only. </p>
<p> Signifies that all resource requirements following in the command line will be soft requirements and are to be filled on an &quot;as available&quot; basis.<br />
 As xxQS_NAMExx scans the command line and script file for xxQS_NAMExx options and parameters, it builds a list of resources required by the job. All such resource requests are normally considered as absolutely essential for the job to commence. However, if the <code>-soft</code> option is encountered during the scan then all following resources are designated as &quot;soft requirements&quot; for execution, or &quot;nice-to-have, but not essential&quot;. If the <code>-hard</code> flag (see above) is encountered at a later stage of the scan, all resource requests following it once again become essential. The <code>-hard</code> and <code>-soft</code> options in effect act as toggles during the scan. However, requests for consumable resources cannot be soft. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then the corresponding <code>-q</code> and <code>-l</code> resource requirements will be passed to defined JSV instances as parameter with the names <code>q_soft</code> and <code>l_soft</code>. Find for information in the sections describing <code>-q</code> and <code>-l</code>. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-sync y</code>[<code>es</code>]|<code>n</code>[<code>o</code>]</p>
<dd> Available for <i>qsub</i>. </p>
<p> <code>-sync y</code> causes <i>qsub</i> to wait for the job to complete before exiting. If the job completes successfully, <i>qsub</i>&#8216;s exit code will be that of the completed job. If the job fails to complete successfully, <i>qsub</i> will print an error message to the standard error stream indicating why the job failed, and will have an exit code of 1. If <i>qsub</i> is interrupted, e.g. with CTRL-C, before the job completes, the job will be canceled.<br />
 With the <code>-sync n</code> option, <i>qsub</i> will exit with an exit code of 0 as soon as the job is submitted successfully. <code>-sync n</code> is default for <i>qsub</i>.<br />
 If <code>-sync y</code> is used in conjunction with <code>-now y</code>, <i>qsub</i> will behave as though only <code>-now y</code> were given until the job has been successfully scheduled, after which time <i>qsub</i> will behave as though only <code>-sync y</code> were given.<br />
 If <code>-sync y</code> is used in conjunction with <code>-t</code>, <i>qsub</i> will wait for all the job&#8217;s tasks to complete before exiting. If all the job&#8217;s tasks complete successfully, <i>qsub</i>&#8216;s exit code will be that of the first completed job task with a non-zero exit code, or 0 if all job tasks exited with an exit code of 0. If any of the job&#8217;s tasks fail to complete successfully, <i>qsub</i> will print an error message to the standard error stream indicating why the job task(s) failed, and will have an exit code of 1. If <i>qsub</i> is interrupted, e.g. with CTRL-C, before the job completes, all of the job&#8217;s tasks will be canceled. </p>
<p> Information that this switch was specified during submission is not available in the JSV context. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-S</code> [[<i>hostname</i>]<code>:</code>]<i>pathname</i><code>,</code>&#8230;</p>
<dd> Available for <i>qsub</i>, <i>qsh</i> and <i>qalter</i>. </p>
<p> Specifies the interpreting shell for the job. <i>pathname</i> must be an executable file which interprets command-line options <code>-c</code> and <code>-s</code> as <code>/bin/sh</code> does. </p>
<p> Only one <i>pathname</i> component without a <i>host</i> specifier is valid and only one path name for a given host is allowed. Shell paths with host assignments define the interpreting shell for the job if the host is the execution host. The shell path without host specification is used if the execution host matches none of the hosts in the list. </p>
<p> Furthermore, the pathname can be constructed with pseudo environment variables as described for the <code>-e</code> option above. </p>
<p> In the case of <i>qsh</i> the specified shell path is used to execute the corresponding command interpreter in the (via its <i>-e</i> option) started on behalf of the interactive job. <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameter with the name <code>S</code>. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-t</code> <i>n</i>[<code>&#8211;</code><i>m</i>[<code>:</code><i>s</i>]]</p>
<dd> Available for <i>qsub</i> only. </p>
<p> Submits a so called <i>Array Job</i>, i.e. an array of identical tasks being differentiated only by an index number and being treated by xxQS_NAMExx almost like a series of jobs. The argument of <code>-t</code> specifies the number of array job tasks and the index number which will be associated with the tasks in terms of the range&#8217;s start (<i>n</i>), default 1, its end (<i>m</i>), and stride (s), default 1. The index numbers will be exported to the job tasks via the environment variable <code>xxQS_NAME_Sxx_TASK_ID</code>. The arguments <i>n</i>,&nbsp;<i>m</i>, and <i>s</i> will be available through the environment variables <code>xxQS_NAME_Sxx_TASK_FIRST</code>, <code>xxQS_NAME_Sxx_TASK_LAST</code> and <code>xxQS_NAME_Sxx_TASK_STEPSIZE</code>. </p>
<p> The following restrictions apply to the values <i>n</i> and <i>m</i>: </p>
<p>1 &lt;= n &lt;= MIN(2 ^ 31 &#8211; 1, max_aj_tasks) 1 &lt;= m &lt;= MIN(2 ^ 31 &#8211; 1, max_aj_tasks)<br />
                                                      n<br />
    &lt;= m</p>
<p> <i>max_aj_tasks</i> is defined in the cluster configuration (see </p>
<p> The task id range specified in the option argument may be a single number, a simple range of the form <i>n</i><code>&#8211;</code><i>m</i> or a range with a step size. Hence, the task id range specified by 2-10:2 would result in the task id indexes 2, 4, 6, 8, and 10, for a total of 5 identical tasks, each with the environment variable xxQS_NAME_Sxx_TASK_ID containing one of the 5 index numbers. </p>
<p> All array job tasks inherit the same resource requests and attribute definitions as specified in the <i>qsub</i> or <i>qalter</i> command line, except for the <code>-t</code> option. The tasks are scheduled independently and, provided enough resources exist, concurrently, very much like separate jobs. However, an array job or a sub-array there of can be accessed as a single unit by commands like or See the corresponding manual pages for further detail. </p>
<p> Array jobs are commonly used to execute the same type of operation on varying input data sets correlated with the task index number. The number of tasks in an array job is unlimited. </p>
<p> STDOUT and STDERR of array job tasks will be written into different files with the default location </p>
<pre>
<i>jobname</i><code>.</code>[<code>e</code>|<code>o</code>]<i>job_id</i><code>.</code><i>task_id</i>
</pre>
<p> In order to change this default, the <code>-e</code> and <code>-o</code> options (see above) can be used together with the pseudo environment variables $HOME, $USER, $JOB_ID, $JOB_NAME, $HOSTNAME, and $TASK_ID. </p>
<p> Note, that you can use the output redirection to divert the output of all tasks into the same file, but the result of this is undefined. </p>
<p> If this option or a corresponding value in <i>qmon</i> is specified then this value will be passed to defined JSV instances as parameters with the names <code>t_min</code>, <code>t_max</code> and <code>t_step</code> (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-tc</code> <i>max_running_tasks</i></p>
<dd> Available for <i>qsub</i> and <i>qalter</i> only. </p>
<p> Used in conjunction with array jobs (see -t option) to set a self-imposed limit on the maximum number of concurrently running tasks per job. </p>
<p> If this option, or a corresponding value in <i>qmon</i> is specified, then this value will be passed to defined JSV instances as a parameter with the name <code>tc</code>. (See the <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-terse</code></p>
<dd> Available for <i>qsub</i> only. </p>
<p> Causes <i>qsub</i> to display only the job-id of the job being submitted rather than the regular &quot;Your job &#8230;&quot; string. In case of an error the error is reported on stderr as usual.<br />
 This can be helpful for scripts which need to parse <i>qsub</i> output to get the job-id. </p>
<p> Information that this switch was specified during submission is not available in the JSV context. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-u</code> <i>username</i><code>,</code>&#8230;</p>
<dd> Available for <i>qalter</i> only. Changes are only made on those jobs which were submitted by users specified in the list of usernames. For managers it is possible to use the <code>qalter -u &#8216;*&#8217;</code> command to modify all jobs of all users. </p>
<p> If you use the <code>-u</code> switch it is not permitted to specify an additional <i>wc_job_range_list</i>.</p>
<dt><code>-v</code> <i>variable</i>[<code>=</code><i>value</i>]<code>,</code>&#8230;</p>
<dd> Available for <i>qsub</i>, <i>qrsh</i> (with command argument) and <i>qalter</i>. </p>
<p> Defines or redefines the environment variables to be exported to the execution context of the job. If the <code>-v</code> option is present xxQS_NAMExx will add the environment variables defined as arguments to the switch and, optionally, values of specified variables, to the execution context of the job. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> All environment variables specified with <code>-v</code>, <code>-V</code> or the DISPLAY variable provided with <code>-display</code> will be exported to the defined JSV instances only optionally when this is requested explicitly during the job submission verification. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-verbose</code></p>
<dd> Available only for <i>qrsh</i> and </p>
<p> Unlike <i>qsh</i> and <i>qlogin</i>, <i>qrsh</i> does not output any informational messages while establishing the session, compliant with the standard and system calls. If the option <code>-verbose</code> is set, <i>qrsh</i> behaves like the <i>qsh</i> and <i>qlogin</i> commands, printing information about the process of establishing the or session.</p>
<dt><code>-verify</code></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i>. </p>
<p> Instead of submitting a job, prints detailed information about the would-be job as though -j were used, including the effects of command-line parameters and the external environment.</p>
<dt><code>-V</code></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh with command</i> and <i>qalter</i>. </p>
<p> Specifies that all environment variables active within the <i>qsub</i> utility be exported to the context of the job. </p>
<p> All environment variables specified with <code>-v</code>, <code>-V</code> or the DISPLAY variable provided with <code>-display</code> will be exported to the defined JSV instances only optionally when this is requested explicitly during the job submission verification. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-w e</code>|<code>w</code>|<code>n</code>|<code>p</code>|<code>v</code></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i>, <i>qlogin</i> and <i>qalter</i>. </p>
<p> Specifies a validation level applied to the job to be submitted (<i>qsub</i>, <i>qlogin</i>, and <i>qsh</i>) or the specified queued job (<i>qalter</i>). </p>
<p> The specifiers <code>e</code>,&nbsp;<code>w</code>,&nbsp;<code>n</code>,&nbsp;<code>p</code>, and <code>v</code> define the following validation modes: </p>
<pre>
<code>e</code>    error - jobs with invalid requests will be rejected.
<code>w</code>    warning - only a warning will be displayed for invalid
     requests.
<code>n</code>    none - switches off validation; the default for <i>qsub</i>,
     <i>qalter</i>, <i>qrsh</i>, <i>qsh</i> and <i>qlogin</i>.
<code>p</code>    poke - does not submit the job but prints a validation
     report based on a cluster as is with all resource
     utilizations in place.
<code>v</code>    verify - does not submit the job but prints a validation 
     report based on a dry scheduling run on an empty cluster,
     ignoring load values.
</pre>
<p> Resource requests exceeding the configured maximal thresholds or requests for unavailable resource attributes are possible causes for jobs to fail `v&#8217; validation. </p>
<p> Note that the necessary checks are performance consuming and hence the checking is switched off by default. It should also be noted that load values are not taken into account with the verification since they are assumed to be too volatile. To cause -w e verification to be passed at submission time, it is possible to specify non-volatile values (non-consumables) or maximum values (consumables) in complex_values. </p>
<p> If this option, or a corresponding value in <i>qmon</i>, is specified, then this value will be passed to defined JSV instances as a parameter with the name <code>w</code>. (See the <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>-wd</code> <i>working_dir</i></p>
<dd> Available for <i>qsub</i>, <i>qsh</i>, <i>qrsh</i> and <i>qalter</i> only. </p>
<p> Execute the job from the directory specified in <i>working_dir</i>. This switch will activate xxQS_NAMExx&#8217;s path aliasing facility, if the corresponding configuration files are present (see </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. The parameter value will be available in defined JSV instances as parameter with the name <code>cwd</code>. (See <code>-cwd</code> switch above or find more information concerning JSV in</p>
<dt><i>command</i></p>
<dd> Available for <i>qsub</i> and <i>qrsh</i> only. </p>
<p> The job&#8217;s scriptfile or binary. If not present or if the operand is the single-character string &#8216;-&#8216;, <i>qsub</i> reads the script from standard input. </p>
<p> The command will be available in defined JSV instances as parameter with the name <code>CMDNAME</code> (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><i>command_args</i></p>
<dd> Available for <i>qsub</i>, <i>qrsh</i> and <i>qalter</i> only. </p>
<p> Arguments to the job. Not valid if the script is entered from standard input. </p>
<p> <i>Qalter</i> allows changing this option even while the job executes. The modified parameter will only be in effect after a restart or migration of the job, however. </p>
<p> The number of command arguments is provided to configured JSV instances as parameter with the name <code>CMDARGS</code>. Also the argument values can by accessed. Argument names have the format <code>CMDARG</code><i>number</i> where <i>number</i> is a integer between 0 and <code>CMDARGS</code>&nbsp;&#8211; 1. (See <code>-jsv</code> option above or find more information concerning JSV in</p>
<dt><code>xterm_args</code></p>
<dd> Available for <i>qsh</i> only. </p>
<p> Arguments to the executable, as defined in the configuration. For details, refer to </p>
<p> Information concerning <code>xterm_args</code> will be available in JSV context as parameters with the name <code>CMDARGS</code> and <code>CMDARG</code><i>number</i>. Find more information above in section <i>command_args</i>. (See <code>-jsv</code> option above or find more information concerning JSV in</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qsub</i>, <i>qsh</i>, <i>qlogin</i> or <i>qalter</i> use the name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL if that is set, and otherwise the name of the default cell, i.e. <code>default</code>.</p>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry for the service &quot;sge_qmaster&quot; instead to define that port.</p>
<dt><code>DISPLAY</code></p>
<dd> For <i>qsh</i> jobs the DISPLAY has to be specified at job submission. If the DISPLAY is not set by using the <code>-display</code> or the <code>-v</code> switch, the contents of the DISPLAY environment variable are used as default.</p>
<dt><code>QRSH_WRAPPER</code></p>
<dd> Wrapper for <i>qrsh</i> commands (see above).</p>
<dt><code>xxQS_NAME_Sxx_JSV_TIMEOUT</code></p>
<dd> If the response time of the client JSV is greater than this timeout value, then the JSV will attempt to be re-started. The default value is 10 seconds, and this value must be greater than 0. If the timeout has been reached, the JSV will only try to re-start once, if the timeout is reached again an error will occur.</dl>
<p> In addition to those environment variables specified to be exported to the job via the <code>-v</code> or the <code>-V</code> option (see above), <i>qsub</i>, <i>qsh</i>, and <i>qlogin</i> add several variables of the form xxQS_NAME_Sxx_<i>O_NAME</i> whose value is taken from <i>NAME</i> in the submission environment. For each, a variable with the same value is added to the job context, but with a lower-case version of the name, i.e. xqs_name_sxx_o_home in the job context corresponds to xQS_NAME_Sxx_O_HOME in the job environment, and HOME in the submission environment as follows. The context variables are displayed by with the -j option.</p>
<dl>
<dt><code>xxQS_NAME_Sxx_O_HOME</code>,&nbsp;<code>xxQS_NAME_Sxx_O_HOST</code>,&nbsp;<code>xxQS_NAME_Sxx_O_MAIL</code>,&nbsp;<code>xxQS_NAME_Sxx_O_PATH</code>,&nbsp;<code>xxQS_NAME_Sxx_O_TZ</code>,&nbsp;<code>xxQS_NAME_Sxx_O_SHELL</code>,&nbsp;<code>xxQS_NAME_Sxx_O_TERM</code></p>
<dd> As in the description of xxQS_NAME_Sxx_<i>O_NAME</i> above, but the xxQS_NAME_Sxx clients use a library call to determine to determine the host name if HOST is not set. Note that there is no guarantee that these are in any way &quot;correct&quot;, e.g. you should not rely on xxQS_NAME_Sxx_O_HOST for any sort of access control or auditing;</p>
<dt><code>xxQS_NAME_Sxx_O_LOGNAME</code></p>
<dd> As above, but the corresponding context variable is xxqs_name_sxx_log_name.</p>
<dt><code>xxQS_NAME_Sxx_O_WORKDIR</code></p>
<dd> The absolute path of the current working directory of the submitting client, reflected in the context as xxqs_name_sxx_o_workdir and typically corresponding to the CWD environment variable.</dl>
<p> xxQS_NAMExx sets other variables in the job&#8217;s environment, as follows.</p>
<dl>
<dt><code>ARC</code>,&nbsp;<code>xxQS_NAME_Sxx_ARCH</code></p>
<dd> The xxQS_NAMExx architecture name of the node on which the job is running. The name is compiled-in into the binary.</p>
<dt><code>xxQS_NAME_Sxx_BINDING</code></p>
<dd> Contains the selected operating system internal processor numbers. There might be more than the number of selected cores in the presence of SMT or CMT because each core could be represented by multiple processor identifiers. The processor numbers are space-separated.</p>
<dt><code>xxQS_NAME_Sxx_CKPT_ENV</code></p>
<dd> Specifies the checkpointing environment (as selected with the <code>-ckpt</code> option) under which a checkpointing job executes. Only set for checkpointing jobs.</p>
<dt><code>xxQS_NAME_Sxx_CKPT_DIR</code></p>
<dd> Only set for checkpointing jobs. Contains path <i>ckpt_dir</i> (see of the checkpoint interface.</p>
<dt><code>xxQS_NAME_Sxx_CWD_PATH</code></p>
<dd> Specifies the current working directory where the job was started.</p>
<dt><code>xxQS_NAME_Sxx_STDERR_PATH</code></p>
<dd> The pathname of the file to which the standard error stream of the job is diverted. Commonly used for enhancing the output with error messages from prolog, epilog, parallel environment start/stop or checkpointing scripts.</p>
<dt><code>xxQS_NAME_Sxx_STDOUT_PATH</code></p>
<dd> The pathname of the file to which the standard output stream of the job is diverted. Commonly used for enhancing the output with messages from prolog, epilog, parallel environment start/stop or checkpointing scripts.</p>
<dt><code>xxQS_NAME_Sxx_STDIN_PATH</code></p>
<dd> The pathname of the file from which the standard input stream of the job is taken. This variable might be used in combination with xxQS_NAME_Sxx_O_HOST in prolog/epilog scripts to transfer the input file from the submit to the execution host.</p>
<dt><code>xxQS_NAME_Sxx_JOB_SPOOL_DIR</code></p>
<dd> The directory used by to store job related data during job execution. This directory is owned by root or by a xxQS_NAMExx administrative account.</p>
<dt><code>xxQS_NAME_Sxx_TASK_ID</code></p>
<dd> The index number of the current array job task (see <code>-t</code> option above). This is a unique number in each array job and can be used to reference different input data records, for example. This environment variable is set to &quot;undefined&quot; for non-array jobs. It is possible to change the predefined value of this variable with <code>-v</code> or <code>-V</code> (see options above).</p>
<dt><code>xxQS_NAME_Sxx_TASK_FIRST</code></p>
<dd> The index number of the first array job task (see <code>-t</code> option above). It is possible to change the predefined value of this variable with <code>-v</code> or <code>-V</code> (see options above).</p>
<dt><code>xxQS_NAME_Sxx_TASK_LAST</code></p>
<dd> The index number of the last array job task (see <code>-t</code> option above). It is possible to change the predefined value of this variable with <code>-v</code> or <code>-V</code> (see options above).</p>
<dt><code>xxQS_NAME_Sxx_TASK_STEPSIZE</code></p>
<dd> The step size of the array job specification (see <code>-t</code> option above). It is possible to change the predefined value of this variable with <code>-v</code> or <code>-V</code> (see options above).</p>
<dt><code>ENVIRONMENT</code></p>
<dd> The ENVIRONMENT variable is set to BATCH to identify that the job is being executed under xxQS_NAMExx control.</p>
<dt><code>HOME</code></p>
<dd> The user&#8217;s home directory path from the database.</p>
<dt><code>HOSTNAME</code></p>
<dd> The hostname of the node on which the job is running.</p>
<dt><code>JOB_ID</code></p>
<dd> A unique identifier assigned by the when the job was submitted. The job ID is a decimal integer in the range 1 to 99999.</p>
<dt><code>JOB_NAME</code></p>
<dd> The job name. For batch jobs or jobs submitted by <i>qrsh</i> with a command, the job name is the basename of the <i>qsub</i> script/binary filename or the <i>qrsh</i> command. For interactive jobs it is set to &quot;INTERACTIVE&quot; for <i>qsh</i> jobs, &quot;QLOGIN&quot; for <i>qlogin</i> jobs and &quot;QRLOGIN&quot; for <i>qrsh</i> jobs without a command. </p>
<p> This default may be overwritten by the <code>-N</code> option.</p>
<dt><code>JOB_SCRIPT</code></p>
<dd> The path to the job script which is executed. The value can not be overwritten by the <code>-v</code> or <code>-V</code> option.</p>
<dt><code>LOGNAME</code></p>
<dd> The user&#8217;s login name from the passwd database.</p>
<dt><code>NHOSTS</code></p>
<dd> The number of hosts in use by a parallel job.</p>
<dt><code>NQUEUES</code></p>
<dd> The number of queues allocated for the job (always 1 for serial jobs).</p>
<dt><code>NSLOTS</code></p>
<dd> The number of queue slots in use by a parallel job.</p>
<dt><code>PATH</code></p>
<dd> A default shell search path of:<br />
 /usr/local/bin:/usr/ucb:/bin:/usr/bin</p>
<dt><code>xxQS_NAME_Sxx_BINARY_PATH</code></p>
<dd> The path where the xxQS_NAMExx binaries are installed. The value is the concatenation of the cluster configuration value <code>binary_path </code> and the architecture name <code>$xxQS_NAME_Sxx_ARCH</code> environment variable.</p>
<dt><code>PE</code></p>
<dd> The parallel environment under which the job executes (for parallel jobs only).</p>
<dt><code>PE_HOSTFILE</code></p>
<dd> The path of a file containing the definition of the virtual parallel machine assigned to a parallel job by xxQS_NAMExx. See the description of the <code>$pe_hostfile</code> parameter in for details on the format of this file. The environment variable is only available for parallel jobs.</p>
<dt><code>QUEUE</code></p>
<dd> The name of the cluster queue in which the job is running.</p>
<dt><code>REQUEST</code></p>
<dd> Available for batch jobs only. </p>
<p> The request name of a job as specified with the <code>-N</code> switch (see above) or taken as the name of the job script file.</p>
<dt><code>RESTARTED</code></p>
<dd> This variable is set to 1 if a job was restarted after a system crash, or after migration of a non-application-level checkpointing job. It is set to 2 when a job with application-level checkpointing is restarted with a checkpoint available. Otherwise its value is 0.</p>
<dt><code>SHELL</code></p>
<dd> The user&#8217;s login shell from the passwd database. <code>Note:</code> This is not necessarily the shell in use for the job.</p>
<dt><code>TMPDIR</code></p>
<dd> The absolute path to the job&#8217;s temporary working directory. This is usually of the form <code>/tmp/$JOB_ID.$TASK_ID.$SGE_CELL</code>).</p>
<dt><code>TMP</code></p>
<dd> The same as TMPDIR; provided for compatibility with NQS.</p>
<dt><code>TERM</code></p>
<dd> The terminal type imported from the submission session (only for interactive jobs).</p>
<dt><code>TZ</code></p>
<dd> The time zone variable imported from if set.</p>
<dt><code>USER</code></p>
<dd> The user&#8217;s login name from the passwd database.</p>
<dt><code>xxQS_NAME_Sxx_JOB_TASK_ID</code></p>
<dd> A combination of JOB_ID and xxQS_NAME_Sxx_TASK_ID as the expansion of &quot;$JOB_ID.$xxQS_NAME_Sxx_TASK_ID&quot; for array jobs, or &quot;$JOB_ID.0&quot; for non-array jobs. This is useful with other software that only reads a single variable, e.g. Lustre jobstats.</dl>
<p> An additional variable, <code>xxQS_NAME_Sxx_JOBEXIT_STAT</code>, is set to the job exit status in the epilog only (see also</p>
<h2>RESTRICTIONS</h2>
<p> Without <code>-pty y</code>, there is no controlling terminal for batch jobs under xxQS_NAMExx, and any tests or actions on a controlling terminal will fail. If these operations are in your <i>.login</i> or <i>.cshrc</i> file, they may cause your job to abort. </p>
<p> Insert the following test before any commands that are not pertinent to batch jobs in your .login: </p>
<pre>
<dl><dt><dd>if ( $?JOB_NAME) then
<dl><dt><dd>echo &quot;xxQS_NAMExx spooled job&quot;
exit 0
</dl>
endif
</dl>
</pre>
<p> or in your .profile: </p>
<pre>
<dl><dt><dd>if [ ! -z &quot;$JOB_NAME&quot; ] then
<dl><dt><dd>echo &quot;xxQS_NAMExx spooled job&quot;
exit 0
</dl>
fi
</dl>
</pre>
<p> Don&#8217;t forget to set your shell&#8217;s search path in your shell start-up before this code.</p>
<h2>EXIT STATUS</h2>
<p> The following exit values are returned:</p>
<dl>
<dt>0</p>
<dd> Operation was executed successfully.</p>
<dt>25</p>
<dd> It was not possible to register a new job according to the configured <i>max_u_jobs</i> or <i>max_jobs</i> limit. Additional information may be found in</p>
<dt>&gt;0</p>
<dd> Error occurred.</dl>
<h2>EXAMPLES</h2>
<p> The following is the simplest form of a xxQS_NAMExx script file. </p>
<dl>
<dt>
<dd>
<pre>
#!/bin/sh
   ./a.out
</pre>
</dl>
<p> The next example is a more complex xxQS_NAMExx script. </p>
<dl>
<dt>
<dd>
#!/ bin / sh<br />
#Which account to be charged cpu time<br />
#$ &#8211; A santa_claus<br />
#date &#8211; time to run, format[[CC] yy] MMDDhhmm[.SS]<br />
#$ &#8211; a 12241200<br />
#to run I want 6 or more parallel processes<br />
#under the PE pvm.the processes require<br />
# 128M of memory<br />
#$ &#8211; pe pvm 6 &#8211; -l mem = 128<br />
#If I run on dec_x put stderr in / tmp / foo, if I<br />
#run on sun_y, put stderr in / usr / me / foo<br />
#$ &#8211; e dec_x : / tmp / foo, sun_y : / usr / me / foo<br />
#Send mail to these users<br />
#$ &#8211; M santa[at] nothpole, claus[at] northpole<br />
#Mail at beginning / end / on suspension<br />
#$ &#8211; m bes<br />
#Export these environmental variables<br />
#$ &#8211; v PVM_ROOT, FOOBAR = BAR<br />
#The job is located in the current<br />
#working directory.<br />
#$ &#8211; cwd
</dl>
<h2>FILES</h2>
<pre><code>
$REQUEST.oJID[.TASKID] STDOUT of job #JID $REQUEST.eJID[.TASKID] STDERR of job
        $REQUEST.poJID[.TASKID] STDOUT of par.env.of job
            $REQUEST.peJID[.TASKID] STDERR of par.env.of job
                $cwd /
        .xxqs_name_sxx_aliases cwd path aliases
            $cwd /
        .xxqs_name_sxx_request cwd default request
            $HOME /
        .xxqs_name_sxx_aliases user path aliases
            $HOME /
        .xxqs_name_sxx_request user default request&lt;xxqs_name_sxx_root&gt; / &lt;cell&gt; / common / xxqs_name_sxx_aliases cluster path aliases&lt;xxqs_name_sxx_root&gt; / &lt;cell&gt; / common / xxqs_name_sxx_request cluster default request&lt;xxqs_name_sxx_root&gt; / &lt;cell&gt; / common / act_qmaster xxQS_NAMExx master host file
</code></pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> If configured correspondingly, <i>qrsh</i> and <i>qlogin</i> contains portions of the <i>rsh</i>, <i>rshd</i>, <i>telnet</i> and <i>telnetd</i> code copyrighted by The Regents of the University of California. Therefore, the following note applies with respect to <i>qrsh</i> and <i>qlogin</i>: This product includes software developed by the University of California, Berkeley and its contributors. </p>
<p> See as well as the information provided in &lt;xxqs_name_sxx_root&gt;/3rd_party/qrsh and &lt;xxqs_name_sxx_root&gt;/3rd_party/qlogin for a statement of further rights and permissions. </p>
<h2>Index</h2>
