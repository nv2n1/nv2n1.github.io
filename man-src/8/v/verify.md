---
title: "verify(8)"
name: "verify"
section: "8"
letter: "v"
url: "/docs/linux/man/8-verify/"
description: "verify – Postfix address verification server"
---

<p>verify &#8211; Postfix address verification server</p>
<h2>Synopsis</h2>
<pre><code>verify</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) address verification server maintains a record of what recipient addresses are known to be deliverable or undeliverable. </p>
<p> Addresses are verified by injecting probe messages into the Postfix queue. Probe messages are run through all the routing and rewriting machinery except for final delivery, and are discarded rather than being deferred or bounced. </p>
<p> Address verification relies on the answer from the nearest MTA for the specified address, and will therefore not detect all undeliverable addresses. </p>
<p> The <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) server is designed to run under control by the Postfix master server. It maintains an optional persistent database. To avoid being interrupted by &quot;postfix stop&quot; in the middle of a database update, the process runs in a separate process group. </p>
<p> The <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) server implements the following requests:</p>
<dl>
<dt><code>update</code><i> address status text</i></p>
<dd>Update the status and text of the specified address.</p>
<dt><code>query</code><i> address</i></p>
<dd>Look up the <i>status</i> and <i>text</i> for the specified <i>address</i>. If the status is unknown, a probe is sent and an &quot;in progress&quot; status is returned.</dl>
<h2>Security</h2>
<p>The address verification server is not security-sensitive. It does not talk to the network, and it does not talk to local users. The verify server can run chrooted at fixed low privilege. </p>
<p> The address verification server can be coerced to store unlimited amounts of garbage. Limiting the cache expiry time trades one problem (disk space exhaustion) for another one (poor response time to client requests). </p>
<p> With Postfix version 2.5 and later, the <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) server no longer uses root privileges when opening the <code>address_verify_map</code> cache file. The file should now be stored under the Postfix-owned <code>data_directory</code>. As a migration aid, an attempt to open a cache file under a non-Postfix directory is redirected to the Postfix-owned <code>data_directory</code>, and a warning is logged.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Bugs</h2>
<p>Address verification probe messages add additional traffic to the mail queue. Recipient verification may cause an increased load on down-stream servers in the case of a dictionary attack or a flood of backscatter bounces. Sender address verification may cause your site to be blacklisted by some providers. </p>
<p> If the persistent database ever gets corrupted then the world comes to an end and human intervention is needed. This violates a basic Postfix principle.</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are not picked up automatically, as <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) processes are long-lived. Use the command &quot;<code>postfix reload</code>&quot; after a configuration change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Probe Message Controls</h2>
<dl>
<dt><code>address_verify_sender ($double_bounce_sender)</code></p>
<dd>The sender address to use in address verification probes; prior to Postfix 2.5 the default was &quot;postmaster&quot;.</dl>
<p> Available with Postfix 2.9 and later:</p>
<dl>
<dt><code>address_verify_sender_ttl (0s)</code></p>
<dd>The time between changes in the time-dependent portion of address verification probe sender addresses.</dl>
<h2>Cache Controls</h2>
<dl>
<dt><code>address_verify_map (see &#8216;postconf -d&#8217; output)</code></p>
<dd>Lookup table for persistent address verification status storage.</p>
<dt><code>address_verify_positive_expire_time (31d)</code></p>
<dd>The time after which a successful probe expires from the address verification cache.</p>
<dt><code>address_verify_positive_refresh_time (7d)</code></p>
<dd>The time after which a successful address verification probe needs to be refreshed.</p>
<dt><code>address_verify_negative_cache (yes)</code></p>
<dd>Enable caching of failed address verification probe results.</p>
<dt><code>address_verify_negative_expire_time (3d)</code></p>
<dd>The time after which a failed probe expires from the address verification cache.</p>
<dt><code>address_verify_negative_refresh_time (3h)</code></p>
<dd>The time after which a failed address verification probe needs to be refreshed.</dl>
<p> Available with Postfix 2.7 and later:</p>
<dl>
<dt><code>address_verify_cache_cleanup_interval (12h)</code></p>
<dd>The amount of time between <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) address verification database cleanup runs.</dl>
<h2>Probe Message Routing Controls</h2>
<p>By default, probe messages are delivered via the same route as regular messages. The following parameters can be used to override specific message routing mechanisms.</p>
<dl>
<dt><code>address_verify_relayhost ($relayhost)</code></p>
<dd>Overrides the relayhost parameter setting for address verification probes.</p>
<dt><code>address_verify_transport_maps ($transport_maps)</code></p>
<dd>Overrides the transport_maps parameter setting for address verification probes.</p>
<dt><code>address_verify_local_transport ($local_transport)</code></p>
<dd>Overrides the local_transport parameter setting for address verification probes.</p>
<dt><code>address_verify_virtual_transport ($virtual_transport)</code></p>
<dd>Overrides the virtual_transport parameter setting for address verification probes.</p>
<dt><code>address_verify_relay_transport ($relay_transport)</code></p>
<dd>Overrides the relay_transport parameter setting for address verification probes.</p>
<dt><code>address_verify_default_transport ($default_transport)</code></p>
<dd>Overrides the default_transport parameter setting for address verification probes.</dl>
<p> Available in Postfix 2.3 and later:</p>
<dl>
<dt><code>address_verify_sender_dependent_relayhost_maps ($sender_dependent_relayhost_maps)</code></p>
<dd>Overrides the sender_dependent_relayhost_maps parameter setting for address verification probes.</dl>
<p> Available in Postfix 2.7 and later:</p>
<dl>
<dt><code>address_verify_sender_dependent_default_transport_maps ($sender_dependent_default_transport_maps)</code></p>
<dd>Overrides the sender_dependent_default_transport_maps parameter setting for address verification probes.</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The location of the Postfix top-level queue directory.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a>(8), Postfix SMTP server
<a href="//www.systutorials.com/docs/linux/man/8-cleanup/">cleanup</a>(8), enqueue Postfix message
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-syslogd/">syslogd</a>(5), system logging</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>ADDRESS_VERIFICATION_README, address verification howto</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>This service was introduced with Postfix version 2.1.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
