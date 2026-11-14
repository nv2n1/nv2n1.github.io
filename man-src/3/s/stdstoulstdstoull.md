---
title: "stdstoulstdstoull(3)"
name: "stdstoulstdstoull"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstoulstdstoull/"
description: "std::stoul,std::stoull – std::stoul,std::stoull"
---

<p>std::stoul,std::stoull &#8211; std::stoul,std::stoull</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;string&gt;

    unsigned long stoul(const std::string &amp;str, std::size_t *pos = 0, int base = 10);
(1)(since C++ 11)

    unsigned long stoul(const std::wstring &amp;str, std::size_t *pos = 0, int base = 10);

unsigned long long stoull(const std::string &amp;str, std::size_t *pos = 0, int base = 10);
(2)(since C++ 11)

    unsigned long long stoull(const std::wstring &amp;str, std::size_t *pos = 0, int base = 10);
Interprets an unsigned integer value in the string str.

1) calls std::strtoul(str.c_str(), &amp;ptr, base) or std::wcstoul(str.c_str(), &amp;ptr, base)

2) calls std::strtoull(str.c_str(), &amp;ptr, base) or std::wcstoull(str.c_str(), &amp;ptr, base)

Discards any whitespace characters (as identified by calling isspace()) until the first non-whitespace character is found, then takes as many characters as possible to form a valid base-n (where n=base) unsigned integer number representation and converts them to an integer value. The valid unsigned integer value consists of the following parts:</code></pre>
<p>* (optional) plus or minus sign<br />
* (optional) prefix <code>(0)</code> indicating octal base (applies only when the base is 8 or 0)<br />
* (optional) prefix (0x or 0X) indicating hexadecimal base (applies only when the base is 16 or 0)<br />
* a sequence of digits<br />
The set of valid values for base is {0,2,3,&#8230;,36}. The set of valid digits for base-2 integers is {0,1}, for base-3 integers is {0,1,2}, and so on. For bases larger than 10, valid digits include alphabetic characters, starting from Aa for base-11 integer, to Zz for base-36 integer. The case of the characters is ignored.<br />
Additional numeric formats may be accepted by the currently installed C locale.<br />
If the value of base is 0, the numeric base is auto-detected: if the prefix is 0, the base is octal, if the prefix is 0x or 0X, the base is hexadecimal, otherwise the base is decimal.<br />
If the minus sign was part of the input sequence, the numeric value calculated from the sequence of digits is negated as if by unary_minus in the result type, which applies unsigned integer wraparound rules.<br />
If pos is not a null pointer, then a pointer ptr, internal to the conversion functions, will receive the address of the first unconverted character in str.c_str(), and the index of that character will be calculated and stored in *pos, giving the number of characters that were processed by the conversion. </p>
<h2>Parameters</h2>
<p>str &#8211; the string to convert<br />
pos &#8211; address of an integer to store the number of characters processed<br />
base &#8211; the number base</p>
<h2>Return value</h2>
<p>The string converted to the specified unsigned integer type. </p>
<h2>Exceptions</h2>
<p>* std::invalid_argument if no conversion could be performed<br />
* std::out_of_range if the converted value would fall out of the range of the result type or if the underlying function (std::strtoul or std::strtoull) sets errno to ERANGE.</p>
<h2>See also</h2>
<p>stoi<br />
stol<br />
stoll converts a string to a signed integer<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
stof<br />
stod<br />
stold converts a string to a floating point value<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i><br />
<i>(C++11)</i> </p>
