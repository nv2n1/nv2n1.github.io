---
title: "stdquoted(3)"
name: "stdquoted"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdquoted/"
description: "std::quoted – std::quoted"
---

<p>std::quoted &#8211; std::quoted</p>
<h2>Synopsis</h2>
<pre><code>Defined in header&lt;iomanip&gt;

    template &lt;class CharT&gt;

    /*unspecified*/ quoted(const CharT *s, (1)(since C++ 14)

                                               CharT delim = CharT('&quot;'),
                           CharT escape = CharT('\'));

template &lt;class CharT, class Traits, class Allocator&gt;

/*unspecified*/ quoted(const std::basic_string&lt;CharT, Traits, Allocator&gt; &amp;s, (2)(since C++ 14)

                                                                                 CharT delim = CharT('&quot;'),
                       CharT escape = CharT('\'));

template &lt;class CharT, class Traits&gt;

/*unspecified*/ quoted(std::basic_string_view&lt;CharT, Traits&gt; s, (3)(since C++ 17)

                                                                    CharT delim = CharT('&quot;'),
                       CharT escape = CharT('\'));

template &lt;class CharT, class Traits, class Allocator&gt;

/*unspecified*/ quoted(std::basic_string&lt;CharT, Traits, Allocator&gt; &amp;s, (4)(since C++ 14)

                                                                           CharT delim = CharT('&quot;'),
                       CharT escape = CharT('\'));</code></pre>
<p>Allows insertion and extraction of quoted strings, such as the ones found in CSV or XML.<br />
When used in an expression out &lt;&lt; quoted(s, delim, escape), where out is an output stream with char_type equal to CharT and, for overloads 2-4, traits_type equal to Traits, behaves as a FormattedOutputFunction, which inserts into out a sequence of characters seq constructed as follows:<br />
a) First, the character delim is added to the sequence<br />
b) Then every character from s, except if the next character to output equals delim or equals escape (as determined by the stream&#8217;s traits_type::eq), then first appends an extra copy of escape<br />
c) In the end, delim is appended to seq once more<br />
Then, if seq.size() &lt; out.width(), adds out.width()-seq.size() copies of the fill character out.fill() either at the end of the sequence (if ios_base::left is set in out.flags()) or at the beginning of the sequence (in all other cases).<br />
Finally, outputs each character from the resulting sequence as if by calling out.rdbuf()-&gt;sputn(seq, n), where n=std::max(out.width(), seq.size()) and out.width<code>(0)</code> to cancel the effects of std::setw, if any.<br />
4) When used in an expression in &gt;&gt; quoted(s, delim, escape), where in is an input stream with char_type equal to CharT and traits_type equal to Traits, extracts characters from in, using std::basic_istream::operator&gt;&gt;, according to the following rules:<br />
a) If the first character extracted does not equal delim (as determined by the stream&#8217;s traits_type::eq), then simply performs in &gt;&gt; s.<br />
b) Otherwise (if the first character is the delimiter):<br />
1) Turns off the skipws flag on the input stream<br />
2) Empties the destination string by calling s.clear()<br />
3) Extracts characters from in and appends them to s, except that whenever an escape character is extracted, it is ignored and the next character is appended to s. Extraction stops when !in==true or when an unescaped delim character is found.<br />
4) Discards the final (unescaped) delim character.<br />
5) Restores the skipws flag on the input stream to its original value. </p>
<h2>Parameters</h2>
<p>s &#8211; the string to insert or extract<br />
delim &#8211; the character to use as the delimiter, defaults to &quot;<br />
escape &#8211; the character to use as the escape character, defaults to \</p>
<h2>Return value</h2>
<p>Returns an object of unspecified type such that the described behavior takes place. </p>
<h2>Exceptions</h2>
<p>Throws std::ios_base::failure if operator&gt;&gt; or operator&lt;&lt; throws.</p>
<h2>Example</h2>
<p>// Run this code </p>
<pre><code>#include &lt;iostream&gt;

#include &lt;iomanip&gt;

#include &lt;sstream&gt;
int main()

{
    std::stringstream ss;
    std::string in = &quot;String with spaces, and embedded \&quot;quotes\&quot; too&quot;;
    std::string out;
    ss &lt;&lt; std::quoted(in);
    std::cout &lt;&lt; &quot;read in     [&quot; &lt;&lt; in &lt;&lt; &quot;]
&quot;
              &lt;&lt; &quot;stored as   [&quot; &lt;&lt; ss.str() &lt;&lt; &quot;]
&quot;;
    ss &gt;&gt; std::quoted(out);
    std::cout &lt;&lt; &quot;written out [&quot; &lt;&lt; out &lt;&lt; &quot;]
&quot;;
}
</code></pre>
<h2>Output:</h2>
<p>&nbsp;<wbr>&nbsp;read in [String with spaces, and embedded &quot;quotes&quot; too]<br />
&nbsp;<wbr>&nbsp;stored as [&quot;String with spaces, and embedded \&quot;quotes\&quot; too&quot;]<br />
&nbsp;<wbr>&nbsp;written out [String with spaces, and embedded &quot;quotes&quot; too]</p>
<h2>See also</h2>
