---
title: "systemd-resolved-service(8)"
name: "systemd-resolved-service"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-resolved-service/"
description: "systemd-resolved.service, systemd-resolved – Network Name Resolution manager"
---

<p>systemd-resolved.service, systemd-resolved &#8211; Network Name Resolution manager</p>
<h2>Synopsis</h2>
<p>systemd-resolved.service </p>
<p> /lib/systemd/systemd-resolved</p>
<h2>Description</h2>
<p><code>systemd-resolved</code> is a system service that provides network name resolution to local applications. It implements a caching and validating DNS/DNSSEC stub resolver, as well as an LLMNR and MulticastDNS resolver and responder. Local applications may submit network name resolution requests via three interfaces: </p>
<dl>
<dd>&bull; The native, fully-featured API <code>systemd-resolved</code> exposes on the bus, see <code><a href="/docs/linux/man/5-org-freedesktop-resolve1/">org.freedesktop.resolve1</a></code>(5) and <code><a href="/docs/linux/man/5-org-freedesktop-logcontrol1/">org.freedesktop.LogControl1</a></code>(5) for details. Usage of this API is generally recommended to clients as it is asynchronous and fully featured (for example, properly returns DNSSEC validation status and interface scope for addresses as necessary for supporting link-local networking).</dl>
<dl>
<dd>&bull; The glibc <code><a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a></code>(3) API as defined by m[blue]<code>RFC3493</code>m[]<font SIZE="-2">[1]</font> and its related resolver functions, including <code><a href="/docs/linux/man/3-gethostbyname/">gethostbyname</a></code>(3). This API is widely supported, including beyond the Linux platform. In its current form it does not expose DNSSEC validation status information however, and is synchronous only. This API is backed by the glibc Name Service Switch (<code><a href="/docs/linux/man/5-nss/">nss</a></code>(5)). Usage of the glibc NSS module <code><a href="/docs/linux/man/8-nss-resolve/">nss-resolve</a></code>(8) is required in order to allow glibc&#8217;s NSS resolver functions to resolve hostnames via <code>systemd-resolved</code>.</dl>
<dl>
<dd>&bull; Additionally, <code>systemd-resolved</code> provides a local DNS stub listener on IP address 127.0.0.53 on the local loopback interface. Programs issuing DNS requests directly, bypassing any local API may be directed to this stub, in order to connect them to <code>systemd-resolved</code>. Note however that it is strongly recommended that local programs use the glibc NSS or bus APIs instead (as described above), as various network resolution concepts (such as link-local addressing, or LLMNR Unicode domains) cannot be mapped to the unicast DNS protocol.</dl>
<p> The DNS servers contacted are determined from the global settings in /etc/systemd/resolved.conf, the per-link static settings in /etc/systemd/network/*.network files (in case <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8) is used), the per-link dynamic settings received over DHCP, information provided via <code><a href="/docs/linux/man/1-resolvectl/">resolvectl</a></code>(1), and any DNS server information made available by other system services. See <code><a href="/docs/linux/man/5-resolved-conf/">resolved.conf</a></code>(5) and <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5) for details about systemd&#8217;s own configuration files for DNS servers. To improve compatibility, /etc/resolv.conf is read in order to discover configured system DNS servers, but only if it is not a symlink to /run/systemd/resolve/stub-resolv.conf, /usr/lib/systemd/resolv.conf or /run/systemd/resolve/resolv.conf (see below).</p>
<h2>Synthetic Records</h2>
<p><code>systemd-resolved</code> synthesizes DNS resource records (RRs) for the following cases: </p>
<dl>
<dd>&bull; The local, configured hostname is resolved to all locally configured IP addresses ordered by their scope, or &#8212; if none are configured &#8212; the IPv4 address 127.0.0.2 (which is on the local loopback interface) and the IPv6 address ::1 (which is the local host).</dl>
<dl>
<dd>&bull; The hostnames &quot;localhost&quot; and &quot;localhost.localdomain&quot; as well as any hostname ending in &quot;.localhost&quot; or &quot;.localhost.localdomain&quot; are resolved to the IP addresses 127.0.0.1 and ::1.</dl>
<dl>
<dd>&bull; The hostname &quot;_gateway&quot; is resolved to all current default routing gateway addresses, ordered by their metric. This assigns a stable hostname to the current gateway, useful for referencing it independently of the current network configuration state.</dl>
<dl>
<dd>&bull; The hostname &quot;_outbound&quot; is resolved to the local IPv4 and IPv6 addresses that are most likely used for communication with other hosts. This is determined by requesting a routing decision to the configured default gateways from the kernel and then using the local IP addresses selected by this decision. This hostname is only available if there is at least one local default gateway configured. This assigns a stable hostname to the local outbound IP addresses, useful for referencing them independently of the current network configuration state.</dl>
<dl>
<dd>&bull; The mappings defined in /etc/hosts are resolved to their configured addresses and back, but they will not affect lookups for non-address types (like MX). Support for /etc/hosts may be disabled with <i>ReadEtcHosts=no</i>, see <code><a href="/docs/linux/man/5-resolved-conf/">resolved.conf</a></code>(5).</dl>
<h2>Protocols And Routing</h2>
<p>The lookup requests that systemd-resolved.service receives are routed to the available DNS servers, LLMNR, and MulticastDNS interfaces according to the following rules: </p>
<dl>
<dd>&bull; Names for which synthetic records are generated (the local hostname, &quot;localhost&quot; and &quot;localdomain&quot;, local gateway, as listed in the previous section) and addresses configured in /etc/hosts are never routed to the network and a reply is sent immediately.</dl>
<dl>
<dd>&bull; Single-label names are resolved using LLMNR on all local interfaces where LLMNR is enabled. Lookups for IPv4 addresses are only sent via LLMNR on IPv4, and lookups for IPv6 addresses are only sent via LLMNR on IPv6. Note that lookups for single-label synthesized names are not routed to LLMNR, MulticastDNS or unicast DNS.</dl>
<dl>
<dd>&bull; Queries for the address records (A and AAAA) of single-label non-synthesized names are resolved via unicast DNS using search domains. For any interface which defines search domains, such look-ups are routed to the servers defined for that interface, suffixed with each of those search domains. When global search domains are defined, such look-ups are routed to the global servers. For each search domain, queries are performed by suffixing the name with each of the search domains in turn. Additionally, lookup of single-label names via unicast DNS may be enabled with the <i>ResolveUnicastSingleLabel=yes</i> setting. The details of which servers are queried and how the final reply is chosen are described below. Note that this means that address queries for single-label names are never sent out to remote DNS servers by default, and resolution is only possible if search domains are defined.</dl>
<dl>
<dd>&bull; Multi-label names with the domain suffix &quot;.local&quot; are resolved using MulticastDNS on all local interfaces where MulticastDNS is enabled. As with LLMNR, IPv4 address lookups are sent via IPv4 and IPv6 address lookups are sent via IPv6.</dl>
<dl>
<dd>&bull; Queries for multi-label names are routed via unicast DNS on local interfaces that have a DNS server configured, plus the globally configured DNS servers if there are any. Which interfaces are used is determined by the routing logic based on search and route-only domains, described below. Note that by default, lookups for domains with the &quot;.local&quot; suffix are not routed to DNS servers, unless the domain is specified explicitly as routing or search domain for the DNS server and interface. This means that on networks where the &quot;.local&quot; domain is defined in a site-specific DNS server, explicit search or routing domains need to be configured to make lookups work within this DNS domain. Note that these days, it&#8217;s generally recommended to avoid defining &quot;.local&quot; in a DNS server, as m[blue]<code>RFC6762</code>m[]<font SIZE="-2">[2]</font> reserves this domain for exclusive MulticastDNS use.</dl>
<dl>
<dd>&bull; Address lookups (reverse lookups) are routed similarly to multi-label names, with the exception that addresses from the link-local address range are never routed to unicast DNS and are only resolved using LLMNR and MulticastDNS (when enabled).</dl>
<p> If lookups are routed to multiple interfaces, the first successful response is returned (thus effectively merging the lookup zones on all matching interfaces). If the lookup failed on all interfaces, the last failing response is returned. </p>
<p> Routing of lookups is determined by the per-interface routing domains (search and route-only) and global search domains. See <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5) and <code><a href="/docs/linux/man/1-resolvectl/">resolvectl</a></code>(1) for a description how those settings are set dynamically and the discussion of <i>Domains=</i> in <code><a href="/docs/linux/man/5-resolved-conf/">resolved.conf</a></code>(5) for a description of globally configured DNS settings. </p>
<p> The following query routing logic applies for unicast DNS lookups initiated by systemd-resolved.service: </p>
<dl>
<dd>&bull; If a name to look up matches (that is: is equal to or has as suffix) any of the configured routing domains (search or route-only) of any link, or the globally configured DNS settings, &quot;best matching&quot; routing domain is determined: the matching one with the most labels. The query is then sent to all DNS servers of any links or the globally configured DNS servers associated with this &quot;best matching&quot; routing domain. (Note that more than one link might have this same &quot;best matching&quot; routing domain configured, in which case the query is sent to all of them in parallel). </p>
<p> In case of single-label names, when search domains are defined, the same logic applies, except that the name is first suffixed by each of the search domains in turn. Note that this search logic doesn&#8217;t apply to any names with at least one dot. Also see the discussion about compatibility with the traditional glibc resolver below.</dl>
<dl>
<dd>&bull; If a query does not match any configured routing domain (either per-link or global), it is sent to all DNS servers that are configured on links with the <i>DefaultRoute=</i> option set, as well as the globally configured DNS server.</dl>
<dl>
<dd>&bull; If there is no link configured as <i>DefaultRoute=</i> and no global DNS server configured, one of the compiled-in fallback DNS servers is used.</dl>
<dl>
<dd>&bull; Otherwise the unicast DNS query fails, as no suitable DNS servers can be determined.</dl>
<p> The <i>DefaultRoute=</i> option is a boolean setting configurable with <code>resolvectl</code> or in .network files. If not set, it is implicitly determined based on the configured DNS domains for a link: if there&#8217;s a route-only domain other than &quot;~.&quot;, it defaults to false, otherwise to true. </p>
<p> Effectively this means: in order to support single-label non-synthesized names, define appropriate search domains. In order to preferably route all DNS queries not explicitly matched by routing domain configuration to a specific link, configure a &quot;~.&quot; route-only domain on it. This will ensure that other links will not be considered for these queries (unless they too carry such a routing domain). In order to route all such DNS queries to a specific link only if no other link is preferred, set the <i>DefaultRoute=</i> option for the link to true and do not configure a &quot;~.&quot; route-only domain on it. Finally, in order to ensure that a specific link never receives any DNS traffic not matching any of its configured routing domains, set the <i>DefaultRoute=</i> option for it to false. </p>
<p> See <code><a href="/docs/linux/man/5-org-freedesktop-resolve1/">org.freedesktop.resolve1</a></code>(5) for information about the D-Bus APIs systemd-resolved provides.</p>
<h2>Compatibility With The Traditional Glibc Stub Resolver</h2>
<p>This section provides a short summary of differences in the stub resolver implemented by <code><a href="/docs/linux/man/8-nss-resolve/">nss-resolve</a></code>(8) together with <code>systemd-resolved</code> and the traditional stub resolver implemented in nss-dns. </p>
<dl>
<dd>&bull; Some names are always resolved internally (see Synthetic Records above). Traditionally they would be resolved by nss-files if provided in /etc/hosts. But note that the details of how a query is constructed are under the control of the client library. nss-dns will first try to resolve names using search domains and even if those queries are routed to systemd-resolved, it will send them out over the network using the usual rules for multi-label name routing <font SIZE="-2">[3]</font>.</dl>
<dl>
<dd>&bull; Single-label names are not resolved for A and AAAA records using unicast DNS (unless overridden with <i>ResolveUnicastSingleLabel=</i>, see <code><a href="/docs/linux/man/5-resolved-conf/">resolved.conf</a></code>(5)). This is similar to the <code>no-tld-query</code> option being set in <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5).</dl>
<dl>
<dd>&bull; Search domains are not used for <i>suffixing</i> of multi-label names. (Search domains are nevertheless used for lookup <i>routing</i>, for names that were originally specified as single-label or multi-label.) Any name with at least one dot is always interpreted as a FQDN. nss-dns would resolve names both as relative (using search domains) and absolute FQDN names. Some names would be resolved as relative first, and after that query has failed, as absolute, while other names would be resolved in opposite order. The <i>ndots</i> option in /etc/resolv.conf was used to control how many dots the name needs to have to be resolved as relative first. This stub resolver does not implement this at all: multi-label names are only resolved as FQDNs.<font SIZE="-2">[4]</font></dl>
<dl>
<dd>&bull; This resolver has a notion of the special &quot;.local&quot; domain used for MulticastDNS, and will not route queries with that suffix to unicast DNS servers unless explicitly configured, see above. Also, reverse lookups for link-local addresses are not sent to unicast DNS servers.</dl>
<dl>
<dd>&bull; This resolver reads and caches /etc/hosts internally. (In other words, nss-resolve replaces nss-files in addition to nss-dns). Entries in /etc/hosts have highest priority.</dl>
<dl>
<dd>&bull; This resolver also implements LLMNR and MulticastDNS in addition to the classic unicast DNS protocol, and will resolve single-label names using LLMNR (when enabled) and names ending in &quot;.local&quot; using MulticastDNS (when enabled).</dl>
<dl>
<dd>&bull; Environment variables <i>$LOCALDOMAIN</i> and <i>$RES_OPTIONS</i> described in <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5) are not supported currently.</dl>
<h2>/Etc/Resolv.Conf</h2>
<p>Four modes of handling /etc/resolv.conf (see <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5)) are supported: </p>
<dl>
<dd>&bull; <code>systemd-resolved</code> maintains the /run/systemd/resolve/stub-resolv.conf file for compatibility with traditional Linux programs. This file may be symlinked from /etc/resolv.conf. This file lists the 127.0.0.53 DNS stub (see above) as the only DNS server. It also contains a list of search domains that are in use by systemd-resolved. The list of search domains is always kept up-to-date. Note that /run/systemd/resolve/stub-resolv.conf should not be used directly by applications, but only through a symlink from /etc/resolv.conf. This file may be symlinked from /etc/resolv.conf in order to connect all local clients that bypass local DNS APIs to <code>systemd-resolved</code> with correct search domains settings. This mode of operation is recommended.</dl>
<dl>
<dd>&bull; A static file /usr/lib/systemd/resolv.conf is provided that lists the 127.0.0.53 DNS stub (see above) as only DNS server. This file may be symlinked from /etc/resolv.conf in order to connect all local clients that bypass local DNS APIs to <code>systemd-resolved</code>. This file does not contain any search domains.</dl>
<dl>
<dd>&bull; <code>systemd-resolved</code> maintains the /run/systemd/resolve/resolv.conf file for compatibility with traditional Linux programs. This file may be symlinked from /etc/resolv.conf and is always kept up-to-date, containing information about all known DNS servers. Note the file format&#8217;s limitations: it does not know a concept of per-interface DNS servers and hence only contains system-wide DNS server definitions. Note that /run/systemd/resolve/resolv.conf should not be used directly by applications, but only through a symlink from /etc/resolv.conf. If this mode of operation is used local clients that bypass any local DNS API will also bypass <code>systemd-resolved</code> and will talk directly to the known DNS servers.</dl>
<dl>
<dd>&bull; Alternatively, /etc/resolv.conf may be managed by other packages, in which case <code>systemd-resolved</code> will read it for DNS configuration data. In this mode of operation <code>systemd-resolved</code> is consumer rather than provider of this configuration file.</dl>
<p> Note that the selected mode of operation for this file is detected fully automatically, depending on whether /etc/resolv.conf is a symlink to /run/systemd/resolve/resolv.conf or lists 127.0.0.53 as DNS server.</p>
<h2>Signals</h2>
<p><code>SIGUSR1</code></p>
<dl>
<dd>Upon reception of the <code>SIGUSR1</code> process signal <code>systemd-resolved</code> will dump the contents of all DNS resource record caches it maintains, as well as all feature level information it learnt about configured DNS servers into the system logs.</dl>
<p> <code>SIGUSR2</code></p>
<dl>
<dd>Upon reception of the <code>SIGUSR2</code> process signal <code>systemd-resolved</code> will flush all caches it maintains. Note that it should normally not be necessary to request this explicitly &#8211; except for debugging purposes &#8211; as <code>systemd-resolved</code> flushes the caches automatically anyway any time the host&#8217;s network configuration changes. Sending this signal to <code>systemd-resolved</code> is equivalent to the <code>resolvectl flush-caches</code> command, however the latter is recommended since it operates in a synchronous way.</dl>
<p> <code>SIGRTMIN+1</code></p>
<dl>
<dd>Upon reception of the <code>SIGRTMIN+1</code> process signal <code>systemd-resolved</code> will forget everything it learnt about the configured DNS servers. Specifically any information about server feature support is flushed out, and the server feature probing logic is restarted on the next request, starting with the most fully featured level. Note that it should normally not be necessary to request this explicitly &#8211; except for debugging purposes &#8211; as <code>systemd-resolved</code> automatically forgets learnt information any time the DNS server configuration changes. Sending this signal to <code>systemd-resolved</code> is equivalent to the <code>resolvectl reset-server-features</code> command, however the latter is recommended since it operates in a synchronous way.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-resolved-conf/">resolved.conf</a></code>(5), <code><a href="/docs/linux/man/5-dnssec-trust-anchors-d/">dnssec-trust-anchors.d</a></code>(5), <code><a href="/docs/linux/man/8-nss-resolve/">nss-resolve</a></code>(8), <code><a href="/docs/linux/man/1-resolvectl/">resolvectl</a></code>(1), <code><a href="/docs/linux/man/5-resolv-conf/">resolv.conf</a></code>(5), <code><a href="/docs/linux/man/5-hosts/">hosts</a></code>(5), <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5), <code><a href="/docs/linux/man/8-systemd-networkd-service/">systemd-networkd.service</a></code>(8)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>RFC3493</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc3493">https://tools.ietf.org/html/rfc3493</a></dl>
<dt> 2.</p>
<dd>RFC6762</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc6762">https://tools.ietf.org/html/rfc6762</a></dl>
<dt> 3.</p>
<dd>For example, if /etc/resolv.conf has</p>
<dl>
<dd>
<dl>
<dd>
<pre>nameserver 127.0.0.53
search foobar.com barbar.com</pre>
</dl>
<p> and we look up &quot;localhost&quot;, nss-dns will send the following queries to systemd-resolved listening on 127.0.0.53:53: first &quot;localhost.foobar.com&quot;, then &quot;localhost.barbar.com&quot;, and finally &quot;localhost&quot;. If (hopefully) the first two queries fail, systemd-resolved will synthesize an answer for the third query.</dl>
<dl>
<dd>When using nss-dns with any search domains, it is thus crucial to always configure nss-files with higher priority and provide mappings for names that should not be resolved using search domains.</dl>
<dt> 4.</p>
<dd>There are currently more than 1500 top-level domain names defined, and new ones are added regularly, often using &quot;attractive&quot; names that are also likely to be used locally. Not looking up multi-label names in this fashion avoids fragility in both directions: a valid global name could be obscured by a local name, and resolution of a relative local name could suddenly break when a new top-level domain is created, or when a new subdomain of a top-level domain in registered. Resolving any given name as either relative or absolute avoids this ambiguity. </p>
