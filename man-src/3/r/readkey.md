---
title: "readkey(3)"
name: "readkey"
section: "3"
letter: "r"
url: "/docs/linux/man/3-readkey/"
description: "readkey – Returns the next character from the keyboard buffer. Allegro game programming library."
---

<p>readkey &#8211; Returns the next character from the keyboard buffer. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int readkey();</code></pre>
<h2>Description</h2>
<p>Returns the next character from the keyboard buffer, in ASCII format. If the buffer is empty, it waits until a key is pressed. You can see if there are queued keypresses with keypressed(). The low byte of the return value contains the ASCII code of the key, and the high byte the scancode. The scancode remains the same whatever the state of the shift, ctrl and alt keys, while the ASCII code is affected by shift and ctrl in the normal way (shift changes case, ctrl+letter gives the position of that letter in the alphabet, eg. ctrl+A = 1, ctrl+B = 2, etc). Pressing alt+key returns only the scancode, with a zero ASCII code in the low byte. For example: </p>
<pre><code>int val;
... val = readkey();
if ((val &amp; 0xff) == 'd') /* by ASCII code */
    allegro_message(&quot;You pressed 'd'
&quot;);

if ((val &gt;&gt; 8) == KEY_SPACE) /* by scancode */
    allegro_message(&quot;You pressed Space
&quot;);

if ((val &amp; 0xff) == 3) /* ctrl+letter */
    allegro_message(&quot;You pressed Control+C
&quot;);

if (val == (KEY_X &lt;&lt; 8)) /* alt+letter */
    allegro_message(&quot;You pressed Alt+X
&quot;);

This function cannot return character values greater than 255. If you
    need to read Unicode input,
    use ureadkey() instead.
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-ureadkey/">ureadkey</a></code>(3), <code><a href="/docs/linux/man/3-keypressed/">keypressed</a></code>(3), <code><a href="/docs/linux/man/3-clear_keybuf/">clear_keybuf</a></code>(3), <code><a href="/docs/linux/man/3-simulate_keypress/">simulate_keypress</a></code>(3) </p>
