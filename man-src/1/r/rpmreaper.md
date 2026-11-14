---
title: "rpmreaper(1)"
name: "rpmreaper"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpmreaper/"
description: "rpmreaper – A tool for removing unnecessary packages from system"
---

<h2>NAME</h2>
<p> rpmreaper &#8211; A tool for removing unnecessary packages from system </p>
<h2>SYNOPSIS</h2>
<p> <code>rpmreaper</code> [<code>-lvh</code>] [<code>-r</code> <i>root</i>] [<i>limit</i>] </p>
<h2>DESCRIPTION</h2>
<p> rpmreaper is a simple ncurses application with a mutt-like interface that allows removing unnecessary packages and their dependencies from the system. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code></p>
<dd> List packages matching <i>limit</i>, or all installed if not specified.</p>
<dt><code>-v</code></p>
<dd> Verbose listing.</p>
<dt><code>-r</code> <i>root</i></p>
<dd> Specify root directory (default is <code>/</code>).</p>
<dt><code>-h</code></p>
<dd> Print help. </p>
</dl>
<p> A <i>limit</i> can be specified to limit the list of displayed packages. The syntax is described in the <code>SEARCH EXPRESSIONS</code> section. </p>
<h2>KEYS</h2>
<dl>
<dt><code>UP, DOWN, LEFT, PGUP, PGDOWN, HOME, END, TAB, BTAB, h, j, k</code></p>
<dd> Move cursor.</p>
<dt><code>[, ], &lt;, &gt;</code></p>
<dd> Scroll screen.</p>
<dt><code>d</code></p>
<dd> Mark the highlighted package to be removed.</p>
<dt><code>D</code></p>
<dd> Mark the highlighted package to be removed even when there are unmarked packages depending on the package.</p>
<dt><code>E</code></p>
<dd> Recursively mark the highlighted package and unmarked packages depending on the package to be removed.</p>
<dt><code>u</code></p>
<dd> Unmark the highlighted package.</p>
<dt><code>U</code></p>
<dd> Unmark the highlighted package even when some dependencies are marked to be removed.</p>
<dt><code>I</code></p>
<dd> Recursively unmark the highlighted package and marked packages that the package depends on. Packages where a choice has to be made to satisfy a dependency will be left with the <code>b</code> flag and the missing packages should be unmarked manually.</p>
<dt><code>r, R</code></p>
<dd> Show/hide list of packages/capabilities that are required by the highlighted package/capability. When a package is highlighted, <code>R</code> includes also packages that are required indirectly.</p>
<dt><code>b, B</code></p>
<dd> Show/hide list of packages/capabilities that require the highlighted package/capability. When a package is highlighted, <code>B</code> includes also packages that require the highlighted package indirectly.</p>
<dt><code>m, M</code></p>
<dd> Show/hide list of capabilities required by the highlighted package. With <code>M</code> the list is limited to capabilities that match with capabilities provided by the parent package of the highlighted package in the currently displayed tree.</p>
<dt><code>p, P</code></p>
<dd> Show/hide list of capabilities provided by the highlighted package. Only capabilities that are required by some other packages may be listed. With <code>P</code> the list is limited to capabilities that match with capabilities required by the parent package of the highlighted package in the currently displayed tree.</p>
<dt><code>o</code></p>
<dd> Sort packages by name, flags or size.</p>
<dt><code>l</code></p>
<dd> Limit the list of displayed packages. Uses the <code>SEARCH EXPRESSION</code> syntax.</p>
<dt><code>/, ?</code></p>
<dd> Search in the package list. Uses the <code>SEARCH EXPRESSION</code> syntax.</p>
<dt><code>n</code></p>
<dd> Search for next package.</p>
<dt><code>N</code></p>
<dd> Search for next package in the opposite direction.</p>
<dt><code>i</code></p>
<dd> Run <code>rpm -qil | less</code> on the highlighted package. If environment variable <code>PAGER</code> is set, its value is used instead of <code>less</code>.</p>
<dt><code>c</code></p>
<dd> Run <code>rpm -e</code> on marked packages to remove them from the system.</p>
<dt><code>C</code></p>
<dd> Similar to <code>c</code>, but extra options can be added to the <code>rpm -e</code> command, e.g. <code>&#8211;nodeps</code> to ignore dependencies when removing the packages.</p>
<dt><code>q</code></p>
<dd> Ask to remove marked packages and quit. If the answer is no, the list of marked packages will be written to <code>stderr</code>.</p>
<dt><code>x</code></p>
<dd> Exit immediately.</p>
<dt><code>F1, F2</code></p>
<dd> Run <code>man rpmreaper</code>.</p>
<dt><code>^R</code></p>
<dd> Reload package list.</p>
<dt><code>^L</code></p>
<dd> Redraw screen. </p>
</dl>
<h2>PACKAGE FLAGS</h2>
<dl>
<dt><code>L</code></p>
<dd> Leaf, no package depends on the package.</p>
<dt><code>l</code></p>
<dd> Partial leaf, some packages may depend on the package and removing the package may remove <code>L</code>/<code>l</code> flag from other packages.</p>
<dt><code>D</code></p>
<dd> Marked to be removed.</p>
<dt><code>o</code></p>
<dd> Part of a dependency cycle.</p>
<dt><code>B</code></p>
<dd> Missing dependencies.</p>
<dt><code>b</code></p>
<dd> Some packages required by the package are marked to be removed. </p>
</dl>
<h2>SEARCH EXPRESSIONS</h2>
<p> Search expression is a regular expression which can be optionally extended with roughly mutt-esque directives for matching package flags. Overall search expression syntax looks like this: </p>
<p> {[!]~<i>flags</i> }[!]<i>regexp</i> </p>
<p> Recognized flags are described in the section <code>PACKAGE FLAGS</code>. Search expression matches a package, if the following three conditions hold: any of the flags specified in <code>~</code> directives is set; none of the flags specified in <code>!~</code> directives are set; and the specified regular expression matches the <code>n-v-r[.a]</code> string of the package. Regular expression consisting of empty string matches all packages. If the regular expression is preceded by <code>!</code>, its meaning is inverted (i.e. it matches where the original wouldn&#8217;t match and vice versa). </p>
<p> Examples: </p>
<dl>
<dt><code>noarch$</code></p>
<dd> Match all noarch packages.</p>
<dt><code>~Ll !i386$</code></p>
<dd> Match all leaf and partial leaf non-i386 packages.</p>
<dt><code>!~D perl</code></p>
<dd> Match all perl packages except those marked for deletion. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-rpm/">rpm</a></code>(8) </p>
<h2>AUTHORS</h2>
<p> Miroslav Lichvar &lt;mlichvar [at] redhat.com&gt;<br />
 Petr Machata &lt;pmachata [at] redhat.com&gt; </p>
<h2>Index</h2>
