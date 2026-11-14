---
title: "stdexperimentalfilesystemdirectory_entryoperator(3)"
name: "stdexperimentalfilesystemdirectory_entryoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalfilesystemdirectory_entryoperator/"
description: "std::experimental::filesystem::directory_entry::operator==,!=,<,<=,>,>= – std::experimental::filesystem::directory_entry::operator==,!=,<,<=,>,>="
---

<p>std::experimental::filesystem::directory_entry::operator==,!=,&lt;,&lt;=,&gt;,&gt;= &#8211; std::experimental::filesystem::directory_entry::operator==,!=,&lt;,&lt;=,&gt;,&gt;=</p>
<h2>Synopsis</h2>
<p>bool operator==( const directory_entry&amp; rhs ) const; <code>(1)</code> (filesystem TS)<br />
bool operator!=( const directory_entry&amp; rhs ) const; <code>(2)</code> (filesystem TS)<br />
bool operator&lt;( const directory_entry&amp; rhs ) const; <code>(3)</code> (filesystem TS)<br />
bool operator&lt;=( const directory_entry&amp; rhs ) const; <code>(4)</code> (filesystem TS)<br />
bool operator&gt;( const directory_entry&amp; rhs ) const; <code>(5)</code> (filesystem TS)<br />
bool operator&gt;=( const directory_entry&amp; rhs ) const; <code>(6)</code> (filesystem TS)<br />
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
<h2>Exceptions</h2>
<p>noexcept specification:<br />
noexcept</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the path the entry refers to<br />
path <i>(public member function)</i><br />
operator_const_path&amp; </p>
