---
title: "rndc(8)"
name: "rndc"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rndc/"
description: "rndc – name server control utility"
---

<p>rndc &#8211; name server control utility</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>rndc</code> [<code>-b&nbsp;<wbr></code><i>source-address</i>] [<code>-c&nbsp;<wbr></code><i>config-file</i>] [<code>-k&nbsp;<wbr></code><i>key-file</i>] [<code>-s&nbsp;<wbr></code><i>server</i>] [<code>-p&nbsp;<wbr></code><i>port</i>] [<code>-V</code>] [<code>-y&nbsp;<wbr></code><i>key_id</i>] {command}</dl>
<h2>Description</h2>
<p><code>rndc</code></p>
<dd>controls the operation of a name server. It supersedes the <code>ndc</code> utility that was provided in old BIND releases. If <code>rndc</code> is invoked with no command line options or arguments, it prints a short summary of the supported commands and the available options and their arguments. </p>
<p> <code>rndc</code> communicates with the name server over a TCP connection, sending commands authenticated with digital signatures. In the current versions of <code>rndc</code> and <code>named</code>, the only supported authentication algorithm is HMAC-MD5, which uses a shared secret on each end of the connection. This provides TSIG-style authentication for the command request and the name server&#8217;s response. All commands sent over the channel must be signed by a key_id known to the server. </p>
<p> <code>rndc</code> reads a configuration file to determine how to contact the name server and decide what algorithm and key it should use.</p>
<h2>Options</h2>
<p>-b <i>source-address</i></p>
<dl>
<dd>Use <i>source-address</i> as the source address for the connection to the server. Multiple instances are permitted to allow setting of both the IPv4 and IPv6 source addresses.</dl>
<p> -c <i>config-file</i></p>
<dl>
<dd>Use <i>config-file</i> as the configuration file instead of the default, <i>/etc/rndc.conf</i>.</dl>
<p> -k <i>key-file</i></p>
<dl>
<dd>Use <i>key-file</i> as the key file instead of the default, <i>/etc/rndc.key</i>. The key in <i>/etc/rndc.key</i> will be used to authenticate commands sent to the server if the <i>config-file</i> does not exist.</dl>
<p> -s <i>server</i></p>
<dl>
<dd><i>server</i> is the name or address of the server which matches a server statement in the configuration file for <code>rndc</code>. If no server is supplied on the command line, the host named by the default-server clause in the options statement of the <code>rndc</code> configuration file will be used.</dl>
<p> -p <i>port</i></p>
<dl>
<dd>Send commands to TCP port <i>port</i> instead of BIND 9&#8217;s default control channel port, 953.</dl>
<p> -V</p>
<dl>
<dd>Enable verbose logging.</dl>
<p> -y <i>key_id</i></p>
<dl>
<dd>Use the key <i>key_id</i> from the configuration file. <i>key_id</i> must be known by named with the same algorithm and secret string in order for control message validation to succeed. If no <i>key_id</i> is specified, <code>rndc</code> will first look for a key clause in the server statement of the server being used, or if no server statement is present for that host, then the default-key clause of the options statement. Note that the configuration file contains shared secrets which are used to send authenticated control commands to name servers. It should therefore not have general read or write access.</dl>
<h2>Commands</h2>
<p>A list of commands supported by <code>rndc</code> can be seen by running <code>rndc</code> without arguments. </p>
<p> Currently supported commands are: </p>
<p> <code>reload</code></p>
<dl>
<dd>Reload configuration file and zones.</dl>
<p> <code>reload </code><i>zone</i><code>[</code><i>class</i> [<i>view</i>]]</p>
<dl>
<dd>Reload the given zone.</dl>
<p> <code>refresh </code><i>zone</i><code>[</code><i>class</i> [<i>view</i>]]</p>
<dl>
<dd>Schedule zone maintenance for the given zone.</dl>
<p> <code>retransfer </code><i>zone</i><code>[</code><i>class</i> [<i>view</i>]]</p>
<dl>
<dd>Retransfer the given zone from the master.</dl>
<p> <code>sign </code><i>zone</i><code>[</code><i>class</i> [<i>view</i>]]</p>
<dl>
<dd>Fetch all DNSSEC keys for the given zone from the key directory (see the <code>key-directory</code> option in the BIND 9 Administrator Reference Manual). If they are within their publication period, merge them into the zone&#8217;s DNSKEY RRset. If the DNSKEY RRset is changed, then the zone is automatically re-signed with the new key set. </p>
<p> This command requires that the <code>auto-dnssec</code> zone option be set to allow or maintain, and also requires the zone to be configured to allow dynamic DNS. (See &quot;Dynamic Update Policies&quot; in the Administrator Reference Manual for more details.)</dl>
<p> <code>loadkeys </code><i>zone</i><code>[</code><i>class</i> [<i>view</i>]]</p>
<dl>
<dd>Fetch all DNSSEC keys for the given zone from the key directory. If they are within their publication period, merge them into the zone&#8217;s DNSKEY RRset. Unlike <code>rndc sign</code>, however, the zone is not immediately re-signed by the new keys, but is allowed to incrementally re-sign over time. </p>
<p> This command requires that the <code>auto-dnssec</code> zone option be set to maintain, and also requires the zone to be configured to allow dynamic DNS. (See &quot;Dynamic Update Policies&quot; in the Administrator Reference Manual for more details.)</dl>
<p> <code>freeze </code><code>[</code><i>zone</i> [<i>class</i> [<i>view</i>]]]</p>
<dl>
<dd>Suspend updates to a dynamic zone. If no zone is specified, then all zones are suspended. This allows manual edits to be made to a zone normally updated by dynamic update. It also causes changes in the journal file to be synced into the master file. All dynamic update attempts will be refused while the zone is frozen.</dl>
<p> <code>thaw </code><code>[</code><i>zone</i> [<i>class</i> [<i>view</i>]]]</p>
<dl>
<dd>Enable updates to a frozen dynamic zone. If no zone is specified, then all frozen zones are enabled. This causes the server to reload the zone from disk, and re-enables dynamic updates after the load has completed. After a zone is thawed, dynamic updates will no longer be refused. If the zone has changed and the <code>ixfr-from-differences</code> option is in use, then the journal file will be updated to reflect changes in the zone. Otherwise, if the zone has changed, any existing journal file will be removed.</dl>
<p> <code>sync </code><code>[-clean]</code><code>[</code><i>zone</i> [<i>class</i> [<i>view</i>]]]</p>
<dl>
<dd>Sync changes in the journal file for a dynamic zone to the master file. If the &quot;-clean&quot; option is specified, the journal file is also removed. If no zone is specified, then all zones are synced.</dl>
<p> <code>notify </code><i>zone</i><code>[</code><i>class</i> [<i>view</i>]]</p>
<dl>
<dd>Resend NOTIFY messages for the zone.</dl>
<p> <code>reconfig</code></p>
<dl>
<dd>Reload the configuration file and load new zones, but do not reload existing zone files even if they have changed. This is faster than a full <code>reload</code> when there is a large number of zones because it avoids the need to examine the modification times of the zones files.</dl>
<p> <code>stats</code></p>
<dl>
<dd>Write server statistics to the statistics file.</dl>
<p> <code>querylog</code> [on|off]</p>
<dl>
<dd>Enable or disable query logging. (For backward compatibility, this command can also be used without an argument to toggle query logging on and off.) </p>
<p> Query logging can also be enabled by explicitly directing the <code>queries</code> <code>category</code> to a <code>channel</code> in the <code>logging</code> section of <i>named.conf</i> or by specifying <code>querylog yes;</code> in the <code>options</code> section of <i>named.conf</i>.</dl>
<p> <code>dumpdb </code><code>[-all|-cache|-zone]</code><code>[</code><i>view &#8230;</i>]</p>
<dl>
<dd>Dump the server&#8217;s caches (default) and/or zones to the dump file for the specified views. If no view is specified, all views are dumped.</dl>
<p> <code>secroots </code><code>[</code><i>view &#8230;</i>]</p>
<dl>
<dd>Dump the server&#8217;s security roots to the secroots file for the specified views. If no view is specified, security roots for all views are dumped.</dl>
<p> <code>stop </code><code>[-p]</code></p>
<dl>
<dd>Stop the server, making sure any recent changes made through dynamic update or IXFR are first saved to the master files of the updated zones. If <code>-p</code> is specified <code>named</code>&#8216;s process id is returned. This allows an external process to determine when <code>named</code> had completed stopping.</dl>
<p> <code>halt </code><code>[-p]</code></p>
<dl>
<dd>Stop the server immediately. Recent changes made through dynamic update or IXFR are not saved to the master files, but will be rolled forward from the journal files when the server is restarted. If <code>-p</code> is specified <code>named</code>&#8216;s process id is returned. This allows an external process to determine when <code>named</code> had completed halting.</dl>
<p> <code>trace</code></p>
<dl>
<dd>Increment the servers debugging level by one.</dl>
<p> <code>trace </code><i>level</i></p>
<dl>
<dd>Sets the server&#8217;s debugging level to an explicit value.</dl>
<p> <code>notrace</code></p>
<dl>
<dd>Sets the server&#8217;s debugging level to 0.</dl>
<p> <code>flush</code></p>
<dl>
<dd>Flushes the server&#8217;s cache.</dl>
<p> <code>flushname</code> <i>name</i> [<i>view</i>]</p>
<dl>
<dd>Flushes the given name from the server&#8217;s DNS cache and, if applicable, from the server&#8217;s nameserver address database or bad-server cache.</dl>
<p> <code>flushtree</code> <i>name</i> [<i>view</i>]</p>
<dl>
<dd>Flushes the given name, and all of its subdomains, from the server&#8217;s DNS cache. Note that this does <i>not</i> affect he server&#8217;s address database or bad-server cache.</dl>
<p> <code>status</code></p>
<dl>
<dd>Display status of the server. Note that the number of zones includes the internal <code>bind/CH</code> zone and the default <code>./IN</code> hint zone if there is not an explicit root zone configured.</dl>
<p> <code>recursing</code></p>
<dl>
<dd>Dump the list of queries <code>named</code> is currently recursing on.</dl>
<p> <code>validation ( on | off | check ) </code><code>[</code><i>view &#8230;</i>]</p>
<dl>
<dd>Enable, disable, or check the current status of DNSSEC validation. Note <code>dnssec-enable</code> also needs to be set to <code>yes</code> or <code>auto</code> to be effective. It defaults to enabled.</dl>
<p> <code>tsig-list</code></p>
<dl>
<dd>List the names of all TSIG keys currently configured for use by <code>named</code> in each view. The list both statically configured keys and dynamic TKEY-negotiated keys.</dl>
<p> <code>tsig-delete</code> <i>keyname</i> [<i>view</i>]</p>
<dl>
<dd>Delete a given TKEY-negotiated key from the server. (This does not apply to statically configured TSIG keys.)</dl>
<p> <code>addzone </code><i>zone</i><code>[</code><i>class</i> [<i>view</i>]]<i>configuration</i></p>
<dl>
<dd>Add a zone while the server is running. This command requires the <code>allow-new-zones</code> option to be set to <code>yes</code>. The <i>configuration</i> string specified on the command line is the zone configuration text that would ordinarily be placed in <i>named.conf</i>. </p>
<p> The configuration is saved in a file called <i>hash</i><i>.nzf</i>, where <i>hash</i> is a cryptographic hash generated from the name of the view. When <code>named</code> is restarted, the file will be loaded into the view configuration, so that zones that were added can persist after a restart. </p>
<p> This sample <code>addzone</code> command would add the zone example.com to the default view: </p>
<p> $<code>rndc addzone example.com &#8216;{ type master; file &quot;example.com.db&quot;; };&#8217;</code> </p>
<p> (Note the brackets and semi-colon around the zone configuration text.)</dl>
<p> <code>delzone </code><i>zone</i><code>[</code><i>class</i> [<i>view</i>]]</p>
<dl>
<dd>Delete a zone while the server is running. Only zones that were originally added via <code>rndc addzone</code> can be deleted in this manner.</dl>
<p> <code>signing </code><code>[( -list | -clear </code><i>keyid/algorithm</i> | -clear all | -nsec3param ( <i>parameters</i> | none ) ) ]<i>zone</i><code>[</code><i>class</i> [<i>view</i>]]</p>
<dl>
<dd>List, edit, or remove the DNSSEC signing state for the specified zone. The status of ongoing DNSSEC operations (such as signing or generating NSEC3 chains) is stored in the zone in the form of DNS resource records of type <code>sig-signing-type</code>. <code>rndc signing -list</code> converts these records into a human-readable form, indicating which keys are currently signing or have finished signing the zone, and which NSEC3 chains are being created or removed. </p>
<p> <code>rndc signing -clear</code> can remove a single key (specified in the same format that <code>rndc signing -list</code> uses to display it), or all keys. In either case, only completed keys are removed; any record indicating that a key has not yet finished signing the zone will be retained. </p>
<p> <code>rndc signing -nsec3param</code> sets the NSEC3 parameters for a zone. This is the only supported mechanism for using NSEC3 with <code>inline-signing</code> zones. Parameters are specified in the same format as an NSEC3PARAM resource record: hash algorithm, flags, iterations, and salt, in that order. </p>
<p> Currently, the only defined value for hash algorithm is 1, representing SHA-1. The <code>flags</code> may be set to 0 or 1, depending on whether you wish to set the opt-out bit in the NSEC3 chain. <code>iterations</code> defines the number of additional times to apply the algorithm when generating an NSEC3 hash. The <code>salt</code> is a string of data expressed in hexidecimal, or a hyphen (`-&#8216;) if no salt is to be used. </p>
<p> So, for example, to create an NSEC3 chain using the SHA-1 hash algorithm, no opt-out flag, 10 iterations, and a salt value of &quot;FFFF&quot;, use: <code>rndc signing -nsec3param 1 0 10 FFFF </code><i>zone</i>. To set the opt-out flag, 15 iterations, and no salt, use: <code>rndc signing -nsec3param 1 1 15 &#8211; </code><i>zone</i>. </p>
<p> <code>rndc signing -nsec3param none</code> removes an existing NSEC3 chain and replaces it with NSEC.</dl>
<h2>Limitations</h2>
<p>There is currently no way to provide the shared secret for a <code>key_id</code> without using the configuration file. </p>
<p> Several error messages could be clearer.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-rndc-conf/">rndc.conf</a></code>(5), <code><a href="/docs/linux/man/8-rndc-confgen/">rndc-confgen</a></code>(8), <code><a href="/docs/linux/man/8-named/">named</a></code>(8), <code><a href="/docs/linux/man/5-named-conf/">named.conf</a></code>(5), <code><a href="/docs/linux/man/8-ndc/">ndc</a></code>(8), BIND 9 Administrator Reference Manual.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004, 2005, 2007, 2013 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium.</p>
