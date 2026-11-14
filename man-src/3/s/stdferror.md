---
title: "stdferror(3)"
name: "stdferror"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdferror/"
---

std::ferror - std::ferror

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    int ferror(std::FILE *stream);</code></pre> 
Checks the given stream for errors. 

<h2>Parameters</h2>

stream - the file stream to check

<h2>Return value</h2>

Nonzero value if the file stream has errors occurred, 0 otherwise 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;

#include &lt;cstdlib&gt;

#include &lt;clocale&gt;

#include &lt;cwchar&gt;
int main(void)

{
    const char *fname = std::tmpnam(nullptr);
    std::FILE *f = std::fopen(fname, &quot;wb&quot;);
    std::fputs(&quot;\xff\xff\n&quot;, f); // not a valid UTF-8 character sequence
    std::fclose(f);
    std::setlocale(LC_ALL, &quot;en_US.utf8&quot;);
    f = std::fopen(fname, &quot;rb&quot;);
    std::wint_t ch;
    while ((ch = std::fgetwc(f)) != WEOF) // attempt to read as UTF-8
        std::printf(&quot;%#x &quot;, ch);
    if (std::feof(f))
        puts(&quot;EOF indicator set&quot;);
    if (std::ferror(f))
        puts(&quot;Error indicator set&quot;);
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;Error indicator set

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;clears errors 
clearerr <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks for the end-of-file 
feof <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;checks if an error has occurred 
fail <i>(public member function of std::basic_ios&lt;CharT,Traits&gt;)</i> 
