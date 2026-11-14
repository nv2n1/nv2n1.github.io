---
title: "dpromdic(1)"
name: "dpromdic"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpromdic/"
description: "dpromdic – Convert the binary-form Romaji-to-Kana conversion table into the text-form table"
---

<p>dpromdic &#8211; Convert the binary-form Romaji-to-Kana conversion table into the text-form table</p>
<h2>SYNOPSYS</h2>
<p> <code>dpromdic</code> [ <i>file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>dpromdic</i> converts the binary-form Romaji-to-Kana conversion table into the text-form table. It then outputs the result to the standard output. </p>
<p> After a dictionary table is converted into the binary dictionary by using <i><a href="/docs/linux/man/1-mkromdic/">mkromdic</a>(1),</i> dpromdic can returns it to the text-form table. </p>
<p> The contents converted into binary dictionary from the text dictionary by using <i><a href="/docs/linux/man/1-mkromdic/">mkromdic</a>(1)</i> is sorted in alphabetical order of Romaji. The comment lines are deleted in this table.</p>
<h2>EXAMPL</h2>
<pre>
<code>% dpromdic test.kp</code>
<code>(The contents of test.kp are output, in text form, to the</code>
<code>standard output.)</code>
<code>% dpromdic test.kp &gt; test1.kpdef</code>
<code>(Dictionary table test1.kpdef is created in text form.)</code>
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mkromdic/">mkromdic</a>(1) </p>
<h2>Index</h2>
