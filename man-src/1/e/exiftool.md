---
title: "exiftool(1)"
name: "exiftool"
section: "1"
letter: "e"
url: "/docs/linux/man/1-exiftool/"
description: "exiftool – Read and write meta information in files"
---

<h2 class="name">NAME</h2>
<p> exiftool &#8211; Read and write meta information in files </p>
<h2>SYNOPSIS</h2>
<h3>Reading</h3>
<p> <code>exiftool</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] [-<i></i><font SIZE="-1"><i>TAG</i></font><i></i>&#8230;] [&#8211;<i></i><font SIZE="-1"><i>TAG</i></font><i></i>&#8230;] <i></i><font SIZE="-1"><i>FILE</i></font><i></i>&#8230;</p>
<h3>Writing</h3>
<p> <code>exiftool</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] &#8211;<i></i><font SIZE="-1"><i>TAG</i></font><i></i>[+-&lt;]=[<i></i><font SIZE="-1"><i>VALUE</i></font><i></i>]&#8230; <i></i><font SIZE="-1"><i>FILE</i></font><i></i>&#8230;</p>
<h3>Copying</h3>
<p> <code>exiftool</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <code>-tagsFromFile</code> <i></i><font SIZE="-1"><i>SRCFILE</i></font><i></i> [-<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>[&gt;<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>]&#8230;] <i></i><font SIZE="-1"><i>FILE</i></font><i></i>&#8230;</p>
<h3>Other</h3>
<p> <code>exiftool</code> [ <code>-ver</code> | <code>-list</code>[<code>w</code>|<code>f</code>|<code>r</code>|<code>wf</code>|<code>g</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>]|<code>d</code>|<code>x</code>] ] </p>
<p> For specific examples, see the <font SIZE="-1">EXAMPLES</font> sections below. </p>
<p> This documentation is displayed if exiftool is run without an input <i></i><font SIZE="-1"><i>FILE</i></font><i></i> when one is expected.</p>
<h2>DESCRIPTION</h2>
<p> A command-line interface to Image::ExifTool, used for reading and writing meta information in a variety of file types. <i></i><font SIZE="-1"><i>FILE</i></font><i></i> is one or more source file names, directory names, or <tt>&quot;-&quot;</tt> for the standard input. Metadata is read from source files and printed in readable form to the console (or written to output text files with <code>-w</code>). </p>
<p> To write or delete metadata, tag values are assigned using the &#8211;<i></i><font SIZE="-1"><i>TAG</i></font><i></i>=[<i></i><font SIZE="-1"><i>VALUE</i></font><i></i>] syntax, or the <code>-geotag</code> option. To copy or move metadata, the <code>-tagsFromFile</code> feature is used. By default the original files are preserved with <tt>&quot;_original&quot;</tt> appended to their names &#8212; be sure to verify that the new files are <font SIZE="-1">OK</font> before erasing the originals. Once in write mode, exiftool will ignore any read-specific options. </p>
<p> Note: If <i></i><font SIZE="-1"><i>FILE</i></font><i></i> is a directory name then only supported file types in the directory are processed (in write mode only writable types are processed). However, files may be specified by name, or the <code>-ext</code> option may be used to force processing of files with any extension. Hidden files in the directory are also processed. Adding the <code>-r</code> option causes subdirectories to be processed recursively, but those with names beginning with &#8220;.&#8221; are skipped unless <code>-r.</code> is used. </p>
<p> Below is a list of file types and meta information formats currently supported by ExifTool (r = read, w = write, c = create): </p>
<pre><code>
File Types-- -- -- -- -- --+-- -- -- -- -- -- -+-- -- -- -- -- -- -+-- -- -- -- -- -- -+-- -- -- -- -- --3FR r | DV r | K25 r | OFR r | RSRC r 3G2 r / w | DVB r / w | KDC r | OGG r | RTF r 3GP r / w | DYLIB r | KEY r | OGV r | RW2 r / w A r | EIP r | LA r | OPUS r | RWL r / w AA r | EPS r / w | LFP r | ORF r / w | RWZ r AAX r / w | EPUB r | LNK r | OTF r | RM r ACR r | ERF r / w | M2TS r | PAC r | SEQ r AFM r | EXE r | M4A / V r / w | PAGES r | SO r AI r / w | EXIF r / w / c | MAX r | PBM r / w | SR2 r / w AIFF r | EXR r | MEF r / w | PCD r | SRF r APE r | EXV r / w / c | MIE r / w / c | PDB r | SRW r / w ARW r / w | F4A / V r / w | MIFF r | PDF r / w | SVG r ASF r | FFF r / w | MKA r | PEF r / w | SWF r AVI r | FLA r | MKS r | PFA r | THM r / w AZW r | FLAC r | MKV r | PFB r | TIFF r / w BMP r | FLIF r / w | MNG r / w | PFM r | TORRENT r BPG r | FLV r | MOBI r | PGF r | TTC r BTF r | FPF r | MODD r | PGM r / w | TTF r CHM r | FPX r | MOI r | PLIST r | VCF r COS r | GIF r / w | MOS r / w | PICT r | VRD r / w / c CR2 r / w | GZ r | MOV r / w | PMP r | VSD r CRW r / w | HDP r / w | MP3 r | PNG r / w | WAV r CS1 r / w | HDR r | MP4 r / w | PPM r / w | WDP r / w DCM r | HTML r | MPC r | PPT r | WEBP r DCP r / w | ICC r / w / c | MPG r | PPTX r | WEBM r DCR r | ICS r | MPO r / w | PS r / w | WMA r DFONT r | IDML r | MQV r / w | PSB r / w | WMV r DIVX r | IIQ r / w | MRW r / w | PSD r / w | WV r DJVU r | IND r / w | MXF r | PSP r | X3F r / w DLL r | INX r | NEF r / w | QTIF r / w | XCF r DNG r / w | ISO r | NRW r / w | RA r | XLS r DOC r | ITC r | NUMBERS r | RAF r / w | XLSX r DOCX r | J2C r | O r | RAM r | XMP r / w / c DPX r | JNG r / w | ODP r | RAR r | ZIP r DR4 r / w / c | JP2 r / w | ODS r | RAW r / w |
    DSS r | JPEG r / w | ODT r | RIFF r |
    Meta Information-- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- --+-- -- -- -- -- -- -- -- -- -- -EXIF r / w / c | CIFF r / w | Ricoh RMETA r GPS r / w / c | AFCP r / w | Picture Info r IPTC r / w / c | Kodak Meta r / w | Adobe APP14 r XMP r / w / c | FotoStation r / w | MPF r MakerNotes r / w / c | PhotoMechanic r / w | Stim r Photoshop IRB r / w / c | JPEG 2000 r | DPX r ICC Profile r / w / c | DICOM r | APE r MIE r / w / c | Flash r | Vorbis r JFIF r / w / c | FlashPix r | SPIFF r Ducky APP12 r / w / c | QuickTime r | DjVu r PDF r / w / c | Matroska r | M2TS r PNG r / w / c | MXF r | PE / COFF r Canon VRD r / w / c | PrintIM r | AVCHD r Nikon Capture r / w / c | FLAC r | ZIP r GeoTIFF r / w / c | ID3 r | (and more)
