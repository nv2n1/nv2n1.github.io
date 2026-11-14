---
title: "stdfgets(3)"
name: "stdfgets"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfgets/"
---

std::fgets - std::fgets

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    char *fgets(char *str, int count, std::FILE *stream);</code></pre> 
Reads at most count - 1 characters from the given file stream and stores them in the character array pointed to by str. Reading stops if end-of-file occurs or a newline character is found, in which case str will contain that newline character. If no errors occur, writes a null character at the position immediately after the last character written to str. 

<h2>Parameters</h2>

str - pointer to an element of a char array 
count - maximum number of characters to write (typically the length of str) 
stream - file stream to read the data from

<h2>Return value</h2>

str on success, null pointer on failure. 
If the failure has been caused by end-of-file condition, additionally sets the eof indicator (see std::feof()) on stream. The contents of the array pointed to by str are not altered in this case. 
If the failure has been caused by some other error, sets the error indicator (see std::ferror()) on stream. The contents of the array pointed to by str are indeterminate (it may not even be null-terminated). 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdio&gt;

#include &lt;cstdlib&gt;
int main()

{
    std::FILE *tmpf = std::tmpfile();
    std::fputs(&quot;Alan Turing\n&quot;, tmpf);
    std::fputs(&quot;John von Neumann\n&quot;, tmpf);
    std::fputs(&quot;Alonzo Church\n&quot;, tmpf);
    std::rewind(tmpf);
    char buf[8];
    while (std::fgets(buf, sizeof buf, tmpf) != NULL) {
        std::cout &lt;&lt; '&quot;' &lt;&lt; buf &lt;&lt; '&quot;' &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;&quot;Alan Tu&quot; 
&nbsp;<wbr>&nbsp;&quot;ring 
&nbsp;<wbr>&nbsp;&quot; 
&nbsp;<wbr>&nbsp;&quot;John vo&quot; 
&nbsp;<wbr>&nbsp;&quot;n Neuma&quot; 
&nbsp;<wbr>&nbsp;&quot;nn 
&nbsp;<wbr>&nbsp;&quot; 
&nbsp;<wbr>&nbsp;&quot;Alonzo &quot; 
&nbsp;<wbr>&nbsp;&quot;Church 
&nbsp;<wbr>&nbsp;&quot;

<h2>See also</h2>

scanf reads formatted input from stdin, a file stream or a buffer 
fscanf <i>(function)</i> 
sscanf 
gets reads a character string from stdin 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
(deprecated in C++11) 
(removed in C++14) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a character string to a file stream 
fputs <i>(function)</i> 
