---
title: "ctow(1)"
name: "ctow"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctow/"
description: "ctow – Convert Canna text-form dictionary into Wnn text-form dictionary"
---

<h2>NAME</h2>
<p> ctow &#8211; Convert Canna text-form dictionary into Wnn text-form dictionary</p>
<h2>SYNOPSIS</h2>
<p> <code>ctow [-f </code><i>hinshidata</i>] [<i>cannajisho</i>] [<i>wnnjisho</i>]</p>
<h2>DESCRIPTION</h2>
<p> ctow converts the Canna text-form dictionary file into the Wnn text-form dictionary. If all dictionary files are omitted, this dictionary is input through the standard input. In this case, the Wnn dictionary is output to the standard output. If only one dictionary file is specified, it is regarded as the one of the Japanes Input System. In this case, the Wnn dictionary is output from the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-f <i>hinshidata</i></p>
<dd> The user can add new information about word-type correspondence between Wnn and Canna. The following word-type correspondence information must be described in the <i>hinshidata</i> file. Within one line, describe the Wnn word type name and the Canna word type while delimiting by a space(s) or tab. </p>
<pre>
  Wnn word type       Canna word type
<br>
  Adverb              #F04
</pre>
</dl>
<h2>SEE ALSO</h2>
<dl>
<dt><a href="/docs/linux/man/1-wtoc/">wtoc</a>(1)</p>
<dd>
</dl>
<h2>Index</h2>
