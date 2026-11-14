---
title: "qalter-torque(1)"
name: "qalter-torque"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qalter-torque/"
description: "qalter – alter pbs batch job"
---

<h2 class="name">NAME</h2>
<p> qalter &#8211; alter pbs batch job </p>
<h2>SYNOPSIS</h2>
<p> qalter [-a date_time] [-A account_string] [-c interval] [-e path] [-h hold_list] [-j join] [-k keep] [-l resource_list] [-m mail_options] [-M user_list] [-n node exclusive] [-N name] [-o path] [-p priority] [-r c] [-S path] [-t array_range] [-u user_list] [-W additional_attributes] job_identifier&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>qalter</code> command modifies the attributes of the job or jobs specified by <i> on the command line. Only those attributes listed as options on the command will be modified. If any of the specified attributes cannot be modified for a job for any reason, none of that job&#8217;s attributes will be modified. </p>
<p> The qalter command accomplishes the modifications by sending a Modify Job</i> batch request to the batch server which owns each job.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-a date_time</p>
<dd> Replaces the time at which the job becomes eligible for execution. The <i> argument syntax is: </i><code></p>
<dt>
<dd> If the month, is not specified, it will default to the current month if the specified day is in the future. Otherwise, the month will be set to next month. Likewise, if the day, is not specified, it will default to today if the time is in the future. Otherwise, the day will be set to tomorrow.</p>
<dt>
<dd> This attribute can be altered once the job has begun execution, but it will not take affect until the job is rerun.</p>
<dt>-A account_string</p>
<dd> Replaces the account string associated with the job.</p>
<dt>
<dd> This attribute cannot be altered once the job has begun execution.</p>
<dt>-c interval</p>
<dd> Replaces the the interval at which the job will be checkpointed. If the job executes upon a host which does not support checkpoint, this option will be ignored.</p>
<dt>
<dd> The </code><i> argument is specified as:</p>
<dl>
<dt>
<dd>
<dl>
<dt>n</p>
<dd> No checkpointing is to be performed.</p>
<dt>s</p>
<dd> Checkpointing is to be performed only when the server executing the job is shutdown.</p>
<dt>c</p>
<dd> Checkpointing is to be performed at the default minimum cpu time for the queue from which the job is executing.</p>
<dt>c=minutes</p>
<dd> Checkpointing is to be performed at an interval of which is the integer number of minutes of CPU time used by the job. This value must be greater than zero. If the number is less than the default checkpoint time, the default time will be used.</dl>
</dl>
<dt>
<dd> This attribute can be altered once the job has begun execution, but the new value does not take affect until the job is rerun.</p>
<dt>-e path</p>
<dd> Replaces the path to be used for the standard error stream of the batch job. The argument is of the form:<br />
 </i><code><br />
 where is the name of a host to which the file will be returned and is the path name on that host in the syntax recognized by POSIX 1003.1. The argument will be interpreted as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>path_name</code></p>
