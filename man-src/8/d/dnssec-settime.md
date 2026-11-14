---
title: "dnssec-settime(8)"
name: "dnssec-settime"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnssec-settime/"
description: "dnssec-settime – Set the key timing metadata for a DNSSEC key"
---

<p>dnssec-settime &#8211; Set the key timing metadata for a DNSSEC key</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>dnssec-settime</code> [<code>-f</code>] [<code>-K&nbsp;<wbr></code><i>directory</i>] [<code>-L&nbsp;<wbr></code><i>ttl</i>] [<code>-P&nbsp;<wbr></code><i>date/offset</i>] [<code>-A&nbsp;<wbr></code><i>date/offset</i>] [<code>-R&nbsp;<wbr></code><i>date/offset</i>] [<code>-I&nbsp;<wbr></code><i>date/offset</i>] [<code>-D&nbsp;<wbr></code><i>date/offset</i>] [<code>-h</code>] [<code>-v&nbsp;<wbr></code><i>level</i>] [<code>-E&nbsp;<wbr></code><i>engine</i>] {keyfile}</dl>
<h2>Description</h2>
<p><code>dnssec-settime</code></p>
<dd>reads a DNSSEC private key file and sets the key timing metadata as specified by the <code>-P</code>, <code>-A</code>, <code>-R</code>, <code>-I</code>, and <code>-D</code> options. The metadata can then be used by <code>dnssec-signzone</code> or other signing software to determine when a key is to be published, whether it should be used for signing a zone, etc. </p>
<p> If none of these options is set on the command line, then <code>dnssec-settime</code> simply prints the key timing metadata already stored in the key. </p>
<p> When key metadata fields are changed, both files of a key pair (<i>Knnnn.+aaa+iiiii.key</i> and <i>Knnnn.+aaa+iiiii.private</i>) are regenerated. Metadata fields are stored in the private file. A human-readable description of the metadata is also placed in comments in the key file. The private file&#8217;s permissions are always set to be inaccessible to anyone other than the owner (mode 0600).</p>
<h2>Options</h2>
<p>-f</p>
<dl>
<dd>Force an update of an old-format key with no metadata fields. Without this option, <code>dnssec-settime</code> will fail when attempting to update a legacy key. With this option, the key will be recreated in the new format, but with the original key data retained. The key&#8217;s creation date will be set to the present time. If no other values are specified, then the key&#8217;s publication and activation dates will also be set to the present time.</dl>
<p> -K <i>directory</i></p>
<dl>
<dd>Sets the directory in which the key files are to reside.</dl>
<p> -L <i>ttl</i></p>
<dl>
<dd>Sets the default TTL to use for this key when it is converted into a DNSKEY RR. If the key is imported into a zone, this is the TTL that will be used for it, unless there was already a DNSKEY RRset in place, in which case the existing TTL would take precedence. Setting the default TTL to 0 or none removes it.</dl>
<p> -h</p>
<dl>
<dd>Emit usage message and exit.</dl>
<p> -v <i>level</i></p>
<dl>
<dd>Sets the debugging level.</dl>
<p> -E <i>engine</i></p>
<dl>
<dd>Use the given OpenSSL engine. When compiled with PKCS#11 support it defaults to pkcs11; the empty name resets it to no engine.</dl>
<h2>Timing Options</h2>
<p>Dates can be expressed in the format YYYYMMDD or YYYYMMDDHHMMSS. If the argument begins with a &#8216;+&#8217; or &#8216;-&#8216;, it is interpreted as an offset from the present time. For convenience, if such an offset is followed by one of the suffixes &#8216;y&#8217;, &#8216;mo&#8217;, &#8216;w&#8217;, &#8216;d&#8217;, &#8216;h&#8217;, or &#8216;mi&#8217;, then the offset is computed in years (defined as 365 24-hour days, ignoring leap years), months (defined as 30 24-hour days), weeks, days, hours, or minutes, respectively. Without a suffix, the offset is computed in seconds. To unset a date, use &#8216;none&#8217;. </p>
<p> -P <i>date/offset</i></p>
<dl>
<dd>Sets the date on which a key is to be published to the zone. After that date, the key will be included in the zone but will not be used to sign it.</dl>
<p> -A <i>date/offset</i></p>
<dl>
<dd>Sets the date on which the key is to be activated. After that date, the key will be included in the zone and used to sign it.</dl>
<p> -R <i>date/offset</i></p>
<dl>
<dd>Sets the date on which the key is to be revoked. After that date, the key will be flagged as revoked. It will be included in the zone and will be used to sign it.</dl>
<p> -I <i>date/offset</i></p>
<dl>
<dd>Sets the date on which the key is to be retired. After that date, the key will still be included in the zone, but it will not be used to sign it.</dl>
<p> -D <i>date/offset</i></p>
<dl>
<dd>Sets the date on which the key is to be deleted. After that date, the key will no longer be included in the zone. (It may remain in the key repository, however.)</dl>
<p> -S <i>predecessor key</i></p>
<dl>
<dd>Select a key for which the key being modified will be an explicit successor. The name, algorithm, size, and type of the predecessor key must exactly match those of the key being modified. The activation date of the successor key will be set to the inactivation date of the predecessor. The publication date will be set to the activation date minus the prepublication interval, which defaults to 30 days.</dl>
<p> -i <i>interval</i></p>
<dl>
<dd>Sets the prepublication interval for a key. If set, then the publication and activation dates must be separated by at least this much time. If the activation date is specified but the publication date isn&#8217;t, then the publication date will default to this much time before the activation date; conversely, if the publication date is specified but activation date isn&#8217;t, then activation will be set to this much time after publication. </p>
<p> If the key is being set to be an explicit successor to another key, then the default prepublication interval is 30 days; otherwise it is zero. </p>
<p> As with date offsets, if the argument is followed by one of the suffixes &#8216;y&#8217;, &#8216;mo&#8217;, &#8216;w&#8217;, &#8216;d&#8217;, &#8216;h&#8217;, or &#8216;mi&#8217;, then the interval is measured in years, months, weeks, days, hours, or minutes, respectively. Without a suffix, the interval is measured in seconds.</dl>
<h2>Printing Options</h2>
<p><code>dnssec-settime</code> can also be used to print the timing metadata associated with a key. </p>
<p> -u</p>
<dl>
<dd>Print times in UNIX epoch format.</dl>
<p> -p <i>C/P/A/R/I/D/all</i></p>
<dl>
<dd>Print a specific metadata value or set of metadata values. The <code>-p</code> option may be followed by one or more of the following letters to indicate which value or values to print: <code>C</code> for the creation date, <code>P</code> for the publication date, <code>A</code> for the activation date, <code>R</code> for the revocation date, <code>I</code> for the inactivation date, or <code>D</code> for the deletion date. To print all of the metadata, use <code>-p all</code>.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dnssec-keygen/">dnssec-keygen</a></code>(8), <code><a href="/docs/linux/man/8-dnssec-signzone/">dnssec-signzone</a></code>(8), BIND 9 Administrator Reference Manual, RFC 5011.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2011 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
