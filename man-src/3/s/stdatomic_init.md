---
title: "stdatomic_init(3)"
name: "stdatomic_init"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_init/"
---

std::atomic_init - std::atomic_init

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;atomic&gt;

    template &lt;class T&gt;

    void atomic_init(std::atomic&lt;T&gt; *obj, (since C++ 11)

                                              typename std::atomic&lt;T&gt;::value_type desired) noexcept;

template &lt;class T&gt;

void atomic_init(volatile std::atomic&lt;T&gt; *obj, (since C++ 11)

                                                   typename std::atomic&lt;T&gt;::value_type desired) noexcept;</code></pre> 
Initializes the default-constructed atomic object obj with the value desired. The function is not atomic: concurrent access from another thread, even through an atomic operation, is a data race. 
If obj was not default-constructed, the behavior is undefined. 
If this function is called twice on the same obj, the behavior is undefined. 

<h2>Parameters</h2>

obj - pointer to an atomic object to initialize 
desired - the value to initialize atomic object with

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

This function is provided for compatibility with C. If the compatibility is not required, std::atomic may be initialized through their non-default constructors. 

<h2>Example</h2>

&nbsp;This section is incomplete 
&nbsp;Reason: no example 
Defect reports 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 
DR Applied to Behavior as published Correct behavior 
P0558R1 C++11 exact type match required because T is deduced from multiple arguments T is deduced from the atomic argument only 

<h2>See also</h2>

ATOMIC_VAR_INIT constant initialization of an atomic variable of static storage duration 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function macro)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs an atomic object 
constructor <i>(public member function of std::atomic&lt;T&gt;)</i> 
