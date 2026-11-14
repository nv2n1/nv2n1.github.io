---
title: "deductionguidesforstdarray(3)"
name: "deductionguidesforstdarray"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdarray/"
---

deductionguidesforstd::array - deductionguidesforstd::array
<h2>Synopsis</h2>Defined in header &lt;array&gt; 
template &lt;class T, class... U&gt; <i>(since C++17)</i> 
array(T, U...) -&gt; array&lt;T, 1 + sizeof...(U)&gt;; 

 
One deduction_guide is provided for std::array to provide an equivalent of std::experimental::make_array for construction of std::array from a variadic parameter pack. 
The program is ill-formed if (std::is_same_v&lt;T, U&gt; &amp;&amp; ...) is not true 

<h2>Example</h2>// Run this code 

 
&nbsp;<wbr>&nbsp;#include &lt;array&gt; 
&nbsp;<wbr>&nbsp;int main() 
&nbsp;<wbr>&nbsp;{ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int const x = 10; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::array a{1, 2, 3, 5, x}; // OK, creates std::array&lt;int, 5&gt; 

 
&nbsp;<wbr>&nbsp;// std::array b{1, 2u}; // Error, all arguments must have same type 
&nbsp;<wbr>&nbsp;}