<dd> Where path_name is not an absolute path name, then the qalter command will expand the path name relative to the current working directory of the command. The command will supply the name of the host upon which it is executing for the <i> component.</p>
<dt></i><code>hostname:path_name</code></p>
<dd> Where path_name is not an absolute path name, then the qalter command will not expand the path name. The execution server will expand it relative to the home directory of the user on the system specified by hostname.</p>
<dt><code>path_name</code></p>
<dd> Where path_name specifies an absolute path name, then qalter will supply the name of the host on which it is executing for the <i></p>
<dt></i><code>hostname:path_name</code></p>
<dd> Where path_name specifies an absolute path name, the path will be used as specified.</dl>
</dl>
<dt>
<dd> This attribute can be altered once the job has begun execution, but it will not take affect until the job is rerun.</p>
<dt>-h hold_list</p>
<dd> Updates the types of holds on the job. The <i> argument is a string of one or more of the following characters:</p>
<dl>
<dt>
<dd>
<dl>
<dt>u</p>
<dd> Add the USER type hold.</p>
<dt>s</p>
<dd> Add the SYSTEM type hold if the user has the appropriate level of privilege. [Typically reserved to the batch administrator.]</p>
<dt>o</p>
<dd> Add the OTHER (or OPERATOR ) type hold if the user has the appropriate level of privilege. [Typically reserved to the batch administrator and batch operator.]</p>
<dt>n</p>
<dd> Set to none; that is clear the hold types which could be applied with the users level of privilege.</dl>
</dl>
<dt>
<dd> Repetition of characters is permitted, but &quot;n&quot; may not appear in the same option argument with the other three characters. This attribute can be altered once the job has begun execution, but the hold will not take affect until the job is rerun.</p>
<dt>-j join</p>
<dd> Declares which standard streams of the job will be merged together. The argument value may be the characters &quot;oe&quot; and &quot;eo&quot;, or the single character &quot;n&quot;.</p>
<dt>
<dd> A argument value of </i><code> directs that the standard output and standard error streams of the job will be merged, intermixed, and returned as the standard output. A argument value of directs that the standard output and standard error streams of the job will be merged, intermixed, and returned as the standard error.</p>
<dt>
<dd> A value of directs that the two streams will be two separate files. This attribute can be altered once the job has begun execution, but it will not take affect until the job is rerun.</p>
<dt>-k keep</p>
<dd> Defines which if either of standard output or standard error of the job will be retained on the execution host. If set for a stream, this option overrides the path name for that stream.</p>
<dt>
<dd> The argument is either the single letter &quot;e</code>&quot;, &quot;<code>o</code>&quot;, or &quot;<code>n</code>&quot;, or one or more of the letters &quot;<code>e</code>&quot; and &quot;<code>o</code>&quot; combined in either order.</p>
<dl>
<dt>
<dd>
<dl>
<dt>n</p>
<dd> No streams are to be retained.</p>
<dt>e</p>
<dd> The standard error stream is to retained on the execution host. The stream will be placed in the home directory of the user under whose user id the job executed. The file name will be the default file name given by: job_name.<code>e</code>sequence where <code>job_name</code> is the name specified for the job, and <code>sequence</code> is the sequence number component of the job identifier.</p>
<dt>o</p>
<dd> The standard output stream is to be retained on the execution host. The stream will be placed in the home directory of the user under whose user id the job executed. The file name will be the default file name given by: job_name.<code>o</code>sequence where <code>job_name</code> is the name specified for the job, and <code>sequence</code> is the sequence number component of the job identifier.</p>
<dt>eo</p>
<dd> Both the standard output and standard error streams will be retained.</p>
<dt>oe</p>
<dd> Both the standard output and standard error streams will be retained.</dl>
</dl>
<dt>
<dd> This attribute cannot be altered once the job has begun execution.</p>
<dt>-l resource_list</p>
<dd> Modifies the list of resources that are required by the job. The <i> argument is in the following syntax:<br />
 </i><code></p>
<dt>
<dd> If a requested modification to a resource would exceed the resource limits for jobs in the current queue, the server will reject the request.</p>
<dt>
<dd> If the job is running, only certain, resources can be altered. Which resources can be altered in the run state is system dependent. A user may only lower the limit for those resources.</p>
<dt>-m mail_options</p>
<dd> Replaces the set of conditions under which the execution server will send a mail message about the job. The </code><i> argument is a string which consists of the single character &quot;</i><code>n</code>&quot;, or one or more of the characters &quot;<code>a</code>&quot;, &quot;<code>b</code>&quot;, and &quot;<code>e</code>&quot;.</p>
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
<dt>-M user_list</p>
<dd> Replaces the list of users to whom mail is sent by the execution server when it sends mail about the job.</p>
<dt>
<dd> The <i> argument is of the form:<br />
 </i><code></p>
<dt>-n node exclusive</p>
<dd> Sets whether or not the job has node exclusive access. To specify node exclusive access, just use the single character &#8216;y&#8217;. To specify that the job should not have node exclusive access, just use the single character &#8216;n&#8217;.</p>
<dt>-N name</p>
<dd> Renames the job. The name specified may be up to and including 15 characters in length. It must consist of printable, non white space characters with the first character alphabetic.</p>
<dt>-o path</p>
<dd> Replaces the path to be used for the standard output stream of the batch job. The </code><i> argument is of the form:<br />
 </i><code><br />
 where is the name of a host to which the file will be returned and is the path name on that host in the syntax recognized by POSIX. The argument will be interpreted as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>path_name</code></p>
