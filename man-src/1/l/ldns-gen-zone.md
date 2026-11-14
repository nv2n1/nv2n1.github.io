---
title: "ldns-gen-zone(1)"
name: "ldns-gen-zone"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-gen-zone/"
description: "ldns-gen-zone – read a zonefile and print it while adding DS records and extra RR’s"
---

<h2>NAME</h2>
<p> ldns-gen-zone &#8211; read a zonefile and print it while adding DS records and extra RR&#8217;s</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-gen-zone </code> <i>ZONEFILE</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-gen-zone</code> reads a DNS zone file and prints it. </p>
<p> It is build for speed, not for a nice formatting. The output has one resource record per line and no pretty-printing makeup. </p>
<p> DNSSEC data (NSEC, NSEC3, RRSIG or DNSKEY) is not stripped. You may want to use <code>ldns-read-zone</code> for that. Existing DS records are also not stripped. </p>
<p> The idea is to use this tool for quickly generating a representative artificial zonefile from a real zonefile, to use it for testing purposes. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a NUM</code></p>
<dd> Adds NUM extra artificial NS RRSets to the output. The RRSets owner names start with &#8216;xn--&#8216; in an attempt to ensure uniqueness (nl.-zone does not support IDN&#8217;s &#8211; and this tool was written with that knowledge in mind). </p>
<p> An artificial NS RRSet has two NS records; ns1.example.com and ns2.example.com. </p>
<dt><code>-p NUM</code></p>
<dd> Add NUM% of DS RRSets to the NS RRSets (anywhere between 1-4 DS records per RRSet). </p>
<dt><code>-o ORIGIN</code></p>
<dd> Sets an $ORIGIN, which can be handy if the one in the zonefile is set to &#8216;@&#8217; for example. If there is an $ORIGIN in the zonefile, this option will silently be ignored. </p>
<dt><code>-s</code></p>
<dd> This is the recommended way of processing large zones that are already sorted and canonicalized (ie lowercase). It skips the sorting and canonicalization step that is required for properly grouping RRSets together (before adding any DS records to them. Skipping this step will speed things up. </p>
<p> It is not recommended to use this option if you want to add DS records to unsorted, non-canonicalized zones. </p>
<dt><code>-h</code></p>
<dd> Show usage and exit. </p>
<dt><code>-v</code></p>
<dd> Show version and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>ldns-gen-zone -a 100000 -p 10 -s ./zonefile.txt</code></p>
<dd> Read a zonefile, add 100.000 artificial NS RRSets and 10% of DS records, print it to standard output. Don&#8217;t sort (will only work well if the input zonefile is already sorted and canonicalized). </p>
<dt><code>ldns-gen-zone -p 10 -s -o nl zonefile.txt | named-compilezone -s relative -i none -o zonefile_10.txt nl /dev/stdin</code></p>
<dd> This creates a nicely formatted zone file with the help of <code>named-compilezone</code>. It adds 10% DS records to the .nl zone, reformats it and saves it as <code>zonefile_10.txt</code>. </p>
</dl>
<h2>AUTHOR</h2>
<p> Initially written by Marco Davids, several modifications added by Miek Gieben, both from SIDN. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>BUGS</h2>
<p> Only undiscovered ones. </p>
<h2>CAVEATS</h2>
<p> May require a machine with a considerable amount of memory for large zone files. </p>
<p> Fake DS records hashes are generated as digest type SHA-256 (RFC4509). Be aware not to change the DIGESTTYPE #define in the source code in anything else but 2 if you want to keep things realistic. </p>
<p> Despite a number of efforts, this program is still not the fastest in the world. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010 SIDN. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
