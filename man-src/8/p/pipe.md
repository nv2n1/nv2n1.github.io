---
title: "pipe(8)"
name: "pipe"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pipe/"
description: "pipe – Postfix delivery to external command"
---

<p>pipe &#8211; Postfix delivery to external command</p>
<h2>Synopsis</h2>
<pre><code>pipe</code> [generic Postfix daemon options] command_attributes...</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-pipe/">pipe</a></code>(8) daemon processes requests from the Postfix queue manager to deliver messages to external commands. This program expects to be run from the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) process manager. </p>
<p> Message attributes such as sender address, recipient address and next-hop host name can be specified as command-line macros that are expanded before the external command is executed. </p>
<p> The <code><a href="/docs/linux/man/8-pipe/">pipe</a></code>(8) daemon updates queue files and marks recipients as finished, or it informs the queue manager that delivery should be tried again at a later time. Delivery status reports are sent to the <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8), <code><a href="/docs/linux/man/8-defer/">defer</a></code>(8) or <code><a href="/docs/linux/man/8-trace/">trace</a></code>(8) daemon as appropriate.</p>
<h2>Single-Recipient Delivery</h2>
<p>Some destinations cannot handle more than one recipient per delivery request. Examples are pagers or fax machines. In addition, multi-recipient delivery is undesirable when prepending a <code>Delivered-to:</code> or <code>X-Original-To:</code> message header. </p>
<p> To prevent Postfix from sending multiple recipients per delivery request, specify </p>
<pre> <i>transport</i><code>_destination_recipient_limit = 1</code></pre>
<p>in the Postfix <code>main.cf</code> file, where <i>transport</i> is the name in the first column of the Postfix <code>master.cf</code> entry for the pipe-based delivery transport.</p>
<h2>Command Attribute Syntax</h2>
<p>The external command attributes are given in the <code>master.cf</code> file at the end of a service definition. The syntax is as follows:</p>
<dl>
<dt><code>chroot=</code><i>pathname</i> (optional)</p>
<dd>Change the process root directory and working directory to the named directory. This happens before switching to the privileges specified with the <code>user</code> attribute, and before executing the optional <code>directory=</code><i>pathname</i> directive. Delivery is deferred in case of failure. </p>
<p> This feature is available as of Postfix 2.3.</p>
<dt><code>directory=</code><i>pathname</i> (optional)</p>
<dd>Change to the named directory before executing the external command. The directory must be accessible for the user specified with the <code>user</code> attribute (see below). The default working directory is <code>$queue_directory</code>. Delivery is deferred in case of failure. </p>
<p> This feature is available as of Postfix 2.2.</p>
<dt><code>eol=</code><i>string</i> (optional, default: <code>
</code>)</p>
<dd>The output record delimiter. Typically one would use either <code>
</code> or <code>
</code>. The usual C-style backslash escape sequences are recognized: <code>   
  	  \</code><i>ddd</i> (up to three octal digits) and <code>\</code>.</p>
