---
title: "set_uformat(3)"
name: "set_uformat"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_uformat/"
description: "set_uformat – Set the global current text encoding format. Allegro game programming library."
---

<p>set_uformat &#8211; Set the global current text encoding format. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void set_uformat(int type);</code></p>
<h2>Description</h2>
<p> Sets the current text encoding format. This will affect all parts of Allegro, wherever you see a function that returns a char *, or takes a char * as a parameter. `type&#8217; should be one of these values: </p>
<pre>
   U_ASCII     - fixed size, 8-bit ASCII characters
   U_ASCII_CP  - alternative 8-bit codepage (see set_ucodepage())
   U_UNICODE   - fixed size, 16-bit Unicode characters
   U_UTF8      - variable size, UTF-8 format Unicode characters
   
</pre>
<p> Although you can change the text format on the fly, this is not a good idea. Many strings, for example the names of your hardware drivers and any language translations, are loaded when you call allegro_init(), so if you change the encoding format after this, they will be in the wrong format, and things will not work properly. Generally you should only call set_uformat() once, before allegro_init(), and then leave it on the same setting for the duration of your program. </p>
<h2>See Also</h2>
<p> <code><a href="/docs/linux/man/3-get_uformat/">get_uformat</a></code>(3), <code><a href="/docs/linux/man/3-register_uformat/">register_uformat</a></code>(3), <code><a href="/docs/linux/man/3-set_ucodepage/">set_ucodepage</a></code>(3), <code><a href="/docs/linux/man/3-set_uformat/">set_uformat</a></code>(3), <code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrsize/">ustrsize</a></code>(3), <code><a href="/docs/linux/man/3-ugetc/">ugetc</a></code>(3), <code><a href="/docs/linux/man/3-ugetx/">ugetx</a></code>(3), <code><a href="/docs/linux/man/3-usetc/">usetc</a></code>(3), <code><a href="/docs/linux/man/3-uwidth/">uwidth</a></code>(3), <code><a href="/docs/linux/man/3-ucwidth/">ucwidth</a></code>(3), <code><a href="/docs/linux/man/3-uisok/">uisok</a></code>(3), <code><a href="/docs/linux/man/3-uoffset/">uoffset</a></code>(3), <code><a href="/docs/linux/man/3-ugetat/">ugetat</a></code>(3), <code><a href="/docs/linux/man/3-usetat/">usetat</a></code>(3), <code><a href="/docs/linux/man/3-uinsert/">uinsert</a></code>(3), <code><a href="/docs/linux/man/3-uremove/">uremove</a></code>(3), <code><a href="/docs/linux/man/3-allegro_init/">allegro_init</a></code>(3), <code><a href="/docs/linux/man/3-exunicod/">exunicod</a></code>(3)</p>
