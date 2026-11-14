---
title: "racoon2-pskgen(8)"
name: "racoon2-pskgen"
section: "8"
letter: "r"
url: "/docs/linux/man/8-racoon2-pskgen/"
description: "pskgen – Pre-shared key generater and converter for IKE"
---

<p><code>pskgen</code> &#8211; Pre-shared key generater and converter for IKE</p>
<h2>Synopsis</h2>
<p><code>pskgen</code> &#8211;<code>r</code> [-<code>s </code><i>length</i> ] [-<code>o </code><i>file</i> ] [-<code>d</code> ]<br />
<code>pskgen</code> &#8211;<code>i </code><i>file</i> [-<code>h</code> ] [-<code>o </code><i>file</i> ] [-<code>d</code> ]<br />
<code>pskgen</code> &#8211;<code>e </code><i>file</i> [-<code>o </code><i>file</i> ] [-<code>d</code> ]</p>
<h2>Description</h2>
<p><code>pskgen</code> creates a pre-share key file for the iked of the Racoon2 system. There are three modes. The first is that it will create a randomized key. The second is that it will create the key from the input file. Note that the Racoon2 only uses the first line of the input file that is plain text format except the case when the &#8211;<code>h</code> option is not specified. <code>pskgen</code> ignores the second line of the file specified and more than that. The third is that it will convert the key file to the format of the &#8211;<code>h</code> option.</p>
<h3>Randomized key mode</h3>
<dl>
<dt><code>-r</code></p>
<dd>output random bytes.</p>
<dt><code>-s</code></p>
<dd>specify the byte length of the key. the default is $default_keysize bytes.</p>
<dt><code>-o</code></p>
<dd>specify the output file.</p>
<dt><code>-d</code></p>
<dd>debug mode. no harm to any file.</dl>
<h3>File specific mode</h3>
<dl>
<dt><code>-i</code></p>
<dd>specify the input file. `-&#8216; means the standard input.</p>
<dt><code>-h</code></p>
<dd>assumed that the input file is writted by the following syntax: 0x leading one or two of hexadecimal number separated space characters. For example: </p>
<blockquote><p><tt>0x72 0x61 0x63 0x6f 0x6f 0x6e</tt></p></blockquote>
<dt><code>-o</code></p>
<dd>specify the output file.</p>
<dt><code>-d</code></p>
<dd>debug mode. no harm to any file.</dl>
<h3>Export Mode</h3>
<dl>
<dt><code>-e</code></p>
<dd>export the key file. the format is like the option &#8211;<code>h</code> defined.</p>
<dt><code>-o</code></p>
<dd>specify the output file.</p>
<dt><code>-d</code></p>
<dd>debug mode. no harm to any file.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-racoon2/">racoon2</a>(7), racoon2.conf5, <a href="/docs/linux/man/8-iked/">iked</a>(8) </p>
