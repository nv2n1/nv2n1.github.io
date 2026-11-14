---
title: "pdfatfi(1)"
name: "pdfatfi"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdfatfi/"
---

<h2 class="name">NAME</h2>
 

 pdfatfi - Help program for the LaTeX package attachfile2. 

<h2>SYNOPSIS</h2>

 pdfatfi &lt;command&gt; [&lt;options&gt;] &lt;file[.atfi]&gt;]

<h2>DESCRIPTION</h2>

 Helper program for the LaTeX package attachfile2. 

 This package also tries to get and add meta information data, such as file size, file date, checksum, .... 

 The script pdfatfi.pl is provided for use with old versions of pdfTeX and XeTeX that do not provide access to file metadata. 

 The use of the Perl script is not mandatory. This data can be shown by PDF viewers, but they are not a requirement of the PDF specification. 

 Package attachfile2 and the Perl script communicate via an auxiliary file with file extension .atfi. The script is used between two LaTeX runs and updates the auxiliary file. 

 <pre>
latex test
pdfatfi test
latex test
dvips test
ps2pdf test.ps test.pdf
</pre> 

<h2>OPTIONS</h2>

 Various options are supported
<dl>
<dt>--help
<dd> Show help text.
<dt>--version
<dd> Print version number
<dt>--(no)quiet
<dd> Suppress/don't suppress messages
<dt>--(no)verbose
<dd> Verbose (not verbose) printing.
<dt>--(no)debug
<dd> Debug infomation printed (not printed)</dl>

<h2>BUGS</h2>

 Please log issues on the GitHub homepage: 
 <a rel="nofollow" HREF="https://github.com/ho-tex/attachfile2/issues.">https://github.com/ho-tex/attachfile2/issues.</a>

<h2>AUTHOR</h2>

 Heiko Oberdiek (ho-tex [at] tug.org)

<h2>SEE ALSO</h2>

 See attachfile2.pdf for more details. 

<h2>Index</h2>


