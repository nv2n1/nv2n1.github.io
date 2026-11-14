---
title: "qsub-torque(1)"
name: "qsub-torque"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qsub-torque/"
description: "qsub – submit pbs job"
---

<h2 class="name">NAME</h2>
<p> qsub &#8211; submit pbs job </p>
<h2>SYNOPSIS</h2>
<p> qsub [-a date_time] [-A account_string] [-b secs] [-c checkpoint_options] [-C directive_prefix] [-d path] [-D path] [-e path] [-f] [-h] [-I] [-j join] [-k keep] [-l resource_list] [-m mail_options] [-M user_list] [-n node exclusive] [-N name] [-o path] [-p priority] [-P proxy_username[:group]] [-q destination] [-r c] [-S path_list] [-t array_request] [-T prologue/epilogue script_name] [-u user_list] [-v variable_list] [-V] [-w] path [-W additional_attributes] [-x] [-X] [-z] [script]</p>
<h2>DESCRIPTION</h2>
<p> To create a job is to submit an executable script to a batch server. The batch server will be the default server unless the <i> option is specified. See discussion of PBS_DEFAULT under Environment Variables below. Typically, the script is a shell script which will be executed by a command shell such as sh or csh. </p>
<p> Options on the </i><code>qsub</code> command allow the specification of attributes which affect the behavior of the job. </p>
<p> The qsub command will pass certain environment variables in the <i> </i><font SIZE="-1"><i> attribute of the job. These variables will be available to the job. The value for the following variables will be taken from the environment of the qsub command: </i><code>HOME</code>, <code>LANG</code>, <code>LOGNAME</code>, <code>PATH</code>, <code>MAIL</code>, <code>SHELL</code>, and <code>TZ</code>. These values will be assigned to a new name which is the current name prefixed with the string &quot;PBS_O_&quot;. For example, the job will have access to an environment variable named <code>PBS_O_HOME</code> which have the value of the variable <code>HOME</code> in the qsub command environment. </p>
<p> In addition to the above, the following environment variables will be available to the batch job.</p>
<dl>
<dt><code>PBS_O_HOST</code></p>
<dd> the name of the host upon which the qsub command is running.</p>
<dt><code>PBS_SERVER</code></p>
<dd> the hostname of the pbs_server which qsub submits the job to.</p>
<dt><code>PBS_O_QUEUE</code></p>
<dd> the name of the original queue to which the job was submitted.</p>
<dt><code>PBS_O_WORKDIR</code></p>
<dd> the absolute path of the current working directory of the qsub command.</p>
<dt><code>PBS_ARRAYID</code></p>
<dd> each member of a job array is assigned a unique identifier (see -t)</p>
<dt><code>PBS_ENVIRONMENT</code></p>
<dd> set to <code> to indicate the job is a batch job, or to to indicate the job is a PBS interactive job, see -I option.</p>
<dt>PBS_JOBID</code></p>
<dd> the job identifier assigned to the job by the batch system.</p>
<dt><code>PBS_JOBNAME</code></p>
<dd> the job name supplied by the user.</p>
<dt><code>PBS_NODEFILE</code></p>
<dd> the name of the file contain the list of nodes assigned to the job (for parallel and cluster systems).</p>
<dt><code>PBS_QUEUE</code></p>
<dd> the name of the queue from which the job is executed.</dl>
<p> </font></p>
<h2>OPTIONS</h2>
<dl>
<dt>-a date_time</p>
<dd> Declares the time after which the job is eligible for execution.</p>
<dl>
<dt>
<dd>
<p> The <i> argument is in the form: </i><code> </p>
<p> Where CC is the first two digits of the year (the century), YY is the second two digits of the year, MM is the two digits for the month, DD is the day of the month, hh is the hour, mm is the minute, and the optional SS is the seconds. </p>
<p> If the month, is not specified, it will default to the current month if the specified day is in the future. Otherwise, the month will be set to next month. Likewise, if the day, is not specified, it will default to today if the time is in the future. Otherwise, the day will be set to tomorrow. For example, if you submit a job at 11:15am with a time of the job will be eligible to run at 11:10am tomorrow.</dl>
<dt>-A account_string</p>
<dd> Defines the account string associated with the job. The </code><i> is an undefined string of characters and is interpreted by the server which executes the job. See section 2.7.1 of the PBS ERS.</p>
<dt>-b seconds</p>
<dd> Defines the maximum number of seconds qsub will block attempting to contact pbs_server. If pbs_server is down, or for a variety of communication failures, qsub will continually retry connecting to pbs_server for job submission. This value overrides the </i><code>CLIENTRETRY</code> parameter in <code>torque.cfg.</code> This is a non-portable TORQUE extension. Portability-minded users can use the <code>PBS_CLIENTRETRY</code> environmental variable. A negative value is interpreted as infinity. The default is 0.</p>
<dt>-c checkpoint_options</p>
<dd> Defines the options that will apply to the job. If the job executes upon a host which does not support checkpoint, these options will be ignored.</p>
<dt>
<dd> Valid checkpoint options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>none</p>
<dd> No checkpointing is to be performed.</p>
<dt>enabled</p>
<dd> Specify that checkpointing is allowed but must be explicitly invoked by either the <code>qhold</code> or <code>qchkpt</code> commands.</p>
<dt>shutdown</p>
<dd> Specify that checkpointing is to be done on a job at pbs_mom shutdown.</p>
<dt>periodic</p>
<dd> Specify that periodic checkpointing is enabled. The default interval is 10 minutes and can be changed by the $checkpoint_interval option in the mom config file or by specifying an interval when the job is submitted</p>
<dt>interval=minutes</p>
<dd> Checkpointing is to be performed at an interval of <i> which is the integer number of minutes of wall time used by the job. This value must be greater than zero.</p>
<dt>depth=number</p>
<dd> Specify a number (depth) of checkpoint images to be kept in the checkpoint directory.</p>
<dt>dir=path</p>
<dd> Specify a checkpoint directory (default is /var/spool/torque/checkpoint).</dl>
</dl>
<dt>-C directive_prefix</p>
<dd> Defines the prefix that declares a directive to the qsub command within the script file. See the paragraph on script directives in the Extended Description section.</p>
<dt>
<dd> If the option is presented with a argument that is the null string, qsub will not scan the script file for directives.</p>
<dt>-d path</p>
<dd> Defines the working directory path to be used for the job. If the option is not specified, the default working directory is the home directory. This option sets the environment variable PBS_O_INITDIR.</p>
<dt>-D path</p>
<dd> Defines the root directory to be used for the job. This option sets the environment variable PBS_O_ROOTDIR.</p>
<dt>-e path</p>
<dd> Defines the path to be used for the standard error stream of the batch job. The argument is of the form:<br />
 </i><code><br />
 where is the name of a host to which the file will be returned and is the path name on that host in the syntax recognized by POSIX. The argument will be interpreted as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>path_name</code></p>
