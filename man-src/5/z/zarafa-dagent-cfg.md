---
title: "zarafa-dagent-cfg(5)"
name: "zarafa-dagent-cfg"
section: "5"
letter: "z"
url: "/docs/linux/man/5-zarafa-dagent-cfg/"
description: "zarafa-dagent.cfg – The Zarafa dagent configuration file"
---

<p>zarafa-dagent.cfg &#8211; The Zarafa dagent configuration file</p>
<h2>Synopsis</h2>
<p><code>dagent.cfg</code></p>
<h2>Description</h2>
<p>The dagent.cfg is a configuration file for the Zarafa Dagent. dagent.cfg contains instructions for the software to set up the logging system and LMTP settings.</p>
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
<h2>Explanation Of Each Parameter</h2>
<p><code>server_bind</code></p>
<dl>
<dd>IP address to bind to. 0.0.0.0 for any address. </p>
<p> Default: <i>0.0.0.0</i></dl>
<p> <code>server_socket</code></p>
<dl>
<dd>Unix socket to find the connection to the Zarafa server. </p>
<p> Default: <i>file:///var/run/zarafa</i></dl>
<p> <code>run_as_user</code></p>
<dl>
<dd>After correctly starting, the dagent process will become this user, dropping root privileges. Note that the log file needs to be writeable by this user, and the directory too to create new logfiles after logrotation. This can also be achieved by setting the correct group and permissions. </p>
<p> Default value is empty, not changing the user after starting.</dl>
<p> <code>run_as_group</code></p>
<dl>
<dd>After correctly starting, the dagent process will become this group, dropping root privileges. </p>
<p> Default value is empty, not changing the group after starting.</dl>
<p> <code>pid_file</code></p>
<dl>
<dd>Write the process ID number to this file. This is used by the init.d script to correctly stop/restart the service. </p>
<p> Default: <i>/var/run/zarafa-dagent.pid</i></dl>
<p> <code>sslkey_file</code></p>
<dl>
<dd>Use this file as key to logon to the server. This is only used when server_socket is set to an HTTPS transport. See the <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1) manual page on how to setup SSL keys. </p>
<p> Default: value not set.</dl>
<p> <code>sslkey_pass</code></p>
<dl>
<dd>The password of the SSL key file that is set in sslkey_file. </p>
<p> Default: value not set.</dl>
<p> <code>lmtp_port</code></p>
<dl>
<dd>Port to listen to for LMTP requests </p>
<p> Default: <i>2003</i></dl>
<p> <code>lmtp_max_threads</code></p>
<dl>
<dd>The maximum number of LMTP threads that can be running simultaneously. This is also limited by your SMTP server. (20 is the postfix default concurrency limit) </p>
<p> Default: <i>20</i></dl>
<p> <code>spam_header_name</code></p>
<dl>
<dd>To detect if the receiving mail is spam, the DAgent can check this header for a value that is in there. This name is case insensitive. If this option is empty, the detection method will be turned off. You can also force a delivery to the Junk Mail folder using the <i>-j</i> commandline option. </p>
<p> Default: <i>X-Spam-Status</i></dl>
<p> <code>spam_header_value</code></p>
<dl>
<dd>When this value is found in the <i>spam_header_name</i>, the mail will be considered spam, and will be delivered in the user&#8217;s Junk Mail folder. The value can be anywhere in the header, not just the start. The value is case insensitive. </p>
<p> Default: <i>Yes,</i></dl>
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
<p> Default: <i>/var/log/zarafa/dagent.log</i></dl>
<p> <code>log_timestamp</code></p>
<dl>
<dd>Specify whether to prefix each log line with a timestamp in &#8216;file&#8217; logging mode. </p>
<p> Default: <i>1</i></dl>
<p> <code>log_level</code></p>
<dl>
<dd>The level of output for logging in the range from 0 to 5. 0 means no logging, 5 means full logging. </p>
<p> Default: <i>2</i></dl>
<p> <code>log_raw_message</code></p>
<dl>
<dd>Log the raw message to a file. The file is saved to the location specifed in <code>log_raw_message_path</code>. </p>
<p> Default: <i>no</i></dl>
<p> <code>log_raw_message_path</code></p>
<dl>
<dd>Path to save the raw message. </p>
<p> Default: <i>/tmp</i></dl>
<p> <code>archive_on_delivery</code></p>
<dl>
<dd>Archive incoming message on delivery. If an archive is attached to the target mailbox, the message will immediately be archived upon delivery. </p>
<p> Rules will be processed before the message is archived, so when a rule moves the message to an alternate location, the archived message will be placed in the correct location in the archive. When the incoming message is copied by a rule, only the original message is archived. </p>
<p> Default: <i>no</i></dl>
<p> <code>mr_autoaccepter</code></p>
<dl>
<dd>Zarafa-dagent can auto-accept meeting requests if the mr-accept option is enabled for a user. When this option is enabled and a meeting request or meeting cancellation is received, this script is started with the following parameters: /usr/bin/zarafa-mr-accept &lt;username&gt; &lt;/path/to/dagent.cfg&gt; [&lt;ENTRYID&gt;]. </p>
<p> If the script is successful (exitcode is 0), then no other actions are performed (eg rules or vacation messages) and the message is not delivered in the inbox. If the script exits with a non-zero exit code, rules and vacation messages are run as usual, and the message is delivered in the inbox (or other folder, depending on rules or options). </p>
<p> Default: <i>/usr/bin/zarafa-mr-accept</i></dl>
<p> <code>plugin_enabled</code></p>
<dl>
<dd>Enable or disable the dagent plugin framework. </p>
<p> Default: <i>yes</i></dl>
<p> <code>plugin_manager_path</code></p>
<dl>
<dd>The path to the dagent plugin manager. </p>
<p> Default: <i>/usr/share/zarafa-dagent/python</i></dl>
<p> <code>plugin_path</code></p>
<dl>
<dd>Path to the activated dagent plugins. This folder contains symlinks to the zarafa plugins and custom scripts. The plugins are installed in <i>/usr/share/zarafa-dagent/python/plugins</i>. To activate a plugin create a symbolic link in the <i>plugin_path</i> directory. </p>
<p> Example: </p>
<p> <code>ln</code><code>-s</code><i>/usr/share/zarafa-dagent/python/plugins/BMP2PNG.py</i><i>/var/lib/zarafa/dagent/plugins/BMP2PNG.py</i> </p>
<p> Default: <i>/var/lib/zarafa/dagent/plugins</i></dl>
<p> <code>default_charset</code></p>
<dl>
<dd>Some emails do not contain any charset information or specify us-ascii even though it isn&#8217;t. In both cases, dagent will assume the following charset is used. Note that this implies that the given charset should be a superset of us-ascii (most charsets are). </p>
<p> Default: <i>iso-8859-15</i></dl>
<p> <code>set_rule_headers</code></p>
<dl>
<dd>Enable the addition of X-Zarafa-Rule-Action headers on messages that have been forwarded or replied by a rule. </p>
<p> Default: <i>yes</i></dl>
<p> <code>no_double_forward</code></p>
<dl>
<dd>Enable this option to prevent rules to cause a loop. An e-mail can only be forwarded once. When this option is enabled, the set_rule_headers option must also be enabled. </p>
<p> Default: <i>no</i></dl>
<h2>Reloading</h2>
<p>The following options are reloadable by sending the zarafa-dagent process a HUP signal: </p>
<p> log_level</p>
<dl>
<dd></dl>
<p> archive_on_delivery</p>
<dl>
<dd></dl>
<p> mr_autoaccepter</p>
<dl>
<dd></dl>
<h2>Files</h2>
<p>/etc/zarafa/dagent.cfg</p>
<dl>
<dd>The Zarafa dagent configuration file.</dl>
<h2>Author</h2>
<p>Written by Zarafa.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-zarafa-dagent/">zarafa-dagent</a></code>(1) </p>
