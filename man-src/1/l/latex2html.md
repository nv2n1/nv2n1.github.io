---

title: "latex2html(1)"
name: "latex2html"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latex2html/"
description: "latex2html – translate LaTeX files to HTML (HyperText Markup Language)"
---

<p> latex2html - translate LaTeX files to HTML (HyperText Markup Language) </p>
<h2>SYNOPSIS</h2>
<p> <code>latex2html</code> <i>[options]</i> [target [target ...]]  </p>
<h2>DESCRIPTION</h2>
<p> This manual page explains the <code>LaTeX2HTML</code> utility, which is a <code>Perl </code> program that translates <code>LaTeX</code> document into <code>HTML </code> format. For each source file given as an argument the translator will create a directory containing the corresponding HTML files. For details and examples, please consult the online html documentation, a copy of which should be available in <i>/usr/share/doc/latex2html/manual.ps.gz</i> or <i>/usr/share/doc/latex2html/html/</i>  </p>
<h2>CAVEAT</h2>
<p> This documentation has been derived from the TeX manual, and may not be up to date. Please refer to the online manual for authoritative documentation.  </p>
<h2>Options controlling Titles, File-Names and Sectioning</h2>
<dl>
<dt><code>-t &lt;top-page-title&gt;</code></dt>
<dd> <p> Same as setting: <i>$TITLE = &lt;top-page-title&gt;;</i> Name the document using this title. </p>
 </dd>
<dt><code>-short_extn</code></dt>
<dd> <p> Same as setting: <i>$SHORTEXTN = 1;</i> Use a filename prefix of .htm for the produced <code>HTML </code> files. This is particularly useful for creating pages to be stored on CD-ROM or other media, to be used with operating systems that require a 3-character extension. </p>
 </dd>
<dt><code>-long_titles &lt;num&gt;</code></dt>
<dd> <p> Same as setting: <i>$LONG_TITLES = &lt;num&gt;;</i> Instead of the standard names: node1.html, node2.html,... the filenames for each <code>HTML </code> page are constructed from the first &lt;num&gt; words of the section heading for that page, separated by the `_&#8216; character. Commas and common short words (a an to by of and for the) are omitted from both title and word-count. Warning: Use this switch with great caution. Currently there are no checks for uniqueness of names or overall length. Very long names can easily result from using this feature. </p>
 </dd>
<dt><code>-custom_titles</code></dt>
<dd> <p> Same as setting: <i>$CUSTOM_TITLES = 1;</i> Instead of the standard names: node1.html, node2.html, ... the filenames for each <code>HTML </code> page are constructed using a <code>Perl </code> subroutine named custom_title_hook . The user may define his/her own version of this subroutine, within a .latex2html-init file say, to override the default (which uses the standard names). This subroutine takes the section-heading as a parameter and must return the required name, or the empty string (default). </p>
 </dd>
<dt><code>-dir &lt;output-directory&gt;</code></dt>
<dd> <p> Same as setting: <i>$DESTDIR = &lt;output-directory&gt;;</i> Redirect the output to the specified directory. The default behaviour is to create (or reuse) a directory having the same name as the prefix of the document being processed. </p>
 </dd>
<dt><code>-no_subdir</code></dt>
<dd> <p> Same as setting: <i>$NO_SUBDIR = 1;</i> Place the generated <code>HTML </code> files into the current directory. This overrides any <i>$DESTDIR </i> setting. </p>
 </dd>
<dt><code>-prefix &lt;filename-prefix&gt;</code></dt>
<dd> <p> Same as setting: <i>$PREFIX = &lt;filename-prefix&gt;;</i> The &lt;filename-prefix&gt; will be prepended to all .gif, .pl and .html files produced, except for the top-level .html file; it may include a (relative) directory path. This will enable multiple products of <code>LaTeX2HTML </code> to peacefully coexist in the same directory. However, do not attempt to simultaneously run multiple instances of <code>LaTeX2HTML </code> using the same output directory, else various temporary files will overwrite each other. </p>
 </dd>
<dt><code>-auto_prefix</code></dt>
<dd> <p> Same as setting: <i>$AUTO_PREFIX = 1;</i> Constructs the prefix as `&lt;title&gt;-&#8216; to be prepended to all the files produced, where &lt;title&gt; is the name of the <code>LaTeX </code> file being processed. (Note the `-&#8216; in this prefix.) This overrides any <i>$PREFIX </i> setting. </p>
 </dd>
<dt><code>-no_auto_link</code></dt>
<dd> <p> Same as setting: <i>$NO_AUTO_LINK = 1;</i> If $NO_AUTO_LINK is empty and variables <i>$LINKPOINT </i> and <i>$LINKNAME </i> are defined appropriately (as is the default in the latex2html.config file), then a hard link to the main <code>HTML </code> page is produced, using the name supplied in <i>$LINKNAME. </i> Typically this is index.html; on many systems a file of this name will be used, if it exists, when a browser tries to view a URL which points to a directory. On other systems a different value for <i>$LINKNAME </i> may be appropriate. Typically <i>$LINKPOINT</i> has value <i>$FILE.html, </i> but this may also be changed to match whichever HTML page is to become the target of the automatic link. Use of the -no_auto_link switch cancels this automatic linking facility, when not required for a particular document. </p>
 </dd>
<dt><code>-split &lt;num&gt;</code></dt>
<dd> <p> Same as setting: <i>$MAX_SPLIT_DEPTH = &lt;num&gt;; (default is 8)</i> Stop splitting sections into separate files at this depth. Specifying -split 0 will put the entire document into a single <code>HTML </code> file. See below for the different levels of sectioning. Also see the next item for how to set a ``relative&#8217;&#8216; depth for splitting. </p>
 </dd>
<dt><code>-split +&lt;num&gt;</code></dt>
<dd> <p> Same as setting: <i>$MAX_SPLIT_DEPTH = -&lt;num&gt;; (default is 8)</i> The level at which to stop splitting sections is calculated ``relative to&#8217;&#8216; the shallowest level of sectioning that occurs within the document. For example, if the document contains \section commands, but no \part or \chapter commands, then -split +1 will cause splitting at each \section but not at any deeper level; whereas -split +2 or -split +3 also split down to \subsection and \subsubsection commands respectively. Specifying -split +0 puts the entire document into a single <code>HTML </code> file. </p>
 </dd>
