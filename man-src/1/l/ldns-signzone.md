---
title: "ldns-signzone(1)"
name: "ldns-signzone"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-signzone/"
description: "ldns-signzone – sign a zonefile with DNSSEC data"
---

<h2>NAME</h2>
<p> ldns-signzone &#8211; sign a zonefile with DNSSEC data</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-signzone </code> [ <i>OPTIONS</i> ] <i>ZONEFILE</i> KEY [KEY [KEY] &#8230; ] </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-signzone</code> is used to generate a DNSSEC signed zone. When run it will create a new zonefile that contains RRSIG and NSEC resource records, as specified in RFC 4033, RFC 4034 and RFC 4035. </p>
<p> Keys must be specified by their base name (i.e. without .private). If the DNSKEY that belongs to the key in the .private file is not present in the zone, it will be read from the file &lt;base name&gt;.key. If that file does not exist, the DNSKEY value will be generated from the private key. </p>
<p> Multiple keys can be specified, Key Signing Keys are used as such when they are either already present in the zone, or specified in a .key file, and have the KSK bit set. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> Augments the zone and the RR&#8217;s with extra comment texts for a more readable layout, easier to debug. DS records will have a bubblebabble version of the data in the comment text, NSEC3 records will have the original NSEC3 in the comment text. </p>
<p> Without this option, only DNSKEY RR&#8217;s will have their Key Tag annotated in the comment text. </p>
<dt><code>-d</code></p>
<dd> Normally, if the DNSKEY RR for a key that is used to sign the zone is not found in the zone file, it will be read from .key, or derived from the private key (in that order). This option turns that feature off, so that only the signatures are added to the zone. </p>
<dt><code>-e</code> <i>date</i></p>
<dd> Set expiration date of the signatures to this date, the format can be YYYYMMDD[hhmmss], or a timestamp. </p>
<dt><code>-f</code> <i>file</i></p>
<dd> Use this file to store the signed zone in (default &lt;originalfile&gt;.signed) </p>
<dt><code>-i</code> <i>date</i></p>
<dd> Set inception date of the signatures to this date, the format can be YYYYMMDD[hhmmss], or a timestamp. </p>
<dt><code>-o</code> <i>origin</i></p>
<dd> Use this as the origin of the zone </p>
<dt><code>-v</code></p>
<dd> Print the version and exit </p>
<dt><code>-A</code></p>
<dd> Sign the DNSKEY record with all keys. By default it is signed with a minimal number of keys, to keep the response size for the DNSKEY query small, and only the SEP keys that are passed are used. If there are no SEP keys, the DNSKEY RRset is signed with the non-SEP keys. This option turns off the default and all keys are used to sign the DNSKEY RRset. </p>
<dt><code>-E</code> <i>name</i></p>
<dd> Use the EVP cryptographic engine with the given name for signing. This can have some extra options; see ENGINE OPTIONS for more information. </p>
<dt><code>-k</code> <i>id,int</i></p>
<dd> Use the key with the given id as the signing key for algorithm int as a Zone signing key. This option is used when you use an OpenSSL engine, see ENGINE OPTIONS for more information. </p>
<dt><code>-K</code> <i>id,int</i></p>
<dd>
<p> Use the key with the given id as the signing key for algorithm int as a Key signing key. This options is used when you use an OpenSSL engine, see ENGINE OPTIONS for more information. </p>
<dt><code>-n</code></p>
<dd> Use NSEC3 instead of NSEC. </p>
<dt>If you use NSEC3, you can specify the following extra options:</p>
<dd>
<dt><code>-a</code> <i>algorithm</i></p>
<dd> Algorithm used to create the hashed NSEC3 owner names </p>
<dt><code>-p</code></p>
<dd> Opt-out. All NSEC3 records in the zone will have the Opt-out flag set. After signing, you can add insecure delegations to the signed zone. </p>
<dt><code>-s</code> <i>string</i></p>
<dd> Salt </p>
<dt><code>-t</code> <i>number</i></p>
<dd> Number of hash iterations </p>
</dl>
<h2>ENGINE OPTIONS</h2>
<p> You can modify the possible engines, if supported, by setting an OpenSSL configuration file. This is done through the environment variable OPENSSL_CONF. If you use -E with a non-existent engine name, ldns-signzone will print a list of engines supported by your configuration. </p>
<p> The key options (-k and -K) work as follows; you specify a key id, and a DNSSEC algorithm number (for instance, 5 for RSASHA1). The key id can be any of the following: </p>
<p>&nbsp;<wbr>&lt;id&gt;<br />
&nbsp;<wbr>&lt;slot&gt;:&lt;id&gt;<br />
&nbsp;<wbr>id_&lt;id&gt;<br />
&nbsp;<wbr>slot_&lt;slot&gt;-id_&lt;id&gt;<br />
&nbsp;<wbr>label_&lt;label&gt;<br />
&nbsp;<wbr>slot_&lt;slot&gt;-label_&lt;label&gt; </p>
<p> Where &#8216;&lt;id&gt;&#8217; is the PKCS #11 key identifier in hexadecimal notation, &#8216;&lt;label&gt;&#8217; is the PKCS #11 human-readable label, and &#8216;&lt;slot&gt;&#8217; is the slot number where the token is present. </p>
<p> If not already present, a DNSKEY RR is generated from the key data, and added to the zone. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>ldns-signzone nlnetlabs.nl Knlnetlabs.nl.+005+12273</p>
<dd> Sign the zone in the file &#8216;nlnetlabs.nl&#8217; with the key in the files &#8216;Knlnetlabs.nl.+005+12273.private&#8217;. If the DNSKEY is not present in the zone, use the key in the file &#8216;Knlnetlabs.nl.+005+12273.key&#8217;. If that is not present, generate one with default values from &#8216;Knlnetlabs.nl.+005+12273.private&#8217;. </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005-2008 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
