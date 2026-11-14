---
title: "ansifilter(1)"
name: "ansifilter"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ansifilter/"
description: "Ansifilter – ANSI escape code processor and converter"
---

<h2 class="name">NAME</h2>
<p> Ansifilter &#8211; ANSI escape code processor and converter</p>
<h2>SYNOPSIS</h2>
<p> <code>ansifilter</code> [d:i:F:o:s:e:fhptvHRT] [-i input file] [-o output file] [&#8211;text] [&#8211;html] [&#8211;latex] [&#8211;tex] [&#8211;rtf] [input files] </p>
<h2>DESCRIPTION</h2>
<p> <code>Ansifilter</code> is a small utility to handle text files containing ANSI terminal escape codes. The command sequences may be stripped or be interpreted to generate formatted output (HTML, LaTeX, TeX, RTF). </p>
<p> See the README file for details.</p>
<h2>File options</h2>
<dl>
<dt>-i, &#8211;input=&lt;file&gt;</p>
<dd> name of input file</p>
<dt>-o, &#8211;output=&lt;file&gt;</p>
<dd> name of output file</p>
<dt>-O, &#8211;outdir=&lt;dir&gt;</p>
<dd> name of output directory</p>
<dt>-t, &#8211;tail</p>
<dd> Continue reading after end-of-file (like tail -f). Use system tail if available. </p>
</dl>
<h2>Output formats</h2>
<dl>
<dt>-T, &#8211;text</p>
<dd> Output text (default)</p>
<dt>-H, &#8211;html</p>
<dd> Output HTML</p>
<dt>-M, &#8211;pango</p>
<dd> Output Pango markup</p>
<dt>-L, &#8211;latex</p>
<dd> Output LaTeX</p>
<dt>-P, &#8211;tex</p>
<dd> Output Plain TeX</p>
<dt>-R, &#8211;rtf</p>
<dd> Output RTF</p>
<dt>-B, &#8211;bbcode</p>
<dd> Output BBCode </p>
</dl>
<h2>Format options</h2>
<dl>
<dt> -a, &#8211;anchors</p>
<dd> Add HTML line anchors (assumes -l)</p>
<dt>-d, &#8211;doc-title</p>
<dd> Set HTML/LaTeX document title</p>
<dt>-f, &#8211;fragment</p>
<dd> Omit HTML header and footer</p>
<dt>-F, &#8211;font=&lt;font&gt;</p>
<dd> Set HTML/RTF font face</p>
<dt>-l, &#8211;line-numbers</p>
<dd> Print line numbers in output file</p>
<dt>-r, &#8211;style-ref=&lt;rf&gt;</p>
<dd> Set HTML/TeX/LaTeX stylesheet path</p>
<dt>-s, &#8211;font-size=&lt;num?&gt;</p>
<dd> Set HTML/RTF font size</p>
<dt>-e, &#8211;encoding=&lt;enc&gt;</p>
<dd> Set HTML encoding (must match input file encoding); omit encoding information if enc=NONE</p>
<dt>-p, &#8211;plain</p>
<dd> Ignore ANSI formatting information</p>
<dt>-w, &#8211;wrap=&lt;len&gt;</p>
<dd> Wrap long lines</p>
<dt>&#8211;wrap-no-numbers</p>
<dd> Omit line numbers of wrapped lines (assumes -l) </p>
</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd> print help</p>
<dt>-v, &#8211;version</p>
<dd> print version and license info </p>
</dl>
<p> If no in- or output files are specified, stdin and stdout will be used for in- or output. Plain text will be generated, if no output format is given. </p>
<h2>Examples</h2>
<p> File conversions: </p>
<p> ansifilter -i text_with_ansi.txt -o text_without_ansi.txt </p>
<p> tail -f server.log | ansifilter </p>
<p> ansifilter *.txt </p>
<h2>AUTHORS</h2>
<p> Andre Simon &lt;andre.simon1 [at] gmx.de&gt;</p>
<h2>SEE ALSO</h2>
<p> README file and webpage at <a rel="nofollow" href="http://www.andre-simon.de/">http://www.andre-simon.de/</a> and <a href="http://wiki.andre-simon.de.">http://wiki.andre-simon.de.</a> </p>
<h2>Index</h2>
