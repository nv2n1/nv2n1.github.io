---
title: "knsec3hash(1)"
name: "knsec3hash"
section: "1"
letter: "k"
url: "/docs/linux/man/1-knsec3hash/"
description: "knsec3hash – Simple utility to compute NSEC3 hash (libknot equivalent of ISC nsec3hash)"
---

<h2>NAME</h2>
<p> <code>knsec3hash</code> &#8211; Simple utility to compute NSEC3 hash (libknot equivalent of ISC nsec3hash)</p>
<h2>SYNOPSIS</h2>
<p> <code>knsec3hash</code> {<i>salt</i>} {<i>algorithm</i>} {<i>iterations</i>} {<i>domain-name</i>}</p>
<h2>DESCRIPTION</h2>
<p> This utility generates NSEC3 hash for a given domain name and parameters of NSEC3 hash.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>salt</i></p>
<dd> Specifies binary salt encoded as a hexadecimal string.</p>
<dt><i>algorithm</i></p>
<dd> Specifies hashing algorithm number. Currently the only supported algorithm is SHA-1 (number 1).</p>
<dt><i>iterations</i></p>
<dd> Specifies the number of additional iterations of the hashing algorithm.</p>
<dt><i>domain-name</i></p>
<dd> Specifies the domain name to be hashed.</dl>
<h2>SEE ALSO</h2>
<p> RFC 5155 &#8211; DNS Security (DNSSEC) Hashed Authenticated Denial of Existence.</p>
<h2>EXAMPLE</h2>
<p> $ knsec3hash c01dcafe 1 10 knot-dns.cz<br />
 7PTVGE7QV67EM61ROS9238P5RAKR2DM7 (salt=c01dcafe, hash=1, iterations=10)</p>
<h2>AUTHOR</h2>
<p> Jan Vcelak (<code><a rel="nofollow" href="http://knot-dns.cz">http://knot-dns.cz</a></code>)</p>
<dl>
<dt>Please send any bugs or comments to <code>knot-dns [at] labs.nic.cz</code></p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-knotc/">knotc</a></code>(8), <code><a href="/docs/linux/man/8-knotd/">knotd</a></code>(8). </p>
<h2>Index</h2>
