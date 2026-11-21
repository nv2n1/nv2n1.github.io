---
title: "latex2png(1)"
name: "latex2png"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latex2png/"
description: "latex2png – manual page for latex2png 1.1"
---

<h2>NAME</h2>
<p> latex2png &#8211; manual page for latex2png 1.1</p>
<h2>DESCRIPTION</h2>
<p> latex2png <code>&#8212;</code> Convert a LaTeX file to a PNG image </p>
<p> USAGE: latex2png [-d density] [-h] [-k] [-c] [-g] [-m] [-H home dir] file[.tex|.eps] </p>
<p> The <i>latex2png</i> command converts a LaTeX file into a PNG image. The first page is translated into an image at the specified resolution. <i>latex2png</i> can also be used to convert encapsulated postscript (EPS) files to PNG images.</p>
<h3>OPTIONS:</h3>
<dl>
<dt> <code>-c</code> produce color image</dt>
<dt><code>-d</code> density</dt>
<dd> <i>density </i></dd>
<dd>is the number of dots per inch to use in the created image (default 144 dpi)</dd>
<dt> <code>-g</code> produce gray images</dt>
<dt><code>-h</code> help</dt>
<dd>
</dd><dt><code>-H</code> home_dir</dt>
<dd> <i>home_dir </i></dd>
<dd>is a directory to be included in search path (default is directory that contains the LaTeX file). This is used to create PNG images in another directory (e.g., /tmp) and still allow LaTeX to find files that it needs to include.</dd>
<dt><code>-k</code> keep intermediate files (for debugging)</dt>
<dd>
</dd><dt><code>-m</code> produce monochrome (black and white) image</dt>
<dd> (default)</dd>
<dt><code>-v</code> version</dt>
<dd></dd></dl>
<h3>EXAMPLES:</h3>
<dl>
<dt>latex2png <code>-d</code> 144 /tmp/file</dt>
<dd> #create /tmp/file.png at 144 dpi</dd>
<dt>latex2png file.eps</dt>
<dd> #create file.png</dd>
<dt>latex2png file.tex</dt>
<dd> #create file.png via latex</dd>
<dt>latex2png <code>-H</code> . /tmp/file</dt>
<dd> #search the cwd for image files</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>latex2png</code> is a part of <code>latex2rtf</code> and has a special mode to assist in finding the baseline of a latex equation. Documentation for <code>latex2rtf </code> may be found in <code>latex2rtf.info,</code> the PDF file <code>latex2rtf.pdf</code> or the HTML file <code>latex2rtf.html</code> which are made from the TeXInfo source file <code>latex2rtf.texi.</code> </p>
