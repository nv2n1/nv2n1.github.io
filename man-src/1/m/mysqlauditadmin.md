---
title: "mysqlauditadmin(1)"
name: "mysqlauditadmin"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mysqlauditadmin/"
description: "mysqlauditadmin – Maintain the audit log"
---

<h2 class="name">NAME</h2>
<p> mysqlauditadmin &#8211; Maintain the audit log </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mysqlauditadmin [</code><i>OPTIONS</i><code>]&#8230; </code><code>mysqlauditadmin [</code><i>OPTIONS</i><code>]&#8230; [</code><i>COMMAND</i><code>]</code><code>mysqlauditadmin l=</code><i>user:pass [at] host:port</i><code> [</code><i>OPTIONS</i><code>]&#8230; [</code><i>COMMAND</i><code>[&#8211;value=</code><i>VALUE</i><code>]]</code><code>mysqlauditadmin &#8211;file-stats &#8211;audit-log-name=</code><i>FULL_PATH</i><code>mysqlauditadmin copy &#8211;audit-log-name=</code><i>FULL_PATH</i><code> &#8211;copy-to=</code><i>DESTINATION</i><code> [&#8211;remote-login=</code><i>user:host</i><code>]</code></dt></dl>
<h2>DESCRIPTION</h2>
<dd>This utility allow you to maintain the m[blue]<code>audit log</code>m[]<font SIZE="-2">[1]</font>, allowing you to monitor the audit log file growth and control its rotation. Rotation refers to the action of replacing the current audit log file by a new one for continuous use, renaming (with a timestamp extension) and copying the previously used audit log file to a defined location. </dd>
<p> This utility allows you to view and modify a subset of audit log control variables, display the audit log file status, perform on-demand rotation of the log file, and copy files to other locations. These features enable you to easily monitor the audit log file growth and control its rotation (automatically based on the defined file size threshold, or manually by a on-demand command). </p>
<p> The available actions include the following: </p>
<dl>
<dt>
</dt><dd> 1. <code>copy</code> </dd>
<p> This command copies the audit log specified by <code>&#8211;audit-log-name</code> to the destination path specified by <code>&#8211;copy-to</code>. The <code>&#8211;remote-login</code> option can be used to copy log files from a remote location. Note: the destination path must be locally accessible by the current user.</dl>
<dl>
<dt>
</dt><dd> 2. <code>policy</code> </dd>
<p> The policy command is used to change the audit logging policy. The accepted values are the following, which are set using the <code>&#8211;value</code> option. </p>
<dl>
<dt>
</dt><dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 The <code>&#8211;server</code> option is also required to execute this command. </dd>
</dl>
<dl>
<dt>
</dt><dd> &bull; ALL: log all events</dd></dl>
<dl>
<dt>
</dt><dd> &bull; NONE: log nothing</dd></dl>
<dl>
<dt>
</dt><dd> &bull; LOGINS: only log login events</dd></dl>
<dl>
<dt>
</dt><dd> &bull; QUERIES: only log query events</dd></dl>
<dl>
<dt>
</dt><dd> &bull; DEFAULT: sets the default log policy</dd></dl>
</dl>
<dl>
<dt>
</dt><dd> 3. <code>rotate_on_size</code> </dd>
<p> This command sets the file size threshold for automatic rotation of the audit log (the audit_log_rotate_on_size variable). The value is set using the <code>&#8211;value</code> option, and must be in the range (0, 4294967295). This command also requires the <code>&#8211;server</code> option to be specified. Note: if the variable is set with a value that is not a multiple of 4096, then it is truncated to the nearest multiple.</dl>
<dl>
<dt>
</dt><dd> 4. <code>rotate</code> </dd>
<p> This command is used to perform an on-demand audit log rotation, and only requires the <code>&#8211;server</code> option to be passed. Note: this command has no effect if the audit log file size is smaller than 4096, which is the minimum value allowed that is greater than 0 for the audit_log_rotate_on_size variable variable).</dl>
<p>OPTIONS </p>
<p> <code>mysqlauditadmin</code> accepts the following command-line options: </p>
<dl>
<dt>
</dt><dd> &bull; &#8211;audit-log-name=&lt;AUDIT_LOG_FILE&gt; </dd>
<p> Full path and file name for the audit log file. Used by the <code>&#8211;file-stats</code> option, and the <i>copy</i> command.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;copy-to=&lt;COPY_DESTINATION&gt; </dd>
<p> The location to copy the specified audit log file. The path must be locally accessible for the current user.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;file-stats </dd>
<p> Display the audit log file statistics.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;help </dd>
<p> Display a help message and exit.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;remote-login=&lt;REMOTE_LOGIN&gt; </dd>
<p> User name and host to be used for the remote login, for copying log files. It is defined using the following format: &lt;<i>user</i>&gt;:&lt;<i>host or IP</i>&gt;. Usage will prompt for the password.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;server=&lt;SERVER&gt; </dd>
<p> Connection information for the server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;show-options </dd>
<p> Display the audit log system variables.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;value=&lt;VALUE&gt; </dd>
<p> Value used to set variables based on the specified commands, such as <i>policy</i> and <i>rotate_on_size</i>.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;server1=&lt;source&gt; </dd>
<p> Connection information for the first server in the format: &lt;<i>user</i>&gt;[:&lt;<i>passwd</i>&gt;]@&lt;<i>host</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;] or &lt;<i>login-path</i>&gt;[:&lt;<i>port</i>&gt;][:&lt;<i>socket</i>&gt;].</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;verbose, -v </dd>
<p> Specify how much information to display. Use this option multiple times to increase the amount of information. For example, <code>-v</code> = verbose, <code>-vv</code> = more verbose, <code>-vvv</code> = debug.</dl>
<dl>
<dt>
</dt><dd> &bull; &#8211;version </dd>
<p> Display version information and exit.</dl>
<p>NOTES </p>
<p> This utility is available as of μ 1.2.0. </p>
<p> This utility can only be applied to servers with the m[blue]<code>audit log plugin enabled</code>m[]<font SIZE="-2">[2]</font>. And the audit log plugin is available as of MySQL Server versions 5.5.28 and 5.6.10. </p>
<p> This utility requires Python version 2.6 or higher, but does not support Python 3. </p>
<p> The path to the MySQL client tools should be included in the PATH environment variable in order to use the authentication mechanism with login-paths. This will allow the utility to use the my_print_defaults tools, which is required to read the login-path values from the login configuration file (.mylogin.cnf). This feature exists as of MySQL Server 5.6.6, see m[blue]<code>mysql_config_editor</code> &#8212; MySQL Configuration Utilitym[]<font SIZE="-2">[3]</font>.<br />
LIMITATIONS </p>
<p> The <code>&#8211;remote-login</code> option is not supported on Microsoft Windows platforms. For Microsoft Windows, use UNC paths and perform a local copy operation, omitting the <code> &#8211;remote-login</code> option.<br />
EXAMPLES </p>
<p> To display the audit log system variables, run the following command: </p>
<dl>
<dt>
</dt><dd>
<pre><code>
$ mysqlauditadmin-- show - options-- server = root[at] localhost : 3310
#
#Audit Log Variables and Options
#
                                                  + -- -- -- -- -- -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -+ |
                                              Variable_name | Value |
                                              +-- -- -- -- -- -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -+ | audit_log_buffer_size | 1048576 |
                                              | audit_log_file | audit.log |
                                              | audit_log_flush | OFF |
                                              | audit_log_policy | ALL |
                                              | audit_log_rotate_on_size | 0 |
                                              | audit_log_strategy | ASYNCHRONOUS |
                                              +-- -- -- -- -- -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -+
