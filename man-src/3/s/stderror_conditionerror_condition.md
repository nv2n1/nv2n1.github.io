---
title: "stderror_conditionerror_condition(3)"
name: "stderror_conditionerror_condition"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_conditionerror_condition/"
---

std::error_condition::error_condition - std::error_condition::error_condition

<h2>Synopsis</h2>

<pre><code>error_condition() noexcept;
(1)(since C++ 11)

    error_condition(const error_condition &amp;other) noexcept;
(2)(since C++ 11)(implicitly declared)

    error_condition(int val, const error_category &amp;cat) noexcept;
(3)(since C++ 11)

    template &lt;class ErrorConditionEnum&gt;
    (4)(since C++ 11)

        error_condition(ErrorConditionEnum e) noexcept;</code></pre> 
Constructs new error condition. 
1) Default constructor. Initializes the error condition with generic category and error code 0. 
2) Copy constructor. Initializes the error condition with the contents of other. 
3) Initializes the error condition with error code val and error category cat. 
4) Initializes the error condition with enum e. Effectively calls make_error_condition(). Does not participate in the overload resolution unless is_error_condition_enum&lt;ErrorConditionEnum&gt;::value is true. 

<h2>Parameters</h2>

other - another error condition to initialize with 
val - error code 
cat - error category 
e - error condition enum

<h2>See also</h2>

make_error_condition(std::errc) constructs an std::errc error condition 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
make_error_condition(std::io_errc) constructs an iostream error_condition 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
make_error_condition(std::future_errc) constructs a future error_condition 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
