---
title: "stdstrtok(3)"
name: "stdstrtok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdstrtok/"
---

std::strtok - std::strtok

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cstring&gt;

    char *strtok(char *str, const char *delim);</code></pre> 
Finds the next token in a null-terminated byte string pointed to by str. The separator characters are identified by null-terminated byte string pointed to by delim. 
This function is designed to be called multiple times to obtain successive tokens from the same string. 
* If str != NULL, the call is treated as the first call to strtok for this particular string. The function searches for the first character which is not contained in delim. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If no such character was found, there are no tokens in str at all, and the function returns a null pointer. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If such character was found, is it the beginning of the token. The function then searches from that point on for the first character that is contained in delim. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If no such character was found, str has only one token, and the future calls to strtok will return a null pointer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If such character was found, it is replaced by the null character '\0' and the pointer to the following character is stored in a static location for subsequent invocations. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The function then returns the pointer to the beginning of the token 
* If str == NULL, the call is treated as a subsequent calls to strtok: the function continues from where it left in previous invocation. The behavior is the same as if the previously stored pointer is passed as str. 

<h2>Parameters</h2>

str - pointer to the null-terminated byte string to tokenize 
delim - pointer to the null-terminated byte string identifying delimiters

<h2>Return value</h2>

Pointer to the beginning of the next token or NULL if there are no more tokens. 

<h2>Notes</h2>

This function is destructive: it writes the '\0' characters in the elements of the string str. In particular, a string_literal cannot be used as the first argument of strtok. 
Each call to this function modifies a static variable: is not thread safe. 
Unlike most other tokenizers, the delimiters in strtok can be different for each subsequent token, and can even depend on the contents of the previous tokens. 

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cstring&gt;

#include &lt;iostream&gt;
int main()

{
    char input[100] = &quot;A bird came down the walk&quot;;
    char *token = std::strtok(input, &quot; &quot;);
    while (token != NULL) {
        std::cout &lt;&lt; token &lt;&lt; '\n';
        token = std::strtok(NULL, &quot; &quot;);
    }
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;A 
&nbsp;<wbr>&nbsp;bird 
&nbsp;<wbr>&nbsp;came 
&nbsp;<wbr>&nbsp;down 
&nbsp;<wbr>&nbsp;the 
&nbsp;<wbr>&nbsp;walk

<h2>See also</h2>

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the first location of any character from a set of separators 
strpbrk <i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the length of the maximum initial segment that consists 
strcspn of only the characters not found in another byte string 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;returns the length of the maximum initial segment that consists 
strspn of only the characters found in another byte string 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>(function)</i> 
