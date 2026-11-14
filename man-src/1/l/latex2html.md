---
title: "latex2html(1)"
name: "latex2html"
section: "1"
letter: "l"
url: "/docs/linux/man/1-latex2html/"
description: "latex2html – translate LaTeX files to HTML (HyperText Markup Language)"
---

<h2 class="name">NAME</h2>
<p> latex2html &#8211; translate LaTeX files to HTML (HyperText Markup Language) </p>
<h2>SYNOPSIS</h2>
<p> <code>latex2html</code> <i>[options]</i> [target [target &#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> This manual page explains the <code>LaTeX2HTML</code> utility, which is a <code>Perl </code> program that translates <code>LaTeX</code> document into <code>HTML </code> format. For each source file given as an argument the translator will create a directory containing the corresponding HTML files. For details and examples, please consult the online html documentation, a copy of which should be available in <i>/usr/share/doc/latex2html/manual.ps.gz</i> or <i>/usr/share/doc/latex2html/html/</i></p>
<h2>CAVEAT</h2>
<p> This documentation has been derived from the TeX manual, and may not be up to date. Please refer to the online manual for authoritative documentation.</p>
<h2>Options controlling Titles, File-Names and Sectioning</h2>
<dl>
<dt><code>-t &lt;top-page-title&gt;</code></p>
<dd> Same as setting: <i>$TITLE = &lt;top-page-title&gt;;</i> Name the document using this title.</p>
<dt><code>-short_extn</code></p>
<dd> Same as setting: <i>$SHORTEXTN = 1;</i> Use a filename prefix of .htm for the produced <code>HTML </code> files. This is particularly useful for creating pages to be stored on CD-ROM or other media, to be used with operating systems that require a 3-character extension.</p>
<dt><code>-long_titles &lt;num&gt;</code></p>
<dd> Same as setting: <i>$LONG_TITLES = &lt;num&gt;;</i> Instead of the standard names: node1.html, node2.html,&#8230; the filenames for each <code>HTML </code> page are constructed from the first &lt;num&gt; words of the section heading for that page, separated by the `_&#8217; character. Commas and common short words (a an to by of and for the) are omitted from both title and word-count. Warning: Use this switch with great caution. Currently there are no checks for uniqueness of names or overall length. Very long names can easily result from using this feature.</p>
<dt><code>-custom_titles</code></p>
<dd> Same as setting: <i>$CUSTOM_TITLES = 1;</i> Instead of the standard names: node1.html, node2.html, &#8230; the filenames for each <code>HTML </code> page are constructed using a <code>Perl </code> subroutine named custom_title_hook . The user may define his/her own version of this subroutine, within a .latex2html-init file say, to override the default (which uses the standard names). This subroutine takes the section-heading as a parameter and must return the required name, or the empty string (default).</p>
<dt><code>-dir &lt;output-directory&gt;</code></p>
<dd> Same as setting: <i>$DESTDIR = &lt;output-directory&gt;;</i> Redirect the output to the specified directory. The default behaviour is to create (or reuse) a directory having the same name as the prefix of the document being processed.</p>
<dt><code>-no_subdir</code></p>
<dd> Same as setting: <i>$NO_SUBDIR = 1;</i> Place the generated <code>HTML </code> files into the current directory. This overrides any <i>$DESTDIR </i> setting.</p>
<dt><code>-prefix &lt;filename-prefix&gt;</code></p>
<dd> Same as setting: <i>$PREFIX = &lt;filename-prefix&gt;;</i> The &lt;filename-prefix&gt; will be prepended to all .gif, .pl and .html files produced, except for the top-level .html file; it may include a (relative) directory path. This will enable multiple products of <code>LaTeX2HTML </code> to peacefully coexist in the same directory. However, do not attempt to simultaneously run multiple instances of <code>LaTeX2HTML </code> using the same output directory, else various temporary files will overwrite each other.</p>
<dt><code>-auto_prefix</code></p>
<dd> Same as setting: <i>$AUTO_PREFIX = 1;</i> Constructs the prefix as `&lt;title&gt;-&#8216; to be prepended to all the files produced, where &lt;title&gt; is the name of the <code>LaTeX </code> file being processed. (Note the `-&#8216; in this prefix.) This overrides any <i>$PREFIX </i> setting.</p>
<dt><code>-no_auto_link</code></p>
<dd> Same as setting: <i>$NO_AUTO_LINK = 1;</i> If $NO_AUTO_LINK is empty and variables <i>$LINKPOINT </i> and <i>$LINKNAME </i> are defined appropriately (as is the default in the latex2html.config file), then a hard link to the main <code>HTML </code> page is produced, using the name supplied in <i>$LINKNAME. </i> Typically this is index.html; on many systems a file of this name will be used, if it exists, when a browser tries to view a URL which points to a directory. On other systems a different value for <i>$LINKNAME </i> may be appropriate. Typically <i>$LINKPOINT</i> has value <i>$FILE.html, </i> but this may also be changed to match whichever HTML page is to become the target of the automatic link. Use of the -no_auto_link switch cancels this automatic linking facility, when not required for a particular document.</p>
<dt><code>-split &lt;num&gt;</code></p>
<dd> Same as setting: <i>$MAX_SPLIT_DEPTH = &lt;num&gt;; (default is 8)</i> Stop splitting sections into separate files at this depth. Specifying -split 0 will put the entire document into a single <code>HTML </code> file. See below for the different levels of sectioning. Also see the next item for how to set a &#8220;relative&#8221; depth for splitting.</p>
<dt><code>-split +&lt;num&gt;</code></p>
<dd> Same as setting: <i>$MAX_SPLIT_DEPTH = -&lt;num&gt;; (default is 8)</i> The level at which to stop splitting sections is calculated &#8220;relative to&#8221; the shallowest level of sectioning that occurs within the document. For example, if the document contains \section commands, but no \part or 
