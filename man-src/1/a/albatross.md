---
title: "albatross(1)"
name: "albatross"
section: "1"
letter: "a"
url: "/docs/linux/man/1-albatross/"
description: "albatross – a tool for finding fonts that contain a given (Unicode) glyph."
---

<h2>SYNOPSIS</h2>
<p> <code>albatross</code> [<i>options</i>] <i>glyphs</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>albatross</code> is a command line tool for finding fonts that contain a given (Unicode) glyph. It relies on Fontconfig, a library for configuring and customizing font access. </p>
<p> Albatross takes a list of glyphs as input. Three formats are supported:</p>
<dl>
<dt>#1</dt>
<dd> The glyph itself, e.g., <code>ß</code> (Eszett). Internally, the tool converts it to the corresponding Unicode code point.</dd>
<dt>#2</dt>
<dd> The glyph as a Unicode code point in the hexadecimal notation, e.g., <code>0xDF</code>. The <code>0x</code> prefix is mandatory. Note that the tool takes the value as case insensitive, e.g., <code>0xDF</code> is equal to <code>0xdf</code> (or any case combination thereof).</dd>
<dt>#3</dt>
<dd> The glyph as a Unicode code point using the multiset union notation, e.g, <code>U+DF</code>. The <code>U+</code> prefix is mandatory. Be mindful that this notation expects an uppercase <code>U</code>.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;show-styles</code></dt>
<dd> Show available font styles</dd>
<dt><code>&#8211;detailed</code></dt>
<dd> Show a detailed font list</dd>
<dt><code>&#8211;ansi-level</code> [n|a16|a256|tc]</dt>
<dd> Set the default ANSI level</dd>
<dt><code>&#8211;border-style</code> [1|2|3|4|5|6]</dt>
<dd> Set the border style</dd>
<dt><code>&#8211;or</code></dt>
<dd> Look for each glyph separately</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show the version and exit</dd>
<dt><code>&#8211;help</code></dt>
<dd> Show a help message and exit</dd></dl>
<h2>BUGS</h2>
<p> Issue tracker at </p>