<dd> Where path_name is not an absolute path name, then the qsub command will expand the path name relative to the current working directory of the command. The command will supply the name of the host upon which it is executing for the <i> component.</p>
<dt></i><code>hostname:path_name</code></p>
<dd> Where path_name is not an absolute path name, then the qsub command will not expand the path name relative to the current working directory of the command. On delivery of the standard error, the path name will be expanded relative to the user&#8217;s home directory on the <code>hostname</code> system.</p>
<dt><code>path_name</code></p>
<dd> Where path_name specifies an absolute path name, then the qsub will supply the name of the host on which it is executing for the <i></p>
<dt></i><code>hostname:path_name</code></p>
<dd> Where path_name specifies an absolute path name, the path will be used as specified. <i></p>
<dt></i><code>hostname:</code></p>
<dd> Where hostname specifies the name of the host that the file should be returned to. The path will be the default file name.</dl>
</dl>
<dt>
<dd> If the <i> option is not specified or the </i><code>path_name</code> is not specified or is specified and is a directory, the default file name for the standard error stream will be used. The default name has the following form:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>job_name.esequence_number</code><br />
 where <code>job_name</code> is the name of the job, see <i> option, and </i><code>sequence_number</code> is the job number assigned when the job is submitted.</p>
<dt>-f</p>
<dd> Specifies that the job is fault tolerant. The <i> </i><font SIZE="-1"><i> attribute will be set to true, which indicates that the job can survive the loss of a mom other than the &quot;mother superior&quot; mom (the first node in the exec hosts )</p>
<dt>-h</p>
<dd> Specifies that a user hold be applied to the job at submission time.</p>
<dt>-I</p>
<dd> Declares that the job is to be run &quot;interactively&quot;. The job will be queued and scheduled as any PBS batch job, but when executed, the standard input, output, and error streams of the job are connected through qsub to the terminal session in which qsub is running. Interactive jobs are forced to not rerunable. See the &quot;Extended Description&quot; paragraph for addition information of interactive jobs.</p>
<dt>-j join</p>
<dd> Declares if the standard error stream of the job will be merged with the standard output stream of the job.</p>
<dt>
<dd> An option argument value of </i><code> directs that the two streams will be merged, intermixed, as standard output. An option argument value of directs that the two streams will be merged, intermixed, as standard error.</p>
<dt>
<dd> If the </code><i> argument is </i><code> or the option is not specified, the two streams will be two separate files.</p>
<dt>-k keep</p>
<dd> Defines which (if either) of standard output or standard error will be retained on the execution host. If set for a stream, this option overrides the path name for that stream. If not set, neither stream is retained on the execution host.</p>
<dt>
<dd> The argument is either the single letter &quot;e&quot; or &quot;o&quot;, or the letters &quot;e&quot; and &quot;o&quot; combined in either order. Or the argument is the letter &quot;n&quot;.</p>
<dl>
<dt>
<dd>
<dl>
<dt>e</p>
<dd> The standard error stream is to retained on the execution host. The stream will be placed in the home directory of the user under whose user id the job executed. The file name will be the default file name given by: job_name.esequence</code> where <code>job_name</code> is the name specified for the job, and <code>sequence</code> is the sequence number component of the job identifier.</p>
<dt>o</p>
<dd> The standard output stream is to retained on the execution host. The stream will be placed in the home directory of the user under whose user id the job executed. The file name will be the default file name given by: <code>job_name.osequence</code> where <code>job_name</code> is the name specified for the job, and <code>sequence</code> is the sequence number component of the job identifier.</p>
<dt>eo</p>
<dd> Both the standard output and standard error streams will be retained.</p>
<dt>oe</p>
<dd> Both the standard output and standard error streams will be retained.</p>
<dt>n</p>
<dd> Neither stream is retained.</dl>
</dl>
<dt>-l resource_list</p>
<dd> Defines the resources that are required by the job and establishes a limit to the amount of resource that can be consumed. If not set for a generally available resource, such as CPU time, the limit is infinite. The <i> argument is of the form:<br />
 </i><code></p>
