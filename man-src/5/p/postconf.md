---
title: "postconf(5)"
name: "postconf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-postconf/"
description: "postconf – Postfix configuration parameters"
---

<p>postconf &#8211; Postfix configuration parameters</p>
<h2>Synopsis</h2>
<pre><code>postconf</code> <i>parameter</i> ...
<code>postconf -e</code> &quot;<i>parameter=value</i>&quot; ...</pre>
<h2>Description</h2>
<p>The Postfix main.cf configuration file specifies parameters that control the operation of the Postfix mail system. Typically the file contains only a small subset of all parameters; parameters not specified are left at their default values. </p>
<p> The general format of the main.cf file is as follows:</p>
<dl>
<dt>&bull;</p>
<dd>Each logical line has the form &quot;parameter = value&quot;. Whitespace around the &quot;=&quot; is ignored, as is whitespace at the end of a logical line.</p>
<dt>&bull;</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>&bull;</p>
<dd>A logical line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</p>
<dt>&bull;</p>
<dd>A parameter value may refer to other parameters.</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>The expressions &quot;$name&quot; and &quot;${name}&quot; are recursively replaced with the value of the named parameter. The parameter name must contain only characters from the set [a-zA-Z0-9_]. An undefined parameter value is replaced with the empty value.</p>
<dt>&bull;</p>
<dd>The expressions &quot;${name?value}&quot; and &quot;${name?{value}}&quot; are replaced with &quot;value&quot; when &quot;$name&quot; is non-empty. The parameter name must contain only characters from the set [a-zA-Z0-9_]. These forms are supported with Postfix versions &gt;= 2.2 and &gt;= 3.0, respectively.</p>
<dt>&bull;</p>
<dd>The expressions &quot;${name:value}&quot; and &quot;${name:{value}}&quot; are replaced with &quot;value&quot; when &quot;$name&quot; is empty. The parameter name must contain only characters from the set [a-zA-Z0-9_]. These forms are supported with Postfix versions &gt;= 2.2 and &gt;= 3.0, respectively.</p>
<dt>&bull;</p>
<dd>The expression &quot;${name?{value1}:{value2}}&quot; is replaced with &quot;value1&quot; when &quot;$name&quot; is non-empty, and with &quot;value2&quot; when &quot;$name&quot; is empty. The &quot;{}&quot; is required for &quot;value1&quot;, optional for &quot;value2&quot;. The parameter name must contain only characters from the set [a-zA-Z0-9_]. This form is supported with Postfix versions &gt;= 3.0.</p>
<dt>&bull;</p>
<dd>The first item inside &quot;${&#8230;}&quot; may be a relational expression of the form: &quot;{value3} == {value4}&quot;. Besides the &quot;==&quot; (equality) operator Postfix supports &quot;!=&quot; (inequality), &quot;&lt;&quot;, &quot;&lt;=&quot;, &quot;&gt;=&quot;, and &quot;&gt;&quot;. The comparison is numerical when both operands are all digits, otherwise the comparison is lexicographical. These forms are supported with Postfix versions &gt;= 3.0.</p>
<dt>&bull;</p>
<dd>Each &quot;value&quot; is subject to recursive named parameter and relational expression evaluation, except where noted.</p>
<dt>&bull;</p>
<dd>Whitespace before or after each &quot;{value}&quot; is ignored.</p>
<dt>&bull;</p>
<dd>Specify &quot;$$&quot; to produce a single &quot;$&quot; character.</p>
<dt>&bull;</p>
<dd>The legacy form &quot;$(&#8230;)&quot; is equivalent to the preferred form &quot;${&#8230;}&quot;.</dl>
</dl>
<dt>&bull;</p>
<dd>When the same parameter is defined multiple times, only the last instance is remembered.</p>
<dt>&bull;</p>
<dd>Otherwise, the order of main.cf parameter definitions does not matter.</dl>
<p> The remainder of this document is a description of all Postfix configuration parameters. Default values are shown after the parameter name in parentheses, and can be looked up with the &quot;<code>postconf -d</code>&quot; command. </p>
<p> Note: this is not an invitation to make changes to Postfix configuration parameters. Unnecessary changes can impair the operation of the mail system.</p>
<h2>2bounce_notice_recipient (default: postmaster)</h2>
<p>The recipient of undeliverable mail that cannot be returned to the sender. This feature is enabled with the notify_classes parameter.</p>
<h2>access_map_defer_code (default: 450)</h2>
<p>The numerical Postfix SMTP server response code for an <code><a href="/docs/linux/man/5-access/">access</a></code>(5) map &quot;defer&quot; action, including &quot;defer_if_permit&quot; or &quot;defer_if_reject&quot;. Prior to Postfix 2.6, the response is hard-coded as &quot;450&quot;. </p>
<p> Do not change this unless you have a complete understanding of RFC 5321. </p>
<p> This feature is available in Postfix 2.6 and later.</p>
<h2>access_map_reject_code (default: 554)</h2>
<p>The numerical Postfix SMTP server response code for an <code><a href="/docs/linux/man/5-access/">access</a></code>(5) map &quot;reject&quot; action. </p>
<p> Do not change this unless you have a complete understanding of RFC 5321.</p>
<h2>address_verify_cache_cleanup_interval (default: 12h)</h2>
<p>The amount of time between <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) address verification database cleanup runs. This feature requires that the database supports the &quot;delete&quot; and &quot;sequence&quot; operators. Specify a zero interval to disable database cleanup. </p>
<p> After each database cleanup run, the <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) daemon logs the number of entries that were retained and dropped. A cleanup run is logged as &quot;partial&quot; when the daemon terminates early after &quot;<code>postfix reload</code>&quot;, &quot;<code>postfix stop</code>&quot;, or no requests for $max_idle seconds. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). </p>
<p> This feature is available in Postfix 2.7.</p>
<h2>address_verify_default_transport (default: $default_transport)</h2>
<p>Overrides the default_transport parameter setting for address verification probes. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_local_transport (default: $local_transport)</h2>
<p>Overrides the local_transport parameter setting for address verification probes. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_map (default: see postconf -d output)</h2>
<p>Lookup table for persistent address verification status storage. The table is maintained by the <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) service, and is opened before the process releases privileges. </p>
<p> The lookup table is persistent by default (Postfix 2.7 and later). Specify an empty table name to keep the information in volatile memory which is lost after &quot;<code>postfix reload</code>&quot; or &quot;<code>postfix stop</code>&quot;. This is the default with Postfix version 2.6 and earlier. </p>
<p> Specify a location in a file system that will not fill up. If the database becomes corrupted, the world comes to an end. To recover delete (NOT: truncate) the file and do &quot;<code>postfix reload</code>&quot;. </p>
<p> Postfix daemon processes do not use root privileges when opening this file (Postfix 2.5 and later). The file must therefore be stored under a Postfix-owned directory such as the data_directory. As a migration aid, an attempt to open the file under a non-Postfix directory is redirected to the Postfix-owned data_directory, and a warning is logged. </p>
<p> Examples: </p>
<pre>address_verify_map = hash:/var/lib/postfix/verify
address_verify_map = btree:/var/lib/postfix/verify</pre>
<p>This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_negative_cache (default: yes)</h2>
<p>Enable caching of failed address verification probe results. When this feature is enabled, the cache may pollute quickly with garbage. When this feature is disabled, Postfix will generate an address probe for every lookup. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_negative_expire_time (default: 3d)</h2>
<p>The time after which a failed probe expires from the address verification cache. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_negative_refresh_time (default: 3h)</h2>
<p>The time after which a failed address verification probe needs to be refreshed. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_pending_request_limit (default: see postconf -d output)</h2>
<p>A safety limit that prevents address verification requests from overwhelming the Postfix queue. By default, the number of pending requests is limited to 1/4 of the active queue maximum size (qmgr_message_active_limit). The queue manager enforces the limit by tempfailing requests that exceed the limit. This affects only unknown addresses and inactive addresses that have expired, because the <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) daemon automatically refreshes an active address before it expires. </p>
<p> This feature is available in Postfix 3.1 and later.</p>
<h2>address_verify_poll_count (default: normal: 3, overload: 1)</h2>
<p>How many times to query the <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) service for the completion of an address verification request in progress. </p>
<p> By default, the Postfix SMTP server polls the <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) service up to three times under non-overload conditions, and only once when under overload. With Postfix version 2.5 and earlier, the SMTP server always polls the <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) service up to three times by default. </p>
<p> Specify 1 to implement a crude form of greylisting, that is, always defer the first delivery request for a new address. </p>
<p> Examples: </p>
<pre># Postfix &lt;= 2.6 default
address_verify_poll_count = 3
# Poor man's greylisting
address_verify_poll_count = 1</pre>
<p>This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_poll_delay (default: 3s)</h2>
<p>The delay between queries for the completion of an address verification request in progress. </p>
<p> The default polling delay is 3 seconds. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_positive_expire_time (default: 31d)</h2>
<p>The time after which a successful probe expires from the address verification cache. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_positive_refresh_time (default: 7d)</h2>
<p>The time after which a successful address verification probe needs to be refreshed. The address verification status is not updated when the probe fails (optimistic caching). </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_relay_transport (default: $relay_transport)</h2>
<p>Overrides the relay_transport parameter setting for address verification probes. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_relayhost (default: $relayhost)</h2>
<p>Overrides the relayhost parameter setting for address verification probes. This information can be overruled with the <code><a href="/docs/linux/man/5-transport/">transport</a></code>(5) table. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_sender (default: $double_bounce_sender)</h2>
<p>The sender address to use in address verification probes; prior to Postfix 2.5 the default was &quot;postmaster&quot;. To avoid problems with address probes that are sent in response to address probes, the Postfix SMTP server excludes the probe sender address from all SMTPD access blocks. </p>
<p> Specify an empty value (address_verify_sender =) or &lt;&gt; if you want to use the null sender address. Beware, some sites reject mail from &lt;&gt;, even though RFCs require that such addresses be accepted. </p>
<p> Examples: </p>
<pre>address_verify_sender = &lt;&gt;
address_verify_sender = postmaster [at] my.domain</pre>
<p>This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_sender_dependent_default_transport_maps (default: $sender_dependent_default_transport_maps)</h2>
<p>Overrides the sender_dependent_default_transport_maps parameter setting for address verification probes. </p>
<p> This feature is available in Postfix 2.7 and later.</p>
<h2>address_verify_sender_dependent_relayhost_maps (default: $sender_dependent_relayhost_maps)</h2>
<p>Overrides the sender_dependent_relayhost_maps parameter setting for address verification probes. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>address_verify_sender_ttl (default: 0s)</h2>
<p>The time between changes in the time-dependent portion of address verification probe sender addresses. The time-dependent portion is appended to the localpart of the address specified with the address_verify_sender parameter. This feature is ignored when the probe sender addresses is the null sender, i.e. the address_verify_sender value is empty or &lt;&gt;. </p>
<p> Historically, the probe sender address was fixed. This has caused such addresses to end up on spammer mailing lists, and has resulted in wasted network and processing resources. </p>
<p> To enable time-dependent probe sender addresses, specify a non-zero time value (an integral value plus an optional one-letter suffix that specifies the time unit). Specify a value of at least several hours, to avoid problems with senders that use greylisting. Avoid nice TTL values, to make the result less predictable. Time units are: s (seconds), m (minutes), h (hours), d (days), w (weeks). </p>
<p> This feature is available in Postfix 2.9 and later.</p>
<h2>address_verify_service_name (default: verify)</h2>
<p>The name of the <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) address verification service. This service maintains the status of sender and/or recipient address verification probes, and generates probes on request by other Postfix processes.</p>
<h2>address_verify_transport_maps (default: $transport_maps)</h2>
<p>Overrides the transport_maps parameter setting for address verification probes. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>address_verify_virtual_transport (default: $virtual_transport)</h2>
<p>Overrides the virtual_transport parameter setting for address verification probes. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>alias_database (default: see postconf -d output)</h2>
<p>The alias databases for <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery that are updated with &quot;<code>newaliases</code>&quot; or with &quot;<code>sendmail -bi</code>&quot;. </p>
<p> This is a separate configuration parameter because not all the tables specified with $alias_maps have to be local files. </p>
<p> Examples: </p>
<pre>alias_database = hash:/etc/aliases
alias_database = hash:/etc/mail/aliases</pre>
<h2>alias_maps (default: see postconf -d output)</h2>
<p>The alias databases that are used for <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery. See <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) for syntax details. Specify zero or more &quot;type:name&quot; lookup tables, separated by whitespace or comma. Tables will be searched in the specified order until a match is found. Note: these lookups are recursive. </p>
<p> The default list is system dependent. On systems with NIS, the default is to search the local alias database, then the NIS alias database. </p>
<p> If you change the alias database, run &quot;<code>postalias /etc/aliases</code>&quot; (or wherever your system stores the mail alias file), or simply run &quot;<code>newaliases</code>&quot; to build the necessary DBM or DB file. </p>
<p> The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent disallows regular expression substitution of $1 etc. in alias_maps, because that would open a security hole. </p>
<p> The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent will silently ignore requests to use the <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server within alias_maps. Instead it will open the table directly. Before Postfix version 2.2, the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent will terminate with a fatal error. </p>
<p> Examples: </p>
<pre>alias_maps = hash:/etc/aliases, nis:mail.aliases
alias_maps = hash:/etc/aliases</pre>
<h2>allow_mail_to_commands (default: alias, forward)</h2>
<p>Restrict <code><a href="/docs/linux/man/8-local/">local</a></code>(8) mail delivery to external commands. The default is to disallow delivery to &quot;|command&quot; in :include: files (see <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) for the text that defines this terminology). </p>
<p> Specify zero or more of: <code>alias</code>, <code>forward</code> or <code>include</code>, in order to allow commands in <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5), .forward files or in :include: files, respectively. </p>
<p> Example: </p>
<pre>allow_mail_to_commands = alias,forward,include</pre>
<h2>allow_mail_to_files (default: alias, forward)</h2>
<p>Restrict <code><a href="/docs/linux/man/8-local/">local</a></code>(8) mail delivery to external files. The default is to disallow &quot;/file/name&quot; destinations in :include: files (see <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) for the text that defines this terminology). </p>
<p> Specify zero or more of: <code>alias</code>, <code>forward</code> or <code>include</code>, in order to allow &quot;/file/name&quot; destinations in <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5), .forward files and in :include: files, respectively. </p>
<p> Example: </p>
<pre>allow_mail_to_files = alias,forward,include</pre>
<h2>allow_min_user (default: no)</h2>
<p>Allow a sender or recipient address to have `-&#8216; as the first character. By default, this is not allowed, to avoid accidents with software that passes email addresses via the command line. Such software would not be able to distinguish a malicious address from a bona fide command-line option. Although this can be prevented by inserting a &quot;&#8211;&quot; option terminator into the command line, this is difficult to enforce consistently and globally. </p>
<p> As of Postfix version 2.5, this feature is implemented by trivial-<code><a href="/docs/linux/man/8-rewrite/">rewrite</a></code>(8). With earlier versions this feature was implemented by <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8) and was limited to recipient addresses only.</p>
<h2>allow_percent_hack (default: yes)</h2>
<p>Enable the rewriting of the form &quot;user%domain&quot; to &quot;user [at] domain&quot;. This is enabled by default. </p>
<p> Note: as of Postfix version 2.2, message header address rewriting happens only when one of the following conditions is true:</p>
<dl>
<dt>&bull;</p>
<dd>The message is received with the Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command,</p>
<dt>&bull;</p>
<dd>The message is received from a network client that matches $local_header_rewrite_clients,</p>
<dt>&bull;</p>
<dd>The message is received from the network, and the remote_header_rewrite_domain parameter specifies a non-empty value.
</dl>
<p> To get the behavior before Postfix version 2.2, specify &quot;local_header_rewrite_clients = static:all&quot;. </p>
<p> Example: </p>
<pre>allow_percent_hack = no</pre>
<h2>allow_untrusted_routing (default: no)</h2>
<p>Forward mail with sender-specified routing (user[@%!]remote[@%!]site) from untrusted clients to destinations matching $relay_domains. </p>
<p> By default, this feature is turned off. This closes a nasty open relay loophole where a backup MX host can be tricked into forwarding junk mail to a primary MX host which then spams it out to the world. </p>
<p> This parameter also controls if non-local addresses with sender-specified routing can match Postfix access tables. By default, such addresses cannot match Postfix access tables, because the address is ambiguous.</p>
<h2>alternate_config_directories (default: empty)</h2>
<p>A list of non-default Postfix configuration directories that may be specified with &quot;-c config_directory&quot; on the command line (in the case of <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1), with the &quot;-C&quot; option), or via the MAIL_CONFIG environment parameter. </p>
<p> This list must be specified in the default Postfix main.cf file, and will be used by set-gid Postfix commands such as <code><a href="/docs/linux/man/1-postqueue/">postqueue</a></code>(1) and <code><a href="/docs/linux/man/1-postdrop/">postdrop</a></code>(1). </p>
<p> Specify absolute pathnames, separated by comma or space. Note: $name expansion is not supported.</p>
<h2>always_add_missing_headers (default: no)</h2>
<p>Always add (Resent-) From:, To:, Date: or Message-ID: headers when not present. Postfix 2.6 and later add these headers only when clients match the local_header_rewrite_clients parameter setting. Earlier Postfix versions always add these headers; this may break DKIM signatures that cover non-existent headers. The undisclosed_recipients_header parameter setting determines whether a To: header will be added.</p>
<h2>always_bcc (default: empty)</h2>
<p>Optional address that receives a &quot;blind carbon copy&quot; of each message that is received by the Postfix mail system. </p>
<p> Note: with Postfix 2.3 and later the BCC address is added as if it was specified with NOTIFY=NONE. The sender will not be notified when the BCC address is undeliverable, as long as all down-stream software implements RFC 3461. </p>
<p> Note: with Postfix 2.2 and earlier the sender will be notified when the BCC address is undeliverable. </p>
<p> Note: automatic BCC recipients are produced only for new mail. To avoid mailer loops, automatic BCC recipients are not generated after Postfix forwards mail internally, or after Postfix generates mail itself.</p>
<h2>anvil_rate_time_unit (default: 60s)</h2>
<p>The time unit over which client connection rates and other rates are calculated. </p>
<p> This feature is implemented by the <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) service which is available in Postfix version 2.2 and later. </p>
<p> The default interval is relatively short. Because of the high frequency of updates, the <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server uses volatile memory only. Thus, information is lost whenever the process terminates. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>anvil_status_update_time (default: 600s)</h2>
<p>How frequently the <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) connection and rate limiting server logs peak usage information. </p>
<p> This feature is available in Postfix 2.2 and later. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>append_at_myorigin (default: yes)</h2>
<p>With locally submitted mail, append the string &quot;@$myorigin&quot; to mail addresses without domain information. With remotely submitted mail, append the string &quot;@$remote_header_rewrite_domain&quot; instead. </p>
<p> Note 1: this feature is enabled by default and must not be turned off. Postfix does not support domain-less addresses. </p>
<p> Note 2: with Postfix version 2.2, message header address rewriting happens only when one of the following conditions is true:</p>
<dl>
<dt>&bull;</p>
<dd>The message is received with the Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command,</p>
<dt>&bull;</p>
<dd>The message is received from a network client that matches $local_header_rewrite_clients,</p>
<dt>&bull;</p>
<dd>The message is received from the network, and the remote_header_rewrite_domain parameter specifies a non-empty value.
</dl>
<p> To get the behavior before Postfix version 2.2, specify &quot;local_header_rewrite_clients = static:all&quot;.</p>
<h2>append_dot_mydomain (default: Postfix &gt;= 3.0: no, Postfix &lt; 3.0: yes)</h2>
<p>With locally submitted mail, append the string &quot;.$mydomain&quot; to addresses that have no &quot;.domain&quot; information. With remotely submitted mail, append the string &quot;.$remote_header_rewrite_domain&quot; instead. </p>
<p> Note 1: this feature is enabled by default. If disabled, users will not be able to send mail to &quot;user [at] partialdomainname&quot; but will have to specify full domain names instead. </p>
<p> Note 2: with Postfix version 2.2, message header address rewriting happens only when one of the following conditions is true:</p>
<dl>
<dt>&bull;</p>
<dd>The message is received with the Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command,</p>
<dt>&bull;</p>
<dd>The message is received from a network client that matches $local_header_rewrite_clients,</p>
<dt>&bull;</p>
<dd>The message is received from the network, and the remote_header_rewrite_domain parameter specifies a non-empty value.
</dl>
<p> To get the behavior before Postfix version 2.2, specify &quot;local_header_rewrite_clients = static:all&quot;.</p>
<h2>application_event_drain_time (default: 100s)</h2>
<p>How long the <code><a href="/docs/linux/man/1-postkick/">postkick</a></code>(1) command waits for a request to enter the Postfix daemon process input buffer before giving up. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds). </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>authorized_flush_users (default: static:anyone)</h2>
<p>List of users who are authorized to flush the queue. </p>
<p> By default, all users are allowed to flush the queue. Access is always granted if the invoking user is the super-user or the $mail_owner user. Otherwise, the real UID of the process is looked up in the system password file, and access is granted only if the corresponding login name is on the access list. The username &quot;unknown&quot; is used for processes whose real UID is not found in the password file. </p>
<p> Specify a list of user names, &quot;/file/name&quot; or &quot;type:table&quot; patterns, separated by commas and/or whitespace. The list is matched left to right, and the search stops on the first match. A &quot;/file/name&quot; pattern is replaced by its contents; a &quot;type:table&quot; lookup table is matched when a name matches a lookup key (the lookup result is ignored). Continue long lines by starting the next line with whitespace. Specify &quot;!pattern&quot; to exclude a name from the list. The form &quot;!/file/name&quot; is supported only in Postfix version 2.4 and later. </p>
<p> This feature is available in Postfix 2.2 and later.</p>
<h2>authorized_mailq_users (default: static:anyone)</h2>
<p>List of users who are authorized to view the queue. </p>
<p> By default, all users are allowed to view the queue. Access is always granted if the invoking user is the super-user or the $mail_owner user. Otherwise, the real UID of the process is looked up in the system password file, and access is granted only if the corresponding login name is on the access list. The username &quot;unknown&quot; is used for processes whose real UID is not found in the password file. </p>
<p> Specify a list of user names, &quot;/file/name&quot; or &quot;type:table&quot; patterns, separated by commas and/or whitespace. The list is matched left to right, and the search stops on the first match. A &quot;/file/name&quot; pattern is replaced by its contents; a &quot;type:table&quot; lookup table is matched when a name matches a lookup key (the lookup result is ignored). Continue long lines by starting the next line with whitespace. Specify &quot;!pattern&quot; to exclude a user name from the list. The form &quot;!/file/name&quot; is supported only in Postfix version 2.4 and later. </p>
<p> This feature is available in Postfix 2.2 and later.</p>
<h2>authorized_submit_users (default: static:anyone)</h2>
<p>List of users who are authorized to submit mail with the <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command (and with the privileged <code><a href="/docs/linux/man/1-postdrop/">postdrop</a></code>(1) helper command). </p>
<p> By default, all users are allowed to submit mail. Otherwise, the real UID of the process is looked up in the system password file, and access is granted only if the corresponding login name is on the access list. The username &quot;unknown&quot; is used for processes whose real UID is not found in the password file. To deny mail submission access to all users specify an empty list. </p>
<p> Specify a list of user names, &quot;/file/name&quot; or &quot;type:table&quot; patterns, separated by commas and/or whitespace. The list is matched left to right, and the search stops on the first match. A &quot;/file/name&quot; pattern is replaced by its contents; a &quot;type:table&quot; lookup table is matched when a name matches a lookup key (the lookup result is ignored). Continue long lines by starting the next line with whitespace. Specify &quot;!pattern&quot; to exclude a user name from the list. The form &quot;!/file/name&quot; is supported only in Postfix version 2.4 and later. </p>
<p> Example: </p>
<pre>authorized_submit_users = !www, static:all</pre>
<p>This feature is available in Postfix 2.2 and later.</p>
<h2>authorized_verp_clients (default: $mynetworks)</h2>
<p>What remote SMTP clients are allowed to specify the XVERP command. This command requests that mail be delivered one recipient at a time with a per recipient return address. </p>
<p> By default, only trusted clients are allowed to specify XVERP. </p>
<p> This parameter was introduced with Postfix version 1.1. Postfix version 2.1 renamed this parameter to smtpd_authorized_verp_clients and changed the default to none. </p>
<p> Specify a list of network/netmask patterns, separated by commas and/or whitespace. The mask specifies the number of bits in the network part of a host address. You can also specify hostnames or .domain names (the initial dot causes the domain to match any name below it), &quot;/file/name&quot; or &quot;type:table&quot; patterns. A &quot;/file/name&quot; pattern is replaced by its contents; a &quot;type:table&quot; lookup table is matched when a table entry matches a lookup string (the lookup result is ignored). Continue long lines by starting the next line with whitespace. Specify &quot;!pattern&quot; to exclude an address or network block from the list. The form &quot;!/file/name&quot; is supported only in Postfix version 2.4 and later. </p>
<p> Note: IP version 6 address information must be specified inside [] in the authorized_verp_clients value, and in files specified with &quot;/file/name&quot;. IP version 6 addresses contain the &quot;:&quot; character, and would otherwise be confused with a &quot;type:table&quot; pattern.</p>
<h2>backwards_bounce_logfile_compatibility (default: yes)</h2>
<p>Produce additional <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) logfile records that can be read by Postfix versions before 2.0. The current and more extensible &quot;name = value&quot; format is needed in order to implement more sophisticated functionality. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>berkeley_db_create_buffer_size (default: 16777216)</h2>
<p>The per-table I/O buffer size for programs that create Berkeley DB hash or btree tables. Specify a byte count. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<h2>berkeley_db_read_buffer_size (default: 131072)</h2>
<p>The per-table I/O buffer size for programs that read Berkeley DB hash or btree tables. Specify a byte count. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<h2>best_mx_transport (default: empty)</h2>
<p>Where the Postfix SMTP client should deliver mail when it detects a &quot;mail loops back to myself&quot; error condition. This happens when the local MTA is the best SMTP mail exchanger for a destination not listed in $mydestination, $inet_interfaces, $proxy_interfaces, $virtual_alias_domains, or $virtual_mailbox_domains. By default, the Postfix SMTP client returns such mail as undeliverable. </p>
<p> Specify, for example, &quot;best_mx_transport = local&quot; to pass the mail from the Postfix SMTP client to the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent. You can specify any message delivery &quot;transport&quot; or &quot;transport:nexthop&quot; that is defined in the master.cf file. See the <code><a href="/docs/linux/man/5-transport/">transport</a></code>(5) manual page for the syntax and meaning of &quot;transport&quot; or &quot;transport:nexthop&quot;. </p>
<p> However, this feature is expensive because it ties up a Postfix SMTP client process while the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent is doing its work. It is more efficient (for Postfix) to list all hosted domains in a table or database.</p>
<h2>biff (default: yes)</h2>
<p>Whether or not to use the local biff service. This service sends &quot;new mail&quot; notifications to users who have requested new mail notification with the UNIX command &quot;biff y&quot;. </p>
<p> For compatibility reasons this feature is on by default. On systems with lots of interactive users, the biff service can be a performance drain. Specify &quot;biff = no&quot; in main.cf to disable.</p>
<h2>body_checks (default: empty)</h2>
<p>Optional lookup tables for content inspection as specified in the <code><a href="/docs/linux/man/5-body_checks/">body_checks</a></code>(5) manual page. </p>
<p> Note: with Postfix versions before 2.0, these rules inspect all content after the primary message headers.</p>
<h2>body_checks_size_limit (default: 51200)</h2>
<p>How much text in a message body segment (or attachment, if you prefer to use that term) is subjected to body_checks inspection. The amount of text is limited to avoid scanning huge attachments. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<h2>bounce_notice_recipient (default: postmaster)</h2>
<p>The recipient of postmaster notifications with the message headers of mail that Postfix did not deliver and of SMTP conversation transcripts of mail that Postfix did not receive. This feature is enabled with the notify_classes parameter.</p>
<h2>bounce_queue_lifetime (default: 5d)</h2>
<p>Consider a bounce message as undeliverable, when delivery fails with a temporary error, and the time in the queue has reached the bounce_queue_lifetime limit. By default, this limit is the same as for regular mail. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is d (days). </p>
<p> Specify 0 when mail delivery should be tried only once. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>bounce_service_name (default: bounce)</h2>
<p>The name of the <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) service. This service maintains a record of failed delivery attempts and generates non-delivery notifications. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<h2>bounce_size_limit (default: 50000)</h2>
<p>The maximal amount of original message text that is sent in a non-delivery notification. Specify a byte count. A message is returned as either message/rfc822 (the complete original) or as text/rfc822-headers (the headers only). With Postfix version 2.4 and earlier, a message is always returned as message/rfc822 and is truncated when it exceeds the size limit. </p>
<p> Notes:</p>
<dl>
<dt>&bull;</p>
<dd>If you increase this limit, then you should increase the mime_nesting_limit value proportionally.</p>
<dt>&bull;</p>
<dd>Be careful when making changes. Excessively large values will result in the loss of non-delivery notifications, when a bounce message size exceeds a local or remote MTA&#8217;s message size limit.
</dl>
<h2>bounce_template_file (default: empty)</h2>
<p>Pathname of a configuration file with bounce message templates. These override the built-in templates of delivery status notification (DSN) messages for undeliverable mail, for delayed mail, successful delivery, or delivery verification. The <code><a href="/docs/linux/man/5-bounce/">bounce</a></code>(5) manual page describes how to edit and test template files. </p>
<p> Template message body text may contain $name references to Postfix configuration parameters. The result of $name expansion can be previewed with &quot;<code>postconf -b </code><i>file_name</i>&quot; before the file is placed into the Postfix configuration directory. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>broken_sasl_auth_clients (default: no)</h2>
<p>Enable interoperability with remote SMTP clients that implement an obsolete version of the AUTH command (RFC 4954). Examples of such clients are MicroSoft Outlook Express version 4 and MicroSoft Exchange version 5.0. </p>
<p> Specify &quot;broken_sasl_auth_clients = yes&quot; to have Postfix advertise AUTH support in a non-standard way.</p>
<h2>canonical_classes (default: envelope_sender, envelope_recipient, header_sender, header_recipient)</h2>
<p>What addresses are subject to canonical_maps address mapping. By default, canonical_maps address mapping is applied to envelope sender and recipient addresses, and to header sender and header recipient addresses. </p>
<p> Specify one or more of: envelope_sender, envelope_recipient, header_sender, header_recipient </p>
<p> This feature is available in Postfix 2.2 and later.</p>
<h2>canonical_maps (default: empty)</h2>
<p>Optional address mapping lookup tables for message headers and envelopes. The mapping is applied to both sender and recipient addresses, in both envelopes and in headers, as controlled with the canonical_classes parameter. This is typically used to clean up dirty addresses from legacy mail systems, or to replace login names by Firstname.Lastname. The table format and lookups are documented in <code><a href="/docs/linux/man/5-canonical/">canonical</a></code>(5). For an overview of Postfix address manipulations see the ADDRESS_REWRITING_README document. </p>
<p> Specify zero or more &quot;type:name&quot; lookup tables, separated by whitespace or comma. Tables will be searched in the specified order until a match is found. Note: these lookups are recursive. </p>
<p> If you use this feature, run &quot;<code>postmap /etc/postfix/canonical</code>&quot; to build the necessary DBM or DB file after every change. The changes will become visible after a minute or so. Use &quot;<code>postfix reload</code>&quot; to eliminate the delay. </p>
<p> Note: with Postfix version 2.2, message header address mapping happens only when message header address rewriting is enabled:</p>
<dl>
<dt>&bull;</p>
<dd>The message is received with the Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command,</p>
<dt>&bull;</p>
<dd>The message is received from a network client that matches $local_header_rewrite_clients,</p>
<dt>&bull;</p>
<dd>The message is received from the network, and the remote_header_rewrite_domain parameter specifies a non-empty value.
</dl>
<p> To get the behavior before Postfix version 2.2, specify &quot;local_header_rewrite_clients = static:all&quot;. </p>
<p> Examples: </p>
<pre>canonical_maps = dbm:/etc/postfix/canonical
canonical_maps = hash:/etc/postfix/canonical</pre>
<h2>cleanup_service_name (default: cleanup)</h2>
<p>The name of the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) service. This service rewrites addresses into the standard form, and performs <code><a href="/docs/linux/man/5-canonical/">canonical</a></code>(5) address mapping and <code><a href="/docs/linux/man/5-virtual/">virtual</a></code>(5) aliasing. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<h2>command_directory (default: see postconf -d output)</h2>
<p>The location of all postfix administrative commands.</p>
<h2>command_execution_directory (default: empty)</h2>
<p>The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent working directory for delivery to external command. Failure to change directory causes the delivery to be deferred. </p>
<p> The command_execution_directory value is not subject to Postfix configuration parameter $name expansion. Instead, the following $name expansions are done on command_execution_directory before the directory is used. Expansion happens in the context of the delivery request. The result of $name expansion is filtered with the character set that is specified with the execution_directory_expansion_filter parameter.</p>
<dl>
<dt><code>$user</code></p>
<dd>The recipient&#8217;s username. </p>
<dt><code>$shell</code></p>
<dd>The recipient&#8217;s login shell pathname. </p>
<dt><code>$home</code></p>
<dd>The recipient&#8217;s home directory. </p>
<dt><code>$recipient</code></p>
<dd>The full recipient address. </p>
<dt><code>$extension</code></p>
<dd>The optional recipient address extension. </p>
<dt><code>$domain</code></p>
<dd>The recipient domain. </p>
<dt><code>$local</code></p>
<dd>The entire recipient localpart. </p>
<dt><code>$recipient_delimiter</code></p>
<dd>The address extension delimiter that was found in the recipient address (Postfix 2.11 and later), or the system-wide recipient address extension delimiter (Postfix 2.10 and earlier). </p>
<dt><code>${name?value}</code></p>
<dd>Expands to <i>value</i> when <i>$name</i> is non-empty. </p>
<dt><code>${name:value}</code></p>
<dd>Expands to <i>value</i> when <i>$name</i> is empty. </p>
</dl>
<p> Instead of $name you can also specify ${name} or $(name). </p>
<p> This feature is available in Postfix 2.2 and later.</p>
<h2>command_expansion_filter (default: see postconf -d output)</h2>
<p>Restrict the characters that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent allows in $name expansions of $mailbox_command and $command_execution_directory. Characters outside the allowed set are replaced by underscores.</p>
<h2>command_time_limit (default: 1000s)</h2>
<p>Time limit for delivery to external commands. This limit is used by the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent, and is the default time limit for delivery by the <code><a href="/docs/linux/man/8-pipe/">pipe</a></code>(8) delivery agent. </p>
<p> Note: if you set this time limit to a large value you must update the global ipc_timeout parameter as well.</p>
<h2>compatibility_level (default: 0)</h2>
<p>A safety net that causes Postfix to run with backwards-compatible default settings after an upgrade to a newer Postfix version. </p>
<p> With backwards compatibility turned on (the main.cf compatibility_level value is less than the Postfix built-in value), Postfix looks for settings that are left at their implicit default value, and logs a message when a backwards-compatible default setting is required. </p>
<pre>using backwards-compatible default setting <i>name=value</i>
 to [accept a specific client request]
using backwards-compatible default setting <i>name=value</i>
 to [enable specific Postfix behavior]</pre>
<p>See COMPATIBILITY_README for specific message details. If such a message is logged in the context of a legitimate request, the system administrator should make the backwards-compatible setting permanent in main.cf or master.cf, for example: </p>
<pre># <code>postconf</code> <i>name=value</i>
# <code>postfix reload</code></pre>
<p>When no more backwards-compatible settings need to be made permanent, the administrator should turn off backwards compatibility by updating the compatibility_level setting in main.cf: </p>
<pre># <code>postconf compatibility_level=</code><i>N</i>
# <code>postfix reload</code></pre>
<p>For <i>N</i> specify the number that is logged in your <code><a href="/docs/linux/man/1-postfix/">postfix</a></code>(1) warning message: </p>
<pre>warning: To disable backwards compatibility use &quot;postconf
 compatibility_level=<i>N</i>&quot; and &quot;postfix reload&quot;</pre>
<p>This feature is available in Postfix 3.0 and later.</p>
<h2>config_directory (default: see postconf -d output)</h2>
<p>The default location of the Postfix main.cf and master.cf configuration files. This can be overruled via the following mechanisms:</p>
<dl>
<dt>&bull;</p>
<dd>The MAIL_CONFIG environment variable (daemon processes and commands).</p>
<dt>&bull;</p>
<dd>The &quot;-c&quot; command-line option (commands only).
</dl>
<p> With Postfix command that run with set-gid privileges, a config_directory override requires either root privileges, or it requires that the directory is listed with the alternate_config_directories parameter in the default main.cf file.</p>
<h2>confirm_delay_cleared (default: no)</h2>
<p>After sending a &quot;your message is delayed&quot; notification, inform the sender when the delay clears up. This can result in a sudden burst of notifications at the end of a prolonged network outage, and is therefore disabled by default. </p>
<p> See also: delay_warning_time. </p>
<p> This feature is available in Postfix 3.0 and later.</p>
<h2>connection_cache_protocol_timeout (default: 5s)</h2>
<p>Time limit for connection cache connect, send or receive operations. The time limit is enforced in the client. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>connection_cache_service_name (default: scache)</h2>
<p>The name of the <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) connection cache service. This service maintains a limited pool of cached sessions. </p>
<p> This feature is available in Postfix 2.2 and later.</p>
<h2>connection_cache_status_update_time (default: 600s)</h2>
<p>How frequently the <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) server logs usage statistics with connection cache hit and miss rates for logical destinations and for physical endpoints.</p>
<h2>connection_cache_ttl_limit (default: 2s)</h2>
<p>The maximal time-to-live value that the <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) connection cache server allows. Requests that specify a larger TTL will be stored with the maximum allowed TTL. The purpose of this additional control is to protect the infrastructure against careless people. The cache TTL is already bounded by $max_idle.</p>
<h2>content_filter (default: empty)</h2>
<p>After the message is queued, send the entire message to the specified <i>transport:destination</i>. The <i>transport</i> name specifies the first field of a mail delivery agent definition in master.cf; the syntax of the next-hop <i>destination</i> is described in the manual page of the corresponding delivery agent. More information about external content filters is in the Postfix FILTER_README file. </p>
<p> Notes:</p>
<dl>
<dt>&bull;</p>
<dd>This setting has lower precedence than a FILTER action that is specified in an <code><a href="/docs/linux/man/5-access/">access</a></code>(5), <code><a href="/docs/linux/man/5-header_checks/">header_checks</a></code>(5) or <code><a href="/docs/linux/man/5-body_checks/">body_checks</a></code>(5) table.</p>
<dt>&bull;</p>
<dd>The meaning of an empty next-hop filter <i>destination</i> is version dependent. Postfix 2.7 and later will use the recipient domain; earlier versions will use $myhostname. Specify &quot;default_filter_nexthop = $myhostname&quot; for compatibility with Postfix 2.6 or earlier, or specify a content_filter value with an explicit next-hop <i>destination</i>.
</dl>
<h2>cyrus_sasl_config_path (default: empty)</h2>
<p>Search path for Cyrus SASL application configuration files, currently used only to locate the $smtpd_sasl_path.conf file. Specify zero or more directories separated by a colon character, or an empty value to use Cyrus SASL&#8217;s built-in search path. </p>
<p> This feature is available in Postfix 2.5 and later when compiled with Cyrus SASL 2.1.22 or later.</p>
<h2>daemon_directory (default: see postconf -d output)</h2>
<p>The directory with Postfix support programs and daemon programs. These should not be invoked directly by humans. The directory must be owned by root.</p>
<h2>daemon_table_open_error_is_fatal (default: no)</h2>
<p>How a Postfix daemon process handles errors while opening lookup tables: gradual degradation or immediate termination.</p>
<dl>
<dt><code> no </code> (default)</p>
<dd>Gradual degradation: a daemon process logs a message of type &quot;error&quot; and continues execution with reduced functionality. Features that do not depend on the unavailable table will work normally, while features that depend on the table will result in a type &quot;warning&quot; message.<br />
 When the notify_classes parameter value contains the &quot;data&quot; class, the Postfix SMTP server and client will report transcripts of sessions with an error because a table is unavailable. </p>
<dt><code> yes </code> (historical behavior)</p>
<dd>Immediate termination: a daemon process logs a type &quot;fatal&quot; message and terminates immediately. This option reduces the number of possible code paths through Postfix, and may therefore be slightly more secure than the default. </p>
</dl>
<p> For the sake of sanity, the number of type &quot;error&quot; messages is limited to 13 over the lifetime of a daemon process. </p>
<p> This feature is available in Postfix 2.9 and later.</p>
<h2>daemon_timeout (default: 18000s)</h2>
<p>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>data_directory (default: see postconf -d output)</h2>
<p>The directory with Postfix-writable data files (for example: caches, pseudo-random numbers). This directory must be owned by the mail_owner account, and must not be shared with non-Postfix software. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>debug_peer_level (default: 2)</h2>
<p>The increment in verbose logging level when a remote client or server matches a pattern in the debug_peer_list parameter.</p>
<h2>debug_peer_list (default: empty)</h2>
<p>Optional list of remote client or server hostname or network address patterns that cause the verbose logging level to increase by the amount specified in $debug_peer_level. </p>
<p> Specify domain names, network/netmask patterns, &quot;/file/name&quot; patterns or &quot;type:table&quot; lookup tables. The right-hand side result from &quot;type:table&quot; lookups is ignored. </p>
<p> Pattern matching of domain names is controlled by the presence or absence of &quot;debug_peer_list&quot; in the parent_domain_matches_subdomains parameter value. </p>
<p> Examples: </p>
<pre>debug_peer_list = 127.0.0.1
debug_peer_list = example.com</pre>
<h2>debugger_command (default: empty)</h2>
<p>The external command to execute when a Postfix daemon program is invoked with the -D option. </p>
<p> Use &quot;command .. &amp; sleep 5&quot; so that the debugger can attach before the process marches on. If you use an X-based debugger, be sure to set up your XAUTHORITY environment variable before starting Postfix. </p>
<p> Note: the command is subject to $name expansion, before it is passed to the default command interpreter. Specify &quot;$$&quot; to produce a single &quot;$&quot; character. </p>
<p> Example: </p>
<pre>debugger_command =
 PATH=/usr/bin:/usr/X11R6/bin
 ddd $daemon_directory/$process_name $process_id &amp; sleep 5</pre>
<h2>default_database_type (default: see postconf -d output)</h2>
<p>The default database type for use in <code><a href="/docs/linux/man/1-newaliases/">newaliases</a></code>(1), <code><a href="/docs/linux/man/1-postalias/">postalias</a></code>(1) and <code><a href="/docs/linux/man/1-postmap/">postmap</a></code>(1) commands. On many UNIX systems the default type is either <code>dbm</code> or <code>hash</code>. The default setting is frozen when the Postfix system is built. </p>
<p> Examples: </p>
<pre>default_database_type = hash
default_database_type = dbm</pre>
<h2>default_delivery_slot_cost (default: 5)</h2>
<p>How often the Postfix queue manager&#8217;s scheduler is allowed to preempt delivery of one message with another. </p>
<p> Each transport maintains a so-called &quot;available delivery slot counter&quot; for each message. One message can be preempted by another one when the other message can be delivered using no more delivery slots (i.e., invocations of delivery agents) than the current message counter has accumulated (or will eventually accumulate &#8211; see about slot loans below). This parameter controls how often is the counter incremented &#8211; it happens after each default_delivery_slot_cost recipients have been delivered. </p>
<p> The cost of 0 is used to disable the preempting scheduling completely. The minimum value the scheduling algorithm can use is 2 &#8211; use it if you want to maximize the message throughput rate. Although there is no maximum, it doesn&#8217;t make much sense to use values above say 50. </p>
<p> The only reason why the value of 2 is not the default is the way this parameter affects the delivery of mailing-list mail. In the worst case, delivery can take somewhere between (cost+1/cost) and (cost/cost-1) times more than if the preemptive scheduler was disabled. The default value of 5 turns out to provide reasonable message response times while making sure the mailing-list deliveries are not extended by more than 20-25 percent even in the worst case. </p>
<p> Use <i>transport</i>_delivery_slot_cost to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport. </p>
<p> Examples: </p>
<pre>default_delivery_slot_cost = 0
default_delivery_slot_cost = 2</pre>
<h2>default_delivery_slot_discount (default: 50)</h2>
<p>The default value for transport-specific _delivery_slot_discount settings. </p>
<p> This parameter speeds up the moment when a message preemption can happen. Instead of waiting until the full amount of delivery slots required is available, the preemption can happen when transport_delivery_slot_discount percent of the required amount plus transport_delivery_slot_loan still remains to be accumulated. Note that the full amount will still have to be accumulated before another preemption can take place later. </p>
<p> Use <i>transport</i>_delivery_slot_discount to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport.</p>
<h2>default_delivery_slot_loan (default: 3)</h2>
<p>The default value for transport-specific _delivery_slot_loan settings. </p>
<p> This parameter speeds up the moment when a message preemption can happen. Instead of waiting until the full amount of delivery slots required is available, the preemption can happen when transport_delivery_slot_discount percent of the required amount plus transport_delivery_slot_loan still remains to be accumulated. Note that the full amount will still have to be accumulated before another preemption can take place later. </p>
<p> Use <i>transport</i>_delivery_slot_loan to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport.</p>
<h2>default_delivery_status_filter (default: empty)</h2>
<p>Optional filter to replace the delivery status code or explanatory text of successful or unsuccessful deliveries. This does not allow the replacement of a successful status code (2.X.X) with an unsuccessful status code (4.X.X or 5.X.X) or vice versa. </p>
<p> Note: the (smtp|lmtp)_delivery_status_filter is applied only once per recipient: when delivery is successful, when delivery is rejected with 5XX, or when there are no more alternate MX or A destinations. Use smtp_reply_filter or lmtp_reply_filter to inspect responses for all delivery attempts. </p>
<p> The following parameters can be used to implement a filter for specific delivery agents: lmtp_delivery_status_filter, local_delivery_status_filter, pipe_delivery_status_filter, smtp_delivery_status_filter or virtual_delivery_status_filter. These parameters support the same filter syntax as described here. </p>
<p> Specify zero or more &quot;type:table&quot; lookup table names, separated by comma or whitespace. For each successful or unsuccessful delivery to a recipient, the tables are queried in the specified order with one line of text that is structured as follows: </p>
<p> enhanced-status-code SPACE explanatory-text </p>
<p> The first table match wins. The lookup result must have the same structure as the query, a successful status code (2.X.X) must be replaced with a successful status code, an unsuccessful status code (4.X.X or 5.X.X) must be replaced with an unsuccessful status code, and the explanatory text field must be non-empty. Other results will result in a warning. </p>
<p> Example 1: convert specific soft TLS errors into hard errors, by overriding the first number in the enhanced status code. </p>
<pre>/etc/postfix/main.cf:
 smtp_delivery_status_filter = pcre:/etc/postfix/smtp_dsn_filter</pre>
<pre>/etc/postfix/smtp_dsn_filter:
 /^4(\.\d+\.\d+ TLS is required, but host \S+ refused to start TLS: .+)/
 5$1
 /^4(\.\d+\.\d+ TLS is required, but was not offered by host .+)/
 5$1
 # Do not change the following into hard bounces. They may
 # result from a local configuration problem.
 # 4.\d+.\d+ TLS is required, but our TLS engine is unavailable
 # 4.\d+.\d+ TLS is required, but unavailable
 # 4.\d+.\d+ Cannot start TLS: handshake failure</pre>
<p>Example 2: censor the per-recipient delivery status text so that it does not reveal the destination command or filename when a remote sender requests confirmation of successful delivery. </p>
<pre>/etc/postfix/main.cf:
 local_delivery_status_filter = pcre:/etc/postfix/local_dsn_filter</pre>
<pre>/etc/postfix/local_dsn_filter:
 /^(2\S+ delivered to file).+/ $1
 /^(2\S+ delivered to command).+/ $1</pre>
<p>Notes:</p>
<dl>
<dt>&bull;</p>
<dd>This feature will NOT override the soft_bounce safety net.</p>
<dt>&bull;</p>
<dd>This feature will change the enhanced status code and text that is logged to the maillog file, and that is reported to the sender in delivery confirmation or non-delivery notifications.
</dl>
<p> This feature is available in Postfix 3.0 and later.</p>
<h2>default_destination_concurrency_failed_cohort_limit (default: 1)</h2>
<p>How many pseudo-cohorts must suffer connection or handshake failure before a specific destination is considered unavailable (and further delivery is suspended). Specify zero to disable this feature. A destination&#8217;s pseudo-cohort failure count is reset each time a delivery completes without connection or handshake failure for that specific destination. </p>
<p> A pseudo-cohort is the number of deliveries equal to a destination&#8217;s delivery concurrency. </p>
<p> Use <i>transport</i>_destination_concurrency_failed_cohort_limit to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport. </p>
<p> This feature is available in Postfix 2.5. The default setting is compatible with earlier Postfix versions.</p>
<h2>default_destination_concurrency_limit (default: 20)</h2>
<p>The default maximal number of parallel deliveries to the same destination. This is the default limit for delivery via the <code><a href="/docs/linux/man/8-lmtp/">lmtp</a></code>(8), <code><a href="/docs/linux/man/8-pipe/">pipe</a></code>(8), <code><a href="/docs/linux/man/8-smtp/">smtp</a></code>(8) and <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) delivery agents. With per-destination recipient limit &gt; 1, a destination is a domain, otherwise it is a recipient. </p>
<p> Use <i>transport</i>_destination_concurrency_limit to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport.</p>
<h2>default_destination_concurrency_negative_feedback (default: 1)</h2>
<p>The per-destination amount of delivery concurrency negative feedback, after a delivery completes with a connection or handshake failure. Feedback values are in the range 0..1 inclusive. With negative feedback, concurrency is decremented at the beginning of a sequence of length 1/feedback. This is unlike positive feedback, where concurrency is incremented at the end of a sequence of length 1/feedback. </p>
<p> As of Postfix version 2.5, negative feedback cannot reduce delivery concurrency to zero. Instead, a destination is marked dead (further delivery suspended) after the failed pseudo-cohort count reaches $default_destination_concurrency_failed_cohort_limit (or $<i>transport</i>_destination_concurrency_failed_cohort_limit). To make the scheduler completely immune to connection or handshake failures, specify a zero feedback value and a zero failed pseudo-cohort limit. </p>
<p> Specify one of the following forms:</p>
<dl>
<dt><i>number</i></p>
<dd>
<dt><i>number</i> / <i>number</i></p>
<dd>Constant feedback. The value must be in the range 0..1 inclusive. The default setting of &quot;1&quot; is compatible with Postfix versions before 2.5, where a destination&#8217;s delivery concurrency is throttled down to zero (and further delivery suspended) after a single failed pseudo-cohort. </p>
<dt><i>number</i> / concurrency</p>
<dd>Variable feedback of &quot;<i>number</i> / (delivery concurrency)&quot;. The <i>number</i> must be in the range 0..1 inclusive. With <i>number</i> equal to &quot;1&quot;, a destination&#8217;s delivery concurrency is decremented by 1 after each failed pseudo-cohort. </p>
</dl>
<p> A pseudo-cohort is the number of deliveries equal to a destination&#8217;s delivery concurrency. </p>
<p> Use <i>transport</i>_destination_concurrency_negative_feedback to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport. </p>
<p> This feature is available in Postfix 2.5. The default setting is compatible with earlier Postfix versions.</p>
<h2>default_destination_concurrency_positive_feedback (default: 1)</h2>
<p>The per-destination amount of delivery concurrency positive feedback, after a delivery completes without connection or handshake failure. Feedback values are in the range 0..1 inclusive. The concurrency increases until it reaches the per-destination maximal concurrency limit. With positive feedback, concurrency is incremented at the end of a sequence with length 1/feedback. This is unlike negative feedback, where concurrency is decremented at the start of a sequence of length 1/feedback. </p>
<p> Specify one of the following forms:</p>
<dl>
<dt><i>number</i></p>
<dd>
<dt><i>number</i> / <i>number</i></p>
<dd>Constant feedback. The value must be in the range 0..1 inclusive. The default setting of &quot;1&quot; is compatible with Postfix versions before 2.5, where a destination&#8217;s delivery concurrency doubles after each successful pseudo-cohort. </p>
<dt><i>number</i> / concurrency</p>
<dd>Variable feedback of &quot;<i>number</i> / (delivery concurrency)&quot;. The <i>number</i> must be in the range 0..1 inclusive. With <i>number</i> equal to &quot;1&quot;, a destination&#8217;s delivery concurrency is incremented by 1 after each successful pseudo-cohort. </p>
</dl>
<p> A pseudo-cohort is the number of deliveries equal to a destination&#8217;s delivery concurrency. </p>
<p> Use <i>transport</i>_destination_concurrency_positive_feedback to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>default_destination_rate_delay (default: 0s)</h2>
<p>The default amount of delay that is inserted between individual message deliveries to the same destination and over the same message delivery transport. Specify a non-zero value to rate-limit those message deliveries to at most one per $default_destination_rate_delay. </p>
<p> The resulting behavior depends on the value of the corresponding per-destination recipient limit.</p>
<dl>
<dt>&bull;</p>
<dd>With a corresponding per-destination recipient limit &gt; 1, the rate delay specifies the time between deliveries to the <i>same domain</i>. Different domains are delivered in parallel, subject to the process limits specified in master.cf.</p>
<dt>&bull;</p>
<dd>With a corresponding per-destination recipient limit equal to 1, the rate delay specifies the time between deliveries to the <i>same recipient</i>. Different recipients are delivered in parallel, subject to the process limits specified in master.cf.
</dl>
<p> To enable the delay, specify a non-zero time value (an integral value plus an optional one-letter suffix that specifies the time unit). </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds). </p>
<p> NOTE: the delay is enforced by the queue manager. The delay timer state does not survive &quot;<code>postfix reload</code>&quot; or &quot;<code>postfix stop</code>&quot;. </p>
<p> Use <i>transport</i>_destination_rate_delay to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport. </p>
<p> NOTE: with a non-zero _destination_rate_delay, specify a <i>transport</i>_destination_concurrency_failed_cohort_limit of 10 or more to prevent Postfix from deferring all mail for the same destination after only one connection or handshake error. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>default_destination_recipient_limit (default: 50)</h2>
<p>The default maximal number of recipients per message delivery. This is the default limit for delivery via the <code><a href="/docs/linux/man/8-lmtp/">lmtp</a></code>(8), <code><a href="/docs/linux/man/8-pipe/">pipe</a></code>(8), <code><a href="/docs/linux/man/8-smtp/">smtp</a></code>(8) and <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) delivery agents. </p>
<p> Setting this parameter to a value of 1 affects email deliveries as follows:</p>
<dl>
<dt>&bull;</p>
<dd>It changes the meaning of the corresponding per-destination concurrency limit, from concurrency of deliveries to the <i>same domain</i> into concurrency of deliveries to the <i>same recipient</i>. Different recipients are delivered in parallel, subject to the process limits specified in master.cf.</p>
<dt>&bull;</p>
<dd>It changes the meaning of the corresponding per-destination rate delay, from the delay between deliveries to the <i>same domain</i> into the delay between deliveries to the <i>same recipient</i>. Again, different recipients are delivered in parallel, subject to the process limits specified in master.cf.</p>
<dt>&bull;</p>
<dd>It changes the meaning of other corresponding per-destination settings in a similar manner, from settings for delivery to the <i>same domain</i> into settings for delivery to the <i>same recipient</i>.
</dl>
<p> Use <i>transport</i>_destination_recipient_limit to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport.</p>
<h2>default_extra_recipient_limit (default: 1000)</h2>
<p>The default value for the extra per-transport limit imposed on the number of in-memory recipients. This extra recipient space is reserved for the cases when the Postfix queue manager&#8217;s scheduler preempts one message with another and suddenly needs some extra recipients slots for the chosen message in order to avoid performance degradation. </p>
<p> Use <i>transport</i>_extra_recipient_limit to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport.</p>
<h2>default_filter_nexthop (default: empty)</h2>
<p>When a content_filter or FILTER request specifies no explicit next-hop destination, use $default_filter_nexthop instead; when that value is empty, use the domain in the recipient address. Specify &quot;default_filter_nexthop = $myhostname&quot; for compatibility with Postfix version 2.6 and earlier, or specify an explicit next-hop destination with each content_filter value or FILTER action. </p>
<p> This feature is available in Postfix 2.7 and later.</p>
<h2>default_minimum_delivery_slots (default: 3)</h2>
<p>How many recipients a message must have in order to invoke the Postfix queue manager&#8217;s scheduling algorithm at all. Messages which would never accumulate at least this many delivery slots (subject to slot cost parameter as well) are never preempted. </p>
<p> Use <i>transport</i>_minimum_delivery_slots to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport.</p>
<h2>default_privs (default: nobody)</h2>
<p>The default rights used by the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent for delivery to external file or command. These rights are used when delivery is requested from an <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) file that is owned by <code>root</code>, or when delivery is done on behalf of <code>root</code>. <code>DO NOT SPECIFY A PRIVILEGED USER OR THE POSTFIX OWNER</code>.</p>
<h2>default_process_limit (default: 100)</h2>
<p>The default maximal number of Postfix child processes that provide a given service. This limit can be overruled for specific services in the master.cf file.</p>
<h2>default_rbl_reply (default: see postconf -d output)</h2>
<p>The default Postfix SMTP server response template for a request that is rejected by an RBL-based restriction. This template can be overruled by specific entries in the optional rbl_reply_maps lookup table. </p>
<p> This feature is available in Postfix 2.0 and later. </p>
<p> The template does not support Postfix configuration parameter $name substitution. Instead, it supports exactly one level of $name substitution for the following attributes:</p>
<dl>
<dt><code>$client</code></p>
<dd>The client hostname and IP address, formatted as name[address]. </p>
<dt><code>$client_address</code></p>
<dd>The client IP address. </p>
<dt><code>$client_name</code></p>
<dd>The client hostname or &quot;unknown&quot;. See reject_unknown_client_hostname for more details. </p>
<dt><code>$reverse_client_name</code></p>
<dd>The client hostname from address-&gt;name lookup, or &quot;unknown&quot;. See reject_unknown_reverse_client_hostname for more details. </p>
<dt><code>$helo_name</code></p>
<dd>The hostname given in HELO or EHLO command or empty string. </p>
<dt><code>$rbl_class</code></p>
<dd>The blacklisted entity type: Client host, Helo command, Sender address, or Recipient address. </p>
<dt><code>$rbl_code</code></p>
<dd>The numerical SMTP response code, as specified with the maps_rbl_reject_code configuration parameter. Note: The numerical SMTP response code is required, and must appear at the start of the reply. With Postfix version 2.3 and later this information may be followed by an RFC 3463 enhanced status code. </p>
<dt><code>$rbl_domain</code></p>
<dd>The RBL domain where $rbl_what is blacklisted. </p>
<dt><code>$rbl_reason</code></p>
<dd>The reason why $rbl_what is blacklisted, or an empty string. </p>
<dt><code>$rbl_what</code></p>
<dd>The entity that is blacklisted (an IP address, a hostname, a domain name, or an email address whose domain was blacklisted). </p>
<dt><code>$recipient</code></p>
<dd>The recipient address or &lt;&gt; in case of the null address. </p>
<dt><code>$recipient_domain</code></p>
<dd>The recipient domain or empty string. </p>
<dt><code>$recipient_name</code></p>
<dd>The recipient address localpart or &lt;&gt; in case of null address. </p>
<dt><code>$sender</code></p>
<dd>The sender address or &lt;&gt; in case of the null address. </p>
<dt><code>$sender_domain</code></p>
<dd>The sender domain or empty string. </p>
<dt><code>$sender_name</code></p>
<dd>The sender address localpart or &lt;&gt; in case of the null address. </p>
<dt><code>${name?text}</code></p>
<dd>Expands to `text&#8217; if $name is not empty. </p>
<dt><code>${name:text}</code></p>
<dd>Expands to `text&#8217; if $name is empty. </p>
</dl>
<p> Instead of $name you can also specify ${name} or $(name). </p>
<p> Note: when an enhanced status code is specified in an RBL reply template, it is subject to modification. The following transformations are needed when the same RBL reply template is used for client, helo, sender, or recipient access restrictions.</p>
<dl>
<dt>&bull;</p>
<dd>When rejecting a sender address, the Postfix SMTP server will transform a recipient DSN status (e.g., 4.1.1-4.1.6) into the corresponding sender DSN status, and vice versa.</p>
<dt>&bull;</p>
<dd>When rejecting non-address information (such as the HELO command argument or the client hostname/address), the Postfix SMTP server will transform a sender or recipient DSN status into a generic non-address DSN status (e.g., 4.0.0).
</dl>
<h2>default_recipient_limit (default: 20000)</h2>
<p>The default per-transport upper limit on the number of in-memory recipients. These limits take priority over the global qmgr_message_recipient_limit after the message has been assigned to the respective transports. See also default_extra_recipient_limit and qmgr_message_recipient_minimum. </p>
<p> Use <i>transport</i>_recipient_limit to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport.</p>
<h2>default_recipient_refill_delay (default: 5s)</h2>
<p>The default per-transport maximum delay between recipients refills. When not all message recipients fit into the memory at once, keep loading more of them at least once every this many seconds. This is used to make sure the recipients are refilled in timely manner even when $default_recipient_refill_limit is too high for too slow deliveries. </p>
<p> Use <i>transport</i>_recipient_refill_delay to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport. </p>
<p> This feature is available in Postfix 2.4 and later.</p>
<h2>default_recipient_refill_limit (default: 100)</h2>
<p>The default per-transport limit on the number of recipients refilled at once. When not all message recipients fit into the memory at once, keep loading more of them in batches of at least this many at a time. See also $default_recipient_refill_delay, which may result in recipient batches lower than this when this limit is too high for too slow deliveries. </p>
<p> Use <i>transport</i>_recipient_refill_limit to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport. </p>
<p> This feature is available in Postfix 2.4 and later.</p>
<h2>default_transport (default: smtp)</h2>
<p>The default mail delivery transport and next-hop destination for destinations that do not match $mydestination, $inet_interfaces, $proxy_interfaces, $virtual_alias_domains, $virtual_mailbox_domains, or $relay_domains. This information can be overruled with the sender_dependent_default_transport_maps parameter and with the <code><a href="/docs/linux/man/5-transport/">transport</a></code>(5) table. </p>
<p> In order of decreasing precedence, the nexthop destination is taken from $sender_dependent_default_transport_maps, $default_transport, $sender_dependent_relayhost_maps, $relayhost, or from the recipient domain. </p>
<p> Specify a string of the form <i>transport:nexthop</i>, where <i>transport</i> is the name of a mail delivery transport defined in master.cf. The <i>:nexthop</i> destination is optional; its syntax is documented in the manual page of the corresponding delivery agent. </p>
<p> Example: </p>
<pre>default_transport = uucp:relayhostname</pre>
<h2>default_transport_rate_delay (default: 0s)</h2>
<p>The default amount of delay that is inserted between individual message deliveries over the same message delivery transport, regardless of destination. Specify a non-zero value to rate-limit those message deliveries to at most one per $default_transport_rate_delay. </p>
<p> Use <i>transport</i>_transport_rate_delay to specify a transport-specific override, where the initial <i>transport</i> is the master.cf name of the message delivery transport. </p>
<p> Example: throttle outbound SMTP mail to at most 3 deliveries per minute. </p>
<pre>/etc/postfix/main.cf:
 smtp_transport_rate_delay = 20s</pre>
<p>To enable the delay, specify a non-zero time value (an integral value plus an optional one-letter suffix that specifies the time unit). </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds). </p>
<p> NOTE: the delay is enforced by the queue manager. </p>
<p> This feature is available in Postfix 3.1 and later.</p>
<h2>default_verp_delimiters (default: +=)</h2>
<p>The two default VERP delimiter characters. These are used when no explicit delimiters are specified with the SMTP XVERP command or with the &quot;<code>sendmail -V</code>&quot; command-line option. Specify characters that are allowed by the verp_delimiter_filter setting. </p>
<p> This feature is available in Postfix 1.1 and later.</p>
<h2>defer_code (default: 450)</h2>
<p>The numerical Postfix SMTP server response code when a remote SMTP client request is rejected by the &quot;defer&quot; restriction. </p>
<p> Do not change this unless you have a complete understanding of RFC 5321.</p>
<h2>defer_service_name (default: defer)</h2>
<p>The name of the defer service. This service is implemented by the <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) daemon and maintains a record of failed delivery attempts and generates non-delivery notifications. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<h2>defer_transports (default: empty)</h2>
<p>The names of message delivery transports that should not deliver mail unless someone issues &quot;<code>sendmail -q</code>&quot; or equivalent. Specify zero or more names of mail delivery transports names that appear in the first field of master.cf. </p>
<p> Example: </p>
<pre>defer_transports = smtp</pre>
<h2>delay_logging_resolution_limit (default: 2)</h2>
<p>The maximal number of digits after the decimal point when logging sub-second delay values. Specify a number in the range 0..6. </p>
<p> Large delay values are rounded off to an integral number seconds; delay values below the delay_logging_resolution_limit are logged as &quot;0&quot;, and delay values under 100s are logged with at most two-digit precision. </p>
<p> The format of the &quot;delays=a/b/c/d&quot; logging is as follows:</p>
<dl>
<dt>&bull;</p>
<dd>a = time from message arrival to last active queue entry</p>
<dt>&bull;</p>
<dd>b = time from last active queue entry to connection setup</p>
<dt>&bull;</p>
<dd>c = time in connection setup, including DNS, EHLO and STARTTLS</p>
<dt>&bull;</p>
<dd>d = time in message transmission
</dl>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>delay_notice_recipient (default: postmaster)</h2>
<p>The recipient of postmaster notifications with the message headers of mail that cannot be delivered within $delay_warning_time time units. </p>
<p> See also: delay_warning_time, notify_classes.</p>
<h2>delay_warning_time (default: 0h)</h2>
<p>The time after which the sender receives a copy of the message headers of mail that is still queued. The confirm_delay_cleared parameter controls sender notification when the delay clears up. </p>
<p> To enable this feature, specify a non-zero time value (an integral value plus an optional one-letter suffix that specifies the time unit). </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is h (hours). </p>
<p> See also: delay_notice_recipient, notify_classes, confirm_delay_cleared.</p>
<h2>deliver_lock_attempts (default: 20)</h2>
<p>The maximal number of attempts to acquire an exclusive lock on a mailbox file or <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) logfile.</p>
<h2>deliver_lock_delay (default: 1s)</h2>
<p>The time between attempts to acquire an exclusive lock on a mailbox file or <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8) logfile. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>destination_concurrency_feedback_debug (default: no)</h2>
<p>Make the queue manager&#8217;s feedback algorithm verbose for performance analysis purposes. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>detect_8bit_encoding_header (default: yes)</h2>
<p>Automatically detect 8BITMIME body content by looking at Content-Transfer-Encoding: message headers; historically, this behavior was hard-coded to be &quot;always on&quot;. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>disable_dns_lookups (default: no)</h2>
<p>Disable DNS lookups in the Postfix SMTP and LMTP clients. When disabled, hosts are looked up with the getaddrinfo() system library routine which normally also looks in /etc/hosts. As of Postfix 2.11, this parameter is deprecated; use smtp_dns_support_level instead. </p>
<p> DNS lookups are enabled by default.</p>
<h2>disable_mime_input_processing (default: no)</h2>
<p>Turn off MIME processing while receiving mail. This means that no special treatment is given to Content-Type: message headers, and that all text after the initial message headers is considered to be part of the message body. </p>
<p> This feature is available in Postfix 2.0 and later. </p>
<p> Mime input processing is enabled by default, and is needed in order to recognize MIME headers in message content.</p>
<h2>disable_mime_output_conversion (default: no)</h2>
<p>Disable the conversion of 8BITMIME format to 7BIT format. Mime output conversion is needed when the destination does not advertise 8BITMIME support. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<h2>disable_verp_bounces (default: no)</h2>
<p>Disable sending one bounce report per recipient. </p>
<p> The default, one per recipient, is what ezmlm needs. </p>
<p> This feature is available in Postfix 1.1 and later.</p>
<h2>disable_vrfy_command (default: no)</h2>
<p>Disable the SMTP VRFY command. This stops some techniques used to harvest email addresses. </p>
<p> Example: </p>
<pre>disable_vrfy_command = no</pre>
<h2>dns_ncache_ttl_fix_enable (default: no)</h2>
<p>Enable a workaround for future libc incompatibility. The Postfix implementation of RFC 2308 negative reply caching relies on the promise that res_query() and res_search() invoke res_send(), which returns the server response in an application buffer even if the requested record does not exist. If this promise is broken, specify &quot;yes&quot; to enable a workaround for DNS reputation lookups. </p>
<p> This feature is available in Postfix 3.1 and later.</p>
<h2>dnsblog_reply_delay (default: 0s)</h2>
<p>A debugging aid to artificially delay DNS responses. </p>
<p> This feature is available in Postfix 2.8.</p>
<h2>dnsblog_service_name (default: dnsblog)</h2>
<p>The name of the <code><a href="/docs/linux/man/8-dnsblog/">dnsblog</a></code>(8) service entry in master.cf. This service performs DNS white/blacklist lookups. </p>
<p> This feature is available in Postfix 2.8 and later.</p>
<h2>dont_remove (default: 0)</h2>
<p>Don&#8217;t remove queue files and save them to the &quot;saved&quot; mail queue. This is a debugging aid. To inspect the envelope information and content of a Postfix queue file, use the <code><a href="/docs/linux/man/1-postcat/">postcat</a></code>(1) command.</p>
<h2>double_bounce_sender (default: double-bounce)</h2>
<p>The sender address of postmaster notifications that are generated by the mail system. All mail to this address is silently discarded, in order to terminate mail bounce loops.</p>
<h2>duplicate_filter_limit (default: 1000)</h2>
<p>The maximal number of addresses remembered by the address duplicate filter for <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) or <code><a href="/docs/linux/man/5-virtual/">virtual</a></code>(5) alias expansion, or for <code><a href="/docs/linux/man/8-showq/">showq</a></code>(8) queue displays.</p>
<h2>empty_address_default_transport_maps_lookup_key (default: &lt;&gt;)</h2>
<p>The sender_dependent_default_transport_maps search string that will be used instead of the null sender address. </p>
<p> This feature is available in Postfix 2.7 and later.</p>
<h2>empty_address_recipient (default: MAILER-DAEMON)</h2>
<p>The recipient of mail addressed to the null address. Postfix does not accept such addresses in SMTP commands, but they may still be created locally as the result of configuration or software error.</p>
<h2>empty_address_relayhost_maps_lookup_key (default: &lt;&gt;)</h2>
<p>The sender_dependent_relayhost_maps search string that will be used instead of the null sender address. </p>
<p> This feature is available in Postfix 2.5 and later. With earlier versions, sender_dependent_relayhost_maps lookups were skipped for the null sender address.</p>
<h2>enable_errors_to (default: no)</h2>
<p>Report mail delivery errors to the address specified with the non-standard Errors-To: message header, instead of the envelope sender address (this feature is removed with Postfix version 2.2, is turned off by default with Postfix version 2.1, and is always turned on with older Postfix versions).</p>
<h2>enable_idna2003_compatibility (default: no)</h2>
<p>Enable &#8216;transitional&#8217; compatibility between IDNA2003 and IDNA2008, when converting UTF-8 domain names to/from the ASCII form that is used for DNS lookups. Specify &quot;yes&quot; for compatibility with Postfix &lt;= 3.1 (not recommended). This affects the conversion of domain names that contain for example the German sz and the Greek zeta. See <a rel="nofollow" href="http://unicode.org/cldr/utility/idna.jsp">http://unicode.org/cldr/utility/idna.jsp</a> for more examples. </p>
<p> This feature is available in Postfix 3.2 and later.</p>
<h2>enable_long_queue_ids (default: no)</h2>
<p>Enable long, non-repeating, queue IDs (queue file names). The benefit of non-repeating names is simpler logfile analysis and easier queue migration (there is no need to run &quot;postsuper&quot; to change queue file names that don&#8217;t match their message file inode number). </p>
<p> Note: see below for how to convert long queue file names to Postfix &lt;= 2.8. </p>
<p> Changing the parameter value to &quot;yes&quot; has the following effects:</p>
<dl>
<dt>&bull;</p>
<dd>Existing queue file names are not affected.</p>
<dt>&bull;</p>
<dd>New queue files are created with names such as 3Pt2mN2VXxznjll. These are encoded in a 52-character alphabet that contains digits (0-9), upper-case letters (B-Z) and lower-case letters (b-z). For safety reasons the vowels (AEIOUaeiou) are excluded from the alphabet. The name format is: 6 or more characters for the time in seconds, 4 characters for the time in microseconds, the &#8216;z&#8217;; the remainder is the file inode number encoded in the first 51 characters of the 52-character alphabet.</p>
<dt>&bull;</p>
<dd>New messages have a Message-ID header with <i>queueID</i>@<i>myhostname</i>.</p>
<dt>&bull;</p>
<dd>The mailq (postqueue -p) output has a wider Queue ID column. The number of whitespace-separated fields is not changed.</p>
<dt>&bull;</p>
<dd>The hash_queue_depth algorithm uses the first characters of the queue file creation time in microseconds, after conversion into hexadecimal representation. This produces the same queue hashing behavior as if the queue file name was created with &quot;enable_long_queue_ids = no&quot;.
</dl>
<p> Changing the parameter value to &quot;no&quot; has the following effects:</p>
<dl>
<dt>&bull;</p>
<dd>Existing long queue file names are renamed to the short form (while running &quot;postfix reload&quot; or &quot;postsuper&quot;).</p>
<dt>&bull;</p>
<dd>New queue files are created with names such as C3CD21F3E90 from a hexadecimal alphabet that contains digits (0-9) and upper-case letters (A-F). The name format is: 5 characters for the time in microseconds; the remainder is the file inode number.</p>
<dt>&bull;</p>
<dd>New messages have a Message-ID header with <i>YYYYMMDDHHMMSS.queueid</i>@<i>myhostname</i>, where <i>YYYYMMDDHHMMSS</i> are the year, month, day, hour, minute and second.</p>
<dt>&bull;</p>
<dd>The mailq (postqueue -p) output has the same format as with Postfix &lt;= 2.8.</p>
<dt>&bull;</p>
<dd>The hash_queue_depth algorithm uses the first characters of the queue file name, with the hexadecimal representation of the file creation time in microseconds.
</dl>
<p> Before migration to Postfix &lt;= 2.8, the following commands are required to convert long queue file names into short names: </p>
<pre># postfix stop
# postconf enable_long_queue_ids=no
# postsuper</pre>
<p>Repeat the postsuper command until it reports no more queue file name changes. </p>
<p> This feature is available in Postfix 2.9 and later.</p>
<h2>enable_original_recipient (default: yes)</h2>
<p>Enable support for the original recipient address after an address is rewritten to a different address (for example with aliasing or with canonical mapping). </p>
<p> The original recipient address is used as follows:</p>
<dl>
<dt>Final delivery</p>
<dd>With &quot;enable_original_recipient = yes&quot;, the original recipient address is stored in the <code>X-Original-To</code> message header. This header may be used to distinguish between different recipients that share the same mailbox. </p>
<dt>Recipient deduplication</p>
<dd>With &quot;enable_original_recipient = yes&quot;, the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon performs duplicate recipient elimination based on the content of (original recipient, maybe-rewritten recipient) pairs. Otherwise, the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon performs duplicate recipient elimination based only on the maybe-rewritten recipient address. </p>
</dl>
<p> Note: with Postfix &lt;= 3.2 the &quot;setting enable_original_recipient = <code>no</code>&quot; breaks address verification for addresses that are aliased or otherwise rewritten (Postfix is unable to store the address verification result under the original probe destination address; instead, it can store the result only under the rewritten address). </p>
<p> This feature is available in Postfix 2.1 and later. Postfix version 2.0 behaves as if this parameter is always set to <code>yes</code>. Postfix versions before 2.0 have no support for the original recipient address.</p>
<h2>error_notice_recipient (default: postmaster)</h2>
<p>The recipient of postmaster notifications about mail delivery problems that are caused by policy, resource, software or protocol errors. These notifications are enabled with the notify_classes parameter.</p>
<h2>error_service_name (default: error)</h2>
<p>The name of the <code><a href="/docs/linux/man/8-error/">error</a></code>(8) pseudo delivery agent. This service always returns mail as undeliverable. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<h2>execution_directory_expansion_filter (default: see postconf -d output)</h2>
<p>Restrict the characters that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent allows in $name expansions of $command_execution_directory. Characters outside the allowed set are replaced by underscores. </p>
<p> This feature is available in Postfix 2.2 and later.</p>
<h2>expand_owner_alias (default: no)</h2>
<p>When delivering to an alias &quot;<i>aliasname</i>&quot; that has an &quot;owner-<i>aliasname</i>&quot; companion alias, set the envelope sender address to the expansion of the &quot;owner-<i>aliasname</i>&quot; alias. Normally, Postfix sets the envelope sender address to the name of the &quot;owner-<i>aliasname</i>&quot; alias.</p>
<h2>export_environment (default: see postconf -d output)</h2>
<p>The list of environment variables that a Postfix process will export to non-Postfix processes. The TZ variable is needed for sane time keeping on System-V-ish systems. </p>
<p> Specify a list of names and/or name=value pairs, separated by whitespace or comma. Specify &quot;{ name=value }&quot; to protect whitespace or comma in parameter values (whitespace after the opening &quot;{&quot; and before the closing &quot;}&quot; is ignored). The form name=value is supported with Postfix version 2.1 and later; the use of {} is supported with Postfix 3.0 and later. </p>
<p> Example: </p>
<pre>export_environment = TZ PATH=/bin:/usr/bin</pre>
<h2>extract_recipient_limit (default: 10240)</h2>
<p>The maximal number of recipient addresses that Postfix will extract from message headers when mail is submitted with &quot;<code>sendmail -t</code>&quot;. </p>
<p> This feature was removed in Postfix version 2.1.</p>
<h2>fallback_relay (default: empty)</h2>
<p>Optional list of relay hosts for SMTP destinations that can&#8217;t be found or that are unreachable. With Postfix 2.3 this parameter is renamed to smtp_fallback_relay. </p>
<p> By default, mail is returned to the sender when a destination is not found, and delivery is deferred when a destination is unreachable. </p>
<p> The fallback relays must be SMTP destinations. Specify a domain, host, host:port, [host]:port, [address] or [address]:port; the form [host] turns off MX lookups. If you specify multiple SMTP destinations, Postfix will try them in the specified order. </p>
<p> Note: before Postfix 2.2, do not use the fallback_relay feature when relaying mail for a backup or primary MX domain. Mail would loop between the Postfix MX host and the fallback_relay host when the final destination is unavailable.</p>
<dl>
<dt>&bull;</p>
<dd>In main.cf specify &quot;relay_transport = relay&quot;,</p>
<dt>&bull;</p>
<dd>In master.cf specify &quot;-o fallback_relay =&quot; (i.e., empty) at the end of the relay entry.</p>
<dt>&bull;</p>
<dd>In transport maps, specify &quot;relay:<i>nexthop&#8230;</i>&quot; as the right-hand side for backup or primary MX domain entries.
</dl>
<p> Postfix version 2.2 and later will not use the fallback_relay feature for destinations that it is MX host for.</p>
<h2>fallback_transport (default: empty)</h2>
<p>Optional message delivery transport that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent should use for names that are not found in the <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) or UNIX password database. </p>
<p> The precedence of <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery features from high to low is: aliases, .forward files, mailbox_transport_maps, mailbox_transport, mailbox_command_maps, mailbox_command, home_mailbox, mail_spool_directory, fallback_transport_maps, fallback_transport and luser_relay.</p>
<h2>fallback_transport_maps (default: empty)</h2>
<p>Optional lookup tables with per-recipient message delivery transports for recipients that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent could not find in the <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) or UNIX password database. </p>
<p> The precedence of <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery features from high to low is: aliases, .forward files, mailbox_transport_maps, mailbox_transport, mailbox_command_maps, mailbox_command, home_mailbox, mail_spool_directory, fallback_transport_maps, fallback_transport and luser_relay. </p>
<p> For safety reasons, this feature does not allow $number substitutions in regular expression maps. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>fast_flush_domains (default: $relay_domains)</h2>
<p>Optional list of destinations that are eligible for per-destination logfiles with mail that is queued to those destinations. </p>
<p> By default, Postfix maintains &quot;fast flush&quot; logfiles only for destinations that the Postfix SMTP server is willing to relay to (i.e. the default is: &quot;fast_flush_domains = $relay_domains&quot;; see the relay_domains parameter in the <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) manual). </p>
<p> Specify a list of hosts or domains, &quot;/file/name&quot; patterns or &quot;type:table&quot; lookup tables, separated by commas and/or whitespace. Continue long lines by starting the next line with whitespace. A &quot;/file/name&quot; pattern is replaced by its contents; a &quot;type:table&quot; lookup table is matched when the domain or its parent domain appears as lookup key. </p>
<p> Pattern matching of domain names is controlled by the presence or absence of &quot;fast_flush_domains&quot; in the parent_domain_matches_subdomains parameter value. </p>
<p> Specify &quot;fast_flush_domains =&quot; (i.e., empty) to disable the feature altogether.</p>
<h2>fast_flush_purge_time (default: 7d)</h2>
<p>The time after which an empty per-destination &quot;fast flush&quot; logfile is deleted. </p>
<p> You can specify the time as a number, or as a number followed by a letter that indicates the time unit: s=seconds, m=minutes, h=hours, d=days, w=weeks. The default time unit is days.</p>
<h2>fast_flush_refresh_time (default: 12h)</h2>
<p>The time after which a non-empty but unread per-destination &quot;fast flush&quot; logfile needs to be refreshed. The contents of a logfile are refreshed by requesting delivery of all messages listed in the logfile. </p>
<p> You can specify the time as a number, or as a number followed by a letter that indicates the time unit: s=seconds, m=minutes, h=hours, d=days, w=weeks. The default time unit is hours.</p>
<h2>fault_injection_code (default: 0)</h2>
<p>Force specific internal tests to fail, to test the handling of errors that are difficult to reproduce otherwise.</p>
<h2>flush_service_name (default: flush)</h2>
<p>The name of the <code><a href="/docs/linux/man/8-flush/">flush</a></code>(8) service. This service maintains per-destination logfiles with the queue file names of mail that is queued for those destinations. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<h2>fork_attempts (default: 5)</h2>
<p>The maximal number of attempts to fork() a child process.</p>
<h2>fork_delay (default: 1s)</h2>
<p>The delay between attempts to fork() a child process. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>forward_expansion_filter (default: see postconf -d output)</h2>
<p>Restrict the characters that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent allows in $name expansions of $forward_path. Characters outside the allowed set are replaced by underscores.</p>
<h2>forward_path (default: see postconf -d output)</h2>
<p>The <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent search list for finding a .forward file with user-specified delivery methods. The first file that is found is used. </p>
<p> The forward_path value is not subject to Postfix configuration parameter $name expansion. Instead, the following $name expansions are done on forward_path before the search actually happens. The result of $name expansion is filtered with the character set that is specified with the forward_expansion_filter parameter.</p>
<dl>
<dt><code>$user</code></p>
<dd>The recipient&#8217;s username. </p>
<dt><code>$shell</code></p>
<dd>The recipient&#8217;s login shell pathname. </p>
<dt><code>$home</code></p>
<dd>The recipient&#8217;s home directory. </p>
<dt><code>$recipient</code></p>
<dd>The full recipient address. </p>
<dt><code>$extension</code></p>
<dd>The optional recipient address extension. </p>
<dt><code>$domain</code></p>
<dd>The recipient domain. </p>
<dt><code>$local</code></p>
<dd>The entire recipient localpart. </p>
<dt><code>$recipient_delimiter</code></p>
<dd>The address extension delimiter that was found in the recipient address (Postfix 2.11 and later), or the system-wide recipient address extension delimiter (Postfix 2.10 and earlier). </p>
<dt><code>${name?value}</code></p>
<dd>Expands to <i>value</i> when <i>$name</i> is non-empty. </p>
<dt><code>${name:value}</code></p>
<dd>Expands to <i>value</i> when <i>$name</i> is empty. </p>
</dl>
<p> Instead of $name you can also specify ${name} or $(name). </p>
<p> Examples: </p>
<pre>forward_path = /var/forward/$user
forward_path =
 /var/forward/$user/.forward$recipient_delimiter$extension,
 /var/forward/$user/.forward</pre>
<h2>frozen_delivered_to (default: yes)</h2>
<p>Update the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent&#8217;s idea of the Delivered-To: address (see prepend_delivered_header) only once, at the start of a delivery attempt; do not update the Delivered-To: address while expanding aliases or .forward files. </p>
<p> This feature is available in Postfix 2.3 and later. With older Postfix releases, the behavior is as if this parameter is set to &quot;no&quot;. The old setting can be expensive with deeply nested aliases or .forward files. When an alias or .forward file changes the Delivered-To: address, it ties up one queue file and one cleanup process instance while mail is being forwarded.</p>
<h2>hash_queue_depth (default: 1)</h2>
<p>The number of subdirectory levels for queue directories listed with the hash_queue_names parameter. Queue hashing is implemented by creating one or more levels of directories with one-character names. Originally, these directory names were equal to the first characters of the queue file name, with the hexadecimal representation of the file creation time in microseconds. </p>
<p> With long queue file names, queue hashing produces the same results as with short names. The file creation time in microseconds is converted into hexadecimal form before the result is used for queue hashing. The base 16 encoding gives finer control over the number of subdirectories than is possible with the base 52 encoding of long queue file names. </p>
<p> After changing the hash_queue_names or hash_queue_depth parameter, execute the command &quot;<code>postfix reload</code>&quot;.</p>
<h2>hash_queue_names (default: deferred, defer)</h2>
<p>The names of queue directories that are split across multiple subdirectory levels. </p>
<p> Before Postfix version 2.2, the default list of hashed queues was significantly larger. Claims about improvements in file system technology suggest that hashing of the incoming and active queues is no longer needed. Fewer hashed directories speed up the time needed to restart Postfix. </p>
<p> After changing the hash_queue_names or hash_queue_depth parameter, execute the command &quot;<code>postfix reload</code>&quot;.</p>
<h2>header_address_token_limit (default: 10240)</h2>
<p>The maximal number of address tokens are allowed in an address message header. Information that exceeds the limit is discarded. The limit is enforced by the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) server.</p>
<h2>header_checks (default: empty)</h2>
<p>Optional lookup tables for content inspection of primary non-MIME message headers, as specified in the <code><a href="/docs/linux/man/5-header_checks/">header_checks</a></code>(5) manual page.</p>
<h2>header_from_format (default: standard)</h2>
<p>The format of the Postfix-generated <code>From:</code> header. This setting affects the appearance of &#8216;full name&#8217; information when a local program such as /bin/mail submits a message without From: header through the Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command. </p>
<p> Specify one of the following:</p>
<dl>
<dt><code>standard</code> (default)</p>
<dd>Produce a header formatted as &quot;<code>From:</code> <i>name</i><code> &lt;</code><i>address</i><code>&gt;</code>&quot;. This is the default as of Postfix 3.3. </p>
<dt><code>obsolete</code></p>
<dd>Produce a header formatted as &quot;<code>From:</code> <i>address</i> <code>(</code><i>name</i><code>)</code>&quot;. This is the behavior prior to Postfix 3.3. </p>
</dl>
<p> Notes:</p>
<dl>
<dt>&bull;</p>
<dd>Postfix generates the format &quot;<code>From:</code> <i>address</i>&quot; when <i>name</i> information is unavailable or the envelope sender address is empty. This is the same behavior as prior to Postfix 3.3.</p>
<dt>&bull;</p>
<dd>In the <code>standard</code> form, the <i>name</i> will be quoted if it contains <code>specials</code> as defined in RFC 5322, or the &quot;!%&quot; address operators.</p>
<dt>&bull;</p>
<dd>The Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command gets <i>name</i> information from the <code>-F</code> command-line option, from the <code>NAME</code> environment variable, or from the UNIX password file.
</dl>
<p> This feature is available in Postfix 3.3 and later.</p>
<h2>header_size_limit (default: 102400)</h2>
<p>The maximal amount of memory in bytes for storing a message header. If a header is larger, the excess is discarded. The limit is enforced by the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) server.</p>
<h2>helpful_warnings (default: yes)</h2>
<p>Log warnings about problematic configuration settings, and provide helpful suggestions. </p>
<p> This feature is available in Postfix 2.0 and later.</p>
<h2>home_mailbox (default: empty)</h2>
<p>Optional pathname of a mailbox file relative to a <code><a href="/docs/linux/man/8-local/">local</a></code>(8) user&#8217;s home directory. </p>
<p> Specify a pathname ending in &quot;/&quot; for qmail-style delivery. </p>
<p> The precedence of <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery features from high to low is: aliases, .forward files, mailbox_transport_maps, mailbox_transport, mailbox_command_maps, mailbox_command, home_mailbox, mail_spool_directory, fallback_transport_maps, fallback_transport and luser_relay. </p>
<p> Examples: </p>
<pre>home_mailbox = Mailbox
home_mailbox = Maildir/</pre>
<h2>hopcount_limit (default: 50)</h2>
<p>The maximal number of Received: message headers that is allowed in the primary message headers. A message that exceeds the limit is bounced, in order to stop a mailer loop.</p>
<h2>html_directory (default: see postconf -d output)</h2>
<p>The location of Postfix HTML files that describe how to build, configure or operate a specific Postfix subsystem or feature.</p>
<h2>ignore_mx_lookup_error (default: no)</h2>
<p>Ignore DNS MX lookups that produce no response. By default, the Postfix SMTP client defers delivery and tries again after some delay. This behavior is required by the SMTP standard. </p>
<p> Specify &quot;ignore_mx_lookup_error = yes&quot; to force a DNS A record lookup instead. This violates the SMTP standard and can result in mis-delivery of mail.</p>
<h2>import_environment (default: see postconf -d output)</h2>
<p>The list of environment parameters that a privileged Postfix process will import from a non-Postfix parent process, or name=value environment overrides. Unprivileged utilities will enforce the name=value overrides, but otherwise will not change their process environment. Examples of relevant parameters:</p>
<dl>
<dt><code>TZ</code></p>
<dd>May be needed for sane time keeping on most System-V-ish systems. </p>
<dt><code>DISPLAY</code></p>
<dd>Needed for debugging Postfix daemons with an X-windows debugger. </p>
<dt><code>XAUTHORITY</code></p>
<dd>Needed for debugging Postfix daemons with an X-windows debugger. </p>
<dt><code>MAIL_CONFIG</code></p>
<dd>Needed to make &quot;<code>postfix -c</code>&quot; work. </p>
</dl>
<p> Specify a list of names and/or name=value pairs, separated by whitespace or comma. Specify &quot;{ name=value }&quot; to protect whitespace or comma in parameter values (whitespace after the opening &quot;{&quot; and before the closing &quot;}&quot; is ignored). The form name=value is supported with Postfix version 2.1 and later; the use of {} is supported with Postfix 3.0 and later.</p>
<h2>in_flow_delay (default: 1s)</h2>
<p>Time to pause before accepting a new message, when the message arrival rate exceeds the message delivery rate. This feature is turned on by default (it&#8217;s disabled on SCO UNIX due to an SCO bug). </p>
<p> With the default 100 Postfix SMTP server process limit, &quot;in_flow_delay = 1s&quot; limits the mail inflow to 100 messages per second above the number of messages delivered per second. </p>
<p> Specify 0 to disable the feature. Valid delays are 0..10.</p>
<h2>inet_interfaces (default: all)</h2>
<p>The network interface addresses that this mail system receives mail on. Specify &quot;all&quot; to receive mail on all network interfaces (default), and &quot;loopback-only&quot; to receive mail on loopback network interfaces only (Postfix version 2.2 and later). The parameter also controls delivery of mail to user@[ip.address]. </p>
<p> Note 1: you need to stop and start Postfix when this parameter changes. </p>
<p> Note 2: address information may be enclosed inside [], but this form is not required here. </p>
<p> When inet_interfaces specifies just one IPv4 and/or IPv6 address that is not a loopback address, the Postfix SMTP client will use this address as the IP source address for outbound mail. Support for IPv6 is available in Postfix version 2.2 and later. </p>
<p> On a multi-homed firewall with separate Postfix instances listening on the &quot;inside&quot; and &quot;outside&quot; interfaces, this can prevent each instance from being able to reach remote SMTP servers on the &quot;other side&quot; of the firewall. Setting smtp_bind_address to 0.0.0.0 avoids the potential problem for IPv4, and setting smtp_bind_address6 to :: solves the problem for IPv6. </p>
<p> A better solution for multi-homed firewalls is to leave inet_interfaces at the default value and instead use explicit IP addresses in the master.cf SMTP server definitions. This preserves the Postfix SMTP client&#8217;s loop detection, by ensuring that each side of the firewall knows that the other IP address is still the same host. Setting $inet_interfaces to a single IPv4 and/or IPV6 address is primarily useful with virtual hosting of domains on secondary IP addresses, when each IP address serves a different domain (and has a different $myhostname setting). </p>
<p> See also the proxy_interfaces parameter, for network addresses that are forwarded to Postfix by way of a proxy or address translator. </p>
<p> Examples: </p>
<pre>inet_interfaces = all (DEFAULT)
inet_interfaces = loopback-only (Postfix version 2.2 and later)
inet_interfaces = 127.0.0.1
inet_interfaces = 127.0.0.1, [::1] (Postfix version 2.2 and later)
inet_interfaces = 192.168.1.2, 127.0.0.1</pre>
<h2>inet_protocols (default: all)</h2>
<p>The Internet protocols Postfix will attempt to use when making or accepting connections. Specify one or more of &quot;ipv4&quot; or &quot;ipv6&quot;, separated by whitespace or commas. The form &quot;all&quot; is equivalent to &quot;ipv4, ipv6&quot; or &quot;ipv4&quot;, depending on whether the operating system implements IPv6. </p>
<p> With Postfix 2.8 and earlier the default is &quot;ipv4&quot;. For backwards compatibility with these releases, the Postfix 2.9 and later upgrade procedure appends an explicit &quot;inet_protocols = ipv4&quot; setting to main.cf when no explicit setting is present. This compatibility workaround will be phased out as IPv6 deployment becomes more common. </p>
<p> This feature is available in Postfix 2.2 and later. </p>
<p> Note: you MUST stop and start Postfix after changing this parameter. </p>
<p> On systems that pre-date IPV6_V6ONLY support (RFC 3493), an IPv6 server will also accept IPv4 connections, even when IPv4 is turned off with the inet_protocols parameter. On systems with IPV6_V6ONLY support, Postfix will use separate server sockets for IPv6 and IPv4, and each will accept only connections for the corresponding protocol. </p>
<p> When IPv4 support is enabled via the inet_protocols parameter, Postfix will look up DNS type A records, and will convert IPv4-in-IPv6 client IP addresses (::ffff:1.2.3.4) to their original IPv4 form (1.2.3.4). The latter is needed on hosts that pre-date IPV6_V6ONLY support (RFC 3493). </p>
<p> When IPv6 support is enabled via the inet_protocols parameter, Postfix will do DNS type AAAA record lookups. </p>
<p> When both IPv4 and IPv6 support are enabled, the Postfix SMTP client will choose the protocol as specified with the smtp_address_preference parameter. Postfix versions before 2.8 attempt to connect via IPv6 before attempting to use IPv4. </p>
<p> Examples: </p>
<pre>inet_protocols = ipv4
inet_protocols = all (DEFAULT)
inet_protocols = ipv6
inet_protocols = ipv4, ipv6</pre>
<h2>initial_destination_concurrency (default: 5)</h2>
<p>The initial per-destination concurrency level for parallel delivery to the same destination. With per-destination recipient limit &gt; 1, a destination is a domain, otherwise it is a recipient. </p>
<p> Use <i>transport</i>_initial_destination_concurrency to specify a transport-specific override, where <i>transport</i> is the master.cf name of the message delivery transport (Postfix 2.5 and later). </p>
<p> Warning: with concurrency of 1, one bad message can be enough to block all mail to a site.</p>
<h2>internal_mail_filter_classes (default: empty)</h2>
<p>What categories of Postfix-generated mail are subject to before-queue content inspection by non_smtpd_milters, header_checks and body_checks. Specify zero or more of the following, separated by whitespace or comma.</p>
<dl>
<dt><code>bounce</code></p>
<dd>Inspect the content of delivery status notifications. </p>
<dt><code>notify</code></p>
<dd>Inspect the content of postmaster notifications by the <code><a href="/docs/linux/man/8-smtp/">smtp</a></code>(8) and <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) processes. </p>
</dl>
<p> NOTE: It&#8217;s generally not safe to enable content inspection of Postfix-generated email messages. The user is warned. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>invalid_hostname_reject_code (default: 501)</h2>
<p>The numerical Postfix SMTP server response code when the client HELO or EHLO command parameter is rejected by the reject_invalid_helo_hostname restriction. </p>
<p> Do not change this unless you have a complete understanding of RFC 5321.</p>
<h2>ipc_idle (default: version dependent)</h2>
<p>The time after which a client closes an idle internal communication channel. The purpose is to allow Postfix daemon processes to terminate voluntarily after they become idle. This is used, for example, by the Postfix address resolving and rewriting clients. </p>
<p> With Postfix 2.4 the default value was reduced from 100s to 5s. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>ipc_timeout (default: 3600s)</h2>
<p>The time limit for sending or receiving information over an internal communication channel. The purpose is to break out of deadlock situations. If the time limit is exceeded the software aborts with a fatal error. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>ipc_ttl (default: 1000s)</h2>
<p>The time after which a client closes an active internal communication channel. The purpose is to allow Postfix daemon processes to terminate voluntarily after reaching their client limit. This is used, for example, by the Postfix address resolving and rewriting clients. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds). </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>line_length_limit (default: 2048)</h2>
<p>Upon input, long lines are chopped up into pieces of at most this length; upon delivery, long lines are reconstructed.</p>
<h2>lmdb_map_size (default: 16777216)</h2>
<p>The initial OpenLDAP LMDB database size limit in bytes. Each time a database becomes full, its size limit is doubled. </p>
<p> This feature is available in Postfix 2.11 and later.</p>
<h2>lmtp_address_preference (default: ipv6)</h2>
<p>The LMTP-specific version of the smtp_address_preference configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.8 and later.</p>
<h2>lmtp_address_verify_target (default: rcpt)</h2>
<p>The LMTP-specific version of the smtp_address_verify_target configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 3.0 and later.</p>
<h2>lmtp_assume_final (default: no)</h2>
<p>When a remote LMTP server announces no DSN support, assume that the server performs final delivery, and send &quot;delivered&quot; delivery status notifications instead of &quot;relayed&quot;. The default setting is backwards compatible to avoid the infinitesimal possibility of breaking existing LMTP-based content filters.</p>
<h2>lmtp_balance_inet_protocols (default: yes)</h2>
<p>The LMTP-specific version of the smtp_balance_inet_protocols configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 3.3 and later.</p>
<h2>lmtp_bind_address (default: empty)</h2>
<p>The LMTP-specific version of the smtp_bind_address configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_bind_address6 (default: empty)</h2>
<p>The LMTP-specific version of the smtp_bind_address6 configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_body_checks (default: empty)</h2>
<p>The LMTP-specific version of the smtp_body_checks configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>lmtp_cache_connection (default: yes)</h2>
<p>Keep Postfix LMTP client connections open for up to $max_idle seconds. When the LMTP client receives a request for the same connection the connection is reused. </p>
<p> This parameter is available in Postfix version 2.2 and earlier. With Postfix version 2.3 and later, see lmtp_connection_cache_on_demand, lmtp_connection_cache_destinations, or lmtp_connection_reuse_time_limit. </p>
<p> The effectiveness of cached connections will be determined by the number of remote LMTP servers in use, and the concurrency limit specified for the Postfix LMTP client. Cached connections are closed under any of the following conditions:</p>
<dl>
<dt>&bull;</p>
<dd>The Postfix LMTP client idle time limit is reached. This limit is specified with the Postfix max_idle configuration parameter.</p>
<dt>&bull;</p>
<dd>A delivery request specifies a different destination than the one currently cached.</p>
<dt>&bull;</p>
<dd>The per-process limit on the number of delivery requests is reached. This limit is specified with the Postfix max_use configuration parameter.</p>
<dt>&bull;</p>
<dd>Upon the onset of another delivery request, the remote LMTP server associated with the current session does not respond to the RSET command.
</dl>
<p> Most of these limitations have been with the Postfix a connection cache that is shared among multiple LMTP client programs.</p>
<h2>lmtp_cname_overrides_servername (default: yes)</h2>
<p>The LMTP-specific version of the smtp_cname_overrides_servername configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_connect_timeout (default: 0s)</h2>
<p>The Postfix LMTP client time limit for completing a TCP connection, or zero (use the operating system built-in time limit). When no connection can be made within the deadline, the LMTP client tries the next address on the mail exchanger list. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds). </p>
<p> Example: </p>
<pre>lmtp_connect_timeout = 30s</pre>
<h2>lmtp_connection_cache_destinations (default: empty)</h2>
<p>The LMTP-specific version of the smtp_connection_cache_destinations configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_connection_cache_on_demand (default: yes)</h2>
<p>The LMTP-specific version of the smtp_connection_cache_on_demand configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_connection_cache_time_limit (default: 2s)</h2>
<p>The LMTP-specific version of the smtp_connection_cache_time_limit configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_connection_reuse_count_limit (default: 0)</h2>
<p>The LMTP-specific version of the smtp_connection_reuse_count_limit configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.11 and later.</p>
<h2>lmtp_connection_reuse_time_limit (default: 300s)</h2>
<p>The LMTP-specific version of the smtp_connection_reuse_time_limit configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_data_done_timeout (default: 600s)</h2>
<p>The Postfix LMTP client time limit for sending the LMTP &quot;.&quot;, and for receiving the remote LMTP server response. When no response is received within the deadline, a warning is logged that the mail may be delivered multiple times. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>lmtp_data_init_timeout (default: 120s)</h2>
<p>The Postfix LMTP client time limit for sending the LMTP DATA command, and for receiving the remote LMTP server response. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>lmtp_data_xfer_timeout (default: 180s)</h2>
<p>The Postfix LMTP client time limit for sending the LMTP message content. When the connection stalls for more than $lmtp_data_xfer_timeout the LMTP client terminates the transfer. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>lmtp_defer_if_no_mx_address_found (default: no)</h2>
<p>The LMTP-specific version of the smtp_defer_if_no_mx_address_found configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_delivery_status_filter (default: empty)</h2>
<p>The LMTP-specific version of the smtp_delivery_status_filter configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 3.0 and later.</p>
<h2>lmtp_destination_concurrency_limit (default: $default_destination_concurrency_limit)</h2>
<p>The maximal number of parallel deliveries to the same destination via the lmtp message delivery transport. This limit is enforced by the queue manager. The message delivery transport name is the first field in the entry in the master.cf file.</p>
<h2>lmtp_destination_recipient_limit (default: $default_destination_recipient_limit)</h2>
<p>The maximal number of recipients per message for the lmtp message delivery transport. This limit is enforced by the queue manager. The message delivery transport name is the first field in the entry in the master.cf file. </p>
<p> Setting this parameter to a value of 1 changes the meaning of lmtp_destination_concurrency_limit from concurrency per domain into concurrency per recipient.</p>
<h2>lmtp_discard_lhlo_keyword_address_maps (default: empty)</h2>
<p>Lookup tables, indexed by the remote LMTP server address, with case insensitive lists of LHLO keywords (pipelining, starttls, auth, etc.) that the Postfix LMTP client will ignore in the LHLO response from a remote LMTP server. See lmtp_discard_lhlo_keywords for details. The table is not indexed by hostname for consistency with smtpd_discard_ehlo_keyword_address_maps. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_discard_lhlo_keywords (default: empty)</h2>
<p>A case insensitive list of LHLO keywords (pipelining, starttls, auth, etc.) that the Postfix LMTP client will ignore in the LHLO response from a remote LMTP server. </p>
<p> This feature is available in Postfix 2.3 and later. </p>
<p> Notes:</p>
<dl>
<dt>&bull;</p>
<dd>Specify the <code>silent-discard</code> pseudo keyword to prevent this action from being logged.</p>
<dt>&bull;</p>
<dd>Use the lmtp_discard_lhlo_keyword_address_maps feature to discard LHLO keywords selectively.
</dl>
<h2>lmtp_dns_reply_filter (default: empty)</h2>
<p>Optional filter for Postfix LMTP client DNS lookup results. See smtp_dns_reply_filter for details including an example. </p>
<p> This feature is available in Postfix 3.0 and later.</p>
<h2>lmtp_dns_resolver_options (default: empty)</h2>
<p>The LMTP-specific version of the smtp_dns_resolver_options configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.8 and later.</p>
<h2>lmtp_dns_support_level (default: empty)</h2>
<p>The LMTP-specific version of the smtp_dns_support_level configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.11 and later.</p>
<h2>lmtp_enforce_tls (default: no)</h2>
<p>The LMTP-specific version of the smtp_enforce_tls configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_fallback_relay (default: empty)</h2>
<p>Optional list of relay hosts for LMTP destinations that can&#8217;t be found or that are unreachable. In main.cf elements are separated by whitespace or commas. </p>
<p> By default, mail is returned to the sender when a destination is not found, and delivery is deferred when a destination is unreachable. </p>
<p> The fallback relays must be TCP destinations, specified without a leading &quot;inet:&quot; prefix. Specify a host or host:port. Since MX lookups do not apply with LMTP, there is no need to use the &quot;[host]&quot; or &quot;[host]:port&quot; forms. If you specify multiple LMTP destinations, Postfix will try them in the specified order. </p>
<p> This feature is available in Postfix 3.1 and later.</p>
<h2>lmtp_generic_maps (default: empty)</h2>
<p>The LMTP-specific version of the smtp_generic_maps configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_header_checks (default: empty)</h2>
<p>The LMTP-specific version of the smtp_header_checks configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>lmtp_host_lookup (default: dns)</h2>
<p>The LMTP-specific version of the smtp_host_lookup configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_lhlo_name (default: $myhostname)</h2>
<p>The hostname to send in the LMTP LHLO command. </p>
<p> The default value is the machine hostname. Specify a hostname or [ip.add.re.ss]. </p>
<p> This information can be specified in the main.cf file for all LMTP clients, or it can be specified in the master.cf file for a specific client, for example: </p>
<pre>/etc/postfix/master.cf:
 mylmtp ... lmtp -o lmtp_lhlo_name=foo.bar.com</pre>
<p>This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_lhlo_timeout (default: 300s)</h2>
<p>The Postfix LMTP client time limit for sending the LHLO command, and for receiving the initial remote LMTP server response. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>lmtp_line_length_limit (default: 990)</h2>
<p>The LMTP-specific version of the smtp_line_length_limit configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_mail_timeout (default: 300s)</h2>
<p>The Postfix LMTP client time limit for sending the MAIL FROM command, and for receiving the remote LMTP server response. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>lmtp_mime_header_checks (default: empty)</h2>
<p>The LMTP-specific version of the smtp_mime_header_checks configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>lmtp_mx_address_limit (default: 5)</h2>
<p>The LMTP-specific version of the smtp_mx_address_limit configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_mx_session_limit (default: 2)</h2>
<p>The LMTP-specific version of the smtp_mx_session_limit configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_nested_header_checks (default: empty)</h2>
<p>The LMTP-specific version of the smtp_nested_header_checks configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>lmtp_per_record_deadline (default: no)</h2>
<p>The LMTP-specific version of the smtp_per_record_deadline configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.9 and later.</p>
<h2>lmtp_pix_workaround_delay_time (default: 10s)</h2>
<p>The LMTP-specific version of the smtp_pix_workaround_delay_time configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_pix_workaround_maps (default: empty)</h2>
<p>The LMTP-specific version of the smtp_pix_workaround_maps configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.4 and later.</p>
<h2>lmtp_pix_workaround_threshold_time (default: 500s)</h2>
<p>The LMTP-specific version of the smtp_pix_workaround_threshold_time configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_pix_workarounds (default: empty)</h2>
<p>The LMTP-specific version of the smtp_pix_workaround configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.4 and later.</p>
<h2>lmtp_quit_timeout (default: 300s)</h2>
<p>The Postfix LMTP client time limit for sending the QUIT command, and for receiving the remote LMTP server response. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>lmtp_quote_rfc821_envelope (default: yes)</h2>
<p>The LMTP-specific version of the smtp_quote_rfc821_envelope configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_randomize_addresses (default: yes)</h2>
<p>The LMTP-specific version of the smtp_randomize_addresses configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_rcpt_timeout (default: 300s)</h2>
<p>The Postfix LMTP client time limit for sending the RCPT TO command, and for receiving the remote LMTP server response. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>lmtp_reply_filter (default: empty)</h2>
<p>The LMTP-specific version of the smtp_reply_filter configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.7 and later.</p>
<h2>lmtp_rset_timeout (default: 20s)</h2>
<p>The Postfix LMTP client time limit for sending the RSET command, and for receiving the remote LMTP server response. The LMTP client sends RSET in order to finish a recipient address probe, or to verify that a cached connection is still alive. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>lmtp_sasl_auth_cache_name (default: empty)</h2>
<p>The LMTP-specific version of the smtp_sasl_auth_cache_name configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>lmtp_sasl_auth_cache_time (default: 90d)</h2>
<p>The LMTP-specific version of the smtp_sasl_auth_cache_time configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>lmtp_sasl_auth_enable (default: no)</h2>
<p>Enable SASL authentication in the Postfix LMTP client.</p>
<h2>lmtp_sasl_auth_soft_bounce (default: yes)</h2>
<p>The LMTP-specific version of the smtp_sasl_auth_soft_bounce configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>lmtp_sasl_mechanism_filter (default: empty)</h2>
<p>The LMTP-specific version of the smtp_sasl_mechanism_filter configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_sasl_password_maps (default: empty)</h2>
<p>Optional Postfix LMTP client lookup tables with one username:password entry per host or domain. If a remote host or domain has no username:password entry, then the Postfix LMTP client will not attempt to authenticate to the remote host.</p>
<h2>lmtp_sasl_path (default: empty)</h2>
<p>Implementation-specific information that is passed through to the SASL plug-in implementation that is selected with <code>lmtp_sasl_type</code>. Typically this specifies the name of a configuration file or rendezvous point. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_sasl_security_options (default: noplaintext, noanonymous)</h2>
<p>SASL security options; as of Postfix 2.3 the list of available features depends on the SASL client implementation that is selected with <code>lmtp_sasl_type</code>. </p>
<p> The following security features are defined for the <code>cyrus</code> client SASL implementation:</p>
<dl>
<dt><code>noplaintext</code></p>
<dd>Disallow authentication methods that use plaintext passwords. </p>
<dt><code>noactive</code></p>
<dd>Disallow authentication methods that are vulnerable to non-dictionary active attacks. </p>
<dt><code>nodictionary</code></p>
<dd>Disallow authentication methods that are vulnerable to passive dictionary attack. </p>
<dt><code>noanonymous</code></p>
<dd>Disallow anonymous logins. </p>
</dl>
<p> Example: </p>
<pre>lmtp_sasl_security_options = noplaintext</pre>
<h2>lmtp_sasl_tls_security_options (default: $lmtp_sasl_security_options)</h2>
<p>The LMTP-specific version of the smtp_sasl_tls_security_options configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_sasl_tls_verified_security_options (default: $lmtp_sasl_tls_security_options)</h2>
<p>The LMTP-specific version of the smtp_sasl_tls_verified_security_options configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_sasl_type (default: cyrus)</h2>
<p>The SASL plug-in type that the Postfix LMTP client should use for authentication. The available types are listed with the &quot;<code>postconf -A</code>&quot; command. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_send_dummy_mail_auth (default: no)</h2>
<p>The LMTP-specific version of the smtp_send_dummy_mail_auth configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.9 and later.</p>
<h2>lmtp_send_xforward_command (default: no)</h2>
<p>Send an XFORWARD command to the remote LMTP server when the LMTP LHLO server response announces XFORWARD support. This allows an <code><a href="/docs/linux/man/8-lmtp/">lmtp</a></code>(8) delivery agent, used for content filter message injection, to forward the name, address, protocol and HELO name of the original client to the content filter and downstream queuing LMTP server. Before you change the value to yes, it is best to make sure that your content filter supports this command. </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>lmtp_sender_dependent_authentication (default: no)</h2>
<p>The LMTP-specific version of the smtp_sender_dependent_authentication configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_skip_5xx_greeting (default: yes)</h2>
<p>The LMTP-specific version of the smtp_skip_5xx_greeting configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_skip_quit_response (default: no)</h2>
<p>Wait for the response to the LMTP QUIT command.</p>
<h2>lmtp_starttls_timeout (default: 300s)</h2>
<p>The LMTP-specific version of the smtp_starttls_timeout configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tcp_port (default: 24)</h2>
<p>The default TCP port that the Postfix LMTP client connects to. Specify a symbolic name (see <code><a href="/docs/linux/man/5-services/">services</a></code>(5)) or a numeric port.</p>
<h2>lmtp_tls_CAfile (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_CAfile configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_CApath (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_CApath configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_block_early_mail_reply (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_block_early_mail_reply configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.7 and later.</p>
<h2>lmtp_tls_cert_file (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_cert_file configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_chain_files (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_chain_files configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 3.4 and later.</p>
<h2>lmtp_tls_ciphers (default: medium)</h2>
<p>The LMTP-specific version of the smtp_tls_ciphers configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.6 and later.</p>
<h2>lmtp_tls_connection_reuse (default: no)</h2>
<p>The LMTP-specific version of the smtp_tls_connection_reuse configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 3.4 and later.</p>
<h2>lmtp_tls_dcert_file (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_dcert_file configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_dkey_file (default: $lmtp_tls_dcert_file)</h2>
<p>The LMTP-specific version of the smtp_tls_dkey_file configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_eccert_file (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_eccert_file configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.6 and later, when Postfix is compiled and linked with OpenSSL 1.0.0 or later.</p>
<h2>lmtp_tls_eckey_file (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_eckey_file configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.6 and later, when Postfix is compiled and linked with OpenSSL 1.0.0 or later.</p>
<h2>lmtp_tls_enforce_peername (default: yes)</h2>
<p>The LMTP-specific version of the smtp_tls_enforce_peername configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_exclude_ciphers (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_exclude_ciphers configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_fingerprint_cert_match (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_fingerprint_cert_match configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>lmtp_tls_fingerprint_digest (default: md5)</h2>
<p>The LMTP-specific version of the smtp_tls_fingerprint_digest configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.5 and later.</p>
<h2>lmtp_tls_force_insecure_host_tlsa_lookup (default: no)</h2>
<p>The LMTP-specific version of the smtp_tls_force_insecure_host_tlsa_lookup configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.11 and later.</p>
<h2>lmtp_tls_key_file (default: $lmtp_tls_cert_file)</h2>
<p>The LMTP-specific version of the smtp_tls_key_file configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_loglevel (default: 0)</h2>
<p>The LMTP-specific version of the smtp_tls_loglevel configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_mandatory_ciphers (default: medium)</h2>
<p>The LMTP-specific version of the smtp_tls_mandatory_ciphers configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_mandatory_exclude_ciphers (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_mandatory_exclude_ciphers configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_mandatory_protocols (default: !SSLv2, !SSLv3)</h2>
<p>The LMTP-specific version of the smtp_tls_mandatory_protocols configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_note_starttls_offer (default: no)</h2>
<p>The LMTP-specific version of the smtp_tls_note_starttls_offer configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_per_site (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_per_site configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_policy_maps (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_policy_maps configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_protocols (default: !SSLv2, !SSLv3)</h2>
<p>The LMTP-specific version of the smtp_tls_protocols configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.6 and later.</p>
<h2>lmtp_tls_scert_verifydepth (default: 9)</h2>
<p>The LMTP-specific version of the smtp_tls_scert_verifydepth configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_secure_cert_match (default: nexthop)</h2>
<p>The LMTP-specific version of the smtp_tls_secure_cert_match configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_security_level (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_security_level configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_servername (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_servername configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 3.4 and later.</p>
<h2>lmtp_tls_session_cache_database (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_session_cache_database configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_session_cache_timeout (default: 3600s)</h2>
<p>The LMTP-specific version of the smtp_tls_session_cache_timeout configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_tls_trust_anchor_file (default: empty)</h2>
<p>The LMTP-specific version of the smtp_tls_trust_anchor_file configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.11 and later.</p>
<h2>lmtp_tls_verify_cert_match (default: hostname)</h2>
<p>The LMTP-specific version of the smtp_tls_verify_cert_match configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_use_tls (default: no)</h2>
<p>The LMTP-specific version of the smtp_use_tls configuration parameter. See there for details. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>lmtp_xforward_timeout (default: 300s)</h2>
<p>The Postfix LMTP client time limit for sending the XFORWARD command, and for receiving the remote LMTP server response. </p>
<p> In case of problems the client does NOT try the next address on the mail exchanger list. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds). </p>
<p> This feature is available in Postfix 2.1 and later.</p>
<h2>local_command_shell (default: empty)</h2>
<p>Optional shell program for <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery to non-Postfix command. By default, non-Postfix commands are executed directly; commands are given to given to the default shell (typically, /bin/sh) only when they contain shell meta characters or shell built-in commands. </p>
<p> &quot;sendmail&#8217;s restricted shell&quot; (smrsh) is what most people will use in order to restrict what programs can be run from e.g. .forward files (smrsh is part of the Sendmail distribution). </p>
<p> Note: when a shell program is specified, it is invoked even when the command contains no shell built-in commands or meta characters. </p>
<p> Example: </p>
<pre>local_command_shell = /some/where/smrsh -c
local_command_shell = /bin/bash -c</pre>
<h2>local_delivery_status_filter (default: $default_delivery_status_filter)</h2>
<p>Optional filter for the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent to change the status code or explanatory text of successful or unsuccessful deliveries. See default_delivery_status_filter for details. </p>
<p> This feature is available in Postfix 3.0 and later.</p>
<h2>local_destination_concurrency_limit (default: 2)</h2>
<p>The maximal number of parallel deliveries via the local mail delivery transport to the same recipient (when &quot;local_destination_recipient_limit = 1&quot;) or the maximal number of parallel deliveries to the same local domain (when &quot;local_destination_recipient_limit &gt; 1&quot;). This limit is enforced by the queue manager. The message delivery transport name is the first field in the entry in the master.cf file. </p>
<p> A low limit of 2 is recommended, just in case someone has an expensive shell command in a .forward file or in an alias (e.g., a mailing list manager). You don&#8217;t want to run lots of those at the same time.</p>
<h2>local_destination_recipient_limit (default: 1)</h2>
<p>The maximal number of recipients per message delivery via the local mail delivery transport. This limit is enforced by the queue manager. The message delivery transport name is the first field in the entry in the master.cf file. </p>
<p> Setting this parameter to a value &gt; 1 changes the meaning of local_destination_concurrency_limit from concurrency per recipient into concurrency per domain.</p>
<h2>local_header_rewrite_clients (default: permit_inet_interfaces)</h2>
<p>Rewrite message header addresses in mail from these clients and update incomplete addresses with the domain name in $myorigin or $mydomain; either don&#8217;t rewrite message headers from other clients at all, or rewrite message headers and update incomplete addresses with the domain specified in the remote_header_rewrite_domain parameter. </p>
<p> See the append_at_myorigin and append_dot_mydomain parameters for details of how domain names are appended to incomplete addresses. </p>
<p> Specify a list of zero or more of the following:</p>
<dl>
<dt><code>permit_inet_interfaces</code></p>
<dd>Append the domain name in $myorigin or $mydomain when the client IP address matches $inet_interfaces. This is enabled by default. </p>
<dt><code>permit_mynetworks</code></p>
<dd>Append the domain name in $myorigin or $mydomain when the client IP address matches any network or network address listed in $mynetworks. This setting will not prevent remote mail header address rewriting when mail from a remote client is forwarded by a neighboring system. </p>
<dt><code>permit_sasl_authenticated </code></p>
<dd>Append the domain name in $myorigin or $mydomain when the client is successfully authenticated via the RFC 4954 (AUTH) protocol. </p>
<dt><code>permit_tls_clientcerts </code></p>
<dd>Append the domain name in $myorigin or $mydomain when the remote SMTP client TLS certificate fingerprint or public key fingerprint (Postfix 2.9 and later) is listed in $relay_clientcerts. The fingerprint digest algorithm is configurable via the smtpd_tls_fingerprint_digest parameter (hard-coded as md5 prior to Postfix version 2.5). </p>
<dt><code>permit_tls_all_clientcerts </code></p>
<dd>Append the domain name in $myorigin or $mydomain when the remote SMTP client TLS certificate is successfully verified, regardless of whether it is listed on the server, and regardless of the certifying authority. </p>
<dt><code>check_address_map </code><i>type:table</i></p>
<dd>
<dt><i>type:table</i></p>
<dd>Append the domain name in $myorigin or $mydomain when the client IP address matches the specified lookup table. The lookup result is ignored, and no subnet lookup is done. This is suitable for, e.g., pop-before-smtp lookup tables. </p>
</dl>
<p> Examples: </p>
<p> The Postfix &lt; 2.2 backwards compatible setting: always rewrite message headers, and always append my own domain to incomplete header addresses. </p>
<pre>local_header_rewrite_clients = static:all</pre>
<p>The purist (and default) setting: rewrite headers only in mail from Postfix sendmail and in SMTP mail from this machine. </p>
<pre>local_header_rewrite_clients = permit_inet_interfaces</pre>
<p>The intermediate setting: rewrite header addresses and append $myorigin or $mydomain information only with mail from Postfix sendmail, from local clients, or from authorized SMTP clients. </p>
<p> Note: this setting will not prevent remote mail header address rewriting when mail from a remote client is forwarded by a neighboring system. </p>
<pre>local_header_rewrite_clients = permit_mynetworks,
 permit_sasl_authenticated permit_tls_clientcerts
 check_address_map hash:/etc/postfix/pop-before-smtp</pre>
<h2>local_recipient_maps (default: proxy:unix:passwd.byname $alias_maps)</h2>
<p>Lookup tables with all names or addresses of local recipients: a recipient address is local when its domain matches $mydestination, $inet_interfaces or $proxy_interfaces. Specify @domain as a wild-card for domains that do not have a valid recipient list. Technically, tables listed with $local_recipient_maps are used as lists: Postfix needs to know only if a lookup string is found or not, but it does not use the result from table lookup. </p>
<p> Specify zero or more &quot;type:name&quot; lookup tables, separated by whitespace or comma. Tables will be searched in the specified order until a match is found. </p>
<p> If this parameter is non-empty (the default), then the Postfix SMTP server will reject mail for unknown local users. </p>
<p> To turn off local recipient checking in the Postfix SMTP server, specify &quot;local_recipient_maps =&quot; (i.e. empty). </p>
<p> The default setting assumes that you use the default Postfix local delivery agent for local delivery. You need to update the local_recipient_maps setting if:</p>
<dl>
<dt>&bull;</p>
<dd>You redefine the local delivery agent in master.cf.</p>
<dt>&bull;</p>
<dd>You redefine the &quot;local_transport&quot; setting in main.cf.</p>
<dt>&bull;</p>
<dd>You use the &quot;luser_relay&quot;, &quot;mailbox_transport&quot;, or &quot;fallback_transport&quot; feature of the Postfix <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent.
</dl>
<p> Details are described in the LOCAL_RECIPIENT_README file. </p>
<p> Beware: if the Postfix SMTP server runs chrooted, you need to access the passwd file via the <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) service, in order to overcome chroot access restrictions. The alternative, maintaining a copy of the system password file in the chroot jail is not practical. </p>
<p> Examples: </p>
<pre>local_recipient_maps =</pre>
<h2>local_transport (default: local:$myhostname)</h2>
<p>The default mail delivery transport and next-hop destination for final delivery to domains listed with mydestination, and for [ipaddress] destinations that match $inet_interfaces or $proxy_interfaces. This information can be overruled with the <code><a href="/docs/linux/man/5-transport/">transport</a></code>(5) table. </p>
<p> By default, local mail is delivered to the transport called &quot;local&quot;, which is just the name of a service that is defined the master.cf file. </p>
<p> Specify a string of the form <i>transport:nexthop</i>, where <i>transport</i> is the name of a mail delivery transport defined in master.cf. The <i>:nexthop</i> destination is optional; its syntax is documented in the manual page of the corresponding delivery agent. </p>
<p> Beware: if you override the default local delivery agent then you need to review the LOCAL_RECIPIENT_README document, otherwise the SMTP server may reject mail for local recipients.</p>
<h2>luser_relay (default: empty)</h2>
<p>Optional catch-all destination for unknown <code><a href="/docs/linux/man/8-local/">local</a></code>(8) recipients. By default, mail for unknown recipients in domains that match $mydestination, $inet_interfaces or $proxy_interfaces is returned as undeliverable. </p>
<p> The luser_relay value is not subject to Postfix configuration parameter $name expansion. Instead, the following $name expansions are done:</p>
<dl>
<dt><code>$domain</code></p>
<dd>The recipient domain. </p>
<dt><code>$extension</code></p>
<dd>The recipient address extension. </p>
<dt><code>$home</code></p>
<dd>The recipient&#8217;s home directory. </p>
<dt><code>$local</code></p>
<dd>The entire recipient address localpart. </p>
<dt><code>$recipient</code></p>
<dd>The full recipient address. </p>
<dt><code>$recipient_delimiter</code></p>
<dd>The address extension delimiter that was found in the recipient address (Postfix 2.11 and later), or the system-wide recipient address extension delimiter (Postfix 2.10 and earlier). </p>
<dt><code>$shell</code></p>
<dd>The recipient&#8217;s login shell. </p>
<dt><code>$user</code></p>
<dd>The recipient username. </p>
<dt><code>${name?value}</code></p>
<dd>Expands to <i>value</i> when <i>$name</i> has a non-empty value. </p>
<dt><code>${name:value}</code></p>
<dd>Expands to <i>value</i> when <i>$name</i> has an empty value. </p>
</dl>
<p> Instead of $name you can also specify ${name} or $(name). </p>
<p> Note: luser_relay works only for the Postfix <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent. </p>
<p> Note: if you use this feature for accounts not in the UNIX password file, then you must specify &quot;local_recipient_maps =&quot; (i.e. empty) in the main.cf file, otherwise the Postfix SMTP server will reject mail for non-UNIX accounts with &quot;User unknown in local recipient table&quot;. </p>
<p> Examples: </p>
<pre>luser_relay = $user [at] other.host
luser_relay = $local [at] other.host
luser_relay = admin+$local</pre>
<h2>mail_name (default: Postfix)</h2>
<p>The mail system name that is displayed in Received: headers, in the SMTP greeting banner, and in bounced mail.</p>
<h2>mail_owner (default: postfix)</h2>
<p>The UNIX system account that owns the Postfix queue and most Postfix daemon processes. Specify the name of an unprivileged user account that does not share a user or group ID with other accounts, and that owns no other files or processes on the system. In particular, don&#8217;t specify nobody or daemon. PLEASE USE A DEDICATED USER ID AND GROUP ID. </p>
<p> When this parameter value is changed you need to re-run &quot;<code>postfix set-permissions</code>&quot; (with Postfix version 2.0 and earlier: &quot;<code>/etc/postfix/post-install set-permissions</code>&quot;.</p>
<h2>mail_release_date (default: see postconf -d output)</h2>
<p>The Postfix release date, in &quot;YYYYMMDD&quot; format.</p>
<h2>mail_spool_directory (default: see postconf -d output)</h2>
<p>The directory where <code><a href="/docs/linux/man/8-local/">local</a></code>(8) UNIX-style mailboxes are kept. The default setting depends on the system type. Specify a name ending in / for maildir-style delivery. </p>
<p> Note: maildir delivery is done with the privileges of the recipient. If you use the mail_spool_directory setting for maildir style delivery, then you must create the top-level maildir directory in advance. Postfix will not create it. </p>
<p> Examples: </p>
<pre>mail_spool_directory = /var/mail
mail_spool_directory = /var/spool/mail</pre>
<h2>mail_version (default: see postconf -d output)</h2>
<p>The version of the mail system. Stable releases are named <i>major</i>.<i>minor</i>.<i>patchlevel</i>. Experimental releases also include the release date. The version string can be used in, for example, the SMTP greeting banner.</p>
<h2>mailbox_command (default: empty)</h2>
<p>Optional external command that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent should use for mailbox delivery. The command is run with the user ID and the primary group ID privileges of the recipient. Exception: command delivery for root executes with $default_privs privileges. This is not a problem, because 1) mail for root should always be aliased to a real user and 2) don&#8217;t log in as root, use &quot;su&quot; instead. </p>
<p> The following environment variables are exported to the command:</p>
<dl>
<dt><code>CLIENT_ADDRESS</code></p>
<dd>Remote client network address. Available in Postfix version 2.2 and later. </p>
<dt><code>CLIENT_HELO</code></p>
<dd>Remote client EHLO command parameter. Available in Postfix version 2.2 and later. </p>
<dt><code>CLIENT_HOSTNAME</code></p>
<dd>Remote client hostname. Available in Postfix version 2.2 and later. </p>
<dt><code>CLIENT_PROTOCOL</code></p>
<dd>Remote client protocol. Available in Postfix version 2.2 and later. </p>
<dt><code>DOMAIN</code></p>
<dd>The domain part of the recipient address. </p>
<dt><code>EXTENSION</code></p>
<dd>The optional address extension. </p>
<dt><code>HOME</code></p>
<dd>The recipient home directory. </p>
<dt><code>LOCAL</code></p>
<dd>The recipient address localpart. </p>
<dt><code>LOGNAME</code></p>
<dd>The recipient&#8217;s username. </p>
<dt><code>ORIGINAL_RECIPIENT</code></p>
<dd>The entire recipient address, before any address rewriting or aliasing. </p>
<dt><code>RECIPIENT</code></p>
<dd>The full recipient address. </p>
<dt><code>SASL_METHOD</code></p>
<dd>SASL authentication method specified in the remote client AUTH command. Available in Postfix version 2.2 and later. </p>
<dt><code>SASL_SENDER</code></p>
<dd>SASL sender address specified in the remote client MAIL FROM command. Available in Postfix version 2.2 and later. </p>
<dt><code>SASL_USER</code></p>
<dd>SASL username specified in the remote client AUTH command. Available in Postfix version 2.2 and later. </p>
<dt><code>SENDER</code></p>
<dd>The full sender address. </p>
<dt><code>SHELL</code></p>
<dd>The recipient&#8217;s login shell. </p>
<dt><code>USER</code></p>
<dd>The recipient username. </p>
</dl>
<p> Unlike other Postfix configuration parameters, the mailbox_command parameter is not subjected to $name substitutions. This is to make it easier to specify shell syntax (see example below). </p>
<p> If you can, avoid shell meta characters because they will force Postfix to run an expensive shell process. If you&#8217;re delivering via &quot;procmail&quot; then running a shell won&#8217;t make a noticeable difference in the total cost. </p>
<p> Note: if you use the mailbox_command feature to deliver mail system-wide, you must set up an alias that forwards mail for root to a real user. </p>
<p> The precedence of <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery features from high to low is: aliases, .forward files, mailbox_transport_maps, mailbox_transport, mailbox_command_maps, mailbox_command, home_mailbox, mail_spool_directory, fallback_transport_maps, fallback_transport and luser_relay. </p>
<p> Examples: </p>
<pre>mailbox_command = /some/where/procmail
mailbox_command = /some/where/procmail -a &quot;$EXTENSION&quot;
mailbox_command = /some/where/maildrop -d &quot;$USER&quot;
 -f &quot;$SENDER&quot; &quot;$EXTENSION&quot;</pre>
<h2>mailbox_command_maps (default: empty)</h2>
<p>Optional lookup tables with per-recipient external commands to use for <code><a href="/docs/linux/man/8-local/">local</a></code>(8) mailbox delivery. Behavior is as with mailbox_command. </p>
<p> The precedence of <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery features from high to low is: aliases, .forward files, mailbox_transport_maps, mailbox_transport, mailbox_command_maps, mailbox_command, home_mailbox, mail_spool_directory, fallback_transport_maps, fallback_transport and luser_relay. </p>
<p> Specify zero or more &quot;type:name&quot; lookup tables, separated by whitespace or comma. Tables will be searched in the specified order until a match is found.</p>
<h2>mailbox_delivery_lock (default: see postconf -d output)</h2>
<p>How to lock a UNIX-style <code><a href="/docs/linux/man/8-local/">local</a></code>(8) mailbox before attempting delivery. For a list of available file locking methods, use the &quot;<code>postconf -l</code>&quot; command. </p>
<p> This setting is ignored with <code>maildir</code> style delivery, because such deliveries are safe without explicit locks. </p>
<p> Note: The <code>dotlock</code> method requires that the recipient UID or GID has write access to the parent directory of the mailbox file. </p>
<p> Note: the default setting of this parameter is system dependent.</p>
<h2>mailbox_size_limit (default: 51200000)</h2>
<p>The maximal size of any <code><a href="/docs/linux/man/8-local/">local</a></code>(8) individual mailbox or maildir file, or zero (no limit). In fact, this limits the size of any file that is written to upon local delivery, including files written by external commands that are executed by the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent. </p>
<p> This limit must not be smaller than the message size limit.</p>
<h2>mailbox_transport (default: empty)</h2>
<p>Optional message delivery transport that the <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery agent should use for mailbox delivery to all local recipients, whether or not they are found in the UNIX passwd database. </p>
<p> The precedence of <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery features from high to low is: aliases, .forward files, mailbox_transport_maps, mailbox_transport, mailbox_command_maps, mailbox_command, home_mailbox, mail_spool_directory, fallback_transport_maps, fallback_transport and luser_relay.</p>
<h2>mailbox_transport_maps (default: empty)</h2>
<p>Optional lookup tables with per-recipient message delivery transports to use for <code><a href="/docs/linux/man/8-local/">local</a></code>(8) mailbox delivery, whether or not the recipients are found in the UNIX passwd database. </p>
<p> The precedence of <code><a href="/docs/linux/man/8-local/">local</a></code>(8) delivery features from high to low is: aliases, .forward files, mailbox_transport_maps, mailbox_transport, mailbox_command_maps, mailbox_command, home_mailbox, mail_spool_directory, fallback_transport_maps, fallback_transport and luser_relay. </p>
<p> Specify zero or more &quot;type:name&quot; lookup tables, separated by whitespace or comma. Tables will be searched in the specified order until a match is found. </p>
<p> For safety reasons, this feature does not allow $number substitutions in regular expression maps. </p>
<p> This feature is available in Postfix 2.3 and later.</p>
<h2>maillog_file (default: empty)</h2>
<p>The name of an optional logfile that is written by the Postfix <code><a href="/docs/linux/man/8-postlogd/">postlogd</a></code>(8) service. An empty value selects logging to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). Specify &quot;/dev/stdout&quot; to select logging to standard output. Stdout logging requires that Postfix is started with &quot;postfix start-fg&quot;. </p>
<p> Note 1: The maillog_file parameter value must contain a prefix that is specified with the maillog_file_prefixes parameter. </p>
<p> Note 2: Some Postfix non-daemon programs may still log information to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8), before they have processed their configuration parameters and command-line options. </p>
<p> This feature is available in Postfix 3.4 and later.</p>
<h2>maillog_file_compressor (default: gzip)</h2>
<p>The program to run after rotating $maillog_file with &quot;postfix logrotate&quot;. The command is run with the rotated logfile name as its first argument. </p>
<p> This feature is available in Postfix 3.4 and later.</p>
<h2>maillog_file_prefixes (default: /var, /dev/stdout)</h2>
<p>A list of allowed prefixes for a maillog_file value. This is a safety feature to contain the damage from a single configuration mistake. Specify one or more prefix strings, separated by comma or whitespace. </p>
<p> This feature is available in Postfix 3.4 and later.</p>
<h2>maillog_file_rotate_suffix (default: %Y%M%d-%H%M%S)</h2>
<p>The format of the suffix to append to $maillog_file while rotating the file with &quot;postfix logrotate&quot;. See <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) for syntax. The default suffix, YYYYMMDD-HHMMSS, allows logs to be rotated frequently. </p>
<p> This feature is available in Postfix 3.4 and later.</p>
<h2>mailq_path (default: see postconf -d output)</h2>
<p>Sendmail compatibility feature that specifies where the Postfix <code><a href="/docs/linux/man/1-mailq/">mailq</a></code>(1) command is installed. This command can be used to list the Postfix mail queue.</p>
<h2>manpage_directory (default: see postconf -d output)</h2>
<p>Where the Postfix manual pages are installed.</p>
<h2>maps_rbl_domains (default: empty)</h2>
<p>Obsolete feature: use the reject_rbl_client feature instead.</p>
<h2>maps_rbl_reject_code (default: 554)</h2>
<p>The numerical Postfix SMTP server response code when a remote SMTP client request is blocked by the reject_rbl_client, reject_rhsbl_client, reject_rhsbl_reverse_client, reject_rhsbl_sender or reject_rhsbl_recipient restriction. </p>
<p> Do not change this unless you have a complete understanding of RFC 5321.</p>
<h2>masquerade_classes (default: envelope_sender, header_sender, header_recipient)</h2>
<p>What addresses are subject to address masquerading. </p>
<p> By default, address masquerading is limited to envelope sender addresses, and to header sender and header recipient addresses. This allows you to use address masquerading on a mail gateway while still being able to forward mail to users on individual machines. </p>
<p> Specify zero or more of: envelope_sender, envelope_recipient, header_sender, header_recipient</p>
<h2>masquerade_domains (default: empty)</h2>
<p>Optional list of domains whose subdomain structure will be stripped off in email addresses. </p>
<p> The list is processed left to right, and processing stops at the first match. Thus, </p>
<pre>masquerade_domains = foo.example.com example.com</pre>
<p>strips &quot;user [at] any.thing.foo.example.com&quot; to &quot;user [at] foo.example.com&quot;, but strips &quot;user [at] any.thing.else.example.com&quot; to &quot;user [at] example.com&quot;. </p>
<p> A domain name prefixed with ! means do not masquerade this domain or its subdomains. Thus, </p>
<pre>masquerade_domains = !foo.example.com example.com</pre>
<p>does not change &quot;user [at] any.thing.foo.example.com&quot; or &quot;user [at] foo.example.com&quot;, but strips &quot;user [at] any.thing.else.example.com&quot; to &quot;user [at] example.com&quot;. </p>
<p> Note: with Postfix version 2.2, message header address masquerading happens only when message header address rewriting is enabled:</p>
<dl>
<dt>&bull;</p>
<dd>The message is received with the Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command,</p>
<dt>&bull;</p>
<dd>The message is received from a network client that matches $local_header_rewrite_clients,</p>
<dt>&bull;</p>
<dd>The message is received from the network, and the remote_header_rewrite_domain parameter specifies a non-empty value.
</dl>
<p> To get the behavior before Postfix version 2.2, specify &quot;local_header_rewrite_clients = static:all&quot;. </p>
<p> Example: </p>
<pre>masquerade_domains = $mydomain</pre>
<h2>masquerade_exceptions (default: empty)</h2>
<p>Optional list of user names that are not subjected to address masquerading, even when their addresses match $masquerade_domains. </p>
<p> By default, address masquerading makes no exceptions. </p>
<p> Specify a list of user names, &quot;/file/name&quot; or &quot;type:table&quot; patterns, separated by commas and/or whitespace. The list is matched left to right, and the search stops on the first match. A &quot;/file/name&quot; pattern is replaced by its contents; a &quot;type:table&quot; lookup table is matched when a name matches a lookup key (the lookup result is ignored). Continue long lines by starting the next line with whitespace. Specify &quot;!pattern&quot; to exclude a name from the list. The form &quot;!/file/name&quot; is supported only in Postfix version 2.4 and later. </p>
<p> Examples: </p>
<pre>masquerade_exceptions = root, mailer-daemon
masquerade_exceptions = root</pre>
<h2>master_service_disable (default: empty)</h2>
<p>Selectively disable <code><a href="/docs/linux/man/8-master/">master</a></code>(8) listener ports by service type or by service name and type. Specify a list of service types (&quot;inet&quot;, &quot;unix&quot;, &quot;fifo&quot;, or &quot;pass&quot;) or &quot;name/type&quot; tuples, where &quot;name&quot; is the first field of a master.cf entry and &quot;type&quot; is a service type. As with other Postfix matchlists, a search stops at the first match. Specify &quot;!pattern&quot; to exclude a service from the list. By default, all <code><a href="/docs/linux/man/8-master/">master</a></code>(8) listener ports are enabled. </p>
<p> Note: this feature does not support &quot;/file/name&quot; or &quot;type:table&quot; patterns, nor does it support wildcards such as &quot;*&quot; or &quot;all&quot;. This is intentional. </p>
<p> Examples: </p>
<pre># With Postfix 2.6..2.10 use '.' instead of '/'.
# Turn on all <code><a href="//www.systutorials.com/docs/linux/man/8-master/">master</a></code>(8) listener ports (the default).
master_service_disable =
# Turn off only the main SMTP listener port.
master_service_disable = smtp/inet
# Turn off all TCP/IP listener ports.
master_service_disable = inet
# Turn off all TCP/IP listener ports except &quot;foo&quot;.
master_service_disable = !foo/inet, inet</pre>
<p>This feature is available in Postfix 2.6 and later.</p>
<h2>max_idle (default: 100s)</h2>
<p>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily. This parameter is ignored by the Postfix queue manager and by other long-lived Postfix daemon processes. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>max_use (default: 100)</h2>
<p>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily. This parameter is ignored by the Postfix queue manager and by other long-lived Postfix daemon processes.</p>
<h2>maximal_backoff_time (default: 4000s)</h2>
<p>The maximal time between attempts to deliver a deferred message. </p>
<p> This parameter should be set to a value greater than or equal to $minimal_backoff_time. See also $queue_run_delay. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is s (seconds).</p>
<h2>maximal_queue_lifetime (default: 5d)</h2>
<p>Consider a message as undeliverable, when delivery fails with a temporary error, and the time in the queue has reached the maximal_queue_lifetime limit. </p>
<p> Time units: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is d (days). </p>
<p> Specify 0 when mail delivery should be tried only once.</p>
<h2>message_drop_headers (default: bcc, content-length, resent-bcc, return-path)</h2>
<p>Names of message headers that the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon will remove after applying <code><a href="/docs/linux/man/5-header_checks/">header_checks</a></code>(5) and before invoking Milter applications. The default setting is compatible with Postfix &lt; 3.0. </p>
<p> Specify a list of header names, separated by comma or space. Names are matched in a case-insensitive manner. The list of supported header names is limited only by available memory. </p>
<p> This feature is available in Postfix 3.0 and later.</p>
<h2>message_reject_characters (default: empty)</h2>
<p>The set of characters that Postfix will reject in message content. The usual C-like escape sequences are recognized:    
  	  \<i>ddd</i> (up to three octal digits) and \. </p>
<p> Note 1: this feature does not recognize text that requires MIME decoding. It inspects raw message content, just like header_checks and body_checks. </p>
<p> Note 2: this feature is disabled with &quot;receive_override_options = no_header_body_checks&quot;. </p>
<p> Example: </p>
<pre>message_reject_characters = 
