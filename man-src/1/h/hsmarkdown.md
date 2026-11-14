---
title: "hsmarkdown(1)"
name: "hsmarkdown"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hsmarkdown/"
---

<h2 class="name">NAME</h2>
 

 

 hsmarkdown - convert markdown-formatted text to HTML 

<h2>SYNOPSIS</h2>

 

 hsmarkdown [input-file]...

<h2>DESCRIPTION</h2>

 

 hsmarkdown converts markdown-formatted text to HTML. It is designed to be usable as a drop-in replacement for John Gruber's Markdown.pl. 

 If no input-file is specified, input is read from stdin. Otherwise, the input-files are concatenated (with a blank line between each) and used as input. Output goes to stdout by default. For output to a file, use shell redirection: 

 
hsmarkdown input.txt&nbsp;<wbr>&gt;&nbsp;<wbr>output.html 

 hsmarkdown is implemented as a symlink to the <a HREF="/docs/linux/man/1-pandoc/">pandoc</a>(1) executable. When called under the name hsmarkdown, pandoc behaves as if it had been called with the options --from markdown --to html --strict and disables all other options. (Command-line options will be interpreted as filenames, as they are by Markdown.pl.)

<h2>SEE ALSO</h2>

 

 <a HREF="/docs/linux/man/1-pandoc/">pandoc</a>(1). The README file distributed with Pandoc contains full documentation. 

 The Pandoc source code and all documentation may be downloaded from &lt;<a rel="nofollow" HREF="http://johnmacfarlane.net/pandoc/">http://johnmacfarlane.net/pandoc/</a>&gt;.

<h2>AUTHORS</h2>

 John MacFarlane. 

 

<h2>Index</h2>


