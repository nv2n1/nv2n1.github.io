---
title: "exiftool(1)"
name: "exiftool"
section: "1"
letter: "e"
url: "/docs/linux/man/1-exiftool/"
description: "exiftool – Read and write meta information in files"
---
<h2 class="name">NAME</h2>
<p> exiftool - Read and write meta information in files </p>
<h2>SYNOPSIS</h2>
<h3>Reading</h3>
<p> <code>exiftool</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] [-<i></i><font SIZE="-1"><i>TAG</i></font><i></i>...] [--<i></i><font SIZE="-1"><i>TAG</i></font><i></i>...] <i></i><font SIZE="-1"><i>FILE</i></font><i></i>...  </p>
<h3>Writing</h3>
<p> <code>exiftool</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] -<i></i><font SIZE="-1"><i>TAG</i></font><i></i>[+-&lt;]=[<i></i><font SIZE="-1"><i>VALUE</i></font><i></i>]... <i></i><font SIZE="-1"><i>FILE</i></font><i></i>...  </p>
<h3>Copying</h3>
<p> <code>exiftool</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <code>-tagsFromFile</code> <i></i><font SIZE="-1"><i>SRCFILE</i></font><i></i> [-<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>[&gt;<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>]...] <i></i><font SIZE="-1"><i>FILE</i></font><i></i>...  </p>
<h3>Other</h3>
<p> <code>exiftool</code> [ <code>-ver</code> | <code>-list</code>[<code>w</code>|<code>f</code>|<code>r</code>|<code>wf</code>|<code>g</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]|<code>d</code>|<code>x</code>] ] </p>
<p> For specific examples, see the <font SIZE="-1">EXAMPLES</font> sections below. </p>
<p> This documentation is displayed if exiftool is run without an input <i></i><font SIZE="-1"><i>FILE</i></font><i></i> when one is expected.  </p>
<h2>DESCRIPTION</h2>
<p> A command-line interface to Image::ExifTool, used for reading and writing meta information in a variety of file types. <i></i><font SIZE="-1"><i>FILE</i></font><i></i> is one or more source file names, directory names, or <code>&quot;-&quot;</code> for the standard input. Metadata is read from source files and printed in readable form to the console (or written to output text files with <code>-w</code>). </p>
<p> To write or delete metadata, tag values are assigned using the -<i></i><font SIZE="-1"><i>TAG</i></font><i></i>=[<i></i><font SIZE="-1"><i>VALUE</i></font><i></i>] syntax, or the <code>-geotag</code> option. To copy or move metadata, the <code>-tagsFromFile</code> feature is used. By default the original files are preserved with <code>&quot;_original&quot;</code> appended to their names --- be sure to verify that the new files are <font SIZE="-1">OK</font> before erasing the originals. Once in write mode, exiftool will ignore any read-specific options. </p>
<p> Note: If <i></i><font SIZE="-1"><i>FILE</i></font><i></i> is a directory name then only supported file types in the directory are processed (in write mode only writable types are processed). However, files may be specified by name, or the <code>-ext</code> option may be used to force processing of files with any extension. Hidden files in the directory are also processed. Adding the <code>-r</code> option causes subdirectories to be processed recursively, but those with names beginning with ``.&#8216;&#8216; are skipped unless <code>-r.</code> is used. </p>
<p> Below is a list of file types and meta information formats currently supported by ExifTool (r = read, w = write, c = create): </p>
<pre><code>  File Types
  ------------+-------------+-------------+-------------+------------
  3FR r | DV r | K25 r | OFR r | RSRC r
  3G2 r/w | DVB r/w | KDC r | OGG r | RTF r
  3GP r/w | DYLIB r | KEY r | OGV r | RW2 r/w
  A r | EIP r | LA r | OPUS r | RWL r/w
  AA r | EPS r/w | LFP r | ORF r/w | RWZ r
  AAX r/w | EPUB r | LNK r | OTF r | RM r
  ACR r | ERF r/w | M2TS r | PAC r | SEQ r
  AFM r | EXE r | M4A/V r/w | PAGES r | SO r
  AI r/w | EXIF r/w/c | MAX r | PBM r/w | SR2 r/w
  AIFF r | EXR r | MEF r/w | PCD r | SRF r
  APE r | EXV r/w/c | MIE r/w/c | PDB r | SRW r/w
  ARW r/w | F4A/V r/w | MIFF r | PDF r/w | SVG r
  ASF r | FFF r/w | MKA r | PEF r/w | SWF r
  AVI r | FLA r | MKS r | PFA r | THM r/w
  AZW r | FLAC r | MKV r | PFB r | TIFF r/w
  BMP r | FLIF r/w | MNG r/w | PFM r | TORRENT r
  BPG r | FLV r | MOBI r | PGF r | TTC r
  BTF r | FPF r | MODD r | PGM r/w | TTF r
  CHM r | FPX r | MOI r | PLIST r | VCF r
  COS r | GIF r/w | MOS r/w | PICT r | VRD r/w/c
  CR2 r/w | GZ r | MOV r/w | PMP r | VSD r
  CRW r/w | HDP r/w | MP3 r | PNG r/w | WAV r
  CS1 r/w | HDR r | MP4 r/w | PPM r/w | WDP r/w
  DCM r | HTML r | MPC r | PPT r | WEBP r
  DCP r/w | ICC r/w/c | MPG r | PPTX r | WEBM r
  DCR r | ICS r | MPO r/w | PS r/w | WMA r
  DFONT r | IDML r | MQV r/w | PSB r/w | WMV r
  DIVX r | IIQ r/w | MRW r/w | PSD r/w | WV r
  DJVU r | IND r/w | MXF r | PSP r | X3F r/w
  DLL r | INX r | NEF r/w | QTIF r/w | XCF r
  DNG r/w | ISO r | NRW r/w | RA r | XLS r
  DOC r | ITC r | NUMBERS r | RAF r/w | XLSX r
  DOCX r | J2C r | O r | RAM r | XMP r/w/c
  DPX r | JNG r/w | ODP r | RAR r | ZIP r
  DR4 r/w/c | JP2 r/w | ODS r | RAW r/w |
  DSS r | JPEG r/w | ODT r | RIFF r |
  Meta Information
  ----------------------+----------------------+---------------------
  EXIF r/w/c | CIFF r/w | Ricoh RMETA r
  GPS r/w/c | AFCP r/w | Picture Info r
  IPTC r/w/c | Kodak Meta r/w | Adobe APP14 r
  XMP r/w/c | FotoStation r/w | MPF r
  MakerNotes r/w/c | PhotoMechanic r/w | Stim r
  Photoshop IRB r/w/c | JPEG 2000 r | DPX r
  ICC Profile r/w/c | DICOM r | APE r
  MIE r/w/c | Flash r | Vorbis r
  JFIF r/w/c | FlashPix r | SPIFF r
  Ducky APP12 r/w/c | QuickTime r | DjVu r
  PDF r/w/c | Matroska r | M2TS r
  PNG r/w/c | MXF r | PE/COFF r
  Canon VRD r/w/c | PrintIM r | AVCHD r
  Nikon Capture r/w/c | FLAC r | ZIP r
  GeoTIFF r/w/c | ID3 r | (and more)
</code></pre>
<h2>OPTIONS</h2>
<p> Case is not significant for any command-line option (including tag and group names), except for single-character options when the corresponding upper-case option exists. Many single-character options have equivalent long-name versions (shown in brackets), and some options have inverses which are invoked with a leading double-dash. Unrecognized options are interpreted as tag names (for this reason, multiple single-character options may <font SIZE="-1">NOT</font> be combined into one argument). Contrary to standard practice, options may appear after source file names on the exiftool command line.  </p>
<h3>Option Summary</h3>
<p> Tag operations </p>
<pre><code>  -TAG or --TAG Extract or exclude specified tag
  -TAG[+-]=[VALUE] Write new value for tag
  -TAG[+-]&lt;=DATFILE Write tag value from contents of file
  -TAG[+-]&lt;SRCTAG Copy tag value (see -tagsFromFile)
  -tagsFromFile SRCFILE Copy tag values from file
  -x TAG (-exclude) Exclude specified tag
</code></pre>
<p> Input-output text formatting </p>
<pre><code>  -args (-argFormat) Format metadata as exiftool arguments
  -b (-binary) Output metadata in binary format
  -c FMT (-coordFormat) Set format for GPS coordinates
  -charset [[TYPE=]CHARSET] Specify encoding for special characters
  -csv[=CSVFILE] Export/import tags in CSV format
  -d FMT (-dateFormat) Set format for date/time values
  -D (-decimal) Show tag ID numbers in decimal
  -E, -ex (-escape(HTML|XML)) Escape values for HTML (-E) or XML (-ex)
  -f (-forcePrint) Force printing of all specified tags
  -g[NUM...] (-groupHeadings) Organize output by tag group
  -G[NUM...] (-groupNames) Print group name for each tag
  -h (-htmlFormat) Use HMTL formatting for output
  -H (-hex) Show tag ID number in hexadecimal
  -htmlDump[OFFSET] Generate HTML-format binary dump
  -j[=JSONFILE] (-json) Export/import tags in JSON format
  -l (-long) Use long 2-line output format
  -L (-latin) Use Windows Latin1 encoding
  -lang [LANG] Set current language
  -listItem INDEX Extract specific item from a list
  -n (--printConv) No print conversion
  -p FMTFILE (-printFormat) Print output in specified format
  -php Export tags as a PHP Array
  -s[NUM] (-short) Short output format
  -S (-veryShort) Very short output format
  -sep STR (-separator) Set separator string for list items
  -sort Sort output alphabetically
  -struct Enable output of structured information
  -t (-tab) Output in tab-delimited list format
  -T (-table) Output in tabular format
  -v[NUM] (-verbose) Print verbose messages
  -w[+|!] EXT (-textOut) Write (or overwrite!) output text files
  -W[+|!] FMT (-tagOut) Write output text file for each tag
  -Wext EXT (-tagOutExt) Write only specified file types with -W
  -X (-xmlFormat) Use RDF/XML output format
</code></pre>
<p> Processing control </p>
<pre><code>  -a (-duplicates) Allow duplicate tags to be extracted
  -e (--composite) Do not calculate composite tags
  -ee (-extractEmbedded) Extract information from embedded files
  -ext EXT (-extension) Process files with specified extension
  -F[OFFSET] (-fixBase) Fix the base for maker notes offsets
  -fast[NUM] Increase speed for slow devices
  -fileOrder [-]TAG Set file processing order
  -i DIR (-ignore) Ignore specified directory name
  -if EXPR Conditionally process files
  -m (-ignoreMinorErrors) Ignore minor errors and warnings
  -o OUTFILE (-out) Set output file or directory name
  -overwrite_original Overwrite original by renaming tmp file
  -overwrite_original_in_place Overwrite original by copying tmp file
  -P (-preserve) Preserve date/time of original file
  -password PASSWD Password for processing protected files
  -progress[:[TITLE]] Show file progress count
  -q (-quiet) Quiet processing
  -r[.] (-recurse) Recursively process subdirectories
  -scanForXMP Brute force XMP scan
  -u (-unknown) Extract unknown tags
  -U (-unknown2) Extract unknown binary tags too
  -wm MODE (-writeMode) Set mode for writing/creating tags
  -z (-zip) Read/write compressed information
</code></pre>
<p> Other options </p>
<pre><code>  -@ ARGFILE Read command-line arguments from file
  -k (-pause) Pause before terminating
  -list[w|f|wf|g[NUM]|d|x] List various exiftool capabilities
  -ver Print exiftool version number
</code></pre>
<p> Special features </p>
<pre><code>  -geotag TRKFILE Geotag images from specified GPS log
  -globalTimeShift SHIFT Shift all formatted date/time values
  -use MODULE Add features from plug-in module
</code></pre>
<p> Utilities </p>
<pre><code>  -delete_original[!] Delete &quot;_original&quot; backups
  -restore_original Restore from &quot;_original&quot; backups
</code></pre>
<p> Advanced options </p>
<pre><code>  -api OPT[=VAL] Set ExifTool API option
  -common_args Define common arguments
  -config CFGFILE Specify configuration file name
  -echo[NUM] TEXT Echo text to stdout or stderr
  -execute[NUM] Execute multiple commands on one line
  -srcfile FMT Process a different source file
  -stay_open FLAG Keep reading -@ argfile even after EOF
  -userParam PARAM[=VAL] Set user parameter (API UserParam opt)
  -windowTitle TITLE Set console window title for each file
</code></pre>
<h3>Option Details</h3>
<p> <i>Tag operations</i> </p>
<dl>
<dt><code>-</code><i></i><font SIZE="-1"><i>TAG</i></font><i></i></dt>
<dd> <p> Extract information for the specified tag (eg. <code>&quot;-CreateDate&quot;</code>). Multiple tags may be specified in a single command. A tag name is the handle by which a piece of information is referenced. See Image::ExifTool::TagNames for documentation on available tag names. A tag name may include leading group names separated by colons (eg. <code>&quot;-EXIF:CreateDate&quot;</code>, or <code>&quot;-Doc1:XMP:Creator&quot;</code>), and each group name may be prefixed by a digit to specify family number (eg. <code>&quot;-1IPTC:City&quot;</code>). Use the <code>-listg</code> option to list available group names by family. </p>
<p> A special tag name of <code>&quot;All&quot;</code> may be used to indicate all meta information (ie. <code>-All</code>). This is particularly useful when a group name is specified to extract all information in a group (but beware that unless the <code>-a</code> option is also used, some tags in the group may be suppressed by same-named tags in other groups). The wildcard characters <code>&quot;?&quot;</code> and <code>&quot;*&quot;</code> may be used in a tag name to match any single character and zero or more characters respectively. <br />
&nbsp;<wbr>These may not be used in a group name, with the exception that a group name of <code>&quot;*&quot;</code> (or <code>&quot;All&quot;</code>) may be used to extract all instances of a tag (as if <code>-a</code> was used). Note that arguments containing wildcards must be quoted on the command line of most systems to prevent shell globbing. </p>
<p> A <code>&quot;#&quot;</code> may be appended to the tag name to disable the print conversion on a per-tag basis (see the <code>-n</code> option). This may also be used when writing or copying tags. </p>
<p> If no tags are specified, all available information is extracted (as if <code>&quot;-All&quot;</code> had been specified). </p>
<p> Note: Descriptions, not tag names, are shown by default when extracting information. Use the <code>-s</code> option to see the tag names instead. </p>
 </dd>
<dt><code>--</code><i></i><font SIZE="-1"><i>TAG</i></font><i></i></dt>
<dd> <p> Exclude specified tag from extracted information. Same as the <code>-x</code> option. Group names and wildcards are permitted as described above for <code>-TAG</code>. Once excluded from the output, a tag may not be re-included by a subsequent option. May also be used following a <code>-tagsFromFile</code> option to exclude tags from being copied (when redirecting to another tag, it is the source tag that should be excluded), or to exclude groups from being deleted when deleting all information (eg. <code>&quot;-all= --exif:all&quot;</code> deletes all but <font SIZE="-1">EXIF</font> information). But note that this will not exclude individual tags from a group delete (unless a family 2 group is specified, see note 4 below). Instead, individual tags may be recovered using the <code>-tagsFromFile</code> option (eg. <code>&quot;-all= -tagsfromfile @ -artist&quot;</code>). </p>
 </dd>
<dt><code>-</code><i></i><font SIZE="-1"><i>TAG</i></font><i></i>[+-]<code>=</code>[<i></i><font SIZE="-1"><i>VALUE</i></font><i></i>]</dt>
<dd> <p> Write a new value for the specified tag (eg. <code>&quot;-comment=wow&quot;</code>), or delete the tag if no <i></i><font SIZE="-1"><i>VALUE</i></font><i></i> is given (eg. <code>&quot;-comment=&quot;</code>). <code>&quot;+=&quot;</code> and <code>&quot;-=&quot;</code> are used to add or remove existing entries from a list, or to shift date/time values (see Image::ExifTool::Shift.pl and note 6 below for more details). <code>&quot;+=&quot;</code> may also be used to increment numerical values (or decrement if <i></i><font SIZE="-1"><i>VALUE</i></font><i></i> is negative), and <code>&quot;-=&quot;</code> may be used to conditionally delete or replace a tag (see ``<font SIZE="-1">WRITING EXAMPLES&#8217;&#8216;</font> for examples). </p>
<p> <i></i><font SIZE="-1"><i>TAG</i></font><i></i> may contain one or more leading family 0, 1 or 2 group names, prefixed by optional family numbers, and separated colons. If no group name is specified, the tag is created in the preferred group, and updated in any other location where a same-named tag already exists. The preferred group is the first group in the following list where <i></i><font SIZE="-1"><i>TAG</i></font><i></i> is valid: 1) <font SIZE="-1">EXIF, 2</font>) <font SIZE="-1">IPTC, 3</font>) <font SIZE="-1">XMP.</font> </p>
<p> The wildcards <code>&quot;*&quot;</code> and <code>&quot;?&quot;</code> may be used in tag names to assign the same value to multiple tags. When specified with wildcards, ``unsafe&#8217;&#8216; tags are not written. A tag name of <code>&quot;All&quot;</code> is equivalent to <code>&quot;*&quot;</code> (except that it doesn&#8217;t require quoting, while arguments with wildcards do on systems with shell globbing), and is often used when deleting all metadata (ie. <code>&quot;-All=&quot;</code>) or an entire group (eg. <code>&quot;-GROUP:All=&quot;</code>, see note 4 below). Note that not all groups are deletable, and that the <font SIZE="-1">JPEG APP14 </font>``Adobe&#8217;&#8216; group is not removed by default with <code>&quot;-All=&quot;</code> because it may affect the appearance of the image. However, this will remove color space information, so the colors may be affected (but this may be avoided by copying back the tags defined by the ColorSpaceTags shortcut). Use the <code>-listd</code> option for a complete list of deletable groups, and see note 5 below regarding the ``<font SIZE="-1">APP&#8217;&#8216;</font> groups. Also, within an image some groups may be contained within others, and these groups are removed if the containing group is deleted: </p>
<pre><code>  JPEG Image:
  - Deleting EXIF or IFD0 also deletes ExifIFD, GlobParamIFD,
    GPS, IFD1, InteropIFD, MakerNotes, PrintIM and SubIFD.
  - Deleting ExifIFD also deletes InteropIFD and MakerNotes.
  - Deleting Photoshop also deletes IPTC.
  TIFF Image:
  - Deleting EXIF only removes ExifIFD which also deletes
    InteropIFD and MakerNotes.
