---
title: "mecab(1)"
name: "mecab"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mecab/"
description: "mecab – manual page for mecab of 0.98pre1"
---

<h2>NAME</h2>
<p> mecab &#8211; manual page for mecab of 0.98pre1</p>
<h2>SYNOPSIS</h2>
<p> <code>mecab</code> [<i>options</i>] <i>files</i></p>
<h2>DESCRIPTION</h2>
<p> MeCab: Yet Another Part-of-Speech and Morphological Analyzer </p>
<p> Copyright(C) 2001-2008 Taku Kudo Copyright(C) 2004-2008 Nippon Telegraph and Telephone Corporation</p>
<dl>
<dt><code>-r</code>, <code>&#8211;rcfile</code>=<i>FILE</i></p>
<dd> use FILE as resource file</p>
<dt><code>-d</code>, <code>&#8211;dicdir</code>=<i>DIR</i></p>
<dd> set DIR as a system dicdir</p>
<dt><code>-u</code>, <code>&#8211;userdic</code>=<i>FILE</i></p>
<dd> use FILE as a user dictionary</p>
<dt><code>-l</code>, <code>&#8211;lattice-level</code>=<i>INT</i></p>
<dd> lattice information level (default 0)</p>
<dt><code>-D</code>, <code>&#8211;dictionary-info</code></p>
<dd> show dictionary information and exit</p>
<dt><code>-a</code>, <code>&#8211;all-morphs</code></p>
<dd> output all morphs(default false)</p>
<dt><code>-O</code>, <code>&#8211;output-format-type</code>=<i>TYPE</i></p>
<dd> set output format type (wakati,none,&#8230;)</p>
<dt><code>-p</code>, <code>&#8211;partial</code></p>
<dd> partial parsing mode</p>
<dt><code>-F</code>, <code>&#8211;node-format</code>=<i>STR</i></p>
<dd> use STR as the user-defined node format</p>
<dt><code>-U</code>, <code>&#8211;unk-format</code>=<i>STR</i></p>
<dd> use STR as the user-defined unk format</p>
<dt><code>-B</code>, <code>&#8211;bos-format</code>=<i>STR</i></p>
<dd> use STR as the user-defined bos format</p>
<dt><code>-E</code>, <code>&#8211;eos-format</code>=<i>STR</i></p>
<dd> use STR as the user-defined eos format</p>
<dt><code>-x</code>, <code>&#8211;unk-feature</code>=<i>STR</i></p>
<dd> use STR as the feature for unknown word</p>
<dt><code>-b</code>, <code>&#8211;input-buffer-size</code>=<i>INT</i></p>
<dd> set input buffer size (default 8192)</p>
<dt><code>-P</code>, <code>&#8211;dump-config</code></p>
<dd> dump MeCab parameters</p>
<dt><code>-M</code>, <code>&#8211;open-mutable-dictionary</code></p>
<dd> open dictioanry with mutable mode (experimental)</p>
<dt><code>-C</code>, <code>&#8211;allocate-sentence</code></p>
<dd> allocate new memory for input sentence</p>
<dt><code>-N</code>, <code>&#8211;nbest</code>=<i>INT</i></p>
<dd> output N best results (default 1)</p>
<dt><code>-t</code>, <code>&#8211;theta</code>=<i>FLOAT</i></p>
<dd> set temparature parameter theta (default 0.75)</p>
<dt><code>-c</code>, <code>&#8211;cost-factor</code>=<i>INT</i></p>
<dd> set cost factor (default 700)</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></p>
<dd> set the output file name</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> show the version and exit.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help and exit. </p>
</dl>
<h2>Index</h2>
