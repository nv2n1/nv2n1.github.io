---
title: "texfind(1)"
name: "texfind"
section: "1"
letter: "t"
url: "/docs/linux/man/1-texfind/"
description: "texfind – graphical tool to search for text in TeX input files"
---

<h2 class="name">NAME</h2>
<p> texfind &#8211; graphical tool to search for text in TeX input files</p>
<h2>SYNOPSIS</h2>
<p> <code>texfind</code> [ <i>OPTION</i> &#8230; ] </p>
<h2>DESCRIPTION</h2>
<p> <code>texfind</code> is a graphical, interactive tool that helps you searching through TeX input files, including subdirectories, and allows you to do search/replace tasks using <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1) regular expressions. It opens two windows: One displays the directory hierarchy and allows you to select different search directories. The second window is used to enter the query and display the results. </p>
<h2>SEARCHING</h2>
<p> Enter a search string in the input box at the top, choose the file extension (<i>tex</i> by default) and hit ENTER to start the search. The results will be displayed in the rest of the window. </p>
<p> The search string is a perl regular expression (see <code><a href="/docs/linux/man/1-perlre/">perlre</a></code>(1)), which gives you lots of flexibility. The search-and-replace function also uses perl regex syntax, but you can also just use simple strings. Currently there is no way to save changed files. </p>
<h2>MENU</h2>
<p> Use the right mouse button to open a menu.</p>
<dl>
<dt> <code>File</code> : Currently only used to exit the program</p>
<dt> <code>Edit</code> : Copy selections, select or unselect all</p>
<dt> <code>Search</code> : Open a <code>Find</code> dialog that allows further searching</p>
<dd>through the displayed results. The <code>Replace</code> option can be used to replace single or all occurrences of a string, but currently it is not possible to change the file.</dl>
<p> <code>View</code> : Select specific lines, and adjust word or character wrapping. </p>
<h2>OPTIONS</h2>
<dl>
<dt> <code>&#8211;font</code> : specify the font used for the menu. Default is</p>
<dd>courier.</p>
<dt>
<dd>Other options probably exist. I appreciate input by the program authors, experienced users, or Perl geeks.</p>
<dt></dl>
<h2>SEE ALSO</h2>
<dl>
<dt>&bull;</p>
<dd> <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1), <code><a href="/docs/linux/man/1-perlre/">perlre</a></code>(1).</p>
<dt>&bull;</p>
<dd> ConTeXt wiki &lt;URL: <a rel="nofollow" href="http://www.contextgarden.net">http://www.contextgarden.net</a> &gt;. </p>
</dl>
<h2>BUGS</h2>
<dd>None known. However, the replace function isn&#8217;t the most useful one. </p>
<h2>AUTHOR</h2>
<p> <code>texfind</code> was written for the ConTeXt package by Hans Hagen and Ton Otten, PRAGMA. </p>
<p> This manual page was written by Frank K&uuml;ster &lt;frank [at] kuesterei.ch&gt; for the Debian GNU/Linux system, and modified by Sanjoy Mahajan &lt;sanjoy [at] mit.edu&gt;. It may be used and modified by others without contacting the authors. </p>
<h2>Index</h2>
