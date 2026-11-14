---
title: "stdmessages_byname(3)"
name: "stdmessages_byname"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmessages_byname/"
description: "std::messages_byname – std::messages_byname"
---

<p>std::messages_byname &#8211; std::messages_byname</p>
<h2>Synopsis</h2>
<pre><code>Defined in header &lt;locale&gt;

template&lt; class CharT &gt;

class messages_byname : public std::messages&lt;CharT&gt;;</code></pre>
<p>std::messages_byname is a std::messages facet which encapsulates retrieval of strings from message catalogs of the locale specified at its construction.<br />
Two specializations are provided by the standard library<br />
Defined in header &lt;locale&gt;<br />
std::messages_byname&lt;char&gt; narrow/multibyte message catalog access<br />
std::messages_byname&lt;wchar_t&gt; wide string message catalog access </p>
<h2>Member types</h2>
<p>Member type Definition<br />
catalog std::messages_base&lt;CharT&gt;::catalog<br />
string_type std::basic_string&lt;CharT&gt;</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constructs a new messages_byname facet<br />
constructor <i>(public member function)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;destroys a messages_byname facet<br />
destructor <i>(protected member function)</i> </p>
<p>&nbsp;std::messages_byname::messages_byname </p>
<p>explicit messages_byname( const char* name, std::size_t refs = 0 );<br />
explicit messages_byname( const std::string&amp; name, std::size_t refs = 0 ); <i>(since C++11)</i> </p>
<p>Constructs a new std::messages_byname facet for a locale with name.<br />
refs is used for resource management: if refs == 0, the implementation destroys the facet, when the last std::locale object holding it is destroyed. Otherwise, the object is not destroyed.</p>
<h2>Parameters</h2>
<p>name &#8211; the name of the locale<br />
refs &#8211; the number of references that link to the facet </p>
<p>&nbsp;std::messages_byname::~messages_byname </p>
<p>protected:<br />
~messages_byname(); </p>
<p>Destroys the facet. </p>
<p>Inherited from std::messages</p>
<h2>Member types</h2>
<p>Member type Definition<br />
char_type charT<br />
string_type std::basic_string&lt;charT&gt;</p>
<h2>Member objects</h2>
<p>Member name Type<br />
id (static) std::locale::id</p>
<h2>Member functions</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_open<br />
open <i>(public member function of std::messages&lt;CharT&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_get<br />
get <i>(public member function of std::messages&lt;CharT&gt;)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;invokes do_close<br />
close <i>(public member function of std::messages&lt;CharT&gt;)</i></p>
<h2>Protected member functions</h2>
<p>do_open opens a named message catalog<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::messages&lt;CharT&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_get retrieves a message from an open message catalog<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::messages&lt;CharT&gt;)</i><br />
<code>[virtual]</code> </p>
<p>do_close closes a message catalog<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(virtual protected member function of std::messages&lt;CharT&gt;)</i><br />
<code>[virtual]</code></p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;
void try_with(const std::locale &amp;loc)

{
    const std::messages&lt;char&gt; &amp;facet = std::use_facet&lt;std::messages&lt;char&gt;&gt;(loc)

        ;
    std::messages&lt;char&gt;::catalog cat = facet.open(&quot;sed&quot;, std::cout.getloc());
    if (cat &lt; 0)
        std::cout &lt;&lt; &quot;Could not open \&quot;sed\&quot; message catalog
&quot;;
    else
        std::cout &lt;&lt; &quot;\&quot;No match\&quot; &quot;
                  &lt;&lt; facet.get(cat, 0, 0, &quot;No match&quot;) &lt;&lt; '
'
                  &lt;&lt; &quot;\&quot;Memory exhausted\&quot; &quot;
                  &lt;&lt; facet.get(cat, 0, 0, &quot;Memory exhausted&quot;) &lt;&lt; '
';
    facet.close(cat);
}

int main()

{
    std::locale loc(&quot;en_US.utf8&quot;);
    std::cout.imbue(loc);
    try_with(std::locale(loc, new std::messages_byname&lt;char&gt;(&quot;de_DE.utf8&quot;)));
    try_with(std::locale(loc, new std::messages_byname&lt;char&gt;(&quot;fr_FR.utf8&quot;)));
    try_with(std::locale(loc, new std::messages_byname&lt;char&gt;(&quot;ja_JP.utf8&quot;)));
}
</code></pre>
<h2>Possible output:</h2>
<p>&nbsp;<wbr>&nbsp;&quot;No match&quot; Keine Übereinstimmung<br />
&nbsp;<wbr>&nbsp;&quot;Memory exhausted&quot; Speicher erschöpft<br />
&nbsp;<wbr>&nbsp;&quot;No match&quot; Pas de concordance<br />
&nbsp;<wbr>&nbsp;&quot;Memory exhausted&quot; Mémoire épuisée<br />
&nbsp;<wbr>&nbsp;&quot;No match&quot; 照合しません<br />
&nbsp;<wbr>&nbsp;&quot;Memory exhausted&quot; メモリーが足りません</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;implements retrieval of strings from message catalogs<br />
messages <i>(class template)</i> </p>
