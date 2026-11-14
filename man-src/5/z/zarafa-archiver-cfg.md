---
title: "zarafa-archiver-cfg(5)"
name: "zarafa-archiver-cfg"
section: "5"
letter: "z"
url: "/docs/linux/man/5-zarafa-archiver-cfg/"
description: "zarafa-archiver.cfg – The Zarafa archiver configuration file"
---

<p>zarafa-archiver.cfg &#8211; The Zarafa archiver configuration file</p>
<h2>Synopsis</h2>
<p><code>archiver.cfg</code></p>
<h2>Description</h2>
<p>The archiver.cfg is a configuration file for the Zarafa Archiver. archiver.cfg contains instructions for the software to set up the logging system and specific actions the archiver can do.</p>
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
<p><code>server_socket</code></p>
<dl>
<dd>Unix socket to find the connection to the Zarafa server. </p>
<p> Default: <i>file:///var/run/zarafa</i></dl>
<p> <code>sslkey_file</code></p>
<dl>
<dd>Use this file as key to logon to the server. This is only used when server_socket is set to an HTTPS transport. See the <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1) manual page on how to setup SSL keys. </p>
<p> Default: value not set.</dl>
<p> <code>sslkey_pass</code></p>
<dl>
<dd>The password of the SSL key file that is set in sslkey_file. </p>
<p> Default: value not set.</dl>
<p> <code>archive_enable</code></p>
<dl>
<dd>Specifies if the archive step will be performed. The archive step is basically the copy to the archive. </p>
<p> Default: <i>yes</i></dl>
<p> <code>archive_after</code></p>
<dl>
<dd>Specifies the age in days of a message before it will be archived. </p>
<p> Default: <i>30</i></dl>
<p> <code>stub_enable</code></p>
<dl>
<dd>Specifies if the stub step will be performed. Stubbing is the process of removing the data from a message and only leaving a reference to one or more archived versions of that message. When such a message is opened it will be de-stubbed on the fly, leaving the user with a normal message to work with. </p>
<p> A message will never be stubbed if it&#8217;s not yet archived. </p>
<p> Default: <i>no</i></dl>
<p> <code>stub_unread</code></p>
<dl>
<dd>Specifies if unread messages will be stubbed. </p>
<p> Default: <i>no</i></dl>
<p> <code>stub_after</code></p>
<dl>
<dd>Specifies the age in days of a message before it will be stubbed. </p>
<p> Default: <i>0</i></dl>
<p> <code>delete_enable</code></p>
<dl>
<dd>Specifies if the delete step will be performed. The delete step deletes messages from the users store if they&#8217;re old enough. This way even more space is freed. </p>
<p> A message will never be deleted if it&#8217;s not yet archived. </p>
<p> A message will never be deleted from the archive. </p>
<p> Default: <i>no</i></dl>
<p> <code>delete_unread</code></p>
<dl>
<dd>Specifies if unread messages will be deleted. </p>
<p> Default: <i>no</i></dl>
<p> <code>delete_after</code></p>
<dl>
<dd>Specifies the age in days of a message before it will be deleted. </p>
<p> Default: <i>0</i></dl>
<p> <code>purge_enable</code></p>
<dl>
<dd>Specifies if message will be purged from the archive after a certain amount of time. </p>
<p> Default: <i>no</i></dl>
<p> <code>purge_after</code></p>
<dl>
<dd>Specifies the age in days of a message before it will be purged. *Note that the age is measured from the time it was originally delivered in the primay store. </p>
<p> Default: <i>0</i></dl>
<p> <code>track_history</code></p>
<dl>
<dd>Specifies the behaviour of the archiver when re-archiving messages that were changed after they were archived. When track_history is set to no, the archived version will be updated to contain the most actual information. When track_history is set to yes, a new copy of the message will be created in the archive, and the previous version is linked to it. This way the change history can be tracked. </p>
<p> Default: <i>no</i></dl>
<p> <code>cleanup_action</code></p>
<dl>
<dd>Specify what action should be taken on archive messages whose primary message has been deleted. The options are &#8216;store&#8217; and &#8216;delete&#8217;, meaning store the archived message in a special &#8216;Deleted&#8217; folder or delete the archived messages respectively. </p>
<p> Default: <i>store</i></dl>
<p> <code>cleanup_follow_purge_after</code></p>
<dl>
<dd>Specify if items that are cleaned up from the archive are at least the age that is specified in the purge_after setting. This is to avoid messages being deleted from the archive when they where deleted from the primary store by a delete operation. Note that setting to yes, will cause a cleanup run to seemingly do nothing. A rule of thumb is to set this to the same value as delete_enable. So when delete_enable is set to yes, make sure cleanup_follow_purge_after is also set to yes. </p>
<p> Default: <i>no</i></dl>
<p> <code>enable_auto_attach</code></p>
<dl>
<dd>Specify whether on each archive run an auto-attach run is performed in order to match the attached archives to the requested state as specified in LDAP or ADS. </p>
<p> Default: <i>no</i></dl>
<p> <code>auto_attach_writable</code></p>
<dl>
<dd>Specify whether an auto attached archive will be granted write permissions for the user it&#8217;s attached to. </p>
<p> Default: <i>yes</i></dl>
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
<p> Default: <i>&#8211;</i></dl>
<p> <code>log_timestamp</code></p>
<dl>
<dd>Specify whether to prefix each log line with a timestamp in &#8216;file&#8217; logging mode. </p>
<p> Default: <i>1</i></dl>
<p> <code>log_level</code></p>
<dl>
<dd>The level of output for logging in the range from 0 to 5. 0 means no logging, 5 means full logging. </p>
<p> Default: <i>2</i></dl>
<p> <code>pid_file</code></p>
<dl>
<dd>The location of the pid file used to guarantee only one instance of zarafa-archiver is running in non-administrative mode. </p>
<p> Default: <i>/var/run/zarafa-archiver.pid </i></dl>
<h2>Explanation Of The Mysql Settings Parameters</h2>
<p><code>mysql_host</code></p>
<dl>
<dd>The hostname of the MySQL server to use. </p>
<p> Default: <i>localhost</i></dl>
<p> <code>mysql_port</code></p>
<dl>
<dd>The port of the MySQL server to use. </p>
<p> Default: <i>3306</i></dl>
<p> <code>mysql_user</code></p>
<dl>
<dd>The user under which we connect with MySQL. </p>
<p> Default: <i>root</i></dl>
<p> <code>mysql_password</code></p>
<dl>
<dd>The password to use for MySQL. Leave empty for no password. </p>
<p> Default:</dl>
<p> <code>mysql_socket</code></p>
<dl>
<dd>The socket of the MySQL server to use. This option can be used to override the default mysql socket. To use the socket, the mysql_host value must be empty or &#8216;localhost&#8217; </p>
<p> Default:</dl>
<p> <code>mysql_database</code></p>
<dl>
<dd>The MySQL database to connect to. </p>
<p> Default: <i>zarafa</i></dl>
<h2>Files</h2>
<p>/etc/zarafa/archiver.cfg</p>
<dl>
<dd>The Zarafa archiver configuration file.</dl>
<h2>Author</h2>
<p>Written by Zarafa.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-zarafa-archiver/">zarafa-archiver</a></code>(1) </p>
