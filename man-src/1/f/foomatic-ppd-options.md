---
title: "foomatic-ppd-options(1)"
name: "foomatic-ppd-options"
section: "1"
letter: "f"
url: "/docs/linux/man/1-foomatic-ppd-options/"
description: "foomatic-ppd-options – show the PPD options"
---

<h2>NAME</h2>
<p> foomatic-ppd-options &#8211; show the PPD options</p>
<h2>SYNOPSIS</h2>
<p> <code>foomatic-ppd-options [-d=debuglevel] [ ppdfiles ]</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>foomatic-ppd-options</code> program reads the specified PPD files or stdin and decodes the PPD file to produce a list of options. This is really just a text based version of other print configuration tools. </p>
<p> The output format consists of a set of lines, each starting with a keyword, followed by a set of options and the default value. For example:</p>
<dl>
<dt>
<dd>
<pre><code>
makemodel = Tektronix Phaser 350 Foomatic / Postscript(recommended)
                                                name = PageSize;
default = Letter;
options = Letter(US Letter),
    A4(A4), 11x17(11x17), A3(A3), A5(A5), B5(B5 \(JIS\)), ... name = PageRegion;
default = Letter;
options = Letter(US Letter), A4(A4), ...
</code></pre>
</dl>
<p> Each option starts with the <code>name</code> tag, followed by a default value (if any), followed by the set of options and a comment describing them. Punctuation in the comment is escaped.</p>
<h3>Options</h3>
<dl>
<dt><code>-d</code><i>debuglevel</i></p>
<dd> Set the debug level. 0 disables debug messages. </p>
<dt><code>[&nbsp;<wbr>files&nbsp;<wbr>]</code></p>
<dd> The list of PPD files to read for options. A &#8216;-&#8216; causes STDIN to be read. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>foomatic-ppd-options</code> exits with a 0 status if successful, and nonzero if an error. An error message is also printed on standard error (STDERR). </p>
<h2>AUTHOR</h2>
<p> Patrick Powell &lt;papowell at astart.com&gt; </p>
<h2>BUGS</h2>
<p> Probably. But it has been tested. </p>
<h2>Index</h2>
