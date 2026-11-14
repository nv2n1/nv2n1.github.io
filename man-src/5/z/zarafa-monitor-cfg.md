---
title: "zarafa-monitor-cfg(5)"
name: "zarafa-monitor-cfg"
section: "5"
letter: "z"
url: "/docs/linux/man/5-zarafa-monitor-cfg/"
description: "zarafa-monitor.cfg – The Zarafa monitor configuration file"
---

<p>zarafa-monitor.cfg &#8211; The Zarafa monitor configuration file</p>
<h2>Synopsis</h2>
<p><code>monitor.cfg</code></p>
<h2>Description</h2>
<p>The monitor.cfg is a configuration file for the Zarafa Monitor. monitor.cfg contains instructions for the software to set up the logging system.</p>
<h2>File Format</h2>
<p>The file consists of one big section, but parameters can be grouped by functionality. </p>
<p> The parameters are written in the form: </p>
<p> <code>name</code> = <i>value</i> </p>
<p> The file is line-based. Each newline-terminated line represents either a comment, nothing, a parameter or a directive. A line beginning with `#&#8217; is considered a comment, and will be ignored by Zarafa. Parameter names are case sensitive. Lines beginning with `!&#8217; are directives. </p>
<p> Directives are written in the form: </p>
<p> !<code>directive</code><i>[argument(s)] </i> </p>
<p> The following directives exist: </p>
<p> <code>include</code></p>
<dl>
<dd>Include and process <i>argument</i> </p>
<p> Example: !include common.cfg</dl>
<p> The types of parameters for the spooler are: server, smtp and log.</p>
<h2>Explanation Of Each Parameter</h2>
<p><code>quota_check_interval</code></p>
<dl>
<dd>Set the interval (in minutes) for checking the quota for all Zarafa users. </p>
<p> Default: <i>15</i></dl>
<p> <code>mailquota_resend_interval</code></p>
<dl>
<dd>Send interval of a quota mail in days when a user reache his warning, soft or hard quota. </p>
<p> Default: <i>1</i></dl>
<p> <code>server_socket</code></p>
<dl>
<dd>Connection URL to find the connection to the Zarafa server. </p>
<p> Default: <i>file:///var/run/zarafa</i></dl>
<p> <code>run_as_user</code></p>
<dl>
<dd>After correctly starting, the monitor process will become this user, dropping root privileges. Note that the log file needs to be writeable by this user, and the directory too to create new logfiles after logrotation. This can also be achieved by setting the correct group and permissions. </p>
<p> Default value is empty, not changing the user after starting.</dl>
<p> <code>run_as_group</code></p>
<dl>
<dd>After correctly starting, the monitor process will become this group, dropping root privileges. </p>
<p> Default value is empty, not changing the group after starting.</dl>
<p> <code>pid_file</code></p>
<dl>
<dd>Write the process ID number to this file. This is used by the init.d script to correctly stop/restart the service. </p>
<p> Default value: /var/run/zarafa-monitor.pid</dl>
<p> <code>running_path</code></p>
<dl>
<dd>Change directory to this path when running in daemonize mode. When using the -F switch to run in the foreground the directory will not be changed. </p>
<p> Default: <i>/</i></dl>
<p> <code>sslkey_file</code></p>
<dl>
<dd>Use this file as key to logon to the server. This is only used when server_socket is set to an HTTPS transport. See the <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1) manual page on how to setup SSL keys. </p>
<p> Default: value not set.</dl>
<p> <code>sslkey_pass</code></p>
<dl>
<dd>The password of the SSL key file that is set in sslkey_file. </p>
<p> Default: value not set.</dl>
<p> <code>log_method</code></p>
<dl>
<dd>The method which should be used for logging. Valid values are: </p>
<p> <i>syslog</i></p>
<dl>
<dd>Use the Linux system log. All messages will be written to the mail facility. See also <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a></code>(5).</dl>
<p> <i>file</i></p>
<dl>
<dd>Log to a file. The filename will be specified in <code>log_file</code>.</dl>
<p> Default: <i>file</i></dl>
<p> <code>log_file</code></p>
<dl>
<dd>When logging to a file, specify the filename in this parameter. Use <i>&#8211;</i> (minus sign) for stderr output. </p>
<p> Default: <i>/var/log/zarafa/monitor.log</i></dl>
<p> <code>log_timestamp</code></p>
<dl>
<dd>Specify whether to prefix each log line with a timestamp in &#8216;file&#8217; logging mode. </p>
<p> Default: <i>1</i></dl>
<p> <code>log_level</code></p>
<dl>
<dd>The level of output for logging in the range from 0 to 5. 0 means no logging, 5 means full logging. </p>
<p> Default: <i>2</i></dl>
<p> <code>userquota_warning_template</code>, <code>companyquota_warning_template</code></p>
<dl>
<dd>These templates are read by the zarafa-monitor when a user or tenant exceeds a particular quota level. In these templates multiple variables can be used which will be replaced before sending the quota warning email. </p>
<p> These files should be saved in the UTF-8 charset. UTF-8 is compatible with US-ASCII, so if you only use western characters, there is no need for special measurements. </p>
<p> <i>${ZARAFA_QUOTA_NAME}</i></p>
<dl>
<dd>userquota template: The name of the user who exceeded his quota </p>
<p> companyquota template: The name of the tenant which exceeded its quota</dl>
<p> <i>${ZARAFA_QUOTA_FULLNAME}</i></p>
<dl>
<dd>userquota template: The fullname for the user who exceeded his quota </p>
<p> tenantquota template: The name of the tenant which exceeded its quota</dl>
<p> <i>${ZARAFA_QUOTA_COMPANY}</i></p>
<dl>
<dd>userquota template: The name of the tenant to which the user belongs </p>
<p> tenantquota template: The name of the tenant which exceeded its quota</dl>
<p> <i>${ZARAFA_QUOTA_STORE_SIZE}</i></p>
<dl>
<dd>userquota template: The total size of the user&#8217;s store </p>
<p> companyquota template: The total size of all stores (including the public store) which belong to this tenant </p>
<p> Note: The size unit (KB,MB) is part of the variable</dl>
<p> <i>${ZARAFA_QUOTA_WARN_SIZE}</i></p>
<dl>
<dd>The quota warning level </p>
<p> Note: The size unit (KB,MB) is part of the variable</dl>
<p> <i>${ZARAFA_QUOTA_SOFT_SIZE}</i></p>
<dl>
<dd>The quota soft level </p>
<p> Note: The size unit (KB,MB) is part of the variable</dl>
<p> <i>${ZARAFA_QUOTA_HARD_SIZE}</i></p>
<dl>
<dd>The quota hard limit </p>
<p> Note: The size unit (KB,MB) is part of the variable</dl>
</dl>
<h2>Reloading</h2>
<p>The following options are reloadable by sending the zarafa-monitor process a HUP signal: </p>
<p> log_level, mailquota_resend_interval, userquota_warning_template</p>
<dl>
<dd></dl>
<h2>Files</h2>
<p>/etc/zarafa/monitor.cfg</p>
<dl>
<dd>The Zarafa monitor configuration file.</dl>
<h2>Author</h2>
<p>Written by Zarafa.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-zarafa-monitor/">zarafa-monitor</a></code>(1) </p>
