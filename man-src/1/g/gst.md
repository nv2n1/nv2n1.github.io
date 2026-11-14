---
title: "gst(1)"
name: "gst"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst/"
description: "Smalltalk – the GNU Smalltalk virtual machine"
---

<h2>NAME</h2>
<p> Smalltalk &#8211; the GNU Smalltalk virtual machine</p>
<h2>DESCRIPTION</h2>
<p> GNU Smalltalk usage:</p>
<dl>
<dt>
<dd> gst [ flag &#8230; ] [ file &#8230; ] gst [ flag &#8230; ] { <code>-f</code> | <code>&#8211;file</code> } file [ args &#8230; ]</dl>
<p> Short flags can appear either as <code>-xyz</code> or as <code>-x</code> <code>-y</code> <code>-z</code>. If an option is mandatory for a long option, it is also mandatory for a short one. The currently defined set of flags is:</p>
<dl>
<dt><code>-a</code> <code>&#8211;smalltalk-args</code></p>
<dd> Pass the remaining arguments to Smalltalk.</p>
<dt><code>-c</code> <code>&#8211;core-dump</code></p>
<dd> Dump core on fatal signal.</p>
<dt><code>-D</code> <code>&#8211;declaration-trace</code></p>
<dd> Trace compilation of all loaded files.</p>
<dt><code>-E</code> <code>&#8211;execution-trace</code></p>
<dd> Trace execution of all loaded files.</p>
<dt><code>-g</code> <code>&#8211;no-gc-message</code></p>
<dd> Do not print garbage collection messages.</p>
<dt><code>-H</code> <code>&#8211;help</code></p>
<dd> Print this message and exit.</p>
<dt><code>-i</code> <code>&#8211;rebuild-image</code></p>
<dd> Ignore the image file; rebuild it from scratch.</p>
<dt><code>&#8211;maybe-rebuild-image</code></p>
<dd> Rebuild the image file from scratch if any kernel file is newer.</p>
<dt><code>-I</code> <code>&#8211;image</code> FILE</p>
<dd> Instead of `gst.im&#8217;, use FILE as the image file, and ignore the kernel files&#8217; timestamps.</p>
<dt><code>-K</code> <code>&#8211;kernel-file</code> FILE</p>
<dd> Make FILE&#8217;s path relative to the image path.</p>
<dt><code>-q</code> <code>&#8211;quiet</code> <code>&#8211;silent</code></p>
<dd> Do not print execution information.</p>
<dt><code>-r</code> <code>&#8211;regression-test</code></p>
<dd> Run in regression test mode, i.e. make printed messages constant.</p>
<dt><code>-S</code> <code>&#8211;snapshot</code></p>
<dd> Save a snapshot just before exiting.</p>
<dt><code>-v</code> <code>&#8211;version</code></p>
<dd> Print the Smalltalk version number and exit.</p>
<dt><code>-V</code> <code>&#8211;verbose</code></p>
<dd> Show names of loaded files and execution stats.</p>
<dt><code>&#8211;emacs-mode</code></p>
<dd> Execute as a `process&#8217; (from within Emacs)</p>
<dt><code>&#8211;kernel-directory</code> DIR</p>
<dd> Look for kernel files in directory DIR.</p>
<dt><code>&#8211;no-user-files</code></p>
<dd> Don&#8217;t read user customization files.</p>
<dt>&#8211;</p>
<dd> Read input from standard input explicitly.</dl>
<p> Files are loaded one after the other. After the last one is loaded, Smalltalk will exit. If no files are specified, Smalltalk reads from the terminal, with prompts. </p>
<p> In the second form, the file after <code>-f</code> is the last loaded file; any parameter after that file is passed to the Smalltalk program.</p>
<h2>AUTHOR</h2>
<p> Written by Steve Byrne (sbb [at] gnu.org) and Paolo Bonzini (bonzini [at] gnu.org) </p>
<p> GNU Smalltalk comes with NO WARRANTY, to the extent permitted by law. You may redistribute copies of GNU Smalltalk under the terms of the GNU General Public License. For more information, see the file named COPYING. </p>
<p> Using default kernel path: (null) Using default image path: (null)</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;help-smalltalk [at] gnu.org&gt; GNU Smalltalk home page: &lt;<a rel="nofollow" href="http://smalltalk.gnu.org/">http://smalltalk.gnu.org/</a>&gt;. General help using GNU software: &lt;<a rel="nofollow" href="http://www.gnu.org/gethelp/">http://www.gnu.org/gethelp/</a>&gt;. </p>
<p> Copyright 2009 Free Software Foundation, Inc.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>Smalltalk</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>Smalltalk</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info gst</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