</code></pre>
<h2>OPTIONS</h2>
<p> Case is not significant for any command-line option (including tag and group names), except for single-character options when the corresponding upper-case option exists. Many single-character options have equivalent long-name versions (shown in brackets), and some options have inverses which are invoked with a leading double-dash. Unrecognized options are interpreted as tag names (for this reason, multiple single-character options may <font SIZE="-1">NOT</font> be combined into one argument). Contrary to standard practice, options may appear after source file names on the exiftool command line.</p>
<h3>Option Summary</h3>
<p> Tag operations </p>
<p>  -TAG or &#8211;TAG                    Extract or exclude specified tag<br />
  -TAG[+-]=[VALUE]                 Write new value for tag<br />
  -TAG[+-]&lt;=DATFILE                Write tag value from contents of file<br />
  -TAG[+-]&lt;SRCTAG                  Copy tag value (see -tagsFromFile)<br />
  -tagsFromFile SRCFILE            Copy tag values from file<br />
  -x TAG      (-exclude)           Exclude specified tag</p>
<p> Input-output text formatting </p>
<p>  -args       (-argFormat)         Format metadata as exiftool arguments<br />
  -b          (-binary)            Output metadata in binary format<br />
  -c FMT      (-coordFormat)       Set format for GPS coordinates<br />
  -charset [[TYPE=]CHARSET]        Specify encoding for special characters<br />
  -csv[=CSVFILE]                   Export/import tags in CSV format<br />
  -d FMT      (-dateFormat)        Set format for date/time values<br />
  -D          (-decimal)           Show tag ID numbers in decimal<br />
  -E, -ex     (-escape(HTML|XML))  Escape values for HTML (-E) or XML (-ex)<br />
  -f          (-forcePrint)        Force printing of all specified tags<br />
  -g[NUM&#8230;]  (-groupHeadings)     Organize output by tag group<br />
  -G[NUM&#8230;]  (-groupNames)        Print group name for each tag<br />
  -h          (-htmlFormat)        Use HMTL formatting for output<br />
  -H          (-hex)               Show tag ID number in hexadecimal<br />
  -htmlDump[OFFSET]                Generate HTML-format binary dump<br />
  -j[=JSONFILE] (-json)            Export/import tags in JSON format<br />
  -l          (-long)              Use long 2-line output format<br />
  -L          (-latin)             Use Windows Latin1 encoding<br />
  -lang [LANG]                     Set current language<br />
  -listItem INDEX                  Extract specific item from a list<br />
  -n          (&#8211;printConv)        No print conversion<br />
  -p FMTFILE  (-printFormat)       Print output in specified format<br />
  -php                             Export tags as a PHP Array<br />
  -s[NUM]     (-short)             Short output format<br />
  -S          (-veryShort)         Very short output format<br />
  -sep STR    (-separator)         Set separator string for list items<br />
  -sort                            Sort output alphabetically<br />
  -struct                          Enable output of structured information<br />
  -t          (-tab)               Output in tab-delimited list format<br />
  -T          (-table)             Output in tabular format<br />
  -v[NUM]     (-verbose)           Print verbose messages<br />
  -w[+|!] EXT (-textOut)           Write (or overwrite!) output text files<br />
  -W[+|!] FMT (-tagOut)            Write output text file for each tag<br />
  -Wext EXT   (-tagOutExt)         Write only specified file types with -W<br />
  -X          (-xmlFormat)         Use RDF/XML output format</p>
<p> Processing control </p>
<p>  -a          (-duplicates)        Allow duplicate tags to be extracted<br />
  -e          (&#8211;composite)        Do not calculate composite tags<br />
  -ee         (-extractEmbedded)   Extract information from embedded files<br />
  -ext EXT    (-extension)         Process files with specified extension<br />
  -F[OFFSET]  (-fixBase)           Fix the base for maker notes offsets<br />
  -fast[NUM]                       Increase speed for slow devices<br />
  -fileOrder [-]TAG                Set file processing order<br />
  -i DIR      (-ignore)            Ignore specified directory name<br />
  -if EXPR                         Conditionally process files<br />
  -m          (-ignoreMinorErrors) Ignore minor errors and warnings<br />
  -o OUTFILE  (-out)               Set output file or directory name<br />
  -overwrite_original              Overwrite original by renaming tmp file<br />
  -overwrite_original_in_place     Overwrite original by copying tmp file<br />
  -P          (-preserve)          Preserve date/time of original file<br />
  -password PASSWD                 Password for processing protected files<br />
  -progress[:[TITLE]]              Show file progress count<br />
  -q          (-quiet)             Quiet processing<br />
  -r[.]       (-recurse)           Recursively process subdirectories<br />
  -scanForXMP                      Brute force XMP scan<br />
  -u          (-unknown)           Extract unknown tags<br />
  -U          (-unknown2)          Extract unknown binary tags too<br />
  -wm MODE    (-writeMode)         Set mode for writing/creating tags<br />
  -z          (-zip)               Read/write compressed information</p>
<p> Other options </p>
<p>&#8211; @ARGFILE Read command &#8211; line arguments from file &#8211; k(-pause)Pause before terminating<br />
    &#8211; list[w | f | wf | g[NUM] | d | x] List various exiftool capabilities<br />
    &#8211; ver Print exiftool version number</p>
<p> Special features </p>
<pre>
  -geotag TRKFILE                  Geotag images from specified GPS log
  -globalTimeShift SHIFT           Shift all formatted date/time values
  -use MODULE                      Add features from plug-in module
</pre>
<p> Utilities </p>
<pre>
  -delete_original[!]              Delete &quot;_original&quot; backups
  -restore_original                Restore from &quot;_original&quot; backups
</pre>
<p> Advanced options </p>
<p>  -api OPT[=VAL]                   Set ExifTool API option<br />
  -common_args                     Define common arguments<br />
  -config CFGFILE                  Specify configuration file name<br />
  -echo[NUM] TEXT                  Echo text to stdout or stderr<br />
  -execute[NUM]                    Execute multiple commands on one line<br />
  -srcfile FMT                     Process a different source file<br />
  -stay_open FLAG                  Keep reading -@ argfile even after EOF<br />
  -userParam PARAM[=VAL]           Set user parameter (API UserParam opt)<br />
  -windowTitle TITLE               Set console window title for each file</p>
<h3>Option Details</h3>
<p> <i>Tag operations</i></p>
<dl>
<dt><code>&#8211;</code><i></i><font SIZE="-1"><i>TAG</i></font><i></i></p>
<dd> Extract information for the specified tag (eg. <tt>&quot;-CreateDate&quot;</tt>). Multiple tags may be specified in a single command. A tag name is the handle by which a piece of information is referenced. See Image::ExifTool::TagNames for documentation on available tag names. A tag name may include leading group names separated by colons (eg. <tt>&quot;-EXIF:CreateDate&quot;</tt>, or <tt>&quot;-Doc1:XMP:Creator&quot;</tt>), and each group name may be prefixed by a digit to specify family number (eg. <tt>&quot;-1IPTC:City&quot;</tt>). Use the <code>-listg</code> option to list available group names by family. </p>
<p> A special tag name of <tt>&quot;All&quot;</tt> may be used to indicate all meta information (ie. <code>-All</code>). This is particularly useful when a group name is specified to extract all information in a group (but beware that unless the <code>-a</code> option is also used, some tags in the group may be suppressed by same-named tags in other groups). The wildcard characters <tt>&quot;?&quot;</tt> and <tt>&quot;*&quot;</tt> may be used in a tag name to match any single character and zero or more characters respectively.<br />
&nbsp;<wbr>These may not be used in a group name, with the exception that a group name of <tt>&quot;*&quot;</tt> (or <tt>&quot;All&quot;</tt>) may be used to extract all instances of a tag (as if <code>-a</code> was used). Note that arguments containing wildcards must be quoted on the command line of most systems to prevent shell globbing. </p>
<p> A <tt>&quot;#&quot;</tt> may be appended to the tag name to disable the print conversion on a per-tag basis (see the <code>-n</code> option). This may also be used when writing or copying tags. </p>
<p> If no tags are specified, all available information is extracted (as if <tt>&quot;-All&quot;</tt> had been specified). </p>
<p> Note: Descriptions, not tag names, are shown by default when extracting information. Use the <code>-s</code> option to see the tag names instead.</p>
<dt><code>&#8212;</code><i></i><font SIZE="-1"><i>TAG</i></font><i></i></p>
<dd> Exclude specified tag from extracted information. Same as the <code>-x</code> option. Group names and wildcards are permitted as described above for <code>-TAG</code>. Once excluded from the output, a tag may not be re-included by a subsequent option. May also be used following a <code>-tagsFromFile</code> option to exclude tags from being copied (when redirecting to another tag, it is the source tag that should be excluded), or to exclude groups from being deleted when deleting all information (eg. <tt>&quot;-all= --exif:all&quot;</tt> deletes all but <font SIZE="-1">EXIF</font> information). But note that this will not exclude individual tags from a group delete (unless a family 2 group is specified, see note 4 below). Instead, individual tags may be recovered using the <code>-tagsFromFile</code> option (eg. <tt>&quot;-all= -tagsfromfile @ -artist&quot;</tt>).</p>
<dt><code>&#8211;</code><i></i><font SIZE="-1"><i>TAG</i></font><i></i>[+-]<code>=</code>[<i></i><font SIZE="-1"><i>VALUE</i></font><i></i>]</p>
<dd> Write a new value for the specified tag (eg. <tt>&quot;-comment=wow&quot;</tt>), or delete the tag if no <i></i><font SIZE="-1"><i>VALUE</i></font><i></i> is given (eg. <tt>&quot;-comment=&quot;</tt>). <tt>&quot;+=&quot;</tt> and <tt>&quot;-=&quot;</tt> are used to add or remove existing entries from a list, or to shift date/time values (see Image::ExifTool::Shift.pl and note 6 below for more details). <tt>&quot;+=&quot;</tt> may also be used to increment numerical values (or decrement if <i></i><font SIZE="-1"><i>VALUE</i></font><i></i> is negative), and <tt>&quot;-=&quot;</tt> may be used to conditionally delete or replace a tag (see &#8220;<font SIZE="-1">WRITING EXAMPLES&#8221;</font> for examples). </p>
<p> <i></i><font SIZE="-1"><i>TAG</i></font><i></i> may contain one or more leading family 0, 1 or 2 group names, prefixed by optional family numbers, and separated colons. If no group name is specified, the tag is created in the preferred group, and updated in any other location where a same-named tag already exists. The preferred group is the first group in the following list where <i></i><font SIZE="-1"><i>TAG</i></font><i></i> is valid: 1) <font SIZE="-1">EXIF, 2</font>) <font SIZE="-1">IPTC, 3</font>) <font SIZE="-1">XMP.</font> </p>
<p> The wildcards <tt>&quot;*&quot;</tt> and <tt>&quot;?&quot;</tt> may be used in tag names to assign the same value to multiple tags. When specified with wildcards, &#8220;unsafe&#8221; tags are not written. A tag name of <tt>&quot;All&quot;</tt> is equivalent to <tt>&quot;*&quot;</tt> (except that it doesn&#8217;t require quoting, while arguments with wildcards do on systems with shell globbing), and is often used when deleting all metadata (ie. <tt>&quot;-All=&quot;</tt>) or an entire group (eg. <tt>&quot;-GROUP:All=&quot;</tt>, see note 4 below). Note that not all groups are deletable, and that the <font SIZE="-1">JPEG APP14 </font>&#8220;Adobe&#8221; group is not removed by default with <tt>&quot;-All=&quot;</tt> because it may affect the appearance of the image. However, this will remove color space information, so the colors may be affected (but this may be avoided by copying back the tags defined by the ColorSpaceTags shortcut). Use the <code>-listd</code> option for a complete list of deletable groups, and see note 5 below regarding the &#8220;<font SIZE="-1">APP&#8221;</font> groups. Also, within an image some groups may be contained within others, and these groups are removed if the containing group is deleted: </p>
<pre>
  JPEG Image:
  - Deleting EXIF or IFD0 also deletes ExifIFD, GlobParamIFD,
    GPS, IFD1, InteropIFD, MakerNotes, PrintIM and SubIFD.
  - Deleting ExifIFD also deletes InteropIFD and MakerNotes.
  - Deleting Photoshop also deletes IPTC.
  TIFF Image:
  - Deleting EXIF only removes ExifIFD which also deletes
    InteropIFD and MakerNotes.
</pre>
<p> Notes: </p>
<p> 1) <code>Many tag values may be assigned in a single command</code>. If two assignments affect the same tag, the latter takes precedence (except for list-type tags, for which both values are written). </p>
<p> 2) In general, MakerNotes tags are considered &#8220;Permanent&#8221;, and may be edited but not created or deleted individually. This avoids many potential problems, including the inevitable compatibility problems with <font SIZE="-1">OEM</font> software which may be very inflexible about the information it expects to find in the maker notes. </p>
<p> 3) Changes to <font SIZE="-1">PDF</font> files by ExifTool are reversible (by deleting the update with <tt>&quot;-PDF-update:all=&quot;</tt>) because the original information is never actually deleted from the file. So ExifTool alone may not be used to securely edit metadata in <font SIZE="-1">PDF</font> files. </p>
<p> 4) Specifying <tt>&quot;-GROUP:all=&quot;</tt> deletes the entire group as a block only if a single family 0 or 1 group is specified. Otherwise all deletable tags in the specified group(s) are removed individually, and in this case is it possible to exclude individual tags from a mass delete. For example, <tt>&quot;-time:all --Exif:Time:All&quot;</tt> removes all deletable Time tags except those in the <font SIZE="-1">EXIF. </font> This difference also applies if family 2 is specified when deleting all groups. For example, <tt>&quot;-2all:all=&quot;</tt> deletes tags individually, while <tt>&quot;-all:all=&quot;</tt> deletes entire blocks. </p>
<p> 5) The &#8220;<font SIZE="-1">APP&#8221;</font> group names (&#8220;<font SIZE="-1">APP0&#8221;</font> through &#8220;<font SIZE="-1">APP15&#8221;</font>) are used to delete <font SIZE="-1">JPEG</font> application segments which are not associated with another deletable group. For example, specifying <tt>&quot;-APP14:All=&quot;</tt> will <font SIZE="-1">NOT</font> delete the <font SIZE="-1">APP14 </font>&#8220;Adobe&#8221; segment because this is accomplished with <tt>&quot;-Adobe:All&quot;</tt>. </p>
<p> 6) When shifting a value, the shift is applied to the original value of the tag, overriding any other values previously assigned to the tag on the same command line. To shift a date/time value and copy it to another tag in the same operation, use the <code>-globalTimeShift</code> option. </p>
<p> Special feature: Integer values may be specified in hexadecimal with a leading <tt>&quot;0x&quot;</tt>, and simple rational values may be specified as fractions.</p>
<dt><code>&#8211;</code><i></i><font SIZE="-1"><i>TAG</i></font><i></i>&lt;=<i></i><font SIZE="-1"><i>DATFILE</i></font><i></i> or <code>&#8211;</code><i></i><font SIZE="-1"><i>TAG</i></font><i></i>&lt;=<i></i><font SIZE="-1"><i>FMT</i></font><i></i></p>
<dd> Set the value of a tag from the contents of file <i></i><font SIZE="-1"><i>DATFILE</i></font><i></i>. The file name may also be given by a <i></i><font SIZE="-1"><i>FMT</i></font><i></i> string where <tt>%d</tt>, <tt>%f</tt> and <tt>%e</tt> represent the directory, file name and extension of the original <i></i><font SIZE="-1"><i>FILE</i></font><i></i> (see the <code>-w</code> option for more details). Note that quotes are required around this argument to prevent shell redirection since it contains a <tt>&quot;&lt;&quot;</tt> symbol. If <i></i><font SIZE="-1"><i>DATFILE</i></font><i></i>/<i></i><font SIZE="-1"><i>FMT</i></font><i></i> is not provided, the effect is the same as <tt>&quot;-TAG=&quot;</tt>, and the tag is simply deleted. <tt>&quot;+&lt;=&quot;</tt> or <tt>&quot;-&lt;=&quot;</tt> may also be used to add or delete specific list entries, or to shift date/time values.</p>
<dt><code>-tagsFromFile</code> <i></i><font SIZE="-1"><i>SRCFILE</i></font><i></i> or <i></i><font SIZE="-1"><i>FMT</i></font><i></i></p>
<dd> Copy tag values from <i></i><font SIZE="-1"><i>SRCFILE</i></font><i></i> to <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. Tag names on the command line after this option specify the tags to be copied, or excluded from the copy. Wildcards are permitted in these tag names. If no tags are specified, then all possible tags (see note 1 below) from the source file are copied to same-named tags in the preferred location of the output file (the same as specifying <tt>&quot;-all&quot;</tt>). More than one <code>-tagsFromFile</code> option may be used to copy tags from multiple files. </p>
<p> By default, this option will update any existing and writable same-named tags in the output <i></i><font SIZE="-1"><i>FILE</i></font><i></i>, but will create new tags only in their preferred groups. This allows some information to be automatically transferred to the appropriate group when copying between images of different formats. However, if a group name is specified for a tag then the information is written only to this group (unless redirected to another group, see below). If <tt>&quot;All&quot;</tt> is used as a group name, then the specified tag(s) are written to the same family 1 group they had in the source file (ie. the same specific location, like ExifIFD or XMP-dc). For example, the common operation of copying all writable tags to the same specific locations in the output <i></i><font SIZE="-1"><i>FILE</i></font><i></i> is achieved by adding <tt>&quot;-all:all&quot;</tt>. A different family may be specified by adding a leading family number to the group name (eg. <tt>&quot;-0all:all&quot;</tt> preserves the same general location, like <font SIZE="-1">EXIF</font> or <font SIZE="-1">XMP</font>). </p>
<p> <i></i><font SIZE="-1"><i>SRCFILE</i></font><i></i> may be the same as <i></i><font SIZE="-1"><i>FILE</i></font><i></i> to move information around within a single file. In this case, <tt>&quot;@&quot;</tt> may be used to represent the source file (ie. <tt>&quot;-tagsFromFile @&quot;</tt>), permitting this feature to be used for batch processing multiple files. Specified tags are then copied from each file in turn as it is rewritten. For advanced batch use, the source file name may also be specified using a <i></i><font SIZE="-1"><i>FMT</i></font><i></i> string in which <tt>%d</tt>, <tt>%f</tt> and <tt>%e</tt> represent the directory, file name and extension of <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. See <code>-w</code> option for <i></i><font SIZE="-1"><i>FMT</i></font><i></i> string examples. </p>
<p> A powerful redirection feature allows a destination tag to be specified for each copied tag. With this feature, information may be written to a tag with a different name or group. This is done using &quot;&#8217;-<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&lt;<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>&#8216;&#8220; or &#8221;&#8217;-<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>&gt;<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&#8216;&quot; on the command line after <code>-tagsFromFile</code>, and causes the value of <i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i> to be copied from <i></i><font SIZE="-1"><i>SRCFILE</i></font><i></i> and written to <i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i> in <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. Note that this argument must be quoted to prevent shell redirection, and there is no <tt>&quot;=&quot;</tt> sign as when assigning new values. Source and/or destination tags may be prefixed by a group name and/or suffixed by <tt>&quot;#&quot;</tt>. Wildcards are allowed in both the source and destination tag names. A destination group and/or tag name of <tt>&quot;All&quot;</tt> or <tt>&quot;*&quot;</tt> writes to the same family 1 group and/or tag name as the source. If no destination group is specified, the information is written to the preferred group. Whitespace around the <tt>&quot;&gt;&quot;</tt> or <tt>&quot;&lt;&quot;</tt> is ignored. As a convenience, <tt>&quot;-tagsFromFile @&quot;</tt> is assumed for any redirected tags which are specified without a prior <code>-tagsFromFile</code> option. Copied tags may also be added or deleted from a list with arguments of the form &quot;&#8217;-<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>+&lt;<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&#8216;&#8220; or &#8221;&#8217;-<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>-&lt;<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&#8216;&quot;. </p>
<p> An extension of the redirection feature allows strings involving tag names to be used on the right hand side of the <tt>&quot;&lt;&quot;</tt> symbol with the syntax &quot;&#8217;-<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&lt;<i></i><font SIZE="-1"><i>STR</i></font><i></i>&#8216;&quot;, where tag names in <i></i><font SIZE="-1"><i>STR</i></font><i></i> are prefixed with a <tt>&quot;$&quot;</tt> symbol. See the <code>-p</code> option for more details about this syntax. Strings starting with a <tt>&quot;=&quot;</tt> sign must insert a single space after the <tt>&quot;&lt;&quot;</tt> to avoid confusion with the <tt>&quot;&lt;=&quot;</tt> operator which sets the tag value from the contents of a file. A single space at the start of the string is removed if it exists, but all other whitespace in the string is preserved. See note 8 below about using shortcuts or wildcards with the redirection feature. </p>
<p> See &#8220;<font SIZE="-1">COPYING EXAMPLES&#8221;</font> for examples using <code>-tagsFromFile</code>. </p>
<p> Notes: </p>
<p> 1) Some tags (generally tags which may affect the appearance of the image) are considered &#8220;unsafe&#8221; to write, and are only copied if specified explicitly (ie. no wildcards). See the tag name documentation for more details about &#8220;unsafe&#8221; tags. </p>
<p> 2) Be aware of the difference between excluding a tag from being copied (&#8211;<i></i><font SIZE="-1"><i>TAG</i></font><i></i>), and deleting a tag (-<i></i><font SIZE="-1"><i>TAG</i></font><i></i>=). Excluding a tag prevents it from being copied to the destination image, but deleting will remove a pre-existing tag from the image. </p>
<p> 3) The maker note information is copied as a block, so it isn&#8217;t affected like other information by subsequent tag assignments on the command line, and individual makernote tags may not be excluded from a block copy. Also, since the PreviewImage referenced from the maker notes may be rather large, it is not copied, and must be transferred separately if desired. </p>
<p> 4) The order of operations is to copy all specified tags at the point of the <code>-tagsFromFile</code> option in the command line. Any tag assignment to the right of the <code>-tagsFromFile</code> option is made after all tags are copied. For example, new tag values are set in the order One, Two, Three then Four with this command: </p>
<pre>
    exiftool -One=1 -tagsFromFile s.jpg -Two -Four=4 -Three d.jpg
