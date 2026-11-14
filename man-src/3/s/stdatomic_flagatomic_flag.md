---
title: "stdatomic_flagatomic_flag(3)"
name: "stdatomic_flagatomic_flag"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdatomic_flagatomic_flag/"
---

std::atomic_flag::atomic_flag - std::atomic_flag::atomic_flag

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;atomic&gt;

atomic_flag() noexcept;
(1)(since C++ 11)

    atomic_flag(const atomic_flag &amp;) = delete;
(2)(since C++ 11)</code></pre> 
Constructs a new std::atomic_flag. 
1) Trivial default constructor, initializes std::atomic_flag to unspecified state. 
2) The copy constructor is deleted; std::atomic_flag is not copyable. 
In addition, std::atomic_flag can be value-initialized to clear state with the expression ATOMIC_FLAG_INIT. For an atomic_flag with static storage_duration, this guarantees static_initialization: the flag can be used in constructors of static objects. 

<h2>See also</h2>

ATOMIC_FLAG_INIT initializes an std::atomic_flag to false 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(macro constant) 
<i>(C++11)</i> 
