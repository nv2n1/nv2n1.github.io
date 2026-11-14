---
title: "ldns-read-zone(1)"
name: "ldns-read-zone"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-read-zone/"
description: "ldns-read-zone – read a zonefile and print it"
---

<h2>NAME</h2>
<p> ldns-read-zone &#8211; read a zonefile and print it</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-read-zone </code> <i>ZONEFILE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-read-zone</code> reads a DNS zone file and prints it. The output has 1 resource record per line, and no pretty-printing makeup. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code></p>
<dd> Canonicalize all resource records in the zone before printing </p>
<dt><code>-d</code></p>
<dd> Only print DNSSEC data from the zone. This option skips every record that is not of type NSEC, NSEC3, RRSIG or DNSKEY. DS records are not printed. </p>
<dt><code>-b</code></p>
<dd> Include Bubble Babble encoding of DS&#8217;s. </p>
<dt><code>-0</code></p>
<dd> Print a (null) for the RRSIG inception, expiry and key data. This option can be used when comparing different signing systems that use the same DNSKEYs for signing but would have a slightly different timings/jitter. </p>
<dt><code>-h</code></p>
<dd> Show usage and exit </p>
<dt><code>-n</code></p>
<dd> Do not print the SOA record </p>
<dt><code>-p</code></p>
<dd> Pad the SOA serial number with spaces so the number and the spaces together take ten characters. This is useful for in file serial number increments. </p>
<dt><code>-s</code></p>
<dd> Strip DNSSEC data from the zone. This option skips every record that is of type NSEC, NSEC3, RRSIG or DNSKEY. DS records are still printed. </p>
<dt><code>-S</code> <i>[[+|0]number | YYYYMMDDxx | unixtime ]</i></p>
<dd> Set serial number to the given <i>number</i>, or when preceded by a sign, offset the exisiting number with it. When giving the literal strings <i>YYYYMMDDxx</i> or <i>unixtime</i>, the serial number is tried to be reset in datecounter or in unixtime format respectively. Though is the updated serial number is smaller than the original one, the original one is simply increased by one. </p>
<p> When updating a serial number, records of type NSEC, NSEC3, RRSIG and DNSKEY will be skipped when printing the zone. </p>
<dt><code>-v</code></p>
<dd> Show the version and exit </p>
<dt><code>-z</code></p>
<dd> Sort the zone before printing (this implies -c) </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
