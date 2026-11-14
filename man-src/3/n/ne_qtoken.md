---
title: "ne_qtoken(3)"
name: "ne_qtoken"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_qtoken/"
description: "ne_token, ne_qtoken – string tokenizers"
---

<p>ne_token, ne_qtoken &#8211; string tokenizers</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_string.h&gt;

char *ne_token(char **str, char sep);

char *ne_qtoken(char **str, char sep, const char *quotes);</code></pre>
<h2>Description</h2>
<p><code>ne_token</code></p>
<dd>and <code>ne_qtoken</code> tokenize the string at the location stored in the pointer <i>str</i>. Each time the function is called, it returns the next token, and modifies the <i>str</i> pointer to point to the remainer of the string, or NULL if there are no more tokens in the string. A token is delimited by the separator character <i>sep</i>; if <code>ne_qtoken</code> is used any quoted segments of the string are skipped when searching for a separator. A quoted segment is enclosed in a pair of one of the characters given in the <i>quotes</i> string. </p>
<p> The string being tokenized is modified each time the tokenizing function is called; replacing the next separator character with a NUL terminator.</p>
<h2>Examples</h2>
<p>The following function prints out each token in a comma-separated string <i>list</i>, which is modified in-place: </p>
<pre><code>static void splitter(char *list)
{
    do {
        printf(&quot;Token: %s
&quot;, ne_token(&amp;list, ','));
        while (list)
            ;
    }</code></pre>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
