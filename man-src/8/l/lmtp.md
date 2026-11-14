---
title: "lmtp(8)"
name: "lmtp"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lmtp/"
description: "smtp – Postfix SMTP+LMTP client"
---

<p>smtp &#8211; Postfix SMTP+LMTP client</p>
<h2>Synopsis</h2>
<pre><code>smtp</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The Postfix SMTP+LMTP client implements the SMTP and LMTP mail delivery protocols. It processes message delivery requests from the queue manager. Each request specifies a queue file, a sender address, a domain or host to deliver to, and recipient information. This program expects to be run from the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) process manager. </p>
<p> The SMTP+LMTP client updates the queue file and marks recipients as finished, or it informs the queue manager that delivery should be tried again at a later time. Delivery status reports are sent to the <code><a href="/docs/linux/man/8-bounce/">bounce</a></code>(8), <code><a href="/docs/linux/man/8-defer/">defer</a></code>(8) or <code><a href="/docs/linux/man/8-trace/">trace</a></code>(8) daemon as appropriate. </p>
<p> The SMTP+LMTP client looks up a list of mail exchanger addresses for the destination host, sorts the list by preference, and connects to each listed address until it finds a server that responds. </p>
<p> When a server is not reachable, or when mail delivery fails due to a recoverable error condition, the SMTP+LMTP client will try to deliver the mail to an alternate host. </p>
<p> After a successful mail transaction, a connection may be saved to the <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) connection cache server, so that it may be used by any SMTP+LMTP client for a subsequent transaction. </p>
<p> By default, connection caching is enabled temporarily for destinations that have a high volume of mail in the active queue. Connection caching can be enabled permanently for specific destinations.</p>
<h2>Smtp Destination Syntax</h2>
<p>SMTP destinations have the following form:</p>
<dl>
<dt><i>domainname</i></p>
<dd>
<dt><i>domainname</i>:<i>port</i></p>
<dd>Look up the mail exchangers for the specified domain, and connect to the specified port (default: <code>smtp</code>).</p>
<dt>[<i>hostname</i>]</p>
<dd>
<dt>[<i>hostname</i>]:<i>port</i></p>
<dd>Look up the address(es) of the specified host, and connect to the specified port (default: <code>smtp</code>).</p>
<dt>[<i>address</i>]</p>
<dd>
<dt>[<i>address</i>]:<i>port</i></p>
<dd>Connect to the host at the specified address, and connect to the specified port (default: <code>smtp</code>). An IPv6 address must be formatted as [<code>ipv6</code>:<i>address</i>].</dl>
<h2>Lmtp Destination Syntax</h2>
<p>LMTP destinations have the following form:</p>
<dl>
<dt><code>unix</code>:<i>pathname</i></p>
<dd>Connect to the local UNIX-domain server that is bound to the specified <i>pathname</i>. If the process runs chrooted, an absolute pathname is interpreted relative to the Postfix queue directory.</p>
<dt><code>inet</code>:<i>hostname</i></p>
<dd>
<dt><code>inet:</code><i>hostname</i>:<i>port</i></p>
<dd>
<dt><code>inet</code>:[<i>address</i>]</p>
<dd>
<dt><code>inet</code>:[<i>address</i>]:<i>port</i></p>
<dd>Connect to the specified TCP port on the specified local or remote host. If no port is specified, connect to the port defined as <code>lmtp</code> in <code><a href="/docs/linux/man/4-services/">services</a></code>(4). If no such service is found, the <code>lmtp_tcp_port</code> configuration parameter (default value of 24) will be used. An IPv6 address must be formatted as [<code>ipv6</code>:<i>address</i>].</dl>
<h2>Security</h2>
<p>The SMTP+LMTP client is moderately security-sensitive. It talks to SMTP or LMTP servers and to DNS servers on the network. The SMTP+LMTP client can be run chrooted at fixed low privilege.</p>
<h2>Standards</h2>
<pre>RFC 821 (SMTP protocol)
RFC 822 (ARPA Internet Text Messages)
RFC 1651 (SMTP service extensions)
RFC 1652 (8bit-MIME transport)
RFC 1870 (Message Size Declaration)
RFC 2033 (LMTP protocol)
RFC 2034 (SMTP Enhanced Error Codes)
RFC 2045 (MIME: Format of Internet Message Bodies)
RFC 2046 (MIME: Media Types)
RFC 2554 (AUTH command)
RFC 2821 (SMTP protocol)
RFC 2920 (SMTP Pipelining)
RFC 3207 (STARTTLS command)
RFC 3461 (SMTP DSN Extension)
RFC 3463 (Enhanced Status Codes)
RFC 4954 (AUTH command)
RFC 5321 (SMTP protocol)</pre>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). Corrupted message files are marked so that the queue manager can move them to the <code>corrupt</code> queue for further inspection. </p>
<p> Depending on the setting of the <code>notify_classes</code> parameter, the postmaster is notified of bounces, protocol problems, and of other trouble.</p>
<h2>Bugs</h2>
<p>SMTP and LMTP connection caching does not work with TLS. The necessary support for TLS object passivation and re-activation does not exist without closing the session, which defeats the purpose. </p>
<p> SMTP and LMTP connection caching assumes that SASL credentials are valid for all destinations that map onto the same IP address and TCP port.</p>
<h2>Configuration Parameters</h2>
<p>Before Postfix version 2.3, the LMTP client is a separate program that implements only a subset of the functionality available with SMTP: there is no support for TLS, and connections are cached in-process, making it ineffective when the client is used for multiple domains. </p>
<p> Most smtp_<i>xxx</i> configuration parameters have an lmtp_<i>xxx</i> &quot;mirror&quot; parameter for the equivalent LMTP feature. This document describes only those LMTP-related parameters that aren&#8217;t simply &quot;mirror&quot; parameters. </p>
<p> Changes to <code>main.cf</code> are picked up automatically, as <code><a href="/docs/linux/man/8-smtp/">smtp</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Compatibility Controls</h2>
<dl>
<dt><code>ignore_mx_lookup_error (no)</code></p>
<dd>Ignore DNS MX lookups that produce no response.</p>
<dt><code>smtp_always_send_ehlo (yes)</code></p>
<dd>Always send EHLO at the start of an SMTP session.</p>
<dt><code>smtp_never_send_ehlo (no)</code></p>
<dd>Never send EHLO at the start of an SMTP session.</p>
<dt><code>smtp_defer_if_no_mx_address_found (no)</code></p>
<dd>Defer mail delivery when no MX record resolves to an IP address.</p>
<dt><code>smtp_line_length_limit (998)</code></p>
<dd>The maximal length of message header and body lines that Postfix will send via SMTP.</p>
<dt><code>smtp_pix_workaround_delay_time (10s)</code></p>
<dd>How long the Postfix SMTP client pauses before sending &quot;.&lt;CR&gt;&lt;LF&gt;&quot; in order to work around the PIX firewall &quot;&lt;CR&gt;&lt;LF&gt;.&lt;CR&gt;&lt;LF&gt;&quot; bug.</p>
<dt><code>smtp_pix_workaround_threshold_time (500s)</code></p>
<dd>How long a message must be queued before the Postfix SMTP client turns on the PIX firewall &quot;&lt;CR&gt;&lt;LF&gt;.&lt;CR&gt;&lt;LF&gt;&quot; bug workaround for delivery through firewalls with &quot;smtp fixup&quot; mode turned on.</p>
<dt><code>smtp_pix_workarounds (disable_esmtp, delay_dotcrlf)</code></p>
<dd>A list that specifies zero or more workarounds for CISCO PIX firewall bugs.</p>
<dt><code>smtp_pix_workaround_maps (empty)</code></p>
<dd>Lookup tables, indexed by the remote SMTP server address, with per-destination workarounds for CISCO PIX firewall bugs.</p>
<dt><code>smtp_quote_rfc821_envelope (yes)</code></p>
<dd>Quote addresses in Postfix SMTP client MAIL FROM and RCPT TO commands as required by RFC 5321.</p>
<dt><code>smtp_reply_filter (empty)</code></p>
<dd>A mechanism to transform replies from remote SMTP servers one line at a time.</p>
<dt><code>smtp_skip_5xx_greeting (yes)</code></p>
<dd>Skip remote SMTP servers that greet with a 5XX status code (go away, do not try again later).</p>
<dt><code>smtp_skip_quit_response (yes)</code></p>
<dd>Do not wait for the response to the SMTP QUIT command.</dl>
<p> Available in Postfix version 2.0 and earlier:</p>
<dl>
<dt><code>smtp_skip_4xx_greeting (yes)</code></p>
<dd>Skip SMTP servers that greet with a 4XX status code (go away, try again later).</dl>
<p> Available in Postfix version 2.2 and later:</p>
<dl>
<dt><code>smtp_discard_ehlo_keyword_address_maps (empty)</code></p>
<dd>Lookup tables, indexed by the remote SMTP server address, with case insensitive lists of EHLO keywords (pipelining, starttls, auth, etc.) that the Postfix SMTP client will ignore in the EHLO response from a remote SMTP server.</p>
<dt><code>smtp_discard_ehlo_keywords (empty)</code></p>
<dd>A case insensitive list of EHLO keywords (pipelining, starttls, auth, etc.) that the Postfix SMTP client will ignore in the EHLO response from a remote SMTP server.</p>
<dt><code>smtp_generic_maps (empty)</code></p>
<dd>Optional lookup tables that perform address rewriting in the Postfix SMTP client, typically to transform a locally valid address into a globally valid address when sending mail across the Internet.</dl>
<p> Available in Postfix version 2.2.9 and later:</p>
<dl>
<dt><code>smtp_cname_overrides_servername (version dependent)</code></p>
<dd>Allow DNS CNAME records to override the servername that the Postfix SMTP client uses for logging, SASL password lookup, TLS policy decisions, or TLS certificate verification.</dl>
<p> Available in Postfix version 2.3 and later:</p>
<dl>
<dt><code>lmtp_discard_lhlo_keyword_address_maps (empty)</code></p>
<dd>Lookup tables, indexed by the remote LMTP server address, with case insensitive lists of LHLO keywords (pipelining, starttls, auth, etc.) that the Postfix LMTP client will ignore in the LHLO response from a remote LMTP server.</p>
<dt><code>lmtp_discard_lhlo_keywords (empty)</code></p>
<dd>A case insensitive list of LHLO keywords (pipelining, starttls, auth, etc.) that the Postfix LMTP client will ignore in the LHLO response from a remote LMTP server.</dl>
<p> Available in Postfix version 2.4.4 and later:</p>
<dl>
<dt><code>send_cyrus_sasl_authzid (no)</code></p>
<dd>When authenticating to a remote SMTP or LMTP server with the default setting &quot;no&quot;, send no SASL authoriZation ID (authzid); send only the SASL authentiCation ID (authcid) plus the authcid&#8217;s password.</dl>
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><code>smtp_header_checks (empty)</code></p>
<dd>Restricted <code><a href="/docs/linux/man/5-header_checks/">header_checks</a></code>(5) tables for the Postfix SMTP client.</p>
<dt><code>smtp_mime_header_checks (empty)</code></p>
<dd>Restricted <code><a href="/docs/linux/man/5-mime_header_checks/">mime_header_checks</a></code>(5) tables for the Postfix SMTP client.</p>
<dt><code>smtp_nested_header_checks (empty)</code></p>
<dd>Restricted <code><a href="/docs/linux/man/5-nested_header_checks/">nested_header_checks</a></code>(5) tables for the Postfix SMTP client.</p>
<dt><code>smtp_body_checks (empty)</code></p>
<dd>Restricted <code><a href="/docs/linux/man/5-body_checks/">body_checks</a></code>(5) tables for the Postfix SMTP client.</dl>
<p> Available in Postfix version 2.6 and later:</p>
<dl>
<dt><code>tcp_windowsize (0)</code></p>
<dd>An optional workaround for routers that break TCP window scaling.</dl>
<p> Available in Postfix version 2.8 and later:</p>
<dl>
<dt><code>smtp_dns_resolver_options (empty)</code></p>
<dd>DNS Resolver options for the Postfix SMTP client.</dl>
<p> Available in Postfix version 2.9 and later:</p>
<dl>
<dt><code>smtp_per_record_deadline (no)</code></p>
<dd>Change the behavior of the smtp_*_timeout time limits, from a time limit per read or write system call, to a time limit to send or receive a complete record (an SMTP command line, SMTP response line, SMTP message content line, or TLS protocol message).</p>
<dt><code>smtp_send_dummy_mail_auth (no)</code></p>
<dd>Whether or not to append the &quot;AUTH=&lt;&gt;&quot; option to the MAIL FROM command in SASL-authenticated SMTP sessions.</dl>
<h2>Mime Processing Controls</h2>
<p>Available in Postfix version 2.0 and later:</p>
<dl>
<dt><code>disable_mime_output_conversion (no)</code></p>
<dd>Disable the conversion of 8BITMIME format to 7BIT format.</p>
<dt><code>mime_boundary_length_limit (2048)</code></p>
<dd>The maximal length of MIME multipart boundary strings.</p>
<dt><code>mime_nesting_limit (100)</code></p>
<dd>The maximal recursion level that the MIME processor will handle.</dl>
<h2>External Content Inspection Controls</h2>
<p>Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>smtp_send_xforward_command (no)</code></p>
<dd>Send the non-standard XFORWARD command when the Postfix SMTP server EHLO response announces XFORWARD support.</dl>
<h2>Sasl Authentication Controls</h2>
<dl>
<dt><code>smtp_sasl_auth_enable (no)</code></p>
<dd>Enable SASL authentication in the Postfix SMTP client.</p>
<dt><code>smtp_sasl_password_maps (empty)</code></p>
<dd>Optional Postfix SMTP client lookup tables with one username:password entry per remote hostname or domain, or sender address when sender-dependent authentication is enabled.</p>
<dt><code>smtp_sasl_security_options (noplaintext, noanonymous)</code></p>
<dd>Postfix SMTP client SASL security options; as of Postfix 2.3 the list of available features depends on the SASL client implementation that is selected with <code>smtp_sasl_type</code>.</dl>
<p> Available in Postfix version 2.2 and later:</p>
<dl>
<dt><code>smtp_sasl_mechanism_filter (empty)</code></p>
<dd>If non-empty, a Postfix SMTP client filter for the remote SMTP server&#8217;s list of offered SASL mechanisms.</dl>
<p> Available in Postfix version 2.3 and later:</p>
<dl>
<dt><code>smtp_sender_dependent_authentication (no)</code></p>
<dd>Enable sender-dependent authentication in the Postfix SMTP client; this is available only with SASL authentication, and disables SMTP connection caching to ensure that mail from different senders will use the appropriate credentials.</p>
<dt><code>smtp_sasl_path (empty)</code></p>
<dd>Implementation-specific information that the Postfix SMTP client passes through to the SASL plug-in implementation that is selected with <code>smtp_sasl_type</code>.</p>
<dt><code>smtp_sasl_type (cyrus)</code></p>
<dd>The SASL plug-in type that the Postfix SMTP client should use for authentication.</dl>
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><code>smtp_sasl_auth_cache_name (empty)</code></p>
<dd>An optional table to prevent repeated SASL authentication failures with the same remote SMTP server hostname, username and password.</p>
<dt><code>smtp_sasl_auth_cache_time (90d)</code></p>
<dd>The maximal age of an smtp_sasl_auth_cache_name entry before it is removed.</p>
<dt><code>smtp_sasl_auth_soft_bounce (yes)</code></p>
<dd>When a remote SMTP server rejects a SASL authentication request with a 535 reply code, defer mail delivery instead of returning mail as undeliverable.</dl>
<p> Available in Postfix version 2.9 and later:</p>
<dl>
<dt><code>smtp_send_dummy_mail_auth (no)</code></p>
<dd>Whether or not to append the &quot;AUTH=&lt;&gt;&quot; option to the MAIL FROM command in SASL-authenticated SMTP sessions.</dl>
<h2>Starttls Support Controls</h2>
<p>Detailed information about STARTTLS configuration may be found in the TLS_README document.</p>
<dl>
<dt><code>smtp_tls_security_level (empty)</code></p>
<dd>The default SMTP TLS security level for the Postfix SMTP client; when a non-empty value is specified, this overrides the obsolete parameters smtp_use_tls, smtp_enforce_tls, and smtp_tls_enforce_peername.</p>
<dt><code>smtp_sasl_tls_security_options ($smtp_sasl_security_options)</code></p>
<dd>The SASL authentication security options that the Postfix SMTP client uses for TLS encrypted SMTP sessions.</p>
<dt><code>smtp_starttls_timeout (300s)</code></p>
<dd>Time limit for Postfix SMTP client write and read operations during TLS startup and shutdown handshake procedures.</p>
<dt><code>smtp_tls_CAfile (empty)</code></p>
<dd>A file containing CA certificates of root CAs trusted to sign either remote SMTP server certificates or intermediate CA certificates.</p>
<dt><code>smtp_tls_CApath (empty)</code></p>
<dd>Directory with PEM format certificate authority certificates that the Postfix SMTP client uses to verify a remote SMTP server certificate.</p>
<dt><code>smtp_tls_cert_file (empty)</code></p>
<dd>File with the Postfix SMTP client RSA certificate in PEM format.</p>
<dt><code>smtp_tls_mandatory_ciphers (medium)</code></p>
<dd>The minimum TLS cipher grade that the Postfix SMTP client will use with mandatory TLS encryption.</p>
<dt><code>smtp_tls_exclude_ciphers (empty)</code></p>
<dd>List of ciphers or cipher types to exclude from the Postfix SMTP client cipher list at all TLS security levels.</p>
<dt><code>smtp_tls_mandatory_exclude_ciphers (empty)</code></p>
<dd>Additional list of ciphers or cipher types to exclude from the Postfix SMTP client cipher list at mandatory TLS security levels.</p>
<dt><code>smtp_tls_dcert_file (empty)</code></p>
<dd>File with the Postfix SMTP client DSA certificate in PEM format.</p>
<dt><code>smtp_tls_dkey_file ($smtp_tls_dcert_file)</code></p>
<dd>File with the Postfix SMTP client DSA private key in PEM format.</p>
<dt><code>smtp_tls_key_file ($smtp_tls_cert_file)</code></p>
<dd>File with the Postfix SMTP client RSA private key in PEM format.</p>
<dt><code>smtp_tls_loglevel (0)</code></p>
<dd>Enable additional Postfix SMTP client logging of TLS activity.</p>
<dt><code>smtp_tls_note_starttls_offer (no)</code></p>
<dd>Log the hostname of a remote SMTP server that offers STARTTLS, when TLS is not already enabled for that server.</p>
<dt><code>smtp_tls_policy_maps (empty)</code></p>
<dd>Optional lookup tables with the Postfix SMTP client TLS security policy by next-hop destination; when a non-empty value is specified, this overrides the obsolete smtp_tls_per_site parameter.</p>
<dt><code>smtp_tls_mandatory_protocols (!SSLv2)</code></p>
<dd>List of SSL/TLS protocols that the Postfix SMTP client will use with mandatory TLS encryption.</p>
<dt><code>smtp_tls_scert_verifydepth (9)</code></p>
<dd>The verification depth for remote SMTP server certificates.</p>
<dt><code>smtp_tls_secure_cert_match (nexthop, dot-nexthop)</code></p>
<dd>How the Postfix SMTP client verifies the server certificate peername for the &quot;secure&quot; TLS security level.</p>
<dt><code>smtp_tls_session_cache_database (empty)</code></p>
<dd>Name of the file containing the optional Postfix SMTP client TLS session cache.</p>
<dt><code>smtp_tls_session_cache_timeout (3600s)</code></p>
<dd>The expiration time of Postfix SMTP client TLS session cache information.</p>
<dt><code>smtp_tls_verify_cert_match (hostname)</code></p>
<dd>How the Postfix SMTP client verifies the server certificate peername for the &quot;verify&quot; TLS security level.</p>
<dt><code>tls_daemon_random_bytes (32)</code></p>
<dd>The number of pseudo-random bytes that an <code><a href="/docs/linux/man/8-smtp/">smtp</a></code>(8) or <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) process requests from the <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) server in order to seed its internal pseudo random number generator (PRNG).</p>
<dt><code>tls_high_cipherlist (ALL:!EXPORT:!LOW:!MEDIUM:+RC4:@STRENGTH)</code></p>
<dd>The OpenSSL cipherlist for &quot;HIGH&quot; grade ciphers.</p>
<dt><code>tls_medium_cipherlist (ALL:!EXPORT:!LOW:+RC4:@STRENGTH)</code></p>
<dd>The OpenSSL cipherlist for &quot;MEDIUM&quot; or higher grade ciphers.</p>
<dt><code>tls_low_cipherlist (ALL:!EXPORT:+RC4:@STRENGTH)</code></p>
<dd>The OpenSSL cipherlist for &quot;LOW&quot; or higher grade ciphers.</p>
<dt><code>tls_export_cipherlist (ALL:+RC4:@STRENGTH)</code></p>
<dd>The OpenSSL cipherlist for &quot;EXPORT&quot; or higher grade ciphers.</p>
<dt><code>tls_null_cipherlist (eNULL:!aNULL)</code></p>
<dd>The OpenSSL cipherlist for &quot;NULL&quot; grade ciphers that provide authentication without encryption.</dl>
<p> Available in Postfix version 2.4 and later:</p>
<dl>
<dt><code>smtp_sasl_tls_verified_security_options ($smtp_sasl_tls_security_options)</code></p>
<dd>The SASL authentication security options that the Postfix SMTP client uses for TLS encrypted SMTP sessions with a verified server certificate.</dl>
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><code>smtp_tls_fingerprint_cert_match (empty)</code></p>
<dd>List of acceptable remote SMTP server certificate fingerprints for the &quot;fingerprint&quot; TLS security level (<code>smtp_tls_security_level</code> = fingerprint).</p>
<dt><code>smtp_tls_fingerprint_digest (md5)</code></p>
<dd>The message digest algorithm used to construct remote SMTP server certificate fingerprints.</dl>
<p> Available in Postfix version 2.6 and later:</p>
<dl>
<dt><code>smtp_tls_protocols (!SSLv2)</code></p>
<dd>List of TLS protocols that the Postfix SMTP client will exclude or include with opportunistic TLS encryption.</p>
<dt><code>smtp_tls_ciphers (export)</code></p>
<dd>The minimum TLS cipher grade that the Postfix SMTP client will use with opportunistic TLS encryption.</p>
<dt><code>smtp_tls_eccert_file (empty)</code></p>
<dd>File with the Postfix SMTP client ECDSA certificate in PEM format.</p>
<dt><code>smtp_tls_eckey_file ($smtp_tls_eccert_file)</code></p>
<dd>File with the Postfix SMTP client ECDSA private key in PEM format.</dl>
<p> Available in Postfix version 2.7 and later:</p>
<dl>
<dt><code>smtp_tls_block_early_mail_reply (no)</code></p>
<dd>Try to detect a mail hijacking attack based on a TLS protocol vulnerability (CVE-2009-3555), where an attacker prepends malicious HELO, MAIL, RCPT, DATA commands to a Postfix SMTP client TLS session.</dl>
<p> Available in Postfix version 2.8 and later:</p>
<dl>
<dt><code>tls_disable_workarounds (see &#8216;postconf -d&#8217; output)</code></p>
<dd>List or bit-mask of OpenSSL bug work-arounds to disable.</dl>
<h2>Obsolete Starttls Controls</h2>
<p>The following configuration parameters exist for compatibility with Postfix versions before 2.3. Support for these will be removed in a future release.</p>
<dl>
<dt><code>smtp_use_tls (no)</code></p>
<dd>Opportunistic mode: use TLS when a remote SMTP server announces STARTTLS support, otherwise send the mail in the clear.</p>
<dt><code>smtp_enforce_tls (no)</code></p>
<dd>Enforcement mode: require that remote SMTP servers use TLS encryption, and never send mail in the clear.</p>
<dt><code>smtp_tls_enforce_peername (yes)</code></p>
<dd>With mandatory TLS encryption, require that the remote SMTP server hostname matches the information in the remote SMTP server certificate.</p>
<dt><code>smtp_tls_per_site (empty)</code></p>
<dd>Optional lookup tables with the Postfix SMTP client TLS usage policy by next-hop destination and by remote SMTP server hostname.</p>
<dt><code>smtp_tls_cipherlist (empty)</code></p>
<dd>Obsolete Postfix &lt; 2.3 control for the Postfix SMTP client TLS cipher list.</dl>
<h2>Resource And Rate Controls</h2>
<dl>
<dt><code>smtp_destination_concurrency_limit ($default_destination_concurrency_limit)</code></p>
<dd>The maximal number of parallel deliveries to the same destination via the smtp message delivery transport.</p>
<dt><code>smtp_destination_recipient_limit ($default_destination_recipient_limit)</code></p>
<dd>The maximal number of recipients per message for the smtp message delivery transport.</p>
<dt><code>smtp_connect_timeout (30s)</code></p>
<dd>The Postfix SMTP client time limit for completing a TCP connection, or zero (use the operating system built-in time limit).</p>
<dt><code>smtp_helo_timeout (300s)</code></p>
<dd>The Postfix SMTP client time limit for sending the HELO or EHLO command, and for receiving the initial remote SMTP server response.</p>
<dt><code>lmtp_lhlo_timeout (300s)</code></p>
<dd>The Postfix LMTP client time limit for sending the LHLO command, and for receiving the initial remote LMTP server response.</p>
<dt><code>smtp_xforward_timeout (300s)</code></p>
<dd>The Postfix SMTP client time limit for sending the XFORWARD command, and for receiving the remote SMTP server response.</p>
<dt><code>smtp_mail_timeout (300s)</code></p>
<dd>The Postfix SMTP client time limit for sending the MAIL FROM command, and for receiving the remote SMTP server response.</p>
<dt><code>smtp_rcpt_timeout (300s)</code></p>
<dd>The Postfix SMTP client time limit for sending the SMTP RCPT TO command, and for receiving the remote SMTP server response.</p>
<dt><code>smtp_data_init_timeout (120s)</code></p>
<dd>The Postfix SMTP client time limit for sending the SMTP DATA command, and for receiving the remote SMTP server response.</p>
<dt><code>smtp_data_xfer_timeout (180s)</code></p>
<dd>The Postfix SMTP client time limit for sending the SMTP message content.</p>
<dt><code>smtp_data_done_timeout (600s)</code></p>
<dd>The Postfix SMTP client time limit for sending the SMTP &quot;.&quot;, and for receiving the remote SMTP server response.</p>
<dt><code>smtp_quit_timeout (300s)</code></p>
<dd>The Postfix SMTP client time limit for sending the QUIT command, and for receiving the remote SMTP server response.</dl>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>smtp_mx_address_limit (5)</code></p>
<dd>The maximal number of MX (mail exchanger) IP addresses that can result from Postfix SMTP client mail exchanger lookups, or zero (no limit).</p>
<dt><code>smtp_mx_session_limit (2)</code></p>
<dd>The maximal number of SMTP sessions per delivery request before the Postfix SMTP client gives up or delivers to a fall-back relay host, or zero (no limit).</p>
<dt><code>smtp_rset_timeout (20s)</code></p>
<dd>The Postfix SMTP client time limit for sending the RSET command, and for receiving the remote SMTP server response.</dl>
<p> Available in Postfix version 2.2 and earlier:</p>
<dl>
<dt><code>lmtp_cache_connection (yes)</code></p>
<dd>Keep Postfix LMTP client connections open for up to $max_idle seconds.</dl>
<p> Available in Postfix version 2.2 and later:</p>
<dl>
<dt><code>smtp_connection_cache_destinations (empty)</code></p>
<dd>Permanently enable SMTP connection caching for the specified destinations.</p>
<dt><code>smtp_connection_cache_on_demand (yes)</code></p>
<dd>Temporarily enable SMTP connection caching while a destination has a high volume of mail in the active queue.</p>
<dt><code>smtp_connection_reuse_time_limit (300s)</code></p>
<dd>The amount of time during which Postfix will use an SMTP connection repeatedly.</p>
<dt><code>smtp_connection_cache_time_limit (2s)</code></p>
<dd>When SMTP connection caching is enabled, the amount of time that an unused SMTP client socket is kept open before it is closed.</dl>
<p> Available in Postfix version 2.3 and later:</p>
<dl>
<dt><code>connection_cache_protocol_timeout (5s)</code></p>
<dd>Time limit for connection cache connect, send or receive operations.</dl>
<p> Available in Postfix version 2.9 and later:</p>
<dl>
<dt><code>smtp_per_record_deadline (no)</code></p>
<dd>Change the behavior of the smtp_*_timeout time limits, from a time limit per read or write system call, to a time limit to send or receive a complete record (an SMTP command line, SMTP response line, SMTP message content line, or TLS protocol message).</dl>
<h2>Trouble Shooting Controls</h2>
<dl>
<dt><code>debug_peer_level (2)</code></p>
<dd>The increment in verbose logging level when a remote client or server matches a pattern in the debug_peer_list parameter.</p>
<dt><code>debug_peer_list (empty)</code></p>
<dd>Optional list of remote client or server hostname or network address patterns that cause the verbose logging level to increase by the amount specified in $debug_peer_level.</p>
<dt><code>error_notice_recipient (postmaster)</code></p>
<dd>The recipient of postmaster notifications about mail delivery problems that are caused by policy, resource, software or protocol errors.</p>
<dt><code>internal_mail_filter_classes (empty)</code></p>
<dd>What categories of Postfix-generated mail are subject to before-queue content inspection by non_smtpd_milters, header_checks and body_checks.</p>
<dt><code>notify_classes (resource, software)</code></p>
<dd>The list of error classes that are reported to the postmaster.</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>best_mx_transport (empty)</code></p>
<dd>Where the Postfix SMTP client should deliver mail when it detects a &quot;mail loops back to myself&quot; error condition.</p>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>delay_logging_resolution_limit (2)</code></p>
<dd>The maximal number of digits after the decimal point when logging sub-second delay values.</p>
<dt><code>disable_dns_lookups (no)</code></p>
<dd>Disable DNS lookups in the Postfix SMTP and LMTP clients.</p>
<dt><code>inet_interfaces (all)</code></p>
<dd>The network interface addresses that this mail system receives mail on.</p>
<dt><code>inet_protocols (all)</code></p>
<dd>The Internet protocols Postfix will attempt to use when making or accepting connections.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
<dt><code>lmtp_assume_final (no)</code></p>
<dd>When a remote LMTP server announces no DSN support, assume that the server performs final delivery, and send &quot;delivered&quot; delivery status notifications instead of &quot;relayed&quot;.</p>
<dt><code>lmtp_tcp_port (24)</code></p>
<dd>The default TCP port that the Postfix LMTP client connects to.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>max_use (100)</code></p>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>proxy_interfaces (empty)</code></p>
<dd>The network interface addresses that this mail system receives mail on by way of a proxy or network address translation unit.</p>
<dt><code>smtp_address_preference (any)</code></p>
<dd>The address type (&quot;ipv6&quot;, &quot;ipv4&quot; or &quot;any&quot;) that the Postfix SMTP client will try first, when a destination has IPv6 and IPv4 addresses with equal MX preference.</p>
<dt><code>smtp_bind_address (empty)</code></p>
<dd>An optional numerical network address that the Postfix SMTP client should bind to when making an IPv4 connection.</p>
<dt><code>smtp_bind_address6 (empty)</code></p>
<dd>An optional numerical network address that the Postfix SMTP client should bind to when making an IPv6 connection.</p>
<dt><code>smtp_helo_name ($myhostname)</code></p>
<dd>The hostname to send in the SMTP EHLO or HELO command.</p>
<dt><code>lmtp_lhlo_name ($myhostname)</code></p>
<dd>The hostname to send in the LMTP LHLO command.</p>
<dt><code>smtp_host_lookup (dns)</code></p>
<dd>What mechanisms the Postfix SMTP client uses to look up a host&#8217;s IP address.</p>
<dt><code>smtp_randomize_addresses (yes)</code></p>
<dd>Randomize the order of equal-preference MX host addresses.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<p> Available with Postfix 2.2 and earlier:</p>
<dl>
<dt><code>fallback_relay (empty)</code></p>
<dd>Optional list of relay hosts for SMTP destinations that can&#8217;t be found or that are unreachable.</dl>
<p> Available with Postfix 2.3 and later:</p>
<dl>
<dt><code>smtp_fallback_relay ($fallback_relay)</code></p>
<dd>Optional list of relay hosts for SMTP destinations that can&#8217;t be found or that are unreachable.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/5-generic/">generic</a>(5), output address rewriting
<a href="//www.systutorials.com/docs/linux/man/5-header_checks/">header_checks</a>(5), message header content inspection
<a href="//www.systutorials.com/docs/linux/man/5-body_checks/">body_checks</a>(5), body parts content inspection
<a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), queue manager
<a href="//www.systutorials.com/docs/linux/man/8-bounce/">bounce</a>(8), delivery status reports
<a href="//www.systutorials.com/docs/linux/man/8-scache/">scache</a>(8), connection cache server
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), generic daemon options
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/8-tlsmgr/">tlsmgr</a>(8), TLS session and PRNG management
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>SASL_README, Postfix SASL howto
TLS_README, Postfix STARTTLS howto</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Command pipelining in cooperation with:
Jon Ribbens
Oaktree Internet Solutions Ltd.,
Internet House,
Canal Basin,
Coventry,
CV1 4LY, United Kingdom.
SASL support originally by:
Till Franke
SuSE Rhein/Main AG
65760 Eschborn, Germany
TLS support originally by:
Lutz Jaenicke
BTU Cottbus
Allgemeine Elektrotechnik
Universitaetsplatz 3-4
D-03044 Cottbus, Germany
Revised TLS and SMTP connection cache support by:
Victor Duchovni
Morgan Stanley</pre>
