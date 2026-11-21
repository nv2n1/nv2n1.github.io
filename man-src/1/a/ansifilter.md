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
<dt>-i, &#8211;input=&lt;file&gt;</dt>
<dd> name of input file</dd>
<dt>-o, &#8211;output=&lt;file&gt;</dt>
<dd> name of output file</dd>
<dt>-O, &#8211;outdir=&lt;dir&gt;</dt>
<dd> name of output directory</dd>
<dt>-t, &#8211;tail</dt>
<dd> Continue reading after end-of-file (like tail -f). Use system tail if available. </dd>
</dl>
<h2>Output formats</h2>
<dl>
<dt>-T, &#8211;text</dt>
<dd> Output text (default)</dd>
<dt>-H, &#8211;html</dt>
<dd> Output HTML</dd>
<dt>-M, &#8211;pango</dt>
<dd> Output Pango markup</dd>
<dt>-L, &#8211;latex</dt>
<dd> Output LaTeX</dd>
<dt>-P, &#8211;tex</dt>
<dd> Output Plain TeX</dd>
<dt>-R, &#8211;rtf</dt>
<dd> Output RTF</dd>
<dt>-B, &#8211;bbcode</dt>
<dd> Output BBCode </dd>
</dl>
<h2>Format options</h2>
<dl>
<dt> -a, &#8211;anchors</dt>
<dd> Add HTML line anchors (assumes -l)</dd>
<dt>-d, &#8211;doc-title</dt>
<dd> Set HTML/LaTeX document title</dd>
<dt>-f, &#8211;fragment</dt>
<dd> Omit HTML header and footer</dd>
<dt>-F, &#8211;font=&lt;font&gt;</dt>
<dd> Set HTML/RTF font face</dd>
<dt>-l, &#8211;line-numbers</dt>
<dd> Print line numbers in output file</dd>
<dt>-r, &#8211;style-ref=&lt;rf&gt;</dt>
<dd> Set HTML/TeX/LaTeX stylesheet path</dd>
<dt>-s, &#8211;font-size=&lt;num?&gt;</dt>
<dd> Set HTML/RTF font size</dd>
<dt>-e, &#8211;encoding=&lt;enc&gt;</dt>
<dd> Set HTML encoding (must match input file encoding); omit encoding information if enc=NONE</dd>
<dt>-p, &#8211;plain</dt>
<dd> Ignore ANSI formatting information</dd>
<dt>-w, &#8211;wrap=&lt;len&gt;</dt>
<dd> Wrap long lines</dd>
<dt>&#8211;wrap-no-numbers</dt>
<dd> Omit line numbers of wrapped lines (assumes -l) </dd>
</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</dt>
<dd> print help</dd>
<dt>-v, &#8211;version</dt>
<dd> print version and license info </dd>
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
