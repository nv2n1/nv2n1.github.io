---
title: "stdios_basesync_with_stdio(3)"
name: "stdios_basesync_with_stdio"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdios_basesync_with_stdio/"
---

std::ios_base::sync_with_stdio - std::ios_base::sync_with_stdio

<h2>Synopsis</h2>

<pre><code>static bool sync_with_stdio( bool sync = true );</code></pre> 
Sets whether the standard C++ streams are synchronized to the standard C streams after each input/output operation. 
The standard C++ streams are the following: std::cin, std::cout, std::cerr, std::clog, std::wcin, std::wcout, std::wcerr and std::wclog 
The standard C streams are the following: stdin, stdout and stderr 
For a standard stream str, synchronized with the C stream f, the following pairs of functions have identical effect: 
1) std::fputc(f, c) and str.rdbuf()-&gt;sputc(c) 
2) std::fgetc(f) and str.rdbuf()-&gt;sbumpc() 
3) std::ungetc(c, f) and str.rdbuf()-&gt;sputbackc(c) 
In practice, this means that the synchronized C++ streams are unbuffered, and each I/O operation on a C++ stream is immediately applied to the corresponding C stream's buffer. This makes it possible to freely mix C++ and C I/O. 
In addition, synchronized C++ streams are guaranteed to be thread-safe (individual characters output from multiple threads may interleave, but no data races occur) 
If the synchronization is turned off, the C++ standard streams are allowed to buffer their I/O independently, which may be considerably faster in some cases. 
By default, all eight standard C++ streams are synchronized with their respective C streams. 
If this function is called after I/O has occurred on the standard stream, the behavior is implementation-defined: implementations range from no effect to destroying the read buffer. 

<h2>Parameters</h2>

sync - the new synchronization setting

<h2>Return value</h2>

synchronization state before the call to the function 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cstdio&gt;
int main()

{
    std::ios::sync_with_stdio(false);
    std::cout &lt;&lt; &quot;a\n&quot;;
    std::printf(&quot;b\n&quot;);
    std::cout &lt;&lt; &quot;c\n&quot;;
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;b 
&nbsp;<wbr>&nbsp;a 
&nbsp;<wbr>&nbsp;c

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to the standard C output stream stdout 
cout (global object) 
wcout 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to the standard C error stream stderr, unbuffered 
cerr (global object) 
wcerr 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;writes to the standard C error stream stderr 
clog (global object) 
wclog 