</pre>
<p> This is significant in the case where an overlap exists between the copied and assigned tags because later operations may override earlier ones. </p>
<p> 5) The normal behaviour of copied tags differs subtly from that of assigned tags for list-type tags. When copying to a list, each copied tag overrides any previous operations on the list. While this avoids duplicate list items when copying groups of tags from a file containing redundant information, it also prevents values of different tags from being copied into the same list when this is the intent. So a <code>-addTagsFromFile</code> option is provided which allows copying of multiple tags into the same list. eg) </p>
<pre>
    exiftool -addtagsfromfile @ '-subject&lt;make' '-subject&lt;model' ...
</pre>
<p> Similarly, <code>-addTagsFromFile</code> must be used when conditionally replacing a tag to prevent overriding earlier conditions. </p>
<p> Other than these differences, the <code>-tagsFromFile</code> and <code>-addTagsFromFile</code> options are equivalent. </p>
<p> 6) The <code>-a</code> option (allow duplicate tags) is always in effect when copying tags from <i></i><font SIZE="-1"><i>SRCFILE</i></font><i></i>. </p>
<p> 7) Structured tags are copied by default when copying tags. See the <code>-struct</code> option for details. </p>
<p> 8) With the redirection feature, copying a tag directly (ie. &quot;&#8217;-<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&lt;<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>&#8216;&#8220;) is not the same as interpolating its value inside a string (ie. &#8221;&#8217;-<i></i><font SIZE="-1"><i>DSTTAG</i></font><i></i>&lt;$<i></i><font SIZE="-1"><i>SRCTAG</i></font><i></i>&#8216;&quot;) for shortcut tags or tag names containing wildcards. When copying directly, the values of each matching source tag are copied individually to the destination tag (as if multiple redirection arguments were used). However, when interpolated inside a string, the values of shortcut tags are concatenated, and wildcards are not allowed.</p>
<dt><code>-x</code> <i></i><font SIZE="-1"><i>TAG</i></font><i></i> (<code>-exclude</code>)</p>
<dd> Exclude the specified tag. There may be multiple <code>-x</code> options. This has the same effect as &#8212;<i></i><font SIZE="-1"><i>TAG</i></font><i></i> on the command line. See the &#8212;<i></i><font SIZE="-1"><i>TAG</i></font><i></i> documentation above for a complete description.</dl>
<p> <i>Input-output text formatting</i> </p>
<p> Note that trailing spaces are removed from extracted values for most output text formats. The exceptions are <tt>&quot;-b&quot;</tt>, <tt>&quot;-csv&quot;</tt>, <tt>&quot;-j&quot;</tt> and <tt>&quot;-X&quot;</tt>.</p>
<dl>
<dt><code>-args</code> (<code>-argFormat</code>)</p>
<dd> Output information in the form of exiftool arguments, suitable for use with the <code>-@</code> option when writing. May be combined with the <code>-G</code> option to include group names. This feature may be used to effectively copy tags between images, but allows the metadata to be altered by editing the intermediate file (<tt>&quot;out.args&quot;</tt> in this example): </p>
<pre>
    exiftool -args -G1 --filename --directory src.jpg &gt; out.args
    exiftool -@ out.args dst.jpg
</pre>
<p> Note: Be careful when copying information with this technique since it is easy to write tags which are normally considered &#8220;unsafe&#8221;. For instance, the FileName and Directory tags are excluded in the example above to avoid renaming and moving the destination file. Also note that the second command above will produce warning messages for any tags which are not writable. </p>
<p> As well, the <code>-sep</code> option should be used when reading back to maintain separate list items, and the <code>-struct</code> option may be used when extracting to preserve structured <font SIZE="-1">XMP</font> information.</p>
<dt><code>-b</code> (<code>-binary</code>)</p>
<dd> Output requested metadata in binary format without tag names or descriptions. This option is mainly used for extracting embedded images or other binary data, but it may also be useful for some text strings since control characters (such as newlines) are not replaced by &#8216;.&#8217; as they are in the default output. List items are separated by a newline when extracted with the <code>-b</code> option. May be combined with <tt>&quot;-j&quot;</tt>, <tt>&quot;-php&quot;</tt> or <tt>&quot;-X&quot;</tt> to extract binary data in <font SIZE="-1">JSON, PHP</font> or <font SIZE="-1">XML</font> format.</p>
<dt><code>-c</code> <i></i><font SIZE="-1"><i>FMT</i></font><i></i> (<code>-coordFormat</code>)</p>
<dd> Set the print format for <font SIZE="-1">GPS</font> coordinates. <i></i><font SIZE="-1"><i>FMT</i></font><i></i> uses the same syntax as the <tt>&quot;printf&quot;</tt> format string. The specifiers correspond to degrees, minutes and seconds in that order, but minutes and seconds are optional. For example, the following table gives the output for the same coordinate using various formats: </p>
<p>            FMT                  Output<br />
    &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;-    &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
    &#8220;%d deg %d&#8217; %.2f&#8221;\&#8221;    54 deg 59&#8242; 22.80&#8243;  (default for reading)<br />
    &#8220;%d %d %.8f&#8221;           54 59 22.80000000  (default for copying)<br />
    &#8220;%d deg %.4f min&#8221;      54 deg 59.3800 min<br />
    &#8220;%.6f degrees&#8221;         54.989667 degrees</p>
<p> Notes: </p>
<p> 1) To avoid loss of precision, the default coordinate format is different when copying tags using the <code>-tagsFromFile</code> option. </p>
<p> 2) If the hemisphere is known, a reference direction (N, S, E or W) is appended to each printed coordinate, but adding a <tt>&quot;+&quot;</tt> to the format specifier (eg. <tt>&quot;%+.6f&quot;</tt>) prints a signed coordinate instead. </p>
<p> 3) This print formatting may be disabled with the <code>-n</code> option to extract coordinates as signed decimal degrees.</p>
<dt><code>-charset</code> [[<i></i><font SIZE="-1"><i>TYPE</i></font><i></i>=]<i></i><font SIZE="-1"><i>CHARSET</i></font><i></i>]</p>
<dd> If <i></i><font SIZE="-1"><i>TYPE</i></font><i></i> is <tt>&quot;ExifTool&quot;</tt> or not specified, this option sets the ExifTool character encoding for output tag values when reading and input values when writing. The default ExifTool encoding is <tt>&quot;UTF8&quot;</tt>. If no <i></i><font SIZE="-1"><i>CHARSET</i></font><i></i> is given, a list of available character sets is returned. Valid <i></i><font SIZE="-1"><i>CHARSET</i></font><i></i> values are: </p>
<p>CHARSET Alias(es) Description<br />
    &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;UTF8 cp65001,<br />
    UTF &#8211; 8 UTF &#8211; 8 characters(default) Latin cp1252, Latin1 Windows Latin1(West European) Latin2 cp1250 Windows Latin2(Central European) Cyrillic cp1251, Russian Windows Cyrillic Greek cp1253 Windows Greek Turkish cp1254 Windows Turkish Hebrew cp1255 Windows Hebrew Arabic cp1256 Windows Arabic Baltic cp1257 Windows Baltic Vietnam cp1258 Windows Vietnamese Thai cp874 Windows Thai MacRoman cp10000, Roman Macintosh Roman MacLatin2 cp10029 Macintosh Latin2(Central Europe) MacCyrillic cp10007 Macintosh Cyrillic MacGreek cp10006 Macintosh Greek MacTurkish cp10081 Macintosh Turkish MacRomanian cp10010 Macintosh Romanian MacIceland cp10079 Macintosh Icelandic MacCroatian cp10082 Macintosh Croatian</p>
