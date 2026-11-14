---
title: "dia(1)"
name: "dia"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dia/"
description: "dia – a diagram drawing program"
---

<h2 class="name">NAME</h2>
<p> dia &#8211; a diagram drawing program </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dia</code> [<code>-c</code>] [<code>&#8211;credits</code>] [<code>-e&nbsp;<wbr></code><i>OUTPUT</i>] [<code>&#8211;export=</code><i>OUTPUT</i>] [<code>-L&nbsp;<wbr></code><i>LAYER,LAYER,&#8230;</i>] [<code>&#8211;show-layers=</code><i>LAYER,LAYER,&#8230;</i>] [<code>-h</code>] [<code>&#8211;help</code>] [<code>-n</code>] [<code>&#8211;nosplash</code>] [<code>-s&nbsp;<wbr></code><i>WxH</i>] [<code>&#8211;size=</code><i>WxH</i>] [<code>-t&nbsp;<wbr></code><i>FORMAT</i>] [<code>&#8211;filter=</code><i>FORMAT</i>] [<code>-v</code>] [<code>&#8211;version</code>] [file &#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>Dia</code></p>
<dd>is used to create diagrams. Dia has a number of basic tools, like lines and boxes but can also dynamically load <i>sheets</i>. A sheet is a collection of tools that are used in a certain type of diagram. </p>
<p> Most diagram objects in <code>Dia</code> have <i>connection points</i>. Lines can be connected to these connection points and this way graph structures can be formed. When objects are moved or resized the connections will follow the objects. </p>
<p> Diagrams drawn in <code>Dia</code> can be exported as PostScript.</p>
<h2>OPTIONS</h2>
<p> <code>Dia</code> accepts the following options: </p>
<p> <code>-c</code> <code>&#8211;credits</code></p>
<dl>
<dt>
<dd> Display credits list and exit.</dl>
<p> <code>-e </code><i>OUTPUT</i> <code>&#8211;export=</code><i>OUTPUT</i></p>
<dl>
<dt>
<dd> Export loaded file to OUTPUT and exit.</dl>
<p> <code>-h</code> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a list of all commandline options.</dl>
<p> <code>-n</code> <code>&#8211;nosplash</code></p>
<dl>
<dt>
<dd> Do not show the splash screen.</dl>
<p> <code>-s </code><i>WxH</i> <code>&#8211;size=</code><i>WxH</i></p>
<dl>
<dt>
<dd> Export loaded file in decimal given width and/or height. It is allowed to only select width or height. E.g. <code>&#8211;size=</code><i>520x</i> exports an image that is 520 pixels wide, while <code>&#8211;size=</code><i>x900</i> exports an image of 900 pixels height. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 This option is currently only implemented for the PNG export filter. </p>
</dl>
</dl>
<p> <code>-L </code><i>LAYER,LAYER,&#8230;</i> <code>&#8211;show-layers=</code><i>LAYER,LAYER,&#8230;</i></p>
<dl>
<dt>
<dd> Only include specified layers when exporting. Layers can be specified either as a layer name, the layer number or a numeric range X-Y of layers. &#8211;show-layers=background,2-5 shows the layer named background and layers 2-5, &#8211;show-layers=2- shows layers 2 and up.</dl>
<p> <code>-t </code><i>FORMAT</i> <code>&#8211;export-to-format=</code><i>FORMAT</i></p>
<dl>
<dt>
<dd> Export loaded file in FORMAT and exit. Format are described below.</dl>
<p> <code>-v</code> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display <code>dia</code> version and exit.</dl>
<h2>EXPORT FORMATS</h2>
<p> The following export formats are supported by <code>dia</code>. </p>
<dl>
<dt>
<dd> &bull; cgm (Computer Graphics Metafile, ISO 8632)</dl>
<dl>
<dt>
<dd> &bull; dia (Native dia diagram)</dl>
<dl>
<dt>
<dd> &bull; dxf (Drawing Interchange File)</dl>
<dl>
<dt>
<dd> &bull; eps or eps-builtin or eps-pango (Encapsulated PostScript) </p>
<p> The format specifications eps and eps-pango both use the font renderer of the Pango library, while eps-builtin uses a dia specific font renderer. If you have problems with Pango rendering, e.g. Unicode, try eps-builtin instead.</dl>
<dl>
<dt>
<dd> &bull; fig (XFig format)</dl>
<dl>
<dt>
<dd> &bull; mp (TeX MetaPost macros)</dl>
<dl>
<dt>
<dd> &bull; plt or hpgl (HP Graphics Language)</dl>
<dl>
<dt>
<dd> &bull; png (Portable Network Graphics)</dl>
<dl>
<dt>
<dd> &bull; shape (Dia Shape File)</dl>
<dl>
<dt>
<dd> &bull; svg (Scalable Vector Graphics)</dl>
<dl>
<dt>
<dd> &bull; tex (TeX PSTricks macros)</dl>
<dl>
<dt>
<dd> &bull; wpg (WordPerfect Graphics)</dl>
<dl>
<dt>
<dd> &bull; wmf (Windows MetaFile)</dl>
<h2>FILES</h2>
<p> <code>dia</code> creates a directory .dia in the user&#8217;s home, which contains different files to store user preferences. To reset <code>dia</code> to it&#8217;s default behaviour, just remove the respective file: </p>
<dl>
<dt>
<dd> &bull; defaults.dia: contains default values for elements (XML format).</dl>
<dl>
<dt>
<dd> &bull; diarc: keeps <code>dia</code> preferences (ASCII).</dl>
<dl>
<dt>
<dd> &bull; history: keeps the list of last edited diagrams (ASCII).</dl>
<dl>
<dt>
<dd> &bull; menurc: contains an automated accelerator map dump (Lisp).</dl>
<dl>
<dt>
<dd> &bull; persistence: contains GUI information, e.g. open windows (XML).</dl>
<dl>
<dt>
<dd> &bull; pluginrc: the list of loaded plugins (XML).</dl>
<h2>SEE ALSO</h2>
<p> m[blue]<code>Pango</code>m[]<font SIZE="-2">[1]</font> </p>
<p> X (1) </p>
<p> xfig (1) </p>
<p> inkscape (1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1999 Alexander Larsson. </p>
<p> Permission to use, copy, modify, and distribute this software and its documentation for any purpose and without fee is hereby granted, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation.</p>
<h2>AUTHORS</h2>
<p> Alexander Larsson </p>
<p> This manual was written by Fredrik Hallenberg.</p>
<h2>AUTHORS</h2>
<p> <code>Fredrik Hallenberg</code> &lt;hallon [at] lysator.liu.se&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>W. Borgert</code> &lt;debacle [at] debian.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<p> <code>Alan Horkan</code> &lt;horkana [at] tcd.ie&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1999, 2004 Fredrik Hallenberg, W. Borgert, Alan Horkan </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Pango</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.pango.org/">http://www.pango.org/</a></dl>
</dl>
<h2>Index</h2>
