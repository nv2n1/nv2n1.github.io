---
title: "stdfwrite(3)"
name: "stdfwrite"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfwrite/"
---

std::fwrite - std::fwrite

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    std::size_t fwrite(const void *buffer, std::size_t size, std::size_t count, std::FILE *stream);</code></pre> 
Writes up to count binary objects from the given array buffer to the output stream stream. The objects are written as if by reinterpreting each object as an array of unsigned char and calling std::fputc size times for each object to write those unsigned chars into stream, in order. The file position indicator for the stream is advanced by the number of characters written. 
If the objects are not TriviallyCopyable, the behavior is undefined. 
If an error occurs, the resulting value of the file position indicator for the stream is indeterminate. 

<h2>Parameters</h2>

buffer - pointer to the first object object in the array to be written 
size - size of each object 
count - the number of the objects to be written 
stream - output file stream to write to

<h2>Return value</h2>

Number of objects written successfully, which may be less than count if an error occurred. 
If size or count is zero, fwrite returns zero and performs no other action. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;

#include &lt;vector&gt;

#include &lt;array&gt;
int main()

{
    // write buffer to file
    if (std::FILE *f1 = std::fopen(&quot;file.bin&quot;, &quot;wb&quot;)) {
        std::array&lt;int, 3&gt; v = {42, -1, 7}; // underlying storage of std::array is an array
        std::fwrite(v.data(), sizeof v[0], v.size(), f1);
        std::fclose(f1);
    }
    // read the same data and print it to the standard output
    if (std::FILE *f2 = std::fopen(&quot;file.bin&quot;, &quot;rb&quot;)) {
        std::vector&lt;int&gt; rbuf(10); // underlying storage of std::vector is also an array
        std::size_t sz = std::fread(rbuf.data(), sizeof rbuf[0], rbuf.size(), f2);
        std::fclose(f2);
        for (std::size_t n = 0; n &lt; sz; ++n) {
            std::printf(&quot;%d\n&quot;, rbuf[n]);
        }
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;42 
&nbsp;<wbr>&nbsp;-1 
&nbsp;<wbr>&nbsp;7

<h2>See also</h2>

printf 
fprintf 
sprintf 
snprintf prints formatted output to stdout, a file stream or a buffer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
<i>(C++11)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes a character string to a file stream 
fputs <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;reads from a file 
fread <i>(function)</i> 
