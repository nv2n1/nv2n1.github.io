---
title: "systemd-positive(5)"
name: "systemd-positive"
section: "5"
letter: "s"
url: "/docs/linux/man/5-systemd-positive/"
description: "dnssec-trust-anchors.d, systemd.positive, systemd.negative – DNSSEC trust anchor configuration files"
---

<p>dnssec-trust-anchors.d, systemd.positive, systemd.negative &#8211; DNSSEC trust anchor configuration files</p>
<h2>Synopsis</h2>
<p>/etc/dnssec-trust-anchors.d/*.positive </p>
<p> /run/dnssec-trust-anchors.d/*.positive </p>
<p> /usr/lib/dnssec-trust-anchors.d/*.positive </p>
<p> /etc/dnssec-trust-anchors.d/*.negative </p>
<p> /run/dnssec-trust-anchors.d/*.negative </p>
<p> /usr/lib/dnssec-trust-anchors.d/*.negative</p>
<h2>Description</h2>
<p>The DNSSEC trust anchor configuration files define positive and negative trust anchors <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8) bases DNSSEC integrity proofs on.</p>
<h2>Positive Trust Anchors</h2>
<p>Positive trust anchor configuration files contain <code>DNSKEY</code> and <code>DS</code> resource record definitions to use as base for DNSSEC integrity proofs. See m[blue]<code>RFC 4035, Section 4.4</code>m[]<font SIZE="-2">[1]</font> for more information about DNSSEC trust anchors. </p>
<p> Positive trust anchors are read from files with the suffix .positive located in /etc/dnssec-trust-anchors.d/, /run/dnssec-trust-anchors.d/ and /usr/lib/dnssec-trust-anchors.d/. These directories are searched in the specified order, and a trust anchor file of the same name in an earlier path overrides a trust anchor files in a later path. To disable a trust anchor file shipped in /usr/lib/dnssec-trust-anchors.d/ it is sufficient to provide an identically-named file in /etc/dnssec-trust-anchors.d/ or /run/dnssec-trust-anchors.d/ that is either empty or a symlink to /dev/null (&quot;masked&quot;). </p>
<p> Positive trust anchor files are simple text files resembling DNS zone files, as documented in m[blue]<code>RFC 1035, Section 5</code>m[]<font SIZE="-2">[2]</font>. One <code>DS</code> or <code>DNSKEY</code> resource record may be listed per line. Empty lines and lines starting with &quot;#&quot; or &quot;;&quot; are ignored, which may be used for commenting. A &lt;consant&gt;DS&lt;/consant&gt; resource record is specified like in the following example: </p>
<dl>
<dd>
<pre>. IN DS 19036 8 2 49aac11d7b6f6446702e54a1607371607a1a41855200fd2ce1cdde32f24e8fb5</pre>
</dl>
<p> The first word specifies the domain, use &quot;.&quot; for the root domain. The domain may be specified with or without trailing dot, which is considered equivalent. The second word must be &quot;IN&quot; the third word &quot;DS&quot;. The following words specify the key tag, signature algorithm, digest algorithm, followed by the hex-encoded key fingerprint. See m[blue]<code>RFC 4034, Section 5</code>m[]<font SIZE="-2">[3]</font> for details about the precise syntax and meaning of these fields. </p>
<p> Alternatively, <code>DNSKEY</code> resource records may be used to define trust anchors, like in the following example: </p>
<dl>
<dd>
<pre>. IN DNSKEY 257 3 8 AwEAAagAIKlVZrpC6Ia7gEzahOR+9W29euxhJhVVLOyQbSEW0O8gcCjFFVQUTf6v58fLjwBd0YI0EzrAcQqBGCzh/RStIoO8g0NfnfL2MTJRkxoXbfDaUeVPQuYEhg37NZWAJQ9VnMVDxP/VHL496M/QZxkjf5/Efucp2gaDX6RS6CXpoY68LsvPVjR0ZSwzz1apAzvN9dlzEheX7ICJBBtuA6G3LQpzW5hOA2hzCTMjJPJ8LbqF6dsV6DoBQzgul0sGIcGOYl7OyQdXfZ57relSQageu+ipAdTTJ25AsRTAoub8ONGcLmqrAmRLKBP1dfwhYB4N7knNnulqQxA+Uk1ihz0=</pre>
</dl>
<p> The first word specifies the domain again, the second word must be &quot;IN&quot;, followed by &quot;DNSKEY&quot;. The subsequent words encode the <code>DNSKEY</code> flags, protocol and algorithm fields, followed by the key data encoded in Base64. See m[blue]<code>RFC 4034, Section 2</code>m[]<font SIZE="-2">[4]</font> for details about the precise syntax and meaning of these fields. </p>
<p> If multiple <code>DS</code> or <code>DNSKEY</code> records are defined for the same domain (possibly even in different trust anchor files), all keys are used and are considered equivalent as base for DNSSEC proofs. </p>
<p> Note that systemd-resolved will automatically use a built-in trust anchor key for the Internet root domain if no positive trust anchors are defined for the root domain. In most cases it is hence unnecessary to define an explicit key with trust anchor files. The built-in key is disabled as soon as at least one trust anchor key for the root domain is defined in trust anchor files. </p>
<p> It is generally recommended to encode trust anchors in <code>DS</code> resource records, rather than <code>DNSKEY</code> resource records. </p>
<p> If a trust anchor specified via a <code>DS</code> record is found revoked it is automatically removed from the trust anchor database for the runtime. See m[blue]<code>RFC 5011</code>m[]<font SIZE="-2">[5]</font> for details about revoked trust anchors. Note that systemd-resolved will not update its trust anchor database from DNS servers automatically. Instead, it is recommended to update the resolver software or update the new trust anchor via adding in new trust anchor files. </p>
<p> The current DNSSEC trust anchor for the Internet&#8217;s root domain is available at the m[blue]<code>IANA Trust Anchor and Keys</code>m[]<font SIZE="-2">[6]</font> page.</p>
<h2>Negative Trust Anchors</h2>
<p>Negative trust anchors define domains where DNSSEC validation shall be turned off. Negative trust anchor files are found at the same location as positive trust anchor files, and follow the same overriding rules. They are text files with the .negative suffix. Empty lines and lines whose first character is &quot;;&quot; are ignored. Each line specifies one domain name which is the root of a DNS subtree where validation shall be disabled. For example: </p>
<dl>
<dd>
<pre># Reverse IPv4 mappings
10.in-addr.arpa
16.172.in-addr.arpa
168.192.in-addr.arpa
...
# Some custom domains
prod
stag</pre>
</dl>
<p> Negative trust anchors are useful to support private DNS subtrees that are not referenced from the Internet DNS hierarchy, and not signed. </p>
<p> m[blue]<code>RFC 7646</code>m[]<font SIZE="-2">[7]</font> for details on negative trust anchors. </p>
<p> If no negative trust anchor files are configured a built-in set of well-known private DNS zone domains is used as negative trust anchors. </p>
<p> It is also possibly to define per-interface negative trust anchors using the <i>DNSSECNegativeTrustAnchors=</i> setting in <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5) files.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-systemd-resolved-service/">systemd-resolved.service</a></code>(8), <code><a href="/docs/linux/man/5-resolved-conf/">resolved.conf</a></code>(5), <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>RFC 4035, Section 4.4</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc4035#section-4.4">https://tools.ietf.org/html/rfc4035#section-4.4</a></dl>
<dt> 2.</p>
<dd>RFC 1035, Section 5</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc1035#section-5">https://tools.ietf.org/html/rfc1035#section-5</a></dl>
<dt> 3.</p>
<dd>RFC 4034, Section 5</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc4034#section-5">https://tools.ietf.org/html/rfc4034#section-5</a></dl>
<dt> 4.</p>
<dd>RFC 4034, Section 2</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc4034#section-2">https://tools.ietf.org/html/rfc4034#section-2</a></dl>
<dt> 5.</p>
<dd>RFC 5011</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc5011">https://tools.ietf.org/html/rfc5011</a></dl>
<dt> 6.</p>
<dd>IANA Trust Anchor and Keys</p>
<dl>
<dd><a rel="nofollow" href="https://data.iana.org/root-anchors/root-anchors.xml">https://data.iana.org/root-anchors/root-anchors.xml</a></dl>
<dt> 7.</p>
<dd>RFC 7646</p>
<dl>
<dd><a rel="nofollow" href="https://tools.ietf.org/html/rfc7646">https://tools.ietf.org/html/rfc7646</a></dl>
