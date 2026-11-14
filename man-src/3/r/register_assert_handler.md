---
title: "register_assert_handler(3)"
name: "register_assert_handler"
section: "3"
letter: "r"
url: "/docs/linux/man/3-register_assert_handler/"
description: "register_assert_handler – Registers a custom handler for assert failures. Allegro game programming library."
---

<p>register_assert_handler &#8211; Registers a custom handler for assert failures. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void register_assert_handler(int (*handler)(const char *msg));</code></pre>
<h2>Description</h2>
<p>Supplies a custom handler function for dealing with assert failures. Your callback will be passed a formatted error message in ASCII, and should return non-zero if it has processed the error, or zero to continue with the default actions. You could use this to ignore assert failures, or to display the error messages on a graphics mode screen without aborting the program. You can call this function even when Allegro has not been initialised. Example: </p>
<pre><code>int show_but_continue(const char *text)
{
    alert(&quot;Uh oh...&quot;, &quot;Fasten your seat belts.&quot;, text,
          &quot;&amp;Go on!&quot;, NULL, 'g', 0);
    return 1;
}
... register_assert(show_but_continue);
ASSERT(0); /* This won't crash the program now. */
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-al_assert/">al_assert</a></code>(3), <code><a href="/docs/linux/man/3-assert/">ASSERT</a></code>(3), <code><a href="/docs/linux/man/3-register_trace_handler/">register_trace_handler</a></code>(3) </p>
