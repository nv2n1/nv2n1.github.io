---
title: "ustrtok_r(3)"
name: "ustrtok_r"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrtok_r/"
description: "ustrtok_r – Reentrant function to retrieve tokens from a string. Allegro game programming library."
---

<p>ustrtok_r &#8211; Reentrant function to retrieve tokens from a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrtok_r(char *s, const char *set, char **last);</code></pre>
<h2>Description</h2>
<p>Reentrant version of ustrtok. The `last&#8217; parameter is used to keep track of where the parsing is up to and must be a pointer to a char * variable allocated by the user that remains the same while parsing the same string. Example: </p>
<pre><code>char *word, *last;
char string[] = &quot;some-words with dashes&quot;;
char *temp = ustrdup(string);
word = ustrtok_r(string, &quot; -&quot;, &amp;last);
while (word) {
    allegro_message(&quot;Found `%s'
&quot;, word);
    word = ustrtok_r(NULL, &quot; -&quot;, &amp;last);
}
free(temp);</code></pre>
<h2>Return Value</h2>
<p>Returns a pointer to the token, or NULL if no more are found. You can free the memory pointed to by `last&#8217; once NULL is returned. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ustrtok/">ustrtok</a></code>(3) </p>
