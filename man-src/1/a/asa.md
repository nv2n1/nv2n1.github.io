---
title: "asa(1)"
name: "asa"
section: "1"
letter: "a"
url: "/docs/linux/man/1-asa/"
description: "asa – convert ASA (Fortran) carriage control charachters"
---

<h2>NAME</h2>
<p> asa &#8211; convert ASA (Fortran) carriage control charachters</p>
<h2>SYNOPSIS</h2>
<p> <code>asa</code> [<i>file</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>asa</code> reads text with ASA cariage control characters from the files specified as its command arguments, or standard input if none are specified, and converts them into line printer control sequences. </p>
<p> These control characters are traditionally used in Fortran programs. </p>
<p> The first character of every line is removed from input, and the following actions are performed: </p>
<p> If the caracter removed is:</p>
<dl>
<dt><code>&lt;space&gt;</code></p>
<dd> the rest of the line is output without change.</p>
<dt><code>0</code></p>
<dd> a <code>&lt;newline&gt;</code> is output, then the rest of the input line.</p>
<dt><code>1</code></p>
<dd> a <code>&lt;form feed&gt;</code> is output, then the rest of the input line.</p>
<dt><code>+</code></p>
<dd> An attempt is made to overstrike the previous line with the one following the character; this can be used for emphasis.</p>
<dt><code>&lt;any other character&gt;</code></p>
<dd> The same actions as for a <code>&lt;space&gt;</code> are performed; this is an extension of the POSIX.2 standard.</dl>
<p> The overstriking generated is compatible to <code><a href="/docs/linux/man/1-less/">less</a>(1)</code> and <code><a href="/docs/linux/man/1-a2ps/">a2ps</a>(1)</code> and may be removed by piping the output through <code>col -b</code> </p>
<p> Tabs in the input file are expanded to a width of eight.</p>
<h2>BUGS</h2>
<p> It is not be possible to use the <code>asa</code> filter for interactive use in Fortran programs, because of the semantics of the <code>+</code> character, and because I/O is buffered.</p>
<h2>CONFORMS TO</h2>
<p> POSIX.2</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-f2c/">f2c</a>(1), <a href="/docs/linux/man/1-f77/">f77</a>(1), <a href="/docs/linux/man/1-col/">col</a>(1), <a href="/docs/linux/man/1-less/">less</a>(1), <a href="/docs/linux/man/1-a2ps/">a2ps</a>(1) </p>
<h2>Index</h2>
