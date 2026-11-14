---
title: "std__detail_prime_rehash_policy(3)"
name: "std__detail_prime_rehash_policy"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_prime_rehash_policy/"
description: "std::__detail::_Prime_rehash_policy –"
---

<p>std::__detail::_Prime_rehash_policy &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>enum { <code>_S_n_primes</code> } </p>
<p> typedef std::size_t <code>_State</code></p>
<h3>Public Member Functions</h3>
<pre><code>_Prime_rehash_policy (float __z=1.0)



std::size_t _M_bkt_for_elements (std::size_t __n) const



std::pair&lt; bool, std::size_t &gt; _M_need_rehash (std::size_t __n_bkt, std::size_t __n_elt, std::size_t __n_ins) const



std::size_t _M_next_bkt (std::size_t __n) const



void _M_reset (_State __state)



_State _M_state () const



float max_load_factor () const noexcept



Public Attributes
float _M_max_load_factor



std::size_t _M_next_resize



Static Public Attributes
static const std::size_t _S_growth_factor</code></pre>
<h2>Detailed Description</h2>
<p>Default value for rehash policy. Bucket size is (usually) the smallest prime that keeps the load factor small enough. </p>
<p> Definition at line 357 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
