---
title: "register_uformat(3)"
name: "register_uformat"
section: "3"
letter: "r"
url: "/docs/linux/man/3-register_uformat/"
description: "register_uformat – Installs handler functions for a new text encoding format. Allegro game programming library."
---

<p>register_uformat &#8211; Installs handler functions for a new text encoding format. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void register_uformat(int type,

                      int (*u_getc)(const char *s),

                      int (*u_getx)(char **s),

                      int (*u_setc)(char *s, int c),

                      int (*u_width)(const char *s),

                      int (*u_cwidth)(int c),

                      int (*u_isok)(int c));</code></pre>
<h2>Description</h2>
<p>Installs a set of custom handler functions for a new text encoding format. The `type&#8217; is the ID code for your new format, which should be a 4-character string as produced by the AL_ID() macro, and which can later be passed to functions like set_uformat() and uconvert(). The function parameters are handlers that implement the character access for your new type: see below for details of these. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_uformat/">set_uformat</a></code>(3), <code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ugetc/">ugetc</a></code>(3), <code><a href="/docs/linux/man/3-ugetx/">ugetx</a></code>(3), <code><a href="/docs/linux/man/3-usetc/">usetc</a></code>(3), <code><a href="/docs/linux/man/3-uwidth/">uwidth</a></code>(3), <code><a href="/docs/linux/man/3-ucwidth/">ucwidth</a></code>(3), <code><a href="/docs/linux/man/3-uisok/">uisok</a></code>(3) </p>
