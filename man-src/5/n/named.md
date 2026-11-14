---
title: "named(5)"
name: "named"
section: "5"
letter: "n"
url: "/docs/linux/man/5-named/"
description: "named.conf – configuration file for named"
---

<p>named.conf &#8211; configuration file for named</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>named.conf</code></dl>
<h2>Description</h2>
<p><i>named.conf</i></p>
<dd>is the configuration file for <code>named</code>. Statements are enclosed in braces and terminated with a semi-colon. Clauses in the statements are also semi-colon terminated. The usual comment styles are supported: </p>
<p> C style: /* */ </p>
<p> C++ style: // to end of line </p>
<p> Unix style: # to end of line</p>
<h2>Acl</h2>
<dl>
<dd>
<pre>acl <i>string</i> { <i>address_match_element</i>; ... };</pre>
</dl>
<h2>Key</h2>
<dl>
<dd>
<pre>key <i>domain_name</i> {
 algorithm <i>string</i>;
 secret <i>string</i>;
};</pre>
</dl>
<h2>Masters</h2>
<dl>
<dd>
<pre>masters <i>string</i> [ port <i>integer</i> ] {
 ( <i>masters</i> | <i>ipv4_address</i> [port <i>integer</i>] |
 <i>ipv6_address</i> [port <i>integer</i>] ) [ key <i>string</i> ]; ...
};</pre>
</dl>
<h2>Server</h2>
<dl>
<dd>
<pre>server ( <i>ipv4_address</i><i>[/prefixlen]</i> | <i>ipv6_address</i><i>[/prefixlen]</i> ) {
 bogus <i>boolean</i>;
 edns <i>boolean</i>;
 edns-udp-size <i>integer</i>;
 max-udp-size <i>integer</i>;
 provide-ixfr <i>boolean</i>;
 request-ixfr <i>boolean</i>;
 keys <i>server_key</i>;
 transfers <i>integer</i>;
 transfer-format ( many-answers | one-answer );
 transfer-source ( <i>ipv4_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 transfer-source-v6 ( <i>ipv6_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 support-ixfr <i>boolean</i>; // obsolete
};</pre>
</dl>
<h2>Trusted-Keys</h2>
<dl>
<dd>
<pre>trusted-keys {
 <i>domain_name</i> <i>flags</i> <i>protocol</i> <i>algorithm</i> <i>key</i>; ... 
};</pre>
</dl>
<h2>Controls</h2>
<dl>
<dd>
<pre>controls {
 inet ( <i>ipv4_address</i> | <i>ipv6_address</i> | * )
 [ port ( <i>integer</i> | * ) ]
 allow { <i>address_match_element</i>; ... }
 [ keys { <i>string</i>; ... } ];
 unix <i>unsupported</i>; // not implemented
};</pre>
</dl>
<h2>Logging</h2>
<dl>
<dd>
<pre>logging {
 channel <i>string</i> {
 file <i>log_file</i>;
 syslog <i>optional_facility</i>;
 null;
 stderr;
 severity <i>log_severity</i>;
 print-time <i>boolean</i>;
 print-severity <i>boolean</i>;
 print-category <i>boolean</i>;
 };
 category <i>string</i> { <i>string</i>; ... };
};</pre>
</dl>
<h2>Lwres</h2>
<dl>
<dd>
<pre>lwres {
 listen-on [ port <i>integer</i> ] {
 ( <i>ipv4_address</i> | <i>ipv6_address</i> ) [ port <i>integer</i> ]; ...
 };
 view <i>string</i> <i>optional_class</i>;
 search { <i>string</i>; ... };
 ndots <i>integer</i>;
};</pre>
</dl>
<h2>Options</h2>
<dl>
<dd>
<pre>options {
 avoid-v4-udp-ports { <i>port</i>; ... };
 avoid-v6-udp-ports { <i>port</i>; ... };
 blackhole { <i>address_match_element</i>; ... };
 coresize <i>size</i>;
 datasize <i>size</i>;
 directory <i>quoted_string</i>;
 dump-file <i>quoted_string</i>;
 files <i>size</i>;
 heartbeat-interval <i>integer</i>;
 host-statistics <i>boolean</i>; // not implemented
 host-statistics-max <i>number</i>; // not implemented
 hostname ( <i>quoted_string</i> | none );
 interface-interval <i>integer</i>;
 listen-on [ port <i>integer</i> ] { <i>address_match_element</i>; ... };
 listen-on-v6 [ port <i>integer</i> ] { <i>address_match_element</i>; ... };
 match-mapped-addresses <i>boolean</i>;
 memstatistics-file <i>quoted_string</i>;
 pid-file ( <i>quoted_string</i> | none );
 port <i>integer</i>;
 querylog <i>boolean</i>;
 recursing-file <i>quoted_string</i>;
 reserved-sockets <i>integer</i>;
 random-device <i>quoted_string</i>;
 recursive-clients <i>integer</i>;
 serial-query-rate <i>integer</i>;
 server-id ( <i>quoted_string</i> | none |;
 stacksize <i>size</i>;
 statistics-file <i>quoted_string</i>;
 statistics-interval <i>integer</i>; // not yet implemented
 tcp-clients <i>integer</i>;
 tcp-listen-queue <i>integer</i>;
 tkey-dhkey <i>quoted_string</i> <i>integer</i>;
 tkey-gssapi-credential <i>quoted_string</i>;
 tkey-domain <i>quoted_string</i>;
 transfers-per-ns <i>integer</i>;
 transfers-in <i>integer</i>;
 transfers-out <i>integer</i>;
 use-ixfr <i>boolean</i>;
 version ( <i>quoted_string</i> | none );
 allow-recursion { <i>address_match_element</i>; ... };
 allow-recursion-on { <i>address_match_element</i>; ... };
 sortlist { <i>address_match_element</i>; ... };
 topology { <i>address_match_element</i>; ... }; // not implemented
 auth-nxdomain <i>boolean</i>; // default changed
 minimal-responses <i>boolean</i>;
 recursion <i>boolean</i>;
 rrset-order {
 [ class <i>string</i> ] [ type <i>string</i> ]
 [ name <i>quoted_string</i> ] <i>string</i> <i>string</i>; ...
 };
 provide-ixfr <i>boolean</i>;
 request-ixfr <i>boolean</i>;
 rfc2308-type1 <i>boolean</i>; // not yet implemented
 additional-from-auth <i>boolean</i>;
 additional-from-cache <i>boolean</i>;
 query-source ( ( <i>ipv4_address</i> | * ) | [ address ( <i>ipv4_address</i> | * ) ] ) [ port ( <i>integer</i> | * ) ];
 query-source-v6 ( ( <i>ipv6_address</i> | * ) | [ address ( <i>ipv6_address</i> | * ) ] ) [ port ( <i>integer</i> | * ) ];
 use-queryport-pool <i>boolean</i>;
 queryport-pool-ports <i>integer</i>;
 queryport-pool-updateinterval <i>integer</i>;
 cleaning-interval <i>integer</i>;
 min-roots <i>integer</i>; // not implemented
 lame-ttl <i>integer</i>;
 max-ncache-ttl <i>integer</i>;
 max-cache-ttl <i>integer</i>;
 transfer-format ( many-answers | one-answer );
 max-cache-size <i>size</i>;
 max-acache-size <i>size</i>;
 clients-per-query <i>number</i>;
 max-clients-per-query <i>number</i>;
 check-names ( master | slave | response )
 ( fail | warn | ignore );
 check-mx ( fail | warn | ignore );
 check-integrity <i>boolean</i>;
 check-mx-cname ( fail | warn | ignore );
 check-srv-cname ( fail | warn | ignore );
 cache-file <i>quoted_string</i>; // test option
 suppress-initial-notify <i>boolean</i>; // not yet implemented
 preferred-glue <i>string</i>;
 dual-stack-servers [ port <i>integer</i> ] {
 ( <i>quoted_string</i> [port <i>integer</i>] |
 <i>ipv4_address</i> [port <i>integer</i>] |
 <i>ipv6_address</i> [port <i>integer</i>] ); ...
 };
 edns-udp-size <i>integer</i>;
 max-udp-size <i>integer</i>;
 root-delegation-only [ exclude { <i>quoted_string</i>; ... } ];
 disable-algorithms <i>string</i> { <i>string</i>; ... };
 dnssec-enable <i>boolean</i>;
 dnssec-validation <i>boolean</i>;
 dnssec-lookaside <i>string</i> trust-anchor <i>string</i>;
 dnssec-must-be-secure <i>string</i> <i>boolean</i>;
 dnssec-accept-expired <i>boolean</i>;
 empty-server <i>string</i>;
 empty-contact <i>string</i>;
 empty-zones-enable <i>boolean</i>;
 disable-empty-zone <i>string</i>;
 dialup <i>dialuptype</i>;
 ixfr-from-differences <i>ixfrdiff</i>;
 allow-query { <i>address_match_element</i>; ... };
 allow-query-on { <i>address_match_element</i>; ... };
 allow-query-cache { <i>address_match_element</i>; ... };
 allow-query-cache-on { <i>address_match_element</i>; ... };
 allow-transfer { <i>address_match_element</i>; ... };
 allow-update { <i>address_match_element</i>; ... };
 allow-update-forwarding { <i>address_match_element</i>; ... };
 update-check-ksk <i>boolean</i>;
 masterfile-format ( text | raw );
 notify <i>notifytype</i>;
 notify-source ( <i>ipv4_address</i> | * ) [ port ( <i>integer</i> | * ) ];
 notify-source-v6 ( <i>ipv6_address</i> | * ) [ port ( <i>integer</i> | * ) ];
 notify-delay <i>seconds</i>;
 notify-to-soa <i>boolean</i>;
 also-notify [ port <i>integer</i> ] { ( <i>ipv4_address</i> | <i>ipv6_address</i> )
 [ port <i>integer</i> ]; ... };
 allow-notify { <i>address_match_element</i>; ... };
 forward ( first | only );
 forwarders [ port <i>integer</i> ] {
 ( <i>ipv4_address</i> | <i>ipv6_address</i> ) [ port <i>integer</i> ]; ...
 };
 max-journal-size <i>size_no_default</i>;
 max-transfer-time-in <i>integer</i>;
 max-transfer-time-out <i>integer</i>;
 max-transfer-idle-in <i>integer</i>;
 max-transfer-idle-out <i>integer</i>;
 max-retry-time <i>integer</i>;
 min-retry-time <i>integer</i>;
 max-refresh-time <i>integer</i>;
 min-refresh-time <i>integer</i>;
 multi-master <i>boolean</i>;
 sig-validity-interval <i>integer</i>;
 sig-re-signing-interval <i>integer</i>;
 sig-signing-nodes <i>integer</i>;
 sig-signing-signatures <i>integer</i>;
 sig-signing-type <i>integer</i>;
 transfer-source ( <i>ipv4_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 transfer-source-v6 ( <i>ipv6_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 alt-transfer-source ( <i>ipv4_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 alt-transfer-source-v6 ( <i>ipv6_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 use-alt-transfer-source <i>boolean</i>;
 zone-statistics <i>boolean</i>;
 key-directory <i>quoted_string</i>;
 try-tcp-refresh <i>boolean</i>;
 zero-no-soa-ttl <i>boolean</i>;
 zero-no-soa-ttl-cache <i>boolean</i>;
 nsec3-test-zone <i>boolean</i>; // testing only
 allow-v6-synthesis { <i>address_match_element</i>; ... }; // obsolete
 deallocate-on-exit <i>boolean</i>; // obsolete
 fake-iquery <i>boolean</i>; // obsolete
 fetch-glue <i>boolean</i>; // obsolete
 has-old-clients <i>boolean</i>; // obsolete
 maintain-ixfr-base <i>boolean</i>; // obsolete
 max-ixfr-log-size <i>size</i>; // obsolete
 multiple-cnames <i>boolean</i>; // obsolete
 named-xfer <i>quoted_string</i>; // obsolete
 serial-queries <i>integer</i>; // obsolete
 treat-cr-as-space <i>boolean</i>; // obsolete
 use-id-pool <i>boolean</i>; // obsolete
};</pre>
</dl>
<h2>View</h2>
<dl>
<dd>
<pre>view <i>string</i> <i>optional_class</i> {
 match-clients { <i>address_match_element</i>; ... };
 match-destinations { <i>address_match_element</i>; ... };
 match-recursive-only <i>boolean</i>;
 key <i>string</i> {
 algorithm <i>string</i>;
 secret <i>string</i>;
 };
 zone <i>string</i> <i>optional_class</i> {
 ...
 };
 server ( <i>ipv4_address</i><i>[/prefixlen]</i> | <i>ipv6_address</i><i>[/prefixlen]</i> ) {
 ...
 };
 trusted-keys {
 <i>string</i> <i>integer</i> <i>integer</i> <i>integer</i> <i>quoted_string</i>; ...
 };
 allow-recursion { <i>address_match_element</i>; ... };
 allow-recursion-on { <i>address_match_element</i>; ... };
 sortlist { <i>address_match_element</i>; ... };
 topology { <i>address_match_element</i>; ... }; // not implemented
 auth-nxdomain <i>boolean</i>; // default changed
 minimal-responses <i>boolean</i>;
 recursion <i>boolean</i>;
 rrset-order {
 [ class <i>string</i> ] [ type <i>string</i> ]
 [ name <i>quoted_string</i> ] <i>string</i> <i>string</i>; ...
 };
 provide-ixfr <i>boolean</i>;
 request-ixfr <i>boolean</i>;
 rfc2308-type1 <i>boolean</i>; // not yet implemented
 additional-from-auth <i>boolean</i>;
 additional-from-cache <i>boolean</i>;
 query-source ( ( <i>ipv4_address</i> | * ) | [ address ( <i>ipv4_address</i> | * ) ] ) [ port ( <i>integer</i> | * ) ];
 query-source-v6 ( ( <i>ipv6_address</i> | * ) | [ address ( <i>ipv6_address</i> | * ) ] ) [ port ( <i>integer</i> | * ) ];
 use-queryport-pool <i>boolean</i>;
 queryport-pool-ports <i>integer</i>;
 queryport-pool-updateinterval <i>integer</i>;
 cleaning-interval <i>integer</i>;
 min-roots <i>integer</i>; // not implemented
 lame-ttl <i>integer</i>;
 max-ncache-ttl <i>integer</i>;
 max-cache-ttl <i>integer</i>;
 transfer-format ( many-answers | one-answer );
 max-cache-size <i>size</i>;
 max-acache-size <i>size</i>;
 clients-per-query <i>number</i>;
 max-clients-per-query <i>number</i>;
 check-names ( master | slave | response )
 ( fail | warn | ignore );
 check-mx ( fail | warn | ignore );
 check-integrity <i>boolean</i>;
 check-mx-cname ( fail | warn | ignore );
 check-srv-cname ( fail | warn | ignore );
 cache-file <i>quoted_string</i>; // test option
 suppress-initial-notify <i>boolean</i>; // not yet implemented
 preferred-glue <i>string</i>;
 dual-stack-servers [ port <i>integer</i> ] {
 ( <i>quoted_string</i> [port <i>integer</i>] |
 <i>ipv4_address</i> [port <i>integer</i>] |
 <i>ipv6_address</i> [port <i>integer</i>] ); ...
 };
 edns-udp-size <i>integer</i>;
 max-udp-size <i>integer</i>;
 root-delegation-only [ exclude { <i>quoted_string</i>; ... } ];
 disable-algorithms <i>string</i> { <i>string</i>; ... };
 dnssec-enable <i>boolean</i>;
 dnssec-validation <i>boolean</i>;
 dnssec-lookaside <i>string</i> trust-anchor <i>string</i>;
 dnssec-must-be-secure <i>string</i> <i>boolean</i>;
 dnssec-accept-expired <i>boolean</i>;
 empty-server <i>string</i>;
 empty-contact <i>string</i>;
 empty-zones-enable <i>boolean</i>;
 disable-empty-zone <i>string</i>;
 dialup <i>dialuptype</i>;
 ixfr-from-differences <i>ixfrdiff</i>;
 allow-query { <i>address_match_element</i>; ... };
 allow-query-on { <i>address_match_element</i>; ... };
 allow-query-cache { <i>address_match_element</i>; ... };
 allow-query-cache-on { <i>address_match_element</i>; ... };
 allow-transfer { <i>address_match_element</i>; ... };
 allow-update { <i>address_match_element</i>; ... };
 allow-update-forwarding { <i>address_match_element</i>; ... };
 update-check-ksk <i>boolean</i>;
 masterfile-format ( text | raw );
 notify <i>notifytype</i>;
 notify-source ( <i>ipv4_address</i> | * ) [ port ( <i>integer</i> | * ) ];
 notify-source-v6 ( <i>ipv6_address</i> | * ) [ port ( <i>integer</i> | * ) ];
 notify-delay <i>seconds</i>;
 notify-to-soa <i>boolean</i>;
 also-notify [ port <i>integer</i> ] { ( <i>ipv4_address</i> | <i>ipv6_address</i> )
 [ port <i>integer</i> ]; ... };
 allow-notify { <i>address_match_element</i>; ... };
 forward ( first | only );
 forwarders [ port <i>integer</i> ] {
 ( <i>ipv4_address</i> | <i>ipv6_address</i> ) [ port <i>integer</i> ]; ...
 };
 max-journal-size <i>size_no_default</i>;
 max-transfer-time-in <i>integer</i>;
 max-transfer-time-out <i>integer</i>;
 max-transfer-idle-in <i>integer</i>;
 max-transfer-idle-out <i>integer</i>;
 max-retry-time <i>integer</i>;
 min-retry-time <i>integer</i>;
 max-refresh-time <i>integer</i>;
 min-refresh-time <i>integer</i>;
 multi-master <i>boolean</i>;
 sig-validity-interval <i>integer</i>;
 transfer-source ( <i>ipv4_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 transfer-source-v6 ( <i>ipv6_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 alt-transfer-source ( <i>ipv4_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 alt-transfer-source-v6 ( <i>ipv6_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 use-alt-transfer-source <i>boolean</i>;
 zone-statistics <i>boolean</i>;
 try-tcp-refresh <i>boolean</i>;
 key-directory <i>quoted_string</i>;
 zero-no-soa-ttl <i>boolean</i>;
 zero-no-soa-ttl-cache <i>boolean</i>;
 allow-v6-synthesis { <i>address_match_element</i>; ... }; // obsolete
 fetch-glue <i>boolean</i>; // obsolete
 maintain-ixfr-base <i>boolean</i>; // obsolete
 max-ixfr-log-size <i>size</i>; // obsolete
};</pre>
</dl>
<h2>Zone</h2>
<dl>
<dd>
<pre>zone <i>string</i> <i>optional_class</i> {
 type ( master | slave | stub | hint |
 forward | delegation-only );
 file <i>quoted_string</i>;
 masters [ port <i>integer</i> ] {
 ( <i>masters</i> |
 <i>ipv4_address</i> [port <i>integer</i>] |
 <i>ipv6_address</i> [ port <i>integer</i> ] ) [ key <i>string</i> ]; ...
 };
 database <i>string</i>;
 delegation-only <i>boolean</i>;
 check-names ( fail | warn | ignore );
 check-mx ( fail | warn | ignore );
 check-integrity <i>boolean</i>;
 check-mx-cname ( fail | warn | ignore );
 check-srv-cname ( fail | warn | ignore );
 dialup <i>dialuptype</i>;
 ixfr-from-differences <i>boolean</i>;
 journal <i>quoted_string</i>;
 zero-no-soa-ttl <i>boolean</i>;
 allow-query { <i>address_match_element</i>; ... };
 allow-query-on { <i>address_match_element</i>; ... };
 allow-transfer { <i>address_match_element</i>; ... };
 allow-update { <i>address_match_element</i>; ... };
 allow-update-forwarding { <i>address_match_element</i>; ... };
 update-policy {
 ( grant | deny ) <i>string</i>
 ( name | subdomain | wildcard | self | selfsub | selfwild |
 krb5-self | ms-self | krb5-subdomain | ms-subdomain |
 tcp-self | 6to4-self ) <i>string</i>
 <i>rrtypelist</i>; ...
 };
 update-check-ksk <i>boolean</i>;
 masterfile-format ( text | raw );
 notify <i>notifytype</i>;
 notify-source ( <i>ipv4_address</i> | * ) [ port ( <i>integer</i> | * ) ];
 notify-source-v6 ( <i>ipv6_address</i> | * ) [ port ( <i>integer</i> | * ) ];
 notify-delay <i>seconds</i>;
 notify-to-soa <i>boolean</i>;
 also-notify [ port <i>integer</i> ] { ( <i>ipv4_address</i> | <i>ipv6_address</i> )
 [ port <i>integer</i> ]; ... };
 allow-notify { <i>address_match_element</i>; ... };
 forward ( first | only );
 forwarders [ port <i>integer</i> ] {
 ( <i>ipv4_address</i> | <i>ipv6_address</i> ) [ port <i>integer</i> ]; ...
 };
 max-journal-size <i>size_no_default</i>;
 max-transfer-time-in <i>integer</i>;
 max-transfer-time-out <i>integer</i>;
 max-transfer-idle-in <i>integer</i>;
 max-transfer-idle-out <i>integer</i>;
 max-retry-time <i>integer</i>;
 min-retry-time <i>integer</i>;
 max-refresh-time <i>integer</i>;
 min-refresh-time <i>integer</i>;
 multi-master <i>boolean</i>;
 sig-validity-interval <i>integer</i>;
 transfer-source ( <i>ipv4_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 transfer-source-v6 ( <i>ipv6_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 alt-transfer-source ( <i>ipv4_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 alt-transfer-source-v6 ( <i>ipv6_address</i> | * )
 [ port ( <i>integer</i> | * ) ];
 use-alt-transfer-source <i>boolean</i>;
 zone-statistics <i>boolean</i>;
 try-tcp-refresh <i>boolean</i>;
 key-directory <i>quoted_string</i>;
 nsec3-test-zone <i>boolean</i>; // testing only
 ixfr-base <i>quoted_string</i>; // obsolete
 ixfr-tmp-file <i>quoted_string</i>; // obsolete
 maintain-ixfr-base <i>boolean</i>; // obsolete
 max-ixfr-log-size <i>size</i>; // obsolete
 pubkey <i>integer</i> <i>integer</i> <i>integer</i> <i>quoted_string</i>; // obsolete
};</pre>
</dl>
<h2>Files</h2>
<p><i>/etc/named.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-named/">named</a></code>(8), <code><a href="/docs/linux/man/8-named-checkconf/">named-checkconf</a></code>(8), <code><a href="/docs/linux/man/8-rndc/">rndc</a></code>(8), BIND 9 Administrator Reference Manual.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2008 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
