---
title: "stdios_basewidth(3)"
name: "stdios_basewidth"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_basewidth/"
description: "std::ios_base::width – std::ios_base::width"
---

<p>std::ios_base::width &#8211; std::ios_base::width</p>
<h2>Synopsis</h2>
<p>streamsize width() const; <code>(1)</code><br />
streamsize width( streamsize new_width ); <code>(2)</code><br />
Manages the minimum number of characters to generate on certain output operations and the maximum number of characters to generate on certain input operations.<br />
1) Returns the current field width.<br />
2) Sets the field width to the given one. Returns the previous field width. </p>
<h2>Parameters</h2>
<p>new_width &#8211; new field width setting</p>
<h2>Return value</h2>
<p>The field width before the call to the function </p>
<h2>Notes</h2>
<p>Some I/O functions call width<code>(0)</code> before returning, see std::setw (this results in this field having effect on the next I/O function only, and not on any subsequent I/O)<br />
The exact effects this modifier has on the input and output vary between the individual I/O functions and are described at each operator&lt;&lt; and operator&gt;&gt; overload page individually. </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;array&gt;

#include &lt;tuple&gt;

#include &lt;ctime&gt;

#include &lt;string&gt;

#include &lt;iostream&gt;

#include &lt;sstream&gt;

#include &lt;iomanip&gt;
int main()

{
    auto str_time = [](int year, int mon, int day) {
        constexpr std::array&lt;const char *, 7&gt; week_day&#123;&#123;&quot;Sunday&quot;, &quot;Monday&quot;, &quot;Tuesday&quot;, &quot;Wednesday&quot;, &quot;Thursday&quot;, &quot;Friday&quot;, &quot;Saturday&quot;}};
        std::tm tm{};
        tm.tm_year = year - 1900;
        tm.tm_mon = mon - 1;
        tm.tm_mday = day;
        day += mon &lt; 3 ? year-- : year - 2;
        tm.tm_wday = (23 * mon / 9 + day + 4 + year / 4 - year / 100 + year / 400) % 7;
        std::ostringstream out;
        out &lt;&lt; week_day[tm.tm_wday] &lt;&lt; &quot;, &quot; &lt;&lt; std::put_time(&amp;tm, &quot;%B %d, %Y&quot;);
        return out.str();
    };
    constexpr int column_size = 4;
    using table_t = std::array&lt;std::string, column_size&gt;;
    table_t headers&#123;&#123;&quot;Name&quot;, &quot;Birthdate&quot;, &quot;Death date&quot;, &quot;Language Created&quot;}};
    std::array&lt;table_t, 5&gt; data&#123;&#123;&#123;&#123;&quot;Dennis MacAlistair Ritchie&quot;, str_time(1941, 9, 9), str_time(2011, 10, 12), &quot;C&quot;}},
                                 &#123;&#123;&quot;Bjarne Stroustrup&quot;, str_time(1950, 12, 30), &quot;&quot;, &quot;C++&quot;}},
                                 &#123;&#123;&quot;Anders Hejlsberg&quot;, str_time(1960, 12, 2), &quot;&quot;, &quot;C#&quot;}},
                                 &#123;&#123;&quot;Guido van Rossum&quot;, str_time(1956, 1, 31), &quot;&quot;, &quot;Python&quot;}},
                                 &#123;&#123;&quot;Brendan Eich&quot;, str_time(1961, 7, 4), &quot;&quot;, &quot;Javascript&quot;}}}};
    constexpr int name_wid = 30;
    constexpr int birth_wid = 30;
    constexpr int death_wid = 30;
    constexpr int lang_wid = 18;
    auto print_line = [](table_t const &amp;tbl) {
        auto const &amp;[Name, Birthdate, DeathDate, LanguageCreated] = tbl;
        std::cout.width(name_wid);
        std::cout &lt;&lt; (&quot;| &quot; + Name) &lt;&lt; '|';
        std::cout.width(birth_wid);
        std::cout &lt;&lt; (' ' + Birthdate) &lt;&lt; '|';
        std::cout.width(death_wid);
        std::cout &lt;&lt; (' ' + DeathDate) &lt;&lt; '|';
        std::cout.width(lang_wid);
        std::cout &lt;&lt; (' ' + LanguageCreated) &lt;&lt; '|';
        std::cout &lt;&lt; '
';
    };
    constexpr int total_wid = name_wid + birth_wid + death_wid + lang_wid + column_size;
    auto print_break = [] {
        std::cout.width(total_wid);
        std::cout.fill('-');
        std::cout &lt;&lt; '-' &lt;&lt; std::endl;
        std::cout.fill(' ');
    };
    std::cout.setf(std::ios::left, std::ios::adjustfield);
    print_break();
    print_line(headers);
    print_break();
    for (auto const &amp;entry : data)
        print_line(entry);
    print_break();
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
&nbsp;<wbr>&nbsp;| Name | Birthdate | Death date | Language Created |<br />
&nbsp;<wbr>&nbsp;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-<br />
&nbsp;<wbr>&nbsp;| Dennis MacAlistair Ritchie | Tuesday, September 09, 1941 | Wednesday, October 12, 2011 | C |<br />
&nbsp;<wbr>&nbsp;| Bjarne Stroustrup | Saturday, December 30, 1950 | | C++ |<br />
&nbsp;<wbr>&nbsp;| Anders Hejlsberg | Friday, December 02, 1960 | | C# |<br />
&nbsp;<wbr>&nbsp;| Guido van Rossum | Tuesday, January 31, 1956 | | Python |<br />
&nbsp;<wbr>&nbsp;| Brendan Eich | Tuesday, July 04, 1961 | | Javascript |<br />
&nbsp;<wbr>&nbsp;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;manages decimal precision of floating point operations<br />
precision <i>(public member function)</i> </p>
