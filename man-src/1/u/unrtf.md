---
title: "unrtf(1)"
name: "unrtf"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unrtf/"
description: "UnRTF – converts document in RTF format to other formats"
---

<h2>NAME</h2>
<p> UnRTF &#8211; converts document in RTF format to other formats</p>
<h2>SYNOPSIS</h2>
<p> <code>unrtf [</code><i>options</i><code>] [</code><i>file&#8230;</i><code>]</code> </p>
<p> Options: <code>[&#8211;nopict]</code> <code>[&#8211;noremap]</code> <code>[-P config_search_path]</code> <code>[&#8211;html]</code> <code>[&#8211;text]</code> <code>[&#8211;vt]</code> <code>[&#8211;rtf]</code> <code>[&#8211;latex]</code> <code>[&#8211;help]</code> <code>[&#8211;verbose]</code> <code>[&#8211;quiet]</code> <code>[&#8211;version]</code> <code>[-t tags_file]</code> </p>
<h2>DESCRIPTION</h2>
<p> The program <code>unrtf</code> is a converter from Rich Text Format (RTF) to a growing number of document formats. At present it supports Hypertext Markup Language (HTML), plain text, text with VT100 codes, LaTeX, and RTF itself. It is possible to produce troff files with macro calls; an example configuration for troff and the mm macro package is provided. All output formats except HTML are &quot;alpha&quot; i.e. limited and development has just begun. However with HTML, the program supports tables, fonts, hyperlinks, and paragraph alignment. Font support includes face and size changes, as well as typical attributes such as italic, bold, underlining, strikethrough, smallcaps, allcaps, expand, compress and both foreground and background colors. Images are always stored to separate files in the current directory, or they can be ignored. </p>
<p> Starting with version 0.21.0, all control of unrtf output is through runtime configuration files. This makes it easy for users to fine-tune the output, and/or define new output formats. The configuration files can be read from the distributed ones, or from user files, searched for in the <i>config_search_path .</i> Note that the order of the -P and output arguments is important. The search path must be set before any argument that will load a configuration file if that file is not in the standard place. </p>
<p> Code page conversion is performed with the <a href="/docs/linux/man/3-iconv/">iconv</a>(3) package.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;nopict</p>
<dd> disables the automatic storing of embedded pictures to the current directory.</p>
<dt>&#8211;noremap</p>
<dd> disables charset conversion (currently only works for 8-bit charsets).</p>
<dt>&#8211;html</p>
<dd> selects HTML output (default).</p>
<dt>&#8211;rtf</p>
<dd> selects RTF output. The resulting output will often be much smaller than the input.</p>
<dt>&#8211;text</p>
<dd> selects plain ASCII text output.</p>
<dt>&#8211;vt</p>
<dd> selects text output with VT100 escape codes.</p>
<dt>&#8211;latex</p>
<dd> selects output of a LaTeX document.</p>
<dt>&#8211;verbose</p>
<dd> prints additional information.</p>
<dt>&#8211;quiet</p>
<dd> suppress output of leading comments</p>
<dt>&#8211;version</p>
<dd> prints the program version.</p>
<dt>-t tags_file</p>
<dd> specifies the tags output configuration file to be used. The command &quot;unrtf -t html&quot; is functionally identical to &quot;unrtf &#8211;html&quot;. The configuration files are a simple format. To change the behaviour of unrtf, a local copy of a system configuration file can be be made and edited. The most complete configuration file and hence the best starting point is /usr/share/unrtf/html.conf.</p>
<dt>-P config_search_path</p>
<dd> specifies the directories in which the configuration file for the specified format will be sought. The path can be provided as a single directory or a list of colon separated directories. The default is /usr/share/unrtf where distributed output configuration files are installed.</dl>
<h2>FILES</h2>
<dl>
<dt>/usr/share/unrtf/*.conf</p>
<dd> &#8211; run time output configuration files.</p>
<dt>/usr/share/unrtf/SYMBOL.charmap</p>
<dd> &#8211; UTF encoding of the SYMBOL font used in many RTF files. Unfortunately the iconv package does not include font encodings. The format is identical to iconv code page files.</dl>
<h2>WEBSITE</h2>
<h2>NOTES</h2>
<p> Report bugs in the program to <a rel="nofollow" href="http://savannah.gnu.org/projects/unrtf/">http://savannah.gnu.org/projects/unrtf/</a> </p>
<h2>Index</h2>
