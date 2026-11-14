---
title: "ksvalidator(1)"
name: "ksvalidator"
section: "1"
letter: "k"
url: "/docs/linux/man/1-ksvalidator/"
description: "ksvalidator — verify the syntax of a kickstart file"
---

<h2>NAME</h2>
<p> ksvalidator &#8212; verify the syntax of a kickstart file</p>
<h2>SYNOPSIS</h2>
<p> <code>ksvalidator</code> [<code>-e</code> | <code>&#8211;firsterror</code>] [<code>-i</code> | <code>&#8211;followincludes</code>] [<code>-l</code> | <code>&#8211;listversions</code>] [<code>-v</code> | <code>&#8211;version VERSION</code>] INFILE</p>
<h2>DESCRIPTION</h2>
<p> <code>ksvalidator</code> is a program that takes an input kickstart file and attempts to verify that it is syntactically correct. This includes checking basics like proper quoting and making sure required options have values, and more advanced checks like verifying the file does not include deprecated or removed kickstart commands. Mutually exclusive options can also be caught, as can certain classes of partitioning errors (like using the same device name multiple times). </p>
<p> <code>ksvalidator</code> does have its limitations. It cannot run validate the syntax of %pre, %pre-install, and %post scripts, nor does it attempt to run them. It cannot check that the %packages section is valid. Most importantly, it cannot guarantee that an input kickstart file will install properly, because it does not understand the complexities of partitioning and what potentially already exists on disk.</p>
<h2>EXIT STATUS</h2>
<p> <code>ksvalidator</code> returns 0 on success, and 1 if INFILE does not exist or there is an error parsing the kickstart file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e</code>, <code>&#8211;firsterror</code></p>
<dd> Stop on the first warning or error. By default, <code>ksvalidator</code> will attempt to process the entire file, potentially raising multiple errors.</p>
<dt><code>-i</code>, <code>&#8211;followincludes</code></p>
<dd> Process included files in the input file when they are seen, like anaconda would. If the included file does not exist (this can happen for a variety of reasons, but the most common being a %pre script that generates an included file) and this option is given, an error will be generated and processing halted.</p>
<dt><code>-l</code>, <code>&#8211;listversions</code></p>
<dd> List all versions of kickstart syntax supported by <code>ksvalidator</code>. This is useful for determining what values can be fed back in on a second run.</p>
<dt><code>-v</code>, <code>&#8211;version VERSION</code></p>
<dd> Use this version of kickstart syntax when processing the file, or the latest if no version is given.</dl>
<h2>SEE ALSO</h2>
<p> ksflatten (1), ksverdiff (1) </p>
<h2>Index</h2>