<dd> Where path_name is not an absolute path name, then the qalter command will expand the path name relative to the current working directory of the command. The command will supply the name of the host upon which it is executing for the <i> component.</p>
<dt></i><code>hostname:path_name</code></p>
<dd> Where path_name is not an absolute path name, then the qalter command will not expand the path name. The execution server will expand it relative to the home directory of the user on the system specified by hostname.</p>
<dt><code>path_name</code></p>
<dd> Where path_name specifies an absolute path name, then the qalter will supply the name of the host on which it is executing for the <i></p>
<dt></i><code>hostname:path_name</code></p>
<dd> Where path_name specifies an absolute path name, the path will be used as specified.</dl>
</dl>
<dt>
<dd> This attribute can be altered once the job has begun execution, but it will not take affect until the job is rerun.</p>
<dt>-p priority</p>
<dd> Replaces the priority of the job. The <i> argument must be a integer between -1024 and +1023 inclusive.</p>
<dt>
<dd> This attribute can be altered once the job has begun execution, but it will not take affect until the job is rerun.</p>
<dt>-r c</p>
<dd> Declares whether the job is rerunable. See the </i><code>qrerun </code> command. The option argument <i> is a single character. PBS recognizes the following characters: </i><code> and</p>
<dt>
<dd> If the argument is &quot;y</code>&quot;, the job is marked rerunable. If the argument is &quot;<code>n</code>&quot;, the job is marked as not rerunable.</p>
<dt>-S path</p>
<dd> Declares the shell that interprets the job script.</p>
<dt>
<dd> The option argument <i> is in the form:<br />
 </i><code><br />
 Only one path may be specified for any host named. Only one path may be specified without the corresponding host name. The path selected will be the one with the host name that matched the name of the execution host. If no matching host is found, then if present the path specified without a host will be selected.</p>
<dt>
<dd> If the </code><i> option is not specified, the option argument is the null string, or no entry from the is selected, the execution will use the login shell of the user on the execution host.</p>
<dt>
<dd> This attribute can be altered once the job has begun execution, but it will not take affect until the job is rerun.</p>
<dt>-t array_range</p>
<dd> The argument is an integer id or a range of integers. Multiple ids or id ranges can be combined in a comma delimted list. Examples : -t 1-100 or -t 1,10,50-100</p>
<dt>
<dd> If an array range isn&#8217;t specified, the command tries to operate on the entire array. The command acts on the array (or specified range of the array) just as it would on an individual job.</p>
<dt>
<dd> An optional slot limit can be specified to limit the amount of jobs that can run concurrently in the job array. The default value is unlimited. The slot limit must be the last thing specified in the array_request and is delimited from the array by a percent sign (%).</p>
<dt>
<dd> qalter weatherSimulationArray[] -t %20</p>
<dt>
<dd> Here, the array weatherSimulationArray[] is configured to allow a maximum of 20 concurrently running jobs.</p>
<dt>
<dd> Note: Slot limits can be applied at job submit time with qsub, or can be set in a global server parameter policy with max_slot_limit.</p>
<dt>-u user_list</p>
<dd> Replaces the user name under which the job is to run on the execution system.</p>
<dt>
<dd> The argument is of the form:<br />
 </i><code><br />
 Only one user name may be given for per specified host. Only one of the specifications may be supplied without the corresponding specification. That user name will be used for execution on any host not named in the argument list.</p>
