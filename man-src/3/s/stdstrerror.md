---
title: "stdstrerror(3)"
name: "stdstrerror"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrerror/"
---

std::strerror - std::strerror

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    char *strerror(int errnum);</code></pre> 
Returns a pointer to the textual description of the system error code errnum, identical to the description that would be printed by std::perror(). 
errnum is usually acquired from the errno variable, however the function accepts any value of type int. The contents of the string are locale-specific. 
The returned string must not be modified by the program, but may be overwritten by a subsequent call to the strerror function. strerror is not required to be thread-safe. Implementations may be returning different pointers to static read-only string literals or may be returning the same pointer over and over, pointing at a static buffer in which strerror places the string. 

<h2>Parameters</h2>

errnum - integral value referring to a error code

<h2>Return value</h2>

Pointer to a null-terminated byte string corresponding to the errno error code errnum. 

<h2>Notes</h2>

POSIX allows subsequent calls to strerror to invalidate the pointer value returned by an earlier call. It also specifies that it is the LC_MESSAGES locale facet that controls the contents of these messages. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;iostream&gt;

#include &lt;cmath&gt;

#include &lt;cerrno&gt;

#include &lt;cstring&gt;

#include &lt;clocale&gt;
int main()

{
    double not_a_number = std::log(-1.0);
    if (errno == EDOM) {
        std::cout &lt;&lt; &quot;log(-1) failed: &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '\n';
        std::setlocale(LC_MESSAGES, &quot;de_DE.utf8&quot;);
        std::cout &lt;&lt; &quot;Or, in German, &quot; &lt;&lt; std::strerror(errno) &lt;&lt; '\n';
    }
}
</code></pre>

<h2>Possible output:</h2>

&nbsp;<wbr>&nbsp;log(-1) failed: Numerical argument out of domain 
&nbsp;<wbr>&nbsp;Or, in German, Das numerische Argument ist ausserhalb des Definitionsbereiches

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;displays a character string corresponding of the current error to stderr 
perror <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;macros for standard POSIX-compatible error conditions 
E2BIG,_EACCES,_...,_EXDEV (macro constant) 
