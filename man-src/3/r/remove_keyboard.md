---
title: "remove_keyboard(3)"
name: "remove_keyboard"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remove_keyboard/"
description: "remove_keyboard – Removes the Allegro keyboard handler."
---

<p>remove_keyboard &#8211; Removes the Allegro keyboard handler.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void remove_keyboard();</code></pre>
<h2>Description</h2>
<p>Removes the keyboard handler, returning control to the operating system. You don&#8217;t normally need to bother calling this, because allegro_exit() will do it for you. However, you might want to call this during runtime if you want to change the keyboard mapping on those platforms were keyboard mappings are needed. You would first modify the configuration variable holding the keyboard mapping and then reinstall the keyboard handler. Example: </p>
<pre> remove_keyboard();
 /* Switch to Spanish keyboard mapping. */
 set_config_string(&quot;system&quot;, &quot;keyboard&quot;, &quot;es&quot;);
 install_keyboard();</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_keyboard/">install_keyboard</a></code>(3), <code><a href="/docs/linux/man/3-allegro_exit/">allegro_exit</a></code>(3), <code><a href="/docs/linux/man/3-set_config_string/">set_config_string</a></code>(3) </p>
