---
title: "ldns-test-edns(1)"
name: "ldns-test-edns"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-test-edns/"
description: "ldns-test-edns – test if dns cache supports EDNS and DNSSEC."
---

<h2>NAME</h2>
<p> ldns-test-edns &#8211; test if dns cache supports EDNS and DNSSEC.</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-test-edns</code> [ <i>-i</i> ] { <i>ip</i> }</p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-test-edns</code> tests a DNS cache and checks if it supports EDNS0 and DNSSEC types so that it can be used as a dnssec-enabled DNS cache. It sends two queries to the cache, one for the root key and one for a DS record. These must succeed, the answer must have EDNS, that type and signatures. </p>
<p> If the IP address is good for DNSSEC, it is printed with &#8216;OK&#8217;. Otherwise short description is given of the failure. If OK is given, the cache should be good to use as a cache for a local configured DNSSEC validator. </p>
<p> The tool assumes the root is signed and Sweden is signed. Also, the queries are sent with the CD flag, the tool does not check that the results are validated, but that they <code>can</code> be validated.</p>
<h2>OPTIONS</h2>
<p> <code>-i</code> option enables a mode where the working IP addresses are printed after another, with no other explanations, and if none work or no IP addresses are on the input, &#8216;off&#8217; is printed. </p>
<p> <code>ldns-test-edns</code> takes one or more IP addresses, it checks them in turn. IPv4 and IPv6 addresses can be given. The exit value is for the last checked IP address: 0 is OK, 1 is failure, 2 is some sort of network failure.</p>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2010 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
