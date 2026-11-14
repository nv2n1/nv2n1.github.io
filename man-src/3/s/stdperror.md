---
title: "stdperror(3)"
name: "stdperror"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdperror/"
---

std::perror - std::perror

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstdio&gt;

    void perror(const char *s);</code></pre> 
Prints a textual description of the error code currently stored in the system variable errno to stderr. 
The description is formed by concatenating the following components: 
* the contents of the null-terminated byte string pointed to by s, followed by &quot;: &quot; (unless s is a null pointer or the character pointed to by s is the null character) 
* implementation-defined error message string describing the error code stored in errno, followed by '\n'. The error message string is identical to the result of std::strerror(errno). 

<h2>Parameters</h2>

s - pointer to a null-terminated string with explanatory message

<h2>Return value</h2>

<i>(none)</i> 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cstdio&gt;
int main()

{
    double not_a_number = std::log(-1.0);
    if (errno == EDOM) {
        std::perror(&quot;log(-1) failed&quot;);
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;log(-1) failed: Numerical argument out of domain

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;macro which expands to POSIX-compatible thread-local error number variable 
errno (macro variable) 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns a text version of a given error code 
strerror <i>(function)</i> 
