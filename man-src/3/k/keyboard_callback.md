---
title: "keyboard_callback(3)"
name: "keyboard_callback"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyboard_callback/"
description: "keyboard_callback – User specified keyboard callback handler. Allegro game programming library."
---

<h2>NAME</h2>
<p> keyboard_callback &#8211; User specified keyboard callback handler. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern int (*keyboard_callback)(int key);</code></p>
<h2>DESCRIPTION</h2>
<p> If set, this function is called by the keyboard handler in response to every keypress. It is passed a copy of the value that is about to be added into the input buffer, and can either return this value unchanged, return zero to cause the key to be ignored, or return a modified value to change what readkey() will later return. This routine executes in an interrupt context, so it must be in locked memory. Example: </p>
<pre><code>
   int enigma_scrambler(int key)
   {
      /* Add one to both the scancode and ascii values. */
      return (((key &gt;&gt; 8) + 1) 
   }
   END_OF_FUNCTION(enigma_scrambler)
   
   ...
   
      install_timer();
   LOCK_FUNCTION(enigma_scrambler);
   install_keyboard();
   keyboard_callback = enigma_scrambler;
</code></pre>
<p> Note that this callback will be ignored if you also set the unicode keyboard callback. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-readkey/">readkey</a></code>(3), <code><a href="/docs/linux/man/3-ureadkey/">ureadkey</a></code>(3), <code><a href="/docs/linux/man/3-keyboard_ucallback/">keyboard_ucallback</a></code>(3), <code><a href="/docs/linux/man/3-keyboard_lowlevel_callback/">keyboard_lowlevel_callback</a></code>(3) </p>
<h2>Index</h2>