<dt>-m mail_options</p>
<dd> Defines the set of conditions under which the execution server will send a mail message about the job. The </code><i> argument is a string which consists of either the single character &quot;</i><code>n</code>&quot;, or one or more of the characters &quot;<code>a</code>&quot;, &quot;<code>b</code>&quot;, and &quot;<code>e</code>&quot;.</p>
<dt>
<dd> If the character &quot;<code>n</code>&quot; is specified, no mail will be sent.</p>
<dt>
<dd> For the letters &quot;<code>a</code>&quot;, &quot;<code>b</code>&quot;, and &quot;<code>e</code>&quot;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>a</p>
<dd> mail is sent when the job is aborted by the batch system.</p>
<dt>b</p>
<dd> mail is sent when the job begins execution.</p>
<dt>e</p>
<dd> mail is sent when the job terminates.</dl>
</dl>
<dt>
<dd> If the <i> option is not specified, mail will be sent if the job is aborted.</p>
<dt>-M user_list</p>
<dd> Declares the list of users to whom mail is sent by the execution server when it sends mail about the job.</p>
<dt>
<dd> The argument is of the form:<br />
 </i><code><br />
 If unset, the list defaults to the submitting user at the qsub host, i.e. the job owner.</p>
<dt>-n</p>
<dd> Specifies that the job has exclusive access to the nodes it is executing on. This is intended to be used in conjunction with a scheduler that enforces exclusive access, and it tells the cpuset to give the job access to all of that node&#8217;s resources.</p>
<dt>-N name</p>
<dd> Declares a name for the job. The name specified may be up to and including 15 characters in length. It must consist of printable, non white space characters with the first character alphabetic.</p>
<dt>
<dd> If the </code><i> option is not specified, the job name will be the base name of the job script file specified on the command line. If no script file name was specified and the script was read from the standard input, then the job name will be set to </i><code></p>
<dt>-o path</p>
<dd> Defines the path to be used for the standard output stream of the batch job. The </code><i> argument is of the form:<br />
 </i><code><br />
 where is the name of a host to which the file will be returned and is the path name on that host in the syntax recognized by POSIX. The argument will be interpreted as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>path_name</code></p>
