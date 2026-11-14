---
title: "exiv2(1)"
name: "exiv2"
section: "1"
letter: "e"
url: "/docs/linux/man/1-exiv2/"
description: "exiv2 – Image metadata manipulation tool"
---

<h2 class="name">NAME</h2>
<p> exiv2 &#8211; Image metadata manipulation tool </p>
<h2>SYNOPSIS</h2>
<p> <code>exiv2</code> [<i>options</i>] [<i>action</i>] <i>file</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>exiv2</code> is a program to read and write Exif, IPTC and XMP image metadata and image comments. The following image formats are supported: </p>
<table>
<tr VALIGN=top>
<td><code>Type</code></td>
<td><code>Exif</code></td>
<td><code>IPTC</code></td>
<td><code>XMP</code></td>
<td><code>Image comments</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>EXV</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write
</td>
</tr>
<tr VALIGN=top>
<td>CR2</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>CRW</td>
<td>Read/Write</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>Read/Write
</td>
</tr>
<tr VALIGN=top>
<td>MRW</td>
<td>Read</td>
<td>Read</td>
<td>Read</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>TIFF</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>DNG</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>NEF</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>PEF</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>ARW</td>
<td>Read</td>
<td>Read</td>
<td>Read</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>RW2</td>
<td>Read</td>
<td>Read</td>
<td>Read</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>SR2</td>
<td>Read</td>
<td>Read</td>
<td>Read</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>SRW</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>ORF</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>PNG</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write
</td>
</tr>
<tr VALIGN=top>
<td>PGF</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write
</td>
</tr>
<tr VALIGN=top>
<td>RAF</td>
<td>Read</td>
<td>Read</td>
<td>Read</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>EPS</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>Read/Write</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>XMP</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>Read/Write</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>GIF</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>PSD</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>TGA</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>BMP</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>&#8211;</td>
<td>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td>JP2</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>Read/Write</td>
<td>&#8211;
</td>
</tr>
</table>
<dl>
<dt>&bull;</p>
<dd> Support for GIF, TGA and BMP images is minimal: the image format is recognized, a MIME type assigned to it and the height and width of the image are determined.</p>
<dt>&bull;</p>
<dd> Reading other TIFF-like RAW image formats, which are not listed in the table, may also work.</dl>
<h2>ACTIONS</h2>
<p> The <i>action</i> argument is only required if it is not clear from the <i>options</i> which action is implied.</p>
<dl>
<dt><code>pr | print</code></p>
<dd> Print image metadata. This is the default action, i.e., the command <i>exiv2 image.jpg</i> will print a summary of the image Exif metadata.</p>
<dt><code>ex | extract</code></p>
<dd> Extract metadata to *.exv, XMP sidecar (*.xmp) and thumbnail image files. Modification commands can be applied on-the-fly.</p>
<dt><code>in | insert</code></p>
<dd> Insert metadata from corresponding *.exv, XMP sidecar (*.xmp) and thumbnail files. Use option <code>-S</code> <i>.suf</i> to change the suffix of the input files. Since files of any supported format can be used as input files, this command can be used to copy the metadata between files of different formats. Modification commands can be applied on-the-fly.</p>
<dt><code>rm | delete</code></p>
<dd> Delete image metadata from the files.</p>
<dt><code>ad | adjust</code></p>
<dd> Adjust Exif timestamps by the given time. Requires at least one of the options <code>-a</code> <i>time</i>, <code>-Y</code> <i>yrs</i>, <code>-O</code> <i>mon</i> or <code>-D</code> <i>day</i>.</p>
<dt><code>mo | modify</code></p>
<dd> Apply commands to modify (add, set, delete) the Exif, IPTC and XMP metadata of image files. Requires option <code>-c</code>, <code>-m</code> or <code>-M</code>.</p>
<dt><code>mv | rename</code></p>
<dd> Rename files and/or set file timestamps according to the Exif create timestamp. Uses the value of tag Exif.Photo.DateTimeOriginal or, if not present, Exif.Image.DateTime to determine the timestamp. The filename format can be set with <code>-r</code> <i>fmt</i>, timestamp options are <code>-t</code> and <code>-T</code>.</p>
<dt><code>fi | fixiso</code></p>
<dd> Copy the ISO setting from one of the proprietary Nikon or Canon makernote ISO tags to the regular Exif ISO tag, Exif.Photo.ISOSpeedRatings. Does not overwrite an existing standard Exif ISO tag.</p>
<dt><code>fc | fixcom</code></p>
<dd> Fix the character encoding of Exif Unicode user comments. Decodes the comment using the auto-detected or specified character encoding and writes it back in UCS-2. Use option <code>-n</code> to specify the current encoding of the comment if necessary.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Display help and exit.</p>
<dt><code>-V</code></p>
<dd> Show the program version and exit.</p>
<dt><code>-v</code></p>
<dd> Be verbose during the program run.</p>
<dt><code>-q</code></p>
<dd> Silence warnings and error messages from the Exiv2 library during the program run (quiet). Note that options <code>-v</code> and <code>-q</code> can be used at the same time.</p>
<dt><code>-Q </code><i>lvl</i></p>
<dd> Set the log-level to &#8216;d'(ebug), &#8216;i'(nfo), &#8216;w'(arning), &#8216;e'(rror) or &#8216;m'(ute). The default log-level is &#8216;w&#8217;. <code>-Qm</code> is equivalent to <code>-q</code>. All log messages are written to standard error.</p>
<dt><code>-b</code></p>
<dd> Show large binary values (default is to suppress them).</p>
<dt><code>-u</code></p>
<dd> Show unknown tags (default is to suppress tags which don&#8217;t have a name).</p>
<dt><code>-g </code><i>key</i></p>
<dd> Only output info for this Exiv2 key (grep). Multiple <code>-g</code> options can be used to grep info for several keys.</p>
<dt><code>-n </code><i>enc</i></p>
<dd> Charset to use to decode Exif Unicode user comments. <i>enc</i> is a name understood by <code><a href="/docs/linux/man/3-iconv_open/">iconv_open</a></code>(3), e.g., &#8216;UTF-8&#8217;.</p>
<dt><code>-k</code></p>
<dd> Preserve file timestamps when updating files (keep). Can be used with all options which update files. The flag is ignored by read-only options.</p>
<dt><code>-t</code></p>
<dd> Set the file timestamp according to the Exif create timestamp in addition to renaming the file (overrides <code>-k</code>). This option is only used with the &#8216;rename&#8217; action.</p>
<dt><code>-T</code></p>
<dd> Only set the file timestamp according to the Exif create timestamp, do not rename the file (overrides <code>-k</code>). This option is only used with the &#8216;rename&#8217; action. Note: On Windows you may have to set the TZ environment variable for this option to work correctly.</p>
<dt><code>-f</code></p>
<dd> Do not prompt before overwriting existing files (force overwrite).</p>
<dt><code>-F</code></p>
<dd> Do not prompt before renaming files (Force rename). Appends &#8216;_1&#8217; (&#8216;_2&#8217;, &#8230;) to the name of the new file.</p>
<dt><code>-a </code><i>time</i></p>
<dd> Time adjustment in the format [-]HH[:MM[:SS]]. This option is only used with the &#8216;adjust&#8217; action. Examples: 1 adds one hour, 1:01 adds one hour and one minute, -0:00:30 subtracts 30 seconds.</p>
<dt><code>-Y </code><i>yrs</i></p>
<dd> Time adjustment by a positive or negative number of years, for the &#8216;adjust&#8217; action.</p>
<dt><code>-O </code><i>mon</i></p>
<dd> Time adjustment by a positive or negative number of months, for the &#8216;adjust&#8217; action.</p>
<dt><code>-D </code><i>day</i></p>
<dd> Time adjustment by a positive or negative number of days, for the &#8216;adjust&#8217; action.</p>
<dt><code>-p </code><i>mode</i></p>
<dd> Print mode for the &#8216;print&#8217; action. Possible modes are:<br />
 s : print a summary of the Exif metadata (the default)<br />
 a : print Exif, IPTC and XMP metadata (shortcut for -Pkyct)<br />
 t : interpreted (translated) Exif tags (-PEkyct)<br />
 v : plain Exif tag values (-PExgnycv)<br />
 h : hexdump of the Exif data (-PExgnycsh)<br />
 i : IPTC datasets (-PIkyct)<br />
 x : XMP properties (-PXkyct)<br />
 c : JPEG comment<br />
 p : list available image previews, sorted by preview image size in pixels</p>
<dt><code>-P </code><i>flgs</i></p>
<dd> Print flags for fine control of the tag list (&#8216;print&#8217; action). Allows control of the type of metadata as well as data columns included in the print output. Valid flags are:<br />
 E : include Exif tags in the list<br />
 I : IPTC datasets<br />
 X : XMP properties<br />
 x : print a column with the tag number<br />
 g : group name<br />
 k : key<br />
 l : tag label<br />
 n : tag name<br />
 y : type<br />
 c : number of components (count)<br />
 s : size in bytes<br />
 v : plain data value<br />
 t : interpreted (translated) data<br />
 h : hexdump of the data</p>
<dt><code>-d </code><i>tgt</i></p>
<dd> Delete target(s) for the &#8216;delete&#8217; action. Possible targets are:<br />
 a : all supported metadata (the default)<br />
 e : Exif section<br />
 t : Exif thumbnail only<br />
 i : IPTC data<br />
 x : XMP packet<br />
 c : JPEG comment</p>
<dt><code>-i </code><i>tgt</i></p>
<dd> Insert target(s) for the &#8216;insert&#8217; action. Possible targets are the same as those for the <code>-d</code> option, plus a modifier:<br />
 X : Insert metadata from an XMP sidecar file &lt;file&gt;.xmp. The remaining insert targets determine what metadata to insert from the sidecar file. Possible are Exif, IPTC and XMP and the default is all of these. Note that the inserted XMP properties include those converted to Exif and IPTC.<br />
 Only JPEG thumbnails can be inserted (not TIFF thumbnails), they need to be named <i>file</i>-thumb.jpg.</p>
<dt><code>-e </code><i>tgt</i></p>
<dd> Extract target(s) for the &#8216;extract&#8217; action. Possible targets are the same as those for the <code>-d</code> option, plus a target to extract preview images and a modifier to generate an XMP sidecar file:<br />
 p[&lt;n&gt;[,&lt;m&gt; &#8230;]] : Extract preview images. The optional comma separated list of preview image numbers is used to determine which preview images to extract. The available preview images and their numbers are displayed with the &#8216;print&#8217; option -pp.<br />
 X : Extract metadata to an XMP sidecar file &lt;file&gt;.xmp. The remaining extract targets determine what metadata to extract to the sidecar file. Possible are Exif, IPTC and XMP and the default is all of these.</p>
<dt><code>-r </code><i>fmt</i></p>
<dd> Filename format for the &#8216;rename&#8217; action. The format string follows <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) and supports the following keywords:<br />
 :basename: &#8211; original filename without extension<br />
 :dirname: &#8211; name of the directory holding the original file<br />
 :parentname: &#8211; name of parent directory<br />
 Default filename format is %Y%m%d_%H%M%S.</p>
<dt><code>-c </code><i>txt</i></p>
<dd> JPEG comment string to set in the image (&#8216;modify&#8217; action). This option can also be used with the &#8216;extract&#8217; and &#8216;insert&#8217; actions to modify metadata on-the-fly.</p>
<dt><code>-m </code><i>file</i></p>
<dd> Command file for the &#8216;modify&#8217; action. This option can also be used with the &#8216;extract&#8217; and &#8216;insert&#8217; actions to modify metadata on-the-fly.</p>
<dt><code>-M </code><i>cmd</i></p>
<dd> Command line for the &#8216;modify&#8217; action. This option can also be used with the &#8216;extract&#8217; and &#8216;insert&#8217; actions to modify metadata on-the-fly. The format for the commands is the same as that of the lines of a command file.</p>
<dt><code>-l </code><i>dir</i></p>
<dd> Location (directory) for files to be inserted or extracted.</p>
<dt><code>-S </code><i>.suf</i></p>
<dd> Use suffix <i>.suf</i> for source files in &#8216;insert&#8217; action.</dl>
<h2>COMMANDS</h2>
<p> Commands for the &#8216;modify&#8217; action can be read from a command file, e.g., </p>
<pre>
   exiv2 -m cmd.txt image.jpg
</pre>
<p> or given on the command line, as in </p>
<pre>
   exiv2 -M&quot;add Iptc.Application2.Credit String Mr. Smith&quot; image.jpg
</pre>
<p> Note the quotes. Multiple <code>-m</code> and <code>-M</code> options can be combined. </p>
<p> When writing Exif, IPTC and XMP metadata, <code>exiv2 </code> enforces only a correct metadata structure. It is possible to write tags with types and values different from those specified in the standards, duplicate Exif tags, undefined tags, or incomplete metadata. While <code>exiv2 </code> is able to read all metadata that it can write, other programs may have difficulties with images that contain non standard-conforming metadata.</p>
<h3>Command format</h3>
<p> The format of a command is </p>
<pre><code>
set | add | del key[[type] value]
</code></pre>
<dl>
<dt><code>set</code></p>
<dd> Set the <i>value</i> of an existing tag with a matching <i>key</i> or add the tag.</p>
<dt><code>add</code></p>
<dd> Add a tag (unless <i>key</i> is a non-repeatable IPTC key; nothing prevents you from adding duplicate Exif tags).</p>
<dt><code>del</code></p>
<dd> Delete all occurrences of a tag (requires only a <i>key</i>).</p>
<dt><i>key</i></p>
<dd> Exiv2 Exif, IPTC or XMP key.</p>
<dt><i>type</i></p>
<dd> <code>Byte | Ascii | Short | Long | Rational | Undefined | SShort | SLong | SRational | Comment</code> for Exif keys,<br />
 <code>String | Date | Time | Short | Undefined</code> for IPTC keys, and<br />
 <code>XmpText | XmpAlt | XmpBag | XmpSeq | LangAlt</code> for XMP keys. </p>
<p> A default <i>type</i> is used if none is explicitly given. The default is determined based on <i>key</i>.</p>
<dt><i>value</i></p>
<dd> The remaining text on the line is the value. It can optionally be enclosed in single quotes (&#8216;<i>value</i>&#8216;) or double quotes (&quot;<i>value</i>&quot;). </p>
<p> The value is optional. Not providing any value is equivalent to an empty value (&quot;&quot;) and is mainly useful to create an XMP array property, e.g., a bag. </p>
<p> The format of Exif <code>Comment</code> values includes an optional charset specification at the beginning: </p>
<p> <code>[charset=Ascii|Jis|Unicode|Undefined ]</code><i>comment</i> </p>
<p> <code>Undefined </code> is used by default if the value doesn&#8217;t start with a charset definition. </p>
<p> The format for IPTC <code>Date</code> values is YYYY-MM-DD (year, month, day), that for IPTC <code>Time</code> values is HH:MM:SS+|-HH:MM, where HH:MM:SS refers to local hour, minute and seconds and +|-HH:MM refers to hours and minutes ahead or behind Universal Coordinated Time (+|- means either a + or a &#8211; sign is required). </p>
<p> The format of XMP <code>LangAlt</code> values includes an optional language qualifier: </p>
<p> <code>[lang=</code><i>language-code</i> ]<i>text</i> </p>
<p> <code>x-default</code> is used by default if the value doesn&#8217;t start with a language qualifier.</p>
<dt>An additional command is available to register XMP namespaces:</p>
<dd>
<dt>
<pre>
<dd><code>reg</code> <i>prefix</i> <i>namespace</i>
</pre>
</dl>
<h3>Command file format</h3>
<p> Empty lines and lines starting with <code>#</code> in a command file are ignored (comments). Remaining lines are commands as described above.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>exiv2 *.jpg</p>
<dd> Prints a summary of the Exif information for all JPEG files in the directory.</p>
<dt>exiv2 -pi image.jpg</p>
<dd> Prints the IPTC metadata of the image.</p>
<dt>exiv2 rename img_1234.jpg</p>
<dd> Renames img_1234.jpg (taken on 13-Nov-05 at 22:58:31) to 20051113_225831.jpg</p>
<dt>exiv2 -r&#8217;:basename:_%Y%m&#8217; rename img_1234.jpg</p>
<dd> Renames img_1234.jpg to img_1234_200511.jpg</p>
<dt>exiv2 -et img1.jpg img2.jpg</p>
<dd> Extracts the Exif thumbnails from the two files into img1-thumb.jpg and img2-thumb.jpg.</p>
<dt>exiv2 -it img1.jpg img2.jpg</p>
<dd> Inserts (copies) metadata from img1.exv to img1.jpg and from img2.exv to img2.jpg.</p>
<dt>exiv2 -ep1,2 image.jpg</p>
<dd> Extracts previews 1 and 2 from the image to the files image-preview1.jpg and image-preview2.jpg.</p>
<dt>exiv2 -eiX image.jpg</p>
<dd> Extracts IPTC datasets into an XMP sidecar file image.xmp and in the process converts them to &quot;IPTC Core&quot; XMP schema.</p>
<dt>exiv2 -iixX image.jpg</p>
<dd> Inserts IPTC and XMP metadata from an XMP sidecar file image.xmp into image.jpg. The resulting IPTC datasets are converted from the &quot;IPTC Core&quot; XMP schema properties in the sidecar file to the older IPTC IIM4 format. The inserted XMP properties include those in the &quot;IPTC Core&quot; XMP schema.</p>
<dt>
<pre>
<dd>exiv2 -M&quot;set Exif.Photo.UserComment charset=Ascii New Exif comment&quot; image.jpg
</pre>
<p> Sets the Exif comment to an ASCII string.</p>
<dt>
<pre>
<dd>exiv2 -M&quot;set Exif.GPSInfo.GPSLatitude 4/1 15/1 33/1&quot; \
-M&quot;set Exif.GPSInfo.GPSLatitudeRef N&quot; image.jpg
</pre>
<p> Sets the latitude to 4 degrees, 15 minutes and 33 seconds north. The Exif standard stipulates that the GPSLatitude tag consists of three Rational numbers for the degrees, minutes and seconds of the latitude and GPSLatitudeRef contains either &#8216;N&#8217; or &#8216;S&#8217; for north or south latitude respectively.</p>
<dt>
<pre>
<dd>exiv2 insert -l/tmp -S.CRW /data/*.JPG
</pre>
<p> Copy all metadata from CRW files in the /tmp directory to JPG files with corresponding basenames in the /data directory. Note that this copies metadata as is, without any modifications to adapt it to the requirements of the target format. Some tags copied like this may not make sense in the target image.</dl>
<h2>SEE ALSO</h2>
<dl>
<dt><i><a rel="nofollow" href="http://www.exiv2.org/sample.html#modify">http://www.exiv2.org/sample.html#modify</a></i></p>
<dd> Sample command files.</p>
<dt><i><a rel="nofollow" href="http://www.exiv2.org/metadata.html">http://www.exiv2.org/metadata.html</a></i></p>
<dd> Taglists with <i>key</i> and default <i>type</i> values.</dl>
<h2>AUTHORS</h2>
<p> <code>exiv2 </code> was written by Andreas Huggel &lt;ahuggel [at] gmx.net&gt;. </p>
<p> This manual page was originally written by KELEMEN Peter &lt;fuji [at] debian.org&gt;, for the Debian project. </p>
<h2>Index</h2>
