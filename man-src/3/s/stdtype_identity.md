---
title: "stdtype_identity(3)"
name: "stdtype_identity"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdtype_identity/"
---

std::type_identity - std::type_identity

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;type_traits&gt;

    template &lt;class T&gt;
    (since C++ 20)

        struct type_identity;</code></pre> 
Provides the member typedef type that names T (i.e., the identity transformation). 

<h2>Member types</h2>

Name Definition 
type T

<h2>Helper types</h2>

template&lt; class T &gt; <i>(since C++20)</i> 
using type_identity_t = typename type_identity&lt;T&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template&lt; class T &gt; 
&nbsp;<wbr>&nbsp;struct type_identity { 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;using type = T; 
&nbsp;<wbr>&nbsp;};

<h2>Notes</h2>

type_identity can be used to block template_argument_deduction: <pre><code>template &lt;class T&gt;

void f(T, T);
template &lt;class T&gt;

void g(T, std::type_identity_t&lt;T&gt;);</code></pre> 
&nbsp;<wbr>&nbsp;f(4.2, 0); // error, deduced conflicting types for 'T' 
&nbsp;<wbr>&nbsp;g(4.2, 0); // OK, calls g&lt;double&gt; 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
