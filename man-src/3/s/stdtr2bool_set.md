---
title: "stdtr2bool_set(3)"
name: "stdtr2bool_set"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtr2bool_set/"
description: "std::tr2::bool_set –"
---

<p>std::tr2::bool_set &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<p>constexpr <code>bool_set</code> () </p>
<p> constexpr <code>bool_set</code> (bool __t) </p>
<p> bool <code>contains</code> (<code>bool_set</code> __b) const </p>
<p> bool <code>equals</code> (<code>bool_set</code> __b) const </p>
<p> bool <code>is_emptyset</code> () const </p>
<p> bool <code>is_indeterminate</code> () const </p>
<p> bool <code>is_singleton</code> () const </p>
<p> <code>operator bool</code> () const</p>
<h3>Static Public Member Functions</h3>
<pre><code>static bool_set emptyset ()



static bool_set indeterminate ()



Friends</code></pre>
<p> <code>bool_set</code> <code>operator!</code> (<code>bool_set</code> __b) </p>
<p> <code>bool_set</code> <code>operator&amp;</code> (<code>bool_set</code> __s, <code>bool_set</code> __t) </p>
<p> template&lt;typename CharT , typename Traits &gt; <code>std::basic_ostream</code>&lt; CharT,<br />
 Traits &gt; &amp; <code>operator&lt;&lt;</code> (<code>std::basic_ostream</code>&lt; CharT, Traits &gt; &amp;__out, <code>bool_set</code> __b)&quot; </p>
<p> <code>bool_set</code> <code>operator==</code> (<code>bool_set</code> __s, <code>bool_set</code> __t) </p>
<p> template&lt;typename CharT , typename Traits &gt; <code>std::basic_istream</code>&lt; CharT,<br />
 Traits &gt; &amp; <code>operator&gt;&gt;</code> (<code>std::basic_istream</code>&lt; CharT, Traits &gt; &amp;__in, <code>bool_set</code> &amp;__b)&quot; </p>
<p> <code>bool_set</code> <code>operator^</code> (<code>bool_set</code> __s, <code>bool_set</code> __t) </p>
<p> <code>bool_set</code> <code>operator|</code> (<code>bool_set</code> __s, <code>bool_set</code> __t)</p>
<h2>Detailed Description</h2>
<p>bool_set </p>
<p> See N2136, Bool_set: multi-valued logic by Hervé Brönnimann, Guillaume Melquiond, Sylvain Pion. </p>
<p> The implicit conversion to bool is slippery! I may use the new explicit conversion. This has been specialized in the language so that in contexts requiring a bool the conversion happens implicitly. Thus most objections should be eliminated. </p>
<p> Definition at line 54 of file bool_set.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>constexpr std::tr2::bool_set::bool_set () [inline]</h3>
<p>Default constructor. </p>
<p> Definition at line 59 of file bool_set.</p>
<h3>constexpr std::tr2::bool_set::bool_set (bool__t) [inline]</h3>
<p>Constructor from bool. </p>
<p> Definition at line 62 of file bool_set.</p>
<h2>Member Function Documentation</h2>
<h3>bool std::tr2::bool_set::equals (<code>bool_set</code>__b) const [inline]</h3>
<p>Return true if states are equal. </p>
<p> Definition at line 69 of file bool_set.</p>
<h3>bool std::tr2::bool_set::is_emptyset () const [inline]</h3>
<p>Return true if this is empty. </p>
<p> Definition at line 73 of file bool_set.</p>
<h3>bool std::tr2::bool_set::is_indeterminate () const [inline]</h3>
<p>Return true if this is indeterminate. </p>
<p> Definition at line 77 of file bool_set.</p>
<h3>bool std::tr2::bool_set::is_singleton () const [inline]</h3>
<p>Return true if this is false or true (normal boolean). </p>
<p> Definition at line 81 of file bool_set. </p>
<p> Referenced by operator bool().</p>
<h3>std::tr2::bool_set::operator bool () const [inline]</h3>
<p>Conversion to bool. </p>
<p> Definition at line 86 of file bool_set. </p>
<p> References is_singleton().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libstdc++ from the source code.</p>
