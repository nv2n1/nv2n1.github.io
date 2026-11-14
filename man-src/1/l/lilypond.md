---
title: "lilypond(1)"
name: "lilypond"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lilypond/"
description: "LilyPond – manual page for LilyPond 2.12.2"
---

<h2>NAME</h2>
<p> LilyPond &#8211; manual page for LilyPond 2.12.2</p>
<h2>SYNOPSIS</h2>
<p> <code>lilypond</code> [<i>OPTION</i>]&#8230; <i>FILE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Typeset music and/or produce MIDI from FILE. </p>
<p> LilyPond produces beautiful music notation. For more information, see <a rel="nofollow" href="http://lilypond.org">http://lilypond.org</a></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;define-default=SYM</code>[=<i>VAL</i>]</p>
<dd> set Scheme option SYM to VAL (default: #t). Use <code>-dhelp</code> for help.</p>
<dt><code>-e</code>, <code>&#8211;evaluate</code>=<i>EXPR</i></p>
<dd> evaluate scheme code</p>
<dt><code>-f</code>, <code>&#8211;formats</code>=<i>FORMATs</i></p>
<dd> dump FORMAT,&#8230; Also as separate options:</p>
<dt><code>&#8211;pdf</code></p>
<dd> generate PDF (default)</p>
<dt><code>&#8211;png</code></p>
<dd> generate PNG</p>
<dt><code>&#8211;ps</code></p>
<dd> generate PostScript</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help and exit</p>
<dt><code>-H</code>, <code>&#8211;header</code>=<i>FIELD</i></p>
<dd> dump header field FIELD to file named BASENAME.FIELD</p>
<dt><code>-I</code>, <code>&#8211;include</code>=<i>DIR</i></p>
<dd> add DIR to search path</p>
<dt><code>-i</code>, <code>&#8211;init</code>=<i>FILE</i></p>
<dd> use FILE as init file</p>
<dt><code>-j</code>, <code>&#8211;jail</code>=<i>USER</i>, GROUP, JAIL, DIR</p>
<dd> chroot to JAIL, become USER:GROUP and cd into DIR</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> write output to FILE (suffix will be added)</p>
<dt><code>&#8211;relocate</code></p>
<dd> relocate using directory of lilypond program</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> show version number and exit</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> be verbose</p>
<dt><code>-w</code>, <code>&#8211;warranty</code></p>
<dd> show warranty and copyright</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs via <a rel="nofollow" href="http://post.gmane.org/post.php?group=gmane.comp.gnu.lilypond.bugs">http://post.gmane.org/post.php?group=gmane.comp.gnu.lilypond.bugs</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1996&#8211;2009 by<br />
&nbsp;<wbr>&nbsp;<wbr>Han-Wen Nienhuys&nbsp;<wbr>&lt;hanwen [at] xs4all.nl&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>Jan Nieuwenhuizen&nbsp;<wbr>&lt;janneke [at] gnu.org&gt;<br />
&nbsp;<wbr>&nbsp;<wbr>and others. </p>
<p> This program is free software. It is covered by the GNU General Public License and you are welcome to change it and/or distribute copies of it under certain conditions. Invoke as `lilypond <code>&#8211;warranty</code>&#8216; for more information.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>LilyPond</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>LilyPond</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info LilyPond</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
