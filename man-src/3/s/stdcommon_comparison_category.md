---
title: "stdcommon_comparison_category(3)"
name: "stdcommon_comparison_category"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcommon_comparison_category/"
---

std::common_comparison_category - std::common_comparison_category

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;compare&gt;

    template &lt;class... Ts&gt;

    struct common_comparison_category {
    (since C++ 20)

        using type = /*see below*/;
};</code></pre> 
The class template std::common_comparison_category provides an alias (as the member typedef type) for the strongest comparison category to which all of the template arguments Ts... can be converted. 
In detail, the common comparison type of a list of n types T0...Tn-1 is defined as follows: 
* If any Ti is not a comparison category type (std::weak_equality, std::strong_equality, std::partial_ordering, std::weak_ordering, std::strong_ordering), U is void. 
* Otherwise, if at least one Ti is std::weak_equality or at least one Ti is std::strong_equality and at least one Ti is std::partial_ordering or std::weak_ordering, U is std::weak_equality 
* Otherwise, if at least one Ti is std::strong_equality, U is std::strong_equality 
* Otherwise, (if there is no std::weak_equality and no std::strong_equality) if at least one Ti is std::partial_ordering, U is std::partial_ordering 
* Otherwise, if at least one Ti is std::weak_ordering, U is std::weak_ordering 
* Otherwise (if every Ti is std::strong_ordering, or if the list is empty), U is std::strong_ordering. 

<h2>Template parameters</h2>

...Ts - a possibly empty list of types 

 

 
Helper template 

 

 
template&lt; class... Ts &gt; <i>(since C++20)</i> 
using common_comparison_category_t = typename common_comparison_category&lt;Ts...&gt;::type;

<h2>Member types</h2>

Member type Definition 
type the strongest common comparison category (as defined above)

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

strong_ordering the result type of 3-way comparison that supports all 6 operators and is substitutable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
weak_ordering the result type of 3-way comparison that supports all 6 operators and is not substitutable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
partial_ordering the result type of 3-way comparison that supports all 6 operators, is not substitutable, and allows incomparable values 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
strong_equality the result type of 3-way comparison that supports only equality/inequality and is substitutable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
weak_equality the result type of 3-way comparison that supports only equality/inequality and is not substitutable 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class)</i> 
(C++20) 
