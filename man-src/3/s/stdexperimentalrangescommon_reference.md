---
title: "stdexperimentalrangescommon_reference(3)"
name: "stdexperimentalrangescommon_reference"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangescommon_reference/"
---

std::experimental::ranges::common_reference - std::experimental::ranges::common_reference

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / type_traits&gt;

    template &lt;class... T&gt;
    (ranges TS)

        struct common_reference;</code></pre> 
Determines the common reference type of the types T..., that is, the type to which all the types in T... can be converted or bound. If such a type exists (as determined according to the rules below), the member type names that type. Otherwise, there is no member type. The behavior is undefined if any of the types in T... is an incomplete type other than (possibly cv-qualified) void. 
When given reference types, common_reference attempts to find a reference type to which the supplied reference types can all be bound, but may return a non-reference type if it cannot find such a reference type. 
* If sizeof...(T) is zero, there is no member type. 
* If sizeof...(T) is one (i.e., T... contains only one type T0), the member type names the same type as T0. 
* If sizeof...(T) is two (i.e., T... contains two types T1 and T2): 
&nbsp;<wbr>&nbsp;o If T1 and T2 are both reference types, and the simple common reference type S of T1 and T2 (as defined below) exists, then the member type type names S; 
&nbsp;<wbr>&nbsp;o Otherwise, if basic_common_reference&lt;T1R, T2R, T1Q, T2Q&gt;::type exists, where TiR is std::remove_cv_t&lt;std::remove_reference_t&lt;Ti&gt;&gt; and TiQ is an alias template such that TiQ&lt;TiR&gt; is Ti, then the member type type names that type; 
&nbsp;<wbr>&nbsp;o Otherwise, if decltype(false? val&lt;T1&gt;() : val&lt;T2&gt;()), where val is a function template template&lt;class T&gt; T val();, denotes a valid type, then the member type type names that type; 
&nbsp;<wbr>&nbsp;o Otherwise, if ranges::common_type_t&lt;T1, T2&gt; is a valid type, then the member type type names that type; 
&nbsp;<wbr>&nbsp;o Otherwise, there is no member type. 
* If sizeof...(T) is greater than two (i.e., T... consists of the types T1, T2, R...), then if ranges::common_reference_t&lt;T1, T2&gt; exists, the member type denotes ranges::common_reference_t&lt;ranges::common_reference_t&lt;T1, T2&gt;, R...&gt; if such a type exists. In all other cases, there is no member type. 
The simple common reference type of two reference types T1 and T2 is defined as follows: 
* If T1 is cv1 X &amp; and T2 is cv2 Y &amp; (i.e., both are lvalue reference types): their simple common reference type is decltype(false? std::declval&lt;cv12 X &amp;&gt;() : std::declval&lt;cv12 Y &amp;&gt;()), where cv12 is the union of cv1 and cv2, if that type exists and is a reference type; 
* If T1 and T2 are both rvalue reference types: if the simple common reference type of T1 &amp; and T2 &amp; (determined according to the previous bullet) exists, then let C denote that type's corresponding rvalue reference type. If std::is_convertible&lt;T1, C&gt;::value and std::is_convertible&lt;T2, C&gt;::value are both true, then the simple common reference type of T1 and T2 is C. 
* Otherwise, one of the two types must be an lvalue reference type A &amp; and the other must be an rvalue reference type B &amp;&amp; (A and B might be cv-qualified). Let D denote the simple common reference type of A &amp; and B const &amp;, if any. If D exists and std::is_convertible&lt;B &amp;&amp;, D&gt;::value is true, then the simple common reference type is D. 
* Otherwise, there's no simple common reference type. 

<h2>Member types</h2>

Name Definition 
type the common reference type for all T...

<h2>Helper types</h2>

template&lt; class... T &gt; 
using common_reference_t = typename common_reference&lt;T...&gt;::type; 
template&lt; class T, class U, template&lt;class&gt; class TQual, template&lt;class&gt; class UQual &gt; 
struct basic_common_reference { }; 

 
The class template basic_common_reference is a customization point that allows users to influence the result of common_reference for user-defined types (typically proxy references). The primary template is empty.

<h2>Specializations</h2>

A program may specialize basic_common_reference&lt;T, U, TQual, UQual&gt; on the first two parameters T and U if std::is_same&lt;T, std::decay_t&lt;T&gt;&gt; and std::is_same&lt;U, std::decay_t&lt;U&gt;&gt; are both true and at least one of them depends on a program-defined type. 
If such a specialization has a member named type, it must be a public and unambiguous member type that names a type to which both TQual&lt;T&gt; and UQual&lt;U&gt; are convertible. Additionally, ranges::basic_common_reference&lt;T, U, TQual, UQual&gt;::type and ranges::basic_common_reference&lt;U, T, UQual, TQual&gt;::type must denote the same type. 
A program may not specialize basic_common_reference on the third or fourth parameters, nor may it specialize common_reference itself. A program that adds specializations in violation of these rules has undefined behavior.

<h2>Notes</h2>

&nbsp;This section is incomplete 

<h2>Examples</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

common_type determines the common type of a group of types 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;determine the common type of a set of types 
common_type <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifies that two types share a common reference type 
CommonReference (concept) 
