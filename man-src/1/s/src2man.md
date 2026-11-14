---
title: "src2man(1)"
name: "src2man"
section: "1"
letter: "s"
url: "/docs/linux/man/1-src2man/"
description: "src2man – extract man pages from source files."
---

<h2>NAME</h2>
<p> <code>src2man </code>&#8211; extract man pages from source files.</p>
<h2>SYNOPSIS</h2>
<pre><code>
src2man[-n][-d date][-v volume][-r release][srcfile...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>src2man</code> scans source file <i>srcfile</i>. Only C source files are supported for now. Comments blocks starting by &quot;/** num&quot;, where num is a section number, are converted into a man file, using <code><a href="/docs/linux/man/1-txt2man/">txt2man</a></code>(1). </p>
<p> The first line of the comment block must contain the name of the manpage, usually the function name, followed by a &quot;-&quot; and a short description. The following lines are the &quot;DESCRIPTION&quot; section content, except if they are in upper case, in which case they define a new section. </p>
<p> If the next line after a comment block is empty, Then no &quot;SYNOPSIS&quot; section will be generated. Otherwise, <code>src2man</code> will look in the following source lines for a function prototype or a type definion (struct, union, typedef, &#8230;) matching the manpage name, and include it in a &quot;SYNOPSIS&quot; section. This avoids to duplicate the type or function prototype in the comment block. </p>
<p> The best place for code documentation is in the source file, where the body is implemented, not the header file which only contains the prototype. <code>src2man</code> automatically searches for the presence of a prototype in the corresponding header file, and if found, will print a &quot;#include&quot; statement in the synopsis.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code> date</p>
<dd> Set the date of the man pages. Defaults to current date.</p>
<dt><code>-n</code></p>
<dd> No man page is created. The name of the manpages that would be created are printed.</p>
<dt><code>-v</code> volume</p>
<dd> Specify the name of the volume to be printed in center header of generated manpages.</p>
<dt><code>-r</code> <i>release</i></p>
<dd> Specify the project name and <i>release</i> number for the generated manpage.</dl>
<h2>EXAMPLE</h2>
<p> The following example displays C code and comments to generate a manpage foobar.3: </p>
<pre><code>
/** 3
 * foobar - a sample dummy function
 * This line is now the first of the description section.
 * Note that function parameters parm1 and parm2 are highlighted
 * in the generated man page.
 */
int foobar(char *parm1, int parm2)
{
    ... return 0;
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-txt2man/">txt2man</a></code>(1), <code><a href="/docs/linux/man/1-bookman/">bookman</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Marc Vertes &lt;mvertes [at] free.fr&gt; </p>
<h2>Index</h2>
