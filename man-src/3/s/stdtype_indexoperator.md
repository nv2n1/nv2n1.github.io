---
title: "stdtype_indexoperator(3)"
name: "stdtype_indexoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtype_indexoperator/"
---

std::type_index::operator==,!=,&lt;,&lt;=,&gt;,&gt;= - std::type_index::operator==,!=,&lt;,&lt;=,&gt;,&gt;=

<h2>Synopsis</h2>

bool operator==( const type_index&amp; rhs ) const noexcept; <i>(since C++11)</i> 
bool operator!=( const type_index&amp; rhs ) const noexcept; <i>(since C++11)</i> 
bool operator&lt;( const type_index&amp; rhs ) const noexcept; <i>(since C++11)</i> 
bool operator&lt;=( const type_index&amp; rhs ) const noexcept; <i>(since C++11)</i> 
bool operator&gt;( const type_index&amp; rhs ) const noexcept; <i>(since C++11)</i> 
bool operator&gt;=( const type_index&amp; rhs ) const noexcept; <i>(since C++11)</i> 
Compares the underlying std::type_info objects. 
1-2) Checks whether the underlying std::type_info objects refer to the same type. 
3-6) Compares the underlying std::type_info objects as defined by an implementation-defined ordering. The comparison is done by type_info::before. 

<h2>Parameters</h2>

rhs - another type_index object to compare to

<h2>Return value</h2>

1) true if the underlying std::type_info objects refer to the same type, false otherwise 
2) true if the underlying std::type_info objects refer not to the same type, false otherwise 
3-6) true if the types referred by the underlying std::type_info objects are ordered by corresponding order, false otherwise. 