</code></pre>
<p> Notes: </p>
<p> 1) <code>Many tag values may be assigned in a single command</code>. If two assignments affect the same tag, the latter takes precedence (except for list-type tags, for which both values are written). </p>
<p> 2) In general, MakerNotes tags are considered ``Permanent&#8217;&#8216;, and may be edited but not created or deleted individually. This avoids many potential problems, including the inevitable compatibility problems with <font SIZE="-1">OEM</font> software which may be very inflexible about the information it expects to find in the maker notes. </p>
<p> 3) Changes to <font SIZE="-1">PDF</font> files by ExifTool are reversible (by deleting the update with <code>&quot;-PDF-update:all=&quot;</code>) because the original information is never actually deleted from the file. So ExifTool alone may not be used to securely edit metadata in <font SIZE="-1">PDF</font> files. </p>
<p> 4) Specifying <code>&quot;-GROUP:all=&quot;</code> deletes the entire group as a block only if a single family 0 or 1 group is specified. Otherwise all deletable tags in the specified group(s) are removed individually, and in this case is it possible to exclude individual tags from a mass delete. For example, <code>&quot;-time:all --Exif:Time:All&quot;</code> removes all deletable Time tags except those in the <font SIZE="-1">EXIF. </font> This difference also applies if family 2 is specified when deleting all groups. For example, <code>&quot;-2all:all=&quot;</code> deletes tags individually, while <code>&quot;-all:all=&quot;</code> deletes entire blocks. </p>
<p> 5) The ``<font SIZE="-1">APP&#8217;&#8216;</font> group names (``<font SIZE="-1">APP0&#8217;&#8216;</font> through ``<font SIZE="-1">APP15&#8217;&#8216;</font>) are used to delete <font SIZE="-1">JPEG</font> application segments which are not associated with another deletable group. For example, specifying <code>&quot;-APP14:All=&quot;</code> will <font SIZE="-1">NOT</font> delete the <font SIZE="-1">APP14 </font>``Adobe&#8217;&#8216; segment because this is accomplished with <code>&quot;-Adobe:All&quot;</code>. </p>
<p> 6) When shifting a value, the shift is applied to the original value of the tag, overriding any other values previously assigned to the tag on the same command line. To shift a date/time value and copy it to another tag in the same operation, use the <code>-globalTimeShift</code> option. </p>
<p> Special feature: Integer values may be specified in hexadecimal with a leading <code>&quot;0x&quot;</code>, and simple rational values may be specified as fractions. </p>
 </dd>
<dt><code>-</code><i></i><font SIZE="-1"><i>TAG</i></font><i></i>&lt;=<i></i><font SIZE="-1"><i>DATFILE</i></font><i></i> or <code>-</code><i></i><font SIZE="-1"><i>TAG</i></font><i></i>&lt;=<i></i><font SIZE="-1"><i>FMT</i></font><i></i></dt>
<dd> <p> Set the value of a tag from the contents of file <i></i><font SIZE="-1"><i>DATFILE</i></font><i></i>. The file name may also be given by a <i></i><font SIZE="-1"><i>FMT</i></font><i></i> string where <code>%d</code>, <code>%f</code> and <code>%e</code> represent the directory, file name and extension of the original <i></i><font SIZE="-1"><i>FILE</i></font><i></i> (see the <code>-w</code> option for more details). Note that quotes are required around this argument to prevent shell redirection since it contains a <code>&quot;&lt;&quot;</code> symbol. If <i></i><font SIZE="-1"><i>DATFILE</i></font><i></i>/<i></i><font SIZE="-1"><i>FMT</i></font><i></i> is not provided, the effect is the same as <code>&quot;-TAG=&quot;</code>, and the tag is simply deleted. <code>&quot;+&lt;=&quot;</code> or <code>&quot;-&lt;=&quot;</code> may also be used to add or delete specific list entries, or to shift date/time values. </p>
 </dd>
<dt><code>-tagsFromFile</code><i></i><font SIZE="-1"><i>SRCFILE</i></font><i></i> or <i></i><font SIZE="-1"><i>FMT</i></font><i></i></dt>
<dd> <p> Copy tag values from <i></i><font SIZE="-1"><i>SRCFILE</i></font><i></i> to <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. Tag names on the command line after this option specify the tags to be copied, or excluded from the copy. Wildcards are permitted in these tag names. If no tags are specified, then all possible tags (see note 1 below) from the source file are copied to same-named tags in the preferred location of the output file (the same as specifying <code>&quot;-all&quot;</code>). More than one <code>-tagsFromFile</code> option may be used to copy tags from multiple files. </p>
<p> By default, this option will update any existing and writable same-named tags in the output <i></i><font SIZE="-1"><i>FILE</i></font><i></i>, but will create new tags only in their preferred groups. This allows some information to be automatically transferred to the appropriate group when copying between images of different formats. However, if a group name is specified for a tag then the information is written only to this group (unless redirected to another group, see below). If <code>&quot;All&quot;</code> is used as a group name, then the specified tag(s) are written to the same family 1 group they had in the source file (ie. the same specific location, like ExifIFD or XMP-dc). For example, the common operation of copying all writable tags to the same specific locations in the output <i></i><font SIZE="-1"><i>FILE</i></font><i></i> is achieved by adding <code>&quot;-all:all&quot;</code>. A different family may be specified by adding a leading family number to the group name (eg. <code>&quot;-0all:all&quot;</code> preserves the same general location, like <font SIZE="-1">EXIF</font> or <font SIZE="-1">XMP</font>). </p>
<p> <i></i><font SIZE="-1"><i>SRCFILE</i></font><i></i> may be the same as <i></i><font SIZE="-1"><i>FILE</i></font><i></i> to move information around within a single file. In this case, <code>&quot;@&quot;</code> may be used to represent the source file (ie. <code>&quot;-tagsFromFile @&quot;</code>), permitting this feature to be used for batch processing multiple files. Specified tags are then copied from each file in turn as it is rewritten. For advanced batch use, the source file name may also be specified using a <i></i><font SIZE="-1"><i>FMT</i></font><i></i> string in which <code>%d</code>, <code>%f</code> and <code>%e</code> represent the directory, file name and extension of <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. See <code>-w</code> option for <i></i><font SIZE="-1"><i>FMT</i></font><i></i> string examples. </p>
<p> A powerful redirection feature allows a destination tag to be specified for each copied tag. With this feature, information may be written to a tag with a different name or group. This is done using &quot;&#8216;-<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&lt;<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>&#8216;`` or &#8216;&#8216;&#8216;-<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>&gt;<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&#8216;&quot; on the command line after <code>-tagsFromFile</code>, and causes the value of <i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i> to be copied from <i></i><font SIZE="-1"><i>SRCFILE</i></font><i></i> and written to <i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i> in <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. Note that this argument must be quoted to prevent shell redirection, and there is no <code>&quot;=&quot;</code> sign as when assigning new values. Source and/or destination tags may be prefixed by a group name and/or suffixed by <code>&quot;#&quot;</code>. Wildcards are allowed in both the source and destination tag names. A destination group and/or tag name of <code>&quot;All&quot;</code> or <code>&quot;*&quot;</code> writes to the same family 1 group and/or tag name as the source. If no destination group is specified, the information is written to the preferred group. Whitespace around the <code>&quot;&gt;&quot;</code> or <code>&quot;&lt;&quot;</code> is ignored. As a convenience, <code>&quot;-tagsFromFile @&quot;</code> is assumed for any redirected tags which are specified without a prior <code>-tagsFromFile</code> option. Copied tags may also be added or deleted from a list with arguments of the form &quot;&#8216;-<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>+&lt;<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&#8216;`` or &#8216;&#8216;&#8216;-<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>-&lt;<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&#8216;&quot;. </p>
<p> An extension of the redirection feature allows strings involving tag names to be used on the right hand side of the <code>&quot;&lt;&quot;</code> symbol with the syntax &quot;&#8216;-<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&lt;<i></i><font SIZE="-1"><i>STR</i></font><i></i>&#8216;&quot;, where tag names in <i></i><font SIZE="-1"><i>STR</i></font><i></i> are prefixed with a <code>&quot;$&quot;</code> symbol. See the <code>-p</code> option for more details about this syntax. Strings starting with a <code>&quot;=&quot;</code> sign must insert a single space after the <code>&quot;&lt;&quot;</code> to avoid confusion with the <code>&quot;&lt;=&quot;</code> operator which sets the tag value from the contents of a file. A single space at the start of the string is removed if it exists, but all other whitespace in the string is preserved. See note 8 below about using shortcuts or wildcards with the redirection feature. </p>
<p> See ``<font SIZE="-1">COPYING EXAMPLES&#8217;&#8216;</font> for examples using <code>-tagsFromFile</code>. </p>
<p> Notes: </p>
<p> 1) Some tags (generally tags which may affect the appearance of the image) are considered ``unsafe&#8217;&#8216; to write, and are only copied if specified explicitly (ie. no wildcards). See the tag name documentation for more details about ``unsafe&#8217;&#8216; tags. </p>
<p> 2) Be aware of the difference between excluding a tag from being copied (--<i></i><font SIZE="-1"><i>TAG</i></font><i></i>), and deleting a tag (-<i></i><font SIZE="-1"><i>TAG</i></font><i></i>=). Excluding a tag prevents it from being copied to the destination image, but deleting will remove a pre-existing tag from the image. </p>
<p> 3) The maker note information is copied as a block, so it isn&#8217;t affected like other information by subsequent tag assignments on the command line, and individual makernote tags may not be excluded from a block copy. Also, since the PreviewImage referenced from the maker notes may be rather large, it is not copied, and must be transferred separately if desired. </p>
<p> 4) The order of operations is to copy all specified tags at the point of the <code>-tagsFromFile</code> option in the command line. Any tag assignment to the right of the <code>-tagsFromFile</code> option is made after all tags are copied. For example, new tag values are set in the order One, Two, Three then Four with this command: </p>
<pre><code>    exiftool -One=1 -tagsFromFile s.jpg -Two -Four=4 -Three d.jpg
</code></pre>
<p> This is significant in the case where an overlap exists between the copied and assigned tags because later operations may override earlier ones. </p>
<p> 5) The normal behaviour of copied tags differs subtly from that of assigned tags for list-type tags. When copying to a list, each copied tag overrides any previous operations on the list. While this avoids duplicate list items when copying groups of tags from a file containing redundant information, it also prevents values of different tags from being copied into the same list when this is the intent. So a <code>-addTagsFromFile</code> option is provided which allows copying of multiple tags into the same list. eg) </p>
<pre><code>    exiftool -addtagsfromfile @ '-subject&lt;make' '-subject&lt;model' ...
</code></pre>
<p> Similarly, <code>-addTagsFromFile</code> must be used when conditionally replacing a tag to prevent overriding earlier conditions. </p>
<p> Other than these differences, the <code>-tagsFromFile</code> and <code>-addTagsFromFile</code> options are equivalent. </p>
<p> 6) The <code>-a</code> option (allow duplicate tags) is always in effect when copying tags from <i></i><font SIZE="-1"><i>SRCFILE</i></font><i></i>. </p>
<p> 7) Structured tags are copied by default when copying tags. See the <code>-struct</code> option for details. </p>
<p> 8) With the redirection feature, copying a tag directly (ie. &quot;&#8216;-<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&lt;<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>&#8216;``) is not the same as interpolating its value inside a string (ie. &#8216;&#8216;&#8216;-<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&lt;$<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>&#8216;&quot;) for shortcut tags or tag names containing wildcards. When copying directly, the values of each matching source tag are copied individually to the destination tag (as if multiple redirection arguments were used). However, when interpolated inside a string, the values of shortcut tags are concatenated, and wildcards are not allowed. </p>
 </dd>
<dt><code>-x</code><i></i><font SIZE="-1"><i>TAG</i></font><i></i> (<code>-exclude</code>)</dt>
<dd> <p> Exclude the specified tag. There may be multiple <code>-x</code> options. This has the same effect as --<i></i><font SIZE="-1"><i>TAG</i></font><i></i> on the command line. See the --<i></i><font SIZE="-1"><i>TAG</i></font><i></i> documentation above for a complete description. </p>
 </dd></dl>
<p> <i>Input-output text formatting</i> </p>
<p> Note that trailing spaces are removed from extracted values for most output text formats. The exceptions are <code>&quot;-b&quot;</code>, <code>&quot;-csv&quot;</code>, <code>&quot;-j&quot;</code> and <code>&quot;-X&quot;</code>. </p>
<dl>
<dt><code>-args</code> (<code>-argFormat</code>)</dt>
<dd> <p> Output information in the form of exiftool arguments, suitable for use with the <code>-@</code> option when writing. May be combined with the <code>-G</code> option to include group names. This feature may be used to effectively copy tags between images, but allows the metadata to be altered by editing the intermediate file (<code>&quot;out.args&quot;</code> in this example): </p>
<pre><code>    exiftool -args -G1 --filename --directory src.jpg &gt; out.args
    exiftool -@ out.args dst.jpg
</code></pre>
<p> Note: Be careful when copying information with this technique since it is easy to write tags which are normally considered ``unsafe&#8217;&#8216;. For instance, the FileName and Directory tags are excluded in the example above to avoid renaming and moving the destination file. Also note that the second command above will produce warning messages for any tags which are not writable. </p>
<p> As well, the <code>-sep</code> option should be used when reading back to maintain separate list items, and the <code>-struct</code> option may be used when extracting to preserve structured <font SIZE="-1">XMP</font> information. </p>
 </dd>
<dt><code>-b</code> (<code>-binary</code>)</dt>
<dd> <p> Output requested metadata in binary format without tag names or descriptions. This option is mainly used for extracting embedded images or other binary data, but it may also be useful for some text strings since control characters (such as newlines) are not replaced by &#8216;.&#8216; as they are in the default output. List items are separated by a newline when extracted with the <code>-b</code> option. May be combined with <code>&quot;-j&quot;</code>, <code>&quot;-php&quot;</code> or <code>&quot;-X&quot;</code> to extract binary data in <font SIZE="-1">JSON, PHP</font> or <font SIZE="-1">XML</font> format. </p>
 </dd>
<dt><code>-c</code><i></i><font SIZE="-1"><i>FMT</i></font><i></i> (<code>-coordFormat</code>)</dt>
<dd> <p> Set the print format for <font SIZE="-1">GPS</font> coordinates. <i></i><font SIZE="-1"><i>FMT</i></font><i></i> uses the same syntax as the <code>&quot;printf&quot;</code> format string. The specifiers correspond to degrees, minutes and seconds in that order, but minutes and seconds are optional. For example, the following table gives the output for the same coordinate using various formats: </p>
<pre><code>            FMT Output
    ------------------- ------------------
    &quot;%d deg %d' %.2f&quot;\&quot; 54 deg 59' 22.80&quot; (default for reading)
    &quot;%d %d %.8f&quot; 54 59 22.80000000 (default for copying)
    &quot;%d deg %.4f min&quot; 54 deg 59.3800 min
    &quot;%.6f degrees&quot; 54.989667 degrees
</code></pre>
<p> Notes: </p>
<p> 1) To avoid loss of precision, the default coordinate format is different when copying tags using the <code>-tagsFromFile</code> option. </p>
<p> 2) If the hemisphere is known, a reference direction (N, S, E or W) is appended to each printed coordinate, but adding a <code>&quot;+&quot;</code> to the format specifier (eg. <code>&quot;%+.6f&quot;</code>) prints a signed coordinate instead. </p>
<p> 3) This print formatting may be disabled with the <code>-n</code> option to extract coordinates as signed decimal degrees. </p>
 </dd>
<dt><code>-charset</code> [[<i></i><font SIZE="-1"><i>TYPE</i></font><i></i>=]<i></i><font SIZE="-1"><i>CHARSET</i></font><i></i>]</dt>
<dd> <p> If <i></i><font SIZE="-1"><i>TYPE</i></font><i></i> is <code>&quot;ExifTool&quot;</code> or not specified, this option sets the ExifTool character encoding for output tag values when reading and input values when writing. The default ExifTool encoding is <code>&quot;UTF8&quot;</code>. If no <i></i><font SIZE="-1"><i>CHARSET</i></font><i></i> is given, a list of available character sets is returned. Valid <i></i><font SIZE="-1"><i>CHARSET</i></font><i></i> values are: </p>
<pre><code>    CHARSET Alias(es) Description
    ---------- --------------- ----------------------------------
    UTF8 cp65001, UTF-8 UTF-8 characters (default)
    Latin cp1252, Latin1 Windows Latin1 (West European)
    Latin2 cp1250 Windows Latin2 (Central European)
    Cyrillic cp1251, Russian Windows Cyrillic
    Greek cp1253 Windows Greek
    Turkish cp1254 Windows Turkish
    Hebrew cp1255 Windows Hebrew
    Arabic cp1256 Windows Arabic
    Baltic cp1257 Windows Baltic
    Vietnam cp1258 Windows Vietnamese
    Thai cp874 Windows Thai
    MacRoman cp10000, Roman Macintosh Roman
    MacLatin2 cp10029 Macintosh Latin2 (Central Europe)
    MacCyrillic cp10007 Macintosh Cyrillic
    MacGreek cp10006 Macintosh Greek
    MacTurkish cp10081 Macintosh Turkish
    MacRomanian cp10010 Macintosh Romanian
    MacIceland cp10079 Macintosh Icelandic
    MacCroatian cp10082 Macintosh Croatian
</code></pre>
<p> <i></i><font SIZE="-1"><i>TYPE</i></font><i></i> may be <code>&quot;FileName&quot;</code> to specify the encoding of file names on the command line (ie. <i></i><font SIZE="-1"><i>FILE</i></font><i></i> arguments). In Windows, this triggers use of wide-character i/o routines, thus providing support for Unicode file names. See the ``<font SIZE="-1">WINDOWS UNICODE FILE NAMES&#8217;&#8216;</font> section below for details. </p>
<p> Other values of <i></i><font SIZE="-1"><i>TYPE</i></font><i></i> listed below are used to specify the internal encoding of various meta information formats. </p>
<pre><code>    TYPE Description Default
    --------- ------------------------------------------- -------
    EXIF Internal encoding of EXIF &quot;ASCII&quot; strings (none)
    ID3 Internal encoding of ID3v1 information Latin
    IPTC Internal IPTC encoding to assume when Latin
                IPTC:CodedCharacterSet is not defined
    Photoshop Internal encoding of Photoshop IRB strings Latin
    QuickTime Internal encoding of QuickTime strings MacRoman
    RIFF Internal encoding of RIFF strings 0
