---
title: "get_config_text(3)"
name: "get_config_text"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_config_text/"
description: "get_config_text – Returns a string translated to the current language. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_config_text &#8211; Returns a string translated to the current language. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>const char *get_config_text(const char *msg);</code></p>
<h2>DESCRIPTION</h2>
<p> This function is primarily intended for use by internal library code, but it may perhaps be helpful to application programmers as well. It uses the `language.dat&#8217; or `XXtext.cfg&#8217; files (where XX is a language code) to look up a translated version of the parameter in the currently selected language. </p>
<p> This is basically the same thing as calling get_config_string() with `[language]&#8217; as the section, `msg&#8217; as the variable name, and `msg&#8217; as the default value, but it contains some special code to handle Unicode format conversions. The `msg&#8217; parameter is always given in ASCII format, but the returned string will be converted into the current text encoding, with memory being allocated as required, so you can assume that this pointer will persist without having to manually allocate storage space for each string. </p>
<p> Note that if you are planning on distributing your game on the Unix platform there is a special issue with how to deal with the `language.dat&#8217; file. Read section &quot;Files shared by Allegro&quot; of the chapter &quot;Unix specifics&quot; to learn more about this.</p>
<h2>RETURN VALUE</h2>
<p> Returns a suitable translation if one can be found or a copy of the parameter if nothing else is available. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_config_string/">get_config_string</a></code>(3), <code><a href="/docs/linux/man/3-reload_config_texts/">reload_config_texts</a></code>(3) </p>
<h2>Index</h2>
