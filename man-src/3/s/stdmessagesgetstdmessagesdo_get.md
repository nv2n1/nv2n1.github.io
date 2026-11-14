---
title: "stdmessagesgetstdmessagesdo_get(3)"
name: "stdmessagesgetstdmessagesdo_get"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmessagesgetstdmessagesdo_get/"
---

std::messages&lt;CharT&gt;::get,std::messages&lt;CharT&gt;::do_get - std::messages&lt;CharT&gt;::get,std::messages&lt;CharT&gt;::do_get

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 string_type get(catalog cat, int set, int msgid, const string_type &amp;dfault) const;

protected:
(2)

    virtual string_type do_get(catalog cat, int set, int msgid, const string_type &amp;dfault) const;</code></pre> 
1) Public member function, calls the protected virtual member function do_get of the most derived class. 
2) Obtains a message from the open message catalog cat using the values set, msgid and dfault in implementation-defined manner. If the expected message is not found in the catalog, returns a copy of dfault. 

<h2>Parameters</h2>

cat - identifier of message catalog obtained from open() and not yet passed to close() 
set - implementation-defined argument, message set in POSIX 
msgid - implementation-defined argument, message id in POSIX 
dfault - the string to look up in the catalog (if the catalog uses string look-up) and also the string to return in case of a failure

<h2>Return value</h2>

The message from the catalog or a copy of dfault if none was found. 

<h2>Notes</h2>

On POSIX systems, this function call usually translates to a call to catgets(), and the parameters set, msgid, and dfault are passed to catgets() as-is. In GNU libstdc++, this function ignores set and msgid and simply calls GNU gettext(dfault) in the required locale. 

<h2>Example</h2>

The following example demonstrated retrieval of messages: on a typical GNU/Linux system it reads from /usr/share/locale/de/LC_MESSAGES/sed.mo 
 // Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;locale&gt;
int main()

{
    std::locale loc(&quot;de_DE.utf8&quot;);
    std::cout.imbue(loc);
    auto &amp;facet = std::use_facet&lt;std::messages&lt;char&gt;&gt;(loc);
    auto cat = facet.open(&quot;sed&quot;, loc);
    if (cat &lt; 0)
        std::cout &lt;&lt; &quot;Could not open german \&quot;sed\&quot; message catalog\n&quot;;
    else
        std::cout &lt;&lt; &quot;\&quot;No match\&quot; in German: &quot;
                  &lt;&lt; facet.get(cat, 0, 0, &quot;No match&quot;) &lt;&lt; '\n'
                  &lt;&lt; &quot;\&quot;Memory exhausted\&quot; in German: &quot;
                  &lt;&lt; facet.get(cat, 0, 0, &quot;Memory exhausted&quot;) &lt;&lt; '\n';
    facet.close(cat);
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;&quot;No match&quot; in German: Keine Übereinstimmung 
&nbsp;<wbr>&nbsp;&quot;Memory exhausted&quot; in German: Speicher erschöpft

<h2>See also</h2>


