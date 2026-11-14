---
title: "simulate_keypress(3)"
name: "simulate_keypress"
section: "3"
letter: "s"
url: "/docs/linux/man/3-simulate_keypress/"
description: "simulate_keypress – Stuffs a key into the keyboard buffer. Allegro game programming library."
---

<p>simulate_keypress &#8211; Stuffs a key into the keyboard buffer. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void simulate_keypress(int key);</code></pre>
<h2>Description</h2>
<p>Stuffs a key into the keyboard buffer, just as if the user had pressed it. The parameter is in the same format returned by readkey(). Example: </p>
<pre><code>simulate_keypress(KEY_SPACE &lt;&lt; 8);
if (readkey() == (KEY_SPACE &lt;&lt; 8))
    allegro_message(&quot;You simulated Alt+Space
&quot;);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-simulate_ukeypress/">simulate_ukeypress</a></code>(3), <code><a href="/docs/linux/man/3-keypressed/">keypressed</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3) </p>
