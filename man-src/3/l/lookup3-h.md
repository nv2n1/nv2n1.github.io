---
title: "lookup3-h(3)"
name: "lookup3-h"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lookup3-h/"
description: "src/lookup3.h –"
---

<p>src/lookup3.h &#8211; </p>
<p> 32bit hash function implementation.</p>
<h2>Synopsis</h2>
<p>#include &lt;pbs_config.h&gt; </p>
<h3>Functions</h3>
<p>uint32_t <code>hashword</code> (const uint32_t *k, size_t length, uint32_t initval)<br />
 <i>This works on all machines. </i><br />
 uint32_t <code>hashlittle</code> (const void *key, size_t length, uint32_t initval)<br />
 <i></i><code>hashlittle()</code> &#8212; hash a variable-length key into a 32-bit value<br />
 uint32_t <code>hashbig</code> (const void *key, size_t length, uint32_t initval)<br />
 <i></i><code>hashbig()</code>: This is the same as <code>hashword()</code> on big-endian machines.</p>
<h2>Detailed Description</h2>
<p>32bit hash function implementation. </p>
<p> Taken from: <a rel="nofollow" href="http://burtleburtle.net/bob/hash/">http://burtleburtle.net/bob/hash/</a></p>
<h2>Function Documentation</h2>
<h3>uint32_t hashword (const uint32 *k, size_tlength, uint32initval)</h3>
<p>This works on all machines. To be useful, it requires &#8212; that the key be an array of uint32&#8217;s, and &#8212; that all your machines have the same endianness, and &#8212; that the length be the number of uint32&#8217;s in the key </p>
<p> The function <code>hashword()</code> is identical to <code>hashlittle()</code> on little-endian machines, and identical to <code>hashbig()</code> on big-endian machines, except that the length has to be measured in uint32s rather than in bytes. <code>hashlittle()</code> is more complicated than <code>hashword()</code> only because <code>hashlittle()</code> has to dance around fitting the key bytes into registers. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>k</i> the key, an array of uint32 values<br />
 <i>length</i> the length of the key, in uint32s<br />
 <i>initval</i> the previous hash, or an arbitrary value</dl>
<h3>uint32_t hashlittle (const void *key, size_tlength, uint32initval)</h3>
<p><code>hashlittle()</code> &#8212; hash a variable-length key into a 32-bit value </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>key</i> the key (the unaligned variable-length array of bytes)<br />
 <i>length</i> the length of the key, counting by bytes<br />
 <i>initval</i> can be any 4-byte value</dl>
<p> Returns a 32-bit value. Every bit of the key affects every bit of the return value. Two keys differing by one or two bits will have totally different hash values. </p>
<p> The best hash table sizes are powers of 2. There is no need to do mod a prime (mod is sooo slow!). If you need less than 32 bits, use a bitmask. For example, if you need only 10 bits, do h = (h &amp; hashmask(10)); In which case, the hash table should have hashsize(10) elements. </p>
<p> If you are hashing n strings (uint8 **)k, do it like this: for (i=0, h=0; i&lt;n; ++i) h = hashlittle( k[i], len[i], h); </p>
<p> By Bob Jenkins, 2006. bob_jenkins [at] burtleburtle.net. You may use this code any way you wish, private, educational, or commercial. It&#8217;s free. </p>
<p> Use for hash table lookup, or anything where one collision in 2^^32 is acceptable. Do NOT use for cryptographic purposes.</p>
<h3>uint32_t hashbig (const void *key, size_tlength, uint32initval)</h3>
<p><code>hashbig()</code>: This is the same as <code>hashword()</code> on big-endian machines. It is different from <code>hashlittle()</code> on all machines. <code>hashbig()</code> takes advantage of big-endian byte ordering.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for torque from the source code.</p>
