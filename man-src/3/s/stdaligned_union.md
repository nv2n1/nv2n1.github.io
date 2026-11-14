---
title: "stdaligned_union(3)"
name: "stdaligned_union"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdaligned_union/"
description: "std::aligned_union – std::aligned_union"
---

<p>std::aligned_union &#8211; std::aligned_union</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;std::size_t Len, class... Types&gt;
    (since C++ 11)

        struct aligned_union;</code></pre>
<p>Provides the nested type type, which is a trivial standard-layout type of a size and alignment suitable for use as uninitialized storage for an object of any of the types listed in Types. The size of the storage is at least Len. std::aligned_union also determines the strictest (largest) alignment requirement among all Types and makes it available as the constant alignment_value.<br />
If sizeof&#8230;(Types) == 0 or if any of the types in Types is not a complete object type, the behavior is undefined.<br />
It is implementation-defined whether any extended_alignment is supported. </p>
<h2>Member types</h2>
<p>Name Definition<br />
type the trivial type suitable for storage of any type from Types</p>
<h2>Helper types</h2>
<p>template&lt; std::size_t Len, class&#8230; Types &gt; <i>(since C++14)</i><br />
using aligned_union_t = typename aligned_union&lt;Len,Types&#8230;&gt;::type;</p>
<h2>Member constants</h2>
<p>alignment_value the strictest alignment requirement of all Types<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Possible implementation</h2>
<p>&nbsp;<wbr>&nbsp;#include &lt;algorithm&gt;<br />
&nbsp;<wbr>&nbsp;template &lt;std::size_t Len, class&#8230; Types&gt;<br />
&nbsp;<wbr>&nbsp;struct aligned_union<br />
&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;static constexpr std::size_t alignment_value = std::max({alignof(Types)&#8230;}); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct type<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;alignas(alignment_value) char _s[std::max({Len, sizeof(Types)&#8230;})];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;};<br />
&nbsp;<wbr>&nbsp;};</p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example<br />
Defect reports<br />
The following behavior-changing defect reports were applied retroactively to previously published C++ standards.<br />
DR Applied to Behavior as published Correct behavior<br />
LWG_2979 C++11 complete type wasn&#8217;t required requires complete types </p>
<h2>See also</h2>
<p>alignment_of obtains the type&#8217;s alignment requirements<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i><br />
aligned_storage defines the type suitable for use as uninitialized storage for types of given size<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i><br />
<i>(C++11)</i> </p>
