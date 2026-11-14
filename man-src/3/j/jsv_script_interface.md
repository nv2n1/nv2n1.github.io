---
title: "jsv_script_interface(3)"
name: "jsv_script_interface"
section: "3"
letter: "j"
url: "/docs/linux/man/3-jsv_script_interface/"
description: "jsv_is_param, jsv_get_param, jsv_del_param, jsv_sub_is_param, jsv_sub_get_param, jsv_sub_add_param, jsv_sub_del_param, jsv_is_env, jsv_get_env, jsv_add_env, jsv_mod_env, jsv_del_env, jsv_accept, js..."
---

<h2 class="name">NAME</h2>
<p> jsv_is_param, jsv_get_param, jsv_del_param, jsv_sub_is_param, jsv_sub_get_param, jsv_sub_add_param, jsv_sub_del_param, jsv_is_env, jsv_get_env, jsv_add_env, jsv_mod_env, jsv_del_env, jsv_accept, jsv_correct, jsv_reject, jsv_reject_wait, jsv_show_params, jsv_show_envs, jsv_log_info, jsv_log_warning, jsv_log_error, jsv_main, jsv_logging_enabled &#8211; xxQS_NAMExx Job Submission Verifier Scripting Interface </p>
<h2>SYNOPSIS</h2>
<pre>
<code>jsv_clear_params</code>();
</pre>
<pre>
<code>jsv_is_param</code>(<i>param_name</i>);
</pre>
<pre>
<code>jsv_get_param</code>(<i>param_name</i>);
</pre>
<pre>
<code>jsv_set_param</code>(<i>param_name</i>, <i>param_value</i>);
</pre>
<pre>
<code>jsv_del_param</code>(<i>param_name</i>);
</pre>
<pre>
<code>jsv_sub_is_param</code>(<i>param_name</i>, <i>variable_name</i>);
</pre>
<pre>
<code>jsv_sub_get_param</code>(<i>param_name</i>, <i>variable_name</i>);
</pre>
<pre>
<code>jsv_sub_add_param</code>(<i>param_name</i>, <i>variable_name</i>, <i>variable_value</i>);
</pre>
<pre>
<code>jsv_sub_del_param</code>(<i>param_name</i>, <i>variable_name</i>);
</pre>
<pre>
<code>jsv_clear_envs</code>();
</pre>
<pre>
<code>jsv_is_env</code>(<i>variable_name</i>);
</pre>
<pre>
<code>jsv_get_env</code>(<i>variable_name</i>);
</pre>
<pre>
<code>jsv_add_env</code>(<i>variable_name</i>, <i>variable_value</i>);
</pre>
<pre>
<code>jsv_mod_env</code>(<i>variable_name</i>, <i>variable_value</i>);
</pre>
<pre>
<code>jsv_del_env</code>(<i>variable_name</i>);
</pre>
<pre>
<code>jsv_accept</code>(<i>message</i>);
</pre>
<pre>
<code>jsv_correct</code>(<i>message</i>);
</pre>
<pre>
<code>jsv_reject</code>(<i>message</i>);
</pre>
<pre>
<code>jsv_reject_wait</code>(<i>message</i>);
</pre>
<pre>
<code>jsv_show_params</code>();
</pre>
<pre>
<code>jsv_show_envs</code>();
</pre>
<pre>
<code>jsv_log_info</code>(<i>message</i>);
</pre>
<pre>
<code>jsv_log_warning</code>(<i>message</i>);
</pre>
<pre>
<code>jsv_log_error</code>(<i>message</i>);
</pre>
<pre>
<code>jsv_main</code>();
</pre>
<pre>
<code>jsv_send_env</code>();
</pre>
<pre>
<code>jsv_on_start</code>();
</pre>
<pre>
<code>jsv_on_verify</code>();
</pre>
<h2>DESCRIPTION</h2>
<p> The functions documented here implement the server side of the JSV protocol as described in (where &quot;server&quot; applies to both client- and server-side JSVs). These functions are available in Bourne shell (preferably using <i><a href="/docs/linux/man/1-bash/">bash</a></i>(1) for greater efficiency), TCL, Perl, or Python scripts after sourcing/including the files jsv_inlcude.sh, jsv_include.tcl, JSV.pm, or JSV.py. The files and corresponding JSV script templates are located in the directory <i>$SGE_ROOT/util/resources/jsv</i>. There is also a Java implementation which has a different structure, with Javadoc documentation normally in <i>$SGE_ROOT/doc/javadocs/jjsv</i>, and example files <i>SimpleJsv.java</i> and <i>jjsv.sh</i> in <i>$SGE_ROOT/util/resources/jsv</i>. </p>
<p> Note that Bourne shell server JSVs are discouraged because any problems with unintended expansion of job parameters represent a security hazard (with the qmaster running as the sgeadmin user). Also they may be relatively slow, and constitute a bottleneck in high-throughput clusters. However, shell JSVs may be faster using even compared with a generally faster shell, since fewer external commands are invoked. </p>
<p> In the descriptions of routines here, a calling sequence like</p>
<dl>
<dt>
<dd> <code>function</code>(<i>arg1</i>, <i>arg2</i>)</dl>
<p> should be interpreted for Bourne shell and Tcl scripts as</p>
<dl>
<dt>
<dd> <code>function</code> <i>arg1</i> <i>arg2</i></dl>
<h3>jsv_clear_params()</h3>
<p> This function clears all received job parameters that were stored during the last job verification process.</p>
<h3>jsv_clear_envs()</h3>
<p> This function clears all received job environment variables that were stored during the last job verification process.</p>
<h3>jsv_show_params()</h3>
<p> A call of this function reports all known job parameters to the counterpart of this script (client or master daemon thread). These parameters will be reported as info messages and appear either in the stdout stream of the client or in the message file of the master process.</p>
<h3>jsv_show_envs()</h3>
<p> This function reports all known job environment variables to the counterpart of this script (client or master daemon thread). They will be reported as info messages and appear in the stdout stream of the client or in the message file of the master process.</p>
<h3>jsv_is_param(<i>param_name</i>)</h3>
<p> This function returns whether or not a specific job parameter is available for the job which is currently being verified. Either the string <code>true</code> or <code>false</code> will be returned. The availability/absence of a job parameter does not mean that the corresponding command line switch was used/not used. </p>
<p> The values allowed for <i>param_name</i> are listed below. Find additional information in describing the availability and value format. Job parameters written in capital letters are pseudo parameters. A detailed description for them can be found in Note that </p>
<p> The following parameters directly reflect arguments of the same name supplied to the submission command (<i>qsub</i> etc.) or corresponding values specified with <i>qmon</i>:<br />
 <code>A</code>, <code>a</code>, <code>ar</code>, <code>b</code>, <code>ckpt</code>, <code>dl</code>, <code>e</code>, <code>h</code>, <code>hold_jid</code>, <code>hold_jid_ad</code>, <code>i</code>, <code>j</code>, <code>js</code>, <code>M</code>, <code>m</code>, <code>masterq</code>, <code>N</code>, <code>notify</code>, <code>o</code>, <code>P</code>, <code>p</code>, <code>R</code>, <code>r</code>, <code>S</code>, <code>shell</code>, <code>tc</code>, <code>w</code><br />
 Other parameters are related to the submission command arguments as follows:</p>
