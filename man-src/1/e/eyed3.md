---
title: "eyed3(1)"
name: "eyed3"
section: "1"
letter: "e"
url: "/docs/linux/man/1-eyed3/"
description: "eyeD3 – displays and manipulates id3-tags on mp3 files"
---

<p><code>eyeD3</code> &#8211; displays and manipulates id3-tags on mp3 files</p>
<h2>Synopsis</h2>
<p><code>eyeD3</code> [<i>options</i>] file [<i>file&#8230;</i>]<br />
 <code>eyeD3</code> [<i>options</i>] dir [<i>dir&#8230;</i>] </p>
<h2>Description</h2>
<p><code>eyeD3</code> Manipulates ID3 tags in mp3 files and is able to read/write and convert between ID3 v1.0, v1.1, v2.3 and v2.4 tags. High-level access is provided to most frames, including APIC (i.e., images) frames. </p>
<h2>Options</h2>
<p><code>-h, &#8211;help</code> Shows a brief help string and exit.</p>
<dl>
<dt><code>&#8211;version</code></p>
<dd>Show program&#8217;s version number and exit.</p>
<dt><code>&#8211;no-color</code></p>
<dd>Disable color output.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Show all available tag information.</p>
<dt><code>&#8211;debug</code></p>
<dd>Trace program execution; for debugging. </p>
</dl>
<h2>Tag Versions</h2>
<dl>
<dt><code>-1, &#8211;v1</code></p>
<dd>Only read/write ID3 v1 tags. By default, v1 tags are only read if there is not a v2 tag.</p>
<dt><code>-2, &#8211;v2</code></p>
<dd>Only read/write ID3 v2.x tags.</p>
<dt><code>&#8211;to-v1.1</code></p>
<dd>Convert the file&#8217;s tag to ID3 v1.1. (Or 1.0 if there is no track number)</p>
<dt><code>&#8211;to-v2.3</code></p>
<dd>Convert the file&#8217;s tag to ID3 v2.3.</p>
<dt><code>&#8211;to-v2.4</code></p>
<dd>Convert the file&#8217;s tag to ID3 v2.4 </p>
</dl>
<h2>Tag Data</h2>
<p>Options for manipulating tag data have the side-effect of removing a frame when the data specified is the empty string. For example, &#8211;artist=&quot;&quot; (or -a &quot;&quot;) would cause the artist frame to be removed. This is especially useful for removing comment frames. </p>
<dl>
<dt><code>-a </code>STRING, <code>&#8211;artist=</code>STRING</p>
<dd>Set artist the to STRING.</p>
<dt><code>-A </code>STRING, <code>&#8211;album=</code>STRING</p>
<dd>Set album to STRING.</p>
<dt><code>-t </code>STRING, <code>&#8211;title=</code>STRING</p>
<dd>Set track title to STRING.</p>
<dt><code>-n </code>NUM, <code>&#8211;track=</code>NUM</p>
<dd>Set track number to NUM.</p>
<dt><code>-N </code>NUM, <code>&#8211;track-total=</code>NUM</p>
<dd>Set total number of tracks to NUM.</p>
<dt><code>-G </code>STRING, <code>&#8211;genre=</code>STRING</p>
<dd>Sets genre to STRING. (See &#8211;list-genres)</p>
<dt><code>-Y </code>YEAR, <code>&#8211;year=</code>YEAR</p>
<dd>Set the four digit year.</p>
<dt><code>-p </code>STRING, <code>&#8211;publisher=</code>STRING</p>
<dd>Set the publisher/label text.</p>
<dt><code>&#8211;comment=</code>[LANGUAGE]:DESCRIPTION:COMMENT</p>
<dd>Add (or remove when COMMENT is &quot;&quot;) a comment. Note that the argument value MUST always contain exactly two &#8216;:&#8217; characters to delimit the fields even when the default language is being used. The DESCRIPTION string is the comment title. The optional LANGUAGE string MUST be a three-character ISO 639 language code. The default is &quot;eng&quot; for English. </p>
<p> A tag may not have more than one comment frame with the same DESCRIPTION and LANGUAGE values.</p>
<dt><code>&#8211;remove-comments</code></p>
<dd>Remove all comment frames from the tag.</p>
<dt><code>&#8211;lyrics=</code>[LANGUAGE]:DESCRIPTION:LYRICS</p>
<dd>Add (or remove when LYRICS is &quot;&quot;) a comment. Note that the argument value MUST always contain exactly two &#8216;:&#8217; characters to delimit the fields even when the default language is being used. The DESCRIPTION string is the lyrics title. The optional LANGUAGE string MUST be a three-character ISO 639 language code. The default is &quot;eng&quot; for English. </p>
<p> A tag may not have more than one lyrics frame with the same DESCRIPTION and LANGUAGE values.</p>
<dt><code>&#8211;remove-lyrics</code></p>
<dd>Remove all lyrics frames from the tag.</p>
<dt><code>&#8211;add-image=</code>IMG_PATH:TYPE[:DESCRIPTION]</p>
<dd>Add an image to the tag (APIC frame). The IMG_PATH is the image file to add to the tag. If the path value is empty the image frame with a value of TYPE is removed from the tag. The TYPE is one of the types listed when &#8216;eyeD3 &#8211;list-image-types&#8217; is run. The DESCRIPTION is optional and will default to &quot;&quot;. </p>
<p> A tag may not have more than one image frame with the same TYPE values.</p>
<dt><code>&#8211;remove-images</code></p>
<dd>Remove all image (APIC) frames from the tag.</p>
<dt><code>&#8211;add-object=</code>OBJ_PATH[:DESCRIPTION[:MIME-TYPE[:FILENAME]]]</p>
<dd>Add an encapsulated object to the tag (GEOB frame). The description and filename are optional, but when used, the &#8216;:&#8217; delimiters must be present. If the OBJ_PATH value is empty the GEOB frame with DESCRIPTION is removed. </p>
<p> A tag may not have more than one object (GEOB) frame with the same DESCRIPTION values.</p>
<dt><code>-i </code>DIR, <code>&#8211;write-images=</code>DIR</p>
<dd>Causes all attached images (APIC frames) to be written to the specified directory. They are named by their &quot;image type&quot;. For example, if the image is a png and the type is OTHER, a file named OTHER.png is written to the desired directory. If the file name already exist, a unique numeric value is appended to the type string.</p>
<dt><code>-o </code>DIR, <code>&#8211;write-objects=</code>DIR</p>
<dd>Causes all attached objects (GEOB frames) to be written to the specified directory. The files are written with the name &quot;&lt;filename&gt;.&lt;mime-subtype&gt;&quot; in the specified directory.</p>
<dt><code>&#8211;set-text-frame=</code>FID:TEXT</p>
<dd>Set the value of a specific (i.e., FID) text frame. To remove the frame, specify an empty value. e.g., &#8211;set-text-frame=&quot;TDRC:&quot;</p>
<dt><code>&#8211;set-user-text-frame=</code>DESC:TEXT</p>
<dd>Set the value of a TXXX text frame with a unique description. To remove the frame, specify an empty value. e.g., &#8211;set-user-text-frame=&quot;Description:&quot;</p>
<dt><code>&#8211;set-url-frame=</code>FID:URL</p>
<dd>Set the value of a specific (i.e., FID) URL frame. To remove the frame, specify an empty URL. e.g., &#8211;set-url-frame=&quot;WCOM:&quot;</p>
<dt><code>&#8211;set-user-url-frame=</code>DESC:URL</p>
<dd>Set the value of a WXXX frame with unique description string. To remove the frame, specify an empty URL. e.g., &#8211;set-user-url-frame=&quot;Description:&quot;</p>
<dt><code>&#8211;play-count=</code>[+]N</p>
<dd>Set the play count (PCNT). If the argument value begins with &#8216;+&#8217; the value is incremented by N, otherwise it is set to exactly N.</p>
<dt><code>&#8211;bpm=</code>N</p>
<dd>Set the beats per minute value. The value MUST be greater than 0.</p>
<dt><code>&#8211;unique-file-id=</code>OWNER_ID:ID</p>
<dd>Add a UFID frame. If the ID arg is empty the UFID frame with OWNER_ID is removed. An OWNER_ID MUST be specified.</p>
<dt><code>&#8211;set-encoding=</code>latin1|utf8|utf16-LE|utf16-BE</p>
<dd>Set the encoding that is used for _all_ text frames in the tag. The encoding is applied only when the tag is updated, therefore a frame must be set or &#8211;force-update is present. Note that, unfortunately, utf8 is not supported by ID3 v2.3 tags.</p>
<dt><code>&#8211;remove-v1</code></p>
<dd>Remove ID3 v1.x tag.</p>
<dt><code>&#8211;remove-v2</code></p>
<dd>Remove ID3 v2.x tag.</p>
<dt><code>&#8211;remove-all</code></p>
<dd>Remove all tags. </p>
</dl>
<h2>Misc. Options</h2>
<dl>
<dt><code>&#8211;rename=</code>PATTERN</p>
<dd>Rename the file based on PATTERN which may contain the following substitution variables: %A (artist), %a (album), %t (title), %n (track number), and %N (the total track count). The PATTERN string MUST not contain the file name extenstion.</p>
<dt><code>&#8211;fs-encoding=</code>ENCODING</p>
<dd>Use the specified character encoding for filenames when renaming files. The default value is iso-8859-1.</p>
<dt><code>-l</code>, <code>&#8211;list-genres</code></p>
<dd>Display the table of &quot;valid&quot; ID3 genres and exit.</p>
<dt><code>&#8211;list-image-types</code></p>
<dd>List all possible image types for APIC frames.</p>
<dt><code>&#8211;strict</code></p>
<dd>Fail for tags that violate the ID3 specification.</p>
<dt><code>&#8211;jep-118</code></p>
<dd>Output the tag per the format described in JEP-0118. See <a rel="nofollow" href="http://www.xmpp.org/extensions/xep-0118.html">http://www.xmpp.org/extensions/xep-0118.html</a></p>
<dt><code>&#8211;nfo</code></p>
<dd>Output NFO information for each album directory.</p>
<dt><code>&#8211;lametag</code></p>
<dd>Prints the LAME Tag.</p>
<dt><code>&#8211;force-update</code></p>
<dd>Update the tag regardless of whether any frames were set on the command line.</p>
<dt><code>&#8211;no-zero-padding</code></p>
<dd>Don&#8217;t pad track or disc numbers with 0&#8217;s.</p>
<dt><code>&#8211;no-tagging-time-frame</code></p>
<dd>When saving tags do not add a TDTG (tagging time) frame.</p>
<dt><code>-F </code>DELIM</p>
<dd>Specify a new delimiter for option values that contain multiple fields (default delimiter is &#8216;:&#8217;) </p>
</dl>
<h2>See Also</h2>
<p><a rel="nofollow" href="http://eyed3.nicfit.net/">http://eyed3.nicfit.net/</a> </p>
<h2>Author</h2>
<p>eyeD3 was written by Travis Shirk &lt;travis [at] pobox.com&gt;. This manpage was written by Alexander Wirt &lt;formorer [at] debian.org&gt; for the Debian Distribution and Travis Shirk.</p>
