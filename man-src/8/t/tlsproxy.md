---
title: "tlsproxy(8)"
name: "tlsproxy"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tlsproxy/"
description: "tlsproxy – Postfix TLS proxy"
---

<p>tlsproxy &#8211; Postfix TLS proxy</p>
<h2>Synopsis</h2>
<pre><code>tlsproxy</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server implements a server-side TLS proxy. It is used by <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) to talk SMTP-over-TLS with remote SMTP clients that are not whitelisted (including clients whose whitelist status has expired), but it should also work for non-SMTP protocols. </p>
<p> Although one <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) process can serve multiple sessions at the same time, it is a good idea to allow the number of processes to increase with load, so that the service remains responsive.</p>
<h2>Protocol Example</h2>
<p>The example below concerns <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8). However, the <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server is agnostic of the application protocol, and the example is easily adapted to other applications. </p>
<p> After receiving a valid remote SMTP client STARTTLS command, the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server sends the remote SMTP client endpoint string, the requested role (server), and the requested timeout to <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8). <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) then receives a &quot;TLS available&quot; indication from <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8). If the TLS service is available, <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) sends the remote SMTP client file descriptor to <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8), and sends the plaintext 220 greeting to the remote SMTP client. This triggers TLS negotiations between the remote SMTP client and <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8). Upon completion of the TLS-level handshake, <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) translates between plaintext from/to <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) and ciphertext to/from the remote SMTP client.</p>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server is moderately security-sensitive. It talks to untrusted clients on the network. The process can be run chrooted at fixed low privilege.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are not picked up automatically, as <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) processes may run for a long time depending on mail server load. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Starttls Support Controls</h2>
<dl>
<dt><code>tlsproxy_tls_CAfile ($smtpd_tls_CAfile)</code></p>
<dd>A file containing (PEM format) CA certificates of root CAs trusted to sign either remote SMTP client certificates or intermediate CA certificates.</p>
<dt><code>tlsproxy_tls_CApath ($smtpd_tls_CApath)</code></p>
<dd>A directory containing (PEM format) CA certificates of root CAs trusted to sign either remote SMTP client certificates or intermediate CA certificates.</p>
<dt><code>tlsproxy_tls_always_issue_session_ids ($smtpd_tls_always_issue_session_ids)</code></p>
<dd>Force the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server to issue a TLS session id, even when TLS session caching is turned off.</p>
<dt><code>tlsproxy_tls_ask_ccert ($smtpd_tls_ask_ccert)</code></p>
<dd>Ask a remote SMTP client for a client certificate.</p>
<dt><code>tlsproxy_tls_ccert_verifydepth ($smtpd_tls_ccert_verifydepth)</code></p>
<dd>The verification depth for remote SMTP client certificates.</p>
<dt><code>tlsproxy_tls_cert_file ($smtpd_tls_cert_file)</code></p>
<dd>File with the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server RSA certificate in PEM format.</p>
<dt><code>tlsproxy_tls_ciphers ($smtpd_tls_ciphers)</code></p>
<dd>The minimum TLS cipher grade that the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server will use with opportunistic TLS encryption.</p>
<dt><code>tlsproxy_tls_dcert_file ($smtpd_tls_dcert_file)</code></p>
<dd>File with the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server DSA certificate in PEM format.</p>
<dt><code>tlsproxy_tls_dh1024_param_file ($smtpd_tls_dh1024_param_file)</code></p>
<dd>File with DH parameters that the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server should use with EDH ciphers.</p>
<dt><code>tlsproxy_tls_dh512_param_file ($smtpd_tls_dh512_param_file)</code></p>
<dd>File with DH parameters that the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server should use with EDH ciphers.</p>
<dt><code>tlsproxy_tls_dkey_file ($smtpd_tls_dkey_file)</code></p>
<dd>File with the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server DSA private key in PEM format.</p>
<dt><code>tlsproxy_tls_eccert_file ($smtpd_tls_eccert_file)</code></p>
<dd>File with the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server ECDSA certificate in PEM format.</p>
<dt><code>tlsproxy_tls_eckey_file ($smtpd_tls_eckey_file)</code></p>
<dd>File with the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server ECDSA private key in PEM format.</p>
<dt><code>tlsproxy_tls_eecdh_grade ($smtpd_tls_eecdh_grade)</code></p>
<dd>The Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server security grade for ephemeral elliptic-curve Diffie-Hellman (EECDH) key exchange.</p>
<dt><code>tlsproxy_tls_exclude_ciphers ($smtpd_tls_exclude_ciphers)</code></p>
<dd>List of ciphers or cipher types to exclude from the <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server cipher list at all TLS security levels.</p>
<dt><code>tlsproxy_tls_fingerprint_digest ($smtpd_tls_fingerprint_digest)</code></p>
<dd>The message digest algorithm to construct remote SMTP client-certificate fingerprints.</p>
<dt><code>tlsproxy_tls_key_file ($smtpd_tls_key_file)</code></p>
<dd>File with the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server RSA private key in PEM format.</p>
<dt><code>tlsproxy_tls_loglevel ($smtpd_tls_loglevel)</code></p>
<dd>Enable additional Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server logging of TLS activity.</p>
<dt><code>tlsproxy_tls_mandatory_ciphers ($smtpd_tls_mandatory_ciphers)</code></p>
<dd>The minimum TLS cipher grade that the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server will use with mandatory TLS encryption.</p>
<dt><code>tlsproxy_tls_mandatory_exclude_ciphers ($smtpd_tls_mandatory_exclude_ciphers)</code></p>
<dd>Additional list of ciphers or cipher types to exclude from the <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server cipher list at mandatory TLS security levels.</p>
<dt><code>tlsproxy_tls_mandatory_protocols ($smtpd_tls_mandatory_protocols)</code></p>
<dd>The SSL/TLS protocols accepted by the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server with mandatory TLS encryption.</p>
<dt><code>tlsproxy_tls_protocols ($smtpd_tls_protocols)</code></p>
<dd>List of TLS protocols that the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server will exclude or include with opportunistic TLS encryption.</p>
<dt><code>tlsproxy_tls_req_ccert ($smtpd_tls_req_ccert)</code></p>
<dd>With mandatory TLS encryption, require a trusted remote SMTP client certificate in order to allow TLS connections to proceed.</p>
<dt><code>tlsproxy_tls_security_level ($smtpd_tls_security_level)</code></p>
<dd>The SMTP TLS security level for the Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server; when a non-empty value is specified, this overrides the obsolete parameters smtpd_use_tls and smtpd_enforce_tls.</p>
<dt><code>tlsproxy_tls_session_cache_timeout ($smtpd_tls_session_cache_timeout)</code></p>
<dd>The expiration time of Postfix <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) server TLS session cache information.</dl>
<h2>Obsolete Starttls Support Controls</h2>
<p>These parameters are supported for compatibility with <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) legacy parameters.</p>
<dl>
<dt><code>tlsproxy_use_tls ($smtpd_use_tls)</code></p>
<dd>Opportunistic TLS: announce STARTTLS support to remote SMTP clients, but do not require that clients use TLS encryption.</p>
<dt><code>tlsproxy_enforce_tls ($smtpd_enforce_tls)</code></p>
<dd>Mandatory TLS: announce STARTTLS support to remote SMTP clients, and require that clients use TLS encryption.</dl>
<h2>Resource Controls</h2>
<dl>
<dt><code>tlsproxy_watchdog_timeout (10s)</code></p>
<dd>How much time a <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) process may take to process local or remote I/O before it is terminated by a built-in watchdog timer.</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-postscreen/">postscreen</a>(8), Postfix zombie blocker
<a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a>(8), Postfix SMTP server
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-syslogd/">syslogd</a>(5), system logging</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>This service was introduced with Postfix version 2.8.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
