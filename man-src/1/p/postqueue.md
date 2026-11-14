---
title: "postqueue(1)"
name: "postqueue"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postqueue/"
description: "postqueue – Postfix queue control"
---

<h2 class="name">NAME</h2>
<p> postqueue &#8211; Postfix queue control </p>
<h2>SYNOPSIS</h2>
<pre><code>

To flush the mail queue : postqueue[-v][-c config_dir] - f postqueue[-v][-c config_dir] - i queue_id postqueue[-v][-c config_dir] - s site

                                                                                                                                        To list the mail queue : postqueue[-v][-c config_dir] -
                                                                                                                                                                 j
                                                                                                                                                                     postqueue[-v][-c config_dir] -
                                                                                                                                                                 p
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-postqueue/">postqueue</a></code>(1) command implements the Postfix user interface for queue management. It implements operations that are traditionally available via the <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command. See the <code><a href="/docs/linux/man/1-postsuper/">postsuper</a></code>(1) command for queue operations that require super-user privileges such as deleting a message from the queue or changing the status of a message. </p>
<p> The following options are recognized:</p>
<dl>
<dt><code>-c </code><i>config_dir</i></p>
<dd> The <code>main.cf</code> configuration file is in the named directory instead of the default configuration directory. See also the MAIL_CONFIG environment setting below.</p>
<dt><code>-f</code></p>
<dd> Flush the queue: attempt to deliver all queued mail. </p>
<p> This option implements the traditional &quot;<code>sendmail -q</code>&quot; command, by contacting the Postfix <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8) daemon. </p>
<p> Warning: flushing undeliverable mail frequently will result in poor delivery performance of all other mail.</p>
<dt><code>-i </code><i>queue_id</i></p>
<dd> Schedule immediate delivery of deferred mail with the specified queue ID. </p>
<p> This option implements the traditional <code>sendmail -qI</code> command, by contacting the <code><a href="/docs/linux/man/8-flush/">flush</a></code>(8) server. </p>
<p> This feature is available with Postfix version 2.4 and later.</p>
<dt><code>-j</code></p>
<dd> Produce a queue listing in JSON format, based on output from the <a href="/docs/linux/man/8-showq/">showq</a>(8) daemon. The result is a stream of zero or more JSON objects, one per queue file. Each object is followed by a newline character to support simple streaming parsers. See &quot;<code>JSON OBJECT FORMAT</code>&quot; below for details. </p>
<p> This feature is available in Postfix 3.1 and later.</p>
<dt><code>-p</code></p>
<dd> Produce a traditional sendmail-style queue listing. This option implements the traditional <code>mailq</code> command, by contacting the Postfix <code><a href="/docs/linux/man/8-showq/">showq</a></code>(8) daemon. </p>
<p> Each queue entry shows the queue file ID, message size, arrival time, sender, and the recipients that still need to be delivered. If mail could not be delivered upon the last attempt, the reason for failure is shown. The queue ID string is followed by an optional status character:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>*</code></p>
<dd> The message is in the <code>active</code> queue, i.e. the message is selected for delivery.</p>
<dt><code>!</code></p>
<dd> The message is in the <code>hold</code> queue, i.e. no further delivery attempt will be made until the mail is taken off hold.</dl>
</dl>
<dt><code>-s </code><i>site</i></p>
<dd> Schedule immediate delivery of all mail that is queued for the named <i>site</i>. A numerical site must be specified as a valid RFC 5321 address literal enclosed in [], just like in email addresses. The site must be eligible for the &quot;fast flush&quot; service. See <code><a href="/docs/linux/man/8-flush/">flush</a></code>(8) for more information about the &quot;fast flush&quot; service. </p>
<p> This option implements the traditional &quot;<code>sendmail -qR</code><i>site</i>&quot; command, by contacting the Postfix <code><a href="/docs/linux/man/8-flush/">flush</a></code>(8) daemon.</p>
<dt><code>-v</code></p>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose. As of Postfix 2.3, this option is available for the super-user only.</dl>
<h2>JSON OBJECT FORMAT</h2>
<p> Each JSON object represents one queue file; it is emitted as a single text line followed by a newline character. </p>
<p> Object members have string values unless indicated otherwise. Programs should ignore object members that are not listed here; the list of members is expected to grow over time.</p>
<dl>
<dt><code>queue_name</code></p>
<dd> The name of the queue where the message was found. Note that the contents of the mail queue may change while it is being listed; some messages may appear more than once, and some messages may be missed.</p>
<dt><code>queue_id</code></p>
<dd> The queue file name. The queue_id may be reused within a Postfix instance unless &quot;enable_long_queue_ids = true&quot; and time is monotonic. Even then, the queue_id is not expected to be unique between different Postfix instances. Management tools that require a unique name should combine the queue_id with the myhostname setting of the Postfix instance.</p>
<dt><code>arrival_time</code></p>
<dd> The number of seconds since the start of the UNIX epoch.</p>
<dt><code>message_size</code></p>
<dd> The number of bytes in the message header and body. This number does not include message envelope information. It is approximately equal to the number of bytes that would be transmitted via SMTP including the &lt;CR&gt;&lt;LF&gt; line endings.</p>
<dt><code>sender</code></p>
<dd> The envelope sender address.</p>
<dt><code>recipients</code></p>
<dd> An array containing zero or more objects with members:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>address</code></p>
<dd> One recipient address.</p>
<dt><code>delay_reason</code></p>
<dd> If present, the reason for delayed delivery. Delayed recipients may have no delay reason, for example, while delivery is in progress, or after the system was stopped before it could record the reason.</dl>
</dl>
</dl>
<h2>SECURITY</h2>
<p> This program is designed to run with set-group ID privileges, so that it can connect to Postfix daemon processes.</p>
<h2>STANDARDS</h2>
<pre>
RFC 7159 (JSON notation)
</pre>
<h2>DIAGNOSTICS</h2>
<p> Problems are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) or <code><a href="/docs/linux/man/8-postlogd/">postlogd</a></code>(8), and to the standard error stream.</p>
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
<dt><code>command_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of all postfix administrative commands.</p>
<dt><code>fast_flush_domains ($relay_domains)</code></p>
<dd> Optional list of destinations that are eligible for per-destination logfiles with mail that is queued to those destinations.</p>
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
<dt><code>authorized_flush_users (static:anyone)</code></p>
<dd> List of users who are authorized to flush the queue.</p>
<dt><code>authorized_mailq_users (static:anyone)</code></p>
<dd> List of users who are authorized to view the queue.</dl>
<h2>FILES</h2>
<pre>
/var/spool/postfix, mail queue
</pre>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), queue manager
<a href="//www.systutorials.com/docs/linux/man/8-showq/">showq</a>(8), list mail queue
<a href="//www.systutorials.com/docs/linux/man/8-flush/">flush</a>(8), fast flush service
<a href="//www.systutorials.com/docs/linux/man/1-sendmail/">sendmail</a>(1), Sendmail-compatible user interface
<a href="//www.systutorials.com/docs/linux/man/1-postsuper/">postsuper</a>(1), privileged queue operations
<a href="//www.systutorials.com/docs/linux/man/8-postlogd/">postlogd</a>(8), Postfix logging
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging
</pre>
<h2>README FILES</h2>
<p> Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>
ETRN_README, Postfix ETRN howto
</pre>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>HISTORY</h2>
<p> The postqueue command was introduced with Postfix version 1.1.</p>
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