<dt><code>-link &lt;num&gt;</code></dt>
<dd> <p> Same as setting: <i>$MAX_LINK_DEPTH = &lt;num&gt;; (default is 4)</i> For each node, create links to child nodes down to this much deeper than the node&#8217;s sectioning-level. Specifying -link 0 will show no links to child nodes from that page, -link 1 will show only the immediate descendants, etc. A value at least as big as that of the -split &lt;num&gt; depth will produce a mini table-of-contents (when not empty) on each page, for the tree structure rooted at that node. When the page has a sectioning-level less than the -split depth, so that the a mini table-of-contents has links to other <code>HTML </code> pages, this table is located at the bottom of the page, unless placed elsewhere using the \tableofchildlinks command. On pages having a sectioning-level just less than the -split depth the mini table-of-contents contains links to subsections etc. occurring on the same <code>HTML </code> page. Now the table is located at the top of this page, unless placed elsewhere using the \tableofchildlinks command. </p>
 </dd>
<dt><code>-toc_depth &lt;num&gt;</code></dt>
<dd> <p> Same as setting: <i>$TOC_DEPTH = &lt;num&gt;; (default is 4)</i> Sectioning levels down to &lt;num&gt; are to be included within the Table-of-Contents tree. </p>
 </dd>
<dt><code>-toc_stars</code></dt>
<dd> <p> Same as setting: <i>$TOC_STARS = 1;</i> Sections created using the starred-form of sectioning commands are included within the Table-of-Contents. As with <code>LaTeX, </code> normally such sections are not listed. </p>
 </dd>
<dt><code>-show_section_numbers</code></dt>
<dd> <p> Same as setting: <i>$SHOW_SECTION_NUMBERS = 1;</i> Show section numbers. By default section numbers are not shown, so as to encourage the use of particular sections as stand-alone documents. In order to be shown, section titles must be unique and must not contain inlined graphics. </p>
 </dd>
<dt><code>-unsegment</code></dt>
<dd> <p> Same as setting: <i>$UNSEGMENT = 1;</i> Treat a segmented document (see the section about document segmentation) like it were not segmented. This will cause the translator to concatenate all segments and process them as a whole. You might find this useful to check a segmented document for consistency. For all documents the sectioning levels referred to above are: </p>
 </dd>
<dl>
<dd> <p> <br />
&nbsp;0&nbsp;<wbr>&nbsp;document <br />
&nbsp;1&nbsp;<wbr>&nbsp;part <br />
&nbsp;2&nbsp;<wbr>&nbsp;chapter <br />
&nbsp;3&nbsp;<wbr>&nbsp;section <br />
&nbsp;4&nbsp;<wbr>&nbsp;subsection <br />
&nbsp;5&nbsp;<wbr>&nbsp;subsubsection <br />
&nbsp;6&nbsp;<wbr>&nbsp;paragraph <br />
&nbsp;7&nbsp;<wbr>&nbsp;subparagraph <br />
&nbsp;8&nbsp;<wbr>&nbsp;subsubparagraph </p>
 </dd></dl>
</dl>
<p> These levels apply even when the document contains no sectioning for the shallower levels; e.g. no \part or \chapter commands is most common, especially when using <code>LaTeX&#8217;s </code> article document-class.  </p>
<h2>Options controlling Extensions and Special Features</h2>
<p> The switches described here govern the type of <code>HTML </code> code that can be generated, and how to choose between the available options when there are alternative strategies for implementing portions of <code>LaTeX </code> code. </p>
<dl>
<dt><code>-html_version (2.0|3.2|4.0|5.0)[,(math|i18n)]*</code></dt>
<dd> <p> Same as setting: <i>$HTML_VERSION = ... ;</i> This specifies both the <code>HTML </code> version to generate, and any extra (non-standard) <code>HTML </code> features that may be required. The version number corresponds to a published DTD for an <code>HTML </code> standard. A corresponding <code>Perl </code> file in the versions/ subdirectory is loaded; these files are named `html&lt;num&gt;.pl&#8217;. Following the version number, a comma-separated list of extensions can be given. Each corresponds to a file `&lt;name&gt;.pl&#8217; also located in the versions/ subdirectory. When such a file is loaded the resulting HTML code can no longer be expected to validate with the specified DTD. An exception is math when the -no_math switch is also used, which should still validate. Currently, versions 2.0, 3.2, 4.0 and 5.0 are available. The default version is usually set to be `5.0&#8217;, within latex2html.config. </p>
 </dd>
<dt><code>-no_tex_defs</code></dt>
<dd> <p> Same as setting: <i>$TEXDEFS = 0; (default is 1)</i> When <i>$TEXDEFS </i> is set (default) the file texdefs.perl will be read. This provides code to allow common TEX commands like \def, \newbox, \newdimen and others, to be recognised, especially within the document preamble. In the case of \def, the definition may even be fully interpreted, but this requires the pattern-matching to be not too complicated. If <i>$TEXDEFS </i> is `0&#8217; or empty, then texdefs.perl will not be loaded; the translator will make no attempt to interpret any raw TEX commands. This feature is intended to enable sophisticated authors the ability to insert arbitrary TEX commands in environments that are destined to be processed by <code>LaTeX </code> anyway; e.g. figures, theorems, pictures, etc. However this should rarely be needed, as now there is better support for these types of environment. There are now other methods to specify which chunks of code are to be passed to <code>LaTeX </code> for explicit image-generation; see the discussion of the makeimage environment. </p>
 </dd>
<dt><code>-external_file &lt;filename&gt;</code></dt>
<dd> <p> Same as setting: <i>$EXTERNAL_FILE = &lt;filename&gt;;</i> Specifies the prefix of the .aux file that this document should read. The .aux extension will be appended to this prefix to get the complete filename, with directory path if needed. This file could contain necessary information regarding citations, figure, table and section numbers from <code>LaTeX </code> and perhaps other information also. Use of this switch is vital for document segments, processed separately and linked to appear as if generated from a single LaTeX document. </p>
 </dd>
<dt><code>-font_size &lt;size&gt;</code></dt>
<dd> <p> Same as setting: <i>$FONT_SIZE = &lt;size&gt;;</i> This option provides better control over the font size of environments made into images using <code>LaTeX. </code> &lt;size&gt; must be one of the font sizes that <code>LaTeX </code> recognizes; i.e. `10pt&#8217;, `11pt&#8217;, `12pt&#8217;, etc. Default is `10pt&#8217;, or whatever option may have been specified on the \documentclass or \documentstyle line. Whatever size is selected, it will be magnified by the installation variables <i>$MATH_SCALE_FACTOR, </i> <i>$FIGURE_SCALE_FACTOR </i> and <i>$DISP_SCALE_FACTOR </i> as appropriate. Note: This switch provides no control over the size of text on the HTML pages. Such control is subject entirely to the user&#8217;s choices of settings for the browser windows. </p>
 </dd>
