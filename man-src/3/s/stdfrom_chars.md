---
title: "stdfrom_chars(3)"
name: "stdfrom_chars"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfrom_chars/"
---

std::from_chars - std::from_chars

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;charconv&gt;

    std::from_chars_result from_chars(const char *first, const char *last, (1)(since C++ 17)

                                                                               /*see below*/
                                                                               &amp; value,
                                      int base = 10);

std::from_chars_result from_chars(const char *first, const char *last, float &amp;value, (2)(since C++ 17)

                                                                                         std::chars_format fmt = std::chars_format::general);

std::from_chars_result from_chars(const char *first, const char *last, double &amp;value, (3)(since C++ 17)

                                                                                          std::chars_format fmt = std::chars_format::general);

std::from_chars_result from_chars(const char *first, const char *last, long double &amp;value, (4)(since C++ 17)

                                                                                               std::chars_format fmt = std::chars_format::general);

struct from_chars_result {

    const char *ptr;
    (5)(since C++ 17)

        std::errc ec;
};</code></pre> 
Analyzes the character sequence [first,last) for a pattern described below. If no characters match the pattern or if the value obtained by parsing the matched characters is not representable in the type of value, value is unmodified, otherwise the characters matching the pattern are interpreted as a text representation of an arithmetic value, which is stored in value. 
1) Integer parsers: Expects the pattern identical to the one used by std::strtol in the default (&quot;C&quot;) locale and the given non-zero numeric base, except that 
* &quot;0x&quot; or &quot;0X&quot; prefixes are not recognized for base 16 
* only the minus sign is recognized (not the plus sign), and only for signed integer types of value. 
The library provides overloads for all signed and unsigned integer types and char as the referenced type of the parameter value. 
2-4) Floating-point parsers: Expects the pattern identical to the one used by std::strtod in the default (&quot;C&quot;) locale, except that 
* the plus sign is not recognized outside of the exponent (only the minus sign is permitted at the beginning) 
* if fmt has std::chars_format::scientific set but not std::chars_format::fixed, the exponent part is required (otherwise it is optional) 
* if fmt has std::chars_format::fixed set but not std::chars_format::scientific, the optional exponent is not permitted 
* if fmt is std::chars_format::hex, the prefix &quot;0x&quot; or &quot;0X&quot; is not permitted (the string &quot;0x123&quot; parses as the value &quot;0&quot; with unparsed remainder &quot;x123&quot;). 
In any case, the resulting value is one of at most two floating-point values closest to the value of the string matching the pattern, after rounding according to std::round_to_nearest. 
5) The return type (see Return value below) 

<h2>Parameters</h2>

first, last - valid character range to parse 
value - the out-parameter where the parsed value is stored if successful 
base - integer base to use: a value between 2 and 36 (inclusive). 
fmt - floating-point formatting to use, a bitmask of type std::chars_format

<h2>Return value</h2>

On success, returns a value of type from_chars_result such that ptr points at the first character not matching the pattern, or has the value equal to last if all characters match and ec is value-initialized. 
If there is no pattern match, returns a value of type from_chars_result such that ptr equals first and ec equals std::errc::invalid_argument. value is unmodified. 
If the pattern was matched, but the parsed value is not in the range representable by the type of value, returns value of type from_chars_result such that ec equals std::errc::result_out_of_range and ptr points at the first character not matching the pattern. value is unmodified. 

<h2>Exceptions</h2>

<i>(none)</i>

<h2>Notes</h2>

Unlike other parsing functions in C++ and C libraries, std::from_chars is locale-independent, non-allocating, and non-throwing. Only a small subset of parsing policies used by other libraries (such as std::sscanf) is provided. This is intended to allow the fastest possible implementation that is useful in common high-throughput contexts such as text-based interchange (JSON or XML). 
The guarantee that std::from_chars can recover every floating-point value formatted by std::to_chars exactly is only provided if both functions are from the same implementation. 
A pattern consisting of a sign with no digits following it is treated as pattern that did not match anything. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;charconv&gt;

#include &lt;array&gt;
int main()

{
    std::array&lt;char, 10&gt; str{&quot;42&quot;};
    int result;
    if (auto [p, ec] = std::from_chars(str.data(), str.data() + str.size(), result);
        ec == std::errc())
        std::cout &lt;&lt; result;
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;42 

 

 
Defect reports 

 
The following behavior-changing defect reports were applied retroactively to previously published C++ standards. 

 
DR Applied to Behavior as published Correct behavior 
LWG_2955 C++17 this function was in &lt;utility&gt; and used std::error_code moved to &lt;charconv&gt; and uses std::errc

<h2>See also</h2>

to_chars converts an integer or floating-point value to a character sequence 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++17)</i> 
stoi 
stol 
stoll converts a string to a signed integer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
stof 
stod 
stold converts a string to a floating point value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;converts a byte string to an integer value 
strtol <i>(function)</i> 
strtoll 
strtof converts a byte string to a floating point value 
strtod <i>(function)</i> 
strtold 
scanf reads formatted input from stdin, a file stream or a buffer 
fscanf <i>(function)</i> 
sscanf 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extracts formatted data 
operator&gt;&gt; <i>(public member function of std::basic_istream&lt;CharT,Traits&gt;)</i> 
