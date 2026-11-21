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
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> target all files.</dd>
<dt><code>-t</code>, <code>&#8211;media-type</code>=<i>MTYPE</i></dt>
<dd> set the media type for all target files to MTYPE.</dd>
<dt><code>-h</code>, <code>&#8211;mailnews</code></dt>
<dd> same as <code>&#8211;media-type=</code>&#8216;message/rfc822&#8217;</dd>
<dt><code>&#8211;mhonarc</code></dt>
<dd> same as <code>&#8211;media-type=</code>&#8216;text/html; x-type=mhonarc&#8217;</dd>
<dt><code>-F</code>, <code>&#8211;target-list</code>=<i>FILE</i></dt>
<dd> load FILE which contains a list of target files.</dd>
<dt><code>&#8211;allow</code>=<i>PATTERN</i></dt>
<dd> set PATTERN for file names which should be allowed.</dd>
<dt><code>&#8211;deny</code>=<i>PATTERN</i></dt>
<dd> set PATTERN for file names which should be denied.</dd>
<dt><code>&#8211;exclude</code>=<i>PATTERN</i></dt>
<dd> set PATTERN for pathnames which should be excluded.</dd>
<dt><code>-e</code>, <code>&#8211;robots</code></dt>
<dd> exclude HTML files containing &lt;meta name=&quot;ROBOTS&quot; content=&quot;NOINDEX&quot;&gt;</dd>
<dt><code>-M</code>, <code>&#8211;meta</code></dt>
<dd> handle HTML meta tags for field-specified search.</dd>
<dt><code>-r</code>, <code>&#8211;replace</code>=<i>CODE</i></dt>
<dd> set CODE for replacing URI.</dd>
<dt><code>&#8211;html-split</code></dt>
<dd> split an HTML file with &lt;a name=&quot;&#8230;&quot;&gt; anchors.</dd>
<dt><code>&#8211;mtime</code>=<i>NUM</i></dt>
<dd> limit by mtime just like <a href="/docs/linux/man/1-find/">find</a>(1)&#8217;s <code>-mtime</code> option. e.g., <code>-50</code> for recent 50 days, +50 for older than 50.</dd></dl>
<h3>Morphological Analysis:</h3>
<dl>
<dt><code>-b</code>, <code>&#8211;use-mecab</code></dt>
<dd> use MeCab for analyzing Japanese.</dd>
<dt><code>-c</code>, <code>&#8211;use-chasen</code></dt>
<dd> use ChaSen for analyzing Japanese.</dd>
<dt><code>-k</code>, <code>&#8211;use-kakasi</code></dt>
<dd> use KAKASI for analyzing Japanese.</dd>
<dt><code>-m</code>, <code>&#8211;use-chasen-noun</code></dt>
<dd> use ChaSen for extracting only nouns.</dd>
<dt> <code>-L</code>, <code>&#8211;indexing-lang</code>=<i>LANG</i> index with language specific processing.</dt></dl>
<h3>Text Operations:</h3>
<dl>
<dt><code>-E</code>, <code>&#8211;no-edge-symbol</code></dt>
<dd>
</dd><dd>remove symbols on edge of word.</dd>
<dt><code>-G</code>, <code>&#8211;no-okurigana</code></dt>
<dd> remove Okurigana in word.</dd>
<dt><code>-H</code>, <code>&#8211;no-hiragana</code></dt>
<dd> ignore words consist of Hiragana only.</dd>
<dt><code>-K</code>, <code>&#8211;no-symbol</code></dt>
<dd> remove symbols.</dd>
<dt><code>&#8211;decode-base64</code></dt>
<dd> decode base64 bodies within multipart entities.</dd></dl>
<h3>Summarization:</h3>
<dl>
<dt><code>-U</code>, <code>&#8211;no-encode-uri</code></dt>
<dd> do not encode URI.</dd>
<dt> <code>-x</code>, <code>&#8211;no-heading-summary</code> do not make summary with HTML&#8217;s headings.</dt></dl>
<h3>Index Construction:</h3>
<dl>
<dt><code>&#8211;update</code>=<i>INDEX</i></dt>
<dd>
</dd><dd>set INDEX for updating.</dd>
<dt><code>-z</code>, <code>&#8211;check-filesize</code></dt>
<dd> detect file size changed.</dd>
<dt><code>-Y</code>, <code>&#8211;no-delete</code></dt>
<dd> do not detect removed documents.</dd>
<dt><code>-Z</code>, <code>&#8211;no-update</code></dt>
<dd> do not detect update and deleted documents.</dd></dl>
<h3>Miscellaneous:</h3>
<dl>
<dt><code>-s</code>, <code>&#8211;checkpoint</code></dt>
<dd> turn on the checkpoint mechanism.</dd>
<dt><code>-C</code>, <code>&#8211;show-config</code></dt>
<dd> show the current configuration.</dd>
<dt><code>-f</code>, <code>&#8211;config</code>=<i>FILE</i></dt>
<dd> use FILE as a config file.</dd>
<dt><code>-I</code>, <code>&#8211;include</code>=<i>FILE</i></dt>
<dd> include your customization FILE.</dd>
<dt><code>-O</code>, <code>&#8211;output-dir</code>=<i>DIR</i></dt>
<dd> set DIR to output the index.</dd>
<dt><code>-T</code>, <code>&#8211;template-dir</code>=<i>DIR</i></dt>
<dd> set DIR having NMZ.{head,foot,body}.*.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> suppress status messages during execution.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> show the version of namazu and exit.</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd> be verbose.</dd>
<dt><code>-d</code>, <code>&#8211;debug</code></dt>
<dd> be debug mode.</dd>
<dt><code>&#8211;help</code></dt>
<dd> show this help and exit.</dd>
<dt><code>&#8211;norc</code></dt>
<dd> do not read the personal initialization files.</dd>
<dt><code>&#8212;</code></dt>
<dd> Terminate option list.</dd></dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://www.namazu.org/trac-namazu/trac.cgi">http://www.namazu.org/trac-namazu/trac.cgi</a>&gt; or &lt;bug-namazu [at] namazu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997-1999 Satoru Takabayashi All rights reserved.<br />
 Copyright &#169; 2000-2009 Namazu Project All rights reserved. </p>
<p> This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
