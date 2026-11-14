---
title: "resolvectl(1)"
name: "resolvectl"
section: "1"
letter: "r"
url: "/docs/linux/man/1-resolvectl/"
description: "resolvectl, resolvconf – Resolve domain names, IPV4 and IPv6 addresses, DNS resource records, and services; introspect and reconfigure the DNS resolver"
---

<h2 class="name">NAME</h2>
<p> resolvectl, resolvconf &#8211; Resolve domain names, IPV4 and IPv6 addresses, DNS resource records, and services; introspect and reconfigure the DNS resolver </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>resolvectl</code> [OPTIONS&#8230;] {COMMAND} [NAME&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>resolvectl</code></p>
<dd>may be used to resolve domain names, IPv4 and IPv6 addresses, DNS resource records and services with the <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8) resolver service. By default, the specified list of parameters will be resolved as hostnames, retrieving their IPv4 and IPv6 addresses. If the parameters specified are formatted as IPv4 or IPv6 operation the reverse operation is done, and a hostname is retrieved for the specified addresses. </p>
<p> The program&#8217;s output contains information about the protocol used for the look-up and on which network interface the data was discovered. It also contains information on whether the information could be authenticated. All data for which local DNSSEC validation succeeds is considered authenticated. Moreover all data originating from local, trusted sources is also reported authenticated, including resolution of the local host name, the &quot;localhost&quot; hostname or all data from /etc/hosts.</p>
<h2>COMMANDS</h2>
<p> <code>query</code> <i>HOSTNAME|ADDRESS</i>&#8230;</p>
<dl>
<dt>
<dd> Resolve domain names, as well as IPv4 and IPv6 addresses. When used in conjunction with <code>&#8211;type=</code> or <code>&#8211;class=</code> (see below), resolves low-level DNS resource records. </p>
<p> If a single-label domain name is specified it is searched for according to the configured search domains &#8212; unless <code>&#8211;search=no</code> or <code>&#8211;type=</code>/<code>&#8211;class=</code> are specified, both of which turn this logic off. </p>
<p> If an international domain name is specified, it is automatically translated according to IDNA rules when resolved via classic DNS &#8212; but not for look-ups via MulticastDNS or LLMNR. If <code>&#8211;type=</code>/<code>&#8211;class=</code> is used IDNA translation is turned off and domain names are processed as specified.</dl>
<p> <code>service</code> [[<i>NAME</i>] <i>TYPE</i>] <i>DOMAIN</i></p>
<dl>
<dt>
<dd> Resolve m[blue]<code>DNS-SD</code>m[]<font SIZE="-2">[1]</font> and m[blue]<code>SRV</code>m[]<font SIZE="-2">[2]</font> services, depending on the specified list of parameters. If three parameters are passed the first is assumed to be the DNS-SD service name, the second the <code>SRV</code> service type, and the third the domain to search in. In this case a full DNS-SD style <code>SRV</code> and <code>TXT</code> lookup is executed. If only two parameters are specified, the first is assumed to be the <code>SRV</code> service type, and the second the domain to look in. In this case no <code>TXT</code> resource record is requested. Finally, if only one parameter is specified, it is assumed to be a domain name, that is already prefixed with an <code>SRV</code> type, and an <code>SRV</code> lookup is done (no <code>TXT</code>).</dl>
<p> <code>openpgp</code> <i>EMAIL [at] DOMAIN</i>&#8230;</p>
<dl>
<dt>
<dd> Query PGP keys stored as <code>OPENPGPKEY</code> resource records, see m[blue]<code>RFC 7929</code>m[]<font SIZE="-2">[3]</font>. Specified e-mail addresses are converted to the corresponding DNS domain name, and any <code>OPENPGPKEY</code> keys are printed.</dl>
<p> <code>tlsa</code> [<i>FAMILY</i>] <i>DOMAIN</i>[:<i>PORT</i>]&#8230;</p>
<dl>
<dt>
<dd> Query TLS public keys stored as <code>TLSA</code> resource records, see m[blue]<code>RFC 6698</code>m[]<font SIZE="-2">[4]</font>. A query will be performed for each of the specified names prefixed with the port and family (&quot;_<i>port</i>._<i>family</i>.<i>domain</i>&quot;). The port number may be specified after a colon (&quot;:&quot;), otherwise <code>443</code> will be used by default. The family may be specified as the first argument, otherwise <code>tcp</code> will be used.</dl>
<p> <code>status</code> [<i>LINK</i>&#8230;]</p>
<dl>
<dt>
<dd> Shows the global and per-link DNS settings currently in effect. If no command is specified, this is the implied default.</dl>
<p> <code>statistics</code></p>
<dl>
<dt>
<dd> Shows general resolver statistics, including information whether DNSSEC is enabled and available, as well as resolution and validation statistics.</dl>
<p> <code>reset-statistics</code></p>
<dl>
<dt>
<dd> Resets the statistics counters shown in <code>statistics</code> to zero. This operation requires root privileges.</dl>
<p> <code>flush-caches</code></p>
<dl>
<dt>
<dd> Flushes all DNS resource record caches the service maintains locally. This is mostly equivalent to sending the <code>SIGUSR2</code> to the <code>systemd-resolved</code> service.</dl>
<p> <code>reset-server-features</code></p>
<dl>
<dt>
<dd> Flushes all feature level information the resolver learnt about specific servers, and ensures that the server feature probing logic is started from the beginning with the next look-up request. This is mostly equivalent to sending the <code>SIGRTMIN+1</code> to the <code>systemd-resolved</code> service.</dl>
<p> <code>dns</code> [<i>LINK</i> [<i>SERVER</i>&#8230;]], <code>domain</code> [<i>LINK</i> [<i>DOMAIN</i>&#8230;]], <code>default-route</code> [<i>LINK</i> [<i>BOOL</i>&#8230;]], <code>llmnr</code> [<i>LINK</i> [<i>MODE</i>]], <code>mdns</code> [<i>LINK</i> [<i>MODE</i>]], <code>dnssec</code> [<i>LINK</i> [<i>MODE</i>]], <code>dnsovertls</code> [<i>LINK</i> [<i>MODE</i>]], <code>nta</code> [<i>LINK</i> [<i>DOMAIN</i>&#8230;]]</p>
<dl>
<dt>
<dd> Get/set per-interface DNS configuration. These commands may be used to configure various DNS settings for network interfaces. These commands may be used to inform <code>systemd-resolved</code> or <code>systemd-networkd</code> about per-interface DNS configuration determined through external means. The <code>dns</code> command expects IPv4 or IPv6 address specifications of DNS servers to use. Each address can optionally take a port number separated with &quot;:&quot;, a network interface name or index separated with &quot;%&quot;, and a Server Name Indication (SNI) separated with &quot;#&quot;. When IPv6 address is specified with a port number, then the address must be in the square brackets. That is, the acceptable full formats are &quot;111.222.333.444:9953%ifname#example.com&quot; for IPv4 and &quot;[1111:2222::3333]:9953%ifname#example.com&quot; for IPv6. The <code>domain</code> command expects valid DNS domains, possibly prefixed with &quot;~&quot;, and configures a per-interface search or route-only domain. The <code>default-route</code> command expects a boolean parameter, and configures whether the link may be used as default route for DNS lookups, i.e. if it is suitable for lookups on domains no other link explicitly is configured for. The <code>llmnr</code>, <code>mdns</code>, <code>dnssec</code> and <code>dnsovertls</code> commands may be used to configure the per-interface LLMNR, MulticastDNS, DNSSEC and DNSOverTLS settings. Finally, <code>nta</code> command may be used to configure additional per-interface DNSSEC NTA domains. </p>
<p> Commands <code>dns</code>, <code>domain</code> and <code>nta</code> can take a single empty string argument to clear their respective value lists. </p>
<p> For details about these settings, their possible values and their effect, see the corresponding settings in <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5).</dl>
<p> <code>revert </code><i>LINK</i></p>
<dl>
<dt>
<dd> Revert the per-interface DNS configuration. If the DNS configuration is reverted all per-interface DNS setting are reset to their defaults, undoing all effects of <code>dns</code>, <code>domain</code>, <code>default-route</code>, <code>llmnr</code>, <code>mdns</code>, <code>dnssec</code>, <code>dnsovertls</code>, <code>nta</code>. Note that when a network interface disappears all configuration is lost automatically, an explicit reverting is not necessary in that case.</dl>
<p> <code>log-level</code> [<i>LEVEL</i>]</p>
<dl>
<dt>
<dd> If no argument is given, print the current log level of the manager. If an optional argument <i>LEVEL</i> is provided, then the command changes the current log level of the manager to <i>LEVEL</i> (accepts the same values as <code>&#8211;log-level=</code> described in <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1)).</dl>
<h2>OPTIONS</h2>
<p> <code>-4</code>, <code>-6</code></p>
<dl>
<dt>
<dd> By default, when resolving a hostname, both IPv4 and IPv6 addresses are acquired. By specifying <code>-4</code> only IPv4 addresses are requested, by specifying <code>-6</code> only IPv6 addresses are requested.</dl>
<p> <code>-i</code> <i>INTERFACE</i>, <code>&#8211;interface=</code><i>INTERFACE</i></p>
<dl>
<dt>
<dd> Specifies the network interface to execute the query on. This may either be specified as numeric interface index or as network interface string (e.g. &quot;en0&quot;). Note that this option has no effect if system-wide DNS configuration (as configured in /etc/resolv.conf or /etc/systemd/resolved.conf) in place of per-link configuration is used.</dl>
<p> <code>-p</code> <i>PROTOCOL</i>, <code>&#8211;protocol=</code><i>PROTOCOL</i></p>
<dl>
<dt>
<dd> Specifies the network protocol for the query. May be one of &quot;dns&quot; (i.e. classic unicast DNS), &quot;llmnr&quot; (m[blue]<code>Link-Local Multicast Name Resolution</code>m[]<font SIZE="-2">[5]</font>), &quot;llmnr-ipv4&quot;, &quot;llmnr-ipv6&quot; (LLMNR via the indicated underlying IP protocols), &quot;mdns&quot; (m[blue]<code>Multicast DNS</code>m[]<font SIZE="-2">[6]</font>), &quot;mdns-ipv4&quot;, &quot;mdns-ipv6&quot; (MDNS via the indicated underlying IP protocols). By default the lookup is done via all protocols suitable for the lookup. If used, limits the set of protocols that may be used. Use this option multiple times to enable resolving via multiple protocols at the same time. The setting &quot;llmnr&quot; is identical to specifying this switch once with &quot;llmnr-ipv4&quot; and once via &quot;llmnr-ipv6&quot;. Note that this option does not force the service to resolve the operation with the specified protocol, as that might require a suitable network interface and configuration. The special value &quot;help&quot; may be used to list known values.</dl>
<p> <code>-t</code> <i>TYPE</i>, <code>&#8211;type=</code><i>TYPE</i>, <code>-c</code> <i>CLASS</i>, <code>&#8211;class=</code><i>CLASS</i></p>
<dl>
<dt>
<dd> When used in conjunction with the <code>query</code> command, specifies the DNS resource record type (e.g. <code>A</code>, <code>AAAA</code>, <code>MX</code>, &#8230;) and class (e.g. <code>IN</code>, <code>ANY</code>, &#8230;) to look up. If these options are used a DNS resource record set matching the specified class and type is requested. The class defaults to <code>IN</code> if only a type is specified. The special value &quot;help&quot; may be used to list known values. </p>
<p> Without these options <code>resolvectl query</code> provides high-level domain name to address and address to domain name resolution. With these options it provides low-level DNS resource record resolution. The search domain logic is automatically turned off when these options are used, i.e. specified domain names need to be fully qualified domain names. Moreover, IDNA internal domain name translation is turned off as well, i.e. international domain names should be specified in &quot;xn--&#8230;&quot; notation, unless look-up in MulticastDNS/LLMNR is desired, in which case UTF-8 characters should be used.</dl>
<p> <code>&#8211;service-address=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter. If true (the default), when doing a service lookup with <code>&#8211;service</code> the hostnames contained in the <code>SRV</code> resource records are resolved as well.</dl>
<p> <code>&#8211;service-txt=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter. If true (the default), when doing a DNS-SD service lookup with <code>&#8211;service</code> the <code>TXT</code> service metadata record is resolved as well.</dl>
<p> <code>&#8211;cname=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter. If true (the default), DNS <code>CNAME</code> or <code>DNAME</code> redirections are followed. Otherwise, if a CNAME or DNAME record is encountered while resolving, an error is returned.</dl>
<p> <code>&#8211;validate=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter; used in conjunction with <code>query</code>. If true (the default), DNSSEC validation is applied as usual &#8212; under the condition that it is enabled for the network and for systemd-resolved.service as a whole. If false, DNSSEC validation is disabled for the specific query, regardless of whether it is enabled for the network or in the service. Note that setting this option to true does not force DNSSEC validation on systems/networks where DNSSEC is turned off. This option is only suitable to turn off such validation where otherwise enabled, not enable validation where otherwise disabled.</dl>
<p> <code>&#8211;synthesize=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter; used in conjunction with <code>query</code>. If true (the default), select domains are resolved on the local system, among them &quot;localhost&quot;, &quot;_gateway&quot; and &quot;_outbound&quot;, or entries from /etc/hosts. If false these domains are not resolved locally, and either fail (in case of &quot;localhost&quot;, &quot;_gateway&quot; or &quot;_outbound&quot; and suchlike) or go to the network via regular DNS/mDNS/LLMNR lookups (in case of /etc/hosts entries).</dl>
<p> <code>&#8211;cache=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter; used in conjunction with <code>query</code>. If true (the default), lookups use the local DNS resource record cache. If false, lookups are routed to the network instead, regardless if already available in the local cache.</dl>
<p> <code>&#8211;zone=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter; used in conjunction with <code>query</code>. If true (the default), lookups are answered from locally registered LLMNR or mDNS resource records, if defined. If false, locally registered LLMNR/mDNS records are not considered for the lookup request.</dl>
<p> <code>&#8211;trust-anchor=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter; used in conjunction with <code>query</code>. If true (the default), lookups for DS and DNSKEY are answered from the local DNSSEC trust anchors if possible. If false, the local trust store is not considered for the lookup request.</dl>
<p> <code>&#8211;network=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter; used in conjunction with <code>query</code>. If true (the default), lookups are answered via DNS, LLMNR or mDNS network requests if they cannot be synthesized locally, or be answered from the local cache, zone or trust anchors (see above). If false, the request is not answered from the network and will thus fail if none of the indicated sources can answer them.</dl>
<p> <code>&#8211;search=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter. If true (the default), any specified single-label hostnames will be searched in the domains configured in the search domain list, if it is non-empty. Otherwise, the search domain logic is disabled. Note that this option has no effect if <code>&#8211;type=</code> is used (see above), in which case the search domain logic is unconditionally turned off.</dl>
<p> <code>&#8211;raw</code>[=payload|packet]</p>
<dl>
<dt>
<dd> Dump the answer as binary data. If there is no argument or if the argument is &quot;payload&quot;, the payload of the packet is exported. If the argument is &quot;packet&quot;, the whole packet is dumped in wire format, prefixed by length specified as a little-endian 64-bit number. This format allows multiple packets to be dumped and unambiguously parsed.</dl>
<p> <code>&#8211;legend=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter. If true (the default), column headers and meta information about the query response are shown. Otherwise, this output is suppressed.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<h2>COMPATIBILITY WITH <a href="/docs/linux/man/8-resolvconf/">RESOLVCONF</a>(8)</h2>
<p> <code>resolvectl</code> is a multi-call binary. When invoked as &quot;resolvconf&quot; (generally achieved by means of a symbolic link of this name to the <code>resolvectl</code> binary) it is run in a limited <code><a href="/docs/linux/man/8-resolvconf/">resolvconf</a></code>(8) compatibility mode. It accepts mostly the same arguments and pushes all data into <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8), similar to how <code>dns</code> and <code>domain</code> commands operate. Note that <code>systemd-resolved.service</code> is the only supported backend, which is different from other implementations of this command. </p>
<p> /etc/resolv.conf will only be updated with servers added with this command when /etc/resolv.conf is a symlink to /run/systemd/resolve/resolv.conf, and not a static file. See the discussion of /etc/resolv.conf handling in <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8). </p>
<p> Not all operations supported by other implementations are supported natively. Specifically: </p>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Registers per-interface DNS configuration data with <code>systemd-resolved</code>. Expects a network interface name as only command line argument. Reads <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5)-compatible DNS configuration data from its standard input. Relevant fields are &quot;nameserver&quot; and &quot;domain&quot;/&quot;search&quot;. This command is mostly identical to invoking <code>resolvectl</code> with a combination of <code>dns</code> and <code>domain</code> commands.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> Unregisters per-interface DNS configuration data with <code>systemd-resolved</code>. This command is mostly identical to invoking <code>resolvectl revert</code>.</dl>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> When specified <code>-a</code> and <code>-d</code> will not complain about missing network interfaces and will silently execute no operation in that case.</dl>
<p> <code>-x</code></p>
<dl>
<dt>
<dd> This switch for &quot;exclusive&quot; operation is supported only partially. It is mapped to an additional configured search domain of &quot;~.&quot; &#8212; i.e. ensures that DNS traffic is preferably routed to the DNS servers on this interface, unless there are other, more specific domains configured on other interfaces.</dl>
<p> <code>-m</code>, <code>-p</code></p>
<dl>
<dt>
<dd> These switches are not supported and are silently ignored.</dl>
<p> <code>-u</code>, <code>-I</code>, <code>-i</code>, <code>-l</code>, <code>-R</code>, <code>-r</code>, <code>-v</code>, <code>-V</code>, <code>&#8211;enable-updates</code>, <code>&#8211;disable-updates</code>, <code>&#8211;are-updates-enabled</code></p>
<dl>
<dt>
<dd> These switches are not supported and the command will fail if used.</dl>
<p> See <code><a href="/docs/linux/man/8-resolvconf/">resolvconf</a></code>(8) for details on those command line options.</p>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Retrieve the addresses of the &quot;<a rel="nofollow" href="http://www.0pointer.net">www.0pointer.net</a>&quot; domain (A and AAAA resource records)</code> </p>
<dl>
<dt>
<dd>
<pre>
$ resolvectl query <a rel="nofollow" href="http://www.0pointer.net">www.0pointer.net</a>
<a rel="nofollow" href="http://www.0pointer.net">www.0pointer.net</a>: 2a01:238:43ed:c300:10c3:bcf3:3266:da74
                  85.214.157.71
-- Information acquired via protocol DNS in 611.6ms.
-- Data is authenticated: no
</pre>
</dl>
<p> <code>Example 2. Retrieve the domain of the &quot;85.214.157.71&quot; IP address (PTR resource record)</code> </p>
<dl>
<dt>
<dd>
<pre>
$ resolvectl query 85.214.157.71
85.214.157.71: gardel.0pointer.net
-- Information acquired via protocol DNS in 1.2997s.
-- Data is authenticated: no
</pre>
</dl>
<p> <code>Example 3. Retrieve the MX record of the &quot;yahoo.com&quot; domain</code> </p>
<dl>
<dt>
<dd>
<pre>
$ resolvectl --legend=no -t MX query yahoo.com
yahoo.com. IN MX    1 mta7.am0.yahoodns.net
yahoo.com. IN MX    1 mta6.am0.yahoodns.net
yahoo.com. IN MX    1 mta5.am0.yahoodns.net
</pre>
</dl>
<p> <code>Example 4. Resolve an SRV service</code> </p>
<dl>
<dt>
<dd>
<pre><code>
$ resolvectl service _xmpp - server._tcp gmail.com _xmpp - server._tcp / gmail.com : alt1.xmpp - server.l.google.com : 5269 [priority = 20, weight = 0] 173.194.210.125 alt4.xmpp - server.l.google.com : 5269 [priority = 20, weight = 0] 173.194.65.125 ...
</code></pre>
</dl>
<p> <code>Example 5. Retrieve a PGP key (OPENPGP resource record)</code> </p>
<dl>
<dt>
<dd>
<pre>
$ resolvectl openpgp zbyszek [at] fedoraproject.org
d08ee310438ca124a6149ea5cc21b6313b390dce485576eff96f8722._openpgpkey.fedoraproject.org. IN OPENPGPKEY
        mQINBFBHPMsBEACeInGYJCb+7TurKfb6wGyTottCDtiSJB310i37/6ZYoeIay/5soJjlMyf
        MFQ9T2XNT/0LM6gTa0MpC1st9LnzYTMsT6tzRly1D1UbVI6xw0g0vE5y2Cjk3xUwAynCsSs
        ...
</pre>
</dl>
<p> <code>Example 6. Retrieve a TLS key (TLSA resource record)</code> </p>
<dl>
<dt>
<dd>
<pre>
$ resolvectl tlsa tcp fedoraproject.org:443
_443._tcp.fedoraproject.org IN TLSA 0 0 1 19400be5b7a31fb733917700789d2f0a2471c0c9d506c0e504c06c16d7cb17c0
        -- Cert. usage: CA constraint
        -- Selector: Full Certificate
        -- Matching type: SHA-256
</pre>
</dl>
<p> &quot;tcp&quot; and &quot;:443&quot; are optional and could be skipped.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8), <code><a href="/docs/linux/man/5-systemd-dnssd/">systemd.dnssd</a></code>(5), <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8), <code><a href="/docs/linux/man/8-resolvconf/">resolvconf</a></code>(8)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> DNS-SD</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://tools.ietf.org/html/rfc6763">https://tools.ietf.org/html/rfc6763</a></dl>
<dt> 2.</p>
<dd> SRV</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://tools.ietf.org/html/rfc2782">https://tools.ietf.org/html/rfc2782</a></dl>
<dt> 3.</p>
<dd> RFC 7929</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://tools.ietf.org/html/rfc7929">https://tools.ietf.org/html/rfc7929</a></dl>
<dt> 4.</p>
<dd> RFC 6698</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://tools.ietf.org/html/rfc6698">https://tools.ietf.org/html/rfc6698</a></dl>
<dt> 5.</p>
<dd> Link-Local Multicast Name Resolution</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://tools.ietf.org/html/rfc4795">https://tools.ietf.org/html/rfc4795</a></dl>
<dt> 6.</p>
<dd> Multicast DNS</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.ietf.org/rfc/rfc6762.txt">https://www.ietf.org/rfc/rfc6762.txt</a></dl>
</dl>
<h2>Index</h2>
