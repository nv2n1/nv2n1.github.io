---
title: "deductionguidesforstdreference_wrapper(3)"
name: "deductionguidesforstdreference_wrapper"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdreference_wrapper/"
---

deductionguidesforstd::reference_wrapper - deductionguidesforstd::reference_wrapper
<h2>Synopsis</h2>Defined in header &lt;functional&gt; 
template&lt;typename T&gt; <i>(since C++17)</i> 
reference_wrapper(T&amp;) -&gt; reference_wrapper&lt;T&gt;; 

 
One deduction_guide is provided for std::reference_wrapper to support deduction of the sole class template parameter. 

<h2>Example</h2>&nbsp;This section is incomplete 
&nbsp;Reason: no example 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2981 C++17 a redundant deduction guide from reference_wrapper&lt;T&gt; was provided removed 
LWG_2993 C++17 defect resolution removed a constructor used for class template argument deduction added deduction guide to compensate
