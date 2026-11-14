---
title: "t1disasm(1)"
name: "t1disasm"
section: "1"
letter: "t"
url: "/docs/linux/man/1-t1disasm/"
description: "t1disasm – disassemble PostScript Type 1 font"
---

<h2 class="name">NAME</h2>
<p> t1disasm &#8211; disassemble PostScript Type 1 font </p>
<h2>SYNOPSIS</h2>
<p> <code>t1disasm</code> [<i>input</i> [<i>output</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>t1disasm</code> disassembles Adobe Type 1 font programs in either PFA (hexadecimal) or PFB (binary) formats into human-readable form. If the file <i>output</i> is not specified output goes to the standard output. If the file <i>input</i> is not specified input comes from the standard input. </p>
<p> <code>t1disasm</code> performs eexec and charstring decryption as specified in the &#8220;black book&#8221;, <i>Adobe Type 1 Font Format.</i> Additionally, the charstring binary tokens are expanded into human-readable text form, using the names given in the black book and later documents describing Type 2 opcodes.</p>
<h2>EXAMPLES</h2>
<pre>
% t1disasm Utopia-Regular.pfb Utopia-Regular.raw
% t1disasm Utopia-Regular.pfa Utopia-Regular.raw
</pre>
<p> In <code>Subrs</code> entries in Utopia-Regular.raw will look like</p>
<dl>
<dt>
<dd>
<pre>
<code>dup 5 {
        8 111 vstem
        -12 128 hstem
        707 -20 hstem
        return
        } |
</code></pre>
</dl>
<p> and the <code>CharStrings</code> entries like</p>
<dl>
<dt>
<dd>
<pre>
<code>/exclam {
        58 242 hsbw
        6 callsubr
        5 4 callsubr
        63 707 rmoveto
        -54 0 -5 -22 4 -45 rrcurveto
        40 -431 rlineto
        29 hlineto
        42 431 rlineto
        4 45 -5 22 -55 0 rrcurveto
        closepath
        6 4 callsubr
        -719 vmoveto
        243 callsubr
        endchar
        } |-
</code></pre>
</dl>
<h2>SEE ALSO</h2>
<p> <i>Adobe Type 1 Font Format</i> is available free from Adobe as a PDF file: <a rel="nofollow" href="http://partners.adobe.com/asn/developer/PDFS/TN/T1_SPEC.PDF">http://partners.adobe.com/asn/developer/PDFS/TN/T1_SPEC.PDF</a> </p>
<p> <i>The Type 2 Charstring Format,</i> also available from Adobe as a PDF file, describes the newer Type 2 operators, which are also used in some multiple-master Type 1 fonts like Adobe Jenson and Kepler: <a rel="nofollow" href="http://partners.adobe.com/asn/developer/PDFS/TN/5177.Type2.pdf">http://partners.adobe.com/asn/developer/PDFS/TN/5177.Type2.pdf</a></p>
<h2>AUTHORS</h2>
<p> Lee Hetherington (ilh [at] lcs.mit.edu)<br />
 Eddie Kohler (ekohler [at] gmail.com) </p>
<h2>Index</h2>
