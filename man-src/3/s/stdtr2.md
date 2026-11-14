---
title: "stdtr2(3)"
name: "stdtr2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtr2/"
description: "std::tr2 –"
---

<p>std::tr2 &#8211;</p>
<h2>Synopsis</h2>
<h3>Namespaces</h3>
<p><code>__detail</code></p>
<h3>Classes</h3>
<pre><code>struct __dynamic_bitset_base



struct __reflection_typelist



struct __reflection_typelist&lt; _First, _Rest...&gt;



struct __reflection_typelist&lt;&gt;



struct bases



class bool_set



struct direct_bases



class dynamic_bitset



Functions</code></pre>
<p> bool <code>certainly</code> (<code>bool_set</code> __b) </p>
<p> bool <code>contains</code> (<code>bool_set</code> __s, <code>bool_set</code> __t) </p>
<p> bool <code>equals</code> (<code>bool_set</code> __s, <code>bool_set</code> __t) </p>
<p> bool <code>is_emptyset</code> (<code>bool_set</code> __b) </p>
<p> bool <code>is_indeterminate</code> (<code>bool_set</code> __b) </p>
<p> bool <code>is_singleton</code> (<code>bool_set</code> __b) </p>
<p> <code>bool_set</code> <code>operator!=</code> (bool __s, <code>bool_set</code> __t) </p>
<p> <code>bool_set</code> <code>operator!=</code> (<code>bool_set</code> __s, bool __t) </p>
<p> <code>bool_set</code> <code>operator!=</code> (<code>bool_set</code> __s, <code>bool_set</code> __t) </p>
<p> <code>bool_set</code> <code>operator&amp;</code> (bool __s, <code>bool_set</code> __t) </p>
<p> <code>bool_set</code> <code>operator&amp;</code> (<code>bool_set</code> __s, bool __t) </p>
<p> <code>bool_set</code> <code>operator==</code> (bool __s, <code>bool_set</code> __t) </p>
<p> <code>bool_set</code> <code>operator==</code> (<code>bool_set</code> __s, bool __t) </p>
<p> <code>bool_set</code> <code>operator^</code> (bool __s, <code>bool_set</code> __t) </p>
<p> <code>bool_set</code> <code>operator^</code> (<code>bool_set</code> __s, bool __t) </p>
<p> <code>bool_set</code> <code>operator|</code> (bool __s, <code>bool_set</code> __t) </p>
<p> <code>bool_set</code> <code>operator|</code> (<code>bool_set</code> __s, bool __t) </p>
<p> bool <code>possibly</code> (<code>bool_set</code> __b) </p>
<p> <code>bool_set</code> <code>set_complement</code> (<code>bool_set</code> __b) </p>
<p> <code>bool_set</code> <code>set_intersection</code> (bool __s, <code>bool_set</code> __t) </p>
<p> <code>bool_set</code> <code>set_intersection</code> (<code>bool_set</code> __s, bool __t) </p>
<p> <code>bool_set</code> <code>set_intersection</code> (<code>bool_set</code> __s, <code>bool_set</code> __t) </p>
<p> <code>bool_set</code> <code>set_union</code> (bool __s, <code>bool_set</code> __t) </p>
<p> <code>bool_set</code> <code>set_union</code> (<code>bool_set</code> __s, bool __t) </p>
<p> <code>bool_set</code> <code>set_union</code> (<code>bool_set</code> __s, <code>bool_set</code> __t) </p>
<p> template&lt;typename _WordT , typename _Alloc &gt; bool <code>operator==</code> (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__lhs, const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _WordT , typename _Alloc &gt; bool <code>operator!=</code> (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__lhs, const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _WordT , typename _Alloc &gt; bool <code>operator&lt;</code> (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__lhs, const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _WordT , typename _Alloc &gt; bool <code>operator&lt;=</code> (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__lhs, const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _WordT , typename _Alloc &gt; bool <code>operator&gt;</code> (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__lhs, const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _WordT , typename _Alloc &gt; bool <code>operator&gt;=</code> (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__lhs, const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__rhs) </p>
<p> template&lt;typename _WordT , typename _Alloc &gt; <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; <code>operator&amp;</code> (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__x, const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _WordT , typename _Alloc &gt; <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; <code>operator|</code> (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__x, const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _WordT , typename _Alloc &gt; <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; <code>operator^</code> (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__x, const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__y) </p>
<p> template&lt;typename _WordT , typename _Alloc &gt; <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; <code>operator-</code> (const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__x, const <code>dynamic_bitset</code>&lt; _WordT, _Alloc &gt; &amp;__y) </p>
<pre><code>
template&lt;typename _CharT , typename _Traits , typename _WordT , typename _Alloc &gt; std::basic_istream&lt; _CharT,


_Traits &gt; &amp; operator&gt;&gt; (std::basic_istream&lt; _CharT, _Traits &gt; &amp;__is, dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__x)&quot;


template&lt;typename _CharT , typename _Traits , typename _WordT , typename _Alloc &gt; std::basic_ostream&lt; _CharT,


_Traits &gt; &amp; operator&lt;&lt; (std::basic_ostream&lt; _CharT, _Traits &gt; &amp;__os, const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__x)&quot;</code></pre>
<h2>Detailed Description</h2>
<p>ISO C++ TR2 entities toplevel namespace is std::tr2.</p>
<h2>Function Documentation</h2>
<h3>template&lt;typename _WordT , typename _Alloc &gt; bool std::tr2::operator!= (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__lhs, const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__rhs)</h3>
<p>These comparisons for equality/inequality are, well, <i>bitwise</i>. </p>
<p> Definition at line 1291 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT , typename _Alloc &gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt; std::tr2::operator&amp; (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__x, const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__y) [inline]</h3>
<p>Global bitwise operations on bitsets. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__x</i> A bitset.<br />
 <i>__y</i> A bitset of the same size as <i>__x</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A new bitset.</dl>
<p> These should be self-explanatory. </p>
<p> Definition at line 1332 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT , typename _Alloc &gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt; std::tr2::operator- (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__x, const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__y) [inline]</h3>
<p>Global bitwise operations on bitsets. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__x</i> A bitset.<br />
 <i>__y</i> A bitset of the same size as <i>__x</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A new bitset.</dl>
<p> These should be self-explanatory. </p>
<p> Definition at line 1362 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT , typename _Alloc &gt; bool std::tr2::operator&lt; (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__lhs, const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__rhs)</h3>
<p>These comparisons for equality/inequality are, well, <i>bitwise</i>. </p>
<p> Definition at line 1297 of file dynamic_bitset.</p>
<h3>template&lt;typename _CharT , typename _Traits , typename _WordT , typename _Alloc &gt; <code>std::basic_ostream</code>&lt;_CharT, _Traits&gt;&amp; std::tr2::operator&lt;&lt; (<code>std::basic_ostream</code>&lt; _CharT, _Traits &gt; &amp;__os, const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__x)</h3>
<p>Global I/O operators for bitsets. Direct I/O between streams and bitsets is supported. Output is straightforward. Input will skip whitespace and only accept &#8216;0&#8217; and &#8216;1&#8217; characters. The dynamic_bitset will grow as necessary to hold the string of bits. </p>
<p> Definition at line 1455 of file dynamic_bitset. </p>
<p> References std::__ctype_abstract_base&lt; _CharT &gt;::widen().</p>
<h3>template&lt;typename _WordT , typename _Alloc &gt; bool std::tr2::operator&lt;= (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__lhs, const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__rhs)</h3>
<p>These comparisons for equality/inequality are, well, <i>bitwise</i>. </p>
<p> Definition at line 1303 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT , typename _Alloc &gt; bool std::tr2::operator== (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__lhs, const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__rhs)</h3>
<p>These comparisons for equality/inequality are, well, <i>bitwise</i>. </p>
<p> Definition at line 1285 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT , typename _Alloc &gt; bool std::tr2::operator&gt; (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__lhs, const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__rhs)</h3>
<p>These comparisons for equality/inequality are, well, <i>bitwise</i>. </p>
<p> Definition at line 1309 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT , typename _Alloc &gt; bool std::tr2::operator&gt;= (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__lhs, const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__rhs)</h3>
<p>These comparisons for equality/inequality are, well, <i>bitwise</i>. </p>
<p> Definition at line 1315 of file dynamic_bitset.</p>
<h3>template&lt;typename _CharT , typename _Traits , typename _WordT , typename _Alloc &gt; <code>std::basic_istream</code>&lt;_CharT, _Traits&gt;&amp; std::tr2::operator&gt;&gt; (<code>std::basic_istream</code>&lt; _CharT, _Traits &gt; &amp;__is, dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__x)</h3>
<p>Global I/O operators for bitsets. Direct I/O between streams and bitsets is supported. Output is straightforward. Input will skip whitespace and only accept &#8216;0&#8217; and &#8216;1&#8217; characters. The dynamic_bitset will grow as necessary to hold the string of bits. </p>
<p> Definition at line 1383 of file dynamic_bitset. </p>
<p> References std::basic_string&lt; _CharT, _Traits, _Alloc &gt;::empty(), std::basic_string&lt; _CharT, _Traits, _Alloc &gt;::push_back(), std::basic_ios&lt; _CharT, _Traits &gt;::rdbuf(), std::basic_string&lt; _CharT, _Traits, _Alloc &gt;::reserve(), std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::resize(), std::basic_ios&lt; _CharT, _Traits &gt;::setstate(), std::basic_string&lt; _CharT, _Traits, _Alloc &gt;::size(), std::tr2::dynamic_bitset&lt; _WordT, _Alloc &gt;::size(), and std::basic_ios&lt; _CharT, _Traits &gt;::widen().</p>
<h3>template&lt;typename _WordT , typename _Alloc &gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt; std::tr2::operator^ (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__x, const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__y) [inline]</h3>
<p>Global bitwise operations on bitsets. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__x</i> A bitset.<br />
 <i>__y</i> A bitset of the same size as <i>__x</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A new bitset.</dl>
<p> These should be self-explanatory. </p>
<p> Definition at line 1352 of file dynamic_bitset.</p>
<h3>template&lt;typename _WordT , typename _Alloc &gt; <code>dynamic_bitset</code>&lt;_WordT, _Alloc&gt; std::tr2::operator| (const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__x, const dynamic_bitset&lt; _WordT, _Alloc &gt; &amp;__y) [inline]</h3>
<p>Global bitwise operations on bitsets. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>__x</i> A bitset.<br />
 <i>__y</i> A bitset of the same size as <i>__x</i>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>A new bitset.</dl>
<p> These should be self-explanatory. </p>
<p> Definition at line 1342 of file dynamic_bitset.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
