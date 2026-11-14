---
title: "ldns_init_random(3)"
name: "ldns_init_random"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldns_init_random/"
description: "ldns_init_random"
---

<h2>NAME</h2>
<p> ldns_init_random </p>
<h2>SYNOPSIS</h2>
<p> #include &lt;stdint.h&gt;<br />
 #include &lt;stdbool.h&gt; </p>
<p> #include &lt;ldns/ldns.h&gt; </p>
<p> int ldns_init_random(FILE *fd, unsigned int size); </p>
<h2>DESCRIPTION</h2>
<dl>
<dt> <i>ldns_init_random</i>()</p>
<dd>Seed the random function. If the file descriptor is specified, the random generator is seeded with data from that file. If not, /dev/urandom is used. </p>
<p> applications should call this if they need entropy data within ldns If openSSL is available, it is automatically seeded from /dev/urandom or /dev/random. </p>
<p> If you need more entropy, or have no openssl available, this function MUST be called at the start of the program </p>
<p> If openssl *is* available, this function just adds more entropy </p>
<p> .br <code>fd</code>: a file providing entropy data for the seed .br <code>size</code>: the number of bytes to use as entropy data. If this is 0, only the minimal amount is taken (usually 4 bytes) .br Returns 0 if seeding succeeds, 1 if it fails</dl>
<h2>AUTHOR</h2>
<p> The ldns team at NLnet Labs. Which consists out of Jelte Jansen and Miek Gieben. </p>
<h2>REPORTING BUGS</h2>
<p> Please report bugs to ldns-team [at] nlnetlabs.nl or in our bugzilla at <a rel="nofollow" href="http://www.nlnetlabs.nl/bugs/index.html">http://www.nlnetlabs.nl/bugs/index.html</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2004 &#8211; 2006 NLnet Labs. </p>
<p> Licensed under the BSD License. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <i>ldns_sign_public</i>, <i>ldns_key</i>. And <code>perldoc Net::DNS</code>, <code>RFC1034</code>, <code>RFC1035</code>, <code>RFC4033</code>, <code>RFC4034</code> and <code>RFC4035</code>.</p>
<h2>REMARKS</h2>
<p> This manpage was automaticly generated from the ldns source code by use of Doxygen and some perl. </p>
<h2>Index</h2>
