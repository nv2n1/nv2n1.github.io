---
title: "trivial-rewrite(8)"
name: "trivial-rewrite"
section: "8"
letter: "t"
url: "/docs/linux/man/8-trivial-rewrite/"
description: "trivial-rewrite – Postfix address rewriting and resolving daemon"
---

<p>trivial-rewrite &#8211; Postfix address rewriting and resolving daemon</p>
<h2>Synopsis</h2>
<pre><code>trivial-rewrite</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a></code>(8) daemon processes three types of client service requests:</p>
<dl>
<dt><code>rewrite </code><i>context address</i></p>
<dd>Rewrite an address to standard form, according to the address rewriting context:</p>
<dl>
<dd>
<dl>
<dt><code>local</code></p>
<dd>Append the domain names specified with <code>$myorigin</code> or <code>$mydomain</code> to incomplete addresses; do <code>swap_bangpath</code> and <code>allow_percent_hack</code> processing as described below, and strip source routed addresses (<i>@site,@site:user [at] domain</i>) to <i>user [at] domain</i> form.</p>
<dt><code>remote</code></p>
<dd>Append the domain name specified with <code>$remote_header_rewrite_domain</code> to incomplete addresses. Otherwise the result is identical to that of the <code>local</code> address rewriting context. This prevents Postfix from appending the local domain to spam from poorly written remote clients.</dl>
</dl>
<dt><code>resolve </code><i>sender</i> <i>address</i></p>
<dd>Resolve the address to a (<i>transport</i>, <i>nexthop</i>, <i>recipient</i>, <i>flags</i>) quadruple. The meaning of the results is as follows:</p>
<dl>
<dd>
<dl>
<dt><i>transport</i></p>
<dd>The delivery agent to use. This is the first field of an entry in the <code>master.cf</code> file.</p>
<dt><i>nexthop</i></p>
<dd>The host to send to and optional delivery method information.</p>
<dt><i>recipient</i></p>
<dd>The envelope recipient address that is passed on to <i>nexthop</i>.</p>
<dt><i>flags</i></p>
<dd>The address class, whether the address requires relaying, whether the address has problems, and whether the request failed.</dl>
</dl>
<dt><code>verify </code><i>sender</i> <i>address</i></p>
<dd>Resolve the address for address verification purposes.</dl>
<h2>Server Process Management</h2>
<p>The <code><a href="/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a></code>(8) servers run under control by the Postfix master server. Each server can handle multiple simultaneous connections. When all servers are busy while a client connects, the master creates a new server process, provided that the trivial-rewrite server process limit is not exceeded. Each trivial-rewrite server terminates after serving at least <code>$max_use</code> clients of after <code>$max_idle</code> seconds of idle time.</p>
<h2>Standards</h2>
<p>None. The command does not interact with the outside world.</p>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a></code>(8) daemon is not security sensitive. By default, this daemon does not talk to remote or local users. It can run at a fixed low privilege in a chrooted environment.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Configuration Parameters</h2>
<p>On busy mail systems a long time may pass before a <code>main.cf</code> change affecting <code><a href="/docs/linux/man/8-trivial-rewrite/">trivial-rewrite</a></code>(8) is picked up. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Compatibility Controls</h2>
<dl>
<dt><code>resolve_dequoted_address (yes)</code></p>
<dd>Resolve a recipient address safely instead of correctly, by looking inside quotes.</p>
<dt><code>resolve_null_domain (no)</code></p>
<dd>Resolve an address that ends in the &quot;@&quot; null domain as if the local hostname were specified, instead of rejecting the address as invalid.</p>
<dt><code>resolve_numeric_domain (no)</code></p>
<dd>Resolve &quot;user [at] ipaddress&quot; as &quot;user@[ipaddress]&quot;, instead of rejecting the address as invalid.</dl>
<p> Available with Postfix version 2.5 and later:</p>
<dl>
<dt><code>allow_min_user (no)</code></p>
<dd>Allow a sender or recipient address to have `-&#8216; as the first character.</dl>
<h2>Address Rewriting Controls</h2>
<dl>
<dt><code>myorigin ($myhostname)</code></p>
<dd>The domain name that locally-posted mail appears to come from, and that locally posted mail is delivered to.</p>
<dt><code>allow_percent_hack (yes)</code></p>
<dd>Enable the rewriting of the form &quot;user%domain&quot; to &quot;user [at] domain&quot;.</p>
<dt><code>append_at_myorigin (yes)</code></p>
<dd>With locally submitted mail, append the string &quot;@$myorigin&quot; to mail addresses without domain information.</p>
<dt><code>append_dot_mydomain (yes)</code></p>
<dd>With locally submitted mail, append the string &quot;.$mydomain&quot; to addresses that have no &quot;.domain&quot; information.</p>
<dt><code>recipient_delimiter (empty)</code></p>
<dd>The separator between user names and address extensions (user+foo).</p>
<dt><code>swap_bangpath (yes)</code></p>
<dd>Enable the rewriting of &quot;site!user&quot; into &quot;user [at] site&quot;.</dl>
<p> Available in Postfix 2.2 and later:</p>
<dl>
<dt><code>remote_header_rewrite_domain (empty)</code></p>
<dd>Don&#8217;t rewrite message headers from remote clients at all when this parameter is empty; otherwise, rewrite message headers and append the specified domain name to incomplete addresses.</dl>
<h2>Routing Controls</h2>
<p>The following is applicable to Postfix version 2.0 and later. Earlier versions do not have support for: virtual_transport, relay_transport, virtual_alias_domains, virtual_mailbox_domains or proxy_interfaces.</p>
<dl>
<dt><code>local_transport (local:$myhostname)</code></p>
<dd>The default mail delivery transport and next-hop destination for final delivery to domains listed with mydestination, and for [ipaddress] destinations that match $inet_interfaces or $proxy_interfaces.</p>
<dt><code>virtual_transport (virtual)</code></p>
<dd>The default mail delivery transport and next-hop destination for final delivery to domains listed with $virtual_mailbox_domains.</p>
<dt><code>relay_transport (relay)</code></p>
<dd>The default mail delivery transport and next-hop destination for remote delivery to domains listed with $relay_domains.</p>
<dt><code>default_transport (smtp)</code></p>
<dd>The default mail delivery transport and next-hop destination for destinations that do not match $mydestination, $inet_interfaces, $proxy_interfaces, $virtual_alias_domains, $virtual_mailbox_domains, or $relay_domains.</p>
<dt><code>parent_domain_matches_subdomains (see &#8216;postconf -d&#8217; output)</code></p>
<dd>What Postfix features match subdomains of &quot;domain.tld&quot; automatically, instead of requiring an explicit &quot;.domain.tld&quot; pattern.</p>
<dt><code>relayhost (empty)</code></p>
<dd>The next-hop destination of non-local mail; overrides non-local domains in recipient addresses.</p>
<dt><code>transport_maps (empty)</code></p>
<dd>Optional lookup tables with mappings from recipient address to (message delivery transport, next-hop destination).</dl>
<p> Available in Postfix version 2.3 and later:</p>
<dl>
<dt><code>sender_dependent_relayhost_maps (empty)</code></p>
<dd>A sender-dependent override for the global relayhost parameter setting.</dl>
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><code>empty_address_relayhost_maps_lookup_key (&lt;&gt;)</code></p>
<dd>The sender_dependent_relayhost_maps search string that will be used instead of the null sender address.</dl>
<p> Available in Postfix version 2.7 and later:</p>
<dl>
<dt><code>empty_address_default_transport_maps_lookup_key (&lt;&gt;)</code></p>
<dd>The sender_dependent_default_transport_maps search string that will be used instead of the null sender address.</p>
<dt><code>sender_dependent_default_transport_maps (empty)</code></p>
<dd>A sender-dependent override for the global default_transport parameter setting.</dl>
<h2>Address Verification Controls</h2>
<p>Postfix version 2.1 introduces sender and recipient address verification. This feature is implemented by sending probe email messages that are not actually delivered. By default, address verification probes use the same route as regular mail. To override specific aspects of message routing for address verification probes, specify one or more of the following:</p>
<dl>
<dt><code>address_verify_local_transport ($local_transport)</code></p>
<dd>Overrides the local_transport parameter setting for address verification probes.</p>
<dt><code>address_verify_virtual_transport ($virtual_transport)</code></p>
<dd>Overrides the virtual_transport parameter setting for address verification probes.</p>
<dt><code>address_verify_relay_transport ($relay_transport)</code></p>
<dd>Overrides the relay_transport parameter setting for address verification probes.</p>
<dt><code>address_verify_default_transport ($default_transport)</code></p>
<dd>Overrides the default_transport parameter setting for address verification probes.</p>
<dt><code>address_verify_relayhost ($relayhost)</code></p>
<dd>Overrides the relayhost parameter setting for address verification probes.</p>
<dt><code>address_verify_transport_maps ($transport_maps)</code></p>
<dd>Overrides the transport_maps parameter setting for address verification probes.</dl>
<p> Available in Postfix version 2.3 and later:</p>
<dl>
<dt><code>address_verify_sender_dependent_relayhost_maps ($sender_dependent_relayhost_maps)</code></p>
<dd>Overrides the sender_dependent_relayhost_maps parameter setting for address verification probes.</dl>
<p> Available in Postfix version 2.7 and later:</p>
<dl>
<dt><code>address_verify_sender_dependent_default_transport_maps ($sender_dependent_default_transport_maps)</code></p>
<dd>Overrides the sender_dependent_default_transport_maps parameter setting for address verification probes.</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>empty_address_recipient (MAILER-DAEMON)</code></p>
<dd>The recipient of mail addressed to the null address.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>max_use (100)</code></p>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</p>
<dt><code>relocated_maps (empty)</code></p>
<dd>Optional lookup tables with new contact information for users or domains that no longer exist.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The location of the Postfix top-level queue directory.</p>
<dt><code>show_user_unknown_table_name (yes)</code></p>
<dd>Display the name of the recipient table in the &quot;User unknown&quot; responses.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<p> Available in Postfix version 2.0 and later:</p>
<dl>
<dt><code>helpful_warnings (yes)</code></p>
<dd>Log warnings about problematic configuration settings, and provide helpful suggestions.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-transport/">transport</a>(5), transport table format
<a href="//www.systutorials.com/docs/linux/man/5-relocated/">relocated</a>(5), format of the &quot;user has moved&quot; table
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>ADDRESS_CLASS_README, Postfix address classes howto
ADDRESS_VERIFICATION_README, Postfix address verification</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
