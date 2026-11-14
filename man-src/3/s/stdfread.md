---
title: "stdfread(3)"
name: "stdfread"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfread/"
---

std::fread - std::fread

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    std::size_t fread(void *buffer, std::size_t size, std::size_t count, std::FILE *stream);</code></pre> 
Reads up to count objects into the array buffer from the given input stream stream as if by calling std::fgetc size times for each object, and storing the results, in the order obtained, into the successive positions of buffer, which is reinterpreted as an array of unsigned char. The file position indicator for the stream is advanced by the number of characters read. 
If the objects are not TriviallyCopyable, the behavior is undefined. 
If an error occurs, the resulting value of the file position indicator for the stream is indeterminate. If a partial element is read, its value is indeterminate. 

<h2>Parameters</h2>

buffer - pointer to the first object in the array to be read 
size - size of each object in bytes 
count - the number of the objects to be read 
stream - input file stream to read from

<h2>Return value</h2>

Number of objects read successfully, which may be less than count if an error or end-of-file condition occurs. 
If size or count is zero, fread returns zero and performs no other action. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdio&gt;

#include &lt;fstream&gt;

#include &lt;vector&gt;

int main()

{
    // prepare file
    std::ofstream(&quot;test.txt&quot;) &lt;&lt; 1 &lt;&lt; ' ' &lt;&lt; 2 &lt;&lt; '\n';
    std::FILE *f = std::fopen(&quot;test.txt&quot;, &quot;r&quot;);
    std::vector&lt;char&gt; buf(4); // char is trivally copyable
    std::fread(&amp;buf[0], sizeof buf[0], buf.size(), f);
    for (char n : buf)
        std::cout &lt;&lt; n;
    std::vector&lt;std::string&gt; buf2; // string is not trivially copyable

    // this would result in undefined behavior

    //    std::fread(&amp;buf2[0], sizeof buf2[0], buf2.size(), f);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;1 2

<h2>See also</h2>

scanf reads formatted input from stdin, a file stream or a buffer 
fscanf <i>(function)</i> 
sscanf 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gets a character string from a file stream 
fgets <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to a file 
fwrite <i>(function)</i> 
