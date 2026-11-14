---
title: "sendmail(1)"
name: "sendmail"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sendmail/"
description: "sendmail – Postfix to Sendmail compatibility interface"
---

<h2 class="name">NAME</h2>
<p> sendmail &#8211; Postfix to Sendmail compatibility interface </p>
<h2>SYNOPSIS</h2>
<pre><code>
sendmail[option...][recipient...] mailq
        sendmail -
    bp
        newaliases
            sendmail -
    I
</code></pre>
<h2>DESCRIPTION</h2>
<p> The Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command implements the Postfix to Sendmail compatibility interface. For the sake of compatibility with existing applications, some Sendmail command-line options are recognized but silently ignored. </p>
<p> By default, Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) reads a message from standard input until EOF or until it reads a line with only a <code>.</code> character, and arranges for delivery. Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) relies on the <code><a href="/docs/linux/man/1-postdrop/">postdrop</a></code>(1) command to create a queue file in the <code>maildrop</code> directory. </p>
<p> Specific command aliases are provided for other common modes of operation:</p>
<dl>
<dt><code>mailq</code></p>
<dd> List the mail queue. Each entry shows the queue file ID, message size, arrival time, sender, and the recipients that still need to be delivered. If mail could not be delivered upon the last attempt, the reason for failure is shown. The queue ID string is followed by an optional status character:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>*</code></p>
<dd> The message is in the <code>active</code> queue, i.e. the message is selected for delivery.</p>
<dt><code>!</code></p>
<dd> The message is in the <code>hold</code> queue, i.e. no further delivery attempt will be made until the mail is taken off hold.</dl>
</dl>
<dt>
<dd> This mode of operation is implemented by executing the <code><a href="/docs/linux/man/1-postqueue/">postqueue</a></code>(1) command.</p>
<dt><code>newaliases</code></p>
<dd> Initialize the alias database. If no input file is specified (with the <code>-oA</code> option, see below), the program processes the file(s) specified with the <code>alias_database</code> configuration parameter. If no alias database type is specified, the program uses the type specified with the <code>default_database_type</code> configuration parameter. This mode of operation is implemented by running the <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) command. </p>
<p> Note: it may take a minute or so before an alias database update becomes visible. Use the &quot;<code>postfix reload</code>&quot; command to eliminate this delay.</dl>
<p> These and other features can be selected by specifying the appropriate combination of command-line options. Some features are controlled by parameters in the <code>main.cf</code> configuration file. </p>
<p> The following options are recognized:</p>
<dl>
<dt><code>-Am</code> (ignored)</p>
<dd>
<dt><code>-Ac</code> (ignored)</p>
<dd> Postfix sendmail uses the same configuration file regardless of whether or not a message is an initial submission.</p>
<dt><code>-B </code><i>body_type</i></p>
<dd> The message body MIME type: <code>7BIT</code> or <code>8BITMIME</code>.</p>
<dt><code>-bd</code></p>
<dd> Go into daemon mode. This mode of operation is implemented by executing the &quot;<code>postfix start</code>&quot; command.</p>
<dt><code>-bh</code> (ignored)</p>
<dd>
<dt><code>-bH</code> (ignored)</p>
<dd> Postfix has no persistent host status database.</p>
<dt><code>-bi</code></p>
<dd> Initialize alias database. See the <code>newaliases</code> command above.</p>
<dt><code>-bl</code></p>
<dd> Go into daemon mode. To accept only local connections as with Sendmail&#8217;s <code>-bl</code> option, specify &quot;<code>inet_interfaces = loopback</code>&quot; in the Postfix <code>main.cf</code> configuration file.</p>
<dt><code>-bm</code></p>
<dd> Read mail from standard input and arrange for delivery. This is the default mode of operation.</p>
<dt><code>-bp</code></p>
<dd> List the mail queue. See the <code>mailq</code> command above.</p>
<dt><code>-bs</code></p>
<dd> Stand-alone SMTP server mode. Read SMTP commands from standard input, and write responses to standard output. In stand-alone SMTP server mode, mail relaying and other access controls are disabled by default. To enable them, run the process as the <code>mail_owner</code> user. </p>
<p> This mode of operation is implemented by running the <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) daemon.</p>
<dt><code>-bv</code></p>
<dd> Do not collect or deliver a message. Instead, send an email report after verifying each recipient address. This is useful for testing address rewriting and routing configurations. </p>
<p> This feature is available in Postfix version 2.1 and later.</p>
<dt><code>-C </code><i>config_file</i></p>
<dd>
<dt><code>-C </code><i>config_dir</i></p>
<dd> The path name of the Postfix <code>main.cf</code> file, or of its parent directory. This information is ignored with Postfix versions before 2.3. </p>
<p> With Postfix version 3.2 and later, a non-default directory must be authorized in the default <code>main.cf</code> file, through the alternate_config_directories or multi_instance_directories parameters. </p>
<p> With all Postfix versions, you can specify a directory pathname with the MAIL_CONFIG environment variable to override the location of configuration files.</p>
<dt><code>-F </code><i>full_name</i></p>
<dd> Set the sender full name. This overrides the NAME environment variable, and is used only with messages that have no <code>From:</code> message header.</p>
<dt><code>-f </code><i>sender</i></p>
<dd> Set the envelope sender address. This is the address where delivery problems are sent to. With Postfix versions before 2.1, the <code>Errors-To:</code> message header overrides the error return address.</p>
<dt><code>-G</code></p>
<dd> Gateway (relay) submission, as opposed to initial user submission. Either do not rewrite addresses at all, or update incomplete addresses with the domain information specified with <code>remote_header_rewrite_domain</code>. </p>
<p> This option is ignored before Postfix version 2.3.</p>
<dt><code>-h </code><i>hop_count</i> (ignored)</p>
<dd> Hop count limit. Use the <code>hopcount_limit</code> configuration parameter instead.</p>
<dt><code>-I</code></p>
<dd> Initialize alias database. See the <code>newaliases</code> command above.</p>
<dt><code>-i</code></p>
<dd> When reading a message from standard input, don&#8217;t treat a line with only a <code>.</code> character as the end of input.</p>
<dt><code>-L </code><i>label</i> (ignored)</p>
<dd> The logging label. Use the <code>syslog_name</code> configuration parameter instead.</p>
<dt><code>-m</code> (ignored)</p>
<dd> Backwards compatibility.</p>
<dt><code>-N </code><i>dsn</i> (default: &#8216;delay, failure&#8217;)</p>
<dd> Delivery status notification control. Specify either a comma-separated list with one or more of <code>failure</code> (send notification when delivery fails), <code>delay</code> (send notification when delivery is delayed), or <code>success</code> (send notification when the message is delivered); or specify <code>never</code> (don&#8217;t send any notifications at all). </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<dt><code>-n</code> (ignored)</p>
<dd> Backwards compatibility.</p>
<dt><code>-oA</code><i>alias_database</i></p>
<dd> Non-default alias database. Specify <i>pathname</i> or <i>type</i>:<i>pathname</i>. See <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) for details.</p>
<dt><code>-O </code><i>option=value</i> (ignored)</p>
<dd> Set the named <i>option</i> to <i>value</i>. Use the equivalent configuration parameter in <code>main.cf</code> instead.</p>
<dt><code>-o7</code> (ignored)</p>
<dd>
<dt><code>-o8</code> (ignored)</p>
<dd> To send 8-bit or binary content, use an appropriate MIME encapsulation and specify the appropriate <code>-B</code> command-line option.</p>
<dt><code>-oi</code></p>
<dd> When reading a message from standard input, don&#8217;t treat a line with only a <code>.</code> character as the end of input.</p>
<dt><code>-om</code> (ignored)</p>
<dd> The sender is never eliminated from alias etc. expansions.</p>
<dt><code>-o </code><i>x value</i> (ignored)</p>
<dd> Set option <i>x</i> to <i>value</i>. Use the equivalent configuration parameter in <code>main.cf</code> instead.</p>
<dt><code>-r </code><i>sender</i></p>
<dd> Set the envelope sender address. This is the address where delivery problems are sent to. With Postfix versions before 2.1, the <code>Errors-To:</code> message header overrides the error return address.</p>
<dt><code>-R </code><i>return</i></p>
<dd> Delivery status notification control. Specify &quot;hdrs&quot; to return only the header when a message bounces, &quot;full&quot; to return a full copy (the default behavior). </p>
<p> The <code>-R</code> option specifies an upper bound; Postfix will return only the header, when a full copy would exceed the bounce_size_limit setting. </p>
<p> This option is ignored before Postfix version 2.10.</p>
<dt><code>-q</code></p>
<dd> Attempt to deliver all queued mail. This is implemented by executing the <code><a href="/docs/linux/man/1-postqueue/">postqueue</a></code>(1) command. </p>
<p> Warning: flushing undeliverable mail frequently will result in poor delivery performance of all other mail.</p>
<dt><code>-q</code><i>interval</i> (ignored)</p>
<dd> The interval between queue runs. Use the <code>queue_run_delay</code> configuration parameter instead.</p>
<dt><code>-qI</code><i>queueid</i></p>
<dd> Schedule immediate delivery of mail with the specified queue ID. This option is implemented by executing the <code><a href="/docs/linux/man/1-postqueue/">postqueue</a></code>(1) command, and is available with Postfix version 2.4 and later.</p>
<dt><code>-qR</code><i>site</i></p>
<dd> Schedule immediate delivery of all mail that is queued for the named <i>site</i>. This option accepts only <i>site</i> names that are eligible for the &quot;fast flush&quot; service, and is implemented by executing the <code><a href="/docs/linux/man/1-postqueue/">postqueue</a></code>(1) command. See <code><a href="/docs/linux/man/8-flush/">flush</a></code>(8) for more information about the &quot;fast flush&quot; service.</p>
<dt><code>-qS</code><i>site</i></p>
<dd> This command is not implemented. Use the slower &quot;<code>sendmail -q</code>&quot; command instead.</p>
<dt><code>-t</code></p>
<dd> Extract recipients from message headers. These are added to any recipients specified on the command line. </p>
<p> With Postfix versions prior to 2.1, this option requires that no recipient addresses are specified on the command line.</p>
<dt><code>-U</code> (ignored)</p>
<dd> Initial user submission.</p>
<dt><code>-V </code><i>envid</i></p>
<dd> Specify the envelope ID for notification by servers that support DSN. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<dt><code>-XV</code> (Postfix 2.2 and earlier: <code>-V</code>)</p>
<dd> Variable Envelope Return Path. Given an envelope sender address of the form <i>owner-listname</i>@<i>origin</i>, each recipient <i>user</i>@<i>domain</i> receives mail with a personalized envelope sender address. </p>
<p> By default, the personalized envelope sender address is <i>owner-listname</i><code>+</code><i>user</i><code>=</code><i>domain</i>@<i>origin</i>. The default <code>+</code> and <code>=</code> characters are configurable with the <code>default_verp_delimiters</code> configuration parameter.</p>
<dt><code>-XV</code><i>xy</i> (Postfix 2.2 and earlier: <code>-V</code><i>xy</i>)</p>
<dd> As <code>-XV</code>, but uses <i>x</i> and <i>y</i> as the VERP delimiter characters, instead of the characters specified with the <code>default_verp_delimiters</code> configuration parameter.</p>
<dt><code>-v</code></p>
<dd> Send an email report of the first delivery attempt (Postfix versions 2.1 and later). Mail delivery always happens in the background. When multiple <code>-v</code> options are given, enable verbose logging for debugging purposes.</p>
<dt><code>-X </code><i>log_file</i> (ignored)</p>
<dd> Log mailer traffic. Use the <code>debug_peer_list</code> and <code>debug_peer_level</code> configuration parameters instead.</dl>
<h2>SECURITY</h2>
<p> By design, this program is not set-user (or group) id. However, it must handle data from untrusted, possibly remote, users. Thus, the usual precautions need to be taken against malicious inputs.</p>
<h2>DIAGNOSTICS</h2>
<p> Problems are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) or <code><a href="/docs/linux/man/8-postlogd/">postlogd</a></code>(8), and to the standard error stream.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MAIL_CONFIG</code></p>
<dd> Directory with Postfix configuration files.</p>
<dt><code>MAIL_VERBOSE</code> (value does not matter)</p>
<dd> Enable verbose logging for debugging purposes.</p>
<dt><code>MAIL_DEBUG</code> (value does not matter)</p>
<dd> Enable debugging with an external command, as specified with the <code>debugger_command</code> configuration parameter.</p>
<dt><code>NAME</code></p>
<dd> The sender full name. This is used only with messages that have no <code>From:</code> message header. See also the <code>-F</code> option above.</dl>
<h2>CONFIGURATION PARAMETERS</h2>
<p> The following <code>main.cf</code> parameters are especially relevant to this program. The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>COMPATIBILITY CONTROLS</h2>
<p> Available with Postfix 2.9 and later:</p>
<dl>
<dt><code>sendmail_fix_line_endings (always)</code></p>
<dd> Controls how the Postfix sendmail command converts email message line endings from &lt;CR&gt;&lt;LF&gt; into UNIX format (&lt;LF&gt;).</dl>
<h2>TROUBLE SHOOTING CONTROLS</h2>
<p> The DEBUG_README file gives examples of how to troubleshoot a Postfix system.</p>
<dl>
<dt><code>debugger_command (empty)</code></p>
<dd> The external command to execute when a Postfix daemon program is invoked with the -D option.</p>
<dt><code>debug_peer_level (2)</code></p>
<dd> The increment in verbose logging level when a remote client or server matches a pattern in the debug_peer_list parameter.</p>
<dt><code>debug_peer_list (empty)</code></p>
<dd> Optional list of remote client or server hostname or network address patterns that cause the verbose logging level to increase by the amount specified in $debug_peer_level.</dl>
<h2>ACCESS CONTROLS</h2>
<p> Available in Postfix version 2.2 and later:</p>
<dl>
<dt><code>authorized_flush_users (static:anyone)</code></p>
<dd> List of users who are authorized to flush the queue.</p>
<dt><code>authorized_mailq_users (static:anyone)</code></p>
<dd> List of users who are authorized to view the queue.</p>
<dt><code>authorized_submit_users (static:anyone)</code></p>
<dd> List of users who are authorized to submit mail with the <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command (and with the privileged <code><a href="/docs/linux/man/1-postdrop/">postdrop</a></code>(1) helper command).</dl>
<h2>RESOURCE AND RATE CONTROLS</h2>
<dl>
<dt><code>bounce_size_limit (50000)</code></p>
<dd> The maximal amount of original message text that is sent in a non-delivery notification.</p>
<dt><code>fork_attempts (5)</code></p>
<dd> The maximal number of attempts to fork() a child process.</p>
<dt><code>fork_delay (1s)</code></p>
<dd> The delay between attempts to fork() a child process.</p>
<dt><code>hopcount_limit (50)</code></p>
<dd> The maximal number of Received: message headers that is allowed in the primary message headers.</p>
<dt><code>queue_run_delay (300s)</code></p>
<dd> The time between deferred queue scans by the queue manager; prior to Postfix 2.4 the default value was 1000s.</dl>
<h2>FAST FLUSH CONTROLS</h2>
<p> The ETRN_README file describes configuration and operation details for the Postfix &quot;fast flush&quot; service.</p>
<dl>
<dt><code>fast_flush_domains ($relay_domains)</code></p>
<dd> Optional list of destinations that are eligible for per-destination logfiles with mail that is queued to those destinations.</dl>
<h2>VERP CONTROLS</h2>
<p> The VERP_README file describes configuration and operation details of Postfix support for variable envelope return path addresses.</p>
<dl>
<dt><code>default_verp_delimiters (+=)</code></p>
<dd> The two default VERP delimiter characters.</p>
<dt><code>verp_delimiter_filter (-=+)</code></p>
<dd> The characters Postfix accepts as VERP delimiter characters on the Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command line and in SMTP commands.</dl>
<h2>MISCELLANEOUS CONTROLS</h2>
<dl>
<dt><code>alias_database (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The alias databases for <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery that are updated with &quot;<code>newaliases</code>&quot; or with &quot;<code>sendmail -bi</code>&quot;.</p>
<dt><code>command_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of all postfix administrative commands.</p>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The directory with Postfix support programs and daemon programs.</p>
<dt><code>default_database_type (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default database type for use in <code><a href="/docs/linux/man/1-newaliases/">newaliases</a></code>(1), <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) and <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) commands.</p>
<dt><code>delay_warning_time (0h)</code></p>
<dd> The time after which the sender receives a copy of the message headers of mail that is still queued.</p>
<dt><code>import_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The list of environment parameters that a privileged Postfix process will import from a non-Postfix parent process, or name=value environment overrides.</p>
<dt><code>mail_owner (postfix)</code></p>
<dd> The UNIX system account that owns the Postfix queue and most Postfix daemon processes.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of the Postfix top-level queue directory.</p>
<dt><code>remote_header_rewrite_domain (empty)</code></p>
<dd> Don&#8217;t rewrite message headers from remote clients at all when this parameter is empty; otherwise, rewrite message headers and append the specified domain name to incomplete addresses.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd> The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd> A prefix that is prepended to the process name in syslog records, so that, for example, &quot;smtpd&quot; becomes &quot;prefix/smtpd&quot;.</dl>
<p> Postfix 3.2 and later:</p>
<dl>
<dt><code>alternate_config_directories (empty)</code></p>
<dd> A list of non-default Postfix configuration directories that may be specified with &quot;-c config_directory&quot; on the command line (in the case of <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1), with the &quot;-C&quot; option), or via the MAIL_CONFIG environment parameter.</p>
<dt><code>multi_instance_directories (empty)</code></p>
<dd> An optional list of non-default Postfix configuration directories; these directories belong to additional Postfix instances that share the Postfix executable files and documentation with the default Postfix instance, and that are started, stopped, etc., together with the default Postfix instance.</dl>
<h2>FILES</h2>
<pre>
/var/spool/postfix, mail queue
/etc/postfix, configuration files
</pre>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/8-pickup/">pickup</a>(8), mail pickup daemon
<a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), queue manager
<a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a>(8), SMTP server
<a href="//www.systutorials.com/docs/linux/man/8-flush/">flush</a>(8), fast flush service
<a href="//www.systutorials.com/docs/linux/man/1-postsuper/">postsuper</a>(1), queue maintenance
<a href="//www.systutorials.com/docs/linux/man/1-postalias/">postalias</a>(1), create/update/query alias database
<a href="//www.systutorials.com/docs/linux/man/1-postdrop/">postdrop</a>(1), mail posting utility
<a href="//www.systutorials.com/docs/linux/man/1-postfix/">postfix</a>(1), mail system control
<a href="//www.systutorials.com/docs/linux/man/1-postqueue/">postqueue</a>(1), mail queue control
<a href="//www.systutorials.com/docs/linux/man/8-postlogd/">postlogd</a>(8), Postfix logging
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging
</pre>
<h2>README_FILES</h2>
<p> Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>
DEBUG_README, Postfix debugging howto
ETRN_README, Postfix ETRN howto
VERP_README, Postfix VERP howto
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
