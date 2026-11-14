---
title: "stdmessagesclosestdmessagesdo_close(3)"
name: "stdmessagesclosestdmessagesdo_close"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdmessagesclosestdmessagesdo_close/"
---

std::messages&lt;CharT&gt;::close,std::messages&lt;CharT&gt;::do_close - std::messages&lt;CharT&gt;::close,std::messages&lt;CharT&gt;::do_close

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;locale&gt;

    public : (1)

                 void close(catalog c) const;

protected:
(2)

    virtual void do_close(catalog c) const;</code></pre> 
1) public member function, calls the protected virtual member function do_close of the most derived class. 
2) Releases the implementation-defined resources associated with an open catalog that is designated by the value c of type catalog (inherited from std::messages_base), which was obtained from open(). 

<h2>Parameters</h2>

c - a valid open catalog identifier, on which close() has not yet been called

<h2>Return value</h2>

<i>(none)</i> 

<h2>Notes</h2>

On POSIX systems, this function call usually translates to a call to catclose(). In GNU libstdc++, which is implemented in terms of GNU gettext(), it does nothing. 

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


