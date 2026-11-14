---
title: "convmv(1)"
name: "convmv"
section: "1"
letter: "c"
url: "/docs/linux/man/1-convmv/"
description: "convmv – converts filenames from one encoding to another"
---

<h2 class="name">NAME</h2>
<p> convmv &#8211; converts filenames from one encoding to another </p>
<h2>SYNOPSIS</h2>
<p> <code>convmv</code> [<code>options</code>] <font SIZE="-1">FILE</font>(S) &#8230; <font SIZE="-1">DIRECTORY</font>(S)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f </code><font SIZE="-1"><code>ENCODING</code></font></p>
<dd> specify the current encoding of the filename(s) from which should be converted</p>
<dt><code>-t </code><font SIZE="-1"><code>ENCODING</code></font></p>
<dd> specify the encoding to which the filename(s) should be converted</p>
<dt><code>-i</code></p>
<dd> interactive mode (ask y/n for each action)</p>
<dt><code>-r</code></p>
<dd> recursively go through directories</p>
<dt><code>&#8211;nfc</code></p>
<dd> target files will be normalization form C for <font SIZE="-1">UTF-8 </font>(Linux etc.)</p>
<dt><code>&#8211;nfd</code></p>
<dd> target files will be normalization form D for <font SIZE="-1">UTF-8 </font>(<font SIZE="-1">OS X</font> etc.).</p>
<dt><code>&#8211;qfrom</code> , <code>&#8211;qto</code></p>
<dd> be more quiet about the &#8220;from&#8221; or &#8220;to&#8221; of a rename (if it screws up your terminal e.g.). This will in fact do nothing else than replace any non-ASCII character (bytewise) with ? and any control character with * on printout, this does not affect rename operation itself.</p>
<dt><code>&#8211;exec</code> command</p>
<dd> execute the given command. You have to quote the command and #1 will be substituted by the old, #2 by the new filename. Using this option link targets will stay untouched. </p>
<p> Example: </p>
<p> convmv -f latin1 -t utf-8 -r &#8211;exec &#8220;echo #1 should be renamed to #2&#8221; path/to/files</p>
<dt><code>&#8211;list</code></p>
<dd> list all available encodings. To get support for more Chinese or Japanese encodings install the Perl HanExtra or <font SIZE="-1">JIS2K</font> Encode packages.</p>
<dt><code>&#8211;lowmem</code></p>
<dd> keep memory footprint low by not creating a hash of all files. This disables checking if symlink targets are in subtree. Symlink target pointers will be converted regardlessly. If you convert multiple hundredthousands or millions of files the memory usage of convmv might grow quite high. This option would help you out in that case.</p>
<dt><code>&#8211;nosmart</code></p>
<dd> by default convmv will detect if a filename is already <font SIZE="-1">UTF8</font> encoded and will skip this file if conversion from some charset to <font SIZE="-1">UTF8</font> should be performed. <tt>&quot;--nosmart&quot;</tt> will also force conversion to <font SIZE="-1">UTF-8</font> for such files, which might result in &#8220;double encoded <font SIZE="-1">UTF-8&#8221; </font>(see section below).</p>
<dt><code>&#8211;fixdouble</code></p>
<dd> using the <tt>&quot;--fixdouble&quot;</tt> option convmv does only convert files which will still be <font SIZE="-1">UTF-8</font> encoded after conversion. That&#8217;s useful for fixing double-encoded <font SIZE="-1">UTF-8</font> files. All files which are not <font SIZE="-1">UTF-8</font> or will not result in <font SIZE="-1">UTF-8</font> after conversion will not be touched. Also see chapter &#8220;How to undo double <font SIZE="-1">UTF-8 &#8230;&#8221;</font> below.</p>
<dt><code>&#8211;notest</code></p>
<dd> Needed to actually rename the files. By default convmv will just print what it wants to do.</p>
<dt><code>&#8211;parsable</code></p>
<dd> This is an advanced option that people who want to write a <font SIZE="-1">GUI</font> front end will find useful (some others maybe, too). It will convmv make print out what it would do in an easy parsable way. The first column contains the action or some kind of information, the second column mostly contains the file that is to be modified and if appropriate the third column contains the modified value. Each column is separated by 