</code></pre>
<p> See &lt;<a rel="nofollow" href="http://owl.phy.queensu.ca/~phil/exiftool/faq.html#Q10">http://owl.phy.queensu.ca/~phil/exiftool/faq.html#Q10</a>&gt; for more information about coded character sets, and the Image::ExifTool Options for more details about the <code>-charset</code> settings. </p>
 </dd>
<dt><code>-csv</code>[=<i></i><font SIZE="-1"><i>CSVFILE</i></font><i></i>]</dt>
<dd> <p> Export information in <font SIZE="-1">CSV</font> format, or import information if <i></i><font SIZE="-1"><i>CSVFILE</i></font><i></i> is specified. When importing, the <font SIZE="-1">CSV</font> file must be in exactly the same format as the exported file. The first row of the <i></i><font SIZE="-1"><i>CSVFILE</i></font><i></i> must be the ExifTool tag names (with optional group names) for each column of the file, and values must be separated by commas. A special ``SourceFile&#8217;&#8216; column specifies the files associated with each row of information (and a SourceFile of ``*&#8216;&#8216; may be used to define default tags to be imported for all files). The following examples demonstrate basic use of this option: </p>
<pre><code>    # generate CSV file with common tags from all images in a directory
    exiftool -common -csv dir &gt; out.csv
    # update metadata for all images in a directory from CSV file
    exiftool -csv=a.csv dir
</code></pre>
<p> Empty values are ignored when importing. Also, FileName and Directory columns are ignored if they exist (ie. ExifTool will not attempt to write these tags with a <font SIZE="-1">CSV</font> import). To force a tag to be deleted, use the <code>-f</code> option and set the value to ``-&#8216;&#8216; in the <font SIZE="-1">CSV</font> file (or to the MissingTagValue if this <font SIZE="-1">API</font> option was used). Multiple databases may be imported in a single command. </p>
<p> When exporting a <font SIZE="-1">CSV</font> file, the <code>-g</code> or <code>-G</code> option to add group names to the tag headings. If the <code>-a</code> option is used to allow duplicate tag names, the duplicate tags are only included in the <font SIZE="-1">CSV</font> output if the column headings are unique. Adding the <code>-G4</code> option ensures a unique column heading for each tag. When exporting specific tags, the <font SIZE="-1">CSV</font> columns are arranged in the same order as the specified tags provided the column headings exactly match the specified tag names, otherwise the columns are sorted in alphabetical order. </p>
<p> When importing from a <font SIZE="-1">CSV</font> file, only files specified on the command line are processed. Any extra entries in the <font SIZE="-1">CSV</font> file are ignored. </p>
<p> List-type tags are stored as simple strings in a <font SIZE="-1">CSV</font> file, but the <code>-sep</code> option may be used to split them back into separate items when importing. </p>
<p> Special feature: <code>-csv</code>+=<i></i><font SIZE="-1"><i>CSVFILE</i></font><i></i> may be used to add items to existing lists. This affects only list-type tags. Also applies to the <code>-j</code> option. </p>
<p> Note that this option is fundamentally different than all other output format options because it requires information from all input files to be buffered in memory before the output is written. This may result in excessive memory usage when processing a very large number of files with a single command. Also, it makes this option incompatible with the <code>-w</code> option. </p>
 </dd>
<dt><code>-d</code><i></i><font SIZE="-1"><i>FMT</i></font><i></i> (<code>-dateFormat</code>)</dt>
<dd> <p> Set the format for date/time tag values. The specifics of the <i></i><font SIZE="-1"><i>FMT</i></font><i></i> syntax are system dependent --- consult the <code>&quot;strftime&quot;</code> man page on your system for details. The default format is equivalent to ``%Y:%m:%d <code>%H:</code>%M:%S&#8217;&#8216;. This option has no effect on date-only or time-only tags and ignores timezone information if present. Only one <code>-d</code> option may be used per command. Requires POSIX::strptime or Time::Piece for the inversion conversion when writing. </p>
 </dd>
<dt><code>-D</code> (<code>-decimal</code>)</dt>
<dd> <p> Show tag <font SIZE="-1">ID</font> number in decimal when extracting information. </p>
 </dd>
<dt><code>-E</code>, <code>-ex</code> (<code>-escapeHTML</code>, <code>-escapeXML</code>)</dt>
<dd> <p> Escape characters in output values for <font SIZE="-1">HTML </font>(<code>-E</code>) or <font SIZE="-1">XML </font>(<code>-ex</code>). For <font SIZE="-1">HTML,</font> all characters with Unicode code points above U+007F are escaped as well as the following 5 characters: &amp; (&amp;amp;) &#8216; (&amp;#39;) &quot; (&amp;quot;) &gt; (&amp;gt;) and &lt; (&amp;lt;). For <font SIZE="-1">XML,</font> only these 5 characters are escaped. The <code>-E</code> option is implied with <code>-h</code>, and <code>-ex</code> is implied with <code>-X</code>. The inverse conversion is applied when writing tags. </p>
 </dd>
<dt><code>-f</code> (<code>-forcePrint</code>)</dt>
<dd> <p> Force printing of tags even if their values are not found. This option only applies when specific tags are requested on the command line (ie. not with wildcards or by <code>&quot;-all&quot;</code>). With this option, a dash (<code>&quot;-&quot;</code>) is printed for the value of any missing tag, but the dash may be changed via the <font SIZE="-1">API</font> MissingTagValue option. May also be used to add a &#8216;flags&#8217; attribute to the <code>-listx</code> output, or to allow tags to be deleted when writing with the <code>-csv</code>=<i></i><font SIZE="-1"><i>CSVFILE</i></font><i></i> feature. </p>
 </dd>
<dt><code>-g</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>][:<i></i><font SIZE="-1"><i>NUM</i></font><i></i>...] (<code>-groupHeadings</code>)</dt>
<dd> <p> Organize output by tag group. <i></i><font SIZE="-1"><i>NUM</i></font><i></i> specifies a group family number, and may be 0 (general location), 1 (specific location), 2 (category), 3 (document number) or 4 (instance number). <code>-g0</code> is assumed if a family number is not specified, and family numbers may be added wherever <code>-g</code> is mentioned in the documentation. Multiple families may be specified by separating them with colons. By default the resulting group name is simplified by removing any leading <code>&quot;Main:&quot;</code> and collapsing adjacent identical group names, but this can be avoided by placing a colon before the first family number (eg. <code>-g:3:1</code>). Use the <code>-listg</code> option to list group names for a specified family. </p>
 </dd>
<dt><code>-G</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>][:<i></i><font SIZE="-1"><i>NUM</i></font><i></i>...] (<code>-groupNames</code>)</dt>
<dd> <p> Same as <code>-g</code> but print group name for each tag. <code>-G0</code> is assumed if <i></i><font SIZE="-1"><i>NUM</i></font><i></i> is not specified. May be combined with a number of other options to add group names to the output. Note that <i></i><font SIZE="-1"><i>NUM</i></font><i></i> may be added wherever <code>-G</code> is mentioned in the documentation. See the <code>-g</code> option above for details. </p>
 </dd>
<dt><code>-h</code> (<code>-htmlFormat</code>)</dt>
<dd> <p> Use <font SIZE="-1">HTML</font> table formatting for output. Implies the <code>-E</code> option. The formatting options <code>-D</code>, <code>-H</code>, <code>-g</code>, <code>-G</code>, <code>-l</code> and <code>-s</code> may be used in combination with <code>-h</code> to influence the <font SIZE="-1">HTML</font> format. </p>
 </dd>
<dt><code>-H</code> (<code>-hex</code>)</dt>
<dd> <p> Show tag <font SIZE="-1">ID</font> number in hexadecimal when extracting information. </p>
 </dd>
<dt><code>-htmlDump</code>[<i></i><font SIZE="-1"><i>OFFSET</i></font><i></i>]</dt>
<dd> <p> Generate a dynamic web page containing a hex dump of the <font SIZE="-1">EXIF</font> information. This can be a very powerful tool for low-level analysis of <font SIZE="-1">EXIF</font> information. The <code>-htmlDump</code> option is also invoked if the <code>-v</code> and <code>-h</code> options are used together. The verbose level controls the maximum length of the blocks dumped. An <i></i><font SIZE="-1"><i>OFFSET</i></font><i></i> may be given to specify the base for displayed offsets. If not provided, the <font SIZE="-1">EXIF/TIFF</font> base offset is used. Use <code>-htmlDump0</code> for absolute offsets. Currently only <font SIZE="-1">EXIF/TIFF</font> and <font SIZE="-1">JPEG</font> information is dumped, but the -u option can be used to give a raw hex dump of other file formats. </p>
 </dd>
<dt><code>-j</code>[=<i></i><font SIZE="-1"><i>JSONFILE</i></font><i></i>] (<code>-json</code>)</dt>
<dd> <p> Use <font SIZE="-1">JSON </font>(JavaScript Object Notation) formatting for console output, or import <font SIZE="-1">JSON</font> file if <i></i><font SIZE="-1"><i>JSONFILE</i></font><i></i> is specified. This option may be combined with <code>-g</code> to organize the output into objects by group, or <code>-G</code> to add group names to each tag. List-type tags with multiple items are output as <font SIZE="-1">JSON</font> arrays unless <code>-sep</code> is used. By default <font SIZE="-1">XMP</font> structures are flattened into individual tags in the <font SIZE="-1">JSON</font> output, but the original structure may be preserved with the <code>-struct</code> option (this also causes all list-type <font SIZE="-1">XMP</font> tags to be output as <font SIZE="-1">JSON</font> arrays, otherwise single-item lists are output as simple strings). The <code>-a</code> option is implied if the <code>-g</code> or <code>-G</code> options are used, otherwise it is ignored and duplicate tags are suppressed. Adding the <code>-D</code> or <code>-H</code> option changes tag values to <font SIZE="-1">JSON</font> objects with ``val&#8217;&#8216; and ``id&#8217;&#8216; fields, and adding <code>-l</code> adds a ``desc&#8217;&#8216; field, and a ``num&#8217;&#8216; field if the numerical value is different from the converted ``val&#8217;&#8216;. The <code>-b</code> option may be added to output binary data, encoded in base64 if necessary (indicated by ``base64:&#8216;&#8216; as the first 7 bytes of the value). The <font SIZE="-1">JSON</font> output is <font SIZE="-1">UTF-8</font> regardless of any <code>-L</code> or <code>-charset</code> option setting, but the <font SIZE="-1">UTF-8</font> validation is disabled if a character set other than <font SIZE="-1">UTF-8</font> is specified. </p>
<p> If <i></i><font SIZE="-1"><i>JSONFILE</i></font><i></i> is specified, the file is imported and the tag definitions from the file are used to set tag values on a per-file basis. The special ``SourceFile&#8217;&#8216; entry in each <font SIZE="-1">JSON</font> object associates the information with a specific target file. An object with a missing SourceFile or a SourceFile of ``*&#8216;&#8216; defines default tags for all target files. The imported <font SIZE="-1">JSON</font> file must have the same format as the exported <font SIZE="-1">JSON</font> files with the exception that the <code>-g</code> option is not compatible with the import file format (use <code>-G</code> instead). Additionally, tag names in the input <font SIZE="-1">JSON</font> file may be suffixed with a <code>&quot;#&quot;</code> to disable print conversion. </p>
<p> Unlike <font SIZE="-1">CSV</font> import, empty values are not ignored, and will cause an empty value to be written if supported by the specific metadata type. Tags are deleted by using the <code>-f</code> option and setting the tag value to ``-&#8216;&#8216; (or to the MissingTagValue setting if this <font SIZE="-1">API</font> option was used). Importing with <code>-j</code>+=<i></i><font SIZE="-1"><i>JSONFILE</i></font><i></i> causes new values to be added to existing lists. </p>
 </dd>
<dt><code>-l</code> (<code>-long</code>)</dt>
<dd> <p> Use long 2-line Canon-style output format. Adds a description and unconverted value (if it is different from the converted value) to the <font SIZE="-1">XML, JSON</font> or <font SIZE="-1">PHP</font> output when <code>-X</code>, <code>-j</code> or <code>-php</code> is used. May also be combined with <code>-listf</code>, <code>-listr</code> or <code>-listwf</code> to add descriptions of the file types. </p>
 </dd>
<dt><code>-L</code> (<code>-latin</code>)</dt>
<dd> <p> Use Windows Latin1 encoding (cp1252) for output tag values instead of the default <font SIZE="-1">UTF-8. </font> When writing, <code>-L</code> specifies that input text values are Latin1 instead of <font SIZE="-1">UTF-8. </font> Equivalent to <code>&quot;-charset latin&quot;</code>. </p>
 </dd>
<dt><code>-lang</code> [<i></i><font SIZE="-1"><i>LANG</i></font><i></i>]</dt>
<dd> <p> Set current language for tag descriptions and converted values. <i></i><font SIZE="-1"><i>LANG</i></font><i></i> is <code>&quot;de&quot;</code>, <code>&quot;fr&quot;</code>, <code>&quot;ja&quot;</code>, etc. Use <code>-lang</code> with no other arguments to get a list of available languages. The default language is <code>&quot;en&quot;</code> if <code>-lang</code> is not specified. Note that tag/group names are always English, independent of the <code>-lang</code> setting, and translation of warning/error messages has not yet been implemented. May also be combined with <code>-listx</code> to output descriptions in one language only. </p>
<p> By default, ExifTool uses <font SIZE="-1">UTF-8</font> encoding for special characters, but the the <code>-L</code> or <code>-charset</code> option may be used to invoke other encodings. </p>
<p> Currently, the language support is not complete, but users are welcome to help improve this by submitting their own translations. To submit a set of translations, first use the <code>-listx</code> option and redirect the output to a file to generate an <font SIZE="-1">XML</font> tag database, then add entries for other languages, zip this file, and email it to phil at owl.phy.queensu.ca for inclusion in ExifTool. </p>
<p> Note: ExifTool uses Unicode::LineBreak if available to help preserve the column alignment of the plain text output for languages with a variable-width character set. </p>
 </dd>
<dt><code>-listItem</code><i></i><font SIZE="-1"><i>INDEX</i></font><i></i></dt>
<dd> <p> For list-type tags, this causes only the item with the specified index to be extracted. <i></i><font SIZE="-1"><i>INDEX</i></font><i></i> is 0 for the first item in the list. Negative indices may also be used to reference items from the end of the list. Has no effect on single-valued tags. Also applies to tag values when copying, and in <code>-if</code> conditions. </p>
 </dd>
<dt><code>-n</code> (<code>--printConv</code>)</dt>
<dd> <p> Disable print conversion for all tags. By default, extracted values are converted to a more human-readable format, but the <code>-n</code> option disables this conversion, revealing the machine-readable values. For example: </p>
<pre><code>    &gt; exiftool -Orientation -S a.jpg
    Orientation: Rotate 90 CW
    &gt; exiftool -Orientation -S -n a.jpg
    Orientation: 6
</code></pre>
<p> The print conversion may also be disabled on a per-tag basis by suffixing the tag name with a <code>&quot;#&quot;</code> character: </p>
<pre><code>    &gt; exiftool -Orientation# -Orientation -S a.jpg
    Orientation: 6
    Orientation: Rotate 90 CW
</code></pre>
<p> These techniques may also be used to disable the inverse print conversion when writing. For example, the following commands all have the same effect: </p>
<pre><code>    &gt; exiftool -Orientation='Rotate 90 CW' a.jpg
    &gt; exiftool -Orientation=6 -n a.jpg
    &gt; exiftool -Orientation#=6 a.jpg
</code></pre>
 </dd>
<dt><code>-p</code><i></i><font SIZE="-1"><i>FMTFILE</i></font><i></i> or <i></i><font SIZE="-1"><i>STR</i></font><i></i> (<code>-printFormat</code>)</dt>
<dd> <p> Print output in the format specified by the given file or string (and ignore other format options). Tag names in the format file or string begin with a <code>&quot;$&quot;</code> symbol and may contain a leading group names and/or a trailing <code>&quot;#&quot;</code>. Case is not significant. Braces <code>&quot;{}&quot;</code> may be used around the tag name to separate it from subsequent text. Use <code>$$</code> to represent a <code>&quot;$&quot;</code> symbol, and <code>$/</code> for a newline. Multiple <code>-p</code> options may be used, each contributing a line of text to the output. Lines beginning with <code>&quot;#[HEAD]&quot;</code> and <code>&quot;#[TAIL]&quot;</code> are output only for the first and last processed files respectively. Lines beginning with <code>&quot;#[BODY]&quot;</code> and lines not beginning with <code>&quot;#&quot;</code> are output for each processed file. Other lines beginning with <code>&quot;#&quot;</code> are ignored. For example, this format file: </p>
<pre><code>    # this is a comment line
    #[HEAD]-- Generated by ExifTool $exifToolVersion --
    File: $FileName - $DateTimeOriginal
    (f/$Aperture, ${ShutterSpeed}s, ISO $EXIF:ISO)
    #[TAIL]-- end --
</code></pre>
<p> with this command: </p>
<pre><code>    exiftool -p test.fmt a.jpg b.jpg
</code></pre>
<p> produces output like this: </p>
<pre><code>    -- Generated by ExifTool 10.40 --
    File: a.jpg - 2003:10:31 15:44:19
    (f/5.6, 1/60s, ISO 100)
    File: b.jpg - 2006:05:23 11:57:38
    (f/8.0, 1/13s, ISO 100)
    -- end --
