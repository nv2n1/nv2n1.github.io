---
title: "stdget_money(3)"
name: "stdget_money"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdget_money/"
---

std::get_money - std::get_money

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;iomanip&gt;

template&lt; class MoneyT &gt;                                      (since C++11)

/*unspecified*/ get_money( MoneyT&amp; mon, bool intl = false );</code></pre> 
When used in an expression in &gt;&gt; get_money(mon, intl), parses the character input as a monetary value, as specified by the std::money_get facet of the locale currently imbued in in, and stores the value in mon. 
The extraction operation in in &gt;&gt; get_money(mon, intl) behaves as a FormattedInputFunction. 

<h2>Parameters</h2>

mon - variable where monetary value will be written. Can be either long double or basic_string 
intl - expects to find required international currency strings if true, expects optional currency symbols otherwise

<h2>Return value</h2>

Returns an object of unspecified type such that if in is the name of an input stream of type std::basic_istream&lt;CharT, Traits&gt;, then the expression in &gt;&gt; get_money(mon, intl) behaves as if the following code was executed :

    typedef std::istreambuf_iterator&lt;CharT, Traits&gt; Iter;

typedef std::money_get&lt;CharT, Iter&gt; MoneyGet;

std::ios_base::iostate err = std::ios_base::goodbit;

const MoneyGet &amp;mg = std::use_facet&lt;MoneyGet&gt;(in.getloc());

mg.get(Iter(in.rdbuf()), Iter(), intl, in, err, mon);

if (std::ios_base::goodbit != err)

    out.setstate(err);


<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;sstream&gt;

#include &lt;locale&gt;

#include &lt;iomanip&gt;
int main()

{
    std::istringstream in(&quot;$1,234.56 2.22 USD  3.33&quot;);
    long double v1, v2;
    std::string v3;
    in.imbue(std::locale(&quot;en_US.UTF-8&quot;));
    in &gt;&gt; std::get_money(v1) &gt;&gt; std::get_money(v2) &gt;&gt; std::get_money(v3, true);
    if (in) {
        std::cout &lt;&lt; std::quoted(in.str()) &lt;&lt; &quot; parsed as: &quot;
                  &lt;&lt; v1 &lt;&lt; &quot;, &quot; &lt;&lt; v2 &lt;&lt; &quot;, &quot; &lt;&lt; v3 &lt;&lt; '\n';
    } else {
        std::cout &lt;&lt; &quot;Parse failed&quot;;
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot;$1,234.56 2.22 USD 3.33&quot; parsed as: 123456, 222, 333

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;parses and constructs a monetary value from an input character sequence 
money_get <i>(class template)</i> 
put_money formats and outputs a monetary value 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function template)</i> 
<i>(C++11)</i> 
