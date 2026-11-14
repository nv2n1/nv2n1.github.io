---
title: "stdtr2dynamic_bitset_reference(3)"
name: "stdtr2dynamic_bitset_reference"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtr2dynamic_bitset_reference/"
description: "std::tr2::dynamic_bitset< _WordT, _Alloc >::reference –"
---

<p>std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::reference &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<pre><code>reference (dynamic_bitset &amp;__b, size_type __pos)



reference &amp; flip ()



operator bool () const



reference &amp; operator= (bool __x)



reference &amp; operator= (const reference &amp;__j)



bool operator~ () const



Friends</code></pre>
<p> class <code>dynamic_bitset</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;typename _WordT = unsigned long long, typename _Alloc = std::allocator&lt;_WordT&gt;&gt;class std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::reference</h3>
<p>This encapsulates the concept of a single bit. An instance of this class is a proxy for an actual bit; this way the individual bit operations are done as faster word-size bitwise instructions. </p>
<p> Most users will never need to use this class directly; conversions to and from bool are automatic and should be transparent. Overloaded operators help to preserve the illusion. </p>
<p> (On a typical system, this &#8216;bit %reference&#8217; is 64 times the size of an actual bit. Ha.) </p>
<p> Definition at line 654 of file dynamic_bitset.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
