---
title: "std__detail_mod_range_hashing(3)"
name: "std__detail_mod_range_hashing"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_mod_range_hashing/"
description: "std::__detail::_Mod_range_hashing –"
---

<p>std::__detail::_Mod_range_hashing &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Types</h3>
<p>typedef std::size_t <code>first_argument_type</code> </p>
<p> typedef std::size_t <code>result_type</code> </p>
<p> typedef std::size_t <code>second_argument_type</code></p>
<h3>Public Member Functions</h3>
<p>result_type <code>operator()</code> (first_argument_type __num, second_argument_type __den) const</p>
<h2>Detailed Description</h2>
<p>Default range hashing function: use division to fold a large number into the range [0, N). </p>
<p> Definition at line 337 of file hashtable_policy.h.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
