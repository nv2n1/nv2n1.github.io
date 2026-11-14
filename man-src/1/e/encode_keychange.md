---
title: "encode_keychange(1)"
name: "encode_keychange"
section: "1"
letter: "e"
url: "/docs/linux/man/1-encode_keychange/"
description: "encode_keychange – produce the KeyChange string for SNMPv3"
---

<h2>NAME</h2>
<p> encode_keychange &#8211; produce the KeyChange string for SNMPv3</p>
<h2>SYNOPSIS</h2>
<p> <code>encode_keychange </code> -t md5|sha1 [<i>OPTIONS</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>encode_keychange</code> produces a KeyChange string using the old and new passphrases as described in Section 5 of RFC 2274 &quot;User-based Security Model (USM) for version 3 of the Simple Network Management Protocol (SNMPv3)&quot;. <code>-t</code> option is mandatory and specifies the hash transform type to use. </p>
<p> The transform is used to convert passphrase to master key for a given user (Ku), convert master key to the localized key (Kul), and to hash the old Kul with the random bits. </p>
<p> Passphrases are obtained by examining a number of sources until success (in order listed):</p>
<dl>
<dt>
<dd> command line options (see <code>-N</code> and <code>-O</code> options below);</p>
<dt>
<dd> the file <code>$HOME/.snmp/passphrase.ek</code> which should only contain two lines with old and new passphrase;</p>
<dt>
<dd> standard input <code>-or-</code> user input from the terminal.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-E</code> [0x]&lt;<i>engineID</i>&gt; EngineID used for Kul generation.</p>
<dd> &lt;<i>engineID</i>&gt; is intepreted as a hex string when preceded by 0x, otherwise it is treated as a text string. If no &lt;<i>engineID</i>&gt; is specified, it is constructed from the first IP address for the local host.</p>
<dt><code>-f</code></p>
<dd> Force passphrases to be read from standard input.</p>
<dt><code>-h</code></p>
<dd> Display the help message.</p>
<dt><code>-N</code> &quot;&lt;<i>new_passphrase</i>&gt;&quot;</p>
<dd> Passphrase used to generate the new Ku.</p>
<dt><code>-O</code> &quot;&lt;<i>old_passphrase</i>&gt;&quot;</p>
<dd> Passphrase used to generate the old Ku.</p>
<dt><code>-P</code></p>
<dd> Turn off the prompt for passphrases when getting data from standard input.</p>
<dt><code>-v</code></p>
<dd> Be verbose.</p>
<dt><code>-V</code></p>
<dd> Echo passphrases to terminal.</dl>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> The localized key method is defined in RFC 2274, Sections 2.6 and A.2, and originally documented in</p>
<dl>
<dt>
<dd> U. Blumenthal, N. C. Hien, B. Wijnen, &quot;Key Derivation for Network Management Applications&quot;, IEEE Network Magazine, April/May issue, 1997. </p>
</dl>
<h2>Index</h2>
