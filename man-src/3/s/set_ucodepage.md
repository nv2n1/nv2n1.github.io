---
title: "set_ucodepage(3)"
name: "set_ucodepage"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_ucodepage/"
description: "set_ucodepage – Sets 8-bit to Unicode conversion tables. Allegro game programming library."
---

<p>set_ucodepage &#8211; Sets 8-bit to Unicode conversion tables. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_ucodepage(const unsigned short *table,

                   const unsigned short *extras);</code></pre>
<h2>Description</h2>
<p>When you select the U_ASCII_CP encoding mode, a set of tables are used to convert between 8-bit characters and their Unicode equivalents. You can use this function to specify a custom set of mapping tables, which allows you to support different 8-bit codepages. The `table&#8217; parameter points to an array of 256 shorts, which contain the Unicode value for each character in your codepage. The `extras&#8217; parameter, if not NULL, points to a list of mapping pairs, which will be used when reducing Unicode data to your codepage. Each pair consists of a Unicode value, followed by the way it should be represented in your codepage. The list is terminated by a zero Unicode value. This allows you to create a many-&gt;one mapping, where many different Unicode characters can be represented by a single codepage value (eg. for reducing accented vowels to 7-bit ASCII). Allegro will use the `table&#8217; parameter when it needs to convert an ASCII string to an Unicode string. But when Allegro converts an Unicode string to ASCII, it will use both parameters. First, it will loop through the `table&#8217; parameter looking for an index position pointing at the Unicode value it is trying to convert (ie. the `table&#8217; parameter is also used for reverse matching). If that fails, the `extras&#8217; list is used. If that fails too, Allegro will put the character `^&#8217;, giving up the conversion. Note that Allegro comes with a default `table&#8217; and `extras&#8217; parameters set internally. The default `table&#8217; will convert 8-bit characters to `^&#8217;. The default `extras&#8217; list reduces Latin-1 and Extended-A characters to 7 bits in a sensible way (eg. an accented vowel will be reduced to the same vowel without the accent). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_uformat/">set_uformat</a></code>(3) </p>
