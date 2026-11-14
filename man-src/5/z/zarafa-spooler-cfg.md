---
title: "zarafa-spooler-cfg(5)"
name: "zarafa-spooler-cfg"
section: "5"
letter: "z"
url: "/docs/linux/man/5-zarafa-spooler-cfg/"
description: "zarafa-spooler.cfg – The Zarafa spooler configuration file"
---

<p>zarafa-spooler.cfg &#8211; The Zarafa spooler configuration file</p>
<h2>Synopsis</h2>
<p><code>spooler.cfg</code></p>
<h2>Description</h2>
<p>The spooler.cfg is a configuration file for the Zarafa Spooler. spooler.cfg contains instructions for the software to set up the logging system and outgoing smtp relay server.</p>
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
<p><code>smtp_server</code></p>
<dl>
<dd>Hostname or IP address of the outgoing SMTP server. This server needs to relay mail for your server. </p>
<p> Default: <i>localhost</i></dl>
<p> <code>smtp_port</code></p>
<dl>
<dd>TCP Port number for smtp_server. </p>
<p> Default: <i>25</i></dl>
<p> <code>server_socket</code></p>
<dl>
<dd>Unix socket to find the connection to the Zarafa server. </p>
<p> Default: <i>file:///var/run/zarafa</i></dl>
<p> <code>run_as_user</code></p>
<dl>
<dd>After correctly starting, the spooler process will become this user, dropping root privileges. Note that the log file needs to be writeable by this user, and the directory too to create new logfiles after logrotation. This can also be achieved by setting the correct group and permissions. </p>
<p> Default value is empty, not changing the user after starting.</dl>
<p> <code>run_as_group</code></p>
<dl>
<dd>After correctly starting, the spooler process will become this group, dropping root privileges. </p>
<p> Default value is empty, not changing the group after starting.</dl>
<p> <code>pid_file</code></p>
<dl>
<dd>Write the process ID number to this file. This is used by the init.d script to correctly stop/restart the service. </p>
<p> Default: <i>/var/run/zarafa-spooler.pid</i></dl>
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
<p> Default: <i>/var/log/zarafa/spooler.log</i></dl>
<p> <code>log_timestamp</code></p>
<dl>
<dd>Specify whether to prefix each log line with a timestamp in &#8216;file&#8217; logging mode. </p>
<p> Default: <i>1</i></dl>
<p> <code>log_level</code></p>
<dl>
<dd>The level of output for logging in the range from 0 to 5. 0 means no logging, 5 means full logging. </p>
<p> Default: <i>2</i></dl>
<p> <code>max_threads</code></p>
<dl>
<dd>The maximum number of threads used to send outgoing messages. For each email in the outgoing queue a seperate thread will be started in order to allow multiple emails to be send out simultaneously. </p>
<p> Default: <i>5</i></dl>
<p> <code>fax_domain</code></p>
<dl>
<dd>When an email is sent to a contact with a FAX type email address, the address will be rewritten to a normal SMTP address, using the scheme: &lt;faxnumber&gt;@&lt;fax_domain&gt;. You can install software in your SMTP server which handles these email addresses to actually fax the message to that number. </p>
<p> Default:</dl>
<p> <code>fax_international</code></p>
<dl>
<dd>When sending an international fax, the number will start with a &#8216;+&#8217; sign. You can rewrite this to the digits you need to dial when dialing to another country. </p>
<p> Default: <i>+</i></dl>
<p> <code>always_send_delegates</code></p>
<dl>
<dd>Normally, a user needs to give explicit rights to other users to be able to send under their name. When setting this value to &#8216;yes&#8217;, the spooler will not check these permissions, and will always send the email with &#8216;On behalf of&#8217; headers. This was the default behaviour in installations before Zarafa 6.20. Please note that this feature overrides &#8216;send-as&#8217; functionality. </p>
<p> Default: <i>no</i></dl>
<p> <code>always_send_tnef</code></p>
<dl>
<dd>Since Zarafa 6.30, meeting requests will be sent using iCalendar files. This adds compatibility to more calendar programs. To use the previous TNEF (winmail.dat) method, set this option to &#8216;yes&#8217;. </p>
<p> When an email body is written in RTF text, normally this data is sent using TNEF. If you want to send an HTML representation of the email instead and not use TNEF, set this to &#8216;minimal&#8217;. </p>
<p> Default: <i>no</i></dl>
<p> <code>always_send_utf8</code></p>
<dl>
<dd>E-mails can be sent in any charset that the e-mail was written in. It may be desirable to always send in the UTF-8 charset, which may be more widely supported. To enable e-mail to always be sent in the utf-8 charset, set this option to &#8216;yes&#8217;. </p>
<p> Default: <i>no</i></dl>
<p> <code>enable_dsn</code></p>
<dl>
<dd>Enable the Delivery Status Notifications (DSN) for users. If a user requests a DSN the spooler sends the request to the MTA and when the MTA support this the user will receive the report in the mailbox. When the MTA doesn&#8217;t support DSN the user will not receive a report. Ensure you have a supported MTA like postfix 2.3 and higher. If DSN is disabled and the user request a DSN then it will be ignored and the delivery report is not sent. </p>
<p> Default: <i>yes</i></dl>
<p> <code>charset_upgrade</code></p>
<dl>
<dd>Upgrades the us-ascii charset to this charset. This makes sure high-characters in recipients and attachment filenames are correctly sent when the body is in plain text. Not used when always_send_utf8 is enabled. </p>
<p> Default: <i>windows-1252</i></dl>
<p> <code>allow_redirect_spoofing</code></p>
<dl>
<dd>Normally, users are not allowed to send e-mail from a different e-mail address than their own. However, the &#8216;redirect&#8217; rule sends e-mails with their original &#8216;from&#8217; address. Enabling this option allows redirected e-mails to be sent with their original &#8216;from&#8217; e-mail address. </p>
<p> Default: <i>yes</i></dl>
<p> <code>copy_delegate_mails</code></p>
<dl>
<dd>Make a copy of the sent mail of delegates in the sent items folder of the representee. This is done for both delegate and send-as e-mails. </p>
<p> Default: <i>yes</i></dl>
<p> <code>allow_delegate_meeting_request</code></p>
<dl>
<dd>Normally, users are not allowed to send meeting requests as external delegate. However, when you want to forward meeting requests you need delegate permissions. Enabling this option allows you to sent and forward a meeting request as a delegate Zarafa and SMTP user. </p>
<p> Default: <i>yes</i></dl>
<p> <code>allow_send_to_everyone</code></p>
<dl>
<dd>When set to &#8216;no&#8217;, sending to the &#8216;everyone&#8217; group is disallowed. The entire message will be bounced if this is attempted. When set to &#8216;yes&#8217;, this allows sending to all users in the &#8216;everyone&#8217; group. </p>
<p> Default: <i>yes</i></dl>
<p> <code>expand_groups</code></p>
<dl>
<dd>Expand groups in headers of sent e-mails. This means that the recipient of an e-mail with one or more groups as recipients will see the members of the groups instead of the groups themselves. If a group has an e-mail address, the group is not expanded irrespective of this setting, since having an e-mail address for the group implies that this address can be used to send messages to the group. </p>
<p> Default: <i>no</i></dl>
<p> <code>archive_on_send</code></p>
<dl>
<dd>Archive outgoing messages. If an archive is attached to the mailbox from which a message is send, the message will immediately be archived to the special Outgoing folder. </p>
<p> Messages that are archived this way are not attached to the original message in the primary store. So there&#8217;s no easy way to find the original sent item based on an archive or find an archive based on the sent item in the primary store. This option is only intended to make sure all outgoing messages are stored without the possibility for the owner to delete them. </p>
<p> Default: <i>no</i></dl>
<p> <code>plugin_enabled</code></p>
<dl>
<dd>Enable or disable the spooler plugin framework. </p>
<p> Default: <i>yes</i></dl>
<p> <code>plugin_manager_path</code></p>
<dl>
<dd>The path to the spooler plugin manager. </p>
<p> Default: <i>/usr/share/zarafa-spooler/python</i></dl>
<p> <code>plugin_path</code></p>
<dl>
<dd>Path to the activated spooler plugins. This folder contains symlinks to the zarafa plugins and custom scripts. The plugins are installed in <i>/usr/share/zarafa-spooler/python/plugins</i>. To activate a plugin create a symbolic link in the <i>plugin_path</i> directory. </p>
<p> Example: </p>
<p> <code>ln</code><code>-s</code><i>/usr/share/zarafa-spooler/python/plugins/BMP2PNG.py</i><i>/var/lib/zarafa/spooler/plugins/BMP2PNG.py</i> </p>
<p> Default: <i>/var/lib/zarafa/spooler/plugins</i></dl>
<h2>Reloading</h2>
<p>The following options are reloadable by sending the zarafa-spooler process a HUP signal: </p>
<p> log_level, max_threads, archive_on_send</p>
<dl>
<dd></dl>
<h2>Files</h2>
<p>/etc/zarafa/spooler.cfg</p>
<dl>
<dd>The Zarafa spooler configuration file.</dl>
<h2>Author</h2>
<p>Written by Zarafa.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-zarafa-spooler/">zarafa-spooler</a></code>(1) </p>