</code></pre>
</dd></dl>
<p> To perform a (manual) rotation of the audit log file, use the following command: </p>
<dl>
<dt>
</dt><dd>
<pre>
shell&gt; mysqlauditadmin --server=root [at] localhost:3310 rotate
#
# Executing ROTATE command.
#
</pre>
</dd></dl>
<p> To display the audit log file statistics, run the following command: </p>
<dl>
<dt>
</dt><dd>
shell &gt; mysqlauditadmin&#8211; file &#8211; stats&#8211; audit &#8211; log &#8211; name =../ SERVER / data / audit.log + &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | File | Size | Created | Last Modified |<br />
                                                             +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | audit.log | 3258 | Wed Sep 26 11 : 07 : 43 2012 | Wed Sep 26 11 : 07 : 43 2012 |<br />
                                                             | audit.log .13486539046497235 | 47317 | Wed Sep 26 11 : 05 : 04 2012 | Wed Sep 26 11 : 05 : 04 2012 |<br />
                                                             +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8211;+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+
</dd></dl>
<p> To change the audit log policy to log only query events, and show the system variables before and after the execution of the <i>policy</i> command, use the following command: </p>
<dl>
<dt>
</dt><dd>
shell &gt; mysqlauditadmin&#8211; show &#8211; options&#8211; server = root[at] localhost : 3310 policy \<br />
    &#8211;value = QUERIES<br />
#<br />
#Showing options before command.<br />
#<br />
#Audit Log Variables and Options<br />
#<br />
                  + &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ |<br />
              Variable_name | Value |<br />
              +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | audit_log_buffer_size | 1048576 |<br />
              | audit_log_file | audit.log |<br />
              | audit_log_flush | OFF |<br />
              | audit_log_policy | ALL |<br />
              | audit_log_rotate_on_size | 0 |<br />
              | audit_log_strategy | ASYNCHRONOUS |<br />
              +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+<br />
