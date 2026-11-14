---
title: "stdnumpunct(3)"
name: "stdnumpunct"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumpunct/"
description: "std::numpunct – std::numpunct"
---

<p>std::numpunct &#8211; std::numpunct</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;locale&gt;

template&lt; class CharT &gt;

class numpunct;</code></pre>
<p>The facet std::numpunct encapsulates numeric punctuation preferences. Stream I/O operations use std::numpunct through std::num_get and std::num_put for parsing numeric input and formatting numeric output.<br />
The numbers that are supported by std::numpunct have the format described below. Here digit represents the radix set specified by the fmtflags argument value, thousands-sep and decimal-point are the results of thousands_sep() and decimal_point() functions respectively. The format of integer values is as follows: integer     ::= [sign] units</p>
<p>sign        ::= plusminus</p>
<p>plusminus   ::= &#8216;+&#8217; | &#8216;-&#8216;</p>
<p>units       ::= digits [thousands-sep units]</p>
<p>digits      ::= digit [digits]<br />
The number of digits between the thousand-seps (maximum size of digits) is specified by the result of grouping().<br />
The format of floating-point values is as follows: floatval    ::= [sign] units [decimal-point [digits]] [e [sign] digits] |<br />
[sign]        decimal-point  digits   [e [sign] digits]</p>
<p>e           ::= &#8216;e&#8217; | &#8216;E&#8217;<br />
&nbsp;std-numpunct-inheritance.svg<br />
Inheritance diagram<br />
Two standalone (locale-independent) specializations are provided by the standard library:<br />
Defined in header &lt;locale&gt;<br />
std::numpunct&lt;char&gt; provides equivalents of the &quot;C&quot; locale preferences<br />
std::numpunct&lt;wchar_t&gt; provides wide character equivalents of the &quot;C&quot; locale preferences<br />
In addition, every locale object constructed in a C++ program implements its own (locale-specific) versions of these specializations. </p>
<h2>Member types</h2>
<p>Member type Definition<br />
char_type charT<br />
string_type std::basic_string&lt;charT&gt;</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new numpunct facet<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs a numpunct facet<br />
destructor <i>(protected member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_decimal_point<br />
decimal_point <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_thousands_sep<br />
thousands_sep <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_grouping<br />
grouping <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_truename or do_falsename<br />
truename <i>(public member function)</i><br />
falsename</p>
<h2>Protected member functions</h2>
<p>do_decimal_point provides the character to use as decimal point<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
<p>do_thousands_sep provides the character to use as thousands separator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
<p>do_grouping provides the numbers of digits between each pair of thousands separators<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
<p>do_truename provides the string to use as the name of the boolean true and false<br />
do_falsename <i>(virtual protected member function)</i> </p>
<p><code>[virtual]</code></p>
<h2>Member objects</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;id of the locale<br />
static std::locale::id id <i>(public member object)</i></p>
<h2>Example</h2>
<p>The following example changes the string representations of true and false<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;
struct french_bool : std::numpunct&lt;char&gt; {
    string_type do_truename() const
    {
        return &quot;oui&quot;;
    }
    string_type do_falsename() const
    {
        return &quot;non&quot;;
    }
};
int main()

{
    std::cout &lt;&lt; &quot;default locale: &quot;
              &lt;&lt; std::boolalpha &lt;&lt; true &lt;&lt; &quot;, &quot; &lt;&lt; false &lt;&lt; '
';
    std::cout.imbue(std::locale(std::cout.getloc(), new french_bool));
    std::cout &lt;&lt; &quot;locale with modified numpunct: &quot;
              &lt;&lt; std::boolalpha &lt;&lt; true &lt;&lt; &quot;, &quot; &lt;&lt; false &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;default locale: true, false<br />
&nbsp;<wbr>&nbsp;locale with modified numpunct: oui, non</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a numpunct facet for the named locale<br />
numpunct_byname <i>(class template)</i> </p>
