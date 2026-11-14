---
title: "nsd-conf(5)"
name: "nsd-conf"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nsd-conf/"
description: "nsd.conf – NSD configuration file"
---

<p><code>nsd.conf</code> &#8211; NSD configuration file</p>
<h2>Synopsis</h2>
<p><code>nsd.conf</code></p>
<h2>Description</h2>
<p><code>Nsd.conf</code> is used to configure <a href="/docs/linux/man/8-nsd/">nsd</a>(8). The file format has attributes and values. Some attributes have attributes inside them. The notation is: attribute: value. </p>
<p> Comments start with # and last to the end of line. Empty lines are ignored as is whitespace at the beginning of a line. Quotes can be used, for names with spaces, eg. &quot;file name.zone&quot;. </p>
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
<dd>server-count: 1 # use this number of cpu cores</dl>
<dl>
<dd>database: &quot;&quot; # or use &quot;&quot;</dl>
<dl>
<dd>zonelistfile: &quot;/var/lib/nsd/zone.list&quot;</dl>
<dl>
<dd>username: nsd</dl>
<dl>
<dd>logfile: &quot;/var/log/nsd.log&quot;</dl>
<dl>
<dd>pidfile: &quot;/var/run/nsd/nsd.pid&quot;</dl>
<dl>
<dd>xfrdfile: &quot;/var/lib/nsd/ixfr.state&quot;</dl>
<dt>zone:</p>
<dd>
<dl>
<dd>name: example.com</dl>
<dl>
<dd>zonefile: /etc/nsd/example.com.zone</dl>
<dt>zone:</p>
<dd>
<dl>
<dd># this server is master, 192.0.2.1 is the secondary.</dl>
<dl>
<dd>name: masterzone.com</dl>
<dl>
<dd>zonefile: /etc/nsd/masterzone.com.zone</dl>
<dl>
<dd>notify: 192.0.2.1 NOKEY</dl>
<dl>
<dd>provide-xfr: 192.0.2.1 NOKEY</dl>
<dt>zone:</p>
<dd>
<dl>
<dd># this server is secondary, 192.0.2.2 is master.</dl>
<dl>
<dd>name: secondzone.com</dl>
<dl>
<dd>zonefile: /etc/nsd/secondzone.com.zone</dl>
<dl>
<dd>allow-notify: 192.0.2.2 NOKEY</dl>
<dl>
<dd>request-xfr: 192.0.2.2 NOKEY</dl>
</dl>
<p> Then, use kill -HUP to reload changes from master zone files. And use kill -TERM to stop the server.</p>
<h2>File Format</h2>
<p>There must be whitespace between keywords. Attribute keywords end with a colon &#8216;:&#8217;. An attribute is followed by its containing attributes, or a value. </p>
<p> At the top level only <code>server:</code> and <code>key: </code> and <code>pattern:</code> and <code>zone: </code> are allowed. These are followed by their attributes or the start of a new <code>server:</code> or <code>key: </code> or <code>pattern:</code> or <code>zone: </code> clause. The <code>zone:</code> attribute is followed by zone options. The <code>server: </code> attribute is followed by global options for the <code>NSD </code> server. A <code>key: </code> attribute is used to define keys for authentication. The <code>pattern:</code> attribute is followed by the zone options for zones that use the pattern. </p>
<p> Files can be included using the <code>include:</code> directive. It can appear anywhere, and takes a single filename as an argument. Processing continues as if the text from the included file was copied into the config file at that point. If a chroot is used an absolute filename is needed (with the chroot prepended), so that the include can be parsed before and after application of the chroot (and the knowledge of what that chroot is). You can use &#8216;*&#8217; to include a wildcard match of files, eg. &quot;foo/nsd.d/*.conf&quot;. Also &#8216;?&#8217;, &#8216;{}&#8217;, &#8216;[]&#8217;, and &#8216;~&#8217; work, see <code><a href="/docs/linux/man/7-glob/">glob</a></code>(7). If no files match the pattern, this is not an error.</p>
<h3>Server Options</h3>
<p>The global options (if not overridden from the NSD commandline) are taken from the <code>server: </code> clause. There may only be one <code>server: </code> clause.</p>
<dl>
<dt><code>ip-address:</code> &lt;ip4 or ip6&gt;[@port]</p>
<dd>NSD will bind to the listed ip-address. Can be give multiple times to bind multiple ip-addresses. Optionally, a port number can be given. If none are given NSD listens to the wildcard interface. Same as commandline option <code>-a.</code> For servers with multiple IP addresses that can be used to send traffic to the internet, list them one by one, or the source address of replies could be wrong. This is because if the udp socket associates a source address of 0.0.0.0 then the kernel picks an ip-address with which to send to the internet, and it picks the wrong one. Typically needed for anycast instances. Use ip-transparent to be able to list addresses that turn on later (typical for certain load-balancing).</p>
<dt><code>interface:</code> &lt;ip4 or ip6&gt;[@port]</p>
<dd>Same as ip-address (for easy of compatibility with unbound.conf).</p>
<dt><code>ip-transparent:</code> &lt;yes or no&gt;</p>
<dd>Allows NSD to bind to non local addresses. This is useful to have NSD listen to IP addresses that are not (yet) added to the network interface, so that it can answer immediately when the address is added. Default is no.</p>
<dt><code>ip-freebind:</code> &lt;yes or no&gt;</p>
<dd>Set the IP_FREEBIND option to bind to nonlocal addresses and interfaces that are down. Similar to ip-transparent. Default is no.</p>
<dt><code>reuseport:</code> &lt;yes or no&gt;</p>
<dd>Use the SO_REUSEPORT socket option, and create file descriptors for every server in the server-count. This improves performance of the network stack. Only really useful if you also configure a server-count higher than 1 (such as, equal to the number of cpus). The default is no. It works on Linux, but does not work on FreeBSD, and likely does not work on other systems.</p>
<dt><code>debug-mode:</code> &lt;yes or no&gt;</p>
<dd>Turns on debugging mode for nsd, does not fork a daemon process. Default is no. Same as commandline option <code>-d.</code> If set to yes it does not fork and stays in the foreground, which can be helpful for commandline debugging, but is also used by certain server supervisor processes to ascertain that the server is running.</p>
<dt><code>do-ip4:</code> &lt;yes or no&gt;</p>
<dd>If yes, NSD listens to IPv4 connections. Default yes.</p>
<dt><code>do-ip6:</code> &lt;yes or no&gt;</p>
<dd>If yes, NSD listens to IPv6 connections. Default yes.</p>
<dt><code>database:</code> &lt;filename&gt;</p>
<dd>By default <i>&#8221;</i> is used. The specified file is used to store the compiled zone information. Same as commandline option <code>-f.</code> If set to &quot;&quot; then no database is used. This uses less memory but zone updates are not (immediately) spooled to disk.</p>
<dt><code>zonelistfile:</code> &lt;filename&gt;</p>
<dd>By default <i>/var/lib/nsd/zone.list</i> is used. The specified file is used to store the dynamically added list of zones. The list is written to by NSD to add and delete zones. It is a text file with a zone-name and pattern-name on each line. This file is used for the nsd-control addzone and delzone commands.</p>
<dt><code>identity:</code> &lt;string&gt;</p>
<dd>Returns the specified identity when asked for CH TXT ID.SERVER. Default is the name as returned by <a href="/docs/linux/man/3-gethostname/">gethostname</a>(3). Same as commandline option <code>-i</code>.</p>
<dt><code>version:</code> &lt;string&gt;</p>
<dd>Returns the specified version string when asked for CH TXT version.server, and version.bind queries. Default is the compiled package version. See hide-version to set the server to not respond to such queries.</p>
<dt><code>nsid:</code> &lt;string&gt;</p>
<dd>Add the specified nsid to the EDNS section of the answer when queried with an NSID EDNS enabled packet. As a sequence of hex characters or with ascii_ prefix and then an ascii string. Same as commandline option <code>-I</code>.</p>
<dt><code>logfile:</code> &lt;filename&gt;</p>
<dd>Log messages to the logfile. The default is to log to stderr and syslog (with facility LOG_DAEMON). Same as commandline option <code>-l</code>.</p>
<dt><code>server-count:</code> &lt;number&gt;</p>
<dd>Start this many NSD servers. Default is 1. Same as commandline option <code>-N</code>.</p>
<dt><code>tcp-count:</code> &lt;number&gt;</p>
<dd>The maximum number of concurrent, active TCP connections by each server. Default is 100. Same as commandline option <code>-n</code>.</p>
<dt><code>tcp-query-count:</code> &lt;number&gt;</p>
<dd>The maximum number of queries served on a single TCP connection. Default is 0, meaning there is no maximum.</p>
<dt><code>tcp-timeout:</code> &lt;number&gt;</p>
<dd>Overrides the default TCP timeout. This also affects zone transfers over TCP.</p>
<dt><code>tcp-mss:</code> &lt;number&gt;</p>
<dd>Maximum segment size (MSS) of TCP socket on which the server responds to queries. Value lower than common MSS on Ethernet (1220 for example) will address path MTU problem. Note that not all platform supports socket option to set MSS (TCP_MAXSEG). Default is system default MSS determined by interface MTU and negotiation between server and client.</p>
<dt><code>outgoing-tcp-mss:</code> &lt;number&gt;</p>
<dd>Maximum segment size (MSS) of TCP socket for outgoing XFR request to other namesevers. Value lower than common MSS on Ethernet (1220 for example) will address path MTU problem. Note that not all platform supports socket option to set MSS (TCP_MAXSEG). Default is system default MSS determined by interface MTU and negotiation between NSD and other servers.</p>
<dt><code>ipv4-edns-size:</code> &lt;number&gt;</p>
<dd>Preferred EDNS buffer size for IPv4. Default 4096.</p>
<dt><code>ipv6-edns-size:</code> &lt;number&gt;</p>
<dd>Preferred EDNS buffer size for IPv6. Default 4096.</p>
<dt><code>pidfile:</code> &lt;filename&gt;</p>
<dd>Use the pid file instead of the platform specific default, usually <i>/var/run/nsd/nsd.pid.</i> Same as commandline option <code>-P</code>.</p>
<dt><code>port:</code> &lt;number&gt;</p>
<dd>Answer queries on the specified port. Default is 53. Same as commandline option <code>-p</code>.</p>
<dt><code>statistics:</code> &lt;number&gt;</p>
<dd>If not present no statistics are dumped. Statistics are produced every number seconds. Same as commandline option <code>-s</code>.</p>
<dt><code>chroot:</code> &lt;directory&gt;</p>
<dd>NSD will chroot on startup to the specified directory. Note that if elsewhere in the configuration you specify an absolute pathname to a file inside the chroot, you have to prepend the <code>chroot</code> path. That way, you can switch the chroot option on and off without having to modify anything else in the configuration. Set the value to &quot;&quot; (the empty string) to disable the chroot. By default &quot;<i></i>&quot; is used. Same as commandline option <code>-t</code>.</p>
<dt><code>username:</code> &lt;username&gt;</p>
<dd>After binding the socket, drop user privileges and assume the username. Can be username, id or id.gid. Same as commandline option <code>-u</code>.</p>
<dt><code>zonesdir:</code> &lt;directory&gt;</p>
<dd>Change the working directory to the specified directory before accessing zone files. Also, NSD will access <code>database</code>, <code>zonelistfile</code>, <code>logfile</code>, <code>pidfile</code>, <code>xfrdfile</code>, <code>xfrdir</code>, <code>server-key-file</code>, <code>server-cert-file</code>, <code>control-key-file</code> and <code>control-cert-file</code> relative to this directory. Set the value to &quot;&quot; (the empty string) to disable the change of working directory. By default &quot;<i>/etc/nsd</i>&quot; is used.</p>
<dt><code>difffile:</code> &lt;filename&gt;</p>
<dd>Ignored, for compatibility with NSD3 config files.</p>
<dt><code>xfrdfile:</code> &lt;filename&gt;</p>
<dd>The soa timeout and zone transfer daemon in NSD will save its state to this file. State is read back after a restart. The state file can be deleted without too much harm, but timestamps of zones will be gone. If it is configured as &quot;&quot;, the state file is not used, all slave zones are checked for updates upon startup. For more details see the section on zone expiry behavior of NSD. Default is <i>/var/lib/nsd/ixfr.state</i>.</p>
<dt><code>xfrdir:</code> &lt;directory&gt;</p>
<dd>The zone transfers are stored here before they are processed. A directory is created here that is removed when NSD exits. Default is <i>/tmp</i>.</p>
<dt><code>xfrd-reload-timeout:</code> &lt;number&gt;</p>
<dd>If this value is -1, xfrd will not trigger a reload after a zone transfer. If positive xfrd will trigger a reload after a zone transfer, then it will wait for the number of seconds before it will trigger a new reload. Setting this value throttles the reloads to once per the number of seconds. The default is 1 second.</p>
<dt><code>verbosity:</code> &lt;level&gt;</p>
<dd>This value specifies the verbosity level for (non-debug) logging. Default is 0. 1 gives more information about incoming notifies and zone transfers. 2 lists soft warnings that are encountered. 3 prints more information.</p>
<dd>Verbosity 0 will print warnings and errors, and other events that are important to keep NSD running.</p>
<dd>Verbosity 1 prints additionally messages of interest. Successful notifies, successful incoming zone transfer (the zone is updated), failed incoming zone transfers or the inability to process zone updates.</p>
<dd>Verbosity 2 prints additionally soft errors, like connection resets over TCP. And notify refusal, and axfr request refusals.</p>
<dt><code>hide-version:</code> &lt;yes or no&gt;</p>
<dd>Prevent NSD from replying with the version string on CHAOS class queries. Default is no.</p>
<dt><code>log-time-ascii:</code> &lt;yes or no&gt;</p>
<dd>Log time in ascii, if &quot;no&quot; then in seconds epoch. Default is yes. This chooses the format when logging to file. The printout via syslog has a timestamp formatted by syslog.</p>
<dt><code>round-robin:</code> &lt;yes or no&gt;</p>
<dd>Enable round robin rotation of records in the answer. This changes the order of records in the answer and this may balance load across them. The default is no.</p>
<dt><code>zonefiles-check:</code> &lt;yes or no&gt;</p>
<dd>Make NSD check the mtime of zone files on start and sighup. If you disable it it starts faster (less disk activity in case of a lot of zones). The default is yes. The nsd-control reload command reloads zone files regardless of this option.</p>
<dt><code>zonefiles-write:</code> &lt;seconds&gt;</p>
<dd>Write changed secondary zones to their zonefile every N seconds. If the zone (pattern) configuration has &quot;&quot; zonefile, it is not written. Zones that have received zone transfer updates are written to their zonefile. Default is 0 (disabled) when there is a database, and 3600 (1 hour) when database is &quot;&quot;. The database also commits zone transfer contents. You can configure it away from the default by putting the config statement for zonefiles-write: after the database: statement in the config file.</p>
<dt><code>rrl-size:</code> &lt;numbuckets&gt;</p>
<dd>This option gives the size of the hashtable. Default 1000000. More buckets use more memory, and reduce the chance of hash collisions.</p>
<dt><code>rrl-ratelimit:</code> &lt;qps&gt;</p>
<dd>The max qps allowed (from one query source). Default is on (with a suggested 200 qps). If set to 0 then it is disabled (unlimited rate), also set the whitelist-ratelimit to 0 to disable ratelimit processing. If you set verbosity to 2 the blocked and unblocked subnets are logged. Blocked queries are blocked and some receive TCP fallback replies. Once the rate limit is reached, NSD begins dropping responses. However, one in every &quot;rrl-slip&quot; number of responses is allowed, with the TC bit set. If slip is set to 2, the outgoing response rate will be halved. If it&#8217;s set to 3, the outgoing response rate will be one-third, and so on. If you set rrl-slip to 10, traffic is reduced to 1/10th. Ratelimit options rrl-ratelimit, rrl-size and rrl-whitelist-ratelimit are updated when nsd-control reconfig is done (also the zone-specific ratelimit options are updated).</p>
<dt><code>rrl-slip:</code> &lt;numpackets&gt;</p>
<dd>This option controls the number of packets discarded before we send back a SLIP response (a response with &quot;truncated&quot; bit set to one). 0 disables the sending of SLIP packets, 1 means every query will get a SLIP response. Default is 2, cuts traffic in half and legit users have a fair chance to get a +TC response.</p>
<dt><code>rrl-ipv4-prefix-length:</code> &lt;subnet&gt;</p>
<dd>IPv4 prefix length. Addresses are grouped by netblock. Default 24.</p>
<dt><code>rrl-ipv6-prefix-length:</code> &lt;subnet&gt;</p>
<dd>IPv6 prefix length. Addresses are grouped by netblock. Default 64.</p>
<dt><code>rrl-whitelist-ratelimit:</code> &lt;qps&gt;</p>
<dd>The max qps for query sorts for a source, which have been whitelisted. Default on (with a suggested 2000 qps). With the rrl-whitelist option you can set specific queries to receive this qps limit instead of the normal limit. With the value 0 the rate is unlimited.</dl>
<h3>Remote Control</h3>
<p>The <code>remote-control:</code> clause is used to set options for using the <i><a href="/docs/linux/man/8-nsd-control/">nsd-control</a></i>(8) tool to give commands to the running NSD server. It is disabled by default, and listens for localhost by default. It uses TLS over TCP where the server and client authenticate to each other with self-signed certificates. The self-signed certificates can be generated with the <i>nsd-control-setup</i> tool. The key files are read by NSD before the chroot and before dropping user permissions, so they can be outside the chroot and readable by the superuser only.</p>
<dl>
<dt><code>control-enable:</code> &lt;yes or no&gt;</p>
<dd>Enable remote control, default is no.</p>
<dt><code>control-interface:</code> &lt;ip4 or ip6&gt;</p>
<dd>NSD will bind to the listed addresses to service control requests (on TCP). Can be given multiple times to bind multiple ip-addresses. Use 0.0.0.0 and ::0 to service the wildcard interface. If none are given NSD listens to the localhost 127.0.0.1 and ::1 interfaces for control, if control is enabled with control-enable.</p>
<dt><code>control-port:</code> &lt;number&gt;</p>
<dd>The port number for remote control service. 8952 by default.</p>
<dt><code>server-key-file:</code> &lt;filename&gt;</p>
<dd>Path to the server private key, by default <i>/etc/nsd/nsd_server.key</i>. This file is generated by the <i>nsd-control-setup</i> utility. This file is used by the nsd server, but not by <i>nsd-control</i>.</p>
<dt><code>server-cert-file:</code> &lt;filename&gt;</p>
<dd>Path to the server self signed certificate, by default <i>/etc/nsd/nsd_server.pem</i>. This file is generated by the <i>nsd-control-setup</i> utility. This file is used by the nsd server, and also by <i>nsd-control</i>.</p>
<dt><code>control-key-file:</code> &lt;filename&gt;</p>
<dd>Path to the control client private key, by default <i>/etc/nsd/nsd_control.key</i>. This file is generated by the <i>nsd-control-setup</i> utility. This file is used by <i>nsd-control</i>.</p>
<dt><code>control-cert-file:</code> &lt;filename&gt;</p>
<dd>Path to the control client certificate, by default <i>/etc/nsd/nsd_control.pem</i>. This certificate has to be signed with the server certificate. This file is generated by the <i>nsd-control-setup</i> utility. This file is used by <i>nsd-control</i>.</dl>
<h3>Pattern Options</h3>
<p>The <code>pattern:</code> clause is used to denote a set of options to apply to some zones. The same zone options as for a zone are allowed.</p>
<dl>
<dt><code>name:</code> &lt;string&gt;</p>
<dd>The name of the pattern. This is a (case sensitive) string. The pattern names that start with &quot;_implicit_&quot; are used internally for zones that have no pattern (they are defined in nsd.conf directly).</p>
<dt><code>include-pattern:</code> &lt;pattern-name&gt;</p>
<dd>The options from the given pattern are included at this point in this pattern. The referenced pattern must be defined above this one.</p>
<dt><code>&lt;zone option&gt;:</code> &lt;value&gt;</p>
<dd>The zone options such as <code>zonefile</code>, <code>allow-notify</code>, <code>request-xfr</code>, <code>allow-axfr-fallback</code>, <code>notify</code>, <code>notify-retry</code>, <code>provide-xfr</code>, <code>zonestats</code>, and <code>outgoing-interface </code> can be given. They are applied to the patterns and zones that include this pattern.</dl>
<h3>Zone Options</h3>
<p>For every zone the options need to be specified in one <code>zone: </code> clause. The access control list elements can be given multiple times to add multiple servers. These elements need to be added explicitly. </p>
<p> For zones that are configured in the <i>nsd.conf</i> config file their settings are hardcoded (in an implicit pattern for themselves only) and they cannot be deleted via delzone, but remove them from the config file and repattern.</p>
<dl>
<dt><code>name:</code> &lt;string&gt;</p>
<dd>The name of the zone. This is the domain name of the apex of the zone. May end with a &#8216;.&#8217; (in FQDN notation). For example &quot;example.com&quot;, &quot;sub.example.net.&quot;. This attribute must be present in each zone.</p>
<dt><code>zonefile:</code> &lt;filename&gt;</p>
<dd>The file containing the zone information. If this attribute is present it is used to read and write the zone contents. If the attribute is absent it prevents writing out of the zone.</p>
<dd>The string is processed so that one string can be used (in a pattern) for a lot of different zones. If the label or character does not exist the percent-character is replaced with a period for output (i.e. for the third character in a two letter domain name).</p>
<dd><code>%s</code> is replaced with the zone name.</p>
<dd><code>%1</code> is replaced with the first character of the zone name.</p>
<dd><code>%2</code> is replaced with the second character of the zone name.</p>
<dd><code>%3</code> is replaced with the third character of the zone name.</p>
<dd><code>%z</code> is replaced with the toplevel domain name of the zone.</p>
<dd><code>%y</code> is replaced with the next label under the toplevel domain.</p>
<dd><code>%x</code> is replaced with the next-next label under the toplevel domain.</p>
<dt><code>allow-notify:</code> &lt;ip-spec&gt; &lt;key-name | NOKEY | BLOCKED&gt;</p>
<dd>Access control list. The listed (primary) address is allowed to send notifies to this (secondary) server. Notifies from unlisted or specifically BLOCKED addresses are discarded. If NOKEY is given no TSIG signature is required. BLOCKED supersedes other entries, other entries are scanned for a match in the order of the statements.</dl>
<dl>
<dd>The ip-spec is either a plain IP address (IPv4 or IPv6), or can be a subnet of the form 1.2.3.4/24, or masked like 1.2.3.4&amp;255.255.255.0 or a range of the form 1.2.3.4-1.2.3.25. A port number can be added using a suffix of @number, for example 1.2.3.4 [at] 5300 or 1.2.3.4/24 [at] 5300 for port 5300. Note the ip-spec ranges do not use spaces around the /, &amp;, @ and &#8211; symbols.</dl>
<dl>
<dt><code>request-xfr:</code> [AXFR|UDP] &lt;ip-address&gt; &lt;key-name | NOKEY&gt;</p>
<dd>Access control list. The listed address (the master) is queried for AXFR/IXFR on update. A port number can be added using a suffix of @number, for example 1.2.3.4 [at] 5300. The specified key is used during AXFR/IXFR.</dl>
<dl>
<dd>If the AXFR option is given, the server will not be contacted with IXFR queries but only AXFR requests will be made to the server. This allows an NSD secondary to have a master server that runs NSD. If the AXFR option is left out then both IXFR and AXFR requests are made to the master server. </p>
<p> If the UDP option is given, the secondary will use UDP to transmit the IXFR requests. You should deploy TSIG when allowing UDP transport, to authenticate notifies and zone transfers. Otherwise, NSD is more vulnerable for Kaminsky-style attacks. If the UDP option is left out then IXFR will be transmitted using TCP.</dl>
<dl>
<dt><code>allow-axfr-fallback:</code> &lt;yes or no&gt;</p>
<dd>This option should be accompanied by request-xfr. It (dis)allows NSD (as secondary) to fallback to AXFR if the primary name server does not support IXFR. Default is yes.</p>
<dt><code>size-limit-xfr:</code> &lt;number&gt;</p>
<dd>This option should be accompanied by request-xfr. It specifies XFR temporary file size limit. It can be used to stop very large zone retrieval, that could otherwise use up a lot of memory and disk space. If this option is 0, unlimited. Default value is 0.</p>
<dt><code>notify:</code> &lt;ip-address&gt; &lt;key-name | NOKEY&gt;</p>
<dd>Access control list. The listed address (a secondary) is notified of updates to this zone. A port number can be added using a suffix of @number, for example 1.2.3.4 [at] 5300. The specified key is used to sign the notify. Only on secondary configurations will NSD be able to detect zone updates (as it gets notified itself, or refreshes after a time).</p>
<dt><code>notify-retry:</code> &lt;number&gt;</p>
<dd>This option should be accompanied by notify. It sets the number of retries when sending notifies.</p>
<dt><code>provide-xfr:</code> &lt;ip-spec&gt; &lt;key-name | NOKEY | BLOCKED&gt;</p>
<dd>Access control list. The listed address (a secondary) is allowed to request AXFR from this server. Zone data will be provided to the address. The specified key is used during AXFR. For unlisted or BLOCKED addresses no data is provided, requests are discarded. BLOCKED supersedes other entries, other entries are scanned for a match in the order of the statements. NSD provides AXFR for its secondaries, but IXFR is not implemented (IXFR is implemented for request-xfr, but not for provide-xfr).</dl>
<dl>
<dd>The ip-spec is either a plain IP address (IPv4 or IPv6), or can be a subnet of the form 1.2.3.4/24, or masked like 1.2.3.4&amp;255.255.255.0 or a range of the form 1.2.3.4-1.2.3.25. A port number can be added using a suffix of @number, for example 1.2.3.4 [at] 5300 or 1.2.3.4/24 [at] 5300 for port 5300. Note the ip-spec ranges do not use spaces around the /, &amp;, @ and &#8211; symbols.</dl>
<dl>
<dt><code>outgoing-interface:</code> &lt;ip-address&gt;</p>
<dd>Access control list. The listed address is used to request AXFR|IXFR (in case of a secondary) or used to send notifies (in case of a primary).</dl>
<dl>
<dd>The ip-address is a plain IP address (IPv4 or IPv6). A port number can be added using a suffix of @number, for example 1.2.3.4 [at] 5300.</dl>
<dl>
<dt><code>max-refresh-time:</code> &lt;seconds&gt;</p>
<dd>Limit refresh time for secondary zones. This is the timer which checks to see if the zone has to be refetched when it expires. Normally the value from the SOA record is used, but this option restricts that value.</p>
<dt><code>min-refresh-time:</code> &lt;seconds&gt;</p>
<dd>Limit refresh time for secondary zones.</p>
<dt><code>max-retry-time:</code> &lt;seconds&gt;</p>
<dd>Limit retry time for secondary zones. This is the timeout after a failed fetch attempt for the zone. Normally the value from the SOA record is used, but this option restricts that value.</p>
<dt><code>min-retry-time:</code> &lt;seconds&gt;</p>
<dd>Limit retry time for secondary zones.</p>
<dt><code>zonestats:</code> &lt;name&gt;</p>
<dd>When compiled with &#8211;enable-zone-stats NSD can collect statistics per zone. This name gives the group where statistics are added to. The groups are output from nsd-control stats and stats_noreset. Default is &quot;&quot;. You can use &quot;%s&quot; to use the name of the zone to track its statistics. If not compiled in, the option can be given but is ignored.</p>
<dt><code>include-pattern:</code> &lt;pattern-name&gt;</p>
<dd>The options from the given pattern are included at this point. The referenced pattern must be defined above this zone.</p>
<dt><code>rrl-whitelist:</code> &lt;rrltype&gt;</p>
<dd>This option causes queries of this rrltype to be whitelisted, for this zone. They receive the whitelist-ratelimit. You can give multiple lines, each enables a new rrltype to be whitelisted for the zone. Default has none whitelisted. The rrltype is the query classification that the NSD RRL employs to make different types not interfere with one another. The types are logged in the loglines when a subnet is blocked (in verbosity 2). The RRL classification types are: nxdomain, error, referral, any, rrsig, wildcard, nodata, dnskey, positive, all.</p>
<dt><code>multi-master-check:</code> &lt;yes or no&gt;</p>
<dd>Default no. If enabled, checks all masters for the last version. It uses the higher version of all the configured masters. Useful if you have multiple masters that have different version numbers served.</dl>
<h3>Key Declarations</h3>
<p>The <code>key: </code> clause establishes a key for use in access control lists. It has the following attributes.</p>
<dl>
<dt><code>name:</code> &lt;string&gt;</p>
<dd>The key name. Used to refer to this key in the access control list. The key name has to be correct for tsig to work. This is because the key name is output on the wire.</p>
<dt><code>algorithm:</code> &lt;string&gt;</p>
<dd>Authentication algorithm for this key. Such as hmac-md5, hmac-sha1, hmac-sha224, hmac-sha256, hmac-sha384 and hmac-sha512. Can also be abbreviated as &#8216;sha1&#8217;, &#8216;sha256&#8217;. Default is sha256. Algorithms are only available when they were compiled in (available in the crypto library).</p>
<dt><code>secret:</code> &lt;base64 blob&gt;</p>
<dd>The base64 encoded shared secret. It is possible to put the <code>secret:</code> declaration (and base64 blob) into a different file, and then to <code>include:</code> that file. In this way the key secret and the rest of the configuration file, which may have different security policies, can be split apart. The content of the secret is the agreed base64 secret content. To make it up, enter a password (its length must be a multiple of 4 characters, A-Za-z0-9), or use dev-random output through a base64 encode filter.</dl>
<h2>Nsd Configuration For Bind9 Hackers</h2>
<p>BIND9 is a name server implementation with its own configuration file format, <a href="/docs/linux/man/5-named-conf/">named.conf</a>(5). BIND9 types zones as &#8216;Master&#8217; or &#8216;Slave&#8217;.</p>
<h3>Slave zones</h3>
<p>For a slave zone, the master servers are listed. The master servers are queried for zone data, and are listened to for update notifications. In NSD these two properties need to be configured separately, by listing the master address in allow-notify and request-xfr statements. </p>
<p> In BIND9 you only need to provide allow-notify elements for any extra sources of notifications (i.e. the operators), NSD needs to have allow-notify for both masters and operators. BIND9 allows additional transfer sources, in NSD you list those as request-xfr. </p>
<p> Here is an example of a slave zone in BIND9 syntax. </p>
<p> # Config file for example.org options {</p>
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
<p> }; </p>
<p> For NSD, DNSSEC is enabled automatically for zones that are signed. The dnssec-enable statement in the options clause is not needed. In NSD keys are associated with an IP address in the access control list statement, therefore the server{} statement is not needed. Below is the same example in an NSD config file. </p>
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
<p> Notice that the master is listed twice, once to allow it to send notifies to this slave server and once to tell the slave server where to look for updates zone data. More allow-notify and request-xfr lines can be added to specify more masters. </p>
<p> It is possible to specify extra allow-notify lines for addresses that are also allowed to send notifications to this slave server.</p>
<h3>Master zones</h3>
<p>For a master zone in BIND9, the slave servers are listed. These slave servers are sent notifications of updated and are allowed to request transfer of the zone data. In NSD these two properties need to be configured separately. </p>
<p> Here is an example of a master zone in BIND9 syntax. </p>
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
<dt>&quot;&quot;</p>
<dd>default <code>NSD</code> database</p>
<dt>/etc/nsd/nsd.conf</p>
<dd>default <code>NSD</code> configuration file</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-nsd/">nsd</a></i>(8), <i><a href="/docs/linux/man/8-nsd-checkconf/">nsd-checkconf</a></i>(8), <i><a href="/docs/linux/man/8-nsd-control/">nsd-control</a></i>(8)</p>
<h2>Authors</h2>
<p><code>NSD</code> was written by NLnet Labs and RIPE NCC joint team. Please see CREDITS file in the distribution for further details.</p>
<h2>Bugs</h2>
<p><code>nsd.conf</code> is parsed by a primitive parser, error messages may not be to the point. </p>
