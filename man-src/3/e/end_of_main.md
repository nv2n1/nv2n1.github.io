---
title: "end_of_main(3)"
name: "end_of_main"
section: "3"
letter: "e"
url: "/docs/linux/man/3-end_of_main/"
description: "END_OF_MAIN – Macro to put after your main() function. Allegro game programming library."
---

<p>END_OF_MAIN &#8211; Macro to put after your main() function. Allegro game programming library.</p>
<h2>Synopsis</h2>
<p><code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>Macro END_OF_MAIN()</code></p>
<h2>Description</h2>
<p>In order to maintain cross-platform compatibility, you have to put this macro at the very end of your main function. This macro uses some `magic&#8217; to mangle your main procedure on platforms that need it like Windows, some flavours of UNIX or MacOS X. On the other platforms this macro compiles to nothing, so you don&#8217;t have to #ifdef around it. Example: </p>
<pre> int main(void)
 {
 allegro_init();
 /* more stuff goes here */
 ...
 return 0;
 }
 END_OF_MAIN()</pre>
<h2>See Also</h2>
