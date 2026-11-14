---
title: "stdchronoparse(3)"
name: "stdchronoparse"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdchronoparse/"
---

std::chrono::parse - std::chrono::parse

<h2>Synopsis</h2>

<pre><code>template &lt;class CharT, class Traits, class Alloc, class Parsable&gt;
(1)(since C++ 20)

    /* unspecified */ parse(const std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;fmt, Parsable &amp;tp);

template &lt;class CharT, class Traits, class Alloc, class Parsable&gt;

/* unspecified */ parse(const std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;fmt, Parsable &amp;tp, (2)(since C++ 20)

                                                                                              std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;abbrev);

template &lt;class CharT, class Traits, class Alloc, class Parsable&gt;

/* unspecified */ parse(const std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;fmt, Parsable &amp;tp, (3)(since C++ 20)

                                                                                              std::chrono::minutes &amp;offset);

template &lt;class CharT, class Traits, class Alloc, class Parsable&gt;

/* unspecified */ parse(const std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;fmt, Parsable &amp;tp, (4)(since C++ 20)

                                                                                              std::basic_string&lt;CharT, Traits, Alloc&gt; &amp;abbrev,

                        std::chrono::minutes &amp;offset);</code></pre> 
Returns an object manip of unspecified type such that, given a std::basic_istream&lt;CharT, Traits&gt; object is, the expression is &gt;&gt; manip calls from_stream (unqualified, to enable argument-dependent_lookup) as follows: 
1) from_stream(is, fmt.c_str(), tp) 
2) from_stream(is, fmt.c_str(), tp, std::addressof(abbrev)) 
3) from_stream(is, fmt.c_str(), tp, nullptr, &amp;offset) 
4) from_stream(is, fmt.c_str(), tp, std::addressof(abbrev), &amp;offset). 
The expression is &gt;&gt; manip is an lvalue of type std::basic_istream&lt;CharT, Traits&gt; with the value is. 
These overloads only participate in overload resolution if the corresponding from_stream expression is well-formed. 
Format string 
The format string consists of zero or more conversion specifiers and ordinary characters. Each ordinary character, excluding whitespace characters and the terminating null character, matches one identical character from the input stream, or causes the function to fail if the next character on the stream does not compare equal. 
Each whitespace character matches zero or more whitespace characters in the input stream. 
Each unmodified conversion specifier begins with a % character followed by a character that determines the behavior of the specifier. Some conversion specifiers have a modified form in which an E or O modifier character is inserted after the % character. Some conversion specifiers have a modified form in which a width parameter given as a positive decimal integer (shown as N below) is inserted after the % character. Each conversion specifier causes the matched characters to be interpreted as parts of date and time types according to the table below. 
A character sequence in the format string that begins with a % but does not match one of the conversion specifiers below is interpreted as ordinary characters. 
If from_stream fails to parse everything specified by the format string, or if insufficient information is parsed to specify a complete result, or if parsing discloses contradictory information, is.setstate(std::ios_base::failbit) is called. 
The following conversion specifiers are available: 
Conversion Explanation 
specifier 
%% Matches a literal % character. 
%n Matches one whitespace character. 
%t Matches zero or one whitespace character. 
Year 
%C 
%NC Parses the century as a decimal number. The width N specifies the maximum number of characters to read. The default width is 2. Leading zeroes are permitted but not required. 
%EC The modified commands %EC and %OC interpret the locale's alternative representation of the century. 
%OC 
%y 
%Ny Parses the last two decimal digits of the year. If the century is not otherwise specified (e.g. with %C), values in the range [69, 99] are presumed to refer to the years 1969 to 1999, and values in the range [00, 68] are presumed to refer to the years 2000 to 2068. The width N specifies the maximum number of characters to read. The default width is 2. Leading zeroes are permitted but not required. 
%Ey The modified commands %Ey and %Oy interpret the locale's alternative representation. 
%Oy 
%Y Parses the year as a decimal number. The width N specifies the maximum number of characters to read. The default width is 4. Leading zeroes are permitted but not required. 
%NY The modified command %EY interprets the locale's alternative representation. 
%EY 
Month 
%b 
%B Parses the locale's full or abbreviated case-insensitive month name. 
%h 
%m Parses the month as a decimal number (January is 1). The width N specifies the maximum number of characters to read. The default width is 2. Leading zeroes are permitted but not required. 
%Nm The modified command %Om interprets the locale's alternative representation. 
%Om 
Day 
%d 
%Nd 
%Ed Parses the day of month as a decimal number. The width N specifies the maximum number of characters to read. The default width is 2. Leading zeroes are permitted but not required. 
%e The modified commands %Ed and %Ee interpret the locale's alternative representation. 
%Ne 
%Ee 
Day of the week 
%a Parses the locale's full or abbreviated case-insensitive weekday name. 
%A 
%u Parses the ISO weekday as a decimal number (1-7), where Monday is 1. The width N specifies the maximum number of characters to read. The default width is 1. Leading zeroes are permitted but not required. 
%Nu The modified command %Ou interprets the locale's alternative representation. 
%Ou 
%w Parses the weekday as a decimal number (0-6), where Sunday is 0. The width N specifies the maximum number of characters to read. The default width is 1. Leading zeroes are permitted but not required. 
%Nw The modified command %Ow interprets the locale's alternative representation. 
%Ow 
ISO 8601 week-based year 
In ISO 8601 weeks begin with Monday and the first week of the year must satisfy the following requirements: 
* Includes January 4 
* Includes first Thursday of the year 
%g Parses the last two decimal digits of the ISO 8601 week-based year. The width N specifies the maximum number of characters to read. The default width is 2. Leading zeroes are permitted but not required. 
%Ng 
%G Parses the ISO 8601 week-based year as a decimal number. The width N specifies the maximum number of characters to read. The default width is 4. Leading zeroes are permitted but not required. 
%NG 
%V Parses the ISO 8601 week of the year as a decimal number. The width N specifies the maximum number of characters to read. The default width is 2. Leading zeroes are permitted but not required. 
%NV 
Week/day of the year 
%j Parses the day of the year as a decimal number (January 1 is 1). The width N specifies the maximum number of characters to read. The default width is 3. Leading zeroes are permitted but not required. 
%Nj 
%U Parses the week number of the year as a decimal number. The first Sunday of the year is the first day of week 01. Days of the same year prior to that are in week 00. The width N specifies the maximum number of characters to read. The default width is 2. Leading zeroes are permitted but not required. 
%NU 
%W Parses the week number of the year as a decimal number. The first Monday of the year is the first day of week 01. Days of the same year prior to that are in week 00. The width N specifies the maximum number of characters to read. The default width is 2. Leading zeroes are permitted but not required. 
%NW 
Date 
%D Equivalent to &quot;%m/%d/%y&quot;. 
%F Equivalent to &quot;%Y-%m-%d&quot;. If the width is specified, it is only applied to the %Y. 
%NF 
%x Parses the locale's date representation. 
%Ex The modified command %Ex interprets the locale's alternate date representation. 
Time of day 
%H Parses the hour (24-hour clock) as a decimal number. The width N specifies the maximum number of characters to read. The default width is 2. Leading zeroes are permitted but not required. 
%NH The modified command %OH interprets the locale's alternative representation. 
%OH 
%I Parses the hour (12-hour clock) as a decimal number. The width N specifies the maximum number of characters to read. The default width is 2. Leading zeroes are permitted but not required. 
%NI 
%M Parses the minute as a decimal number. The width N specifies the maximum number of characters to read. The default width is 2. Leading zeroes are permitted but not required. 
%NM The modified command %OM interprets the locale's alternative representation. 
%OM 
%S Parses the second as a decimal number. The width N specifies the maximum number of characters to read. The default width is 2. Leading zeroes are permitted but not required. 
%NS The modified command %OS interprets the locale's alternative representation. 
%OS 
%p Parses the locale's equivalent of the AM/PM designations associated with a 12-hour clock. The command %I must precede %p in the format string. 
%R Equivalent to &quot;%H:%M&quot;. 
%T Equivalent to &quot;%H:%M:%S&quot;. 
%r Parses the locale's 12-hour clock time. 
%X Parses the locale's time representation. 
%EX The modified command %EX interprets the locale's alternate time representation.

