---
title: "stdvariant_alternativestdvariant_alternative_t(3)"
name: "stdvariant_alternativestdvariant_alternative_t"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdvariant_alternativestdvariant_alternative_t/"
---

std::variant_alternative,std::variant_alternative_t - std::variant_alternative,std::variant_alternative_t

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;variant&gt;

    template &lt;std::size_t I, class T&gt;
    (1)(since C++ 17)

        struct variant_alternative; /* undefined */

template &lt;size_t I, class... Types&gt;
(2)(since C++ 17)

    struct variant_alternative&lt;I, variant&lt;Types...&gt;&gt;;

template &lt;size_t I, class T&gt;
class variant_alternative&lt;I, const T&gt;;

template &lt;size_t I, class T&gt;
class variant_alternative&lt;I, volatile T&gt;;
(3)(since C++ 17)

    template &lt;size_t I, class T&gt;
    class variant_alternative&lt;I, const volatile T&gt;;</code></pre> 
Provides compile-time indexed access to the types of the alternatives of the possibly cv-qualified variant, combining cv-qualifications of the variant (if any) with the cv-qualifications of the alternative. 
Formally, 
2) meets the TransformationTrait requirements with a member typedef type equal to the type of the alternative with index I 
3) meets the TransformationTrait requirements with a member typedef type that names, respectively, std::add_const_t&lt;std::variant_alternative&lt;I,T&gt;&gt;, std::add_volatile_t&lt;std::variant_alternative&lt;I,T&gt;&gt;, and std::add_cv_t&lt;std::variant_alternative&lt;I,T&gt;&gt; 

<h2>Member types</h2>

Member type Definition 
type the type of Ith alternative of the variant, where I must be in [0, sizeof...(Types)), otherwise the program is ill-formed. 

 

 
Helper template alias 

 

 
template &lt;size_t I, class T&gt; <i>(since C++17)</i> 
using variant_alternative_t = typename variant_alternative&lt;I, T&gt;::type;

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
LWG_2974 C++17 out-of-bounds index resulted in undefined behavior made ill-formed 

<h2>See also</h2>

variant_size obtains the size of the variant's list of alternatives at compile time 
variant_size_v <i>(class template)</i> (variable template) 
<i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains the type of the specified element 
tuple_element <i>(class template specialization)</i> 
