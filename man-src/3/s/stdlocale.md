---
title: "stdlocale(3)"
name: "stdlocale"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdlocale/"
description: "std::locale – std::locale"
---

<p>std::locale &#8211; std::locale</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;locale&gt;

class locale;</code></pre>
<p>An object of class std::locale is an immutable indexed set of immutable facets. Each stream object of the C++ input/output library is associated with an std::locale object and uses its facets for parsing and formatting of all data. In addition, a locale object is associated with each std::basic_regex object. Locale objects can also be used as predicates that perform string collation with the standard containers and algorithms and can be accessed directly to obtain or modify the facets they hold.<br />
Each locale constructed in a C++ program holds at least the following standard facets, but a program may define additional specializations or completely new facets and add them to any existing locale object.<br />
Supported facets<br />
std::collate&lt;char&gt; std::collate&lt;wchar_t&gt;<br />
std::ctype&lt;char&gt; std::ctype&lt;wchar_t&gt;<br />
std::codecvt&lt;char,char,mbstate_t&gt; std::codecvt&lt;char32_t,char,mbstate_t&gt;<br />
std::codecvt&lt;char16_t,char,mbstate_t&gt; std::codecvt&lt;wchar_t,char,mbstate_t&gt;<br />
std::moneypunct&lt;char&gt; std::moneypunct&lt;wchar_t&gt;<br />
std::moneypunct&lt;char,true&gt; std::moneypunct&lt;wchar_t,true&gt;<br />
std::money_get&lt;char&gt; std::money_get&lt;wchar_t&gt;<br />
std::money_put&lt;char&gt; std::money_put&lt;wchar_t&gt;<br />
std::numpunct&lt;char&gt; std::numpunct&lt;wchar_t&gt;<br />
std::num_get&lt;char&gt; std::num_get&lt;wchar_t&gt;<br />
std::num_put&lt;char&gt; std::num_put&lt;wchar_t&gt;<br />
std::time_get&lt;char&gt; std::time_get&lt;wchar_t&gt;<br />
std::time_put&lt;char&gt; std::time_put&lt;wchar_t&gt;<br />
std::messages&lt;char&gt; std::messages&lt;wchar_t&gt;<br />
Internally, a locale object is implemented as-if it is a reference-counted pointer to an array (indexed by std::locale::id) of reference-counted pointers to facets: copying a locale only copies one pointer and increments several reference counts. To maintain the standard C++ library thread safety guarantees (operations on different objects are always thread-safe), both the locale reference count and each facet reference count are updated in thread-safe manner, similar to std::shared_ptr. </p>
<h2>Member types</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the facet index type: each facet class must declare or inherit a public static member of this type<br />
id <i>(class)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the base class for all facet categories: each facet of any category is derived from this type<br />
facet <i>(class)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int<br />
category <i>(typedef)</i></p>
<h2>Member objects</h2>
<p>none a zero value of type category indicating no facet category<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>collate a bitmask value of type category indicating the collate facet category<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>ctype a bitmask value of type category indicating the ctype facet category<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>monetary a bitmask value of type category indicating the monetary facet category<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>numeric a bitmask value of type category indicating the numeric facet category<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>time a bitmask value of type category indicating the time facet category<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>messages a bitmask value of type category indicating the messages facet category<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code> </p>
<p>all collate | ctype | monetary | numeric | time | messages<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member constant)</i><br />
<code>[static]</code></p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new locale<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs the locale and the facets whose reference count becomes zero<br />
destructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;replaces a locale<br />
operator= <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a locale with compile-time identified facet copied from another locale<br />
combine <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the name of the locale or &quot;*&quot; if unnamed<br />
name <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;equality comparison between locale objects<br />
operator== <i>(public member function)</i><br />
operator!=<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lexicographically compares two strings using this locale&#8217;s collate facet<br />
operator() <i>(public member function)</i> </p>
<p>global changes the global locale<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code> </p>
<p>classic obtains a reference to the &quot;C&quot; locale<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(public static member function)</i><br />
<code>[static]</code></p>
<h2>Example</h2>
<p>Demonstrates the typical prologue of a locale-sensitive program (cross-platform)<br />
 // Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;
int main()

{
    std::wcout &lt;&lt; &quot;User-preferred locale setting is &quot; &lt;&lt; std::locale(&quot;&quot;).name().c_str() &lt;&lt; '
';
    // on startup, the global locale is the &quot;C&quot; locale
    std::wcout &lt;&lt; 1000.01 &lt;&lt; '
';
    // replace the C++ global locale as well as the C locale with the user-preferred locale
    std::locale::global(std::locale(&quot;&quot;));
    // use the new global locale for future wide character output
    std::wcout.imbue(std::locale());
    // output the same number again
    std::wcout &lt;&lt; 1000.01 &lt;&lt; '
';
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;User-preferred locale setting is en_US.UTF8<br />
&nbsp;<wbr>&nbsp;1000.01<br />
&nbsp;<wbr>&nbsp;1,000.01</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;obtains a facet from a locale<br />
use_facet <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if a locale implements a specific facet<br />
has_facet <i>(function template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sets locale<br />
imbue <i>(public member function of std::ios_base)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns current locale<br />
getloc <i>(public member function of std::ios_base)</i> </p>
