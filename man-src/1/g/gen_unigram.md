---

title: "gen_unigram(1)"
name: "gen_unigram"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gen_unigram/"
description: "libpinyin – Library to deal with pinyin"
---

<p> The libpinyin project aims to provide the algorithms core for intelligent sentence-based Chinese pinyin input methods. </p>
<h2>TOOLS</h2>
<p> gen_binary_files &#8211; generate initially binary pinyin libraries import_interpolation &#8211; import libpinyin textual format model data gen_unigram &#8211; increase the unigram frequency for all phrases </p>
<h2>USAGE</h2>
<dl>
<dt>
</dt><dd>gen_binary_files &#8211;table-dir &lt;DIRNAME&gt;</dd>
<dl>
<dl>
<dt> <code>&#8211;table-dir</code></dt>
<dd>Read textual format files from the &lt;DIRNAME&gt; directory.</dd></dl>
</dl>
<dt>
</dt><dd>import_interpolation &lt; &lt;MODELFILE&gt;</dd>
<dt>
</dt><dd>gen_unigram </dd>
</dl>
<h2>EXAMPLE</h2>
<p> Download the model.text.tar.gz, and extracts all files into a folder, then run the commands below to generate the binary model data. </p>
<dl>
<dt>
</dt><dd> rm gb_char.bin gbk_char.bin phrase_index.bin pinyin_index.bin bigram.db </dd>
<p> gen_binary_files &#8211;table-dir ../data </p>
<p> import_interpolation &lt; ../data/interpolation.text </p>
<p> gen_unigram</dl>
