---
title: "nsec3hash(8)"
name: "nsec3hash"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsec3hash/"
description: "nsec3hash – generate NSEC3 hash"
---

<p>nsec3hash &#8211; generate NSEC3 hash</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>nsec3hash</code> {<i>salt</i>} {<i>algorithm</i>} {<i>iterations</i>} {<i>domain</i>}</dl>
<h2>Description</h2>
<p><code>nsec3hash</code></p>
<dd>generates an NSEC3 hash based on a set of NSEC3 parameters. This can be used to check the validity of NSEC3 records in a signed zone.</p>
<h2>Arguments</h2>
<p>salt</p>
<dl>
<dd>The salt provided to the hash algorithm.</dl>
<p> algorithm</p>
<dl>
<dd>A number indicating the hash algorithm. Currently the only supported hash algorithm for NSEC3 is SHA-1, which is indicated by the number 1; consequently &quot;1&quot; is the only useful value for this argument.</dl>
<p> iterations</p>
<dl>
<dd>The number of additional times the hash should be performed.</dl>
<p> domain</p>
<dl>
<dd>The domain name to be hashed.</dl>
<h2>See Also</h2>
<p>BIND 9 Administrator Reference Manual, RFC 5155.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009 Internet Systems Consortium, Inc. (&quot;ISC&quot;)</p>