<dt>
<dd> This attribute cannot be altered once the job has begun execution.</p>
<dt>-W additional_attributes</p>
<dd> The -W option allows for the modification of additional job attributes. The general syntax of the -W is in the form:<br />
 </code> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-W attr_name=value[,attr_name=value&#8230;]<br />
 Note if white space occurs anywhere within the option argument string or the equal sign, &quot;=&quot;, occurs within an <i> string, then the string must be enclosed with either single or double quote marks.</p>
<dt>
<dd> PBS currently supports the following attributes within the -W option.</p>
<dt>
<dd> </i><code><br />
 Redefines the dependencies between this and other jobs. The </code><i> is in the form: </i><code><br />
 The </code><i>argument</i> is either a numeric count or a PBS job id according to <i>type .</i> If argument is a count, it must be greater than 0. If it is a job id and is not fully specified in the form: <code> it will be expanded according to the default server rules. If </code><i>argument</i> is null (the preceding colon need not be specified), the dependency of the corresponding type is cleared (unset).</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>synccount:count</code></p>
<dd> This job is the first in a set of jobs to be executed at the same time. <i>Count</i> is the number of additional jobs in the set.</p>
<dt><code>syncwith:jobid</code></p>
<dd> This job is an additional member of a set of jobs to be executed at the same time. <i>Jobid</i> is the job identifier of the first job in the set.</p>
<dt><code>after:jobid[:jobid&#8230;]</code></p>
<dd> This job may be scheduled for execution at any point after jobs <i>jobid</i> have started execution.</p>
<dt><code>afterok:jobid[:jobid&#8230;]</code></p>
<dd> This job may be scheduled for execution only after jobs <i>jobid</i> have terminated with no errors.</p>
<dt><code>afternotok:jobid[:jobid&#8230;]</code></p>
<dd> This job may be scheduled for execution only after jobs <i>jobid</i> have terminated with errors.</p>
<dt><code>afterany:jobid[:jobid&#8230;]</code></p>
<dd> This job may be scheduled for execution after jobs <i>jobid</i> have terminated, with or without errors.</p>
<dt><code>on:count</code></p>
<dd> This job may be scheduled for execution after <code>count</code> dependencies on other jobs have been satisfied. This form is used in conjunction with one of the <code>before</code> forms, see below.</p>
<dt><code>before:jobid[:jobid&#8230;]</code></p>
<dd> When this job has begun execution, then jobs <code>jobid&#8230;</code> may begin.</p>
<dt><code>beforeok:jobid[:jobid&#8230;]</code></p>
<dd> If this job terminates execution without errors, then jobs <code>jobid&#8230;</code> may begin.</p>
<dt><code>beforenotok:jobid[:jobid&#8230;]</code></p>
<dd> If this job terminates execution with errors, then jobs <code>jobid&#8230;</code> may begin.</p>
<dt><code>beforeany:jobid[:jobid&#8230;]</code></p>
<dd> When this job terminates execution, jobs <code>jobid&#8230;</code> may begin.</p>
<dt>
<dd> If any of the <code>before</code> forms are used, the job referenced by <code>jobid</code> must have been submitted with a dependency type of <code>on</code>.</p>
<dt>
<dd> The job specified in any of the <code>before</code> forms must have the same owner as the job being altered.. Otherwise, the dependency will not take effect.</dl>
<p> Error processing of the existence, state, or condition of the job on which the newly submitted job is a deferred service, i.e. the check is performed after the job is queued. If an error is detected, the new job will be deleted by the server. Mail will be sent to the job submitter stating the error.</dl>
<dt>
<dd> <code><br />
 Alters the group name under which the job is to run on the execution system.</p>
<dt>
<dd> The </code><i> argument is of the form: </i><code><br />
 Only one group name may be given per specified host. Only one of the specifications may be supplied without the corresponding specification. That group name will used for execution on any host not named in the argument list.</p>
<dt>
<dd>
<p> Alters which files are staged (copied) in before job start or staged out after the job completes execution. The </code><i> is in the form: </i><code><br />
 The name is the name on the system where the job executes. It may be an absolute path or a path relative to the home directory of the user. The name is the destination name on the host specified by The name may be absolute or relative to the user&#8217;s home directory on the destination host.</dl>
<p> </code></p>
<h2>OPERANDS</h2>
<p> The qalter command accepts one or more <i> operands of the form:<br />
 </i><code><br />
 </code></p>
<h2>STANDARD ERROR</h2>
<p> Any error condition, either in processing the options or the operands, or any error received in reply to the batch requests will result in a error message being written to standard error.</p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qalter command, the exit status will be a value of zero. </p>
<p> If the qalter command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qstat/">qstat</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_alterjob/">pbs_alterjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_statjob/">pbs_statjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_selectjob/">pbs_selectjob</a>(3B), pbs_resources_*(7B), where * is system type, and the PBS ERS. </p>
<h2>Index</h2>
