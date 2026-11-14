---
title: "stdrewind(3)"
name: "stdrewind"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdrewind/"
---

std::rewind - std::rewind

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    void rewind(std::FILE *stream);</code></pre> 
Moves the file position indicator to the beginning of the given file stream. 
The function is equivalent to std::fseek(stream, 0, SEEK_SET);, except that end-of-file and error indicators are cleared. 
The function drops any effects from previous calls to ungetc. 

<h2>Parameters</h2>

stream - file stream to modify

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;
int main()

{
    std::FILE *f;
    char ch;
    char str[20];
    f = std::fopen(&quot;file.txt&quot;, &quot;w&quot;);
    for (ch = '0'; ch &lt;= '9'; ch++) {
        std::fputc(ch, f);
    }
    std::fclose(f);

    std::FILE *f2 = std::fopen(&quot;file.txt&quot;, &quot;r&quot;);
    unsigned int size = std::fread(str, 1, 10, f2);
    std::puts(str);
    std::printf(&quot;\n%u\n&quot;, size);
    std::rewind(f2);
    unsigned int size2 = std::fread(str, 1, 10, f2);
    std::puts(str);
    std::printf(&quot;\n%u&quot;, size2);
    std::fclose(f2);
}
</code></pre>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;moves the file position indicator to a specific location in a file 
fseek <i>(function)</i> 
