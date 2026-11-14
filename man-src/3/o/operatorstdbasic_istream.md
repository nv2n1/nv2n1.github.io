---
title: "operatorstdbasic_istream(3)"
name: "operatorstdbasic_istream"
section: "3"
letter: "o"
url: "/docs/linux/man/3-operatorstdbasic_istream/"
description: "operator>>(std::basic_istream) – operator>>(std::basic_istream)"
---

<p>operator&gt;&gt;(std::basic_istream) &#8211; operator&gt;&gt;(std::basic_istream)</p>
<h2>Synopsis</h2>
<pre><code>template &lt;class CharT, class Traits&gt;

basic_istream&lt;CharT, Traits&gt; &amp;operator&gt;&gt;(basic_istream&lt;CharT, Traits&gt; &amp;st, CharT &amp;ch);
template &lt;class Traits&gt;
(1)

    basic_istream&lt;char, Traits&gt; &amp;
    operator&gt;&gt;(basic_istream&lt;char, Traits&gt; &amp;st, signed char &amp;ch);
template &lt;class Traits&gt;

basic_istream&lt;char, Traits&gt; &amp;operator&gt;&gt;(basic_istream&lt;char, Traits&gt; &amp;st, unsigned char &amp;ch);

template &lt;class CharT, class Traits&gt;

basic_istream&lt;CharT, Traits&gt; &amp;operator&gt;&gt;(basic_istream&lt;CharT, Traits&gt; &amp;st, CharT *s);
template &lt;class Traits&gt;
(until C++ 20)

    basic_istream&lt;char, Traits&gt; &amp;
    operator&gt;&gt;(basic_istream&lt;char, Traits&gt; &amp;st, signed char *s);</code></pre>
<p>template&lt; class Traits &gt;<br />
basic_istream&lt;char,Traits&gt;&amp; operator&gt;&gt;( basic_istream&lt;char,Traits&gt;&amp; st, unsigned char* s );<br />
template&lt; class CharT, class Traits, std::size_t N &gt;<br />
basic_istream&lt;CharT,Traits&gt;&amp; operator&gt;&gt;( basic_istream&lt;CharT,Traits&gt;&amp; st, CharT (&amp;s)[N] ); <code>(2)</code> template &lt;class Traits, std::size_t N&gt;<br />
(since C++ 20)</p>
<p>    basic_istream&lt;char, Traits&gt; &amp;<br />
    operator&gt;&gt;(basic_istream&lt;char, Traits&gt; &amp;st, signed char (&amp;s)[N]);<br />
template &lt;class Traits, std::size_t N&gt;</p>
<p>basic_istream&lt;char, Traits&gt; &amp;operator&gt;&gt;(basic_istream&lt;char, Traits&gt; &amp;st, unsigned char (&amp;s)[N]);</p>
<p>template &lt;class CharT, class Traits, class T&gt;<br />
(since C++ 11)</p>
<p>    basic_istream&lt;CharT, Traits&gt; &amp;<br />
    operator&gt;&gt;(basic_istream&lt;CharT, Traits&gt; &amp;&amp;st, T &amp;value);<br />
(3)(until C++ 17)</p>
<p>    template &lt;class CharT, class Traits, class T&gt;<br />
    (since C++ 17)</p>
<p>        basic_istream&lt;CharT, Traits&gt; &amp;<br />
        operator&gt;&gt;(basic_istream&lt;CharT, Traits&gt; &amp;&amp;st, T &amp;&amp;value);</p>
<p>1-2) Performs character input operations.<br />
1) Behaves as an FormattedInputFunction. After constructing and checking the sentry object, which may skip leading whitespace, extracts a character and stores it to ch. If no character is available, sets failbit (in addition to eofbit that is set as required of a FormattedInputFunction).<br />
2) Behaves as an FormattedInputFunction. After constructing and checking the sentry object, which may skip leading whitespace, extracts successive characters and stores them at successive locations of<br />
a character array whose first element is pointed to by<br />
<i>(until C++20)</i> s. The extraction stops if one of the following conditions are met:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* a whitespace character (as determined by the ctype&lt;CharT&gt; facet) is found. The whitespace character is not extracted.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* st.width() &#8211; 1 characters are extracted (if st.width() is greater than zero) <i>(until C++20)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* min(std::size_t(st.width()), N) &#8211; 1 characters are extracted (if st.width() is greater than zero) <i>(since C++20)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* N &#8211; 1 characters are extracted otherwise<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* end of file occurs in the input sequence (this also sets eofbit)<br />
In either case, an additional null character value CharT() is stored at the end of the output. If no characters were extracted, sets failbit (the null character is still written, to the first position in the output). Finally, calls st.width<code>(0)</code> to cancel the effects of std::setw, if any.<br />
3)<br />
Calls the appropriate extraction operator, given an rvalue reference to an input stream object (equivalent to st &gt;&gt; value). <i>(since C++11)</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++17)</i><br />
Calls the appropriate extraction operator, given an rvalue reference to an input stream object (equivalent to st &gt;&gt; std::forward&lt;T&gt;(value)). This function does not participate in overload resolution unless the expression st &gt;&gt; std::forward&lt;T&gt;(value) is well-formed. <i>(since C++17)</i> </p>
<h2>Notes</h2>
<p>Extracting a single character that is the last character of the stream does not set eofbit: this is different from other formatted input functions, such as extracting the last integer with operator&gt;&gt;, but this behavior matches the behavior of std::scanf with &quot;%c&quot; format specifier. </p>
<h2>Parameters</h2>
<p>st &#8211; input stream to extract the data from<br />
ch &#8211; reference to a character to store the extracted character to </p>
<p>s &#8211; pointer to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(until C++20)</i> a character array to store the extracted characters to</p>
<h2>Return value</h2>
<p>st </p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;sstream&gt;
int main()

{
    std::string input = &quot;n greetings&quot;;
    std::istringstream stream(input);
    char c;
    const int MAX = 6;
    char cstr[MAX];
    stream &gt;&gt; c &gt;&gt; std::setw(MAX) &gt;&gt; cstr;
    std::cout &lt;&lt; &quot;c = &quot; &lt;&lt; c &lt;&lt; '
'
              &lt;&lt; &quot;cstr = &quot; &lt;&lt; cstr &lt;&lt; '
';
    double f;
    std::istringstream(&quot;1.23&quot;) &gt;&gt; f; // rvalue stream extraction
    std::cout &lt;&lt; &quot;f = &quot; &lt;&lt; f &lt;&lt; '
';
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;c = n<br />
&nbsp;<wbr>&nbsp;cstr = greet<br />
&nbsp;<wbr>&nbsp;f = 1.23</p>
<h2>See also</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extracts formatted data<br />
operator&gt;&gt; <i>(public member function)</i> </p>