<dt><code>-scalable_fonts</code></dt>
<dd> <p> Same as setting: <i>$SCALABLE_FONTS = 1;</i> This is used when scalable fonts, such as PostScript versions of the TEX fonts, are available for image-generation. It has the effect of setting <i>$PK_GENERATION </i> to `1&#8217;, and <i>$DVIPS_MODE </i> to be empty, overriding any previous settings for these variables. </p>
 </dd>
<dt><code>-no_math</code></dt>
<dd> <p> Same as setting: <i>$NO_SIMPLE_MATH = 1;</i> Ordinarily simple mathematical expressions are set using the ordinary text font, but italicized. When part of the expression can not be represented this way, an image is made of the whole formula. This is called ``simple math&#8217;&#8216;. When <i>$NO_SIMPLE_MATH </i> is set, then all mathematics is made into images, whether simple or not. However, if the math extension is loaded, using the -html_version switch described earlier, then specifying -no_math produces a quite different effect. Now it is the special &lt;MATH&gt; tags and entities which are canceled. In their place a sophisticated scheme for parsing mathematical expressions is used. Images are made of those sub-parts of a formula which cannot be adequately expressed using (italicized) text characters and &lt;SUB&gt; and &lt;SUP&gt; tags. See the subsection on mathematics for more details. </p>
 </dd>
<dt><code>-local_icons</code></dt>
<dd> <p> Same as setting: <i>$LOCAL_ICONS = 1;</i> A copy of each of the icons actually used within the document is placed in the directory along with the <code>HTML </code> files and generated images. This allows the whole document to be fully self-contained, within this directory; otherwise the icons must be retrieved from a (perhaps remote) server. It is also the default behavior if $ICONSERVER is not set. The icons are normally copied from a subdirectory of the </p>
<p> <code>$LATEX2HTMLDIR,</code> <br />
&nbsp;set within latex2html.config. An alternative set of icons can be used by specifying a (relative) directory path in $ALTERNATIVE_ICONS to where the customised images can be found. </p>
 </dd>
<dt><code>-init_file &lt;file&gt;</code></dt>
<dd> <p> Load the specified initialisation file. This <code>Perl </code> file will be loaded after loading <i>$HOME/.latex2html-init, </i> or .latex2html-init in the local directory, if either file exists. It is read at the time the switch is processed, so the contents of the file may change any of the values of any of the variables that were previously established, as well as any default options. More than one initialisation file can be read in this way. [change_begin]98.1 </p>
 </dd>
<dt><code>-no_fork</code></dt>
<dd> <p> Same as setting: <i>$NOFORK = 1;</i> When set this disables a feature in the early part of the processing whereby some memory-intensive operations are performed by `forked&#8217; child processes. Some single-task operating systems, such as DOS, do not support this feature. Having <i>$NOFORK </i> set then ensures that unnecessary file-handles that are needed with the forked processes, are not consumed unnecessarily, perhaps resulting in a fatal <code>Perl </code> error. </p>
 </dd>
<dt><code>-iso_language &lt;type&gt;</code></dt>
<dd> <p> This enables you to specify a different language type than &#8216;EN&#8217; to be used in the DTD entries of the <code>HTML </code> document, e.g. &#8216;EN.US&#8217;. [change_end] 98.1 </p>
 </dd>
<dt><code>-short_index</code></dt>
<dd> <p> Same as setting: <i>$SHORT_INDEX = 1;</i> Creates shorter Index listings, using codified links; this is fully compatible with the makeidx package. </p>
 </dd>
<dt><code>-no_footnode</code></dt>
<dd> <p> Same as setting: <i>$NO_FOOTNODE = 1;</i> Suppresses use of a separate file for footnotes; instead these are placed at the bottom of the <code>HTML </code> pages where the references occur. When this option is used, it is frequently desirable to change the style of the marker used to indicate the presence of a footnote. This is done as in <code>LaTeX, </code> using code such as follows. \renewcommand{\thefootnote}{\arabic{footnote}} All the styles \arabic, \alph, \roman, \Alph and \Roman are available. [change_begin]98.1 </p>
 </dd>
<dt><code>-numbered_footnotes</code></dt>
<dd> <p> Same as setting: <i>$NUMBERED_FOOTNOTES = 1;</i> If this is set you will get every footnote applied with a subsequent number, to ease readability. [change_end] 98.1 </p>
 </dd>
<dt><code>-address &lt;author-address&gt;</code></dt>
<dd> <p> Same as setting: <i>$ADDRESS = &lt;author-address&gt;;</i> Sign each page with this address. See latex2html.config for an example using <code>Perl </code> code to automatically include the date. A user-defined <code>Perl </code> subroutine called &amp;custom_address can be used instead, if defined; it takes the value of <i>$ADDRESS </i> as a parameter, which may be used or ignored as desired. At the time when this subroutine will be called, variables named $depth, <i>$title, </i> <i>$file </i> hold the sectioning-level, title and filename of the <code>HTML </code> page being produced; <i>$FILE </i> holds the name of the filename for the title-page of the whole document. </p>
 </dd>
<dt><code>-info &lt;string&gt;</code></dt>
<dd> <p> Same as setting: <i>$INFO = &lt;string&gt;;</i> Generate a new section ``About this document&#8217;&#8216; containing information about the document being translated. The default is to generate such a section with information on the original document, the date, the user and the translator. An empty string (or the value `0&#8217;) disables the creation of this extra section. If a non-empty string is given, it will be placed as the contents of the ``About this document&#8217;&#8216; page instead of the default information. </p>
 </dd></dl>
<h2>Switches controlling Image Generation</h2>
<p> These switches affect whether images are created at all, whether old images are reused on subsequent runs or new ones created afresh, and whether anti-aliasing effects are used within the images themselves. </p>
<dl>
<dt><code>-use_dvipng</code></dt>
<dd> <p> Use the dvipng program to generate png images, rather than using dvips followed by gs. This method produces better alignment of math formulas which extend significantly above or below the line of text in which they are contained. </p>
 </dd>
<dt><code>-use_pdftex</code></dt>
<dd> <p> Generate intermediate images with pdflatex instead of plain latex. Produced PDF output will then be translated into images with GhostScript. Useful for pdflatex documents which cannot be translated by latex. </p>
 </dd>
