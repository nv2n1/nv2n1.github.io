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
<h2>SYNOPSIS</h2>
<p> <code>ksflatten</code> [<code>-i</code> | <code>&#8211;input INFILE</code>] [<code>-o</code> | <code>&#8211;output OUTFILE</code>] [<code>-v</code> | <code>&#8211;version VERSION</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>ksshell</code> is an interactive kickstart shell. It optionally takes an input kickstart file as the basis, allows the user to specify additional kickstart commands, and then writes out the finished kickstart file to stdout or the given file name. This program supports all the usual readline niceties including tab completion of kickstart commands and their options, though not the values those options can take. </p>
<p> In addition to understanding all the kickstart commands, <code>ksshell</code> has some builtin commands of its own to make working with kickstart files in the context of a shell easier:</p>
<dl>
<dt>.clear</p>
<dd> Clear the existing kickstart data, including any from INFILE. This essentially starts you over from a blank state.</p>
<dt>.quit</p>
<dd> Quit the interactive shell, either saving to the file given by OUTFILE or printing to stdout if none was given.</p>
<dt>.show</p>
<dd> Print the current kickstart file state.</dl>
<h2>EXIT STATUS</h2>
<p> <code>ksflatten</code> returns 0 on success, and 1 if VERSION is incorrect. If INFILE does not exist, a warning will be printed but the user will still be dumped to the interactive shell.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;input INFILE</code></p>
<dd> The name of the input kickstart file.</p>
<dt><code>-o</code>, <code>&#8211;output OUTFILE</code></p>
<dd> Write the flattened kickstart file to OUTFILE, or stdout if no filename is given.</p>
<dt><code>-v</code>, <code>&#8211;version VERSION</code></p>
<dd> Use this version of kickstart syntax when processing the file, or the latest if no version is given.</dl>
<h2>SEE ALSO</h2>
<p> ksvalidator (1), ksverdiff (1) </p>
<h2>Index</h2>
