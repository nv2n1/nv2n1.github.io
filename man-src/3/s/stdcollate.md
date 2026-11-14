---
title: "stdcollate(3)"
name: "stdcollate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcollate/"
description: "std::collate – std::collate"
---

<p>std::collate &#8211; std::collate</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;locale&gt;

template&lt; class CharT &gt;

class collate;</code></pre>
<p>Class std::collate encapsulates locale-specific collation (comparison) and hashing of strings. This facet is used by std::basic_regex and can be applied, by means of std::locale::operator(), directly to all standard algorithms that expect a string comparison predicate.<br />
&nbsp;std-collate-inheritance.svg<br />
Inheritance diagram<br />
Two standalone (locale-independent) specializations are provided by the standard library:<br />
Defined in header &lt;locale&gt;<br />
std::collate&lt;char&gt; implements lexicographical ordering of byte strings<br />
std::collate&lt;wchar_t&gt; implements lexicographical ordering of wide strings<br />
In addition, every locale object constructed in a C++ program implements its own (locale-specific) versions of these specializations. </p>
<h2>Member types</h2>
<p>Member type Definition<br />
char_type CharT<br />
string_type std::basic_string&lt;CharT&gt;</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new collate facet<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destructs a collate facet<br />
destructor <i>(protected member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_compare<br />
compare <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_transform<br />
transform <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_hash<br />
hash <i>(public member function)</i></p>
<h2>Member objects</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;id of the locale<br />
static std::locale::id id <i>(public member object)</i></p>
<h2>Protected member functions</h2>
<p>do_compare compares two strings using this facet&#8217;s collation rules<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
<p>do_transform transforms a string so that collation can be replaced by comparison<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code> </p>
<p>do_hash generates an integer hash value using this facet&#8217;s collation rules<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function)</i><br />
<code>[virtual]</code></p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;locale&gt;

#include &lt;iostream&gt;

#include &lt;string&gt;

#include &lt;vector&gt;

#include &lt;algorithm&gt;
int main()

{
    std::wcout.imbue(std::locale(&quot;&quot;));
    std::vector&lt;std::wstring&gt; v = {L&quot;ar&quot;, L&quot;zebra&quot;, L&quot;ögrupp&quot;, L&quot;Zebra&quot;, L&quot;ängel&quot;,
                                   L&quot;år&quot;, L&quot;förnamn&quot;};
    std::wcout &lt;&lt; &quot;Default locale collation order: &quot;;
    std::sort(v.begin(), v.end());
    for (auto s : v)
        std::wcout &lt;&lt; s &lt;&lt; ' ';
    std::wcout &lt;&lt; '
';
    std::wcout &lt;&lt; &quot;English locale collation order: &quot;;
    std::sort(v.begin(), v.end(), std::locale(&quot;en_US.UTF-8&quot;));
    for (auto s : v)
        std::wcout &lt;&lt; s &lt;&lt; ' ';
    std::wcout &lt;&lt; '
';
    std::wcout &lt;&lt; &quot;Swedish locale collation order: &quot;;
    std::sort(v.begin(), v.end(), std::locale(&quot;sv_SE.UTF-8&quot;));
    for (auto s : v)
        std::wcout &lt;&lt; s &lt;&lt; ' ';
    std::wcout &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;Default locale collation order: Zebra ar förnamn zebra ängel år ögrupp<br />
&nbsp;<wbr>&nbsp;English locale collation order: ängel ar år förnamn ögrupp zebra Zebra<br />
&nbsp;<wbr>&nbsp;Swedish locale collation order: ar förnamn zebra Zebra år ängel ögrupp</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lexicographically compares two strings using this locale&#8217;s collate facet<br />
operator() <i>(public member function of std::locale)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;creates a collate facet for the named locale<br />
collate_byname <i>(class template)</i> </p>
