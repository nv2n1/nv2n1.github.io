---
title: "std__detail_default_ranged_hash(3)"
name: "std__detail_default_ranged_hash"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_default_ranged_hash/"
---

std::__detail::_Default_ranged_hash -

<h2>Synopsis</h2>



<h2>Detailed Description</h2>

Default ranged hash function H. In principle it should be a function object composed from objects of type H1 and H2 such that h(k, N) = h2(h1(k), N), but that would mean making extra copies of h1 and h2. So instead we'll just use a tag to tell class template hashtable to do that composition. 

 Definition at line 353 of file hashtable_policy.h.

<h2>Author</h2>

Generated automatically by Doxygen for libstdc++ from the source code.
