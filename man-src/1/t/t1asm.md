---
title: "t1asm(1)"
name: "t1asm"
section: "1"
letter: "t"
url: "/docs/linux/man/1-t1asm/"
description: "t1asm – assemble PostScript Type 1 font"
---

<h2 class="name">NAME</h2>
<p> t1asm &#8211; assemble PostScript Type 1 font </p>
<h2>SYNOPSIS</h2>
<p> <code>t1asm</code> [<code>-a</code>|<code>-b</code>] [<code>-l</code> <i>length</i>] [<i>input</i> [<i>output</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>t1asm</code> assembles Adobe Type 1 font programs into either PFA (hexadecimal) or PFB (binary) formats from a human-readable form. If the file <i>output</i> is not specified output goes to the standard output. If the file <i>input</i> is not specified input comes from the standard input. </p>
<p> <code>t1asm</code> tokenizes the charstring data and performs eexec and charstring encryption as specified in the &#8220;black book,&#8221; <i>Adobe Type 1 Font Format.</i> </p>
<p> The input must have a line of the form</p>
<dl>
<dt>
<dd>
<pre>
<code>/-|{string currentfile exch readstring pop}executeonly def
</code></pre>
</dl>
<p> which defines the command, in this case `-|&#8217;, that is to start charstring data. It is an error not to define such a command. Another common name for this command is `RD&#8217;. </p>
<p> After the start of the <code>Subrs</code> array in the input, all open braces `{&#8216; not in a comment begin a charstring. Such a charstring is terminated by the next non-comment close brace `}&#8217;. Within such a charstring, only comments, integers, and valid charstring commands are allowed. Valid charstring command names can be found in <i>Adobe Type 1 Font Format</i> and other documents describing the newer Type 2 opcodes. The format within a charstring is unimportant as long as integers and commands are separated by at least a one whitespace (space, tab, newline) character. Note that within charstrings, comments are discarded because they cannot be encoded.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;pfa</code>, <code>-a</code></p>
<dd> Output in PFA (ASCII) format.</p>
<dt><code>&#8211;pfb</code>, <code>-b</code></p>
<dd> Output in PFB (binary) format. This is the default.</p>
<dt><code>&#8211;block-length=</code><i>num</i>, <code>-l</code><i> num</i></p>
<dd> PFB only: Set the maximum output block length to <i>num.</i> The default length is as large as memory allows.</p>
<dt><code>&#8211;line-length=</code><i>num</i>, <code>-l</code><i> num</i></p>
<dd> PFA only: Set the maximum length of encrypted lines in the output to <i>num.</i> (These are the lines consisting wholly of hexadecimal digits.) The default is 64.</dl>
<h2>EXAMPLES</h2>
<pre>
% t1asm Utopia-Regular.raw &gt; Utopia-Regular.pfb
% t1asm -a Utopia-Regular.raw &gt; Utopia-Regular.pfa
</pre>
<h2>SEE ALSO</h2>
<p> <i>Adobe Type 1 Font Format</i> is available free from Adobe as a PDF file. <a rel="nofollow" href="http://partners.adobe.com/asn/developer/PDFS/TN/T1_SPEC.PDF">http://partners.adobe.com/asn/developer/PDFS/TN/T1_SPEC.PDF</a> </p>
<p> <i>The Type 2 Charstring Format,</i> also available from Adobe as a PDF file, describes the newer Type 2 operators, which are also used in some multiple-master Type 1 fonts like Adobe Jenson and Kepler. <a rel="nofollow" href="http://partners.adobe.com/asn/developer/PDFS/TN/5177.Type2.pdf">http://partners.adobe.com/asn/developer/PDFS/TN/5177.Type2.pdf</a></p>
<h2>AUTHORS</h2>
<p> Lee Hetherington (ilh [at] lcs.mit.edu)<br />
 Eddie Kohler (ekohler [at] gmail.com) </p>
<h2>Index</h2>