</code></pre>
<p> When <code>-ee</code> (<code>-extractEmbedded</code>) is combined with <code>-p</code>, embedded documents are effectively processed as separate input files. </p>
<p> If a specified tag does not exist, a minor warning is issued and the line with the missing tag is not printed. However, the <code>-f</code> option may be used to set the value of missing tags to &#8216;-&#8216; (but this may be configured via the MissingTagValue <font SIZE="-1">API</font> option), or the <code>-m</code> option may be used to ignore minor warnings and leave the missing values empty. </p>
<p> An advanced formatting feature allows an arbitrary Perl expression to be applied to the value of any tag by placing it inside the braces after the tag name, separated by a semicolon. The expression acts on the value of the tag through the default input variable (<code>$_</code>), and has access to the full ExifTool <font SIZE="-1">API</font> through the current ExifTool object (<code>$self</code>). It may contain any valid Perl code, including translation (<code>&quot;tr///&quot;</code>) and substitution (<code>&quot;s///&quot;</code>) operations, but note that braces within the expression must be balanced. The example below prints the camera Make with spaces translated to underlines, and multiple consecutive underlines replaced by a single underline: </p>
<pre><code>    exiftool -p '${make;tr/ /_/;s/__+/_/g}' image.jpg
</code></pre>
<p> A default expression of <code>&quot;tr(/\\?*:|&quot;&lt;&gt;\0)()d&quot;</code> is assumed if the expression is empty. This removes the characters / \ ? * : | &lt; &gt; and null from the printed value. (These characters are illegal in Windows file names, so this feature is useful if tag values are used in file names.) </p>
 </dd>
<dt><code>-php</code></dt>
<dd> <p> Format output as a <font SIZE="-1">PHP</font> Array. The <code>-g</code>, <code>-G</code>, <code>-D</code>, <code>-H</code>, <code>-l</code>, <code>-sep</code> and <code>-struct</code> options combine with <code>-php</code>, and duplicate tags are handled in the same way as with the <code>-json</code> option. As well, the <code>-b</code> option may be added to output binary data. Here is a simple example showing how this could be used in a <font SIZE="-1">PHP</font> script: </p>
<pre><code>    &lt;?php
    eval('$array=' . `exiftool -php -q image.jpg`);
    print_r($array);
    ?&gt;
</code></pre>
 </dd>
<dt><code>-s</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>] (<code>-short</code>)</dt>
<dd> <p> Short output format. Prints tag names instead of descriptions. Add <i></i><font SIZE="-1"><i>NUM</i></font><i></i> or up to 3 <code>-s</code> options for even shorter formats: </p>
<pre><code>    -s1 or -s - print tag names instead of descriptions
    -s2 or -s -s - no extra spaces to column-align values
    -s3 or -s -s -s - print values only (no tag names)
</code></pre>
<p> Also effective when combined with <code>-t</code>, <code>-h</code>, <code>-X</code> or <code>-listx</code> options. </p>
 </dd>
<dt><code>-S</code> (<code>-veryShort</code>)</dt>
<dd> <p> Very short format. The same as <code>-s2</code> or two <code>-s</code> options. Tag names are printed instead of descriptions, and no extra spaces are added to column-align values. </p>
 </dd>
<dt><code>-sep</code><i></i><font SIZE="-1"><i>STR</i></font><i></i> (<code>-separator</code>)</dt>
<dd> <p> Specify separator string for items in list-type tags. When reading, the default is to join list items with ``, &#8216;&#8216;. When writing, this option causes values assigned to list-type tags to be split into individual items at each substring matching <i></i><font SIZE="-1"><i>STR</i></font><i></i> (otherwise they are not split by default). Space characters in <i></i><font SIZE="-1"><i>STR</i></font><i></i> match zero or more whitespace characters in the value. </p>
<p> Note that an empty separator (&quot;&quot;) is allowed, and will join items with no separator when reading, or split the value into individual characters when writing. </p>
 </dd>
<dt><code>-sort</code>, <code>--sort</code></dt>
<dd> <p> Sort output by tag description, or by tag name if the <code>-s</code> option is used. When sorting by description, the sort order will depend on the <code>-lang</code> option setting. Without the <code>-sort</code> option, tags appear in the order they were specified on the command line, or if not specified, the order they were extracted from the file. By default, tags are organized by groups when combined with the <code>-g</code> or <code>-G</code> option, but this grouping may be disabled with <code>--sort</code>. </p>
 </dd>
<dt><code>-struct</code>, <code>--struct</code></dt>
<dd> <p> Output structured <font SIZE="-1">XMP</font> information instead of flattening to individual tags. This option works well when combined with the <font SIZE="-1">XML </font>(<code>-X</code>) and <font SIZE="-1">JSON </font>(<code>-j</code>) output formats. For other output formats, the structures are serialized into the same format as when writing structured information (see &lt;<a rel="nofollow" href="http://owl.phy.queensu.ca/~phil/exiftool/struct.html">http://owl.phy.queensu.ca/~phil/exiftool/struct.html</a>&gt; for details). When copying, structured tags are copied by default unless <code>--struct</code> is used to disable this feature (although flattened tags may still be copied by specifying them individually unless <code>-struct</code> is used). These options have no effect when assigning new values since both flattened and structured tags may always be used when writing. </p>
 </dd>
<dt><code>-t</code> (<code>-tab</code>)</dt>
<dd> <p> Output a tab-delimited list of description/values (useful for database import). May be combined with <code>-s</code> to print tag names instead of descriptions, or <code>-S</code> to print tag values only, tab-delimited on a single line. The <code>-t</code> option may also be used to add tag table information to the <code>-X</code> option output. </p>
 </dd>
<dt><code>-T</code> (<code>-table</code>)</dt>
<dd> <p> Output tag values in table form. Equivalent to <code>-t -S -q -f</code>. </p>
 </dd>
<dt><code>-v</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>] (<code>-verbose</code>)</dt>
<dd> <p> Print verbose messages. <i></i><font SIZE="-1"><i>NUM</i></font><i></i> specifies the level of verbosity in the range 0-5, with higher numbers being more verbose. If <i></i><font SIZE="-1"><i>NUM</i></font><i></i> is not given, then each <code>-v</code> option increases the level of verbosity by 1. With any level greater than 0, most other options are ignored and normal console output is suppressed unless specific tags are extracted. Using <code>-v0</code> causes the console output buffer to be flushed after each line (which may be useful to avoid delays when piping exiftool output), and prints the name of each processed file when writing. Also see the <code>-progress</code> option. </p>
 </dd>
<dt><code>-w</code>[+|!] <i></i><font SIZE="-1"><i>EXT</i></font><i></i> or <i></i><font SIZE="-1"><i>FMT</i></font><i></i> (<code>-textOut</code>)</dt>
<dd> <p> Write console output to files with names ending in <i></i><font SIZE="-1"><i>EXT</i></font><i></i>, one for each source file. The output file name is obtained by replacing the source file extension (including the &#8216;.&#8216;) with the specified extension (and a &#8216;.&#8216; is added to the start of <i></i><font SIZE="-1"><i>EXT</i></font><i></i> if it doesn&#8217;t already contain one). Alternatively, a <i></i><font SIZE="-1"><i>FMT</i></font><i></i> string may be used to give more control over the output file name and directory. In the format string, <code>%d</code>, <code>%f</code> and <code>%e</code> represent the directory, filename and extension of the source file, and <code>%c</code> represents a copy number which is automatically incremented if the file already exists. <code>%d</code> includes the trailing &#8216;/&#8216; if necessary, but <code>%e</code> does not include the leading &#8216;.&#8216;. For example: </p>
<pre><code>    -w %d%f.txt # same effect as &quot;-w txt&quot;
    -w dir/%f_%e.out # write files to &quot;dir&quot; as &quot;FILE_EXT.out&quot;
    -w dir2/%d%f.txt # write to &quot;dir2&quot;, keeping dir structure
    -w a%c.txt # write to &quot;a.txt&quot; or &quot;a1.txt&quot; or &quot;a2.txt&quot;...
</code></pre>
<p> Existing files will not be overwritten unless an exclamation point is added to the option name (ie. <code>-w!</code> or <code>-textOut!</code>), or a plus sign to append to the existing file (ie. <code>-w+</code> or <code>-textOut+</code>). Both may be used (ie. <code>-w+!</code> or <code>-textOut+!</code>) to overwrite output files that didn&#8217;t exist before the command was run, and append the output from multiple source files. For example, to write one output file for all source files in each directory: </p>
<pre><code>    exiftool -filename -createdate -T -w+! %d/out.txt -r DIR
</code></pre>
<p> Capitalized format codes <code>%D</code>, <code>%F</code>, <code>%E</code> and <code>%C</code> provide slightly different alternatives to the lower case versions. <code>%D</code> does not include the trailing &#8216;/&#8216;, <code>%F</code> is the full filename including extension, <code>%E</code> includes the leading &#8216;.&#8216;, and <code>%C</code> increments the count for each processed file (see below). </p>
<p> Notes: </p>
<p> 1) In a Windows <font SIZE="-1">BAT</font> file the <code>&quot;%&quot;</code> character is represented by <code>&quot;%%&quot;</code>, so an argument like <code>&quot;%d%f.txt&quot;</code> is written as <code>&quot;%%d%%f.txt&quot;</code>. </p>
<p> 2) If the argument for <code>-w</code> does not contain a valid format code (eg. <code>%f</code>), then it is interpreted as a file extension. It is not possible to specify a simple filename as an argument --- creating a single output file from multiple source files is typically done by shell redirection, ie) </p>
<pre><code>    exiftool FILE1 FILE2 ... &gt; out.txt
</code></pre>
<p> But if necessary, an empty format code may be used to force the argument to be interpreted as a format string, and the same result may be obtained without the use of shell redirection: </p>
<pre><code>    exiftool -w+! %0fout.txt FILE1 FILE2 ...
</code></pre>
<p> Advanced features: </p>
<p> A substring of the original file name, directory or extension may be taken by specifying a field width immediately following the &#8216;%&#8216; character. If the width is negative, the substring is taken from the end. The substring position (characters to ignore at the start or end of the string) may be given by a second optional value after a decimal point. For example: </p>
<pre><code>    Input File Name Format Specifier Output File Name
    ---------------- ---------------- ----------------
    Picture-123.jpg %7f.txt Picture.txt
    Picture-123.jpg %-.4f.out Picture.out
    Picture-123.jpg %7f.%-3f Picture.123
    Picture-123a.jpg Meta%-3.1f.txt Meta123.txt
</code></pre>
<p> For <code>%d</code> and <code>%D</code>, the field width/position specifiers may be applied to the directory levels instead of substring position by using a colon instead of a decimal point in the format specifier. For example: </p>
<pre><code>    Source Dir Format Result Notes
    ------------ ------ ---------- ------------------
    pics/2012/02 %2:d pics/2012/ take top 2 levels
    pics/2012/02 %-:1d pics/2012/ up one directory level
    pics/2012/02 %:1d 2012/02/ ignore top level
    pics/2012/02 %1:1d 2012/ take 1 level after top
    pics/2012/02 %-1:D 02 bottom level folder name
    /Users/phil %:2d phil/ ignore top 2 levels
</code></pre>
<p> (Note that the root directory counts as one level when an absolute path is used as in the last example above.) </p>
<p> For <code>%c</code>, these modifiers have a different effects. If a field width is given, the copy number is padded with zeros to the specified width. A leading &#8216;-&#8216; adds a dash before the copy number, and a &#8216;+&#8216; adds an underline. By default, the copy number is omitted from the first file of a given name, but this can be changed by adding a decimal point to the modifier. For example: </p>
<pre><code>    -w A%-cZ.txt # AZ.txt, A-1Z.txt, A-2Z.txt ...
    -w B%5c.txt # B.txt, B00001.txt, B00002.txt ...
    -w C%.c.txt # C0.txt, C1.txt, C2.txt ...
    -w D%-.c.txt # D-0.txt, D-1.txt, D-2.txt ...
    -w E%-.4c.txt # E-0000.txt, E-0001.txt, E-0002.txt ...
    -w F%-.4nc.txt # F-0001.txt, F-0002.txt, F-0003.txt ...
    -w G%+c.txt # G.txt, G_1.txt G_2.txt ...
    -w H%-lc.txt # H.txt, H-b.txt, H-c.txt ...
    -w I.%.3uc.txt # I.AAA.txt, I.AAB.txt, I.AAC.txt ...
</code></pre>
<p> A special feature allows the copy number to be incremented for each processed file by using <code>%C</code> (upper case) instead of <code>%c</code>. This allows a sequential number to be added to output file names, even if the names are different. For <code>%C</code>, a copy number of zero is not omitted as it is with <code>%c</code>. The number before the decimal place gives the starting index, the number after the decimal place gives the field width. The following examples show the output filenames when used with the command <code>&quot;exiftool rose.jpg star.jpg jet.jpg ...&quot;</code>: </p>
<pre><code>    -w %C%f.txt # 0rose.txt, 1star.txt, 2jet.txt
    -w %f-%10C.txt # rose-10.txt, star-11.txt, jet-12.txt
    -w %.3C-%f.txt # 000-rose.txt, 001-star.txt, 002-jet.txt
    -w %57.4C%f.txt # 0057rose.txt, 0058star.txt, 0059jet.txt
</code></pre>
<p> All format codes may be modified by &#8216;l&#8217; or &#8216;u&#8217; to specify lower or upper case respectively (ie. <code>%le</code> for a lower case file extension). When used to modify <code>%c</code> or <code>%C</code>, the numbers are changed to an alphabetical base (see example H above). Also, <code>%c</code> and <code>%C</code> may be modified by &#8216;n&#8217; to count using natural numbers starting from 1, instead of 0 (see example F above). </p>
<p> This same <i></i><font SIZE="-1"><i>FMT</i></font><i></i> syntax is used with the <code>-o</code> and <code>-tagsFromFile</code> options, although <code>%c</code> and <code>%C</code> are only valid for output file names. </p>
 </dd>
<dt><code>-W</code>[!|+] <i></i><font SIZE="-1"><i>FMT</i></font><i></i> (<code>-tagOut</code>)</dt>
<dd> <p> This enhanced version of the <code>-w</code> option allows a separate output file to be created for each extracted tag. The differences between <code>-W</code> and <code>-w</code> are as follows: </p>
<p> 1) With <code>-W</code>, a new output file is created for each extracted tag. </p>
<p> 2) <code>-W</code> supports three additional format codes: <code>%t</code>, <code>%g</code> and <code>%s</code> represent the tag name, group name, and suggested extension for the output file (based on the format of the data). The <code>%g</code> code may be followed by a single digit to specify the group family number (eg. <code>%g1</code>), otherwise family 0 is assumed. The substring width/position/case specifiers may be used with these format codes in exactly the same way as with <code>%f</code> and <code>%e</code>. </p>
<p> 3) The argument for <code>-W</code> is interpreted as a file name if it contains no format codes. (For <code>-w</code>, this would be a file extension.) This change allows a simple file name to be specified, which, when combined with the append feature, provides a method to write metadata from multiple source files to a single output file without the need for shell redirection. </p>
<p> 4) Adding the <code>-v</code> option to <code>-W</code> generates a list of the tags and output file names instead of giving a verbose dump of the entire file. (Unless appending all output to one file for each source file by using <code>-W+</code> with an output file <i></i><font SIZE="-1"><i>FMT</i></font><i></i> that does not contain <code>%t</code>, <code>$g</code> or <code>%s</code>.) </p>
<p> 5) Individual list items are stored in separate files when <code>-W</code> is combined with <code>-b</code>, but note that for separate files to be created <code>%c</code> or <code>%C</code> must be used in <i></i><font SIZE="-1"><i>FMT</i></font><i></i> to give the files unique names. </p>
 </dd>
<dt><code>-Wext</code><i></i><font SIZE="-1"><i>EXT</i></font><i></i>, <code>--Wext</code><i></i><font SIZE="-1"><i>EXT</i></font><i></i> (<code>-tagOutExt</code>)</dt>
<dd> <p> This option is used to specify the type of output file(s) written by the <code>-W</code> option. An output file is written only if the suggested extension matches <i></i><font SIZE="-1"><i>EXT</i></font><i></i>. Multiple <code>-Wext</code> options may be used to write more than one type of file. Use <code>--Wext</code> to write all but the specified type(s). </p>
 </dd>
<dt><code>-X</code> (<code>-xmlFormat</code>)</dt>
<dd> <p> Use ExifTool-specific <font SIZE="-1">RDF/XML</font> formatting for console output. Implies the <code>-a</code> option, so duplicate tags are extracted. The formatting options <code>-b</code>, <code>-D</code>, <code>-H</code>, <code>-l</code>, <code>-s</code>, <code>-sep</code>, <code>-struct</code> and <code>-t</code> may be used in combination with <code>-X</code> to affect the output, but note that the tag <font SIZE="-1">ID </font>(<code>-D</code>, <code>-H</code> and <code>-t</code>), binary data (<code>-b</code>) and structured output (<code>-struct</code>) options are not effective for the short output (<code>-s</code>). Another restriction of <code>-s</code> is that only one tag with a given group and name may appear in the output. Note that the tag <font SIZE="-1">ID</font> options (<code>-D</code>, <code>-H</code> and <code>-t</code>) will produce non-standard <font SIZE="-1">RDF/XML</font> unless the <code>-l</code> option is also used. </p>
<p> By default, <code>-X</code> outputs flattened tags, so <code>-struct</code> should be added if required to preserve <font SIZE="-1">XMP</font> structures. List-type tags with multiple values are formatted as an <font SIZE="-1">RDF</font> Bag, but they are combined into a single string when <code>-s</code> or <code>-sep</code> is used. Using <code>-L</code> changes the <font SIZE="-1">XML</font> encoding from ``<font SIZE="-1">UTF-8&#8217;&#8216;</font> to ``windows-1252&#8217;&#8216;. Other <code>-charset</code> settings change the encoding only if there is a corresponding standard <font SIZE="-1">XML</font> character set. The <code>-b</code> option causes binary data values to be written, encoded in base64 if necessary. The <code>-t</code> option adds tag table information to the output (table <code>&quot;name&quot;</code>, decimal tag <code>&quot;id&quot;</code>, and <code>&quot;index&quot;</code> for cases where multiple conditional tags exist with the same <font SIZE="-1">ID</font>). </p>
<p> Note: This output is <font SIZE="-1">NOT</font> the same as <font SIZE="-1">XMP</font> because it uses dynamically-generated property names corresponding to the ExifTool tag names, and not the standard <font SIZE="-1">XMP</font> properties. To write <font SIZE="-1">XMP</font> instead, use the <code>-o</code> option with an <font SIZE="-1">XMP</font> extension for the output file. </p>
 </dd></dl>
<p> <i>Processing control</i> </p>
<dl>
<dt><code>-a</code>, <code>--a</code> (<code>-duplicates</code>, <code>--duplicates</code>)</dt>
<dd> <p> Allow (<code>-a</code>) or suppress (<code>--a</code>) duplicate tag names to be extracted. By default, duplicate tags are suppressed unless the <code>-ee</code> or <code>-X</code> options are used or the Duplicates option is enabled in the configuration file. This option also has an affect when writing to allow duplicate Warning messages to be shown. </p>
 </dd>
<dt><code>-e</code> (<code>--composite</code>)</dt>
<dd> <p> Extract existing tags only --- don&#8217;t calculate composite tags. </p>
 </dd>
