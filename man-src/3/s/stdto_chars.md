---
title: "stdto_chars(3)"
name: "stdto_chars"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdto_chars/"
---

std::to_chars - std::to_chars

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;charconv&gt;

    std::to_chars_result to_chars(char *first, char *last, (1)(since C++ 17)

                                  /*see below*/ value,
                                  int base = 10);

std::to_chars_result to_chars(char *first, char *last, float value);

std::to_chars_result to_chars(char *first, char *last, double value);
(2)(since C++ 17)

    std::to_chars_result to_chars(char *first, char *last, long double value);

std::to_chars_result to_chars(char *first, char *last, float value,

                              std::chars_format fmt);

std::to_chars_result to_chars(char *first, char *last, double value, (3)(since C++ 17)

                                                                         std::chars_format fmt);

std::to_chars_result to_chars(char *first, char *last, long double value,

                              std::chars_format fmt);

std::to_chars_result to_chars(char *first, char *last, float value,

                              std::chars_format fmt, int precision);

std::to_chars_result to_chars(char *first, char *last, double value, (4)(since C++ 17)

                                                                         std::chars_format fmt,
                              int precision);

std::to_chars_result to_chars(char *first, char *last, long double value,

                              std::chars_format fmt, int precision);

struct to_chars_result {

    char *ptr;
    (5)(since C++ 17)

        std::errc ec;
};
Converts value into a character string by successively filling the range [first, last), where [first, last) is required to be a valid range.

1) Integer formatters: value is converted to a string of digits in the given base (with no redundant leading zeroes). Digits in the range 10..35 (inclusive) are represented as lowercase characters a..z. If value is less than zero, the representation starts with a minus sign. The library provides overloads for all signed and unsigned integer types and for the type char as the type of the parameter value.

2) value is converted to a string as if by std::printf in the default (&quot;C&quot;) locale. The conversion specifier is f or e (resolving in favor of f in case of a tie), chosen according to the requirement for a shortest representation: the string representation consists of the smallest number of characters such that there is at least one digit before the radix point (if present) and parsing the representation using the corresponding std::from_chars function recovers value exactly. If there are several such representations, one with the smallest difference to value is chosen, resolving any remaining ties using rounding according to std::round_to_nearest

3) same as (2), but the conversion specified for the as-if printf is f if fmt is std::chars_format::fixed, e if fmt is std::chars_format::scientific, a (but without leading &quot;0x&quot; in the result) if fmt is std::chars_format::hex, and g if fmt is chars_format::general.

4) same as (3), except the precision is specified by the parameter precision rather than by the shortest representation requirement.

5) The return type (see Return value below)
</code></pre>

<h2>Parameters</h2>

first, last - character range to write to 
value - the value to convert to its string representation 
base - integer base to use: a value between 2 and 36 (inclusive). 
fmt - floating-point formatting to use, a bitmask of type std::chars_format 
precision - floating-point precision to use

<h2>Return value</h2>

On success, returns a value of type to_chars_result such that ec equals value-initialized std::errc and ptr is the one-past-the-end pointer of the characters written. Note that the string is not NUL-terminated. 
On error, returns a value of type to_chars_result holding std::errc::value_too_large in ec, a copy of the value last in ptr, and leaves the contents of the range [first, last) in unspecified state. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

Unlike other formatting functions in C++ and C libraries, std::to_chars is locale-independent, non-allocating, and non-throwing. Only a small subset of formatting policies used by other libraries (such as std::sprintf) is provided. This is intended to allow the fastest possible implementation that is useful in common high-throughput contexts such as text-based interchange (JSON or XML). 
The guarantee that std::from_chars can recover every floating-point value formatted by to_chars exactly is only provided if both functions are from the same implementation. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;charconv&gt;

#include &lt;system_error&gt;

#include &lt;string_view&gt;

#include &lt;array&gt;
int main()

{
    std::array&lt;char, 10&gt; str;
    if (auto [p, ec] = std::to_chars(str.data(), str.data() + str.size(), 42);
        ec == std::errc())
        std::cout &lt;&lt; std::string_view(str.data(), p - str.data());
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;42 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2955 C++17 this function was in &lt;utility&gt; and used std::error_code moved to &lt;charconv&gt; and uses std::errc

<h2>See also</h2>

from_chars converts a character sequence to an integer or floating-point value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
to_string converts an integral or floating point value to string 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
printf 
fprintf 
sprintf 
snprintf prints formatted output to stdout, a file stream or a buffer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;inserts formatted data 
operator&lt;&lt; <i>(public member function of std::basic_ostream&lt;CharT,Traits&gt;)</i> 