<h2>Miscellaneous</h2>

%c Parses the locale's date and time representation. 
%Ec The modified command %Ec interprets the locale's alternative date and time representation. 
%z Parses the offset from UTC in the format [+|-]hh[mm]. For example -0430 refers to 4 hours 30 minutes behind UTC and 04 refers to 4 hours ahead of UTC. 
%Ez The modified commands %Ez and %Oz parses the format [+|-]h[h][:mm] (i.e., requiring a : between the hours and minutes and making the leading zero for hour optional). 
%Oz 
%Z Parses the time zone abbreviation or name, taken as the longest sequence of characters that only contains the characters A through Z, a through z, 0 through 9, -, +, _, and /.

<h2>See also</h2>

from_stream_(std::chrono::sys_time) parses a sys_time from a stream according to the provided format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
from_stream_(std::chrono::utc_time) parses a utc_time from a stream according to the provided format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
from_stream_(std::chrono::tai_time) parses a tai_time from a stream according to the provided format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
from_stream_(std::chrono::gps_time) parses a gps_time from a stream according to the provided format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
from_stream_(std::chrono::file_time) parses a file_time from a stream according to the provided format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
from_stream_(std::chrono::local_time) parses a local_time from a stream according to the provided format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
(C++20) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses a year from a stream according to the provided format 
from_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses a month from a stream according to the provided format 
from_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses a day from a stream according to the provided format 
from_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses a weekday from a stream according to the provided format 
from_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses a month_day from a stream according to the provided format 
from_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses a year_month from a stream according to the provided format 
from_stream <i>(function template)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses a year_month_day from a stream according to the provided format 
from_stream <i>(function template)</i> 
