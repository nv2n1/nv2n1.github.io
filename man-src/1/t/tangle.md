---
title: "tangle(1)"
name: "tangle"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tangle/"
description: "tangle – translate WEB to Pascal"
---

<h2 class="name">NAME</h2>
<p> tangle &#8211; translate WEB to Pascal </p>
<h2>SYNOPSIS</h2>
<p> <code>tangle</code> [<i>options</i>] <i>webfile</i>[<i></i><code>.web</code>] [<i>changefile</i>[<i></i><code>.ch</code>]]</p>
<h2>DESCRIPTION</h2>
<p> This manual page is not meant to be exhaustive. The complete documentation for this version of TeX can be found in the info file or manual <i>Web2C: A TeX implementation</i>. </p>
<p> The <code>tangle</code> program converts a Web source document into a Pascal program that may be compiled in the usual way with the on-line Pascal compiler (e.g., <code><a href="/docs/linux/man/1-pc/">pc</a></code>(1)). The output file is packed into lines of 72 characters or less, with the only concession to readability being the termination of lines at semicolons when this can be done conveniently. </p>
<p> The Web language allows you to prepare a single document containing all the information that is needed both to produce a compilable Pascal program and to produce a well-formatted document describing the program in as much detail as the writer may desire. The user of Web must be familiar with both TeX and Pascal. Web also provides a relatively simple, although adequate, macro facility that permits a Pascal program to be written in small easily-understood modules. </p>
<p> The command line should have either one or two names on it. The first is taken as the Web file (and <code>.web</code> is added if there is no extension). If there is another name, it is a change file (and <code>.ch</code> is added if there is no extension). The change file overrides parts of the Web file, as described in the Web system documentation. </p>
<p> The output files are a Pascal file and a string pool file, whose names are formed by adding <code>.p</code> and <code>.pool</code> respectively to the root of the Web file name.</p>
<h2>OPTIONS</h2>
<p> This version of <code>tangle</code> understands the following options. Note that some of these options may render the output unsuitable for processing by a Pascal compiler.</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>&#8211;length</code><i>&nbsp;number</i></p>
<dd> Compare only the first <i>number</i> characters of identifiers when checking for collisions. The default is 32, the original <code>tangle</code> used 7.</p>
<dt><code>&#8211;loose</code></p>
<dd> When checking for collisions between identifiers, honor the settings of the <code>&#8211;lowercase</code>, <code>&#8211;mixedcase</code>, <code>&#8211;uppercase</code>, and <code>&#8211;underline</code> options. This is the default.</p>
<dt><code>&#8211;lowercase</code></p>
<dd> Convert all identifiers to lowercase.</p>
<dt><code>&#8211;mixedcase</code></p>
<dd> Retain the case of identifiers. This is the default.</p>
<dt><code>&#8211;strict</code></p>
<dd> When checking for collisions between identifiers, strip underlines and convert all identifiers to uppercase first.</p>
<dt><code>&#8211;underline</code></p>
<dd> Retain underlines (also known as underscores) in identifiers.</p>
<dt><code>&#8211;uppercase</code></p>
<dd> Convert all identifiers to uppercase. This is the behaviour of the original <code>tangle</code>.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version information and exit.</dl>
<h2>ENVIRONMENT</h2>
<p> The environment variable WEBINPUTS is used to search for the input files, or the system default if WEBINPUTS is not set. See <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) for the details of the searching.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pc/">pc</a></code>(1), <code><a href="/docs/linux/man/1-pxp/">pxp</a></code>(1) (for formatting <code>tangle</code> output when debugging), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1). </p>
<p> Donald E. Knuth, <i>The Web System of Structured Documentation</i>. </p>
<p> Donald E. Knuth, <i>Literate Programming</i>, Computer Journal <code>27</code>, 97-111, 1984. </p>
<p> Wayne Sewell, <i>Weaving a Program</i>, Van Nostrand Reinhold, 1989, ISBN 0-442-31946-0. </p>
<p> Donald E. Knuth, <i>TeX: The Program</i> (Volume B of <i>Computers and Typesetting</i>), Addison-Wesley, 1986, ISBN 0-201-13437-3. </p>
<p> Donald E. Knuth, <i>Metafont: The Program</i> (Volume D of <i>Computers and Typesetting</i>), Addison-Wesley, 1986, ISBN 0-201-13438-1. </p>
<p> These last two are by far the largest extant examples of Web programs. </p>
<p> There is an active Internet electronic mail discussion list on the subject of literate programming; send a subscription request to <i>litprog-request [at] shsu.edu</i> to join.</p>
<h2>AUTHORS</h2>
<p> Web was designed by Donald E. Knuth, based on an earlier system called DOC (implemented by Ignacio Zabala). The <code>tangle</code> and <code>weave</code> programs are themselves written in Web. The system was originally ported to Unix at Stanford by Howard Trickey, and at Cornell by Pavel Curtis. </p>
<h2>Index</h2>
