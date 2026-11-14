---
title: "gopen(1)"
name: "gopen"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gopen/"
description: "gopen – open files"
---

<h2>NAME</h2>
<p> gopen &#8211; open files</p>
<h2>SYNOPSIS</h2>
<p> <code>gopen</code> [<code>-a</code> <i>application</i>] [<code>-o</code>] [<code>-p</code>] [<code>-NXHost</code> <i>hostname</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code>gopen</code> command allows you open a file (or directory) as if you had double clicked the object&#8217;s icon. </p>
<p> It is possible to specify one or more <i>filenames</i> which are interpreted relative to the current working directory. </p>
<p> By default, <code>gopen</code> will open <i>filename</i> with the application currently assigned to the file&#8217;s extension. But by specifing the <code>-a</code> flag on the command line you can tell <code>gopen</code> to open the file with another application. </p>
<p> You can also directly print a file without ( <code>-p</code> ) or with ( <code>-p -o </code> ) opening it. </p>
<p> As with most other GNUstep software, it is easily possible to attach the process to a remote window server using the <code>-NXHost</code> flag. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a </code><i>application</p>
<dd> use application</i> to open <i>filename</i></p>
<dt><code>-o</p>
<dd> open </code><i>filename</i> (may be used in conjunction with <code>-p</code> ).</p>
<dt><code>-p</p>
<dd> print </code><i>filename</i> instead of opening.</p>
<dt><code>-NXHost </code><i>hostname</p>
<dd> attach to remote window server on hostname</i></dl>
<h2>EXAMPLES</h2>
<p> Open all files with a .txt extension in the current directory: </p>
<p> <i>gopen *.txt</i> </p>
<p> To open a source file in CodeEditor (instead of the current default application), type: </p>
<p> <i>gopen -a CodeEditor MySourceFile.m</i> </p>
<p> To print the .plan file in your home folder, use the <code>-p</code> flag: </p>
<p> <i>gopen -p ~/.plan</i> </p>
<h2>BUGS</h2>
<p> Using the <code>-a</code> <i>application</i> argument, <code>gopen</code> allows you to open any kind of file with any application you want. This does, however, not work with applications employing the NSDocument architecture as they will only receive filenames whose types the application has registered. To circumvent this limitation, applications may advertise their ability to open all kinds of files through the &quot;*&quot; filetype. When <code>gopen</code> is used with only the <code>-a</code> <i>application </i> argument but no <i>filename</i><br />
&nbsp;<wbr>present, the application is simply launched without opening a specific file.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-gnustep/">GNUstep</a>(7), <a href="/docs/linux/man/1-openapp/">openapp</a>(1)</p>
<h2>HISTORY</h2>
<p> <code>gopen</code> was written November 2001. This manual page was first written July 2003.</p>
<h2>AUTHORS</h2>
<p> <code>gopen </code> was written by Gregory Casamento &lt;greg_casamento [at] yahoo.com&gt;. This man page was written by Martin Brecher &lt;martin [at] mb-itconsulting.com&gt;. </p>
<h2>Index</h2>