<p> <i></i><font SIZE="-1"><i>TYPE</i></font><i></i> may be <tt>&quot;FileName&quot;</tt> to specify the encoding of file names on the command line (ie. <i></i><font SIZE="-1"><i>FILE</i></font><i></i> arguments). In Windows, this triggers use of wide-character i/o routines, thus providing support for Unicode file names. See the &#8220;<font SIZE="-1">WINDOWS UNICODE FILE NAMES&#8221;</font> section below for details. </p>
<p> Other values of <i></i><font SIZE="-1"><i>TYPE</i></font><i></i> listed below are used to specify the internal encoding of various meta information formats. </p>
<p>TYPE Description Default&#8211; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211; &#8212; &#8212; &#8212; -EXIF Internal encoding of EXIF &#8220;ASCII&#8221; strings(none)<br />
    ID3 Internal encoding of ID3v1 information Latin<br />
    IPTC Internal IPTC encoding to assume when Latin<br />
    IPTC : CodedCharacterSet is not defined<br />
           Photoshop Internal encoding of Photoshop IRB strings Latin<br />
           QuickTime Internal encoding of QuickTime strings MacRoman<br />
           RIFF Internal encoding of RIFF strings 0</p>
<p> See &lt;<a rel="nofollow" href="http://owl.phy.queensu.ca/~phil/exiftool/faq.html#Q10">http://owl.phy.queensu.ca/~phil/exiftool/faq.html#Q10</a>&gt; for more information about coded character sets, and the Image::ExifTool Options for more details about the <code>-charset</code> settings.</p>
<dt><code>-csv</code>[=<i></i><font SIZE="-1"><i>CSVFILE</i></font><i></i>]</p>
<dd> Export information in <font SIZE="-1">CSV</font> format, or import information if <i></i><font SIZE="-1"><i>CSVFILE</i></font><i></i> is specified. When importing, the <font SIZE="-1">CSV</font> file must be in exactly the same format as the exported file. The first row of the <i></i><font SIZE="-1"><i>CSVFILE</i></font><i></i> must be the ExifTool tag names (with optional group names) for each column of the file, and values must be separated by commas. A special &#8220;SourceFile&#8221; column specifies the files associated with each row of information (and a SourceFile of &#8220;*&#8221; may be used to define default tags to be imported for all files). The following examples demonstrate basic use of this option: </p>
<pre>
    # generate CSV file with common tags from all images in a directory
    exiftool -common -csv dir &gt; out.csv
    # update metadata for all images in a directory from CSV file
    exiftool -csv=a.csv dir
