---
title: "irpty(1)"
name: "irpty"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irpty/"
description: "irpty – pseudo tty driver"
---

<h2>NAME</h2>
<p> irpty &#8211; pseudo tty driver</p>
<h2>SYNOPSIS</h2>
<p> <code>irpty</code> [<i>options</i>] <i>config_file &#8212; program </i>[<i>args </i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> irpty connects to lircd to receive infrared codes and converts them to key strokes. E.g. type irpty ~/.config/lircrc &#8212; workbone to control the CD-player program workbone. Of course you will have to create an appropriate config file for this purpose first. The config string will be passed to the desired application. Note that you can use escape sequences to specify non printable characters. Have a look at the<br />
&nbsp;<wbr>.lircrc file format description for details.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> display usage summary</p>
<dt><code>-V</code> <code>&#8211;version</code></p>
<dd> display version</p>
<dt><code>-e</code> <code>&#8211;no-echo</code></p>
<dd> disable echo</p>
<dt><code>-i</code> <code>&#8211;ignore-eof</code></p>
<dd> ignore EOF</p>
<dt><code>-n</code> <code>&#8211;non-interactive</code></p>
<dd> force non-interactive mode</p>
<dt><code>-v</code> <code>&#8211;verbose</code></p>
<dd> verbose mode</dl>
<h2>SEE ALSO</h2>
<p> The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
<h2>Index</h2>
