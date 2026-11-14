---
title: "postsuper(1)"
name: "postsuper"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postsuper/"
description: "postsuper – Postfix superintendent"
---

<h2 class="name">NAME</h2>
<p> postsuper &#8211; Postfix superintendent </p>
<h2>SYNOPSIS</h2>
<p> <code>postsuper</code> [<code>-psSv</code>] [<code>-c </code><i>config_dir</i>] [<code>-d </code><i>queue_id</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-h&nbsp;</code><i>queue_id</i>]&nbsp;[<code>-H&nbsp;</code><i>queue_id</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>-r&nbsp;</code><i>queue_id</i>]&nbsp;[<i>directory &#8230;</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-postsuper/">postsuper</a></code>(1) command does maintenance jobs on the Postfix queue. Use of the command is restricted to the superuser. See the <code><a href="/docs/linux/man/1-postqueue/">postqueue</a></code>(1) command for unprivileged queue operations such as listing or flushing the mail queue. </p>
<p> By default, <code><a href="/docs/linux/man/1-postsuper/">postsuper</a></code>(1) performs the operations requested with the <code>-s</code> and <code>-p</code> command-line options on all Postfix queue directories &#8211; this includes the <code>incoming</code>, <code>active</code> and <code>deferred</code> directories with mail files and the <code>bounce</code>, <code>defer</code>, <code>trace</code> and <code>flush</code> directories with log files. </p>
<p> Options:</p>
<dl>
<dt><code>-c </code><i>config_dir</i></p>
<dd> The <code>main.cf</code> configuration file is in the named directory instead of the default configuration directory. See also the MAIL_CONFIG environment setting below.</p>
<dt><code>-d </code><i>queue_id</i></p>
<dd> Delete one message with the named queue ID from the named mail queue(s) (default: <code>hold</code>, <code>incoming</code>, <code>active</code> and <code>deferred</code>). </p>
<p> To delete multiple files, specify the <code>-d</code> option multiple times, or specify a <i>queue_id</i> of <code>&#8211;</code> to read queue IDs from standard input. For example, to delete all mail with exactly one recipient <code>user [at] example.com</code>: </p>
<pre><code>
mailq | tail - n + 2 | grep - v '^ *(' | awk  'BEGIN { RS = "" }
#$7 = sender, $8 = recipient1, $9 = recipient2
{
    if ($8 == "user [at] example.com" &amp;&amp; $9 == "")
        print $1
}
' | tr -d ' * !' | postsuper -d -
</code></pre>
<p> Specify &quot;<code>-d ALL</code>&quot; to remove all messages; for example, specify &quot;<code>-d ALL deferred</code>&quot; to delete all mail in the <code>deferred</code> queue. As a safety measure, the word <code>ALL</code> must be specified in upper case. </p>
<p> Warning: Postfix queue IDs are reused (always with Postfix &lt;= 2.8; and with Postfix &gt;= 2.9 when enable_long_queue_ids=no). There is a very small possibility that postsuper deletes the wrong message file when it is executed while the Postfix mail system is delivering mail. </p>
<p> The scenario is as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1)</p>
<dd> The Postfix queue manager deletes the message that <code><a href="/docs/linux/man/1-postsuper/">postsuper</a></code>(1) is asked to delete, because Postfix is finished with the message (it is delivered, or it is returned to the sender).</p>
<dt>2)</p>
<dd> New mail arrives, and the new message is given the same queue ID as the message that <code><a href="/docs/linux/man/1-postsuper/">postsuper</a></code>(1) is supposed to delete. The probability for reusing a deleted queue ID is about 1 in 2**15 (the number of different microsecond values that the system clock can distinguish within a second).</p>
<dt>3)</p>
<dd> <code><a href="/docs/linux/man/1-postsuper/">postsuper</a></code>(1) deletes the new message, instead of the old message that it should have deleted.</dl>
</dl>
<dt><code>-h </code><i>queue_id</i></p>
<dd> Put mail &quot;on hold&quot; so that no attempt is made to deliver it. Move one message with the named queue ID from the named mail queue(s) (default: <code>incoming</code>, <code>active</code> and <code>deferred</code>) to the <code>hold</code> queue. </p>
<p> To hold multiple files, specify the <code>-h</code> option multiple times, or specify a <i>queue_id</i> of <code>&#8211;</code> to read queue IDs from standard input. </p>
<p> Specify &quot;<code>-h ALL</code>&quot; to hold all messages; for example, specify &quot;<code>-h ALL deferred</code>&quot; to hold all mail in the <code>deferred</code> queue. As a safety measure, the word <code>ALL</code> must be specified in upper case. </p>
<p> Note: while mail is &quot;on hold&quot; it will not expire when its time in the queue exceeds the <code>maximal_queue_lifetime</code> or <code>bounce_queue_lifetime</code> setting. It becomes subject to expiration after it is released from &quot;hold&quot;. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<dt><code>-H </code><i>queue_id</i></p>
<dd> Release mail that was put &quot;on hold&quot;. Move one message with the named queue ID from the named mail queue(s) (default: <code>hold</code>) to the <code>deferred</code> queue. </p>
<p> To release multiple files, specify the <code>-H</code> option multiple times, or specify a <i>queue_id</i> of <code>&#8211;</code> to read queue IDs from standard input. </p>
<p> Note: specify &quot;<code>postsuper -r</code>&quot; to release mail that was kept on hold for a significant fraction of <code>$maximal_queue_lifetime</code> or <code>$bounce_queue_lifetime</code>, or longer. </p>
<p> Specify &quot;<code>-H ALL</code>&quot; to release all mail that is &quot;on hold&quot;. As a safety measure, the word <code>ALL</code> must be specified in upper case. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<dt><code>-p</code></p>
<dd> Purge old temporary files that are left over after system or software crashes.</p>
<dt><code>-r </code><i>queue_id</i></p>
<dd> Requeue the message with the named queue ID from the named mail queue(s) (default: <code>hold</code>, <code>incoming</code>, <code>active</code> and <code>deferred</code>). </p>
<p> To requeue multiple files, specify the <code>-r</code> option multiple times, or specify a <i>queue_id</i> of <code>&#8211;</code> to read queue IDs from standard input. </p>
<p> Specify &quot;<code>-r ALL</code>&quot; to requeue all messages. As a safety measure, the word <code>ALL</code> must be specified in upper case. </p>
<p> A requeued message is moved to the <code>maildrop</code> queue, from where it is copied by the <code><a href="/docs/linux/man/8-pickup/">pickup</a></code>(8) and <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemons to a new queue file. In many respects its handling differs from that of a new local submission.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> The message is not subjected to the smtpd_milters or non_smtpd_milters settings. When mail has passed through an external content filter, this would produce incorrect results with Milter applications that depend on original SMTP connection state information.</p>
<dt>&bull;</p>
<dd> The message is subjected again to mail address rewriting and substitution. This is useful when rewriting rules or virtual mappings have changed. </p>
<p> The address rewriting context (local or remote) is the same as when the message was received.</p>
<dt>&bull;</p>
<dd> The message is subjected to the same content_filter settings (if any) as used for new local mail submissions. This is useful when content_filter settings have changed.</dl>
</dl>
<dt>
<dd> Warning: Postfix queue IDs are reused (always with Postfix &lt;= 2.8; and with Postfix &gt;= 2.9 when enable_long_queue_ids=no). There is a very small possibility that <code><a href="/docs/linux/man/1-postsuper/">postsuper</a></code>(1) requeues the wrong message file when it is executed while the Postfix mail system is running, but no harm should be done. </p>
<p> This feature is available in Postfix 1.1 and later.</p>
<dt><code>-s</code></p>
<dd> Structure check and structure repair. This should be done once before Postfix startup.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Rename files whose name does not match the message file inode number. This operation is necessary after restoring a mail queue from a different machine or from backup, when queue files were created with Postfix &lt;= 2.8 or with &quot;enable_long_queue_ids = no&quot;.</p>
<dt>&bull;</p>
<dd> Move queue files that are in the wrong place in the file system hierarchy and remove subdirectories that are no longer needed. File position rearrangements are necessary after a change in the <code>hash_queue_names</code> and/or <code>hash_queue_depth</code> configuration parameters.</p>
<dt>&bull;</p>
<dd> Rename queue files created with &quot;enable_long_queue_ids = yes&quot; to short names, for migration to Postfix &lt;= 2.8. The procedure is as follows: </p>
<pre>
# postfix stop
# postconf enable_long_queue_ids=no
# postsuper
</pre>
<p> Run <code><a href="/docs/linux/man/1-postsuper/">postsuper</a></code>(1) repeatedly until it stops reporting file name changes.</dl>
</dl>
<dt><code>-S</code></p>
<dd> A redundant version of <code>-s</code> that requires that long file names also match the message file inode number. This option exists for testing purposes, and is available with Postfix 2.9 and later.</p>
<dt><code>-v</code></p>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose.</dl>
<h2>DIAGNOSTICS</h2>
<p> Problems are reported to the standard error stream and to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) or <code><a href="/docs/linux/man/8-postlogd/">postlogd</a></code>(8). </p>
<p> <code><a href="/docs/linux/man/1-postsuper/">postsuper</a></code>(1) reports the number of messages deleted with <code>-d</code>, the number of messages requeued with <code>-r</code>, and the number of messages whose queue file name was fixed with <code>-s</code>. The report is written to the standard error stream and to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) or <code><a href="/docs/linux/man/8-postlogd/">postlogd</a></code>(8).</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt>MAIL_CONFIG</p>
<dd> Directory with the <code>main.cf</code> file.</dl>
<h2>BUGS</h2>
<p> Mail that is not sanitized by Postfix (i.e. mail in the <code>maildrop</code> queue) cannot be placed &quot;on hold&quot;.</p>
<h2>CONFIGURATION PARAMETERS</h2>
<p> The following <code>main.cf</code> parameters are especially relevant to this program. The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>hash_queue_depth (1)</code></p>
<dd> The number of subdirectory levels for queue directories listed with the hash_queue_names parameter.</p>
<dt><code>hash_queue_names (deferred, defer)</code></p>
<dd> The names of queue directories that are split across multiple subdirectory levels.</p>
<dt><code>import_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The list of environment parameters that a privileged Postfix process will import from a non-Postfix parent process, or name=value environment overrides.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of the Postfix top-level queue directory.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd> The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd> A prefix that is prepended to the process name in syslog records, so that, for example, &quot;smtpd&quot; becomes &quot;prefix/smtpd&quot;.</dl>
<p> Available in Postfix version 2.9 and later:</p>
<dl>
<dt><code>enable_long_queue_ids (no)</code></p>
<dd> Enable long, non-repeating, queue IDs (queue file names).</dl>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-sendmail/">sendmail</a>(1), Sendmail-compatible user interface
<a href="//www.systutorials.com/docs/linux/man/1-postqueue/">postqueue</a>(1), unprivileged queue operations
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