<dd> Where path_name is not an absolute path name, then the qsub command will expand the path name relative to the current working directory of the command. The command will supply the name of the host upon which it is executing for the <i> component.</p>
<dt></i><code>hostname:path_name</code></p>
<dd> Where path_name is not an absolute path name, then the qsub command will not expand the path name relative to the current working directory of the command. On delivery of the standard output, the path name will be expanded relative to the user&#8217;s home directory on the <code>hostname</code> system.</p>
<dt><code>path_name</code></p>
<dd> Where path_name specifies an absolute path name, then the qsub will supply the name of the host on which it is executing for the <i></p>
<dt></i><code>hostname:path_name</code></p>
<dd> Where path_name specifies an absolute path name, the path will be used as specified. <i></p>
<dt></i><code>hostname:</code></p>
<dd> Where hostname specifies the name of the host that the file should be returned to. The path will be the default file name.</dl>
</dl>
<dt>
<dd> If the <i> option is not specified or the </i><code>path_name</code> is not specified or is specified and is a directory, the default file name for the standard output stream will be used. The default name has the following form:<br />
 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>job_name.osequence_number</code><br />
 where <code>job_name</code> is the name of the job, see <i> option, and </i><code>sequence_number</code> is the job number assigned when the job is submitted.</p>
<dt>-p priority</p>
<dd> Defines the priority of the job. The <i> argument must be a integer between -1024 and +1023 inclusive. The default is no priority which is equivalent to a priority of zero.</p>
<dt>-P proxy_user[:group]</p>
<dd> Proxy user for whom the job should be submitted. This option is only available for the super user.</p>
<dt>-q destination</p>
<dd> Defines the destination of the job. The names a queue, a server, or a queue at a server.</p>
<dt>
<dd> The qsub command will submit the script to the server defined by the argument. If the destination is a routing queue,</i> the job may be routed by the server to a new destination.</p>
<dt>
<dd> If the <i> option is not specified, the qsub command will submit the script to the default server. See PBS_DEFAULT under the Environment Variables section on this man page and the PBS ERS section 2.7.4, &quot;Default Server&quot;.</p>
<dt>
<dd> If the option is specified, it is in one of the following three forms:<br />
 </i><code> </p>
<dt>
<dd> If the </code><i> argument names a queue and does not name a server, the job will be submitted to the named queue at the default server.</p>
<dt>
<dd> If the argument names a server and does not name a queue, the job will be submitted to the default queue at the named server.</p>
<dt>
<dd> If the argument names both a queue and a server, the job will be submitted to the named queue at the named server.</p>
<dt>-r y|n</p>
<dd> Declares whether the job is rerunable. See the </i><code>qrerun</code> command. The option argument is a single character, either <code> or</p>
<dt>
<dd> If the argument is &quot;y</code>&quot;, the job is rerunable. If the argument is &quot;<code>n</code>&quot;, the job is not rerunable. The default value is &#8216;y&#8217;, rerunable.</p>
<dt>-S path_list</p>
<dd> Declares the shell that interprets the job script.</p>
<dt>
<dd> The option argument <i> is in the form:<br />
 </i><code><br />
 Only one path may be specified for any host named. Only one path may be specified without the corresponding host name. The path selected will be the one with the host name that matched the name of the execution host. If no matching host is found, then the path specified without a host will be selected, if present.</p>
<dt>
<dd> If the </code><i> option is not specified, the option argument is the null string, or no entry from the is selected, the execution will use the user&#8217;s login shell on the execution host.</p>
<dt>-t array_request</p>
<dd> Specifies the task ids of a job array. Single task arrays are allowed.</p>
<dt>
<dd> The argument is an integer id or a range of integers. Multiple ids or id ranges can be combined in a comma delimted list. Examples : -t 1-100 or -t 1,10,50-100</p>
<dt>
<dd> An optional slot limit can be specified to limit the amount of jobs that can run concurrently in the job array. The default value is unlimited. The slot limit must be the last thing specified in the array_request and is delimited from the array by a percent sign (%).</p>
<dt>
<dd> qsub script.sh -t 0-299%5</p>
<dt>
<dd> This sets the slot limit to 5. Only 5 jobs from this array can run at the same time.</p>
<dt>
<dd> Note: You can use qalter to modify slot limits on an array. The server parameter max_slot_limit can be used to set a global slot limit policy.</p>
<dt>-T script_name</p>
<dd> Allows for per job prologue and epilogue scripts. The full script name will be prologue.[name] or epilogue.[name]. For the job submission, only request the name of the prologue or epilogue script.</p>
<dt>
<dd> Example: </i><code><br />
 Specifies to use the script prologue.prescript</p>
