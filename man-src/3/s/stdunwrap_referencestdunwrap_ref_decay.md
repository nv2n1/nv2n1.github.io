---
title: "stdunwrap_referencestdunwrap_ref_decay(3)"
name: "stdunwrap_referencestdunwrap_ref_decay"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdunwrap_referencestdunwrap_ref_decay/"
---

std::unwrap_reference,std::unwrap_ref_decay - std::unwrap_reference,std::unwrap_ref_decay

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;functional&gt;

    template &lt;class T&gt;
    (1)(since C++ 20)

        struct unwrap_reference;

template &lt;class T&gt;
(2)(since C++ 20)

    struct unwrap_ref_decay : std::unwrap_reference&lt;std::decay_t&lt;T&gt;&gt; {
};</code></pre> 
1) If T is std::reference_wrapper&lt;U&gt; for some type U, provides a member typedef type that names U&amp;; otherwise, provides a member typedef type that names T. 
2) If T is std::reference_wrapper&lt;U&gt; for some type U, ignoring cv-qualification and referenceness, provides a member typedef type that names U&amp;; otherwise, provides a member typedef type that names std::decay_t&lt;T&gt;. 

<h2>Member types</h2>

Name Definition 
type 1) U&amp; if T is std::reference_wrapper&lt;U&gt;; T otherwise 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;2) U&amp; if std::decay_t&lt;T&gt; is std::reference_wrapper&lt;U&gt;; std::decay_t&lt;T&gt; otherwise

<h2>Helper types</h2>

template&lt;class T&gt; <i>(since C++20)</i> 
using unwrap_ref_decay_t = typename unwrap_ref_decay&lt;T&gt;::type;

<h2>Possible implementation</h2>

&nbsp;<wbr>&nbsp;template &lt;class T&gt; 
&nbsp;<wbr>&nbsp;struct unwrap_reference { using type = T; }; 
&nbsp;<wbr>&nbsp;template &lt;class U&gt; 
&nbsp;<wbr>&nbsp;struct unwrap_reference&lt;std::reference_wrapper&lt;U&gt;&gt; { using type = U&amp;; };

<h2>Notes</h2>

std::unwrap_ref_decay performs the same transformation as used by std::make_pair and std::make_tuple. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 

<h2>See also</h2>

reference_wrapper CopyConstructible and CopyAssignable reference wrapper 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(class template)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a pair object of type, defined by the argument types 
make_pair <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a tuple object of the type defined by the argument types 
make_tuple <i>(function template)</i> 
