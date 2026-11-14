---
title: "spooky_hash128(3)"
name: "spooky_hash128"
section: "3"
letter: "s"
url: "/docs/linux/man/3-spooky_hash128/"
description: "spooky_hash128 – generate a \"spooky\" hash of an arbitrary blob of data"
---

<p>spooky_hash128 &#8211; generate a &quot;spooky&quot; hash of an arbitrary blob of data</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;spooky-c.h&gt;
void spooky_hash128(const void *message, size_t len, uint64_t *hash1, uint64_t *hash2);</code></pre>
<p> uint64_t spooky_hash64(const void *message, size_t len, uint64_t seed); uint32_t spooky_hash32(const void *message, size_t len, uint32_t seed);</p>
<h2>Description</h2>
<p>Quoting from Bob Jenkins&#8217; web page (inventor of the spooky hash function): </p>
<p> &#8220;SpookyHash is a public domain noncryptographic hash function producing well-distributed 128-bit hash values for byte arrays of any length.&#8221; </p>
<p> It can also produce 64-bit and 32-bit hash values too, by simply discarding the upper bits of the returned hash value. <code>spooky_hash32</code> and <code>spooky_hash64</code> are wrappers around <code>spooky_hash128</code> that do this discarding. </p>
<p> The <code>message</code> is a pointer to the stream of bytes to be hashed. <code>len</code> is the length of <code>message</code>. <code>seed</code> allows the function to generate different hashes for the same key. </p>
<p> <code>spooky_hash128</code> also accepts seed values in <code>hash1</code> and <code>hash2</code>. Those values will be overwritten with the actual hash results on return.</p>
<h2>Return Value</h2>
<p><code>spooky_hash64</code> and <code>spooky_hash32</code> return the hash value directly. <code>spooky_hash128</code> is a void return function. It overwrites the two 64-bit integers that <code>hash1</code> and <code>hash2</code> on return. These functions never return errors, only hash values.</p>
<h2>Notes</h2>
<p>The original code was written in C<font SIZE="-2">++</font>. The spooky-c library is a reimplementation of the hash function in C. It&#8217;s quite fast on 64-bit hardware. </p>
<p> There are some caveats with the SpookyHash function:</p>
<dl>
<dt>&bull;</p>
<dd>It was written for little-endian machines. It will run and work on big-endian machines as well, but it will produce different results. Do not use these functions if you plan to distribute these hashes in a mixed endianness environment.</p>
<dt>&bull;</p>
<dd>It is optimized for 64-bit machines that can do unaligned reads. It will work on 32-bit hardware and on machines that require aligned reads, but it won&#8217;t perform as well on that hardware. You may want to consider a different hash function in that situation.</dl>
<h2>See Also</h2>
<p>Bob Jenkins&#8217; webpage on SpookyHash: &lt;<a rel="nofollow" href="http://www.burtleburtle.net/bob/hash/spooky.html">http://www.burtleburtle.net/bob/hash/spooky.html</a>&gt;</p>
<h2>Authors</h2>
<p>Bob Jenkins &lt;bob_jenkins [at] burtleburtle.net&gt; invented the SpookyHash algorithm and wrote the original C<font SIZE="-2">++</font> implementation. The C implementation (spooky-c) was written by Andi Kleen &lt;andi [at] firstfloor.org&gt;. This manpage was authored by Jeff Layton &lt;jlayton [at] poochiereds.net&gt;.</p>
