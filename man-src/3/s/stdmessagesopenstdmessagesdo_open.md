---
title: "stdmessagesopenstdmessagesdo_open(3)"
name: "stdmessagesopenstdmessagesdo_open"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmessagesopenstdmessagesdo_open/"
---

std::messages&lt;CharT&gt;::open,std::messages&lt;CharT&gt;::do_open - std::messages&lt;CharT&gt;::open,std::messages&lt;CharT&gt;::do_open

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 catalog open(const std::basic_string&lt;char&gt; &amp;name, const std::locale &amp;loc) const;

protected:
(2)

    virtual catalog do_open(const std::basic_string&lt;char&gt; &amp;name, const std::locale &amp;loc) const;</code></pre> 
1) Public member function, calls the protected virtual member function do_open of the most derived class. 
2) Obtains a value of type catalog (inherited from std::messages_base), which can be passed to get() to retrieve messages from the message catalog named by name. This value is usable until passed to close(). 

<h2>Parameters</h2>

name - name of the message catalog to open 
loc - a locale object that provides additional facets that may be required to read messages from the catalog, such as std::codecvt to perform wide/multibyte conversions

<h2>Return value</h2>

The non-negative value of type catalog that can be used with get() and close(). Returns a negative value if the catalog could not be opened. 

<h2>Notes</h2>

On POSIX systems, this function call usually translates to a call to catopen(). In GNU libstdc++, it calls textdomain. 
The actual catalog location is implementation-defined: for the catalog &quot;sed&quot; (message catalogs installed with the Unix utility 'sed') in German locale, for example, the file opened by this function call may be /usr/lib/nls/msg/de_DE/sed.cat, /usr/lib/locale/de_DE/LC_MESSAGES/sed.cat, or /usr/share/locale/de/LC_MESSAGES/sed.mo. 

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


