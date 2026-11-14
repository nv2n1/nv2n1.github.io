---
title: "qr(1)"
name: "qr"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qr/"
description: "qr – script to create QR codes at the command line"
---

<h2>NAME</h2>
<p> qr &#8211; script to create QR codes at the command line</p>
<h2>SYNOPSIS</h2>
<p> qr [&#8211;help] [&#8211;factory=FACTORY] [&#8211;optimize=OPTIMIZE] [data]</p>
<h2>DESCRIPTION</h2>
<p> This script uses the python qrcode module. It can take data from stdin or from the commandline and generate a QR code. Normally it will output the QR code as ascii art to the terminal. If the output is piped to a file, it will output the image (default type of PNG).</p>
<h2>OPTIONS</h2>
<p> <code>&nbsp;<wbr>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Show a help message.</dl>
<p> <code>&nbsp;<wbr>&#8211;factory=FACTORY</code></p>
<dl>
<dt>
<dd> Full python path to the image factory class to create the image with. You can use the following shortcuts to the built-in image factory classes: pil (default), pymaging, svg, svg-fragment, svg-path.</dl>
<p> <code>&nbsp;<wbr>&#8211;optimize=OPTIMIZE</code></p>
<dl>
<dt>
<dd> Optimize the data by looking for chunks of at least this many characters that could use a more efficient encoding method. Use 0 to turn off chunk optimization.</dl>
<p> <code>&nbsp;<wbr>data</code></p>
<dl>
<dt>
<dd> The data from which the QR code will be generated.</dl>
<h2>SEE ALSO</h2>
<p> <a rel="nofollow" href="https://github.com/lincolnloop/python-qrcode/">https://github.com/lincolnloop/python-qrcode/</a> </p>
<h2>Index</h2>
