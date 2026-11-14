---
title: "musicxml2ly(1)"
name: "musicxml2ly"
section: "1"
letter: "m"
url: "/docs/linux/man/1-musicxml2ly/"
description: "musicxml2ly – manual page for musicxml2ly (LilyPond) 2.12.2"
---

<h2>NAME</h2>
<p> musicxml2ly &#8211; manual page for musicxml2ly (LilyPond) 2.12.2</p>
<h2>SYNOPSIS</h2>
<p> <code>musicxml2ly</code> [<i>OPTION</i>]&#8230; <i>FILE.xml</i></p>
<h2>DESCRIPTION</h2>
<p> Convert MusicXML from FILE.xml to LilyPond input. If the given filename is -, musicxml2ly reads from the command line.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> show version number and exit</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> be verbose</p>
<dt><code>&#8211;lxml</code></p>
<dd> use lxml.etree; uses less memory and cpu time</p>
<dt><code>-z</code>, <code>&#8211;compressed</code></p>
<dd> input file is a zip-compressed MusicXML file</p>
<dt><code>-r</code>, <code>&#8211;relative</code></p>
<dd> convert pitches in relative mode (default)</p>
<dt><code>-a</code>, <code>&#8211;absolute</code></p>
<dd> convert pitches in absolute mode</p>
<dt><code>-l</code>, <code>&#8211;language</code>=<i>LANG</i></p>
<dd> use a different language file &#8216;LANG.ly&#8217; and corresponding pitch names, e.g. &#8216;deutsch&#8217; for deutsch.ly</p>
<dt><code>&#8211;nd</code> <code>&#8211;no-articulation-directions</code></p>
<dd> do not convert directions (^, _ or -) for articulations, dynamics, etc.</p>
<dt><code>&#8211;nrp</code> <code>&#8211;no-rest-positions</code></p>
<dd> do not convert exact vertical positions of rests</p>
<dt><code>&#8211;no-beaming</code></p>
<dd> do not convert beaming information, use lilypond&#8217;s automatic beaming instead</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> set output filename to FILE, stdout if &#8211;</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs via <a rel="nofollow" href="http://post.gmane.org/post.php?group=gmane.comp.gnu.lilypond.bugs">http://post.gmane.org/post.php?group=gmane.comp.gnu.lilypond.bugs</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005&#8211;2009 by<br />
&nbsp;<wbr>Han-Wen Nienhuys&nbsp;<wbr>&lt;hanwen [at] xs4all.nl&gt;,<br />
&nbsp;<wbr>Jan Nieuwenhuizen&nbsp;<wbr>&lt;janneke [at] gnu.org&gt;&nbsp;<wbr>and<br />
&nbsp;<wbr>Reinhold Kainhofer&nbsp;<wbr>&lt;reinhold [at] kainhofer.com&gt; </p>
<p> This program is free software. It is covered by the GNU General Public License and you are welcome to change it and/or distribute copies of it under certain conditions. Invoke as `lilypond <code>&#8211;warranty</code>&#8216; for more information.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>musicxml2ly</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>musicxml2ly</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info musicxml2ly</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