#<br />
#Executing POLICY command.<br />
#<br />
#<br />
#Showing options after command.<br />
#<br />
#Audit Log Variables and Options<br />
#<br />
                                                                              +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ |<br />
              Variable_name | Value |<br />
              +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+ | audit_log_buffer_size | 1048576 |<br />
              | audit_log_file | audit.log |<br />
              | audit_log_flush | OFF |<br />
              | audit_log_policy | QUERIES |<br />
              | audit_log_rotate_on_size | 0 |<br />
              | audit_log_strategy | ASYNCHRONOUS |<br />
              +&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; -+
</dd></dl>
<p> To change the audit log automatic file rotation size to 32535, and show the system variables before and after the execution of the <i>rotate_on_size</i> command, use the following command. (Notice that the value set is actually 28672 because the specified rotate_on_size value is truncated to a multiple of 4096): </p>
<dl>
<dt>
</dt><dd>
<pre><code>
shell &gt; mysqlauditadmin-- show - options-- server = root[at] localhost : 3310 rotate_on_size-- value = 32535
#
#Showing options before command.
#
#Audit Log Variables and Options
#
                                                                                                           + -- -- -- -- -- -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -+ |
                                                                                                       Variable_name | Value |
                                                                                                       +-- -- -- -- -- -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -+ | audit_log_buffer_size | 1048576 |
                                                                                                       | audit_log_file | audit.log |
                                                                                                       | audit_log_flush | OFF |
                                                                                                       | audit_log_policy | ALL |
                                                                                                       | audit_log_rotate_on_size | 0 |
                                                                                                       | audit_log_strategy | ASYNCHRONOUS |
                                                                                                       +-- -- -- -- -- -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -+
#
#Executing ROTATE_ON_SIZE command.
#
#
#Showing options after command.
#
#Audit Log Variables and Options
#
                                                                                                                                                                       +-- -- -- -- -- -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -+ |
                                                                                                       Variable_name | Value |
                                                                                                       +-- -- -- -- -- -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -+ | audit_log_buffer_size | 1048576 |
                                                                                                       | audit_log_file | audit.log |
                                                                                                       | audit_log_flush | OFF |
                                                                                                       | audit_log_policy | ALL |
                                                                                                       | audit_log_rotate_on_size | 28672 |
                                                                                                       | audit_log_strategy | ASYNCHRONOUS |
                                                                                                       +-- -- -- -- -- -- -- -- -- -- -- -- -- -+-- -- -- -- -- -- -- -+
</code></pre>
</dd></dl>
<p> To perform a copy of a audit log file to another location, use the following command: </p>
<dl>
<dt>
</dt><dd>
<pre>
shell&gt; mysqlauditadmin --audit-log-name=../SERVER/data/audit.log.13486539046497235 \
     copy --copy-to=/BACKUP/Audit_Logs
</pre>
</dd></dl>
<p> To copy a audit log file from a remote server/location to the current location (user password will be prompted), use the following command: </p>
<dl>
<dt>
</dt><dd>
<pre>
shell&gt; mysqlauditadmin --audit-log-name=audit.log.13486539046497235 \
     copy --remote-login=user:host --copy-to=.
</pre>
</dd></dl>
<h2>COPYRIGHT</h2>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> audit log</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://dev.mysql.com/doc/refman/5.6/en/audit-log-plugin.html">http://dev.mysql.com/doc/refman/5.6/en/audit-log-plugin.html</a></dd></dl>
<dt> 2.</dt>
<dd> audit log plugin enabled</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://dev.mysql.com/doc/refman/5.6/en/audit-log-plugin-installation.html">http://dev.mysql.com/doc/refman/5.6/en/audit-log-plugin-installation.html</a></dd></dl>
<dt> 3.</dt>
<dd> <code>mysql_config_editor</code> &#8212; MySQL Configuration Utility</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://dev.mysql.com/doc/refman/5.6/en/mysql-config-editor.html">http://dev.mysql.com/doc/refman/5.6/en/mysql-config-editor.html</a></dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> For more information, please refer to the MySQL Utilities section of the MySQL Workbench Reference Manual, which is available online at <a rel="nofollow" href="http://dev.mysql.com/doc/workbench/en/.">http://dev.mysql.com/doc/workbench/en/.</a></p>
<h2>AUTHOR</h2>
<p> Oracle Corporation (<a rel="nofollow" href="http://dev.mysql.com/">http://dev.mysql.com/</a>). </p>
<h2>Index</h2>
