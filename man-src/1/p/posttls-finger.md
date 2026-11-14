---
title: "posttls-finger(1)"
name: "posttls-finger"
section: "1"
letter: "p"
url: "/docs/linux/man/1-posttls-finger/"
description: "posttls-finger – Probe the TLS properties of an ESMTP or LMTP server."
---

<h2 class="name">NAME</h2>
<p> posttls-finger &#8211; Probe the TLS properties of an ESMTP or LMTP server. </p>
<h2>SYNOPSIS</h2>
<pre><code>
posttls - finger[options] [inet:] domain[:port][match...]

                                               posttls -
                                               finger - S[options] unix : pathname[match...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-posttls-finger/">posttls-finger</a></code>(1) connects to the specified destination and reports TLS-related information about the server. With SMTP, the destination is a domainname; with LMTP it is either a domainname prefixed with <code>inet:</code> or a pathname prefixed with <code>unix:</code>. If Postfix is built without TLS support, the resulting posttls-finger program has very limited functionality, and only the <code>-a</code>, <code>-c</code>, <code>-h</code>, <code>-o</code>, <code>-S</code>, <code>-t</code>, <code>-T</code> and <code>-v</code> options are available. </p>
<p> Note: this is an unsupported test program. No attempt is made to maintain compatibility between successive versions. </p>
<p> For SMTP servers that don&#8217;t support ESMTP, only the greeting banner and the negative EHLO response are reported. Otherwise, the reported EHLO response details further server capabilities. </p>
<p> If TLS support is enabled when <code><a href="/docs/linux/man/1-posttls-finger/">posttls-finger</a></code>(1) is compiled, and the server supports <code>STARTTLS</code>, a TLS handshake is attempted. </p>
<p> If DNSSEC support is available, the connection TLS security level (<code>-l</code> option) defaults to <code>dane</code>; see TLS_README for details. Otherwise, it defaults to <code>secure</code>. This setting determines the certificate matching policy. </p>
<p> If TLS negotiation succeeds, the TLS protocol and cipher details are reported. The server certificate is then verified in accordance with the policy at the chosen (or default) security level. With public CA-based trust, when the <code>-L</code> option includes <code>certmatch</code>, (true by default) name matching is performed even if the certificate chain is not trusted. This logs the names found in the remote SMTP server certificate and which if any would match, were the certificate chain trusted. </p>
<p> Note: <code><a href="/docs/linux/man/1-posttls-finger/">posttls-finger</a></code>(1) does not perform any table lookups, so the TLS policy table and obsolete per-site tables are not consulted. It does not communicate with the <code><a href="/docs/linux/man/8-tlsmgr/">tlsmgr</a></code>(8) daemon (or any other Postfix daemons); its TLS session cache is held in private memory, and disappears when the process exits. </p>
<p> With the <code>-r </code><i>delay</i> option, if the server assigns a TLS session id, the TLS session is cached. The connection is then closed and re-opened after the specified delay, and <code><a href="/docs/linux/man/1-posttls-finger/">posttls-finger</a></code>(1) then reports whether the cached TLS session was re-used. </p>
<p> When the destination is a load balancer, it may be distributing load between multiple server caches. Typically, each server returns its unique name in its EHLO response. If, upon reconnecting with <code>-r</code>, a new server name is detected, another session is cached for the new server, and the reconnect is repeated up to a maximum number of times (default 5) that can be specified via the <code>-m</code> option. </p>
<p> The choice of SMTP or LMTP (<code>-S</code> option) determines the syntax of the destination argument. With SMTP, one can specify a service on a non-default port as <i>host</i>:<i>service</i>, and disable MX (mail exchanger) DNS lookups with [<i>host</i>] or [<i>host</i>]:<i>port</i>. The [] form is required when you specify an IP address instead of a hostname. An IPv6 address takes the form [<code>ipv6:</code><i>address</i>]. The default port for SMTP is taken from the <code>smtp/tcp</code> entry in /etc/services, defaulting to 25 if the entry is not found. </p>
<p> With LMTP, specify <code>unix:</code><i>pathname</i> to connect to a local server listening on a unix-domain socket bound to the specified pathname; otherwise, specify an optional <code>inet:</code> prefix followed by a <i>domain</i> and an optional port, with the same syntax as for SMTP. The default TCP port for LMTP is 24. </p>
<p> Arguments:</p>
<dl>
<dt><code>-a</code> <i>family</i> (default: <code>any</code>)</p>
<dd> Address family preference: <code>ipv4</code>, <code>ipv6</code> or <code>any</code>. When using <code>any</code>, posttls-finger will randomly select one of the two as the more preferred, and exhaust all MX preferences for the first address family before trying any addresses for the other.</p>
<dt><code>-A</code> <i>trust-anchor.pem</i> (default: none)</p>
<dd> A list of PEM trust-anchor files that overrides CAfile and CApath trust chain verification. Specify the option multiple times to specify multiple files. See the main.cf documentation for smtp_tls_trust_anchor_file for details.</p>
<dt><code>-c</code></p>
<dd> Disable SMTP chat logging; only TLS-related information is logged.</p>
<dt><code>-C</code></p>
<dd> Print the remote SMTP server certificate trust chain in PEM format. The issuer DN, subject DN, certificate and public key fingerprints (see <code>-d </code><i>mdalg</i> option below) are printed above each PEM certificate block. If you specify <code>-F </code><i>CAfile</i> or <code>-P </code><i>CApath</i>, the OpenSSL library may augment the chain with missing issuer certificates. To see the actual chain sent by the remote SMTP server leave <i>CAfile</i> and <i>CApath</i> unset.</p>
<dt><code>-d </code><i>mdalg</i> (default: <code>sha1</code>)</p>
<dd> The message digest algorithm to use for reporting remote SMTP server fingerprints and matching against user provided certificate fingerprints (with DANE TLSA records the algorithm is specified in the DNS).</p>
<dt><code>-f</code></p>
<dd> Lookup the associated DANE TLSA RRset even when a hostname is not an alias and its address records lie in an unsigned zone. See smtp_tls_force_insecure_host_tlsa_lookup for details.</p>
<dt><code>-F </code><i>CAfile.pem</i> (default: none)</p>
<dd> The PEM formatted CAfile for remote SMTP server certificate verification. By default no CAfile is used and no public CAs are trusted.</p>
<dt><code>-g </code><i>grade</i> (default: medium)</p>
<dd> The minimum TLS cipher grade used by posttls-finger. See smtp_tls_mandatory_ciphers for details.</p>
<dt><code>-h </code><i>host_lookup</i> (default: <code>dns</code>)</p>
<dd> The hostname lookup methods used for the connection. See the documentation of smtp_host_lookup for syntax and semantics.</p>
<dt><code>-H </code><i>chainfiles</i> (default: <i>none</i>)</p>
<dd> List of files with a sequence PEM-encoded TLS client certificate chains. The list can be built-up incrementally, by specifying the option multiple times, or all at once via a comma or whitespace separated list of filenames. Each chain starts with a private key, which is followed immediately by the corresponding certificate, and optionally by additional issuer certificates. Each new key begins a new chain for the corresponding algorithm. This option is mutually exclusive with the below <code>-k</code> and <code>-K</code> options.</p>
<dt><code>-k </code><i>certfile</i> (default: <i>keyfile</i>)</p>
<dd> File with PEM-encoded TLS client certificate chain. This defaults to <i>keyfile</i> if one is specified.</p>
<dt><code>-K </code><i>keyfile</i> (default: <i>certfile</i>)</p>
<dd> File with PEM-encoded TLS client private key. This defaults to <i>certfile</i> if one is specified.</p>
<dt><code>-l </code><i>level</i> (default: <code>dane</code> or <code>secure</code>)</p>
<dd> The security level for the connection, default <code>dane</code> or <code>secure</code> depending on whether DNSSEC is available. For syntax and semantics, see the documentation of smtp_tls_security_level. When <code>dane</code> or <code>dane-only</code> is supported and selected, if no TLSA records are found, or all the records found are unusable, the <i>secure</i> level will be used instead. The <code>fingerprint</code> security level allows you to test certificate or public-key fingerprint matches before you deploy them in the policy table.</p>
<dt>
<dd> Note, since <code>posttls-finger</code> does not actually deliver any email, the <code>none</code>, <code>may</code> and <code>encrypt</code> security levels are not very useful. Since <code>may</code> and <code>encrypt</code> don&#8217;t require peer certificates, they will often negotiate anonymous TLS ciphersuites, so you won&#8217;t learn much about the remote SMTP server&#8217;s certificates at these levels if it also supports anonymous TLS (though you may learn that the server supports anonymous TLS).</p>
<dt><code>-L </code><i>logopts</i> (default: <code>routine,certmatch</code>)</p>
<dd> Fine-grained TLS logging options. To tune the TLS features logged during the TLS handshake, specify one or more of:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>0, none</code></p>
<dd> These yield no TLS logging; you&#8217;ll generally want more, but this is handy if you just want the trust chain:</p>
<dl>
<dt>
<dd>
<pre>
$ posttls-finger -cC -L none destination
</pre>
</dl>
<dt><code>1, routine, summary</code></p>
<dd> These synonymous values yield a normal one-line summary of the TLS connection.</p>
<dt><code>2, debug</code></p>
<dd> These synonymous values combine routine, ssl-debug, cache and verbose.</p>
<dt><code>3, ssl-expert</code></p>
<dd> These synonymous values combine debug with ssl-handshake-packet-dump. For experts only.</p>
<dt><code>4, ssl-developer</code></p>
<dd> These synonymous values combine ssl-expert with ssl-session-packet-dump. For experts only, and in most cases, use wireshark instead.</p>
<dt><code>ssl-debug</code></p>
<dd> Turn on OpenSSL logging of the progress of the SSL handshake.</p>
<dt><code>ssl-handshake-packet-dump</code></p>
<dd> Log hexadecimal packet dumps of the SSL handshake; for experts only.</p>
<dt><code>ssl-session-packet-dump</code></p>
<dd> Log hexadecimal packet dumps of the entire SSL session; only useful to those who can debug SSL protocol problems from hex dumps.</p>
<dt><code>untrusted</code></p>
<dd> Logs trust chain verification problems. This is turned on automatically at security levels that use peer names signed by Certification Authorities to validate certificates. So while this setting is recognized, you should never need to set it explicitly.</p>
<dt><code>peercert</code></p>
<dd> This logs a one line summary of the remote SMTP server certificate subject, issuer, and fingerprints.</p>
<dt><code>certmatch</code></p>
<dd> This logs remote SMTP server certificate matching, showing the CN and each subjectAltName and which name matched. With DANE, logs matching of TLSA record trust-anchor and end-entity certificates.</p>
<dt><code>cache</code></p>
<dd> This logs session cache operations, showing whether session caching is effective with the remote SMTP server. Automatically used when reconnecting with the <code>-r</code> option; rarely needs to be set explicitly.</p>
<dt><code>verbose</code></p>
<dd> Enables verbose logging in the Postfix TLS driver; includes all of peercert..cache and more.</dl>
</dl>
<dt>
<dd> The default is <code>routine,certmatch</code>. After a reconnect, <code>peercert</code>, <code>certmatch</code> and <code>verbose</code> are automatically disabled while <code>cache</code> and <code>summary</code> are enabled.</p>
<dt><code>-m </code><i>count</i> (default: <code>5</code>)</p>
<dd> When the <code>-r </code><i>delay</i> option is specified, the <code>-m</code> option determines the maximum number of reconnect attempts to use with a server behind a load balancer, to see whether connection caching is likely to be effective for this destination. Some MTAs don&#8217;t expose the underlying server identity in their EHLO response; with these servers there will never be more than 1 reconnection attempt.</p>
<dt><code>-M </code><i>insecure_mx_policy</i> (default: <code>dane</code>)</p>
<dd> The TLS policy for MX hosts with &quot;secure&quot; TLSA records when the nexthop destination security level is <code>dane</code>, but the MX record was found via an &quot;insecure&quot; MX lookup. See the main.cf documentation for smtp_tls_insecure_mx_policy for details.</p>
<dt><code>-o </code><i>name=value</i></p>
<dd> Specify zero or more times to override the value of the main.cf parameter <i>name</i> with <i>value</i>. Possible use-cases include overriding the values of TLS library parameters, or &quot;myhostname&quot; to configure the SMTP EHLO name sent to the remote server.</p>
<dt><code>-p </code><i>protocols</i> (default: !SSLv2)</p>
<dd> List of TLS protocols that posttls-finger will exclude or include. See smtp_tls_mandatory_protocols for details.</p>
<dt><code>-P </code><i>CApath/</i> (default: none)</p>
<dd> The OpenSSL CApath/ directory (indexed via <a href="/docs/linux/man/1-c_rehash/">c_rehash</a>(1)) for remote SMTP server certificate verification. By default no CApath is used and no public CAs are trusted.</p>
<dt><code>-r </code><i>delay</i></p>
<dd> With a cacheable TLS session, disconnect and reconnect after <i>delay</i> seconds. Report whether the session is re-used. Retry if a new server is encountered, up to 5 times or as specified with the <code>-m</code> option. By default reconnection is disabled, specify a positive delay to enable this behavior.</p>
<dt><code>-s </code><i>servername</i></p>
<dd> The server name to send with the TLS Server Name Indication (SNI) extension. When the server has DANE TLSA records, this parameter is ignored and the TLSA base domain is used instead. Otherwise, SNI is not used by default, but can be enabled by specifying the desired value with this option.</p>
<dt><code>-S</code></p>
<dd> Disable SMTP; that is, connect to an LMTP server. The default port for LMTP over TCP is 24. Alternative ports can specified by appending &quot;<i>:servicename</i>&quot; or &quot;:<i>portnumber</i>&quot; to the destination argument.</p>
<dt><code>-t </code><i>timeout</i> (default: <code>30</code>)</p>
<dd> The TCP connection timeout to use. This is also the timeout for reading the remote server&#8217;s 220 banner.</p>
<dt><code>-T </code><i>timeout</i> (default: <code>30</code>)</p>
<dd> The SMTP/LMTP command timeout for EHLO/LHLO, STARTTLS and QUIT.</p>
<dt><code>-v</code></p>
<dd> Enable verbose Postfix logging. Specify more than once to increase the level of verbose logging.</p>
<dt><code>-w</code></p>
<dd> Enable outgoing TLS wrapper mode, or SMTPS support. This is typically provided on port 465 by servers that are compatible with the ad-hoc SMTP in SSL protocol, rather than the standard STARTTLS protocol. The destination <i>domain</i>:<i>port</i> should of course provide such a service.</p>
<dt><code>-X</code></p>
<dd> Enable <code><a href="/docs/linux/man/8-tlsproxy/">tlsproxy</a></code>(8) mode. This is an unsupported mode, for program development only.</p>
<dt>[<code>inet:</code>]<i>domain</i>[:<i>port</i>]</p>
<dd> Connect via TCP to domain <i>domain</i>, port <i>port</i>. The default port is <code>smtp</code> (or 24 with LMTP). With SMTP an MX lookup is performed to resolve the domain to a host, unless the domain is enclosed in <code>[]</code>. If you want to connect to a specific MX host, for instance <i>mx1.example.com</i>, specify [<i>mx1.example.com</i>] as the destination and <i>example.com</i> as a <code>match</code> argument. When using DNS, the destination domain is assumed fully qualified and no default domain or search suffixes are applied; you must use fully-qualified names or also enable <code>native</code> host lookups (these don&#8217;t support <code>dane</code> or <code>dane-only</code> as no DNSSEC validation information is available via <code>native</code> lookups).</p>
<dt><code>unix:</code><i>pathname</i></p>
<dd> Connect to the UNIX-domain socket at <i>pathname</i>. LMTP only.</p>
<dt><code>match &#8230;</code></p>
<dd> With no match arguments specified, certificate peername matching uses the compiled-in default strategies for each security level. If you specify one or more arguments, these will be used as the list of certificate or public-key digests to match for the <code>fingerprint</code> level, or as the list of DNS names to match in the certificate at the <code>verify</code> and <code>secure</code> levels. If the security level is <code>dane</code>, or <code>dane-only</code> the match names are ignored, and <code>hostname, nexthop</code> strategies are used.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MAIL_CONFIG</code></p>
<dd> Read configuration parameters from a non-default location.</p>
<dt><code>MAIL_VERBOSE</code></p>
<dd> Same as <code>-v</code> option.</dl>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-smtp-source/">smtp-source</a>(1), SMTP/LMTP message source
<a href="//www.systutorials.com/docs/linux/man/1-smtp-sink/">smtp-sink</a>(1), SMTP/LMTP message dump
</pre>
<h2>README FILES</h2>
<p> Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>
TLS_README, Postfix STARTTLS howto
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
Viktor Dukhovni
</pre>
<h2>Index</h2>
