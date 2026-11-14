---
title: "stdput_money(3)"
name: "stdput_money"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdput_money/"
---

std::put_money - std::put_money

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;iomanip&gt;

    template &lt;class MoneyT&gt;
    (since C++ 11)

    /*unspecified*/ put_money(const MoneyT &amp;mon, bool intl = false);</code></pre> 
When used in an expression out &lt;&lt; put_money(mon, intl), converts the monetary value mon to its character representation as specified by the std::money_put facet of the locale currently imbued in out. 
The insertion operation in out &lt;&lt; put_money(mon, intl) behaves as a FormattedOutputFunction. 

<h2>Parameters</h2>

mon - a monetary value, either long double or std::basic_string 
intl - use international currency strings if true, use currency symbols otherwise

<h2>Return value</h2>

Returns an object of unspecified type such that if out is the name of an output stream of type std::basic_ostream&lt;CharT, Traits&gt;, then the expression out &lt;&lt; put_money(mon, intl) behaves as if the following code was executed :

    typedef std::ostreambuf_iterator&lt;CharT, Traits&gt;
        Iter;

typedef std::money_put&lt;CharT, Iter&gt; MoneyPut;

const MoneyPut &amp;mp = std::use_facet&lt;MoneyPut&gt;(out.getloc());

const Iter end = mp.put(Iter(out.rdbuf()), intl, out, out.fill(), mon);

if (end.failed())

    out.setstate(std::ios::badbit);


<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;
int main()

{
    long double mon = 123.45; // or std::string mon = &quot;123.45&quot;;
    std::cout.imbue(std::locale(&quot;en_US.utf8&quot;));
    std::cout &lt;&lt; std::showbase
              &lt;&lt; &quot;en_US: &quot; &lt;&lt; std::put_money(mon)
              &lt;&lt; &quot; or &quot; &lt;&lt; std::put_money(mon, true) &lt;&lt; '\n';
    std::cout.imbue(std::locale(&quot;ru_RU.utf8&quot;));
    std::cout &lt;&lt; &quot;ru_RU: &quot; &lt;&lt; std::put_money(mon)
              &lt;&lt; &quot; or &quot; &lt;&lt; std::put_money(mon, true) &lt;&lt; '\n';
    std::cout.imbue(std::locale(&quot;ja_JP.utf8&quot;));
    std::cout &lt;&lt; &quot;ja_JP: &quot; &lt;&lt; std::put_money(mon)
              &lt;&lt; &quot; or &quot; &lt;&lt; std::put_money(mon, true) &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;en_US: $1.23 or USD 1.23 
&nbsp;<wbr>&nbsp;ru_RU: 1.23 руб or 1.23 RUB 
&nbsp;<wbr>&nbsp;ja_JP: ￥123 or JPY 123

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;formats a monetary value for output as a character sequence 
money_put <i>(class template)</i> 
get_money parses a monetary value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
