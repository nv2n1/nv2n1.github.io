---
title: "postdrop(1)"
name: "postdrop"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postdrop/"
description: "postdrop – Postfix mail posting utility"
---

<h2 class="name">NAME</h2>
<p> postdrop &#8211; Postfix mail posting utility </p>
<h2>SYNOPSIS</h2>
<pre><code>
postdrop[-rv][-c config_dir]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-postdrop/">postdrop</a></code>(1) command creates a file in the <code>maildrop</code> directory and copies its standard input to the file. </p>
<p> Options:</p>
<dl>
<dt><code>-c </code><i>config_dir</i></p>
<dd> The <code>main.cf</code> configuration file is in the named directory instead of the default configuration directory. See also the MAIL_CONFIG environment setting below.</p>
<dt><code>-r</code></p>
<dd> Use a Postfix-internal protocol for reading the message from standard input, and for reporting status information on standard output. This is currently the only supported method.</p>
<dt><code>-v</code></p>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose. As of Postfix 2.3, this option is available for the super-user only.</dl>
<h2>SECURITY</h2>
<p> The command is designed to run with set-group ID privileges, so that it can write to the <code>maildrop</code> queue directory and so that it can connect to Postfix daemon processes.</p>
<h2>DIAGNOSTICS</h2>
<p> Fatal errors: malformed input, I/O error, out of memory. Problems are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) or <code><a href="/docs/linux/man/8-postlogd/">postlogd</a></code>(8) and to the standard error stream. When the input is incomplete, or when the process receives a HUP, INT, QUIT or TERM signal, the queue file is deleted.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>MAIL_CONFIG</p>
<dd> Directory with the <code>main.cf</code> file. In order to avoid exploitation of set-group ID privileges, a non-standard directory is allowed only if:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The name is listed in the standard <code>main.cf</code> file with the <code>alternate_config_directories</code> configuration parameter.</p>
<dt>&bull;</p>
<dd> The command is invoked by the super-user.</dl>
</dl>
</dl>
<h2>CONFIGURATION PARAMETERS</h2>
<p> The following <code>main.cf</code> parameters are especially relevant to this program. The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>alternate_config_directories (empty)</code></p>
<dd> A list of non-default Postfix configuration directories that may be specified with &quot;-c config_directory&quot; on the command line (in the case of <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1), with the &quot;-C&quot; option), or via the MAIL_CONFIG environment parameter.</p>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>import_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The list of environment parameters that a privileged Postfix process will import from a non-Postfix parent process, or name=value environment overrides.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of the Postfix top-level queue directory.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd> The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd> A prefix that is prepended to the process name in syslog records, so that, for example, &quot;smtpd&quot; becomes &quot;prefix/smtpd&quot;.</p>
<dt><code>trigger_timeout (10s)</code></p>
<dd> The time limit for sending a trigger to a Postfix daemon (for example, the <code><a href="/docs/linux/man/8-pickup/">pickup</a></code>(8) or <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8) daemon).</dl>
<p> Available in Postfix version 2.2 and later:</p>
<dl>
<dt><code>authorized_submit_users (static:anyone)</code></p>
<dd> List of users who are authorized to submit mail with the <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command (and with the privileged <code><a href="/docs/linux/man/1-postdrop/">postdrop</a></code>(1) helper command).</dl>
<h2>FILES</h2>
<pre>
/var/spool/postfix/maildrop, maildrop queue
</pre>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-sendmail/">sendmail</a>(1), compatibility interface
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/8-postlogd/">postlogd</a>(8), Postfix logging
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging
</pre>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>AUTHOR(S)</h2>
<pre>
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA
</pre>
<h2>Index</h2>
