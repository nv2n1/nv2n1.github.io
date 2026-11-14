---
title: "local(8)"
name: "local"
section: "8"
letter: "l"
url: "/docs/linux/man/8-local/"
description: "local – Postfix local mail delivery"
---

<p>local &#8211; Postfix local mail delivery</p>
<h2>Synopsis</h2>
<pre><code>local</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) daemon processes delivery requests from the Postfix queue manager to deliver mail to local recipients. Each delivery request specifies a queue file, a sender address, a domain or host to deliver to, and one or more recipients. This program expects to be run from the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) process manager. </p>
<p> The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) daemon updates queue files and marks recipients as finished, or it informs the queue manager that delivery should be tried again at a later time. Delivery status reports are sent to the <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8), <code><a href="/docs/linux/man/8-defer/">defer</a></code>(8) or <code><a href="/docs/linux/man/8-trace/">trace</a></code>(8) daemon as appropriate.</p>
<h2>Case Folding</h2>
<p>All delivery decisions are made using the bare recipient name (i.e. the address localpart), folded to lower case. See also under ADDRESS EXTENSION below for a few exceptions.</p>
<h2>System-Wide And User-Level Aliasing</h2>
<p>The system administrator can set up one or more system-wide <code>sendmail</code>-style alias databases. Users can have <code>sendmail</code>-style ~/.<code>forward</code> files. Mail for <i>name</i> is delivered to the alias <i>name</i>, to destinations in ~<i>name</i>/.<code>forward</code>, to the mailbox owned by the user <i>name</i>, or it is sent back as undeliverable. </p>
<p> The system administrator can specify a comma/space separated list of ~/.<code>forward</code> like files through the <code>forward_path</code> configuration parameter. Upon delivery, the local delivery agent tries each pathname in the list until a file is found. </p>
<p> Delivery via ~/.<code>forward</code> files is done with the privileges of the recipient. Thus, ~/.<code>forward</code> like files must be readable by the recipient, and their parent directory needs to have &quot;execute&quot; permission for the recipient. </p>
<p> The <code>forward_path</code> parameter is subject to interpolation of <code>$user</code> (recipient username), <code>$home</code> (recipient home directory), <code>$shell</code> (recipient shell), <code>$recipient</code> (complete recipient address), <code>$extension</code> (recipient address extension), <code>$domain</code> (recipient domain), <code>$local</code> (entire recipient address localpart) and <code>$recipient_delimiter.</code> The forms <i>${name?value}</i> and <i>${name:value}</i> expand conditionally to <i>value</i> when <i>$name</i> is (is not) defined. Characters that may have special meaning to the shell or file system are replaced by underscores. The list of acceptable characters is specified with the <code>forward_expansion_filter</code> configuration parameter. </p>
<p> An alias or ~/.<code>forward</code> file may list any combination of external commands, destination file names, <code>:include:</code> directives, or mail addresses. See <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) for a precise description. Each line in a user&#8217;s .<code>forward</code> file has the same syntax as the right-hand part of an alias. </p>
<p> When an address is found in its own alias expansion, delivery is made to the user instead. When a user is listed in the user&#8217;s own ~/.<code>forward</code> file, delivery is made to the user&#8217;s mailbox instead. An empty ~/.<code>forward</code> file means do not forward mail. </p>
<p> In order to prevent the mail system from using up unreasonable amounts of memory, input records read from <code>:include:</code> or from ~/.<code>forward</code> files are broken up into chunks of length <code>line_length_limit</code>. </p>
<p> While expanding aliases, ~/.<code>forward</code> files, and so on, the program attempts to avoid duplicate deliveries. The <code>duplicate_filter_limit</code> configuration parameter limits the number of remembered recipients.</p>
<h2>Mail Forwarding</h2>
<p>For the sake of reliability, forwarded mail is re-submitted as a new message, so that each recipient has a separate on-file delivery status record. </p>
<p> In order to stop mail forwarding loops early, the software adds an optional <code>Delivered-To:</code> header with the final envelope recipient address. If mail arrives for a recipient that is already listed in a <code>Delivered-To:</code> header, the message is bounced.</p>
<h2>Mailbox Delivery</h2>
<p>The default per-user mailbox is a file in the UNIX mail spool directory (<code>/var/mail/</code><i>user</i> or <code>/var/spool/mail/</code><i>user</i>); the location can be specified with the <code>mail_spool_directory</code> configuration parameter. Specify a name ending in <code>/</code> for <code>qmail</code>-compatible <code>maildir</code> delivery. </p>
<p> Alternatively, the per-user mailbox can be a file in the user&#8217;s home directory with a name specified via the <code>home_mailbox</code> configuration parameter. Specify a relative path name. Specify a name ending in <code>/</code> for <code>qmail</code>-compatible <code>maildir</code> delivery. </p>
<p> Mailbox delivery can be delegated to an external command specified with the <code>mailbox_command_maps</code> and <code>mailbox_command</code> configuration parameters. The command executes with the privileges of the recipient user (exceptions: secondary groups are not enabled; in case of delivery as root, the command executes with the privileges of <code>default_privs</code>). </p>
<p> Mailbox delivery can be delegated to alternative message transports specified in the <code>master.cf</code> file. The <code>mailbox_transport_maps</code> and <code>mailbox_transport</code> configuration parameters specify an optional message transport that is to be used for all local recipients, regardless of whether they are found in the UNIX passwd database. The <code>fallback_transport_maps</code> and <code>fallback_transport</code> parameters specify an optional message transport for recipients that are not found in the <a href="/docs/linux/man/5-aliases/">aliases</a>(5) or UNIX passwd database. </p>
<p> In the case of UNIX-style mailbox delivery, the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) daemon prepends a &quot;<code>From </code><i>sender time_stamp</i>&quot; envelope header to each message, prepends an <code>X-Original-To:</code> header with the recipient address as given to Postfix, prepends an optional <code>Delivered-To:</code> header with the final envelope recipient address, prepends a <code>Return-Path:</code> header with the envelope sender address, prepends a <code>&gt;</code> character to lines beginning with &quot;<code>From </code>&quot;, and appends an empty line. The mailbox is locked for exclusive access while delivery is in progress. In case of problems, an attempt is made to truncate the mailbox to its original length. </p>
<p> In the case of <code>maildir</code> delivery, the local daemon prepends an optional <code>Delivered-To:</code> header with the final envelope recipient address, prepends an <code>X-Original-To:</code> header with the recipient address as given to Postfix, and prepends a <code>Return-Path:</code> header with the envelope sender address.</p>
<h2>External Command Delivery</h2>
<p>The <code>allow_mail_to_commands</code> configuration parameter restricts delivery to external commands. The default setting (<code>alias, forward</code>) forbids command destinations in <code>:include:</code> files. </p>
<p> Optionally, the process working directory is changed to the path specified with <code>command_execution_directory</code> (Postfix 2.2 and later). Failure to change directory causes mail to be deferred. </p>
<p> The <code>command_execution_directory</code> parameter value is subject to interpolation of <code>$user</code> (recipient username), <code>$home</code> (recipient home directory), <code>$shell</code> (recipient shell), <code>$recipient</code> (complete recipient address), <code>$extension</code> (recipient address extension), <code>$domain</code> (recipient domain), <code>$local</code> (entire recipient address localpart) and <code>$recipient_delimiter.</code> The forms <i>${name?value}</i> and <i>${name:value}</i> expand conditionally to <i>value</i> when <i>$name</i> is (is not) defined. Characters that may have special meaning to the shell or file system are replaced by underscores. The list of acceptable characters is specified with the <code>execution_directory_expansion_filter</code> configuration parameter. </p>
<p> The command is executed directly where possible. Assistance by the shell (<code>/bin/sh</code> on UNIX systems) is used only when the command contains shell magic characters, or when the command invokes a shell built-in command. </p>
<p> A limited amount of command output (standard output and standard error) is captured for inclusion with non-delivery status reports. A command is forcibly terminated if it does not complete within <code>command_time_limit</code> seconds. Command exit status codes are expected to follow the conventions defined in &lt;<code>sysexits.h</code>&gt;. Exit status 0 means normal successful completion. </p>
<p> Postfix version 2.3 and later support RFC 3463-style enhanced status codes. If a command terminates with a non-zero exit status, and the command output begins with an enhanced status code, this status code takes precedence over the non-zero exit status. </p>
<p> A limited amount of message context is exported via environment variables. Characters that may have special meaning to the shell are replaced by underscores. The list of acceptable characters is specified with the <code>command_expansion_filter</code> configuration parameter.</p>
<dl>
<dt><code>SHELL</code></p>
<dd>The recipient user&#8217;s login shell.</p>
<dt><code>HOME</code></p>
<dd>The recipient user&#8217;s home directory.</p>
<dt><code>USER</code></p>
<dd>The bare recipient name.</p>
<dt><code>EXTENSION</code></p>
<dd>The optional recipient address extension.</p>
<dt><code>DOMAIN</code></p>
<dd>The recipient address domain part.</p>
<dt><code>LOGNAME</code></p>
<dd>The bare recipient name.</p>
<dt><code>LOCAL</code></p>
<dd>The entire recipient address localpart (text to the left of the rightmost @ character).</p>
<dt><code>ORIGINAL_RECIPIENT</code></p>
<dd>The entire recipient address, before any address rewriting or aliasing (Postfix 2.5 and later).</p>
<dt><code>RECIPIENT</code></p>
<dd>The entire recipient address.</p>
<dt><code>SENDER</code></p>
<dd>The entire sender address.</dl>
<p> Additional remote client information is made available via the following environment variables:</p>
<dl>
<dt><code>CLIENT_ADDRESS</code></p>
<dd>Remote client network address. Available as of Postfix 2.2.</p>
<dt><code>CLIENT_HELO</code></p>
<dd>Remote client EHLO command parameter. Available as of Postfix 2.2.</p>
<dt><code>CLIENT_HOSTNAME</code></p>
<dd>Remote client hostname. Available as of Postfix 2.2.</p>
<dt><code>CLIENT_PROTOCOL</code></p>
<dd>Remote client protocol. Available as of Postfix 2.2.</p>
<dt><code>SASL_METHOD</code></p>
<dd>SASL authentication method specified in the remote client AUTH command. Available as of Postfix 2.2.</p>
<dt><code>SASL_SENDER</code></p>
<dd>SASL sender address specified in the remote client MAIL FROM command. Available as of Postfix 2.2.</p>
<dt><code>SASL_USERNAME</code></p>
<dd>SASL username specified in the remote client AUTH command. Available as of Postfix 2.2.</dl>
<p> The <code>PATH</code> environment variable is always reset to a system-dependent default path, and environment variables whose names are blessed by the <code>export_environment</code> configuration parameter are exported unchanged. </p>
<p> The current working directory is the mail queue directory. </p>
<p> The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) daemon prepends a &quot;<code>From </code><i>sender time_stamp</i>&quot; envelope header to each message, prepends an <code>X-Original-To:</code> header with the recipient address as given to Postfix, prepends an optional <code>Delivered-To:</code> header with the final recipient envelope address, prepends a <code>Return-Path:</code> header with the sender envelope address, and appends no empty line.</p>
<h2>External File Delivery</h2>
<p>The delivery format depends on the destination filename syntax. The default is to use UNIX-style mailbox format. Specify a name ending in <code>/</code> for <code>qmail</code>-compatible <code>maildir</code> delivery. </p>
<p> The <code>allow_mail_to_files</code> configuration parameter restricts delivery to external files. The default setting (<code>alias, forward</code>) forbids file destinations in <code>:include:</code> files. </p>
<p> In the case of UNIX-style mailbox delivery, the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) daemon prepends a &quot;<code>From </code><i>sender time_stamp</i>&quot; envelope header to each message, prepends an <code>X-Original-To:</code> header with the recipient address as given to Postfix, prepends an optional <code>Delivered-To:</code> header with the final recipient envelope address, prepends a <code>&gt;</code> character to lines beginning with &quot;<code>From </code>&quot;, and appends an empty line. The envelope sender address is available in the <code>Return-Path:</code> header. When the destination is a regular file, it is locked for exclusive access while delivery is in progress. In case of problems, an attempt is made to truncate a regular file to its original length. </p>
<p> In the case of <code>maildir</code> delivery, the local daemon prepends an optional <code>Delivered-To:</code> header with the final envelope recipient address, and prepends an <code>X-Original-To:</code> header with the recipient address as given to Postfix. The envelope sender address is available in the <code>Return-Path:</code> header.</p>
<h2>Address Extension</h2>
<p>The optional <code>recipient_delimiter</code> configuration parameter specifies how to separate address extensions from local recipient names. </p>
<p> For example, with &quot;<code>recipient_delimiter = +</code>&quot;, mail for <i>name</i>+<i>foo</i> is delivered to the alias <i>name</i>+<i>foo</i> or to the alias <i>name</i>, to the destinations listed in ~<i>name</i>/.<code>forward</code>+<i>foo</i> or in ~<i>name</i>/.<code>forward</code>, to the mailbox owned by the user <i>name</i>, or it is sent back as undeliverable.</p>
<h2>Delivery Rights</h2>
<p>Deliveries to external files and external commands are made with the rights of the receiving user on whose behalf the delivery is made. In the absence of a user context, the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) daemon uses the owner rights of the <code>:include:</code> file or alias database. When those files are owned by the superuser, delivery is made with the rights specified with the <code>default_privs</code> configuration parameter.</p>
<h2>Standards</h2>
<pre>RFC 822 (ARPA Internet Text Messages)
RFC 3463 (Enhanced status codes)</pre>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). Corrupted message files are marked so that the queue manager can move them to the <code>corrupt</code> queue afterwards. </p>
<p> Depending on the setting of the <code>notify_classes</code> parameter, the postmaster is notified of bounces and of other trouble.</p>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent needs a dual personality 1) to access the private Postfix queue and IPC mechanisms, 2) to impersonate the recipient and deliver to recipient-specified files or commands. It is therefore security sensitive. </p>
<p> The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent disallows regular expression substitution of $1 etc. in <code>alias_maps</code>, because that would open a security hole. </p>
<p> The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent will silently ignore requests to use the <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server within <code>alias_maps</code>. Instead it will open the table directly. Before Postfix version 2.2, the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent will terminate with a fatal error.</p>
<h2>Bugs</h2>
<p>For security reasons, the message delivery status of external commands or of external files is never checkpointed to file. As a result, the program may occasionally deliver more than once to a command or external file. Better safe than sorry. </p>
<p> Mutually-recursive aliases or ~/.<code>forward</code> files are not detected early. The resulting mail forwarding loop is broken by the use of the <code>Delivered-To:</code> message header.</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are picked up automatically, as <code><a href="/docs/linux/man/8-local/">local</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Compatibility Controls</h2>
<dl>
<dt><code>biff (yes)</code></p>
<dd>Whether or not to use the local biff service.</p>
<dt><code>expand_owner_alias (no)</code></p>
<dd>When delivering to an alias &quot;aliasname&quot; that has an &quot;owner-aliasname&quot; companion alias, set the envelope sender address to the expansion of the &quot;owner-aliasname&quot; alias.</p>
<dt><code>owner_request_special (yes)</code></p>
<dd>Give special treatment to owner-listname and listname-request address localparts: don&#8217;t split such addresses when the recipient_delimiter is set to &quot;-&quot;.</p>
<dt><code>sun_mailtool_compatibility (no)</code></p>
<dd>Obsolete SUN mailtool compatibility feature.</dl>
<p> Available in Postfix version 2.3 and later:</p>
<dl>
<dt><code>frozen_delivered_to (yes)</code></p>
<dd>Update the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent&#8217;s idea of the Delivered-To: address (see prepend_delivered_header) only once, at the start of a delivery attempt; do not update the Delivered-To: address while expanding aliases or .forward files.</dl>
<p> Available in Postfix version 2.5.3 and later:</p>
<dl>
<dt><code>strict_mailbox_ownership (yes)</code></p>
<dd>Defer delivery when a mailbox file is not owned by its recipient.</p>
<dt><code>reset_owner_alias (no)</code></p>
<dd>Reset the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent&#8217;s idea of the owner-alias attribute, when delivering mail to a child alias that does not have its own owner alias.</dl>
<h2>Delivery Method Controls</h2>
<p>The precedence of <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery methods from high to low is: aliases, .forward files, mailbox_transport_maps, mailbox_transport, mailbox_command_maps, mailbox_command, home_mailbox, mail_spool_directory, fallback_transport_maps, fallback_transport, and luser_relay.</p>
<dl>
<dt><code>alias_maps (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The alias databases that are used for <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery.</p>
<dt><code>forward_path (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent search list for finding a .forward file with user-specified delivery methods.</p>
<dt><code>mailbox_transport_maps (empty)</code></p>
<dd>Optional lookup tables with per-recipient message delivery transports to use for <code><a href="/docs/linux/man/8-local/">local</a></code>(8) mailbox delivery, whether or not the recipients are found in the UNIX passwd database.</p>
<dt><code>mailbox_transport (empty)</code></p>
<dd>Optional message delivery transport that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent should use for mailbox delivery to all local recipients, whether or not they are found in the UNIX passwd database.</p>
<dt><code>mailbox_command_maps (empty)</code></p>
<dd>Optional lookup tables with per-recipient external commands to use for <code><a href="/docs/linux/man/8-local/">local</a></code>(8) mailbox delivery.</p>
<dt><code>mailbox_command (empty)</code></p>
<dd>Optional external command that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent should use for mailbox delivery.</p>
<dt><code>home_mailbox (empty)</code></p>
<dd>Optional pathname of a mailbox file relative to a <code><a href="/docs/linux/man/8-local/">local</a></code>(8) user&#8217;s home directory.</p>
<dt><code>mail_spool_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The directory where <code><a href="/docs/linux/man/8-local/">local</a></code>(8) UNIX-style mailboxes are kept.</p>
<dt><code>fallback_transport_maps (empty)</code></p>
<dd>Optional lookup tables with per-recipient message delivery transports for recipients that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent could not find in the <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) or UNIX password database.</p>
<dt><code>fallback_transport (empty)</code></p>
<dd>Optional message delivery transport that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent should use for names that are not found in the <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) or UNIX password database.</p>
<dt><code>luser_relay (empty)</code></p>
<dd>Optional catch-all destination for unknown <code><a href="/docs/linux/man/8-local/">local</a></code>(8) recipients.</dl>
<p> Available in Postfix version 2.2 and later:</p>
<dl>
<dt><code>command_execution_directory (empty)</code></p>
<dd>The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent working directory for delivery to external command.</dl>
<h2>Mailbox Locking Controls</h2>
<dl>
<dt><code>deliver_lock_attempts (20)</code></p>
<dd>The maximal number of attempts to acquire an exclusive lock on a mailbox file or <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) logfile.</p>
<dt><code>deliver_lock_delay (1s)</code></p>
<dd>The time between attempts to acquire an exclusive lock on a mailbox file or <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) logfile.</p>
<dt><code>stale_lock_time (500s)</code></p>
<dd>The time after which a stale exclusive mailbox lockfile is removed.</p>
<dt><code>mailbox_delivery_lock (see &#8216;postconf -d&#8217; output)</code></p>
<dd>How to lock a UNIX-style <code><a href="/docs/linux/man/8-local/">local</a></code>(8) mailbox before attempting delivery.</dl>
<h2>Resource And Rate Controls</h2>
<dl>
<dt><code>command_time_limit (1000s)</code></p>
<dd>Time limit for delivery to external commands.</p>
<dt><code>duplicate_filter_limit (1000)</code></p>
<dd>The maximal number of addresses remembered by the address duplicate filter for <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) or <code><a href="/docs/linux/man/5-virtual/">virtual</a></code>(5) alias expansion, or for <code><a href="/docs/linux/man/8-showq/">showq</a></code>(8) queue displays.</p>
<dt><code>local_destination_concurrency_limit (2)</code></p>
<dd>The maximal number of parallel deliveries via the local mail delivery transport to the same recipient (when &quot;local_destination_recipient_limit = 1&quot;) or the maximal number of parallel deliveries to the same local domain (when &quot;local_destination_recipient_limit &gt; 1&quot;).</p>
<dt><code>local_destination_recipient_limit (1)</code></p>
<dd>The maximal number of recipients per message delivery via the local mail delivery transport.</p>
<dt><code>mailbox_size_limit (51200000)</code></p>
<dd>The maximal size of any <code><a href="/docs/linux/man/8-local/">local</a></code>(8) individual mailbox or maildir file, or zero (no limit).</dl>
<h2>Security Controls</h2>
<dl>
<dt><code>allow_mail_to_commands (alias, forward)</code></p>
<dd>Restrict <code><a href="/docs/linux/man/8-local/">local</a></code>(8) mail delivery to external commands.</p>
<dt><code>allow_mail_to_files (alias, forward)</code></p>
<dd>Restrict <code><a href="/docs/linux/man/8-local/">local</a></code>(8) mail delivery to external files.</p>
<dt><code>command_expansion_filter (see &#8216;postconf -d&#8217; output)</code></p>
<dd>Restrict the characters that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent allows in $name expansions of $mailbox_command and $command_execution_directory.</p>
<dt><code>default_privs (nobody)</code></p>
<dd>The default rights used by the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent for delivery to external file or command.</p>
<dt><code>forward_expansion_filter (see &#8216;postconf -d&#8217; output)</code></p>
<dd>Restrict the characters that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent allows in $name expansions of $forward_path.</dl>
<p> Available in Postfix version 2.2 and later:</p>
<dl>
<dt><code>execution_directory_expansion_filter (see &#8216;postconf -d&#8217; output)</code></p>
<dd>Restrict the characters that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent allows in $name expansions of $command_execution_directory.</dl>
<p> Available in Postfix version 2.5.3 and later:</p>
<dl>
<dt><code>strict_mailbox_ownership (yes)</code></p>
<dd>Defer delivery when a mailbox file is not owned by its recipient.</dl>
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
<dt><code>local_command_shell (empty)</code></p>
<dd>Optional shell program for <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery to non-Postfix command.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>max_use (100)</code></p>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</p>
<dt><code>prepend_delivered_header (command, file, forward)</code></p>
<dd>The message delivery contexts where the Postfix <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent prepends a Delivered-To: message header with the address that the mail was delivered to.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>propagate_unmatched_extensions (canonical, virtual)</code></p>
<dd>What address lookup tables copy an address extension from the lookup key to the lookup result.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The location of the Postfix top-level queue directory.</p>
<dt><code>recipient_delimiter (empty)</code></p>
<dd>The separator between user names and address extensions (user+foo).</p>
<dt><code>require_home_directory (no)</code></p>
<dd>Require that a <code><a href="/docs/linux/man/8-local/">local</a></code>(8) recipient&#8217;s home directory exists before mail delivery is attempted.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<h2>Files</h2>
<pre>The following are examples; details differ between systems.
$HOME/.forward, per-user aliasing
/etc/aliases, system-wide alias database
/var/spool/mail, system mailboxes</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), queue manager
<a href="//www.systutorials.com/docs/linux/man/8-bounce/">bounce</a>(8), delivery status reports
<a href="//www.systutorials.com/docs/linux/man/1-newaliases/">newaliases</a>(1), create/update alias database
<a href="//www.systutorials.com/docs/linux/man/1-postalias/">postalias</a>(1), create/update alias database
<a href="//www.systutorials.com/docs/linux/man/5-aliases/">aliases</a>(5), format of alias database
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), generic daemon options
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>The <code>Delivered-To:</code> message header appears in the <code>qmail</code> system by Daniel Bernstein. </p>
<p> The <i>maildir</i> structure appears in the <code>qmail</code> system by Daniel Bernstein.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
