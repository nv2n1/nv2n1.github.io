---
title: "mknmz(1)"
name: "mknmz"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mknmz/"
description: "mknmz – an indexer of Namazu"
---

<h2>NAME</h2>
<p> mknmz &#8211; an indexer of Namazu</p>
<h2>SYNOPSIS</h2>
<p> <code>mknmz</code> [<i>options</i>] <i>&lt;target&gt;</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> mknmz 2.0.19, an indexer of Namazu.</p>
<h3>Target files:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> target all files.</p>
<dt><code>-t</code>, <code>&#8211;media-type</code>=<i>MTYPE</i></p>
<dd> set the media type for all target files to MTYPE.</p>
<dt><code>-h</code>, <code>&#8211;mailnews</code></p>
<dd> same as <code>&#8211;media-type=</code>&#8216;message/rfc822&#8217;</p>
<dt><code>&#8211;mhonarc</code></p>
<dd> same as <code>&#8211;media-type=</code>&#8216;text/html; x-type=mhonarc&#8217;</p>
<dt><code>-F</code>, <code>&#8211;target-list</code>=<i>FILE</i></p>
<dd> load FILE which contains a list of target files.</p>
<dt><code>&#8211;allow</code>=<i>PATTERN</i></p>
<dd> set PATTERN for file names which should be allowed.</p>
<dt><code>&#8211;deny</code>=<i>PATTERN</i></p>
<dd> set PATTERN for file names which should be denied.</p>
<dt><code>&#8211;exclude</code>=<i>PATTERN</i></p>
<dd> set PATTERN for pathnames which should be excluded.</p>
<dt><code>-e</code>, <code>&#8211;robots</code></p>
<dd> exclude HTML files containing &lt;meta name=&quot;ROBOTS&quot; content=&quot;NOINDEX&quot;&gt;</p>
<dt><code>-M</code>, <code>&#8211;meta</code></p>
<dd> handle HTML meta tags for field-specified search.</p>
<dt><code>-r</code>, <code>&#8211;replace</code>=<i>CODE</i></p>
<dd> set CODE for replacing URI.</p>
<dt><code>&#8211;html-split</code></p>
<dd> split an HTML file with &lt;a name=&quot;&#8230;&quot;&gt; anchors.</p>
<dt><code>&#8211;mtime</code>=<i>NUM</i></p>
<dd> limit by mtime just like <a href="/docs/linux/man/1-find/">find</a>(1)&#8217;s <code>-mtime</code> option. e.g., <code>-50</code> for recent 50 days, +50 for older than 50.</dl>
<h3>Morphological Analysis:</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;use-mecab</code></p>
<dd> use MeCab for analyzing Japanese.</p>
<dt><code>-c</code>, <code>&#8211;use-chasen</code></p>
<dd> use ChaSen for analyzing Japanese.</p>
<dt><code>-k</code>, <code>&#8211;use-kakasi</code></p>
<dd> use KAKASI for analyzing Japanese.</p>
<dt><code>-m</code>, <code>&#8211;use-chasen-noun</code></p>
<dd> use ChaSen for extracting only nouns.</p>
<dt> <code>-L</code>, <code>&#8211;indexing-lang</code>=<i>LANG</i> index with language specific processing.</dl>
<h3>Text Operations:</h3>
<dl>
<dt><code>-E</code>, <code>&#8211;no-edge-symbol</code></p>
<dd>
<dd>remove symbols on edge of word.</p>
<dt><code>-G</code>, <code>&#8211;no-okurigana</code></p>
<dd> remove Okurigana in word.</p>
<dt><code>-H</code>, <code>&#8211;no-hiragana</code></p>
<dd> ignore words consist of Hiragana only.</p>
<dt><code>-K</code>, <code>&#8211;no-symbol</code></p>
<dd> remove symbols.</p>
<dt><code>&#8211;decode-base64</code></p>
<dd> decode base64 bodies within multipart entities.</dl>
<h3>Summarization:</h3>
<dl>
<dt><code>-U</code>, <code>&#8211;no-encode-uri</code></p>
<dd> do not encode URI.</p>
<dt> <code>-x</code>, <code>&#8211;no-heading-summary</code> do not make summary with HTML&#8217;s headings.</dl>
<h3>Index Construction:</h3>
<dl>
<dt><code>&#8211;update</code>=<i>INDEX</i></p>
<dd>
<dd>set INDEX for updating.</p>
<dt><code>-z</code>, <code>&#8211;check-filesize</code></p>
<dd> detect file size changed.</p>
<dt><code>-Y</code>, <code>&#8211;no-delete</code></p>
<dd> do not detect removed documents.</p>
<dt><code>-Z</code>, <code>&#8211;no-update</code></p>
<dd> do not detect update and deleted documents.</dl>
<h3>Miscellaneous:</h3>
<dl>
<dt><code>-s</code>, <code>&#8211;checkpoint</code></p>
<dd> turn on the checkpoint mechanism.</p>
<dt><code>-C</code>, <code>&#8211;show-config</code></p>
<dd> show the current configuration.</p>
<dt><code>-f</code>, <code>&#8211;config</code>=<i>FILE</i></p>
<dd> use FILE as a config file.</p>
<dt><code>-I</code>, <code>&#8211;include</code>=<i>FILE</i></p>
<dd> include your customization FILE.</p>
<dt><code>-O</code>, <code>&#8211;output-dir</code>=<i>DIR</i></p>
<dd> set DIR to output the index.</p>
<dt><code>-T</code>, <code>&#8211;template-dir</code>=<i>DIR</i></p>
<dd> set DIR having NMZ.{head,foot,body}.*.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> suppress status messages during execution.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> show the version of namazu and exit.</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd> be verbose.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd> be debug mode.</p>
<dt><code>&#8211;help</code></p>
<dd> show this help and exit.</p>
<dt><code>&#8211;norc</code></p>
<dd> do not read the personal initialization files.</p>
<dt><code>&#8212;</code></p>
<dd> Terminate option list.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://www.namazu.org/trac-namazu/trac.cgi">http://www.namazu.org/trac-namazu/trac.cgi</a>&gt; or &lt;bug-namazu [at] namazu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997-1999 Satoru Takabayashi All rights reserved.<br />
 Copyright &#169; 2000-2009 Namazu Project All rights reserved. </p>
<p> This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>Index</h2>
