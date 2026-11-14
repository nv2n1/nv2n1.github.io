---
title: "stderror_conditionoperator(3)"
name: "stderror_conditionoperator"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_conditionoperator/"
---

std::error_condition::operator= - std::error_condition::operator=

<h2>Synopsis</h2>

<pre><code>error_condition &amp;operator=(const error_condition &amp;other) noexcept;
(1)(since C++ 11)(implicitly declared)

    template &lt;class ErrorConditionEnum&gt;
    (2)(since C++ 11)

        error_condition &amp;
        operator=(ErrorConditionEnum e) noexcept;</code></pre> 
Assigns contents to an error condition. 
1) Copy assignment operator. Assigns the contents of other. 
2) Assigns error condition for enum e. Effectively calls make_error_condition(). Does not participate in the overload resolution unless is_error_condition_enum&lt;ErrorConditionEnum&gt;::value is true. 

<h2>Parameters</h2>

other - another error condition to initialize with 
e - error condition enum

<h2>Return value</h2>

*this. 
