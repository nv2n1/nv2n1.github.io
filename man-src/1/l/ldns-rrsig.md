---
title: "ldns-rrsig(1)"
name: "ldns-rrsig"
section: "1"
letter: "l"
url: "/docs/linux/man/1-ldns-rrsig/"
description: "ldns-rrsig – print out the inception and expiration dates in human readable form"
---

<h2>NAME</h2>
<p> ldns-rrsig &#8211; print out the inception and expiration dates in human readable form</p>
<h2>SYNOPSIS</h2>
<p> <code>ldns-rrsig </code> <i>domain</i> [ <i>type</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>ldns-rrsig</code> is used to print the expiration and inception date of a RRSIG. The first argument is a domain name. <code>ldns-rrsig</code> will query the authoritative servers for that domain to get a list of RRSIGs. It will then print out the inception and experiration dates for the RRSIG covering the SOA record. </p>
<p> If the second argument <code>type</code> is given the RRSIG covering that type will be shown. </p>
<h2>AUTHOR</h2>
<p> Written by the ldns team as an example for ldns usage. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;ldns-team [at] nlnetlabs.nl&gt;. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2005 NLnet Labs. This is free software. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