<dt>-u user_list</p>
<dd> Defines the user name under which the job is to run on the execution system.</p>
<dt>
<dd> The </code><i> argument is of the form:<br />
 </i><code><br />
 Only one user name may be given per specified host. Only one of the specifications may be supplied without the corresponding specification. That user name will used for execution on any host not named in the argument list. If unset, the user list defaults to the user who is running qsub.</p>
<dt>-v variable_list</p>
<dd> Expands the list of environment variables that are exported to the job.</p>
<dt>
<dd> In addition to the variables described in the &quot;Description&quot; section above, </code><i> names environment variables from the qsub command environment which are made available to the job when it executes. The is a comma separated list of strings of the form </i><code> or These variables and their values are passed to the job.</p>
<dt>-V</p>
<dd> Declares that all environment variables in the qsub command&#8217;s environment are to be exported to the batch job.</p>
<dt>-w path</p>
<dd> Defines the working directory path to be used for the job. If the </code><i> option is not specified, the default working directory is the current directory. This option sets the environment variable PBS_O_WORKDIR.</p>
<dt>-W additional_attributes</p>
<dd> The -W option allows for the specification of additional job attributes. The general syntax of the -W is in the form:<br />
 </i><code><br />
 Note if white space occurs anywhere within the option argument string or the equal sign, &quot;=&quot;, occurs within an </code><i> string, then the string must be enclosed with either single or double quote marks.</p>
<dt>
<dd> PBS currently supports the following attributes within the -W option.</p>
<dt>
<dd> </i><code><br />
 Defines the dependency between this and other jobs. The </code><i> is in the form:<br />
 </i><code><br />
 The </code><i>argument</i> is either a numeric count or a PBS job id according to <i>type .</i> If argument is a count, it must be greater than 0. If it is a job id and not fully specified in the form <code> it will be expanded according to the default server rules which apply to job IDs on most commands. If </code><i>argument</i> is null (the preceding colon need not be specified), the dependency of the corresponding type is cleared (unset).</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>synccount:count</code></p>
