---
title: "ustrtok(3)"
name: "ustrtok"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrtok/"
description: "ustrtok – Retrieves tokens from a string. Allegro game programming library."
---

<p>ustrtok &#8211; Retrieves tokens from a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrtok(char *s, const char *set);</code></pre>
<h2>Description</h2>
<p>This function retrieves tokens from `s&#8217; which are delimited by characters from `set&#8217;. To initiate the search, pass the string to be searched as `s&#8217;. For the remaining tokens, pass NULL instead. Warning: Since ustrtok alters the string it is parsing, you should always copy the string to a temporary buffer before parsing it. Also, this function is not re-entrant (ie. you cannot parse two strings at the same time). Example: </p>
<pre><code>char *word;
char string[] = &quot;some-words with dashes&quot;;
char *temp = ustrdup(string);
word = ustrtok(temp, &quot; -&quot;);
while (word) {
    allegro_message(&quot;Found `%s'
&quot;, word);
    word = ustrtok(NULL, &quot; -&quot;);
}
free(temp);</code></pre>
<h2>Return Value</h2>
<p>Returns a pointer to the token, or NULL if no more are found. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrchr/">ustrchr</a></code>(3), <code><a href="/docs/linux/man/3-ustrrchr/">ustrrchr</a></code>(3), <code><a href="/docs/linux/man/3-ustrstr/">ustrstr</a></code>(3), <code><a href="/docs/linux/man/3-ustrpbrk/">ustrpbrk</a></code>(3), <code><a href="/docs/linux/man/3-ustrtok_r/">ustrtok_r</a></code>(3), <code><a href="/docs/linux/man/3-allegro_message/">allegro_message</a></code>(3), <code><a href="/docs/linux/man/3-ustrncpy/">ustrncpy</a></code>(3), <code><a href="/docs/linux/man/3-exgui/">exgui</a></code>(3) </p>