<dt><code>-use_luatex</code></dt>
<dd> <p> Generate intermediate images with lualatex instead of plain latex. Produced PDF output will then be translated into images with GhostScript. Useful for lualatex documents which cannot be translated by latex or pdflatex. </p>
 </dd>
<dt><code>-use_luadvi</code></dt>
<dd> <p> Generate intermediate images with dvilualatex instead of plain latex. Useful for dvilualatex documents which cannot be translated by latex. </p>
 </dd>
<dt><code>-ascii_mode</code></dt>
<dd> <p> Same as setting: <i>$ASCII_MODE = $EXTERNAL_IMAGES = 1;</i> Use only ASCII characters and do not include any images in the final output. With -ascii_mode the output of the translator can be used on character-based browsers, such as lynx, which do not support inlined images (via the &lt;IMG&gt; tag). </p>
 </dd>
<dt><code>-nolatex</code></dt>
<dd> <p> Same as setting: <i>$NOLATEX = 1;</i> Disable the mechanism for passing unknown environments to <code>LaTeX </code> for processing. This can be thought of as ``draft mode&#8217;&#8216; which allows faster translation of the basic document structure and text, without fancy figures, equations or tables. (This option has been superseded by the -no_images option, see below.) </p>
 </dd>
<dt><code>-external_images</code></dt>
<dd> <p> Same as setting: <i>$EXTERNAL_IMAGES = 1;</i> Instead of including any generated images inside the document, leave them outside the document and provide hypertext links to them. </p>
 </dd>
<dt><code>-ps_images</code></dt>
<dd> <p> Same as setting: <i>$PS_IMAGES = $EXTERNAL_IMAGES = 1;</i> Use links to external PostScript files rather than inlined images in the chosen graphics format. </p>
 </dd>
<dt><code>-discard</code></dt>
<dd> <p> Same as setting: <i>$DISCARD_PS = 1;</i> The temporary PostScript files are discarded immediately after they have been used to create the image in the desired graphics format. </p>
 </dd>
<dt><code>-no_images</code></dt>
<dd> <p> Same as setting: <i>$NO_IMAGES = 1;</i> Do not attempt to produce any inlined images. The missing images can be generated ``off-line&#8217;&#8216; by restarting <code>LaTeX2HTML </code> with the option -images_only . </p>
 </dd>
<dt><code>-images_only</code></dt>
<dd> <p> Same as setting: <i>$IMAGES_ONLY = 1;</i> Try to convert any inlined images that were left over from previous runs of <code>LaTeX2HTML.</code> </p>
 </dd>
<dt><code>-reuse &lt;reuse_option&gt;</code></dt>
<dd> <p> Same as setting: <i>$REUSE = &lt;reuse_option&gt;;</i> This switch specifies the extent to which image files are to be shared or recycled. There are three valid options: [*] 0 Do not ever share or recycle image files. This choice also invokes an interactive session prompting the user about what to do about a pre-existing <code>HTML </code> directory, if it exists. [*] 1 Recycle image files from a previous run if they are available, but do not share identical images that must be created in this run. [*] 2 Recycle image files from a previous run and share identical images from this run. This is the default. A later section provides additional information about image-reuse. </p>
 </dd>
<dt><code>-no_reuse</code></dt>
<dd> <p> Same as setting: <i>$REUSE = 0;</i> Do not share or recycle images generated during previous translations. This is equivalent to -reuse 0 . (This will enable the initial interactive session during which the user is asked whether to reuse the old directory, delete its contents or quit.) </p>
 </dd>
<dt><code>-antialias</code></dt>
<dd> <p> Same as setting: <i>$ANTI_ALIAS = 1; (Default is 0.)</i> Generated images of figure environments and external PostScript files should use anti-aliasing. By default anti-aliasing is not used with these images, since this may interfere with the contents of the images themselves. </p>
 </dd>
<dt><code>-antialias_text</code></dt>
<dd> <p> Same as setting: <i>$ANTI_ALIAS_TEXT = 1; (Default is 1.)</i> Generated images of typeset material such as text, mathematical formulas, tables and the content of makeimage environments, should use anti-aliasing effects. The default is normally to use anti-aliasing for text, since the resulting images are much clearer on-screen. However the default may have been changed locally. </p>
 </dd>
<dt><code>-no_antialias</code></dt>
<dd> <p> Same as setting: <i>$ANTI_ALIAS = 0; (Default is 0.)</i> Generated images of figure environments and external PostScript files should not use anti-aliasing with images, though the local default may have been changed to use it. </p>
 </dd>
<dt><code>-no_antialias_text</code></dt>
<dd> <p> Same as setting: <i>$ANTI_ALIAS_TEXT = 0; (Default is 1.)</i> Generated images of typeset material should not use anti-aliasing effects. Although on-screen images of text are definitely improved using anti-aliasing, printed images can be badly blurred, even at 300dpi. Higher resolution printers do a much better job with the resulting grey-scale images. [change_begin]98.1 </p>
 </dd>
<dt><code>-white</code></dt>
<dd> <p> Same as setting: <i>$WHITE_BACKGROUND = 1; (Default is 1.)</i> Ensures that images of figure environments have a white background. Otherwise transparency effects may not work correctly. </p>
 </dd>
<dt><code>-no_white</code></dt>
<dd> <p> Same as setting: <i>$WHITE_BACKGROUND = &#8216;&#8216;; (Default is 1.)</i> Cancels the requirement that figure environments have a white background. </p>
 </dd>
<dt><code>-ldump</code></dt>
<dd> <p> Same as setting: <i>$LATEX_DUMP = 1; (Default is 0.)</i> Use this if you want to speed up image processing during the 2nd and subsequent runs of <code>LaTeX2HTML </code> on the same document. The translator now produces a <code>LaTeX </code> format-dump of the preamble to images.tex which is used on subsequent runs. This significantly reduces the startup time when <code>LaTeX </code> reads the images.tex file for image-generation. This process actually consumes additional time on the first run, since <code>LaTeX</code> is called twice -- once to create the format-dump, then again to load and use it. The pay-off comes with the faster loading on subsequent runs. Approximately 1 Meg of disk space is consumed by the dump file. [change_end] 98.1 </p>
 </dd></dl>
<h2>Switches controlling Navigation Panels</h2>
<p> The following switches govern whether to include one or more navigation panels on each <code>HTML </code> page, also which buttons to include within such a panel. </p>
<dl>
<dt><code>-no_navigation</code></dt>
<dd> <p> Same as setting: <i>$NO_NAVIGATION = 1;</i> Disable the mechanism for putting navigation links in each page. This overrides any settings of the <i>$TOP_NAVIGATION, </i> <i>$BOTTOM_NAVIGATION</i> and <i>$AUTO_NAVIGATION </i> variables. </p>
 </dd>
