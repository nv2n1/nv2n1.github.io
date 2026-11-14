---
title: "stdequal_tonot_equal_tolessgreaterless_equalgreater_equalstdexperimentalpropagate_const(3)"
name: "stdequal_tonot_equal_tolessgreaterless_equalgreater_equalstdexperimentalpropagate_const"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdequal_tonot_equal_tolessgreaterless_equalgreater_equalstdexperimentalpropagate_const/"
---

std::equal_to,not_equal_to,less,greater,less_equal,greater_equal(std::experimental::propagate_const) - std::equal_to,not_equal_to,less,greater,less_equal,greater_equal(std::experimental::propagate_const)

<h2>Synopsis</h2>

Defined in header &lt;experimental/propagate_const&gt; 
template&lt;class T&gt; struct equal_to&lt;std::experimental::propagate_const&lt;T&gt;&gt;; (library fundamentals TS v2) 
template&lt;class T&gt; struct not_equal_to&lt;std::experimental::propagate_const&lt;T&gt;&gt;; (library fundamentals TS v2) 
template&lt;class T&gt; struct less&lt;std::experimental::propagate_const&lt;T&gt;&gt;; (library fundamentals TS v2) 
template&lt;class T&gt; struct greater&lt;std::experimental::propagate_const&lt;T&gt;&gt;; (library fundamentals TS v2) 
template&lt;class T&gt; struct less_equal&lt;std::experimental::propagate_const&lt;T&gt;&gt;; (library fundamentals TS v2) 
template&lt;class T&gt; struct greater_equal&lt;std::experimental::propagate_const&lt;T&gt;&gt;; (library fundamentals TS v2) 
The standard comparison function objects are partially specialized for std::experimental::propagate_const&lt;T&gt;. 
Let p.t_ denote the pointer-like object wrapped by a std::experimental::propagate_const&lt;T&gt; p, then given objects p and q of type std::experimental::propagate_const&lt;T&gt;, the following shall hold: 
* std::equal_to&lt;std::experimental::propagate_const&lt;T&gt;&gt;()(p, q) == std::equal_to&lt;T&gt;()(p.t_, q.t_) 
* std::not_equal_to&lt;std::experimental::propagate_const&lt;T&gt;&gt;()(p, q) == std::not_equal_to&lt;T&gt;()(p.t_, q.t_) 
* std::less&lt;std::experimental::propagate_const&lt;T&gt;&gt;()(p, q) == std::less&lt;T&gt;()(p.t_, q.t_) 
* std::greater&lt;std::experimental::propagate_const&lt;T&gt;&gt;()(p, q) == std::greater&lt;T&gt;()(p.t_, q.t_) 
* std::less_equal&lt;std::experimental::propagate_const&lt;T&gt;&gt;()(p, q) == std::less_equal&lt;T&gt;()(p.t_, q.t_) 
* std::greater_equal&lt;std::experimental::propagate_const&lt;T&gt;&gt;()(p, q) == std::greater_equal&lt;T&gt;()(p.t_, q.t_) 

<h2>Notes</h2>

These specializations ensure that when T is a pointer type, specializations of these class templates for std::experimental::propagate_const&lt;T&gt; yield a total order, even if the corresponding built-in operators do not. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x == y 
equal_to <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x != y 
not_equal_to <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x &lt; y 
less <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x &gt; y 
greater <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x &lt;= y 
less_equal <i>(class template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;function object implementing x &gt;= y 
greater_equal <i>(class template)</i> 
