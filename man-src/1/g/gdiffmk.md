---

title: "gdiffmk(1)"
name: "gdiffmk"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdiffmk/"
description: "gdiffmk – mark differences between groff/nroff/troff files"
---

<p> gdiffmk &#8211; mark differences between groff/nroff/troff files </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-a </code><i>addmark</i> ] [ <code>-c </code><i>changemark</i> ] [ <code>-d </code><i>deletemark</i> ] [<code>-D</code> [<code>-B</code>] [<code>-M</code> <i>mark1 mark2</i>]] [ <code>-x </code><i>diffcmd</i> ] [ <code>&#8212;</code> ] <i>file1</i> <i>file2</i> [<i>output</i>] <code>&#8211;help</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>gdiffmk</code> compares two <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1), or <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1) documents, <i>file1</i> and <i>file2</i>, and creates an output which is <i>file2</i> with added &#8220;margin character&#8221; (.mc) commands that indicate the differences. </p>
<p> If the <i>output</i> filename is present, the output is written there. If it is <code>&#8211;</code> or absent the output is written to the standard output. </p>
<p> If the <i>file1</i> or <i>file2</i> argument is <code>&#8211;</code> the standard input is read for that input. Clearly both cannot be <code>&#8211;</code>. </p>
<p> Note that the output is not necessarily compatible with all macro packages and all preprocessors. See section &#8220;Bugs&#8221; below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code><i>addmark</i></dt>
<dd> Use the <i>addmark</i> for source lines not in <i>file1</i> but present in <i>file2</i>. Default: <code>+</code>.</dd>
<dt><code>-B</code></dt>
<dd> By default, the deleted texts marked by the <code>-D</code> option end with an added troff break command, <code>.br</code>, to ensure that the deletions are marked properly. This is the only way to guarantee that deletions and small changes get flagged. This option directs the program not to insert these breaks; it makes no sense to use it without <code>-D</code>.</dd>
<dt><code>-c</code><i>changemark</i></dt>
<dd> Use the <i>changemark</i> for changed source lines. Default: <code>|</code>.</dd>
<dt><code>-d</code><i>deletemark</i></dt>
<dd> Use the <i>deletemark</i> for deleted source lines. Default: <code>*</code>.</dd>
<dt><code>-D</code></dt>
<dd> Show the deleted portions from changed and deleted text. Default delimiting marks: <code>[[</code> &#8230; <code>]]</code>.</dd>
<dt><code>-M</code><i>mark1 mark2</i></dt>
<dd> Change the delimiting marks for the <code>-D</code> option. It makes no sense to use this option without <code>-D</code>.</dd>
<dt><code>-x</code><i>diffcmd</i></dt>
<dd> Use the <i>diffcmd</i> command to perform the comparison of <i>file1</i> and <i>file2</i>. In particular, <i>diffcmd</i> should accept the GNU <code>diff</code> <code>-D</code><i>name</i> option. Default: <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1).</dd>
<dt><code>&#8212;</code></dt>
<dd> All the following arguments are treated as file names, even if they begin with <code>&#8211;</code>.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Print a usage message on standard error output and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version information on the standard output and exit.</dd></dl>
<h2>BUGS</h2>
<p> The output is not necessarily compatible with all macro packages and all preprocessors. A workaround that is often successful against preprocessor problems is to run <code>gdiffmk</code> on the output of all the preprocessors instead of the input source. </p>
<p> <code>gdiffmk</code> relies on the <code>-D</code><i>name</i> option of GNU <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1) to make a merged &#8220;#ifdef&#8221; output format. It hasn&#8217;t been tested whether other versions of <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1) do support this option. See also the <code>-x</code><i>diffcmd</i> option.</p>
<h2>AUTHORS</h2>
<p> <code>gdiffmk</code> was written and is maintained by Mike Bianchi</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1), <code>gtroff</code>(1), <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1) </p>
