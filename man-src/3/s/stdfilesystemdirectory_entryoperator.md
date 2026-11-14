---
title: "stdfilesystemdirectory_entryoperator(3)"
name: "stdfilesystemdirectory_entryoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfilesystemdirectory_entryoperator/"
description: "std::filesystem::directory_entry::operator==,!=,<,<=,>,>= – std::filesystem::directory_entry::operator==,!=,<,<=,>,>="
---

<p>std::filesystem::directory_entry::operator==,!=,&lt;,&lt;=,&gt;,&gt;= &#8211; std::filesystem::directory_entry::operator==,!=,&lt;,&lt;=,&gt;,&gt;=</p>
<h2>Synopsis</h2>
<p>bool operator==( const directory_entry&amp; rhs ) const noexcept; <code>(1)</code> <i>(since C++17)</i><br />
bool operator!=( const directory_entry&amp; rhs ) const noexcept; <code>(2)</code> <i>(since C++17)</i><br />
bool operator&lt;( const directory_entry&amp; rhs ) const noexcept; <code>(3)</code> <i>(since C++17)</i><br />
bool operator&lt;=( const directory_entry&amp; rhs ) const noexcept; <code>(4)</code> <i>(since C++17)</i><br />
bool operator&gt;( const directory_entry&amp; rhs ) const noexcept; <code>(5)</code> <i>(since C++17)</i><br />
bool operator&gt;=( const directory_entry&amp; rhs ) const noexcept; <code>(6)</code> <i>(since C++17)</i><br />
Compares the path with the directory entry rhs. </p>
<h2>Parameters</h2>
<p>rhs &#8211; directory_entry to compare</p>
<h2>Return value</h2>
<p>1) true if path() == rhs.path(), false otherwise.<br />
2) true if path() != rhs.path(), false otherwise.<br />
3) true if path() &lt; rhs.path(), false otherwise.<br />
4) true if path() &lt;= rhs.path(), false otherwise.<br />
5) true if path() &gt; rhs.path(), false otherwise.<br />
6) true if path() &gt;= rhs.path(), false otherwise. </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the path the entry refers to<br />
path <i>(public member function)</i><br />
operator_const_path&amp; </p>
