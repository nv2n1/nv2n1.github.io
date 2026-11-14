---
title: "wtoc(1)"
name: "wtoc"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wtoc/"
description: "wtoc – Convert a Wnn text-form dictionary (or dictionaries) into Canna text-form dictionaries"
---

<h2>NAME</h2>
<p> wtoc &#8211; Convert a Wnn text-form dictionary (or dictionaries) into Canna text-form dictionaries</p>
<h2>SYNOPSIS</h2>
<p> <code>wtoc [-f </code><i>hinshidata</i>] [<i>wnnjisho</i>] [<i>cannajisho</i>]</p>
<h2>DESCRIPTION</h2>
<p> wtoc converts a Wnn text-form dictionary file into Canna text-form dictionary file. If all dictionary files are omitted, the Wnn dictionary data is input through the standard input. In this case, the dictionary of the Japanes Input System is output from the standard output. If one dictionary file is specified, it will be regarded as a Wnn dictionary. At this time, Canna dictionary output to the standard output.</p>
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
<h2>EXAMPLE</h2>
<pre>
% wtoc -f tsuikahinshi kihon.u kihon.t
</pre>
<p> Inputs word-type correspondence information from tsuikahinshi, then converts Wnn text-form dictionary kihon.u into the Canna text-form dictionary before output. </p>
<pre>
% wtoc special.u | lpr
</pre>
<p> Converts Wnn text-form dictionary special.u into Canna text-form dictionary, then outputs the result to the line printer.</p>
<h2>SEE ALSO</h2>
<dl>
<dt><a href="/docs/linux/man/1-ctow/">ctow</a>(1)</p>
<dd>
</dl>
<h2>Index</h2>
