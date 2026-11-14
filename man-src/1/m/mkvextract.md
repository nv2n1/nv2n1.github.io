---
title: "mkvextract(1)"
name: "mkvextract"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkvextract/"
description: "mkvextract – extract tracks from Matroska(TM) files into other files"
---

<h2 class="name">NAME</h2>
<p> mkvextract &#8211; extract tracks from Matroska(TM) files into other files </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mkvextract</code> {mode} {source-filename} [options] [extraction-spec]</dl>
<h2>DESCRIPTION</h2>
<dd>This program extracts specific parts from a Matroska(TM) file to other useful formats. The first argument, <code>mode</code>, tells <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) what to extract. Currently supported is the extraction of tracks, tags, attachments, chapters, CUE sheets and timecodes. The second argument is the name of the source file. It must be a Matroska(TM) file. All following arguments are options and extraction specifications; both of which depend on the selected mode.</p>
<h3>Common options</h3>
<p> The following options are available in all modes and only described once in this section. </p>
<p> <code>-f</code>, <code>&#8211;parse-fully</code></p>
<dl>
<dt>
<dd> Sets the parse mode to &#8216;full&#8217;. The default mode does not parse the whole file but uses the meta seek elements for locating the required elements of a source file. In 99% of all cases this is enough. But for files that do not contain meta seek elements or which are damaged the user might have to use this mode. A full scan of a file can take a couple of minutes while a fast scan only takes seconds.</dl>
<p> <code>&#8211;command-line-charset</code> <i>character-set</i></p>
<dl>
<dt>
<dd> Sets the character set to convert strings given on the command line from. It defaults to the character set given by system&#8217;s current locale.</dl>
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
<dd> Forces the translations for the language <i>code</i> to be used (e.g. &#8216;de_DE&#8217; for the German translations). It is preferable to use the environment variables <i>LANG</i>, <i>LC_MESSAGES</i> and <i>LC_ALL</i> though. Entering &#8216;list&#8217; as the <i>code</i> will cause <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) to output a list of available translations.</dl>
<p> <code>&#8211;debug</code> <i>topic</i></p>
<dl>
<dt>
<dd> Turn on debugging for a specific feature. This option is only useful for developers.</dl>
<p> <code>&#8211;engage</code> <i>feature</i></p>
<dl>
<dt>
<dd> Turn on experimental features. A list of available features can be requested with <code>mkvextract &#8211;engage list</code>. These features are not meant to be used in normal situations.</dl>
<p> <code>&#8211;gui-mode</code></p>
<dl>
<dt>
<dd> Turns on GUI mode. In this mode specially-formatted lines may be output that can tell a controlling GUI what&#8217;s happening. These messages follow the format &#8216;#GUI#message&#8217;. The message may be followed by key/value pairs as in &#8216;#GUI#message#key1=value1#key2=value2&#8230;&#8217;. Neither the messages nor the keys are ever translated and always output in English.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Be verbose and show all the important Matroska(TM) elements as they&#8217;re read.</dl>
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
<p> <code>@</code><i>options-file</i></p>
<dl>
<dt>
<dd> Reads additional command line arguments from the file <i>options-file</i>. Lines whose first non-whitespace character is a hash mark (&#8216;#&#8217;) are treated as comments and ignored. White spaces at the start and end of a line will be stripped. Each line must contain exactly one option. </p>
<p> Several chars can be escaped, e.g. if you need to start a non-comment line with &#8216;#&#8217;. The rules are described in the section about escaping text. </p>
<p> The command line &#8216;<code>mkvextract tracks source.mkv &#8211;raw 1:destination.raw</code>&#8216; could be converted into the following option file: </p>
<dl>
<dt>
<dd>
<pre>
# Extract a track from source.mkv
tracks
source.mkv
# Output the track as raw data.
--raw
1:destination.raw
</pre>
</dl>
</dl>
<h3>Track extraction mode</h3>
<p> Syntax: <code>mkvextract </code><code>tracks</code><i>source-filename</i><code>[</code><i>options</i>]<i>TID1:dest-filename1</i><code>[</code><i>TID2:dest-filename2</i> &#8230;] </p>
<p> The following command line options are available for each track in the &#8216;tracks&#8217; extraction mode. They have to appear in front of the track specification (see below) they should be applied to. </p>
<p> <code>-c</code> <i>character-set</i></p>
<dl>
<dt>
<dd> Sets the character set to convert the next text subtitle track to. Only valid if the next track ID targets a text subtitle track. It defaults to UTF-8.</dl>
<p> <code>&#8211;blockadd</code> <i>level</i></p>
<dl>
<dt>
<dd> Keep only the BlockAdditions up to this level. The default is to keep all levels. This option only affects certain kinds of codecs like WAVPACK4.</dl>
<p> <code>&#8211;cuesheet</code></p>
<dl>
<dt>
<dd> Causes <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) to extract a CUE sheet from the chapter information and tag data for the following track into a file whose name is the track&#8217;s output name with &#8216;.cue&#8217; appended to it.</dl>
<p> <code>&#8211;raw</code></p>
<dl>
<dt>
<dd> Extracts the raw data into a file without any container data around it. Unlike the <code>&#8211;fullraw</code> flag this flag does not cause the contents of the CodecPrivate element to be written to the file. This mode works with all CodecIDs, even the ones that <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) doesn&#8217;t support otherwise, but the resulting files might not be usable.</dl>
<p> <code>&#8211;fullraw</code></p>
<dl>
<dt>
<dd> Extracts the raw data into a file without any container data around it. The contents of the CodecPrivate element will be written to the file first if the track contains such a header element. This mode works with all CodecIDs, even the ones that <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) doesn&#8217;t support otherwise, but the resulting files might not be usable.</dl>
<p> <i>TID:outname</i></p>
<dl>
<dt>
<dd> Causes extraction of the track with the ID <i>TID</i> into the file <i>outname</i> if such a track exists in the source file. This option can be given multiple times. The track IDs are the same as the ones output by <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8217;s <code>&#8211;identify</code> option. </p>
<p> Each output name should be used only once. The exception are RealAudio and RealVideo tracks. If you use the same name for different tracks then those tracks will be saved in the same file. Example: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvextract tracks input.mkv 1:output-two-tracks.rm 2:output-two-tracks.rm
</pre>
</dl>
</dl>
<h3>Tags extraction mode</h3>
<p> Syntax: <code>mkvextract </code><code>tags</code><i>source-filename</i><code>[</code><i>options</i>] </p>
<p> The extracted tags are written to the console unless the output is redirected (see the section about output redirection for details).</p>
<h3>Attachments extraction mode</h3>
<p> Syntax: <code>mkvextract </code><code>attachments</code><i>source-filename</i><code>[</code><i>options</i>]<i>AID1:outname1</i><code>[</code><i>AID2:outname2</i> &#8230;] </p>
<p> <i>AID</i>:<i>outname</i></p>
<dl>
<dt>
<dd> Causes extraction of the attachment with the ID <i>AID</i> into the file <i>outname</i> if such an attachment exists in the source file. If the <i>outname</i> is left empty then the name of the attachment inside the source Matroska(TM) file is used instead. This option can be given multiple times. The attachment IDs are the same as the ones output by <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8217;s <code>&#8211;identify</code> option.</dl>
<h3>Chapters extraction mode</h3>
<p> Syntax: <code>mkvextract </code><code>chapters</code><i>source-filename</i><code>[</code><i>options</i>] </p>
<p> <code>-s</code>, <code>&#8211;simple</code></p>
<dl>
<dt>
<dd> Exports the chapter information in the simple format used in the OGM tools (CHAPTER01=&#8230;, CHAPTER01NAME=&#8230;). In this mode some information has to be discarded. Default is to output the chapters in XML format.</dl>
<p> The extracted chapters are written to the console unless the output is redirected (see the section about output redirection for details).</p>
<h3>Cue sheet extraction mode</h3>
<p> Syntax: <code>mkvextract </code><code>cuesheet</code><i>source-filename</i><code>[</code><i>options</i>] </p>
<p> The extracted cue sheet is written to the console unless the output is redirected (see the section about output redirection for details).</p>
<h3>Timecode extraction mode</h3>
<p> Syntax: <code>mkvextract </code><code>timecodes_v2</code><i>source-filename</i><code>[</code><i>options</i>]<i>TID1:dest-filename1</i><code>[</code><i>TID2:dest-filename2</i> &#8230;] </p>
<p> The extracted timecodes are written to the console unless the output is redirected (see the section about output redirection for details). </p>
<p> <i>TID:outname</i></p>
<dl>
<dt>
<dd> Causes extraction of the timecodes for the track with the ID <i>TID</i> into the file <i>outname</i> if such a track exists in the source file. This option can be given multiple times. The track IDs are the same as the ones output by <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8217;s <code>&#8211;identify</code> option. </p>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvextract timecodes_v2 input.mkv 1:tc-track1.txt 2:tc-track2.txt
</pre>
</dl>
</dl>
<h2>OUTPUT REDIRECTION</h2>
<p> Several extraction modes cause <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) to write the extracted data to the console. There are generally two ways of writing this data into a file: one provided by the shell and one provided by <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) itself. </p>
<p> The shell&#8217;s builtin redirection mechanism is used by appending &#8216;&gt; output-filename.ext&#8217; to the command line. Example: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvextract tags source.mkv &gt; tags.xml
</pre>
</dl>
<p> <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1)&#8217;s own redirection is invoked with the <code>&#8211;redirect-output</code> option. Example: </p>
<dl>
<dt>
<dd>
<pre>
$ mkvextract tags source.mkv --redirect-output tags.xml
</pre>
</dl>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> On Windows you should probably use the <code>&#8211;redirect-output</code> option because <code>cmd.exe</code> sometimes interpretes special characters before they&#8217;re written into the output file resulting in broken output. </p>
</dl>
<h2>TEXT FILES AND CHARACTER SET CONVERSIONS</h2>
<p> For an in-depth discussion about how all tools in the MKVToolNix suite handle character set conversions, input/output encoding, command line encoding and console encoding please see the identically-named section in the <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) man page.</p>
<h2>OUTPUT FILE FORMATS</h2>
<p> The decision about the output format is based on the track type, not on the extension used for the output file name. The following track types are supported at the moment: </p>
<p> V_MPEG4/ISO/AVC</p>
<dl>
<dt>
<dd> H.264 / AVC video tracks are written to H.264 elementary streams which can be processed further with e.g. MP4Box(TM) from the GPAC(TM) package.</dl>
<p> V_MS/VFW/FOURCC</p>
<dl>
<dt>
<dd> Fixed FPS video tracks with this CodecID are written to AVI files.</dl>
<p> V_REAL/*</p>
<dl>
<dt>
<dd> RealVideo(TM) tracks are written to RealMedia(TM) files.</dl>
<p> V_THEORA</p>
<dl>
<dt>
<dd> Theora(TM) streams will be written within an Ogg(TM) container</dl>
<p> V_VP8, V_VP9</p>
<dl>
<dt>
<dd> VP8 / VP9 tracks are written to IVF files.</dl>
<p> A_MPEG/L2</p>
<dl>
<dt>
<dd> MPEG-1 Audio Layer II streams will be extracted to raw MP2 files.</dl>
<p> A_MPEG/L3, A_AC3</p>
<dl>
<dt>
<dd> These will be extracted to raw MP3 and AC3 files.</dl>
<p> A_PCM/INT/LIT</p>
<dl>
<dt>
<dd> Raw PCM data will be written to a WAV file.</dl>
<p> A_AAC/MPEG2/*, A_AAC/MPEG4/*, A_AAC</p>
<dl>
<dt>
<dd> All AAC files will be written into an AAC file with ADTS headers before each packet. The ADTS headers will not contain the deprecated emphasis field.</dl>
<p> A_VORBIS</p>
<dl>
<dt>
<dd> Vorbis audio will be written into an OggVorbis(TM) file.</dl>
<p> A_REAL/*</p>
<dl>
<dt>
<dd> RealAudio(TM) tracks are written to RealMedia(TM) files.</dl>
<p> A_TTA1</p>
<dl>
<dt>
<dd> TrueAudio(TM) tracks are written to TTA files. Please note that due to Matroska(TM)&#8217;s limited timecode precision the extracted file&#8217;s header will be different regarding two fields: <i>data_length</i> (the total number of samples in the file) and the CRC.</dl>
<p> A_ALAC</p>
<dl>
<dt>
<dd> ALAC tracks are written to CAF files.</dl>
<p> A_FLAC</p>
<dl>
<dt>
<dd> FLAC tracks are written to raw FLAC files.</dl>
<p> A_WAVPACK4</p>
<dl>
<dt>
<dd> WavPack(TM) tracks are written to WV files.</dl>
<p> A_OPUS</p>
<dl>
<dt>
<dd> Opus(TM) tracks are written to OggOpus(TM) files.</dl>
<p> S_TEXT/UTF8</p>
<dl>
<dt>
<dd> Simple text subtitles will be written as SRT files.</dl>
<p> S_TEXT/SSA, S_TEXT/ASS</p>
<dl>
<dt>
<dd> SSA and ASS text subtitles will be written as SSA/ASS files respectively.</dl>
<p> S_KATE</p>
<dl>
<dt>
<dd> Kate(TM) streams will be written within an Ogg(TM) container.</dl>
<p> S_VOBSUB</p>
<dl>
<dt>
<dd> VobSub(TM) subtitles will be written as SUB files along with the respective index files, as IDX files.</dl>
<p> S_TEXT/USF</p>
<dl>
<dt>
<dd> USF text subtitles will be written as USF files.</dl>
<p> S_HDMV/PGS</p>
<dl>
<dt>
<dd> PGS subtitles will be written as SUP files.</dl>
<p> Tags</p>
<dl>
<dt>
<dd> Tags are converted to a XML format. This format is the same that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) supports for reading tags.</dl>
<p> Attachments</p>
<dl>
<dt>
<dd> Attachments are written to they output file as they are. No conversion whatsoever is done.</dl>
<p> Chapters</p>
<dl>
<dt>
<dd> Chapters are converted to a XML format. This format is the same that <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) supports for reading chapters. Alternatively a stripped-down version can be output in the simple OGM style format.</dl>
<p> Timecodes</p>
<dl>
<dt>
<dd> Timecodes are first sorted and then output as a timecode v2 format compliant file ready to be fed to <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1). The extraction to other formats (v1, v3 and v4) is not supported.</dl>
<h2>EXIT CODES</h2>
<p> <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) exits with one of three exit codes: </p>
<dl>
<dt>
<dd> &bull; <code>0</code> &#8212; This exit codes means that extraction has completed successfully.</dl>
<dl>
<dt>
<dd> &bull; <code>1</code> &#8212; In this case <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) has output at least one warning, but extraction did continue. A warning is prefixed with the text &#8216;Warning:&#8217;. Depending on the issues involved the resulting files might be ok or not. The user is urged to check both the warning and the resulting files.</dl>
<dl>
<dt>
<dd> &bull; <code>2</code> &#8212; This exit code is used after an error occurred. <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1) aborts right after outputting the error message. Error messages range from wrong command line arguments over read/write errors to broken files.</dl>
<h2>ESCAPING SPECIAL CHARS IN TEXT</h2>
<p> There are a few places in which special characters in text must or should be escaped. The rules for escaping are simple: each character that needs escaping is replaced with a backslash followed by another character. </p>
<p> The rules are: &#8216; &#8216; (a space) becomes &#8216;\s&#8217;, &#8216;&quot;&#8217; (double quotes) becomes &#8216;\2&#8217;, &#8216;:&#8217; becomes &#8216;
