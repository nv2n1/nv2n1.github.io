---
title: "simulate_ukeypress-2(3)"
name: "simulate_ukeypress-2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-simulate_ukeypress-2/"
description: "simulate_ukeypress – Stuffs an unicode key into the keyboard buffer. Allegro game programming library."
---

<p>simulate_ukeypress &#8211; Stuffs an unicode key into the keyboard buffer. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void simulate_ukeypress(int key, int scancode);</code></pre>
<h2>Description</h2>
<p>Stuffs a key into the keyboard buffer, just as if the user had pressed it. The parameter is in the same format returned by ureadkey(). Example: </p>
<pre><code>/* We ignore the scancode simulation. */
simulate_ukeypress(0x00DF, 0);
if (ureadkey(&amp;scancode) == 0x00DF)
    allegro_message(&quot;You simulated sharp s
&quot;);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-simulate_keypress/">simulate_keypress</a></code>(3), <code><a href="/docs/linux/man/3-keypressed/">keypressed</a></code>(3), <code><a href="/docs/linux/man/3-ureadkey/">ureadkey</a></code>(3) </p>
