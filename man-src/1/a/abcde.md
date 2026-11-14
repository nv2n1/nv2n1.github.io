---
title: "abcde(1)"
name: "abcde"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abcde/"
description: "abcde – Grab an entire CD and compress it to Ogg/Vorbis, MP3, FLAC, Ogg/Speex and/or MPP/MP+(Musepack) format."
---

<h2>NAME</h2>
<p> abcde &#8211; Grab an entire CD and compress it to Ogg/Vorbis, MP3, FLAC, Ogg/Speex and/or MPP/MP+(Musepack) format.</p>
<h2>SYNOPSIS</h2>
<p> <code>abcde</code> <i>[options] [tracks]</i></p>
<h2>DESCRIPTION</h2>
<p> Ordinarily, the process of grabbing the data off a CD and encoding it, then tagging or commenting it, is very involved. <code>abcde</code> is designed to automate this. It will take an entire CD and convert it into a compressed audio format &#8211; Ogg/Vorbis, MPEG Audio Layer III, Free Lossless Audio Codec (FLAC), Ogg/Speex, MPP/MP+(Musepack) and/or M4A (AAC) format(s). With one command, it will:</p>
<dl>
<dt><code>*</code></p>
<dd> Do a CDDB or Musicbrainz query over the Internet to look up your CD or use a locally stored CDDB entry</p>
<dt><code>*</code></p>
<dd> Grab an audio track (or all the audio CD tracks) from your CD</p>
<dt><code>*</code></p>
<dd> Normalize the volume of the individual file (or the album as a single unit)</p>
<dt><code>*</code></p>
<dd> Compress to Ogg/Vorbis, MP3, FLAC, Ogg/Speex, MPP/MP+(Musepack) and/or M4A format(s), all in one CD read</p>
<dt><code>*</code></p>
<dd> Comment or ID3/ID3v2 tag</p>
<dt><code>*</code></p>
<dd> Give an intelligible filename</p>
<dt><code>*</code></p>
<dd> Calculate replaygain values for the individual file (or the album as a single unit)</p>
<dt><code>*</code></p>
<dd> Delete the intermediate WAV file (or save it for later use)</p>
<dt><code>*</code></p>
<dd> Repeat until finished</dl>
<p> Alternatively, <code>abcde</code> can also grab a CD and turn it into a single FLAC file with an embedded cuesheet which can be user later on as a source for other formats, and will be treated as if it was the original CD. In a way, <code>abcde</code> can take a compressed backup of your CD collection.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1</code></p>
<dd> Encode the whole CD in a single file. The resulting file uses the CD title for tagging. If the resulting format is a flac file with an embedded cuesheet, the file can be used as a source for creating other formats. Use &quot;-1 -o flac -a default,cue&quot; for obtaining such a file.</p>
<dt><code>-a [actions]</code></p>
<dd> Comma-delimited list of actions to perform. Can be one or more of: cddb, cue, read, normalize, encode, tag, move, replaygain, playlist, clean. Normalize and encode imply read. Tag implies cddb, read, encode. Move implies cddb, read, encode, tag. Replaygain implies cddb, read, encode, tag and move. Playlist implies cddb. The default is to do all actions except cue, normalize, replaygain and playlist.</p>
<dt><code>-b</code></p>
<dd> Enable batch mode normalization. See the BATCHNORM configuration variable.</p>
<dt><code>-B</code></p>
<dd> Disable batch mode replaygain. It processes file by file to add the replaygain information. See the NOBATCHREPLAYGAIN configuration variable.</p>
<dt><code>-c [filename]</code></p>
<dd> Specifies an additional configuration file to parse. Configuration options in this file override those in <i>/etc/abcde.conf</i> or <i>$HOME/.abcde.conf</i>.</p>
<dt><code>-C [discid]</code></p>
<dd> Allows you to resume a session for <i>discid</i> when you no longer have the CD available (<code>abcde</code> will automatically resume if you still have the CD in the drive). You must have already finished at least the &quot;read&quot; action during the previous session.</p>
<dt><code>-d [devicename | filename]</code></p>
<dd> CD-ROM block device that contains audio tracks to be read. Alternatively, a single-track flac file with embedded cuesheet.</p>
<dt><code>-D</code></p>
<dd> Capture debugging information (you&#8217;ll want to redirect this &#8211; try &#8216;abcde -D 2&gt;logfile&#8217;)</p>
<dt><code>-e</code></p>
<dd> Erase information about encoded tracks from the internal status file, to enable other encodings if the wav files have been kept.</p>
<dt><code>-f</code></p>
<dd> Force the removal of the temporary ABCDETEMPDIR directory, even when we have not finished. For example, one can read and encode several formats, including &#8216;.ogg&#8217;, and later on execute a &#8216;move&#8217; action with only one of the given formats. On a normal situation it would erase the rest of those encoded formats. In this case, <code>abcde</code> will refuse to execute such command, except if -f is used.</p>
<dt><code>-g</code></p>
<dd> Enable lame&#8217;s &#8211;nogap option. See the NOGAP variable. WARNING: lame&#8217;s &#8211;nogap disables the Xing mp3 tag. This tag is required for mp3 players to correctly display track lengths when playing variable-bit-rate mp3 files.</p>
<dt><code>-h</code></p>
<dd> Get help information.</p>
<dt><code>-j [number]</code></p>
<dd> Start [number] encoder processes at once. Useful for SMP systems. Overrides the MAXPROCS configuration variable. Set it to &quot;0&quot; when using <code>distmp3</code> to avoid local encoding processes.</p>
<dt><code>-k</code></p>
<dd> Keep the wav files after encoding.</p>
<dt><code>-l</code></p>
<dd> Use the low-diskspace algorithm. See the LOWDISK configuration variable.</p>
<dt><code>-L</code></p>
<dd> Use a local CDDB repository. See CDDBLOCALDIR variable.</p>
<dt><code>-m</code></p>
<dd> Create DOS-style playlists, modifying the resulting one by adding CRLF line endings. Some hardware players insist on having those to work.</p>
<dt><code>-n</code></p>
<dd> Do not query CDDB database. Create and use a template. Edit the template to provide song names, artist(s), &#8230;</p>
<dt><code>-N</code></p>
<dd> Non interactive mode. Do not ask anything from the user. Just go ahead.</p>
<dt><code>-o [filetype][:filetypeoptions]</code></p>
<dd> Select output type. Can be &quot;vorbis&quot; (or &quot;ogg&quot;), &quot;mp3&quot;, &quot;flac&quot;, &quot;spx&quot;, &quot;mpc&quot;, &quot;m4a&quot; or &quot;wav&quot;. Specify a comma-delimited list of output types to obtain all specified types. See the OUTPUTTYPE configuration variable. One can pass options to the encoder for a specific filetype on the command line separating them with a colon. The options must be escaped with double-quotes.</p>
<dt><code>-p</code></p>
<dd> Pads track numbers with 0&#8217;s.</p>
<dt><code>-P</code></p>
<dd> Use Unix PIPES to read and encode in one step. It disables multiple encodings, since the WAV audio file is never stored in the disc.</p>
<dt><code>-q [quality]</code></p>
<dd> Use a pre-defined quality level for the encoding process. Defined as low, medium or high. The &quot;medium&quot; value is used to reset the default values if other are used in the config file(s).</p>
<dt><code>-r [hosts&#8230;]</code></p>
<dd> Remote encode on this comma-delimited list of machines using <code>distmp3</code>. See the REMOTEHOSTS configuration variable.</p>
<dt><code>-s [fields&#8230;]</code></p>
<dd> List, separated by commas, the fields to be shown in the CDDB parsed entries. Right now it only uses &quot;year&quot; and &quot;genre&quot;.</p>
<dt><code>-S [speed]</code></p>
<dd> Set the speed of the CD drive. Needs CDSPEED and CDSPEEDOPTS set properly and both the program and device must support the capability.</p>
<dt><code>-t [number]</code></p>
<dd> Start the numbering of the tracks at a given number. It only affects the filenames and the playlist. Internal (tag) numbering remains the same.</p>
<dt><code>-T [number]</code></p>
<dd> Same as -t but changes also the internal (tag) numbering. Keep in mind that the default TRACK tag for MP3 is $T/$TRACKS so it is changed to simply $T.</p>
<dt><code>-U</code></p>
<dd> Set CDDBPROTO to version 5, so that we retrieve ISO-8859-15 encoded CDDB information, and we tag and add comments with Latin1 encoding.</p>
<dt><code>-v</code></p>
<dd> Show the version and exit</p>
<dt><code>-V</code></p>
<dd> Be more verbose. On slow networks the CDDB requests might give the sensation nothing is happening. Add this more than once to make things even more verbose.</p>
<dt><code>-x</code></p>
<dd> Eject the CD when all tracks have been read. See the EJECTCD configuration variable.</p>
<dt><code>-X [cue2discid]</code></p>
<dd> Use an alternative &quot;cue2discid&quot; implementation. The name of the binary must be exactly that. <code>abcde</code> comes with an implementation in python under the examples directory. The special keyword &quot;builtin&quot; forces the usage of the internal (default) implementation in shell script.</p>
<dt><code>-w [comment]</code></p>
<dd> Add a comment to the tracks ripped from the CD.</p>
<dt><code>-W [number]</code></p>
<dd> Concatenate CD&#8217;s. It uses the number provided to define a comment &quot;CD #&quot; and to modify the numbering of the tracks, starting with &quot;#01&quot;. For Ogg/Vorbis and FLAC files, it also defines a DISCNUMBER tag.</p>
<dt><code>-z</code></p>
<dd> DEBUG mode: it will rip, using <code>cdparanoia</code>, the very first second of each track and proceed with the actions requested very quickly, also providing some &quot;hidden&quot; information about what happens on the background. CAUTION: IT WILL ERASE ANY EXISTING RIPS WITHOUT WARNING!</p>
<dt><code>[tracks]</code></p>
<dd> A list of tracks you want <code>abcde</code> to process. If this isn&#8217;t specified, <code>abcde</code> will process the entire CD. Accepts ranges of track numbers &#8211; &quot;abcde 1-5 7 9&quot; will process tracks 1, 2, 3, 4, 5, 7, and 9.</dl>
<h2>OUTPUT</h2>
<p> Each track is, by default, placed in a separate file named after the track in a subdirectory named after the artist under the current directory. This can be modified using the OUTPUTFORMAT and VAOUTPUTFORMAT variables in your <i>abcde.conf</i>. Each file is given an extension identifying its compression format, &#8216;vorbis&#8217; for &#8216;.ogg&#8217;, &#8216;.mp3&#8217;, &#8216;.flac&#8217;, &#8216;.spx&#8217;, &#8216;.mpc&#8217;, &#8216;.aac&#8217; or &#8216;.wav&#8217;.</p>
<h2>CONFIGURATION</h2>
<p> <code>abcde</code> sources two configuration files on startup &#8211; <i>/etc/abcde.conf</i> and <i>$HOME/.abcde.conf</i>, in that order. </p>
<p> The configuration options stated in those files can be overridden by providing the appropriate flags at runtime. </p>
<p> The configuration variables have to be set as follows:</p>
<dl>
<dt><code>VARIABLE=value</code></p>
<dd> Except when &quot;value&quot; needs to be quoted or otherwise interpreted. If other variables within &quot;value&quot; are to be expanded upon reading the configuration file, then double quotes should be used. If they are only supposed to be expanded upon use (for example OUTPUTFORMAT) then single quotes must be used.</p>
<dt>All shell escaping/quoting rules apply.</p>
<dd>
<dt>Here is a list of options <code>abcde</code> recognizes:</p>
<dd>
<dt><code>CDDBMETHOD</code></p>
<dd> Specifies the method we want to use to retrieve the track information. Two values are recognized: &quot;cddb&quot; and &quot;musicbrainz&quot;. The &quot;cddb&quot; value needs the CDDBURL and HELLOINFO variables described below. The &quot;musicbrainz&quot; value uses the Perl helper script <code>abcde-musicbrainz-tool</code> to establish a conversation with the Musicbrainz server for information retrieval.</p>
<dt><code>CDDBURL</code></p>
<dd> Specifies a server to use for CDDB lookups.</p>
<dt><code>CDDBPROTO</code></p>
<dd> Specifies the protocol version used for the CDDB retrieval of results. Version 6 retrieves CDDB entries in UTF-8 format.</p>
<dt><code>HELLOINFO</code></p>
<dd> Specifies the Hello information to send to the CDDB server. The CDDB protocol requires you to send a valid username and hostname each time you connect. The format of this is username [at] hostname.</p>
<dt><code>CDDBLOCALDIR</code></p>
<dd> Specifies a directory where we store a local CDDB repository. The entries must be standard CDDB entries, with the filename being the DISCID value. Other CD playing and ripping programs (like Grip) store the entries under <i>~/.cddb</i> and we can make use of those entries.</p>
<dt><code>CDDBLOCALRECURSIVE</code></p>
<dd> Specifies if the CDDBLOCALDIR has to be searched recursively trying to find a match for the CDDB entry. If a match is found and selected, and CDDBCOPYLOCAL is selected, it will be copied to the root of the CDDBLOCALDIR if CDDBLOCALPOLICY is &quot;modified&quot; or &quot;new&quot;.</p>
<dt><code>CDDBLOCALPOLICY</code></p>
<dd> Defines when a CDDB entry should be stored in the defined CDDBLOCALDIR. The possible policies are: &quot;net&quot; for a CDDB entry which has been received from the net (overwriting any possible local CDDB entry); &quot;new&quot; for a CDDB entry which was received from the net, but will request confirmation to overwrite a local CDDB entry found in the root of the CDDBLOCALDIR directory; &quot;modified&quot; for a CDDB entry found in the local repository but which has been modified by the user; and &quot;always&quot; which forces the CDDB entry to be stored back in the root of the CDDBLOCALDIR no matter where it was found, and no matter it was not edited. This last option will always overwrite the one found in the root of the local repository (if any). STILL NOT WORKING!!</p>
<dt><code>CDDBCOPYLOCAL</code></p>
<dd> Store local copies of the CDDB entries under the $CDDBLOCALDIR directory.</p>
<dt><code>CDDBUSELOCAL</code></p>
<dd> Actually use the stored copies of the CDDB entries. Can be overridden using the &quot;-L&quot; flag (if is CDDBUSELOCAL in &quot;n&quot;). If an entry is found, we always give the choice of retrieving a CDDB entry from the internet.</p>
<dt><code>SHOWCDDBFIELDS</code></p>
<dd> Coma-separated list of fields we want to parse during the CDDB parsing. Defaults to &quot;year,genre&quot;.</p>
<dt><code>OGGENCODERSYNTAX</code></p>
<dd> Specifies the style of encoder to use for the Ogg/Vorbis encoder. Valid options are &#8216;oggenc&#8217; (default for Ogg/Vorbis) and &#8216;vorbize&#8217;. This affects the default location of the binary, the variable to pick encoder command-line options from, and where the options are given.</p>
<dt><code>MP3ENCODERSYNTAX</code></p>
<dd> Specifies the style of encoder to use for the MP3 encoder. Valid options are &#8216;lame&#8217; (default for MP3), &#8216;gogo&#8217;, &#8216;bladeenc&#8217;, &#8216;l3enc&#8217; and &#8216;mp3enc&#8217;. Affects the same way as explained above for Ogg/Vorbis.</p>
<dt><code>FLACENCODERSYNTAX</code></p>
<dd> Specifies the style of encoder to use for the FLAC encoder. At this point only &#8216;flac&#8217; is available for FLAC encoding.</p>
<dt><code>SPEEXENCODERSYNTAX</code></p>
<dd> Specifies the style of encoder to use for Speex encoder. At this point only &#8216;speexenc&#8217; is available for Ogg/Speex encoding.</p>
<dt><code>MPPENCODERSYNTAX</code></p>
<dd> Specifies the style of encoder to use for MPP/MP+ (Musepack) encoder. At this point we only have &#8216;mppenc&#8217; available, from corecodecs.org.</p>
<dt><code>AACENCODERSYNTAX</code></p>
<dd> Specifies the style of encoder to use for M4A (AAC) encoder. At this point we only support &#8216;faac&#8217;, so &#8216;default&#8217; points to it.</p>
<dt><code>NORMALIZERSYNTAX</code></p>
<dd> Specifies the style of normalizer to use. Valid options are &#8216;default&#8217; and &#8216;normalize&#8217;&nbsp;<wbr>(and both run &#8216;normalize&#8217;), since we only support it, ATM.</p>
<dt><code>CDROMREADERSYNTAX</code></p>
<dd> Specifies the style of cdrom reader to use. Valid options are &#8216;cdparanoia&#8217;, &#8216;debug&#8217; and &#8216;flac&#8217;. It is used for querying the CDROM and obtain a list of valid tracks and DATA tracks. The special &#8216;flac&#8217; case is used to &quot;rip&quot; CD tracks from a single-track flac file.</p>
<dt><code>CUEREADERSYNTAX</code></p>
<dd> Specifies the syntax of the program we use to read the CD CUE sheet. Right now we only support &#8216;mkcue&#8217;, but in the future other readers might be used.</p>
<dt><code>KEEPWAVS</code></p>
<dd> It defaults to no, so if you want to keep those wavs ripped from your CD, set it to &quot;y&quot;. You can use the &quot;-k&quot; switch in the command line. The default behaviour with KEEPWAVS set is to keep the temporary directory and the wav files even you have requested the &quot;clean&quot; action.</p>
<dt><code>PADTRACKS</code></p>
<dd> If set to &quot;y&quot;, it adds 0&#8217;s to the file numbers to complete a two-number holder. Useful when encoding tracks 1-9.</p>
<dt><code>INTERACTIVE</code></p>
<dd> Set to &quot;n&quot; if you want to perform automatic rips, without user intervention.</p>
<dt><code>NICE VALUES</code></p>
<dd> Define the values for priorities (nice values) for the different CPU-hungry processes: encoding (ENCNICE), CDROM read (READNICE) and distributed encoder with <code>distmp3</code> (DISTMP3NICE).</p>
<dt><code>PATHNAMES</code></p>
<dd> The following configuration file options specify the pathnames of their respective utilities: LAME, TOOLAME, GOGO, BLADEENC, L3ENC, XINGMP3ENC, MP3ENC, VORBIZE, OGGENC, FLAC, SPEEXENC, MPPENC, AACEND, ID3, ID3V2, EYED3, METAFLAC, CDPARANOIA, CDDA2WAV, CDDAFS, CDDISCID, CDDBTOOL, EJECT, MD5SUM, DISTMP3, VORBISCOMMENT, NORMALIZE, CDSPEED, MP3GAIN, VORBISGAIN, MPPGAIN, MKCUE, MKTOC, CUE2DISCID (see option &quot;-X&quot;), DIFF and HTTPGET.</p>
<dt><code>COMMAND-LINE OPTIONS</code></p>
<dd> If you wish to specify command-line options to any of the programs <code>abcde</code> uses, set the following configuration file options: LAMEOPTS, TOOLAMEOPTS, GOGOOPTS, BLADEENCOPTS, L3ENCOPTS, XINGMP3ENCOPTS, MP3ENCOPTS, VORBIZEOPTS, OGGENCOPTS, FLACOPTS, SPEEXENCOPTS, MPPENCOPTS, AACENCOPTS, ID3OPTS, ID3V2OPTS, MP3GAINOPTS, CDPARANOIAOPTS, CDDA2WAVOPTS, CDDAFSOPTS, CDDBTOOLOPTS, EJECTOPTS, DISTMP3OPTS, NORMALIZEOPTS, CDSPEEDOPTS, MKCUEOPTS, VORBISCOMMMENTOPTS, METAFLACOPTS, DIFFOPTS, FLACGAINOPTS, VORBISGAINOPTS and HTTPGETOPTS.</p>
<dt><code>CDSPEEDVALUE</code></p>
<dd> Set the value of the CDROM speed. The default is to read the disc as fast as the reading program and the system permits. The steps are defined as 150kB/s (1x).</p>
<dt><code>ACTIONS</code></p>
<dd> The default actions to be performed when reading a disc.</p>
<dt><code>CDROM</code></p>
<dd> If set, it points to the CD-Rom device which has to be used for audio extraction. Abcde tries to guess the right device, but it may fail. The special &#8216;flac&#8217; option is defined to extract tracks from a single-track flac file.</p>
<dt><code>CDPARANOIACDROMBUS</code></p>
<dd> Defined as &quot;d&quot; when using <code>cdparanoia</code> with an IDE bus and as &quot;g&quot; when using <code>cdparanoia</code> with the ide-scsi emulation layer.</p>
<dt><code>OUTPUTDIR</code></p>
<dd> Specifies the directory to place completed tracks/playlists in.</p>
<dt><code>WAVOUTPUTDIR</code></p>
<dd> Specifies the temporary directory to store .wav files in. Abcde may use up to 700MB of temporary space for each session (although it is rare to use over 100MB for a machine that can encode music as fast as it can read it).</p>
<dt><code>OUTPUTTYPE</code></p>
<dd> Specifies the encoding format to output, as well as the default extension and encoder. Defaults to &quot;vorbis&quot;. Valid settings are &quot;vorbis&quot; (or &quot;ogg&quot;) (Ogg/Vorbis), &quot;mp3&quot; (MPEG-1 Audio Layer III), &quot;flac&quot; (Free Lossless Audio Codec), &quot;spx&quot; (Ogg/Speex), &quot;mpc&quot; (MPP/MP+ (Musepack)), &quot;m4a&quot; (for M4A (AAC)) or &quot;wav&quot; (Microsoft Waveform). Values like &quot;vorbis,mp3&quot; encode the tracks in both Ogg/Vorbis and MP3 formats. For example<br />
 OUTPUTTYPE=vorbis,flac<br />
 For each value in OUTPUTTYPE, <code>abcde</code> expands a different process for encoding, tagging and moving, so you can use the format placeholder, OUTPUT, to create different subdirectories to hold the different types. The variable OUTPUT will be &#8216;vorbis&#8217;, &#8216;mp3&#8217;, &#8216;flac&#8217;, &#8216;spx&#8217;, &#8216;mpc&#8217;, &#8216;m4a&#8217; and/or &#8216;wav&#8217;, depending on the OUTPUTTYPE you define. For example<br />
 OUTPUTFORMAT=&#8217;${OUTPUT}/${ARTISTFILE}/${ALBUMFILE}/${TRACKNUM}._${TRACKFILE}&#8217;</p>
<dt><code>OUTPUTFORMAT</code></p>
<dd> Specifies the format for completed Ogg/Vorbis, MP3, FLAC, Ogg/Speex, MPP/MP+ (Musepack) or M4A filenames. Variables are included using standard shell syntax. Allowed variables are GENRE, ALBUMFILE, ARTISTFILE, TRACKFILE, TRACKNUM, and YEAR. Default is &#8216;${ARTISTFILE}-${ALBUMFILE}/${TRACKNUM}-${TRACKFILE}&#8217;. Make sure to use single quotes around this variable. TRACKNUM is automatically zero-padded, when the number of encoded tracks is higher than 9. When lower, you can force with &#8216;-p&#8217; in the command line.</p>
<dt><code>VAOUTPUTFORMAT</code></p>
<dd> Just like OUTPUTFORMAT but for Various Artists discs. The default is &#8216;Various-${ALBUMFILE}/${TRACKNUM}.${ARTISTFILE}-${TRACKFILE}&#8217;</p>
<dt><code>ONETRACKOUTPUTFORMAT</code></p>
<dd> Just like OUTPUTFORMAT but for single-track rips (see option &quot;-1&quot;). The default is &#8216;${ARTISTFILE}-${ALBUMFILE}/${ALBUMFILE}&#8217;</p>
<dt><code>VAONETRACKOUTPUTFORMAT</code></p>
<dd> Just like ONETRACKOUTPUTFORMAT but for Various Artists discs. The default is &#8216;Various-${ALBUMFILE}/${ALBUMFILE}&#8217;</p>
<dt><code>MAXPROCS</code></p>
<dd> Defines how many encoders to run at once. This makes for huge speedups on SMP systems. You should run one encoder per CPU at once for maximum efficiency, although more doesn&#8217;t hurt very much. Set it &quot;0&quot; when using mp3dist to avoid getting encoding processes in the local host.</p>
<dt><code>LOWDISK</code></p>
<dd> If set to y, conserves disk space by encoding tracks immediately after reading them. This is substantially slower than normal operation but requires several hundred MB less space to complete the encoding of an entire CD. Use only if your system is low on space and cannot encode as quickly as it can read. </p>
<p> Note that this option may also help when reading a CD with errors. This is because on a scratchy disk reading is quite timing sensitive and this option reduces the background load on the system which allows the ripping program more precise control.</p>
<dt><code>BATCHNORM</code></p>
<dd> If set to y, enables batch mode normalization, which preserves relative volume differences between tracks of an album. Also enables nogap encoding when using the &#8216;lame&#8217; encoder.</p>
<dt><code>NOGAP</code></p>
<dd> Activate the lame&#8217;s &#8211;nogap option, that allows files found in CDs with no silence between songs (such as live concerts) to be encoded without noticeable gaps. WARNING: lame&#8217;s &#8211;nogap disables the Xing mp3 tag. This tag is required for mp3 players to correctly display track lengths when playing variable-bit-rate mp3 files.</p>
<dt><code>PLAYLISTFORMAT</code></p>
<dd> Specifies the format for completed playlist filenames. Works like the OUTPUTFORMAT configuration variable. Default is &#8216;${ARTISTFILE}_-_${ALBUMFILE}.m3u&#8217;. Make sure to use single quotes around this variable.</p>
<dt><code>PLAYLISTDATAPREFIX</code></p>
<dd> Specifies a prefix for filenames within a playlist. Useful for http playlists, etc.</p>
<dt><code>DOSPLAYLIST</code></p>
<dd> If set, the resulting playlist will have CR-LF line endings, needed by some hardware-based players.</p>
<dt><code>COMMENT</code></p>
<dd> Specifies a comment to embed in the ID3 or Ogg comment field of each finished track. Can be up to 28 characters long. Supports the same syntax as OUTPUTFORMAT. Does not currently support ID3v2.</p>
<dt><code>REMOTEHOSTS</code></p>
<dd> Specifies a comma-delimited list of systems to use for remote encoding using <code>distmp3</code>. Equivalent to -r.</p>
<dt><code>mungefilename</code></p>
<dd> mungefilename() is an <code>abcde</code> shell function that can be overridden via <i>abcde.conf</i>. It takes CDDB data as $1 and outputs the resulting filename on stdout. It defaults to eating control characters, apostrophes and question marks, translating spaces and forward slashes to underscores, and translating colons to an underscore and a hyphen.<br />
 If you modify this function, it is probably a good idea to keep the forward slash munging (UNIX cannot store a file with a &#8216;/&#8217; char in it) as well as the control character munging (NULs can&#8217;t be in a filename either, and newlines and such in filenames are typically not desirable).</p>
<dt><code>mungegenre</code></p>
<dd> mungegenre () is a shell function used to modify the $GENRE variable. As a default action, it takes $GENRE as $1 and outputs the resulting value to stdout converting all UPPERCASE characters to lowercase.</p>
<dt><code>pre_read</code></p>
<dd> pre_read () is a shell function which is executed before the CDROM is read for the first time, during <code>abcde</code> execution. It can be used to close the CDROM tray, to set its speed (via &quot;setcd&quot; or via &quot;eject&quot;, if available) and other preparation actions. The default function is empty.</p>
<dt><code>post_read</code></p>
<dd> post_read () is a shell function which is executed after the CDROM is read (and, if applies, before the CDROM is ejected). It can be used to read a TOC from the CDROM, or to try to read the DATA areas from the CD (if any exist). The default function is empty.</p>
<dt><code>EJECTCD</code></p>
<dd> If set to &quot;y&quot;, <code>abcde</code> will call <code><a href="/docs/linux/man/1-eject/">eject</a></code>(1) to eject the cdrom from the drive after all tracks have been read. It has no effect when CDROM is set to a flac file.</p>
<dt><code>EXTRAVERBOSE</code></p>
<dd> If set to &quot;1&quot;, some operations which are usually now shown to the end user are visible, such as CDDB queries. Useful for initial debug and if your network/CDDB server is slow. Set to &quot;2&quot; or more for even more verbose output.</dl>
<h2>EXAMPLES</h2>
<p> Possible ways one can call <code>abcde</code>:</p>
<dl>
<dt><code>abcde</code></p>
<dd> Will work in most systems</p>
<dt><code>abcde -d /dev/cdrom2</code></p>
<dd> If the CDROM you are reading from is not the standard <i>/dev/cdrom</i> (in GNU/Linux systems)</p>
<dt><code>abcde -o vorbis,flac</code></p>
<dd> Will create both Ogg/Vorbis and Ogg/FLAC files.</p>
<dt><code>abcde -o vorbis:-b 192</code></p>
<dd> Will pass &quot;-b 192&quot; to the Ogg/Vorbis encoder, without having to modify the config file</p>
<dt><code>abcde -W 1</code></p>
<dd> For double+ CD settings: will create the 1st CD starting with the track number 101, and will add a comment &quot;CD 1&quot; to the tracks, the second starting with 201 and so on.</p>
<dt><code>abcde -d singletrack.flac</code></p>
<dd> Will extract the files contained in singletrack using the embedded cuesheet.</dl>
<h2>BACKEND TOOLS</h2>
<p> <code>abcde</code> requires the following backend tools to work:</p>
<dl>
<dt><code>*</code></p>
<dd> An Ogg/Vorbis, MP3, FLAC, Ogg/Speex, MPP/MP+(Musepack) or M4A encoder (oggenc, vorbize, lame, gogo, bladeenc, l3enc, mp3enc, flac, speexenc, mppenc, faac)</p>
<dt><code>*</code></p>
<dd> An audio CD reading utility (cdparanoia, icedax, cdda2wav, dagrab)</p>
<dt><code>*</code></p>
<dd> cd-discid, a CDDB DiscID reading program.</p>
<dt><code>*</code></p>
<dd> An HTTP retrieval program: wget, fetch (FreeBSD) or curl (Mac OS X, among others). Alternatively, abcde-musicbrainz-tool (which depends on Perl and some Musicbrainz libraries) can be used to retrieve CDDB information about the CD.</p>
<dt><code>*</code></p>
<dd> (for MP3s) id3 or id3v2, id3 v1 and v2 tagging programs.</p>
<dt><code>*</code></p>
<dd> (optional) distmp3, a client/server for distributed mp3 encoding.</p>
<dt><code>*</code></p>
<dd> (optional) normalize, a WAV file volume normalizer.</p>
<dt><code>*</code></p>
<dd> (optional) a replaygain file volume modifier (vorbisgain, metaflac, mp3gain, replaygain),</p>
<dt><code>*</code></p>
<dd> (optional) mkcue, a CD cuesheet extractor.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cdparanoia/">cdparanoia</a></code>(1), <code><a href="/docs/linux/man/1-icedax/">icedax</a></code>(1), <code><a href="/docs/linux/man/1-cdda2wav/">cdda2wav</a></code>(1), <code><a href="/docs/linux/man/1-dagrab/">dagrab</a></code>(1), <code><a href="/docs/linux/man/1-normalize/">normalize</a></code>(1), <code><a href="/docs/linux/man/1-oggenc/">oggenc</a></code>(1), <code><a href="/docs/linux/man/1-vorbize/">vorbize</a></code>(1), <code><a href="/docs/linux/man/1-flac/">flac</a></code>(1), <code><a href="/docs/linux/man/1-toolame/">toolame</a></code>(1), <code><a href="/docs/linux/man/1-speexenc/">speexenc</a></code>(1), <code><a href="/docs/linux/man/1-mppenc/">mppenc</a></code>(1), <code><a href="/docs/linux/man/1-faac/">faac</a></code>(1), <code><a href="/docs/linux/man/1-id3/">id3</a></code>(1), <code><a href="/docs/linux/man/1-id3v2/">id3v2</a></code>(1), <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1), <code><a href="/docs/linux/man/1-fetch/">fetch</a></code>(1), <code><a href="/docs/linux/man/1-cd-discid/">cd-discid</a></code>(1), <code><a href="/docs/linux/man/1-distmp3/">distmp3</a></code>(1), <code><a href="/docs/linux/man/1-distmp3host/">distmp3host</a></code>(1), <code><a href="/docs/linux/man/1-curl/">curl</a></code>(1), <code><a href="/docs/linux/man/1-mkcue/">mkcue</a></code>(1), <code><a href="/docs/linux/man/1-vorbisgain/">vorbisgain</a></code>(1), <code><a href="/docs/linux/man/1-mp3gain/">mp3gain</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> Robert Woodcock &lt;rcw [at] debian.org&gt;, Jesus Climent &lt;jesus.climent [at] hispalinux.es&gt;, Colin Tuckley &lt;colint [at] debian.org&gt;, Steve McIntyre &lt;93sam [at] debian.org&gt; and contributions from many others. </p>
<h2>Index</h2>
