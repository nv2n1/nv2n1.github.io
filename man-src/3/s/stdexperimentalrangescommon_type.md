---
title: "stdexperimentalrangescommon_type(3)"
name: "stdexperimentalrangescommon_type"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangescommon_type/"
---

std::experimental::ranges::common_type - std::experimental::ranges::common_type

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / type_traits&gt;

    template &lt;class... T&gt;
    (ranges TS)

        struct common_type;</code></pre> 
Determines the common type among all types T..., that is the type all T... can be implicitly converted to. If such a type exists (as determined according to the rules below), the member type names that type. Otherwise, there is no member type. The behavior is undefined if any of the types in T... is an incomplete type other than (possibly cv-qualified) void. 
* If sizeof...(T) is zero, there is no member type. 
* If sizeof...(T) is one (i.e., T... contains only one type T0), the member type names the same type as std::decay_t&lt;T0&gt;. 
* If sizeof...(T) is two (i.e., T... contains exactly two types T1 and T2), 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If applying std::decay to at least one of T1 and T2 produces a different type, the member type names the same type as ranges::common_type_t&lt;std::decay_t&lt;T1&gt;, std::decay_t&lt;T2&gt;&gt;, if it exists; if not, there is no member type. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, (and unless there is a user specialization for ranges::common_type&lt;T1, T2&gt;), if std::common_type_t&lt;T1, T2&gt; is well-formed, then the member type denotes that type; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* Otherwise, the member type denotes the type std::decay_t&lt;decltype(false ? std::declval&lt;const T1&amp;&gt;() : std::declval&lt;const T2&amp;&gt;())&gt;, if that conditional expression is well-formed; if not, there is no member type. 
* If sizeof...(T) is greater than two (i.e., T... consists of the types T1, T2, R...), then if ranges::common_type_t&lt;T1, T2&gt; exists, the member type denotes ranges::common_type_t&lt;ranges::common_type_t&lt;T1, T2&gt;, R...&gt; if such a type exists. In all other cases, there is no member type. 

<h2>Member types</h2>

Name Definition 
type the common type for all T...

<h2>Helper types</h2>

template&lt; class... T &gt; 
using common_type_t = typename common_type&lt;T...&gt;::type;

<h2>Specializations</h2>

Users may specialize common_type for types T1 and T2 if 

 
* At least one of T1 and T2 depends on a user-defined type, and 
* std::decay is an identity transformation for both T1 and T2. 

 
If such a specialization has a member named type, it must be a public and unambiguous member type that names a cv-unqualified non-reference type to which both T1 and T2 are explicitly convertible. Additionally, ranges::common_type_t&lt;T1, T2&gt; and ranges::common_type_t&lt;T2, T1&gt; must denote the same type. 
A program that adds common_type specializations in violation of these rules has undefined behavior.

<h2>Notes</h2>

For arithmetic types not subject to promotion, the common type may be viewed as the type of the (possibly mixed-mode) arithmetic expression such as T0() + T1() + ... + Tn(). 

<h2>Examples</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

common_type determines the common type of a group of types 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determine the common reference type of a set of types 
common_reference <i>(class template)</i> 
