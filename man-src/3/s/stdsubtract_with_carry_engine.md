---
title: "stdsubtract_with_carry_engine(3)"
name: "stdsubtract_with_carry_engine"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdsubtract_with_carry_engine/"
description: "std::subtract_with_carry_engine<UIntType,w,s,r>::subtract_with_carry_engine – std::subtract_with_carry_engine<UIntType,w,s,r>::subtract_with_carry_engine"
---

<p>std::subtract_with_carry_engine&lt;UIntType,w,s,r&gt;::subtract_with_carry_engine &#8211; std::subtract_with_carry_engine&lt;UIntType,w,s,r&gt;::subtract_with_carry_engine</p>
<h2>Synopsis</h2>
<p>subtract_with_carry_engine() : subtract_with_carry_engine(default_seed) {} <code>(1)</code> <i>(since C++11)</i><br />
explicit subtract_with_carry_engine( result_type value ); <code>(2)</code> <i>(since C++11)</i><br />
template&lt; class Sseq &gt; <code>(3)</code> <i>(since C++11)</i><br />
explicit subtract_with_carry_engine( Sseq&amp; s );<br />
subtract_with_carry_engine( const subtract_with_carry_engine&amp; ); <code>(4)</code> <i>(since C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(implicitly declared)<br />
Constructs the pseudo-random number engine.<br />
1) Default constructor. Seeds the engine with default_seed.<br />
&nbsp;This section is incomplete<br />
The overload <code>(3)</code> only participates in overload resolution if Sseq qualifies as a SeedSequence. In particular, it is excluded from the set of candidate functions if Sseq is convertible to result_type. </p>
<h2>Parameters</h2>
<p>value &#8211; seed value to use in the initialization of the internal state<br />
s &#8211; seed sequence to use in the initialization of the internal state</p>
<h2>Complexity</h2>
<p>&nbsp;This section is incomplete </p>
<p>Defect reports </p>
<p>The following behavior-changing defect reports were applied retroactively to previously published C++ standards. </p>
<p>DR Applied to Behavior as published Correct behavior<br />
P0935R0 C++11 default constructor was explicit made implicit</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets the current state of the engine<br />
seed <i>(public member function)</i> </p>
