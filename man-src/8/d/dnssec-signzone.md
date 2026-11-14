---
title: "dnssec-signzone(8)"
name: "dnssec-signzone"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnssec-signzone/"
description: "dnssec-signzone – DNSSEC zone signing tool"
---

<p>dnssec-signzone &#8211; DNSSEC zone signing tool</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>dnssec-signzone</code> [<code>-a</code>] [<code>-c&nbsp;<wbr></code><i>class</i>] [<code>-d&nbsp;<wbr></code><i>directory</i>] [<code>-D</code>] [<code>-E&nbsp;<wbr></code><i>engine</i>] [<code>-e&nbsp;<wbr></code><i>end-time</i>] [<code>-f&nbsp;<wbr></code><i>output-file</i>] [<code>-g</code>] [<code>-h</code>] [<code>-K&nbsp;<wbr></code><i>directory</i>] [<code>-k&nbsp;<wbr></code><i>key</i>] [<code>-L&nbsp;<wbr></code><i>serial</i>] [<code>-l&nbsp;<wbr></code><i>domain</i>] [<code>-i&nbsp;<wbr></code><i>interval</i>] [<code>-I&nbsp;<wbr></code><i>input-format</i>] [<code>-j&nbsp;<wbr></code><i>jitter</i>] [<code>-N&nbsp;<wbr></code><i>soa-serial-format</i>] [<code>-o&nbsp;<wbr></code><i>origin</i>] [<code>-O&nbsp;<wbr></code><i>output-format</i>] [<code>-P</code>] [<code>-p</code>] [<code>-R</code>] [<code>-r&nbsp;<wbr></code><i>randomdev</i>] [<code>-S</code>] [<code>-s&nbsp;<wbr></code><i>start-time</i>] [<code>-T&nbsp;<wbr></code><i>ttl</i>] [<code>-t</code>] [<code>-u</code>] [<code>-v&nbsp;<wbr></code><i>level</i>] [<code>-X&nbsp;<wbr></code><i>extended end-time</i>] [<code>-x</code>] [<code>-z</code>] [<code>-3&nbsp;<wbr></code><i>salt</i>] [<code>-H&nbsp;<wbr></code><i>iterations</i>] [<code>-A</code>] {zonefile} [key&#8230;]</dl>
<h2>Description</h2>
<p><code>dnssec-signzone</code></p>
<dd>signs a zone. It generates NSEC and RRSIG records and produces a signed version of the zone. The security status of delegations from the signed zone (that is, whether the child zones are secure or not) is determined by the presence or absence of a <i>keyset</i> file for each child zone.</p>
<h2>Options</h2>
<p>-a</p>
<dl>
<dd>Verify all generated signatures.</dl>
<p> -c <i>class</i></p>
<dl>
<dd>Specifies the DNS class of the zone.</dl>
<p> -C</p>
<dl>
<dd>Compatibility mode: Generate a <i>keyset-</i><i>zonename</i> file in addition to <i>dsset-</i><i>zonename</i> when signing a zone, for use by older versions of <code>dnssec-signzone</code>.</dl>
<p> -d <i>directory</i></p>
<dl>
<dd>Look for <i>dsset-</i> or <i>keyset-</i> files in <code>directory</code>.</dl>
<p> -D</p>
<dl>
<dd>Output only those record types automatically managed by <code>dnssec-signzone</code>, i.e. RRSIG, NSEC, NSEC3 and NSEC3PARAM records. If smart signing (<code>-S</code>) is used, DNSKEY records are also included. The resulting file can be included in the original zone file with <code>$INCLUDE</code>. This option cannot be combined with <code>-O raw</code> or serial number updating.</dl>
<p> -E <i>engine</i></p>
<dl>
<dd>Uses a crypto hardware (OpenSSL engine) for the crypto operations it supports, for instance signing with private keys from a secure key store. When compiled with PKCS#11 support it defaults to pkcs11; the empty name resets it to no engine.</dl>
<p> -g</p>
<dl>
<dd>Generate DS records for child zones from <i>dsset-</i> or <i>keyset-</i> file. Existing DS records will be removed.</dl>
<p> -K <i>directory</i></p>
<dl>
<dd>Key repository: Specify a directory to search for DNSSEC keys. If not specified, defaults to the current directory.</dl>
<p> -k <i>key</i></p>
<dl>
<dd>Treat specified key as a key signing key ignoring any key flags. This option may be specified multiple times.</dl>
<p> -l <i>domain</i></p>
<dl>
<dd>Generate a DLV set in addition to the key (DNSKEY) and DS sets. The domain is appended to the name of the records.</dl>
<p> -s <i>start-time</i></p>
<dl>
<dd>Specify the date and time when the generated RRSIG records become valid. This can be either an absolute or relative time. An absolute start time is indicated by a number in YYYYMMDDHHMMSS notation; 20000530144500 denotes 14:45:00 UTC on May 30th, 2000. A relative start time is indicated by +N, which is N seconds from the current time. If no <code>start-time</code> is specified, the current time minus 1 hour (to allow for clock skew) is used.</dl>
<p> -e <i>end-time</i></p>
<dl>
<dd>Specify the date and time when the generated RRSIG records expire. As with <code>start-time</code>, an absolute time is indicated in YYYYMMDDHHMMSS notation. A time relative to the start time is indicated with +N, which is N seconds from the start time. A time relative to the current time is indicated with now+N. If no <code>end-time</code> is specified, 30 days from the start time is used as a default. <code>end-time</code> must be later than <code>start-time</code>.</dl>
<p> -X <i>extended end-time</i></p>
<dl>
<dd>Specify the date and time when the generated RRSIG records for the DNSKEY RRset will expire. This is to be used in cases when the DNSKEY signatures need to persist longer than signatures on other records; e.g., when the private component of the KSK is kept offline and the KSK signature is to be refreshed manually. </p>
<p> As with <code>start-time</code>, an absolute time is indicated in YYYYMMDDHHMMSS notation. A time relative to the start time is indicated with +N, which is N seconds from the start time. A time relative to the current time is indicated with now+N. If no <code>extended end-time</code> is specified, the value of <code>end-time</code> is used as the default. (<code>end-time</code>, in turn, defaults to 30 days from the start time.) <code>extended end-time</code> must be later than <code>start-time</code>.</dl>
<p> -f <i>output-file</i></p>
<dl>
<dd>The name of the output file containing the signed zone. The default is to append <i>.signed</i> to the input filename. If <code>output-file</code> is set to &quot;-&quot;, then the signed zone is written to the standard output, with a default output format of &quot;full&quot;.</dl>
<p> -h</p>
<dl>
<dd>Prints a short summary of the options and arguments to <code>dnssec-signzone</code>.</dl>
<p> -i <i>interval</i></p>
<dl>
<dd>When a previously-signed zone is passed as input, records may be resigned. The <code>interval</code> option specifies the cycle interval as an offset from the current time (in seconds). If a RRSIG record expires after the cycle interval, it is retained. Otherwise, it is considered to be expiring soon, and it will be replaced. </p>
<p> The default cycle interval is one quarter of the difference between the signature end and start times. So if neither <code>end-time</code> or <code>start-time</code> are specified, <code>dnssec-signzone</code> generates signatures that are valid for 30 days, with a cycle interval of 7.5 days. Therefore, if any existing RRSIG records are due to expire in less than 7.5 days, they would be replaced.</dl>
<p> -I <i>input-format</i></p>
<dl>
<dd>The format of the input zone file. Possible formats are <code>&quot;text&quot;</code> (default) and <code>&quot;raw&quot;</code>. This option is primarily intended to be used for dynamic signed zones so that the dumped zone file in a non-text format containing updates can be signed directly. The use of this option does not make much sense for non-dynamic zones.</dl>
<p> -j <i>jitter</i></p>
<dl>
<dd>When signing a zone with a fixed signature lifetime, all RRSIG records issued at the time of signing expires simultaneously. If the zone is incrementally signed, i.e. a previously-signed zone is passed as input to the signer, all expired signatures have to be regenerated at about the same time. The <code>jitter</code> option specifies a jitter window that will be used to randomize the signature expire time, thus spreading incremental signature regeneration over time. </p>
<p> Signature lifetime jitter also to some extent benefits validators and servers by spreading out cache expiration, i.e. if large numbers of RRSIGs don&#8217;t expire at the same time from all caches there will be less congestion than if all validators need to refetch at mostly the same time.</dl>
<p> -L <i>serial</i></p>
<dl>
<dd>When writing a signed zone to &#8216;raw&#8217; format, set the &quot;source serial&quot; value in the header to the specified serial number. (This is expected to be used primarily for testing purposes.)</dl>
<p> -n <i>ncpus</i></p>
<dl>
<dd>Specifies the number of threads to use. By default, one thread is started for each detected CPU.</dl>
<p> -N <i>soa-serial-format</i></p>
<dl>
<dd>The SOA serial number format of the signed zone. Possible formats are <code>&quot;keep&quot;</code> (default), <code>&quot;increment&quot;</code> and <code>&quot;unixtime&quot;</code>.</p>
<dl>
<dd><code>&quot;keep&quot;</code></p>
<dl>
<dd>Do not modify the SOA serial number.</dl>
<p> <code>&quot;increment&quot;</code></p>
<dl>
<dd>Increment the SOA serial number using RFC 1982 arithmetics.</dl>
<p> <code>&quot;unixtime&quot;</code></p>
<dl>
<dd>Set the SOA serial number to the number of seconds since epoch.</dl>
</dl>
</dl>
<p> -o <i>origin</i></p>
<dl>
<dd>The zone origin. If not specified, the name of the zone file is assumed to be the origin.</dl>
<p> -O <i>output-format</i></p>
<dl>
<dd>The format of the output file containing the signed zone. Possible formats are <code>&quot;text&quot;</code> (default) <code>&quot;full&quot;</code>, which is text output in a format suitable for processing by external scripts, and <code>&quot;raw&quot;</code> or <code>&quot;raw=N&quot;</code>, which store the zone in a binary format for rapid loading by <code>named</code>. <code>&quot;raw=N&quot;</code> specifies the format version of the raw zone file: if N is 0, the raw file can be read by any version of <code>named</code>; if N is 1, the file can be read by release 9.9.0 or higher. The default is 1.</dl>
<p> -p</p>
<dl>
<dd>Use pseudo-random data when signing the zone. This is faster, but less secure, than using real random data. This option may be useful when signing large zones or when the entropy source is limited.</dl>
<p> -P</p>
<dl>
<dd>Disable post sign verification tests. </p>
<p> The post sign verification test ensures that for each algorithm in use there is at least one non revoked self signed KSK key, that all revoked KSK keys are self signed, and that all records in the zone are signed by the algorithm. This option skips these tests.</dl>
<p> -R</p>
<dl>
<dd>Remove signatures from keys that no longer exist. </p>
<p> Normally, when a previously-signed zone is passed as input to the signer, and a DNSKEY record has been removed and replaced with a new one, signatures from the old key that are still within their validity period are retained. This allows the zone to continue to validate with cached copies of the old DNSKEY RRset. The <code>-R</code> forces <code>dnssec-signzone</code> to remove all orphaned signatures.</dl>
<p> -r <i>randomdev</i></p>
<dl>
<dd>Specifies the source of randomness. If the operating system does not provide a <i>/dev/random</i> or equivalent device, the default source of randomness is keyboard input. <i>randomdev</i> specifies the name of a character device or file containing random data to be used instead of the default. The special value <i>keyboard</i> indicates that keyboard input should be used.</dl>
<p> -S</p>
<dl>
<dd>Smart signing: Instructs <code>dnssec-signzone</code> to search the key repository for keys that match the zone being signed, and to include them in the zone if appropriate. </p>
<p> When a key is found, its timing metadata is examined to determine how it should be used, according to the following rules. Each successive rule takes priority over the prior ones:</p>
<dl>
<dd>
<dl>
<dd>If no timing metadata has been set for the key, the key is published in the zone and used to sign the zone.</dl>
<dl>
<dd>If the key&#8217;s publication date is set and is in the past, the key is published in the zone.</dl>
<dl>
<dd>If the key&#8217;s activation date is set and in the past, the key is published (regardless of publication date) and used to sign the zone.</dl>
<dl>
<dd>If the key&#8217;s revocation date is set and in the past, and the key is published, then the key is revoked, and the revoked key is used to sign the zone.</dl>
<dl>
<dd>If either of the key&#8217;s unpublication or deletion dates are set and in the past, the key is NOT published or used to sign the zone, regardless of any other metadata.</dl>
</dl>
</dl>
<p> -T <i>ttl</i></p>
<dl>
<dd>Specifies a TTL to be used for new DNSKEY records imported into the zone from the key repository. If not specified, the default is the TTL value from the zone&#8217;s SOA record. This option is ignored when signing without <code>-S</code>, since DNSKEY records are not imported from the key repository in that case. It is also ignored if there are any pre-existing DNSKEY records at the zone apex, in which case new records&#8217; TTL values will be set to match them, or if any of the imported DNSKEY records had a default TTL value. In the event of a a conflict between TTL values in imported keys, the shortest one is used.</dl>
<p> -t</p>
<dl>
<dd>Print statistics at completion.</dl>
<p> -u</p>
<dl>
<dd>Update NSEC/NSEC3 chain when re-signing a previously signed zone. With this option, a zone signed with NSEC can be switched to NSEC3, or a zone signed with NSEC3 can be switch to NSEC or to NSEC3 with different parameters. Without this option, <code>dnssec-signzone</code> will retain the existing chain when re-signing.</dl>
<p> -v <i>level</i></p>
<dl>
<dd>Sets the debugging level.</dl>
<p> -x</p>
<dl>
<dd>Only sign the DNSKEY RRset with key-signing keys, and omit signatures from zone-signing keys. (This is similar to the <code>dnssec-dnskey-kskonly yes;</code> zone option in <code>named</code>.)</dl>
<p> -z</p>
<dl>
<dd>Ignore KSK flag on key when determining what to sign. This causes KSK-flagged keys to sign all records, not just the DNSKEY RRset. (This is similar to the <code>update-check-ksk no;</code> zone option in <code>named</code>.)</dl>
<p> -3 <i>salt</i></p>
<dl>
<dd>Generate an NSEC3 chain with the given hex encoded salt. A dash (<i>salt</i>) can be used to indicate that no salt is to be used when generating the NSEC3 chain.</dl>
<p> -H <i>iterations</i></p>
<dl>
<dd>When generating an NSEC3 chain, use this many interations. The default is 10.</dl>
<p> -A</p>
<dl>
<dd>When generating an NSEC3 chain set the OPTOUT flag on all NSEC3 records and do not generate NSEC3 records for insecure delegations. </p>
<p> Using this option twice (i.e., <code>-AA</code>) turns the OPTOUT flag off for all records. This is useful when using the <code>-u</code> option to modify an NSEC3 chain which previously had OPTOUT set.</dl>
<p> zonefile</p>
<dl>
<dd>The file containing the zone to be signed.</dl>
<p> key</p>
<dl>
<dd>Specify which keys should be used to sign the zone. If no keys are specified, then the zone will be examined for DNSKEY records at the zone apex. If these are found and there are matching private keys, in the current directory, then these will be used for signing.</dl>
<h2>Example</h2>
<p>The following command signs the <code>example.com</code> zone with the DSA key generated by <code>dnssec-keygen</code> (Kexample.com.+003+17247). Because the <code>-S</code> option is not being used, the zone&#8217;s keys must be in the master file (<i>db.example.com</i>). This invocation looks for <i>dsset</i> files, in the current directory, so that DS records can be imported from them (<code>-g</code>). </p>
<dl>
<dd>
<pre>% dnssec-signzone -g -o example.com db.example.com \
Kexample.com.+003+17247
db.example.com.signed
%</pre>
</dl>
<p> In the above example, <code>dnssec-signzone</code> creates the file <i>db.example.com.signed</i>. This file should be referenced in a zone statement in a <i>named.conf</i> file. </p>
<p> This example re-signs a previously signed zone with default parameters. The private keys are assumed to be in the current directory. </p>
<dl>
<dd>
<pre>% cp db.example.com.signed db.example.com
% dnssec-signzone -o example.com db.example.com
db.example.com.signed
%</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dnssec-keygen/">dnssec-keygen</a></code>(8), BIND 9 Administrator Reference Manual, RFC 4033.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2009, 2011 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000-2003 Internet Software Consortium.</p>