<dt><code>-top_navigation</code></dt>
<dd> <p> Same as setting: <i>$TOP_NAVIGATION = 1;</i> Put navigation links at the top of each page. </p>
 </dd>
<dt><code>-bottom_navigation</code></dt>
<dd> <p> Same as setting: <i>$BOTTOM_NAVIGATION = 1;</i> Put navigation links at the bottom of each page as well as the top. </p>
 </dd>
<dt><code>-auto_navigation</code></dt>
<dd> <p> Same as setting: <i>$AUTO_NAVIGATION = 1;</i> Put navigation links at the top of each page. Also put one at the bottom of the page, if the page exceeds <i>$WORDS_IN_PAGE </i> number of words (default = 450). </p>
 </dd>
<dt><code>-next_page_in_navigation</code></dt>
<dd> <p> Same as setting: <i>$NEXT_PAGE_IN_NAVIGATION = 1;</i> Put a link to the next logical page in the navigation panel. </p>
 </dd>
<dt><code>-previous_page_in_navigation</code></dt>
<dd> <p> Same as setting: <i>$PREVIOUS_PAGE_IN_NAVIGATION = 1;</i> Put a link to the previous logical page in the navigation panel. </p>
 </dd>
<dt><code>-contents_in_navigation</code></dt>
<dd> <p> Same as setting: <i>$CONTENTS_IN_NAVIGATION = 1;</i> Put a link to the table-of-contents in the navigation panel if there is one. </p>
 </dd>
<dt><code>-index_in_navigation</code></dt>
<dd> <p> Same as setting: <i>$INDEX_IN_NAVIGATION = 1;</i> Put a link to the index-page in the navigation panel if there is an index. </p>
 </dd></dl>
<h2>Switches for Linking to other documents</h2>
<p> When processing a single stand-alone document, the switches described in this section should not be needed at all, since the automatically generated navigation panels, described on the previous page should generate all the required navigation links. However if a document is to be regarded as part of a much larger document, then links from its first and final pages, to locations in other parts of the larger (virtual) document, need to be provided explicitly for some of the buttons in the navigation panel. The following switches allow for such links to other documents, by providing the title and URL for navigation panel hyperlinks. In particular, the ``Document Segmentation&#8217;&#8216; feature necessarily makes great use of these switches. It is usual for the text and targets of these navigation hyperlinks to be recorded in a Makefile, to avoid tedious typing of long command-lines having many switches. </p>
<dl>
<dt><code>-up_url &lt;URL&gt;</code></dt>
<dd> <p> Same as setting: <i>$EXTERNAL_UP_LINK = &lt;URL&gt;;</i> Specifies a universal resource locator (URL) to associate with the ``UP&#8217;&#8216; button in the navigation panel(s). </p>
 </dd>
<dt><code>-up_title &lt;string&gt;</code></dt>
<dd> <p> Same as setting: <i>$EXTERNAL_UP_TITLE = &lt;string&gt;;</i> Specifies a title associated with this URL. </p>
 </dd>
<dt><code>-prev_url &lt;URL&gt;</code></dt>
<dd> <p> Same as setting: <i>$EXTERNAL_PREV_LINK = &lt;URL&gt;;</i> Specifies a URL to associate with the ``PREVIOUS&#8217;&#8216; button in the navigation panel(s). </p>
 </dd>
<dt><code>-prev_title &lt;string&gt;</code></dt>
<dd> <p> Same as setting: <i>$EXTERNAL_PREV_TITLE = &lt;string&gt;;</i> Specifies a title associated with this URL. </p>
 </dd>
<dt><code>-down_url &lt;URL&gt;</code></dt>
<dd> <p> Same as setting: <i>$EXTERNAL_DOWN_LINK = &lt;URL&gt;;</i> Specifies a URL for the ``NEXT&#8217;&#8216; button in the navigation panel(s). </p>
 </dd>
<dt><code>-down_title &lt;string&gt;</code></dt>
<dd> <p> Same as setting: <i>$EXTERNAL_DOWN_TITLE = &lt;string&gt;;</i> Specifies a title associated with this URL. </p>
 </dd>
<dt><code>-contents &lt;URL&gt;</code></dt>
<dd> <p> Same as setting: <i>$EXTERNAL_CONTENTS = &lt;URL&gt;;</i> Specifies a URL for the ``CONTENTS&#8217;&#8216; button, for document segments that would not otherwise have one. </p>
 </dd>
<dt><code>-index &lt;URL&gt;</code></dt>
<dd> <p> Same as setting: <i>$EXTERNAL_INDEX = &lt;URL&gt;;</i> Specifies a URL for the ``INDEX&#8217;&#8216; button, for document segments that otherwise would not have an index. </p>
 </dd>
<dt><code>-biblio &lt;URL&gt;</code></dt>
<dd> <p> Same as setting: <i>$EXTERNAL_BIBLIO = &lt;URL&gt;;</i> Specifies the URL for the bibliography page to be used, when not explicitly part of the document itself. Warning: On some systems it is difficult to give text-strings &lt;string&gt; containing space characters, on the command-line or via a Makefile. One way to overcome this is to use the corresponding variable. Another way is to replace the spaces with underscores (_). </p>
 </dd></dl>
<h2>Switches for Help and Tracing</h2>
<p> The first two of the following switches are self-explanatory. When problems arise in processing a document, the switches -debug and -verbosity will each cause <code>LaTeX2HTML </code> to generate more output to the screen. These extra messages should help to locate the cause of the problem. </p>
<dl>
<dt><code>-tmp &lt;path&gt;</code></dt>
<dd> <p> Define a temporary directory to use for image generation. If &lt;path&gt; is 0, the standard temporary directory /tmp is used. </p>
 </dd>
<dt><code>-h(elp)</code></dt>
<dd> <p> Print out the list of all command-line options. </p>
 </dd>
<dt><code>-v</code></dt>
<dd> <p> Print the current version of <code>LaTeX2HTML.</code> </p>
 </dd>
