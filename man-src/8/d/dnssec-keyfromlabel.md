---
title: "dnssec-keyfromlabel(8)"
name: "dnssec-keyfromlabel"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnssec-keyfromlabel/"
description: "dnssec-keyfromlabel – DNSSEC key generation tool"
---

<p>dnssec-keyfromlabel &#8211; DNSSEC key generation tool</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>dnssec-keyfromlabel</code> {-l&nbsp;<wbr><i>label</i>} [<code>-3</code>] [<code>-a&nbsp;<wbr></code><i>algorithm</i>] [<code>-A&nbsp;<wbr></code><i>date/offset</i>] [<code>-c&nbsp;<wbr></code><i>class</i>] [<code>-D&nbsp;<wbr></code><i>date/offset</i>] [<code>-E&nbsp;<wbr></code><i>engine</i>] [<code>-f&nbsp;<wbr></code><i>flag</i>] [<code>-G</code>] [<code>-I&nbsp;<wbr></code><i>date/offset</i>] [<code>-k</code>] [<code>-K&nbsp;<wbr></code><i>directory</i>] [<code>-L&nbsp;<wbr></code><i>ttl</i>] [<code>-n&nbsp;<wbr></code><i>nametype</i>] [<code>-P&nbsp;<wbr></code><i>date/offset</i>] [<code>-p&nbsp;<wbr></code><i>protocol</i>] [<code>-R&nbsp;<wbr></code><i>date/offset</i>] [<code>-t&nbsp;<wbr></code><i>type</i>] [<code>-v&nbsp;<wbr></code><i>level</i>] [<code>-y</code>] {name}</dl>
<h2>Description</h2>
<p><code>dnssec-keyfromlabel</code></p>
<dd>gets keys with the given label from a crypto hardware and builds key files for DNSSEC (Secure DNS), as defined in RFC 2535 and RFC 4034. </p>
<p> The <code>name</code> of the key is specified on the command line. This must match the name of the zone for which the key is being generated.</p>
<h2>Options</h2>
<p>-a <i>algorithm</i></p>
<dl>
<dd>Selects the cryptographic algorithm. The value of <code>algorithm</code> must be one of RSAMD5, RSASHA1, DSA, NSEC3RSASHA1, NSEC3DSA, RSASHA256, RSASHA512, ECCGOST, ECDSAP256SHA256 or ECDSAP384SHA384. These values are case insensitive. </p>
<p> If no algorithm is specified, then RSASHA1 will be used by default, unless the <code>-3</code> option is specified, in which case NSEC3RSASHA1 will be used instead. (If <code>-3</code> is used and an algorithm is specified, that algorithm will be checked for compatibility with NSEC3.) </p>
<p> Note 1: that for DNSSEC, RSASHA1 is a mandatory to implement algorithm, and DSA is recommended. </p>
<p> Note 2: DH automatically sets the -k flag.</dl>
<p> -3</p>
<dl>
<dd>Use an NSEC3-capable algorithm to generate a DNSSEC key. If this option is used and no algorithm is explicitly set on the command line, NSEC3RSASHA1 will be used by default.</dl>
<p> -E <i>engine</i></p>
<dl>
<dd>Specifies the name of the crypto hardware (OpenSSL engine). When compiled with PKCS#11 support it defaults to &quot;pkcs11&quot;.</dl>
<p> -l <i>label</i></p>
<dl>
<dd>Specifies the label of the key pair in the crypto hardware. The label may be preceded by an optional OpenSSL engine name, separated by a colon, as in &quot;pkcs11:keylabel&quot;.</dl>
<p> -n <i>nametype</i></p>
<dl>
<dd>Specifies the owner type of the key. The value of <code>nametype</code> must either be ZONE (for a DNSSEC zone key (KEY/DNSKEY)), HOST or ENTITY (for a key associated with a host (KEY)), USER (for a key associated with a user(KEY)) or OTHER (DNSKEY). These values are case insensitive.</dl>
<p> -C</p>
<dl>
<dd>Compatibility mode: generates an old-style key, without any metadata. By default, <code>dnssec-keyfromlabel</code> will include the key&#8217;s creation date in the metadata stored with the private key, and other dates may be set there as well (publication date, activation date, etc). Keys that include this data may be incompatible with older versions of BIND; the <code>-C</code> option suppresses them.</dl>
<p> -c <i>class</i></p>
<dl>
<dd>Indicates that the DNS record containing the key should have the specified class. If not specified, class IN is used.</dl>
<p> -f <i>flag</i></p>
<dl>
<dd>Set the specified flag in the flag field of the KEY/DNSKEY record. The only recognized flags are KSK (Key Signing Key) and REVOKE.</dl>
<p> -G</p>
<dl>
<dd>Generate a key, but do not publish it or sign with it. This option is incompatible with -P and -A.</dl>
<p> -h</p>
<dl>
<dd>Prints a short summary of the options and arguments to <code>dnssec-keyfromlabel</code>.</dl>
<p> -K <i>directory</i></p>
<dl>
<dd>Sets the directory in which the key files are to be written.</dl>
<p> -k</p>
<dl>
<dd>Generate KEY records rather than DNSKEY records.</dl>
<p> -L <i>ttl</i></p>
<dl>
<dd>Sets the default TTL to use for this key when it is converted into a DNSKEY RR. If the key is imported into a zone, this is the TTL that will be used for it, unless there was already a DNSKEY RRset in place, in which case the existing TTL would take precedence. Setting the default TTL to 0 or none removes it.</dl>
<p> -p <i>protocol</i></p>
<dl>
<dd>Sets the protocol value for the key. The protocol is a number between 0 and 255. The default is 3 (DNSSEC). Other possible values for this argument are listed in RFC 2535 and its successors.</dl>
<p> -t <i>type</i></p>
<dl>
<dd>Indicates the use of the key. <code>type</code> must be one of AUTHCONF, NOAUTHCONF, NOAUTH, or NOCONF. The default is AUTHCONF. AUTH refers to the ability to authenticate data, and CONF the ability to encrypt data.</dl>
<p> -v <i>level</i></p>
<dl>
<dd>Sets the debugging level.</dl>
<p> -y</p>
<dl>
<dd>Allows DNSSEC key files to be generated even if the key ID would collide with that of an existing key, in the event of either key being revoked. (This is only safe to use if you are sure you won&#8217;t be using RFC 5011 trust anchor maintenance with either of the keys involved.)</dl>
<h2>Timing Options</h2>
<p>Dates can be expressed in the format YYYYMMDD or YYYYMMDDHHMMSS. If the argument begins with a &#8216;+&#8217; or &#8216;-&#8216;, it is interpreted as an offset from the present time. For convenience, if such an offset is followed by one of the suffixes &#8216;y&#8217;, &#8216;mo&#8217;, &#8216;w&#8217;, &#8216;d&#8217;, &#8216;h&#8217;, or &#8216;mi&#8217;, then the offset is computed in years (defined as 365 24-hour days, ignoring leap years), months (defined as 30 24-hour days), weeks, days, hours, or minutes, respectively. Without a suffix, the offset is computed in seconds. </p>
<p> -P <i>date/offset</i></p>
<dl>
<dd>Sets the date on which a key is to be published to the zone. After that date, the key will be included in the zone but will not be used to sign it. If not set, and if the -G option has not been used, the default is &quot;now&quot;.</dl>
<p> -A <i>date/offset</i></p>
<dl>
<dd>Sets the date on which the key is to be activated. After that date, the key will be included in the zone and used to sign it. If not set, and if the -G option has not been used, the default is &quot;now&quot;.</dl>
<p> -R <i>date/offset</i></p>
<dl>
<dd>Sets the date on which the key is to be revoked. After that date, the key will be flagged as revoked. It will be included in the zone and will be used to sign it.</dl>
<p> -I <i>date/offset</i></p>
<dl>
<dd>Sets the date on which the key is to be retired. After that date, the key will still be included in the zone, but it will not be used to sign it.</dl>
<p> -D <i>date/offset</i></p>
<dl>
<dd>Sets the date on which the key is to be deleted. After that date, the key will no longer be included in the zone. (It may remain in the key repository, however.)</dl>
<h2>Generated Key Files</h2>
<p>When <code>dnssec-keyfromlabel</code> completes successfully, it prints a string of the form <i>Knnnn.+aaa+iiiii</i> to the standard output. This is an identification string for the key files it has generated.</p>
<dl>
<dt>&bull;</p>
<dd><i>nnnn</i> is the key name.</p>
<dt>&bull;</p>
<dd><i>aaa</i> is the numeric representation of the algorithm.</p>
<dt>&bull;</p>
<dd><i>iiiii</i> is the key identifier (or footprint).</dl>
<p> <code>dnssec-keyfromlabel</code> creates two files, with names based on the printed string. <i>Knnnn.+aaa+iiiii.key</i> contains the public key, and <i>Knnnn.+aaa+iiiii.private</i> contains the private key. </p>
<p> The <i>.key</i> file contains a DNS KEY record that can be inserted into a zone file (directly or with a $INCLUDE statement). </p>
<p> The <i>.private</i> file contains algorithm-specific fields. For obvious security reasons, this file does not have general read permission.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dnssec-keygen/">dnssec-keygen</a></code>(8), <code><a href="/docs/linux/man/8-dnssec-signzone/">dnssec-signzone</a></code>(8), BIND 9 Administrator Reference Manual, RFC 4034.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2008-2012 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
