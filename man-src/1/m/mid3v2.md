---
title: "mid3v2(1)"
name: "mid3v2"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mid3v2/"
description: "mid3v2 – audio tag editor similar to ‘id3v2’"
---

<h2>NAME</h2>
<p> mid3v2 &#8211; audio tag editor similar to &#8216;id3v2&#8217;</p>
<h2>SYNOPSIS</h2>
<p> <code>mid3v2</code> [<i>options</i>] <i>filename</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>mid3v2</code> is a Mutagen-based replacement for id3lib&#8217;s id3v2. It supports ID3v2.4 and more frames; it also does not have the numerous bugs that plague id3v2. </p>
<p> This program exists mostly for compatibility with programs that want to tag files using id3v2. For a more usable interface, we recommend Ex Falso.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q</code>,<code> &#8211;quiet</code></p>
<dd> Be quiet: do not mention file operations that perform the user&#8217;s request. Warnings will still be printed.</p>
<dt><code>-v</code>,<code> &#8211;verbose</code></p>
<dd> Be verbose: state all operations performed. This is the opposite of &#8211;quiet. This is the default.</p>
<dt><code>-e</code>,<code> &#8211;escape</code></p>
<dd> Enable interpretation of backslash escapes for tag values. Makes it possible to escape the colon-separator in TXXX, COMM values like &#8216;\:&#8217; and insert escape sequences like &#8216;
&#8217;, &#8216;	&#8217; etc.</p>
<dt><code>-f</code>,<code> &#8211;list-frames</code></p>
<dd> Display all supported ID3v2.3/2.4 frames and their meanings.</p>
<dt><code>-L</code>,<code> &#8211;list-genres</code></p>
<dd> List all ID3v1 numeric genres. These can be used to set TCON frames, but it is not recommended.</p>
<dt><code>-l</code>,<code> &#8211;list</code></p>
<dd> List all tags in the files. The output format is <i>not</i> the same as id3v2&#8217;s; instead, it is easily parsable and readable. Some tags may not have human-readable representations.</p>
<dt><code>&#8211;list-raw</code></p>
<dd> List all tags in the files, in raw format. Although this format is nominally human-readable, it may be very long if the tag contains embedded binary data.</p>
<dt><code>-d</code>,<code> &#8211;delete-v2</code></p>
<dd> Delete ID3v2 tags.</p>
<dt><code>-s</code>,<code> &#8211;delete-v1</code></p>
<dd> Delete ID3v1 tags.</p>
<dt><code>-D</code>,<code> &#8211;delete-all</code></p>
<dd> Delete all ID3 tags.</p>
<dt><code>&#8211;delete-frames=</code><i>FRAMES</i></p>
<dd> Delete specific ID3v2 frames (or groups of frames) from the files. <i>FRAMES</i> is a &quot;,&quot; separated list of frame names e.g. <code>&quot;TPE1,TALB&quot;</code></p>
<dt><code>-C</code>,<code> &#8211;convert</code></p>
<dd> Convert ID3v1 tags to ID3v2 tags. This will also happen automatically during any editing.</p>
<dt><code>-a</code>,<i>&#8211;artist</i><code>=ARTIST</code></p>
<dd> Set the artist information (TPE1).</p>
<dt><code>-A</code>,<i>&#8211;album</i><code>=ALBUM</code></p>
<dd> Set the album information (TALB).</p>
<dt><code>-t</code>,<i>&#8211;song</i><code>=TITLE</code></p>
<dd> Set the title information (TIT2).</p>
<dt><code>-c</code>,<i>&#8211;comment</i><code>=&lt;DESCRIPTION:COMMENT:LANGUAGE&gt;</code></p>
<dd> Set a comment (COMM). The language and description may be omitted, in which case the language defaults to English, and the description to an empty string.</p>
<dt><code>-g</code>,<i>&#8211;genre</i><code>=GENRE</code></p>
<dd> Set the genre information (TCON).</p>
<dt><code>-y</code>,<i>&#8211;year</i><code>=&lt;YYYY&gt;</code>,<i>&nbsp;<wbr>&#8211;date</i><code>=&lt;YYYY-[MM-DD]&gt;</code></p>
<dd> Set the year/date information (TDRC).</p>
<dt><code>-T</code>,<i>&#8211;track</i><code>=&lt;NUM/NUM&gt;</code></p>
<dd> Set the track number (TRCK). </p>
<p> Any text or URL frame (those beginning with T or W) can be modified or added by prefixing the name of the frame with &quot;&#8211;&quot;. For example, <code>&#8211;TIT3 &quot;Monkey!&quot;</code> will set the TIT3 (subtitle) frame to <code>Monkey!</code>. </p>
<p> The TXXX frame requires a colon-separated description key; many TXXX frames may be set in the file as long as they have different keys. To set this key, just separate the text with a colon, e.g. <code>&#8211;TXXX &quot;ALBUMARTISTSORT:Examples, The&quot;</code>. </p>
<p> The special POPM frame can be set in a similar way: <code>&#8211;POPM &quot;bob [at] example.com:128:2&quot;</code> to set Bob&#8217;s rating to 128/255 with 2 plays.</dl>
<h2>BUGS</h2>
<p> No sanity checking is done on the editing operations you perform, so mid3v2 will happily accept &#8211;TSIZ when editing an ID3v2.4 frame. However, it will also automatically throw it out during the next edit operation.</p>
<h2>AUTHOR</h2>
<p> Joe Wreschnig is the author of mid3v2, but he doesn&#8217;t like to admit it. </p>
<h2>Index</h2>
