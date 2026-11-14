---
title: "stdmoneypunct_byname(3)"
name: "stdmoneypunct_byname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmoneypunct_byname/"
description: "std::moneypunct_byname – std::moneypunct_byname"
---

<p>std::moneypunct_byname &#8211; std::moneypunct_byname</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;locale&gt;

template&lt; class CharT, bool Intl = false &gt;

class moneypunct_byname : public std::moneypunct&lt;CharT, Intl&gt;;</code></pre>
<p>std::moneypunct_byname is a std::moneypunct facet which encapsulates monetary formatting preferences of a locale specified at its construction.<br />
Two specializations are provided by the standard library<br />
Defined in header &lt;locale&gt;<br />
std::moneypunct_byname&lt;char, Intl&gt; locale-specific std::moneypunct facet for narrow character I/O<br />
std::moneypunct_byname&lt;wchar_t, Intl&gt; locale-specific std::moneypunct facet for wide character I/O </p>
<h2>Member types</h2>
<p>Member type Definition<br />
pattern std::money_base::pattern<br />
string_type std::basic_string&lt;CharT&gt;</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new moneypunct_byname facet<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a moneypunct_byname facet<br />
destructor <i>(protected member function)</i> </p>
<p>&nbsp;std::moneypunct_byname::moneypunct_byname </p>
<p>explicit moneypunct_byname( const char* name, std::size_t refs = 0 );<br />
explicit moneypunct_byname( const std::string&amp; name, std::size_t refs = 0 ); <i>(since C++11)</i> </p>
<p>Constructs a new std::moneypunct_byname facet for a locale with name.<br />
refs is used for resource management: if refs == 0, the implementation destroys the facet, when the last std::locale object holding it is destroyed. Otherwise, the object is not destroyed.</p>
<h2>Parameters</h2>
<p>name &#8211; the name of the locale<br />
refs &#8211; the number of references that link to the facet </p>
<p>&nbsp;std::moneypunct_byname::~moneypunct_byname </p>
<p>protected:<br />
~moneypunct_byname(); </p>
<p>Destroys the facet. </p>
<p>Inherited from std::moneypunct</p>
<h2>Member types</h2>
<p>Member type Definition<br />
char_type CharT<br />
string_type std::basic_string&lt;CharT&gt;</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_decimal_point<br />
decimal_point <i>(public member function of std::moneypunct&lt;CharT,International&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_thousands_sep<br />
thousands_sep <i>(public member function of std::moneypunct&lt;CharT,International&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_grouping<br />
grouping <i>(public member function of std::moneypunct&lt;CharT,International&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_curr_symbol<br />
curr_symbol <i>(public member function of std::moneypunct&lt;CharT,International&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_positive_sign or do_negative_sign<br />
positive_sign <i>(public member function of std::moneypunct&lt;CharT,International&gt;)</i><br />
negative_sign<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_frac_digits<br />
frac_digits <i>(public member function of std::moneypunct&lt;CharT,International&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_pos_format/do_neg_format<br />
pos_format <i>(public member function of std::moneypunct&lt;CharT,International&gt;)</i><br />
neg_format</p>
<h2>Protected member functions</h2>
<p>do_decimal_point provides the character to use as decimal point<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::moneypunct&lt;CharT,International&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_thousands_sep provides the character to use as thousands separator<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::moneypunct&lt;CharT,International&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_grouping provides the numbers of digits between each pair of thousands separators<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::moneypunct&lt;CharT,International&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_curr_symbol provides the string to use as the currency identifier<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::moneypunct&lt;CharT,International&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_positive_sign provides the string to indicate a positive or negative value<br />
do_negative_sign <i>(virtual protected member function of std::moneypunct&lt;CharT,International&gt;)</i> </p>
<p><code>[virtual]</code> </p>
<p>do_frac_digits provides the number of digits to display after the decimal point<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::moneypunct&lt;CharT,International&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_pos_format provides the formatting pattern for currency values<br />
do_neg_format <i>(virtual protected member function of std::moneypunct&lt;CharT,International&gt;)</i> </p>
<p><code>[virtual]</code></p>
<h2>Member constants</h2>
<p>Member Definition<br />
const bool intl (static) International</p>
<h2>Member objects</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;id of the locale<br />
static std::locale::id id <i>(public member object)</i> </p>
<p>Inherited from std::money_base </p>
<p>Member type Definition<br />
enum part { none, space, symbol, sign, value }; unscoped enumeration type<br />
struct pattern { char field[4]; }; the monetary format type </p>
<p>Enumeration constant Definition<br />
none whitespace is permitted but not required except in the last position, where whitespace is not permitted<br />
space one or more whitespace characters are required<br />
symbol the sequence of characters returned by moneypunct::curr_symbol is required<br />
sign the first of the characters returned by moneypunct::positive_sign or moneypunct::negative_sign is required<br />
value the absolute numeric monetary value is required</p>
<h2>Example</h2>
<p>This example demonistrates how to apply monetary formatting rules of another language without changing the rest of the locale.<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;locale&gt;

int main()

{
    long double mon = 1234567;
    std::locale::global(std::locale(&quot;en_US.utf8&quot;));
    std::wcout.imbue(std::locale());
    std::wcout &lt;&lt; L&quot;american locale : &quot; &lt;&lt; std::showbase
               &lt;&lt; std::put_money(mon) &lt;&lt; '
';
    std::wcout.imbue(std::locale(std::wcout.getloc(),
                                 new std::moneypunct_byname&lt;wchar_t&gt;(&quot;ru_RU.utf8&quot;)));
    std::wcout &lt;&lt; L&quot;american locale with russian moneypunct: &quot;
               &lt;&lt; std::put_money(mon) &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;american locale : $12,345.67<br />
&nbsp;<wbr>&nbsp;american locale with russian moneypunct: 12 345.67 руб</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;defines monetary formatting parameters used by std::money_get and std::money_put<br />
moneypunct <i>(class template)</i> </p>
