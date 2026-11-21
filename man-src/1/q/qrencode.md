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
<dt><code>-h, &#8211;help</code></dt>
<dd> display help message.</dd>
<dt><code>-o FILENAME, &#8211;output=FILENAME</code></dt>
<dd> write image to FILENAME. If &#8216;-&#8216; is specified, the result will be output to standard output. If -S is given, structured symbols are written to FILENAME-01.png, FILENAME-02.png, &#8230; (suffix is removed from FILENAME, if specified)</dd>
<dt><code>-s NUMBER, &#8211;size=NUMBER</code></dt>
<dd> specify the size of dot (pixel). (default=3)</dd>
<dt><code>-l {LMQH}, &#8211;level={LMQH}</code></dt>
<dd> specify error collectin level from L (lowest) to H (highest). (default=L)</dd>
<dt><code>-v NUMBER, &#8211;symversion=NUMBER</code></dt>
<dd> specify the version of the symbol. (default=auto)</dd>
<dt><code>-m NUMBER, &#8211;margin=NUMBER</code></dt>
<dd> specify the width of margin. (default=4)</dd>
<dt><code>-d NUMBER, &#8211;dpi=NUMBER</code></dt>
<dd> specify the DPI of the generated PNG. (default=72)</dd>
<dt>
</dt><dd> <code>-t {PNG,EPS,SVG,ANSI,ANSI256,ASCII,ASCIIi,UTF8,ANSIUTF8}</code></dd>
<dt>
</dt><dd> <code>&#8211;type={PNG,EPS,SVG,ANSI,ANSI256,ASCII,ASCIIi,UTF8,ANSIUTF8}</code> specify the type of the generated image. (default=PNG)</dd>
<dt><code>-S, &#8211;structured</code></dt>
<dd> make structured symbols. Version must be specified.</dd>
<dt><code>-k, &#8211;kanji</code></dt>
<dd> assume that the input text contains kanji (shift-jis).</dd>
<dt><code>-c, &#8211;casesensitive</code></dt>
<dd> encode lower-case alphabet characters in 8-bit mode. (default)</dd>
<dt><code>-i, &#8211;ignorecase</code></dt>
<dd> ignore case distinctions and use only upper-case characters.</dd>
<dt><code>-8, &#8211;8bit</code></dt>
<dd> encode entire data in 8-bit mode. -k, -c and -i will be ignored.</dd>
<dt><code>-M, &#8211;micro</code></dt>
<dd> encode in a Micro QR Code. (experimental)</dd>
<dt>
</dt><dd> <code>&#8211;foreground=RRGGBB[AA]</code></dd>
<dt>
</dt><dd> <code>&#8211;background=RRGGBB[AA]</code> specify foreground/background color in hexadecimal notation. 6-digit (RGB) or 8-digit (RGBA) form are supported. Color output support available only in PNG and SVG.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> display the version number and copyrights of the qrencode.</dd>
<dt><code>[STRING]</code></dt>
<dd> input data. If it is not specified, data will be taken from standard input. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>qrencode -l L -v 1 -o output.png &#8216;Hello, world!&#8217;</code></dt>
<dd> encode into a symbol version 1, level L.</dd>
<dt><code>qrencode -iSv 1 &#8211;output=output.png</code></dt>
<dd> read standard input and encode it into a structured-appended symbols in case-insensitive mode. </dd>
</dl>
<h2>AUTHOR</h2>
<p> Written by Kentaro Fukuchi. </p>
<h2>RESOURCES</h2>
<dl>
<dt>Main Web Site: <a rel="nofollow" href="http://fukuchi.org/works/qrencode/">http://fukuchi.org/works/qrencode/</a></dt>
<dd>
</dd><dt>Source code repository: <a rel="nofollow" href="https://github.com/fukuchi/libqrencode/">https://github.com/fukuchi/libqrencode/</a></dt>
<dd>
</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2006-2012 Kentaro Fukuchi. </p>
