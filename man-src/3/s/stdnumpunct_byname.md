---
title: "stdnumpunct_byname(3)"
name: "stdnumpunct_byname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdnumpunct_byname/"
description: "std::numpunct_byname – std::numpunct_byname"
---

<p>std::numpunct_byname &#8211; std::numpunct_byname</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;locale&gt;

template&lt; class CharT &gt;

class numpunct_byname : public std::numpunct&lt;CharT&gt;;</code></pre>
<p>std::numpunct_byname is a std::numpunct facet which encapsulates numeric punctuation preferences of a locale specified at its construction.<br />
Two specializations are provided by the standard library<br />
Defined in header &lt;locale&gt;<br />
std::numpunct_byname&lt;char&gt; locale-specific std::numpunct facet for narrow character I/O<br />
std::numpunct_byname&lt;wchar_t&gt; locale-specific std::numpunct facet for wide characters I/O </p>
<h2>Member types</h2>
<p>Member type Definition<br />
char_type CharT<br />
string_type std::basic_string&lt;CharT&gt;</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new numpunct_byname facet<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a numpunct_byname facet<br />
destructor <i>(protected member function)</i> </p>
<p>&nbsp;std::numpunct_byname::numpunct_byname </p>
<p>explicit numpunct_byname( const char* name, std::size_t refs = 0 );<br />
explicit numpunct_byname( const std::string&amp; name, std::size_t refs = 0 ); <i>(since C++11)</i> </p>
<p>Constructs a new std::numpunct_byname facet for a locale with name.<br />
refs is used for resource management: if refs == 0, the implementation destroys the facet, when the last std::locale object holding it is destroyed. Otherwise, the object is not destroyed.</p>
<h2>Parameters</h2>
<p>name &#8211; the name of the locale<br />
refs &#8211; the number of references that link to the facet </p>
<p>&nbsp;std::numpunct_byname::~numpunct_byname </p>
<p>protected:<br />
~numpunct_byname(); </p>
<p>Destroys the facet. </p>
<p>Inherited from std::numpunct</p>
<h2>Member types</h2>
<p>Member type Definition<br />
char_type charT<br />
string_type std::basic_string&lt;charT&gt;</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_decimal_point<br />
decimal_point <i>(public member function of std::numpunct&lt;CharT&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_thousands_sep<br />
thousands_sep <i>(public member function of std::numpunct&lt;CharT&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_grouping<br />
grouping <i>(public member function of std::numpunct&lt;CharT&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_truename or do_falsename<br />
truename <i>(public member function of std::numpunct&lt;CharT&gt;)</i><br />
falsename</p>
<h2>Protected member functions</h2>
<p>do_decimal_point provides the character to use as decimal point<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::numpunct&lt;CharT&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_thousands_sep provides the character to use as thousands separator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::numpunct&lt;CharT&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_grouping provides the numbers of digits between each pair of thousands separators<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::numpunct&lt;CharT&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_truename provides the string to use as the name of the boolean true and false<br />
do_falsename <i>(virtual protected member function of std::numpunct&lt;CharT&gt;)</i> </p>
<p><code>[virtual]</code></p>
<h2>Member objects</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;id of the locale<br />
static std::locale::id id <i>(public member object)</i></p>
<h2>Example</h2>
<p>This example demonistrates how to apply numeric punctuation rules of another language without changing the rest of the locale.<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;

int main()

{
    const double number = 1000.25;
    std::wcout &lt;&lt; L&quot;default locale: &quot; &lt;&lt; number &lt;&lt; L'
';
    std::wcout.imbue(std::locale(std::wcout.getloc(),
                                 new std::numpunct_byname&lt;wchar_t&gt;(&quot;ru_RU.UTF8&quot;)));
    std::wcout &lt;&lt; L&quot;default locale with russian numpunct: &quot; &lt;&lt; number &lt;&lt; L'
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;default locale: 1000.25<br />
&nbsp;<wbr>&nbsp;default locale with russian numpunct: 1 000,25</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;defines numeric punctuation rules<br />
numpunct <i>(class template)</i> </p>
