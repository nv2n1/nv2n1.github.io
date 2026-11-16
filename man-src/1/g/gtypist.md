---
title: "gtypist(1)"
name: "gtypist"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gtypist/"
description: "gtypist – manual page for gtypist 2.8.1"
---

<h2>NAME</h2>
<p> gtypist &#8211; manual page for gtypist 2.8.1</p>
<h2>SYNOPSIS</h2>
<p> <code>gtypist</code> [ <i>Options</i>&#8230; ] [ <i>script-file </i>]</p>
<h2>DESCRIPTION</h2>
<p> `gtypist&#8217; is a typing tutor with several lessons for different keyboards and languages. New lessons can be written by the user easily.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code> % <code>&#8211;max-error=</code>%</dt>
<dd> default maximum error percentage (default 3.0); valid values are between 0.0 and 100.0</dd>
<dt><code>-n</code> <code>&#8211;notimer</code></dt>
<dd> turn off WPM timer in drills</dd>
<dt><code>-t</code> <code>&#8211;term-cursor</code></dt>
<dd> use the terminal&#8217;s hardware cursor</dd>
<dt><code>-f</code> P <code>&#8211;curs-flash</code>=<i>P</i></dt>
<dd> cursor flash period P*.1 sec (default 10); valid values are between 0 and 512; this is ignored if <code>-t</code> is specified</dd>
<dt><code>-c</code> F,B <code>&#8211;colours</code>=<i>F</i>,B</dt>
<dd> set initial display colours where available</dd>
<dt><code>-s</code> <code>&#8211;silent</code></dt>
<dd> don&#8217;t beep on errors</dd>
<dt><code>-q</code> <code>&#8211;quiet</code></dt>
<dd> same as <code>-s</code>, <code>&#8211;silent</code></dd>
<dt><code>-l</code> L <code>&#8211;start-label</code>=<i>L</i></dt>
<dd> start the lesson at label &#8216;L&#8217;</dd>
<dt> <code>-w</code> <code>&#8211;word-processor</code> try to mimic word processors</dt>
<dt><code>-k</code> <code>&#8211;no-skip</code></dt>
<dd>
</dd><dd>forbid the user to skip exercises</dd>
<dt><code>-i</code> <code>&#8211;show-errors</code></dt>
<dd> highlight errors with reverse video</dd>
<dt><code>-h</code> <code>&#8211;help</code></dt>
<dd> print this message</dd>
<dt><code>-v</code> <code>&#8211;version</code></dt>
<dd> output version information and exit</dd>
<dt><code>-S</code> <code>&#8211;always-sure</code></dt>
<dd> do not ask confirmation questions</dd>
<dt><code>&#8211;banner-colors</code>=<i>F</i>,B,P,V set top banner colours (background, foreground,</dt>
<dd> package and version respectively)</dd>
<dt><code>&#8211;scoring</code>=<i>wpm</i>,cpm</dt>
<dd> set scoring mode (words per minute or characters per minute)</dd></dl>
<p> If not supplied, script-file defaults to &#8216;/usr/local/share/gtypist/gtypist.typ&#8217;. The path $GTYPIST_PATH is searched for script files.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd> To run the default lesson in english `gtypist.typ&#8217;:</dd>
<dt>
</dt><dd> gtypist</dd>
<dt>
</dt><dd> To run the lesson in spanish:</dd>
<dt>
</dt><dd> gtypist esp.typ</dd>
<dt>
</dt><dd> To instruct gtypist to look for lesson `bar.typ&#8217; in a non standard directory:</dd>
<dt>
</dt><dd> GTYPIST_PATH=&quot;/home/foo&quot; gtypist bar.typ</dd>
<dt>
</dt><dd> To run the lesson in the file `test.typ&#8217; of directory `temp&#8217;, starting at label `TEST1&#8242;, using the terminal&#8217;s cursor, and run silently:</dd>
<dt>
</dt><dd> gtypist <code>-t</code> <code>-q</code> <code>-l</code> TEST1 /temp/test.typ</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Simon Baldwin</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to bug-gtypist [at] gnu.org</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1998, 1999, 2000, 2001, 2002, 2003 Simon Baldwin.<br />
 Copyright &#169; 2003, 2004, 2008 GNU Typist Development Team. This program comes with ABSOLUTELY NO WARRANTY; for details please see the file &#8216;COPYING&#8217; supplied with the source code.<br />
 This is free software, and you are welcome to redistribute it under certain conditions; again, see &#8216;COPYING&#8217; for details. This program is released under the GNU General Public License.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gtypist</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>gtypist</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info gtypist</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
