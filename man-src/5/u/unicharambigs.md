---
title: "unicharambigs(5)"
name: "unicharambigs"
section: "5"
letter: "u"
url: "/docs/linux/man/5-unicharambigs/"
description: "unicharambigs – Tesseract unicharset ambiguities"
---

<p>unicharambigs &#8211; Tesseract unicharset ambiguities</p>
<h2>Description</h2>
<p>The unicharambigs file (a component of traineddata, see <a href="/docs/linux/man/1-combine_tessdata/">combine_tessdata</a>(1) ) is used by Tesseract to represent possible ambiguities between characters, or groups of characters. The file contains a number of lines, laid out as follow:</p>
<dl>
<dd>
<pre>[num] &lt;TAB&gt; [char(s)] &lt;TAB&gt; [num] &lt;TAB&gt; [char(s)] &lt;TAB&gt; [num]</pre>
</dl>
<p>  Field one </td>
<td> the number of characters contained in field two
</td>
</tr>
<tr VALIGN=top>
<td> Field two </td>
<td> the character sequence to be replaced
</td>
</tr>
<tr VALIGN=top>
<td> Field three </td>
<td> the number of characters contained in field four
</td>
</tr>
<tr VALIGN=top>
<td> Field four </td>
<td> the character sequence used to replace field two
</td>
</tr>
<tr VALIGN=top>
<td> Field five </td>
<td> contains either 1 or 0. 1 denotes a mandatory replacement, 0 denotes an optional replacement.
</td>
</tr>
</table>
<p> Characters appearing in fields two and four should appear in unicharset. The numbers in fields one and three refer to the number of unichars (not bytes).</p>
<h2>Example</h2>
<dl>
<dd>
<pre>2 ' ' 1 &quot; 1
1 m 2 r n 0
3 i i i 1 m 0</pre>
</dl>
<p> In this example, all instances of the <i>2</i> character sequence <i>&#8216;</i>&#8216; will <code>always</code> be replaced by the <i>1</i> character sequence <i>&quot;</i>; a <i>1</i> character sequence <i>m</i> <code>may</code> be replaced by the <i>2</i> character sequence <i>rn</i>, and the <i>3</i> character sequence <code>may</code> be replaced by the <i>1</i> character sequence <i>m</i>.</p>
<h2>History</h2>
<p>The unicharambigs file first appeared in Tesseract 3.00; prior to that, a similar format, called DangAmbigs (<i>dangerous ambiguities</i>) was used: the format was almost identical, except only mandatory replacements could be specified, and field 5 was absent.</p>
<h2>Bugs</h2>
<p>This is a documentation &quot;bug&quot;: it&#8217;s not currently clear what should be done in the case of ligatures (such as <i>fi</i>) which may also appear as regular letters in the unicharset.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-tesseract/">tesseract</a>(1), <a href="/docs/linux/man/5-unicharset/">unicharset</a>(5)</p>
<h2>Author</h2>
<p>The Tesseract OCR engine was written by Ray Smith and his research groups at Hewlett Packard (1985-1995) and Google (2006-present).</p>
