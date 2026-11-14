---
title: "ddd(1)"
name: "ddd"
section: "1"
letter: "d"
url: "/docs/linux/man/1-ddd/"
description: "ddd – The Data Display Debugger"
---

<h2>NAME</h2>
<p> ddd &#8211; The Data Display Debugger</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>ddd</code></p>
<dd> [<code>&#8211;help</code>] [<code>&#8211;gdb</code>] [<code>&#8211;dbx</code>] [<code>&#8211;ladebug</code>] [<code>&#8211;wdb</code>] [<code>&#8211;xdb</code>] [<code>&#8211;jdb</code>] [<code>&#8211;pydb</code>] [<code>&#8211;perl</code>] [<code>&#8211;debugger</code> <i>name</i>] [<code>&#8212;</code>[<code>r</code>]<code>host</code> [[<i>username</i><code>@</code>]<i>hostname</i>]] [<code>&#8211;trace</code>] [<code>&#8211;version</code>] [<code>&#8211;configuration</code>] [<i>options&#8230;</i>] [<i>prog</i>[<i>core</i>|<i>procID</i>]]</p>
<dt>but usually just</p>
<dd>
<dt><code>ddd</code></p>
<dd> <i>program</i></dl>
<h2>DESCRIPTION</h2>
<p> <font SIZE="-1">DDD</font> is a graphical front-end for <font SIZE="-1">GDB</font> and other command-line debuggers. Using DDD, you can see what is going on &#8220;inside&#8221; another program while it executes&#8212;or what another program was doing at the moment it crashed. </p>
<p> <font SIZE="-1">DDD</font> can do four main kinds of things (plus other things in support of these) to help you catch bugs in the act:</p>
<dl>
<dt>&bull;</p>
<dd> Start your program, specifying anything that might affect its behavior. </p>
<dt>&bull;</p>
<dd> Make your program stop on specified conditions. </p>
<dt>&bull;</p>
<dd> Examine what has happened, when your program has stopped. </p>
<dt>&bull;</p>
<dd> Change things in your program, so you can experiment with correcting the effects of one bug and go on to learn about another.</dl>
<p> &#8220;Classical&#8221; <font SIZE="-1">UNIX</font> debuggers such as the <font SIZE="-1">GNU</font> debugger (<font SIZE="-1">GDB</font>) provide a command-line interface and a multitude of commands for these and other debugging purposes. <font SIZE="-1">DDD</font> is a comfortable <i>graphical user interface</i> around an inferior <font SIZE="-1">GDB</font>, <font SIZE="-1">DBX</font>, Ladebug, <font SIZE="-1">XDB</font>, <font SIZE="-1">JDB</font>, Python debugger, or Perl debugger. </p>
<p> <font SIZE="-1">DDD</font> is invoked with the shell command <code>ddd</code>. You can open a program to be debugged using `<code>File&rarr;Open Program</code>&#8216; (the `<code>Open Program</code>&#8216; item in the `<code>File</code>&#8216; menu. You can get online help at any time using the `<code>Help</code>&#8216; menu; for the first steps, try `<code>Help&rarr;What Now?</code>&#8216;. Quit <font SIZE="-1">DDD</font> using `<code>File&rarr;Exit</code>&#8216;. </p>
<p> More information on <font SIZE="-1">DDD</font> is contained in the <font SIZE="-1">DDD</font> Manual. You can read the text-only version in <font SIZE="-1">DDD</font> (via `<code>Help&rarr;DDD Reference</code>&#8216;) or in Emacs (as Info file). Full-fledged HTML, PostScript, and PDF versions are available online via the <font SIZE="-1">DDD</font> WWW page, </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code><a rel="nofollow" href="http://www.gnu.org/software/ddd/">http://www.gnu.org/software/ddd/</a></code> </p>
<h2>OPTIONS</h2>
<p> These are the most important options used when starting <font SIZE="-1">DDD</font>. All options may be abbreviated, as long as they are unambiguous; single dashes may also be used. <font SIZE="-1">DDD</font> also understands the usual X options such as `<code>-display</code>&#8216; or `<code>-geometry</code>&#8216;; see <code><a href="/docs/linux/man/1-x/">X</a>(1)</code> for details. </p>
<p> All arguments and options not handled by <font SIZE="-1">DDD</font> are passed to the inferior debugger. To pass an option to the inferior debugger that conflicts with an X option, or with a <font SIZE="-1">DDD</font> option listed here, use the `<code>&#8211;debugger</code>&#8216; option, below. </p>
<dl>
<dt><code>&#8211;configuration</code></p>
<dd> Show the <font SIZE="-1">DDD</font> configuration settings and exit.</p>
<dt><code>&#8211;dbx</code></p>
<dd> Run the <font SIZE="-1">DBX</font> debugger as inferior debugger.</p>
<dt><code>&#8211;debugger </code><i>name</i></p>
<dd> Invoke the inferior debugger <i>name</i>. This is useful if you have several debugger versions around, or if the inferior debugger cannot be invoked as `<code>gdb</code>&#8216;, `<code>dbx</code>&#8216;, `<code>xdb</code>&#8216;, `<code>jdb</code>&#8216;, `<code>pydb</code>&#8216;, or `<code>perl</code>&#8216; respectively.<br />
 This option can also be used to pass options to the inferior debugger that would otherwise conflict with <font SIZE="-1">DDD</font> options. For instance, to pass the option `<code>-d </code><i>directory</i>&#8216; to <font SIZE="-1">XDB</font>, use: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>ddd &#8211;debugger&nbsp;<wbr>&quot;xdb -d&nbsp;<wbr></code><i>directory</i><code>&quot;</code> </p>
<p> If you use the `<code>&#8211;debugger</code>&#8216; option, be sure that the type of inferior debugger is specified as well. That is, use one of the options `<code>&#8211;gdb</code>&#8216;, `<code>&#8211;dbx</code>&#8216;, `<code>&#8211;xdb</code>&#8216;, `<code>&#8211;jdb</code>&#8216;, `<code>&#8211;pydb</code>&#8216;, or `<code>&#8211;perl</code>&#8216; (unless the default setting works fine).</p>
<dt><code>&#8211;gdb</code></p>
<dd> Run the <font SIZE="-1">GDB</font> debugger as inferior debugger.</p>
<dt><code>&#8211;help</code></p>
<dd> Give a list of frequently used options. Show options of the inferior debugger as well.</p>
<dt><code>&#8211;host </code>[<i>username</i><code>@</code>]<i>hostname</i></p>
<dd> Invoke the inferior debugger directly on the remote host <i>hostname</i>. If <i>username</i> is given and the `<code>&#8211;login</code>&#8216; option is not used, use <i>username</i> as remote user name.</p>
<dt><code>&#8211;jdb</code></p>
<dd> Run <font SIZE="-1">JDB</font> as inferior debugger.</p>
<dt><code>&#8211;ladebug</code></p>
<dd> Run Ladebug as inferior debugger.</p>
<dt><code>&#8211;perl</code></p>
<dd> Run Perl as inferior debugger.</p>
<dt><code>&#8211;pydb</code></p>
<dd> Run <font SIZE="-1">PYDB</font> as inferior debugger.</p>
<dt><code>&#8211;rhost </code>[<i>username</i><code>@</code>]<i>hostname</i></p>
<dd> Run the inferior debugger interactively on the remote host <i>hostname</i>. If <i>username</i> is given and the `<code>&#8211;login</code>&#8216; option is not used, use <i>username</i> as remote user name.</p>
<dt><code>&#8211;trace</code></p>
<dd> Show the interaction between <font SIZE="-1">DDD</font> and the inferior debugger on standard error. This is useful for debugging <font SIZE="-1">DDD</font>. If `<code>&#8211;trace</code>&#8216; is not specified, this information is written into `<code>$HOME/.ddd/log</code>&#8216;, such that you can also do a post-mortem debugging.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the <font SIZE="-1">DDD</font> version and exit.</p>
<dt><code>&#8211;wdb</code></p>
<dd> Run the <font SIZE="-1">WDB</font> debugger as inferior debugger.</p>
<dt><code>&#8211;xdb</code></p>
<dd> Run <font SIZE="-1">XDB</font> as inferior debugger.</dl>
<p> A full list of options, including important options of the inferior debugger, can be found in the <font SIZE="-1">DDD</font> manual.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-x/">X</a></code>(1), <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <code><a href="/docs/linux/man/1-dbx/">dbx</a></code>(1), <code><a href="/docs/linux/man/1-wdb/">wdb</a></code>(1), <code><a href="/docs/linux/man/1-xdb/">xdb</a></code>(1), <code><a href="/docs/linux/man/1-perldebug/">perldebug</a></code>(1) </p>
<p> `<code>ddd</code>&#8216; entry in <code>info</code>. </p>
<p> `<code>gdb</code>&#8216; entry in <code>info</code>. </p>
<p> <i>Debugging with </i><font SIZE="-1"><i>DDD</i></font><i>: User&#8217;s Guide and Reference Manual</i>, by Andreas Zeller. </p>
<p> <i>Using </i><font SIZE="-1"><i>GDB</i></font><i>: A Guide to the </i><font SIZE="-1"><i>GNU</i></font><i> Source-Level Debugger</i>, by Richard M. Stallman and Roland H. Pesch. </p>
<p> <i>Java Language Debugging</i>, at <code><a rel="nofollow" href="http://java.sun.com/">http://java.sun.com/</a></code> (and its mirrors) in <code>/products/jdk/1.1/debugging/</code> </p>
<p> <i>The Python Language</i>, at <code><a rel="nofollow" href="http://www.python.org/">http://www.python.org/</a></code> and its mirrors. </p>
<p> <i></i><font SIZE="-1"><i>DDD</i></font><i>&#8212;A Free Graphical Front-End for </i><font SIZE="-1"><i>UNIX</i></font><i> Debuggers</i>, by Andreas Zeller and Dorothea Luetkehaus, Computer Science Report 95-07, Technische Universitaet Braunschweig, 1995. </p>
<p> <i></i><font SIZE="-1"><i>DDD</i></font><i> &#8211; ein Debugger mit graphischer Datendarstellung</i>, by Dorothea Luetkehaus, Diploma Thesis, Technische Universitaet Braunschweig, 1994. </p>
<p> The <font SIZE="-1">DDD</font> <i></i><font SIZE="-1"><i>FTP</i></font><i> site,</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code><a href="ftp://ftp.gnu.org/gnu/ddd">ftp://ftp.gnu.org/gnu/ddd</a></code> </p>
<p> The <font SIZE="-1">DDD</font> <i></i><font SIZE="-1"><i>WWW</i></font><i> page,</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code><a rel="nofollow" href="http://www.gnu.org/software/ddd/">http://www.gnu.org/software/ddd/</a></code> </p>
<p> The <font SIZE="-1">DDD</font> <i>Mailing List,</i> </p>
<p><code>ddd [at] gnu.org</code> </p>
<p> For more information on this list, send a mail to </p>
<p><code>ddd-request [at] gnu.org</code>&nbsp;<wbr>. </p>
<h2>COPYRIGHT</h2>
<p> This manual page is Copyright &#169; 2001 Universitaet Passau, Germany and &#169; 2001-2004 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this manual page provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this manual page under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this manual page into another language, under the above conditions for modified versions, except that this permission notice may be included in translations approved by the Free Software Foundation instead of in the original English. </p>
<h2>Index</h2>
