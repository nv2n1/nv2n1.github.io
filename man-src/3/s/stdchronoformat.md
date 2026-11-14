---
title: "stdchronoformat(3)"
name: "stdchronoformat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoformat/"
---

std::chrono::format - std::chrono::format

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Streamable&gt;
(1)(since C++ 20)

    std::basic_string&lt;CharT&gt; format(const CharT *fmt, const Streamable &amp;s);

template &lt;class CharT, class Streamable&gt;
(2)(since C++ 20)

    std::basic_string&lt;CharT&gt; format(const std::locale &amp;loc, const CharT *fmt, const Streamable &amp;s);

template &lt;class CharT, class Traits, class Alloc, class Streamable&gt;

std::basic_string&lt;CharT, Traits, Alloc&gt; format(const std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;fmt, (3)(since C++ 20)

                                                                                                       const Streamable &amp;s);

template &lt;class CharT, class Traits, class Alloc, class Streamable&gt;

std::basic_string&lt;CharT, Traits, Alloc&gt; format(const std::locale &amp;loc, (4)(since C++ 20)

                                                                           const std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;fmt,

                                               const Streamable &amp;s);</code></pre> 
Formats the streamable object s using the format string fmt and the locale loc (if provided). 
These function templates behave as if they <pre><code>*construct a std::basic_ostringstream&lt;CharT, Traits, Alloc&gt; os(where Traits is std::char_traits&lt;CharT&gt; and Alloc is std::allocator&lt;CharT&gt; for (1, 2));

*execute os.exceptions(std::ios_base::failbit | std::ios_base::badbit);

* call os.imbue(loc) (for overloads (2,4) only);

*call to_stream(os, fmt, s)(for (1, 2)) or to_stream(os, fmt.c_str(), s)(for (3, 4)), where to_stream is called unqualified to enable argument - dependent_lookup;

