---

title: "stest(1)"
name: "stest"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stest/"
description: "stest – filter a list of files by properties"
---

<p> stest &#8211; filter a list of files by properties</p>
<h2>SYNOPSIS</h2>
<p> <code>stest</code> [<code>-abcdefghlpqrsuwx</code>] [<code>-n</code> <i>file</i>] [<code>-o</code> <i>file</i>] [<i>file</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>stest</code> takes a list of files and filters by the files&#8217; properties, analogous to <i><a href="/docs/linux/man/1-test/">test</a></i>(1). Files which pass all tests are printed to stdout. If no files are given, stest reads files from stdin.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd> Test hidden files.</dd>
<dt><code>-b</code></dt>
<dd> Test that files are block specials.</dd>
<dt><code>-c</code></dt>
<dd> Test that files are character specials.</dd>
<dt><code>-d</code></dt>
<dd> Test that files are directories.</dd>
<dt><code>-e</code></dt>
<dd> Test that files exist.</dd>
<dt><code>-f</code></dt>
<dd> Test that files are regular files.</dd>
<dt><code>-g</code></dt>
<dd> Test that files have their set-group-ID flag set.</dd>
<dt><code>-h</code></dt>
<dd> Test that files are symbolic links.</dd>
<dt><code>-l</code></dt>
<dd> Test the contents of a directory given as an argument.</dd>
<dt><code>-n</code><i> file</i></dt>
<dd> Test that files are newer than <i>file</i>.</dd>
<dt><code>-o</code><i> file</i></dt>
<dd> Test that files are older than <i>file</i>.</dd>
<dt><code>-p</code></dt>
<dd> Test that files are named pipes.</dd>
<dt><code>-q</code></dt>
<dd> No files are printed, only the exit status is returned.</dd>
<dt><code>-r</code></dt>
<dd> Test that files are readable.</dd>
<dt><code>-s</code></dt>
<dd> Test that files are not empty.</dd>
<dt><code>-u</code></dt>
<dd> Test that files have their set-user-ID flag set.</dd>
<dt><code>-v</code></dt>
<dd> Invert the sense of tests, only failing files pass.</dd>
<dt><code>-w</code></dt>
<dd> Test that files are writable.</dd>
<dt><code>-x</code></dt>
<dd> Test that files are executable.</dd></dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></dt>
<dd> At least one file passed all tests.</dd>
<dt><code>1</code></dt>
<dd> No files passed all tests.</dd>
<dt><code>2</code></dt>
<dd> An error occurred.</dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-dmenu/">dmenu</a></i>(1), <i><a href="/docs/linux/man/1-test/">test</a></i>(1) </p>
