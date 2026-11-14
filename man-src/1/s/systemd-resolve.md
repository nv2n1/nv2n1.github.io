---
title: "systemd-resolve(1)"
name: "systemd-resolve"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-resolve/"
description: "resolvectl, resolvconf, systemd-resolve – Resolve domain names, IPV4 and IPv6 addresses, DNS resource records, and services; introspect and reconfigure the DNS resolver"
---

<h2 class="name">NAME</h2>
<p> resolvectl, resolvconf, systemd-resolve &#8211; Resolve domain names, IPV4 and IPv6 addresses, DNS resource records, and services; introspect and reconfigure the DNS resolver </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>resolvectl</code> [OPTIONS&#8230;] {COMMAND} [NAME&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>resolvectl</code></p>
<dd>may be used to resolve domain names, IPv4 and IPv6 addresses, DNS resource records and services with the <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8) resolver service. By default, the specified list of parameters will be resolved as hostnames, retrieving their IPv4 and IPv6 addresses. If the parameters specified are formatted as IPv4 or IPv6 operation the reverse operation is done, and a hostname is retrieved for the specified addresses. </p>
<p> The program&#8217;s output contains information about the protocol used for the look-up and on which network interface the data was discovered. It also contains information on whether the information could be authenticated. All data for which local DNSSEC validation succeeds is considered authenticated. Moreover all data originating from local, trusted sources is also reported authenticated, including resolution of the local host name, the &quot;localhost&quot; host name or all data from /etc/hosts.</p>
<h2>COMMANDS</h2>
<p> <code>query</code> <i>HOSTNAME|ADDRESS</i>&#8230;</p>
<dl>
<dt>
<dd> Resolve domain names, IPv4 and IPv6 addresses.</dl>
<p> <code>service</code> [[<i>NAME</i>] <i>TYPE</i>] <i>DOMAIN</i></p>
<dl>
<dt>
<dd> Resolve m[blue]<code>DNS-SD</code>m[]<font SIZE="-2">[1]</font> and m[blue]<code>SRV</code>m[]<font SIZE="-2">[2]</font> services, depending on the specified list of parameters. If three parameters are passed the first is assumed to be the DNS-SD service name, the second the SRV service type, and the third the domain to search in. In this case a full DNS-SD style SRV and TXT lookup is executed. If only two parameters are specified, the first is assumed to be the SRV service type, and the second the domain to look in. In this case no TXT RR is requested. Finally, if only one parameter is specified, it is assumed to be a domain name, that is already prefixed with an SRV type, and an SRV lookup is done (no TXT).</dl>
<p> <code>openpgp</code> <i>EMAIL [at] DOMAIN</i>&#8230;</p>
<dl>
<dt>
<dd> Query PGP keys stored as m[blue]<code>OPENPGPKEY</code>m[]<font SIZE="-2">[3]</font> resource records. Specified e-mail addresses are converted to the corresponding DNS domain name, and any OPENPGPKEY keys are printed.</dl>
<p> <code>tlsa</code> [<i>FAMILY</i>] <i>DOMAIN</i>[:<i>PORT</i>]&#8230;</p>
<dl>
<dt>
<dd> Query TLS public keys stored as m[blue]<code>TLSA</code>m[]<font SIZE="-2">[4]</font> resource records. A query will be performed for each of the specified names prefixed with the port and family (&quot;_<i>port</i>._<i>family</i>.<i>domain</i>&quot;). The port number may be specified after a colon (&quot;:&quot;), otherwise <code>443</code> will be used by default. The family may be specified as the first argument, otherwise <code>tcp</code> will be used.</dl>
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
<dd> Get/set per-interface DNS configuration. These commands may be used to configure various DNS settings for network interfaces. These commands may be used to inform <code>systemd-resolved</code> or <code>systemd-networkd</code> about per-interface DNS configuration determined through external means. The <code>dns</code> command expects IPv4 or IPv6 address specifications of DNS servers to use. The <code>domain</code> command expects valid DNS domains, possibly prefixed with &quot;~&quot;, and configures a per-interface search or route-only domain. The <code>default-route</code> command expects a boolean parameter, and configures whether the link may be used as default route for DNS lookups, i.e. if it is suitable for lookups on domains no other link explicitly is configured for. The <code>llmnr</code>, <code>mdns</code>, <code>dnssec</code> and <code>dnsovertls</code> commands may be used to configure the per-interface LLMNR, MulticastDNS, DNSSEC and DNSOverTLS settings. Finally, <code>nta</code> command may be used to configure additional per-interface DNSSEC NTA domains. </p>
<p> Commands <code>dns</code>, <code>domain</code> and <code>nta</code> can take a single empty string argument to clear their respective value lists. </p>
<p> For details about these settings, their possible values and their effect, see the corresponding settings in <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5).</dl>
<p> <code>revert </code><i>LINK</i></p>
<dl>
<dt>
<dd> Revert the per-interface DNS configuration. If the DNS configuration is reverted all per-interface DNS setting are reset to their defaults, undoing all effects of <code>dns</code>, <code>domain</code>, <code>default-route</code>, <code>llmnr</code>, <code>mdns</code>, <code>dnssec</code>, <code>dnsovertls</code>, <code>nta</code>. Note that when a network interface disappears all configuration is lost automatically, an explicit reverting is not necessary in that case.</dl>
<h2>OPTIONS</h2>
<p> <code>-4</code>, <code>-6</code></p>
<dl>
<dt>
<dd> By default, when resolving a hostname, both IPv4 and IPv6 addresses are acquired. By specifying <code>-4</code> only IPv4 addresses are requested, by specifying <code>-6</code> only IPv6 addresses are requested.</dl>
<p> <code>-i</code> <i>INTERFACE</i>, <code>&#8211;interface=</code><i>INTERFACE</i></p>
<dl>
<dt>
<dd> Specifies the network interface to execute the query on. This may either be specified as numeric interface index or as network interface string (e.g. &quot;en0&quot;). Note that this option has no effect if system-wide DNS configuration (as configured in /etc/resolv.conf or /etc/systemd/resolve.conf) in place of per-link configuration is used.</dl>
<p> <code>-p</code> <i>PROTOCOL</i>, <code>&#8211;protocol=</code><i>PROTOCOL</i></p>
<dl>
<dt>
<dd> Specifies the network protocol for the query. May be one of &quot;dns&quot; (i.e. classic unicast DNS), &quot;llmnr&quot; (m[blue]<code>Link-Local Multicast Name Resolution</code>m[]<font SIZE="-2">[5]</font>), &quot;llmnr-ipv4&quot;, &quot;llmnr-ipv6&quot; (LLMNR via the indicated underlying IP protocols), &quot;mdns&quot; (m[blue]<code>Multicast DNS</code>m[]<font SIZE="-2">[6]</font>), &quot;mdns-ipv4&quot;, &quot;mdns-ipv6&quot; (MDNS via the indicated underlying IP protocols). By default the lookup is done via all protocols suitable for the lookup. If used, limits the set of protocols that may be used. Use this option multiple times to enable resolving via multiple protocols at the same time. The setting &quot;llmnr&quot; is identical to specifying this switch once with &quot;llmnr-ipv4&quot; and once via &quot;llmnr-ipv6&quot;. Note that this option does not force the service to resolve the operation with the specified protocol, as that might require a suitable network interface and configuration. The special value &quot;help&quot; may be used to list known values.</dl>
<p> <code>-t</code> <i>TYPE</i>, <code>&#8211;type=</code><i>TYPE</i>, <code>-c</code> <i>CLASS</i>, <code>&#8211;class=</code><i>CLASS</i></p>
<dl>
<dt>
<dd> Specifies the DNS resource record type (e.g. A, AAAA, MX, &#8230;) and class (e.g. IN, ANY, &#8230;) to look up. If these options are used a DNS resource record set matching the specified class and type is requested. The class defaults to IN if only a type is specified. The special value &quot;help&quot; may be used to list known values.</dl>
<p> <code>&#8211;service-address=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter. If true (the default), when doing a service lookup with <code>&#8211;service</code> the hostnames contained in the SRV resource records are resolved as well.</dl>
<p> <code>&#8211;service-txt=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter. If true (the default), when doing a DNS-SD service lookup with <code>&#8211;service</code> the TXT service metadata record is resolved as well.</dl>
<p> <code>&#8211;cname=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter. If true (the default), DNS CNAME or DNAME redirections are followed. Otherwise, if a CNAME or DNAME record is encountered while resolving, an error is returned.</dl>
<p> <code>&#8211;search=</code><i>BOOL</i></p>
<dl>
<dt>
<dd> Takes a boolean parameter. If true (the default), any specified single-label hostnames will be searched in the domains configured in the search domain list, if it is non-empty. Otherwise, the search domain logic is disabled.</dl>
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
<p> <code>resolvectl</code> is a multi-call binary. When invoked as &quot;resolvconf&quot; (generally achieved by means of a symbolic link of this name to the <code>resolvectl</code> binary) it is run in a limited <code><a href="/docs/linux/man/8-resolvconf/">resolvconf</a></code>(8) compatibility mode. It accepts mostly the same arguments and pushes all data into <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8), similar to how <code>dns</code> and <code>domain</code> commands operate. Note that <code>systemd-resolved.service</code> is the only supported backend, which is different from other implementations of this command. Note that not all operations supported by other implementations are supported natively. Specifically: </p>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Registers per-interface DNS configuration data with <code>systemd-resolved</code>. Expects a network interface name as only command line argument. Reads <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5) compatible DNS configuration data from its standard input. Relevant fields are &quot;nameserver&quot; and &quot;domain&quot;/&quot;search&quot;. This command is mostly identical to invoking <code>resolvectl</code> with a combination of <code>dns</code> and <code>domain</code> commands.</dl>
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
<p> See <code><a href="/docs/linux/man/8-resolvconf/">resolvconf</a></code>(8) for details on this command line options.</p>
<h2>BACKWARDS COMPATIBILITY WITH SYSTEMD-RESOLVE</h2>
<p> <code>resolvectl</code> is a multi-call binary, which previously was named &quot;systemd-resolve&quot; and used slightly different parameters. When it is invoked as &quot;systemd-resolve&quot; (generally achieved by means of a symbolic link of this name to the <code>resolvectl</code> binary), it runs in compatibility mode. For details on the specific parameters and calling syntax, see the output from <code>systemd-resolve &#8211;help</code>. Calling the binary as &quot;systemd-resolve&quot; is deprecated and should only be done for backwards compatibility. All current and new use should call the binary as &quot;resolvectl&quot;.</p>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Retrieve the addresses of the &quot;<a rel="nofollow" href="http://www.0pointer.net">www.0pointer.net</a>&quot; domain</code> </p>
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
<p> <code>Example 2. Retrieve the domain of the &quot;85.214.157.71&quot; IP address</code> </p>
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
<p> <code>Example 5. Retrieve a PGP key</code> </p>
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
<p> <code>Example 6. Retrieve a TLS key (&quot;tcp&quot; and &quot;:443&quot; could be skipped)</code> </p>
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
<dd> OPENPGPKEY</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://tools.ietf.org/html/rfc7929">https://tools.ietf.org/html/rfc7929</a></dl>
<dt> 4.</p>
<dd> TLSA</p>
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
