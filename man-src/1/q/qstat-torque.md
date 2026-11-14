---
title: "qstat-torque(1)"
name: "qstat-torque"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qstat-torque/"
description: "qstat – show status of pbs batch jobs"
---

<h2 class="name">NAME</h2>
<p> qstat &#8211; show status of pbs batch jobs </p>
<h2>SYNOPSIS</h2>
<p> qstat [-f [-1]] [-l] [-W site_specific] [-x] [job_identifier&#8230; | destination&#8230;] </p>
<p> qstat [-a|-i|-r|-e] [-l] [-n [-1]] [-s] [-G|-M] [-R] [-u user_list] [job_identifier&#8230; |&nbsp;<wbr> destination&#8230;] </p>
<p> qstat -Q [-f [-1]][-W site_specific] [-l] [destination&#8230;] </p>
<p> qstat -q [-G|-M] [-l] [destination&#8230;] </p>
<p> qstat -B [-f [-1]][-W site_specific] [-l] [server_name&#8230;] </p>
<p> qstat -t</p>
<h2>DESCRIPTION</h2>
<p> The <code>qstat</code> command is used to request the status of jobs, queues, or a batch server. The requested status is written to standard out. </p>
<p> When requesting job status, synopsis format 1 or 2, <code>qstat</code> will output information about each <i> or all jobs at each Jobs for which the user does not have status privilege are not displayed. </p>
<p> When requesting queue or server status, synopsis format 3 through 5, qstat will output information about each </i></p>
<h2>OPTIONS</h2>
<dl>
<dt>-f</p>
<dd> Specifies that a full status display be written to standard out.</p>
<dt>-a</p>
<dd> &quot;All&quot; jobs are displayed in the alternative format, see the Standard Output section. If the operand is a destination id, all jobs at that destination are displayed. If the operand is a job id, information about that job is displayed.</p>
<dt>-e</p>
<dd> If the operand is a job id or not specified, only jobs in executable queues are displayed. Setting the PBS_QSTAT_EXECONLY environment variable will also enable this option.</p>
<dt>-i</p>
<dd> Job status is displayed in the alternative format. For a destination id operand, status for jobs at that destination which are not running are displayed. This includes jobs which are queued, held or waiting. If an operand is a job id, status for that job is displayed regardless of its state.</p>
<dt>-r</p>
<dd> If an operand is a job id, status for that job is displayed. For a destination id operand, status for jobs at that destination which are running are displayed, this includes jobs which are suspended.</p>
<dt>-n</p>
<dd> In addition to the basic information, nodes allocated to a job are listed.</p>
<dt>-1</p>
<dd> In combination with -n, the -1 option puts all of the nodes on the same line as the job ID. In combination with -f, attributes are not folded to fit in a terminal window. This is intended to ease the parsing of the qstat output.</p>
<dt>-s</p>
<dd> In addition to the basic information, any comment provided by the batch administrator or scheduler is shown.</p>
<dt>-G</p>
<dd> Show size information in giga-bytes.</p>
<dt>-M</p>
<dd> Show size information, disk or memory in mega-words. A word is considered to be 8 bytes.</p>
<dt>-R</p>
<dd> In addition to other information, disk reservation information is shown. Not applicable to all systems.</p>
<dt>-t</p>
<dd> Normal qstat output displays a summary of the array instead of the entire array, job for job. qstat -t expands the output to display the entire array. Note that arrays are now named with brackets following the array name; for example: </p>
<p> echo sleep 20 | qsub -t 0-299 189[].pali </p>
<p> Individual jobs in the array are now also noted using square brackets instead of dashes; for example, here is part of the output of qstat -t for the preceding array: </p>
<p> 189[299].napali STDIN[299] dbeer 0 Q batch</p>
<dt>-u</p>
<dd> Job status is displayed in the alternative format. If an operand is a job id, status for that job is displayed. For a destination id operand, status for jobs at that destination which are owned by the user(s) listed in <i> are displayed. The syntax of the is:<br />
 </i><code><br />
 Host names may be wild carded on the left end, e.g. &quot;*.nasa.gov&quot;. User_name without a &quot;@host&quot; is equivalent to &quot;user_name@*&quot;, that is at any host.</p>
<dt>-Q</p>
<dd> Specifies that the request is for queue status and that the operands are destination identifiers.</p>
<dt>-q</p>
<dd> Specifies that the request is for queue status which should be shown in the alternative format.</p>
<dt>-B</p>
<dd> Specifies that the request is for batch server status and that the operands are the names of servers.</p>
<dt>-x</p>
<dd> Specifies that the output is to be displayed in XML form. This option is only valid with the -f option or by itself, which will also specify the -f full status display.</p>
<dt>-l</p>
<dd> Specifies that the long name of the job (or the job name appended with the suffix alias) should be displayed.</dl>
<p> </code></p>
<h2>OPERANDS</h2>
<p> If neither the <i> nor the option is given, the operands on the qstat command must be either job identifiers or destinations identifiers. </p>
<p> If the operand is a job identifier, it must be in the following form:</p>
<dl>
<dt>
<dd> </i><code></dl>
<p> where is the job identifier assigned at submittal time, see qsub</code>. If the <code> is omitted, the name of the default server will be used. If is supplied, the request will be for the job identifier currently at that Server. </p>
<p> If the operand is a destination identifier, it is one of the following three forms:</p>
<dl>
<dt>
<dd>
</dl>
<p> If is specified, the request is for status of all jobs in that queue at the default server. If the form is given, the request is for status of all jobs at that server. If a full destination identifier, is given, the request is for status of all jobs in the named queue at the named server. </p>
<p> If the </code><i> option is given, the operands are destination identifiers as specified above. If </i><code> is specified, the status of that queue at the default server will be given. If is specified, the status of the named queue at the named server will be given. If is specified, the status of all queues at the named server will be given. If no destination is specified, the status of all queues at the default server will be given. </p>
<p> If the </code><i> option is given, the operand is the name of a server. </i></p>
<h2>STANDARD OUTPUT</h2>
<p> Displaying Job Status </p>
<p> If job status is being displayed in the default format and the <i> option is not specified, the following items are displayed on a single line, in the specified order, separated by white space:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> the job identifier assigned by PBS.</p>
<dt>&#8211;</p>
<dd> the job name given by the submitter.</p>
<dt>&#8211;</p>
<dd> the job owner</p>
<dt>&#8211;</p>
<dd> the CPU time used</p>
<dt>&#8211;</p>
<dd> the job state:</p>
<dl>
<dt>
<dd> C &#8211; Job is completed after having run/<br />
 E &#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Job is exiting after having run.</p>
<p> H &#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Job is held.</p>
<p> Q &#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>job is queued, eligible to run or routed.</p>
<p> R &#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>job is running.</p>
<p> T &#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>job is being moved to new location.</p>
<p> W &#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>job is waiting for its execution time</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(-a option) to be reached.</p>
<p> S &#8211;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>(Unicos only) job is suspend.</p>
</dl>
<dt>&#8211;</p>
<dd> the queue in which the job resides</dl>
</dl>
<p> If job status is being displayed and the option is specified, the output will depend on whether </i><code>qstat</code> was compiled to use a <code>Tcl</code> interpreter. See the configuration section for details. If <code>Tcl</code> is not being used, full display for each job consists of the header line:<br />
 <code> job identifier<br />
 Followed by one line per job attribute of the form: </p>
<p> If any of the options -a, -i, -r, -u, -n, -s, -G or -M are provided, the alternative display format for jobs is used. The following items are displayed on a single line, in the specified order, separated by white space:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> the job identifier assigned by PBS.</p>
<dt>&#8211;</p>
<dd> the job owner.</p>
<dt>&#8211;</p>
<dd> The queue in which the job currently resides.</p>
<dt>&#8211;</p>
<dd> The job name given by the submitter.</p>
<dt>&#8211;</p>
<dd> The session id (if the job is running).</p>
<dt>&#8211;</p>
<dd> The number of nodes requested by the job.</p>
<dt>&#8211;</p>
<dd> The number of cpus or tasks requested by the job.</p>
<dt>&#8211;</p>
<dd> The amount of memory requested by the job.</p>
<dt>&#8211;</p>
<dd> Either the cpu time, if specified, or wall time requested by the job, (hh:mm).</p>
<dt>&#8211;</p>
<dd> The job&#8217;s current state.</p>
<dt>&#8211;</p>
<dd> The amount of cpu time or wall time used by the job (hh:mm).</dl>
</dl>
<p> If the -R option is provided, the line contains:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> the job identifier assigned by PBS.</p>
<dt>&#8211;</p>
<dd> the job owner.</p>
<dt>&#8211;</p>
<dd> The queue in which the job currently resides.</p>
<dt>&#8211;</p>
<dd> The number of nodes requested by the job.</p>
<dt>&#8211;</p>
<dd> The number of cpus or tasks requested by the job.</p>
<dt>&#8211;</p>
<dd> The amount of memory requested by the job.</p>
<dt>&#8211;</p>
<dd> Either the cpu time or wall time requested by the job.</p>
<dt>&#8211;</p>
<dd> The job&#8217;s current state.</p>
<dt>&#8211;</p>
<dd> The amount of cpu time or wall time used by the job.</p>
<dt>&#8211;</p>
<dd> The amount of SRFS space requested on the big file system.</p>
<dt>&#8211;</p>
<dd> The amount of SRFS space requested on the fast file system.</p>
<dt>&#8211;</p>
<dd> The amount of space requested on the parallel I/O file system.</dl>
</dl>
<p> The last three fields may not contain useful information at all sites or on all systems.<br />
 Note: Remaining walltime does not account for walltime multiplication factors. </p>
<p> Displaying Queue Status </p>
<p> If queue status is being displayed and the </code><i> option was not specified, the following items are displayed on a single line, in the specified order, separated by white space:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> the queue name</p>
<dt>&#8211;</p>
<dd> the maximum number of jobs that may be run in the queue concurrently</p>
<dt>&#8211;</p>
<dd> the total number of jobs in the queue</p>
<dt>&#8211;</p>
<dd> the enable or disabled status of the queue</p>
<dt>&#8211;</p>
<dd> the started or stopped status of the queue</p>
<dt>&#8211;</p>
<dd> for each job state, the name of the state and the number of jobs in the queue in that state.</p>
<dt>&#8211;</p>
<dd> the type of queue, execution or routing.</dl>
</dl>
<p> If queue status is being displayed and the option is specified, the output will depend on whether </i><code>qstat</code> was compiled to use a <code>Tcl</code> interpreter. See the configuration section for details. If <code>Tcl</code> is not being used, the full display for each queue consists of the header line:<br />
 <code> queue_name<br />
 Followed by one line per queue attribute of the form: </p>
<p> If the -q option is specified, queue information is displayed in the alternative format: The following information is displayed on a single line:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> the queue name</p>
<dt>&#8211;</p>
<dd> the maximum amount of memory a job in the queue may request</p>
<dt>&#8211;</p>
<dd> the maximum amount of cpu time a job in the queue may request</p>
<dt>&#8211;</p>
<dd> the maximum amount of wall time a job in the queue may request</p>
<dt>&#8211;</p>
<dd> the maximum amount of nodes a job in the queue may request</p>
<dt>&#8211;</p>
<dd> the number of jobs in the queue in the running state</p>
<dt>&#8211;</p>
<dd> the number of jobs in the queue in the queued state</p>
<dt>&#8211;</p>
<dd> the maximum number (limit) of jobs that may be run in the queue concurrently</p>
<dt>&#8211;</p>
<dd> the state of the queue given by a pair of letters:<br />
 &#8211; either the letter E if the queue is Enabled or D if Disabled, and<br />
 &#8211; either the letter R if the queue is Running (started) or S if Stopped.</dl>
</dl>
<p> Displaying Server Status </p>
<p> If batch server status is being displayed and the </code><i> option is not specified, the following items are displayed on a single line, in the specified order, separated by white space:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> the server name</p>
<dt>&#8211;</p>
<dd> the maximum number of jobs that the server may run concurrently</p>
<dt>&#8211;</p>
<dd> the total number of jobs currently managed by the server</p>
<dt>&#8211;</p>
<dd> the status of the server</p>
<dt>&#8211;</p>
<dd> for each job state, the name of the state and the number of jobs in the server in that state</dl>
</dl>
<p> If server status is being displayed and the option is specified, the output will depend on whether </i><code>qstat</code> was compiled to use a <code>Tcl</code> interpreter. See the configuration section for details. If <code>Tcl</code> is not being used, the full display for the server consist of the header line:<br />
 <code> server name<br />
 Followed by one line per server attribute of the form: </p>
<p> </code></p>
<h2>STANDARD ERROR</h2>
<p> The qstat command will write a diagnostic message to standard error for each error occurrence.</p>
<h2>CONFIGURATION</h2>
<p> If <code>qstat</code> is compiled with an option to include a <code>Tcl</code> interpreter, using the <i> flag to get a full display causes a check to be made for a script file to use to output the requested information. The first location checked is $HOME/.qstatrc. If this does not exist, the next location checked is administrator configured. If one of these is found, a </i><code>Tcl</code> interpreter is started and the script file is passed to it along with three global variables. The command line arguments are split into two variable named <code>flags</code> and <code>operands .</code> The status information is passed in a variable named <code>objects .</code> All of these variables are <code>Tcl</code> lists. The <code>flags</code> list contains the name of the command (usually &quot;qstat&quot;) as its first element. Any other elements are command line option flags with any options they use, presented in the order given on the command line. They are broken up individually so that if two flags are given together on the command line, they are separated in the list. For example, if the user typed </p>
<p> <code> </p>
<p> the flags</code> list would contain </p>
<p> <code> </p>
<p> The operands</code> list contains all other command line arguments following the flags. There will always be at least one element in <code>operands</code> because if no operands are typed by the user, the default destination or server name is used. The <code>objects</code> list contains all the information retrieved from the server(s) so the Tcl interpreter can run once to format the entire output. This list has the same number of elements as the <code>operands</code> list. Each element is another list with two elements. The first element is a string giving the type of objects to be found in the second. The string can take the values &quot;server&quot;, &quot;queue&quot;, &quot;job&quot; or &quot;error&quot;. The second element will be a list in which each element is a single batch status object of the type given by the string discussed above. In the case of &quot;error&quot;, the list will be empty. Each object is again a list. The first element is the name of the object. The second is a list of attributes. The third element will be the object text. All three of these object elements correspond with fields in the structure <code> which is described in detail for each type of object by the man pages for <a href="/docs/linux/man/3-pbs_statjob/">pbs_statjob</a>(3), <a href="/docs/linux/man/3-pbs_statque/">pbs_statque</a>(3), and <a href="/docs/linux/man/3-pbs_statserver/">pbs_statserver</a>(3).</code> Each attribute in the second element list whose elements correspond with the <code> structure. Each will be a list with two elements. The first will be the attribute name and the second will be the attribute value. </code></p>
<h2>EXIT STATUS</h2>
<p> Upon successful processing of all the operands presented to the qstat command, the exit status will be a value of zero. </p>
<p> If the qstat command fails to process any operand, the command exits with a value greater than zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1B-qalter/">qalter</a>(1B), <a href="//www.systutorials.com/docs/linux/man/1B-qsub/">qsub</a>(1B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_alterjob/">pbs_alterjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_statjob/">pbs_statjob</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_statque/">pbs_statque</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_statserver/">pbs_statserver</a>(3B), <a href="//www.systutorials.com/docs/linux/man/3B-pbs_submit/">pbs_submit</a>(3B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_job_attributes/">pbs_job_attributes</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_queue_attributes/">pbs_queue_attributes</a>(7B), <a href="//www.systutorials.com/docs/linux/man/7B-pbs_server_attributes/">pbs_server_attributes</a>(7B), pbs_resources_*(7B) where * is system type, and the PBS ERS. </p>
<h2>Index</h2>
