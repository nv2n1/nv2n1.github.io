---
title: "dpbindic(1)"
name: "dpbindic"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpbindic/"
description: "dpbindic – Convert a binary-form dictionary into a text-form dictionary"
---

<h2>NAME</h2>
<p> dpbindic &#8211; Convert a binary-form dictionary into a text-form dictionary</p>
<h2>SYNOPSYS</h2>
<p> <code>dpbindic</code> [ <code>-xiu</code> [ <i>frequency</i> ] ] <i>binary-file</i> [ <i>text-file</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>dpbindic</i> outputs the file information of the binary-form dictionary file specified in <i>binary-file</i>. At this time, the word information of the dictionary can be output in text form to the standard output. To do so, use <i>test-file</i> to specify the text-form dictionary used as the source of binary-form dictionary file. If this specification is omitted, the text dictionary file information in the binary dictionary file will be output. The standard grammar file name is /usr/local/canna/lib/dic/hyoujun.gram. It will be used if the grammar file name specification is omitted. The output format of word information data is specified using an option.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-x</code></p>
<dd> Outputs the data without using omission symbol @, which is used when the initial word represents the reading.</p>
<dt><code>-i</code></p>
<dd> Replaces the reading and word for output.</p>
<dt><code>-u</code></p>
<dd> Outputs the candidates used in conversion. Outputs all candidates having <i>frequency</i> or more. If <i>frequency</i> is omitted, all candidates having frequency 1 will be output.</dl>
<h2>EXAMPLES</h2>
<p> (1) If the text-form dictionary file name is omitted: </p>
<pre>
<code>%dibindic iroha.cbd</code>
<code>(Text dictionary file name = Directory size + Word size, packed)</code>
<code>iroha.swd = 2985 + 5306 pak a4</code>
<code>iroha.mwd = 36276 + 113139 pak a4</code>
(2) If the text-form dictionary file name iroha.mwd is specified:
<code>%dpbindic iroha.cbd iroha.mwd</code>
<code>(Text dictionary file name = Directory size + Word size, packed)</code>
<code>iroha.mwd = 36276 + 113139 pak a4</code>
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mkbindic/">mkbindic</a>(1), <a href="/docs/linux/man/1-dicar/">dicar</a>(1) </p>
<h2>Index</h2>
