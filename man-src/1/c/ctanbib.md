---
title: "ctanbib(1)"
name: "ctanbib"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctanbib/"
---

<h2 class="name">NAME</h2>
 

 ctanbib - retrieve bibliographic information for packages hosted on CTAN. 

<h2>SYNOPSIS</h2>

 ctanbib &lt;options&gt; [package name]

<h2>DESCRIPTION</h2>

 This command can retrieve bibliographic information for TeX packages hosted on CTAN in the BibTeX format.

<h2>OPTIONS</h2>

<dl>
<dt>-c,--ctan
<dd> use @ctan type instead of @manual. The difference between the two is that the url field contains package CTAN path, instead of link to the package.
<dt>-C,--CTAN
<dd> like --ctan option, but use original url instead of CTAN path.
<dt>-h,--help
<dd> print the help message.
<dt>-v,--version
<dd> print the version info.</dl>

<h2>EXAMPLES</h2>

 

 $ ctanbib latex 

 

 This invocation will print data in the BibLaTeX format to the standard output: 

 <pre><code>
@manual
{
    latex,
        title = {The Latex package},
        subtitle = {A TeX macro package that defines LaTeX},
        author = {Lamport, Leslie and The LaTeX Team},
        url = { http : // www.latex-project.org/},
                    urldate = {2018 - 08 - 23},
                date = {2018 - 04 - 01},
                version = {PL 5}
        }
</code></pre> 

 

 The --ctan option: 

 $ ctanbib -c hyperref 

 

 This produces bib record with the @ctan type: 

 <pre><code>
@ctan
{hyperref,
title = {The Hyperref package},
subtitle = {Extensive support for hypertext in LaTeX},
author = {Rahtz, Sebastian and Oberdiek, Heiko},
url = {/macros/latex/contrib/hyperref},
urldate = {2018-08-27}, 
date = {},
version = {6.86b}
}
</code></pre> 

<h2>See also</h2>

 See ctanbib-doc.pdf for more details

<h2>BUGS</h2>

 No known bugs.

<h2>AUTHOR</h2>

 Michal Hoftich (michal.h21 [at] gmail.com)

<h2>LICENSE</h2>

 Permission is granted to copy, distribute and/or modify this software under the terms of the LaTeX Project Public License, version 1.3. 

 

<h2>Index</h2>


