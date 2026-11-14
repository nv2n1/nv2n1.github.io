---
title: "set_leds(3)"
name: "set_leds"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_leds/"
description: "set_leds – Sets the state of the keyboard LED indicators. Allegro game programming library."
---

<p>set_leds &#8211; Sets the state of the keyboard LED indicators. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_leds(int leds);</code></pre>
<h2>Description</h2>
<p>Overrides the state of the keyboard LED indicators. The parameter is a bitmask containing any of the values KB_SCROLOCK_FLAG, KB_NUMLOCK_FLAG, and KB_CAPSLOCK_FLAG, or -1 to restore the default behavior. Example: </p>
<pre> /* Cycle led indicators. */
 set_leds(KB_SCROLOCK_FLAG);
 rest(1000);
 set_leds(KB_CAPSLOCK_FLAG);
 rest(1000);
 set_leds(KB_NUMLOCK_FLAG);
 rest(1000);
 set_leds(-1);</pre>
<p>Note that the led behaviour cannot be guaranteed on some platforms, some leds might not react, or none at all. Therefore you shouldn&#8217;t rely only on them to communicate information to the user, just in case it doesn&#8217;t get through. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-key_led_flag/">key_led_flag</a></code>(3) </p>
