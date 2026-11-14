---
title: "jsv(1)"
name: "jsv"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jsv/"
description: "JSV – xxQS_NAMExx Job Submission Verifier"
---

<h2 class="name">NAME</h2>
<p> JSV &#8211; xxQS_NAMExx Job Submission Verifier </p>
<h2>DESCRIPTION</h2>
<p> JSV is an abbreviation for Job Submission Verifier. A JSV is a script or binary that can be used to verify, modify or reject a job during job submission. </p>
<p> JSVs will be triggered by submit clients like <i>qsub</i>, <i>qrsh</i>, <i>qsh</i> and <i>qmon</i> on submit hosts (Client JSV), or they verify incoming jobs on the master host (Server JSV), or both.</p>
<h2>CONFIGURATION</h2>
<p> JSVs can be configured in various locations. Either a <code>jsv_url</code> can be provided with the <code>-jsv</code> submit parameter during job submission, a corresponding switch can be added to one of the <code>sge_request</code> files, or a <code>jsv_url</code> can be configured in the global cluster configuration of the xxQS_NAMExx installation. </p>
<p> All defined JSV instances will be executed in following order: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1)&nbsp;qsub -jsv &#8230;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;2)&nbsp;$cwd/.sge_request<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;3)&nbsp;$HOME/.sge_request<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;4)&nbsp;$SGE_ROOT/$SGE_CELL/common/sge_request<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;5)&nbsp;Global configuration&nbsp; </p>
<p> The Client JSVs (1-3) can be defined by xxQS_NAMExx end users, whereas the client JSV defined in the global sge_request file (4) and the server JSV (5) can only be defined by the xxQS_NAMExx administrators. </p>
<p> Due to the fact that (4) and (5) are defined and configured by xxQS_NAMExx administrators and executed as the last JSV instances in the sequence of JSV scripts, an administrator has a way to enforce certain policies for a cluster. However, note that (4) may be over-ridden trivially with <code>qsub -clear</code>. </p>
<p> As soon as one JSV instance rejects a job the whole process of verification is stopped and the end user will get a corresponding error message that the submission of the job has failed. </p>
<p> If a JSV accepts a job, or accepts a job after it applied several modifications, then the following JSV instance will get the job parameters including all modifications as input for the verification process. This is done as long as either the job is accepted or rejected. </p>
<p> Find more information on how to use Client JSVs in and for Server JSVs in</p>
<h2>LIFETIME</h2>
<p> A Client or Server JSV is started as own process. This process communicates either with a xxQS_NAMExx client process or the master daemon by exchanging commands, job parameters, and other data via stdin/stdout streams. </p>
<p> Client JSV instances are started by client applications before a job is sent to qmaster. This instance does the job verification for the job to be submitted. After that verification the JSV process is stopped. </p>
<p> Server JSV instances are started for each worker thread part of the qmaster process. (For version 6.2 of xxQS_NAMExx this means that two processes are started.) Each of those processes has to verify job parameters for multiple jobs as long as the master is running, the underlying JSV configuration is not changed, and no error occurs.</p>
<h2>TIMEOUT</h2>
<p> The timeout is a modifiable value that will measure the response time of either the client or server JSV. In the event that the response time of the JSV is longer than timeout value specified, this will result in the JSV being re-started. The server JSV timeout value is specified through the qmaster parameter <code>jsv_timeout</code>. The client JSV timeout value is set through the environment variable <code>SGE_JSV_TIMEOUT</code>. The default value is 10 seconds, and this value must be greater than 0. If the timeout has been reached, the JSV will only try to re-start once, and if the timeout is reached again, an error will occur.</p>
<h2>THRESHOLD</h2>
<p> The threshold value is defined as a qmaster parameter <code>jsv_threshold</code>. This value measures the time for a server job verification. If this time exceeds the defined threshold then additional logging will appear in the master message file at the INFO level. This value is specified in milliseconds and has a default value of 5000. If a value of 0 is defined then this means all jobs will be logged in the message file.</p>
<h2>PROTOCOL</h2>
<p> After a JSV script or binary is started it will get commands through its stdin stream, and it has to respond with certain commands on the stdout stream. Data sent via the stderr stream of a JSV instance is ignored. Each command which is sent to/by a JSV script has to be terminated by a newline character (&#8216;<code>
</code>&#8216;), whereas newline characters are not allowed in the whole command string itself. </p>
<p> In general, commands which are exchanged between a JSV and client/qmaster have following format. Commands and arguments are case sensitive. Find the EBNF command description below. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>command</i>&nbsp;:=&nbsp;<i>command_name</i>&nbsp;&#8216;&nbsp;&#8216;&nbsp;{&nbsp;<i>argument</i>&nbsp;&#8216;&nbsp;&#8216;&nbsp;} </p>
<p> A <i>command</i> starts with a <i>command_name</i> followed by a space character and a space-separated list of <i>argument</i>s.</p>
<h2>PROTOCOL (JSV side)</h2>
<p> The following <i>command</i>s have to be implemented by a JSV script so that it conforms to version 1.0 of the JSV protocol, which was first implemented in xxQS_NAMExx 6.2u2:</p>
<dl>
<dt><i>begin_command</i> := <code>BEGIN</code></p>
<dd> After a JSV instance has received all the <i>env_command</i>s and <i>param_command</i>s of a job which should be verified, the client/qmaster will trigger the verification process by sending one <i>begin_command</i>. After that it will wait for <i>param_command</i>s and <i>env_command</i>s which are sent back from the JSV instance to modify the job specification. As part of the verification process a JSV script or binary has to use the <i>result_command</i> to indicate that the verification process is finished for a job.</p>
<dt><i>env_command</i> := <code>ENV</code> &#8216; &#8216; <i>modifier</i> &#8216; &#8216; <i>name</i> &#8216; &#8216; <i>value</i></p>
<dd>
<dt><i>modifier</i> := <code>ADD</code> | <code>MOD</code> | <code>DEL</code></p>
<dd> The <i>env_command</i> is an optional command which has only to be implemented by a JSV instance if the <i>send_data_command</i> is sent by this JSV before a <i>started_command</i> was sent. Only in that case, the client or master will use one or multiple <i>env_command</i>s to pass the environment variables (<i>name</i> and <i>value</i>) to the JSV instance to be exported to the job environment when the job is started. Client and qmaster will only send <i>env_command</i>s with the modifier <code>ADD</code>. </p>
<p> JSV instances modify the set of environment variables by sending back <i>env_command</i>s, and by using the <i>modifier</i>s <code>ADD</code>, <code>MOD</code>, and <code>DEL</code>.</p>
<dt><i>param_command</i> := <code>PARAM</code> &#8216; &#8216; <i>param_parameter</i> &#8216; &#8216; <i>value</i></p>
<dd>
<dt><i>param_parameter</i> := <i>submit_parameter</i> | <i>pseudo_parameter</i></p>
<dd> The <i>param_command</i> has two additional arguments which are separated by space characters. The first argument is either a <i>submit_parameter</i> as specified in or it is a <i>pseudo_parameter</i>, as documented below. The second parameter is the <i>value</i> of the corresponding <i>param_parameter</i>. </p>
<p> Multiple <i>param_command</i>s will be sent to a JSV instance after the JSV has sent a <i>started_command</i>. The sum of all <i>param_command</i>s sent represents a job specification of the job which should be verified. </p>
<p> <i>submit_parameter</i>s are, for example, <code>b</code> (similar to the <code>qsub</code> <code>-b</code> switch), or <code>masterq</code> (similar to <code>qsub</code> <code>-masterq</code> switch). Find a complete list of <i>submit_parameter</i>s in the man page. Please note that the <i>param_parameter</i> name and the corresponding <i>value</i> format is not equivalent to the <code>qsub</code> switch name and its argument format in all cases. E.g. the <code>qsub</code> <code>-pe</code> parameters will by available as a set of parameters with the name <i>pe_name</i>, <i>pe_min</i>, <i>pe_max</i> and the switch combination <code>-soft -l</code> will be passed to JSV scripts as <code>l_soft</code> parameter. For details concerning these differences consult also the man page.</p>
<dt><i>start_command</i> := <code>START</code></p>
<dd> The <i>start_command</i> has no additional arguments. This command indicates that a new job verification should be started. It is the first command which will be sent to JSV script after it has been started and it will initiate each new job verification. A JSV instance might trash cached values which are still stored due to a previous job verification. The application which sends the <i>start_command</i> will wait for a <i>started_command</i> before it continues.</p>
<dt><i>quit_command</i> := <code>QUIT</code></p>
<dd> The <i>quit_command</i> has no additional arguments. If this command is sent to a JSV instance then it should terminate itself immediately.</dl>
<h2>PROTOCOL (client/qmaster side)</h2>
<p> A JSV script or binary can send a set of commands to a client/qmaster process to indicate its state in the communication process, to change the job specification of a job which should be verified, and to report messages or errors. Below you can find the commands which are understood by the client/qmaster which implements version 1.0 of the communication protocol introduced in xxQS_NAMExx 6.2u2:</p>
<dl>
<dt><i>error_command</i> := <code>ERROR</code> <i>message</i></p>
<dd> Any time a JSV script encounters an error it might report it to the client/qmaster. If the error happens during a job verification the job which is currently verified will be rejected. The JSV binary or script will also be restarted before it gets a new verification task.</p>
<dt><i>log_command</i> := <code>LOG</code> <i>log_level</i></p>
<dd>
<dt><i>log_level</i> := <code>INFO</code> | <code>WARNING</code> | <code>ERROR</code></p>
<dd> <i>log_command</i>s can be used whenever the client or qmaster expects input from a JSV instance. This command can be used in client JSVs to send information to the user submitting the job. In client JSVs all messages, independent of the <i>log_level</i>, will be printed to the stdout stream of the submit client. If a server JSV receives a <i>log_command</i> it will add the received message to the message file, respecting the specified <i>log_level</i>. Please note that <i>message</i> might contain spaces, but no newline characters.</p>
<dt><i>param_command</i> (find definition above)</p>
<dd> By sending <i>param_command</i>s, a JSV script can change the job specification of the job which should be verified. If a JSV instance later on sends a <i>result_command</i> which indicates that a JSV instance should be accepted with corrections, then the values provided with these <i>param_command</i>s will be used to modify the job before it is accepted by the xxQS_NAMExx system.</p>
<dt><i>result_command</i> := <code>RESULT</code> <i>result_type</i> [ <i>message</i> ]</p>
<dd>
<dt><i>result_type</i> := <code>ACCEPT</code> | <code>CORRECT</code> | <code>REJECT</code> | <code>REJECT_WAIT</code></p>
<dd> After the verification of a job is done, a JSV script or binary has to send a <i>result_command</i> which indicates what should happen with the job. If the <i>result_type</i> is <code>ACCEPTED</code> the job will be accepted as it was initially submitted by the end user. All <i>param_command</i>s and <i>env_command</i>s which might have been sent before the <i>result_command</i> are ignored in this case. The <i>result_type</i> <code>CORRECT</code> indicates that the job should be accepted after all modifications sent via <i>param_command</i>s and <i>env_command</i> are applied to the job. <code>REJECT</code> and <code>REJECT_WAIT</code> cause the client or qmaster instance to reject the job.</p>
<dt><i>send_data_command</i> := <code>SEND</code> <i>data_name</i></p>
<dd>
<dt><i>data_name</i> := <code>ENV</code></p>
<dd> If a client/qmaster receives a <i>send_env_command</i> from a JSV instance before a <i>started_command</i> is sent, then it will not only pass job parameters with <i>param_command</i>s, but also <i>env_command</i>s which provide the JSV with the information about which environment variables will be exported to the job environment if the job is accepted and started later on. </p>
<p> The job environment is not passed to JSV instances by default because the job environment of the end user might contain data which might be interpreted wrongly in the JSV context, and might therefore cause errors or security issues.</p>
<dt><i>started_command</i> := <code>STARTED</code></p>
<dd> By sending the <i>started_command</i> a JSV instance indicates that it is ready to receive <i>param_command</i>s and <i>env_command</i>s for a new job verification. It will only receive <i>env_command</i>s if it sends a <i>send_data_command</i> before the <i>started_command</i>.</dl>
<h2>PSEUDO PARAMETERS</h2>
<dl>
<dt><code>CLIENT</code></p>
<dd> The corresponding value for the <code>CLIENT</code> parameter is either <code>qmaster</code> or the name of a submit client like <code>qsub</code>, <code>qsh</code>, <code>qrsh</code>, <code>qlogin</code>, and so on. This parameter value can&#8217;t be changed by JSV instances. It will always be sent as part of a job verification.</p>
<dt><code>CMDARGS</code></p>
<dd> Number of arguments which will be passed to the job script or command when the job execution is started. It will always be sent as part of a job verification. If no arguments should be passed to the job script or command it will have the value 0. This parameter can be changed by JSV instances. If the value of <code>CMDARGS</code> is bigger than the number of available <code>CMDARG</code><i>n</i> parameters, then the missing parameters will be automatically passed as empty parameters to the job script.</p>
<dt><code>CMDARG</code><i>n</i></p>
<dd> Individual command arguments, where <i>n</i> is an integer between 0 and <code>CMDARGS</code>-1.</p>
<dt><code>CMDNAME</code></p>
<dd> Either the path to the script, the command name for binary submission, <code>STDIN</code> for standard input, or <code>NONE</code> in the case of an interactive job. It will always be sent as part of a job verification.</p>
<dt><code>CONTEXT</code></p>
<dd> Either <code>client</code>, if the JSV which receives this <i>param_command</i> was started by a command-line client like <i>qsub</i>, or <i>qsh</i>, or <code>master</code> if it was started by the <i>sge_qmaster</i> process. It will always be sent as part of a job verification. This parameter value can&#8217;t be changed by JSV instances.</p>
<dt><code>GROUP</code></p>
<dd> Defines the primary group of the user who tries to submit the job which should be verified. This parameter cannot be changed but is always sent as part of the verification process. The user name is passed as a parameter with the name <code>USER</code>.</p>
<dt><code>JOB_ID</code></p>
<dd> Not available in the client context (see <code>CONTEXT</code>). Otherwise it contains the job number of the job which will be submitted to Grid Engine when the verification process is successful. <code>JOB_ID</code> is an optional parameter which can&#8217;t be changed by JSV instances.</p>
<dt><code>USER</code></p>
<dd> User name of the user who tries to submit the job which should be verified. Cannot be changed but is always sent as part of the verification process. The group name is passed as a parameter with the name <code>GROUP</code>.</p>
<dt><code>VERSION</code></p>
<dd> <code>VERSION</code> will always be sent as part of a job verification process and it will always be the first parameter which is sent. It will contain a version number of the format <i>major</i><code>.</code><i>minor</i>. In version 6.2u2 and higher the value will be <code>1.0</code>, or higher if the protocol is changed in the future. The value of this parameter can&#8217;t be changed.</dl>
<h2>CAVEATS</h2>
<p> See for advice concerning shell script JSVs.</p>
<h2>EXAMPLE</h2>
<p> Here is an example for the communication of a client with a JSV instance when the following job is submitted: </p>
<pre>
&gt; qsub -pe p 3 -hard -l a=1,b=5 -soft -l q=all.q $SGE_ROOT/examples/jobs/sleeper.sh
</pre>
<p> Data in the first column are sent from the client/qmaster to the JSV instance. Data contained in the second column are sent from the JSV script to the client/qmaster. Newline characters which terminate each line in the communication protocol are omitted. </p>
<pre>
   START
                                        SEND ENV
                                        STARTED
   PARAM VERSION 1.0
   PARAM CONTEXT client
   PARAM CLIENT qsub
   PARAM USER ernst
   PARAM GROUP staff
   PARAM CMDNAME /sge_root/examples/jobs/sleeper.sh
   PARAM CMDARGS 1
   PARAM CMDARG0 12 
   PARAM l_hard a=1,b=5
   PARAM l_soft q=all.q
   PARAM M user [at] hostname
   PARAM N Sleeper
   PARAM o /dev/null
   PARAM pe_name pe1
   PARAM pe_min 3
   PARAM pe_max 3
   PARAM S /bin/sh
   BEGIN
                                        RESULT STATE ACCEPT
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
