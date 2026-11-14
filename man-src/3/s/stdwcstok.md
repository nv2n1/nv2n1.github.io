---
title: "stdwcstok(3)"
name: "stdwcstok"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdwcstok/"
---

std::wcstok - std::wcstok

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;cwchar&gt;

    wchar_t *wcstok(wchar_t *str, const wchar_t *delim, wchar_t **ptr);</code></pre> 
Finds the next token in a null-terminated wide string pointed to by str. The separator characters are identified by null-terminated wide string pointed to by delim. 
This function is designed to be called multiples times to obtain successive tokens from the same string. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If str != NULL, the call is treated as the first call to std::wcstok for this particular wide string. The function searches for the first wide character which is not contained in delim. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If no such wide character was found, there are no tokens in str at all, and the function returns a null pointer. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If such wide character was found, it is the beginning of the token. The function then searches from that point on for the first wide character that is contained in delim. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If no such wide character was found, str has only one token, and future calls to std::wcstok will return a null pointer 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If such wide character was found, it is replaced by the null wide character L'\0' and the parser state (typically a pointer to the following wide character) is stored in the user-provided location *ptr. 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* The function then returns the pointer to the beginning of the token 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;* If str == NULL, the call is treated as a subsequent calls to std::wcstok: the function continues from where it left in previous invocation with the same *ptr. The behavior is the same as if the pointer to the wide character that follows the last detected token is passed as str. 

<h2>Parameters</h2>

str - pointer to the null-terminated wide string to tokenize 
delim - pointer to the null-terminated wide string identifying delimiters 
ptr - pointer to an object of type wchar_t*, which is used by wcstok to store its internal state

<h2>Return value</h2>

Pointer to the beginning of the next token or null pointer if there are no more tokens. 

<h2>Note</h2>

This function is destructive: it writes the L'\0' characters in the elements of the string str. In particular, a wide string literal cannot be used as the first argument of std::wcstok. 
Unlike std::strtok, this function does not update static storage: it stores the parser state in the user-provided location. 
Unlike most other tokenizers, the delimiters in std::wcstok can be different for each subsequent token, and can even depend on the contents of the previous tokens.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;cwchar&gt;

#include &lt;iostream&gt;
int main()

{
    wchar_t input[100] = L&quot;A bird came down the walk&quot;;
    wchar_t *buffer;
    wchar_t *token = std::wcstok(input, L&quot; &quot;, &amp;buffer);
    while (token) {
        std::wcout &lt;&lt; token &lt;&lt; '\n';
        token = std::wcstok(nullptr, L&quot; &quot;, &amp;buffer);
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

&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;finds the next token in a byte string 
strtok <i>(function)</i> 
