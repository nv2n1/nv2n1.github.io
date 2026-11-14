---
title: "postscreen(8)"
name: "postscreen"
section: "8"
letter: "p"
url: "/docs/linux/man/8-postscreen/"
description: "postscreen – Postfix zombie blocker"
---

<p>postscreen &#8211; Postfix zombie blocker</p>
<h2>Synopsis</h2>
<pre><code>postscreen</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The Postfix <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server provides additional protection against mail server overload. One <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) process handles multiple inbound SMTP connections, and decides which clients may talk to a Postfix SMTP server process. By keeping spambots away, <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) leaves more SMTP server processes available for legitimate clients, and delays the onset of server overload conditions. </p>
<p> This program should not be used on SMTP ports that receive mail from end-user clients (MUAs). In a typical deployment, <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) handles the MX service on TCP port 25, while MUA clients submit mail via the <code>submission</code> service on TCP port 587 which requires client authentication. Alternatively, a site could set up a dedicated, non-postscreen, &quot;port 25&quot; server that provides <code>submission</code> service and client authentication, but no MX service. </p>
<p> <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) maintains a temporary whitelist for clients that have passed a number of tests. When an SMTP client IP address is whitelisted, <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) hands off the connection immediately to a Postfix SMTP server process. This minimizes the overhead for legitimate mail. </p>
<p> By default, <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) logs statistics and hands off every connection to a Postfix SMTP server process, while excluding clients in mynetworks from all tests (primarily, to avoid problems with non-standard SMTP implementations in network appliances). This mode is useful for non-destructive testing. </p>
<p> In a typical production setting, <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) is configured to reject mail from clients that fail one or more tests. <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) logs rejected mail with the client address, helo, sender and recipient information. </p>
<p> <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) is not an SMTP proxy; this is intentional. The purpose is to keep spambots away from Postfix SMTP server processes, while minimizing overhead for legitimate traffic.</p>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server is moderately security-sensitive. It talks to untrusted clients on the network. The process can be run chrooted at fixed low privilege.</p>
<h2>Standards</h2>
<pre>RFC 821 (SMTP protocol)
RFC 1123 (Host requirements)
RFC 1652 (8bit-MIME transport)
RFC 1869 (SMTP service extensions)
RFC 1870 (Message Size Declaration)
RFC 1985 (ETRN command)
RFC 2034 (SMTP Enhanced Status Codes)
RFC 2821 (SMTP protocol)
Not: RFC 2920 (SMTP Pipelining)
RFC 3207 (STARTTLS command)
RFC 3461 (SMTP DSN Extension)
RFC 3463 (Enhanced Status Codes)
RFC 5321 (SMTP protocol, including multi-line 220 banners)</pre>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Bugs</h2>
<p>The <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) built-in SMTP protocol engine currently does not announce support for AUTH, XCLIENT or XFORWARD. If you need to make these services available on port 25, then do not enable the optional &quot;after 220 server greeting&quot; tests, and do not use DNSBLs that reject traffic from dial-up and residential networks. </p>
<p> The optional &quot;after 220 server greeting&quot; tests involve <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8)&#8217;s built-in SMTP protocol engine. When these tests succeed, <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) adds the client to the temporary whitelist, but it cannot not hand off the &quot;live&quot; connection to a Postfix SMTP server process in the middle of a session. Instead, <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) defers attempts to deliver mail with a 4XX status, and waits for the client to disconnect. When the client connects again, <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) will allow the client to talk to a Postfix SMTP server process (provided that the whitelist status has not expired). <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) mitigates the impact of this limitation by giving the &quot;after 220 server greeting&quot; tests a long expiration time.</p>
<h2>Configuration Parameters</h2>
<p>Changes to main.cf are not picked up automatically, as <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) processes may run for several hours. Use the command &quot;postfix reload&quot; after a configuration change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples. </p>
<p> NOTE: Some <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) parameters implement stress-dependent behavior. This is supported only when the default parameter value is stress-dependent (that is, it looks like ${stress?X}${stress:Y}, or it is the $<i>name</i> of an smtpd parameter with a stress-dependent default). Other parameters always evaluate as if the <code>stress</code> parameter value is the empty string.</p>
<h2>Compatibility Controls</h2>
<dl>
<dt><code>postscreen_command_filter ($smtpd_command_filter)</code></p>
<dd>A mechanism to transform commands from remote SMTP clients.</p>
<dt><code>postscreen_discard_ehlo_keyword_address_maps ($smtpd_discard_ehlo_keyword_address_maps)</code></p>
<dd>Lookup tables, indexed by the remote SMTP client address, with case insensitive lists of EHLO keywords (pipelining, starttls, auth, etc.) that the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server will not send in the EHLO response to a remote SMTP client.</p>
<dt><code>postscreen_discard_ehlo_keywords ($smtpd_discard_ehlo_keywords)</code></p>
<dd>A case insensitive list of EHLO keywords (pipelining, starttls, auth, etc.) that the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server will not send in the EHLO response to a remote SMTP client.</dl>
<h2>Trouble Shooting Controls</h2>
<dl>
<dt><code>postscreen_expansion_filter (see &#8216;postconf -d&#8217; output)</code></p>
<dd>List of characters that are permitted in postscreen_reject_footer attribute expansions.</p>
<dt><code>postscreen_reject_footer ($smtpd_reject_footer)</code></p>
<dd>Optional information that is appended after a 4XX or 5XX <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server response.</p>
<dt><code>soft_bounce (no)</code></p>
<dd>Safety net to keep mail queued that would otherwise be returned to the sender.</dl>
<h2>Before-Postscreen Proxy Agent</h2>
<p>Available in Postfix version 2.10 and later:</p>
<dl>
<dt><code>postscreen_upstream_proxy_protocol (empty)</code></p>
<dd>The name of the proxy protocol used by an optional before-postscreen proxy agent.</p>
<dt><code>postscreen_upstream_proxy_timeout (5s)</code></p>
<dd>The time limit for the proxy protocol specified with the postscreen_upstream_proxy_protocol parameter.</dl>
<h2>Permanent White/Blacklist Test</h2>
<p>This test is executed immediately after a remote SMTP client connects. If a client is permanently whitelisted, the client will be handed off immediately to a Postfix SMTP server process.</p>
<dl>
<dt><code>postscreen_access_list (permit_mynetworks)</code></p>
<dd>Permanent white/blacklist for remote SMTP client IP addresses.</p>
<dt><code>postscreen_blacklist_action (ignore)</code></p>
<dd>The action that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) takes when a remote SMTP client is permanently blacklisted with the postscreen_access_list parameter.</dl>
<h2>Mail Exchanger Policy Tests</h2>
<p>When <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) is configured to monitor all primary and backup MX addresses, it can refuse to whitelist clients that connect to a backup MX address only. For small sites, this requires configuring primary and backup MX addresses on the same MTA. Larger sites would have to share the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) cache between primary and backup MTAs, which would introduce a common point of failure.</p>
<dl>
<dt><code>postscreen_whitelist_interfaces (static:all)</code></p>
<dd>A list of local <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server IP addresses where a non-whitelisted remote SMTP client can obtain <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8)&#8217;s temporary whitelist status.</dl>
<h2>Before-Greeting Tests</h2>
<p>These tests are executed before the remote SMTP client receives the &quot;220 servername&quot; greeting. If no tests remain after the successful completion of this phase, the client will be handed off immediately to a Postfix SMTP server process.</p>
<dl>
<dt><code>dnsblog_service_name (dnsblog)</code></p>
<dd>The name of the <code><a href="/docs/linux/man/8-dnsblog/">dnsblog</a></code>(8) service entry in master.cf.</p>
<dt><code>postscreen_dnsbl_action (ignore)</code></p>
<dd>The action that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) takes when a remote SMTP client&#8217;s combined DNSBL score is equal to or greater than a threshold (as defined with the postscreen_dnsbl_sites and postscreen_dnsbl_threshold parameters).</p>
<dt><code>postscreen_dnsbl_reply_map (empty)</code></p>
<dd>A mapping from actual DNSBL domain name which includes a secret password, to the DNSBL domain name that postscreen will reply with when it rejects mail.</p>
<dt><code>postscreen_dnsbl_sites (empty)</code></p>
<dd>Optional list of DNS white/blacklist domains, filters and weight factors.</p>
<dt><code>postscreen_dnsbl_threshold (1)</code></p>
<dd>The inclusive lower bound for blocking a remote SMTP client, based on its combined DNSBL score as defined with the postscreen_dnsbl_sites parameter.</p>
<dt><code>postscreen_greet_action (ignore)</code></p>
<dd>The action that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) takes when a remote SMTP client speaks before its turn within the time specified with the postscreen_greet_wait parameter.</p>
<dt><code>postscreen_greet_banner ($smtpd_banner)</code></p>
<dd>The <i>text</i> in the optional &quot;220-<i>text</i>&#8230;&quot; server response that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) sends ahead of the real Postfix SMTP server&#8217;s &quot;220 text&#8230;&quot; response, in an attempt to confuse bad SMTP clients so that they speak before their turn (pre-greet).</p>
<dt><code>postscreen_greet_wait (${stress?2}${stress:6}s)</code></p>
<dd>The amount of time that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) will wait for an SMTP client to send a command before its turn, and for DNS blocklist lookup results to arrive (default: up to 2 seconds under stress, up to 6 seconds otherwise).</p>
<dt><code>smtpd_service_name (smtpd)</code></p>
<dd>The internal service that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) hands off allowed connections to.</dl>
<h2>After-Greeting Tests</h2>
<p>These tests are executed after the remote SMTP client receives the &quot;220 servername&quot; greeting. If a client passes all tests during this phase, it will receive a 4XX response to RCPT TO commands until the client hangs up. After this, the client will be allowed to talk directly to a Postfix SMTP server process.</p>
<dl>
<dt><code>postscreen_bare_newline_action (ignore)</code></p>
<dd>The action that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) takes when a remote SMTP client sends a bare newline character, that is, a newline not preceded by carriage return.</p>
<dt><code>postscreen_bare_newline_enable (no)</code></p>
<dd>Enable &quot;bare newline&quot; SMTP protocol tests in the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server.</p>
<dt><code>postscreen_disable_vrfy_command ($disable_vrfy_command)</code></p>
<dd>Disable the SMTP VRFY command in the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) daemon.</p>
<dt><code>postscreen_forbidden_commands ($smtpd_forbidden_commands)</code></p>
<dd>List of commands that the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server considers in violation of the SMTP protocol.</p>
<dt><code>postscreen_helo_required ($smtpd_helo_required)</code></p>
<dd>Require that a remote SMTP client sends HELO or EHLO before commencing a MAIL transaction.</p>
<dt><code>postscreen_non_smtp_command_action (drop)</code></p>
<dd>The action that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) takes when a remote SMTP client sends non-SMTP commands as specified with the postscreen_forbidden_commands parameter.</p>
<dt><code>postscreen_non_smtp_command_enable (no)</code></p>
<dd>Enable &quot;non-SMTP command&quot; tests in the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server.</p>
<dt><code>postscreen_pipelining_action (enforce)</code></p>
<dd>The action that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) takes when a remote SMTP client sends multiple commands instead of sending one command and waiting for the server to respond.</p>
<dt><code>postscreen_pipelining_enable (no)</code></p>
<dd>Enable &quot;pipelining&quot; SMTP protocol tests in the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server.</dl>
<h2>Cache Controls</h2>
<dl>
<dt><code>postscreen_cache_cleanup_interval (12h)</code></p>
<dd>The amount of time between <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) cache cleanup runs.</p>
<dt><code>postscreen_cache_map (btree:$data_directory/postscreen_cache)</code></p>
<dd>Persistent storage for the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server decisions.</p>
<dt><code>postscreen_cache_retention_time (7d)</code></p>
<dd>The amount of time that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) will cache an expired temporary whitelist entry before it is removed.</p>
<dt><code>postscreen_bare_newline_ttl (30d)</code></p>
<dd>The amount of time that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) will use the result from a successful &quot;bare newline&quot; SMTP protocol test.</p>
<dt><code>postscreen_dnsbl_ttl (1h)</code></p>
<dd>The amount of time that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) will use the result from a successful DNS blocklist test.</p>
<dt><code>postscreen_greet_ttl (1d)</code></p>
<dd>The amount of time that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) will use the result from a successful PREGREET test.</p>
<dt><code>postscreen_non_smtp_command_ttl (30d)</code></p>
<dd>The amount of time that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) will use the result from a successful &quot;non_smtp_command&quot; SMTP protocol test.</p>
<dt><code>postscreen_pipelining_ttl (30d)</code></p>
<dd>The amount of time that <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) will use the result from a successful &quot;pipelining&quot; SMTP protocol test.</dl>
<h2>Resource Controls</h2>
<dl>
<dt><code>line_length_limit (2048)</code></p>
<dd>Upon input, long lines are chopped up into pieces of at most this length; upon delivery, long lines are reconstructed.</p>
<dt><code>postscreen_client_connection_count_limit ($smtpd_client_connection_count_limit)</code></p>
<dd>How many simultaneous connections any remote SMTP client is allowed to have with the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) daemon.</p>
<dt><code>postscreen_command_count_limit (20)</code></p>
<dd>The limit on the total number of commands per SMTP session for <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8)&#8217;s built-in SMTP protocol engine.</p>
<dt><code>postscreen_command_time_limit (${stress?10}${stress:300}s)</code></p>
<dd>The time limit to read an entire command line with <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8)&#8217;s built-in SMTP protocol engine.</p>
<dt><code>postscreen_post_queue_limit ($default_process_limit)</code></p>
<dd>The number of clients that can be waiting for service from a real Postfix SMTP server process.</p>
<dt><code>postscreen_pre_queue_limit ($default_process_limit)</code></p>
<dd>The number of non-whitelisted clients that can be waiting for a decision whether they will receive service from a real Postfix SMTP server process.</p>
<dt><code>postscreen_watchdog_timeout (10s)</code></p>
<dd>How much time a <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) process may take to respond to a remote SMTP client command or to perform a cache operation before it is terminated by a built-in watchdog timer.</dl>
<h2>Starttls Controls</h2>
<dl>
<dt><code>postscreen_tls_security_level ($smtpd_tls_security_level)</code></p>
<dd>The SMTP TLS security level for the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server; when a non-empty value is specified, this overrides the obsolete parameters postscreen_use_tls and postscreen_enforce_tls.</p>
<dt><code>tlsproxy_service_name (tlsproxy)</code></p>
<dd>The name of the <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) service entry in master.cf.</dl>
<h2>Obsolete Starttls Support Controls</h2>
<p>These parameters are supported for compatibility with <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) legacy parameters.</p>
<dl>
<dt><code>postscreen_use_tls ($smtpd_use_tls)</code></p>
<dd>Opportunistic TLS: announce STARTTLS support to remote SMTP clients, but do not require that clients use TLS encryption.</p>
<dt><code>postscreen_enforce_tls ($smtpd_enforce_tls)</code></p>
<dd>Mandatory TLS: announce STARTTLS support to remote SMTP clients, and require that clients use TLS encryption.</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>delay_logging_resolution_limit (2)</code></p>
<dd>The maximal number of digits after the decimal point when logging sub-second delay values.</p>
<dt><code>command_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The location of all postfix administrative commands.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a>(8), Postfix SMTP server
<a href="//www.systutorials.com/docs/linux/man/8-tlsproxy/">tlsproxy</a>(8), Postfix TLS proxy server
<a href="//www.systutorials.com/docs/linux/man/8-dnsblog/">dnsblog</a>(8), DNS black/whitelist logger
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>POSTSCREEN_README, Postfix Postscreen Howto</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>This service was introduced with Postfix version 2.8. </p>
<p> Many ideas in <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) were explored in earlier work by Michael Tokarev, in OpenBSD spamd, and in MailChannels Traffic Control.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
