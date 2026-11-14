---
title: "colordiff(1)"
name: "colordiff"
section: "1"
letter: "c"
url: "/docs/linux/man/1-colordiff/"
description: "colordiff – a tool to colorize diff output"
---

<h2 class="name">NAME</h2>
<p> colordiff &#8211; a tool to colorize <code>diff</code> output </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>colordiff</code> [<i>diff options</i>] [<i>colordiff options</i>] {<i>file1</i>} {<i>file2</i>}</dl>
<h2>DESCRIPTION</h2>
<dd>colordiff is a wrapper for <code>diff</code> and produces the same output as <code>diff</code> but with coloured syntax highlighting at the command line to improve readability. The output is similar to how a <code>diff</code>-generated patch might appear in Vim or Emacs with the appropriate syntax highlighting options enabled. The colour schemes can be read from a central configuration file or from a local user ~/.colordiffrc file. </p>
<p> colordiff makes use of ANSI colours and as such will only work when ANSI colours can be used &#8211; typical examples are xterms and Eterms, as well as console sessions. </p>
<p> colordiff has been tested on various flavours of Linux and under OpenBSD, but should be broadly portable to other systems.</p>
<h2>USAGE</h2>
<p> Use colordiff wherever you would normally use <code>diff</code>, or instead pipe output to colordiff: </p>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
$ colordiff file1 file2
$ diff -u file1 file2 | colordiff
</pre>
</dl>
<p> You can pipe the output to &#8216;less&#8217;, using the &#8216;-R&#8217; option (some systems or terminal types may get better results using &#8216;-r&#8217; instead), which keeps the colour escape sequences, otherwise displayed incorrectly or discarded by &#8216;less&#8217;: </p>
<dl>
<dt>
<dd>
<pre>
$ diff -u file1 file2 | colordiff | less -R
</pre>
</dl>
<p> If you want to force disable colour escape sequences (for example pipe the output to <code>patch</code>), you can use option &#8216;&#8211;color=no&#8217; to do so: </p>
<dl>
<dt>
<dd>
<pre>
$ diff -u file1 file2 | colordiff --color=no | patch -p0 -d another-working-dir
</pre>
</dl>
<p> If you have <code>wdiff</code> installed, colordiff will correctly colourise the added and removed text, provided that the &#8216;-n&#8217; option is given to <code>wdiff</code>: </p>
<dl>
<dt>
<dd>
<pre>
$ wdiff -n file1 file2 | colordiff
</pre>
</dl>
<p> You may find it useful to make <code>diff</code> automatically call <code>colordiff</code>. Add the following line to ~/.bashrc (or equivalent): </p>
<dl>
<dt>
<dd>
<pre>
alias diff=colordiff
</pre>
</dl>
<p> Any options passed to colordiff are passed through to <code>diff</code> except for the colordiff-specific option &#8216;difftype&#8217;, e.g. </p>
<dl>
<dt>
<dd>
<pre>
colordiff --difftype=debdiff file1 file2
</pre>
</dl>
<p> Valid values for &#8216;difftype&#8217; are: diff, diffc, diffu, diffy, wdiff, debdiff; these correspond to plain diffs, context diffs, unified diffs, side-by-side diffs, wdiff output and debdiff output respectively. Use these overrides when colordiff is not able to determine the diff-type automatically. </p>
<p> Alternatively, a construct such as &#8216;cvs diff SOMETHING | colordiff&#8217; can be included in ~/.bashrc as follows: </p>
<dl>
<dt>
<dd>
<pre>
function cvsdiff () { cvs diff $@ | colordiff; }
</pre>
</dl>
<p> Or, combining the idea above using &#8216;less&#8217;: </p>
<dl>
<dt>
<dd>
<pre>
function cvsdiff () { cvs diff $@ | colordiff |less -R; }
</pre>
</dl>
<p> Note that the function name, cvsdiff, can be customized. </p>
<p> By default colordiff returns the exit code of the underlying diff invocation (if there is one), but there are some circumstances where it is useful to force colordiff&#8217;s exit code to be zero: to do this use the option &#8216;&#8211;fakeexitcode&#8217;: </p>
<dl>
<dt>
<dd>
<pre>
colordiff --fakeexitcode ...
</pre>
</dl>
<h2>FILES</h2>
<p> /etc/colordiffrc</p>
<dl>
<dt>
<dd> Central configuration file. User-specific settings can be enabled by copying this file to ~/.colordiffrc and making the appropriate changes.</dl>
<p> colordiffrc-lightbg</p>
<dl>
<dt>
<dd> Alternate configuration template for use with terminals having light backgrounds. Copy this to /etc/colordiffrc or ~/.colordiffrc and customize.</dl>
<p> colordiffrc-gitdiff</p>
<dl>
<dt>
<dd> Alternate configuration template for use with terminals having dark backgrounds, with colour defaults set to match the output of &#8216;git diff&#8217;. Copy this to /etc/colordiffrc or ~/.colordiffrc and customize.</dl>
<h2>BUGS</h2>
<p> Bug reports and suggestions/patches to davee [at] sungate.co.uk please.</p>
<h2>AUTHORS</h2>
<p> <code>Dave Ewart</code></p>
<dl>
<dt>
<dd> colordiff author and Debian packager</dl>
<p> <code>Graham Wilson</code></p>
<dl>
<dt>
<dd> Manual page and XML source author</dl>
<p> <code>Colin Tuckley</code></p>
<dl>
<dt>
<dd> Debian package sponsor</dl>
<h2>Index</h2>
