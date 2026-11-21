---

title: "metaflac(1)"
name: "metaflac"
section: "1"
letter: "m"
url: "/docs/linux/man/1-metaflac/"
description: "metaflac – program to list, add, remove, or edit metadata in one or more FLAC files."
---

<p> metaflac &#8211; program to list, add, remove, or edit metadata in one or more FLAC files. </p>
<h2>SYNOPSIS</h2>
<p> <code>metaflac</code> [ <i>options</i> ] [ <i>operations</i> ] <i>FLACfile</i><i> &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> Use <code>metaflac</code> to list, add, remove, or edit metadata in one or more FLAC files. You may perform one major operation, or many shorthand operations at a time.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;preserve-modtime</code></dt>
<dd> Preserve the original modification time in spite of edits.</dd>
<dt><code>&#8211;with-filename</code></dt>
<dd> Prefix each output line with the FLAC file name (the default if more than one FLAC file is specified).</dd>
<dt><code>&#8211;no-filename</code></dt>
<dd> Do not prefix each output line with the FLAC file name (the default if only one FLAC file is specified).</dd>
<dt><code>&#8211;no-utf8-convert</code></dt>
<dd> Do not convert tags from UTF-8 to local charset, or vice versa. This is useful for scripts, and setting tags in situations where the locale is wrong.</dd>
<dt><code>&#8211;dont-use-padding</code></dt>
<dd> By default metaflac tries to use padding where possible to avoid rewriting the entire file if the metadata size changes. Use this option to tell metaflac to not take advantage of padding this way.</dd></dl>
<h2>SHORTHAND OPERATIONS</h2>
<dl>
<dt><code>&#8211;show-md5sum</code></dt>
<dd> Show the MD5 signature from the STREAMINFO block.</dd>
<dt><code>&#8211;show-min-blocksize</code></dt>
<dd> Show the minimum block size from the STREAMINFO block.</dd>
<dt><code>&#8211;show-max-blocksize</code></dt>
<dd> Show the maximum block size from the STREAMINFO block.</dd>
<dt><code>&#8211;show-min-framesize</code></dt>
<dd> Show the minimum frame size from the STREAMINFO block.</dd>
<dt><code>&#8211;show-max-framesize</code></dt>
<dd> Show the maximum frame size from the STREAMINFO block.</dd>
<dt><code>&#8211;show-sample-rate</code></dt>
<dd> Show the sample rate from the STREAMINFO block.</dd>
<dt><code>&#8211;show-channels</code></dt>
<dd> Show the number of channels from the STREAMINFO block.</dd>
<dt><code>&#8211;show-bps</code></dt>
<dd> Show the # of bits per sample from the STREAMINFO block.</dd>
<dt><code>&#8211;show-total-samples</code></dt>
<dd> Show the total # of samples from the STREAMINFO block.</dd>
<dt><code>&#8211;show-vendor-tag</code></dt>
<dd> Show the vendor string from the VORBIS_COMMENT block.</dd>
<dt><code>&#8211;show-tag=name</code></dt>
<dd> Show all tags where the the field name matches &#8216;name&#8217;.</dd>
<dt><code>&#8211;remove-tag=name</code></dt>
<dd> Remove all tags whose field name is &#8216;name&#8217;.</dd>
<dt><code>&#8211;remove-first-tag=name</code></dt>
<dd> Remove first tag whose field name is &#8216;name&#8217;.</dd>
<dt><code>&#8211;remove-all-tags</code></dt>
<dd> Remove all tags, leaving only the vendor string.</dd>
<dt><code>&#8211;set-tag=field</code></dt>
<dd> Add a tag. The field must comply with the Vorbis comment spec, of the form &quot;NAME=VALUE&quot;. If there is currently no tag block, one will be created.</dd>
<dt><code>&#8211;set-tag-from-file=field</code></dt>
<dd> Like &#8211;set-tag, except the VALUE is a filename whose contents will be read verbatim to set the tag value. Unless &#8211;no-utf8-convert is specified, the contents will be converted to UTF-8 from the local charset. This can be used to store a cuesheet in a tag (e.g. &#8211;set-tag-from-file=&quot;CUESHEET=image.cue&quot;). Do not try to store binary data in tag fields! Use APPLICATION blocks for that.</dd>
<dt><code>&#8211;import-tags-from=file</code></dt>
<dd> Import tags from a file. Use &#8216;-&#8216; for stdin. Each line should be of the form NAME=VALUE. Multi-line comments are currently not supported. Specify &#8211;remove-all-tags and/or &#8211;no-utf8-convert before &#8211;import-tags-from if necessary. If FILE is &#8216;-&#8216; (stdin), only one FLAC file may be specified.</dd>
<dt><code>&#8211;export-tags-to=file</code></dt>
<dd> Export tags to a file. Use &#8216;-&#8216; for stdout. Each line will be of the form NAME=VALUE. Specify &#8211;no-utf8-convert if necessary.</dd>
<dt><code>&#8211;import-cuesheet-from=file</code></dt>
<dd> Import a cuesheet from a file. Use &#8216;-&#8216; for stdin. Only one FLAC file may be specified. A seekpoint will be added for each index point in the cuesheet to the SEEKTABLE unless &#8211;no-cued-seekpoints is specified.</dd>
<dt><code>&#8211;export-cuesheet-to=file</code></dt>
<dd> Export CUESHEET block to a cuesheet file, suitable for use by CD authoring software. Use &#8216;-&#8216; for stdout. Only one FLAC file may be specified on the command line.</dd>
<dt><code>&#8211;import-picture-from={</code><i>FILENAME</i><code>|</code><i>SPECIFICATION</i><code>}</code></dt>
<dd> Import a picture and store it in a PICTURE metadata block. More than one &#8211;import-picture-from command can be specified. Either a filename for the picture file or a more complete specification form can be used. The SPECIFICATION is a string whose parts are separated by | (pipe) characters. Some parts may be left empty to invoke default values. FILENAME is just shorthand for &quot;||||FILENAME&quot;. The format of SPECIFICATION is </dd>
<p> [TYPE]|[MIME-TYPE]|[DESCRIPTION]|[WIDTHxHEIGHTxDEPTH[/COLORS]]|FILE </p>
<p> TYPE is optional; it is a number from one of: </p>
<p> 0: Other </p>
<p> 1: 32&#215;32 pixels &#8216;file icon&#8217; (PNG only) </p>
<p> 2: Other file icon </p>
<p> 3: Cover (front) </p>
<p> 4: Cover (back) </p>
<p> 5: Leaflet page </p>
<p> 6: Media (e.g. label side of CD) </p>
<p> 7: Lead artist/lead performer/soloist </p>
<p> 8: Artist/performer </p>
<p> 9: Conductor </p>
<p> 10: Band/Orchestra </p>
<p> 11: Composer </p>
<p> 12: Lyricist/text writer </p>
<p> 13: Recording Location </p>
<p> 14: During recording </p>
<p> 15: During performance </p>
<p> 16: Movie/video screen capture </p>
<p> 17: A bright coloured fish </p>
<p> 18: Illustration </p>
<p> 19: Band/artist logotype </p>
<p> 20: Publisher/Studio logotype </p>
<p> The default is 3 (front cover). There may only be one picture each of type 1 and 2 in a file. </p>
<p> MIME-TYPE is optional; if left blank, it will be detected from the file. For best compatibility with players, use pictures with MIME type image/jpeg or image/png. The MIME type can also be &#8211;&gt; to mean that FILE is actually a URL to an image, though this use is discouraged. </p>
<p> DESCRIPTION is optional; the default is an empty string. </p>
<p> The next part specfies the resolution and color information. If the MIME-TYPE is image/jpeg, image/png, or image/gif, you can usually leave this empty and they can be detected from the file. Otherwise, you must specify the width in pixels, height in pixels, and color depth in bits-per-pixel. If the image has indexed colors you should also specify the number of colors used. When manually specified, it is not checked against the file for accuracy. </p>
<p> FILE is the path to the picture file to be imported, or the URL if MIME type is &#8211;&gt; </p>
<p> For example, &quot;|image/jpeg|||../cover.jpg&quot; will embed the JPEG file at ../cover.jpg, defaulting to type 3 (front cover) and an empty description. The resolution and color info will be retrieved from the file itself. </p>
<p> The specification &quot;4|&#8211;&gt;|CD|320x300x24/173|<a rel="nofollow" href="http://blah.blah/backcover.tiff">http://blah.blah/backcover.tiff</a>&quot; will embed the given URL, with type 4 (back cover), description &quot;CD&quot;, and a manually specified resolution of 320&#215;300, 24 bits-per-pixel, and 173 colors. The file at the URL will not be fetched; the URL itself is stored in the PICTURE metadata block.</p>
<dt><code>&#8211;export-picture-to=file</code></dt>
<dd> Export PICTURE block to a file. Use &#8216;-&#8216; for stdout. Only one FLAC file may be specified on the command line. The first PICTURE block will be exported unless &#8211;export-picture-to is preceded by a &#8211;block-number=# option to specify the exact metadata block to extract. Note that the block number is the one shown by &#8211;list.</dd>
<dt><code>&#8211;add-replay-gain</code></dt>
<dd> Calculates the title and album gains/peaks of the given FLAC files as if all the files were part of one album, then stores them as FLAC tags. The tags are the same as those used by vorbisgain. Existing ReplayGain tags will be replaced. If only one FLAC file is given, the album and title gains will be the same. Since this operation requires two passes, it is always executed last, after all other operations have been completed and written to disk. All FLAC files specified must have the same resolution, sample rate, and number of channels. The sample rate must be one of 8, 11.025, 12, 16, 18.9, 22.05, 24, 28, 32, 37.8, 44.1, 48, 56, 64, 88.2, 96, 112, 128, 144, 176.4, or 192kHz.</dd>
<dt><code>&#8211;remove-replay-gain</code></dt>
<dd> Removes the ReplayGain tags.</dd>
<dt><code>&#8211;add-seekpoint={</code><i>#</i><code>|</code><i>X</i><code>|</code><i>#x</i><code>|</code><i>#s</i><code>}</code></dt>
<dd> Add seek points to a SEEKTABLE block. Using #, a seek point at that sample number is added. Using X, a placeholder point is added at the end of a the table. Using #x, # evenly spaced seek points will be added, the first being at sample 0. Using #s, a seekpoint will be added every # seconds (# does not have to be a whole number; it can be, for example, 9.5, meaning a seekpoint every 9.5 seconds). If no SEEKTABLE block exists, one will be created. If one already exists, points will be added to the existing table, and any duplicates will be turned into placeholder points. You may use many &#8211;add-seekpoint options; the resulting SEEKTABLE will be the unique-ified union of all such values. Example: &#8211;add-seekpoint=100x &#8211;add-seekpoint=3.5s will add 100 evenly spaced seekpoints and a seekpoint every 3.5 seconds.</dd>
<dt><code>&#8211;add-padding=length</code></dt>
<dd> Add a padding block of the given length (in bytes). The overall length of the new block will be 4 + length; the extra 4 bytes is for the metadata block header.</dd></dl>
<h2>MAJOR OPERATIONS</h2>
<dl>
<dt><code>&#8211;list</code></dt>
<dd> List the contents of one or more metadata blocks to stdout. By default, all metadata blocks are listed in text format. Use the following options to change this behavior:</dd>
<dl>
<dl>
<dt><code>&#8211;block-number=#[,#[&#8230;]]</code></dt>
<dd> An optional comma-separated list of block numbers to display. The first block, the STREAMINFO block, is block 0.</dd>
<dt><code>&#8211;block-type=type[,type[&#8230;]]</code></dt>
<dd>
</dd><dt><code>&#8211;except-block-type=type[,type[&#8230;]]</code></dt>
<dd> An optional comma-separated list of block types to be included or ignored with this option. Use only one of &#8211;block-type or &#8211;except-block-type. The valid block types are: STREAMINFO, PADDING, APPLICATION, SEEKTABLE, VORBIS_COMMENT, PICTURE. You may narrow down the types of APPLICATION blocks displayed as follows: </dd>
<p> APPLICATION:abcd The APPLICATION block(s) whose textual repre- sentation of the 4-byte ID is &quot;abcd&quot; APPLICATION:0xXXXXXXXX The APPLICATION block(s) whose hexadecimal big- endian representation of the 4-byte ID is &quot;0xXXXXXXXX&quot;. For the example &quot;abcd&quot; above the hexadecimal equivalalent is 0x61626364 </p>
<dl>
<dt>
</dt><dd> <code>Note:</code> if both &#8211;block-number and &#8211;[except-]block-type are specified, the result is the logical AND of both arguments.</dd></dl>
<dt><code>&#8211;application-data-format=hexdump|text</code></dt>
<dd> If the application block you are displaying contains binary data but your &#8211;data-format=text, you can display a hex dump of the application data contents instead using &#8211;application-data-format=hexdump.</dd></dl>
</dl>
<dt><code>&#8211;remove</code></dt>
<dd> Remove one or more metadata blocks from the metadata. Unless &#8211;dont-use-padding is specified, the blocks will be replaced with padding. You may not remove the STREAMINFO block.</dd>
<dl>
<dl>
<dt><code>&#8211;block-number=#[,#[&#8230;]]</code></dt>
<dd>
</dd><dt><code>&#8211;block-type=type[,type[&#8230;]]</code></dt>
<dd>
</dd><dt><code>&#8211;except-block-type=type[,type[&#8230;]]</code></dt>
<dd> See &#8211;list above for usage. </dd>
<dl>
<dt>
</dt><dd> <code>Note:</code> if both &#8211;block-number and &#8211;[except-]block-type are specified, the result is the logical AND of both arguments.</dd></dl>
</dl>
</dl>
<dt><code>&#8211;remove-all</code></dt>
<dd> Remove all metadata blocks (except the STREAMINFO block) from the metadata. Unless &#8211;dont-use-padding is specified, the blocks will be replaced with padding.</dd>
<dt><code>&#8211;merge-padding</code></dt>
<dd> Merge adjacent PADDING blocks into single blocks.</dd>
<dt><code>&#8211;sort-padding</code></dt>
<dd> Move all PADDING blocks to the end of the metadata and merge them into a single block.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-flac/">flac</a>(1). </p>
