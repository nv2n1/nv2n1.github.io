---
title: "cleanup(8)"
name: "cleanup"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cleanup/"
description: "cleanup – canonicalize and enqueue Postfix message"
---

<p>cleanup &#8211; canonicalize and enqueue Postfix message</p>
<h2>Synopsis</h2>
<pre><code>cleanup</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon processes inbound mail, inserts it into the <code>incoming</code> mail queue, and informs the queue manager of its arrival. </p>
<p> The <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon always performs the following transformations:</p>
<dl>
<dt>&bull;</dt>
<dd>Insert missing message headers: (<code>Resent-</code>) <code>From:</code>, <code>To:</code>, <code>Message-Id:</code>, and <code>Date:</code>.</dd>
<dt>&bull;</dt>
<dd>Transform envelope and header addresses to the standard <i>user [at] fully-qualified-domain</i> form that is expected by other Postfix programs. This task is delegated to the <code><a href="/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a></code>(8) daemon.</dd>
<dt>&bull;</dt>
<dd>Eliminate duplicate envelope recipient addresses.</dd></dl>
<p> The following address transformations are optional:</p>
<dl>
<dt>&bull;</dt>
<dd>Optionally, rewrite all envelope and header addresses according to the mappings specified in the <code><a href="/docs/linux/man/5-canonical/">canonical</a></code>(5) lookup tables.</dd>
<dt>&bull;</dt>
<dd>Optionally, masquerade envelope sender addresses and message header addresses (i.e. strip host or domain information below all domains listed in the <code>masquerade_domains</code> parameter, except for user names listed in <code>masquerade_exceptions</code>). By default, address masquerading does not affect envelope recipients.</dd>
<dt>&bull;</dt>
<dd>Optionally, expand envelope recipients according to information found in the <code><a href="/docs/linux/man/5-virtual/">virtual</a></code>(5) lookup tables.</dd></dl>
<p> The <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon performs sanity checks on the content of each message. When it finds a problem, by default it returns a diagnostic status to the client, and leaves it up to the client to deal with the problem. Alternatively, the client can request the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon to bounce the message back to the sender in case of trouble.</p>
<h2>Standards</h2>
<pre>RFC 822 (ARPA Internet Text Messages)
RFC 2045 (MIME: Format of Internet Message Bodies)
RFC 2046 (MIME: Media Types)
RFC 2822 (Internet Message Format)
RFC 3463 (Enhanced Status Codes)
RFC 3464 (Delivery status notifications)
RFC 5322 (Internet Message Format)</pre>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code>syslogd</code>(8).</p>
<h2>Bugs</h2>
<p>Table-driven rewriting rules make it hard to express <code>if then else</code> and other logical relationships.</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are picked up automatically, as <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Compatibility Controls</h2>
<dl>
<dt><code>undisclosed_recipients_header (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>Message header that the Postfix <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) server inserts when a message contains no To: or Cc: message header.</dd></dl>
<p> Available in Postfix version 2.1 only:</p>
<dl>
<dt><code>enable_errors_to (no)</code></dt>
<dd>Report mail delivery errors to the address specified with the non-standard Errors-To: message header, instead of the envelope sender address (this feature is removed with Postfix version 2.2, is turned off by default with Postfix version 2.1, and is always turned on with older Postfix versions).</dd></dl>
<p> Available in Postfix version 2.6 and later:</p>
<dl>
<dt><code>always_add_missing_headers (no)</code></dt>
<dd>Always add (Resent-) From:, To:, Date: or Message-ID: headers when not present.</dd></dl>
<p> Available in Postfix version 2.9 and later:</p>
<dl>
<dt><code>enable_long_queue_ids (no)</code></dt>
<dd>Enable long, non-repeating, queue IDs (queue file names).</dd></dl>
<h2>Built-In Content Filtering Controls</h2>
<p>Postfix built-in content filtering is meant to stop a flood of worms or viruses. It is not a general content filter.</p>
<dl>
<dt><code>body_checks (empty)</code></dt>
<dd>Optional lookup tables for content inspection as specified in the <code><a href="/docs/linux/man/5-body_checks/">body_checks</a></code>(5) manual page.</dd>
<dt><code>header_checks (empty)</code></dt>
<dd>Optional lookup tables for content inspection of primary non-MIME message headers, as specified in the <code><a href="/docs/linux/man/5-header_checks/">header_checks</a></code>(5) manual page.</dd></dl>
<p> Available in Postfix version 2.0 and later:</p>
<dl>
<dt><code>body_checks_size_limit (51200)</code></dt>
<dd>How much text in a message body segment (or attachment, if you prefer to use that term) is subjected to body_checks inspection.</dd>
<dt><code>mime_header_checks ($header_checks)</code></dt>
<dd>Optional lookup tables for content inspection of MIME related message headers, as described in the <code><a href="/docs/linux/man/5-header_checks/">header_checks</a></code>(5) manual page.</dd>
<dt><code>nested_header_checks ($header_checks)</code></dt>
<dd>Optional lookup tables for content inspection of non-MIME message headers in attached messages, as described in the <code><a href="/docs/linux/man/5-header_checks/">header_checks</a></code>(5) manual page.</dd></dl>
<p> Available in Postfix version 2.3 and later:</p>
<dl>
<dt><code>message_reject_characters (empty)</code></dt>
<dd>The set of characters that Postfix will reject in message content.</dd>
<dt><code>message_strip_characters (empty)</code></dt>
<dd>The set of characters that Postfix will remove from message content.</dd></dl>
<h2>Before Queue Milter Controls</h2>
<p>As of version 2.3, Postfix supports the Sendmail version 8 Milter (mail filter) protocol. When mail is not received via the <a href="/docs/linux/man/8-smtpd/">smtpd</a>(8) server, the <a href="/docs/linux/man/8-cleanup/">cleanup</a>(8) server will simulate SMTP events to the extent that this is possible. For details see the MILTER_README document.</p>
<dl>
<dt><code>non_smtpd_milters (empty)</code></dt>
<dd>A list of Milter (mail filter) applications for new mail that does not arrive via the Postfix <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) server.</dd>
<dt><code>milter_protocol (6)</code></dt>
<dd>The mail filter protocol version and optional protocol extensions for communication with a Milter application; prior to Postfix 2.6 the default protocol is 2.</dd>
<dt><code>milter_default_action (tempfail)</code></dt>
<dd>The default action when a Milter (mail filter) application is unavailable or mis-configured.</dd>
<dt><code>milter_macro_daemon_name ($myhostname)</code></dt>
<dd>The {daemon_name} macro value for Milter (mail filter) applications.</dd>
<dt><code>milter_macro_v ($mail_name $mail_version)</code></dt>
<dd>The {v} macro value for Milter (mail filter) applications.</dd>
<dt><code>milter_connect_timeout (30s)</code></dt>
<dd>The time limit for connecting to a Milter (mail filter) application, and for negotiating protocol options.</dd>
<dt><code>milter_command_timeout (30s)</code></dt>
<dd>The time limit for sending an SMTP command to a Milter (mail filter) application, and for receiving the response.</dd>
<dt><code>milter_content_timeout (300s)</code></dt>
<dd>The time limit for sending message content to a Milter (mail filter) application, and for receiving the response.</dd>
<dt><code>milter_connect_macros (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>The macros that are sent to Milter (mail filter) applications after completion of an SMTP connection.</dd>
<dt><code>milter_helo_macros (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>The macros that are sent to Milter (mail filter) applications after the SMTP HELO or EHLO command.</dd>
<dt><code>milter_mail_macros (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>The macros that are sent to Milter (mail filter) applications after the SMTP MAIL FROM command.</dd>
<dt><code>milter_rcpt_macros (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>The macros that are sent to Milter (mail filter) applications after the SMTP RCPT TO command.</dd>
<dt><code>milter_data_macros (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>The macros that are sent to version 4 or higher Milter (mail filter) applications after the SMTP DATA command.</dd>
<dt><code>milter_unknown_command_macros (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>The macros that are sent to version 3 or higher Milter (mail filter) applications after an unknown SMTP command.</dd>
<dt><code>milter_end_of_data_macros (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>The macros that are sent to Milter (mail filter) applications after the message end-of-data.</dd></dl>
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><code>milter_end_of_header_macros (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>The macros that are sent to Milter (mail filter) applications after the end of the message header.</dd></dl>
<p> Available in Postfix version 2.7 and later:</p>
<dl>
<dt><code>milter_header_checks (empty)</code></dt>
<dd>Optional lookup tables for content inspection of message headers that are produced by Milter applications.</dd></dl>
<h2>Mime Processing Controls</h2>
<p>Available in Postfix version 2.0 and later:</p>
<dl>
<dt><code>disable_mime_input_processing (no)</code></dt>
<dd>Turn off MIME processing while receiving mail.</dd>
<dt><code>mime_boundary_length_limit (2048)</code></dt>
<dd>The maximal length of MIME multipart boundary strings.</dd>
<dt><code>mime_nesting_limit (100)</code></dt>
<dd>The maximal recursion level that the MIME processor will handle.</dd>
<dt><code>strict_8bitmime (no)</code></dt>
<dd>Enable both strict_7bit_headers and strict_8bitmime_body.</dd>
<dt><code>strict_7bit_headers (no)</code></dt>
<dd>Reject mail with 8-bit text in message headers.</dd>
<dt><code>strict_8bitmime_body (no)</code></dt>
<dd>Reject 8-bit message body text without 8-bit MIME content encoding information.</dd>
<dt><code>strict_mime_encoding_domain (no)</code></dt>
<dd>Reject mail with invalid Content-Transfer-Encoding: information for the message/* or multipart/* MIME content types.</dd></dl>
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><code>detect_8bit_encoding_header (yes)</code></dt>
<dd>Automatically detect 8BITMIME body content by looking at Content-Transfer-Encoding: message headers; historically, this behavior was hard-coded to be &quot;always on&quot;.</dd></dl>
<h2>Automatic Bcc Recipient Controls</h2>
<p>Postfix can automatically add BCC (blind carbon copy) when mail enters the mail system:</p>
<dl>
<dt><code>always_bcc (empty)</code></dt>
<dd>Optional address that receives a &quot;blind carbon copy&quot; of each message that is received by the Postfix mail system.</dd></dl>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>sender_bcc_maps (empty)</code></dt>
<dd>Optional BCC (blind carbon-copy) address lookup tables, indexed by sender address.</dd>
<dt><code>recipient_bcc_maps (empty)</code></dt>
<dd>Optional BCC (blind carbon-copy) address lookup tables, indexed by recipient address.</dd></dl>
<h2>Address Transformation Controls</h2>
<p>Address rewriting is delegated to the <code><a href="/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a></code>(8) daemon. The <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) server implements table driven address mapping.</p>
<dl>
<dt><code>empty_address_recipient (MAILER-DAEMON)</code></dt>
<dd>The recipient of mail addressed to the null address.</dd>
<dt><code>canonical_maps (empty)</code></dt>
<dd>Optional address mapping lookup tables for message headers and envelopes.</dd>
<dt><code>recipient_canonical_maps (empty)</code></dt>
<dd>Optional address mapping lookup tables for envelope and header recipient addresses.</dd>
<dt><code>sender_canonical_maps (empty)</code></dt>
<dd>Optional address mapping lookup tables for envelope and header sender addresses.</dd>
<dt><code>masquerade_classes (envelope_sender, header_sender, header_recipient)</code></dt>
<dd>What addresses are subject to address masquerading.</dd>
<dt><code>masquerade_domains (empty)</code></dt>
<dd>Optional list of domains whose subdomain structure will be stripped off in email addresses.</dd>
<dt><code>masquerade_exceptions (empty)</code></dt>
<dd>Optional list of user names that are not subjected to address masquerading, even when their address matches $masquerade_domains.</dd>
<dt><code>propagate_unmatched_extensions (canonical, virtual)</code></dt>
<dd>What address lookup tables copy an address extension from the lookup key to the lookup result.</dd></dl>
<p> Available before Postfix version 2.0:</p>
<dl>
<dt><code>virtual_maps (empty)</code></dt>
<dd>Optional lookup tables with a) names of domains for which all addresses are aliased to addresses in other local or remote domains, and b) addresses that are aliased to addresses in other local or remote domains.</dd></dl>
<p> Available in Postfix version 2.0 and later:</p>
<dl>
<dt><code>virtual_alias_maps ($virtual_maps)</code></dt>
<dd>Optional lookup tables that alias specific mail addresses or domains to other local or remote address.</dd></dl>
<p> Available in Postfix version 2.2 and later:</p>
<dl>
<dt><code>canonical_classes (envelope_sender, envelope_recipient, header_sender, header_recipient)</code></dt>
<dd>What addresses are subject to canonical_maps address mapping.</dd>
<dt><code>recipient_canonical_classes (envelope_recipient, header_recipient)</code></dt>
<dd>What addresses are subject to recipient_canonical_maps address mapping.</dd>
<dt><code>sender_canonical_classes (envelope_sender, header_sender)</code></dt>
<dd>What addresses are subject to sender_canonical_maps address mapping.</dd>
<dt><code>remote_header_rewrite_domain (empty)</code></dt>
<dd>Don&#8217;t rewrite message headers from remote clients at all when this parameter is empty; otherwise, rewrite message headers and append the specified domain name to incomplete addresses.</dd></dl>
<h2>Resource And Rate Controls</h2>
<dl>
<dt><code>duplicate_filter_limit (1000)</code></dt>
<dd>The maximal number of addresses remembered by the address duplicate filter for <code><a href="/docs/linux/man/5-aliases/">aliases</a></code>(5) or <code><a href="/docs/linux/man/5-virtual/">virtual</a></code>(5) alias expansion, or for <code><a href="/docs/linux/man/8-showq/">showq</a></code>(8) queue displays.</dd>
<dt><code>header_size_limit (102400)</code></dt>
<dd>The maximal amount of memory in bytes for storing a message header.</dd>
<dt><code>hopcount_limit (50)</code></dt>
<dd>The maximal number of Received: message headers that is allowed in the primary message headers.</dd>
<dt><code>in_flow_delay (1s)</code></dt>
<dd>Time to pause before accepting a new message, when the message arrival rate exceeds the message delivery rate.</dd>
<dt><code>message_size_limit (10240000)</code></dt>
<dd>The maximal size in bytes of a message, including envelope information.</dd></dl>
<p> Available in Postfix version 2.0 and later:</p>
<dl>
<dt><code>header_address_token_limit (10240)</code></dt>
<dd>The maximal number of address tokens are allowed in an address message header.</dd>
<dt><code>mime_boundary_length_limit (2048)</code></dt>
<dd>The maximal length of MIME multipart boundary strings.</dd>
<dt><code>mime_nesting_limit (100)</code></dt>
<dd>The maximal recursion level that the MIME processor will handle.</dd>
<dt><code>queue_file_attribute_count_limit (100)</code></dt>
<dd>The maximal number of (name=value) attributes that may be stored in a Postfix queue file.</dd></dl>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>virtual_alias_expansion_limit (1000)</code></dt>
<dd>The maximal number of addresses that virtual alias expansion produces from each original recipient.</dd>
<dt><code>virtual_alias_recursion_limit (1000)</code></dt>
<dd>The maximal nesting depth of virtual alias expansion.</dd></dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</dd>
<dt><code>daemon_timeout (18000s)</code></dt>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</dd>
<dt><code>delay_logging_resolution_limit (2)</code></dt>
<dd>The maximal number of digits after the decimal point when logging sub-second delay values.</dd>
<dt><code>delay_warning_time (0h)</code></dt>
<dd>The time after which the sender receives a copy of the message headers of mail that is still queued.</dd>
<dt><code>ipc_timeout (3600s)</code></dt>
<dd>The time limit for sending or receiving information over an internal communication channel.</dd>
<dt><code>max_idle (100s)</code></dt>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</dd>
<dt><code>max_use (100)</code></dt>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</dd>
<dt><code>myhostname (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>The internet hostname of this mail system.</dd>
<dt><code>myorigin ($myhostname)</code></dt>
<dd>The domain name that locally-posted mail appears to come from, and that locally posted mail is delivered to.</dd>
<dt><code>process_id (read-only)</code></dt>
<dd>The process ID of a Postfix command or daemon process.</dd>
<dt><code>process_name (read-only)</code></dt>
<dd>The process name of a Postfix command or daemon process.</dd>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>The location of the Postfix top-level queue directory.</dd>
<dt><code>soft_bounce (no)</code></dt>
<dd>Safety net to keep mail queued that would otherwise be returned to the sender.</dd>
<dt><code>syslog_facility (mail)</code></dt>
<dd>The syslog facility of Postfix logging.</dd>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></dt>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dd></dl>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>enable_original_recipient (yes)</code></dt>
<dd>Enable support for the X-Original-To message header.</dd></dl>
<h2>Files</h2>
<pre>/etc/postfix/canonical*, canonical mapping table
/etc/postfix/virtual*, virtual mapping table</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a>(8), address rewriting
<a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), queue manager
<a href="//www.systutorials.com/docs/linux/man/5-header_checks/">header_checks</a>(5), message header content inspection
<a href="//www.systutorials.com/docs/linux/man/5-body_checks/">body_checks</a>(5), body parts content inspection
<a href="//www.systutorials.com/docs/linux/man/5-canonical/">canonical</a>(5), canonical address lookup table format
<a href="//www.systutorials.com/docs/linux/man/5-virtual/">virtual</a>(5), virtual alias lookup table format
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), generic daemon options
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
syslogd(8), system logging</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>ADDRESS_REWRITING_README Postfix address manipulation
CONTENT_INSPECTION_README content inspection</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