<dt><code>flags=BDFORXhqu.&gt;</code> (optional)</p>
<dd>Optional message processing flags. By default, a message is copied unchanged.</p>
<dl>
<dd>
<dl>
<dt><code>B</code></p>
<dd>Append a blank line at the end of each message. This is required by some mail user agents that recognize &quot;<code>From </code>&quot; lines only when preceded by a blank line.</p>
<dt><code>D</code></p>
<dd>Prepend a &quot;<code>Delivered-To: </code><i>recipient</i>&quot; message header with the envelope recipient address. Note: for this to work, the <i>transport</i><code>_destination_recipient_limit</code> must be 1 (see SINGLE-RECIPIENT DELIVERY above for details). </p>
<p> The <code>D</code> flag also enforces loop detection (Postfix 2.5 and later): if a message already contains a <code>Delivered-To:</code> header with the same recipient address, then the message is returned as undeliverable. The address comparison is case insensitive. </p>
<p> This feature is available as of Postfix 2.0.</p>
<dt><code>F</code></p>
<dd>Prepend a &quot;<code>From </code><i>sender time_stamp</i>&quot; envelope header to the message content. This is expected by, for example, <code>UUCP</code> software.</p>
<dt><code>O</code></p>
<dd>Prepend an &quot;<code>X-Original-To: </code><i>recipient</i>&quot; message header with the recipient address as given to Postfix. Note: for this to work, the <i>transport</i><code>_destination_recipient_limit</code> must be 1 (see SINGLE-RECIPIENT DELIVERY above for details). </p>
<p> This feature is available as of Postfix 2.0.</p>
<dt><code>R</code></p>
<dd>Prepend a <code>Return-Path:</code> message header with the envelope sender address.</p>
<dt><code>X</code></p>
<dd>Indicate that the external command performs final delivery. This flag affects the status reported in &quot;success&quot; DSN (delivery status notification) messages, and changes it from &quot;relayed&quot; into &quot;delivered&quot;. </p>
<p> This feature is available as of Postfix 2.5.</p>
<dt><code>h</code></p>
<dd>Fold the command-line <code>$original_recipient</code> and <code>$recipient</code> address domain part (text to the right of the right-most <code>@</code> character) to lower case; fold the entire command-line <code>$domain</code> and <code>$nexthop</code> host or domain information to lower case. This is recommended for delivery via <code>UUCP</code>.</p>
<dt><code>q</code></p>
<dd>Quote white space and other special characters in the command-line <code>$sender</code>, <code>$original_recipient</code> and <code>$recipient</code> address localparts (text to the left of the right-most <code>@</code> character), according to an 8-bit transparent version of RFC 822. This is recommended for delivery via <code>UUCP</code> or <code>BSMTP</code>. </p>
<p> The result is compatible with the address parsing of command-line recipients by the Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) mail submission command. </p>
<p> The <code>q</code> flag affects only entire addresses, not the partial address information from the <code>$user</code>, <code>$extension</code> or <code>$mailbox</code> command-line macros.</p>
<dt><code>u</code></p>
<dd>Fold the command-line <code>$original_recipient</code> and <code>$recipient</code> address localpart (text to the left of the right-most <code>@</code> character) to lower case. This is recommended for delivery via <code>UUCP</code>.</p>
<dt><code>.</code></p>
<dd>Prepend &quot;<code>.</code>&quot; to lines starting with &quot;<code>.</code>&quot;. This is needed by, for example, <code>BSMTP</code> software.</p>
<dt><code>&gt;</code></p>
<dd>Prepend &quot;<code>&gt;</code>&quot; to lines starting with &quot;<code>From </code>&quot;. This is expected by, for example, <code>UUCP</code> software.</dl>
</dl>
<dt><code>null_sender</code>=<i>replacement</i> (default: MAILER-DAEMON)</p>
<dd>Replace the null sender address (typically used for delivery status notifications) with the specified text when expanding the <code>$sender</code> command-line macro, and when generating a From_ or Return-Path: message header. </p>
<p> If the null sender replacement text is a non-empty string then it is affected by the <code>q</code> flag for address quoting in command-line arguments. </p>
<p> The null sender replacement text may be empty; this form is recommended for content filters that feed mail back into Postfix. The empty sender address is not affected by the <code>q</code> flag for address quoting in command-line arguments. </p>
<p> Caution: a null sender address is easily mis-parsed by naive software. For example, when the <code><a href="/docs/linux/man/8-pipe/">pipe</a></code>(8) daemon executes a command such as: </p>
<pre> <i>Wrong</i>: command -f$sender -- $recipient</pre>
<dd>the command will mis-parse the -f option value when the sender address is a null string. For correct parsing, specify <code>$sender</code> as an argument by itself: </p>
<pre> <i>Right</i>: command -f $sender -- $recipient</pre>
<dd>This feature is available as of Postfix 2.3.</p>
<dt><code>size</code>=<i>size_limit</i> (optional)</p>
<dd>Don&#8217;t deliver messages that exceed this size limit (in bytes); return them to the sender instead.</p>
<dt><code>user</code>=<i>username</i> (required)</p>
<dd>
<dt><code>user</code>=<i>username</i>:<i>groupname</i></p>
<dd>Execute the external command with the user ID and group ID of the specified <i>username</i>. The software refuses to execute commands with root privileges, or with the privileges of the mail system owner. If <i>groupname</i> is specified, the corresponding group ID is used instead of the group ID of <i>username</i>.</p>
<dt><code>argv</code>=<i>command</i>&#8230; (required)</p>
<dd>The command to be executed. This must be specified as the last command attribute. The command is executed directly, i.e. without interpretation of shell meta characters by a shell command interpreter. </p>
<p> In the command argument vector, the following macros are recognized and replaced with corresponding information from the Postfix queue manager delivery request. </p>
<p> In addition to the form ${<i>name</i>}, the forms $<i>name</i> and $(<i>name</i>) are also recognized. Specify <code>$$</code> where a single <code>$</code> is wanted.</p>
<dl>
<dd>
<dl>
<dt><code>${client_address</code>}</p>
<dd>This macro expands to the remote client network address. </p>
<p> This feature is available as of Postfix 2.2.</p>
<dt><code>${client_helo</code>}</p>
<dd>This macro expands to the remote client HELO command parameter. </p>
<p> This feature is available as of Postfix 2.2.</p>
<dt><code>${client_hostname</code>}</p>
<dd>This macro expands to the remote client hostname. </p>
<p> This feature is available as of Postfix 2.2.</p>
<dt><code>${client_port</code>}</p>
<dd>This macro expands to the remote client TCP port number. </p>
<p> This feature is available as of Postfix 2.5.</p>
<dt><code>${client_protocol</code>}</p>
<dd>This macro expands to the remote client protocol. </p>
<p> This feature is available as of Postfix 2.2.</p>
<dt><code>${domain</code>}</p>
<dd>This macro expands to the domain portion of the recipient address. For example, with an address <i>user+foo [at] domain</i> the domain is <i>domain</i>. </p>
<p> This information is modified by the <code>h</code> flag for case folding. </p>
<p> This feature is available as of Postfix 2.5.</p>
<dt><code>${extension</code>}</p>
<dd>This macro expands to the extension part of a recipient address. For example, with an address <i>user+foo [at] domain</i> the extension is <i>foo</i>. </p>
<p> A command-line argument that contains <code>${extension</code>} expands into as many command-line arguments as there are recipients. </p>
<p> This information is modified by the <code>u</code> flag for case folding.</p>
<dt><code>${mailbox</code>}</p>
<dd>This macro expands to the complete local part of a recipient address. For example, with an address <i>user+foo [at] domain</i> the mailbox is <i>user+foo</i>. </p>
<p> A command-line argument that contains <code>${mailbox</code>} expands to as many command-line arguments as there are recipients. </p>
<p> This information is modified by the <code>u</code> flag for case folding.</p>
<dt><code>${nexthop</code>}</p>
<dd>This macro expands to the next-hop hostname. </p>
<p> This information is modified by the <code>h</code> flag for case folding.</p>
<dt><code>${original_recipient</code>}</p>
<dd>This macro expands to the complete recipient address before any address rewriting or aliasing. </p>
<p> A command-line argument that contains <code>${original_recipient</code>} expands to as many command-line arguments as there are recipients. </p>
<p> This information is modified by the <code>hqu</code> flags for quoting and case folding. </p>
<p> This feature is available as of Postfix 2.5.</p>
<dt><code>${recipient</code>}</p>
<dd>This macro expands to the complete recipient address. </p>
<p> A command-line argument that contains <code>${recipient</code>} expands to as many command-line arguments as there are recipients. </p>
<p> This information is modified by the <code>hqu</code> flags for quoting and case folding.</p>
<dt><code>${sasl_method</code>}</p>
<dd>This macro expands to the name of the SASL authentication mechanism in the AUTH command when the Postfix SMTP server received the message. </p>
<p> This feature is available as of Postfix 2.2.</p>
<dt><code>${sasl_sender</code>}</p>
<dd>This macro expands to the SASL sender name (i.e. the original submitter as per RFC 4954) in the MAIL FROM command when the Postfix SMTP server received the message. </p>
<p> This feature is available as of Postfix 2.2.</p>
<dt><code>${sasl_username</code>}</p>
<dd>This macro expands to the SASL user name in the AUTH command when the Postfix SMTP server received the message. </p>
<p> This feature is available as of Postfix 2.2.</p>
<dt><code>${sender</code>}</p>
<dd>This macro expands to the envelope sender address. By default, the null sender address expands to MAILER-DAEMON; this can be changed with the <code>null_sender</code> attribute, as described above. </p>
<p> This information is modified by the <code>q</code> flag for quoting.</p>
<dt><code>${size</code>}</p>
<dd>This macro expands to Postfix&#8217;s idea of the message size, which is an approximation of the size of the message as delivered.</p>
<dt><code>${user</code>}</p>
<dd>This macro expands to the username part of a recipient address. For example, with an address <i>user+foo [at] domain</i> the username part is <i>user</i>. </p>
<p> A command-line argument that contains <code>${user</code>} expands into as many command-line arguments as there are recipients. </p>
<p> This information is modified by the <code>u</code> flag for case folding.</dl>
</dl>
</dl>
<h2>Standards</h2>
<pre>RFC 3463 (Enhanced status codes)</pre>
<h2>Diagnostics</h2>
<p>Command exit status codes are expected to follow the conventions defined in &lt;<code>sysexits.h</code>&gt;. Exit status 0 means normal successful completion. </p>
<p> In the case of a non-zero exit status, a limited amount of command output is reported in an delivery status notification. When the output begins with a 4.X.X or 5.X.X enhanced status code, the status code takes precedence over the non-zero exit status (Postfix version 2.3 and later). </p>
<p> Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). Corrupted message files are marked so that the queue manager can move them to the <code>corrupt</code> queue for further inspection.</p>
<h2>Security</h2>
<p>This program needs a dual personality 1) to access the private Postfix queue and IPC mechanisms, and 2) to execute external commands as the specified user. It is therefore security sensitive.</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are picked up automatically as <code><a href="/docs/linux/man/8-pipe/">pipe</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Resource And Rate Controls</h2>
<p>In the text below, <i>transport</i> is the first field in a <code>master.cf</code> entry.</p>
<dl>
<dt><i>transport</i><code>_destination_concurrency_limit ($default_destination_concurrency_limit)</code></p>
<dd>Limit the number of parallel deliveries to the same destination, for delivery via the named <i>transport</i>. The limit is enforced by the Postfix queue manager.</p>
<dt><i>transport</i><code>_destination_recipient_limit ($default_destination_recipient_limit)</code></p>
<dd>Limit the number of recipients per message delivery, for delivery via the named <i>transport</i>. The limit is enforced by the Postfix queue manager.</p>
<dt><i>transport</i><code>_time_limit ($command_time_limit)</code></p>
<dd>Limit the time for delivery to external command, for delivery via the named <i>transport</i>. The limit is enforced by the pipe delivery agent. </p>
<p> Postfix 2.4 and later support a suffix that specifies the time unit: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is seconds.</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>delay_logging_resolution_limit (2)</code></p>
<dd>The maximal number of digits after the decimal point when logging sub-second delay values.</p>
<dt><code>export_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The list of environment variables that a Postfix process will export to non-Postfix processes.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
<dt><code>mail_owner (postfix)</code></p>
<dd>The UNIX system account that owns the Postfix queue and most Postfix daemon processes.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>max_use (100)</code></p>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The location of the Postfix top-level queue directory.</p>
<dt><code>recipient_delimiter (empty)</code></p>
<dd>The separator between user names and address extensions (user+foo).</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), queue manager
<a href="//www.systutorials.com/docs/linux/man/8-bounce/">bounce</a>(8), delivery status reports
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), generic daemon options
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