<dt><code>-debug</code></dt>
<dd> <p> Same as setting: <i>$DEBUG = 1;</i> Run in debug-mode, displaying messages and/or diagnostic information about files read, and utilities called by <code>LaTeX2HTML.</code> Shows any messages produced by these calls. More extensive diagnostics, from the <code>Perl </code> debugger, can be obtained by appending the string `-w-&#8216; to the 1st line of the latex2html (and other) <code>Perl </code> script(s). </p>
 </dd>
<dt><code>-verbosity &lt;num&gt;</code></dt>
<dd> <p> Same as setting: <i>$VERBOSITY = &lt;num&gt;;</i> Display messages revealing certain aspects of the processing performed by <code>LaTeX2HTML </code> on the provided input file(s). The &lt;num&gt; parameter can be an integer in the range 0 to 8. Each higher value adds to the messages produced. </p>
 </dd>
<dt>0. </dt>
<dd> <p> No special tracing; as for versions of <code>LaTeX2HTML </code> prior to V97.1. </p>
 </dd>
<dt>1. </dt>
<dd> <p> (This is the default.) Show section-headings and the corresponding HTML file names, and indicators that major stages in the processing have been completed. </p>
 </dd>
<dt>2. </dt>
<dd> <p> Print environment names and identifier numbers, and new theorem-types. Show warnings as they occur, and indicators for more stages of processing. Print names of files for storing auxiliary data arrays. </p>
 </dd>
<dt>3. </dt>
<dd> <p> Print command names as they are encountered and processed; also any unknown commands encountered while pre-processing. Show names of new commands, environments, theorems, counters and counter-dependencies, for each document partition. </p>
 </dd>
<dt>4. </dt>
<dd> <p> Indicate command-substitution the pre-process of math-environments. Print the contents of unknown environments for processing in <code>LaTeX, </code> both before and after reverting to <code>LaTeX</code> source. Show all operations affecting the values of counters. Also show links, labels and sectioning keys, at the stages of processing. </p>
 </dd>
<dt>5. </dt>
<dd> <p> Detail the processing in the document preamble. Show substitutions of new environments. Show the contents of all recognised environments, both before and after processing. Show the cached/encoded information for the image keys, allowing two images to be tested for equality. </p>
 </dd>
<dt>6. </dt>
<dd> <p> Show replacements of new commands, accents and wrapped commands. </p>
 </dd>
<dt>7. </dt>
<dd> <p> Trace the processing of commands in math mode; both before and after. </p>
 </dd>
<dt>8. </dt>
<dd> <p> Trace the processing of all commands, both before and after. The command-line option sets an initial value only. During processing the value of <i>$VERBOSITY </i> can be set dynamically using the \htmltracing{...} command, whose argument is the desired value, or by using the more general \HTMLset command as follows: \HTMLset{VERBOSITY}{&lt;num&gt;}. </p>
 </dd></dl>
<h2>Other Configuration Variables, without switches</h2>
<p> The configuration variables described here do not warrant having a command-line switch to assign values. Either they represent aspects of <code>LaTeX2HTML </code> that are specific to the local site, or they govern properties that should apply to all documents, rather than something that typically would change for the different documents within a particular sub-directory. Normally these variables have their value set within the latex2html.config file. In the following listing the defaults are shown, as the lines of Perl code used to establish these values. If a different value is required, then these can be assigned from a local .latex2html-init initialisation file, without affecting the defaults for other users, or documents processed from other directories. </p>
<dl>
<dt><code>$dd</code></dt>
<dd> <p> holds the string to be used in file-names to delimit directories; it is set internally to `/&#8216;, unless the variable has already been given a value within latex2html.config . Note: This value cannot be set within a .latex2html-init initialisation file, since its value needs to be known in order to find such a file. </p>
 </dd>
<dt><code>$LATEX2HTMLDIR</code></dt>
<dd> <p> Read by the install-test script from latex2html.config, its value is inserted into the latex2html <code>Perl </code> script as part of the installation process. </p>
 </dd>
<dt><code>$LATEX2HTMLSTYLES = $LATEX2HTMLDIR/styles;</code></dt>
<dd> <p> Read from the latex2html.config file by install-test, its value is checked to locate the styles/ directory. </p>
 </dd>
<dt><code>$LATEX2HTMLVERSIONS = $LATEX2HTMLDIR/versions;</code></dt>
<dd> <p> The value of this variable should be set within latex2html.config to specify the directory path where the version and extension files can be found. </p>
 </dd>
<dt><code>$ALTERNATIVE_ICONS = &#8216;&#8216;;</code></dt>
<dd> <p> This may contain the (relative) directory path to a set of customised icons to be used in conjunction with the -local_icons switch. </p>
 </dd>
<dt><code>$TEXEXPAND = $LATEX2HTMLDIR/texexpand;</code></dt>
<dd> <p> Read by the install-test <code>Perl </code> script from latex2html.config, its value is used to locate the texexpand <code>Perl </code> script. </p>
 </dd>
<dt><code>$PSTOIMG = $LATEX2HTMLDIR/pstoimg;</code></dt>
<dd> <p> Read by the install-test <code>Perl </code> script from latex2html.config, its value is used to locate the pstoimg <code>Perl </code> script. </p>
 </dd>
<dt><code>$IMAGE_TYPE = &#8216;&lt;image-type&gt;&#8216;;</code></dt>
<dd> <p> Set in latex2html.config, the currently supported &lt;image-type&gt;s are: svg, png and gif. Vector formats such as svg look better at high resolution, while bitmap formats such as png or gif are generally faster to download and to render. </p>
 </dd>
<dt><code>$DVIPS = &#8216;dvips&#8217;;</code></dt>
<dd> <p> Read from latex2html.config by install-test, its value is checked to locate the dvips program or script. There could be several reasons to change the value here: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> add a switch -P&lt;printer&gt; to load a specific configuration-file; e.g. to use a specific set of PostScript fonts, for improved image-generation. </p>
<p> to prepend a path to a different version of dvips than normally available as the system default (e.g. the printing requirements are different). </p>
<p> to append debugging switches, in case of poor quality images; one can see which paths are being searched for fonts and other resources. </p>
<p> to prepend commands for setting path variables that dvips may need in order to locate fonts or other resources. </p>
 </dd></dl>
<p> If automatic generation of fonts is required, using Metafont, the following configuration variables are important. </p>
<dl>
<dt><code>$PK_GENERATION = 1;</code></dt>
<dd> <p> This variable must be set, to initiate font-generation; otherwise fonts will be scaled from existing resources on the local system. In particular this variable must not be set, if one wishes to use PostScript fonts or other scalable font resources (see the -scalable_fonts switch). </p>
 </dd>
