---
title: "stdcollate_byname(3)"
name: "stdcollate_byname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdcollate_byname/"
description: "std::collate_byname – std::collate_byname"
---

<p>std::collate_byname &#8211; std::collate_byname</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;locale&gt;

template&lt; class CharT &gt;

class collate_byname : public std::collate&lt;CharT&gt;;</code></pre>
<p>std::collate_byname is a std::collate facet which encapsulates locale-specific collation (comparison) and hashing of strings. Just like std::collate, it can be imbued in std::regex and applied, by means of std::locale::operator(), directly to all standard algorithms that expect a string comparison predicate.<br />
Two specializations are provided by the standard library<br />
Defined in header &lt;locale&gt;<br />
std::collate_byname&lt;char&gt; locale-specific collation of multibyte strings<br />
std::collate_byname&lt;wchar_t&gt; locale-specific collation of wide strings </p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new collate_byname facet<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a collate_byname facet<br />
destructor <i>(protected member function)</i> </p>
<p>&nbsp;std::collate_byname::collate_byname </p>
<p>explicit collate_byname( const char* name, std::size_t refs = 0 );<br />
explicit collate_byname( const std::string&amp; name, std::size_t refs = 0 ); <i>(since C++11)</i> </p>
<p>Constructs a new std::collate_byname facet for a locale with name.<br />
refs is used for resource management: if refs == 0, the implementation destroys the facet, when the last std::locale object holding it is destroyed. Otherwise, the object is not destroyed.</p>
<h2>Parameters</h2>
<p>name &#8211; the name of the locale<br />
refs &#8211; the number of references that link to the facet </p>
<p>&nbsp;std::collate_byname::~collate_byname </p>
<p>protected:<br />
~collate_byname(); </p>
<p>Destroys the facet. </p>
<p>Inherited from std::collate</p>
<h2>Member types</h2>
<p>Member type Definition<br />
char_type charT<br />
string_type std::basic_string&lt;charT&gt;</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_compare<br />
compare <i>(public member function of std::collate&lt;CharT&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_transform<br />
transform <i>(public member function of std::collate&lt;CharT&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_hash<br />
hash <i>(public member function of std::collate&lt;CharT&gt;)</i></p>
<h2>Protected member functions</h2>
<p>do_compare compares two strings using this facet&#8217;s collation rules<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::collate&lt;CharT&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_transform transforms a string so that collation can be replaced by comparison<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::collate&lt;CharT&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_hash generates an integer hash value using this facet&#8217;s collation rules<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::collate&lt;CharT&gt;)</i><br />
<code>[virtual]</code></p>
<h2>Notes</h2>
<p>Collation order is the dictionary order: the position of the letter in the national alphabet (its equivalence class) has higher priority than its case or variant. Within an equivalence class, lowercase characters collate before their uppercase equivalents and locale-specific order may apply to the characters with diacritics. In some locales, groups of characters compare as single collation units. For example, &quot;ch&quot; in Czech follows &quot;h&quot; and precedes &quot;i&quot;, and &quot;dzs&quot; in Hungarian follows &quot;dz&quot; and precedes &quot;g&quot;. </p>
<h2>Example</h2>
<p>&nbsp;This section is incomplete<br />
&nbsp;Reason: no example </p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;defines lexicographical comparison and hashing of strings<br />
collate <i>(class template)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two strings in accordance to the current locale<br />
strcoll <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;compares two wide strings in accordance to the current locale<br />
wcscoll <i>(function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;lexicographically compares two strings using this locale&#8217;s collate facet<br />
operator() <i>(public member function of std::locale)</i> </p>
