---
title: "remove_sound_input(3)"
name: "remove_sound_input"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remove_sound_input/"
description: "remove_sound_input – Cleans up after you are finished with the sound input routines. Allegro game programming library."
---

<p>remove_sound_input &#8211; Cleans up after you are finished with the sound input routines. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void remove_sound_input();</code></pre>
<h2>Description</h2>
<p>Cleans up after you are finished with the sound input routines. You don&#8217;t normally need to call this, because remove_sound() and/or allegro_exit() will do it for you. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_sound_input/">install_sound_input</a></code>(3), <code><a href="/docs/linux/man/3-remove_sound/">remove_sound</a></code>(3), <code><a href="/docs/linux/man/3-allegro_exit/">allegro_exit</a></code>(3) </p>
