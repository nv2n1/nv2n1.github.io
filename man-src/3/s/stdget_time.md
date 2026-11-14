---
title: "stdget_time(3)"
name: "stdget_time"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdget_time/"
---

std::get_time - std::get_time

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iomanip&gt;

    template &lt;class CharT&gt;
    (since C++ 11)

    /*unspecified*/ get_time(std::tm *tmb, const CharT *fmt);</code></pre> 
When used in an expression in &gt;&gt; get_time(tmb, fmt), parses the character input as a date/time value according to format string fmt according to the std::time_get facet of the locale currently imbued in the input stream in. The resultant value is stored in a std::tm object pointed to by tmb. 

<h2>Parameters</h2>

tmb - valid pointer to the std::tm object where the result will be stored 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointer to a null-terminated CharT string specifying the conversion format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The format string consists of zero or more conversion specifiers, whitespace characters, and ordinary characters (except %). Each ordinary character is expected to match one character in the input stream in case-insensitive comparison. Each whitespace character matches arbitrary whitespace in the input string. Each conversion specification begins with % character, optionally followed by E or O modifier (ignored if unsupported by the locale), followed by the character that determines the behavior of the specifier. The format specifiers match the POSIX function strptime(): 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Conversion Explanation Writes to fields 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;specifier 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;% matches a literal %. The full conversion specification must be %%. <i>(none)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;t matches any whitespace. <i>(none)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;n matches any whitespace. <i>(none)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Year 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Y parses full year as a 4 digit decimal number, leading zeroes permitted but not required tm_year 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;EY parses year in the alternative representation, e.g.平成23年 (year Heisei 23) which writes 2011 to tm_year in ja_JP locale tm_year 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;y parses last 2 digits of year as a decimal number. Range [69,99] results in values 1969 to 1999, range [00,68] results in 2000-2068 tm_year 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Oy parses last 2 digits of year using the alternative numeric system, e.g. 十一 is parsed as 11 in ja_JP locale tm_year 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Ey parses year as offset from locale's alternative calendar period %EC tm_year 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;C parses the first 2 digits of year as a decimal number (range [00,99]) tm_year 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;EC parses the name of the base year (period) in the locale's alternative representation, e.g. 平成 (Heisei era) in ja_JP tm_year 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Month 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;b parses the month name, either full or abbreviated, e.g. Oct tm_mon 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;h synonym of b tm_mon 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;B synonym of b tm_mon 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;m parses the month as a decimal number (range [01,12]), leading zeroes permitted but not required tm_mon 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Om parses the month using the alternative numeric system, e.g. 十二 parses as 12 in ja_JP locale tm_mon 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Week 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;U parses the week of the year as a decimal number (Sunday is the first day of the week) (range [00,53]), leading zeroes permitted but not required tm_year, tm_wday, tm_yday 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OU parses the week of the year, as by %U, using the alternative numeric system, e.g. 五十二 parses as 52 in ja_JP locale tm_year, tm_wday, tm_yday 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;W parses the week of the year as a decimal number (Monday is the first day of the week) (range [00,53]), leading zeroes permitted but not required tm_year, tm_wday, tm_yday 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OW parses the week of the year, as by %W, using the alternative numeric system, e.g. 五十二 parses as 52 in ja_JP locale tm_year, tm_wday, tm_yday 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Day of the year/month 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;j parses day of the year as a decimal number (range [001,366]), leading zeroes permitted but not required tm_yday 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d parses the day of the month as a decimal number (range [01,31]), leading zeroes permitted but not required tm_mday 
fmt - Od parses the day of the month using the alternative numeric system, e.g 二十七 parses as 27 in ja_JP locale, leading zeroes permitted but not reqtm_mday 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e synonym of d tm_mday 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Oe synonym of Od tm_mday 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Day of the week 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a parses the name of the day of the week, either full or abbreviated, e.g. Fri tm_wday 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;A synonym of a tm_wday 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;w parses weekday as a decimal number, where Sunday is 0 (range [0-6]) tm_wday 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Ow parses weekday as a decimal number, where Sunday is 0, using the alternative numeric system, e.g. 二 parses as 2 in ja_JP locale tm_wday 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Hour, minute, second 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;H parses the hour as a decimal number, 24 hour clock (range [00-23]), leading zeroes permitted but not required tm_hour 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OH parses hour from 24-hour clock using the alternative numeric system, e.g. 十八 parses as 18 in ja_JP locale tm_hour 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;I parses hour as a decimal number, 12 hour clock (range [01,12]), leading zeroes permitted but not required tm_hour 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OI parses hour from 12-hour clock using the alternative numeric system, e.g. 六 reads as 06 in ja_JP locale tm_hour 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;M parses minute as a decimal number (range [00,59]), leading zeroes permitted but not required tm_min 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OM parses minute using the alternative numeric system, e.g. 二十五 parses as 25 in ja_JP locale tm_min 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;S parses second as a decimal number (range [00,60]), leading zeroes permitted but not required tm_sec 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;OS parses second using the alternative numeric system, e.g. 二十四 parses as 24 in ja_JP locale tm_sec

