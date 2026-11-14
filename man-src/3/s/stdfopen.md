---
title: "stdfopen(3)"
name: "stdfopen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdfopen/"
---

std::fopen - std::fopen

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    std::FILE *fopen(const char *filename, const char *mode);</code></pre> 
Opens a file indicated by filename and returns a file stream associated with that file. mode is used to determine the file access mode. 

<h2>Parameters</h2>

filename - file name to associate the file stream to 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;null-terminated character string determining file access mode 

 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;File access Meaning Explanation Action if file Action if file 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mode string already exists does not exist 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;r&quot; read Open a file for reading read from start failure to open 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;w&quot; write Create a file for writing destroy contents create new 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;a&quot; append Append to a file write to end create new 
mode - &quot;r+&quot; read extended Open a file for read/write read from start error 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;w+&quot; write extended Create a file for read/write destroy contents create new 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&quot;a+&quot; append extended Open a file for read/write write to end create new 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;File access mode flag &quot;b&quot; can optionally be specified to open a file in_binary_mode. This flag has no effect on POSIX systems, but on Windows, for example, it disables special handling of '\n' and 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;'\x1A'. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;On the append file access modes, data is written to the end of the file regardless of the current position of the file position indicator. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;File access mode flag &quot;x&quot; can optionally be appended to &quot;w&quot; or &quot;w+&quot; specifiers. This flag forces the function to fail if the file exists, instead of overwriting it. <i>(C++17)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;The behavior is undefined if the mode is not one of the strings listed above. Some implementations define additional supported modes (e.g. Windows).

<h2>Return value</h2>

If successful, returns a pointer to the object that controls the opened file stream, with both eof and error bits cleared. The stream is fully buffered unless filename refers to an interactive device. 
On error, returns a null pointer. POSIX_requires that errno is set in this case. 

<h2>Notes</h2>

The format of filename is implementation-defined, and does not necessarily refer to a file (e.g. it may be the console or another device accessible through filesystem API). On platforms that support them, filename may include absolute or relative filesystem path. 
For portable directory and file naming, see C++_filesystem_library or boost.filesystem 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstdio&gt;

#include &lt;cstdlib&gt;
int main()

{
    FILE *fp = std::fopen(&quot;test.txt&quot;, &quot;r&quot;);
    if (!fp) {
        std::perror(&quot;File opening failed&quot;);
        return EXIT_FAILURE;
    }
    int c;                                // note: int, not char, required to handle EOF
    while ((c = std::fgetc(fp)) != EOF) { // standard C I/O file reading loop
        std::putchar(c);
    }
    if (std::ferror(fp))
        std::puts(&quot;I/O error when reading&quot;);
    else if (std::feof(fp))
        std::puts(&quot;End of file reached successfully&quot;);
    std::fclose(fp);
}
</code></pre>

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;closes a file 
fclose <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;synchronizes an output stream with the actual file 
fflush <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;open an existing stream with a different name 
freopen <i>(function)</i> 