<dl>
<dt><code>ac</code></p>
<dd> The the job context. The outcome of the evaluation of all <code>-ac</code>, <code>-dc</code>, and <code>-sc</code> options is passed as a parameter with the name <code>ac</code>, whose value is a comma-separated list of variable/value pairs;</p>
<dt><code>binding_strategy</code>,&nbsp;<code>binding_type</code>,&nbsp;<code>binding_amount</code>,&nbsp;<code>binding_step</code>,&nbsp;<code>binding_socket</code>,&nbsp;<code>binding_core</code>,&nbsp;<code>binding_exp_n</code>,&nbsp;<code>binding_exp_socket</code><i>id</i>,&nbsp;<code>binding_exp_core</code><i>id</i></p>
<dd> The values passed to the <code>-binding</code> parameter are passed as multiple parameters to JSV instances. <code>binding_strategy</code> represents the strategy to be used and is one of: <code>linear</code>, <code>striding</code> or <code>explicit</code>. <code>binding_type</code> is the instance that should do the binding, one of: <code>env</code>, <code>set</code> or <code>pe</code>. <code>binding_socket</code> and <code>binding_core</code> are socket/core values whereas <code>binding_step</code> is the step size (used only for striding binding). The length of the socket/core value list of the explicit binding is reported as <code>binding_exp_n</code>. The <i>id</i> part of <code>binding_exp_socket</code><i>id</i> and <code>binding_exp_core</code><i>id</i> will be replaced by the position of the socket/core pair within the explicit binding list (0 &lt;= <i>id</i> &lt; <code>binding_exp</code><i>_n</i>). The first socket/core pair of the explicit binding will be reported with the parameter names <code>binding_exp_socket0</code> and <code>binding_exp_core0</code>. Values that do not apply for the specified binding will not be reported to JSV. E.g. <code>binding_step</code> will only be reported for the striding binding and all <code>binding_exp_&#8230;</code> values will only be passed if explicit binding was specified.</p>
<dt><code>c_interval</code></p>
<dd> Checkpoint interval, specified as a numeric value with <code>-c</code>;</p>
<dt><code>c_occasion</code></p>
<dd> Checkpoint &quot;occasion_specifier&quot; <code>-c</code>. (<code>n</code>, <code>s</code>, <code>m</code>, or <code>x</code>) specified with <code>-c</code>;</p>
<dt><code>cwd</code></p>
<dd> Working directory, possibly specified with <code>-cwd</code> or <code>-wd</code>;</p>
<dt><code>display</code></p>
<dd> Reflects the <code>-display</code> submit argument and also sets job environment variable DISPLAY to the same value;</p>
<dt><code>l_hard</code></p>
<dd> <code>-l</code> or <code>-hard</code> followed by <code>-l</code>;</p>
<dt><code>l_soft</code></p>
<dd> <code>-soft</code> followed by <code>-l</code>;</p>
<dt><code>pe_name</code>, <code>pe_min</code>, <code>pe_max</code></p>
<dd> The PE name and range limits specified with <code>-pe</code>;</p>
<dt><code>q_hard</code></p>
<dd> <code>-q</code>, or <code>-hard</code> followed by <code>-q</code>;</p>
<dt><code>q_soft</code></p>
<dd> <code>-soft</code> followed by <code>-q</code>.</dl>
<p> See for explanation of the following pseudo parameters: <code>CLIENT</code>, <code>CMDNAME</code>, <code>CMDARGS</code>, <code>CMDARG</code><i>i</i>, <code>CONTEXT</code>, <code>GROUP</code>, <code>JOB_ID</code>, <code>USER</code>, <code>VERSION</code>.</p>
<h3>jsv_get_param(<i>param_name</i>)</h3>
<p> This function returns the value of a specific job parameter <i>param_name</i>. </p>
<p> This value is only available if the function <code>jsv_is_param</code>() returns <code>true</code>. Otherwise an empty string is returned. </p>
<p> Find a list of allowed parameter names in the section for the function <code>jsv_is_param</code>().</p>
<h3>jsv_set_param(<i>param_name</i>, <i>param_value</i>)</h3>
<p> This function changes the job parameter <i>param_name</i> to the value <i>param_value</i>. </p>
<p> If <i>param_value</i> is an empty string then the corresponding job parameter will be deleted, similarly to the function <code>jsv_del_param</code>(). As a result, the job parameter is not available, as if the corresponding command line switch was not specified during job submission. </p>
<p> For boolean parameters that only accept the values <code>yes</code> or <code>no</code> it is not allowed to pass an empty string as <i>param_value. </p>
<p> Also for the parameters </i><code>c</code> and <code>m</code> it is not allowed to use empty strings. Details can be found in</p>
<h3>jsv_del_param(<i>param_name</i>)</h3>
<p> This function deletes the job parameter <i>param_name</i>. </p>
<p> Find a list of allowed parameter names in the section for the function <code>jsv_is_param</code>().</p>
<h3>jsv_sub_is_param(<i>param_name</i>, <i>variable_name</i>)</h3>
<p> Some job parameters are lists that can contain multiple variables with an optional value. </p>
<p> This function returns <code>true</code> if a job&#8217;s parameters contain the list-valued <i>param_name</i>, with <i>variable_name</i> in the list; otherwise it returns <code>false</code>. <code>false</code> might also indicate that the parameter list itself is not available. Use the function <code>jsv_is_param</code>() to check if the parameter list is not available. </p>
<p> The following parameters are list parameters. The second column describes the corresponding variable names to be used. The third column contains a dash (-) if there is no value (<i>variable_value</i>) allowed with the function <code>jsv_sub_add_param</code>() or <code>jsv_sub_get_param</code>() will return always an empty string. A question mark (?) shows that the value is optional. </p>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>param_name</code> </td>
<td> <code>description of variable_name</code> </td>
<td> <code>variable_value</code>
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>ac </td>
<td> job context variable name </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>hold_jid </td>
<td> job identifier </td>
<td> &#8211;
</td>
</tr>
<tr VALIGN=top>
<td>hold_jid_id </td>
<td> array job identifier </td>
<td> &#8211;
</td>
</tr>
<tr VALIGN=top>
<td>l_hard </td>
<td> complex attribute name </td>
<td> ?
</td>
</tr>
<tr VALIGN=top>
<td>l_soft </td>
<td> complex attribute name </td>
<td> ?
</td>
</tr>
<tr VALIGN=top>
<td>M </td>
<td> mail address </td>
<td> &#8211;
</td>
</tr>
<tr VALIGN=top>
<td>masterq </td>
<td> cluster queue name or </td>
<td> &#8211;
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;</td>
<td> queue instance name </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>q_hard </td>
<td> cluster queue name or </td>
<td> &#8211;
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;</td>
<td> queue instance name<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> </td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>q_soft </td>
<td> cluster queue name or </td>
<td> &#8211;
</td>
</tr>
<tr VALIGN=top>
<td>
&nbsp;</td>
<td> queue instance name </td>
<td>
</td>
</tr>
</table>
</table>
<h3>jsv_sub_get_param(<i>param_name</i>, <i>variable_name</i>)</h3>
<p> Some job parameters are lists that can contain multiple variables<br />
 with an optional value. </p>