<dt><code>-ee</code> (<code>-extractEmbedded</code>)</dt>
<dd> <p> Extract information from embedded documents in <font SIZE="-1">EPS</font> files, embedded <font SIZE="-1">EPS</font> information and <font SIZE="-1">JPEG</font> and Jpeg2000 images in <font SIZE="-1">PDF</font> files, embedded <font SIZE="-1">MPF</font> images in <font SIZE="-1">JPEG</font> and <font SIZE="-1">MPO</font> files, streaming metadata in <font SIZE="-1">AVCHD</font> videos, and the resource fork of Mac <font SIZE="-1">OS</font> files. Implies the <code>-a</code> option. Use <code>-g3</code> or <code>-G3</code> to identify the originating document for extracted information. Embedded documents containing sub-documents are indicated with dashes in the family 3 group name. (eg. <code>&quot;Doc2-3&quot;</code> is the 3rd sub-document of the 2nd embedded document.) Note that this option may increase processing time substantially, especially for <font SIZE="-1">PDF</font> files with many embedded images. </p>
 </dd>
<dt><code>-ext</code><i></i><font SIZE="-1"><i>EXT</i></font><i></i>, <code>--ext</code><i></i><font SIZE="-1"><i>EXT</i></font><i></i> (<code>-extension</code>)</dt>
<dd> <p> Process only files with (<code>-ext</code>) or without (<code>--ext</code>) a specified extension. There may be multiple <code>-ext</code> and <code>--ext</code> options. <font SIZE="-1">EXT</font> may begin with a leading &#8216;.&#8216;, and case is not significant. <code>&quot;*&quot;</code> may be used to process files with any extension (or none at all), as in the last three examples: </p>
<pre><code>    exiftool -ext .JPG DIR # process only JPG files
    exiftool --ext cr2 --ext dng DIR # supported files but CR2/DNG
    exiftool -ext &quot;*&quot; DIR # process all files
    exiftool -ext &quot;*&quot; --ext xml DIR # process all but XML files
    exiftool -ext &quot;*&quot; --ext . DIR # all but those with no ext
</code></pre>
<p> Using this option has two main advantages over specifying <code>&quot;*.</code>EXT <code>&quot;</code> on the command line: 1) It applies to files in subdirectories when combined with the <code>-r</code> option. 2) The <code>-ext</code> option is case-insensitive, which is useful when processing files on case-sensitive filesystems. </p>
 </dd>
<dt><code>-F</code>[<i></i><font SIZE="-1"><i>OFFSET</i></font><i></i>] (<code>-fixBase</code>)</dt>
<dd> <p> Fix the base for maker notes offsets. A common problem with some image editors is that offsets in the maker notes are not adjusted properly when the file is modified. This may cause the wrong values to be extracted for some maker note entries when reading the edited file. This option allows an integer <i></i><font SIZE="-1"><i>OFFSET</i></font><i></i> to be specified for adjusting the maker notes base offset. If no <i></i><font SIZE="-1"><i>OFFSET</i></font><i></i> is given, ExifTool takes its best guess at the correct base. Note that exiftool will automatically fix the offsets for images which store original offset information (eg. newer Canon models). Offsets are fixed permanently if <code>-F</code> is used when writing <font SIZE="-1">EXIF</font> to an image. eg) </p>
<pre><code>    exiftool -F -exif:resolutionunit=inches image.jpg
</code></pre>
 </dd>
<dt><code>-fast</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]</dt>
<dd> <p> Increase speed of extracting information. With this option, ExifTool will not scan to the end of a <font SIZE="-1">JPEG</font> image to check for an <font SIZE="-1">AFCP</font> or PreviewImage trailer, or past the first comment in <font SIZE="-1">GIF</font> images or the audio/video data in <font SIZE="-1">WAV/AVI</font> files to search for additional metadata. These speed benefits are small when reading images directly from disk, but can be substantial if piping images through a network connection. For more substantial speed benefits, <code>-fast2</code> also causes exiftool to avoid extracting any <font SIZE="-1">EXIF</font> MakerNote information. <code>-fast3</code> avoids processing the file entirely, and returns only an initial guess at FileType and the pseudo System tags. </p>
 </dd>
<dt><code>-fileOrder</code> [-]<i></i><font SIZE="-1"><i>TAG</i></font><i></i></dt>
<dd> <p> Set file processing order according to the sorted value of the specified <i></i><font SIZE="-1"><i>TAG</i></font><i></i>. For example, to process files in order of date: </p>
<pre><code>    exiftool -fileOrder DateTimeOriginal DIR
</code></pre>
<p> Additional <code>-fileOrder</code> options may be added for secondary sort keys. Numbers are sorted numerically, and all other values are sorted alphabetically. The sort order may be reversed by prefixing the tag name with a <code>&quot;-&quot;</code> (eg. <code>&quot;-fileOrder -createdate&quot;</code>). Print conversion of the sorted values is disabled with the <code>-n</code> option, or a <code>&quot;#&quot;</code> appended to the tag name. Other formatting options (eg. <code>-d</code>) have no effect on the sorted values. Note that the <code>-fileOrder</code> option has a large performance impact since it involves an additional processing pass of each file. </p>
 </dd>
<dt><code>-i</code><i></i><font SIZE="-1"><i>DIR</i></font><i></i> (<code>-ignore</code>)</dt>
<dd> <p> Ignore specified directory name. <i></i><font SIZE="-1"><i>DIR</i></font><i></i> may be either an individual folder name, or a full path. If a full path is specified, it must match the Directory tag exactly to be ignored. Use multiple <code>-i</code> options to ignore more than one directory name. A special <i></i><font SIZE="-1"><i>DIR</i></font><i></i> value of <code>&quot;SYMLINKS&quot;</code> (case sensitive) may be specified to ignore symbolic links when the <code>-r</code> option is used. </p>
 </dd>
<dt><code>-if</code><i></i><font SIZE="-1"><i>EXPR</i></font><i></i></dt>
<dd> <p> Specify a condition to be evaluated before processing each <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. <i></i><font SIZE="-1"><i>EXPR</i></font><i></i> is a Perl-like logic expression containing tag names prefixed by <code>&quot;$&quot;</code> symbols. It is evaluated with the tags from each <i></i><font SIZE="-1"><i>FILE</i></font><i></i> in turn, and the file is processed only if the expression returns true. Unlike Perl variable names, tag names are not case sensitive and may contain a hyphen. As well, tag names may have a leading group names separated by colons, and/or a trailing <code>&quot;#&quot;</code> character to disable print conversion. The expression <code>$GROUP:all</code> evaluates to 1 if any tag exists in the specified <code>&quot;GROUP&quot;</code>, or 0 otherwise (see note 2 below). When multiple <code>-if</code> options are used, all conditions must be satisfied to process the file. Returns an exit status of 1 if all files fail the condition. Below are a few examples: </p>
<pre><code>    # extract shutterspeed from all Canon images in a directory
    exiftool -shutterspeed -if '$make eq &quot;Canon&quot;' dir
    # add one hour to all images created on or after Apr. 2, 2006
    exiftool -alldates+=1 -if '$CreateDate ge &quot;2006:04:02&quot;' dir
    # set EXIF ISO value if possible, unless it is set already
    exiftool '-exif:iso&lt;iso' -if 'not $exif:iso' dir
    # find images containing a specific keyword (case insensitive)
    exiftool -if '$keywords =~ /harvey/i' -filename dir
</code></pre>
<p> Notes: </p>
<p> 1) The <code>-n</code> and <code>-b</code> options also apply to tags used in <i></i><font SIZE="-1"><i>EXPR</i></font><i></i>. </p>
<p> 2) Some binary data blocks are not extracted unless specified explicitly. These tags are not available for use in the <code>-if</code> condition unless they are also specified on the command line. The alternative is to use the <code>$GROUP:all</code> syntax. (eg. Use <code>$exif:all</code> instead of <code>$exif</code> in <i></i><font SIZE="-1"><i>EXPR</i></font><i></i> to test for the existence of <font SIZE="-1">EXIF</font> tags.) </p>
<p> 3) Tags in the string are interpolated the same way as with <code>-p</code> before the expression is evaluated. In this interpolation, <code>$/</code> is converted to a newline and <code>$$</code> represents a single <code>&quot;$&quot;</code> symbol (so Perl variables, if used, require a double <code>&quot;$&quot;</code>). </p>
<p> 4) The condition may only test tags from the file being processed. To process one file based on tags from another, two steps are required. For example, to process <font SIZE="-1">XMP</font> sidecar files in directory <code>&quot;DIR&quot;</code> based on tags from the associated <font SIZE="-1">NEF:</font> </p>
<pre><code>    exiftool -if EXPR -p '$directory/$filename' -ext nef DIR &gt; nef.txt
    exiftool -@ nef.txt -srcfile %d%f.xmp ...
</code></pre>
<p> 5) The <code>-a</code> option has no effect on the evaluation of the expression, and the values of duplicate tags are accessible only by specifying a group name (such as a family 4 instance number, eg. <code>$Copy1:TAG</code>, <code>$Copy2:TAG</code>, etc). </p>
 </dd>
<dt><code>-m</code> (<code>-ignoreMinorErrors</code>)</dt>
<dd> <p> Ignore minor errors and warnings. This enables writing to files with minor errors and disables some validation checks which could result in minor warnings. Generally, minor errors/warnings indicate a problem which usually won&#8217;t result in loss of metadata if ignored. However, there are exceptions, so ExifTool leaves it up to you to make the final decision. Minor errors and warnings are indicated by ``[minor]&#8216;&#8216; at the start of the message. Warnings which affect processing when ignored are indicated by ``[Minor]&#8216;&#8216; (with a capital ``M&#8217;&#8216;). </p>
 </dd>
<dt><code>-o</code><i></i><font SIZE="-1"><i>OUTFILE</i></font><i></i> or <i></i><font SIZE="-1"><i>FMT</i></font><i></i> (<code>-out</code>)</dt>
<dd> <p> Set the output file or directory name when writing information. Without this option, when any ``real&#8217;&#8216; tags are written the original file is renamed to <code>&quot;FILE_original&quot;</code> and output is written to <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. When writing only FileName and/or Directory ``pseudo&#8217;&#8216; tags, <code>-o</code> causes the file to be copied instead of moved, but directories specified for either of these tags take precedence over that specified by the <code>-o</code> option. </p>
<p> <i></i><font SIZE="-1"><i>OUTFILE</i></font><i></i> may be <code>&quot;-&quot;</code> to write to stdout. The output file name may also be specified using a <i></i><font SIZE="-1"><i>FMT</i></font><i></i> string in which <code>%d</code>, <code>%f</code> and <code>%e</code> represent the directory, file name and extension of <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. Also, <code>%c</code> may be used to add a copy number. See the <code>-w</code> option for <i></i><font SIZE="-1"><i>FMT</i></font><i></i> string examples. </p>
<p> The output file is taken to be a directory name if it already exists as a directory or if the name ends with &#8216;/&#8216;. Output directories are created if necessary. Existing files will not be overwritten. Combining the <code>-overwrite_original</code> option with <code>-o</code> causes the original source file to be erased after the output file is successfully written. </p>
<p> A special feature of this option allows the creation of certain types of files from scratch, or with the metadata from another type of file. The following file types may be created using this technique: </p>
<pre><code>    XMP, EXIF, EXV, MIE, ICC/ICM, VRD, DR4
</code></pre>
<p> The output file type is determined by the extension of <i></i><font SIZE="-1"><i>OUTFILE</i></font><i></i> (specified as <code>&quot;-.EXT&quot;</code> when writing to stdout). The output file is then created from a combination of information in <i></i><font SIZE="-1"><i>FILE</i></font><i></i> (as if the <code>-tagsFromFile</code> option was used), and tag values assigned on the command line. If no <i></i><font SIZE="-1"><i>FILE</i></font><i></i> is specified, the output file may be created from scratch using only tags assigned on the command line. </p>
 </dd>
<dt><code>-overwrite_original</code></dt>
<dd> <p> Overwrite the original <i></i><font SIZE="-1"><i>FILE</i></font><i></i> (instead of preserving it by adding <code>&quot;_original&quot;</code> to the file name) when writing information to an image. Caution: This option should only be used if you already have separate backup copies of your image files. The overwrite is implemented by renaming a temporary file to replace the original. This deletes the original file and replaces it with the edited version in a single operation. When combined with <code>-o</code>, this option causes the original file to be deleted if the output file was successfully written (ie. the file is moved instead of copied). </p>
 </dd>
<dt><code>-overwrite_original_in_place</code></dt>
<dd> <p> Similar to <code>-overwrite_original</code> except that an extra step is added to allow the original file attributes to be preserved. For example, on a Mac this causes the original file creation date, type, creator, label color, icon, Finder tags and hard links to the file to be preserved (but note that the Mac <font SIZE="-1">OS</font> resource fork is always preserved unless specifically deleted with <code>&quot;-rsrc:all=&quot;</code>). This is implemented by opening the original file in update mode and replacing its data with a copy of a temporary file before deleting the temporary. The extra step results in slower performance, so the <code>-overwrite_original</code> option should be used instead unless necessary. </p>
 </dd>
<dt><code>-P</code> (<code>-preserve</code>)</dt>
<dd> <p> Preserve the filesystem modification date/time of the original file (<code>&quot;FileModifyDate&quot;</code>) when writing. Note that some filesystems store a creation date (<code>&quot;FileCreateDate&quot;</code>) which is not affected by this option. This creation date is preserved only on Windows systems where Win32API::File and Win32::API are available. For other systems, the <code>-overwrite_original_in_place</code> option may be used if necessary to preserve the creation date. This option is superseded by writing the FileModifyDate tag (and FileCreateDate in Windows). </p>
 </dd>
<dt><code>-password</code><i></i><font SIZE="-1"><i>PASSWD</i></font><i></i></dt>
<dd> <p> Specify password to allow processing of password-protected <font SIZE="-1">PDF</font> documents. If a password is required but not given, a warning is issued and the document is not processed. This option is ignored if a password is not required. </p>
 </dd>
<dt><code>-progress</code>[:[<i></i><font SIZE="-1"><i>TITLE</i></font><i></i>]]</dt>
<dd> <p> Show file progress count in messages. The progress count appears in brackets after the name of each processed file, and gives the current file number and the total number of files to be processed. Implies the <code>-v0</code> option if <i></i><font SIZE="-1"><i>TITLE</i></font><i></i> is not used, printing the name of each processed file when writing. When combined with the <code>-if</code> option, the total count includes all files before the condition is applied, but files that fail the condition will not have their names printed. </p>
<p> If followed by a colon (ie. <code>-progress:</code>), the console window title is set according to the specified <i></i><font SIZE="-1"><i>TITLE</i></font><i></i> string. If no <i></i><font SIZE="-1"><i>TITLE</i></font><i></i> is given, a default <i></i><font SIZE="-1"><i>TITLE</i></font><i></i> string of ``ExifTool <code>%p</code>%%&#8216;&#8216; is assumed. In the string, <code>%f</code> represents the file name, <code>%p</code> is the progress as a percent, <code>%r</code> is the progress as a ratio, and %% is a % character. May be combined with the normal <code>-progress</code> option to also show the progress count in console messages. (Note: This feature works on Mac/Linux only if stderr goes to the console.) </p>
 </dd>
<dt><code>-q</code> (<code>-quiet</code>)</dt>
<dd> <p> Quiet processing. One <code>-q</code> suppresses normal informational messages, and a second <code>-q</code> suppresses warnings as well. Error messages can not be suppressed, although minor errors may be downgraded to warnings with the <code>-m</code> option, which may then be suppressed with <code>&quot;-q -q&quot;</code>. </p>
 </dd>
<dt><code>-r</code>[.] (<code>-recurse</code>)</dt>
<dd> <p> Recursively process files in subdirectories. Only meaningful if <i></i><font SIZE="-1"><i>FILE</i></font><i></i> is a directory name. Subdirectories with names beginning with ``.&#8216;&#8216; are not processed unless ``.&#8216;&#8216; is added to the option name (ie. <code>-r.</code> or <code>-recurse.</code>). By default, exiftool will also follow symbolic links to directories if supported by the system, but this may be disabled with <code>&quot;-i SYMLINKS&quot;</code> (see the <code>-i</code> option for details). </p>
 </dd>
<dt><code>-scanForXMP</code></dt>
<dd> <p> Scan all files (even unsupported formats) for <font SIZE="-1">XMP</font> information unless found already. When combined with the <code>-fast</code> option, only unsupported file types are scanned. Warning: It can be time consuming to scan large files. </p>
 </dd>
<dt><code>-u</code> (<code>-unknown</code>)</dt>
<dd> <p> Extract values of unknown tags. Add another <code>-u</code> to also extract unknown information from binary data blocks. This option applies to tags with numerical tag <font SIZE="-1">ID</font>&#8216;s, and causes tag names like ``Exif_0xc5d9&#8217;&#8216; to be generated for unknown information. It has no effect on information types which have human-readable tag <font SIZE="-1">ID</font>&#8216;s (such as <font SIZE="-1">XMP</font>), since unknown tags are extracted automatically from these formats. </p>
 </dd>
<dt><code>-U</code> (<code>-unknown2</code>)</dt>
<dd> <p> Extract values of unknown tags as well as unknown information from some binary data blocks. This is the same as two <code>-u</code> options. </p>
 </dd>
<dt><code>-wm</code><i></i><font SIZE="-1"><i>MODE</i></font><i></i> (<code>-writeMode</code>)</dt>
<dd> <p> Set mode for writing/creating tags. <i></i><font SIZE="-1"><i>MODE</i></font><i></i> is a string of one or more characters from the list below. Write mode is <code>&quot;wcg&quot;</code> unless otherwise specified. </p>
<pre><code>    w - Write existing tags
    c - Create new tags
    g - create new Groups as necessary
</code></pre>
<p> For example, use <code>&quot;-wm cg&quot;</code> to only create new tags (and avoid editing existing ones). </p>
<p> The level of the group is the SubDirectory level in the metadata structure. For <font SIZE="-1">XMP</font> or <font SIZE="-1">IPTC</font> this is the full <font SIZE="-1">XMP/IPTC</font> block (the family 0 group), but for <font SIZE="-1">EXIF</font> this is the individual <font SIZE="-1">IFD </font>(the family 1 group). </p>
 </dd>
