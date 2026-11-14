---
title: "mkvmerge(1)"
name: "mkvmerge"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkvmerge/"
description: "mkvmerge – Merge multimedia streams into a Matroska(TM) file"
---

<h2 class="name">NAME</h2>
<p> mkvmerge &#8211; Merge multimedia streams into a Matroska(TM) file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mkvmerge</code> [global options] {-o out} [options1] {file1} [[options2]&nbsp;<wbr>{file2}] [@optionsfile]</dl>
<h2>DESCRIPTION</h2>
<dd>This program takes the input from several media files and joins their streams (all of them or just a selection) into a Matroska(TM) file; see m[blue]<code>the Matroska(TM) website</code>m[]<font SIZE="-2">[1]</font>. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font> </p>
<p> The order of command line options is important. Please read the section &quot;Option order&quot; if you&#8217;re new to the program. </p>
</dl>
<h3>Global options</h3>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Increase verbosity.</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Suppress status output.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>file-name</i></p>
<dl>
<dt>
<dd> Write to the file <i>file-name</i>. If splitting is used then this parameter is treated a bit differently. See the explanation for the <code>&#8211;split</code> option for details.</dl>
<p> <code>-w</code>, <code>&#8211;webm</code></p>
<dl>
<dt>
<dd> Create a WebM compliant file. This is also turned on if the output file name&#8217;s extension is &quot;webm&quot;. This mode enforces several restrictions. The only allowed codecs are VP8, VP9 video and Opus, Vorbis audio tracks. Neither chapters nor tags are allowed. The DocType header item is changed to &quot;webm&quot;.</dl>
<p> <code>&#8211;title</code> <i>title</i></p>
<dl>
<dt>
<dd> Sets the general title for the output file, e.g. the movie name.</dl>
<p> <code>&#8211;default-language</code> <i>language-code</i></p>
<dl>
<dt>
<dd> Sets the default language code that will be used for all tracks unless overwritten with the <code>&#8211;language</code> option. The default language code is &#8216;und&#8217; for &#8216;undefined&#8217;.</dl>
<h3>Segment info handling (global options)</h3>
<p> <code>&#8211;segmentinfo</code> <i>filename.xml</i></p>
<dl>
<dt>
<dd> Read segment information from a XML file. This file can contain the segment family UID, segment UID, previous and next segment UID elements. An example file and a DTD are included in the MKVToolNix distribution. </p>
<p> See the section about segment info XML files below for details.</dl>
<p> <code>&#8211;segment-uid</code> <i>SID1,SID2,&#8230;</i></p>
<dl>
<dt>
<dd> Sets the segment UIDs to use. This is a comma-separated list of 128bit segment UIDs in the usual UID form: hex numbers with or without the &quot;0x&quot; prefix, with or without spaces, exactly 32 digits. </p>
<p> Each file created contains one segment, and each segment has one segment UID. If more segment UIDs are specified than segments are created then the surplus UIDs are ignored. If fewer UIDs are specified than segments are created then random UIDs will be created for them.</dl>
<h3>Chapter and tag handling (global options)</h3>
<p> <code>&#8211;chapter-language</code> <i>language-code</i></p>
<dl>
<dt>
<dd> Sets the ISO639-2 language code that is written for each chapter entry. Defaults to &#8216;eng&#8217;. See the section about chapters below for details. </p>
<p> This option can be used both for simple chapter files and for source files that contain chapters but no information about the chapters&#8217; language, e.g. MP4 and OGM files.</dl>
<p> <code>&#8211;chapter-charset</code> <i>character-set</i></p>
<dl>
<dt>
<dd> Sets the character set that is used for the conversion to UTF-8 for simple chapter files. See the section about text files and character sets for an explanation how <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) converts between character sets. </p>
<p> This switch does also apply to chapters that are copied from certain container types, e.g. Ogg/OGM and MP4 files. See the section about chapters below for details.</dl>
<p> <code>&#8211;cue-chapter-name-format</code> <i>format</i></p>
<dl>
<dt>
<dd> <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) supports reading CUE sheets for audio files as the input for chapters. CUE sheets usually contain the entries <i>PERFORMER</i> and <i>TITLE</i> for each index entry. <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) uses these two strings in order to construct the chapter name. With this option the format used for this name can be set. </p>
<p> If this option is not given then <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) defaults to the format &#8216;%p &#8211; %t&#8217; (the performer, followed by a space, a dash, another space and the title). </p>
<p> If the format is given then everything except the following meta characters is copied as-is, and the meta characters are replaced like this: </p>
<dl>
<dt>
<dd> &bull; <i>%p</i> is replaced by the current entry&#8217;s <i>PERFORMER</i> string,</dl>
<dl>
<dt>
<dd> &bull; <i>%t</i> is replaced by the current entry&#8217;s <i>TITLE</i> string,</dl>
<dl>
<dt>
<dd> &bull; <i>%n</i> is replaced by the current track number and</dl>
<dl>
<dt>
<dd> &bull; <i>%N</i> is replaced by the current track number padded with a leading zero if it is &lt; 10.</dl>
</dl>
<p> <code>&#8211;chapters</code> <i>file-name</i></p>
<dl>
<dt>
<dd> Read chapter information from the file <i>file-name</i>. See the section about chapters below for details.</dl>
<p> <code>&#8211;global-tags</code> <i>file-name</i></p>
<dl>
<dt>
<dd> Read global tags from the file <i>file-name</i>. See the section about tags below for details.</dl>
<h3>General output control (advanced global options)</h3>
<p> <code>&#8211;track-order</code> <i>FID1:TID1,FID2:TID2,&#8230;</i></p>
<dl>
<dt>
<dd> This option changes the order in which the tracks for an input file are created. The argument is a comma separated list of pairs IDs. Each pair contains first the file ID (<i>FID1</i>) which is simply the number of the file on the command line starting at 0. The second is a track ID (<i>TID1</i>) from that file. If some track IDs are omitted then those tracks are created after the ones given with this option have been created.</dl>
<p> <code>&#8211;cluster-length</code> <i>spec</i></p>
<dl>
<dt>
<dd> Limit the number of data blocks or the duration of data in each cluster. The <i>spec</i> parameter can either be a number <i>n</i> without a unit or a number <i>d</i> postfixed with &#8216;ms&#8217;. </p>
<p> If no unit is used then <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will put at most <i>n</i> data blocks into each cluster. The maximum number of blocks is 65535. </p>
<p> If the number <i>d</i> is postfixed with &#8216;ms&#8217; then <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) puts at most <i>d</i> milliseconds of data into each cluster. The minimum for <i>d</i> is &#8216;100ms&#8217;, and the maximum is &#8216;32000ms&#8217;. </p>
<p> <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) defaults to putting at most 65535 data blocks and 5000ms of data into a cluster. </p>
<p> Programs trying to find a certain frame can only seek directly to a cluster and have to read the whole cluster afterwards. Therefore creating larger clusters may lead to imprecise or slow seeking.</dl>
<p> <code>&#8211;no-cues</code></p>
<dl>
<dt>
<dd> Tells <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) not to create and write the cue data which can be compared to an index in an AVI. Matroska(TM) files can be played back without the cue data, but seeking will probably be imprecise and slower. Use this only if you&#8217;re really desperate for space or for testing purposes. See also option <code>&#8211;cues</code> which can be specified for each input file.</dl>
<p> <code>&#8211;clusters-in-meta-seek</code></p>
<dl>
<dt>
<dd> Tells <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) to create a meta seek element at the end of the file containing all clusters. See also the section about the Matroska(TM) file layout.</dl>
<p> <code>&#8211;disable-lacing</code></p>
<dl>
<dt>
<dd> Disables lacing for all tracks. This will increase the file&#8217;s size, especially if there are many audio tracks. This option is not intended for everyday use.</dl>
<p> <code>&#8211;enable-durations</code></p>
<dl>
<dt>
<dd> Write durations for all blocks. This will increase file size and does not offer any additional value for players at the moment.</dl>
<p> <code>&#8211;disable-track-statistics-tags</code></p>
<dl>
<dt>
<dd> Normally <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will write certain tags with statistics for each track. If such tags are already present then they will be overwritten. The tags are <code>BPS</code>, <code>DURATION</code>, <code>NUMBER_OF_BYTES</code> and <code>NUMBER_OF_FRAMES</code>. </p>
<p> Enabling this option prevents <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) from writing those tags and from touching any existing tags with same names.</dl>
<p> <code>&#8211;timecode-scale</code> <i>factor</i></p>
<dl>
<dt>
<dd> Forces the timecode scale factor to <i>factor</i>. Valid values are in the range <code>1000</code>..<code>10000000</code> or the special value <code>-1</code>. </p>
<p> Normally <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will use a value of <code>1000000</code> which means that timecodes and durations will have a precision of 1ms. For files that will not contain a video track but at least one audio track <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will automatically chose a timecode scale factor so that all timecodes and durations have a precision of one audio sample. This causes bigger overhead but allows precise seeking and extraction. </p>
<p> If the special value <code>-1</code> is used then <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will use sample precision even if a video track is present.</dl>
<h3>File splitting, linking, appending and concatenation (more global options)</h3>
<p> <code>&#8211;split</code> <i>specification</i></p>
<dl>
<dt>
<dd> Splits the output file after a given size or a given time. Please note that tracks can only be split right before a key frame. Due to buffering <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will split right before the next key frame after the split point has been reached. Therefore the split point may be a bit off from what the user has specified. </p>
<p> At the moment <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) supports four different modes. </p>
<dl>
<dt>
<dd> 1. Splitting by size. </p>
<p> Syntax: <code>&#8211;split</code>[size:]<i>d</i>[k|m|g] </p>
<p> Examples: &#8211;split size:700m or &#8211;split 150000000 </p>
<p> The parameter <i>d</i> may end with &#8216;k&#8217;, &#8216;m&#8217; or &#8216;g&#8217; to indicate that the size is in KB, MB or GB respectively. Otherwise a size in bytes is assumed. After the current output file has reached this size limit a new one will be started. </p>
<p> The &#8216;size:&#8217; prefix may be omitted for compatibility reasons.</dl>
<dl>
<dt>
<dd> 2. Splitting after a duration. </p>
<p> Syntax: <code>&#8211;split</code>[duration:]<i>HH:MM:SS.nnnnnnnnn</i>|<i>d</i>s </p>
<p> Examples: &#8211;split duration:00:60:00.000 or &#8211;split 3600s </p>
<p> The parameter must either have the form <i>HH:MM:SS.nnnnnnnnn</i> for specifying the duration in up to nano-second precision or be a number <i>d</i> followed by the letter &#8216;s&#8217; for the duration in seconds. <i>HH</i> is the number of hours, <i>MM</i> the number of minutes, <i>SS</i> the number of seconds and <i>nnnnnnnnn</i> the number of nanoseconds. Both the number of hours and the number of nanoseconds can be omitted. There can be up to nine digits after the decimal point. After the duration of the contents in the current output has reached this limit a new output file will be started. </p>
<p> The &#8216;duration:&#8217; prefix may be omitted for compatibility reasons.</dl>
<dl>
<dt>
<dd> 3. Splitting after specific timecodes. </p>
<p> Syntax: <code>&#8211;split</code>timecodes:<i>A</i>[,<i>B</i>[,<i>C</i>&#8230;]] </p>
<p> Example: &#8211;split timecodes:00:45:00.000,01:20:00.250,6300s </p>
<p> The parameters <i>A</i>, <i>B</i>, <i>C</i> etc must all have the same format as the ones used for the duration (see above). The list of timecodes is separated by commas. After the input stream has reached the current split point&#8217;s timecode a new file is created. Then the next split point given in this list is used. </p>
<p> The &#8216;timecodes:&#8217; prefix must not be omitted.</dl>
<dl>
<dt>
<dd> 4. Keeping specific parts by specifying timecode ranges while discarding others. </p>
<p> Syntax: <code>&#8211;split</code>parts:<i>start1</i>&#8211;<i>end1</i>[,[+]<i>start2</i>&#8211;<i>end2</i>[,[+]<i>start3</i>&#8211;<i>end3</i>&#8230;]] </p>
<p> Examples: </p>
<dl>
<dt>
<dd> 1. &#8211;split parts:00:01:20-00:02:45,00:05:50-00:10:30</dl>
<dl>
<dt>
<dd> 2. &#8211;split parts:00:01:20-00:02:45,+00:05:50-00:10:30</dl>
<dl>
<dt>
<dd> 3. &#8211;split parts:-00:02:45,00:05:50-</dl>
<p> The parts mode tells <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) to keep certain ranges of timecodes while discarding others. The ranges to keep have to be listed after the parts: keyword and be separated by commas. A range itself consists of a start and an end timecode in the same format the other variations of <i>&#8211;split</i> accept (e.g. both 00:01:20 and 80s refer to the same timecode). </p>
<p> If a start timecode is left out then it defaults to the previous range&#8217;s end timecode. If there was no previous range then it defaults to the start of the file (see example 3). </p>
<p> If an end timecode is left out then it defaults to the end of the source files which basically tells <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) to keep the rest (see example 3). </p>
<p> Normally each range will be written to a new file. This can be changed so that consecutive ranges are written to the same file. For that the user has to prefix the start timecode with a +. This tells <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) not to create a new file and instead append the range to the same file the previous range was written to. Timecodes will be adjusted so that there will be no gap in the output file even if there was a gap in the two ranges in the input file. </p>
<p> In example 1 <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will create two files. The first will contain the content starting from 00:01:20 until 00:02:45. The second file will contain the content starting from 00:05:50 until 00:10:30. </p>
<p> In example 2 <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will create only one file. This file will contain both the content starting from 00:01:20 until 00:02:45 and the content starting from 00:05:50 until 00:10:30. </p>
<p> In example 3 <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will create two files. The first will contain the content from the start of the source files until 00:02:45. The second file will contain the content starting from 00:05:50 until the end of the source files. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 Note that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) only makes decisions about splitting at key frame positions. This applies to both the start and the end of each range. So even if an end timecode is between two key frames <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will continue outputting the frames up to but excluding the following key frame. </p>
</dl>
</dl>
<dl>
<dt>
<dd> 5. Keeping specific parts by specifying frame/field number ranges while discarding others. </p>
<p> Syntax: <code>&#8211;split</code>parts-frames:<i>start1</i>&#8211;<i>end1</i>[,[+]<i>start2</i>&#8211;<i>end2</i>[,[+]<i>start3</i>&#8211;<i>end3</i>&#8230;]] </p>
<p> Examples: </p>
<dl>
<dt>
<dd> 1. &#8211;split parts-frames:137-258,548-1211</dl>
<dl>
<dt>
<dd> 2. &#8211;split parts-frames:733-912,+1592-2730</dl>
<dl>
<dt>
<dd> 3. &#8211;split parts-frames:-430,2512-</dl>
<p> The parts-frames mode tells <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) to keep certain ranges of frame/field numbers while discarding others. The ranges to keep have to be listed after the parts-frames: keyword and be separated by commas. A range itself consists of a start and an end frame/field number. Numbering starts at 1. </p>
<p> If a start number is left out then it defaults to the previous range&#8217;s end number. If there was no previous range then it defaults to the start of the file (see example 3). </p>
<p> If an end number is left out then it defaults to the end of the source files which basically tells <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) to keep the rest (see example 3). </p>
<p> Normally each range will be written to a new file. This can be changed so that consecutive ranges are written to the same file. For that the user has to prefix the start number with a +. This tells <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) not to create a new file and instead append the range to the same file the previous range was written to. Timecodes will be adjusted so that there will be no gap in the output file even if there was a gap in the two ranges in the input file. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 Note that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) only makes decisions about splitting at key frame positions. This applies to both the start and the end of each range. So even if an end frame/field number is between two key frames <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will continue outputting the frames up to but excluding the following key frame. </p>
</dl>
<p> In example 1 <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will create two files. The first will contain the content starting from the first key frame at or after 137 up to but excluding the first key frame at or after 258. The second file will contain the content starting from 548 until 1211. </p>
<p> In example 2 <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will create only one file. This file will contain both the content starting from 733 until 912 and the content starting from 1592 until 2730. </p>
<p> In example 3 <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will create two files. The first will contain the content from the start of the source files until 430. The second file will contain the content starting from 2512 until the end of the source files. </p>
<p> This mode considers only the first video track that is output. If no video track is output no splitting will occur. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 The numbers given with this argument are interpreted based on the number of Matroska(TM) blocks that are output. A single Matroska(TM) block contains either a full frame (for progressive content) or a single field (for interlaced content). mkvmerge does not distinguish between those two and simply counts the number of blocks. For example: If one wanted to split after the 25th full frame with interlaced content one would have to use 50 (two fields per full frame) as the split point. </p>
</dl>
</dl>
<dl>
<dt>
<dd> 6. Splitting after specific frames/fields. </p>
<p> Syntax: <code>&#8211;split</code>frames:<i>A</i>[,<i>B</i>[,<i>C</i>&#8230;]] </p>
<p> Example: &#8211;split frames:120,237,891 </p>
<p> The parameters <i>A</i>, <i>B</i>, <i>C</i> etc must all be positive integers. Numbering starts at 1. The list of frame/field numbers is separated by commas. After the input stream has reached the current split point&#8217;s frame/field number a new file is created. Then the next split point given in this list is used. </p>
<p> The &#8216;frames:&#8217; prefix must not be omitted. </p>
<p> This mode considers only the first video track that is output. If no video track is output no splitting will occur. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 The numbers given with this argument are interpreted based on the number of Matroska(TM) blocks that are output. A single Matroska(TM) block contains either a full frame (for progressive content) or a single field (for interlaced content). mkvmerge does not distinguish between those two and simply counts the number of blocks. For example: If one wanted to split after the 25th full frame with interlaced content one would have to use 50 (two fields per full frame) as the split point. </p>
</dl>
</dl>
<dl>
<dt>
<dd> 7. Splitting before specific chapters. </p>
<p> Syntax: <code>&#8211;split</code>chapters:all or <code>&#8211;split</code>chapters:<i>A</i>[,<i>B</i>[,<i>C</i>&#8230;]] </p>
<p> Example: &#8211;split chapters:5,8 </p>
<p> The parameters <i>A</i>, <i>B</i>, <i>C</i> etc must all be positive integers. Numbering starts at 1. The list of chapter numbers is separated by commas. Splitting will occur right before the first key frame whose timecode is equal to or bigger than the start timecode for the chapters whose numbers are listed. A chapter starting at 0s is never considered for splitting and discarded silently. </p>
<p> The keyword all can be used instead of listing all chapter numbers manually. </p>
<p> The &#8216;chapters:&#8217; prefix must not be omitted. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 The Matroska(TM) file format supports arbitrary deeply nested chapter structures called &#8216;edition entries&#8217; and &#8216;chapter atoms&#8217;. However, this mode only considers the top-most level of chapters across all edition entries. </p>
</dl>
</dl>
<p> For this splitting mode the output filename is treated differently than for the normal operation. It may contain a <code>printf</code> like expression &#8216;%d&#8217; including an optional field width, e.g. &#8216;%02d&#8217;. If it does then the current file number will be formatted appropriately and inserted at that point in the filename. If there is no such pattern then a pattern of &#8216;-%03d&#8217; is assumed right before the file&#8217;s extension: &#8216;-o output.mkv&#8217; would result in &#8216;output-001.mkv&#8217; and so on. If there&#8217;s no extension then &#8216;-%03d&#8217; will be appended to the name.</dl>
<p> <code>&#8211;link</code></p>
<dl>
<dt>
<dd> Link files to one another when splitting the output file. See the section on file linking below for details.</dl>
<p> <code>&#8211;link-to-previous</code> <i>segment-UID</i></p>
<dl>
<dt>
<dd> Links the first output file to the segment with the segment UID given by the <i>segment-UID</i> parameter. See the section on file linking below for details.</dl>
<p> <code>&#8211;link-to-next</code> <i>segment-UID</i></p>
<dl>
<dt>
<dd> Links the last output file to the segment with the segment UID given by the <i>segment-UID</i> parameter. See the section on file linking below for details.</dl>
<p> <code>&#8211;append-mode</code> <i>mode</i></p>
<dl>
<dt>
<dd> Determines how timecodes are calculated when appending files. The parameter <i>mode</i> can have two values: &#8216;file&#8217; which is also the default and &#8216;track&#8217;. </p>
<p> When mkvmerge appends a track (called &#8216;track2_1&#8217; from now on) from a second file (called &#8216;file2&#8217;) to a track (called &#8216;track1_1&#8217;) from the first file (called &#8216;file1&#8217;) then it has to offset all timecodes for &#8216;track2_1&#8217; by an amount. For &#8216;file&#8217; mode this amount is the highest timecode encountered in &#8216;file1&#8217; even if that timecode was from a different track than &#8216;track1_1&#8217;. In track mode the offset is the highest timecode of &#8216;track1_1&#8217;. </p>
<p> Unfortunately mkvmerge cannot detect which mode to use reliably. Therefore it defaults to &#8216;file&#8217; mode. &#8216;file&#8217; mode usually works better for files that have been created independently of each other; e.g. when appending AVI or MP4 files. &#8216;track&#8217; mode may work better for sources that are essentially just parts of one big file, e.g. for VOB and EVO files. </p>
<p> Subtitle tracks are always treated as if &#8216;file&#8217; mode were active even if &#8216;track&#8217; mode actually is.</dl>
<p> <code>&#8211;append-to</code> <i>SFID1:STID1:DFID1:DTID1</i><i>[,&#8230;]</i></p>
<dl>
<dt>
<dd> This option controls to which track another track is appended. Each spec contains four IDs: a file ID, a track ID, a second file ID and a second track ID. The first pair, &quot;source file ID&quot; and &quot;source track ID&quot;, identifies the track that is to be appended. The second pair, &quot;destination file ID&quot; and &quot;destination track ID&quot;, identifies the track the first one is appended to. </p>
<p> If this option has been omitted then a standard mapping is used. This standard mapping appends each track from the current file to a track from the previous file with the same track ID. This allows for easy appending if a movie has been split into two parts and both file have the same number of tracks and track IDs with the command <code>mkvmerge -o output.mkv part1.mkv +part2.mkv</code>.</dl>
<p> <code>+</code></p>
<dl>
<dt>
<dd> A single &#8216;+&#8217; causes the next file to be appended instead of added. The &#8216;+&#8217; can also be put in front of the next file name. Therefore the following two commands are equivalent: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o full.mkv file1.mkv + file2.mkv
$ mkvmerge -o full.mkv file1.mkv +file2.mkv
</pre>
</dl>
</dl>
<p> <code>=</code></p>
<dl>
<dt>
<dd> Normally <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) looks for files in the same directory as an input file that have the same base name and only differ in their running number (e.g. &#8216;VTS_01_1.VOB&#8217;, &#8216;VTS_01_2.VOB&#8217;, &#8216;VTS_01_3.VOB&#8217; etc) and treats all of those files as if they were concatenated into a single big file. This option, a single &#8216;=&#8217;, causes mkvmerge not to look for those additional files. </p>
<p> The &#8216;=&#8217; can also be put in front of the next file name. Therefore the following two commands are equivalent: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o full.mkv = file1.mkv
$ mkvmerge -o full.mkv =file1.mkv
</pre>
</dl>
</dl>
<p> <code>(</code> <i>file1</i> <i>file2</i> <code>)</code></p>
<dl>
<dt>
<dd> If multiple file names are contained in a pair of parenthesis then those files will be treated as if they were concatenated into a single big file consisting of the content of each of the files one after the other. </p>
<p> This can be used for e.g. VOB files coming from a DVD or MPEG transport streams. It cannot be used if each file contains its own set of headers which is usually the case with stand-alone files like AVI or MP4. </p>
<p> Putting a file name into parenthesis also prevents <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) from looking for additional files with the same base name as described in option <code>=</code>. Therefore these two command lines are equivalent: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o out.mkv = file.mkv
$ mkvmerge -o out.mkv '(' file.mkv ')'
</pre>
</dl>
<p> Several things should be noted: </p>
<dl>
<dt>
<dd> 1. There must be spaces both after the opening and before the closing parenthesis.</dl>
<dl>
<dt>
<dd> 2. Every parameter between parenthesis is interpreted as a file name. Therefore all options applying to this logical file must be listed before the opening parenthesis.</dl>
<dl>
<dt>
<dd> 3. Some shells treat parenthesis as special characters. Hence you must escape or quote them as shown in the example above.</dl>
</dl>
<h3>Attachment support (more global options)</h3>
<p> <code>&#8211;attachment-description</code> <i>description</i></p>
<dl>
<dt>
<dd> Plain text description of the following attachment. Applies to the next <code>&#8211;attach-file</code> or <code>&#8211;attach-file-once</code> option.</dl>
<p> <code>&#8211;attachment-mime-type</code> <i>MIME type</i></p>
<dl>
<dt>
<dd> MIME type of the following attachment. Applies to the next <code>&#8211;attach-file</code> or <code>&#8211;attach-file-once</code> option. A list of officially recognized MIME types can be found e.g. at m[blue]<code>the IANA homepage</code>m[]<font SIZE="-2">[2]</font>. The MIME type is mandatory for an attachment.</dl>
<p> <code>&#8211;attachment-name</code> <i>name</i></p>
<dl>
<dt>
<dd> Sets the name that will be stored in the output file for this attachment. If this option is not given then the name will be derived from the file name of the attachment as given with the <code>&#8211;attach-file</code> or the <code>&#8211;attach-file-once</code> option.</dl>
<p> <code>&#8211;attach-file</code> <i>file-name</i>, <code>&#8211;attach-file-once</code> <i>file-name</i></p>
<dl>
<dt>
<dd> Creates a file attachment inside the Matroska(TM) file. The MIME type must have been set before this option can used. The difference between the two forms is that during splitting the files attached with <code>&#8211;attach-file</code> are attached to all output files while the ones attached with <code>&#8211;attach-file-once</code> are only attached to the first file created. If splitting is not used then both do the same. </p>
<p> <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) can be used to extract attached files from a Matroska(TM) file.</dl>
<h3>Options that can be used for each input file</h3>
<p> <code>-a</code>, <code>&#8211;audio-tracks</code> <i>[!]</i><i>n,m,&#8230;</i></p>
<dl>
<dt>
<dd> Copy the audio tracks <i>n</i>, <i>m</i> etc. The numbers are track IDs which can be obtained with the <code>&#8211;identify</code> switch. They&#8217;re not simply the track numbers (see section track IDs). Default: copy all audio tracks. </p>
<p> If the IDs are prefixed with ! then the meaning is reversed: copy everything but the IDs listed after the !.</dl>
<p> <code>-d</code>, <code>&#8211;video-tracks</code> <i>[!]</i><i>n,m,&#8230;</i></p>
<dl>
<dt>
<dd> Copy the video tracks <i>n</i>, <i>m</i> etc. The numbers are track IDs which can be obtained with the <code>&#8211;identify</code> switch. They&#8217;re not simply the track numbers (see section track IDs). Default: copy all video tracks. </p>
<p> If the IDs are prefixed with ! then the meaning is reversed: copy everything but the IDs listed after the !.</dl>
<p> <code>-s</code>, <code>&#8211;subtitle-tracks</code> <i>[!]</i><i>n,m,&#8230;</i></p>
<dl>
<dt>
<dd> Copy the subtitle tracks <i>n</i>, <i>m</i> etc. The numbers are track IDs which can be obtained with the <code>&#8211;identify</code> switch. They&#8217;re not simply the track numbers (see section track IDs). Default: copy all subtitle tracks. </p>
<p> If the IDs are prefixed with ! then the meaning is reversed: copy everything but the IDs listed after the !.</dl>
<p> <code>-b</code>, <code>&#8211;button-tracks</code> <i>[!]</i><i>n,m,&#8230;</i></p>
<dl>
<dt>
<dd> Copy the button tracks <i>n</i>, <i>m</i> etc. The numbers are track IDs which can be obtained with the <code>&#8211;identify</code> switch. They&#8217;re not simply the track numbers (see section track IDs). Default: copy all button tracks. </p>
<p> If the IDs are prefixed with ! then the meaning is reversed: copy everything but the IDs listed after the !.</dl>
<p> <code>&#8211;track-tags</code> <i>[!]</i><i>n,m,&#8230;</i></p>
<dl>
<dt>
<dd> Copy the tags for tracks <i>n</i>, <i>m</i> etc. The numbers are track IDs which can be obtained with the <code>&#8211;identify</code> switch (see section track IDs). They&#8217;re not simply the track numbers. Default: copy tags for all tracks. </p>
<p> If the IDs are prefixed with ! then the meaning is reversed: copy everything but the IDs listed after the !.</dl>
<p> <code>-m</code>, <code>&#8211;attachments</code> <i>[!]</i><i>n</i><i>[:all|first]</i><i>,m</i><i>[:all|first]</i><i>,&#8230;</i></p>
<dl>
<dt>
<dd> Copy the attachments with the IDs <i>n</i>, <i>m</i> etc to all or only the first output file. Each ID can be followed by either &#8216;:all&#8217; (which is the default if neither is entered) or &#8216;:first&#8217;. If splitting is active then those attachments whose IDs are specified with &#8216;:all&#8217; are copied to all of the resulting output files while the others are only copied into the first output file. If splitting is not active then both variants have the same effect. </p>
<p> The default is to copy all attachments to all output files. </p>
<p> If the IDs are prefixed with ! then the meaning is reversed: copy everything but the IDs listed after the !.</dl>
<p> <code>-A</code>, <code>&#8211;no-audio</code></p>
<dl>
<dt>
<dd> Don&#8217;t copy any audio track from this file.</dl>
<p> <code>-D</code>, <code>&#8211;no-video</code></p>
<dl>
<dt>
<dd> Don&#8217;t copy any video track from this file.</dl>
<p> <code>-S</code>, <code>&#8211;no-subtitles</code></p>
<dl>
<dt>
<dd> Don&#8217;t copy any subtitle track from this file.</dl>
<p> <code>-B</code>, <code>&#8211;no-buttons</code></p>
<dl>
<dt>
<dd> Don&#8217;t copy any button track from this file.</dl>
<p> <code>-T</code>, <code>&#8211;no-track-tags</code></p>
<dl>
<dt>
<dd> Don&#8217;t copy any track specific tags from this file.</dl>
<p> <code>&#8211;no-chapters</code></p>
<dl>
<dt>
<dd> Don&#8217;t copy chapters from this file.</dl>
<p> <code>-M</code>, <code>&#8211;no-attachments</code></p>
<dl>
<dt>
<dd> Don&#8217;t copy attachments from this file.</dl>
<p> <code>&#8211;no-global-tags</code></p>
<dl>
<dt>
<dd> Don&#8217;t copy global tags from this file.</dl>
<p> <code>&#8211;chapter-charset</code> <i>character-set</i></p>
<dl>
<dt>
<dd> Sets the charset that is used for the conversion to UTF-8 for chapter information contained in the source file. See the section about text files and character sets for an explanation how <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) converts between character sets.</dl>
<p> <code>&#8211;chapter-language</code> <i>language-code</i></p>
<dl>
<dt>
<dd> Sets the ISO639-2 language code that is written for each chapter entry. This option can be used for source files that contain chapters but no information about the chapters&#8217; languages, e.g. for MP4 and OGM files.</dl>
<p> <code>-y</code>, <code>&#8211;sync</code> <i>TID:d</i><i>[,o[/p]]</i></p>
<dl>
<dt>
<dd> Adjust the timecodes of the track with the id <i>TID</i> by <i>d</i> ms. The track IDs are the same as the ones given with <code>&#8211;identify</code> (see section track IDs). </p>
<p> <i>o</i>/<i>p</i>: adjust the timestamps by <i>o</i>/<i>p</i> to fix linear drifts. <i>p</i> defaults to 1 if omitted. Both <i>o</i> and <i>p</i> can be floating point numbers. </p>
<p> Defaults: no manual sync correction (which is the same as <i>d</i> = <code>0</code> and <i>o</i>/<i>p</i> = <code>1.0</code>). </p>
<p> This option can be used multiple times for an input file applying to several tracks by selecting different track IDs each time.</dl>
<p> <code>&#8211;cues</code> <i>TID:none|iframes|all</i></p>
<dl>
<dt>
<dd> Controls for which tracks cue (index) entries are created for the given track (see section track IDs). &#8216;none&#8217; inhibits the creation of cue entries. For &#8216;iframes&#8217; only blocks with no backward or forward references ( = I frames in video tracks) are put into the cue sheet. &#8216;all&#8217; causes <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) to create cue entries for all blocks which will make the file very big. </p>
<p> The default is &#8216;iframes&#8217; for video tracks and &#8216;none&#8217; for all others. See also option <code>&#8211;no-cues</code> which inhibits the creation of cue entries regardless of the <code>&#8211;cues</code> options used. </p>
<p> This option can be used multiple times for an input file applying to several tracks by selecting different track IDs each time.</dl>
<p> <code>&#8211;default-track</code> <i>TID</i><i>[:bool]</i></p>
<dl>
<dt>
<dd> Sets the &#8216;default&#8217; flag for the given track (see section track IDs) if the optional argument <i>bool</i> is not present. If the user does not explicitly select a track himself then the player should prefer the track that has his &#8216;default&#8217; flag set. Only one track of each kind (audio, video, subtitles, buttons) can have his &#8216;default&#8217; flag set. If the user wants no track to have the default track flag set then he has to set <i>bool</i> to <code>0</code> for all tracks. </p>
<p> This option can be used multiple times for an input file applying to several tracks by selecting different track IDs each time.</dl>
<p> <code>&#8211;forced-track</code> <i>TID</i><i>[:bool]</i></p>
<dl>
<dt>
<dd> Sets the &#8216;forced&#8217; flag for the given track (see section track IDs) if the optional argument <i>bool</i> is not present. A player must play all tracks for which this flag is set to <code>1</code>. </p>
<p> This option can be used multiple times for an input file applying to several tracks by selecting different track IDs each time.</dl>
<p> <code>&#8211;blockadd</code> <i>TID:level</i></p>
<dl>
<dt>
<dd> Keep only the BlockAdditions up to the level <i>level</i> for the given track. The default is to keep all levels. This option only affects certain kinds of codecs like WAVPACK4.</dl>
<p> <code>&#8211;track-name</code> <i>TID:name</i></p>
<dl>
<dt>
<dd> Sets the track name for the given track (see section track IDs) to <i>name</i>.</dl>
<p> <code>&#8211;language</code> <i>TID:language</i></p>
<dl>
<dt>
<dd> Sets the language for the given track (see section track IDs). Both ISO639-2 language codes and ISO639-1 country codes are allowed. The country codes will be converted to language codes automatically. All languages including their ISO639-2 codes can be listed with the <code>&#8211;list-languages</code> option. </p>
<p> This option can be used multiple times for an input file applying to several tracks by selecting different track IDs each time.</dl>
<p> <code>-t</code>, <code>&#8211;tags</code> <i>TID:file-name</i></p>
<dl>
<dt>
<dd> Read tags for the track with the number <i>TID</i> from the file <i>file-name</i>. See the section about tags below for details.</dl>
<p> <code>&#8211;aac-is-sbr</code> <i>TID</i><i>[:0|1]</i></p>
<dl>
<dt>
<dd> Tells <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) that the track with the ID <i>TID</i> is SBR AAC (also known as HE-AAC or AAC+). This options is needed if a) the source file is an AAC file (<i>not</i> for a Matroska(TM) file) and b) the AAC file contains SBR AAC data. The reason for this switch is that it is technically impossible to automatically tell normal AAC data from SBR AAC data without decoding a complete AAC frame. As there are several patent issues with AAC decoders <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will never contain this decoding stage. So for SBR AAC files this switch is mandatory. The resulting file might not play back correctly or even not at all if the switch was omitted. </p>
<p> If the source file is a Matroska(TM) file then the CodecID should be enough to detect SBR AAC. However, if the CodecID is wrong then this switch can be used to correct that. </p>
<p> If mkvmerge wrongfully detects that an AAC file is SBR then you can add &#8216;:0&#8217; to the track ID.</dl>
<p> <code>&#8211;timecodes</code> <i>TID:file-name</i></p>
<dl>
<dt>
<dd> Read the timecodes to be used for the specific track ID from <i>file-name</i>. These timecodes forcefully override the timecodes that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) normally calculates. Read the section about external timecode files.</dl>
<p> <code>&#8211;default-duration</code> <i>TID:x</i></p>
<dl>
<dt>
<dd> Forces the default duration of a given track to the specified value. Also modifies the track&#8217;s timecodes to match the default duration. The argument <i>x</i> must be postfixed with &#8216;s&#8217;, &#8216;ms&#8217;, &#8216;us&#8217;, &#8216;ns&#8217;, &#8216;fps&#8217;, &#8216;p&#8217; or &#8216;i&#8217; to specify the default duration in seconds, milliseconds, microseconds, nanoseconds, &#8216;frames per second&#8217;, &#8216;progressive frames per second&#8217; or &#8216;interlaced frames per second&#8217; respectively. The number <i>x</i> itself can be a floating point number or a fraction. </p>
<p> If the default duration is not forced then mkvmerge will try to derive the track&#8217;s default duration from the container and/or the encoded bitstream for certain track types, e.g. AVC/h.264 or MPEG-2. </p>
<p> This option can also be used to change the FPS of video tracks without having to use an external timecode file.</dl>
<p> <code>&#8211;fix-bitstream-timing-information</code> <i>TID</i><i>[:0|1]</i></p>
<dl>
<dt>
<dd> Normally <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) does not change the timing information (frame/field rate) stored in the video bitstream. With this option that information is adjusted to match the container timing information. The container timing information can come from various sources: from the command line (see option <code>&#8211;default-duration</code>), the source container or derived from the bitstream. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font><br />
 This has only been implemented for AVC/h.264 video tracks so far. </p>
</dl>
</dl>
<p> <code>&#8211;nalu-size-length</code> <i>TID:n</i></p>
<dl>
<dt>
<dd> Forces the NALU size length to <i>n</i> bytes. This parameter is only used if the AVC/h.264 elementary stream packetizer is used. If left out it defaults to 4 bytes, but there are files that contain frames or slices that are all smaller than 65536 bytes. For such files you can use this parameter and decrease the size to 2.</dl>
<p> <code>&#8211;compression</code> <i>TID:n</i></p>
<dl>
<dt>
<dd> Selects the compression method to be used for the track. Note that the player also has to support this method. Valid values are &#8216;none&#8217;, &#8216;zlib&#8217;, &#8216;lzo&#8217;/&#8217;lxo1x&#8217;, &#8216;bz2&#8217;/&#8217;bzlib&#8217; and &#8216;mpeg4_p2&#8217;/&#8217;mpeg4p2&#8217;. The values &#8216;lzo&#8217;/&#8217;lxo1x&#8217; and &#8216;bz2&#8217;/&#8217;bzlib&#8217; are only available if <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) has been compiled with support for the liblzo(TM) and bzlib(TM) compression libraries, respectively. </p>
<p> The compression method &#8216;mpeg4_p2&#8217;/&#8217;mpeg4p2&#8217; is a special compression method called &#8216;header removal&#8217; that is only available for MPEG4 part 2 video tracks. </p>
<p> The default for some subtitle tracks is &#8216;zlib&#8217; compression. This compression method is also the one that most if not all playback applications support. Support for other compression methods other than &#8216;none&#8217; is not assured.</dl>
<h3>Options that only apply to video tracks</h3>
<p> <code>-f</code>, <code>&#8211;fourcc</code> <i>TID:FourCC</i></p>
<dl>
<dt>
<dd> Forces the FourCC to the specified value. Works only for video tracks in the &#8216;MS compatibility mode&#8217;.</dl>
<p> <code>&#8211;display-dimensions</code> <i>TID:widthxheight</i></p>
<dl>
<dt>
<dd> Matroska(TM) files contain two values that set the display properties that a player should scale the image on playback to: display width and display height. These values can be set with this option, e.g. &#8216;1:640&#215;480&#8217;. </p>
<p> Another way to specify the values is to use the <code>&#8211;aspect-ratio</code> or the <code>&#8211;aspect-ratio-factor</code> option (see below). These options are mutually exclusive.</dl>
<p> <code>&#8211;aspect-ratio</code> <i>TID:ratio|width/height</i></p>
<dl>
<dt>
<dd> Matroska(TM) files contain two values that set the display properties that a player should scale the image on playback to: display width and display height. With this option <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will automatically calculate the display width and display height based on the image&#8217;s original width and height and the aspect ratio given with this option. The ratio can be given either as a floating point number <i>ratio</i> or as a fraction &#8216;<i>width</i>/<i>height</i>&#8216;, e.g. &#8217;16/9&#8217;. </p>
<p> Another way to specify the values is to use the <code>&#8211;aspect-ratio-factor</code> or <code>&#8211;display-dimensions</code> options (see above and below). These options are mutually exclusive.</dl>
<p> <code>&#8211;aspect-ratio-factor</code> <i>TID:factor|n/d</i></p>
<dl>
<dt>
<dd> Another way to set the aspect ratio is to specify a <i>factor</i>. The original aspect ratio is first multiplied with this <i>factor</i> and used as the target aspect ratio afterwards. </p>
<p> Another way to specify the values is to use the <code>&#8211;aspect-ratio</code> or <code>&#8211;display-dimensions</code> options (see above). These options are mutually exclusive.</dl>
<p> <code>&#8211;cropping</code> <i>TID:left,top,right,bottom</i></p>
<dl>
<dt>
<dd> Sets the pixel cropping parameters of a video track to the given values.</dl>
<p> <code>&#8211;stereo-mode</code> <i>TID:n|keyword</i></p>
<dl>
<dt>
<dd> Sets the stereo mode for the video track with the track ID <i>TID</i>. The mode can either be a number <i>n</i> between <code>0</code> and <code>14</code> or one of these keywords: </p>
<p> &#8216;mono&#8217;, &#8216;side_by_side_left_first&#8217;, &#8216;top_bottom_right_first&#8217;, &#8216;top_bottom_left_first&#8217;, &#8216;checkerboard_right_first&#8217;, &#8216;checkerboard_left_first&#8217;, &#8216;row_interleaved_right_first&#8217;, &#8216;row_interleaved_left_first&#8217;, &#8216;column_interleaved_right_first&#8217;, &#8216;column_interleaved_left_first&#8217;, &#8216;anaglyph_cyan_red&#8217;, &#8216;side_by_side_right_first&#8217;, &#8216;anaglyph_green_magenta&#8217;, &#8216;both_eyes_laced_left_first&#8217;, &#8216;both_eyes_laced_right_first&#8217;.</dl>
<h3>Options that only apply to text subtitle tracks</h3>
<p> <code>&#8211;sub-charset</code> <i>TID:character-set</i></p>
<dl>
<dt>
<dd> Sets the character set for the conversion to UTF-8 for UTF-8 subtitles for the given track ID. If not specified the charset will be derived from the current locale settings. Note that a charset is not needed for subtitles read from Matroska(TM) files or from Kate streams, as these are always stored in UTF-8. See the section about text files and character sets for an explanation how <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) converts between character sets. </p>
<p> This option can be used multiple times for an input file applying to several tracks by selecting different track IDs each time.</dl>
<h3>Other options</h3>
<p> <code>-i</code>, <code>&#8211;identify</code> <i>file-name</i></p>
<dl>
<dt>
<dd> Will let <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) probe the single file and report its type, the tracks contained in the file and their track IDs. If this option is used then the only other option allowed is the filename.</dl>
<p> <code>-I</code>, <code>&#8211;identify-verbose</code> <i>file-name</i></p>
<dl>
<dt>
<dd> Will let <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) probe the single file and report its type, the tracks contained in the file and their track IDs. If this option is used then the only other option allowed is the filename. </p>
<p> This option causes <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) to output additional information about the container and each track within. The extra information is surronded by square brackets. It consists of space-saparated key/value pairs where keys and values are separated by a colon. </p>
<p> Each value is escaped according to the rules described in the section about escaping special characters in text.</dl>
<p> <code>-l</code>, <code>&#8211;list-types</code></p>
<dl>
<dt>
<dd> Lists supported input file types.</dl>
<p> <code>&#8211;list-languages</code></p>
<dl>
<dt>
<dd> Lists all languages and their ISO639-2 code which can be used with the <code>&#8211;language</code> option.</dl>
<p> <code>&#8211;priority</code> <i>priority</i></p>
<dl>
<dt>
<dd> Sets the process priority that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) runs with. Valid values are &#8216;lowest&#8217;, &#8216;lower&#8217;, &#8216;normal&#8217;, &#8216;higher&#8217; and &#8216;highest&#8217;. If nothing is given then &#8216;normal&#8217; is used. On Unix like systems <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) will use the <code><a href="/docs/linux/man/2-nice/">nice</a></code>(2) function. Therefore only the super user can use &#8216;higher&#8217; and &#8216;highest&#8217;. On Windows all values are useable for every user. </p>
<p> Selecting &#8216;lowest&#8217; also causes <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) to select idle I/O priority in addition to the lowest possible process priority.</dl>
<p> <code>&#8211;command-line-charset</code> <i>character-set</i></p>
<dl>
<dt>
<dd> Sets the character set to convert strings given on the command line from. It defaults to the character set given by system&#8217;s current locale. This settings applies to arguments of the following options: <code>&#8211;title</code>, <code>&#8211;track-name</code> and <code>&#8211;attachment-description</code>.</dl>
<p> <code>&#8211;output-charset</code> <i>character-set</i></p>
<dl>
<dt>
<dd> Sets the character set to which strings are converted that are to be output. It defaults to the character set given by system&#8217;s current locale.</dl>
<p> <code>-r</code>, <code>&#8211;redirect-output</code> <i>file-name</i></p>
<dl>
<dt>
<dd> Writes all messages to the file <i>file-name</i> instead of to the console. While this can be done easily with output redirection there are cases in which this option is needed: when the terminal reinterprets the output before writing it to a file. The character set set with <code>&#8211;output-charset</code> is honored.</dl>
<p> <code>&#8211;ui-language</code> <i>code</i></p>
<dl>
<dt>
<dd> Forces the translations for the language <i>code</i> to be used (e.g. &#8216;de_DE&#8217; for the German translations). It is preferable to use the environment variables <i>LANG</i>, <i>LC_MESSAGES</i> and <i>LC_ALL</i> though. Entering &#8216;list&#8217; as the <i>code</i> will cause <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) to output a list of available translations.</dl>
<p> <code>&#8211;debug</code> <i>topic</i></p>
<dl>
<dt>
<dd> Turn on debugging for a specific feature. This option is only useful for developers.</dl>
<p> <code>&#8211;engage</code> <i>feature</i></p>
<dl>
<dt>
<dd> Turn on experimental features. A list of available features can be requested with <code>mkvmerge &#8211;engage list</code>. These features are not meant to be used in normal situations.</dl>
<p> <code>&#8211;gui-mode</code></p>
<dl>
<dt>
<dd> Turns on GUI mode. In this mode specially-formatted lines may be output that can tell a controlling GUI what&#8217;s happening. These messages follow the format &#8216;#GUI#message&#8217;. The message may be followed by key/value pairs as in &#8216;#GUI#message#key1=value1#key2=value2&#8230;&#8217;. Neither the messages nor the keys are ever translated and always output in English.</dl>
<p> <code>@</code><i>options-file</i></p>
<dl>
<dt>
<dd> Reads additional command line arguments from the file <i>options-file</i>. See the section about option files for further information.</dl>
<p> <code>&#8211;capabilities</code></p>
<dl>
<dt>
<dd> Lists information about optional features that have been compiled in and exit. The first line output will be the version information. All following lines contain exactly one word whose presence indicates that the feature has been compiled in. These features are: </p>
<dl>
<dt>
<dd> &bull; &#8216;BZ2&#8217; &#8212; the bzlib(TM) compression library. Affects the available compression methods for the <code>&#8211;compression</code> option.</dl>
<dl>
<dt>
<dd> &bull; &#8216;LZO&#8217; &#8212; the lzo(TM) compression library. Affects the available compression methods for the <code>&#8211;compression</code> option.</dl>
<dl>
<dt>
<dd> &bull; &#8216;FLAC&#8217; &#8212; reading raw FLAC files and handling FLAC tracks in other containers, e.g. Ogg(TM) or Matroska(TM).</dl>
</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show usage information and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show version information and exit.</dl>
<p> <code>&#8211;check-for-updates</code></p>
<dl>
<dt>
<dd> Checks online for new releases by downloading the URL m[blue]<code><a rel="nofollow" href="http://mkvtoolnix-releases.bunkus.org/latest-release.xml">http://mkvtoolnix-releases.bunkus.org/latest-release.xml</a></code>m[]. Four lines will be output in key=value style: the URL from where the information was retrieved (key version_check_url), the currently running version (key running_version), the latest release&#8217;s version (key available_version) and the download URL (key download_url). </p>
<p> Afterwards the program exists with an exit code of 0 if no newer release is available, with 1 if a newer release is available and with 2 if an error occured (e.g. if the update information could not be retrieved). </p>
<p> This option is only available if the program was built with support for libcurl.</dl>
<h2>USAGE</h2>
<p> For each file the user can select which tracks <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) should take. They are all put into the file specified with <code>-o</code>. A list of known (and supported) source formats can be obtained with the <code>-l</code> option. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Important</code> </font> </p>
<p> The order of command line options is important. Please read the section &quot;Option order&quot; if you&#8217;re new to the program. </p>
</dl>
<h2>OPTION ORDER</h2>
<p> The order in which options are entered is important for some options. Options fall into two categories: </p>
<dl>
<dt>
<dd> 1. Options that affect the whole program and are not tied to any input file. These include but are not limited to <code>&#8211;command-line-charset</code>, <code>&#8211;output</code> or <code>&#8211;title</code>. These can appear anywhere on the command line.</dl>
<dl>
<dt>
<dd> 2. Options that affect a single input file or a single track in an input file. These options all apply to the following input file on the command line. All options applying to the same input (or to tracks from the same input file) file can be written in any order as long as they all appear before that input file&#8217;s name. Examples for options applying to an input file are <code>&#8211;no-chapters</code> or <code>&#8211;chapter-charset</code>. Examples for options applying to a single track are <code>&#8211;default-duration</code> or <code>&#8211;language</code>.</dl>
<p> The options are processed from left to right. If an option appears multiple times within the same scope then the last occurence will be used. Therefore the title will be set to &quot;Something else&quot; in the following example: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o output.mkv --title 'This and that' input.avi --title 'Something else'
</pre>
</dl>
<p> The following example shows that using the <code>&#8211;language</code> option twice is OK because they&#8217;re used in different scopes. Even though they apply to the same track ID they apply to different input files and therefore have different scopes: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o output.mkv --language 0:fre français.ogg --language 0:deu deutsch.ogg
</pre>
</dl>
<h2>EXAMPLES</h2>
<p> Let&#8217;s assume you have a file called MyMovie.avi and the audio track in a separate file, e.g. &#8216;MyMovie.wav&#8217;. First you want to encode the audio to OggVorbis(TM): </p>
<dl>
<dt>
<dd>
<pre>
$ oggenc -q4 -oMyMovie.ogg MyMovie.wav
</pre>
</dl>
<p> After a couple of minutes you can join video and audio: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o MyMovie-with-sound.mkv MyMovie.avi MyMovie.ogg
</pre>
</dl>
<p> If your AVI already contains an audio track then it will be copied as well (if <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) supports the audio format). To avoid that simply do </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o MyMovie-with-sound.mkv -A MyMovie.avi MyMovie.ogg
</pre>
</dl>
<p> After some minutes of consideration you rip another audio track, e.g. the director&#8217;s comments or another language to &#8216;MyMovie-add-audio.wav&#8217;. Encode it again and join it up with the other file: </p>
<dl>
<dt>
<dd>
<pre>
$ oggenc -q4 -oMyMovie-add-audio.ogg MyMovie-add-audio.wav
$ mkvmerge -o MM-complete.mkv MyMovie-with-sound.mkv MyMovie-add-audio.ogg
</pre>
</dl>
<p> The same result can be achieved with </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o MM-complete.mkv -A MyMovie.avi MyMovie.ogg MyMovie-add-audio.ogg
</pre>
</dl>
<p> Now fire up mplayer(TM) and enjoy. If you have multiple audio tracks (or even video tracks) then you can tell mplayer(TM) which track to play with the &#8216;<code>-vid</code>&#8216; and &#8216;<code>-aid</code>&#8216; options. These are 0-based and do not distinguish between video and audio. </p>
<p> If you need an audio track synchronized you can do that easily. First find out which track ID the Vorbis track has with </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge --identify outofsync.ogg
</pre>
</dl>
<p> Now you can use that ID in the following command line: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o goodsync.mkv -A source.avi -y 12345:200 outofsync.ogg
</pre>
</dl>
<p> This would add 200ms of silence at the beginning of the audio track with the ID <code>12345</code> taken from &#8216;outofsync.ogg&#8217;. </p>
<p> Some movies start synced correctly but slowly drift out of sync. For these kind of movies you can specify a delay factor that is applied to all timestamps &#8212; no data is added or removed. So if you make that factor too big or too small you&#8217;ll get bad results. An example is that an episode I transcoded was <code>0.2</code> seconds out of sync at the end of the movie which was <code>77340</code> frames long. At <code>29.97fps</code><code>0.2</code> seconds correspond to approx. <code>6</code> frames. So I did </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o goodsync.mkv -y 23456:0,77346/77340 outofsync.mkv
</pre>
</dl>
<p> The result was fine. </p>
<p> The sync options can also be used for subtitles in the same manner. </p>
<p> For text subtitles you can either use some Windows software (like SubRipper(TM)) or the subrip(TM) package found in <code><a href="/docs/linux/man/1-transcode/">transcode</a></code>(1)&#8217;s sources in the &#8216;contrib/subrip&#8217; directory. The general process is: </p>
<dl>
<dt>
<dd> 1. extract a raw subtitle stream from the source: </p>
<dl>
<dt>
<dd>
<pre>
$ tccat -i /path/to/copied/dvd/ -T 1 -L | tcextract -x ps1 -t vob -a 0x20 | subtitle2pgm -o mymovie
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 2. convert the resulting PGM images to text with gocr: </p>
<dl>
<dt>
<dd>
<pre>
$ pgm2txt mymovie
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 3. spell-check the resulting text files: </p>
<dl>
<dt>
<dd>
<pre>
$ ispell -d american *txt
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> 4. convert the text files to a SRT file: </p>
<dl>
<dt>
<dd>
<pre>
$ srttool -s -w -i mymovie.srtx -o mymovie.srt
</pre>
</dl>
</dl>
<p> The resulting file can be used as another input file for <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1): </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o mymovie.mkv mymovie.avi mymovie.srt
</pre>
</dl>
<p> If you want to specify the language for a given track then this is easily done. First find out the ISO639-2 code for your language. <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) can list all of those codes for you: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge --list-languages
</pre>
</dl>
<p> Search the list for the languages you need. Let&#8217;s assume you have put two audio tracks into a Matroska(TM) file and want to set their language codes and that their track IDs are 2 and 3. This can be done with </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o with-lang-codes.mkv --language 2:ger --language 3:dut without-lang-codes.mkv
</pre>
</dl>
<p> As you can see you can use the <code>&#8211;language</code> switch multiple times. </p>
<p> Maybe you&#8217;d also like to have the player use the Dutch language as the default language. You also have extra subtitles, e.g. in English and French, and want to have the player display the French ones by default. This can be done with </p>
<dl>
<dt>
<dd>
<pre><code>
$ mkvmerge - o with - lang - codes.mkv-- language 2 : ger-- language 3 : dut-- default - track 3 without - lang - codes.mkv-- language 0 : eng english.srt-- default - track 0 --language 0 : fre french.srt
</code></pre>
</dl>
<p> If you do not see the language or default track flags that you&#8217;ve specified in <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1)&#8217;s output then please read the section about default values. </p>
<p> Turn off the compression for an input file. </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -o no-compression.mkv --compression -1:none MyMovie.avi --compression -1:none mymovie.srt
</pre>
</dl>
<h2>TRACK IDS</h2>
<p> Some of the options for <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) need a track ID to specify which track they should be applied to. Those track IDs are printed by the readers when demuxing the current input file, or if <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) is called with the <code>&#8211;identify</code> option. An example for such output: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvmerge -i v.mkv
File 'v.mkv': container: Matroska(TM)
Track ID 0: video (V_MS/VFW/FOURCC, DIV3)
Track ID 1: audio (A_MPEG/L3)
</pre>
</dl>
<p> Do not confuse the track IDs that are assigned to the tracks that are placed in the output MKV file with the track IDs of the input files. Only the input file track IDs are used for options needing these values. </p>
<p> Also note that each input file has its own set of track IDs. Therefore the track IDs for file &#8216;file1.ext&#8217; as reported by &#8216;mkvmerge &#8211;identify&#8217; do not change no matter how many other input files are there or in which position &#8216;file1.ext&#8217; is used. </p>
<p> Track IDs are assigned like this: </p>
<dl>
<dt>
<dd> &bull; AVI files: The video track has the ID 0. The audio tracks get IDs in ascending order starting at 1.</dl>
<dl>
<dt>
<dd> &bull; AAC, AC3, MP3, SRT and WAV files: The one &#8216;track&#8217; in that file gets the ID 0.</dl>
<dl>
<dt>
<dd> &bull; Most other files: The track IDs are assigned in order the tracks are found in the file starting at 0.</dl>
<p> The special track ID &#8216;<code>-1</code>&#8216; is a wild card and applies the given switch to all tracks that are read from an input file. </p>
<p> The options that use the track IDs are the ones whose description contains &#8216;TID&#8217;. The following options use track IDs as well: <code>&#8211;audio-tracks</code>, <code>&#8211;video-tracks</code>, <code>&#8211;subtitle-tracks</code>, <code>&#8211;button-tracks</code> and <code>&#8211;track-tags</code>.</p>
<h2>TEXT FILES AND CHARACTER SET CONVERSIONS</h2>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> This section applies to all programs in MKVToolNix even if it only mentions <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1). </p>
</dl>
<h3>Introduction</h3>
<p> All text in a Matroska(TM) file is encoded in UTF-8. This means that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) has to convert every text file it reads as well as every text given on the command line from one character set into UTF-8. In return this also means that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8217;s output has to be converted back to that character set from UTF-8, e.g. if a non-English translation is used with <code>&#8211;ui-language</code> or for text originating from a Matroska(TM) file. </p>
<p> <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) does this conversion automatically based on the presence of a byte order marker (short: BOM) or the system&#8217;s current locale. How the character set is inferred from the locale depends on the operating system that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) is run on.</p>
<h3>Byte order markers (BOM)</h3>
<p> Text files that start with a BOM are already encoded in one representation of UTF. <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) supports the following five modes: UTF-8, UTF-16 Little and Big Endian, UTF-32 Little and Big Endian. Text files with a BOM are automatically converted to UTF-8. Any of the parameters that would otherwise set the character set for such a file (e.g. <code>&#8211;sub-charset</code>) is silently ignored.</p>
<h3>Linux and Unix-like systems including Mac OS</h3>
<p> On Unix-like systems <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) uses the <code><a href="/docs/linux/man/3-setlocale/">setlocale</a></code>(3) system call which in turn uses the environment variables <i>LANG</i>, <i>LC_ALL</i> and <i>LC_CYPE</i>. The resulting character set is often one of UTF-8 or the ISO-8859-* family and is used for all text file operations and for encoding strings on the command line and for output to the console.</p>
<h3>Windows</h3>
<p> On Windows the default character set used for converting text files is determined by a call to the <code>GetACP()</code> system call. </p>
<p> Reading the command line is done with the <code>GetCommandLineW()</code> function which already returns a Unicode string. Therefore the option <code>&#8211;command-line-charset</code> is ignored on Windows. </p>
<p> Output to the console consists of three scenarios: </p>
<dl>
<dt>
<dd> 1. If the output is redirected with the option <code>&#8211;redirect-output</code> then the default charset is UTF-8. This can be changed with <code>&#8211;output-charset</code>. </p>
<p> If the output is redirected with <code>cmd.exe</code> itself, e.g. with mkvinfo file.mkv &gt; info.txt, then the charset is always UTF-8 and cannot be changed. </p>
<p> Otherwise (when writing directly to the console) the Windows function <code>WriteConsoleW()</code> is used and the option <code>&#8211;output-charset</code> is ignored. The console should be able to output all Unicode characters for which the corresponding language support is installed (e.g. Chinese characters might not be displayed on English Windows versions).</dl>
<h3>Command line options</h3>
<p> The following options exist that allow specifying the character sets: </p>
<dl>
<dt>
<dd> &bull; <code>&#8211;sub-charset</code> for text subtitle files and for text subtitle tracks stored in container formats for which the character set cannot be determined unambiguously (e.g. Ogg files),</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;chapter-charset</code> for chapter text files and for chapters and file titles stored in container formats for which the character set cannot be determined unambiguously (e.g. Ogg files for chapter information, track and file titles etc; MP4 files for chapter information),</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;command-line-charset</code> for all strings on the command line,</dl>
<dl>
<dt>
<dd> &bull; <code>&#8211;output-charset</code> for all strings written to the console or to a file if the output has been redirected with the <code>&#8211;redirect-output</code> option. On non-Windows systems the default for the output charset is the system&#8217;s current charset. On Windows it defaults to UTF-8 both for redirecting with <code>&#8211;redirect-output</code> and with <code>cmd.exe</code> itself, e.g. mkvinfo file.mkv &gt; info.txt.</dl>
<h2>OPTION FILES</h2>
<p> An option file is a file <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) can read additional command line arguments from. This can be used in order to circumvent certain limitations of the shell or the operating system when executing external programs like a limited command line length. </p>
<p> There are several rules regarding option files. Lines whose first non-whitespace character is a hash mark (&#8216;#&#8217;) are treated as comments and ignored. White spaces at the start and end of a line will be stripped. Each line must contain exactly one option. </p>
<p> A line not containing anything is also ignored. An empty argument is represented by the line &#8216;#EMPTY#&#8217;. </p>
<p> Several chars can be escaped, e.g. if you need to start a non-comment line with &#8216;#&#8217;. The rules are described in the section about escaping text. </p>
<p> Note that backslashes must always be escaped. Hash marks (&#8216;#&#8217;) must be escaped if they should not start a comment. </p>
<p> The command line &#8216;<code>mkvmerge -o &quot;my file.mkv&quot; -A &quot;a movie.avi&quot; sound.ogg</code>&#8216; could be converted into the following option file: </p>
<dl>
<dt>
<dd>
<pre>
# Write to the file &quot;c:\Matroska\my file.mkv&quot; on Windows.
-o
c:\Matroska\my file.mkv
# Set the title to '#65'.
--title
\h65
# Only take the video from &quot;a movie.avi&quot;.
-A
a movie.avi
sound.ogg
</pre>
</dl>
<h2>ESCAPING SPECIAL CHARS IN TEXT</h2>
<p> There are a few places in which special characters in text must or should be escaped. The rules for escaping are simple: each character that needs escaping is replaced with a backslash followed by another character. </p>
<p> The rules are: &#8216; &#8216; (a space) becomes &#8216;\s&#8217;, &#8216;&quot;&#8217; (double quotes) becomes &#8216;\2&#8217;, &#8216;:&#8217; becomes &#8216;