*then return os.str().</code></pre> 
1-2) These overloads only participate in overload resolution if to_stream(std::declval&lt;std::basic_ostream&lt;CharT&gt;&amp;&gt;(), fmt, s) is a valid expression. 
3-4) These overloads only participate in overload resolution if to_stream(std::declval&lt;std::basic_ostringstream&lt;CharT, Traits, Alloc&gt;&amp;&gt;(), fmt.c_str(), s) is a valid expression. 
Format string 
The format string consists of zero or more conversion specifiers and ordinary characters. All ordinary characters, excluding the terminating null character, are written into the output stream without modification. Each unmodified conversion specifier begins with a % character followed by a character that determines the behavior of the specifier. Some conversion specifiers have a modified form in which an E or O modifier character is inserted after the % character. Each conversion specifier is replaced by appropriate characters in the output as described below. 
A character sequence in the format string that begins with a % but does not match one of the format specifiers below is interpreted as ordinary characters. 
The following format specifiers are available: 
Conversion Explanation 
specifier 
%% Writes a literal % character. 
%n Writes a newline character. 
%t Writes a horizontal tab character. 
Year 
%C Writes the year divided by 100 using floored division. If the result is a single decimal digit, it is prefixed with 0. 
%EC The modified command %EC writes the locale's alternative representation of the century. 
%y Writes the last two decimal digits of the year. If the result is a single digit it is prefixed by 0. 
%Y Writes the year as a decimal number. If the result is less than four digits it is left-padded with 0 to four digits. 
Month 
%b Writes the locale's abbreviated month name. 
%h 
%B Writes the locale's full month name. 
%m Writes the month as a decimal number (January is 01). If the result is a single digit, it is prefixed with 0. 
%Om The modified command %Om writes the locale's alternative representation. 
Day 
%d Writes the day of month as a decimal number. If the result is a single decimal digit, it is prefixed with 0. 
%Od The modified command %Od writes the locale's alternative representation. 
%e Writes the day of month as a decimal number. If the result is a single decimal digit, it is prefixed with a space. 
%Oe The modified command %Oe writes the locale's alternative representation. 
Day of the week 
%a Writes the locale's abbreviated weekday name. 
%A Writes the locale's full weekday name. 
%u Writes the ISO weekday as a decimal number (1-7), where Monday is 1. 
%Ou The modified command %Ou writes the locale's alternative representation. 
%w Writes the weekday as a decimal number (0-6), where Sunday is 0. 
%Ow The modified command %Ow writes the locale's alternative representation. 
ISO 8601 week-based year 
In ISO 8601 weeks begin with Monday and the first week of the year must satisfy the following requirements: 
* Includes January 4 
* Includes first Thursday of the year 
%g Writes the last two decimal digits of the ISO 8601 week-based year. If the result is a single digit it is prefixed by 0. 
%G Writes the ISO 8601 week-based year as a decimal number. If the result is less than four digits it is left-padded with 0 to four digits. 
%V Writes the ISO 8601 week of the year as a decimal number. If the result is a single digit, it is prefixed with 0. 
%OV The modified command %OV writes the locale's alternative representation. 
Week/day of the year 
%j Writes the day of the year as a decimal number (January 1 is 001). If the result is less than three digits, it is left-padded with 0 to three digits. 
%U Writes the week number of the year as a decimal number. The first Sunday of the year is the first day of week 01. Days of the same year prior to that are in week 00. If the result is a single digit, it is prefixed with 0. 
%OU The modified command %OU writes the locale's alternative representation. 
%W Writes the week number of the year as a decimal number. The first Monday of the year is the first day of week 01. Days of the same year prior to that are in week 00. If the result is a single digit, it is prefixed with 0. 
%OW The modified command %OW writes the locale's alternative representation. 
Date 
%D Equivalent to &quot;%m/%d/%y&quot;. 
%F Equivalent to &quot;%Y-%m-%d&quot;. 
%x Writes the locale's date representation. 
%Ex The modified command %Ex produces the locale's alternate date representation. 
Time of day 
%H Writes the hour (24-hour clock) as a decimal number. If the result is a single digit, it is prefixed with 0. 
%OH The modified command %OH writes the locale's alternative representation. 
%I Writes the hour (12-hour clock) as a decimal number. If the result is a single digit, it is prefixed with 0. 
%OI The modified command %OI writes the locale's alternative representation. 
%M Writes the minute as a decimal number. If the result is a single digit, it is prefixed with 0. 
%OM The modified command %OM writes the locale's alternative representation. 
%S Writes the second as a decimal number. If the number of seconds is less than 10, the result is prefixed with 0. 
%OS If the precision of the input cannot be exactly represented with seconds, then the format is a decimal floating point number with a fixed format and a precision matching that of the precision of the input (or to a microseconds precision if the conversion to floating point decimal seconds cannot be made within 18 fractional digits). The character for the decimal point is localized according to the locale. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The modified command %OS writes the locale's alternative representation. 
%p Writes the locale's equivalent of the AM/PM designations associated with a 12-hour clock. 
%R Equivalent to &quot;%H:%M&quot;. 
%T Equivalent to &quot;%H:%M:%S&quot;. 
%r Writes the locale's 12-hour clock time. 
%X Writes the locale's time representation. 
%EX The modified command %EX writes the locale's alternate time representation.

<h2>Miscellaneous</h2>

%c Writes the locale's date and time representation. 
%Ec The modified command %Ec writes the locale's alternative date and time representation. 
%z Writes the offset from UTC in the ISO 8601 format. For example -0430 refers to 4 hours 30 minutes behind UTC. If the offset is zero, +0000 is used. 
%Ez The modified commands %Ez and %Oz insert a : between the hours and minutes (e.g., -04:30). 
%Oz 
%Z Writes the time zone abbreviation.

<h2>See also</h2>

to_stream_(std::chrono::sys_time) outputs a sys_time into a stream according to the provided format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
to_stream_(std::chrono::utc_time) outputs a utc_time into a stream according to the provided format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
to_stream_(std::chrono::tai_time) outputs a tai_time into a stream according to the provided format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
to_stream_(std::chrono::gps_time) outputs a gps_time into a stream according to the provided format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
to_stream_(std::chrono::file_time) outputs a file_time into a stream according to the provided format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
to_stream_(std::chrono::local_time) outputs a local_time into a stream according to the provided format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a year into a stream according to the provided format 
to_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a month into a stream according to the provided format 
to_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a day into a stream according to the provided format 
to_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a weekday into a stream according to the provided format 
to_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a month_day into a stream according to the provided format 
to_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a year_month into a stream according to the provided format 
to_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a year_month_day into a stream according to the provided format 
to_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;outputs a zoned_time into a stream according to the provided format 
to_stream <i>(function template)</i> 