</pre>
<p> Empty values are ignored when importing. Also, FileName and Directory columns are ignored if they exist (ie. ExifTool will not attempt to write these tags with a <font SIZE="-1">CSV</font> import). To force a tag to be deleted, use the <code>-f</code> option and set the value to &#8220;-&#8221; in the <font SIZE="-1">CSV</font> file (or to the MissingTagValue if this <font SIZE="-1">API</font> option was used). Multiple databases may be imported in a single command. </p>
<p> When exporting a <font SIZE="-1">CSV</font> file, the <code>-g</code> or <code>-G</code> option to add group names to the tag headings. If the <code>-a</code> option is used to allow duplicate tag names, the duplicate tags are only included in the <font SIZE="-1">CSV</font> output if the column headings are unique. Adding the <code>-G4</code> option ensures a unique column heading for each tag. When exporting specific tags, the <font SIZE="-1">CSV</font> columns are arranged in the same order as the specified tags provided the column headings exactly match the specified tag names, otherwise the columns are sorted in alphabetical order. </p>
<p> When importing from a <font SIZE="-1">CSV</font> file, only files specified on the command line are processed. Any extra entries in the <font SIZE="-1">CSV</font> file are ignored. </p>
<p> List-type tags are stored as simple strings in a <font SIZE="-1">CSV</font> file, but the <code>-sep</code> option may be used to split them back into separate items when importing. </p>
<p> Special feature: <code>-csv</code>+=<i></i><font SIZE="-1"><i>CSVFILE</i></font><i></i> may be used to add items to existing lists. This affects only list-type tags. Also applies to the <code>-j</code> option. </p>
<p> Note that this option is fundamentally different than all other output format options because it requires information from all input files to be buffered in memory before the output is written. This may result in excessive memory usage when processing a very large number of files with a single command. Also, it makes this option incompatible with the <code>-w</code> option.</p>
<dt><code>-d</code> <i></i><font SIZE="-1"><i>FMT</i></font><i></i> (<code>-dateFormat</code>)</p>
<dd> Set the format for date/time tag values. The specifics of the <i></i><font SIZE="-1"><i>FMT</i></font><i></i> syntax are system dependent &#8212; consult the <tt>&quot;strftime&quot;</tt> man page on your system for details. The default format is equivalent to &#8220;%Y:%m:%d <tt>%H:</tt>%M:%S&#8221;. This option has no effect on date-only or time-only tags and ignores timezone information if present. Only one <code>-d</code> option may be used per command. Requires POSIX::strptime or Time::Piece for the inversion conversion when writing.</p>
<dt><code>-D</code> (<code>-decimal</code>)</p>
<dd> Show tag <font SIZE="-1">ID</font> number in decimal when extracting information.</p>
<dt><code>-E</code>, <code>-ex</code> (<code>-escapeHTML</code>, <code>-escapeXML</code>)</p>
<dd> Escape characters in output values for <font SIZE="-1">HTML </font>(<code>-E</code>) or <font SIZE="-1">XML </font>(<code>-ex</code>). For <font SIZE="-1">HTML,</font> all characters with Unicode code points above U+007F are escaped as well as the following 5 characters: &amp; (&amp;amp;) &#8216; (&amp;#39;) &quot; (&amp;quot;) &gt; (&amp;gt;) and &lt; (&amp;lt;). For <font SIZE="-1">XML,</font> only these 5 characters are escaped. The <code>-E</code> option is implied with <code>-h</code>, and <code>-ex</code> is implied with <code>-X</code>. The inverse conversion is applied when writing tags.</p>
<dt><code>-f</code> (<code>-forcePrint</code>)</p>
<dd> Force printing of tags even if their values are not found. This option only applies when specific tags are requested on the command line (ie. not with wildcards or by <tt>&quot;-all&quot;</tt>). With this option, a dash (<tt>&quot;-&quot;</tt>) is printed for the value of any missing tag, but the dash may be changed via the <font SIZE="-1">API</font> MissingTagValue option. May also be used to add a &#8216;flags&#8217; attribute to the <code>-listx</code> output, or to allow tags to be deleted when writing with the <code>-csv</code>=<i></i><font SIZE="-1"><i>CSVFILE</i></font><i></i> feature.</p>
<dt><code>-g</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>][:<i></i><font SIZE="-1"><i>NUM</i></font><i></i>&#8230;] (<code>-groupHeadings</code>)</p>
<dd> Organize output by tag group. <i></i><font SIZE="-1"><i>NUM</i></font><i></i> specifies a group family number, and may be 0 (general location), 1 (specific location), 2 (category), 3 (document number) or 4 (instance number). <code>-g0</code> is assumed if a family number is not specified, and family numbers may be added wherever <code>-g</code> is mentioned in the documentation. Multiple families may be specified by separating them with colons. By default the resulting group name is simplified by removing any leading <tt>&quot;Main:&quot;</tt> and collapsing adjacent identical group names, but this can be avoided by placing a colon before the first family number (eg. <code>-g:3:1</code>). Use the <code>-listg</code> option to list group names for a specified family.</p>
<dt><code>-G</code>[<i></i><font SIZE="-1"><i>NUM</i></font><i></i>][:<i></i><font SIZE="-1"><i>NUM</i></font><i></i>&#8230;] (<code>-groupNames</code>)</p>
<dd> Same as <code>-g</code> but print group name for each tag. <code>-G0</code> is assumed if <i></i><font SIZE="-1"><i>NUM</i></font><i></i> is not specified. May be combined with a number of other options to add group names to the output. Note that <i></i><font SIZE="-1"><i>NUM</i></font><i></i> may be added wherever <code>-G</code> is mentioned in the documentation. See the <code>-g</code> option above for details.</p>
<dt><code>-h</code> (<code>-htmlFormat</code>)</p>
<dd> Use <font SIZE="-1">HTML</font> table formatting for output. Implies the <code>-E</code> option. The formatting options <code>-D</code>, <code>-H</code>, <code>-g</code>, <code>-G</code>, <code>-l</code> and <code>-s</code> may be used in combination with <code>-h</code> to influence the <font SIZE="-1">HTML</font> format.</p>
<dt><code>-H</code> (<code>-hex</code>)</p>
<dd> Show tag <font SIZE="-1">ID</font> number in hexadecimal when extracting information.</p>
<dt><code>-htmlDump</code>[<i></i><font SIZE="-1"><i>OFFSET</i></font><i></i>]</p>
<dd> Generate a dynamic web page containing a hex dump of the <font SIZE="-1">EXIF</font> information. This can be a very powerful tool for low-level analysis of <font SIZE="-1">EXIF</font> information. The <code>-htmlDump</code> option is also invoked if the <code>-v</code> and <code>-h</code> options are used together. The verbose level controls the maximum length of the blocks dumped. An <i></i><font SIZE="-1"><i>OFFSET</i></font><i></i> may be given to specify the base for displayed offsets. If not provided, the <font SIZE="-1">EXIF/TIFF</font> base offset is used. Use <code>-htmlDump0</code> for absolute offsets. Currently only <font SIZE="-1">EXIF/TIFF</font> and <font SIZE="-1">JPEG</font> information is dumped, but the -u option can be used to give a raw hex dump of other file formats.</p>
<dt><code>-j</code>[=<i></i><font SIZE="-1"><i>JSONFILE</i></font><i></i>] (<code>-json</code>)</p>
<dd> Use <font SIZE="-1">JSON </font>(JavaScript Object Notation) formatting for console output, or import <font SIZE="-1">JSON</font> file if <i></i><font SIZE="-1"><i>JSONFILE</i></font><i></i> is specified. This option may be combined with <code>-g</code> to organize the output into objects by group, or <code>-G</code> to add group names to each tag. List-type tags with multiple items are output as <font SIZE="-1">JSON</font> arrays unless <code>-sep</code> is used. By default <font SIZE="-1">XMP</font> structures are flattened into individual tags in the <font SIZE="-1">JSON</font> output, but the original structure may be preserved with the <code>-struct</code> option (this also causes all list-type <font SIZE="-1">XMP</font> tags to be output as <font SIZE="-1">JSON</font> arrays, otherwise single-item lists are output as simple strings). The <code>-a</code> option is implied if the <code>-g</code> or <code>-G</code> options are used, otherwise it is ignored and duplicate tags are suppressed. Adding the <code>-D</code> or <code>-H</code> option changes tag values to <font SIZE="-1">JSON</font> objects with &#8220;val&#8221; and &#8220;id&#8221; fields, and adding <code>-l</code> adds a &#8220;desc&#8221; field, and a &#8220;num&#8221; field if the numerical value is different from the converted &#8220;val&#8221;. The <code>-b</code> option may be added to output binary data, encoded in base64 if necessary (indicated by &#8220;base64:&#8221; as the first 7 bytes of the value). The <font SIZE="-1">JSON</font> output is <font SIZE="-1">UTF-8</font> regardless of any <code>-L</code> or <code>-charset</code> option setting, but the <font SIZE="-1">UTF-8</font> validation is disabled if a character set other than <font SIZE="-1">UTF-8</font> is specified. </p>
<p> If <i></i><font SIZE="-1"><i>JSONFILE</i></font><i></i> is specified, the file is imported and the tag definitions from the file are used to set tag values on a per-file basis. The special &#8220;SourceFile&#8221; entry in each <font SIZE="-1">JSON</font> object associates the information with a specific target file. An object with a missing SourceFile or a SourceFile of &#8220;*&#8221; defines default tags for all target files. The imported <font SIZE="-1">JSON</font> file must have the same format as the exported <font SIZE="-1">JSON</font> files with the exception that the <code>-g</code> option is not compatible with the import file format (use <code>-G</code> instead). Additionally, tag names in the input <font SIZE="-1">JSON</font> file may be suffixed with a <tt>&quot;#&quot;</tt> to disable print conversion. </p>
<p> Unlike <font SIZE="-1">CSV</font> import, empty values are not ignored, and will cause an empty value to be written if supported by the specific metadata type. Tags are deleted by using the <code>-f</code> option and setting the tag value to &#8220;-&#8221; (or to the MissingTagValue setting if this <font SIZE="-1">API</font> option was used). Importing with <code>-j</code>+=<i></i><font SIZE="-1"><i>JSONFILE</i></font><i></i> causes new values to be added to existing lists.</p>
<dt><code>-l</code> (<code>-long</code>)</p>
<dd> Use long 2-line Canon-style output format. Adds a description and unconverted value (if it is different from the converted value) to the <font SIZE="-1">XML, JSON</font> or <font SIZE="-1">PHP</font> output when <code>-X</code>, <code>-j</code> or <code>-php</code> is used. May also be combined with <code>-listf</code>, <code>-listr</code> or <code>-listwf</code> to add descriptions of the file types.</p>
<dt><code>-L</code> (<code>-latin</code>)</p>
<dd> Use Windows Latin1 encoding (cp1252) for output tag values instead of the default <font SIZE="-1">UTF-8. </font> When writing, <code>-L</code> specifies that input text values are Latin1 instead of <font SIZE="-1">UTF-8. </font> Equivalent to <tt>&quot;-charset latin&quot;</tt>.</p>
<dt><code>-lang</code> [<i></i><font SIZE="-1"><i>LANG</i></font><i></i>]</p>
<dd> Set current language for tag descriptions and converted values. <i></i><font SIZE="-1"><i>LANG</i></font><i></i> is <tt>&quot;de&quot;</tt>, <tt>&quot;fr&quot;</tt>, <tt>&quot;ja&quot;</tt>, etc. Use <code>-lang</code> with no other arguments to get a list of available languages. The default language is <tt>&quot;en&quot;</tt> if <code>-lang</code> is not specified. Note that tag/group names are always English, independent of the <code>-lang</code> setting, and translation of warning/error messages has not yet been implemented. May also be combined with <code>-listx</code> to output descriptions in one language only. </p>
<p> By default, ExifTool uses <font SIZE="-1">UTF-8</font> encoding for special characters, but the the <code>-L</code> or <code>-charset</code> option may be used to invoke other encodings. </p>
<p> Currently, the language support is not complete, but users are welcome to help improve this by submitting their own translations. To submit a set of translations, first use the <code>-listx</code> option and redirect the output to a file to generate an <font SIZE="-1">XML</font> tag database, then add entries for other languages, zip this file, and email it to phil at owl.phy.queensu.ca for inclusion in ExifTool. </p>
<p> Note: ExifTool uses Unicode::LineBreak if available to help preserve the column alignment of the plain text output for languages with a variable-width character set.</p>
<dt><code>-listItem</code> <i></i><font SIZE="-1"><i>INDEX</i></font><i></i></p>
<dd> For list-type tags, this causes only the item with the specified index to be extracted. <i></i><font SIZE="-1"><i>INDEX</i></font><i></i> is 0 for the first item in the list. Negative indices may also be used to reference items from the end of the list. Has no effect on single-valued tags. Also applies to tag values when copying, and in <code>-if</code> conditions.</p>
<dt><code>-n</code> (<code>&#8211;printConv</code>)</p>
<dd> Disable print conversion for all tags. By default, extracted values are converted to a more human-readable format, but the <code>-n</code> option disables this conversion, revealing the machine-readable values. For example: </p>
<pre>
    &gt; exiftool -Orientation -S a.jpg
    Orientation: Rotate 90 CW
    &gt; exiftool -Orientation -S -n a.jpg
    Orientation: 6
</pre>
<p> The print conversion may also be disabled on a per-tag basis by suffixing the tag name with a <tt>&quot;#&quot;</tt> character: </p>
<pre>
    &gt; exiftool -Orientation# -Orientation -S a.jpg
    Orientation: 6
    Orientation: Rotate 90 CW
</pre>
<p> These techniques may also be used to disable the inverse print conversion when writing. For example, the following commands all have the same effect: </p>
<pre>
    &gt; exiftool -Orientation='Rotate 90 CW' a.jpg
    &gt; exiftool -Orientation=6 -n a.jpg
    &gt; exiftool -Orientation#=6 a.jpg
</pre>
<dt><code>-p</code> <i></i><font SIZE="-1"><i>FMTFILE</i></font><i></i> or <i></i><font SIZE="-1"><i>STR</i></font><i></i> (<code>-printFormat</code>)</p>
<dd> Print output in the format specified by the given file or string (and ignore other format options). Tag names in the format file or string begin with a <tt>&quot;$&quot;</tt> symbol and may contain a leading group names and/or a trailing <tt>&quot;#&quot;</tt>. Case is not significant. Braces <tt>&quot;{}&quot;</tt> may be used around the tag name to separate it from subsequent text. Use <tt>$$</tt> to represent a <tt>&quot;$&quot;</tt> symbol, and <tt>$/</tt> for a newline. Multiple <code>-p</code> options may be used, each contributing a line of text to the output. Lines beginning with <tt>&quot;#[HEAD]&quot;</tt> and <tt>&quot;#[TAIL]&quot;</tt> are output only for the first and last processed files respectively. Lines beginning with <tt>&quot;#[BODY]&quot;</tt> and lines not beginning with <tt>&quot;#&quot;</tt> are output for each processed file. Other lines beginning with <tt>&quot;#&quot;</tt> are ignored. For example, this format file: </p>
<p>#this is a comment line<br />
#[HEAD] &#8212; Generated by ExifTool $exifToolVersion &#8212;<br />
File : $FileName &#8211; $DateTimeOriginal(f / $Aperture, ${ShutterSpeed} s, ISO $EXIF<br />
                                     : ISO)<br />
#[TAIL] &#8212; end &#8212;</p>
<p> with this command: </p>
<pre>
    exiftool -p test.fmt a.jpg b.jpg
</pre>
<p> produces output like this: </p>
<p>&#8211;Generated by ExifTool 10.40 &#8211;File : a.jpg &#8211; 2003 : 10 : 31 15 : 44 : 19(f / 5.6, 1 / 60s, ISO 100) File : b.jpg &#8211; 2006 : 05 : 23 11 : 57 : 38(f / 8.0, 1 / 13s, ISO 100)&#8211; end&#8211;</p>
<p> When <code>-ee</code> (<code>-extractEmbedded</code>) is combined with <code>-p</code>, embedded documents are effectively processed as separate input files. </p>
<p> If a specified tag does not exist, a minor warning is issued and the line with the missing tag is not printed. However, the <code>-f</code> option may be used to set the value of missing tags to &#8216;-&#8216; (but this may be configured via the MissingTagValue <font SIZE="-1">API</font> option), or the <code>-m</code> option may be used to ignore minor warnings and leave the missing values empty. </p>
<p> An advanced formatting feature allows an arbitrary Perl expression to be applied to the value of any tag by placing it inside the braces after the tag name, separated by a semicolon. The expression acts on the value of the tag through the default input variable (<tt>$_</tt>), and has access to the full ExifTool <font SIZE="-1">API</font> through the current ExifTool object (<tt>$self</tt>). It may contain any valid Perl code, including translation (<tt>&quot;tr///&quot;</tt>) and substitution (<tt>&quot;s///&quot;</tt>) operations, but note that braces within the expression must be balanced. The example below prints the camera Make with spaces translated to underlines, and multiple consecutive underlines replaced by a single underline: </p>
<p>exiftool &#8211; p &#8216;${make;tr/ /_/;s/__+/_/g}&#8217; image.jpg</p>
<p> A default expression of <tt>&quot;tr(/\?*:|&quot;&lt;&gt;