<h2>Other</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;c parses the locale's standard date and time string format, e.g. Sun Oct 17 04:41:13 2010 (locale dependent) all 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Ec parses the locale's alternative date and time string format, e.g. expecting 平成23年 (year Heisei 23) instead of 2011年 (year 2011) in ja_JP lallle 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;x parses the locale's standard date representation all 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Ex parses the locale's alternative date representation, e.g. expecting 平成23年 (year Heisei 23) instead of 2011年 (year 2011) in ja_JP locale all 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;X parses the locale's standard time representation all 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;EX parses the locale's alternative time representation all 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;D equivalent to &quot;%m / %d / %y &quot; tm_mon, tm_mday, tm_year 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;r parses locale's standard 12-hour clock time (in POSIX, &quot;%I : %M : %S %p&quot;) tm_hour, tm_min, tm_sec 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;R equivalent to &quot;%H : %M&quot; tm_hour, tm_min 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;T equivalent to &quot;%H : %M : %S&quot; tm_hour, tm_min, tm_sec 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;p parses the locale's equivalent of a.m. or p.m. tm_hour 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Note: tm_isdst is not written to, and needs to be set explicitly for use with functions such as mktime

<h2>Return value</h2>

Returns an object of unspecified type such that if in is the name of an input stream of type std::basic_istream&lt;CharT, Traits&gt;, then the expression in &gt;&gt; get_time(tmb, fmt) behaves as if the following code was executed :

    typedef std::istreambuf_iterator&lt;CharT, Traits&gt; Iter;

typedef std::time_get&lt;CharT, Iter&gt; TimeGet;

std::ios_base::iostate err = std::ios_base::goodbit;

const TimeGet &amp;tg = std::use_facet&lt;TimeGet&gt;(in.getloc());

tg.get(Iter(in.rdbuf()), Iter(), in, err, tmb, fmt, fmt + traits::length(fmt));

if (err != std::ios_base::goodbit)

    in.setstate(err);


<h2>Notes</h2>

As specified in std::time_get::do_get, which this function calls, it's unspecified if this function zero out the fields in *tmb that are not set directly by the conversion specifiers that appear in fmt: portable programs should initialize every field of *tmb to zero before calling std::get_time. 

<h2>Example</h2>

note: choose clang to observe the output. libstdc++ does not correctly implement the %b specifier: bug_78714 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;sstream&gt;

#include &lt;locale&gt;

#include &lt;iomanip&gt;
int main()

{
    std::tm t = {};
    std::istringstream ss(&quot;2011-Februar-18 23:12:34&quot;);
    ss.imbue(std::locale(&quot;de_DE.utf-8&quot;));
    ss &gt;&gt; std::get_time(&amp;t, &quot;%Y-%b-%d %H:%M:%S&quot;);
    if (ss.fail()) {
        std::cout &lt;&lt; &quot;Parse failed\n&quot;;
    } else {
        std::cout &lt;&lt; std::put_time(&amp;t, &quot;%c&quot;) &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;Sun Feb 18 23:12:34 2011

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses time/date values from an input character sequence into struct std::tm 
time_get <i>(class template)</i> 
put_time formats and outputs a date/time value according to the specified format 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