<dt><code>$DVIPS_MODE = &#8216;toshiba&#8217;;</code></dt>
<dd> <p> The mode given here must be available in the modes.mf file, located with the Metafont resource files, perhaps in the misc/ subdirectory. </p>
 </dd>
<dt><code>$METAFONT_DPI = 180;</code></dt>
<dd> <p> The required resolution, in dots-per-inch, should be listed specifically within the MakeTeXPK script, called by dvips to invoke Metafont with the correct parameters for the required fonts. </p>
 </dd></dl>
</dl>
<dt><code>$LATEX = &#8216;latex&#8217;;</code></dt>
<dd> <p> Read from latex2html.config by install-test, its value is checked to locate the latex program or script. If <code>LaTeX </code> is having trouble finding style-files and/or packages, then the default command can be prepended with other commands to set environment variables intended to resolve these difficulties; e.g. <i>$LATEX = &#8216;setenv TEXINPUTS &lt;path to search&gt; ; latex&#8217; .</i> There are several variables to help control exactly which files are read by <code>LaTeX2HTML </code> and by <code>LaTeX </code> when processing images: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>$TEXINPUTS</code></dt>
<dd> <p> This is normally set from the environment variable of the same name. If difficulties occur so that styles and packages are not being found, then extra paths can be specified here, to resolve these difficulties. </p>
 </dd>
<dt><code>$DONT_INCLUDE</code></dt>
<dd> <p> This provides a list of filenames and extensions to not include, even if requested to do so by an \input or \include command. (Consult latex2html.config for the default list.) </p>
 </dd>
<dt><code>$DO_INCLUDE = &#8216;&#8216;;</code></dt>
<dd> <p> List of exceptions within the <i>$DONT_INCLUDE </i> list. These files are to be read if requested by an \input or \include command. </p>
 </dd></dl>
</dl>
<dt><code>$ICONSERVER = &#8216;&lt;URL&gt;&#8216;;</code></dt>
<dd> <p> This is used to specify a URL to find the standard icons, as used for the navigation buttons. Names for the specific images size, as well as size information, can be found in latex2html.config. The icons themselves can be replaced by customised versions, provided this information is correctly updated and the location of the customised images specified as the value of $ICONSERVER. When the -local_icons switch is used, so that a copy of the icons is placed with the <code>HTML </code> files and other generated images, the value of $ICONSERVER is not needed within the <code>HTML </code> files themselves. </p>
 </dd>
<dt><code>$NAV_BORDER = &lt;num&gt;;</code></dt>
<dd> <p> The value given here results in a border, measured in points, around each icon. A value of `0&#8217; is common, to maintain strict alignment of inactive and active buttons in the control panels. </p>
 </dd>
<dt><code>$LINKNAME = &#8216;index.$EXTN&#8217;;</code></dt>
<dd> <p> This is used when the <i>$NO_AUTO_LINK </i> variable is empty, to allow a URL to the working directory to be sufficient to reach the main page of the completed document. It specifies the name of the <code>HTML </code> file which will be automatically linked to the directory name. The value of <i>$EXTN </i> is .html unless <i>$SHORTEXTN </i> is set, in which case it is .htm . </p>
 </dd>
<dt><code>$LINKPOINT = &#8216;$FILE$EXTN&#8217;;</code></dt>
<dd> <p> This specifies the name of the <code>HTML </code> file to be duplicated, or symbolically linked, with the name specified in <i>$LINKNAME.</i> At the appropriate time the value of <i>$FILE </i> is the document name, which usually coincides with the name of the working directory. </p>
 </dd>
<dt><code>$CHARSET = &#8216;iso_8859_1&#8217;;</code></dt>
<dd> <p> This specifies the character set used within the <code>HTML </code> pages produced by <code>LaTeX2HTML.</code> If no value is set in a configuration or initialisation file, the default value will be assumed. The lowercase form <i>$charset </i> is also recognised, but this is overridden by the uppercase form. </p>
 </dd>
<dt><code>$ACCENT_IMAGES = &#8216;large&#8217;;</code></dt>
<dd> <p> Accented characters that are not part of the ISO-Latin fonts can be generated by making an image using <code>LaTeX. </code> This variable contains a (comma-separated) list of <code>LaTeX </code> commands for setting the style to be used when these images are made. If the value of this variable is empty then the accent is simply ignored, using an un-accented font character (not an image) instead. </p>
 </dd></dl>
<p> Within the color.perl package, the following two variables are used to identify the names of files containing specifications for named colors. Files having these names are provided, in the <i>$LATEX2HTMLSTYLES </i> directory, but they could be moved elsewhere, or replaced by alternative files having different names. In such a case the values of these variables should be altered accordingly. </p>
<p> <code>$RGBCOLORFILE = &#8216;rgb.txt&#8217;;</code> </p>
<p> <code>$CRAYOLAFILE = &#8216;crayola.txt&#8217;;</code> </p>
<p> The following variables may well be altered from the system defaults, but this is best done using a local .latex2html-init initialisation file, for overall consistency of style within documents located at the same site, or sites in close proximity. </p>
<dl>
<dt><code>$default_language = &#8216;english&#8217;;</code></dt>
<dd> <p> This establishes which language code is to be placed within the &lt;!DOCTYPE ... &gt; tag that may appear at the beginning of the <code>HTML </code> pages produced. Loading a package for an alternative language can be expected to change the value of this variable. See also the <i>$TITLES_LANGUAGE </i> variable, described next. </p>
 </dd>
<dt><code>$TITLES_LANGUAGE = &#8216;english&#8217;;</code></dt>
<dd> <p> This variable is used to specify the actual strings used for standard document sections, such as ``Contents&#8217;&#8216;, ``References&#8217;&#8216;, ``Table of Contents&#8217;&#8216;, etc. Support for French and German titles is available in corresponding packages. Loading such a package will normally alter the value of this variable, as well as the <i>$default_language </i> variable described above. </p>
 </dd>
<dt><code>$WORDS_IN_NAVIGATION_PANEL_TITLES = 4;</code></dt>
<dd> <p> Specifies how many words to use from section titles, within the textual hyperlinks which accompany the navigation buttons. </p>
 </dd>
<dt><code>$WORDS_IN_PAGE = 450;</code></dt>
<dd> <p> Specifies the minimum page length required before a navigation panel is placed at the bottom of a page, when the <i>$AUTO_NAVIGATION </i> variable is set. </p>
 </dd>
<dt><code>$CHILDLINE = &quot;&lt;BR&gt;&lt;HR&gt;\\n&quot;;</code></dt>
<dd> <p> This gives the <code>HTML </code> code to be placed between the child-links table and the ordinary contents of the page on which it occurs. </p>
 </dd>
<dt><code>$NETSCAPE_HTML = 0;</code></dt>
<dd> <p> When set, this variable specifies that <code>HTML </code> code may be present which does not conform to any official standard. This restricts the contents of any &lt;!DOCTYPE ... &gt; tag which may be placed at the beginning of the HTML pages produced. </p>
 </dd>
<dt><code>$BODYTEXT = &#8216;&#8216;;</code></dt>
<dd> <p> The value of this variable is used within the &lt;BODY ... &gt; tag; e.g. to set text and/or background colors. It&#8217;s value is overridden by the \bodytext command, and can be added-to or parts changed using the \htmlbody command or \color and \pagecolor from the color package. </p>
 </dd>
<dt><code>$INTERLACE = 1;</code></dt>
<dd> <p> When set, interlaced images should be produced. This requires graphics utilities to be available to perform the interlacing operation. </p>
 </dd>
<dt><code>$TRANSPARENT_FIGURES = 1;</code></dt>
<dd> <p> When set, the background of images should be made transparent; otherwise it is white. This requires graphics utilities to be available which can specify the color to be made transparent. </p>
 </dd>
<dt><code>$FIGURE_SCALE_FACTOR = 1.6;</code></dt>
<dd> <p> Scale factor applied to all images of figure and other environments, when being made into an image. Note that this does not apply to recognised mathematics environments, which instead use the contents of <i>$MATH_SCALE_FACTOR </i> and $DISP_SCALE_FACTOR to specify scaling. </p>
 </dd>
<dt><code>$MATH_SCALE_FACTOR = 1.6;</code></dt>
<dd> <p> Scale factor applied to all images of mathematics, both inline and displayed. A value of 1.4 is a good alternative, with anti-aliased images. </p>
 </dd>
<dt><code>$DISP_SCALE_FACTOR = 1;</code></dt>
<dd> <p> Extra scale factor applied to images of displayed math environments. When set, this value multiplies <i>$MATH_SCALE_FACTOR </i> to give the total scaling. A value of `1.2&#8217; is a good choice to accompany $MATH_SCALE_FACTOR = 1.4;. </p>
 </dd>