<p> This function returns the value of a variable <i>variable_name</i> in the parameter list <i>param_name</i>. For sub list elements that have no value an empty string will be returned. </p>
<p> Find a list of allowed parameter names (<i>param_name</i>) and variable names (<i>variable_name</i>) in the section for the function <code>jsv_sub_is_param</code>().</p>
<h3>jsv_sub_add_param(<i>param_name</i>, <i>variable_name</i>, <i>variable_value</i>)</h3>
<p> Some job parameters are lists that can contain multiple variables with an optional value. </p>
<p> This function either adds a new variable with a new value or it modifies the value if the variable is already in the list. <i>variable_value</i> is optional, and if it is not supplied the variable has no value. </p>
<p> Find a list of allowed parameter names (<i>param_name</i>) and variable names (<i>variable_name</i>) in the section for the function <code>jsv_sub_is_param</code>().</p>
<h3>jsv_sub_del_param(<i>param_name</i>, <i>variable_name</i>)</h3>
<p> Some job parameters are lists which can contain multiple variables with an optional value. </p>
<p> This function deletes a variable <i>variable_name</i> and, if available, the corresponding value. If <i>variable_name</i> is not available in the job parameter then the command will be ignored. </p>
<p> Find a list of allowed parameter names (<i>param_name</i>) and variable names (<i>variable_name </i>) in the section for the function <code>jsv_sub_is_param</code>().</p>
<h3>jsv_is_env(<i>variable_name</i>)</h3>
<p> If the function returns <code>true</code>, then the job environment variable with the name <i>variable_name</i> exists in the job currently being verified, and <code>jsv_get_env</code>() can be used to retrieve the value of that variable. If the function returns <code>false</code>, then the job environment variable does not exist.</p>
<h3>jsv_get_env(<i>variable_name</i>)</h3>
<p> This function returns the value of a job environment variable <i>variable_name</i>. </p>
<p> This variable has to be passed with the <i>qsub</i> command line switch <code>-v</code> or <code>-V</code>, and passing of environment variable data to JSV scripts has to be enabled. Environment variable data are passed when the function <code>jsv_send_env</code>() is called in the callback function <code>jsv_on_start</code>(). </p>
<p> If the variable does not exist, or if environment variable information is not available, then an empty string will be returned.</p>
<h3>jsv_add_env(<i>variable_name</i>, <i>variable_value</i>)</h3>
<p> This function adds an additional environment variable to the set of variables that will exported to the job when it is started. As a result the <i>variable_name</i> and <i>variable_value</i> become available, as if <code>-v</code> Or <code>-V</code> was specified during job submission. </p>
<p> <i>variable_value</i> is optional. If an empty string is passed, then the variable is defined without a value. </p>
<p> If <i>variable_name</i> already exists in the set of job environment variables, the corresponding value will be replaced by <i>variable_value</i>, as if the function <code>jsv_mod_env</code>() was used. If an empty string is passed then the old value will be deleted. </p>
<p> To delete an environment variable, the function <code>jsv_del_env</code>() has to be used.</p>
<h3>jsv_mod_env(<i>variable_name</i>, <i>variable_value</i>)</h3>
<p> This function modifies an existing environment variable that is in the set of variables which will exported to the job when it is started. As a result, the <i>variable_name</i> and <i>variable_value</i> will be available as if <code>-v</code> Or <code>-V</code> was specified during job submission. </p>
<p> <i>variable_value</i> is optional. If an empty string is passed, then the variable is defined without a value. </p>
<p> If <i>variable_name</i> does not already exist in the set of job environment variables, then the corresponding name and value will be added as if the function <code>jsv_add_env</code>() was used. </p>
<p> To delete a environment variable, use the function <code>jsv_del_env</code>().</p>
<h3>jsv_del_env(<i>variable_name</i>)</h3>
<p> This function removes job environment variable <i>variable_name</i> from the set of variables that will be exported to the job when it is started. </p>
<p> If <i>variable_name</i> does not already exist in the set of job environment variables then the command is ignored. </p>
<p> To change the value of a variable use the function <code>jsv_mod_env</code>(); to add a new value, call the function <code>jsv_add_env</code>().</p>
<h3>jsv_accept(<i>message</i>)</h3>
<p> This function can only be used in <code>jsv_on_verify</code>(). After it has been called, the function <code>jsv_on_verify</code>() has to return immediately. </p>
<p> A call to this function indicates that the job that is currently being verified should be accepted as it was initially provided. All job modifications that might have been applied in <code>jsv_on_verify</code>() before this function was called, are then ignored. </p>
<p> Instead of calling <code>jsv_accept</code>() in <code>jsv_on_verify</code>(), the functions <code>jsv_correct</code>(), <code>jsv_reject</code>() or <code>jsv_reject_wait</code>() can be called, but only one of these functions can be used at a time.</p>
<h3>jsv_correct(<i>message</i>)</h3>
<p> This function can only be used in <code>jsv_on_verify</code>(). After it has been called, the function <code>jsv_on_verify</code>() has to return immediately. </p>
<p> A call to this function indicates that the job that is currently being verified has to be modified before it can be accepted. All job parameter modifications that were previously applied will be committed and the job will be accepted. &quot;Accept&quot; in that case means that the job will either be passed to the next JSV instance for modification or that it is passed to that component in the master daemon that adds it to the master data store when the last JSV instance has verified the job. </p>
<p> Instead of calling <code>jsv_correct</code>() in <code>jsv_on_verify</code>(), the functions <code>jsv_accept</code>(), <code>jsv_reject</code>() or <code>jsv_reject_wait</code>() can be called, but only one of these functions can be used.</p>
<h3>jsv_reject(<i>message</i>)</h3>
<p> This function can only be used in <code>jsv_on_verify</code>(). After it has been called the function <code>jsv_on_verify</code>() has to return immediately. </p>
<p> The job that is currently being verified will be rejected. <i>message</i> will be passed to the client application that tried to submit the job. Commandline clients like <i>qsub</i> will print that message to stdout to inform the user that the submission has failed. </p>
<p> <code>jsv_reject_wait</code>() should be called if the user may try to submit the job again. <code>jsv_reject_wait</code>() indicates that the verification process might be successful in the future. </p>
<p> Instead of calling <code>jsv_reject</code>() in <code>jsv_on_verify</code>(), the functions <code>jsv_accept()</code>, <code>jsv_correct</code>() or <code>jsv_reject_wait</code>() can be called, but only one of these functions can be used.</p>
<h3>jsv_reject_wait(<i>message</i>)</h3>
<p> This function can only be used in <code>jsv_on_verify</code>(). After it has been called the function <code>jsv_on_verify</code>() has to return immediately. </p>
<p> The job which is currently verified will be rejected. <i>message</i> will be passed to the client application, that tries to submit the job. Commandline clients like <i>qsub</i> will print that message to stdout to inform the user that the submission has failed. </p>
<p> This function should be called if the user who tries to submit the job might have a chance to submit the job later. <code>jsv_reject</code> indicates that the verified job will also be rejected in future. </p>
<p> Instead of calling <code>jsv_reject_wait</code>() in <code>jsv_on_verify</code>() the functions <code>jsv_accept</code>(), <code>jsv_correct</code>() or <code>jsv_reject</code>() can be called, but only one of these functions can be used.</p>
<h3>jsv_log_info(<i>message</i>)</h3>
<p> This function sends an info <i>message</i> to the client or master daemon instance that started the JSV script. </p>
<p> For client JSVs, this means that the command line client will get the information and print it to the stdout stream. Server JSVs will print that message as an info message to the master daemon message file. </p>
<p> If <i>message</i> is missing then an empty line will be printed.</p>
<h3>jsv_log_warning(<i>message</i>)</h3>
<p> This function sends a warning <i>message</i> to the client or master daemon instance that started the JSV script. </p>
<p> For client JSVs, this means that the command line client will get the information and print it to the stdout stream. Server JSVs will print that message as a warning message to the master daemon message file. </p>
<p> If <i>message</i> is missing then an empty line will be printed.</p>
<h3>jsv_log_error(<i>message</i>)</h3>
<p> This function sends an error <i>message</i> to the client or master daemon instance that started the JSV script. </p>
<p> For client JSVs, this means that the command line client will get the information and print it to the stdout stream. Server JSVs will print that message as an error message to the master daemon message file. </p>
<p> If <i>message</i> is missing then an empty line will be printed.</p>
<h3>jsv_send_env()</h3>
<p> This function can only be used in <code>jsv_on_start</code>(). If it is used there, then the job environment information will be available in <code>jsv_on_verify</code>() for the next job that is scheduled to be verified. </p>
<p> This function must be called for the functions <code>jsv_show_envs()</code>, <code>jsv_is_env</code>(), <code>jsv_get_env</code>(), <code>jsv_add_env</code>() and <code>jsv_mod_env</code>() to behave correctly. </p>
<p> Job environments might become very big (10kB and more). This will slow down the executing component (submit client or master daemon thread). For this reason, job environment information is not passed to JSV scripts by default. </p>
<p> Please note also that the data in the job environment can&#8217;t be verified by Grid Engine and might therefore contain values which could be misinterpreted in the script environment and cause security issues.</p>
<h3>jsv_main()</h3>
<p> This function has to be called in the main function in JSV scripts. It implements the JSV protocol and performs the communication with client and server components which might start JSV scripts. </p>
<p> This function does not return immediately. It returns only when the &quot;QUIT&quot; command is sent by the client or server component. </p>
<p> During the communication with client and server components, this function triggers two callback functions for each job that should be verified. First <code>jsv_on_start</code>() and later on <code>jsv_on_verify</code>(). </p>
<p> <code>jsv_on_start</code>() can be used to initialize certain things that might be needed for the verification process. <code>jsv_on_verify</code>() does the verification process itself. </p>
<p> The function <code>jsv_send_env</code>() can be called in <code>jsv_on_start</code>() so that the job environment is available in <code>jsv_on_verify</code>(). </p>
<p> The following functions can only be used in <code>jsv_on_verify</code>(). Simple job parameters can be accessed/modified with: <code>jsv_is_param</code>, <code>jsv_get_param</code>, <code>jsv_set_param</code> and <code>jsv_del_param</code>. </p>
<p> List based job parameters can be accessed with: <code>jsv_sub_is_param</code>, <code>jsv_sub_get_param</code>, <code>jsv_sub_add_param</code> and <code>jsv_sub_del_param</code>. </p>
<p> If the environment was requested with <code>jsv_send_env</code>() in <code>jsv_on_start</code>() then the environment can be accessed/modified with the following commands: <code>jsv_is_env</code>, <code>jsv_get_env</code>, <code>jsv_add_env</code>, <code>jsv_mod_env</code> and <code>jsv_del_env</code>. </p>
<p> Jobs can be accepted/rejected with the following: <code>jsv_accept</code>, <code>jsv_correct</code>, <code>jsv_reject</code> and <code>jsv_reject_wait</code>. </p>
<p> The following functions send messages to the calling component of a JSV that will either appear on the stdout stream of the client or in the master message file. This is especially useful when new JSV scripts should be tested: jsv_show_params<code>, </code>jsv_show_envs<code>, </code>jsv_log_info<code>, </code>jsv_log_warning<code> and </code>jsv_log_error<code>. </code></p>
<h3>jsv_on_start()</h3>
<p> This is a callback function that has to be defined by the creator of a JSV script. It is called for every job a short time before the verification process of a job starts. </p>
<p> Within this function <code>jsv_send_env</code> can be called to request job environment information for the next job scheduled to be verified. </p>
<p> After this function returns <code>jsv_on_verify</code>() will be called. This function does the verification process itself.</p>
<h3>jsv_on_verify()</h3>
<p> This is a callback function that has to be defined by the creator of a JSV script. It is called for every job, and when it returns the job will either be accepted or rejected. Find implementation examples in the directory <i>$SGE_ROOT/util/resources/jsv</i>. </p>
<p> The logic of this function completely depends on its creator. The creator has only to take care that one of the functions <code>jsv_accept</code>(), <code>jsv_reject</code>(), <code>jsv_reject_wait</code>() or <code>jsv_correct</code>() is called before the function returns.</p>
<h3>jsv_logging_enabled</h3>
<p> Setting this variable to <code>true</code> produces logging output tracing the JSV protocol, sent to a file of the form <code>/tmp/jsv_$$.log</code>. In the case of shell JSVs, it may be set in the environment of the job submission to effect logging without modifying the script. </p>
<h2>EXAMPLES</h2>
<p> Find in the table below the returned values for the &quot;*is*&quot; and &quot;*get*&quot; functions when following job is submitted:</p>
<dl>
<dt>
<dd>
<pre>
qsub -l mem=1G,mem2=200M -l a=lx-amd64 ...
</pre>
<table>
<tr VALIGN=top>
<td>function call </td>
<td> returned value
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>jsv_is_param(l_hard) </td>
<td> &quot;true&quot;
</td>
</tr>
<tr VALIGN=top>
<td>jsv_get_param(l_hard) </td>
<td> &quot;mem=1G,mem2=200M,a=lx-amd64&quot;
</td>
</tr>
<tr VALIGN=top>
<td>jsv_sub_is_param(l_hard,mem) </td>
<td> &quot;true&quot;
</td>
</tr>
<tr VALIGN=top>
<td>jsv_sub_get_param(l_hard,mem) </td>
<td> &quot;1G&quot;
</td>
</tr>
<tr VALIGN=top>
<td>jsv_sub_is_param(l_hard,mem3) </td>
<td> &quot;false&quot;
</td>
</tr>
<tr VALIGN=top>
<td>jsv_sub_get_param(l_hard,mem3) </td>
<td> &quot;&quot;
</td>
</tr>
<tr VALIGN=top>
<td>jsv_sub_is_param(l_hard,a) </td>
<td> &quot;true&quot;
</td>
</tr>
<tr VALIGN=top>
<td>jsv_sub_get_param(l_hard,a) </td>
<td> &quot;lx-amd64&quot;
</td>
</tr>
<tr VALIGN=top>
<td>jsv_sub_is_param(l_hard,arch) </td>
<td> &quot;false&quot;
</td>
</tr>
<tr VALIGN=top>
<td>jsv_sub_get_param(l_hard,arch) </td>
<td> &quot;&quot;
</td>
</tr>
</table>
</dl>
<h2>FILES</h2>
<pre>
Include files:
<i>$SGE_ROOT/util/resources/jsv/jsv_include.sh</i>
<i>$SGE_ROOT/util/resources/jsv/jsv_include.tcl</i>
<i>$SGE_ROOT/util/resources/jsv/JSV.pm</i>
Example files:
<i>$SGE_ROOT/util/resources/jsv/jsv.sh</i>
<i>$SGE_ROOT/util/resources/jsv/jsv.tcl</i>
<i>$SGE_ROOT/util/resources/jsv/jsv.pl</i>
<i>$SGE_ROOT/util/resources/jsv/jjsv.sh</i>
<i>$SGE_ROOT/util/resources/jsv/SimpleJsv.java</i>
</pre>
<p> Debugging log file:<br />
 <i>/tmp/jsv_$$.log</i></p>
<h2>BUGS</h2>
<p> Complex names seen by the script are not canonicalized, i.e. if the name and shortcut vary, it is necessary to consider both.</p>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
<dt><a href="#lbBH">EXAMPLES</a></p>
<dd>
<dt><a href="#lbBI">FILES</a></p>
<dd>
<dt><a href="#lbBJ">BUGS</a></p>
<dd>
<dt><a href="#lbBK">SEE ALSO</a></p>
<dd>
<dt><a href="#lbBL">COPYRIGHT</a></p>
<dd></dl>
