---
title: "scancode_to_name(3)"
name: "scancode_to_name"
section: "3"
letter: "s"
url: "/docs/linux/man/3-scancode_to_name/"
description: "scancode_to_name – Converts a scancode to a key name. Allegro game programming library."
---

<p>scancode_to_name &#8211; Converts a scancode to a key name. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

const char *scancode_to_name(int scancode);</code></pre>
<h2>Description</h2>
<p>This function returns a string pointer containing the name of they key with the given scancode. This is useful if you e.g. let the user choose a key for some action, and want to display something more meaningful than just the scancode. Example: </p>
<pre><code>char const *keyname = scancode_to_name(scancode);
allegro_message(&quot;You pressed the %s key.&quot;, keyname);
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-scancode_to_ascii/">scancode_to_ascii</a></code>(3), <code><a href="/docs/linux/man/3-exkeys/">exkeys</a></code>(3) </p>
