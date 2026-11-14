---
title: "operon(1)"
name: "operon"
section: "1"
letter: "o"
url: "/docs/linux/man/1-operon/"
description: "operon – command line music tagger"
---

<h2>NAME</h2>
<p> operon &#8211; command line music tagger</p>
<h2>SYNOPSIS</h2>
<pre><code>
operon[--version][--help][-v | --verbose]&lt;command&gt;[&lt;argument&gt;...] operon help&lt;command&gt;
</code></pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> Print the program version</p>
<dt><code>-v</code>,<code> &#8211;verbose</code></p>
<dd> Verbose mode</dl>
<h2>COMMAND-OVERVIEW</h2>
<h3>Edit Tags</h3>
<pre>
<i>add</i>         Add a tag value
<i>remove</i>      Remove a tag value
<i>set</i>         Set a tag and remove existing values
<i>clear</i>       Remove tags
<i>copy</i>        Copy tags from one file to another
<i>dump</i>        Print all tags to stdout
</pre>
<h3>Show file metadata</h3>
<pre>
<i>list</i>        List tags
<i>info</i>        List file information
<i>print</i>       Print tags based on the given pattern
</pre>
<h3>Edit Embedded Images</h3>
<pre>
<i>image-extract</i>    Extract embedded images
<i>image-set</i>        Set embedded image
<i>image-clear</i>      Remove embedded images
</pre>
<h3>Miscellaneous</h3>
<pre>
<i>tags</i>        List all common tags
<i>help</i>        Display help information
</pre>
<h2>EDIT TAGS</h2>
<h3>add</h3>
<p> Add a new tag <code>&lt;tag&gt;</code> with the value <code>&lt;value&gt;</code> to all files. </p>
<p> operon add [-h] &lt;tag&gt; &lt;value&gt; &lt;file&gt;&#8230;</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>Example:</code></p>
<dd> operon add artist &#8216;The Beatles&#8217; song1.ogg song2.ogg</dl>
<h3>remove</h3>
<p> Remove all values from the tag <code>&lt;tag&gt;</code> that match either <code>&lt;value&gt;</code> or the regular expression <code>&lt;pattern&gt;</code> from all files. </p>
<p> operon remove [-h] [&#8211;dry-run] &lt;tag&gt; (-e &lt;pattern&gt; | &lt;value&gt;) &lt;file&gt;&#8230;</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Print the results without changing any files</p>
<dt><code>-e</code>,<i>&#8211;regexp</i><code>&nbsp;<wbr>&lt;regexp&gt;</code></p>
<dd> Remove all tag values that match the given regular expression</p>
<dt><code>Example:</code></p>
<dd> operon remove artist &#8216;The Beatles&#8217; song.ogg</dl>
<h3>set</h3>
<p> Replace all values of the tag <code>&lt;tag&gt;</code> by <code>&lt;value&gt;</code> in all files. </p>
<p> operon set [-h] [&#8211;dry-run] &lt;tag&gt; &lt;value&gt; &lt;file&gt;&#8230;</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Print the results without changing any files</p>
<dt><code>Example:</code></p>
<dd> operon set artist &#8216;The Beatles&#8217; song.ogg</dl>
<h3>clear</h3>
<p> Remove all tags that match <code>&lt;tag&gt;</code> or the regular expression <code>&lt;pattern&gt;</code> from all files. If <i>&#8211;all</i> is specified, all known tags will be removed. </p>
<p> operon clear [-h] [&#8211;dry-run] (-a | -e &lt;pattern&gt; | &lt;tag&gt;) &lt;file&gt;&#8230;</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Print the results without changing any files</p>
<dt><code>-a</code>,<code> &#8211;all</code></p>
<dd> Remove all tags</p>
<dt><code>-e</code>,<i>&#8211;regexp</i><code>&nbsp;<wbr>&lt;regexp&gt;</code></p>
<dd> Remove all tags that match the given regular expression</p>
<dt><code>Example:</code></p>
<dd> operon clear -a song.ogg </p>
<p> operon clear -e &#8216;musicbrainz_.*&#8217; song.ogg </p>
<p> operon clear date song.ogg</dl>
<h3>copy</h3>
<p> Copy all tags from the file <i>&lt;source&gt;</i> to <i>&lt;dest&gt;</i>. All tags in <code>&lt;dest&gt;</code> will be preserved. In case the destination format doesn&#8217;t support setting a tag from source, no tags will be copied. To ignore tags that aren&#8217;t supported by the destination format pass <i>&#8211;ignore-errors</i>. </p>
<p> operon copy [-h] [&#8211;dry-run] [&#8211;ignore-errors] &lt;source&gt; &lt;dest&gt;</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Print the results without changing any files</p>
<dt><code>&#8211;ignore-errors</code></p>
<dd> Skip tags which the target file does not support</p>
<dt><code>Example:</code></p>
<dd> operon copy song.flac song.ogg</dl>
<h3>dump</h3>
<p> Print all tags to stdout. The format is not specified. The data can be loaded again using <i>operon load</i>, given the same version was used to create the data. </p>
<p> operon dump [-h] &lt;src-file&gt;</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>Example:</code></p>
<dd> operon dump song.flac &gt; backup.tags</dl>
<h2>SHOW FILE METADATA</h2>
<h3>list</h3>
<p> Lists all tags, values and a description of each tag in a table. </p>
<p> operon list [-h] [-a] [-t] [-c &lt;c1&gt;,&lt;c2&gt;&#8230;] &lt;file&gt;</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>-a</code>,<code> &#8211;all</code></p>
<dd> Also list programmatic tags</p>
<dt><code>-t</code>,<code> &#8211;terse</code></p>
<dd> Output is terse and suitable for script processing</p>
<dt><code>-c, &#8211;columns &lt;name&gt;,&#8230;</code></p>
<dd> Defines which columns should be printed and in which order</p>
<dt><code>Example:</code></p>
<dd> operon list -a song.flac </p>
<p> operon list -t -c tag,value song.ogg</dl>
<h3>info</h3>
<p> Lists non-tag metadata like length, size and format. </p>
<p> operon info [-h] [-t] [-c &lt;c1&gt;,&lt;c2&gt;&#8230;] &lt;file&gt;</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>-t</code>,<code> &#8211;terse</code></p>
<dd> Output is terse and suitable for script processing</p>
<dt><code>-c, &#8211;columns &lt;name&gt;,&#8230;</code></p>
<dd> Defines which columns should be printed and in which order</p>
<dt><code>Example:</code></p>
<dd> operon info a.ogg</dl>
<h3>print</h3>
<p> Prints information per file built from tag values. The pattern can be customized by passing a pattern string (See <code><a href="/docs/linux/man/1-quodlibet/">quodlibet</a></code>(1) for the pattern format) </p>
<p> operon print [-h] [-p &lt;pattern&gt;] &lt;file&gt;&#8230;</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>-p</code>,<i>&#8211;pattern</i><code>&nbsp;<wbr>&lt;pattern&gt;</code></p>
<dd> Use a custom pattern</p>
<dt><code>Example:</code></p>
<dd> operon print -p &quot;&lt;album&gt; &#8211; &lt;artist&gt;&quot; a.ogg</dl>
<h2>EDIT EMBEDDED IMAGES</h2>
<h3>image-extract</h3>
<p> Extract all embedded images to the current working directory or the specified destination directory. </p>
<p> operon image-extract [-h] [&#8211;dry-run] [&#8211;primary] [-d &lt;destination&gt;] &lt;file&gt;&#8230;</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Print the found images and resulting file paths but don&#8217;t save them</p>
<dt><code>&#8211;primary</code></p>
<dd> Only extract the primary images for each file</p>
<dt><code>-d</code>,<i>&#8211;destination</i><code>&nbsp;<wbr>&lt;destination&gt;</code></p>
<dd> Save all images to the specified destination</p>
<dt><code>Example:</code></p>
<dd> operon image-extract asong.mp3 anotherone.ogg</dl>
<h3>image-set</h3>
<p> Set the provided image as primary embedded image and remove all other embedded images. </p>
<p> operon image-set &lt;image-file&gt; &lt;file&gt;&#8230;</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>Example:</code></p>
<dd> operon image-set cover.jpg song.mp3</dl>
<h3>image-clear</h3>
<p> Remove all embedded images from all specified files. </p>
<p> operon image-clear &lt;file&gt;&#8230;</p>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Display help and exit</p>
<dt><code>Example:</code></p>
<dd> operon image-clear song.mp3</dl>
<h2>COMMANDS</h2>
<h3>help</h3>
<p> operon help [&lt;command&gt;]</p>
<dl>
<dt><code>Example:</code></p>
<dd> operon help list</dl>
<h2>SEE ALSO</h2>
<pre>
<code><a href="//www.systutorials.com/docs/linux/man/7-regex/">regex</a></code>(7)
<code><a href="//www.systutorials.com/docs/linux/man/1-exfalso/">exfalso</a></code>(1)
<code><a href="//www.systutorials.com/docs/linux/man/1-quodlibet/">quodlibet</a></code>(1)
</pre>
<h2>Index</h2>