<dt><code>-z</code> (<code>-zip</code>)</dt>
<dd> <p> When reading, causes information to be extracted from .gz and .bz2 compressed images. (Only one image per archive. Requires gzip and bzip2 to be installed on the system.) When writing, causes compressed information to be written if supported by the metadata format. (eg. <font SIZE="-1">PNG</font> supports compressed textual metadata.) This option also disables the recommended padding in embedded <font SIZE="-1">XMP,</font> saving 2424 bytes when writing <font SIZE="-1">XMP</font> in a file. </p>
 </dd></dl>
<p> <i>Other options</i> </p>
<dl>
<dt><code>-@</code><i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i></dt>
<dd> <p> Read command-line arguments from the specified file. The file contains one argument per line (<font SIZE="-1">NOT</font> one option per line --- some options require additional arguments, and all arguments must be placed on separate lines). Blank lines and lines beginning with <code>&quot;#&quot;</code> are ignored. White space at the start of a line is removed. Normal shell processing of arguments is not performed, which among other things means that arguments should not be quoted and spaces are treated as any other character. <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i> may exist relative to either the current directory or the exiftool directory unless an absolute pathname is given. </p>
<p> For example, the following <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i> will set the value of Copyright to ``Copyright <font SIZE="-1">YYYY,</font> Phil Harvey&#8217;&#8216;, where ``<font SIZE="-1">YYYY&#8217;&#8216;</font> is the year of CreateDate: </p>
<pre><code>    -d
    %Y
    -copyright&lt;Copyright $createdate, Phil Harvey
</code></pre>
 </dd>
<dt><code>-k</code> (<code>-pause</code>)</dt>
<dd> <p> Pause with the message <code>&quot;-- press any key --&quot;</code> or <code>&quot;-- press RETURN --&quot;</code> (depending on your system) before terminating. This option is used to prevent the command window from closing when run as a Windows drag and drop application. </p>
 </dd>
<dt><code>-list</code>, <code>-listw</code>, <code>-listf</code>, <code>-listr</code>, <code>-listwf</code>, <code>-listg</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>], <code>-listd</code>, <code>-listx</code></dt>
<dd> <p> Print a list of all valid tag names (<code>-list</code>), all writable tag names (<code>-listw</code>), all supported file extensions (<code>-listf</code>), all recognized file extensions (<code>-listr</code>), all writable file extensions (<code>-listwf</code>), all tag groups [in a specified family] (<code>-listg</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]), all deletable tag groups (<code>-listd</code>), or an <font SIZE="-1">XML</font> database of tag details including language translations (<code>-listx</code>). The <code>-list</code>, <code>-listw</code> and <code>-listx</code> options may be followed by an additional argument of the form <code>&quot;-GROUP:All&quot;</code> to list only tags in a specific group, where <code>&quot;GROUP&quot;</code> is one or more family 0-2 group names (excepting <font SIZE="-1">EXIF IFD</font> groups) separated by colons. With <code>-listg</code>, <i></i><font SIZE="-1"><i>NUM</i></font><i></i> may be given to specify the group family, otherwise family 0 is assumed. The <code>-l</code> option may be combined with <code>-listf</code>, <code>-listr</code> or <code>-listwf</code> to add file descriptions to the list. The <code>-lang</code> option may be combined with <code>-listx</code> to output descriptions in a single language. Here are some examples: </p>
<pre><code>    -list # list all tag names
    -list -EXIF:All # list all EXIF tags
    -list -xmp:time:all # list all XMP tags relating to time
    -listw -XMP-dc:All # list all writable XMP-dc tags
    -listf # list all supported file extensions
    -listr # list all recognized file extensions
    -listwf # list all writable file extensions
    -listg1 # list all groups in family 1
    -listd # list all deletable groups
    -listx -EXIF:All # list database of EXIF tags in XML format
    -listx -XMP:All -s # list short XML database of XMP tags
</code></pre>
<p> When combined with <code>-listx</code>, the <code>-s</code> option shortens the output by omitting the descriptions and values (as in the last example above), and <code>-f</code> adds a &#8216;flags&#8217; attribute if applicable. The flags are formatted as a comma-separated list of the following possible values: Avoid, Binary, List, Mandatory, Permanent, Protected, Unknown and Unsafe (see the Tag Name documentation). For <font SIZE="-1">XMP</font> List tags, the list type (Alt, Bag or Seq) is added to the flags, and flattened structure tags are indicated by a Flattened flag. </p>
<p> Note that none of the <code>-list</code> options require an input <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. </p>
 </dd>
<dt><code>-ver</code></dt>
<dd> <p> Print exiftool version number. The <code>-v</code> option may be added to print addition system information (see the <font SIZE="-1">README</font> file of the full distribution for more details about optional libraries). </p>
 </dd></dl>
<p> <i>Special features</i> </p>
<dl>
<dt><code>-geotag</code><i></i><font SIZE="-1"><i>TRKFILE</i></font><i></i></dt>
<dd> <p> Geotag images from the specified <font SIZE="-1">GPS</font> track log file. Using the <code>-geotag</code> option is equivalent to writing a value to the <code>&quot;Geotag&quot;</code> tag. After the <code>-geotag</code> option has been specified, the value of the <code>&quot;Geotime&quot;</code> tag is written to define a date/time for the position interpolation. If <code>&quot;Geotime&quot;</code> is not specified, the value is copied from <code>&quot;DateTimeOriginal#&quot;</code> (the <code>&quot;#&quot;</code> is added to copy the unformatted value, avoiding potential conflicts with the <code>-d</code> option). For example, the following two commands are equivalent: </p>
<pre><code>    exiftool -geotag trk.log image.jpg
    exiftool -geotag trk.log &quot;-Geotime&lt;DateTimeOriginal#&quot; image.jpg
