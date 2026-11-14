---
title: "voikkohyphenate(1)"
name: "voikkohyphenate"
section: "1"
letter: "v"
url: "/docs/linux/man/1-voikkohyphenate/"
description: "voikkohyphenate – test program for Voikko hyphenator"
---

<h2>NAME</h2>
<p> voikkohyphenate &#8211; test program for Voikko hyphenator</p>
<h2>SYNOPSIS</h2>
<p> <code>voikkohyphenate</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>voikkohyphenate</code> is a test program for hyphenator functionality in libvoikko, library of Finnish language tools. It reads words from stdin (one word on a line) and prints them stdout in fully hyphenated form.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code><i>c</i></p>
<dd> Use <i>c</i> to separate syllables. By default &#8211; is used. If separator is set to a character other than -, all original characters of the hyphenated word are printed.</p>
<dt><code>min_hyphenated_word_length=</code><i>n</i></p>
<dd> Set <i>n</i> as the minimun length for words to hyphenate.</p>
<dt><code>no_ugly_hyphenation=</code><i>n</i></p>
<dd>
<dt><code>hyphenate_unknown_words=</code><i>n</i></p>
<dd> Set the value of the specified boolean option. <i>n</i> can be either 0 (false) or 1 (true).</dl>
<h2>SEE ALSO</h2>
<p> <code>voikkospell</code> for common options of different Voikko test tools.</p>
<h2>AUTHOR</h2>
<p> voikkohyphenate and this manual page were written by Harri Pitk&auml;nen (hatapitk [at] iki.fi). </p>
<h2>Index</h2>
