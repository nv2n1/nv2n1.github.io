---

title: "mecab(1)"
name: "mecab"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mecab/"
description: "mecab – manual page for mecab of 0.98pre1"
---

<p> mecab &#8211; manual page for mecab of 0.98pre1</p>
<h2>SYNOPSIS</h2>
<p> <code>mecab</code> [<i>options</i>] <i>files</i></p>
<h2>DESCRIPTION</h2>
<p> MeCab: Yet Another Part-of-Speech and Morphological Analyzer </p>
<p> Copyright(C) 2001-2008 Taku Kudo Copyright(C) 2004-2008 Nippon Telegraph and Telephone Corporation</p>
<dl>
<dt><code>-r</code>, <code>&#8211;rcfile</code>=<i>FILE</i></dt>
<dd> use FILE as resource file</dd>
<dt><code>-d</code>, <code>&#8211;dicdir</code>=<i>DIR</i></dt>
<dd> set DIR as a system dicdir</dd>
<dt><code>-u</code>, <code>&#8211;userdic</code>=<i>FILE</i></dt>
<dd> use FILE as a user dictionary</dd>
<dt><code>-l</code>, <code>&#8211;lattice-level</code>=<i>INT</i></dt>
<dd> lattice information level (default 0)</dd>
<dt><code>-D</code>, <code>&#8211;dictionary-info</code></dt>
<dd> show dictionary information and exit</dd>
<dt><code>-a</code>, <code>&#8211;all-morphs</code></dt>
<dd> output all morphs(default false)</dd>
<dt><code>-O</code>, <code>&#8211;output-format-type</code>=<i>TYPE</i></dt>
<dd> set output format type (wakati,none,&#8230;)</dd>
<dt><code>-p</code>, <code>&#8211;partial</code></dt>
<dd> partial parsing mode</dd>
<dt><code>-F</code>, <code>&#8211;node-format</code>=<i>STR</i></dt>
<dd> use STR as the user-defined node format</dd>
<dt><code>-U</code>, <code>&#8211;unk-format</code>=<i>STR</i></dt>
<dd> use STR as the user-defined unk format</dd>
<dt><code>-B</code>, <code>&#8211;bos-format</code>=<i>STR</i></dt>
<dd> use STR as the user-defined bos format</dd>
<dt><code>-E</code>, <code>&#8211;eos-format</code>=<i>STR</i></dt>
<dd> use STR as the user-defined eos format</dd>
<dt><code>-x</code>, <code>&#8211;unk-feature</code>=<i>STR</i></dt>
<dd> use STR as the feature for unknown word</dd>
<dt><code>-b</code>, <code>&#8211;input-buffer-size</code>=<i>INT</i></dt>
<dd> set input buffer size (default 8192)</dd>
<dt><code>-P</code>, <code>&#8211;dump-config</code></dt>
<dd> dump MeCab parameters</dd>
<dt><code>-M</code>, <code>&#8211;open-mutable-dictionary</code></dt>
<dd> open dictioanry with mutable mode (experimental)</dd>
<dt><code>-C</code>, <code>&#8211;allocate-sentence</code></dt>
<dd> allocate new memory for input sentence</dd>
<dt><code>-N</code>, <code>&#8211;nbest</code>=<i>INT</i></dt>
<dd> output N best results (default 1)</dd>
<dt><code>-t</code>, <code>&#8211;theta</code>=<i>FLOAT</i></dt>
<dd> set temparature parameter theta (default 0.75)</dd>
<dt><code>-c</code>, <code>&#8211;cost-factor</code>=<i>INT</i></dt>
<dd> set cost factor (default 700)</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>FILE</i></dt>
<dd> set the output file name</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> show the version and exit.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help and exit. </dd>
</dl>
