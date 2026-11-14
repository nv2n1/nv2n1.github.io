---
title: "gen_binary_files(1)"
name: "gen_binary_files"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gen_binary_files/"
description: "libpinyin – Library to deal with pinyin"
---

<h2 class="name">NAME</h2>
<p> libpinyin &#8211; Library to deal with pinyin</p>
<h2>DESCRIPTION</h2>
<p> The libpinyin project aims to provide the algorithms core for intelligent sentence-based Chinese pinyin input methods. </p>
<h2>TOOLS</h2>
<p> gen_binary_files &#8211; generate initially binary pinyin libraries import_interpolation &#8211; import libpinyin textual format model data gen_unigram &#8211; increase the unigram frequency for all phrases </p>
<h2>USAGE</h2>
<dl>
<dt>
<dd>gen_binary_files &#8211;table-dir &lt;DIRNAME&gt;</p>
<dl>
<dt>
<dd>
<dl>
<dt> <code>&#8211;table-dir</code></p>
<dd>Read textual format files from the &lt;DIRNAME&gt; directory.</dl>
</dl>
<dt>
<dd>import_interpolation &lt; &lt;MODELFILE&gt;</p>
<dt>
<dd>gen_unigram </p>
</dl>
<h2>EXAMPLE</h2>
<p> Download the model.text.tar.gz, and extracts all files into a folder, then run the commands below to generate the binary model data. </p>
<dl>
<dt>
<dd> rm gb_char.bin gbk_char.bin phrase_index.bin pinyin_index.bin bigram.db </p>
<p> gen_binary_files &#8211;table-dir ../data </p>
<p> import_interpolation &lt; ../data/interpolation.text </p>
<p> gen_unigram</dl>
<h2>Index</h2>
