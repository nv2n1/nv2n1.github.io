---
title: "cdrdao(1)"
name: "cdrdao"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cdrdao/"
description: "cdrdao – reads and writes CDs in disc-at-once mode"
---

<h2 class="name">NAME</h2>
<p> cdrdao &#8211; reads and writes CDs in disc-at-once mode </p>
<h2>SYNOPSIS</h2>
<p> <code>cdrdao</code> {<code>show-toc|toc-info|toc-size|read-toc|read-cd|read-cddb|show-data|read-test|disk-info|discid|msinfo|drive-info|unlock|scanbus|simulate|write|copy|blank</code>} [<code>&#8211;device</code> <i>device</i>] [<code>&#8211;source-device</code> <i>device</i>] [<code>&#8211;driver</code> <i>driver-id</i>] [<code>&#8211;source-driver</code> <i>driver-id</i>] [<code>&#8211;simulate</code>] [<code>&#8211;speed</code> <i>writing-speed</i>] [<code>&#8211;blank-mode</code> <i>mode]</i> [<code>&#8211;datafile</code> <i>file</i>] [<code>&#8211;read-raw</code>] [<code>&#8211;read-subchan</code> [<code>&#8211;no-mode2-mixed</code>] <i>mode</i>] [<code>&#8211;tao-source</code>] [<code>&#8211;tao-source-adjust</code> <i>link-blocks</i>] [<code>&#8211;fast-toc</code>] [<code>&#8211;buffers</code> <i>buffer-count</i>] [<code>&#8211;multi</code>] [<code>&#8211;overburn</code>] [<code>&#8211;eject</code>] [<code>&#8211;swap</code>] [<code>&#8211;session</code>] [<code>&#8211;force</code>] [<code>&#8211;reload</code>] [<code>&#8211;keepimage</code>] [<code>&#8211;on-the-fly</code>] [<code>&#8211;paranoia-mode</code> <i>mode</i>] [<code>&#8211;with-cddb</code>] [<code>&#8211;cddb-servers</code> <i>server-list</i>] [<code>&#8211;cddb-timeout</code> <i>timeout</i>] [<code>&#8211;cddb-directory</code> <i>directory</i>] [<code>&#8211;tmpdir</code> <i>directory</i>] [<code>&#8211;keep</code>] [<code>&#8211;save</code>] [<code>-n</code>] [<code>-v</code> <i>verbose-level</i>] toc-file</p>
<h2>DESCRIPTION</h2>
<p> <i>cdrdao</i> creates audio and data CD-Rs in disk-at-once (DAO) mode driven by a description file called <i>toc-file.</i> In DAO mode it is possible to create non standard track pre-gaps that have other lengths than 2 seconds and contain nonzero audio data. This is for example useful to divide live recordings into tracks where 2 second gaps would be kind of irritating. </p>
<p> Instead of a <i>toc-file</i> a cue file (used by a famous DOS/Windows mastering tool) may be used. See the CUE FILES section for more details. </p>
<h2>COMMANDS</h2>
<dl>
<dt>The first argument must be one of the following commands:</p>
<dd>
<dt><code>show-toc</code></p>
<dd> Print out a summary about what will be written to the CD-R.</p>
<dt><code>toc-info</code></p>
<dd> Prints out short toc-file summary.</p>
<dt><code>toc-size</code></p>
<dd> Prints total number of blocks for toc.</p>
<dt><code>read-toc</code></p>
<dd> Analyze each track of the inserted CD and create a <i>toc-file</i> that can be used to make a more or less exact copy of the CD. This command does not read out the audio or data tracks, use <code>read-cd</code> for this purpose. </p>
<p> You can specify a filename for the data file via the <code>&#8211;datafile</code> option.</p>
<dt><code>read-cd</code></p>
<dd> Copies all tracks of the inserted CD to an image file and creates a corresponding <i>toc-file.</i> The name of the image file defaults to &quot;data.bin&quot; if no <code>&#8211;datafile</code> option is given.</p>
<dt><code>read-cddb</code></p>
<dd> Tries to retrieve title and artist data from a CDDB server for the CD represented by the given toc-file. The retrieved data is added as CD-TEXT data for language 0 to the toc-file. Existing CD-TEXT data for language 0 will be overwritten.</p>
<dt><code>show-data</code></p>
<dd> Print out all samples that would be written to the CD-R. Each line contains the sample number (starting at 0) and the decimal sample value for the left and right channel. Useful to check if the byte order of audio files is correct.</p>
<dt><code>read-test</code></p>
<dd> Check if all data can be read from the audio files that are defined in the <i>toc-file.</i> This will also check the communication with the slave process that is responsible for writing the audio data to the CD-recorder. Mainly used for testing.</p>
<dt><code>disk-info</code></p>
<dd> Shows information about the inserted CD-R. If the CD-R has an open session it will also print the start of the last and current session which is used by mkisofs to create an image for a second or higher session.</p>
<dt><code>discid</code></p>
<dd> Prints out CDDB information.</p>
<dt><code>msinfo</code></p>
<dd> Shows information required for creating multi session disks with mkisofs. The output is meant for processing by scripts.</p>
<dt><code>drive-info</code></p>
<dd> Shows drive information.</p>
<dt><code>unlock</code></p>
<dd> Tries to unlock the recorder device after a failed write or simulation run. If you cannot eject the CD after a cdrdao run try this command.</p>
<dt><code>blank</code></p>
<dd> Blanks a CD-RW. The CD-RW is minimally blanked by default. Use option <code>&#8211;blank-mode</code> to select another blanking mode. Sometimes the blanking speed must be manually reduced for a successful blanking operation. Use option <code>&#8211;speed</code> to select another blanking speed.</p>
<dt><code>scanbus</code></p>
<dd> Scan for devices.</p>
<dt><code>simulate</code></p>
<dd> Like <code>write</code> but laser stays cold. It is a shortcut for <code>write &#8211;simulate.</code></p>
<dt><code>write</code></p>
<dd> Write the CD-R according to the specifications in the <i>toc-file.</i></p>
<dt><code>copy</code></p>
<dd> Performs all steps to copy a CD. The device containing the source CD must be specified with option <code>&#8211;source-device</code> and the recorder device with option <code>&#8211;device.</code> If only a single device is available the option <code>&#8211;source-device</code> must be omitted and cdrdao will prompt to insert the CD-R after an image of the source CD was created. </p>
<p> The image file with name &quot;cddata&lt;pid&gt;.bin&quot; will be created in the current working directory if no <code>&#8211;datafile</code> option is given. The created image will be removed after it has been written. </p>
<p> If option <code>&#8211;on-the-fly</code> is given no image file is created and the data will be directly piped from the reading device to the CD recorder. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;device</code><i> [prot:]bus,id,lun</i></p>
<dd> Sets the SCSI address of the CD-recorder in form of a bus/id/lun triple, e.g. &#8216;0,2,0&#8217; for the logical unit 0 of SCSI device with ID 2 on bus 0. ATAPI devices can be specified by using the prefix &#8216;ATAPI:&#8217;, e.g. &#8216;ATAPI:0,0,0&#8217;. On some systems a device node may be specified directly, e.g. &#8216;/dev/sg0&#8217; on Linux systems. Linux 2.6 users may also try the newer ATAPI interface with the &#8216;ATA:&#8217; prefix.</p>
<dt><code>&#8211;source-device</code><i> [prot:]bus,id,lun</i></p>
<dd> Like above but used for the <code>copy</code> command to specify the source device.</p>
<dt><code>&#8211;driver</code><i> driver-id:option-flags</i></p>
<dd> Force usage of specified driver instead of the automatically determined driver. Available driver IDs:<br />
 cdd2600, plextor, plextor-scan, generic-mmc, generic-mmc-raw, ricoh-mp6200, yamaha-cdr10x, teac-cdr55, sony-cdu920, sony-cdu948, taiyo-yuden, toshiba.<br />
 Specifying an illegal driver ID will give a list of available drivers. Option flags may be used to modify the behavior of some drivers. See <code>README</code> for details.</p>
<dt><code>&#8211;source-driver</code><i> driver-id:option-flags</i></p>
<dd> Like above but used for the device specified with option <code>&#8211;source-device.</code></p>
<dt><code>&#8211;speed</code><i> value</i></p>
<dd> Set the writing speed to <i>value.</i> Default is the highest possible speed.</p>
<dt><code>&#8211;blank-mode</code><i> mode</i></p>
<dd> Sets the blanking mode. Available modes are <code>full</code> and <code>minimal.</code> Please consider that the data of minimally blanked disks may be easily recovered. Use the <code>full</code> blanking mode for completely erasing all data. The default blanking mode is <code>minimal.</code></p>
<dt><code>&#8211;datafile</code><i> file</i></p>
<dd> Used for <code>read-toc, read-cd</code> and <code>copy.</code> Set the default data file placed in the toc-file by <code>read-toc.</code> Use &quot;-&quot; to indicate STDIN. For commands <code>read-cd</code> and <code>copy</code> it specifies the name of the created image file.</p>
<dt><code>&#8211;read-raw</code></p>
<dd> Only used for commands <code>read-cd</code> and <code>read-toc.</code> All data sectors will be written as 2352 byte blocks including the sector header and L-EC data to the image file. The track mode will be set to MODE1_RAW or MODE2_RAW in the created <i>toc-file.</i></p>
<dt><code>&#8211;read-subchan</code><i> mode</i></p>
<dd> Used by commands <code>read-cd,</code> <code>read-toc</code> and <code>copy.</code> Specifies the type of sub-channel data that is extracted from the source CD and written to the track image or copied to the destination CD. Mode may be <code>rw</code> for reading packed R-W sub-channel data (de-interleaved and error corrected) and <code>rw_raw</code> for reading raw R-W sub-channel data (not de-interleaved, not error corrected, L-EC data included in the track image). If this option is not specified no sub-channel data will be extracted.</p>
<dt><code>&#8211;no-mode2-mixed</code></p>
<dd> Only used for commands <code>read-cd</code> and <code>read-toc.</code> If we have MODE2_FORM1 or MODE2_FORM2, don&#8217;t extract it as MODE2_FORM_MIX. <i>toc-file.</i></p>
<dt><code>&#8211;tao-source</code></p>
<dd> This option indicates to the commands <i>read-toc</i> and <i>read-cd</i> that the source CD was written in TAO mode. It will be assumed that the pre-gap length between all tracks (except between two audio tracks) is the standard 150 blocks plus the number of link blocks (usually 2). The number of link blocks can be controlled with option <i>&#8211;tao-source-adjust.</i> </p>
<p> Use this option only if <i>read-toc</i> or <i>read-cd</i> give error messages in the transition areas between two tracks. If you use this option with pressed CDs or CDs written in DAO mode you will get wrong results.</p>
<dt><code>&#8211;tao-source-adjust</code><i> link-blocks</i></p>
<dd> Specifies the number of link blocks for tracks written in TAO mode. This option has only an effect if option <i>&#8211;tao-source</i> is given.</p>
<dt><code>&#8211;fast-toc</code></p>
<dd> Only used for command <code>read-toc.</code> This option suppresses the pre-gap length and index mark extraction which speeds up the read-toc process. Standard 2 second pre-gaps (but no silence!) will be placed into the toc-file. The resulting CD will sound like the source CD. Only the CD player&#8217;s display will behave slightly different in the transition area between two tracks. </p>
<p> This option might help, too, if read-toc fails with your drive otherwise. </p>
<dt><code>&#8211;buffers</code><i> buffer-count</i></p>
<dd> Specifies the number of buffers that are allocated to avoid buffer under runs. The minimal buffer count is fixed to 10, default is 32 except on FreeBSD systems, on which default is 20. Each buffer holds 1 second of audio data so that dividing <i>buffer-count</i> by the writing speed gives the maximum time for which reading of audio data may be stalled.</p>
<dt><code>&#8211;multi</code></p>
<dd> If this option is given the session will not be closed after the audio data is successfully written. It is possible to append another session on such disks, e.g. to create a CD-EXTRA.</p>
<dt><code>&#8211;overburn</code></p>
<dd> By default cdrdao will not allow one to write more data on a medium than specified by the current medium. This option allows one to ignore this condition.</p>
<dt><code>&#8211;eject</code></p>
<dd> Eject the CD-R after writing or write simulation.</p>
<dt><code>&#8211;swap</code></p>
<dd> Swap the byte order of all samples that are send to the CD-recorder.</p>
<dt><code>&#8211;session</code><i> session-nr</i></p>
<dd> Used for <code>read-toc</code> and <code>read-cd</code> to specify the session which should be processed on multi session CDs.</p>
<dt><code>&#8211;reload</code></p>
<dd> Indicates that the tray may be opened before writing without prompting the user to reset the disk status after a simulation run.</p>
<dt><code>&#8211;force</code></p>
<dd> Forces the execution of an operation that otherwise would not be performed.</p>
<dt><code>&#8211;paranoia-mode</code><i> mode</i></p>
<dd> Sets the correction mode for digital audio extraction. 0: No checking, data is copied directly from the drive. 1: Perform overlapped reading to avoid jitter. 2: Like 1 but with additional checks of the read audio data. 3: Like 2 but with additional scratch detection and repair. </p>
<p> The extraction speed reduces from 0 to 3. </p>
<p> Default is the full paranoia mode (3).</p>
<dt><code>&#8211;keepimage</code></p>
<dd> If a CD is copied with command <i>copy</i> this option will cause that the created image is not removed after the copy process has finished.</p>
<dt><code>&#8211;on-the-fly</code></p>
<dd> Perform CD copy on the fly without creating an image file.</p>
<dt><code>&#8211;with-cddb</code></p>
<dd> Enables the automatic fetching of CDDB data for use as CD-TEXT data for commands <i>copy,</i> <i>read-toc</i> and <i>read-cd.</i></p>
<dt><code>&#8211;cddb-servers</code><i> server-list</i></p>
<dd> Sets space or &#8216;,&#8217; separated list of CDDB servers used for command <i>read-cddb</i> or for commands where the <i>&#8211;with-cddb</i> option is active. A server entry may have the following forms:</p>
<dt>&lt;server&gt;</p>
<dd> Connect to &lt;server&gt;, default cddbp port (888), use cddbp protocol.</p>
<dt>&lt;server&gt;:&lt;port&gt;</p>
<dd> Connect to &lt;server&gt;, port &lt;port&gt;, use cddbp protocol.</p>
<dt>&lt;server&gt;:&lt;cgi-bin-path&gt;</p>
<dd> Connect to &lt;server&gt;, default http port (80), use http protocol, url: &lt;cgi-bin-path&gt;.</p>
<dt>&lt;server&gt;:&lt;port&gt;:&lt;cgi-bin-path&gt;</p>
<dd> Connect to &lt;server&gt;, port &lt;port&gt;, use http protocol, url: &lt;cgi-bin-path&gt;.</p>
<dt>&lt;server&gt;:&lt;port&gt;:&lt;cgi-bin-path&gt;:&lt;proxy-server&gt;</p>
<dd> Connect to &lt;proxy-server&gt;, default http port (80), use http protocol, url: http://&lt;server&gt;:&lt;port&gt;/&lt;cgi-bin-path&gt;.</p>
<dt>&lt;server&gt;:&lt;port&gt;:&lt;cgi-bin-path&gt;:&lt;proxy-server&gt;:&lt;proxy-port&gt;</p>
<dd> Connect to &lt;proxy-server&gt;, port &lt;proxy-port&gt;, use http protocol, url: http://&lt;server&gt;:&lt;port&gt;/&lt;cgi-bin-path&gt;. </p>
<p> The &lt;cgi-bin-path&gt; is usually &quot;/~cddb/cddb.cgi&quot;. </p>
<p> All servers of the server list will be tried in the given order until a successful connection can be established. For http proxy servers the first successful connected http proxy server will be used independent of the ability to connect to the target http server. </p>
<p> Example: freedb.freedb.org:/~cddb/cddb.cgi</p>
<dt><code>&#8211;cddb-timeout</code><i> timeout</i></p>
<dd> Sets the timeout in seconds used for connections to CDDB servers.</p>
<dt><code>&#8211;cddb-directory</code><i> directory</i></p>
<dd> Specifies the local CDDB database directory where fetched CDDB records will be stored. If this option is not given a fetched CDDB record will not be stored locally.</p>
<dt><code>&#8211;tmpdir</code><i> directory</i></p>
<dd> Specifies the directory in which to store temporary data files created from decoding MP3 and Ogg Vorbis files. By default, &quot;/tmp&quot; is used.</p>
<dt><code>&#8211;keep</code></p>
<dd> Upon exit from cdrdao, do not delete temporary WAV files created from MP3 and Ogg Vorbis files.</p>
<dt><code>&#8211;save</code></p>
<dd> Saves some of the current options to the settings file &quot;$HOME/.cdrdao&quot; and exit. See section &#8216;SETTINGS&#8217; for more details.</p>
<dt><code>-n</code></p>
<dd> Suppresses the 10 second pause before writing or simulating.</p>
<dt><code>-v</code><i> verbose-level</i></p>
<dd> Sets verbose level. Levels &gt; 2 are debug levels which produce a lot of output. </p>
</dl>
<h2>TOC FILES</h2>
<p> The <i>toc-file</i> describes what data is written to the CD-R and allows control over track/index positions, pre-gaps and sub-channel information. It is a simple text file, use your favorite text editor to create it. </p>
<p> A <i>toc-file</i> contains an optional header and a sequence of track specifications. Comments starting with &#8216;//&#8217; reaching until end of line can be placed anywhere. </p>
<h3>Header</h3>
<dl>
<dt>CATALOG ddddddddddddd</p>
<dd> Specifies the optional catalog number of the CD. The string must contain exactly 13 digits.</dl>
<p> The following flags specify the type of session that will be created. It is used to create the correct CD-TOC format and to check the consistency of the track modes for the desired session type. If multiple flags are given the last one will take effect.</p>
<dl>
<dt>CD_DA</p>
<dd> The disc contains only audio tracks.</p>
<dt>CD_ROM</p>
<dd> The disc contains just mode 1 tracks or mode 1 and audio tracks (mixed mode CD).</p>
<dt>CD_ROM_XA</p>
<dd> The disc contains mode 2 form 1 or mode 2 form 2 tracks. Audio tracks are allowed, too. This type must be used if multi session disks are created (option &#8211;multi).</p>
<dt>CD_TEXT&nbsp;{&nbsp;&#8230;&nbsp;}</p>
<dd> Defines global CD-TEXT data like the album title and the used languages. See the CD-TEXT section below for the syntax of the CD-TEXT block contents.</dl>
<h3>Track Specification</h3>
<dl>
<dt>TRACK&nbsp;&lt;track-mode&gt;&nbsp;[&lt;sub-channel-mode&gt;]</p>
<dd> Starts a new track, the track number is incremented by 1. The length of a track must be at least 4 seconds. The block length of the input data depends on the &lt;track-mode&gt;: AUDIO: 2352 bytes (588 samples), MODE1: 2048 bytes, MODE1_RAW: 2352 bytes, MODE2: 2336 bytes, MODE2_FORM1: 2048 bytes, MODE2_FORM2: 2324 bytes, MODE2_FORM_MIX: 2336 bytes including the sub-header, MODE2_RAW: 2352 bytes. The &lt;sub-channel-mode&gt; is optional. If given it specifies the type of sub-channel data for each sector. RW: packed R-W sub-channel data (96 bytes, L-EC data will be generated if required), RW_RAW: raw R-W sub-channel data (interleaved and L-EC data already calculated, 96 bytes). The block length is increased by the sub-channel data length if a &lt;sub-channel-mode&gt; is specified. If the input data length is not a multiple of the block length it will be padded with zeros.</dl>
<p> The following flags may follow the track start statement. They are used to set sub-channel information for the current track. Each flag is optional. If not given the following defaults are used: copy not permitted, no pre emphasis, two channel audio, no ISRC code.</p>
<dl>
<dt>[ NO ] COPY</p>
<dd> Sets or clears the copy permitted flag.</p>
<dt>[ NO ] PRE_EMPHASIS</p>
<dd> Sets or clears the pre emphasis flag (only for audio tracks).</p>
<dt>TWO_CHANNEL_AUDIO</p>
<dd> Indicates that track contains two channel audio data (only for audio tracks).</p>
<dt>FOUR_CHANNEL_AUDIO</p>
<dd> Indicates that track contains four channel audio data (only for audio tracks).</p>
<dt>ISRC CCOOOYYSSSSS</p>
<dd> Sets ISRC code of track (only for audio tracks).<br />
 C: country code (upper case letters or digits)<br />
 O: owner code (upper case letters or digits)<br />
 Y: year (digits)<br />
 S: serial number (digits)</dl>
<p> An optional CD-TEXT block that defines the CD-TEXT data for this track may follow. See the CD-TEXT section below for the syntax of the CD-TEXT block contents.</p>
<dl>
<dt>CD_TEXT { &#8230; }</p>
<dd></dl>
<p> At least one of the following statements must appear to specify the data for the current track. Lengths and start positions may be expressed in samples (1/44100 seconds) for audio tracks or in bytes for data tracks. It is also possible to give the length in blocks with the MSF format &#8216;MM:SS:FF&#8217; specifying minutes, seconds and frames (0 &lt;= &#8216;FF&#8217; &lt; 75) . A frame equals one block. </p>
<p> If more than one statement is used the track will be composed by concatenating the data in the specified order.</p>
<dl>
<dt>SILENCE &lt;length&gt;</p>
<dd> Adds zero audio data of specified length to the current audio track. Useful to create silent pre-gaps.</p>
<dt>ZERO &lt;length&gt;</p>
<dd> Adds zero data to data tracks. Must be used to define pre- or post-gaps between tracks of different mode.</p>
<dt>[&nbsp;FILE | AUDIOFILE&nbsp;]&nbsp;&lt;filename&gt;&nbsp;&lt;start&gt;&nbsp;[&nbsp;&lt;length&gt;&nbsp;]</p>
<dd> Adds the audio data of specified file to the current audio track. It is possible to select a portion of an audio file with &lt;start&gt; and &lt;length&gt; which allows non destructive cutting. The first sample of an audio file is addressed with &lt;start&gt; = 0. If &lt;length&gt; is omitted or set to 0 all audio data from &lt;start&gt; until the end of file is used. </p>
<p> Audio files may have raw or WAVE format with 16 bits per sample, 44.1 kHz sampling rate, stereo. Raw files must have the layout &#8216;MSBLeft LSBLeft MSBRight LSBRight &#8230;&#8217; (big endian byte order). WAVE files are expected to have little endian byte order. The option &#8211;swap reverses the expected byte order for all raw and WAVE files. Only filenames with a &quot;.wav&quot; ending are treated as WAVE files, all other names are assumed to be raw audio files. Use tools like <a href="/docs/linux/man/1-sox/">sox</a>(1) to convert other file formats to supported formats. </p>
<p> Specifying a &quot;-&quot; as filename causes data to be read from STDIN. Currently only raw files are supported from STDIN.<br />
&nbsp; If you are unsure about the byte order of your audio files try the command &#8216;show-data&#8217;. If the byte order is correct you will see a sequence of increasing or decreasing numbers for both channels. Otherwise numbers are jumping between very high and low values &#8211; high volume static.</p>
<dt>DATAFILE&nbsp;&lt;filename&gt;&nbsp;[&nbsp;&lt;length&gt;&nbsp;]</p>
<dd> Adds data from given file to the current data track. If &lt;length&gt; is omitted the actual file length will be used.</p>
<dt>FIFO&nbsp;&lt;fifo path&gt;&nbsp;&lt;length&gt;</p>
<dd> Adds data from specified FIFO path to the current audio or data track. &lt;length&gt; must specify the amount of data that will be read from the FIFO. The value is always in terms of bytes (scalar value) or in terms of the block length (MSF value).</p>
<dt>START [ MM:SS:FF ]</p>
<dd> Defines the length of the pre-gap (position where index switches from 0 to 1). If the MSF value is omitted the current track length is used. If the current track length is not a multiple of the block length the pre-gap length will be rounded up to next block boundary. </p>
<p> If no START statement is given the track will not have a pre-gap.</p>
<dt>PREGAP MM:SS:FF</p>
<dd> This is an alternate way to specify a pre-gap with zero audio data. It may appear before the first SILENCE, ZERO or FILE statement. Either PREGAP or START can be used within a track specification. It is equivalent to the sequence </p>
<p>&nbsp;<wbr>&nbsp;SILENCE MM:SS:FF </p>
<p>&nbsp;<wbr>&nbsp;START<br />
 for audio tracks or </p>
<p>&nbsp;<wbr>&nbsp;ZERO MM:SS:FF </p>
<p>&nbsp;<wbr>&nbsp;START<br />
 for data tracks.</dl>
<p> Nothing prevents mixing &#8216;DATAFILE&#8217;/&#8217;ZERO&#8217; and &#8216;AUDIOFILE&#8217;/&#8217;SILENCE&#8217; statements within the same track. The results, however, are undefined. </p>
<p> The end of a track specification may contain zero or more index increment statements:</p>
<dl>
<dt>INDEX MM:SS:FF</p>
<dd> Increments the index number at given position within the track. The first statement will increment from 1 to 2. The position is relative to the real track start, not counting an existing pre-gap. </p>
</dl>
<h3>CD-TEXT Blocks</h3>
<p> A CD-TEXT block may be placed in the global section to define data valid for the whole CD and in each track specification of a <i>toc-file.</i> The global section must define a language map that is used to map a <i>language-number</i> to country codes. Up to 8 different languages can be defined:</p>
<dl>
<dt>LANGUAGE_MAP { 0 : c1 1 : c2 &#8230; 7 : c7 }</p>
<dd> The country code may be an integer value in the range 0..255 or one of the following countries (the corresponding integer value is placed in braces behind the token): EN(9, English)<br />
 It is just necessary to define a mapping for the used languages.</dl>
<p> If no mapping exists for a <i>language-number</i> the data for this language will be ignored. </p>
<p> For each language a language block must exist that defines the actual data for a certain language.</p>
<dl>
<dt>LANGUAGE language-number { cd-text-item cd-text-data cd-text-item cd-text-data &#8230; }</p>
<dd> Defines the CD-TEXT items for given <i>language-number</i> which must be defined in the language map.</dl>
<p> The <i>cd-text-data</i> may be either a string enclosed by &quot; or binary data like </p>
<pre>
{ 0, 10, 255, ... }
</pre>
<p> where each integer number must be in the range 0..255.<br />
 The <i>cd-text-item</i> may be one of the following:</p>
<dl>
<dt>TITLE</p>
<dd> String data: Title of CD or track.</p>
<dt>PERFORMER</p>
<dd> String data.</p>
<dt>SONGWRITER</p>
<dd> String data.</p>
<dt>COMPOSER</p>
<dd> String data.</p>
<dt>ARRANGER</p>
<dd> String data.</p>
<dt>MESSAGE</p>
<dd> String data. Message to the user.</p>
<dt>DISC_ID</p>
<dd> String data: Should only appear in the global CD-TEXT block. The format is usually: XY12345</p>
<dt>GENRE</p>
<dd> Mixture of binary data (genre code) and string data. Should only appear in the global CD-TEXT block. Useful entries will be created by <i>gcdmaster.</i></p>
<dt>TOC_INFO1</p>
<dd> Binary data: Optional table of contents 1. Should only appear in the global CD-TEXT block.</p>
<dt>TOC_INFO2</p>
<dd> Binary data: Optional table of contents 2. Should only appear in the global CD-TEXT block.</p>
<dt>UPC_EAN</p>
<dd> String data: This item should only appear in the global CD-TEXT block. Was always an empty string on the CD-TEXT CDs I had access to.</p>
<dt>ISRC</p>
<dd> String data: ISRC code of track. The format is usually: CC-OOO-YY-SSSSS</p>
<dt>SIZE_INFO</p>
<dd> Binary data: Contains summary about all CD-TEXT data and should only appear in the global CD-TEXT block. The data will be automatically (re)created when the CD-TEXT data is written. </p>
<p> If one of the CD-TEXT items TITLE, PERFORMER, SONGWRITER, COMPOSER, ARRANGER, ISRC is defined for at least on track or in the global section it must be defined for all tracks and in the global section. If a DISC_ID item is defined in the global section, an ISRC entry must be defined for each track. </p>
</dl>
<h3>Examples</h3>
<p> Simple track without pre-gap with all audio data from WAVE file &quot;data.wav&quot;: </p>
<pre>
CD_DA
TRACK AUDIO
FILE &quot;data.wav&quot; 0
</pre>
<p> Standard track with two second pre-gap, ISRC code and CD-TEXT: </p>
<pre><code>
CD_DA
CD_TEXT
{
    LANGUAGE_MAP{
        0 : EN
    } LANGUAGE 0
    {
        TITLE "CD Title" PERFORMER "Performer" DISC_ID "XY12345" UPC_EAN ""
    }
}
TRACK AUDIO
    ISRC "DEXXX9800001" CD_TEXT
{
    LANGUAGE 0
    {
        TITLE "Track Title" PERFORMER "Performer" ISRC "DE-XXX-98-00001"
    }
}
PREGAP 0 : 2 : 0 FILE "data.wav" 0
</code></pre>
<p> Track with 10 second pre-gap containing audio data from raw file &quot;data.cdr&quot;: </p>
<pre>
CD_DA
TRACK AUDIO
FILE &quot;data.cdr&quot; 0 
START 0:10:0
</pre>
<p> Composed track with data from different files. Pre-gap data and length is taken from &quot;pregapdata.wav&quot;. The first minute of &quot;track.cdr&quot; is omitted and two seconds silence are inserted at &#8216;2:0:0&#8217;. Index will be incremented after 2 and 4 minutes past track start: </p>
<pre>
CD_DA
TRACK AUDIO
FILE &quot;pregapdata.wav&quot; 0 
START
FILE &quot;track.cdr&quot; 1:0:0 1:0:0
SILENCE 0:2:0
FILE &quot;track.cdr&quot; 2:0:0
INDEX 2:0:0
INDEX 4:0:0
</pre>
<p> Mixed mode CD with a data track as first track followed by two audio tracks. </p>
<pre>
CD_ROM
TRACK MODE1
DATAFILE &quot;data_1&quot;
ZERO 00:02:00 // post-gap
TRACK AUDIO
SILENCE 00:02:00 // pre-gap
START
FILE &quot;data_2.wav&quot; 0 
TRACK AUDIO
FILE &quot;data_3.wav&quot; 0
</pre>
<h2>CUE FILES</h2>
<p> Cue files may be used wherever a <i>toc-file</i> is expected. The corresponding bin file is not taken from the FILE statement of a cue file but constructed from the cue file name by replacing &quot;.cue&quot; by &quot;.bin&quot;. The cue file must have exactly one FILE statement. </p>
<p> Currently, following track modes are supported: MODE1/2048, MODE1/2352, MODE2/2336, MODE2/2352. The CATALOG, ISRC and POSTGAP statements are parsed but not evaluated, yet. </p>
<h2>SETTINGS</h2>
<p> Some of the command line options can be stored as settings at following locations. The files will be read on startup of <i>cdrdao</i> in that order: </p>
<p> 1. /etc/cdrdao.conf </p>
<p> 2. /etc/defaults/cdrdao </p>
<p> 3. /etc/default/cdrdao </p>
<p> 4. $HOME/.cdrdao </p>
<p> Command line options will overwrite the loaded settings. The settings file contains name &#8211; value pairs separated by a colon. String values must be enclosed by &quot;. The file is automatically written if the command line option <i>&#8211;save</i> is used but it is also possible to modify it manually. Following values are defined:</p>
<dl>
<dt>write_device</p>
<dd> Device used for operations <i>simulate, write, copy, blank, disk-info</i> and <i>unlock.</i> Corresponding option: <i>&#8211;device</i></p>
<dt>write_driver</p>
<dd> Driver (including driver options) that is used for operations <i>simulate, write, copy, blank, disk-info </i> and <i>unlock.</i> Corresponding option: <i>&#8211;driver</i></p>
<dt>write_speed</p>
<dd> Specifies writing speed. Corresponding option: &#8211;speed</p>
<dt>write_buffers</p>
<dd> Specifies fifo buffers used for recording. Corresponding option: &#8211;buffers</p>
<dt>read_device</p>
<dd> Device used for operations <i>read-toc, read-cd</i> and <i>copy.</i> Corresponding option: <i>&#8211;device</i> or <i>&#8211;source-device</i></p>
<dt>read_driver</p>
<dd> Driver (including driver options) used for operations <i>read-toc, read-cd</i> and <i>copy.</i> Corresponding option: <i>&#8211;driver</i> or <i>&#8211;source-driver</i></p>
<dt>read_paranoia_mode</p>
<dd> Paranoia mode used for operations <i>read-cd and copy.</i> Corresponding option: <i>&#8211;paranoia-mode</i></p>
<dt>cddb_server_list</p>
<dd> CDDB server list for <i>read-cddb.</i> Corresponding option: <i>&#8211;cddb-servers</i></p>
<dt>cddb_timeout</p>
<dd> CDDB connection timeout in seconds used by <i>read-cddb.</i> Corresponding option: <i>&#8211;cddb-timeout</i></p>
<dt>cddb_directory</p>
<dd> Local directory where fetched CDDB records will be stored, used by <i>read-cddb.</i> Corresponding option: <i>&#8211;cddb-directory</i></p>
<dt>tmp_file_dir</p>
<dd> Directory where temporary WAV files will be created from decoding MP3 and Ogg Vorbis files. Corresponding option: <i>&#8211;tmpdir</i></dl>
<h2>BUGS</h2>
<p> If the program is terminated during the write/simulation process used IPC resources may not be released. Use <a href="/docs/linux/man/8-ipcs/">ipcs</a>(8) and <a href="/docs/linux/man/8-ipcrm/">ipcrm</a>(8) to delete them.</p>
<h2>AUTHOR</h2>
<pre><code>
Andreas Mueller mueller[at] daneb.ping.de[DEFUNCT] Denis Leroy&lt;denis[at] poolshark.org&gt;
    Manuel Clos&lt;llanero[at] users.sourceforge.net&gt;
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gcdmaster/">gcdmaster</a></code>(1), <a href="/docs/linux/man/1-cdrecord/">cdrecord</a><code>(1), <a href="/docs/linux/man/1-cdda2wav/">cdda2wav</a></code>(1), <a href="/docs/linux/man/1-cdparanoia/">cdparanoia</a><code>(1), </code><a href="/docs/linux/man/1-sox/">sox</a><code>(1), <a href="/docs/linux/man/8-ipcs/">ipcs</a></code>(8), <code><a href="/docs/linux/man/8-ipcrm/">ipcrm</a></code>(8) </p>
<h2>Index</h2>
