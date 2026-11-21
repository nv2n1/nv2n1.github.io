---

title: "ksshell(1)"
name: "ksshell"
section: "1"
letter: "k"
url: "/docs/linux/man/1-ksshell/"
description: "ksshell — an interactive kickstart shell"
---

<h2>NAME</h2>
<p> ksshell &#8212; an interactive kickstart shell</p>
<p> <code>ksflatten</code> [<code>-i</code> | <code>&#8211;input INFILE</code>] [<code>-o</code> | <code>&#8211;output OUTFILE</code>] [<code>-v</code> | <code>&#8211;version VERSION</code>]</p>
<p> <code>ksshell</code> is an interactive kickstart shell. It optionally takes an input kickstart file as the basis, allows the user to specify additional kickstart commands, and then writes out the finished kickstart file to stdout or the given file name. This program supports all the usual readline niceties including tab completion of kickstart commands and their options, though not the values those options can take. </p>
<p> In addition to understanding all the kickstart commands, <code>ksshell</code> has some builtin commands of its own to make working with kickstart files in the context of a shell easier:</p>
<dl>
<dt>.clear</dt>
<dd> Clear the existing kickstart data, including any from INFILE. This essentially starts you over from a blank state.</dd>
<dt>.quit</dt>
<dd> Quit the interactive shell, either saving to the file given by OUTFILE or printing to stdout if none was given.</dd>
<dt>.show</dt>
<dd> Print the current kickstart file state.</dd></dl>
<h2>EXIT STATUS</h2>
<p> <code>ksflatten</code> returns 0 on success, and 1 if VERSION is incorrect. If INFILE does not exist, a warning will be printed but the user will still be dumped to the interactive shell.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;input INFILE</code></dt>
<dd> The name of the input kickstart file.</dd>
<dt><code>-o</code>, <code>&#8211;output OUTFILE</code></dt>
<dd> Write the flattened kickstart file to OUTFILE, or stdout if no filename is given.</dd>
<dt><code>-v</code>, <code>&#8211;version VERSION</code></dt>
<dd> Use this version of kickstart syntax when processing the file, or the latest if no version is given.</dd></dl>
<h2>SEE ALSO</h2>
<p> ksvalidator (1), ksverdiff (1) </p>
