---
title: "ureadkey(3)"
name: "ureadkey"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ureadkey/"
description: "ureadkey – Returns the next unicode character from the keyboard buffer. Allegro game programming library."
---

<p>ureadkey &#8211; Returns the next unicode character from the keyboard buffer. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int ureadkey(int *scancode);</code></pre>
<h2>Description</h2>
<p>Returns the next character from the keyboard buffer, in Unicode format. If the buffer is empty, it waits until a key is pressed. You can see if there are queued keypresses with keypressed(). The return value contains the Unicode value of the key, and if not NULL, the pointer argument will be set to the scancode. Unlike readkey(), this function is able to return character values greater than 255. Example: </p>
<pre><code>int val, scancode;
... val = ureadkey(&amp;scancode);
if (val == 0x00F1)
    allegro_message(&quot;You pressed n with tilde
&quot;);

if (val == 0x00DF)
    allegro_message(&quot;You pressed sharp s
&quot;);

You should be able to find Unicode character maps at
http://www.unicode.org/. Remember that on DOS you must specify a custom
keyboard map (like those found in `keyboard.dat') usually with the help of
a configuration file specifying the language mapping (keyboard variable in
system section of `allegro.cfg'), or you will get the default US keyboard
mapping.
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3), <code><a href="/docs/linux/man/3-keypressed/">keypressed</a></code>(3), <code><a href="/docs/linux/man/3-clear_keybuf/">clear_keybuf</a></code>(3), <code><a href="/docs/linux/man/3-simulate_ukeypress/">simulate_ukeypress</a></code>(3), <code><a href="/docs/linux/man/3-exkeys/">exkeys</a></code>(3) </p>
