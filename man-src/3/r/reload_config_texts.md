---
title: "reload_config_texts(3)"
name: "reload_config_texts"
section: "3"
letter: "r"
url: "/docs/linux/man/3-reload_config_texts/"
description: "reload_config_texts – Reloads translated strings returned by get_config_text(). Allegro game programming library."
---

<p>reload_config_texts &#8211; Reloads translated strings returned by get_config_text(). Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void reload_config_texts(const char *new_language);</code></pre>
<h2>Description</h2>
<p>Reloads the translated strings returned by get_config_text(). This is useful to switch to another language in your program at runtime. If you want to modify the `[system]&#8217; language configuration variable yourself, or you have switched configuration files, you will want to pass NULL to just reload whatever language is currently selected. Or you can pass a string containing the two letter code of the language you desire to switch to, and the function will modify the language variable. After you call this function, the previously returned pointers of get_config_text() will be invalid. Example: </p>
<pre> ...
 /* The user selects French from a language choice menu. */
 reload_config_texts(&quot;FR&quot;);</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-get_config_text/">get_config_text</a></code>(3), <code><a href="/docs/linux/man/3-get_config_string/">get_config_string</a></code>(3) </p>
