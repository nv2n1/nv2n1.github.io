---
title: "qrencode(1)"
name: "qrencode"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qrencode/"
description: "qrencode – Encode input data in a QR Code and save as a PNG or EPS image."
---

<h2>NAME</h2>
<p> qrencode &#8211; Encode input data in a QR Code and save as a PNG or EPS image.</p>
<h2>SYNOPSIS</h2>
<p> <code>qrencode</code> [OPTION]&#8230; [STRING] </p>
<h2>DESCRIPTION</h2>
<p> Libqrencode is a library for encoding data in a QR Code symbol, a kind of 2D symbology that can be scanned by handy terminals such as a mobile phone with CCD. The capacity of QR Code is up to 7000 digits or 4000 characters, and has high robustness. </p>
<p> Qrencode is a utility software using libqrencode to encode string data in a QR Code and save as a PNG or EPS image. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> display help message.</p>
<dt><code>-o FILENAME, &#8211;output=FILENAME</code></p>
<dd> write image to FILENAME. If &#8216;-&#8216; is specified, the result will be output to standard output. If -S is given, structured symbols are written to FILENAME-01.png, FILENAME-02.png, &#8230; (suffix is removed from FILENAME, if specified)</p>
<dt><code>-s NUMBER, &#8211;size=NUMBER</code></p>
<dd> specify the size of dot (pixel). (default=3)</p>
<dt><code>-l {LMQH}, &#8211;level={LMQH}</code></p>
<dd> specify error collectin level from L (lowest) to H (highest). (default=L)</p>
<dt><code>-v NUMBER, &#8211;symversion=NUMBER</code></p>
<dd> specify the version of the symbol. (default=auto)</p>
<dt><code>-m NUMBER, &#8211;margin=NUMBER</code></p>
<dd> specify the width of margin. (default=4)</p>
<dt><code>-d NUMBER, &#8211;dpi=NUMBER</code></p>
<dd> specify the DPI of the generated PNG. (default=72)</p>
<dt>
<dd> <code>-t {PNG,EPS,SVG,ANSI,ANSI256,ASCII,ASCIIi,UTF8,ANSIUTF8}</code></p>
<dt>
<dd> <code>&#8211;type={PNG,EPS,SVG,ANSI,ANSI256,ASCII,ASCIIi,UTF8,ANSIUTF8}</code> specify the type of the generated image. (default=PNG)</p>
<dt><code>-S, &#8211;structured</code></p>
<dd> make structured symbols. Version must be specified.</p>
<dt><code>-k, &#8211;kanji</code></p>
<dd> assume that the input text contains kanji (shift-jis).</p>
<dt><code>-c, &#8211;casesensitive</code></p>
<dd> encode lower-case alphabet characters in 8-bit mode. (default)</p>
<dt><code>-i, &#8211;ignorecase</code></p>
<dd> ignore case distinctions and use only upper-case characters.</p>
<dt><code>-8, &#8211;8bit</code></p>
<dd> encode entire data in 8-bit mode. -k, -c and -i will be ignored.</p>
<dt><code>-M, &#8211;micro</code></p>
<dd> encode in a Micro QR Code. (experimental)</p>
<dt>
<dd> <code>&#8211;foreground=RRGGBB[AA]</code></p>
<dt>
<dd> <code>&#8211;background=RRGGBB[AA]</code> specify foreground/background color in hexadecimal notation. 6-digit (RGB) or 8-digit (RGBA) form are supported. Color output support available only in PNG and SVG.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> display the version number and copyrights of the qrencode.</p>
<dt><code>[STRING]</code></p>
<dd> input data. If it is not specified, data will be taken from standard input. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>qrencode -l L -v 1 -o output.png &#8216;Hello, world!&#8217;</code></p>
<dd> encode into a symbol version 1, level L.</p>
<dt><code>qrencode -iSv 1 &#8211;output=output.png</code></p>
<dd> read standard input and encode it into a structured-appended symbols in case-insensitive mode. </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by Kentaro Fukuchi. </p>
<h2>RESOURCES</h2>
<dl>
<dt>Main Web Site: <a rel="nofollow" href="http://fukuchi.org/works/qrencode/">http://fukuchi.org/works/qrencode/</a></p>
<dd>
<dt>Source code repository: <a rel="nofollow" href="https://github.com/fukuchi/libqrencode/">https://github.com/fukuchi/libqrencode/</a></p>
<dd>
</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2006-2012 Kentaro Fukuchi. </p>
<h2>Index</h2>
