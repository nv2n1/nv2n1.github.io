---
title: "condor_submit(1)"
name: "condor_submit"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_submit/"
description: "condor_submit Queue jobs for execution under HTCondor"
---

<h2>Name</h2>
<p> <i>condor_submit</i> Queue jobs for execution under HTCondor </p>
<h2>Synopsis</h2>
<p> <i>condor_submit</i> [ <code>-verbose</code> ] [ <code>-unused</code> ] [ <code>-name </code> <i>schedd_name</i> ] [ <code>-remote </code> <i>schedd_name</i> ] [ <code>-addr </code> <i>&lt;ip:port&gt;</i> ] [ <code>-pool </code> <i>pool_name</i> ] [ <code>-disable</code> ] [ <code>-password </code> <i>passphrase</i> ] [ <code>-debug</code> ] [ <code>-append</code> <i>command</i> <code>&#8230; </code> ] [ <code>-spool</code> ] [ <code>-dump </code> <i>filename</i> ] [ <code>-interactive</code> ] [ <code>-dry-run</code> ] [ <code>-maxjobs </code> <i>&lt;number-of-jobs&gt;</i> ] [ <code>-single-cluster</code> ] [ <code>&lt;submit-variable&gt;=&lt;value&gt;</code> ] [ <i>submit description file</i> ] [ <code>-queue </code> <i>queue_arguments</i> ] </p>
<h2>Description</h2>
<p> <i>condor_submit</i> is the program for submitting jobs for execution under HTCondor. <i>condor_submit</i> requires a submit description file which contains commands to direct the queuing of jobs. One submit description file may contain specifications for the queuing of many HTCondor jobs at once. A single invocation of <i>condor_submit</i> may cause one or more clusters. A cluster is a set of jobs specified in the submit description file between <code>queue</code> commands for which the executable is not changed. It is advantageous to submit multiple jobs as a single cluster because:</p>
<dl>
<dt>
<dd> * Only one copy of the checkpoint file is needed to represent all jobs in a cluster until they begin execution.</p>
<dt>
<dd> * There is much less overhead involved for HTCondor to start the next job in a cluster than for HTCondor to start a new cluster. This can make a big difference when submitting lots of short jobs.</dl>
<p> Multiple clusters may be specified within a single submit description file. Each cluster must specify a single executable. </p>
<p> The job ClassAd attribute ClusterId identifies a cluster. </p>
<p> The <i>submit description file</i> argument is the path and file name of the submit description file. If this optional argument is missing or is the dash character ( &#8211; ), then the commands are taken from standard input. </p>
<p> Note that submission of jobs from a Windows machine requires a stashed password to allow HTCondor to impersonate the user submitting the job. To stash a password, use the <i>condor_store_cred</i> command. See the manual page for details. </p>
<p> For lengthy lines within the submit description file, the backslash () is a line continuation character. Placing the backslash at the end of a line causes the current line&#8217;s command to be continued with the next line of the file. Submit description files may contain comments. A comment is any line beginning with a pound character ( # ). </p>
<h2>Options</h2>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> Verbose output &#8211; display the created job ClassAd</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-unused</code></p>
<dl>
<dt>
<dd> As a default, causes no warnings to be issued about user-defined macros not being used within the submit description file. The meaning reverses (toggles) when the configuration variable WARN_ON_UNUSED_SUBMIT_FILE_MACROS is set to the non default value of False . Printing the warnings can help identify spelling errors of submit description file commands. The warnings are sent to stderr.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-name </code> <i>schedd_name</i></p>
<dl>
<dt>
<dd> Submit to the specified <i>condor_schedd</i> . Use this option to submit to a <i>condor_schedd</i> other than the default local one. <i>schedd_name</i> is the value of the Name ClassAd attribute on the machine where the <i>condor_schedd</i> daemon runs.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-remote </code> <i>schedd_name</i></p>
<dl>
<dt>
<dd> Submit to the specified <i>condor_schedd</i> , spooling all required input files over the network connection. <i>schedd_name</i> is the value of the Name ClassAd attribute on the machine where the <i>condor_schedd</i> daemon runs. This option is equivalent to using both <code>-name</code> and <code>-spool</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-addr </code> <i>&lt;ip:port&gt;</i></p>
<dl>
<dt>
<dd> Submit to the <i>condor_schedd</i> at the IP address and port given by the <i>sinful string</i> argument <i>&lt;ip:port&gt;</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-pool </code> <i>pool_name</i></p>
<dl>
<dt>
<dd> Look in the specified pool for the <i>condor_schedd</i> to submit to. This option is used with <code>-name</code> or <code>-remote</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-disable</code></p>
<dl>
<dt>
<dd> Disable file permission checks when submitting a job for read permissions on all input files, such as those defined by commands <code>input</code> and <code>transfer_input_files</code> , as well as write permission to output files, such as a log file defined by <code>log</code> and output files defined with <code>output</code> or <code>transfer_output_files</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-password </code> <i>passphrase</i></p>
<dl>
<dt>
<dd> Specify a password to the <i>MyProxy</i> server.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-debug</code></p>
<dl>
<dt>
<dd> Cause debugging information to be sent to stderr , based on the value of the configuration variable TOOL_DEBUG .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-append </code> <i>command</i></p>
<dl>
<dt>
<dd> Augment the commands in the submit description file with the given <i>command</i> . This command will be considered to immediately precede the <code>queue</code> command within the submit description file, and come after all other previous commands. If the <i>command</i> specifies a <code>queue</code> command, as in the example</p>
<dt>
<dd>
&nbsp;<wbr>condor_submit mysubmitfile -append&nbsp;<wbr>&quot;queue input in A, B, C&quot;&nbsp;<wbr></p>
<dt>
<dd> then the entire <code>-append</code> command line option and its arguments are converted to</p>
<dt>
<dd>
&nbsp;<wbr>condor_submit mysubmitfile -queue input in A, B, C&nbsp;<wbr></p>
<dt>
<dd> The submit description file is not modified. Multiple commands are specified by using the <code>-append</code> option multiple times. Each new command is given in a separate <code>-append</code> option. Commands with spaces in them will need to be enclosed in double quote marks.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-spool</code></p>
<dl>
<dt>
<dd> Spool all required input files, job event log, and proxy over the connection to the <i>condor_schedd</i> . After submission, modify local copies of the files without affecting your jobs. Any output files for completed jobs need to be retrieved with <i>condor_transfer_data</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-dump </code> <i>filename</i></p>
<dl>
<dt>
<dd> Sends all ClassAds to the specified file, instead of to the <i>condor_schedd</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-interactive</code></p>
<dl>
<dt>
<dd> Indicates that the user wants to run an interactive shell on an execute machine in the pool. This is equivalent to creating a submit description file of a vanilla universe sleep job, and then running <i>condor_ssh_to_job</i> by hand. Without any additional arguments, <i>condor_submit</i> with the -interactive flag creates a dummy vanilla universe job that sleeps, submits it to the local scheduler, waits for the job to run, and then launches <i>condor_ssh_to_job</i> to run a shell. If the user would like to run the shell on a machine that matches a particular <code>requirements</code> expression, the submit description file is specified, and it will contain the expression. Note that all policy expressions specified in the submit description file are honored, but any <code>executable</code> or <code>universe</code> commands are overwritten to be sleep and vanilla. The job ClassAd attribute InteractiveJob is set to True to identify interactive jobs for <i>condor_startd</i> policy usage.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-dry-run</code></p>
<dl>
<dt>
<dd> Parse the submit description file, sending the job ClassAd to stderr , but do not submit the job(s). This permits an observation of job specification, and it facilitates debugging the submit description file contents.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-maxjobs </code> <i>&lt;number-of-jobs&gt;</i></p>
<dl>
<dt>
<dd> If the total number of jobs specified by the submit description file is more than the integer value given by <code>&lt;number-of-jobs&gt;</code> , then no jobs are submitted for execution and an error message is generated. A 0 or negative value for the <code>&lt;number-of-jobs&gt;</code> causes no limit to be imposed.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-single-cluster</code></p>
<dl>
<dt>
<dd> If the jobs specified by the submit description file causes more than a single cluster value to be assigned, then no jobs are submitted for execution and an error message is generated.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&lt;submit-variable&gt;=&lt;value&gt;</code></p>
<dl>
<dt>
<dd> Defines a submit command or submit variable with a value, and parses it as if it was placed at the beginning of the submit description file. The submit description file is not changed. To correctly parse the <i>condor_submit</i> command line, this option must be specified without white space characters before and after the equals sign ( = ), or the entire option must be surrounded by double quote marks.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>-queue </code> <i>queue_arguments</i></p>
<dl>
<dt>
<dd> A command line specification of how many jobs to queue, which is only permitted if the submit description file does not have a <code>queue</code> command. The <i>queue_arguments</i> are the same as may be within a submit description file. The parsing of the <i>queue_arguments</i> finishes at the end of the line or when a dash character ( &#8211; ) is encountered. Therefore, its best placement within the command line will be at the end of the command line.</p>
<dt>
<dd> On a Unix command line, the shell expands file globs before parsing occurs.</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>Submit Description File Commands</h2>
<p> Each submit description file describes one cluster of jobs to be placed in the HTCondor execution pool. All jobs in a cluster must share the same executable, but they may have different input and output files, and different program arguments. The submit description file is the only command-line argument to <i>condor_submit</i> . If the submit description file argument is omitted, <i>condor_submit</i> will read the submit description from standard input. </p>
<p> The submit description file must contain one <i>executable</i> command and at least one <i>queue</i> command. All of the other commands have default actions. </p>
<p> The commands which can appear in the submit description file are numerous. They are listed here in alphabetical order by category. </p>
<p> <i>BASIC COMMANDS</i></p>
<dl>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>arguments = &lt;argument_list&gt;</code></p>
<dl>
<dt>
<dd> List of arguments to be supplied to the executable as part of the command line.</p>
<dt>
<dd> In the <code>java</code> universe, the first argument must be the name of the class containing main .</p>
<dt>
<dd> There are two permissible formats for specifying arguments, identified as the old syntax and the new syntax. The old syntax supports white space characters within arguments only in special circumstances; when used, the command line arguments are represented in the job ClassAd attribute Args . The new syntax supports uniform quoting of white space characters within arguments; when used, the command line arguments are represented in the job ClassAd attribute Arguments .</p>
<dt>
<dd> <code>Old Syntax</code></p>
<dt>
<dd> In the old syntax, individual command line arguments are delimited (separated) by space characters. To allow a double quote mark in an argument, it is escaped with a backslash; that is, the two character sequence \&quot; becomes a single double quote mark within an argument.</p>
<dt>
<dd> Further interpretation of the argument string differs depending on the operating system. On Windows, the entire argument string is passed verbatim (other than the backslash in front of double quote marks) to the Windows application. Most Windows applications will allow spaces within an argument value by surrounding the argument with double quotes marks. In all other cases, there is no further interpretation of the arguments.</p>
<dt>
<dd> Example:</p>
<dt>
<dd></dl>
<p> arguments = one \&quot;two\&quot; &#8216;three&#8217;</p>
<dl>
<dt>
<dd> Produces in Unix vanilla universe:</p>
<dt>
<dd></dl>
<p> argument 1: one<br />
 argument 2: &quot;two&quot;<br />
 argument 3: &#8216;three&#8217;</p>
<dl>
<dt>
<dd> <code>New Syntax</code></p>
<dt>
<dd> Here are the rules for using the new syntax:</p>
<dt>
<dd>
<dt>
<dd> 1. The entire string representing the command line arguments is surrounded by double quote marks. This permits the white space characters of spaces and tabs to potentially be embedded within a single argument. Putting the double quote mark within the arguments is accomplished by escaping it with another double quote mark.</p>
<dt>
<dd>
<dt>
<dd> 2. The white space characters of spaces or tabs delimit arguments.</p>
<dt>
<dd>
<dt>
<dd> 3. To embed white space characters of spaces or tabs within a single argument, surround the entire argument with single quote marks.</p>
<dt>
<dd>
<dt>
<dd> 4. To insert a literal single quote mark, escape it within an argument already delimited by single quote marks by adding another single quote mark.</p>
<dt>
<dd>
<dt>
<dd> Example:</dl>
<p> arguments = &quot;3 simple arguments&quot;</p>
<dl>
<dt>
<dd> Produces:</dl>
<p> argument 1: 3<br />
 argument 2: simple<br />
 argument 3: arguments</p>
<dl>
<dt>
<dd> Another example:</dl>
<p> arguments = &quot;one &#8216;two with spaces&#8217; 3&quot;</p>
<dl>
<dt>
<dd> Produces:</dl>
<p> argument 1: one<br />
 argument 2: two with spaces<br />
 argument 3: 3</p>
<dl>
<dt>
<dd> And yet another example:</dl>
<p> arguments = &quot;one &quot;&quot;two&quot;&quot; &#8216;spacey &#8221;quoted&#8221; argument&#8217;&quot;</p>
<dl>
<dt>
<dd> Produces:</dl>
<p> argument 1: one<br />
 argument 2: &quot;two&quot;<br />
 argument 3: spacey &#8216;quoted&#8217; argument</p>
<dl>
<dt>
<dd> Notice that in the new syntax, the backslash has no special meaning. This is for the convenience of Windows users.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>environment = &lt;parameter_list&gt;</code></p>
<dl>
<dt>
<dd> List of environment variables.</p>
<dt>
<dd> There are two different formats for specifying the environment variables: the old format and the new format. The old format is retained for backward-compatibility. It suffers from a platform-dependent syntax and the inability to insert some special characters into the environment.</p>
<dt>
<dd> The new syntax for specifying environment values:</p>
<dt>
<dd>
<dt>
<dd> 1. Put double quote marks around the entire argument string. This distinguishes the new syntax from the old. The old syntax does not have double quote marks around it. Any literal double quote marks within the string must be escaped by repeating the double quote mark.</p>
<dt>
<dd>
<dt>
<dd> 2. Each environment entry has the form</p>
<dt>
<dd></dl>
<p> &lt;name&gt;=&lt;value&gt;</p>
<dl>
<dt>
<dd>
<dt>
<dd> 3. Use white space (space or tab characters) to separate environment entries.</p>
<dt>
<dd>
<dt>
<dd> 4. To put any white space in an environment entry, surround the space and as much of the surrounding entry as desired with single quote marks.</p>
<dt>
<dd>
<dt>
<dd> 5. To insert a literal single quote mark, repeat the single quote mark anywhere inside of a section surrounded by single quote marks.</p>
<dt>
<dd>
<dt>
<dd> Example:</p>
<dt>
<dd></dl>
<p> environment = &quot;one=1 two=&quot;&quot;2&quot;&quot; three=&#8217;spacey &#8221;quoted&#8221; value&#8217;&quot;</p>
<dl>
<dt>
<dd> Produces the following environment entries:</p>
<dt>
<dd></dl>
<p> one=1<br />
 two=&quot;2&quot;<br />
 three=spacey &#8216;quoted&#8217; value</p>
<dl>
<dt>
<dd> Under the old syntax, there are no double quote marks surrounding the environment specification. Each environment entry remains of the form</dl>
<p> &lt;name&gt;=&lt;value&gt;</p>
<dl>
<dt>
<dd> Under Unix, list multiple environment entries by separating them with a semicolon (;). Under Windows, separate multiple entries with a vertical bar (| ). There is no way to insert a literal semicolon under Unix or a literal vertical bar under Windows. Note that spaces are accepted, but rarely desired, characters within parameter names and values, because they are treated as literal characters, not separators or ignored white space. Place spaces within the parameter list only if required.</p>
<dt>
<dd> A Unix example:</p>
<dt>
<dd></dl>
<p> environment = one=1;two=2;three=&quot;quotes have no &#8216;special&#8217; meaning&quot;</p>
<dl>
<dt>
<dd> This produces the following:</p>
<dt>
<dd></dl>
<p> one=1<br />
 two=2<br />
 three=&quot;quotes have no &#8216;special&#8217; meaning&quot;</p>
<dl>
<dt>
<dd> If the environment is set with the <code>environment</code> command <i>and</i> <code>getenv</code> is also set to true, values specified with <code>environment</code> override values in the submitter&#8217;s environment (regardless of the order of the <code>environment</code> and <code>getenv</code> commands).</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>error = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> A path and file name used by HTCondor to capture any error messages the program would normally write to the screen (that is, this file becomes stderr ). A path is given with respect to the file system of the machine on which the job is submitted. The file is written (by the job) in the remote scratch directory of the machine where the job is executed. When the job exits, the resulting file is transferred back to the machine where the job was submitted, and the path is utilized for file placement. If not specified, the default value of /dev/null is used for submission to a Unix machine. If not specified, error messages are ignored for submission to a Windows machine. More than one job should not use the same error file, since this will cause one job to overwrite the errors of another. The error file and the output file should not be the same file as the outputs will overwrite each other or be lost. For grid universe jobs, <code>error</code> may be a URL that the Globus tool <i>globus_url_copy</i> understands.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>executable = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> An optional path and a required file name of the executable file for this job cluster. Only one <code>executable</code> command within a submit description file is guaranteed to work properly. More than one often works.</p>
<dt>
<dd> If no path or a relative path is used, then the executable file is presumed to be relative to the current working directory of the user as the <i>condor_submit</i> command is issued.</p>
<dt>
<dd> If submitting into the standard universe, then the named executable must have been re-linked with the HTCondor libraries (such as via the <i>condor_compile</i> command). If submitting into the vanilla universe (the default), then the named executable need not be re-linked and can be any process which can run in the background (shell scripts work fine as well). If submitting into the Java universe, then the argument must be a compiled .class file.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>getenv = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> If <code>getenv</code> is set to True , then <i>condor_submit</i> will copy all of the user&#8217;s current shell environment variables at the time of job submission into the job ClassAd. The job will therefore execute with the same set of environment variables that the user had at submit time. Defaults to False .</p>
<dt>
<dd> If the environment is set with the <code>environment</code> command <i>and</i> <code>getenv</code> is also set to true, values specified with <code>environment</code> override values in the submitter&#8217;s environment (regardless of the order of the <code>environment</code> and <code>getenv</code> commands).</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>input = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> HTCondor assumes that its jobs are long-running, and that the user will not wait at the terminal for their completion. Because of this, the standard files which normally access the terminal, ( stdin , stdout , and stderr ), must refer to files. Thus, the file name specified with <code>input</code> should contain any keyboard input the program requires (that is, this file becomes stdin ). A path is given with respect to the file system of the machine on which the job is submitted. The file is transferred before execution to the remote scratch directory of the machine where the job is executed. If not specified, the default value of /dev/null is used for submission to a Unix machine. If not specified, input is ignored for submission to a Windows machine. For grid universe jobs, <code>input</code> may be a URL that the Globus tool <i>globus_url_copy</i> understands.</p>
<dt>
<dd> Note that this command does <i>not</i> refer to the command-line arguments of the program. The command-line arguments are specified by the <code>arguments</code> command.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>log = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> Use <code>log</code> to specify a file name where HTCondor will write a log file of what is happening with this job cluster, called a job event log. For example, HTCondor will place a log entry into this file when and where the job begins running, when the job produces a checkpoint, or moves (migrates) to another machine, and when the job completes. Most users find specifying a <code>log</code> file to be handy; its use is recommended. If no <code>log</code> entry is specified, HTCondor does not create a log for this cluster. If a relative path is specified, it is relative to the current working directory as the job is submitted or the directory specified by submit command <code>initialdir</code> on the submit machine.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>log_xml = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> If <code>log_xml</code> is True , then the job event log file will be written in ClassAd XML. If not specified, XML is not used. Note that the file is an XML fragment; it is missing the file header and footer. Do not mix XML and non-XML within a single file. If multiple jobs write to a single job event log file, ensure that all of the jobs specify this option in the same way.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>notification = &lt;Always | Complete | Error | Never&gt;</code></p>
<dl>
<dt>
<dd> Owners of HTCondor jobs are notified by e-mail when certain events occur. If defined by <i>Always</i> , the owner will be notified whenever the job produces a checkpoint, as well as when the job completes. If defined by <i>Complete</i> , the owner will be notified when the job terminates. If defined by <i>Error</i> , the owner will only be notified if the job terminates abnormally, or if the job is placed on hold because of a failure, and not by user request. If defined by <i>Never</i> (the default), the owner will not receive e-mail, regardless to what happens to the job. The HTCondor User&#8217;s manual documents statistics included in the e-mail.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>notify_user = &lt;email-address&gt;</code></p>
<dl>
<dt>
<dd> Used to specify the e-mail address to use when HTCondor sends e-mail about a job. If not specified, HTCondor defaults to using the e-mail address defined by</dl>
<p> job-owner [at] UID_DOMAIN</p>
<dl>
<dt>
<dd> where the configuration variable UID_DOMAIN is specified by the HTCondor site administrator. If UID_DOMAIN has not been specified, HTCondor sends the e-mail to:</dl>
<p> job-owner [at] submit-machine-name</p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>output = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> The <code>output</code> file captures any information the program would ordinarily write to the screen (that is, this file becomes stdout ). A path is given with respect to the file system of the machine on which the job is submitted. The file is written (by the job) in the remote scratch directory of the machine where the job is executed. When the job exits, the resulting file is transferred back to the machine where the job was submitted, and the path is utilized for file placement. If not specified, the default value of /dev/null is used for submission to a Unix machine. If not specified, output is ignored for submission to a Windows machine. Multiple jobs should not use the same output file, since this will cause one job to overwrite the output of another. The output file and the error file should not be the same file as the outputs will overwrite each other or be lost. For grid universe jobs, <code>output</code> may be a URL that the Globus tool <i>globus_url_copy</i> understands.</p>
<dt>
<dd> Note that if a program explicitly opens and writes to a file, that file should <i>not</i> be specified as the <code>output</code> file.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>priority = &lt;integer&gt;</code></p>
<dl>
<dt>
<dd> An HTCondor job priority can be any integer, with 0 being the default. Jobs with higher numerical priority will run before jobs with lower numerical priority. Note that this priority is on a per user basis. One user with many jobs may use this command to order his/her own jobs, and this will have no effect on whether or not these jobs will run ahead of another user&#8217;s jobs.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>queue [</code> <code>number-of-procs</code> ]</p>
<dl>
<dt>
<dd> Places one or more copies of the job into the HTCondor queue. The optional argument <i>number-of-procs</i> specifies how many times to submit the job to the queue, and it defaults to 1. If desired, any commands may be placed between subsequent <code>queue</code> commands, such as new <code>input</code> , <code>output</code> , <code>error</code> , <code>initialdir</code> , or <code>arguments</code> commands. This is handy when submitting multiple runs into one cluster with one submit description file.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>universe = &lt;vanilla | standard | scheduler | local | grid | java | vm | docker&gt;</code></p>
<dl>
<dt>
<dd> Specifies which HTCondor universe to use when running this job. The HTCondor universe specifies an HTCondor execution environment.</p>
<dt>
<dd> The <code>vanilla</code> universe is the default (except where the configuration variable DEFAULT_UNIVERSE defines it otherwise), and is an execution environment for jobs which do not use HTCondor&#8217;s mechanisms for taking checkpoints; these are ones that have not been linked with the HTCondor libraries. Use the <code>vanilla</code> universe to submit shell scripts to HTCondor.</p>
<dt>
<dd> The <code>standard</code> universe tells HTCondor that this job has been re-linked via <i>condor_compile</i> with the HTCondor libraries and therefore supports taking checkpoints and remote system calls.</p>
<dt>
<dd> The <code>scheduler</code> universe is for a job that is to run on the machine where the job is submitted. This universe is intended for a job that acts as a metascheduler and will not be preempted.</p>
<dt>
<dd> The <code>local</code> universe is for a job that is to run on the machine where the job is submitted. This universe runs the job immediately and will not be preempt the job.</p>
<dt>
<dd> The <code>grid</code> universe forwards the job to an external job management system. Further specification of the <code>grid</code> universe is done with the <code>grid_resource</code> command.</p>
<dt>
<dd> The <code>java</code> universe is for programs written to the Java Virtual Machine.</p>
<dt>
<dd> The <code>vm</code> universe facilitates the execution of a virtual machine.</p>
<dt>
<dd> The <code>docker</code> universe runs a docker container as an HTCondor job.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <i>COMMANDS FOR MATCHMAKING</i></p>
<dl>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>rank = &lt;ClassAd Float Expression&gt;</code></p>
<dl>
<dt>
<dd> A ClassAd Floating-Point expression that states how to rank machines which have already met the requirements expression. Essentially, rank expresses preference. A higher numeric value equals better rank. HTCondor will give the job the machine with the highest rank. For example,</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>requirements&nbsp;<wbr>=&nbsp;<wbr>Memory&nbsp;<wbr>&gt;&nbsp;<wbr>60 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>rank&nbsp;<wbr>=&nbsp;<wbr>Memory</p>
<dl>
<dt>
<dd> asks HTCondor to find all available machines with more than 60 megabytes of memory and give to the job the machine with the most amount of memory. The HTCondor User&#8217;s Manual contains complete information on the syntax and available attributes that can be used in the ClassAd expression.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>request_cpus = &lt;num-cpus&gt;</code></p>
<dl>
<dt>
<dd> A requested number of CPUs (cores). If not specified, the number requested will be 1. If specified, the expression</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>(RequestCpus&nbsp;<wbr>&lt;=&nbsp;<wbr>Target.Cpus)</p>
<dl>
<dt>
<dd> is appended to the <code>requirements</code> expression for the job.</p>
<dt>
<dd> For pools that enable dynamic <i>condor_startd</i> provisioning, specifies the minimum number of CPUs requested for this job, resulting in a dynamic slot being created with this many cores.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>request_disk = &lt;quantity&gt;</code></p>
<dl>
<dt>
<dd> The requested amount of disk space in KiB requested for this job. If not specified, it will be set to the job ClassAd attribute DiskUsage . The expression</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>(RequestDisk&nbsp;<wbr>&lt;=&nbsp;<wbr>Target.Disk)</p>
<dl>
<dt>
<dd> is appended to the <code>requirements</code> expression for the job.</p>
<dt>
<dd> For pools that enable dynamic <i>condor_startd</i> provisioning, a dynamic slot will be created with at least this much disk space.</p>
<dt>
<dd> Characters may be appended to a numerical value to indicate units. K or KB indicates KiB, numbers of bytes. M or MB indicates MiB, numbers of bytes. G or GB indicates GiB, numbers of bytes. T or TB indicates TiB, numbers of bytes.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>request_memory = &lt;quantity&gt;</code></p>
<dl>
<dt>
<dd> The required amount of memory in MiB that this job needs to avoid excessive swapping. If not specified and the submit command <code>vm_memory</code> is specified, then the value specified for <code>vm_memory</code> defines <code>request_memory</code> . If neither <code>request_memory</code> nor <code>vm_memory</code> is specified, the value is set by the configuration variable JOB_DEFAULT_REQUESTMEMORY . The actual amount of memory used by a job is represented by the job ClassAd attribute MemoryUsage .</p>
<dt>
<dd> For pools that enable dynamic <i>condor_startd</i> provisioning, a dynamic slot will be created with at least this much RAM.</p>
<dt>
<dd> The expression</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>(RequestMemory&nbsp;<wbr>&lt;=&nbsp;<wbr>Target.Memory)</p>
<dl>
<dt>
<dd> is appended to the <code>requirements</code> expression for the job.</p>
<dt>
<dd> Characters may be appended to a numerical value to indicate units. K or KB indicates KiB, numbers of bytes. M or MB indicates MiB, numbers of bytes. G or GB indicates GiB, numbers of bytes. T or TB indicates TiB, numbers of bytes.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>request_&lt;name&gt; = &lt;quantity&gt;</code></p>
<dl>
<dt>
<dd> The required amount of the custom machine resource identified by &lt;name&gt; that this job needs. The custom machine resource is defined in the machine&#8217;s configuration. Machines that have available GPUs will define &lt;name&gt; to be GPUs .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>requirements = &lt;ClassAd Boolean Expression&gt;</code></p>
<dl>
<dt>
<dd> The requirements command is a boolean ClassAd expression which uses C-like operators. In order for any job in this cluster to run on a given machine, this requirements expression must evaluate to true on the given machine.</p>
<dt>
<dd> For scheduler and local universe jobs, the requirements expression is evaluated against the Scheduler ClassAd which represents the the <i>condor_schedd</i> daemon running on the submit machine, rather than a remote machine. Like all commands in the submit description file, if multiple requirements commands are present, all but the last one are ignored. By default, <i>condor_submit</i> appends the following clauses to the requirements expression:</p>
<dt>
<dd> 1. Arch and OpSys are set equal to the Arch and OpSys of the submit machine. In other words: unless you request otherwise, HTCondor will give your job machines with the same architecture and operating system version as the machine running <i>condor_submit</i> .</p>
<dt>
<dd> 2. Cpus &gt;=RequestCpus, if the job ClassAd attribute RequestCpus is defined.</p>
<dt>
<dd> 3. Disk &gt;=RequestDisk, if the job ClassAd attribute RequestDisk is defined. Otherwise, Disk &gt;=DiskUsage is appended to the requirements. The DiskUsage attribute is initialized to the size of the executable plus the size of any files specified in a <code>transfer_input_files</code> command. It exists to ensure there is enough disk space on the target machine for HTCondor to copy over both the executable and needed input files. The DiskUsage attribute represents the maximum amount of total disk space required by the job in kilobytes. HTCondor automatically updates the DiskUsage attribute approximately every 20 minutes while the job runs with the amount of space being used by the job on the execute machine.</p>
<dt>
<dd> 4. Memory &gt;=RequestMemory, if the job ClassAd attribute RequestMemory is defined.</p>
<dt>
<dd> 5. If Universe is set to Vanilla, FileSystemDomain is set equal to the submit machine&#8217;s FileSystemDomain. View the requirements of a job which has already been submitted (along with everything else about the job ClassAd) with the command <i>condor_q -l</i> ; see the command reference for <i>condor_q</i> on page . Also, see the HTCondor Users Manual for complete information on the syntax and available attributes that can be used in the ClassAd expression.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <i>FILE TRANSFER COMMANDS</i></p>
<dl>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>dont_encrypt_input_files = &lt;file1,file2,file&#8230; &gt;</code></p>
<dl>
<dt>
<dd> A comma and/or space separated list of input files that are <i>not</i> to be network encrypted when transferred with the file transfer mechanism. Specification of files in this manner overrides configuration that would use encryption. Each input file must also be in the list given by <code>transfer_input_files</code> . When a path to an input file or directory is specified, this specifies the path to the file on the submit side. A single wild card character ( * ) may be used in each file name.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>dont_encrypt_output_files = &lt;file1,file2,file&#8230; &gt;</code></p>
<dl>
<dt>
<dd> A comma and/or space separated list of output files that are <i>not</i> to be network encrypted when transferred back with the file transfer mechanism. Specification of files in this manner overrides configuration that would use encryption. The output file(s) must also either be in the list given by <code>transfer_output_files</code> or be discovered and to be transferred back with the file transfer mechanism. When a path to an output file or directory is specified, this specifies the path to the file on the execute side. A single wild card character ( * ) may be used in each file name.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>encrypt_execute_directory = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> Defaults to False . If set to True , HTCondor will encrypt the contents of the remote scratch directory of the machine where the job is executed. This encryption is transparent to the job itself, but ensures that files left behind on the local disk of the execute machine, perhaps due to a system crash, will remain private. In addition, <i>condor_submit</i> will append to the job&#8217;s <code>requirements</code> expression</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>(TARGET.HasEncryptExecuteDirectory)</p>
<dl>
<dt>
<dd> to ensure the job is matched to a machine that is capable of encrypting the contents of the execute directory. This support is limited to Windows platforms that use the NTFS file system and Linux platforms with the <i>ecryptfs-utils</i> package installed.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>encrypt_input_files = &lt;file1,file2,file&#8230; &gt;</code></p>
<dl>
<dt>
<dd> A comma and/or space separated list of input files that are to be network encrypted when transferred with the file transfer mechanism. Specification of files in this manner overrides configuration that would <i>not</i> use encryption. Each input file must also be in the list given by <code>transfer_input_files</code> . When a path to an input file or directory is specified, this specifies the path to the file on the submit side. A single wild card character ( * ) may be used in each file name. The method of encryption utilized will be as agreed upon in security negotiation; if that negotiation failed, then the file transfer mechanism must also fail for files to be network encrypted.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>encrypt_output_files = &lt;file1,file2,file&#8230; &gt;</code></p>
<dl>
<dt>
<dd> A comma and/or space separated list of output files that are to be network encrypted when transferred back with the file transfer mechanism. Specification of files in this manner overrides configuration that would <i>not</i> use encryption. The output file(s) must also either be in the list given by <code>transfer_output_files</code> or be discovered and to be transferred back with the file transfer mechanism. When a path to an output file or directory is specified, this specifies the path to the file on the execute side. A single wild card character ( * ) may be used in each file name. The method of encryption utilized will be as agreed upon in security negotiation; if that negotiation failed, then the file transfer mechanism must also fail for files to be network encrypted.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>max_transfer_input_mb = &lt;ClassAd Integer Expression&gt;</code></p>
<dl>
<dt>
<dd> This integer expression specifies the maximum allowed total size in MiB of the input files that are transferred for a job. This expression does <i>not</i> apply to grid universe, standard universe, or files transferred via file transfer plug-ins. The expression may refer to attributes of the job. The special value -1 indicates no limit. If not defined, the value set by configuration variable MAX_TRANSFER_INPUT_MB is used. If the observed size of all input files at submit time is larger than the limit, the job will be immediately placed on hold with a HoldReasonCode value of 32. If the job passes this initial test, but the size of the input files increases or the limit decreases so that the limit is violated, the job will be placed on hold at the time when the file transfer is attempted.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>max_transfer_output_mb = &lt;ClassAd Integer Expression&gt;</code></p>
<dl>
<dt>
<dd> This integer expression specifies the maximum allowed total size in MiB of the output files that are transferred for a job. This expression does <i>not</i> apply to grid universe, standard universe, or files transferred via file transfer plug-ins. The expression may refer to attributes of the job. The special value -1 indicates no limit. If not set, the value set by configuration variable MAX_TRANSFER_OUTPUT_MB is used. If the total size of the job&#8217;s output files to be transferred is larger than the limit, the job will be placed on hold with a HoldReasonCode value of 33. The output will be transferred up to the point when the limit is hit, so some files may be fully transferred, some partially, and some not at all.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>output_destination = &lt;destination-URL&gt;</code></p>
<dl>
<dt>
<dd> When present, defines a URL that specifies both a plug-in and a destination for the transfer of the entire output sandbox or a subset of output files as specified by the submit command <code>transfer_output_files</code> . The plug-in does the transfer of files, and no files are sent back to the submit machine. The HTCondor Administrator&#8217;s manual has full details.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>should_transfer_files = &lt;YES | NO | IF_NEEDED &gt;</code></p>
<dl>
<dt>
<dd> The <code>should_transfer_files</code> setting is used to define if HTCondor should transfer files to and from the remote machine where the job runs. The file transfer mechanism is used to run jobs which are not in the standard universe (and can therefore use remote system calls for file access) on machines which do not have a shared file system with the submit machine. <code>should_transfer_files</code> equal to <i>YES</i> will cause HTCondor to always transfer files for the job. <i>NO</i> disables HTCondor&#8217;s file transfer mechanism. <i>IF_NEEDED</i> will not transfer files for the job if it is matched with a resource in the same FileSystemDomain as the submit machine (and therefore, on a machine with the same shared file system). If the job is matched with a remote resource in a different FileSystemDomain , HTCondor will transfer the necessary files.</p>
<dt>
<dd> For more information about this and other settings related to transferring files, see the HTCondor User&#8217;s manual section on the file transfer mechanism.</p>
<dt>
<dd> Note that <code>should_transfer_files</code> is not supported for jobs submitted to the grid universe.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>skip_filechecks = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> When True , file permission checks for the submitted job are disabled. When False , file permissions are checked; this is the behavior when this command is not present in the submit description file. File permissions are checked for read permissions on all input files, such as those defined by commands <code>input</code> and <code>transfer_input_files</code> , and for write permission to output files, such as a log file defined by <code>log</code> and output files defined with <code>output</code> or <code>transfer_output_files</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>stream_error = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> If True , then stderr is streamed back to the machine from which the job was submitted. If False , stderr is stored locally and transferred back when the job completes. This command is ignored if the job ClassAd attribute TransferErr is False . The default value is False . This command must be used in conjunction with <code>error</code> , otherwise stderr will sent to /dev/null on Unix machines and ignored on Windows machines.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>stream_input = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> If True , then stdin is streamed from the machine on which the job was submitted. The default value is False . The command is only relevant for jobs submitted to the vanilla or java universes, and it is ignored by the grid universe. This command must be used in conjunction with <code>input</code> , otherwise stdin will be /dev/null on Unix machines and ignored on Windows machines.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>stream_output = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> If True , then stdout is streamed back to the machine from which the job was submitted. If False , stdout is stored locally and transferred back when the job completes. This command is ignored if the job ClassAd attribute TransferOut is False . The default value is False . This command must be used in conjunction with <code>output</code> , otherwise stdout will sent to /dev/null on Unix machines and ignored on Windows machines.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>transfer_executable = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> This command is applicable to jobs submitted to the grid and vanilla universes. If <code>transfer_executable</code> is set to False , then HTCondor looks for the executable on the remote machine, and does not transfer the executable over. This is useful for an already pre-staged executable; HTCondor behaves more like rsh. The default value is True .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>transfer_input_files = &lt;file1,file2,file&#8230; &gt;</code></p>
<dl>
<dt>
<dd> A comma-delimited list of all the files and directories to be transferred into the working directory for the job, before the job is started. By default, the file specified in the <code>executable</code> command and any file specified in the <code>input</code> command (for example, stdin ) are transferred.</p>
<dt>
<dd> When a path to an input file or directory is specified, this specifies the path to the file on the submit side. The file is placed in the job&#8217;s temporary scratch directory on the execute side, and it is named using the base name of the original path. For example, /path/to/input_file becomes input_file in the job&#8217;s scratch directory.</p>
<dt>
<dd> A directory may be specified by appending the forward slash character (/) as a trailing path separator. This syntax is used for both Windows and Linux submit hosts. A directory example using a trailing path separator is input_data/ . When a directory is specified with the trailing path separator, the contents of the directory are transferred, but the directory itself is not transferred. It is as if each of the items within the directory were listed in the transfer list. When there is no trailing path separator, the directory is transferred, its contents are transferred, and these contents are placed inside the transferred directory.</p>
<dt>
<dd> For grid universe jobs other than HTCondor-C, the transfer of directories is not currently supported.</p>
<dt>
<dd> Symbolic links to files are transferred as the files they point to. Transfer of symbolic links to directories is not currently supported.</p>
<dt>
<dd> For vanilla and vm universe jobs only, a file may be specified by giving a URL, instead of a file name. The implementation for URL transfers requires both configuration and available plug-in.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>transfer_output_files = &lt;file1,file2,file&#8230; &gt;</code></p>
<dl>
<dt>
<dd> This command forms an explicit list of output files and directories to be transferred back from the temporary working directory on the execute machine to the submit machine. If there are multiple files, they must be delimited with commas. Setting <code>transfer_output_files</code> to the empty string ( &quot;&quot; ) means that no files are to be transferred.</p>
<dt>
<dd> For HTCondor-C jobs and all other non-grid universe jobs, if <code>transfer_output_files</code> is not specified, HTCondor will automatically transfer back all files in the job&#8217;s temporary working directory which have been modified or created by the job. Subdirectories are not scanned for output, so if output from subdirectories is desired, the output list must be explicitly specified. For grid universe jobs other than HTCondor-C, desired output files must also be explicitly listed. Another reason to explicitly list output files is for a job that creates many files, and the user wants only a subset transferred back.</p>
<dt>
<dd> For grid universe jobs other than with grid type <code>condor</code> , to have files other than standard output and standard error transferred from the execute machine back to the submit machine, do use <code>transfer_output_files</code> , listing all files to be transferred. These files are found on the execute machine in the working directory of the job.</p>
<dt>
<dd> When a path to an output file or directory is specified, it specifies the path to the file on the execute side. As a destination on the submit side, the file is placed in the job&#8217;s initial working directory, and it is named using the base name of the original path. For example, path/to/output_file becomes output_file in the job&#8217;s initial working directory. The name and path of the file that is written on the submit side may be modified by using <code>transfer_output_remaps</code> . Note that this remap function only works with files but not with directories.</p>
<dt>
<dd> A directory may be specified using a trailing path separator. An example of a trailing path separator is the slash character on Unix platforms; a directory example using a trailing path separator is input_data/ . When a directory is specified with a trailing path separator, the contents of the directory are transferred, but the directory itself is not transferred. It is as if each of the items within the directory were listed in the transfer list. When there is no trailing path separator, the directory is transferred, its contents are transferred, and these contents are placed inside the transferred directory.</p>
<dt>
<dd> For grid universe jobs other than HTCondor-C, the transfer of directories is not currently supported.</p>
<dt>
<dd> Symbolic links to files are transferred as the files they point to. Transfer of symbolic links to directories is not currently supported.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>transfer_output_remaps &lt;&#8220; name newname ; name2 newname2 &#8230; &#8221;&gt;</code></p>
<dl>
<dt>
<dd> This specifies the name (and optionally path) to use when downloading output files from the completed job. Normally, output files are transferred back to the initial working directory with the same name they had in the execution directory. This gives you the option to save them with a different path or name. If you specify a relative path, the final path will be relative to the job&#8217;s initial working directory.</p>
<dt>
<dd> <i>name</i> describes an output file name produced by your job, and <i>newname</i> describes the file name it should be downloaded to. Multiple remaps can be specified by separating each with a semicolon. If you wish to remap file names that contain equals signs or semicolons, these special characters may be escaped with a backslash. You cannot specify directories to be remapped.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>when_to_transfer_output = &lt;ON_EXIT | ON_EXIT_OR_EVICT &gt;</code></p>
<dl>
<dt>
<dd>
<dt>
<dd> Setting <code>when_to_transfer_output</code> equal to <i>ON_EXIT</i> will cause HTCondor to transfer the job&#8217;s output files back to the submitting machine only when the job completes (exits on its own).</p>
<dt>
<dd> The <i>ON_EXIT_OR_EVICT</i> option is intended for fault tolerant jobs which periodically save their own state and can restart where they left off. In this case, files are spooled to the submit machine any time the job leaves a remote site, either because it exited on its own, or was evicted by the HTCondor system for any reason prior to job completion. The files spooled back are placed in a directory defined by the value of the SPOOL configuration variable. Any output files transferred back to the submit machine are automatically sent back out again as input files if the job restarts.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <i>POLICY COMMANDS</i></p>
<dl>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>hold = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> If <code>hold</code> is set to True , then the submitted job will be placed into the Hold state. Jobs in the Hold state will not run until released by <i>condor_release</i> . Defaults to False .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>keep_claim_idle = &lt;integer&gt;</code></p>
<dl>
<dt>
<dd> An integer number of seconds that a job requests the <i>condor_schedd</i> to wait before releasing its claim after the job exits or after the job is removed.</p>
<dt>
<dd> The process by which the <i>condor_schedd</i> claims a <i>condor_startd</i> is somewhat time-consuming. To amortize this cost, the <i>condor_schedd</i> tries to reuse claims to run subsequent jobs, after a job using a claim is done. However, it can only do this if there is an idle job in the queue at the moment the previous job completes. Sometimes, and especially for the node jobs when using DAGMan, there is a subsequent job about to be submitted, but it has not yet arrived in the queue when the previous job completes. As a result, the <i>condor_schedd</i> releases the claim, and the next job must wait an entire negotiation cycle to start. When this submit command is defined with a non-negative integer, when the job exits, the <i>condor_schedd</i> tries as usual to reuse the claim. If it cannot, instead of releasing the claim, the <i>condor_schedd</i> keeps the claim until either the number of seconds given as a parameter, or a new job which matches that claim arrives, whichever comes first. The <i>condor_startd</i> in question will remain in the Claimed/Idle state, and the original job will be &quot;charged&quot; (in terms of priority) for the time in this state.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>leave_in_queue = &lt;ClassAd Boolean Expression&gt;</code></p>
<dl>
<dt>
<dd> When the ClassAd Expression evaluates to True , the job is not removed from the queue upon completion. This allows the user of a remotely spooled job to retrieve output files in cases where HTCondor would have removed them as part of the cleanup associated with completion. The job will only exit the queue once it has been marked for removal (via <i>condor_rm</i> , for example) and the <code>leave_in_queue</code> expression has become False . <code>leave_in_queue</code> defaults to False .</p>
<dt>
<dd> As an example, if the job is to be removed once the output is retrieved with <i>condor_transfer_data</i> , then use</dl>
<p> leave_in_queue = (JobStatus == 4) &amp;&amp; ((StageOutFinish =?= UNDEFINED) ||\ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(StageOutFinish&nbsp;<wbr>==&nbsp;<wbr>0))</p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>next_job_start_delay = &lt;ClassAd Boolean Expression&gt;</code></p>
<dl>
<dt>
<dd> This expression specifies the number of seconds to delay after starting up this job before the next job is started. The maximum allowed delay is specified by the HTCondor configuration variable MAX_NEXT_JOB_START_DELAY , which defaults to 10 minutes. This command does not apply to <code>scheduler</code> or <code>local</code> universe jobs.</p>
<dt>
<dd> This command has been historically used to implement a form of job start throttling from the job submitter&#8217;s perspective. It was effective for the case of multiple job submission where the transfer of extremely large input data sets to the execute machine caused machine performance to suffer. This command is no longer useful, as throttling should be accomplished through configuration of the <i>condor_schedd</i> daemon.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>on_exit_hold = &lt;ClassAd Boolean Expression&gt;</code></p>
<dl>
<dt>
<dd> The ClassAd expression is checked when the job exits, and if True , places the job into the Hold state. If False (the default value when not defined), then nothing happens and the on_exit_remove expression is checked to determine if that needs to be applied.</p>
<dt>
<dd> For example: Suppose a job is known to run for a minimum of an hour. If the job exits after less than an hour, the job should be placed on hold and an e-mail notification sent, instead of being allowed to leave the queue.</p>
<dt>
<dd></dl>
<p>&nbsp;<wbr>&nbsp;<wbr>on_exit_hold&nbsp;<wbr>=&nbsp;<wbr>(time()&nbsp;<wbr>&#8211; JobStartDate)&nbsp;<wbr>&lt;&nbsp;<wbr>(60&nbsp;<wbr>*&nbsp;<wbr>$(MINUTE))</p>
<dl>
<dt>
<dd> This expression places the job on hold if it exits for any reason before running for an hour. An e-mail will be sent to the user explaining that the job was placed on hold because this expression became True .</p>
<dt>
<dd>
&nbsp;<wbr>periodic_*&nbsp;<wbr>expressions take precedence over&nbsp;<wbr>&nbsp;<wbr>on_exit_*&nbsp;<wbr>expressions, and&nbsp;<wbr>&nbsp;<wbr>*_hold expressions take precedence over a&nbsp;<wbr>&nbsp;<wbr>*_remove expressions.&nbsp;<wbr></p>
<dt>
<dd> Only job ClassAd attributes will be defined for use by this ClassAd expression. This expression is available for the vanilla, java, parallel, grid, local and scheduler universes. It is additionally available, when submitted from a Unix machine, for the standard universe.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>on_exit_hold_reason = &lt;ClassAd String Expression&gt;</code></p>
<dl>
<dt>
<dd> When the job is placed on hold due to the <code>on_exit_hold</code> expression becoming True , this expression is evaluated to set the value of HoldReason in the job ClassAd. If this expression is UNDEFINED or produces an empty or invalid string, a default description is used.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>on_exit_hold_subcode = &lt;ClassAd Integer Expression&gt;</code></p>
<dl>
<dt>
<dd> When the job is placed on hold due to the <code>on_exit_hold</code> expression becoming True , this expression is evaluated to set the value of HoldReasonSubCode in the job ClassAd. The default subcode is 0. The HoldReasonCode will be set to 3, which indicates that the job went on hold due to a job policy expression.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>on_exit_remove = &lt;ClassAd Boolean Expression&gt;</code></p>
<dl>
<dt>
<dd> The ClassAd expression is checked when the job exits, and if True (the default value when undefined), then it allows the job to leave the queue normally. If False , then the job is placed back into the Idle state. If the user job runs under the vanilla universe, then the job restarts from the beginning. If the user job runs under the standard universe, then it continues from where it left off, using the last checkpoint.</p>
<dt>
<dd> For example, suppose a job occasionally segfaults, but chances are that the job will finish successfully if the job is run again with the same data. The <code>on_exit_remove</code> expression can cause the job to run again with the following command. Assume that the signal identifier for the segmentation fault is 11 on the platform where the job will be running.</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>on_exit_remove&nbsp;<wbr>=&nbsp;<wbr>(ExitBySignal&nbsp;<wbr>==&nbsp;<wbr>False)&nbsp;<wbr>||&nbsp;<wbr>(ExitSignal&nbsp;<wbr>!=&nbsp;<wbr>11)</p>
<dl>
<dt>
<dd> This expression lets the job leave the queue if the job was not killed by a signal or if it was killed by a signal other than 11, representing segmentation fault in this example. So, if the exited due to signal 11, it will stay in the job queue. In any other case of the job exiting, the job will leave the queue as it normally would have done.</p>
<dt>
<dd> As another example, if the job should only leave the queue if it exited on its own with status 0, this <code>on_exit_remove</code> expression works well:</p>
<dt>
<dd></dl>
<p>&nbsp;<wbr>&nbsp;<wbr>on_exit_remove&nbsp;<wbr>=&nbsp;<wbr>(ExitBySignal&nbsp;<wbr>==&nbsp;<wbr>False)&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>(ExitCode&nbsp;<wbr>==&nbsp;<wbr>0)</p>
<dl>
<dt>
<dd> If the job was killed by a signal or exited with a non-zero exit status, HTCondor would leave the job in the queue to run again.</p>
<dt>
<dd>
&nbsp;<wbr>periodic_*&nbsp;<wbr>expressions take precedence over&nbsp;<wbr>&nbsp;<wbr>on_exit_*&nbsp;<wbr>expressions, and&nbsp;<wbr>&nbsp;<wbr>*_hold expressions take precedence over a&nbsp;<wbr>&nbsp;<wbr>*_remove expressions.&nbsp;<wbr></p>
<dt>
<dd> Only job ClassAd attributes will be defined for use by this ClassAd expression. This expression is available for the vanilla, java, parallel, grid, local and scheduler universes. It is additionally available, when submitted from a Unix machine, for the standard universe. Note that the <i>condor_schedd</i> daemon, by default, only checks these periodic expressions once every 300 seconds. The period of these evaluations can be adjusted by setting the PERIODIC_EXPR_INTERVAL configuration macro.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>periodic_hold = &lt;ClassAd Boolean Expression&gt;</code></p>
<dl>
<dt>
<dd> This expression is checked periodically at an interval of the number of seconds set by the configuration variable PERIODIC_EXPR_INTERVAL . If it becomes True , the job will be placed on hold. If unspecified, the default value is False .</p>
<dt>
<dd>
&nbsp;<wbr>periodic_*&nbsp;<wbr>expressions take precedence over&nbsp;<wbr>&nbsp;<wbr>on_exit_*&nbsp;<wbr>expressions, and&nbsp;<wbr>&nbsp;<wbr>*_hold expressions take precedence over a&nbsp;<wbr>&nbsp;<wbr>*_remove expressions.&nbsp;<wbr></p>
<dt>
<dd> Only job ClassAd attributes will be defined for use by this ClassAd expression. This expression is available for the vanilla, java, parallel, grid, local and scheduler universes. It is additionally available, when submitted from a Unix machine, for the standard universe. Note that the <i>condor_schedd</i> daemon, by default, only checks these periodic expressions once every 300 seconds. The period of these evaluations can be adjusted by setting the PERIODIC_EXPR_INTERVAL configuration macro.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>periodic_hold_reason = &lt;ClassAd String Expression&gt;</code></p>
<dl>
<dt>
<dd> When the job is placed on hold due to the <code>periodic_hold</code> expression becoming True , this expression is evaluated to set the value of HoldReason in the job ClassAd. If this expression is UNDEFINED or produces an empty or invalid string, a default description is used.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>periodic_hold_subcode = &lt;ClassAd Integer Expression&gt;</code></p>
<dl>
<dt>
<dd> When the job is placed on hold due to the <code>periodic_hold</code> expression becoming true, this expression is evaluated to set the value of HoldReasonSubCode in the job ClassAd. The default subcode is 0. The HoldReasonCode will be set to 3, which indicates that the job went on hold due to a job policy expression.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>periodic_release = &lt;ClassAd Boolean Expression&gt;</code></p>
<dl>
<dt>
<dd> This expression is checked periodically at an interval of the number of seconds set by the configuration variable PERIODIC_EXPR_INTERVAL while the job is in the Hold state. If the expression becomes True , the job will be released.</p>
<dt>
<dd> Only job ClassAd attributes will be defined for use by this ClassAd expression. This expression is available for the vanilla, java, parallel, grid, local and scheduler universes. It is additionally available, when submitted from a Unix machine, for the standard universe. Note that the <i>condor_schedd</i> daemon, by default, only checks periodic expressions once every 300 seconds. The period of these evaluations can be adjusted by setting the PERIODIC_EXPR_INTERVAL configuration macro.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>periodic_remove = &lt;ClassAd Boolean Expression&gt;</code></p>
<dl>
<dt>
<dd> This expression is checked periodically at an interval of the number of seconds set by the configuration variable PERIODIC_EXPR_INTERVAL . If it becomes True , the job is removed from the queue. If unspecified, the default value is False .</p>
<dt>
<dd> See the Examples section of this manual page for an example of a <code>periodic_remove</code> expression.</p>
<dt>
<dd>
&nbsp;<wbr>periodic_*&nbsp;<wbr>expressions take precedence over&nbsp;<wbr>&nbsp;<wbr>on_exit_*&nbsp;<wbr>expressions, and&nbsp;<wbr>&nbsp;<wbr>*_hold expressions take precedence over a&nbsp;<wbr>&nbsp;<wbr>*_remove expressions. So, the&nbsp;<wbr>&nbsp;<wbr>periodic_remove expression takes precedent over the&nbsp;<wbr>&nbsp;<wbr>on_exit_remove expression, if the two describe conflicting actions.&nbsp;<wbr></p>
<dt>
<dd> Only job ClassAd attributes will be defined for use by this ClassAd expression. This expression is available for the vanilla, java, parallel, grid, local and scheduler universes. It is additionally available, when submitted from a Unix machine, for the standard universe. Note that the <i>condor_schedd</i> daemon, by default, only checks periodic expressions once every 300 seconds. The period of these evaluations can be adjusted by setting the PERIODIC_EXPR_INTERVAL configuration macro.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <i>COMMANDS SPECIFIC TO THE STANDARD UNIVERSE</i> </p>
<dl>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>allow_startup_script = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> If True, a standard universe job will execute a script instead of submitting the job, and the consistency check to see if the executable has been linked using <i>condor_compile</i> is omitted. The <code>executable</code> command within the submit description file specifies the name of the script. The script is used to do preprocessing before the job is submitted. The shell script ends with an <i>exec</i> of the job executable, such that the process id of the executable is the same as that of the shell script. Here is an example script that gets a copy of a machine-specific executable before the <i>exec</i> .</dl>
<p>&nbsp;<wbr> </p>
<p>#!&nbsp;<wbr>/bin/sh </p>
<p>#&nbsp;<wbr>get the host name of the machine </p>
<p>$host=`uname -n` </p>
<p>#&nbsp;<wbr>grab a standard universe executable designed specifically </p>
<p>#&nbsp;<wbr>for this host </p>
<p>scp elsewhere [at] cs.wisc.edu:${host}&nbsp;<wbr>executable </p>
<p>#&nbsp;<wbr>The PID MUST stay the same, so exec the new standard universe process. </p>
<p>exec executable&nbsp;<wbr>${1+&quot;$@&quot;} If this command is not present (defined), then the value defaults to false.</p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>append_files = file1, file2, &#8230;</code></p>
<dl>
<dt>
<dd>
<dt>
<dd> If your job attempts to access a file mentioned in this list, HTCondor will force all writes to that file to be appended to the end. Furthermore, condor_submit will not truncate it. This list uses the same syntax as compress_files, shown above.</p>
<dt>
<dd> This option may yield some surprising results. If several jobs attempt to write to the same file, their output may be intermixed. If a job is evicted from one or more machines during the course of its lifetime, such an output file might contain several copies of the results. This option should be only be used when you wish a certain file to be treated as a running log instead of a precise result.</p>
<dt>
<dd> This option only applies to standard-universe jobs.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>buffer_files &lt;&#8220; name (size,block-size) ; name2 (size,block-size) &#8230; &#8221; &gt;</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>buffer_size &lt;bytes-in-buffer&gt;</code></p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>buffer_block_size &lt;bytes-in-block&gt;</code></p>
<dl>
<dt>
<dd> HTCondor keeps a buffer of recently-used data for each file a job accesses. This buffer is used both to cache commonly-used data and to consolidate small reads and writes into larger operations that get better throughput. The default settings should produce reasonable results for most programs.</p>
<dt>
<dd> These options only apply to standard-universe jobs.</p>
<dt>
<dd> If needed, you may set the buffer controls individually for each file using the buffer_files option. For example, to set the buffer size to 1 MiB and the block size to 256 KiB for the file input.data , use this command:</p>
<dt>
<dd></dl>
<p> buffer_files = &quot;input.data=(1000000,256000)&quot;</p>
<dl>
<dt>
<dd> Alternatively, you may use these two options to set the default sizes for all files used by your job:</p>
<dt>
<dd></dl>
<p> buffer_size = 1000000<br />
 buffer_block_size = 256000</p>
<dl>
<dt>
<dd> If you do not set these, HTCondor will use the values given by these two configuration file macros:</p>
<dt>
<dd></dl>
<p> DEFAULT_IO_BUFFER_SIZE = 1000000<br />
 DEFAULT_IO_BUFFER_BLOCK_SIZE = 256000</p>
<dl>
<dt>
<dd> Finally, if no other settings are present, HTCondor will use a buffer of 512 KiB and a block size of 32 KiB.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>compress_files = file1, file2, &#8230;</code></p>
<dl>
<dt>
<dd>
<dt>
<dd> If your job attempts to access any of the files mentioned in this list, HTCondor will automatically compress them (if writing) or decompress them (if reading). The compress format is the same as used by GNU gzip.</p>
<dt>
<dd> The files given in this list may be simple file names or complete paths and may include as a wild card. For example, this list causes the file /tmp/data.gz, any file named event.gz, and any file ending in .gzip to be automatically compressed or decompressed as needed:</p>
<dt>
<dd></dl>
<p> compress_files = /tmp/data.gz, event.gz, *.gzip</p>
<dl>
<dt>
<dd> Due to the nature of the compression format, compressed files must only be accessed sequentially. Random access reading is allowed but is very slow, while random access writing is simply not possible. This restriction may be avoided by using both compress_files and fetch_files at the same time. When this is done, a file is kept in the decompressed state at the execution machine, but is compressed for transfer to its original location.</p>
<dt>
<dd> This option only applies to standard universe jobs.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>fetch_files = file1, file2, &#8230;</code></p>
<dl>
<dt>
<dd> If your job attempts to access a file mentioned in this list, HTCondor will automatically copy the whole file to the executing machine, where it can be accessed quickly. When your job closes the file, it will be copied back to its original location. This list uses the same syntax as compress_files, shown above.</p>
<dt>
<dd> This option only applies to standard universe jobs.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>file_remaps &lt;&#8220; name newname ; name2 newname2 &#8230; &#8221;&gt;</code></p>
<dl>
<dt>
<dd>
<dt>
<dd> Directs HTCondor to use a new file name in place of an old one. <i>name</i> describes a file name that your job may attempt to open, and <i>newname</i> describes the file name it should be replaced with. <i>newname</i> may include an optional leading access specifier, local: or remote: . If left unspecified, the default access specifier is remote: . Multiple remaps can be specified by separating each with a semicolon.</p>
<dt>
<dd> This option only applies to standard universe jobs.</p>
<dt>
<dd> If you wish to remap file names that contain equals signs or semicolons, these special characters may be escaped with a backslash.</p>
<dt>
<dd>
<dt>
<dd> <code>Example One:</code></p>
<dt>
<dd> Suppose that your job reads a file named dataset.1 . To instruct HTCondor to force your job to read other.dataset instead, add this to the submit file:</dl>
<p> file_remaps = &quot;dataset.1=other.dataset&quot;</p>
<dl>
<dt>
<dd>
<dt>
<dd> <code>Example Two:</code></p>
<dt>
<dd> Suppose that your run many jobs which all read in the same large file, called very.big . If this file can be found in the same place on a local disk in every machine in the pool, (say /bigdisk/bigfile ,) you can instruct HTCondor of this fact by remapping very.big to /bigdisk/bigfile and specifying that the file is to be read locally, which will be much faster than reading over the network.</dl>
<p> file_remaps = &quot;very.big = local:/bigdisk/bigfile&quot;</p>
<dl>
<dt>
<dd>
<dt>
<dd> <code>Example Three:</code></p>
<dt>
<dd> Several remaps can be applied at once by separating each with a semicolon.</dl>
<p> file_remaps = &quot;very.big = local:/bigdisk/bigfile ; dataset.1 = other.dataset&quot;</p>
<dl>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>local_files = file1, file2, &#8230;</code></p>
<dl>
<dt>
<dd>
<dt>
<dd> If your job attempts to access a file mentioned in this list, HTCondor will cause it to be read or written at the execution machine. This is most useful for temporary files not used for input or output. This list uses the same syntax as compress_files, shown above.</p>
<dt>
<dd></dl>
<p> local_files = /tmp/*</p>
<dl>
<dt>
<dd> This option only applies to standard universe jobs.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>want_remote_io = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> This option controls how a file is opened and manipulated in a standard universe job. If this option is true, which is the default, then the <i>condor_shadow</i> makes all decisions about how each and every file should be opened by the executing job. This entails a network round trip (or more) from the job to the <i>condor_shadow</i> and back again for every single open() in addition to other needed information about the file. If set to false, then when the job queries the <i>condor_shadow</i> for the first time about how to open a file, the <i>condor_shadow</i> will inform the job to automatically perform all of its file manipulation on the local file system on the execute machine and any file remapping will be ignored. This means that there <code>must</code> be a shared file system (such as NFS or AFS) between the execute machine and the submit machine and that <code>ALL</code> paths that the job could open on the execute machine must be valid. The ability of the standard universe job to checkpoint, possibly to a checkpoint server, is not affected by this attribute. However, when the job resumes it will be expecting the same file system conditions that were present when the job checkpointed.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <i>COMMANDS FOR THE GRID</i></p>
<dl>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>batch_queue = &lt;queuename&gt;</code></p>
<dl>
<dt>
<dd> Used for <code>pbs</code> , <code>lsf</code> , and <code>sge</code> grid universe jobs. Specifies the name of the PBS/LSF/SGE job queue into which the job should be submitted. If not specified, the default queue is used.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>boinc_authenticator_file = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>boinc</code> jobs, specifies a path and file name of the authorization file that grants permission for HTCondor to use the BOINC service. There is no default value when not specified.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>cream_attributes = &lt;name=value;&#8230; ;name=value&gt;</code></p>
<dl>
<dt>
<dd> Provides a list of attribute/value pairs to be set in a CREAM job description of a grid universe job destined for the CREAM grid system. The pairs are separated by semicolons, and written in New ClassAd syntax.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>delegate_job_GSI_credentials_lifetime = &lt;seconds&gt;</code></p>
<dl>
<dt>
<dd> Specifies the maximum number of seconds for which delegated proxies should be valid. The default behavior when this command is not specified is determined by the configuration variable DELEGATE_JOB_GSI_CREDENTIALS_LIFETIME , which defaults to one day. A value of 0 indicates that the delegated proxy should be valid for as long as allowed by the credential used to create the proxy. This setting currently only applies to proxies delegated for non-grid jobs and for HTCondor-C jobs. It does not currently apply to globus grid jobs, which always behave as though this setting were 0. This variable has no effect if the configuration variable DELEGATE_JOB_GSI_CREDENTIALS is False , because in that case the job proxy is copied rather than delegated.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deltacloud_hardware_profile = &lt;Deltacloud profile name&gt;</code></p>
<dl>
<dt>
<dd> Used for <code>deltacloud</code> jobs. An optional identifier for the type of VM desired. If not provided, a service-defined default is used.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deltacloud_hardware_profile_cpu = &lt;cpu details&gt;</code></p>
<dl>
<dt>
<dd> Used for <code>deltacloud</code> jobs. An optional description of the CPUs desired for the VM, overriding the selected hardware profile.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deltacloud_hardware_profile_memory = &lt;memory details&gt;</code></p>
<dl>
<dt>
<dd> Used for <code>deltacloud</code> jobs. An optional description of the memory (RAM) desired for the VM, overriding the selected hardware profile.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deltacloud_hardware_profile_storage = &lt;storage details&gt;</code></p>
<dl>
<dt>
<dd> Used for <code>deltacloud</code> jobs. An optional description of the storage (disk) desired for the VM, overriding the selected hardware profile.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deltacloud_image_id = &lt;Deltacloud image ID&gt;</code></p>
<dl>
<dt>
<dd> Used for <code>deltacloud</code> jobs. Identifier of the VM image to run.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deltacloud_keyname = &lt;Deltacloud key name&gt;</code></p>
<dl>
<dt>
<dd> Used for <code>deltacloud</code> jobs. Identifier of the SSH key pair that should be used to allow remote login to the running instance. The key pair needs to be created before submission.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deltacloud_password_file = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> Used for <code>deltacloud</code> jobs. Path and file name of a file containing the secret key to be used to authenticate with a Deltacloud service.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deltacloud_realm_id = &lt;Deltacloud realm ID&gt;</code></p>
<dl>
<dt>
<dd> Used for <code>deltacloud</code> jobs. An optional identifier specifying which of multiple locations within a cloud service should be used to run the VM. If not provided, a service-selected default is used.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deltacloud_user_data = &lt;data&gt;</code></p>
<dl>
<dt>
<dd> Used for <code>deltacloud</code> jobs. A string, representing a block of data that can be accessed by the virtual machine job inside the cloud service.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deltacloud_username = &lt;Deltacloud username&gt;</code></p>
<dl>
<dt>
<dd> Used for <code>deltacloud</code> jobs. The user name to be used to authenticate with a Deltacloud service.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_access_key_id = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, identifies the file containing the access key.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_ami_id = &lt;EC2 xMI ID&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, identifies the machine image. Services compatible with the EC2 Query API may refer to these with abbreviations other than AMI , for example EMI is valid for Eucalyptus.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_availability_zone = &lt;zone name&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, specifies the Availability Zone that the instance should be run in. This command is optional, unless <code>ec2_ebs_volumes</code> is set. As an example, one current zone is us-east-1b .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_block_device_mapping = &lt;block-device&gt;:&lt;kernel-device&gt;,&lt;block-device&gt;:&lt;kernel-device&gt;, &#8230; </code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, specifies the block device to kernel device mapping. This command is optional.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_ebs_volumes = &lt;ebs name&gt;:&lt;device name&gt;,&lt;ebs name&gt;:&lt;device name&gt;,&#8230; </code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, optionally specifies a list of Elastic Block Store (EBS) volumes to be made available to the instance and the device names they should have in the instance.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_elastic_ip = &lt;elastic IP address&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, and optional specification of an Elastic IP address that should be assigned to this instance.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_iam_profile_arn = &lt;IAM profile ARN&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, an Amazon Resource Name (ARN) identifying which Identity and Access Management (IAM) (instance) profile to associate with the instance.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_iam_profile_name= &lt;IAM profile name&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, a name identifying which Identity and Access Management (IAM) (instance) profile to associate with the instance.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_instance_type = &lt;instance type&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, identifies the instance type. Different services may offer different instance types, so no default value is set.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_key_pair = &lt;ssh key-pair name&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, specifies the name of an SSH key-pair that is already registered with the EC2 service. The associated private key can be used to <i>ssh</i> into the virtual machine once it is running.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_key_pair_file = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, specifies the complete path and file name of a file into which HTCondor will write an SSH key for use with ec2 jobs. The key can be used to <i>ssh</i> into the virtual machine once it is running. If <code>ec2_keypair</code> is specified for a job, <code>ec2_keypair_file</code> is ignored.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_parameter_names = ParameterName1, ParameterName2, &#8230;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, a space or comma separated list of the names of additional parameters to pass when instantiating an instance.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_parameter_&lt;name&gt;= &lt;value&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, specifies the value for the correspondingly named (instance instantiation) parameter. <code>&lt;name&gt;</code> is the parameter name specified in the submit command <code>ec2_parameter_names</code> , but with any periods replaced by underscores.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_secret_access_key = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, specifies the path and file name containing the secret access key.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_security_groups = group1, group2, &#8230;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, defines the list of EC2 security groups which should be associated with the job.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_security_ids = id1, id2, &#8230;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, defines the list of EC2 security group IDs which should be associated with the job.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_spot_price = &lt;bid&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, specifies the spot instance bid, which is the most that the job submitter is willing to pay per hour to run this job.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_tag_names = &lt;name0,name1,name&#8230;&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, specifies the case of tag names that will be associated with the running instance. This is only necessary if a tag name case matters. By default the list will be automatically generated.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_tag_&lt;name&gt;= &lt;value&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, specifies a tag to be associated with the running instance. The tag name will be lower-cased, use <code>ec2_tag_names</code> to change the case.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_user_data = &lt;data&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, provides a block of data that can be accessed by the virtual machine. If both <code>ec2_user_data</code> and <code>ec2_user_data_file</code> are specified for a job, the two blocks of data are concatenated, with the data from this <code>ec2_user_data</code> submit command occurring first.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_user_data_file = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, specifies a path and file name whose contents can be accessed by the virtual machine. If both <code>ec2_user_data</code> and <code>ec2_user_data_file</code> are specified for a job, the two blocks of data are concatenated, with the data from that <code>ec2_user_data</code> submit command occurring first.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_vpc_ip = &lt;a.b.c.d&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, that are part of a Virtual Private Cloud (VPC), an optional specification of the IP address that this instance should have within the VPC.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>ec2_vpc_subnet = &lt;subnet specification string&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>ec2</code> jobs, an optional specification of the Virtual Private Cloud (VPC) that this instance should be a part of.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>gce_auth_file = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>gce</code> jobs, specifies a path and file name of the authorization file that grants permission for HTCondor to use the Google account. There is no default value when not specified.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>gce_image = &lt;URL&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>gce</code> jobs, the URL of the virtual machine image representing the HTCondor job to be run. This virtual machine image must already be register with GCE and reside in Google&#8217;s Cloud Storage service.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>gce_machine_type = &lt;machine type&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>gce</code> jobs, the long form of the URL that describes the machine configuration that the virtual machine instance is to run on.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>gce_metadata = &lt;name=value,&#8230; ,name=value&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>gce</code> jobs, a comma separated list of name and value pairs that define metadata for a virtual machine instance that is an HTCondor job.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>gce_metadata_file = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> For grid type <code>gce</code> jobs, specifies a path and file name of the file that contains metadata for a virtual machine instance that is an HTCondor job. Within the file, each name and value pair is on its own line; so, the pairs are separated by the newline character.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>globus_rematch = &lt;ClassAd Boolean Expression&gt;</code></p>
<dl>
<dt>
<dd> This expression is evaluated by the <i>condor_gridmanager</i> whenever:</p>
<dt>
<dd> 1. the <code>globus_resubmit</code> expression evaluates to True</p>
<dt>
<dd> 2. the <i>condor_gridmanager</i> decides it needs to retry a submission (as when a previous submission failed to commit) If <code>globus_rematch</code> evaluates to True , then <i>before</i> the job is submitted again to globus, the <i>condor_gridmanager</i> will request that the <i>condor_schedd</i> daemon renegotiate with the matchmaker (the <i>condor_negotiator</i> ). The result is this job will be matched again.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>globus_resubmit = &lt;ClassAd Boolean Expression&gt;</code></p>
<dl>
<dt>
<dd> The expression is evaluated by the <i>condor_gridmanager</i> each time the <i>condor_gridmanager</i> gets a job ad to manage. Therefore, the expression is evaluated:</p>
<dt>
<dd> 1. when a grid universe job is first submitted to HTCondor-G</p>
<dt>
<dd> 2. when a grid universe job is released from the hold state</p>
<dt>
<dd> 3. when HTCondor-G is restarted (specifically, whenever the <i>condor_gridmanager</i> is restarted) If the expression evaluates to True , then any previous submission to the grid universe will be forgotten and this job will be submitted again as a fresh submission to the grid universe. This may be useful if there is a desire to give up on a previous submission and try again. Note that this may result in the same job running more than once. Do not treat this operation lightly.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>globus_rsl = &lt;RSL-string&gt;</code></p>
<dl>
<dt>
<dd> Used to provide any additional Globus RSL string attributes which are not covered by other submit description file commands or job attributes. Used for <code>grid</code> <code>universe</code> jobs, where the grid resource has a <code>grid-type-string</code> of <code>gt2</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>grid_resource = &lt;grid-type-string&gt;&lt;grid-specific-parameter-list&gt;</code></p>
<dl>
<dt>
<dd> For each <code>grid-type-string</code> value, there are further type-specific values that must specified. This submit description file command allows each to be given in a space-separated list. Allowable <code>grid-type-string</code> values are <code>batch</code> , <code>condor</code> , <code>cream</code> , <code>deltacloud</code> , <code>ec2</code> , <code>gt2</code> , <code>gt5</code> , <code>lsf</code> , <code>nordugrid</code> , <code>pbs</code> , <code>sge</code> , and <code>unicore</code> . The HTCondor manual chapter on Grid Computing details the variety of grid types.</p>
<dt>
<dd> For a <code>grid-type-string</code> of <code>batch</code> , the single parameter is the name of the local batch system, and will be one of pbs , lsf , or sge .</p>
<dt>
<dd> For a <code>grid-type-string</code> of <code>condor</code> , the first parameter is the name of the remote <i>condor_schedd</i> daemon. The second parameter is the name of the pool to which the remote <i>condor_schedd</i> daemon belongs.</p>
<dt>
<dd> For a <code>grid-type-string</code> of <code>cream</code> , there are three parameters. The first parameter is the web services address of the CREAM server. The second parameter is the name of the batch system that sits behind the CREAM server. The third parameter identifies a site-specific queue within the batch system.</p>
<dt>
<dd> For a <code>grid-type-string</code> of <code>deltacloud</code> , the single parameter is the URL of the deltacloud service requested.</p>
<dt>
<dd> For a <code>grid-type-string</code> of <code>ec2</code> , one additional parameter specifies the EC2 URL.</p>
<dt>
<dd> For a <code>grid-type-string</code> of <code>gt2</code> , the single parameter is the name of the pre-WS GRAM resource to be used.</p>
<dt>
<dd> For a <code>grid-type-string</code> of <code>gt5</code> , the single parameter is the name of the pre-WS GRAM resource to be used, which is the same as for the <code>grid-type-string</code> of <code>gt2</code> .</p>
<dt>
<dd> For a <code>grid-type-string</code> of <code>lsf</code> , no additional parameters are used.</p>
<dt>
<dd> For a <code>grid-type-string</code> of <code>nordugrid</code> , the single parameter is the name of the NorduGrid resource to be used.</p>
<dt>
<dd> For a <code>grid-type-string</code> of <code>pbs</code> , no additional parameters are used.</p>
<dt>
<dd> For a <code>grid-type-string</code> of <code>sge</code> , no additional parameters are used.</p>
<dt>
<dd> For a <code>grid-type-string</code> of <code>unicore</code> , the first parameter is the name of the Unicore Usite to be used. The second parameter is the name of the Unicore Vsite to be used.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>keystore_alias = &lt;name&gt;</code></p>
<dl>
<dt>
<dd> A string to locate the certificate in a Java keystore file, as used for a <code>unicore</code> job.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>keystore_file = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> The complete path and file name of the Java keystore file containing the certificate to be used for a <code>unicore</code> job.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>keystore_passphrase_file = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> The complete path and file name to the file containing the passphrase protecting a Java keystore file containing the certificate. Relevant for a <code>unicore</code> job.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>MyProxyCredentialName = &lt;symbolic name&gt;</code></p>
<dl>
<dt>
<dd> The symbolic name that identifies a credential to the <i>MyProxy</i> server. This symbolic name is set as the credential is initially stored on the server (using <i>myproxy-init</i> ).</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>MyProxyHost = &lt;host&gt;:&lt;port&gt;</code></p>
<dl>
<dt>
<dd> The Internet address of the host that is the <i>MyProxy</i> server. The <code>host</code> may be specified by either a host name (as in head.example.com ) or an IP address (of the form 123.456.7.8). The <code>port</code> number is an integer.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>MyProxyNewProxyLifetime = &lt;number-of-minutes&gt;</code></p>
<dl>
<dt>
<dd> The new lifetime (in minutes) of the proxy after it is refreshed.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>MyProxyPassword = &lt;password&gt;</code></p>
<dl>
<dt>
<dd> The password needed to refresh a credential on the <i>MyProxy</i> server. This password is set when the user initially stores credentials on the server (using <i>myproxy-init</i> ). As an alternative to using <code>MyProxyPassword</code> in the submit description file, the password may be specified as a command line argument to <i>condor_submit</i> with the <i>-password</i> argument.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>MyProxyRefreshThreshold = &lt;number-of-seconds&gt;</code></p>
<dl>
<dt>
<dd> The time (in seconds) before the expiration of a proxy that the proxy should be refreshed. For example, if <code>MyProxyRefreshThreshold</code> is set to the value 600, the proxy will be refreshed 10 minutes before it expires.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>MyProxyServerDN = &lt;credential subject&gt;</code></p>
<dl>
<dt>
<dd> A string that specifies the expected Distinguished Name (credential subject, abbreviated DN) of the <i>MyProxy</i> server. It must be specified when the <i>MyProxy</i> server DN does not follow the conventional naming scheme of a host credential. This occurs, for example, when the <i>MyProxy</i> server DN begins with a user credential.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>nordugrid_rsl = &lt;RSL-string&gt;</code></p>
<dl>
<dt>
<dd> Used to provide any additional RSL string attributes which are not covered by regular submit description file parameters. Used when the <code>universe</code> is <code>grid</code> , and the type of grid system is <code>nordugrid</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>transfer_error = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> For jobs submitted to the grid universe only. If True , then the error output (from stderr ) from the job is transferred from the remote machine back to the submit machine. The name of the file after transfer is given by the <code>error</code> command. If False , no transfer takes place (from the remote machine to submit machine), and the name of the file is given by the <code>error</code> command. The default value is True .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>transfer_input = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> For jobs submitted to the grid universe only. If True , then the job input ( stdin ) is transferred from the machine where the job was submitted to the remote machine. The name of the file that is transferred is given by the <code>input</code> command. If False , then the job&#8217;s input is taken from a pre-staged file on the remote machine, and the name of the file is given by the <code>input</code> command. The default value is True .</p>
<dt>
<dd> For transferring files other than stdin , see <code>transfer_input_files</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>transfer_output = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> For jobs submitted to the grid universe only. If True , then the output (from stdout ) from the job is transferred from the remote machine back to the submit machine. The name of the file after transfer is given by the <code>output</code> command. If False , no transfer takes place (from the remote machine to submit machine), and the name of the file is given by the <code>output</code> command. The default value is True .</p>
<dt>
<dd> For transferring files other than stdout , see <code>transfer_output_files</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>use_x509userproxy = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> Set this command to True to indicate that the job requires an X.509 user proxy. If <code>x509userproxy</code> is set, then that file is used for the proxy. Otherwise, the proxy is looked for in the standard locations. If <code>x509userproxy</code> is set or if the job is a grid universe job of grid type <code>gt2</code> , <code>gt5</code> , <code>cream</code> , or <code>nordugrid</code> , then the value of <code>use_x509userproxy</code> is forced to True . Defaults to False .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>x509userproxy = &lt;full-pathname&gt;</code></p>
<dl>
<dt>
<dd> Used to override the default path name for X.509 user certificates. The default location for X.509 proxies is the /tmp directory, which is generally a local file system. Setting this value would allow HTCondor to access the proxy in a shared file system (for example, AFS). HTCondor will use the proxy specified in the submit description file first. If nothing is specified in the submit description file, it will use the environment variable X509_USER_PROXY. If that variable is not present, it will search in the default location.</p>
<dt>
<dd> <code>x509userproxy</code> is relevant when the <code>universe</code> is <code>vanilla</code> , or when the <code>universe</code> is <code>grid</code> and the type of grid system is one of <code>gt2</code> , <code>gt5</code> , <code>condor</code> , <code>cream</code> , or <code>nordugrid</code> . Defining a value causes the proxy to be delegated to the execute machine. Further, VOMS attributes defined in the proxy will appear in the job ClassAd.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <i>COMMANDS FOR PARALLEL, JAVA, and SCHEDULER UNIVERSES</i></p>
<dl>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>hold_kill_sig = &lt;signal-number&gt;</code></p>
<dl>
<dt>
<dd> For the scheduler universe only, <code>signal-number</code> is the signal delivered to the job when the job is put on hold with <i>condor_hold</i> . <code>signal-number</code> may be either the platform-specific name or value of the signal. If this command is not present, the value of <code>kill_sig</code> is used.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>jar_files = &lt;file_list&gt;</code></p>
<dl>
<dt>
<dd> Specifies a list of additional JAR files to include when using the Java universe. JAR files will be transferred along with the executable and automatically added to the classpath.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>java_vm_args = &lt;argument_list&gt;</code></p>
<dl>
<dt>
<dd> Specifies a list of additional arguments to the Java VM itself, When HTCondor runs the Java program, these are the arguments that go before the class name. This can be used to set VM-specific arguments like stack size, garbage-collector arguments and initial property values.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>machine_count = &lt;max&gt;</code></p>
<dl>
<dt>
<dd> For the parallel universe, a single value ( <i>max</i> ) is required. It is neither a maximum or minimum, but the number of machines to be dedicated toward running the job.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>remove_kill_sig = &lt;signal-number&gt;</code></p>
<dl>
<dt>
<dd> For the scheduler universe only, <code>signal-number</code> is the signal delivered to the job when the job is removed with <i>condor_rm</i> . <code>signal-number</code> may be either the platform-specific name or value of the signal. This example shows it both ways for a Linux signal:</dl>
<p> remove_kill_sig = SIGUSR1<br />
 remove_kill_sig = 10</p>
<dl>
<dt>
<dd> If this command is not present, the value of <code>kill_sig</code> is used.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <i>COMMANDS FOR THE VM UNIVERSE</i></p>
<dl>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>vm_disk = file1:device1:permission1, file2:device2:permission2:format2, &#8230; </code></p>
<dl>
<dt>
<dd> A list of comma separated disk files. Each disk file is specified by 4 colon separated fields. The first field is the path and file name of the disk file. The second field specifies the device. The third field specifies permissions, and the optional fourth field specifies the image format.</p>
<dt>
<dd> An example that specifies two disk files:</dl>
<p> vm_disk = /myxen/diskfile.img:sda1:w,/myxen/swap.img:sda2:w</p>
<dl>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>vm_checkpoint = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> A boolean value specifying whether or not to take checkpoints. If not specified, the default value is False . In the current implementation, setting both <code>vm_checkpoint</code> and <code>vm_networking</code> to True does not yet work in all cases. Networking cannot be used if a vm universe job uses a checkpoint in order to continue execution after migration to another machine.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>vm_macaddr = &lt;MACAddr&gt;</code></p>
<dl>
<dt>
<dd> Defines that MAC address that the virtual machine&#8217;s network interface should have, in the standard format of six groups of two hexadecimal digits separated by colons.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>vm_memory = &lt;MBytes-of-memory&gt;</code></p>
<dl>
<dt>
<dd> The amount of memory in MBytes that a vm universe job requires.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>vm_networking = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> Specifies whether to use networking or not. In the current implementation, setting both <code>vm_checkpoint</code> and <code>vm_networking</code> to True does not yet work in all cases. Networking cannot be used if a vm universe job uses a checkpoint in order to continue execution after migration to another machine.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>vm_networking_type = &lt;nat | bridge &gt;</code></p>
<dl>
<dt>
<dd> When <code>vm_networking</code> is True , this definition augments the job&#8217;s requirements to match only machines with the specified networking. If not specified, then either networking type matches.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>vm_no_output_vm = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> When True , prevents HTCondor from transferring output files back to the machine from which the vm universe job was submitted. If not specified, the default value is False .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>vm_type = &lt;vmware | xen | kvm&gt;</code></p>
<dl>
<dt>
<dd> Specifies the underlying virtual machine software that this job expects.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>vmware_dir = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> The complete path and name of the directory where VMware-specific files and applications such as the VMDK (Virtual Machine Disk Format) and VMX (Virtual Machine Configuration) reside. This command is optional; when not specified, all relevant VMware image files are to be listed using <code>transfer_input_files</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>vmware_should_transfer_files = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> Specifies whether HTCondor will transfer VMware-specific files located as specified by <code>vmware_dir</code> to the execute machine ( True ) or rely on access through a shared file system ( False ). Omission of this required command (for VMware vm universe jobs) results in an error message from <i>condor_submit</i> , and the job will not be submitted.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>vmware_snapshot_disk = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> When True , causes HTCondor to utilize a VMware snapshot disk for new or modified files. If not specified, the default value is True .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>xen_initrd = &lt;image-file&gt;</code></p>
<dl>
<dt>
<dd> When <code>xen_kernel</code> gives a path and file name for the kernel image to use, this optional command may specify a path to and ramdisk ( initrd ) image file.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>xen_kernel = &lt;included | path-to-kernel&gt;</code></p>
<dl>
<dt>
<dd> A value of <code>included</code> specifies that the kernel is included in the disk file. If not one of these values, then the value is a path and file name of the kernel to be used.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>xen_kernel_params = &lt;string&gt;</code></p>
<dl>
<dt>
<dd> A string that is appended to the Xen kernel command line.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>xen_root = &lt;string&gt;</code></p>
<dl>
<dt>
<dd> A string that is appended to the Xen kernel command line to specify the root device. This string is required when <code>xen_kernel</code> gives a path to a kernel. Omission for this required case results in an error message during submission.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <i>COMMANDS FOR THE DOCKER UNIVERSE</i></p>
<dl>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>docker_image = &lt;image-name &gt;</code></p>
<dl>
<dt>
<dd> Defines the name of the Docker image that is the basis for the docker container.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <i>ADVANCED COMMANDS</i></p>
<dl>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>accounting_group = &lt;accounting-group-name&gt;</code></p>
<dl>
<dt>
<dd> Causes jobs to negotiate under the given accounting group. This value is advertised in the job ClassAd as AcctGroup . The HTCondor Administrator&#8217;s manual contains more information about accounting groups.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>accounting_group_user = &lt;accounting-group-user-name&gt;</code></p>
<dl>
<dt>
<dd> Sets the user name associated with the accounting group name for resource usage accounting purposes. If not set, defaults to the value of the job ClassAd attribute Owner . This value is advertised in the job ClassAd as AcctGroupUser . If an accounting group has not been set with the <code>accounting_group</code> command, this command is ignored.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>concurrency_limits = &lt;string-list&gt;</code></p>
<dl>
<dt>
<dd> A list of resources that this job needs. The resources are presumed to have concurrency limits placed upon them, thereby limiting the number of concurrent jobs in execution which need the named resource. Commas and space characters delimit the items in the list. Each item in the list is a string that identifies the limit, or it is a ClassAd expression that evaluates to a string, and it is evaluated in the context of machine ClassAd being considered as a match. Each item in the list also may specify a numerical value identifying the integer number of resources required for the job. The syntax follows the resource name by a colon character ( : ) and the numerical value. Details on concurrency limits are in the HTCondor Administrator&#8217;s manual.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>concurrency_limits_expr = &lt;ClassAd String Expression&gt;</code></p>
<dl>
<dt>
<dd> A ClassAd expression that represents the list of resources that this job needs after evaluation. The ClassAd expression may specify machine ClassAd attributes that are evaluated against a matched machine. After evaluation, the list sets <code>concurrency_limits</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>copy_to_spool = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> If <code>copy_to_spool</code> is True , then <i>condor_submit</i> copies the executable to the local spool directory before running it on a remote host. As copying can be quite time consuming and unnecessary, the default value is False for all job universes other than the standard universe. When False , <i>condor_submit</i> does not copy the executable to a local spool directory. The default is True in standard universe, because resuming execution from a checkpoint can only be guaranteed to work using precisely the same executable that created the checkpoint.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>coresize = &lt;size&gt;</code></p>
<dl>
<dt>
<dd> Should the user&#8217;s program abort and produce a core file, <code>coresize</code> specifies the maximum size in bytes of the core file which the user wishes to keep. If <code>coresize</code> is not specified in the command file, the system&#8217;s user resource limit coredumpsize is used. A value of -1 results in no limits being applied to the core file size.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>cron_day_of_month = &lt;Cron-evaluated Day&gt;</code></p>
<dl>
<dt>
<dd> The set of days of the month for which a deferral time applies. The HTCondor User&#8217;s manual section on Time Scheduling for Job Execution has further details.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>cron_day_of_week = &lt;Cron-evaluated Day&gt;</code></p>
<dl>
<dt>
<dd> The set of days of the week for which a deferral time applies. The HTCondor User&#8217;s manual section on Time Scheduling for Job Execution has further details.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>cron_hour = &lt;Cron-evaluated Hour&gt;</code></p>
<dl>
<dt>
<dd> The set of hours of the day for which a deferral time applies. The HTCondor User&#8217;s manual section on Time Scheduling for Job Execution has further details.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>cron_minute = &lt;Cron-evaluated Minute&gt;</code></p>
<dl>
<dt>
<dd> The set of minutes within an hour for which a deferral time applies. The HTCondor User&#8217;s manual section on Time Scheduling for Job Execution has further details.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>cron_month = &lt;Cron-evaluated Month&gt;</code></p>
<dl>
<dt>
<dd> The set of months within a year for which a deferral time applies. The HTCondor User&#8217;s manual section on Time Scheduling for Job Execution has further details.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>cron_prep_time = &lt;ClassAd Integer Expression&gt;</code></p>
<dl>
<dt>
<dd> Analogous to <code>deferral_prep_time</code> . The number of seconds prior to a job&#8217;s deferral time that the job may be matched and sent to an execution machine.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>cron_window = &lt;ClassAd Integer Expression&gt;</code></p>
<dl>
<dt>
<dd> Analogous to the submit command <code>deferral_window</code> . It allows cron jobs that miss their deferral time to begin execution.</p>
<dt>
<dd> The HTCondor User&#8217;s manual section on Time Scheduling for Job Execution has further details.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>dagman_log = &lt;pathname&gt;</code></p>
<dl>
<dt>
<dd> DAGMan inserts this command to specify an event log that it watches to maintain the state of the DAG. If the <code>log</code> command is not specified in the submit file, DAGMan uses the <code>log</code> command to specify the event log.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deferral_prep_time = &lt;ClassAd Integer Expression&gt;</code></p>
<dl>
<dt>
<dd> The number of seconds prior to a job&#8217;s deferral time that the job may be matched and sent to an execution machine.</p>
<dt>
<dd> The HTCondor User&#8217;s manual section on Time Scheduling for Job Execution has further details.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deferral_time = &lt;ClassAd Integer Expression&gt;</code></p>
<dl>
<dt>
<dd> Allows a job to specify the time at which its execution is to begin, instead of beginning execution as soon as it arrives at the execution machine. The deferral time is an expression that evaluates to a Unix Epoch timestamp (the number of seconds elapsed since 00:00:00 on January 1, 1970, Coordinated Universal Time). Deferral time is evaluated with respect to the execution machine. This option delays the start of execution, but not the matching and claiming of a machine for the job. If the job is not available and ready to begin execution at the deferral time, it has missed its deferral time. A job that misses its deferral time will be put on hold in the queue.</p>
<dt>
<dd> The HTCondor User&#8217;s manual section on Time Scheduling for Job Execution has further details.</p>
<dt>
<dd> Due to implementation details, a deferral time may not be used for scheduler universe jobs.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>deferral_window = &lt;ClassAd Integer Expression&gt;</code></p>
<dl>
<dt>
<dd> The deferral window is used in conjunction with the <code>deferral_time</code> command to allow jobs that miss their deferral time to begin execution.</p>
<dt>
<dd> The HTCondor User&#8217;s manual section on Time Scheduling for Job Execution has further details.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>description = &lt;string&gt;</code></p>
<dl>
<dt>
<dd> A string that sets the value of the job ClassAd attribute JobDescription . When set, tools which display the executable such as <i>condor_q</i> will instead use this string.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>email_attributes = &lt;list-of-job-ad-attributes&gt;</code></p>
<dl>
<dt>
<dd> A comma-separated list of attributes from the job ClassAd. These attributes and their values will be included in the e-mail notification of job completion.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>image_size = &lt;size&gt;</code></p>
<dl>
<dt>
<dd> Advice to HTCondor specifying the maximum virtual image size to which the job will grow during its execution. HTCondor will then execute the job only on machines which have enough resources, (such as virtual memory), to support executing the job. If not specified, HTCondor will automatically make a (reasonably accurate) estimate about the job&#8217;s size and adjust this estimate as the program runs. If specified and underestimated, the job may crash due to the inability to acquire more address space; for example, if malloc() fails. If the image size is overestimated, HTCondor may have difficulty finding machines which have the required resources. <i>size</i> is specified in KiB. For example, for an image size of 8 MiB, <i>size</i> should be 8000.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>initialdir = &lt;directory-path&gt;</code></p>
<dl>
<dt>
<dd> Used to give jobs a directory with respect to file input and output. Also provides a directory (on the machine from which the job is submitted) for the job event log, when a full path is not specified.</p>
<dt>
<dd> For vanilla universe jobs where there is a shared file system, it is the current working directory on the machine where the job is executed.</p>
<dt>
<dd> For vanilla or grid universe jobs where file transfer mechanisms are utilized (there is <i>not</i> a shared file system), it is the directory on the machine from which the job is submitted where the input files come from, and where the job&#8217;s output files go to.</p>
<dt>
<dd> For standard universe jobs, it is the directory on the machine from which the job is submitted where the <i>condor_shadow</i> daemon runs; the current working directory for file input and output accomplished through remote system calls.</p>
<dt>
<dd> For scheduler universe jobs, it is the directory on the machine from which the job is submitted where the job runs; the current working directory for file input and output with respect to relative path names.</p>
<dt>
<dd> Note that the path to the executable is <i>not</i> relative to <code>initialdir</code> ; if it is a relative path, it is relative to the directory in which the <i>condor_submit</i> command is run.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>job_ad_information_attrs = &lt;attribute-list&gt;</code></p>
<dl>
<dt>
<dd> A comma-separated list of job ClassAd attribute names. The named attributes and their values are written to the job event log whenever any event is being written to the log. This implements the same thing as the configuration variable EVENT_LOG_INFORMATION_ATTRS (see page ), but it applies to the job event log, instead of the system event log.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>job_lease_duration = &lt;number-of-seconds&gt;</code></p>
<dl>
<dt>
<dd> For vanilla and java universe jobs only, the duration (in seconds) of a job lease. The default value is twenty minutes for universes that support it. If a job lease is not desired, the value can be explicitly set to 0 to disable the job lease semantics. The HTCondor User&#8217;s manual section on Special Environment Considerations has further details.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>job_machine_attrs = &lt;attr1, attr2, &#8230; &gt;</code></p>
<dl>
<dt>
<dd> A comma and/or space separated list of machine attribute names that should be recorded in the job ClassAd in addition to the ones specified by the <i>condor_schedd</i> daemon&#8217;s system configuration variable SYSTEM_JOB_MACHINE_ATTRS . When there are multiple run attempts, history of machine attributes from previous run attempts may be kept. The number of run attempts to store may be extended beyond the system-specified history length by using the submit file command <code>job_machine_attrs_history_length</code> . A machine attribute named X will be inserted into the job ClassAd as an attribute named MachineAttrX0 . The previous value of this attribute will be named MachineAttrX1 , the previous to that will be named MachineAttrX2 , and so on, up to the specified history length. A history of length 1 means that only MachineAttrX0 will be recorded. The value recorded in the job ClassAd is the evaluation of the machine attribute in the context of the job ClassAd when the <i>condor_schedd</i> daemon initiates the start up of the job. If the evaluation results in an Undefined or Error result, the value recorded in the job ad will be Undefined or Error , respectively.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>want_graceful_removal = &lt;boolean expression&gt;</code></p>
<dl>
<dt>
<dd> When True , this causes a graceful shutdown of the job when the job is removed or put on hold, giving it time to clean up or save state. Otherwise, the job is abruptly killed. The default is false .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>kill_sig = &lt;signal-number&gt;</code></p>
<dl>
<dt>
<dd> When HTCondor needs to kick a job off of a machine, it will send the job the signal specified by <code>signal-number</code> . <code>signal-number</code> needs to be an integer which represents a valid signal on the execution machine. For jobs submitted to the standard universe, the default value is the number for SIGTSTP which tells the HTCondor libraries to initiate a checkpoint of the process. For jobs submitted to other universes, the default value, when not defined, is SIGTERM , which is the standard way to terminate a program in Unix.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>kill_sig_timeout = &lt;seconds&gt;</code></p>
<dl>
<dt>
<dd> This submit command should no longer be used as of HTCondor version 7.7.3; use <code>job_max_vacate_time</code> instead. If <code>job_max_vacate_time</code> is not defined, this defines the number of seconds that HTCondor should wait following the sending of the kill signal defined by <code>kill_sig</code> and forcibly killing the job. The actual amount of time between sending the signal and forcibly killing the job is the smallest of this value and the configuration variable KILLING_TIMEOUT , as defined on the execute machine.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>load_profile = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> When True , loads the account profile of the dedicated run account for Windows jobs. May not be used with <code>run_as_owner</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>match_list_length = &lt;integer value&gt;</code></p>
<dl>
<dt>
<dd> Defaults to the value zero (0). When <code>match_list_length</code> is defined with an integer value greater than zero (0), attributes are inserted into the job ClassAd. The maximum number of attributes defined is given by the integer value. The job ClassAds introduced are given as</dl>
<p> LastMatchName0 = &quot;most-recent-Name&quot;<br />
 LastMatchName1 = &quot;next-most-recent-Name&quot;</p>
<dl>
<dt>
<dd> The value for each introduced ClassAd is given by the value of the Name attribute from the machine ClassAd of a previous execution (match). As a job is matched, the definitions for these attributes will roll, with LastMatchName1 becoming LastMatchName2 , LastMatchName0 becoming LastMatchName1 , and LastMatchName0 being set by the most recent value of the Name attribute.</p>
<dt>
<dd> An intended use of these job attributes is in the requirements expression. The requirements can allow a job to prefer a match with either the same or a different resource than a previous match.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>job_max_vacate_time = &lt;integer expression&gt;</code></p>
<dl>
<dt>
<dd> An integer-valued expression (in seconds) that may be used to adjust the time given to an evicted job for gracefully shutting down. If the job&#8217;s setting is less than the machine&#8217;s, the job&#8217;s is used. If the job&#8217;s setting is larger than the machine&#8217;s, the result depends on whether the job has any excess retirement time. If the job has more retirement time left than the machine&#8217;s max vacate time setting, then retirement time will be converted into vacating time, up to the amount requested by the job.</p>
<dt>
<dd> Setting this expression does not affect the job&#8217;s resource requirements or preferences. For a job to only run on a machine with a minimum MachineMaxVacateTime , or to preferentially run on such machines, explicitly specify this in the requirements and/or rank expressions.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>max_job_retirement_time = &lt;integer expression&gt;</code></p>
<dl>
<dt>
<dd> An integer-valued expression (in seconds) that does nothing unless the machine that runs the job has been configured to provide retirement time. Retirement time is a grace period given to a job to finish when a resource claim is about to be preempted. The default behavior in many cases is to take as much retirement time as the machine offers, so this command will rarely appear in a submit description file.</p>
<dt>
<dd> When a resource claim is to be preempted, this expression in the submit file specifies the maximum run time of the job (in seconds, since the job started). This expression has no effect, if it is greater than the maximum retirement time provided by the machine policy. If the resource claim is <i>not</i> preempted, this expression and the machine retirement policy are irrelevant. If the resource claim <i>is</i> preempted the job will be allowed to run until the retirement time expires, at which point it is hard-killed. The job will be soft-killed when it is getting close to the end of retirement in order to give it time to gracefully shut down. The amount of lead-time for soft-killing is determined by the maximum vacating time granted to the job.</p>
<dt>
<dd> Standard universe jobs and any jobs running with <code>nice_user</code> priority have a default <code>max_job_retirement_time</code> of 0, so no retirement time is utilized by default. In all other cases, no default value is provided, so the maximum amount of retirement time is utilized by default.</p>
<dt>
<dd> Setting this expression does not affect the job&#8217;s resource requirements or preferences. For a job to only run on a machine with a minimum MaxJobRetirementTime , or to preferentially run on such machines, explicitly specify this in the requirements and/or rank expressions.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>nice_user = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> Normally, when a machine becomes available to HTCondor, HTCondor decides which job to run based upon user and job priorities. Setting <code>nice_user</code> equal to True tells HTCondor not to use your regular user priority, but that this job should have last priority among all users and all jobs. So jobs submitted in this fashion run only on machines which no other non-nice_user job wants &#8212; a true bottom-feeder job! This is very handy if a user has some jobs they wish to run, but do not wish to use resources that could instead be used to run other people&#8217;s HTCondor jobs. Jobs submitted in this fashion have &quot;nice-user.&quot; prepended to the owner name when viewed from <i>condor_q</i> or <i>condor_userprio</i> . The default value is False .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>noop_job = &lt;ClassAd Boolean Expression&gt;</code></p>
<dl>
<dt>
<dd> When this boolean expression is True , the job is immediately removed from the queue, and HTCondor makes no attempt at running the job. The log file for the job will show a job submitted event and a job terminated event, along with an exit code of 0, unless the user specifies a different signal or exit code.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>noop_job_exit_code = &lt;return value&gt;</code></p>
<dl>
<dt>
<dd> When <code>noop_job</code> is in the submit description file and evaluates to True , this command allows the job to specify the return value as shown in the job&#8217;s log file job terminated event. If not specified, the job will show as having terminated with status 0. This overrides any value specified with <code>noop_job_exit_signal</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>noop_job_exit_signal = &lt;signal number&gt;</code></p>
<dl>
<dt>
<dd> When <code>noop_job</code> is in the submit description file and evaluates to True , this command allows the job to specify the signal number that the job&#8217;s log event will show the job having terminated with.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>remote_initialdir = &lt;directory-path&gt;</code></p>
<dl>
<dt>
<dd> The path specifies the directory in which the job is to be executed on the remote machine. This is currently supported in all universes except for the standard universe.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>rendezvousdir = &lt;directory-path&gt;</code></p>
<dl>
<dt>
<dd> Used to specify the shared file system directory to be used for file system authentication when submitting to a remote scheduler. Should be a path to a preexisting directory.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>run_as_owner = &lt;True | False&gt;</code></p>
<dl>
<dt>
<dd> A boolean value that causes the job to be run under the login of the submitter, if supported by the joint configuration of the submit and execute machines. On Unix platforms, this defaults to True , and on Windows platforms, it defaults to False . May not be used with <code>load_profile</code> . See the HTCondor manual Platform-Specific Information chapter for administrative details on configuring Windows to support this option.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>stack_size = &lt;size in bytes&gt;</code></p>
<dl>
<dt>
<dd> This command applies only to Linux platform jobs that are not standard universe jobs. An integer number of bytes, representing the amount of stack space to be allocated for the job. This value replaces the default allocation of stack space, which is unlimited in size.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>submit_event_notes = &lt;note&gt;</code></p>
<dl>
<dt>
<dd> A string that is appended to the submit event in the job&#8217;s log file. For DAGMan jobs, the string DAG Node: and the node&#8217;s name is automatically defined for <code>submit_event_notes</code> , causing the logged submit event to identify the DAG node job submitted.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>+&lt;attribute&gt;= &lt;value&gt;</code></p>
<dl>
<dt>
<dd> A line which begins with a &#8216;+&#8217; (plus) character instructs <i>condor_submit</i> to insert the following <i>attribute</i> into the job ClassAd with the given <i>value</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <i>PRE AND POST SCRIPTS IMPLEMENTED WITH SPECIALLY-NAMED ATTRIBUTES</i></p>
<dl>
<dt>
<dd>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>+PreCmd = &lt;executable&gt; </code></p>
<dl>
<dt>
<dd> A vanilla universe job may specify that a script is to be run on the execute machine before the job, and this is called a prescript. Definition of this specifically-named attribute causes the script, identified by path and file name, to be executed. The prescript could prepare or initialize the job. Note that this definition of a prescript is different from the PRE script described in DAGMan. The prescript is not automatically transferred with the job, as the main executable is, so it must be entered into the <code>transfer_input_files</code> list, when file transfer is enabled.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>+PreArgs = &lt;argument_list&gt; </code></p>
<dl>
<dt>
<dd> Defines command line arguments for the prescript, presuming the Old argument syntax.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>+PreArguments = &lt;argument_list&gt; </code></p>
<dl>
<dt>
<dd> Defines command line arguments for the prescript, presuming the New argument syntax. An exception to the syntax is that double quotes must be escaped with a backslash instead of another double quote.</p>
<dt>
<dd> Note that if both +PreArgs and +PreArguments are specified, the +PreArguments value is used and the +PreArgs value is ignored.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>+PostCmd = &lt;executable&gt; </code></p>
<dl>
<dt>
<dd> A vanilla universe job may specify that a script is to be run on the execute machine after the job exits, and this is called a postscript. Definition of this specifically-named attribute causes the script, identified by path and file name, to be executed. The postscript is run if the job exits, but not if the job is evicted. Note that this definition of a postscript is different from the POST script described in DAGMan. The postscript is not automatically transferred with the job, as the main executable is, so it must be entered into the <code>transfer_input_files</code> list, when file transfer is enabled.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>+PostArgs = &lt;argument_list&gt; </code></p>
<dl>
<dt>
<dd> Defines command line arguments for the postscript, presuming the Old argument syntax.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>+PostArguments = &lt;argument_list&gt; </code></p>
<dl>
<dt>
<dd> Defines command line arguments for the postscript, presuming the New argument syntax. An exception to the syntax is that double quotes must be escaped with a backslash instead of another double quote mark.</p>
<dt>
<dd> Note that if both +PostArgs and +PostArguments are specified, the +PostArguments value is used and the +PostArgs value is ignored.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> If any of the prescript or postscript values are not enclosed in double quotes, they are silently ignored. </p>
<p> Below is an example of the use of starter pre and post scripts: </p>
<p> +PreCmd = &quot;my_pre&quot;<br />
 +PreArgs = &quot;pre\&quot;arg1 prea&#8217;rg2&quot;<br />
 +PostCmd = &quot;my_post&quot;<br />
 +PostArguments = &quot;post\&quot;arg1 &#8216;post&#8221;ar g2&#8217;&quot; </p>
<p> For this example PreArgs generates a first argument of pre&quot;a1&quot; and a second argument of pre&#8217;a2 . PostArguments generates a first argument of post&quot;a1 and a second argument of post&#8217;a 2 . </p>
<p> <i>MACROS AND COMMENTS</i> </p>
<p> In addition to commands, the submit description file can contain macros and comments. </p>
<p> <code>Macros</code></p>
<dl>
<dt>
<dd> Parameterless macros in the form of $(macro_name:default initial value) may be used anywhere in HTCondor submit description files to provide textual substitution at submit time. Macros can be defined by lines in the form of</dl>
<p>&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;macro_name&gt;&nbsp;<wbr>=&nbsp;<wbr>&lt;string&gt;</p>
<dl>
<dt>
<dd> Two pre-defined macros are supplied by the submit description file parser. The $(Cluster) or $(ClusterId) macro supplies the value of the ClusterId job ClassAd attribute, and the $(Process) or $(ProcId) macro supplies the value of the ProcId job ClassAd attribute. These macros are intended to aid in the specification of input/output files, arguments, etc., for clusters with lots of jobs, and/or could be used to supply an HTCondor process with its own cluster and process numbers on the command line.</p>
<dt>
<dd> The $(Node) macro is defined for parallel universe jobs, and is especially relevant for MPI applications. It is a unique value assigned for the duration of the job that essentially identifies the machine (slot) on which a program is executing. Values assigned start at 0 and increase monotonically. The values are assigned as the parallel job is about to start.</p>
<dt>
<dd> Recursive definition of macros is permitted. An example of a construction that works is the following:</dl>
<p> foo = bar<br />
 foo = snap $(foo)</p>
<dl>
<dt>
<dd> As a result, foo = snap bar .</p>
<dt>
<dd> Note that both left- and right- recursion works, so</dl>
<p> foo = bar<br />
 foo = $(foo) snap</p>
<dl>
<dt>
<dd> has as its result foo = bar snap .</p>
<dt>
<dd> The construction</dl>
<p> foo = $(foo) bar</p>
<dl>
<dt>
<dd> by itself will <i>not</i> work, as it does not have an initial base case. Mutually recursive constructions such as:</dl>
<p> B = bar<br />
 C = $(B)<br />
 B = $(C) boo</p>
<dl>
<dt>
<dd> will <i>not</i> work, and will fill memory with expansions.</p>
<dt>
<dd> A default value may be specified, for use if the macro has no definition. Consider the example</dl>
<p> D = $(E:24)</p>
<dl>
<dt>
<dd> Where E is not defined within the submit description file, the default value 24 is used, resulting in</dl>
<p> D = 24</p>
<dl>
<dt>
<dd> This is of limited value, as the scope of macro substitution is the submit description file. Thus, either the macro is or is not defined within the submit description file. If the macro is defined, then the default value is useless. If the macro is not defined, then there is no point in using it in a submit command.</p>
<dt>
<dd> To use the dollar sign character ( $ ) as a literal, without macro expansion, use</dl>
<p> $(DOLLAR)</p>
<dl>
<dt>
<dd> In addition to the normal macro, there is also a special kind of macro called a <i>substitution macro</i> that allows the substitution of a machine ClassAd attribute value defined on the resource machine itself (gotten after a match to the machine has been made) into specific commands within the submit description file. The substitution macro is of the form:</dl>
<p>&nbsp;<wbr><br />
 $$(attribute)</p>
<dl>
<dt>
<dd> As this form of the substitution macro is only evaluated within the context of the machine ClassAd, use of a scope resolution prefix TARGET. or MY. is not allowed.</p>
<dt>
<dd> A common use of this form of the substitution macro is for the heterogeneous submission of an executable:</dl>
<p> executable = povray.$$(OpSys).$$(Arch)</p>
<dl>
<dt>
<dd> Values for the OpSys and Arch attributes are substituted at match time for any given resource. This example allows HTCondor to automatically choose the correct executable for the matched machine.</p>
<dt>
<dd> An extension to the syntax of the substitution macro provides an alternative string to use if the machine attribute within the substitution macro is undefined. The syntax appears as:</dl>
<p>&nbsp;<wbr><br />
 $$(attribute:string_if_attribute_undefined)</p>
<dl>
<dt>
<dd> An example using this extended syntax provides a path name to a required input file. Since the file can be placed in different locations on different machines, the file&#8217;s path name is given as an argument to the program.</dl>
<p>&nbsp;<wbr><br />
 arguments = $$(input_file_path:/usr/foo)</p>
<dl>
<dt>
<dd> On the machine, if the attribute input_file_path is not defined, then the path /usr/foo is used instead.</p>
<dt>
<dd> A further extension to the syntax of the substitution macro allows the evaluation of a ClassAd expression to define the value. In this form, the expression may refer to machine attributes by prefacing them with the TARGET. scope resolution prefix. To place a ClassAd expression into the substitution macro, square brackets are added to delimit the expression. The syntax appears as:</dl>
<p>&nbsp;<wbr><br />
 $$([ClassAd expression])</p>
<dl>
<dt>
<dd> An example of a job that uses this syntax may be one that wants to know how much memory it can use. The application cannot detect this itself, as it would potentially use all of the memory on a multi-slot machine. So the job determines the memory per slot, reducing it by 10% to account for miscellaneous overhead, and passes this as a command line argument to the application. In the submit description file will be</dl>
<p>&nbsp;<wbr><br />
 arguments = &#8211;memory $$([TARGET.Memory * 0.9])</p>
<dl>
<dt>
<dd> To insert two dollar sign characters ( $$ ) as literals into a ClassAd string, use</dl>
<p> $$(DOLLARDOLLAR)</p>
<dl>
<dt>
<dd> The environment macro, $ENV, allows the evaluation of an environment variable to be used in setting a submit description file command. The syntax used is</dl>
<p>&nbsp;<wbr><br />
 $ENV(variable)</p>
<dl>
<dt>
<dd> An example submit description file command that uses this functionality evaluates the submitter&#8217;s home directory in order to set the path and file name of a log file:</dl>
<p>&nbsp;<wbr><br />
 log = $ENV(HOME)/jobs/logfile</p>
<dl>
<dt>
<dd> The environment variable is evaluated when the submit description file is processed.</p>
<dt>
<dd> The $RANDOM_CHOICE macro allows a random choice to be made from a given list of parameters at submission time. For an expression, if some randomness needs to be generated, the macro may appear as</dl>
<p>&nbsp;<wbr> </p>
<p>&nbsp;<wbr>$RANDOM_CHOICE(0,1,2,3,4,5,6)</p>
<dl>
<dt>
<dd> When evaluated, one of the parameters values will be chosen.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>Comments</code></p>
<dl>
<dt>
<dd> Blank lines and lines beginning with a pound sign (&#8216;#&#8217;) character are ignored by the submit description file parser.</p>
<dt>
<dd>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_submit</i> will exit with a status value of 0 (zero) upon success, and a non-zero value upon failure. </p>
<h2>Examples</h2>
<dl>
<dt>
<dd> * Submit Description File Example 1: This example queues three jobs for execution by HTCondor. The first will be given command line arguments of <i>15</i> and <i>2000</i> , and it will write its standard output to foo.out1 . The second will be given command line arguments of <i>30</i> and <i>2000</i> , and it will write its standard output to foo.out2 . Similarly the third will have arguments of <i>45</i> and <i>6000</i> , and it will use foo.out3 for its standard output. Standard error output (if any) from all three programs will appear in foo.error .</p>
<dt>
<dd></dl>
<p>#################### </p>
<p># </p>
<p>#&nbsp;<wbr>submit description file </p>
<p>#&nbsp;<wbr>Example 1: queuing multiple jobs with differing </p>
<p>#&nbsp;<wbr>command line arguments and output files. </p>
<p>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>####################&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Executable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>foo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Universe&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>standard </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Arguments&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>15 2000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Output&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>foo.out1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Error&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>foo.err1 </p>
<p>Queue&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Arguments&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>30 2000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Output&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>foo.out2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Error&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>foo.err2 </p>
<p>Queue&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Arguments&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>45 6000&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Output&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>foo.out3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Error&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>foo.err3 </p>
<p>Queue</p>
<dl>
<dt>
<dd>
<dt>
<dd> * Submit Description File Example 2: This submit description file example queues 150 runs of program <i>foo</i> which must have been compiled and linked for an Intel x86 processor running RHEL 3. HTCondor will not attempt to run the processes on machines which have less than 32 Megabytes of physical memory, and it will run them on machines which have at least 64 Megabytes, if such machines are available. Stdin, stdout, and stderr will refer to in.0 , out.0 , and err.0 for the first run of this program (process 0). Stdin, stdout, and stderr will refer to in.1 , out.1 , and err.1 for process 1, and so forth. A log file containing entries about where and when HTCondor runs, takes checkpoints, and migrates processes in this cluster will be written into file foo.log .</p>
<dt>
<dd></dl>
<p>####################&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>#&nbsp;<wbr>Example 2: Show off some fancy features including </p>
<p>#&nbsp;<wbr>use of pre-defined macros and logging.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>####################&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Executable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>foo&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Universe&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>standard </p>
<p>Requirements&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>OpSys&nbsp;<wbr>==&nbsp;<wbr>&quot;LINUX&quot;&nbsp;<wbr>&amp;&amp;&nbsp;<wbr>Arch&nbsp;<wbr>==&quot;INTEL&quot; </p>
<p>Rank&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>Memory&nbsp;<wbr>&gt;=&nbsp;<wbr>64 </p>
<p>Request_Memory&nbsp;<wbr>=&nbsp;<wbr>32 Mb </p>
<p>Image_Size&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>28 Mb </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Error&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>err.$(Process)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Input&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>in.$(Process)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Output&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>out.$(Process)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Log&nbsp;<wbr>=&nbsp;<wbr>foo.log&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Queue 150</p>
<dl>
<dt>
<dd>
<dt>
<dd> * Submit Description File Example 3: This example targets the <i>/bin/sleep</i> program to run only on a platform running a RHEL 6 operating system. The example presumes that the pool contains machines running more than one version of Linux, and this job needs the particular operating system to run correctly.</p>
<dt>
<dd></dl>
<p>####################&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>#&nbsp;<wbr>Example 3: Run on a RedHat 6 machine </p>
<p>#&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>####################&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Universe&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>vanilla </p>
<p>Executable&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>/bin/sleep </p>
<p>Arguments&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>30 </p>
<p>Requirements&nbsp;<wbr>=&nbsp;<wbr>(OpSysAndVer&nbsp;<wbr>==&nbsp;<wbr>&quot;RedHat6&quot;) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Error&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>err.$(Process)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Input&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>in.$(Process)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Output&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>out.$(Process)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Log&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>=&nbsp;<wbr>sleep.log&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> </p>
<p>Queue</p>
<dl>
<dt>
<dd>
<dt>
<dd> * Command Line example: The following command uses the <code>-append</code> option to add two commands before the job(s) is queued. A log file and an error log file are specified. The submit description file is unchanged.</dl>
<p> condor_submit -a &quot;log = out.log&quot; -a &quot;error = error.log&quot; mysubmitfile</p>
<dl>
<dt>
<dd> Note that each of the added commands is contained within quote marks because there are space characters within the command.</p>
<dt>
<dd>
<dt>
<dd> * periodic_remove example: A job should be removed from the queue, if the total suspension time of the job is more than half of the run time of the job.</p>
<dt>
<dd> Including the command</dl>
<p>periodic_remove&nbsp;<wbr>=&nbsp;<wbr>CumulativeSuspensionTime&nbsp;<wbr>&gt;&nbsp;<wbr> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>((RemoteWallClockTime &#8211; CumulativeSuspensionTime)&nbsp;<wbr>/&nbsp;<wbr>2.0)</p>
<dl>
<dt>
<dd> in the submit description file causes this to happen.</p>
<dt>
<dd></dl>
<h2>General Remarks</h2>
<dl>
<dt>
<dd> * For security reasons, HTCondor will refuse to run any jobs submitted by user root (UID = 0) or by a user whose default group is group wheel (GID = 0). Jobs submitted by user root or a user with a default group of wheel will appear to sit forever in the queue in an idle state.</p>
<dt>
<dd>
<dt>
<dd> * All path names specified in the submit description file must be less than 256 characters in length, and command line arguments must be less than 4096 characters in length; otherwise, <i>condor_submit</i> gives a warning message but the jobs will not execute properly.</p>
<dt>
<dd>
<dt>
<dd> * Somewhat understandably, behavior gets bizarre if the user makes the mistake of requesting multiple HTCondor jobs to write to the same file, and/or if the user alters any files that need to be accessed by an HTCondor job which is still in the queue. For example, the compressing of data or output files before an HTCondor job has completed is a common mistake.</p>
<dt>
<dd>
<dt>
<dd> * To disable checkpointing for Standard Universe jobs, include the line:</dl>
<p>+WantCheckpoint&nbsp;<wbr>=&nbsp;<wbr>False</p>
<dl>
<dt>
<dd> in the submit description file before the queue command(s).</dl>
<h2>See Also</h2>
<p> HTCondor User Manual </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
