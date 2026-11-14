---
title: "stdgetline(3)"
name: "stdgetline"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdgetline/"
---

std::getline - std::getline

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;string&gt;

template&lt; class CharT, class Traits, class Allocator &gt;

std::basic_istream&lt;CharT,Traits&gt;&amp; getline( std::basic_istream&lt;CharT,Traits&gt;&amp; input,  (1)

std::basic_string&lt;CharT,Traits,Allocator&gt;&amp; str,

CharT delim );

template&lt; class CharT, class Traits, class Allocator &gt;

std::basic_istream&lt;CharT,Traits&gt;&amp; getline( std::basic_istream&lt;CharT,Traits&gt;&amp;&amp; input, (1) (since C++11)

std::basic_string&lt;CharT,Traits,Allocator&gt;&amp; str,

CharT delim );

template&lt; class CharT, class Traits, class Allocator &gt;

std::basic_istream&lt;CharT,Traits&gt;&amp; getline( std::basic_istream&lt;CharT,Traits&gt;&amp; input,  (2)

std::basic_string&lt;CharT,Traits,Allocator&gt;&amp; str );

template&lt; class CharT, class Traits, class Allocator &gt;

std::basic_istream&lt;CharT,Traits&gt;&amp; getline( std::basic_istream&lt;CharT,Traits&gt;&amp;&amp; input, (2) (since C++11)

std::basic_string&lt;CharT,Traits,Allocator&gt;&amp; str );</code></pre> 
getline reads characters from an input stream and places them into a string: 
1) Behaves as UnformattedInputFunction, except that input.gcount() is not affected. After constructing and checking the sentry object, performs the following: 
1) Calls str.erase() 
2) Extracts characters from input and appends them to str until one of the following occurs (checked in the order listed) 
a) end-of-file condition on input, in which case, getline sets eofbit. 
b) the next available input character is delim, as tested by Traits::eq(c, delim), in which case the delimiter character is extracted from input, but is not appended to str. 
c) str.max_size() characters have been stored, in which case getline sets failbit and returns. 
3) If no characters were extracted for whatever reason (not even the discarded delimiter), getline sets failbit and returns. 
2) Same as getline(input, str, input.widen('\n')), that is, the default delimiter is the endline character. 

<h2>Parameters</h2>

input - the stream to get data from 
str - the string to put the data into 
delim - the delimiter character

<h2>Return value</h2>

input 

<h2>Notes</h2>

When used immediately after whitespace-delimited input, e.g. after int n; std::cin &gt;&gt; n;, getline consumes the endline character left on the input stream by operator&gt;&gt;, and returns immediately. A common solution is to ignore all leftover characters on the line of input with cin.ignore(std::numeric_limits&lt;std::streamsize&gt;::max(), '\n'); before switching to line-oriented input. 

<h2>Example</h2>

The following example demonstrates how to use getline function to read user's input and how to process file line by line. 
 // Run this code <pre><code>#include &lt;string&gt;

#include &lt;iostream&gt;

#include &lt;sstream&gt;
int main()

{
    // greet the user
    std::string name;
    std::cout &lt;&lt; &quot;What is your name? &quot;;
    std::getline(std::cin, name);
    std::cout &lt;&lt; &quot;Hello &quot; &lt;&lt; name &lt;&lt; &quot;, nice to meet you.\n&quot;;
    // read file line by line
    std::istringstream input;
    input.str(&quot;1\n2\n3\n4\n5\n6\n7\n&quot;);
    int sum = 0;
    for (std::string line; std::getline(input, line);) {
        sum += std::stoi(line);
    }
    std::cout &lt;&lt; &quot;\nThe sum is: &quot; &lt;&lt; sum &lt;&lt; &quot;\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;What is your name? John Q. Public 
&nbsp;<wbr>&nbsp;Hello John Q. Public, nice to meet you. 

 
&nbsp;<wbr>&nbsp;The sum is 28

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;extracts characters until the given character is found 
getline <i>(public member function of std::basic_istream&lt;CharT,Traits&gt;)</i> 
