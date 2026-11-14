---
title: "stderror_codeerror_code(3)"
name: "stderror_codeerror_code"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stderror_codeerror_code/"
---

std::error_code::error_code - std::error_code::error_code

<h2>Synopsis</h2>

<pre><code>error_code() noexcept;
(1)(since C++ 11)

    error_code(int ec, const error_category &amp;ecat) noexcept;
(2)(since C++ 11)

    template &lt;class ErrorCodeEnum&gt;
    (3)(since C++ 11)

        error_code(ErrorCodeEnum e) noexcept;</code></pre> 
Constructs new error code. 
1) Constructs error code with default value. Equivalent to error_code(0, std::system_category()). 
2) Constructs error code with ec as the platform-dependent error code and ecat as the corresponding error category. 
3) Constructs error code from an error code enum e. Equivalent to *this = make_error_code(e). The overload participates in overload resolutions only if std::is_error_code_enum&lt;ErrorCodeEnum&gt;::value == true. 

<h2>Parameters</h2>

ec - platform dependent error code to construct with 
ecat - error category corresponding to ec 
e - error code enum to construct with

<h2>See also</h2>

make_error_code(std::errc) constructs an std::errc error code 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
make_error_code(std::io_errc) constructs an iostream error code 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
make_error_code(std::future_errc) constructs a future error code 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
