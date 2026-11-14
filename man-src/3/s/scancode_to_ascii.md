---
title: "scancode_to_ascii(3)"
name: "scancode_to_ascii"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scancode_to_ascii/"
description: "scancode_to_ascii – Converts a scancode to an ASCII character. Allegro game programming library."
---

<p>scancode_to_ascii &#8211; Converts a scancode to an ASCII character. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int scancode_to_ascii(int scancode);</code></pre>
<h2>Description</h2>
<p>Converts the given scancode to an ASCII character for that key (mangling Unicode values), returning the unshifted uncapslocked result of pressing the key, or zero if the key isn&#8217;t a character-generating key or the lookup can&#8217;t be done. The lookup cannot be done for keys like the F1-F12 keys or the cursor keys, and some drivers will only return approximate values. Generally, if you want to display the name of a key to the user, you should use the scancode_to_name function. Example: </p>
<pre><code>int ascii;
... ascii = scancode_to_ascii(scancode);
allegro_message(&quot;You pressed '%c'
&quot;, ascii);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-scancode_to_name/">scancode_to_name</a></code>(3) </p>
