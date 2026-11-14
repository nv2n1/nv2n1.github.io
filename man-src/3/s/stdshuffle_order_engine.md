---
title: "stdshuffle_order_engine(3)"
name: "stdshuffle_order_engine"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdshuffle_order_engine/"
description: "std::shuffle_order_engine<Engine,K>::shuffle_order_engine – std::shuffle_order_engine<Engine,K>::shuffle_order_engine"
---

<p>std::shuffle_order_engine&lt;Engine,K&gt;::shuffle_order_engine &#8211; std::shuffle_order_engine&lt;Engine,K&gt;::shuffle_order_engine</p>
<h2>Synopsis</h2>
<p>shuffle_order_engine(); <code>(1)</code> <i>(since C++11)</i><br />
explicit shuffle_order_engine( result_type s ); <code>(2)</code> <i>(since C++11)</i><br />
template&lt; class Sseq &gt; <code>(3)</code> <i>(since C++11)</i><br />
explicit shuffle_order_engine( Sseq&amp; seq );<br />
explicit shuffle_order_engine( const Engine&amp; e ); <code>(4)</code> <i>(since C++11)</i><br />
explicit shuffle_order_engine( Engine&amp;&amp; e ); <code>(5)</code> <i>(since C++11)</i><br />
Constructs new pseudo-random engine adaptor.<br />
1) Default constructor. The underlying engine is also default-constructed.<br />
2) Constructs the underlying engine with s.<br />
3) Constructs the underlying engine with seed sequence seq. This constructor only participate in overload resolution if Sseq qualifies as a SeedSequence. In particular, this constructor does not participate in overload resolution if Sseq is implicitly convertible to result_type.<br />
4) Constructs the underlying engine with a copy of e.<br />
5) Move-constructs the underlying engine with e. e holds unspecified, but valid state afterwards. </p>
<h2>Parameters</h2>
<p>s &#8211; integer value to construct the underlying engine with<br />
seq &#8211; seed sequence to construct the underlying engine with<br />
e &#8211; pseudo-random number engine to initialize with</p>