<dt><code>$EXTRA_IMAGE_SCALE</code></dt>
<dd> <p> This may hold an extra scale factor that can be applied to all generated images. When set, it specifies that a scaling of <i>$EXTRA_IMAGE_SCALE </i> be applied when images are created, but to have their height and width recorded as the un-scaled size. This is to coax browsers into scaling the (usually larger) images to fit the desired size; when printed a better quality can be obtained. Values of `1.5&#8217; and `2&#8217; give good print quality at 600dpi. </p>
 </dd>
<dt><code>$PAPERSIZE = &#8216;a5&#8217;;</code></dt>
<dd> <p> Specifies the size of a page for typesetting figures or displayed math, when an image is to be generated. This affects the lengths of lines of text within images. Since images of text or mathematics should use larger sizes than when printed, else clarity is lost at screen resolutions, then a smaller paper-size is generally advisable. This is especially so if both the $MATH_SCALE_FACTOR and <i>$DISP_SCALE_FACTOR </i> scaling factors are being used, else some images may become excessively large, including a lot of blank space. </p>
 </dd>
<dt><code>$LINE_WIDTH = 500;</code></dt>
<dd> <p> Formerly specified the width of an image, when the contents were to be right- or center-justified. (No longer used.) </p>
 </dd></dl>
<p> The following variables are used to access the utilities required during image-generation. File and program locations on the local system are established by the configure-pstoimg <code>Perl </code> script and stored within <i>$LATEX2HTMLDIR/local.pm </i> as <code>Perl </code> code, to be read by pstoimg when required. After running the configure-pstoimg Perl script it should not be necessary to alter the values obtained. Those shown below are what happens on the author&#8217;s system; they are for illustration only and do not represent default values. </p>
<p> <br />
&nbsp;$GS_LIB&nbsp;=&nbsp;&#8216;/usr/local/share/ghostscript/4.02&#8217;; <br />
&nbsp;$PNMCAT&nbsp;=&nbsp;&#8216;/usr/local/bin/pnmcat&#8217;; <br />
&nbsp;$PPMQUANT&nbsp;=&nbsp;&#8216;/usr/local/bin/ppmquant&#8217;; <br />
&nbsp;$PNMFLIP&nbsp;=&nbsp;&#8216;/usr/local/bin/pnmflip&#8217;; <br />
&nbsp;$PPMTOGIF&nbsp;=&nbsp;&#8216;/usr/local/bin/ppmtogif&#8217;; <br />
&nbsp;$HOWTO_TRANSPARENT_GIF&nbsp;=&nbsp;&#8216;netpbm&#8217;; <br />
&nbsp;$GS_DEVICE&nbsp;=&nbsp;&#8216;pnmraw&#8217;; <br />
&nbsp;$GS&nbsp;=&nbsp;&#8216;/usr/local/bin/gs&#8217;; <br />
&nbsp;$PNMFILE&nbsp;=&nbsp;&#8216;/usr/local/bin/pnmfile&#8217;; <br />
&nbsp;$HOWTO_INTERLACE_GIF&nbsp;=&nbsp;&#8216;netpbm&#8217;; <br />
&nbsp;$PBMMAKE&nbsp;=&nbsp;&#8216;/usr/local/bin/pbmmake&#8217;; <br />
&nbsp;$PNMCROP&nbsp;=&nbsp;&#8216;/usr/local/bin/pnmcrop&#8217;; <br />
&nbsp;$TMP&nbsp;=&nbsp;&#8216;/usr/var/tmp&#8217;; The following variables are no longer needed, having been replaced by the more specific information obtained using the Perl script configure-pstoimg. <br />
&nbsp;$USENETPBM&nbsp;=&nbsp;1; <br />
&nbsp;$PBMPLUSDIR&nbsp;=&nbsp;&#8216;/usr/local/bin&#8217;;  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-latex/">latex</a></code>(1)  </p>
<h2>AUTHOR</h2>
<p> Nikos Drakos, Computer Based Learning Unit, University of Leeds &lt;nikos [at] cbl.leeds.ac.uk&gt;. Several people have contributed suggestions, ideas, solutions, support and encouragement. The current maintainer is Ross Moore. This manual page was written by Manoj Srivastava &lt;srivasta [at] debian.org&gt;, for the Debian GNU/Linux system, based on the LaTeX documentation accompanying the program. </p>
