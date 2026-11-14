---
title: "zile(1)"
name: "zile"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zile/"
description: "Zile – Zile Is Lossy Emacs"
---

<h2>NAME</h2>
<p> Zile &#8211; Zile Is Lossy Emacs</p>
<h2>SYNOPSIS</h2>
<p> <code>zile</code> [<i>OPTION-OR-FILENAME</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Zile is a lightweight Emacs clone that provides a subset of Emacs&#8217;s functionality suitable for basic editing. </p>
<p> Run Zile, the lightweight Emacs clone. </p>
<p> Initialization options:</p>
<dl>
<dt><code>&#8211;no-init-file</code>, <code>-q</code></p>
<dd> do not load ~/.zile</p>
<dt><code>&#8211;funcall</code>, <code>-f</code> FUNC</p>
<dd> call Zile Lisp function FUNC with no arguments</p>
<dt><code>&#8211;load</code>, <code>-l</code> FILE</p>
<dd> load Zile Lisp FILE using the load function</p>
<dt><code>&#8211;help</code></p>
<dd> display this help message and exit</p>
<dt><code>&#8211;version</code></p>
<dd> display version information and exit</dl>
<p> Action options:</p>
<dl>
<dt>FILE</p>
<dd> visit FILE using find-file</p>
<dt>+LINE FILE</p>
<dd> visit FILE using find-file, then go to line LINE</dl>
<p> Exit status is 0 if OK, 1 if it cannot start up, for example because of an invalid command-line argument, and 2 if it crashes or runs out of memory.</p>
<h2>FILES</h2>
<p> ~/.zile &#8212; user&#8217;s Zile init file </p>
<p> /usr/share/zile/dotzile.sample &#8212; which contains some useful code for the init file.</p>
<h2>AUTHOR</h2>
<p> Zile was written by Sandro Sigala, David A. Capello and Reuben Thomas. The Lisp interpreter is based on code by Scott Lawrence.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to bug-zile [at] gnu.org.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2014 Free Software Foundation, Inc. GNU Zile comes with ABSOLUTELY NO WARRANTY. You may redistribute copies of Zile under the terms of the GNU General Public License. For more information about these matters, see the file named COPYING.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-emacs/">emacs</a></code>(1) </p>
<h2>Index</h2>
