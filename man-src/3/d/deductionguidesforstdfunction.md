---
title: "deductionguidesforstdfunction(3)"
name: "deductionguidesforstdfunction"
section: "3"
letter: "d"
url: "/docs/linux/man/3-deductionguidesforstdfunction/"
description: "deductionguidesforstd::function – deductionguidesforstd::function"
---

<p>deductionguidesforstd::function &#8211; deductionguidesforstd::function</p>
<h2>Synopsis</h2>
<p>Defined in header &lt;functional&gt;<br />
template&lt;class R, class&#8230; ArgTypes&gt; <code>(1)</code> <i>(since C++17)</i><br />
function(R(*)(ArgTypes&#8230;)) -&gt; function&lt;R(ArgTypes&#8230;)&gt;;<br />
template&lt;class F&gt; <code>(2)</code> <i>(since C++17)</i><br />
function(F) -&gt; function&lt;/*see below*/&gt;; </p>
<p>1) This deduction_guide is provided for std::function to allow deduction from functions.<br />
2) If decltype(&amp;F::operator()) is of the form R(G::*)(A&#8230;) (optionally cv-qualified, optionally noexcept, optionally lvalue reference qualified) for some class type G, then the deduced type is std::function&lt;R(A&#8230;)&gt;. This overload only participates in overload resolution if &amp;F::operator() is well-formed when treated as an unevaluated operand. </p>
<h2>Notes</h2>
<p>The type deduced by these deduction guides may change in a later standard revision (in particular, this might happen if noexcept support is added to std::function in a later standard). </p>
<h2>Example</h2>
<p>// Run this code </p>
<p>&nbsp;<wbr>&nbsp;#include &lt;functional&gt;<br />
&nbsp;<wbr>&nbsp;int func(double) { return 0; }<br />
&nbsp;<wbr>&nbsp;int main() {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::function f{func}; // guide #1 deduces function&lt;int(double)&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int i = 5;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;std::function g = [&amp;](double) { return i; }; // guide #2 deduces function&lt;int(double)&gt;<br />
&nbsp;<wbr>&nbsp;}</p>
