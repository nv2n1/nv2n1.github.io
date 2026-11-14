---
title: "renrot(1)"
name: "renrot"
section: "1"
letter: "r"
url: "/docs/linux/man/1-renrot/"
description: "renrot – rename and rotate images according EXIF data"
---

<h2 class="name">NAME</h2>
<p> renrot &#8211; rename and rotate images according EXIF data </p>
<h2>SYNOPSIS</h2>
<p> renrot [<font SIZE="-1">OPTIONS</font>] [[<code>&#8212;</code>] <font SIZE="-1">FILE1 FILE2 &#8230;</font>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Renrot</code> is intended to work with a set of files containing <font SIZE="-1">EXIF</font> data and can do two things to them &#8212; rename and rotate. A set of files can be given either explicitly or using the <code>&#8211;extension</code> option, which select the files with the given suffix. <code>Renrot</code> operates on files in current working directory, unless given the <code>&#8211;work-directory</code> option, which changes this default. </p>
<p> <code>Renrot</code> renames input files using a flexible name template (which, among others, uses DateTimeOriginal and FileModifyDate <font SIZE="-1">EXIF</font> tags, if they exist, otherwise names the file according to the current timestamp). Further, <code>renrot</code> can aggregate files according to the shooting time period or to a given template. </p>
<p> Additionally, it rotates files and their thumbnails, as per Orientation <font SIZE="-1">EXIF</font> tag. If that tag is absent, the program allows to set rotation parameters using <code>&#8211;rotate-angle</code> and <code>&#8211;rotate-thumb</code> command line options. This is currently implemented only for <font SIZE="-1">JPEG</font> format. </p>
<p> The program can also place commentaries into the following locations: </p>
<dl>
<dt>
<dd> &#8211; Commentary tag from file (see <code>&#8211;comment-file</code> option) </p>
<p> &#8211; UserComment tag from configuration variable (see &#8220;<font SIZE="-1">TAGS&#8221;</font> section)</dl>
<p> Personal details may be specified via <font SIZE="-1">XMP</font> tags defined in a configuration file, see &#8220;<font SIZE="-1">TAGS&#8221;</font> section. </p>
<p> In addition, <code>renrot</code> can aggregate all files in different directories, according to a given date/time pattern template, set with <code>&#8211;aggr-template</code>.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> or <code>&#8211;config-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Path to the configuration file.</p>
<dt><code>-d</code> or <code>&#8211;work-directory</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i></p>
<dd> Define the working directory.</p>
<dt><code>&#8211;exclude</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Specify files to exclude. Wildcards are not allowed. If a set of files is given, there must be as many occurrences of this option as there are files in the set.</p>
<dt><code>&#8211;sub-fileset</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Get names of files to operate upon from <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. The file must contain a file name per line. This option is useful when you need to process only a set of X from Y files in the directory. If specified, the rest of files given in the command line is ignored.</p>
<dt><code>-e</code> or <code>&#8211;extension</code> <i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i></p>
<dd> Process the files with given <i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i> (<font SIZE="-1">JPG,</font> jpeg, <font SIZE="-1">CRW,</font> crw, etc). Depending on the operating system, the extension search might or might not be case-sensitive.</p>
<dt><code>&#8211;mtime</code>, <code>&#8211;no-mtime</code></p>
<dd> Defines whether to set the file&#8217;s mtime, using DateTimeOriginal tag value. Use <code>&#8211;no-mtime</code> to set it to current time stamp after processing.</p>
<dt><code>&#8211;no-renrot</code> or <code>&#8211;nochg</code></p>
<dd> Do not rename, rotate, tag and mtime images. It saves files from any changes while allows to do aggregation, contact sheet generation e.t.c.</p>
<dt><code>&#8211;use-color</code>, <code>&#8211;no-use-color</code></p>
<dd> Colorize output. This does <font SIZE="-1">NOT</font> work under Windows.</p>
<dt><code>&#8211;dry-run</code></p>
<dd> Do not do anything, only print would have been done.</p>
<dt><code>-g</code> or <code>&#8211;generate-thumb</code></p>
<dd> Generation and writing ThumbnailImage tag. The original value of the ThumbnailImage tag remains intact. To rewrite it you need to delete it first (look exiftool examples).</p>
<dt><code>&#8211;use-ipc</code>, <code>&#8211;no-use-ipc</code></p>
<dd> Rotate thumbnails using pipe, rather than files. This does <font SIZE="-1">NOT</font> work under Windows.</p>
<dt><code>-v</code></p>
<dd> Increase debugging level by 1. Debugging levels from 1 to 4 are internal levels, the levels from 5 till 9 are equivalent to levels 1-5 levels ExifTool with the maximum verbosity for <code>renrot</code>.</p>
<dt><code>-?</code> or <code>&#8211;help</code></p>
<dd> Display short usage summary and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit.</dl>
<h2><code>AGGREGATION</code></h2>
<dl>
<dt><code>&#8211;aggr-mode</code> <i></i><font SIZE="-1"><i>MODE</i></font><i></i></p>
<dd> Run aggregation process in given <i></i><font SIZE="-1"><i>MODE</i></font><i></i>. Possible values are: none, delta or template.</p>
<dt><code>&#8211;aggr-delta</code> <i></i><font SIZE="-1"><i>NUMBER</i></font><i></i></p>
<dd> Aggregation time delta, in seconds. Files with DateTimeOriginal and ones of the previous file delta, greater than <code>&#8211;aggr-delta</code> are placed in the directories, with the names are constructed by concatenating the value of the <code>&#8211;aggr-directory</code> option and the directory name counter.</p>
<dt><code>&#8211;aggr-directory</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i></p>
<dd> Aggregation directory name prefix (default is <i>Images</i>), have to be on the same file system (or on the file system which supports symbolic links in case of virtual aggregation), relative to the current working directory or an absolute path.</p>
<dt><code>-a</code> or <code>&#8211;aggr-template</code> <i></i><font SIZE="-1"><i>TEMPLATE</i></font><i></i></p>
<dd> File name template to use for file aggregation. Images are aggregated by date/time patterns. You may use combination of %d, %H, %M, %m, %S, %Y, and %y meta-characters. The template can also be defined in the configuration file (see Aggregation Template variable). The default is <i></i>%Y<i>%m%d</i>. For the detailed description, refer to <code>&#8211;name-template</code> option. For practical uses, see &#8220;<font SIZE="-1">TEMPLATE EXAMPLES&#8221;</font> section.</p>
<dt><code>&#8211;aggr-virtual</code>, <code>&#8211;no-aggr-virtual</code></p>
<dd> Defines virtualization for existent aggregation modes. The main effect of <code>&#8211;aggr-virtual</code> is that any files to be aggregated remain untouched in their places, and relative symbolic links pointing to them are stored in the directory tree created. Use <code>&#8211;no-aggr-virtual</code> to prevent virtualization.</dl>
<h2><code>CONTACT SHEET GENERATOR</code></h2>
<dl>
<dt><code>&#8211;contact-sheet</code>, <code>&#8211;no-contact-sheet</code> or <code>&#8211;cs</code>, <code>&#8211;no-cs</code></p>
<dd> Create the contact sheet. Currently it works with ThumbnailImage EXIFs and the files defined as thumbnails (see the option <code>&#8211;contact-sheet-thm</code>, below)</p>
<dt><code>&#8211;contact-sheet-file</code> or <code>&#8211;cs-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Base file name for montage files.</p>
<dt><code>&#8211;contact-sheet-dir</code> or <code>&#8211;cs-dir</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i></p>
<dd> Temporary directory for montage (created in the begining and deleted at the end of the process)</p>
<dt><code>&#8211;contact-sheet-thm</code> or <code>&#8211;cs-thm</code></p>
<dd> Files for the montage are already thumbnails</dl>
<p> Options bellow are native ImageMagic montage options look ImageMagick documentation for montage options: <i>montage &#8211;help</i> and <i><a rel="nofollow" href="http://www.imagemagick.org/">http://www.imagemagick.org/</a></i> </p>
<p> Note please, for <i></i><font SIZE="-1"><i>COLOR</i></font><i></i> use <font SIZE="-1">RGB</font> triplets only like <i>000</i> for the <i>black</i> or <i>F00</i> for the <i>red</i>.</p>
<dl>
<dt><code>&#8211;contact-sheet-tile</code> or <code>&#8211;cs-tile</code> <i></i><font SIZE="-1"><i>GEOMETRY</i></font><i></i></p>
<dd> Tile MxN (<font SIZE="-1">IM:</font> -tile)</p>
<dt><code>&#8211;contact-sheet-title</code> or <code>&#8211;cs-title</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dd> Set the title of the contact sheet (<font SIZE="-1">IM:</font> -title).</p>
<dt><code>&#8211;contact-sheet-bg</code> or <code>&#8211;cs-bg</code> <i></i><font SIZE="-1"><i>COLOR</i></font><i></i></p>
<dd> Background color (<font SIZE="-1">IM:</font> -background).</p>
<dt><code>&#8211;contact-sheet-bd</code> or <code>&#8211;cs-bd</code> <i></i><font SIZE="-1"><i>COLOR</i></font><i></i></p>
<dd> Border color (<font SIZE="-1">IM:</font> -bordercolor).</p>
<dt><code>&#8211;contact-sheet-mt</code> or <code>&#8211;cs-mt</code> <i></i><font SIZE="-1"><i>COLOR</i></font><i></i></p>
<dd> Frame color (<font SIZE="-1">IM:</font> -mattecolor).</p>
<dt><code>&#8211;contact-sheet-fn</code> or <code>&#8211;cs-fn</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dd> Render text with this font (<font SIZE="-1">IM:</font> -font).</p>
<dt><code>&#8211;contact-sheet-fl</code> or <code>&#8211;cs-fl</code> <i></i><font SIZE="-1"><i>COLOR</i></font><i></i></p>
<dd> Color to fill the text (<font SIZE="-1">IM:</font> -fill).</p>
<dt><code>&#8211;contact-sheet-lb</code> or <code>&#8211;cs-lb</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dd> Assign a label to an image (<font SIZE="-1">IM:</font> -label).</p>
<dt><code>&#8211;contact-sheet-fr</code> or <code>&#8211;cs-fr</code> <i></i><font SIZE="-1"><i>GEOMETRY</i></font><i></i></p>
<dd> Surround image with an ornamental border in N pixels (<font SIZE="-1">IM:</font> -frame).</p>
<dt><code>&#8211;contact-sheet-pntsz</code> or <code>&#8211;cs-pntsz</code> <i></i><font SIZE="-1"><i>NUMBER</i></font><i></i></p>
<dd> Font point size (<font SIZE="-1">IM:</font> -pointsize).</p>
<dt><code>&#8211;contact-sheet-shadow</code> or <code>&#8211;cs-shadow</code></p>
<dd> Set the shadow beneath a tile to simulate depth (<font SIZE="-1">IM:</font> -shadow).</p>
<dt><code>&#8211;contact-sheet-thm-fl</code> or <code>&#8211;cs-thm-fl</code> <i></i><font SIZE="-1"><i>COLOR</i></font><i></i></p>
<dd> Color to fill the text in generated thumbnail.</p>
<dt><code>&#8211;contact-sheet-thm-fn</code> or <code>&#8211;cs-thm-fn</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dd> Render the generated thumbnail text with this font (<font SIZE="-1">IM:</font> -font).</p>
<dt><code>&#8211;contact-sheet-thm-grfr</code> or <code>&#8211;cs-thm-grfr</code> <i></i><font SIZE="-1"><i>COLOR</i></font><i></i></p>
<dd> Generated thumbnail background gradient COLOR-from</p>
<dt><code>&#8211;contact-sheet-thm-grto</code> or <code>&#8211;cs-thm-grto</code> <i></i><font SIZE="-1"><i>COLOR</i></font><i></i></p>
<dd> Generated thumbnail background gradient COLOR-to</p>
<dt><code>&#8211;contact-sheet-thm-text</code> or <code>&#8211;cs-thm-text</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dd> Generated thumbnail text</p>
<dt><code>&#8211;contact-sheet-rank</code> or <code>&#8211;cs-rank</code></p>
<dd> Run ranking process according to the ranks defined with <code>&#8211;contact-sheet-rank-file</code> The result is the colored frames of the thumbnails of contact sheets.</p>
<dt><code>&#8211;contact-sheet-rank-file</code> or <code>&#8211;cs-rank-file</code></p>
<dd> Path to the file with ranks. Its format is a &#8220;file rankcolor&#8221; per line. Filename separated from the color by space or tabulation.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 01.file.jpg red </p>
<p> 02.JPG CornflowerBlue </p>
<p> 03.jpg aquamarine </p>
<p> 04.file.JPG green</dl>
</dl>
<dl>
<dt>
<dd>
<p> Only the files found in the file will be ranked.</dl>
</dl>
<h2><code>KEYWORDIZER</code></h2>
<dl>
<dt><code>&#8211;keywords</code>, <code>&#8211;no-keywords</code></p>
<dd> Whether to fill Keywords tag. Default is to not. Be careful, since with this option enabled, the existing keywords are rewriten. The keywords are taken from <i>.keywords</i> file or file specified with option <code>&#8211;keywords-file</code>.</p>
<dt><code>-k</code> or <code>&#8211;keywords-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Path to the file with keywords. Its format is a keyword per line. The <font SIZE="-1">CR</font> and <font SIZE="-1">LF</font> symbols are removed. Empty (only whitespace) lines are ignored. Any leading and trailing whitespace is removed. For example, the line <tt>&quot; _Test_ CRLF&quot;</tt> is read as <tt>&quot;_Test_&quot;</tt>.</p>
<dt><code>&#8211;keywords-replace</code>, <code>&#8211;no-keywords-replace</code></p>
<dd> Replace existing Keywords tag list rather than add new values to it. Default is not to replace.</dl>
<h2><code>RENAMING</code></h2>
<dl>
<dt><code>-n</code> or <code>&#8211;name-template</code> <i></i><font SIZE="-1"><i>TEMPLATE</i></font><i></i></p>
<dd> A template to use for creating new file names while renaming. It can also be defined in the configuration file (variable Name Template). The default is <i></i>%Y<i>%m%d%H%M%S</i>. For practical uses, see &#8220;<font SIZE="-1">TEMPLATE EXAMPLES&#8221;</font> section. </p>
<p> Interpreted sequences are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <code>%%</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>a literal %</p>
<p> <code>%#</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>a literal #</p>
<p> %C<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Numeric part of the original file name. Implemented for the sake<br />
 of cameras, that do not supply FileNumber <font SIZE="-1">EXIF</font> tag (currently all makes, except <i>Canon</i>). Such cameras generate file names starting with letters and ended with digits. No other symbols are allowed in file names, except <tt>&quot;-&quot;</tt>, <tt>&quot;.&quot;</tt> and <tt>&quot;_&quot;</tt>. </p>
<p> %c<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Ordinal number of file in the processed file set (see also<br />
 <code>&#8211;counter-fixed-field</code> option). </p>
<p> %d<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Day of month (01-31).</p>
<p> %E<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>The value of ExposureTime tag, if defined.</p>
<p> %e<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Old file extension</p>
<p> %F<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>The value of FNumber tag, if defined.</p>
<p> %H<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Hour (00-23).</p>
<p> %I<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>The value of <font SIZE="-1">ISO</font> tag, if defined.</p>
<p> %i<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>FileNumber tag if exists (otherwise, it is replaced by string<br />
 <tt>&quot;NA&quot;</tt>). </p>
<p> %M<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Minute (00-59).</p>
<p> %m<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Month (01-12).</p>
<p> %n<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Previous filename (the one before <code>renrot</code> started processing).</p>
<p> %O<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Base part of the original filename (see %o). In other words, the<br />
 first part from the beginning to the last dot character. </p>
<p> %o<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>The name file had before it was processed by <code>renrot</code> for the first<br />
 time. If the file was processed only once, the tag RenRotFileNameOriginal is set to the original file name. </p>
<p> %S<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Second (00-59)</p>
<p> %W<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>The value of WhiteBalance tag, if defined.</p>
<p> %Y<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Year with the century (1900, 1901, and so on)</p>
<p> %y<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Year without a century (00..99)</p>
<p> You can use value of any <font SIZE="-1">EXIF</font> tag to be included as name part. To do that you need to embrace tag name with sign <code>&#8220;#&#8221;</code>, while building name template (see &#8220;<font SIZE="-1">TEMPLATE EXAMPLES&#8221;</font>). </p>
<p> Be careful, since any binary <font SIZE="-1">EXIF </font>(like ThumbnaiImage) can produce totally unexpected results.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;no-rename</code></p>
<dd> Do not rename files (default is to rename them to YYYYmmddHHMMSS.ext)</p>
<dt><code>&#8211;counter-fixed-field</code>, <code>&#8211;no-counter-fixed-field</code></p>
<dd> Set fixed length for file counter, used in file name templates (see %c). It is enabled by default. Use <code>&#8211;no-counter-fixed-field</code> to undo its effect.</p>
<dt><code>&#8211;counter-start</code> <i></i><font SIZE="-1"><i>NUMBER</i></font><i></i></p>
<dd> Initial value for the file counter (default is <i>1</i>)</p>
<dt><code>&#8211;counter-step</code> <i></i><font SIZE="-1"><i>NUMBER</i></font><i></i></p>
<dd> Step to increment file counter with (default is <i>1</i>)</dl>
<h2><code>ROTATING</code></h2>
<dl>
<dt><code>-r</code> or <code>&#8211;rotate-angle</code> <i></i><font SIZE="-1"><i>ANGLE</i></font><i></i></p>
<dd> Define the angle to rotate files and thumbnails. Allowed values for <i></i><font SIZE="-1"><i>ANGLE</i></font><i></i> are 90, 180 or 270. It is useful for files not having Orientation tag.</p>
<dt><code>&#8211;rotate-thumb</code> <i></i><font SIZE="-1"><i>ANGLE</i></font><i></i></p>
<dd> Rotate only thumbnails. Allowed values for <i></i><font SIZE="-1"><i>ANGLE</i></font><i></i> are 90, 180 or 270 degrees. Use if the files which were already rotated, but their thumbnails were not.</p>
<dt><code>&#8211;only-orientation</code></p>
<dd> Rotate by changing the value of Orientation tag, no real rotation will be made. The sequence of values to rotate an image from normal (0 degrees) by 90 degrees clockwise is: 0 -&gt; 90 -&gt; 180 -&gt; 270 -&gt; 0. It means. set Orientation tag to 90cw after the first rotation, and increase that value by 90 each time the rotation is applied. For 270cw the rotation algorithm uses the reverted sequence. Rotation by 180cw triggers values in two pairs: 0 &lt;-&gt; 180 and 90 &lt;-&gt; 270. This option cannot be applied to mirror values of Orientation tag.</p>
<dt><code>&#8211;trim</code>, <code>&#8211;no-trim</code></p>
<dd> Pass the <tt>&quot;-trim&quot;</tt> option to <i><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></i>(1), to trim if needed. By default, trimming is enabled. Use <code>&#8211;no-trim</code> to disable it.</p>
<dt><code>&#8211;no-rotate</code></p>
<dd> Do not rotate images (default is to rotate according to <font SIZE="-1">EXIF</font> data).</dl>
<h2><code>TAG WRITER</code></h2>
<dl>
<dt><code>&#8211;comment-file</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> File with commentaries. It is a low priority alias to <i>TagFile = Comment: </i><font SIZE="-1"><i>FILE</i></font><i></i>.</p>
<dt><code>&#8211;user-comment</code> <i></i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dd> A low priority alias to <i>&#8211;tag UserComment: </i><font SIZE="-1"><i>STRING</i></font><i></i></p>
<dt><code>-t</code> or <code>&#8211;tag</code> <i></i><font SIZE="-1"><i>TAG</i></font><i></i></p>
<dd> See the section &#8220;<font SIZE="-1">TAGS&#8221;</font>, for the detailed description</p>
<dt><code>&#8211;no-tags</code></p>
<dd> No user&#8217;s defined tags will be written.</dl>
<h2><code>TEMPLATE EXAMPLES</code></h2>
<p> The name template <tt>&quot;01.%c.%Y%m%d%H%M%S.%i.shtr-%E.f-%F.wb-%W.iso-%I&quot;</tt> (where <i>F</i> stays for FNumber, <i>E</i> for ExposureTime, <i>I</i> for <font SIZE="-1">ISO</font> and <i>W</i> for WhiteBalance) can produce the following names: </p>
<dl>
<dt>
<dd> 01.0021.20030414103656.NA.shtr-1by40.f-2.8.wb-Auto.iso-160.jpg </p>
<p> 01.0024.20040131230857.100-0078.shtr-1by320.f-2.8.wb-Auto.iso-50.jpg </p>
<p> 01.0022.20000820222108.NA.jpg</dl>
<p> The name template <tt>&quot;01.%c.%Y%m%d%H%M%S.%i.shtr-#ExposureTime#.f-#FNumber#.wb-#WhiteBalance#.iso-#ISO#&quot;</tt> can produce the following names: </p>
<dl>
<dt>
<dd> 01.0021.20030414103656.NA.shtr-1_40.f-2.8.wb-Auto.iso-160.jpg </p>
<p> 01.0024.20040131230857.100-0078.shtr-1_320.f-2.8.wb-Auto.iso-50.jpg </p>
<p> 01.0022.20000820222108.NA.jpg</dl>
<p> The aggregation template <tt>&quot;%Y%m%d&quot;</tt> produces the following aggregation: </p>
<p> these three files </p>
<dl>
<dt>
<dd> 01.11.20030414103656.NA.jpg </p>
<p> 01.12.20030414103813.NA.jpg </p>
<p> 01.13.20030414103959.NA.jpg</dl>
<p> will be stored in the directory <i>20030414</i>, and </p>
<dl>
<dt>
<dd> 01.14.20040131130857.100-0078.jpg </p>
<p> 01.15.20040131131857.100-0079.jpg </p>
<p> 01.16.20040131133019.100-0080.jpg</dl>
<p> will be stored in the directory <i>20040131</i>.</p>
<h2>CONFIG</h2>
<p> A configuration file can be used to set some variables. <code>Renrot</code> looks for its configuration file, named <i>renrot.conf</i>, in system configuration directories <i>/etc/renrot</i> and <i>/usr/local/etc/renrot</i>, and in subdirectory <i>.renrot</i>. of the current user home directory. An alternate configuration file can also be explicitly given using the <code>&#8211;config-file</code> option. </p>
<p> The configuration file consists of a set of case-insensive keywords and their values separated by equal sign. Each such keyword/value pair occupies a separate line. Boolean variables can have one of the following values: 0, No, False, Off, Disable for false, and 1, Yes, True, On, Enable for true. </p>
<p> The variables defined for use in the configuration file are, for example:</p>
<dl>
<dt><code>mtime</code></p>
<dd> Set to <tt>&quot;Yes&quot;</tt> for synchronize mtime with tags, otherwise set it to <tt>&quot;No&quot;</tt>.</p>
<dt><code>name template</code></p>
<dd> File name template (see <code>&#8211;name-template</code>, for the description).</p>
<dt><code>trim</code></p>
<dd> Set to <tt>&quot;Yes&quot;</tt> to trim rotated images when using <i><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></i>(1).</p>
<dt><code>aggregation mode</code></p>
<dd> Aggregation mode, possible values are: none, delta or template.</p>
<dt><code>aggregation template</code></p>
<dd> Aggregation template, which defines the file aggregation (see <code>&#8211;aggr-template</code>, for the description).</p>
<dt><code>aggregation virtual</code></p>
<dd> Defines virtualization for the existing aggregation modes (see the <code>&#8211;aggr-virtual</code> option).</p>
<dt><code>Tag</code>, <code>TagFile</code></p>
<dd> Refer to the section &#8220;<font SIZE="-1">TAGS&#8221;</font>, for the detailed description</p>
<dt><code>include</code></p>
<dd> Include the named file.</dl>
<h2>TAGS</h2>
<p> A <i></i><font SIZE="-1"><i>TAG</i></font><i></i> is defined by the following combination: <i>TagName [Group]: &#8216;value&#8217;</i>. The defined tags are selected to be set and writen to the <font SIZE="-1">EXIF</font> tree using the command line option <code>&#8211;tag</code> and/or configuration file options <code>Tag</code>. </p>
<p> The syntax of the command line option <code>&#8211;tag</code> is: </p>
<dl>
<dt>
<dd> <code>&#8211;tag</code> <i>TagName [Group]: &#8216;value&#8217;</i></dl>
<p> The syntax of the configuration file option <code>Tag</code>: </p>
<dl>
<dt>
<dd> <code>Tag</code> = <i>TagName [Group]: &#8216;value&#8217;</i></dl>
<p> The parameters <i>TagName</i> and <i>Group</i> are passed to ExifTool as is. The name of the group must be enclosed in square brackets. Its <i>value</i> (after the semicolon) can be enclosed in single quotes. </p>
<p> The TagFile keyword allows to set multi-line tags from a file. Its syntax is: </p>
<dl>
<dt>
<dd> <code>TagFile</code> = <i>TagName [Group]:</i> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></dl>
<p> The following table summarizes the tags that can be used with the <code>&#8211;tag</code> option and <code>Tag</code> keyword:</p>
<dl>
<dt><code>Copyright</code></p>
<dd> Copyright notes.</p>
<dt><code>Comment</code></p>
<dd> General comment.</p>
<dt><code>UserComment</code></p>
<dd> Anything you would like to put as a comment.</p>
<dt><code>CreatorContactInfoCiAdrCity</code></p>
<dd> A city tag.</p>
<dt><code>CreatorContactInfoCiAdrCtry</code></p>
<dd> A country tag.</p>
<dt><code>CreatorContactInfoCiAdrExtadr</code></p>
<dd> Extended address (usually includes street and apartment number).</p>
<dt><code>CreatorContactInfoCiAdrPcode</code></p>
<dd> Zip code.</p>
<dt><code>CreatorContactInfoCiAdrRegion</code></p>
<dd> Region.</p>
<dt><code>CreatorContactInfoCiEmailWork</code></p>
<dd> Email.</p>
<dt><code>CreatorContactInfoCiTelWork</code></p>
<dd> Phone number.</p>
<dt><code>CreatorContactInfoCiUrlWork</code></p>
<dd> <font SIZE="-1">URL.</font></dl>
<p> Additionally, you can add any known tag here, using <code>Tag</code> or <code>TagFile</code> options as described above.</p>
<h2>FILES</h2>
<dl>
<dt>&bull;</p>
<dd> The main configuration file <code>renrot.conf</code> is searched in the following locations (in the order of their appearance):</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>~/.renrot/</code></p>
<dd> directory under user&#8217;s home place</p>
<dt><code>/usr/local/etc/renrot/</code></p>
<dd> system directory</p>
<dt><code>/etc/renrot/</code></p>
<dd> system directory</dl>
</dl>
<dl>
<dt>
<dd>
<p> Take into consideration, the files which are found will be loaded and parsed in the order when user&#8217;s configuration has maximal priority.</dl>
<dt>&bull;</p>
<dd> Other configuration files with additional options could be included into main file:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>colors.conf</code></p>
<dd> colors setup for different output facilities</p>
<dt><code>tags.conf</code></p>
<dd> different tags setup</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&bull;</p>
<dd> The following files could be placed locally in the working directory:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>.keywords</code></p>
<dd> file with keywords (see <code>&#8211;keywords-file</code>)</p>
<dt><code>.rank</code></p>
<dd> file with ranks (see <code>&#8211;contact-sheet-rank-file</code>)</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>BUGS</h2>
<p> If you found some bug or have some nice propositions, you are welcome. Additionally, please, read the section <font SIZE="-1">RESTRICTIONS</font> in file <font SIZE="-1">README.</font></p>
<dl>
<dt>1.</p>
<dd> It seems that on FreeBSD 6, Perl versions 5.8.x exhibits a bug that causes <code>renrot</code> to crash. The overal amount of memory for the perl process increasing up to the user datasize limit (in FreeBSD default is 512M). </p>
<p> It seems to be a bug in perl&#8217;s own malloc implementation. The bug should not occur in any perl which uses the system malloc (unless the system malloc has the same bug). </p>
<p> <code>renrot</code> aborts with the error message:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> Out of memory during &#8220;large&#8221; request for <font SIZE="-1">XXXX</font> bytes &#8230;</dl>
</dl>
<dl>
<dt>
<dd>
<p> This, however, does not happen with Perl v.5.6.x</dl>
<dt>2.</p>
<dd> Some versions of ImageMagick render contact sheets incorrectly. it seems it is the question to ImageMagick.</dl>
<h2>AUTHORS</h2>
<p> Copyright 2005-2012, Zeus Panchenko, Andy Shevchenko. </p>
<p> This program is free software; you can redistribute it and/or modify it under the same terms as Perl itself.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="//www.systutorials.com/docs/linux/man/3pm-Image::ExifTool/">Image::ExifTool</a></i>(3pm), <i><a href="/docs/linux/man/1-exiftool/">exiftool</a></i>(1), <i><a href="/docs/linux/man/1-jpegtran/">jpegtran</a></i>(1), <i><a href="//www.systutorials.com/docs/linux/man/3pm-Image::Magick/">Image::Magick</a></i>(3pm) </p>
<h2>Index</h2>
