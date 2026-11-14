---
title: "dvi2tty(1)"
name: "dvi2tty"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvi2tty/"
description: "dvi2tty – preview a TeX DVI file on an ordinary ASCII terminal"
---

<h2 class="name">NAME</h2>
<p> dvi2tty &#8211; preview a TeX DVI file on an ordinary ASCII terminal </p>
<h2>SYNOPSIS</h2>
<p> <code>dvi2tty</code> [ options ] dvifile</p>
<h2>DESCRIPTION</h2>
<p> <i>dvi2tty</i> converts a TeX DVI file to a format that is appropriate for terminals and line printers. The program is intended to be used for preliminary proofreading of TeX-ed documents. By default the output is directed to the terminal, possibly through a pager (depending on how the program was installed), but it can be directed to a file or a pipe. </p>
<p> The output leaves much to be desired, but is still useful if you want to avoid walking to the laser printer (or whatever) for each iteration of your document.<br />
 Since <i>dvi2tty</i> produces output for terminals and line printers the representation of documents is naturally quite primitive. In principle font changes are totally ignored, but <i>dvi2tty</i> recognizes a few mathematical and special symbols that can be displayed on an ordinary ASCII terminal, such as the &#8216;+&#8217; and &#8216;-&#8216; symbol. </p>
<p> If the width of the output text requires more columns than fits in one line (cf. the -w option) it is broken into several lines by <i>dvi2tty</i> although they will be printed as one line on regular TeX output devices (e.g., laser printers). To show that a broken line is really just one logical line an asterisk (&#8220;*&#8221;) in the last position means that the logical line is continued on the next physical line output by <i>dvi2tty.</i> Such a continuation line is started with a space and an asterisk in the first two columns. </p>
<p> Options may be specified in the environment variable DVI2TTY. Any option on the command line, conflicting with one in the environment, will override the one from the environment. </p>
<p> <code>Options:</code> </p>
<dl>
<dt><code>-o file</code></p>
<dd> Write output to file &#8220;file&#8221;.</p>
<dt><code>-p list</code></p>
<dd> Print the pages chosen by list. Numbers refer to TeX page numbers (known as 
