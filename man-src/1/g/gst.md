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
<p> GNU Smalltalk usage:</p>
<dl>
<dt>
</dt><dd> gst [ flag &#8230; ] [ file &#8230; ] gst [ flag &#8230; ] { <code>-f</code> | <code>&#8211;file</code> } file [ args &#8230; ]</dd></dl>
<p> Short flags can appear either as <code>-xyz</code> or as <code>-x</code> <code>-y</code> <code>-z</code>. If an option is mandatory for a long option, it is also mandatory for a short one. The currently defined set of flags is:</p>
<dl>
<dt><code>-a</code> <code>&#8211;smalltalk-args</code></dt>
<dd> Pass the remaining arguments to Smalltalk.</dd>
<dt><code>-c</code> <code>&#8211;core-dump</code></dt>
<dd> Dump core on fatal signal.</dd>
<dt><code>-D</code> <code>&#8211;declaration-trace</code></dt>
<dd> Trace compilation of all loaded files.</dd>
<dt><code>-E</code> <code>&#8211;execution-trace</code></dt>
<dd> Trace execution of all loaded files.</dd>
<dt><code>-g</code> <code>&#8211;no-gc-message</code></dt>
<dd> Do not print garbage collection messages.</dd>
<dt><code>-H</code> <code>&#8211;help</code></dt>
<dd> Print this message and exit.</dd>
<dt><code>-i</code> <code>&#8211;rebuild-image</code></dt>
<dd> Ignore the image file; rebuild it from scratch.</dd>
<dt><code>&#8211;maybe-rebuild-image</code></dt>
<dd> Rebuild the image file from scratch if any kernel file is newer.</dd>
<dt><code>-I</code> <code>&#8211;image</code> FILE</dt>
<dd> Instead of `gst.im&#8217;, use FILE as the image file, and ignore the kernel files&#8217; timestamps.</dd>
<dt><code>-K</code> <code>&#8211;kernel-file</code> FILE</dt>
<dd> Make FILE&#8217;s path relative to the image path.</dd>
<dt><code>-q</code> <code>&#8211;quiet</code> <code>&#8211;silent</code></dt>
<dd> Do not print execution information.</dd>
<dt><code>-r</code> <code>&#8211;regression-test</code></dt>
<dd> Run in regression test mode, i.e. make printed messages constant.</dd>
<dt><code>-S</code> <code>&#8211;snapshot</code></dt>
<dd> Save a snapshot just before exiting.</dd>
<dt><code>-v</code> <code>&#8211;version</code></dt>
<dd> Print the Smalltalk version number and exit.</dd>
<dt><code>-V</code> <code>&#8211;verbose</code></dt>
<dd> Show names of loaded files and execution stats.</dd>
<dt><code>&#8211;emacs-mode</code></dt>
<dd> Execute as a `process&#8217; (from within Emacs)</dd>
<dt><code>&#8211;kernel-directory</code> DIR</dt>
<dd> Look for kernel files in directory DIR.</dd>
<dt><code>&#8211;no-user-files</code></dt>
<dd> Don&#8217;t read user customization files.</dd>
<dt>&#8211;</dt>
<dd> Read input from standard input explicitly.</dd></dl>
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
</dt><dd> <code>info gst</code></dd></dl>
<p> should give you access to the complete manual. </p>
