---
title: "opdvips(1)"
name: "opdvips"
section: "1"
letter: "o"
url: "/docs/linux/man/1-opdvips/"
description: "dvips – convert a TeX DVI file to PostScript"
---

<h2>NAME</h2>
<p> dvips &#8211; convert a TeX DVI file to PostScript</p>
<h2>SYNOPSIS</h2>
<p> <code>dvips</code> [ <i>options</i> ] <i>file</i>[<code>.dvi</code>]</p>
<h2>DESCRIPTION</h2>
<p> THIS MAN PAGE IS OBSOLETE! See the Texinfo documentation instead. You can read it either in Emacs or with the standalone <code>info</code> program which comes with the GNU texinfo distribution as prep.ai.mit.edu:pub/gnu/texinfo*.tar.gz. </p>
<p> The program <code>dvips</code> takes a DVI file <i>file</i>[<code>.dvi</code>] produced by TeX (or by some other processor such as GFtoDVI) and converts it to PostScript, normally sending the result directly to the (laser)printer. The DVI file may be specified without the <code>.dvi</code> extension. Fonts used may either be resident in the printer or defined as bitmaps in PK files, or a `virtual&#8217; combination of both. If the <code>mktexpk</code> program is installed, <code>dvips</code> will automatically invoke METAFONT to generate fonts that don&#8217;t already exist. </p>
<p> For more information, see the Texinfo manual <i>dvips.texi</i>, which should be installed somewhere on your system, hopefully accessible through the standard Info tree.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Conserve memory by making three passes over the .dvi file instead of two and only loading those characters actually used. Generally only useful on machines with a very limited amount of memory, like some PCs.</p>
<dt><code>-A</code></p>
<dd> Print only odd pages (TeX pages, not sequence pages).</p>
<dt><code>-b num</code></p>
<dd> Generate <i>num</i> copies of each page, but duplicating the page body rather than using the <i>#numcopies</i> option. This can be useful in conjunction with a header file setting <i>op-hook</i> to do color separations or other neat tricks.</p>
<dt><code>-B</code></p>
<dd> Print only even pages (TeX pages, not sequence pages).</p>
<dt><code>-c num</code></p>
<dd> Generate <i>num</i> copies of every page. Default is 1. (For collated copies, see the <i>-C</i> option below.)</p>
<dt><code>-C num</code></p>
<dd> Create <i>num </i> copies, but collated (by replicating the data in the PostScript file). Slower than the <i>-c</i> option, but easier on the hands, and faster than resubmitting the same PostScript file multiple times.</p>
<dt><code>-d num</code></p>
<dd> Set the debug flags. This is intended only for emergencies or for unusual fact-finding expeditions; it will work only if <code>dvips</code> has been compiled with the DEBUG option. If nonzero, prints additional information on standard error. The number is taken as a set of independent bits. The meaning of each bit follows. 1=specials; 2=paths; 4=fonts; 8=pages; 16=headers; 32=font compression; 64=files; 128=memory; 256=Kpathsea <a href="/docs/linux/man/2-stat/">stat</a>(2) calls; 512=Kpathsea hash table lookups; 1024=Kpathsea path element expansion; 2048=Kpathsea searches. To trace everything having to do with file searching and opening, use 3650 (2048 + 1024 + 512 + 64 + 2). To track all classes, you can use `-1&#8242; (output is extremely voluminous).</p>
<dt><code>-D num</code></p>
<dd> Set the resolution in dpi (dots per inch) to <i>num</i>. This affects the choice of bitmap fonts that are loaded and also the positioning of letters in resident PostScript fonts. Must be between 10 and 10000. This affects both the horizontal and vertical resolution. If a high resolution (something greater than 400 dpi, say) is selected, the <i>-Z</i> flag should probably also be used.</p>
<dt><code>-e num</code></p>
<dd> Make sure that each character is placed at most this many pixels from its `true&#8217; resolution-independent position on the page. The default value of this parameter is resolution dependent. Allowing individual characters to `drift&#8217; from their correctly rounded positions by a few pixels, while regaining the true position at the beginning of each new word, improves the spacing of letters in words.</p>
<dt><code>-E</code></p>
<dd> makes <code>dvips</code> attempt to generate an EPSF file with a tight bounding box. This only works on one-page files, and it only looks at marks made by characters and rules, not by any included graphics. In addition, it gets the glyph metrics from the <i>tfm</i> file, so characters that lie outside their enclosing <i>tfm</i> box may confuse it. In addition, the bounding box might be a bit too loose if the character glyph has significant left or right side bearings. Nonetheless, this option works well for creating small EPSF files for equations or tables or the like. (Note, of course, that <code>dvips</code> output is resolution dependent and thus does not make very good EPSF files, especially if the images are to be scaled; use these EPSF files with a great deal of care.)</p>
<dt><code>-f</code></p>
<dd> Run as a filter. Read the <i>.dvi</i> file from standard input and write the PostScript to standard output. The standard input must be seekable, so it cannot be a pipe. If you must use a pipe, write a shell script that copies the pipe output to a temporary file and then points <code>dvips</code> at this file. This option also disables the automatic reading of the <i>PRINTER</i> environment variable, and turns off the automatic sending of control D if it was turned on with the <i>-F</i> option or in the configuration file; use <i>-F</i> after this option if you want both.</p>
<dt><code>-F</code></p>
<dd> Causes Control-D (ASCII code 4) to be appended as the very last character of the PostScript file. This is useful when <code>dvips</code> is driving the printer directly instead of working through a spooler, as is common on extremely small systems. NOTE! DO NOT USE THIS OPTION!</p>
<dt><code>-G</code></p>
<dd> Causes <code>dvips</code> to shift non-printing characters to higher-numbered positions. This may be useful sometimes.</p>
<dt><code>-h name</code></p>
<dd> Prepend file <i>name</i> as an additional header file. (However, if the name is simply `-&#8216; suppress all header files from the output.) This header file gets added to the PostScript <i>userdict</i>.</p>
<dt><code>-i</code></p>
<dd> Make each section be a separate file. Under certain circumstances, <code>dvips</code> will split the document up into `sections&#8217; to be processed independently; this is most often done for memory reasons. Using this option tells <code>dvips</code> to place each section into a separate file; the new file names are created replacing the suffix of the supplied output file name by a three-digit sequence number. This option is most often used in conjunction with the <i>-S</i> option which sets the maximum section length in pages. For instance, some phototypesetters cannot print more than ten or so consecutive pages before running out of steam; these options can be used to automatically split a book into ten-page sections, each to its own file.</p>
<dt><code>-j</code></p>
<dd> Download only needed characters from Type 1 fonts. This is the default in the current release. Some debugging flags trace this operation. You can also control partial downloading on a per-font basis, via the <code>psfonts.map</code> file.</p>
<dt><code>-k</code></p>
<dd> Print crop marks. This option increases the paper size (which should be specified, either with a paper size special or with the <i>-T</i> option) by a half inch in each dimension. It translates each page by a quarter inch and draws cross-style crop marks. It is mostly useful with typesetters that can set the page size automatically.</p>
<dt><code>-K</code></p>
<dd> This option causes comments in included PostScript graphics, font files, and headers to be removed. This is sometimes necessary to get around bugs in spoolers or PostScript post-processing programs. Specifically, the %%Page comments, when left in, often cause difficulties. Use of this flag can cause some included graphics to fail, since the PostScript header macros from some software packages read portions of the input stream line by line, searching for a particular comment. This option has been turned off by default because PostScript previewers and spoolers have been getting better.</p>
<dt><code>-l num</code></p>
<dd> The last page printed will be the first one numbered <i>num</i> Default is the last page in the document. If the <i>num</i> is prefixed by an equals sign, then it (and any argument to the <i>-p</i> option) is treated as a sequence number, rather than a value to compare with <i>
