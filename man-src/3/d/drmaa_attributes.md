---
title: "drmaa_attributes(3)"
name: "drmaa_attributes"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa_attributes/"
description: "drmaa_get_attribute_names, drmaa_get_vector_attribute_names, drmaa_get_next_attr_name, drmaa_get_num_attr_names, drmaa_release_attr_names – DRMAA job template attributes"
---

<h2 class="name">NAME</h2>
<p> drmaa_get_attribute_names, drmaa_get_vector_attribute_names, drmaa_get_next_attr_name, drmaa_get_num_attr_names, drmaa_release_attr_names &#8211; DRMAA job template attributes</p>
<h2>SYNOPSIS</h2>
<p> <code>#include drmaa.h</code> </p>
<pre>
<code>int drmaa_get_attribute_names(
<dl><dt><dd>drmaa_attr_names_t **values,
char *error_diagnosis,
size_t error_diag_len
</dl>
</code></pre>
<p> );<code> </p>
<p> </code></p>
<pre>
<code>int drmaa_get_vector_attribute_names(
<dl><dt><dd>drmaa_attr_names_t **values,
char *error_diagnosis,
size_t error_diag_len
</dl>
</code></pre>
<p> );<code> </p>
<p> </code></p>
<pre>
<code>int drmaa_get_next_attr_name(
<dl><dt><dd>drmaa_attr_names_t* values,
char *value,
int value_len
</dl>
</code></pre>
<p> );<code> </p>
<p> </code></p>
<pre>
<code>int drmaa_get_next_attr_value(
<dl><dt><dd>drmaa_attr_values_t* values,
char *value,
int value_len
</dl>
</code></pre>
<p> );<code> </p>
<p> </code></p>
<pre>
<code>int drmaa_get_num_attr_names(
<dl><dt><dd>drmaa_attr_names_t* values,
int *size
</dl>
</code></pre>
<p> );<code> </p>
<p> </code></p>
<pre>
<code>void drmaa_release_attr_names(
<dl><dt><dd>drmaa_attr_names_t* values
</dl>
</code></pre>
<p> );<code> </p>
<p> </code></p>
<h2>DESCRIPTION</h2>
<p> The drmaa_get_attribute_names() function returns into <i>values</i> a DRMAA names string vector containing the set of supported non-vector DRMAA job template attribute names. The set includes supported DRMAA reserved attribute names and xxQS_NAMExx native attribute names. The names in the names string vector can be extracted using The number of names in the names string vector can be determined using Note that this function is only available in the 1.0 implementation. The caller is responsible for releasing the names string vector returned into <i>values</i> using Use and for setting and inspecting non-vector attributes.</p>
<h3>drmaa_get_vector_attribute_names()</h3>
<p> The drmaa_get_vector_attribute_names() function returns into <i>values</i> a DRMAA names string vector containing the set of supported vector DRMAA job template attribute names. The set includes supported DRMAA reserved attribute names and xxQS_NAMExx native attribute names. The names in the names string vector can be extracted using The caller is responsible for releasing the names string vector returned into <i>values</i> using Use and for setting and inspecting vector attributes. </p>
<h3>drmaa_get_next_attr_name()</h3>
<p> Each time drmaa_get_next_attr_name() is called it returns into the buffer, <i>value</i>, up to <i>value_len</i> bytes of the next entry stored in the DRMAA names string vector, <i>values</i>. Once the names list has been exhausted, DRMAA_ERRNO_NO_MORE_ELEMENTS is returned. </p>
<h3>drmaa_get_num_attr_names()</h3>
<p> The drmaa_get_num_attr_names() returns into <i>size</i> the number of entries in the DRMAA names string vector. This function is only available in the 1.0 implementation. </p>
<h3>drmaa_release_attr_names()</h3>
<p> The drmaa_release_attr_names() function releases all resources associated with the DRMAA names string vector, <i>values</i>. </p>
<h3>Attribute Priorities</h3>
<p> DRMAA job template attributes can be set from six different sources. In order of precedence, from lowest to highest, these are: options set by DRMAA automatically by default, options set in the file(s), options set in the script file, options set by the drmaa_job_category attribute, options set by the drmaa_native_specification attribute, and options set through other DRMAA attributes. </p>
<p> By default DRMAA sets four options for all jobs. These are &quot;-p 0&quot;, &quot;-b yes&quot;, &quot;-shell no&quot;, and &quot;-w e&quot;. This means that by default, all jobs will have priority 0, all jobs will be treated as binary, i.e. no scripts args will be parsed, all jobs will be executed without a wrapper shell, and jobs which are unschedulable will cause a submit error. </p>
<p> The file, found in the $xxQS_NAME_Sxx_ROOT/$xxQS_NAME_Sxx_CELL/common directory, may contain options to be applied to all jobs. The .sge_request file found in the user&#8217;s home directory or the current working directory may also contain options to be applied to certain jobs. See for more information. </p>
<p> If the file contains &quot;-b no&quot; or if the drmaa_native_specification attribute is set and contains &quot;-b no&quot;, the script file will be parsed for in-line arguments. Otherwise, no scripts args will be interpreted. See for more information. </p>
<p> If the drmaa_job_category attribute is set, and the category it points to exists in one of the files, the options associated with that category will be applied to the job template. See and the drmaa_job_category attribute below for more information. </p>
<p> If the drmaa_native_specification attribute is set, all options contained therein will be applied to the job template. See the drmaa_native_specification below for more information. </p>
<p> Other DRMAA attributes will override any previous settings. For example, if the sge_request file contains &quot;-j y&quot;, but the drmaa_join_files attribute is set to &quot;n&quot;, the ultimate result is that the input and output files will remain separate. </p>
<p> For various reasons, some options are silently ignored by DRMAA. Setting any of these options will have no effect. The ignored options are: -cwd, -help, -sync, -t, -verify, -w w, and -w v. The -cwd option can be re-enabled by setting the environment variable, SGE_DRMAA_ALLOW_CWD. However, the -cwd option is not thread safe and should not be used in a multi-threaded context. </p>
<h3>Attribute Correlations</h3>
<p> The following DRMAA attributes correspond to the listed options: </p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>DRMAA Attribute </td>
<td> qsub Option
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_remote_command </td>
<td> script file
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_v_argv </td>
<td> script file args
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_js_state = &quot;drmaa_hold&quot; </td>
<td> -h
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_v_env </td>
<td> -v
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_wd = $PWD </td>
<td> -cwd
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_job_category </td>
<td> (qtsch qtask)*
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_native_specification </td>
<td> ALL*
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_v_email </td>
<td> -M
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_block_email = &quot;1&quot; </td>
<td> -m n
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_start_time </td>
<td> -a
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_job_name </td>
<td> -N
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_input_path </td>
<td> -i
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_output_path </td>
<td> -o
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_error_path </td>
<td> -e
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_join_files </td>
<td> -j
</td>
</tr>
<tr VALIGN=top>
<td>drmaa_transfer_files </td>
<td> (prolog and epilog)*
</td>
</tr>
</table>
<p> * See the individual attribute description below</dl>
<h2>DRMAA JOB TEMPLATE ATTRIBUTES</h2>
<h3>drmaa_remote_command &#8211; <i>remote_command</i></h3>
<p> Specifies the remote command to execute. The <i>remote_command</i> must be the path of an executable that is available at the job&#8217;s execution host. If the path is relative, it is assumed to be relative to the working directory, usually set through the drmaa_wd attribute. If working directory is not set, the path is assumed to be relative to the user&#8217;s home directory. </p>
<p> The file pointed to by remote_command may either be an executable binary or an executable script. If a script, it must include the path to the shell in a #! line at the beginning of the script. By default, the remote command will be executed directly, as by To have the remote command executed in a shell, such as to preserve environment settings, use the drmaa_native_specification attribute to include the &quot;-shell yes&quot; option. Jobs which are executed by a wrapper shell fail differently from jobs which are executed directly. When a job which contains a user error, such as an invalid path to the executable, is executed by a wrapper shell, the job will execute successfully, but exit with a return code of 1. When a job which contains such an error is executed directly, it will enter the DRMAA_PS_FAILED state upon execution. </p>
<h3>drmaa_js_state &#8211; {drmaa_hold|drmaa_active}</h3>
<p> Specifies the job state at submission. The string values &#8216;drmaa_hold&#8217; and &#8216;drmaa_active&#8217; are supported. When &#8216;drmaa_active&#8217; is used the job is submitted in a runnable state. When &#8216;drmaa_hold&#8217; is used the job is submitted in user hold state (either DRMAA_PS_USER_ON_HOLD or DRMAA_PS_USER_SYSTEM_ON_HOLD). This attribute is largely equivalent to the submit option &#8216;-h&#8217;. </p>
<h3>drmaa_wd &#8211; <i>directory_name</i></h3>
<p> Specifies the directory name where the job will be executed. A &#8216;$drmaa_hd_ph$&#8217; placeholder at the beginning of the <i>directory_name</i> denotes the remaining string portion as a relative directory name that is resolved relative to the job user&#8217;s home directory at the execution host. When the DRMAA job template is used for bulk job submission (see also the &#8216;$drmaa_incr_ph$&#8217; placeholder can be used at any position within <i>directory_name</i> to cause a substitution with the parametric job&#8217;s index. The <i>directory_name</i> must be specified in a syntax that is common at the host where the job is executed. If set to a relative path and no placeholder is used, a path relative to the user&#8217;s home directory is assumed. If not set, the working directory will default to the user&#8217;s home directory. If set and the given directory does not exist the job will enter the DRMAA_PS_FAILED state when run. </p>
<p> Note that the working directory path is the path on the execution host. If binary mode is disabled, an attempt to find the job script will be made, relative to the working directory path. That means that the path to the script must be the same on both the submission and execution hosts. </p>
<h3>drmaa_job_name &#8211; <i>job_name</i></h3>
<p> Specifies the job&#8217;s name. Setting the job name is equivalent to use of submit option &#8216;-N&#8217; with <i>job_name</i> as option argument. </p>
<h3>drmaa_input_path &#8211; [<i>hostname</i>]:<i>file_path</i></h3>
<p> Specifies the standard input of the job. Unless set elsewhere, if not explicitly set in the job template, the job is started with an empty input stream. If the standard input is set it specifies the network path of the job&#8217;s input stream file. </p>
<p> When the &#8216;drmaa_transfer_files&#8217; job template attribute is supported and contains the character &#8216;i&#8217;, the input file will be fetched by xxQS_NAMExx from the specified host or from the submit host if no <i>hostname</i> is specified. When the &#8216;drmaa_transfer_files&#8217; job template attribute is not supported or does not contain the character &#8216;i&#8217;, the input file is always expected at the host where the job is executed regardless of any <i>hostname</i> specified. </p>
<p> If the DRMAA job template will be used for bulk job submission, (see also the &#8216;$drmaa_incr_ph$&#8217; placeholder can be used at any position within <i>file_path</i> to cause a substitution with the parametric job&#8217;s index. A &#8216;$drmaa_hd_ph$&#8217; placeholder at the beginning of <i>file_path</i> denotes the remaining portion of the <i>file_path</i> as a relative file specification resolved relative to the job user&#8217;s home directory at the host where the file is located. A &#8216;$drmaa_wd_ph$&#8217; placeholder at the beginning of <i>file_path</i> denotes the remaining portion of the <i>file_path</i> as a relative file specification resolved relative to the job&#8217;s working directory at the host where the file is located. The <i>file_path</i> must be specified in a syntax that is common at the host where the file is located. If set and the file can&#8217;t be read the job enters the state DRMAA_PS_FAILED. </p>
<h3>drmaa_output_path &#8211; [<i>hostname</i>]:<i>file_path</i></h3>
<p> Specifies the standard output of the job. If not explicitly set in the job template, the whereabouts of the job&#8217;s output stream is not defined. If set, this attribute specifies the network path of the job&#8217;s output stream file. </p>
<p> When the &#8216;drmaa_transfer_files&#8217; job template attribute is supported and contains the character &#8216;o&#8217;, the output file will be transferred by xxQS_NAMExx to the specified host or to the submit host if no <i>hostname</i> is specified. When the &#8216;drmaa_transfer_files&#8217; job template attribute is not supported or does not contain the character &#8216;o&#8217;, the output file is always kept at the host where the job is executed regardless of any <i>hostname</i> specified. </p>
<p> If the DRMAA job template will be used for of bulk job submission (see also the &#8216;$drmaa_incr_ph$&#8217; placeholder can be used at any position within the <i>file_path</i> to cause a substitution with the parametric job&#8217;s index. A &#8216;$drmaa_hd_ph$&#8217; placeholder at the beginning of <i>file_path</i> denotes the remaining portion of the <i>file_path</i> as a relative file specification resolved relative to the job user&#8217;s home directory at the host where the file is located. A &#8216;$drmaa_wd_ph$&#8217; placeholder at the beginning of the <i>file_path</i> denotes the remaining portion of <i>file_path</i> as a relative file specification resolved relative to the job&#8217;s working directory at the host where the file is located. The <i>file_path</i> must be specified in a syntax that is common at the host where the file is located. If set and the file can&#8217;t be written before execution the job enters the state DRMAA_PS_FAILED. </p>
<h3>drmaa_error_path &#8211; [<i>hostname</i>]:<i>file_path</i></h3>
<p> Specifies the standard error of the job. If not explicitly set in the job template, the whereabouts of the job&#8217;s error stream is not defined. If set, this attribute specifies the network path of the job&#8217;s error stream file. </p>
<p> When the &#8216;drmaa_transfer_files&#8217; job template attribute is supported and contains the character &#8216;e&#8217;, the output file will be transferred by xxQS_NAMExx to the specified host or to the submit host if no <i>hostname</i> is specified. When the &#8216;drmaa_transfer_files&#8217; job template attribute is not supported or does not contain the character &#8216;e&#8217;, the error file is always kept at the host where the job is executed regardless of any <i>hostname</i> specified. </p>
<p> If the DRMAA job template will be used for of bulk job submission (see also the &#8216;$drmaa_incr_ph$&#8217; placeholder can be used at any position within the <i>file_path</i> to cause a substitution with the parametric job&#8217;s index. A &#8216;$drmaa_hd_ph$&#8217; placeholder at the beginning of the <i>file_path</i> denotes the remaining portion of the <i>file_path</i> as a relative file specification resolved relative to the job user&#8217;s home directory at the host where the file is located. A &#8216;$drmaa_wd_ph$&#8217; placeholder at the beginning of the <i>file_path</i> denotes the remaining portion of the <i>file_path</i> as a relative file specification resolved relative to the job&#8217;s working directory at the host where the file is located. The <i>file_path</i> must be specified in a syntax that is common at the host where the file is located. If set and the file can&#8217;t be written before execution the job enters the state DRMAA_PS_FAILED. The attribute name is drmaa_error_path. </p>
<h3>drmaa_join_files &#8211; {y|n}</h3>
<p> Specifies if the job&#8217;s error stream should be intermixed with the output stream. If not explicitly set in the job template the attribute defaults to &#8216;n&#8217;. Either &#8216;y&#8217; or &#8216;n&#8217; can be specified. If &#8216;y&#8217; is specified xxQS_NAMExx will ignore the value of the &#8216;drmaa_error_path&#8217; job template attribute and intermix the standard error stream with the standard output stream as specified with &#8216;drmaa_output_path&#8217;. </p>
<h3>drmaa_submit_as_euid &#8211; {y|n}</h3>
<p> Specifies whether the jobs submitted using the job template will will run under the authority of the real or the effective user and group ID. If not explicitly set in the job template, the attribute defaults to &#8216;n&#8217;. Either &#8216;y&#8217; or &#8216;n&#8217; can be specified. If &#8216;y&#8217; is specified xxQS_NAMExx will use the effective user and group ID, otherwise the real user and group ID is used. </p>
<p> With MUNGE security the euid is always used. (See for information on security settings.) </p>
<h3>drmaa_v_argv &#8211; <i>argv1 argv2</i> &#8230;</h3>
<p> Specifies the arguments to the job. </p>
<h3>drmaa_job_category &#8211; <i>category</i></h3>
<p> Specifies the DRMAA job category. The <i>category</i> string is used by xxQS_NAMExx as a reference into the file. Certain options used in the referenced qtask file line are applied to the job template before submission to allow site-specific resolving of resources and/or policies. The cluster qtask file, the local qtask file, and the user qtask file are searched. Job settings resulting from job template category are overridden by settings resulting from the job template drmaa_native_specification attribute as well as by explicit DRMAA job template settings. </p>
<p> In order to avoid collisions with command names in the qtask files, it is recommended that DRMAA job category names take the form: &lt;category_name&gt;.cat. </p>
<p> The options -help, -sync, -t, -verify, and -w w|v are ignored. The -cwd option is ignored unless the $SGE_DRMAA_ALLOW_CWD environment variable is set. </p>
<h3>drmaa_native_specification &#8211; <i>native_specification</i></h3>
<p> Specifies xxQS_NAMExx native options which will be interpreted as part of the DRMAA job template. All options available to command may be used in the <i>native_specification</i>, except for -help, -sync, -t, -verify, and -w w|v. The -cwd option may only be used if the SGE_DRMAA_ALLOW_CWD environment variable is set. This is because the current parsing algorithm for -cwd is not thread-safe. Options set in the <i>native specification</i> will be overridden by the corresponding DRMAA attributes. See for more information on qsub options. </p>
<h3>drmaa_v_env &#8211; <i>name1</i>=<i>value1 name2</i>=<i>value2</i> &#8230;</h3>
<p> Specifies the job environment. Each environment <i>value</i> defines the remote environment. The <i>value</i> overrides the remote environment values if there is a collision. </p>
<h3>drmaa_v_email &#8211; <i>email1 email2</i> &#8230;</h3>
<p> Specifies e-mail addresses that are used to report the job completion and status. </p>
<h3>drmaa_block_email &#8211; {0|1}</h3>
<p> Specifies whether e-mail sending shall blocked or not. By default email is not sent. If, however, a setting in a cluster or user settings file or the &#8216;drmaa_native_specification&#8217; or &#8216;drmaa_job_category&#8217; attribute enables sending email in association with job events, the &#8216;drmaa_block_email&#8217; attribute will override that setting, causing no email to be sent. </p>
<h3>drmaa_start_time &#8211; [[[[<i>CC</i>]<i>YY</i>/]<i>MM</i>/]<i>DD</i>] <i>hh</i>:<i>mm</i>[:<i>ss</i>] [{-|+}<i>UU</i>:<i>uu</i>]</h3>
<p> Specifies the earliest time when the job may be eligible to be run where </p>
<pre><code>
CC is the first two digits of the year(century - 1)
    YY is the last two digits of the year
    MM is the two digits of the month[01, 12] DD is the two digit day of the month[01, 31] hh is the two digit hour of the day[00, 23] mm is the two digit minute of the day[00, 59] ss is the two digit second of the minute[00, 61] UU is the two digit hours since(before)
UTC
    uu is the two digit minutes
    since(before) UTC
</code></pre>
<p> If the optional UTC-offset is not specified, the offset associated with the local timezone will be used. If the day (DD) is not specified, the current day will be used unless the specified hour:mm:ss has already elapsed, in which case the next day will be used. Similarly for month (MM), year (YY), and century-1 (CC). Example: The time: Sep 3 4:47:27 PM PDT 2002, could be represented as: 2002/09/03 16:47:27 -07:00. </p>
<h3>drmaa_transfer_files &#8211; [i][o][e]</h3>
<p> Specifies, which of the standard I/O files (stdin, stdout and stderr) are to be transferred to/from the execution host. If not set, defaults to &quot;&quot;. Any combination of &#8216;e&#8217;, &#8216;i&#8217; and &#8216;o&#8217; may be specified. See drmaa_input_path, drmaa_output_path and drmaa_error_path for information about how to specify the standard input file, standard output file and standard error file. The file transfer mechanism itself must be configured by the administrator (see When it is configured, the administrator has to enable drmaa_transfer_files. If it is not configured, &quot;drmaa_transfer_files&quot; is not enabled and can&#8217;t be used. </p>
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell to be used. To address a xxQS_NAMExx cell xxQS_NAMExx uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry instead to define that port.</p>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>SGE_DRMAA_ALLOW_CWD</code></p>
<dd> Enables the parsing of the -cwd option from the sge_request file(s), job category, and/or the native specification attribute. This option is disabled by default because the algorithm for parsing the -cwd option is not thread-safe.</dl>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, drmaa_get_attribute_names(), drmaa_get_vector_attribute_names(), and drmaa_get_next_attr_name() return DRMAA_ERRNO_SUCCESS. Other values indicate an error. Up to <i>error_diag_len</i> characters of error related diagnosis information is then provided in the buffer <i>error_diagnosis</i>. </p>
<h2>ERRORS</h2>
<p> The drmaa_get_attribute_names(), drmaa_get_vector_attribute_names(), and drmaa_get_next_attr_name() functions will fail if:</p>
<h3>DRMAA_ERRNO_INTERNAL_ERROR</h3>
<p> Unexpected or internal DRMAA error, like system call failure, etc.</p>
<h3>DRMAA_ERRNO_DRM_COMMUNICATION_FAILURE</h3>
<p> Could not contact DRM system for this request.</p>
<h3>DRMAA_ERRNO_AUTH_FAILURE</h3>
<p> The specified request is not processed successfully due to authorization failure.</p>
<h3>DRMAA_ERRNO_INVALID_ARGUMENT</h3>
<p> The input value for an argument is invalid.</p>
<h3>DRMAA_ERRNO_NO_ACTIVE_SESSION</h3>
<p> Failed because there is no active session.</p>
<h3>DRMAA_ERRNO_NO_MEMORY</h3>
<p> Failed allocating memory. </p>
<p> The drmaa_get_next_attr_name() will fail if:</p>
<h3>DRMAA_ERRNO_INVALID_ATTRIBUTE_VALUE</h3>
<p> When there are no more entries in the vector. </p>
<h2>SEE ALSO</h2>
<p> and </p>
<h2>Index</h2>
<dt><a href="#lbBC">ENVIRONMENTAL VARIABLES</a></p>
<dd>
<dt><a href="#lbBD">RETURN VALUES</a></p>
<dd>
<dt><a href="#lbBE">ERRORS</a></p>
<dd>
<dt><a href="#lbBM">SEE ALSO</a></p>
<dd></dl>