<dd> This job is the first in a set of jobs to be executed at the same time. <i>Count</i> is the number of additional jobs in the set.</p>
<dt><code>syncwith:jobid</code></p>
<dd> This job is an additional member of a set of jobs to be executed at the same time. In the above and following dependency types, <i>jobid</i> is the job identifier of the first job in the set.</p>
<dt><code>after:jobid[:jobid&#8230;]</code></p>
<dd> This job may be scheduled for execution at any point after jobs <i>jobid</i> have started execution.</p>
<dt><code>afterok:jobid[:jobid&#8230;]</code></p>
<dd> This job may be scheduled for execution only after jobs <i>jobid</i> have terminated with no errors. See the csh warning under &quot;Extended Description&quot;.</p>
<dt><code>afternotok:jobid[:jobid&#8230;]</code></p>
<dd> This job may be scheduled for execution only after jobs <i>jobid</i> have terminated with errors. See the csh warning under &quot;Extended Description&quot;.</p>
<dt><code>afterany:jobid[:jobid&#8230;]</code></p>
<dd> This job may be scheduled for execution after jobs <i>jobid</i> have terminated, with or without errors.</p>
<dt><code>on:count</code></p>
<dd> This job may be scheduled for execution after <code>count</code> dependencies on other jobs have been satisfied. This form is used in conjunction with one of the <code>before</code> forms, see below.</p>
<dt><code>before:jobid[:jobid&#8230;]</code></p>
<dd> When this job has begun execution, then jobs <code>jobid&#8230;</code> may begin.</p>
<dt><code>beforeok:jobid[:jobid&#8230;]</code></p>
<dd> If this job terminates execution without errors, then jobs <code>jobid&#8230;</code> may begin. See the csh warning under &quot;Extended Description&quot;.</p>
<dt><code>beforenotok:jobid[:jobid&#8230;]</code></p>
<dd> If this job terminates execution with errors, then jobs <code>jobid&#8230;</code> may begin. See the csh warning under &quot;Extended Description&quot;.</p>
<dt><code>beforeany:jobid[:jobid&#8230;]</code></p>
<dd> When this job terminates execution, jobs <code>jobid&#8230;</code> may begin.</p>
<dt>
<dd> If any of the <code>before</code> forms are used, the jobs referenced by <code>jobid</code> must have been submitted with a dependency type of <code>on</code>.</p>
<dt><code>Array Dependencies</code></p>
<dd> It is now possible to have a job depend on an array. These dependencies are in the form depend=arraydep:arrayid[num]. If [num] is not present, then the dependencies applies to the entire array. If [num] is present, then num means the number of jobs that must meet the condition for the dependency to be satisfied.</p>
<dt><code>afterstartarray:arrayid[count]</code></p>
<dd> This job may be scheduled for execution only after jobs in <i>arrayid</i> have started execution.</p>
<dt><code>afterokarray:arrayid[count]</code></p>
<dd> This job may be scheduled for execution only after jobs in <i>arrayid</i> have terminated with no errors.</p>
<dt><code>afternotok:arrayid[count]</code></p>
<dd> This job may be scheduled for execution only after jobs in <i>arrayid</i> have terminated with errors.</p>
<dt><code>afteranyarray:arrayid[count]</code></p>
<dd> This job may be scheduled for execution after jobs in <i>array id</i> have terminated, with or without errors.</p>
<dt><code>beforestartarray:arrayid[count]</code></p>
<dd> This job may be scheduled for execution only before jobs in <i>arrayid</i> have started execution.</p>
<dt><code>beforeokarray:arrayid[count]</code></p>
<dd> This job may be scheduled for execution only before jobs in <i>arrayid</i> have terminated with no errors.</p>
<dt><code>beforenotok:arrayid[count]</code></p>
<dd> This job may be scheduled for execution only before jobs in <i>arrayid</i> have terminated with errors.</p>
<dt><code>beforeanyarray:arrayid[count]</code></p>
<dd> This job may be scheduled for execution before jobs in <i>array id</i> have terminated, with or without errors.</p>
<dt>
<dd> If any of the <code>before</code> forms are used, the jobs referenced by <code>jobid</code> must have the same owner as the job being submitted. Otherwise, the dependency is ignored.</dl>
<p> Error processing of the existence, state, or condition of the job on which the newly submitted job is a deferred service, i.e. the check is performed after the job is queued. If an error is detected, the new job will be deleted by the server. Mail will be sent to the job submitter stating the error. </p>
<p> Dependency examples:<br />
 <code> </p>
</dl>
<dt>
<dd>
 Defines the group name under which the job is to run on the execution system. The </code><i> argument is of the form:<br />
 </i><code><br />
 Only one group name may be given per specified host. Only one of the specifications may be supplied without the corresponding specification. That group name will used for execution on any host not named in the argument list. If not set, the </code><i> </i></font><font SIZE="-2"><i> defaults to the primary group of the user under which the job will be run.</p>
<dt>
<dd> </i><code><br />
 If the interactive attribute is specified, the job is an interactive job. The -I option is a alternative method of specifying this attribute.</p>
<dt>
<dd>
<p> Specifies which files are staged (copied) in before job start or staged out after the job completes execution. On completion of the job, all staged-in and staged-out files are removed from the execution system. The </code><i> is in the form<br />
 </i><code><br />
 regardless of the direction of the copy. The name is the name of the file on the system where the job executed. It may be an absolute path or relative to the home directory of the user. The name is the destination name on the host specified by The name may be absolute or relative to the user&#8217;s home directory on the destination host. The use of wildcards in the file name is not recommended. The file names map to a remote copy program (rcp) call on the execution system in the follow manner:<br />
 For stagein: rcp hostname:remote_file local_file<br />
 For stageout: rcp local_file hostname:remote_file<br />
 Data staging examples: </p>
<p> If TORQUE has been compiled with wordexp support, then variables can be used in the specified paths. Currently only $PBS_JOBID, $HOME, and $TMPDIR are supported for stagein.</p>
<dt>
<dd>
 Sets umask used to create stdout and stderr spool files in pbs_mom spool directory. Values starting with 0 are treated as octal values, otherwise the value is treated as a decimal umask value. </p>
<dt>-x</p>
<dd> When running an interactive job, the -x flag makes it so that the script won&#8217;t be parsed for PBS directives, but instead will be a command that is launched once the interactive job has started. The job will terminate at the completion of this command.</p>
<dt>-X</p>
<dd> Enables X11 forwarding. The DISPLAY environment variable must be set.</p>
<dt>-z</p>
<dd> Directs that the qsub command is not to write the job identifier assigned to the job to the command&#8217;s standard output.</dl>
<p> </code></font></p>
<h2>OPERANDS</h2>
<p> The qsub command accepts a <i> operand that is the path to the script of the job. If the path is relative, it will be expanded relative to the working directory of the qsub command. </p>
<p> If the operand is not provided or the operand is the single character &quot;-&quot;, the qsub command reads the script from standard input. When the script is being read from Standard Input, qsub will copy the file to a temporary file. This temporary file is passed to the library interface routine pbs_submit. The temporary file is removed by qsub after pbs_submit returns or upon the receipt of a signal which would cause qsub to terminate. </i></p>
<h2>STANDARD INPUT</h2>
<p> The qsub command reads the script for the job from standard input if the <i> operand is missing or is the single character &quot;-&quot;. </i></p>
<h2>INPUT FILES</h2>
<p> The <i> file is read by the qsub command. Qsub acts upon any directives found in the script. </p>
<p> When the job is created, a copy of the script file is made and that copy cannot be modified. </i></p>
<h2>STANDARD OUTPUT</h2>
<p> Unless the <i> option is set, the job identifier assigned to the job will be written to standard output if the job is successfully created. </i></p>
<h2>STANDARD ERROR</h2>
<p> The qsub command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The values of some or all of the variables in the qsub command&#8217;s environment are exported with the job, see the -v and -V options. </p>
<p> The environment variable <code>PBS_DEFAULT</code> defines the name of the default server. Typically, it corresponds to the system name of the host on which the server is running. If PBS_DEFAULT is not set, the default is defined by an administrator established file. </p>
<p> The environment variable <code>PBS_DPREFIX</code> determines the prefix string which identifies directives in the script. </p>
<p> The environment variable <code>PBS_CLIENTRETRY</code> defines the maximum number of seconds qsub will block. See the -b option above. Despite the name, currently qsub is the only client that supports this option.</p>
<h2>TORQUE.CFG</h2>
<p> The torque.cfg file, located in PBS_SERVER_HOME (/var/spool/torque by default) controls the behavior of the qsub command. This file contains a list of parameters and values separated by whitespace </p>
<p> <code>QSUBSLEEP</code> takes an integer operand which specifies time to sleep when running qsub command. Used to prevent users from overwhelming the scheduler. </p>
<p> <code>SUBMITFILTER</code> specifies the path to the submit filter used to pre-process job submission. The default path is $(libexecdir)/qsub_filter, which falls back to /usr/local/sbin/torque_submitfilter for backwards compatibility. This torque.cfg parameter overrides this default. </p>
<p> <code>SERVERHOST</code> specifies the value for the PBS_SERVER environment variable </p>
<p> <code>QSUBHOST</code> specifies the hostname for the jobs QSUB_O_HOST variable </p>
<p> <code>QSUBSENDUID</code> specifies a uid to use for the jobs PBS_O_UID variable </p>
<p> <code>XAUTHPATH</code> specifies the path to xauth </p>
<p> <code>CLIENTRETRY</code> specifies the integer seconds between retry attempts to communicate with pbs_server </p>
<p> <code>VALIDATEGROUP</code> set this parameter to force qsub to verify the submitter&#8217;s group id </p>
<p> <code>DEFAULTCKPT</code> specifies the default value for the jobs checkpoint attribute. The user overrides this with the -c qsub option. </p>
<p> <code>VALIDATEPATH</code> set this parameter to force qsub to validate local existence of a &quot;-d&quot; working directory </p>
<p> <code>RERUNNABLEBYDEFAULT</code> this parameter specifies if a job is rerunnable by default. The default is true, setting this to false causes the rerunnable attribute value to be false unless the users specifies otherwise with the -r option </p>
<p> <code>FAULT_TOLERANT_BY_DEFAULT</code> this parameter specifies if a job is fault tolerant by default. The default value for the fault_tolerant job attribute is false, setting this parameter to true causes the default value of the attribute to be true. The user can specify their preference with the -f qsub option. </p>
<p> For example:</p>
<dl>
<dt>
<dd></dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> Script Processing: </p>
<p> A job script may consist of PBS directives, comments and executable statements. A PBS directive provides a way of specifying job attributes in addition to the command line options. For example:</p>
<dl>
<dt>
<dd></dl>
<p> The qsub command scans the lines of the script file for directives. An initial line in the script that begins with the characters &quot;#!&quot; or the character &quot;:&quot; will be ignored and scanning will start with the next line. Scanning will continue until the first executable line, that is a line that is not blank, not a directive line, nor a line whose first non white space character is &quot;#&quot;. If directives occur on subsequent lines, they will be ignored. </p>
<p> A line in the script file will be processed as a directive to qsub if and only if the string of characters starting with the first non white space character on the line and of the same length as the directive prefix matches the directive prefix. </p>
<p> The remainder of the directive line consists of the options to qsub in the same syntax as they appear on the command line. The option character is to be preceded with the &quot;-&quot; character. </p>
<p> If an option is present in both a directive and on the command line, that option and its argument, if any, will be ignored in the directive. The command line takes precedence. </p>
<p> If an option is present in a directive and not on the command line, that option and its argument, if any, will be processed as if it had occurred on the command line. </p>
<p> The directive prefix string will be determined in order of preference from:</p>
<dl>
<dt>
<dd>
<p> The value of the <i> option argument if the option is specified on the command line. </p>
<p> The value of the environment variable </i><code>PBS_DPREFIX </code> if it is defined. </p>
<p> The four character string <code> </p>
</dl>
<p> If the </code><i> option is found in a directive in the script file, it will be ignored. </p>
<p> User Authorization: </p>
<p> When the user submits a job from a system other than the one on which the PBS Server is running, the name under which the job is to be executed is selected according to the rules listed under the -u option. The user submitting the job must be authorized to run the job under the execution user name. This authorization is provided if</p>
<dl>
<dt>
<dd>
<dl>
<dt>(1)</p>
<dd> The host on which qsub is run is trusted by the execution host (see /etc/hosts.equiv),</p>
<dt>(2)</p>
<dd> The execution user has an .rhosts file naming the submitting user on the submitting host.</dl>
</dl>
<p> C-Shell .logout File: </p>
<p> The following warning applies for users of the c-shell, csh. If the job is executed under the csh and a .logout</i> file exists in the home directory in which the job executes, the exit status of the job is that of the .logout script, not the job script. This may impact any inter-job dependencies. To preserve the job exit status, either remove the .logout file or place the following line as the first line in the .logout file<br />
 <code><br />
 and the following line as the last executable line in .logout </p>
<p> Interactive Jobs: </p>
<p> If the </code><i> option is specified on the command line or in a script directive, or if the &quot;interactive&quot; job attribute declared true via the -W option, </i><code> either on the command line or in a script directive, the job is an interactive job. The script will be processed for directives, but will not be included with the job. When the job begins execution, all input to the job is from the terminal session in which qsub is running. </p>
<p> When an interactive job is submitted, the qsub command will not terminate when the job is submitted. Qsub will remain running until the job terminates, is aborted, or the user interrupts qsub with an SIGINT (the control-C key). If qsub is interrupted prior to job start, it will query if the user wishes to exit. If the user response &quot;yes&quot;, qsub exits and the job is aborted. </p>
<p> Once the interactive job has started execution, input to and output from the job pass through qsub. Keyboard generated interrupts are passed to the job. Lines entered that begin with the tilde (&#8216;~&#8217;) character and contain special sequences are escaped by qsub. The recognized escape sequences are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>~.</p>
<dd> Qsub terminates execution. The batch job is also terminated.</p>
<dt>~susp</p>
<dd> Suspend the qsub program if running under the C shell. &quot;susp&quot; is the suspend character, usually CNTL-Z.</p>
<dt>~asusp</p>
<dd> Suspend the input half of qsub (terminal to job), but allow output to continue to be displayed. Only works under the C shell. &quot;asusp&quot; is the auxiliary suspend character, usually CNTL-Y.</dl>
</dl>
<p> </code></p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing, the qsub exit status will be a value of zero. </p>
<p> If the qsub command fails, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qalter/">qalter</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qdel/">qdel</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qhold/">qhold</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qmove/">qmove</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qmsg/">qmsg</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qrerun/">qrerun</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qrls/">qrls</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qselect/">qselect</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qsig/">qsig</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qstat/">qstat</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_connect/">pbs_connect</a>(3B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_job_attributes/">pbs_job_attributes</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_queue_attributes/">pbs_queue_attributes</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_irix5/">pbs_resources_irix5</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_sp2/">pbs_resources_sp2</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_sunos4/">pbs_resources_sunos4</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_resources_unicos8/">pbs_resources_unicos8</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_server_attributes/">pbs_server_attributes</a>(7B), and <a href="//www.systutorials.com/docs/linux/man/8B-pbs_server/">pbs_server</a>(8B) </p>
<h2>Index</h2>
