---
title: "nsd(5)"
name: "nsd"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nsd/"
description: "nsd.conf – NSD configuration file"
---

<p><code>nsd.conf</code> &#8211; NSD configuration file</p>
<h2>Synopsis</h2>
<p><code>nsd.conf</code></p>
<h2>Description</h2>
<p><code>Nsd.conf</code> is used to configure <a href="/docs/linux/man/8-nsd/">nsd</a>(8). The file format has attributes and values. Some attributes have attributes inside them. The notation is: attribute: value. </p>
<p> Comments start with # and last to the end of line. Empty lines are ignored as is whitespace at the beginning of a line. </p>
<p> <code>Nsd.conf</code> specifies options for the nsd server, zone files, primaries and secondaries.</p>
<h2>Example</h2>
<p>An example of a short nsd.conf file is below. </p>
<p> # Example.com nsd.conf file</p>
<dl>
<dd># This is a comment.</dl>
<dl>
<dt>server:</p>
<dd>
<dl>
<dd>database: &quot;/var/db/nsd/nsd.db&quot;</dl>
<dl>
<dd>username: nsd</dl>
<dl>
<dd>logfile: &quot;/var/log/nsd.log&quot;</dl>
<dl>
<dd>pidfile: &quot;/var/run/nsd.pid&quot;</dl>
<dl>
<dd>difffile: &quot;/var/db/nsd/ixfr.db&quot;</dl>
<dl>
<dd>xfrdfile: &quot;/var/db/nsd/xfrd.state&quot;</dl>
<dt>zone:</p>
<dd>
<dl>
<dd>name: example.com</dl>
<dl>
<dd># note that quotes are optional on the value</dl>
<dl>
<dd>zonefile: /etc/nsd/example.com.zone</dl>
</dl>
<h2>File Format</h2>
<p>There must be whitespace between keywords. Attribute keywords end with a colon &#8216;:&#8217;. An attribute is followed by its containing attributes, or a value. At the top level only <code>server:</code> or <code>zone: </code> or <code>key: </code> are allowed. These are followed by their attributes or the start of a new <code>server:</code> or <code>zone: </code> or <code>key: </code> clause. The <code>zone:</code> attribute is followed by zone options. The <code>server: </code> attribute is followed by global options for the <code>NSD </code> server. A <code>key: </code> attribute is used to define keys for authentication. Files can be included using the <code>include:</code> directive. It can appear anywhere, and takes a single filename as an argument. Processing continues as if the text from the included file was copied into the config file at that point. </p>
<p> The global options (if not overridden from the NSD commandline) are taken from the <code>server: </code> clause. There may only be one <code>server: </code> clause.</p>
<dl>
<dt><code>ip-address:</code> &lt;ip4 or ip6&gt;</p>
<dd>NSD will bind to the listed ip-address. Can be give multiple times to bind multiple ip-addresses. If none are given NSD listens to all IP addresses. Same as commandline option <code>-a.</code></p>
<dt><code>debug-mode:</code> &lt;yes or no&gt;</p>
<dd>Turns on debugging mode for nsd, does not fork a daemon process. Default is no. Same as commandline option <code>-d.</code></p>
<dt><code>ip4-only:</code> &lt;yes or no&gt;</p>
<dd>If yes, NSD only listens to IPv4 connections. Same as commandline option <code>-4.</code></p>
<dt><code>ip6-only:</code> &lt;yes or no&gt;</p>
<dd>If yes, NSD only listens to IPv6 connections. Same as commandline option <code>-6.</code></p>
<dt><code>database:</code> &lt;filename&gt;</p>
<dd>By default <i>/var/db/nsd/nsd.db</i> is used. The specified file is used to store the compiled zone information. Same as commandline option <code>-f.</code></p>
<dt><code>identity:</code> &lt;string&gt;</p>
<dd>Returns the specified identity when asked for CH TXT ID.SERVER. Default is the name as returned by <a href="/docs/linux/man/3-gethostname/">gethostname</a>(3). Same as commandline option <code>-i</code>.</p>
<dt><code>logfile:</code> &lt;filename&gt;</p>
<dd>Log messages to the logfile. The default is to log to stderr and syslog. Same as commandline option <code>-l</code>.</p>
<dt><code>server-count:</code> &lt;number&gt;</p>
<dd>
<dt><code>server-count:</code> &lt;number&gt;</p>
<dd>Start this many NSD servers. Default is 1. Same as commandline option <code>-N</code>.</p>
<dt><code>tcp-count:</code> &lt;number&gt;</p>
<dd>The maximum number of concurrent, active TCP connections by each server. Default is 10. This option should have a value below 1000. Same as commandline option <code>-n</code>.</p>
<dt><code>tcp-query-count:</code> &lt;number&gt;</p>
<dd>The maximum number of queries served on a single TCP connection. Default is 0, meaning there is no maximum.</p>
<dt><code>tcp-timeout:</code> &lt;number&gt;</p>
<dd>Overrides the default TCP timeout. This also affects zone transfers over TCP.</p>
<dt><code>ipv4-edns-size:</code> &lt;number&gt;</p>
<dd>Preferred EDNS buffer size for IPv4.</p>
<dt><code>ipv6-edns-size:</code> &lt;number&gt;</p>
<dd>Preferred EDNS buffer size for IPv6.</p>
<dt><code>pidfile:</code> &lt;filename&gt;</p>
<dd>Use the pid file instead of the platform specific default, usually <i>/var/run/nsd.pid.</i> Same as commandline option <code>-P</code>.</p>
<dt><code>port:</code> &lt;number&gt;</p>
<dd>Answer queries on the specified port. Default is 53. Same as commandline option <code>-p</code>.</p>
<dt><code>statistics:</code> &lt;number&gt;</p>
<dd>If not present no statistics are dumped. Statistics are produced every number seconds. Same as commandline option <code>-s</code>.</p>
<dt><code>chroot:</code> &lt;directory&gt;</p>
<dd>NSD will chroot on startup to the specified directory. Same as commandline option <code>-t</code>.</p>
<dt><code>username:</code> &lt;username&gt;</p>
<dd>After binding the socket, drop user privileges and assume the username. Can be username, id or id.gid. Same as commandline option <code>-u</code>.</p>
<dt><code>zonesdir:</code> &lt;directory&gt;</p>
<dd>Change the working directory to the specified directory before accessing zone files. Same as commandline option <code>-d </code> for <a href="/docs/linux/man/8-zonec/">zonec</a>(8). Also <a href="/docs/linux/man/8-nsd/">nsd</a>(8) will access files (pid file, database file, log file) relative to this directory. Set the value to &quot;&quot; (the empty string) to disable the change of working directory.</p>
<dt><code>difffile:</code> &lt;filename&gt;</p>
<dd>When NSD receives IXFR updates it will store them in this file. This file contains the differences between the database file and the latest zone version. Default is <i>/var/db/nsd/ixfr.db</i>.</p>
<dt><code>xfrdfile:</code> &lt;filename&gt;</p>
<dd>The soa timeout and zone transfer daemon in NSD will save its state to this file. State is read back after a restart. The state file can be deleted without too much harm, but timestamps of zones will be gone. For more details see the section on zone expiry behavior of NSD. Default is <i>/var/db/nsd/xfrd.state</i>.</p>
<dt><code>xrfd-reload-timeout:</code> &lt;number&gt;</p>
<dd>If this value is -1, xfrd will not trigger a reload after a zone transfer. If positive xfrd will trigger a reload after a zone transfer, then it will wait for the number of seconds before it will trigger a new reload. Setting this value throttles the reloads to once per the number of seconds. The default is 10 seconds.</p>
<dt><code>verbosity:</code> &lt;level&gt;</p>
<dd>This value specifies the verbosity level for (non-debug) logging. Default is 0. 1 gives more information about incoming notifies and zone transfers. 2 lists soft warnings that are encountered.</p>
<dt><code>hide-version:</code> &lt;yes or no&gt;</p>
<dd>Prevent NSD from replying with the version string on CHAOS class queries.</dl>
<h3>Zone Options</h3>
<p>For every zone the options need to be specified in one <code>zone: </code> clause. The access control list elements can be given multiple times to add multiple servers.</p>
<dl>
<dt><code>name:</code> &lt;string&gt;</p>
<dd>The name of the zone. This is the domain name of the apex of the zone. May end with a &#8216;.&#8217; (in FQDN notation). For example &quot;example.com&quot;, &quot;sub.example.net.&quot;. This attribute must be present in each zone.</p>
<dt><code>zonefile:</code> &lt;filename&gt;</p>
<dd>The file containing the zone information. This file is used by <a href="/docs/linux/man/8-zonec/">zonec</a>(8). This attribute must be present in each zone.</p>
<dt><code>allow-notify:</code> &lt;ip-spec&gt; &lt;key-name | NOKEY | BLOCKED&gt;</p>
<dd>Access control list. The listed (primary) address is allowed to send notifies to this (secondary) server. Notifies from unlisted or specifically BLOCKED addresses are discarded. If NOKEY is given no TSIG signature is required.</p>
<dl>
<dd>The ip-spec is either a plain IP address (IPv4 or IPv6), or can be a subnet of the form 1.2.3.4/24, or masked like 1.2.3.4&amp;255.255.255.0 or a range of the form 1.2.3.4-1.2.3.25. A port number can be added using a suffix of @number, for example 1.2.3.4 [at] 5300 or 1.2.3.4/24 [at] 5300 for port 5300. Note the ip-spec ranges do not use spaces around the /, &amp;, @ and &#8211; symbols.</dl>
<dt><code>request-xfr:</code> [AXFR|UDP] &lt;ip-address&gt; &lt;key-name | NOKEY&gt;</p>
<dd>Access control list. The listed address (the master) is queried for AXFR/IXFR on update. The specified key is used during AXFR/IXFR.</p>
<dl>
<dd>If the AXFR option is given, the server will not be contacted with IXFR queries but only AXFR requests will be made to the server. This allows an NSD secondary to have a master server that runs NSD. If the AXFR option is left out then both IXFR and AXFR requests are made to the master server. If the UDP option is given, the secondary will use UDP to transmit the IXFR requests. You should deploy TSIG when allowing UDP transport, to authenticate notifies and zone transfers. Otherwise, NSD is more vulnerable for Kaminsky-style attacks. If the UDP option is left out then IXFR will be transmitted using TCP.</dl>
<dt><code>allow-axfr-fallback:</code> &lt;yes or no&gt;</p>
<dd>This option should be accompanied by request-xfr. It (dis)allows NSD (as secondary) to fallback to AXFR if the primary name server does not support IXFR.</p>
<dt><code>notify:</code> &lt;ip-address&gt; &lt;key-name | NOKEY&gt;</p>
<dd>Access control list. The listed address (a secondary) is notified of updates to this zone. The specified key is used to sign the notify. Only on secondary configurations will NSD be able to detect zone updates (as it gets notified itself, or refreshes after a time).</p>
<dt><code>notify-retry:</code> &lt;number&gt;</p>
<dd>This option should be accompanied by notify. It sets the number of retries when sending notifies.</p>
<dt><code>provide-xfr:</code> &lt;ip-spec&gt; &lt;key-name | NOKEY | BLOCKED&gt;</p>
<dd>Access control list. The listed address (a secondary) is allowed to request AXFR from this server. Zone data will be provided to the address. The specified key is used during AXFR. For unlisted or BLOCKED addresses no data is provided, requests are discarded.</p>
<dl>
<dd>The ip-spec is either a plain IP address (IPv4 or IPv6), or can be a subnet of the form 1.2.3.4/24, or masked like 1.2.3.4&amp;255.255.255.0 or a range of the form 1.2.3.4-1.2.3.25. A port number can be added using a suffix of @number, for example 1.2.3.4 [at] 5300 or 1.2.3.4/24 [at] 5300 for port 5300. Note the ip-spec ranges do not use spaces around the /, &amp;, @ and &#8211; symbols.</dl>
<dt><code>outgoing-interface:</code> &lt;ip-address&gt;</p>
<dd>Access control list. The listed address is used to request AXFR|IXFR (in case of a secondary) or used to send notifies (in case of a primary).</p>
<dl>
<dd>The ip-address is either a plain IP address (IPv4 or IPv6), or can be a subnet of the form 1.2.3.4/24, or masked like 1.2.3.4&amp;255.255.255.0 or a range of the form 1.2.3.4-1.2.3.25.</dl>
</dl>
<h3>Key Declarations</h3>
<p>The <code>key: </code> clause establishes a key for use in access control lists. It has the following attributes.</p>
<dl>
<dt><code>name:</code> &lt;string&gt;</p>
<dd>The key name. Used to refer to this key in the access control list.</p>
<dt><code>algorithm:</code> &lt;string&gt;</p>
<dd>Authentication algorithm for this key.</p>
<dt><code>secret:</code> &lt;base64 blob&gt;</p>
<dd>The base64 encoded shared secret. It is possible to put the <code>secret:</code> declaration (and base64 blob) into a different file, and then to <code>include:</code> that file. In this way the key secret and the rest of the configuration file, which may have different security policies, can be split apart.</dl>
<h2>Nsd Configuration For Bind9 Hackers</h2>
<p>BIND9 is a name server implementation with its own configuration file format, <a href="/docs/linux/man/5-named-conf/">named.conf</a>(5). BIND9 types zones as &#8216;Master&#8217; or</p>
<h3>Slave zones</h3>
<p>For a slave zone, the master servers are listed. The master servers are queried for zone data, and are listened to for update notifications. In NSD these two properties need to be configured seperately, by listing the master address in allow-notify and request-xfr statements. In BIND9 you only need to provide allow-notify elements for any extra sources of notifications (i.e. the operators), NSD needs to have allow-notify for both masters and operators. BIND9 allows additional transfer sources, in NSD you list those as request-xfr. Here is an example of a slave zone in BIND9 syntax. # Config file for example.org options {</p>
<dl>
<dd>dnssec-enable yes;</dl>
<dl>
<dd>};</dl>
<p> key tsig.example.org. {</p>
<dl>
<dd>algorithm hmac-md5;</dl>
<dl>
<dd>secret &quot;aaaaaabbbbbbccccccdddddd&quot;;</dl>
<p> }; </p>
<p> server 162.0.4.49 {</p>
<dl>
<dd>keys { tsig.example.org. ; };</dl>
<p> }; </p>
<p> zone &quot;example.org&quot; {</p>
<dl>
<dd>type slave;</dl>
<dl>
<dd>file &quot;secondary/example.org.signed&quot;;</dl>
<dl>
<dd>masters { 162.0.4.49; };</dl>
<p> }; For NSD, DNSSEC is enabled automatically for zones that are signed. The dnssec-enable statement in the options clause is not needed. In NSD keys are associated with an IP address in the access control list statement, therefore the server{} statement is not needed. Below is the same example in an NSD config file. </p>
<p> # Config file for example.org</p>
<dl>
<dd>key:</dl>
<dl>
<dd>name: tsig.example.org.</dl>
<dl>
<dd>algorithm: hmac-md5</dl>
<dl>
<dd>secret: &quot;aaaaaabbbbbbccccccdddddd&quot;</dl>
<p> zone:</p>
<dl>
<dd>name: &quot;example.org&quot;</dl>
<dl>
<dd>zonefile: &quot;secondary/example.org.signed&quot;</dl>
<dl>
<dd># the master is allowed to notify and will provide zone data.</dl>
<dl>
<dd>allow-notify: 162.0.4.49 NOKEY</dl>
<dl>
<dd>request-xfr: 162.0.4.49 tsig.example.org.</dl>
<p> Notice that the master is listed twice, once to allow it to send notifies to this slave server and once to tell the slave server where to look for updates zone data. More allow-notify and request-xfr lines can be added to specify more masters. It is possible to specify extra allow-notify lines for addresses that are also allowed to send notifications to this slave server.</p>
<h3>Master zones</h3>
<p>For a master zone in BIND9, the slave servers are listed. These slave servers are sent notifications of updated and are allowed to request transfer of the zone data. In NSD these two properties need to be configured seperately. Here is an example of a master zone in BIND9 syntax. </p>
<p> zone &quot;example.nl&quot; {</p>
<dl>
<dd>type master;</dl>
<dl>
<dd>file &quot;example.nl&quot;;</dl>
<p> }; </p>
<p> In NSD syntax this becomes: </p>
<p> zone:</p>
<dl>
<dd>name: &quot;example.nl&quot;</dl>
<dl>
<dd>zonefile: &quot;example.nl&quot;</dl>
<dl>
<dd># allow anybody to request xfr.</dl>
<dl>
<dd>provide-xfr: 0.0.0.0/0 NOKEY</dl>
<dl>
<dd>provide-xfr: ::0/0 NOKEY</dl>
<dl>
<dd># to list a slave server you would in general give</dl>
<dl>
<dd># provide-xfr: 1.2.3.4 tsig-key.name.</dl>
<dl>
<dd># notify: 1.2.3.4 NOKEY</dl>
<h3>Other</h3>
<p>NSD is an authoritative only DNS server. This means that it is meant as a primary or secondary server for zones, providing DNS data to DNS resolvers and caches. BIND9 can function as an authoritative DNS server, the configuration options for that are compared with those for NSD in this section. However, BIND9 can also function as a resolver or cache. The configuration options that BIND9 has for the resolver or caching thus have no equivalents for NSD.</p>
<h2>Files</h2>
<dl>
<dt>/var/db/nsd/nsd.db</p>
<dd>default <code>NSD</code> database</p>
<dt>/etc/nsd/nsd.conf</p>
<dd>default <code>NSD</code> configuration file</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-nsd/">nsd</a>(8), <a href="/docs/linux/man/8-nsdc/">nsdc</a>(8), <a href="/docs/linux/man/8-nsd-checkconf/">nsd-checkconf</a>(8), <a href="/docs/linux/man/8-nsd-notify/">nsd-notify</a>(8), <a href="/docs/linux/man/8-nsd-patch/">nsd-patch</a>(8), <a href="/docs/linux/man/8-nsd-xfer/">nsd-xfer</a>(8), <a href="/docs/linux/man/8-zonec/">zonec</a>(8)</p>
<h2>Authors</h2>
<p><code>NSD</code> was written by NLnet Labs and RIPE NCC joint team. Please see CREDITS file in the distribution for further details.</p>
<h2>Bugs</h2>
<p><code>nsd.conf</code> is parsed by a primitive parser, error messages may not be to the point. </p>