</code></pre>
<p> When the <code>&quot;Geotime&quot;</code> value is converted to <font SIZE="-1">UTC,</font> the local system timezone is assumed unless the date/time value contains a timezone. Writing <code>&quot;Geotime&quot;</code> causes the following tags to be written (provided they can be calculated from the track log, and they are supported by the destination metadata format): GPSLatitude, GPSLatitudeRef, GPSLongitude, GPSLongitudeRef, GPSAltitude, GPSAltitudeRef, GPSDateStamp, GPSTimeStamp, GPSDateTime, GPSTrack, GPSTrackRef, GPSSpeed, GPSSpeedRef, GPSImgDirection, GPSImgDirectionRef, GPSPitch and GPSRoll. By default, tags are created in <font SIZE="-1">EXIF,</font> and updated in <font SIZE="-1">XMP</font> only if they already exist. However, <code>&quot;EXIF:Geotime&quot;</code> or <code>&quot;XMP:Geotime&quot;</code> may be specified to write only <font SIZE="-1">EXIF</font> or <font SIZE="-1">XMP</font> tags respectively. Note that GPSPitch and GPSRoll are non-standard, and require user-defined tags in order to be written. </p>
<p> The <code>&quot;Geosync&quot;</code> tag may be used to specify a time correction which is applied to each <code>&quot;Geotime&quot;</code> value for synchronization with <font SIZE="-1">GPS</font> time. For example, the following command compensates for image times which are 1 minute and 20 seconds behind <font SIZE="-1">GPS:</font> </p>
<pre><code>    exiftool -geosync=+1:20 -geotag a.log DIR
</code></pre>
<p> <code>&quot;Geosync&quot;</code> must be set before <code>&quot;Geotime&quot;</code> (if specified) to be effective. Advanced <code>&quot;Geosync&quot;</code> features allow a linear time drift correction and synchronization from previously geotagged images. See ``geotag.html&#8217;&#8216; in the full ExifTool distribution for more information. </p>
<p> Multiple <code>-geotag</code> options may be used to concatenate <font SIZE="-1">GPS</font> track log data. Also, a single <code>-geotag</code> option may be used to load multiple track log files by using wildcards in the <i></i><font SIZE="-1"><i>TRKFILE</i></font><i></i> name, but note that in this case <i></i><font SIZE="-1"><i>TRKFILE</i></font><i></i> must be quoted on most systems (with the notable exception of Windows) to prevent filename expansion. For example: </p>
<pre><code>    exiftool -geotag &quot;TRACKDIR/*.log&quot; IMAGEDIR
</code></pre>
<p> Currently supported track file formats are <font SIZE="-1">GPX, NMEA RMC/GGA/GLL, KML, IGC,</font> Garmin <font SIZE="-1">XML</font> and <font SIZE="-1">TCX,</font> Magellan <font SIZE="-1">PMGNTRK,</font> Honeywell <font SIZE="-1">PTNTHPR,</font> Winplus Beacon text, and Bramor gEO log files. See ``<font SIZE="-1">GEOTAGGING EXAMPLES&#8217;&#8216;</font> for examples. Also see ``geotag.html&#8217;&#8216; in the full ExifTool distribution and the Image::ExifTool Options for more details and for information about geotag configuration options. </p>
 </dd>
<dt><code>-globalTimeShift</code><i></i><font SIZE="-1"><i>SHIFT</i></font><i></i></dt>
<dd> <p> Shift all formatted date/time values by the specified amount when reading. Does not apply to unformatted (<code>-n</code>) output. <i></i><font SIZE="-1"><i>SHIFT</i></font><i></i> takes the same form as the date/time shift when writing (see Image::ExifTool::Shift.pl for details), with a negative shift being indicated with a minus sign (<code>&quot;-&quot;</code>) at the start of the <i></i><font SIZE="-1"><i>SHIFT</i></font><i></i> string. For example: </p>
<pre><code>    # return all date/times, shifted back by 1 hour
    exiftool -globalTimeShift -1 -time:all a.jpg
    # set the file name from the shifted CreateDate (-1 day) for
    # all images in a directory
    exiftool &quot;-filename&lt;createdate&quot; -globaltimeshift &quot;-0:0:1 0:0:0&quot; \
        -d %Y%m%d-%H%M%S.%%e dir
</code></pre>
 </dd>
<dt><code>-use</code><i></i><font SIZE="-1"><i>MODULE</i></font><i></i></dt>
<dd> <p> Add features from specified plug-in <i></i><font SIZE="-1"><i>MODULE</i></font><i></i>. Currently, the <font SIZE="-1">MWG</font> module is the only plug-in module distributed with exiftool. This module adds read/write support for tags as recommended by the Metadata Working Group. To save typing, <code>&quot;-use MWG&quot;</code> is assumed if the <code>&quot;MWG&quot;</code> group is specified for any tag on the command line. See the <font SIZE="-1">MWG</font> Tags documentation for more details. Note that this option is not reversible, and remains in effect until the application terminates, even across the <code>&quot;-execute&quot;</code> option. </p>
 </dd></dl>
<p> <i>Utilities</i> </p>
<dl>
<dt><code>-restore_original</code></dt>
<dd>  </dd>
<dt><code>-delete_original</code>[!]</dt>
<dd> <p> These utility options automate the maintenance of the <code>&quot;_original&quot;</code> files created by exiftool. They have no effect on files without an <code>&quot;_original&quot;</code> copy. The <code>-restore_original</code> option restores the specified files from their original copies by renaming the <code>&quot;_original&quot;</code> files to replace the edited versions. For example, the following command restores the originals of all <font SIZE="-1">JPG</font> images in directory <code>&quot;DIR&quot;</code>: </p>
<pre><code>    exiftool -restore_original -ext jpg DIR
</code></pre>
<p> The <code>-delete_original</code> option deletes the <code>&quot;_original&quot;</code> copies of all files specified on the command line. Without a trailing <code>&quot;!&quot;</code> this option prompts for confirmation before continuing. For example, the following command deletes <code>&quot;a.jpg_original&quot;</code> if it exists, after asking ``Are you sure?&#8216;&#8216;: </p>
<pre><code>    exiftool -delete_original a.jpg
</code></pre>
<p> These options may not be used with other options to read or write tag values in the same command, but may be combined with options such <code>-ext</code>, <code>-if</code>, <code>-r</code>, <code>-q</code> and <code>-v</code>. </p>
 </dd></dl>
<p> <i>Advanced options</i> </p>
<p> Among other things, the advanced options allow complex processing to be performed from a single command without the need for additional scripting. This may be particularly useful for implementations such as Windows drag-and-drop applications. These options may also be used to improve performance in multi-pass processing by reducing the overhead required to load exiftool for each invocation. </p>
<dl>
<dt><code>-api</code><i>OPT[=VAL]</i></dt>
<dd> <p> Set ExifTool <font SIZE="-1">API</font> option. <i></i><font SIZE="-1"><i>OPT</i></font><i></i> is an <font SIZE="-1">API</font> option name. The option value is set to 1 if <i>=VAL</i> is omitted, or undef if just <i></i><font SIZE="-1"><i>VAL</i></font><i></i> is omitted. An option may not be set to an empty string (&quot;&quot;) via the command line, but the config file may be used to accomplish this if necessary. See Image::ExifTool Options for a list of available <font SIZE="-1">API</font> options. This overrides <font SIZE="-1">API</font> options set via the config file. </p>
 </dd>
<dt><code>-common_args</code></dt>
<dd> <p> Specifies that all arguments following this option are common to all executed commands when <code>-execute</code> is used. This and the <code>-config</code> option are the only options that may not be used inside a <code>-@</code> <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i>. Note that by definition this option and its arguments <font SIZE="-1">MUST</font> come after all other options on the command line. </p>
 </dd>
<dt><code>-config</code><i></i><font SIZE="-1"><i>CFGFILE</i></font><i></i></dt>
<dd> <p> Load specified configuration file instead of the default ``.ExifTool_config&#8217;&#8216;. If used, this option must come before all other arguments on the command line. The <i></i><font SIZE="-1"><i>CFGFILE</i></font><i></i> name may contain a directory specification (otherwise the file must exist in the current directory), or may be set to an empty string (&quot;``) to disable loading of the config file. See the sample configuration file and &#8216;&#8216;config.html&quot; in the full ExifTool distribution for more information about the ExifTool configuration file. </p>
 </dd>
<dt><code>-echo</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>] <i></i><font SIZE="-1"><i>TEXT</i></font><i></i></dt>
<dd> <p> Echo <i></i><font SIZE="-1"><i>TEXT</i></font><i></i> to stdout (<code>-echo</code> or <code>-echo1</code>) or stderr (<code>-echo2</code>). Text is output as the command line is parsed, before the processing of any input files. <i></i><font SIZE="-1"><i>NUM</i></font><i></i> may also be 3 or 4 to output text (to stdout or stderr respectively) after processing is complete. </p>
 </dd>
<dt><code>-execute</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]</dt>
<dd> <p> Execute command for all arguments up to this point on the command line (plus any arguments specified by <code>-common_args</code>). The result is as if the commands were executed as separate command lines (with the exception of the <code>-use</code> option which remains in effect for subsequent commands). Allows multiple commands to be executed from a single command line. <i></i><font SIZE="-1"><i>NUM</i></font><i></i> is an optional number that is echoed in the ``{ready}&#8216;&#8216; message when using the <code>-stay_open</code> feature. </p>
 </dd>
<dt><code>-srcfile</code><i></i><font SIZE="-1"><i>FMT</i></font><i></i></dt>
<dd> <p> Specify a different source file to be processed based on the name of the original <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. This may be useful in some special situations for processing related preview images or sidecar files. See the <code>-w</code> option for a description of the <i></i><font SIZE="-1"><i>FMT</i></font><i></i> syntax. Note that file name <i></i><font SIZE="-1"><i>FMT</i></font><i></i> strings for all options are based on the original <i></i><font SIZE="-1"><i>FILE</i></font><i></i> specified from the command line, not the name of the source file specified by <code>-srcfile</code>. </p>
<p> For example, to copy metadata from <font SIZE="-1">NEF</font> files to the corresponding <font SIZE="-1">JPG</font> previews in a directory where other <font SIZE="-1">JPG</font> images may exist: </p>
<pre><code>    exiftool -ext nef -tagsfromfile @ -srcfile %d%f.jpg dir
</code></pre>
<p> If than one <code>-srcfile</code> option is specified, the files are tested in order and the first existing source file is processed. If none of the source files already exist, then exiftool uses the first <code>-srcfile</code> specified. </p>
<p> A <i></i><font SIZE="-1"><i>FMT</i></font><i></i> of <code>&quot;@&quot;</code> may be used to represent the original <i></i><font SIZE="-1"><i>FILE</i></font><i></i>, which may be useful when specifying multiple <code>-srcfile</code> options (eg. to fall back to processing the original <i></i><font SIZE="-1"><i>FILE</i></font><i></i> if no sidecar exists). </p>
 </dd>
<dt><code>-stay_open</code><i></i><font SIZE="-1"><i>FLAG</i></font><i></i></dt>
<dd> <p> If <i></i><font SIZE="-1"><i>FLAG</i></font><i></i> is <code>1</code> or <code>&quot;True&quot;</code>, causes exiftool keep reading from the <code>-@</code> <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i> even after reaching the end of file. This feature allows calling applications to pre-load exiftool, thus avoiding the overhead of loading exiftool for each command. The procedure is as follows: </p>
<p> 1) Execute <code>&quot;exiftool -stay_open True -@ </code>ARGFILE <code>&quot;</code>, where <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i> is the name of an existing (possibly empty) argument file or <code>&quot;-&quot;</code> to pipe arguments from the standard input. </p>
<p> 2) Write exiftool command-line arguments to <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i>, one argument per line (see the <code>-@</code> option for details). </p>
<p> 3) Write <code>&quot;-execute\n&quot;</code> to <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i>, where <code>&quot;\n&quot;</code> represents a newline sequence. (Note: You may need to flush your write buffers here if using buffered output.) Exiftool will then execute the command with the arguments received up to this point, send a ``{ready}&#8216;&#8216; message to stdout when done (unless the <code>-q</code> or <code>-T</code> option is used), and continue trying to read arguments for the next command from <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i>. To aid in command/response synchronization, any number appended to the <code>&quot;-execute&quot;</code> option is echoed in the ``{ready}&#8216;&#8216; message. For example, <code>&quot;-execute613&quot;</code> results in ``{ready613}&#8216;&#8216;. </p>
<p> 4) Repeat steps 2 and 3 for each command. </p>
<p> 5) Write <code>&quot;-stay_open\nFalse\n&quot;</code> to <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i> when done. This will cause exiftool to process any remaining command-line arguments then exit normally. </p>
<p> The input <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i> may be changed at any time before step 5 above by writing the following lines to the currently open <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i>: </p>
<pre><code>    -stay_open
    True
    -@
    NEWARGFILE
</code></pre>
<p> This causes <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i> to be closed, and <i></i><font SIZE="-1"><i>NEWARGFILE</i></font><i></i> to be kept open. (Without the <code>-stay_open</code> here, exiftool would have returned to reading arguments from <i></i><font SIZE="-1"><i>ARGFILE</i></font><i></i> after reaching the end of <i></i><font SIZE="-1"><i>NEWARGFILE</i></font><i></i>.) </p>
<p> Note: When writing arguments to a disk file there is a delay of up to 0.01 seconds after writing <code>&quot;-execute\n&quot;</code> before exiftool starts processing the command. This delay may be avoided by sending a <font SIZE="-1">CONT</font> signal to the exiftool process immediately after writing <code>&quot;-execute\n&quot;</code>. (There is no associated delay when writing arguments via a pipe with <code>&quot;-@ -&quot;</code>, so the signal is not necessary when using this technique.) </p>
 </dd>
<dt><code>-userParam</code><i>PARAM[=VAL]</i></dt>
<dd> <p> Set user parameter. <i></i><font SIZE="-1"><i>PARAM</i></font><i></i> is an arbitrary user parameter name. This is an interface to the <font SIZE="-1">API</font> UserParam option (see the Image::ExifTool Options documentation), and provides a method to access user-defined parameters from inside tag name expressions (as if it were any other tag, see example below), and from PrintConv/ValueConv logic (via the ExifTool Options function). Similar to the <code>-api</code> option, the parameter value is set to 1 if <i>=VAL</i> is omitted, or undef if just <i></i><font SIZE="-1"><i>VAL</i></font><i></i> is omitted. </p>
<pre><code>    exiftool -p '$test from $filename' -userparam test=Hello FILE
</code></pre>
 </dd></dl>
<h2>WINDOWS UNICODE FILE NAMES</h2>
<p> In Windows, by default, file and directory names are specified on the command line (or in arg files) using the system code page, which varies with the system settings. Unfortunately, these code pages are not complete character sets, so not all file names may be represented. </p>
<p> ExifTool 9.79 and later allow the file name encoding to be specified with <code>&quot;-charset filename=CHARSET&quot;</code>, where <code>&quot;CHARSET&quot;</code> is the name of a valid ExifTool character set, preferably <code>&quot;UTF8&quot;</code> (see the <code>-charset</code> option for a complete list). Setting this triggers the use of Windows wide-character i/o routines, thus providing support for all Unicode file names. But note that it is not trivial to pass properly encoded file names on the Windows command line (see &lt;<a rel="nofollow" href="http://owl.phy.queensu.ca/~phil/exiftool/faq.html#Q18">http://owl.phy.queensu.ca/~phil/exiftool/faq.html#Q18</a>&gt; for details), so placing them in a <font SIZE="-1">UTF-8</font> encoded <code>-@</code> argfile is recommended if possible. </p>
<p> When a directory name is provided, the file name encoding need not be specified (unless the directory name contains special characters), and ExifTool will automatically use wide-character routines to scan the directory. </p>
<p> The filename character set applies to the <i></i><font SIZE="-1"><i>FILE</i></font><i></i> arguments as well as filename arguments of <code>-@</code>, <code>-geotag</code>, <code>-o</code>, <code>-p</code>, <code>-srcfile</code>, <code>-tagsFromFile</code>, <code>-csv</code>=, <code>-j</code>= and <code>-</code><i></i><font SIZE="-1"><i>TAG</i></font><i></i>&lt;=. However, it does not apply to the <code>-config</code> filename, which always uses the system character set. The <code>&quot;-charset filename=&quot;</code> option must come before the <code>-@</code> option to be effective, but the order doesn&#8217;t matter with respect to other options. </p>
<p> Notes: </p>
<p> 1) FileName and Directory tag values still use the same encoding as other tag values, and are converted to/from the filename character set when writing/reading if specified. </p>
<p> 2) Unicode support is not yet implemented for other Windows-based systems like Cygwin. </p>
<p> 3) See ``<font SIZE="-1">WRITING</font> READ-ONLY <font SIZE="-1">FILES&#8217;&#8216;</font> below for a note about editing read-only files with Unicode names.  </p>
<h2>WRITING READ-ONLY FILES</h2>
<p> In general, ExifTool may be used to write metadata to read-only files provided that the user has write permission in the directory. However, there are three cases where file write permission is also required: </p>
<p> 1) When using the <code>-overwrite_original_in_place</code> option. </p>
<p> 2) When writing only pseudo System tags (eg. FileModifyDate). </p>
<p> 3) On Windows if the file has Unicode characters in its name, and a) the <code>-overwrite_original</code> option is used, or b) the <code>&quot;_original&quot;</code> backup already exists.  </p>
<h2>READING EXAMPLES</h2>
<p> <code>Note</code>: Beware when cutting and pasting these examples into your terminal! Some characters such as single and double quotes and hyphens may have been changed into similar-looking yet functionally-different characters by the text formatter used to display this documentation. Also note that Windows users must use double quotes instead of single quotes as below around arguments containing special characters. </p>
<dl>
<dt>exiftool -a -u -g1 a.jpg</dt>
<dd> <p> Print all meta information in an image, including duplicate and unknown tags, sorted by group (for family 1). </p>
 </dd>
<dt>exiftool -common dir</dt>
<dd> <p> Print common meta information for all images in <code>&quot;dir&quot;</code>. <code>&quot;-common&quot;</code> is a shortcut tag representing common <font SIZE="-1">EXIF</font> meta information. </p>
 </dd>
<dt>exiftool -T -createdate -aperture -shutterspeed -iso dir &gt; out.txt</dt>
<dd> <p> List specified meta information in tab-delimited column form for all images in <code>&quot;dir&quot;</code> to an output text file named ``out.txt&#8217;&#8216;. </p>
 </dd>
<dt>exiftool -s -ImageSize -ExposureTime b.jpg</dt>
<dd> <p> Print ImageSize and ExposureTime tag names and values. </p>
 </dd>
<dt>exiftool -l -canon c.jpg d.jpg</dt>
<dd> <p> Print standard Canon information from two image files. </p>
 </dd>
<dt>exiftool -r -w .txt -common pictures</dt>
<dd> <p> Recursively extract common meta information from files in <code>&quot;pictures&quot;</code> directory, writing text output to <code>&quot;.txt&quot;</code> files with the same names. </p>
 </dd>
<dt>exiftool -b -ThumbnailImage image.jpg &gt; thumbnail.jpg</dt>
<dd> <p> Save thumbnail image from <code>&quot;image.jpg&quot;</code> to a file called <code>&quot;thumbnail.jpg&quot;</code>. </p>
 </dd>
<dt>exiftool -b -JpgFromRaw -w _JFR.JPG -ext <font SIZE="-1">NEF</font> -r .</dt>
<dd> <p> Recursively extract <font SIZE="-1">JPG</font> image from all Nikon <font SIZE="-1">NEF</font> files in the current directory, adding <code>&quot;_JFR.JPG&quot;</code> for the name of the output <font SIZE="-1">JPG</font> files. </p>
 </dd>
<dt>exiftool -a -b -W %d%f_%t%-c.%s -preview:all dir</dt>
<dd> <p> Extract all types of preview images (ThumbnailImage, PreviewImage, JpgFromRaw, etc.) from files in directory ``dir&#8217;&#8216;, adding the tag name to the output preview image file names. </p>
 </dd>
<dt>exiftool -d &#8216;%r %a, %B %e, %Y&#8217; -DateTimeOriginal -S -s -ext jpg .</dt>
<dd> <p> Print formatted date/time for all <font SIZE="-1">JPG</font> files in the current directory. </p>
 </dd>
<dt>exiftool -IFD1:XResolution -IFD1:YResolution image.jpg</dt>
<dd> <p> Extract image resolution from <font SIZE="-1">EXIF IFD1</font> information (thumbnail image <font SIZE="-1">IFD</font>). </p>
 </dd>
<dt>exiftool &#8216;-*resolution*&#8216; image.jpg</dt>
<dd> <p> Extract all tags with names containing the word ``Resolution&#8217;&#8216; from an image. </p>
 </dd>
<dt>exiftool -xmp:author:all -a image.jpg</dt>
<dd> <p> Extract all author-related <font SIZE="-1">XMP</font> information from an image. </p>
 </dd>
<dt>exiftool -xmp -b a.jpg &gt; out.xmp</dt>
<dd> <p> Extract complete <font SIZE="-1">XMP</font> data record intact from <code>&quot;a.jpg&quot;</code> and write it to <code>&quot;out.xmp&quot;</code> using the special <code>&quot;XMP&quot;</code> tag (see the Extra tags in Image::ExifTool::TagNames). </p>
 </dd>
<dt>exiftool -p &#8216;$filename has date $dateTimeOriginal&#8217; -q -f dir</dt>
<dd> <p> Print one line of output containing the file name and DateTimeOriginal for each image in directory <code>&quot;dir&quot;</code>. </p>
 </dd>
<dt>exiftool -ee -p &#8216;$gpslatitude, $gpslongitude, $gpstimestamp&#8217; a.m2ts</dt>
<dd> <p> Extract all <font SIZE="-1">GPS</font> positions from an <font SIZE="-1">AVCHD</font> video. </p>
 </dd>
<dt>exiftool -icc_profile -b -w icc image.jpg</dt>
<dd> <p> Save complete ICC_Profile from an image to an output file with the same name and an extension of <code>&quot;.icc&quot;</code>. </p>
 </dd>
<dt>exiftool -htmldump -w tmp/%f_%e.html t/images</dt>
<dd> <p> Generate <font SIZE="-1">HTML</font> pages from a hex dump of <font SIZE="-1">EXIF</font> information in all images from the <code>&quot;t/images&quot;</code> directory. The output <font SIZE="-1">HTML</font> files are written to the <code>&quot;tmp&quot;</code> directory (which is created if it didn&#8217;t exist), with names of the form &#8216;<font SIZE="-1">FILENAME_EXT</font>.html&#8217;. </p>
 </dd>
<dt>exiftool -a -b -ee -embeddedimage -W Image_%.3g3.%s file.pdf</dt>
<dd> <p> Extract embedded <font SIZE="-1">JPG</font> and <font SIZE="-1">JP2</font> images from a <font SIZE="-1">PDF</font> file. The output images will have file names like ``Image_#.jpg&#8217;&#8216; or ``Image_#.jp2&#8217;&#8216;, where ``#&#8216;&#8216; is the ExifTool family 3 embedded document number for the image. </p>
 </dd></dl>
<h2>WRITING EXAMPLES</h2>
<p> Note that quotes are necessary around arguments which contain certain special characters such as <code>&quot;&gt;&quot;</code>, <code>&quot;&lt;&quot;</code> or any white space. These quoting techniques are shell dependent, but the examples below will work for most Unix shells. With the Windows cmd shell however, double quotes should be used (eg. -Comment=``This is a new comment&#8217;&#8216;). </p>
<dl>
<dt>exiftool -Comment=&#8216;This is a new comment&#8217; dst.jpg</dt>
<dd> <p> Write new comment to a <font SIZE="-1">JPG</font> image (replaces any existing comment). </p>
 </dd>
<dt>exiftool -comment= -o newdir -ext jpg .</dt>
<dd> <p> Remove comment from all <font SIZE="-1">JPG</font> images in the current directory, writing the modified images to a new directory. </p>
 </dd>
<dt>exiftool -keywords=EXIF -keywords=editor dst.jpg</dt>
<dd> <p> Replace existing keyword list with two new keywords (<code>&quot;EXIF&quot;</code> and <code>&quot;editor&quot;</code>). </p>
 </dd>
<dt>exiftool -Keywords+=word -o newfile.jpg src.jpg</dt>
<dd> <p> Copy a source image to a new file, and add a keyword (<code>&quot;word&quot;</code>) to the current list of keywords. </p>
 </dd>
<dt>exiftool -exposurecompensation+=-0.5 a.jpg</dt>
<dd> <p> Decrement the value of ExposureCompensation by 0.5 <font SIZE="-1">EV. </font> Note that += with a negative value is used for decrementing because the -= operator is used for conditional deletion (see next example). </p>
 </dd>
<dt>exiftool -credit-=xxx dir</dt>
<dd> <p> Delete Credit information from all files in a directory where the Credit value was <code>&quot;xxx&quot;</code>. </p>
 </dd>
<dt>exiftool -xmp:description-de=&#8216;k&amp;uuml;hl&#8217; -E dst.jpg</dt>
<dd> <p> Write alternate language for XMP:Description, using <font SIZE="-1">HTML</font> character escaping to input special characters. </p>
 </dd>
<dt>exiftool -all= dst.jpg</dt>
<dd> <p> Delete all meta information from an image. Note: You should <font SIZE="-1">NOT</font> do this to <font SIZE="-1">RAW</font> images (except <font SIZE="-1">DNG</font>) since proprietary <font SIZE="-1">RAW</font> image formats often contain information in the makernotes that is necessary for converting the image. </p>
 </dd>
<dt>exiftool -all= -comment=&#8216;lonely&#8217; dst.jpg</dt>
<dd> <p> Delete all meta information from an image and add a comment back in. (Note that the order is important: <code>&quot;-comment=&#8216;lonely&#8217; -all=&quot;</code> would also delete the new comment.) </p>
 </dd>
<dt>exiftool -all= --jfif:all dst.jpg</dt>
<dd> <p> Delete all meta information except <font SIZE="-1">JFIF</font> group from an image. </p>
 </dd>
<dt>exiftool -Photoshop:All= dst.jpg</dt>
<dd> <p> Delete Photoshop meta information from an image (note that the Photoshop information also includes <font SIZE="-1">IPTC</font>). </p>
 </dd>
<dt>exiftool -r -XMP-crss:all= <font SIZE="-1">DIR</font></dt>
<dd> <p> Recursively delete all XMP-crss information from images in a directory. </p>
 </dd>
<dt>exiftool &#8216;-ThumbnailImage&lt;=thumb.jpg&#8217; dst.jpg</dt>
<dd> <p> Set the thumbnail image from specified file (Note: The quotes are necessary to prevent shell redirection). </p>
 </dd>
<dt>exiftool &#8216;-JpgFromRaw&lt;=%d%f_JFR.JPG&#8217; -ext <font SIZE="-1">NEF</font> -r .</dt>
<dd> <p> Recursively write <font SIZE="-1">JPEG</font> images with filenames ending in <code>&quot;_JFR.JPG&quot;</code> to the JpgFromRaw tag of like-named files with extension <code>&quot;.NEF&quot;</code> in the current directory. (This is the inverse of the <code>&quot;-JpgFromRaw&quot;</code> command of the ``<font SIZE="-1">READING EXAMPLES&#8217;&#8216;</font> section above.) </p>
 </dd>
<dt>exiftool -DateTimeOriginal-=&#8216;0:0:0 1:30:0&#8217; dir</dt>
<dd> <p> Adjust original date/time of all images in directory <code>&quot;dir&quot;</code> by subtracting one hour and 30 minutes. (This is equivalent to <code>&quot;-DateTimeOriginal-=1.5&quot;</code>. See Image::ExifTool::Shift.pl for details.) </p>
 </dd>
<dt>exiftool -createdate+=3 -modifydate+=3 a.jpg b.jpg</dt>
<dd> <p> Add 3 hours to the CreateDate and ModifyDate timestamps of two images. </p>
 </dd>
<dt>exiftool -AllDates+=1:30 -if &#8216;$make eq &quot;Canon&quot;&#8216; dir</dt>
<dd> <p> Shift the values of DateTimeOriginal, CreateDate and ModifyDate forward by 1 hour and 30 minutes for all Canon images in a directory. (The AllDates tag is provided as a shortcut for these three tags, allowing them to be accessed via a single tag.) </p>
 </dd>
<dt>exiftool -xmp:city=Kingston image1.jpg image2.nef</dt>
<dd> <p> Write a tag to the <font SIZE="-1">XMP</font> group of two images. (Without the <code>&quot;xmp:&quot;</code> this tag would get written to the <font SIZE="-1">IPTC</font> group since <code>&quot;City&quot;</code> exists in both, and <font SIZE="-1">IPTC</font> is preferred by default.) </p>
 </dd>
<dt>exiftool -LightSource-=&#8216;Unknown (0)&#8216; dst.tiff</dt>
<dd> <p> Delete <code>&quot;LightSource&quot;</code> tag only if it is unknown with a value of 0. </p>
 </dd>
<dt>exiftool -whitebalance-=auto -WhiteBalance=tung dst.jpg</dt>
<dd> <p> Set <code>&quot;WhiteBalance&quot;</code> to <code>&quot;Tungsten&quot;</code> only if it was previously <code>&quot;Auto&quot;</code>. </p>
 </dd>
<dt>exiftool -comment-= -comment=&#8216;new comment&#8217; a.jpg</dt>
<dd> <p> Write a new comment only if the image doesn&#8217;t have one already. </p>
 </dd>
<dt>exiftool -o %d%f.xmp dir</dt>
<dd> <p> Create <font SIZE="-1">XMP</font> meta information data files for all images in <code>&quot;dir&quot;</code>. </p>
 </dd>
<dt>exiftool -o test.xmp -owner=Phil -title=&#8216;<font SIZE="-1">XMP</font> File&#8217;</dt>
<dd> <p> Create an <font SIZE="-1">XMP</font> data file only from tags defined on the command line. </p>
 </dd>
<dt>exiftool &#8216;-ICC_Profile&lt;=%d%f.icc&#8217; image.jpg</dt>
<dd> <p> Write ICC_Profile to an image from a <code>&quot;.icc&quot;</code> file of the same name. </p>
 </dd>
<dt>exiftool -hierarchicalkeywords=&#8216;{keyword=one,children={keyword=B}}&#8216;</dt>
<dd> <p> Write structured <font SIZE="-1">XMP</font> information. See &lt;<a rel="nofollow" href="http://owl.phy.queensu.ca/~phil/exiftool/struct.html">http://owl.phy.queensu.ca/~phil/exiftool/struct.html</a>&gt; for more details. </p>
 </dd>
<dt>exiftool -trailer:all= image.jpg</dt>
<dd> <p> Delete any trailer found after the end of image (<font SIZE="-1">EOI</font>) in a <font SIZE="-1">JPEG</font> file. A number of digital cameras store a large PreviewImage after the <font SIZE="-1">JPEG EOI,</font> and the file size may be reduced significantly by deleting this trailer. See the <font SIZE="-1">JPEG</font> Tags documentation for a list of recognized <font SIZE="-1">JPEG</font> trailers. </p>
 </dd></dl>
<h2>COPYING EXAMPLES</h2>
<p> These examples demonstrate the ability to copy tag values between files. </p>
<dl>
<dt>exiftool -tagsFromFile src.cr2 dst.jpg</dt>
<dd> <p> Copy the values of all writable tags from <code>&quot;src.cr2&quot;</code> to <code>&quot;dst.jpg&quot;</code>, writing the information to same-named tags in the preferred groups. </p>
 </dd>
<dt>exiftool -TagsFromFile src.jpg -all:all dst.jpg</dt>
<dd> <p> Copy the values of all writable tags from <code>&quot;src.jpg&quot;</code> to <code>&quot;dst.jpg&quot;</code>, preserving the original tag groups. </p>
 </dd>
<dt>exiftool -all= -tagsfromfile src.jpg -exif:all dst.jpg</dt>
<dd> <p> Erase all meta information from <code>&quot;dst.jpg&quot;</code> image, then copy <font SIZE="-1">EXIF</font> tags from <code>&quot;src.jpg&quot;</code>. </p>
 </dd>
<dt>exiftool -exif:all= -tagsfromfile @ -all:all -unsafe bad.jpg</dt>
<dd> <p> Rebuild all <font SIZE="-1">EXIF</font> meta information from scratch in an image. This technique can be used in <font SIZE="-1">JPEG</font> images to repair corrupted <font SIZE="-1">EXIF</font> information which otherwise could not be written due to errors. The <code>&quot;Unsafe&quot;</code> tag is a shortcut for unsafe <font SIZE="-1">EXIF</font> tags in <font SIZE="-1">JPEG</font> images which are not normally copied. See the tag name documentation for more details about unsafe tags. </p>
 </dd>
<dt>exiftool -Tagsfromfile a.jpg out.xmp</dt>
<dd> <p> Copy meta information from <code>&quot;a.jpg&quot;</code> to an <font SIZE="-1">XMP</font> data file. If the <font SIZE="-1">XMP</font> data file <code>&quot;out.xmp&quot;</code> already exists, it will be updated with the new information. Otherwise the <font SIZE="-1">XMP</font> data file will be created. Only <font SIZE="-1">XMP, ICC</font> and <font SIZE="-1">MIE</font> files may be created like this (other file types may be edited but not created). See ``<font SIZE="-1">WRITING EXAMPLES&#8217;&#8216;</font> above for another technique to generate <font SIZE="-1">XMP</font> files. </p>
 </dd>
<dt>exiftool -tagsFromFile a.jpg -XMP:All= -ThumbnailImage= -m b.jpg</dt>
<dd> <p> Copy all meta information from <code>&quot;a.jpg&quot;</code> to <code>&quot;b.jpg&quot;</code>, deleting all <font SIZE="-1">XMP</font> information and the thumbnail image from the destination. </p>
 </dd>
<dt>exiftool -TagsFromFile src.jpg -title -author=Phil dst.jpg</dt>
<dd> <p> Copy title from one image to another and set a new author name. </p>
 </dd>
<dt>exiftool -TagsFromFile a.jpg -ISO -TagsFromFile b.jpg -comment dst.jpg</dt>
<dd> <p> Copy <font SIZE="-1">ISO</font> from one image and Comment from another image to a destination image. </p>
 </dd>
<dt>exiftool -tagsfromfile src.jpg -exif:all --subifd:all dst.jpg</dt>
<dd> <p> Copy only the <font SIZE="-1">EXIF</font> information from one image to another, excluding SubIFD tags. </p>
 </dd>
<dt>exiftool &#8216;-FileModifyDate&lt;DateTimeOriginal&#8217; dir</dt>
<dd> <p> Use the original date from the meta information to set the same file&#8217;s filesystem modification date for all images in a directory. (Note that <code>&quot;-TagsFromFile @&quot;</code> is assumed if no other <code>-TagsFromFile</code> is specified when redirecting information as in this example.) </p>
 </dd>
<dt>exiftool -TagsFromFile src.jpg &#8216;-xmp:all&lt;all&#8217; dst.jpg</dt>
<dd> <p> Copy all possible information from <code>&quot;src.jpg&quot;</code> and write in <font SIZE="-1">XMP</font> format to <code>&quot;dst.jpg&quot;</code>. </p>
 </dd>
<dt>exiftool -@ iptc2xmp.args -iptc:all= a.jpg</dt>
<dd> <p> Translate <font SIZE="-1">IPTC</font> information to <font SIZE="-1">XMP</font> with appropriate tag name conversions, and delete the original <font SIZE="-1">IPTC</font> information from an image. This example uses iptc2xmp.args, which is a file included with the ExifTool distribution that contains the required arguments to convert <font SIZE="-1">IPTC</font> information to <font SIZE="-1">XMP</font> format. Also included with the distribution are xmp2iptc.args (which performs the inverse conversion) and a few more .args files for other conversions between <font SIZE="-1">EXIF, IPTC</font> and <font SIZE="-1">XMP.</font> </p>
 </dd>
<dt>exiftool -tagsfromfile %d%f.CR2 -r -ext <font SIZE="-1">JPG</font> dir</dt>
<dd> <p> Recursively rewrite all <code>&quot;JPG&quot;</code> images in <code>&quot;dir&quot;</code> with information copied from the corresponding <code>&quot;CR2&quot;</code> images in the same directories. </p>
 </dd>
<dt>exiftool &#8216;-keywords+&lt;make&#8217; image.jpg</dt>
<dd> <p> Add camera make to list of keywords. </p>
 </dd>
<dt>exiftool &#8216;-comment&lt;ISO=$exif:iso Exposure=${shutterspeed}&#8216; dir</dt>
<dd> <p> Set the Comment tag of all images in <code>&quot;dir&quot;</code> from the values of the <font SIZE="-1">EXIF:ISO</font> and ShutterSpeed tags. The resulting comment will be in the form ``ISO=100 Exposure=1/60&#8217;&#8216;. </p>
 </dd>
<dt>exiftool -TagsFromFile src.jpg -icc_profile dst.jpg</dt>
<dd> <p> Copy ICC_Profile from one image to another. </p>
 </dd>
<dt>exiftool -TagsFromFile src.jpg -all:all dst.mie</dt>
<dd> <p> Copy all meta information in its original form from a <font SIZE="-1">JPEG</font> image to a <font SIZE="-1">MIE</font> file. The <font SIZE="-1">MIE</font> file will be created if it doesn&#8217;t exist. This technique can be used to store the metadata of an image so it can be inserted back into the image (with the inverse command) later in a workflow. </p>
 </dd>
<dt>exiftool -o dst.mie -all:all src.jpg</dt>
<dd> <p> This command performs exactly the same task as the command above, except that the <code>-o</code> option will not write to an output file that already exists. </p>
 </dd>
<dt>exiftool -if &#8216;$jpgfromraw&#8217; -b -jpgfromraw -w %d%f_%ue.jpg -execute -if &#8216;$previewimage&#8217; -b -previewimage -w %d%f_%ue.jpg -execute -tagsfromfile @ -srcfile %d%f_%ue.jpg -overwrite_original -common_args --ext jpg <font SIZE="-1">DIR</font></dt>
<dd> <p> [Advanced] Extract JpgFromRaw or PreviewImage from all but <font SIZE="-1">JPG</font> files in <font SIZE="-1">DIR,</font> saving them with file names like <code>&quot;image_EXT.jpg&quot;</code>, then add all meta information from the original files to the extracted images. Here, the command line is broken into three sections (separated by <code>-execute</code> options), and each is executed as if it were a separate command. The <code>-common_args</code> option causes the <code>&quot;--ext jpg DIR&quot;</code> arguments to be applied to all three commands, and the <code>-srcfile</code> option allows the extracted <font SIZE="-1">JPG</font> image to be the source file for the third command (whereas the <font SIZE="-1">RAW</font> files are the source files for the other two commands). </p>
 </dd></dl>
<h2>RENAMING EXAMPLES</h2>
<p> By writing the <code>&quot;FileName&quot;</code> and <code>&quot;Directory&quot;</code> tags, files are renamed and/or moved to new directories. This can be particularly useful and powerful for organizing files by date when combined with the <code>-d</code> option. New directories are created as necessary, but existing files will not be overwritten. The format codes <code>%d</code>, <code>%f</code> and <code>%e</code> may be used in the new file name to represent the directory, name and extension of the original file, and <code>%c</code> may be used to add a copy number if the file already exists (see the <code>-w</code> option for details). Note that if used within a date format string, an extra &#8216;%&#8216; must be added to pass these codes through the date/time parser. (And further note that in a Windows batch file, all &#8216;%&#8216; characters must also be escaped, so in this extreme case &#8216;%%%%f&#8217; is necessary to pass a simple &#8216;%f&#8217; through the two levels of parsing.) See &lt;<a rel="nofollow" href="http://owl.phy.queensu.ca/~phil/exiftool/filename.html">http://owl.phy.queensu.ca/~phil/exiftool/filename.html</a>&gt; for additional documentation and examples. </p>
<dl>
<dt>exiftool -filename=new.jpg dir/old.jpg</dt>
<dd> <p> Rename <code>&quot;old.jpg&quot;</code> to <code>&quot;new.jpg&quot;</code> in directory <code>&quot;dir&quot;</code>. </p>
 </dd>
<dt>exiftool -directory=%e dir</dt>
<dd> <p> Move all files from directory <code>&quot;dir&quot;</code> into directories named by the original file extensions. </p>
 </dd>
<dt>exiftool &#8216;-Directory&lt;DateTimeOriginal&#8217; -d %Y/%m/%d dir</dt>
<dd> <p> Move all files in <code>&quot;dir&quot;</code> into a directory hierarchy based on year, month and day of <code>&quot;DateTimeOriginal&quot;</code>. eg) This command would move the file <code>&quot;dir/image.jpg&quot;</code> with a <code>&quot;DateTimeOriginal&quot;</code> of <code>&quot;2005:10:12 16:05:56&quot;</code> to <code>&quot;2005/10/12/image.jpg&quot;</code>. </p>
 </dd>
<dt>exiftool -o . &#8216;-Directory&lt;DateTimeOriginal&#8217; -d %Y/%m/%d dir</dt>
<dd> <p> Same effect as above except files are copied instead of moved. </p>
 </dd>
<dt>exiftool &#8216;-filename&lt;%f_${model;}.%e&#8217; dir</dt>
<dd> <p> Rename all files in <code>&quot;dir&quot;</code> by adding the camera model name to the file name. The semicolon after the tag name inside the braces causes characters which are invalid in Windows file names to be deleted from the tag value (see the <code>-p</code> option documentation for an explanation). </p>
 </dd>
<dt>exiftool &#8216;-FileName&lt;CreateDate&#8217; -d %Y%m%d_%H%M%S%%-c.%%e dir</dt>
<dd> <p> Rename all images in <code>&quot;dir&quot;</code> according to the <code>&quot;CreateDate&quot;</code> date and time, adding a copy number with leading &#8216;-&#8216; if the file already exists (<code>&quot;%-c&quot;</code>), and preserving the original file extension (<code>%e</code>). Note the extra &#8216;%&#8216; necessary to escape the filename codes (<code>%c</code> and <code>%e</code>) in the date format string. </p>
 </dd>
<dt>exiftool -r &#8216;-FileName&lt;CreateDate&#8217; -d %Y-%m-%d/%H%M_%%f.%%e dir</dt>
<dd> <p> Both the directory and the filename may be changed together via the <code>&quot;FileName&quot;</code> tag if the new <code>&quot;FileName&quot;</code> contains a &#8216;/&#8216;. The example above recursively renames all images in a directory by adding a <code>&quot;CreateDate&quot;</code> timestamp to the start of the filename, then moves them into new directories named by date. </p>
 </dd>
<dt>exiftool &#8216;-FileName&lt;${CreateDate}_$filenumber.jpg&#8217; -d %Y%m%d -ext jpg .</dt>
<dd> <p> Set the filename of all <font SIZE="-1">JPG</font> images in the current directory from the CreateDate and FileNumber tags, in the form ``20060507_118-1861.jpg&#8217;&#8216;. </p>
 </dd></dl>
<h2>GEOTAGGING EXAMPLES</h2>
<p> ExifTool implements geotagging via 3 special tags: Geotag (which for convenience is also implemented as an exiftool option), Geosync and Geotime. The examples below highlight some geotagging features. See &lt;<a rel="nofollow" href="http://owl.phy.queensu.ca/~phil/exiftool/geotag.html">http://owl.phy.queensu.ca/~phil/exiftool/geotag.html</a>&gt; for additional documentation. </p>
<dl>
<dt>exiftool -geotag track.log a.jpg</dt>
<dd> <p> Geotag an image (<code>&quot;a.jpg&quot;</code>) from position information in a <font SIZE="-1">GPS</font> track log (<code>&quot;track.log&quot;</code>). Since the <code>&quot;Geotime&quot;</code> tag is not specified, the value of DateTimeOriginal is used for geotagging. Local system time is assumed unless DateTimeOriginal contains a timezone. </p>
 </dd>
<dt>exiftool -geotag t.log -geotime=&#8216;2009:04:02 13:41:12-05:00&#8217; a.jpg</dt>
<dd> <p> Geotag an image with the <font SIZE="-1">GPS</font> position for a specific time. (Note that the <code>&quot;Geotag&quot;</code> tag must be assigned before <code>&quot;Geotime&quot;</code> for the <font SIZE="-1">GPS</font> data to be available when <code>&quot;Geotime&quot;</code> is set.) </p>
 </dd>
<dt>exiftool -geotag log.gpx &#8216;-xmp:geotime&lt;createdate&#8217; dir</dt>
<dd> <p> Geotag all images in directory <code>&quot;dir&quot;</code> with <font SIZE="-1">XMP</font> tags instead of <font SIZE="-1">EXIF</font> tags, based on the image CreateDate. (In this case, the order of the arguments doesn&#8217;t matter because tags with values copied from other tags are always set after constant values.) </p>
 </dd>
<dt>exiftool -geotag a.log -geosync=-20 dir</dt>
<dd> <p> Geotag images in directory <code>&quot;dir&quot;</code>, accounting for image timestamps which were 20 seconds ahead of <font SIZE="-1">GPS.</font> </p>
 </dd>
<dt>exiftool -geotag a.log -geosync=1.jpg -geosync=2.jpg dir</dt>
<dd> <p> Geotag images using time synchronization from two previously geotagged images (1.jpg and 2.jpg), synchronizing the image and <font SIZE="-1">GPS</font> times using a linear time drift correction. </p>
 </dd>
<dt>exiftool -geotag a.log &#8216;-geotime&lt;${createdate}+01:00&#8217; dir</dt>
<dd> <p> Geotag images in <code>&quot;dir&quot;</code> using CreateDate with the specified timezone. If CreateDate already contained a timezone, then the timezone specified on the command line is ignored. </p>
 </dd>
<dt>exiftool -geotag= a.jpg</dt>
<dd> <p> Delete <font SIZE="-1">GPS</font> tags which may have been added by the geotag feature. Note that this does not remove all <font SIZE="-1">GPS</font> tags --- to do this instead use <code>&quot;-gps:all=&quot;</code>. </p>
 </dd>
<dt>exiftool -xmp:geotag= a.jpg</dt>
<dd> <p> Delete <font SIZE="-1">XMP GPS</font> tags which were added by the geotag feature. </p>
 </dd>
<dt>exiftool -xmp:geotag=track.log a.jpg</dt>
<dd> <p> Geotag an image with <font SIZE="-1">XMP</font> tags, using the time from DateTimeOriginal. </p>
 </dd>
<dt>exiftool -geotag a.log -geotag b.log -r dir</dt>
<dd> <p> Combine multiple track logs and geotag an entire directory tree of images. </p>
 </dd>
<dt>exiftool -geotag &#8216;tracks/*.log&#8217; -r dir</dt>
<dd> <p> Read all track logs from the <code>&quot;tracks&quot;</code> directory. </p>
 </dd>
<dt>exiftool -p gpx.fmt -d %Y-%m-%dT%H:%M:%SZ dir &gt; out.gpx</dt>
<dd> <p> Generate a <font SIZE="-1">GPX</font> track log from all images in directory <code>&quot;dir&quot;</code>. This example uses the <code>&quot;gpx.fmt&quot;</code> file included in the full ExifTool distribution package and assumes that the images in <code>&quot;dir&quot;</code> have all been previously geotagged. </p>
 </dd></dl>
<h2>PIPING EXAMPLES</h2>
<dl>
<dt>cat a.jpg | exiftool -</dt>
<dd> <p> Extract information from stdin. </p>
 </dd>
<dt>exiftool image.jpg -thumbnailimage -b | exiftool -</dt>
<dd> <p> Extract information from an embedded thumbnail image. </p>
 </dd>
<dt>cat a.jpg | exiftool -iptc:keywords+=fantastic - &gt; b.jpg</dt>
<dd> <p> Add an <font SIZE="-1">IPTC</font> keyword in a pipeline, saving output to a new file. </p>
 </dd>
<dt>curl -s <a rel="nofollow" href="http://a.domain.com/bigfile.jpg">http://a.domain.com/bigfile.jpg</a> | exiftool -fast -</dt>
<dd> <p> Extract information from an image over the internet using the cURL utility. The <code>-fast</code> option prevents exiftool from scanning for trailer information, so only the meta information header is transferred. </p>
 </dd>
<dt>exiftool a.jpg -thumbnailimage -b | exiftool -comment=wow - | exiftool a.jpg -thumbnailimage&#8217;&lt;=-&#8216;</dt>
<dd> <p> Add a comment to an embedded thumbnail image. (Why anyone would want to do this I don&#8217;t know, but I&#8217;ve included this as an example to illustrate the flexibility of ExifTool.) </p>
 </dd></dl>
<h2>DIAGNOSTICS</h2>
<p> The exiftool application exits with a status of 0 on success, or 1 if an error occurred or if all files failed the <code>-if</code> condition (for any of the commands if <code>-execute</code> was used).  </p>
<h2>AUTHOR</h2>
<p> Copyright 2003-2017, Phil Harvey </p>
<p> This is free software; you can redistribute it and/or modify it under the same terms as Perl itself.  </p>
<h2>SEE ALSO</h2>
<p> <i>Image::ExifTool</i>(3pm), <i>Image::ExifTool::TagNames</i>(3pm), <i>Image::ExifTool::Shortcuts</i>(3pm), Image::ExifTool::Shift.pl </p>
