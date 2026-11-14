---
title: "smtpd(8)"
name: "smtpd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smtpd/"
description: "smtpd – Postfix SMTP server"
---

<p>smtpd &#8211; Postfix SMTP server</p>
<h2>Synopsis</h2>
<pre><code>smtpd</code> [generic Postfix daemon options]
<code>sendmail -bs</code></pre>
<h2>Description</h2>
<p>The SMTP server accepts network connection requests and performs zero or more SMTP transactions per connection. Each received message is piped through the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon, and is placed into the <code>incoming</code> queue as one single queue file. For this mode of operation, the program expects to be run from the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) process manager. </p>
<p> Alternatively, the SMTP server be can run in stand-alone mode; this is traditionally obtained with &quot;<code>sendmail -bs</code>&quot;. When the SMTP server runs stand-alone with non $<code>mail_owner</code> privileges, it receives mail even while the mail system is not running, deposits messages directly into the <code>maildrop</code> queue, and disables the SMTP server&#8217;s access policies. As of Postfix version 2.3, the SMTP server refuses to receive mail from the network when it runs with non $<code>mail_owner</code> privileges. </p>
<p> The SMTP server implements a variety of policies for connection requests, and for parameters given to <code>HELO, ETRN, MAIL FROM, VRFY</code> and <code>RCPT TO</code> commands. They are detailed below and in the <code>main.cf</code> configuration file.</p>
<h2>Security</h2>
<p>The SMTP server is moderately security-sensitive. It talks to SMTP clients and to DNS servers on the network. The SMTP server can be run chrooted at fixed low privilege.</p>
<h2>Standards</h2>
<pre>RFC 821 (SMTP protocol)
RFC 1123 (Host requirements)
RFC 1652 (8bit-MIME transport)
RFC 1869 (SMTP service extensions)
RFC 1870 (Message size declaration)
RFC 1985 (ETRN command)
RFC 2034 (SMTP enhanced status codes)
RFC 2554 (AUTH command)
RFC 2821 (SMTP protocol)
RFC 2920 (SMTP pipelining)
RFC 3207 (STARTTLS command)
RFC 3461 (SMTP DSN extension)
RFC 3463 (Enhanced status codes)
RFC 3848 (ESMTP transmission types)
RFC 4409 (Message submission)
RFC 4954 (AUTH command)
RFC 5321 (SMTP protocol)</pre>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). </p>
<p> Depending on the setting of the <code>notify_classes</code> parameter, the postmaster is notified of bounces, protocol problems, policy violations, and of other trouble.</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are picked up automatically, as <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Compatibility Controls</h2>
<p>The following parameters work around implementation errors in other software, and/or allow you to override standards in order to prevent undesirable use.</p>
<dl>
<dt><code>broken_sasl_auth_clients (no)</code></p>
<dd>Enable inter-operability with remote SMTP clients that implement an obsolete version of the AUTH command (RFC 4954).</p>
<dt><code>disable_vrfy_command (no)</code></p>
<dd>Disable the SMTP VRFY command.</p>
<dt><code>smtpd_noop_commands (empty)</code></p>
<dd>List of commands that the Postfix SMTP server replies to with &quot;250 Ok&quot;, without doing any syntax checks and without changing state.</p>
<dt><code>strict_rfc821_envelopes (no)</code></p>
<dd>Require that addresses received in SMTP MAIL FROM and RCPT TO commands are enclosed with &lt;&gt;, and that those addresses do not contain RFC 822 style comments or phrases.</dl>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>resolve_null_domain (no)</code></p>
<dd>Resolve an address that ends in the &quot;@&quot; null domain as if the local hostname were specified, instead of rejecting the address as invalid.</p>
<dt><code>smtpd_reject_unlisted_sender (no)</code></p>
<dd>Request that the Postfix SMTP server rejects mail from unknown sender addresses, even when no explicit reject_unlisted_sender access restriction is specified.</p>
<dt><code>smtpd_sasl_exceptions_networks (empty)</code></p>
<dd>What remote SMTP clients the Postfix SMTP server will not offer AUTH support to.</dl>
<p> Available in Postfix version 2.2 and later:</p>
<dl>
<dt><code>smtpd_discard_ehlo_keyword_address_maps (empty)</code></p>
<dd>Lookup tables, indexed by the remote SMTP client address, with case insensitive lists of EHLO keywords (pipelining, starttls, auth, etc.) that the Postfix SMTP server will not send in the EHLO response to a remote SMTP client.</p>
<dt><code>smtpd_discard_ehlo_keywords (empty)</code></p>
<dd>A case insensitive list of EHLO keywords (pipelining, starttls, auth, etc.) that the Postfix SMTP server will not send in the EHLO response to a remote SMTP client.</p>
<dt><code>smtpd_delay_open_until_valid_rcpt (yes)</code></p>
<dd>Postpone the start of an SMTP mail transaction until a valid RCPT TO command is received.</dl>
<p> Available in Postfix version 2.3 and later:</p>
<dl>
<dt><code>smtpd_tls_always_issue_session_ids (yes)</code></p>
<dd>Force the Postfix SMTP server to issue a TLS session id, even when TLS session caching is turned off (smtpd_tls_session_cache_database is empty).</dl>
<p> Available in Postfix version 2.6 and later:</p>
<dl>
<dt><code>tcp_windowsize (0)</code></p>
<dd>An optional workaround for routers that break TCP window scaling.</dl>
<p> Available in Postfix version 2.7 and later:</p>
<dl>
<dt><code>smtpd_command_filter (empty)</code></p>
<dd>A mechanism to transform commands from remote SMTP clients.</dl>
<p> Available in Postfix version 2.9 and later:</p>
<dl>
<dt><code>smtpd_per_record_deadline (normal: no, overload: yes)</code></p>
<dd>Change the behavior of the smtpd_timeout time limit, from a time limit per read or write system call, to a time limit to send or receive a complete record (an SMTP command line, SMTP response line, SMTP message content line, or TLS protocol message).</dl>
<h2>Address Rewriting Controls</h2>
<p>See the ADDRESS_REWRITING_README document for a detailed discussion of Postfix address rewriting.</p>
<dl>
<dt><code>receive_override_options (empty)</code></p>
<dd>Enable or disable recipient validation, built-in content filtering, or address mapping.</dl>
<p> Available in Postfix version 2.2 and later:</p>
<dl>
<dt><code>local_header_rewrite_clients (permit_inet_interfaces)</code></p>
<dd>Rewrite message header addresses in mail from these clients and update incomplete addresses with the domain name in $myorigin or $mydomain; either don&#8217;t rewrite message headers from other clients at all, or rewrite message headers and update incomplete addresses with the domain specified in the remote_header_rewrite_domain parameter.</dl>
<h2>Before-Smtpd Proxy Agent</h2>
<p>Available in Postfix version 2.10 and later:</p>
<dl>
<dt><code>smtpd_upstream_proxy_protocol (empty)</code></p>
<dd>The name of the proxy protocol used by an optional before-smtpd proxy agent.</p>
<dt><code>smtpd_upstream_proxy_timeout (5s)</code></p>
<dd>The time limit for the proxy protocol specified with the smtpd_upstream_proxy_protocol parameter.</dl>
<h2>After Queue External Content Inspection Controls</h2>
<p>As of version 1.0, Postfix can be configured to send new mail to an external content filter AFTER the mail is queued. This content filter is expected to inject mail back into a (Postfix or other) MTA for further delivery. See the FILTER_README document for details.</p>
<dl>
<dt><code>content_filter (empty)</code></p>
<dd>After the message is queued, send the entire message to the specified <i>transport:destination</i>.</dl>
<h2>Before Queue External Content Inspection Controls</h2>
<p>As of version 2.1, the Postfix SMTP server can be configured to send incoming mail to a real-time SMTP-based content filter BEFORE mail is queued. This content filter is expected to inject mail back into Postfix. See the SMTPD_PROXY_README document for details on how to configure and operate this feature.</p>
<dl>
<dt><code>smtpd_proxy_filter (empty)</code></p>
<dd>The hostname and TCP port of the mail filtering proxy server.</p>
<dt><code>smtpd_proxy_ehlo ($myhostname)</code></p>
<dd>How the Postfix SMTP server announces itself to the proxy filter.</p>
<dt><code>smtpd_proxy_options (empty)</code></p>
<dd>List of options that control how the Postfix SMTP server communicates with a before-queue content filter.</p>
<dt><code>smtpd_proxy_timeout (100s)</code></p>
<dd>The time limit for connecting to a proxy filter and for sending or receiving information.</dl>
<h2>Before Queue Milter Controls</h2>
<p>As of version 2.3, Postfix supports the Sendmail version 8 Milter (mail filter) protocol. These content filters run outside Postfix. They can inspect the SMTP command stream and the message content, and can request modifications before mail is queued. For details see the MILTER_README document.</p>
<dl>
<dt><code>smtpd_milters (empty)</code></p>
<dd>A list of Milter (mail filter) applications for new mail that arrives via the Postfix <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) server.</p>
<dt><code>milter_protocol (6)</code></p>
<dd>The mail filter protocol version and optional protocol extensions for communication with a Milter application; prior to Postfix 2.6 the default protocol is 2.</p>
<dt><code>milter_default_action (tempfail)</code></p>
<dd>The default action when a Milter (mail filter) application is unavailable or mis-configured.</p>
<dt><code>milter_macro_daemon_name ($myhostname)</code></p>
<dd>The {daemon_name} macro value for Milter (mail filter) applications.</p>
<dt><code>milter_macro_v ($mail_name $mail_version)</code></p>
<dd>The {v} macro value for Milter (mail filter) applications.</p>
<dt><code>milter_connect_timeout (30s)</code></p>
<dd>The time limit for connecting to a Milter (mail filter) application, and for negotiating protocol options.</p>
<dt><code>milter_command_timeout (30s)</code></p>
<dd>The time limit for sending an SMTP command to a Milter (mail filter) application, and for receiving the response.</p>
<dt><code>milter_content_timeout (300s)</code></p>
<dd>The time limit for sending message content to a Milter (mail filter) application, and for receiving the response.</p>
<dt><code>milter_connect_macros (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The macros that are sent to Milter (mail filter) applications after completion of an SMTP connection.</p>
<dt><code>milter_helo_macros (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The macros that are sent to Milter (mail filter) applications after the SMTP HELO or EHLO command.</p>
<dt><code>milter_mail_macros (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The macros that are sent to Milter (mail filter) applications after the SMTP MAIL FROM command.</p>
<dt><code>milter_rcpt_macros (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The macros that are sent to Milter (mail filter) applications after the SMTP RCPT TO command.</p>
<dt><code>milter_data_macros (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The macros that are sent to version 4 or higher Milter (mail filter) applications after the SMTP DATA command.</p>
<dt><code>milter_unknown_command_macros (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The macros that are sent to version 3 or higher Milter (mail filter) applications after an unknown SMTP command.</p>
<dt><code>milter_end_of_header_macros (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The macros that are sent to Milter (mail filter) applications after the end of the message header.</p>
<dt><code>milter_end_of_data_macros (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The macros that are sent to Milter (mail filter) applications after the message end-of-data.</dl>
<h2>General Content Inspection Controls</h2>
<p>The following parameters are applicable for both built-in and external content filters. </p>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>receive_override_options (empty)</code></p>
<dd>Enable or disable recipient validation, built-in content filtering, or address mapping.</dl>
<h2>External Content Inspection Controls</h2>
<p>The following parameters are applicable for both before-queue and after-queue content filtering. </p>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>smtpd_authorized_xforward_hosts (empty)</code></p>
<dd>What remote SMTP clients are allowed to use the XFORWARD feature.</dl>
<h2>Sasl Authentication Controls</h2>
<p>Postfix SASL support (RFC 4954) can be used to authenticate remote SMTP clients to the Postfix SMTP server, and to authenticate the Postfix SMTP client to a remote SMTP server. See the SASL_README document for details.</p>
<dl>
<dt><code>broken_sasl_auth_clients (no)</code></p>
<dd>Enable inter-operability with remote SMTP clients that implement an obsolete version of the AUTH command (RFC 4954).</p>
<dt><code>smtpd_sasl_auth_enable (no)</code></p>
<dd>Enable SASL authentication in the Postfix SMTP server.</p>
<dt><code>smtpd_sasl_local_domain (empty)</code></p>
<dd>The name of the Postfix SMTP server&#8217;s local SASL authentication realm.</p>
<dt><code>smtpd_sasl_security_options (noanonymous)</code></p>
<dd>Postfix SMTP server SASL security options; as of Postfix 2.3 the list of available features depends on the SASL server implementation that is selected with <code>smtpd_sasl_type</code>.</p>
<dt><code>smtpd_sender_login_maps (empty)</code></p>
<dd>Optional lookup table with the SASL login names that own sender (MAIL FROM) addresses.</dl>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>smtpd_sasl_exceptions_networks (empty)</code></p>
<dd>What remote SMTP clients the Postfix SMTP server will not offer AUTH support to.</dl>
<p> Available in Postfix version 2.1 and 2.2:</p>
<dl>
<dt><code>smtpd_sasl_application_name (smtpd)</code></p>
<dd>The application name that the Postfix SMTP server uses for SASL server initialization.</dl>
<p> Available in Postfix version 2.3 and later:</p>
<dl>
<dt><code>smtpd_sasl_authenticated_header (no)</code></p>
<dd>Report the SASL authenticated user name in the <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) Received message header.</p>
<dt><code>smtpd_sasl_path (smtpd)</code></p>
<dd>Implementation-specific information that the Postfix SMTP server passes through to the SASL plug-in implementation that is selected with <code>smtpd_sasl_type</code>.</p>
<dt><code>smtpd_sasl_type (cyrus)</code></p>
<dd>The SASL plug-in type that the Postfix SMTP server should use for authentication.</dl>
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><code>cyrus_sasl_config_path (empty)</code></p>
<dd>Search path for Cyrus SASL application configuration files, currently used only to locate the $smtpd_sasl_path.conf file.</dl>
<h2>Starttls Support Controls</h2>
<p>Detailed information about STARTTLS configuration may be found in the TLS_README document.</p>
<dl>
<dt><code>smtpd_tls_security_level (empty)</code></p>
<dd>The SMTP TLS security level for the Postfix SMTP server; when a non-empty value is specified, this overrides the obsolete parameters smtpd_use_tls and smtpd_enforce_tls.</p>
<dt><code>smtpd_sasl_tls_security_options ($smtpd_sasl_security_options)</code></p>
<dd>The SASL authentication security options that the Postfix SMTP server uses for TLS encrypted SMTP sessions.</p>
<dt><code>smtpd_starttls_timeout (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The time limit for Postfix SMTP server write and read operations during TLS startup and shutdown handshake procedures.</p>
<dt><code>smtpd_tls_CAfile (empty)</code></p>
<dd>A file containing (PEM format) CA certificates of root CAs trusted to sign either remote SMTP client certificates or intermediate CA certificates.</p>
<dt><code>smtpd_tls_CApath (empty)</code></p>
<dd>A directory containing (PEM format) CA certificates of root CAs trusted to sign either remote SMTP client certificates or intermediate CA certificates.</p>
<dt><code>smtpd_tls_always_issue_session_ids (yes)</code></p>
<dd>Force the Postfix SMTP server to issue a TLS session id, even when TLS session caching is turned off (smtpd_tls_session_cache_database is empty).</p>
<dt><code>smtpd_tls_ask_ccert (no)</code></p>
<dd>Ask a remote SMTP client for a client certificate.</p>
<dt><code>smtpd_tls_auth_only (no)</code></p>
<dd>When TLS encryption is optional in the Postfix SMTP server, do not announce or accept SASL authentication over unencrypted connections.</p>
<dt><code>smtpd_tls_ccert_verifydepth (9)</code></p>
<dd>The verification depth for remote SMTP client certificates.</p>
<dt><code>smtpd_tls_cert_file (empty)</code></p>
<dd>File with the Postfix SMTP server RSA certificate in PEM format.</p>
<dt><code>smtpd_tls_exclude_ciphers (empty)</code></p>
<dd>List of ciphers or cipher types to exclude from the SMTP server cipher list at all TLS security levels.</p>
<dt><code>smtpd_tls_dcert_file (empty)</code></p>
<dd>File with the Postfix SMTP server DSA certificate in PEM format.</p>
<dt><code>smtpd_tls_dh1024_param_file (empty)</code></p>
<dd>File with DH parameters that the Postfix SMTP server should use with EDH ciphers.</p>
<dt><code>smtpd_tls_dh512_param_file (empty)</code></p>
<dd>File with DH parameters that the Postfix SMTP server should use with EDH ciphers.</p>
<dt><code>smtpd_tls_dkey_file ($smtpd_tls_dcert_file)</code></p>
<dd>File with the Postfix SMTP server DSA private key in PEM format.</p>
<dt><code>smtpd_tls_key_file ($smtpd_tls_cert_file)</code></p>
<dd>File with the Postfix SMTP server RSA private key in PEM format.</p>
<dt><code>smtpd_tls_loglevel (0)</code></p>
<dd>Enable additional Postfix SMTP server logging of TLS activity.</p>
<dt><code>smtpd_tls_mandatory_ciphers (medium)</code></p>
<dd>The minimum TLS cipher grade that the Postfix SMTP server will use with mandatory TLS encryption.</p>
<dt><code>smtpd_tls_mandatory_exclude_ciphers (empty)</code></p>
<dd>Additional list of ciphers or cipher types to exclude from the Postfix SMTP server cipher list at mandatory TLS security levels.</p>
<dt><code>smtpd_tls_mandatory_protocols (!SSLv2)</code></p>
<dd>The SSL/TLS protocols accepted by the Postfix SMTP server with mandatory TLS encryption.</p>
<dt><code>smtpd_tls_received_header (no)</code></p>
<dd>Request that the Postfix SMTP server produces Received: message headers that include information about the protocol and cipher used, as well as the remote SMTP client CommonName and client certificate issuer CommonName.</p>
<dt><code>smtpd_tls_req_ccert (no)</code></p>
<dd>With mandatory TLS encryption, require a trusted remote SMTP client certificate in order to allow TLS connections to proceed.</p>
<dt><code>smtpd_tls_session_cache_database (empty)</code></p>
<dd>Name of the file containing the optional Postfix SMTP server TLS session cache.</p>
<dt><code>smtpd_tls_session_cache_timeout (3600s)</code></p>
<dd>The expiration time of Postfix SMTP server TLS session cache information.</p>
<dt><code>smtpd_tls_wrappermode (no)</code></p>
<dd>Run the Postfix SMTP server in the non-standard &quot;wrapper&quot; mode, instead of using the STARTTLS command.</p>
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
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><code>smtpd_tls_fingerprint_digest (md5)</code></p>
<dd>The message digest algorithm to construct remote SMTP client-certificate fingerprints or public key fingerprints (Postfix 2.9 and later) for <code>check_ccert_access</code> and <code>permit_tls_clientcerts</code>.</dl>
<p> Available in Postfix version 2.6 and later:</p>
<dl>
<dt><code>smtpd_tls_protocols (empty)</code></p>
<dd>List of TLS protocols that the Postfix SMTP server will exclude or include with opportunistic TLS encryption.</p>
<dt><code>smtpd_tls_ciphers (export)</code></p>
<dd>The minimum TLS cipher grade that the Postfix SMTP server will use with opportunistic TLS encryption.</p>
<dt><code>smtpd_tls_eccert_file (empty)</code></p>
<dd>File with the Postfix SMTP server ECDSA certificate in PEM format.</p>
<dt><code>smtpd_tls_eckey_file ($smtpd_tls_eccert_file)</code></p>
<dd>File with the Postfix SMTP server ECDSA private key in PEM format.</p>
<dt><code>smtpd_tls_eecdh_grade (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The Postfix SMTP server security grade for ephemeral elliptic-curve Diffie-Hellman (EECDH) key exchange.</p>
<dt><code>tls_eecdh_strong_curve (prime256v1)</code></p>
<dd>The elliptic curve used by the Postfix SMTP server for sensibly strong ephemeral ECDH key exchange.</p>
<dt><code>tls_eecdh_ultra_curve (secp384r1)</code></p>
<dd>The elliptic curve used by the Postfix SMTP server for maximally strong ephemeral ECDH key exchange.</dl>
<p> Available in Postfix version 2.8 and later:</p>
<dl>
<dt><code>tls_preempt_cipherlist (no)</code></p>
<dd>With SSLv3 and later, use the Postfix SMTP server&#8217;s cipher preference order instead of the remote client&#8217;s cipher preference order.</p>
<dt><code>tls_disable_workarounds (see &#8216;postconf -d&#8217; output)</code></p>
<dd>List or bit-mask of OpenSSL bug work-arounds to disable.</dl>
<h2>Obsolete Starttls Controls</h2>
<p>The following configuration parameters exist for compatibility with Postfix versions before 2.3. Support for these will be removed in a future release.</p>
<dl>
<dt><code>smtpd_use_tls (no)</code></p>
<dd>Opportunistic TLS: announce STARTTLS support to remote SMTP clients, but do not require that clients use TLS encryption.</p>
<dt><code>smtpd_enforce_tls (no)</code></p>
<dd>Mandatory TLS: announce STARTTLS support to remote SMTP clients, and require that clients use TLS encryption.</p>
<dt><code>smtpd_tls_cipherlist (empty)</code></p>
<dd>Obsolete Postfix &lt; 2.3 control for the Postfix SMTP server TLS cipher list.</dl>
<h2>Verp Support Controls</h2>
<p>With VERP style delivery, each recipient of a message receives a customized copy of the message with his/her own recipient address encoded in the envelope sender address. The VERP_README file describes configuration and operation details of Postfix support for variable envelope return path addresses. VERP style delivery is requested with the SMTP XVERP command or with the &quot;sendmail -V&quot; command-line option and is available in Postfix version 1.1 and later.</p>
<dl>
<dt><code>default_verp_delimiters (+=)</code></p>
<dd>The two default VERP delimiter characters.</p>
<dt><code>verp_delimiter_filter (-=+)</code></p>
<dd>The characters Postfix accepts as VERP delimiter characters on the Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command line and in SMTP commands.</dl>
<p> Available in Postfix version 1.1 and 2.0:</p>
<dl>
<dt><code>authorized_verp_clients ($mynetworks)</code></p>
<dd>What remote SMTP clients are allowed to specify the XVERP command.</dl>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>smtpd_authorized_verp_clients ($authorized_verp_clients)</code></p>
<dd>What remote SMTP clients are allowed to specify the XVERP command.</dl>
<h2>Trouble Shooting Controls</h2>
<p>The DEBUG_README document describes how to debug parts of the Postfix mail system. The methods vary from making the software log a lot of detail, to running some daemon processes under control of a call tracer or debugger.</p>
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
<dd>The list of error classes that are reported to the postmaster.</p>
<dt><code>smtpd_reject_footer (empty)</code></p>
<dd>Optional information that is appended after each Postfix SMTP server 4XX or 5XX response.</p>
<dt><code>soft_bounce (no)</code></p>
<dd>Safety net to keep mail queued that would otherwise be returned to the sender.</dl>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>smtpd_authorized_xclient_hosts (empty)</code></p>
<dd>What remote SMTP clients are allowed to use the XCLIENT feature.</dl>
<p> Available in Postfix version 2.10 and later:</p>
<dl>
<dt><code>smtpd_log_access_permit_actions (empty)</code></p>
<dd>Enable logging of the named &quot;permit&quot; actions in SMTP server access lists.</dl>
<h2>Known Versus Unknown Recipient Controls</h2>
<p>As of Postfix version 2.0, the SMTP server rejects mail for unknown recipients. This prevents the mail queue from clogging up with undeliverable MAILER-DAEMON messages. Additional information on this topic is in the LOCAL_RECIPIENT_README and ADDRESS_CLASS_README documents.</p>
<dl>
<dt><code>show_user_unknown_table_name (yes)</code></p>
<dd>Display the name of the recipient table in the &quot;User unknown&quot; responses.</p>
<dt><code>canonical_maps (empty)</code></p>
<dd>Optional address mapping lookup tables for message headers and envelopes.</p>
<dt><code>recipient_canonical_maps (empty)</code></p>
<dd>Optional address mapping lookup tables for envelope and header recipient addresses.</dl>
<p> Parameters concerning known/unknown local recipients:</p>
<dl>
<dt><code>mydestination ($myhostname, localhost.$mydomain, localhost)</code></p>
<dd>The list of domains that are delivered via the $local_transport mail delivery transport.</p>
<dt><code>inet_interfaces (all)</code></p>
<dd>The network interface addresses that this mail system receives mail on.</p>
<dt><code>proxy_interfaces (empty)</code></p>
<dd>The network interface addresses that this mail system receives mail on by way of a proxy or network address translation unit.</p>
<dt><code>inet_protocols (all)</code></p>
<dd>The Internet protocols Postfix will attempt to use when making or accepting connections.</p>
<dt><code>local_recipient_maps (proxy:unix:passwd.byname $alias_maps)</code></p>
<dd>Lookup tables with all names or addresses of local recipients: a recipient address is local when its domain matches $mydestination, $inet_interfaces or $proxy_interfaces.</p>
<dt><code>unknown_local_recipient_reject_code (550)</code></p>
<dd>The numerical Postfix SMTP server response code when a recipient address is local, and $local_recipient_maps specifies a list of lookup tables that does not match the recipient.</dl>
<p> Parameters concerning known/unknown recipients of relay destinations:</p>
<dl>
<dt><code>relay_domains ($mydestination)</code></p>
<dd>What destination domains (and subdomains thereof) this system will relay mail to.</p>
<dt><code>relay_recipient_maps (empty)</code></p>
<dd>Optional lookup tables with all valid addresses in the domains that match $relay_domains.</p>
<dt><code>unknown_relay_recipient_reject_code (550)</code></p>
<dd>The numerical Postfix SMTP server reply code when a recipient address matches $relay_domains, and relay_recipient_maps specifies a list of lookup tables that does not match the recipient address.</dl>
<p> Parameters concerning known/unknown recipients in virtual alias domains:</p>
<dl>
<dt><code>virtual_alias_domains ($virtual_alias_maps)</code></p>
<dd>Postfix is final destination for the specified list of virtual alias domains, that is, domains for which all addresses are aliased to addresses in other local or remote domains.</p>
<dt><code>virtual_alias_maps ($virtual_maps)</code></p>
<dd>Optional lookup tables that alias specific mail addresses or domains to other local or remote address.</p>
<dt><code>unknown_virtual_alias_reject_code (550)</code></p>
<dd>The Postfix SMTP server reply code when a recipient address matches $virtual_alias_domains, and $virtual_alias_maps specifies a list of lookup tables that does not match the recipient address.</dl>
<p> Parameters concerning known/unknown recipients in virtual mailbox domains:</p>
<dl>
<dt><code>virtual_mailbox_domains ($virtual_mailbox_maps)</code></p>
<dd>Postfix is final destination for the specified list of domains; mail is delivered via the $virtual_transport mail delivery transport.</p>
<dt><code>virtual_mailbox_maps (empty)</code></p>
<dd>Optional lookup tables with all valid addresses in the domains that match $virtual_mailbox_domains.</p>
<dt><code>unknown_virtual_mailbox_reject_code (550)</code></p>
<dd>The Postfix SMTP server reply code when a recipient address matches $virtual_mailbox_domains, and $virtual_mailbox_maps specifies a list of lookup tables that does not match the recipient address.</dl>
<h2>Resource And Rate Controls</h2>
<p>The following parameters limit resource usage by the SMTP server and/or control client request rates.</p>
<dl>
<dt><code>line_length_limit (2048)</code></p>
<dd>Upon input, long lines are chopped up into pieces of at most this length; upon delivery, long lines are reconstructed.</p>
<dt><code>queue_minfree (0)</code></p>
<dd>The minimal amount of free space in bytes in the queue file system that is needed to receive mail.</p>
<dt><code>message_size_limit (10240000)</code></p>
<dd>The maximal size in bytes of a message, including envelope information.</p>
<dt><code>smtpd_recipient_limit (1000)</code></p>
<dd>The maximal number of recipients that the Postfix SMTP server accepts per message delivery request.</p>
<dt><code>smtpd_timeout (normal: 300s, overload: 10s)</code></p>
<dd>The time limit for sending a Postfix SMTP server response and for receiving a remote SMTP client request.</p>
<dt><code>smtpd_history_flush_threshold (100)</code></p>
<dd>The maximal number of lines in the Postfix SMTP server command history before it is flushed upon receipt of EHLO, RSET, or end of DATA.</dl>
<p> Available in Postfix version 2.3 and later:</p>
<dl>
<dt><code>smtpd_peername_lookup (yes)</code></p>
<dd>Attempt to look up the remote SMTP client hostname, and verify that the name matches the client IP address.</dl>
<p> The per SMTP client connection count and request rate limits are implemented in co-operation with the <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) service, and are available in Postfix version 2.2 and later.</p>
<dl>
<dt><code>smtpd_client_connection_count_limit (50)</code></p>
<dd>How many simultaneous connections any client is allowed to make to this service.</p>
<dt><code>smtpd_client_connection_rate_limit (0)</code></p>
<dd>The maximal number of connection attempts any client is allowed to make to this service per time unit.</p>
<dt><code>smtpd_client_message_rate_limit (0)</code></p>
<dd>The maximal number of message delivery requests that any client is allowed to make to this service per time unit, regardless of whether or not Postfix actually accepts those messages.</p>
<dt><code>smtpd_client_recipient_rate_limit (0)</code></p>
<dd>The maximal number of recipient addresses that any client is allowed to send to this service per time unit, regardless of whether or not Postfix actually accepts those recipients.</p>
<dt><code>smtpd_client_event_limit_exceptions ($mynetworks)</code></p>
<dd>Clients that are excluded from smtpd_client_*_count/rate_limit restrictions.</dl>
<p> Available in Postfix version 2.3 and later:</p>
<dl>
<dt><code>smtpd_client_new_tls_session_rate_limit (0)</code></p>
<dd>The maximal number of new (i.e., uncached) TLS sessions that a remote SMTP client is allowed to negotiate with this service per time unit.</dl>
<p> Available in Postfix version 2.9 and later:</p>
<dl>
<dt><code>smtpd_per_record_deadline (normal: no, overload: yes)</code></p>
<dd>Change the behavior of the smtpd_timeout time limit, from a time limit per read or write system call, to a time limit to send or receive a complete record (an SMTP command line, SMTP response line, SMTP message content line, or TLS protocol message).</dl>
<h2>Tarpit Controls</h2>
<p>When a remote SMTP client makes errors, the Postfix SMTP server can insert delays before responding. This can help to slow down run-away software. The behavior is controlled by an error counter that counts the number of errors within an SMTP session that a client makes without delivering mail.</p>
<dl>
<dt><code>smtpd_error_sleep_time (1s)</code></p>
<dd>With Postfix version 2.1 and later: the SMTP server response delay after a client has made more than $smtpd_soft_error_limit errors, and fewer than $smtpd_hard_error_limit errors, without delivering mail.</p>
<dt><code>smtpd_soft_error_limit (10)</code></p>
<dd>The number of errors a remote SMTP client is allowed to make without delivering mail before the Postfix SMTP server slows down all its responses.</p>
<dt><code>smtpd_hard_error_limit (normal: 20, overload: 1)</code></p>
<dd>The maximal number of errors a remote SMTP client is allowed to make without delivering mail.</p>
<dt><code>smtpd_junk_command_limit (normal: 100, overload: 1)</code></p>
<dd>The number of junk commands (NOOP, VRFY, ETRN or RSET) that a remote SMTP client can send before the Postfix SMTP server starts to increment the error counter with each junk command.</dl>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>smtpd_recipient_overshoot_limit (1000)</code></p>
<dd>The number of recipients that a remote SMTP client can send in excess of the limit specified with $smtpd_recipient_limit, before the Postfix SMTP server increments the per-session error count for each excess recipient.</dl>
<h2>Access Policy Delegation Controls</h2>
<p>As of version 2.1, Postfix can be configured to delegate access policy decisions to an external server that runs outside Postfix. See the file SMTPD_POLICY_README for more information.</p>
<dl>
<dt><code>smtpd_policy_service_max_idle (300s)</code></p>
<dd>The time after which an idle SMTPD policy service connection is closed.</p>
<dt><code>smtpd_policy_service_max_ttl (1000s)</code></p>
<dd>The time after which an active SMTPD policy service connection is closed.</p>
<dt><code>smtpd_policy_service_timeout (100s)</code></p>
<dd>The time limit for connecting to, writing to or receiving from a delegated SMTPD policy server.</dl>
<h2>Access Controls</h2>
<p>The SMTPD_ACCESS_README document gives an introduction to all the SMTP server access control features.</p>
<dl>
<dt><code>smtpd_delay_reject (yes)</code></p>
<dd>Wait until the RCPT TO command before evaluating $smtpd_client_restrictions, $smtpd_helo_restrictions and $smtpd_sender_restrictions, or wait until the ETRN command before evaluating $smtpd_client_restrictions and $smtpd_helo_restrictions.</p>
<dt><code>parent_domain_matches_subdomains (see &#8216;postconf -d&#8217; output)</code></p>
<dd>What Postfix features match subdomains of &quot;domain.tld&quot; automatically, instead of requiring an explicit &quot;.domain.tld&quot; pattern.</p>
<dt><code>smtpd_client_restrictions (empty)</code></p>
<dd>Optional restrictions that the Postfix SMTP server applies in the context of a client connection request.</p>
<dt><code>smtpd_helo_required (no)</code></p>
<dd>Require that a remote SMTP client introduces itself with the HELO or EHLO command before sending the MAIL command or other commands that require EHLO negotiation.</p>
<dt><code>smtpd_helo_restrictions (empty)</code></p>
<dd>Optional restrictions that the Postfix SMTP server applies in the context of a client HELO command.</p>
<dt><code>smtpd_sender_restrictions (empty)</code></p>
<dd>Optional restrictions that the Postfix SMTP server applies in the context of a client MAIL FROM command.</p>
<dt><code>smtpd_recipient_restrictions (see &#8216;postconf -d&#8217; output)</code></p>
<dd>Optional restrictions that the Postfix SMTP server applies in the context of a client RCPT TO command, after smtpd_relay_restrictions.</p>
<dt><code>smtpd_etrn_restrictions (empty)</code></p>
<dd>Optional restrictions that the Postfix SMTP server applies in the context of a client ETRN command.</p>
<dt><code>allow_untrusted_routing (no)</code></p>
<dd>Forward mail with sender-specified routing (user[@%!]remote[@%!]site) from untrusted clients to destinations matching $relay_domains.</p>
<dt><code>smtpd_restriction_classes (empty)</code></p>
<dd>User-defined aliases for groups of access restrictions.</p>
<dt><code>smtpd_null_access_lookup_key (&lt;&gt;)</code></p>
<dd>The lookup key to be used in SMTP <code><a href="/docs/linux/man/5-access/">access</a></code>(5) tables instead of the null sender address.</p>
<dt><code>permit_mx_backup_networks (empty)</code></p>
<dd>Restrict the use of the permit_mx_backup SMTP access feature to only domains whose primary MX hosts match the listed networks.</dl>
<p> Available in Postfix version 2.0 and later:</p>
<dl>
<dt><code>smtpd_data_restrictions (empty)</code></p>
<dd>Optional access restrictions that the Postfix SMTP server applies in the context of the SMTP DATA command.</p>
<dt><code>smtpd_expansion_filter (see &#8216;postconf -d&#8217; output)</code></p>
<dd>What characters are allowed in $name expansions of RBL reply templates.</dl>
<p> Available in Postfix version 2.1 and later:</p>
<dl>
<dt><code>smtpd_reject_unlisted_sender (no)</code></p>
<dd>Request that the Postfix SMTP server rejects mail from unknown sender addresses, even when no explicit reject_unlisted_sender access restriction is specified.</p>
<dt><code>smtpd_reject_unlisted_recipient (yes)</code></p>
<dd>Request that the Postfix SMTP server rejects mail for unknown recipient addresses, even when no explicit reject_unlisted_recipient access restriction is specified.</dl>
<p> Available in Postfix version 2.2 and later:</p>
<dl>
<dt><code>smtpd_end_of_data_restrictions (empty)</code></p>
<dd>Optional access restrictions that the Postfix SMTP server applies in the context of the SMTP END-OF-DATA command.</dl>
<p> Available in Postfix version 2.10 and later:</p>
<dl>
<dt><code>smtpd_relay_restrictions (permit_mynetworks, reject_unauth_destination)</code></p>
<dd>Access restrictions for mail relay control that the Postfix SMTP server applies in the context of the RCPT TO command, before smtpd_recipient_restrictions.</dl>
<h2>Sender And Recipient Address Verification Controls</h2>
<p>Postfix version 2.1 introduces sender and recipient address verification. This feature is implemented by sending probe email messages that are not actually delivered. This feature is requested via the reject_unverified_sender and reject_unverified_recipient access restrictions. The status of verification probes is maintained by the <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) server. See the file ADDRESS_VERIFICATION_README for information about how to configure and operate the Postfix sender/recipient address verification service.</p>
<dl>
<dt><code>address_verify_poll_count (normal: 3, overload: 1)</code></p>
<dd>How many times to query the <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) service for the completion of an address verification request in progress.</p>
<dt><code>address_verify_poll_delay (3s)</code></p>
<dd>The delay between queries for the completion of an address verification request in progress.</p>
<dt><code>address_verify_sender ($double_bounce_sender)</code></p>
<dd>The sender address to use in address verification probes; prior to Postfix 2.5 the default was &quot;postmaster&quot;.</p>
<dt><code>unverified_sender_reject_code (450)</code></p>
<dd>The numerical Postfix SMTP server response code when a recipient address is rejected by the reject_unverified_sender restriction.</p>
<dt><code>unverified_recipient_reject_code (450)</code></p>
<dd>The numerical Postfix SMTP server response when a recipient address is rejected by the reject_unverified_recipient restriction.</dl>
<p> Available in Postfix version 2.6 and later:</p>
<dl>
<dt><code>unverified_sender_defer_code (450)</code></p>
<dd>The numerical Postfix SMTP server response code when a sender address probe fails due to a temporary error condition.</p>
<dt><code>unverified_recipient_defer_code (450)</code></p>
<dd>The numerical Postfix SMTP server response when a recipient address probe fails due to a temporary error condition.</p>
<dt><code>unverified_sender_reject_reason (empty)</code></p>
<dd>The Postfix SMTP server&#8217;s reply when rejecting mail with reject_unverified_sender.</p>
<dt><code>unverified_recipient_reject_reason (empty)</code></p>
<dd>The Postfix SMTP server&#8217;s reply when rejecting mail with reject_unverified_recipient.</p>
<dt><code>unverified_sender_tempfail_action ($reject_tempfail_action)</code></p>
<dd>The Postfix SMTP server&#8217;s action when reject_unverified_sender fails due to a temporary error condition.</p>
<dt><code>unverified_recipient_tempfail_action ($reject_tempfail_action)</code></p>
<dd>The Postfix SMTP server&#8217;s action when reject_unverified_recipient fails due to a temporary error condition.</dl>
<p> Available with Postfix 2.9 and later:</p>
<dl>
<dt><code>address_verify_sender_ttl (0s)</code></p>
<dd>The time between changes in the time-dependent portion of address verification probe sender addresses.</dl>
<h2>Access Control Responses</h2>
<p>The following parameters control numerical SMTP reply codes and/or text responses.</p>
<dl>
<dt><code>access_map_reject_code (554)</code></p>
<dd>The numerical Postfix SMTP server response code for an <code><a href="/docs/linux/man/5-access/">access</a></code>(5) map &quot;reject&quot; action.</p>
<dt><code>defer_code (450)</code></p>
<dd>The numerical Postfix SMTP server response code when a remote SMTP client request is rejected by the &quot;defer&quot; restriction.</p>
<dt><code>invalid_hostname_reject_code (501)</code></p>
<dd>The numerical Postfix SMTP server response code when the client HELO or EHLO command parameter is rejected by the reject_invalid_helo_hostname restriction.</p>
<dt><code>maps_rbl_reject_code (554)</code></p>
<dd>The numerical Postfix SMTP server response code when a remote SMTP client request is blocked by the reject_rbl_client, reject_rhsbl_client, reject_rhsbl_reverse_client, reject_rhsbl_sender or reject_rhsbl_recipient restriction.</p>
<dt><code>non_fqdn_reject_code (504)</code></p>
<dd>The numerical Postfix SMTP server reply code when a client request is rejected by the reject_non_fqdn_helo_hostname, reject_non_fqdn_sender or reject_non_fqdn_recipient restriction.</p>
<dt><code>plaintext_reject_code (450)</code></p>
<dd>The numerical Postfix SMTP server response code when a request is rejected by the <code>reject_plaintext_session</code> restriction.</p>
<dt><code>reject_code (554)</code></p>
<dd>The numerical Postfix SMTP server response code when a remote SMTP client request is rejected by the &quot;reject&quot; restriction.</p>
<dt><code>relay_domains_reject_code (554)</code></p>
<dd>The numerical Postfix SMTP server response code when a client request is rejected by the reject_unauth_destination recipient restriction.</p>
<dt><code>unknown_address_reject_code (450)</code></p>
<dd>The numerical Postfix SMTP server response code when a sender or recipient address is rejected by the reject_unknown_sender_domain or reject_unknown_recipient_domain restriction.</p>
<dt><code>unknown_client_reject_code (450)</code></p>
<dd>The numerical Postfix SMTP server response code when a client without valid address &lt;=&gt; name mapping is rejected by the reject_unknown_client_hostname restriction.</p>
<dt><code>unknown_hostname_reject_code (450)</code></p>
<dd>The numerical Postfix SMTP server response code when the hostname specified with the HELO or EHLO command is rejected by the reject_unknown_helo_hostname restriction.</dl>
<p> Available in Postfix version 2.0 and later:</p>
<dl>
<dt><code>default_rbl_reply (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default Postfix SMTP server response template for a request that is rejected by an RBL-based restriction.</p>
<dt><code>multi_recipient_bounce_reject_code (550)</code></p>
<dd>The numerical Postfix SMTP server response code when a remote SMTP client request is blocked by the reject_multi_recipient_bounce restriction.</p>
<dt><code>rbl_reply_maps (empty)</code></p>
<dd>Optional lookup tables with RBL response templates.</dl>
<p> Available in Postfix version 2.6 and later:</p>
<dl>
<dt><code>access_map_defer_code (450)</code></p>
<dd>The numerical Postfix SMTP server response code for an <code><a href="/docs/linux/man/5-access/">access</a></code>(5) map &quot;defer&quot; action, including &quot;defer_if_permit&quot; or &quot;defer_if_reject&quot;.</p>
<dt><code>reject_tempfail_action (defer_if_permit)</code></p>
<dd>The Postfix SMTP server&#8217;s action when a reject-type restriction fails due to a temporary error condition.</p>
<dt><code>unknown_helo_hostname_tempfail_action ($reject_tempfail_action)</code></p>
<dd>The Postfix SMTP server&#8217;s action when reject_unknown_helo_hostname fails due to an temporary error condition.</p>
<dt><code>unknown_address_tempfail_action ($reject_tempfail_action)</code></p>
<dd>The Postfix SMTP server&#8217;s action when reject_unknown_sender_domain or reject_unknown_recipient_domain fail due to a temporary error condition.</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>command_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The location of all postfix administrative commands.</p>
<dt><code>double_bounce_sender (double-bounce)</code></p>
<dd>The sender address of postmaster notifications that are generated by the mail system.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
<dt><code>mail_name (Postfix)</code></p>
<dd>The mail system name that is displayed in Received: headers, in the SMTP greeting banner, and in bounced mail.</p>
<dt><code>mail_owner (postfix)</code></p>
<dd>The UNIX system account that owns the Postfix queue and most Postfix daemon processes.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>max_use (100)</code></p>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</p>
<dt><code>myhostname (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The internet hostname of this mail system.</p>
<dt><code>mynetworks (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The list of &quot;trusted&quot; remote SMTP clients that have more privileges than &quot;strangers&quot;.</p>
<dt><code>myorigin ($myhostname)</code></p>
<dd>The domain name that locally-posted mail appears to come from, and that locally posted mail is delivered to.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The location of the Postfix top-level queue directory.</p>
<dt><code>recipient_delimiter (empty)</code></p>
<dd>The separator between user names and address extensions (user+foo).</p>
<dt><code>smtpd_banner ($myhostname ESMTP $mail_name)</code></p>
<dd>The text that follows the 220 status code in the SMTP greeting banner.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<p> Available in Postfix version 2.2 and later:</p>
<dl>
<dt><code>smtpd_forbidden_commands (CONNECT, GET, POST)</code></p>
<dd>List of commands that cause the Postfix SMTP server to immediately terminate the session with a 221 code.</dl>
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><code>smtpd_client_port_logging (no)</code></p>
<dd>Enable logging of the remote SMTP client port in addition to the hostname and IP address.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-anvil/">anvil</a>(8), connection/rate limiting
<a href="//www.systutorials.com/docs/linux/man/8-cleanup/">cleanup</a>(8), message canonicalization
<a href="//www.systutorials.com/docs/linux/man/8-tlsmgr/">tlsmgr</a>(8), TLS session and PRNG management
<a href="//www.systutorials.com/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a>(8), address resolver
<a href="//www.systutorials.com/docs/linux/man/8-verify/">verify</a>(8), address verification service
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), generic daemon options
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>ADDRESS_CLASS_README, blocking unknown hosted or relay recipients
ADDRESS_REWRITING_README Postfix address manipulation
FILTER_README, external after-queue content filter
LOCAL_RECIPIENT_README, blocking unknown local recipients
MILTER_README, before-queue mail filter applications
SMTPD_ACCESS_README, built-in access policies
SMTPD_POLICY_README, external policy server
SMTPD_PROXY_README, external before-queue content filter
SASL_README, Postfix SASL howto
TLS_README, Postfix STARTTLS howto
VERP_README, Postfix XVERP extension
XCLIENT_README, Postfix XCLIENT extension
XFORWARD_README, Postfix XFORWARD extension</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
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
Revised TLS support by:
Victor Duchovni
Morgan Stanley</pre>
