---
title: "std__detail_hash_code_base(3)"
name: "std__detail_hash_code_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-std__detail_hash_code_base/"
---

std::__detail::_Hash_code_base&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, __cache_hash_code &gt; -

<h2>Synopsis</h2>



<h2>Detailed Description</h2>

<h3>template&lt;typename _Key, typename _Value, typename _ExtractKey, typename _H1, typename _H2, typename _Hash, bool __cache_hash_code&gt;struct std::__detail::_Hash_code_base&lt; _Key, _Value, _ExtractKey, _H1, _H2, _Hash, __cache_hash_code &gt;</h3>

Primary class template _Hash_code_base. 

 Encapsulates two policy issues that aren't quite orthogonal. (1) the difference between using a ranged hash function and using the combination of a hash function and a range-hashing function. In the former case we don't have such things as hash codes, so we have a dummy type as placeholder. (2) Whether or not we cache hash codes. Caching hash codes is meaningless if we have a ranged hash function. 

 We also put the key extraction objects here, for convenience. Each specialization derives from one or more of the template parameters to benefit from Ebo. This is important as this type is inherited in some cases by the _Local_iterator_base type used to implement local_iterator and const_local_iterator. As with any iterator type we prefer to make it as small as possible. 

 Primary template is unused except as a hook for specializations. 

 Definition at line 907 of file hashtable_policy.h.

<h2>Author</h2>

Generated automatically by Doxygen for libstdc++ from the source code.
