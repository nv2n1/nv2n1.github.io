---
title: "dicar(1)"
name: "dicar"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dicar/"
description: "dicar – Archive Binary Dictionary"
---

<h2>NAME</h2>
<p> dicar &#8211; Archive Binary Dictionary</p>
<h2>SYNOPSYS</h2>
<p> <code>dicar</code> <code>-t</code> <i>bindic1</i><br />
 <code>dicar</code> <code>-x</code> <i>bindic1</i> [ <code>bindic2</code> ]<br />
 <code>dicar</code> <code>-r</code> <i>bindic1</i> <i>bindic2</i><br />
 <code>dicar</code> <code>-d </code> <i>bindic1</i> <i>bindic2</i> </p>
<h2>DESCRIPTION</h2>
<p> <i>dicar</i> archives binary dictionary <i>bindic1.</i> The hyphen of each option may be omitted. [ <code>TIONS</code> ]</p>
<dl>
<dt><code>-t</code></p>
<dd> Displays the dictionaries contained in binary dictionary file <i>bindic1.</i> Each displayed name of the dictionaries consists of the text file name followed by extension &#8216;.d&#8217;. This text file name is that before the dictionary file is converted into the binary file.</p>
<dt><code>-x</code></p>
<dd> Fetches dictionary <i>bindic2</i> from <i>bindic1.</i> <i>Bindic2</i> consists of the text file name followed by extension &#8216;.d&#8217;. This text file name is that before the dictionary file is converted into the binary file. The fetched file <i>bindic2</i> becomes a dictionary file in binary format. If <i>bindic2</i> is omitted, all dictionaries within <i>bindic1</i> will be fetched.</p>
<dt><code>-r</code></p>
<dd> Adds to <i>bindic1,</i> all dictionaries that are contained in the dictionary file specified in <i>bindic2.</i> Any dictionary in <i>bindic1</i> that is contained in <i>bindic1 is overwritten.</i></p>
<dt><code>-d</code></p>
<dd> Deletes <i>bindic2</i> from <i>bindic1.</i> </p>
</dl>
<h2>EXAMPLES</h2>
<pre>
<code>% ls</code>
<code>chimei.d shima.d</code>
<code>% dicar -t shima.d</code>
<code>(Text dictionary file name = Directory size + Word size, packed)</code>
<code>% dicar r shima.d shima.mwd.d (Replaces shima.mwd.d.)</code>
<code>% dicar r shima.d chimedi.d (Adds chimedi.d to shima.d.)</code>
<code>% dicar -t shma.d</code>
<code>(Text dictionary file name = Directory size + Word size, packed)</code>
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-dpbindic/">dpbindic</a>(1), <a href="/docs/linux/man/1-mkbindic/">mkbindic</a>(1) </p>
<h2>Index</h2>
