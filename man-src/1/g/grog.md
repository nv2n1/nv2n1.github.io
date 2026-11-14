---
title: "grog(1)"
name: "grog"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grog/"
description: "grog – guess options for a following groff command"
---

<h2 class="name">NAME</h2>
<p> grog &#8211; guess options for a following groff command </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-C</code> ] [ <code>-T </code><i>device</i> ] [ <code>&#8211;run</code> ] [ <code>&#8211;warnings</code> ] [ <code>&#8211;ligatures</code> ] [<i>groff-option</i> &#8230; ] [ <code>&#8212;</code> ] [<i>filespec</i> &#8230; ] <code>-h</code> <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>grog</code> reads the input (file names or standard input) and guesses which of the <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1) options are needed to perform the input with the <code>groff</code> program. A suitable device is now always written as <code>-T</code><i>device</i> including the groff default as <code>-T ps</code>. </p>
<p> The corresponding <code>groff</code> command is usually displayed in standard output. With the option <code>&#8211;run</code>, the generated line is output into standard error and the generated <code>groff</code> command is run on the <i>standard output</i>. <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1) relies on a perfectly running <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> The option <code>-v</code> or <code>&#8211;version</code> prints information on the version number. Also <code>-h</code> or <code>&#8211;help</code> prints usage information. Both of these options automatically end the <code>grog</code> program. Other options are thenignored, and no <code>groff</code> command line is generated. The following 3 options are the only <code>grog</code> options,</p>
<dl>
<dt><code>-C</code></p>
<dd> this option means enabling the <i>groff</i> compatibility mode, which is also transfered to the generated <code>groff</code> command line.</p>
<dt><code>&#8211;ligatures</code></p>
<dd> this option forces to include the arguments <code>-P-y -PU</code> within the generated <code>groff</code> command line.</p>
<dt><code>&#8211;run</code></p>
<dd> with this option, the command line is output at standard error and then run on the computer.</p>
<dt><code>&#8211;warnings</code></p>
<dd> with this option, some more warnings are output to standard error.</dl>
<p> All other specified short options (words starting with one minus character <code>&#8211;</code>) are interpreted as <code>groff</code> options or option clusters with or without argument. No space is allowed between options and their argument. Except from the <code>-m</code><i>arg</i> options, all options will be passed on, i.e. they are included unchanged in the command for the output without effecting the work of <code>grog</code>. </p>
<p> A <i>filespec</i> argument can either be the name of an existing file or a single minus <code>&#8211;</code> to mean standard input. If no <i>filespec</i> is specified standard input is read automatically.</p>
<h2>DETAILS</h2>
<p> <code>grog</code> reads all <i>filespec</i> parameters as a whole. It tries to guess which of the following <code>groff</code> options are required for running the input under <code>groff</code>: <code>-e</code>, <code>-g</code>, <code>-G</code>, <code>-j</code>, <code>-p</code>, <code>-R</code>, <code>-s</code>, <code>-t</code> (preprocessors); and <code>-man</code>, <code>-mdoc</code>, <code>-mdoc-old</code>, <code>-me</code>, <code>-mm</code>, <code>-mom</code>, and <code>-ms</code> (macro packages). </p>
<p> The guessed <code>groff</code> command including those options and the found <i>filespec</i> parameters is put on the standard output. </p>
<p> It is possible to specify arbitrary <code>groff</code> options on the command line. These are passed on the output without change, except for the <code>-m</code><i>arg</i> options. </p>
<p> The <code>groff</code> program has trouble when the wrong <code>-m</code><i>arg</i> option or several of these options are specified. In these cases, <code>grog</code> will print an error message and exit with an error code. It is better to specify no <code>-m</code><i>arg</i> option. Because such an option is only accepted and passed when <code>grog</code> does not find any of these options or the same option is found. </p>
<p> If several different <code>-m</code><i>arg</i> options are found by <code>grog</code> an error message is produced and the program is terminated with an error code. But the output is written with the wrong options nevertheless. </p>
<p> Remember that it is not necessary to determine a macro package. A <i>roff</i> file can also be written in the <i>groff</i> language without any macro package. <code>grog</code> will produce an output without an <code>-m</code><i>arg</i> option. </p>
<p> As <code>groff</code> also works with pure text files without any <i>roff</i> requests, <code>grog</code> cannot be used to identify a file to be a <i>roff</i> file. </p>
<p> The <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1) program heavily depends on a working <code>grog</code>.</p>
<h2>EXAMPLES</h2>
<p> Calling</p>
<dl>
<dt>
<dd> grog meintro.me</dl>
<p> results in</p>
<dl>
<dt>
<dd> groff -me meintro.me</dl>
<p> So <code>grog</code> recognized that the file <code>meintro.me</code> is written with the <code>-me</code> macro package. On the other hand,</p>
<dl>
<dt>
<dd> grog pic.ms</dl>
<p> outputs</p>
<dl>
<dt>
<dd> groff -p -t -e -ms pic.ms</dl>
<p> Besides determining the macro package <code>-ms</code>, <code>grog</code> recognized that the file <code>pic.ms</code> additionally needs <code>-pte</code>, the combination of <code>-p</code> for <i>pic</i>, <code>-t</code> for <i>tbl</i>, and <code>-e</code> for <i>eqn</i>. If both of the former example files are combined by the command</p>
<dl>
<dt>
<dd> grog meintro.me pic.ms</dl>
<p> an error message is sent to standard error because <code>groff</code> cannot work with two different macro packages:</p>
<dl>
<dt>
<dd> grog: error: there are several macro packages: -me -ms</dl>
<p> Additionally the corresponding output with the wrong options is printed to standard output:</p>
<dl>
<dt>
<dd> groff -pte -me -ms meintro.me pic.ms</dl>
<p> But the program is terminated with an error code. The call of</p>
<dl>
<dt>
<dd> grog -ksS -Tdvi grnexmpl.g</dl>
<p> contains several <code>groff</code> options that are just passed on the output without any interface to <code>grog</code>. These are the option cluster <code>-ksS</code> consisting of <code>-k</code>, <code>-s</code>, and <code>-S</code>; and the option <code>-T</code> with argument <code>dvi</code>. The output is</p>
<dl>
<dt>
<dd> groff -k -s -S -Tdvi grnexmpl.g</dl>
<p> so no additional option was added by <code>grog</code>. As no option <code>-m</code><i>arg</i> was found by <code>grog</code> this file does not use a macro package.</p>
<h2>AUTHORS</h2>
<p> <code>grog</code> was originally written by James Clark. The current Perl implementation was written by Bernd Warken with contributions from Ralph Corderoy, and is maintained by Werner Lemberg</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1) </p>
<h2>Index</h2>
