---
title: "poll_keyboard-2(3)"
name: "poll_keyboard-2"
section: "3"
letter: "p"
url: "/docs/linux/man/3-poll_keyboard-2/"
description: "poll_keyboard – Polls the keyboard. Allegro game programming library."
---

<p>poll_keyboard &#8211; Polls the keyboard. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int poll_keyboard();</code></pre>
<h2>Description</h2>
<p>Wherever possible, Allegro will read the keyboard input asynchronously (ie. from inside an interrupt handler), but on some platforms that may not be possible, in which case you must call this routine at regular intervals to update the keyboard state variables. </p>
<p> To help you test your keyboard polling code even if you are programming on a platform that doesn&#8217;t require it, after the first time that you call this function Allegro will switch into polling mode, so from that point onwards you will have to call this routine in order to get any keyboard input at all, regardless of whether the current driver actually needs to be polled or not. </p>
<p> The keypressed(), readkey(), and ureadkey() functions call poll_keyboard() automatically, so you only need to use this function when accessing the key[] array and key_shifts variable.</p>
<h2>Return Value</h2>
<p>Returns zero on success, or a negative number on failure (ie. no keyboard driver installed). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-keyboard_needs_poll/">keyboard_needs_poll</a></code>(3), <code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-key/">key</a></code>(3), <code><a href="/docs/linux/man/3-key_shifts/">key_shifts</a></code>(3), <code><a href="/docs/linux/man/3-excamera/">excamera</a></code>(3), <code><a href="/docs/linux/man/3-exsample/">exsample</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3) </p>
