---
title: "ldns-verify-zone(1)"
name: "ldns-verify-zone"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-verify-zone/"
description: "ldns-verify-zone – read a DNSSEC signed zone and verify it."
---

<h2>NAME</h2>
<p> ldns-verify-zone &#8211; read a DNSSEC signed zone and verify it.</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-verify-zone </code> <i>ZONEFILE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-verify-zone</code> reads a DNS zone file and verifies it. </p>
<p> RRSIG resource records are checked against the DNSKEY set at the zone apex. </p>
<p> Each name is checked for an <a href="/docs/linux/man/3-nsec/">NSEC</a>(3), if appropriate. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Show usage and exit </p>
<dt><code>-a</code></p>
<dd> Apex only, check only the zone apex </p>
<dt><code>-e</code> <i>period</i></p>
<dd> Signatures may not expire within this period. Default no period is used. </p>
<dt><code>-i</code> <i>period</i></p>
<dd> Signatures must have been valid at least this long. Default signatures should just be valid now. </p>
<dt><code>-k</code> <i>file</i></p>
<dd> A file that contains a trusted DNSKEY or DS rr. This option may be given more than once. </p>
<p> Alternatively, if <code>-k</code> is not specified, and a default trust anchor (/var/lib/unbound/root.key) exists and contains a valid DNSKEY or DS record, it will be used as the trust anchor.</p>
<dt><code>-p</code> <i>[0-100]</i></p>
<dd> Only check this percentage of the zone. Which names to check is determined randomly. Defaults to 100. </p>
<dt><code>-S</code></p>
<dd> Chase signature(s) to a known key. The network may be accessed to validate the zone&#8217;s DNSKEYs. (implies -k) </p>
<dt><code>-t</code> <i>YYYYMMDDhhmmss | [+|-]offset</i></p>
<dd> Set the validation time either by an absolute time value or as an offset in seconds from the current time. </p>
<dt><code>-v</code></p>
<dd> Show the version and exit </p>
<dt><code>-V</code> <i>number</i></p>
<dd> Set the verbosity level (default 3): </p>
<p>&nbsp;<wbr>0: Be silent<br />
&nbsp;<wbr>1: Print result, and any errors<br />
&nbsp;<wbr>2: Same as 1 for now<br />
&nbsp;<wbr>3: Print result, any errors, and the names that are<br />
&nbsp;<wbr>being checked<br />
&nbsp;<wbr>4: Same as 3 for now<br />
&nbsp;<wbr>5: Print the zone after it has been read, the result,&nbsp;<wbr><br />
&nbsp;<wbr>any errors, and the names that are being checked </p>
</dl>
<p> <i>period</i>s are given in ISO 8601 duration format:</p>
<dl>
<dt>
<dd> P[n]Y[n]M[n]DT[n]H[n]M[n]S</dl>
<p> If no file is given standard input is read. </p>
<h2>FILES</h2>
<dl>
<dt>/var/lib/unbound/root.key</p>
<dd> The file from which trusted keys are loaded for signature chasing, when no <code>-k</code> option is given. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-unbound-anchor/">unbound-anchor</a>(8) </p>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2008 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
