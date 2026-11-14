---
title: "ezstream(1)"
name: "ezstream"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ezstream/"
description: "ezstream – source client for Icecast with external de-/encoder support"
---

<h2 class="name">NAME</h2>
<p> <code>ezstream</code> &#8211; source client for Icecast with external de-/encoder support </p>
<h2>SYNOPSIS</h2>
<p> -words [-<code>hmnqVv </code>&#8211;<code>c </code><i>configfile</i> ]<br />
 -words &#8211;<code>s</code> [<i>playlist</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The utility is a source client for the Icecast media streaming server. In its basic mode of operation, it streams media files and data from standard input Qq as-is &#8212; such as Ogg Vorbis, Ogg Theora and MP3 &#8212; to a server. It can also use various external decoders and encoders to re-encode from one format to another, and stream the result. The only requirement is that the external programs support writing to or reading from standard input, and can be used from the command line.</p>
<h3>Command line parameters</h3>
<dl>
<dt><code>-c </code><i>configfile</i></p>
<dd> Use the XML configuration in <i>configfile</i></p>
<dt><code>-h</code></p>
<dd> Print a summary of available command line parameters with short descriptions and exit.</p>
<dt><code>-m</code></p>
<dd> Disable all metadata updates and keep existing metadata in streams untouched.</p>
<dt><code>-n</code></p>
<dd> Normalize metadata strings by removing excess whitespaces.</p>
<dt><code>-q</code></p>
<dd> Be more quiet. Suppress the output that external programs send to standard error.</p>
<dt><code>-s </code>[<i>playlist</i> ]</p>
<dd> Run as a line-based shuffling utility. If no <i>playlist</i> argument is given, a list of media file names is read from standard input instead of an input file. After successfully reading the entire list, it is shuffled and printed to standard output, and will exit.</p>
<dt><code>-V</code></p>
<dd> Print the version number and exit.</p>
<dt><code>-v</code></p>
<dd> Produce more verbose output from <code>.</code> Use twice for even more verbose output.</dl>
<p> When the &#8211;<code>q</code> and &#8211;<code>v</code> parameters are provided simultaneously, an additional line of information about the currently streamed file &#8212; playlist position, approximate playing time and bit rate &#8212; is displayed.</p>
<h3>Runtime control</h3>
<p> On POSIX systems, offers limited runtime control via signals. By sending a signal to the ezstream process, e.g. with the <a href="/docs/linux/man/1-kill/">kill</a>(1) utility, a certain action will be triggered.</p>
<dl>
<dt><code>SIGHUP</code></p>
<dd> Rereads the playlist file after the track that is currently streamed. If the playlist is not to be shuffled, attempts to find the previously streamed file and continue with the one following it, or restarts from the beginning of the list otherwise.</p>
<dt><code>SIGUSR1</code></p>
<dd> Skips the currently playing track and moves on to the next in playlist mode, or restarts the current track when streaming a single file.</p>
<dt><code>SIGUSR2</code></p>
<dd> Triggers rereading of metadata for the stream by running the program or script specified in <code>&lt;metadata_progname/&gt;</code> (see below.) This is the only meaningful signal when streaming from standard input.</dl>
<h2>CONFIGURATION FILE SYNTAX</h2>
<p> The utility uses a simple XML configuration file format. It has a tree-like structure and is made up of <i>XML elements</i> Of all the possible XML features, only regular elements that contain text or other elements, and comments, appear in an configuration file. </p>
<p> Each element in the configuration file consists of a <i>start tag</i> its content and an <i>end tag</i> For example: </p>
<blockquote><p><tt>&lt;filename&gt;playlist.m3u&lt;/filename&gt;</tt></p></blockquote>
<blockquote><p><tt>&lt;!-- XML comments look like this. --&gt;</tt></p></blockquote>
<h2>XML CONFIGURATION</h2>
<p> In this section, each available element is listed and described. Note that for this purpose, elements are introduced in their short, i.e. empty form. In the configuration file, they need to be used as <i>start tag + content + end tag</i> like in the introductory example shown above.</p>
<h3>Root element</h3>
<dl>
<dt><code>&lt;ezstream&nbsp;<wbr>/&gt;</code></p>
<dd> (Mandatory.) The configuration file&#8217;s root element. It contains all other configuration elements.</dl>
<h3>Global configuration elements</h3>
<p> Each of the global configuration elements have the <code>&lt;ezstream/&gt;</code> element as their parent.</p>
<dl>
<dt><code>&lt;url&nbsp;<wbr>/&gt;</code></p>
<dd> (Mandatory.) Specifies the location and mount point of the Icecast server, to which the stream will be sent. The content must be of the form <a rel="nofollow" href="http://server:port/mountpoint">http://server:port/mountpoint</a> For example: </p>
<blockquote><p><tt>&lt;url&gt;<a rel="nofollow" href="http://example.com:8000/stream.ogg">http://example.com:8000/stream.ogg</a>&lt;/url&gt;</tt></p></blockquote>
<dt><code>&lt;sourceuser&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Sets the source username for authentication with the Icecast server. The default user Po usually &#8220;<code>source</code> &#8221; Pc is used if this element is not provided.</p>
<dt><code>&lt;sourcepassword&nbsp;<wbr>/&gt;</code></p>
<dd> (Mandatory.) Sets the source password for authentication with the Icecast server.</p>
<dt><code>&lt;format&nbsp;<wbr>/&gt;</code></p>
<dd> (Mandatory.) This element has two different meanings, depending on whether re-encoding is enabled or not. It specifies the <i>output format</i> of the stream if re-encoding is enabled. Otherwise, it specifies the <i>input format</i> of <code>all</code> input files. Recognized and supported values for output stream formats are <code>VORBIS</code> <code>MP3</code> and <code>THEORA</code> Other values will be ignored and cause to simply pass through the data, which may or may not work.</p>
<dt><code>&lt;filename&nbsp;<wbr>/&gt;</code></p>
<dd> (Mandatory.) Set the path and name of a single media file, a playlist, the name of an external program (see below) or the keyword stdin for streaming from standard input. Playlists are recognized by their filename extension and end with either <i>.m3u</i> or <i>.txt</i> </p>
<p> A playlist consists of filenames, one entry per line. Comments in playlists are introduced by a `<code>#</code> &#8216; sign at the beginning of a line and ignored by <code>.</code></p>
<dt><code>&lt;playlist_program&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set to <code>1</code> (one) to indicate that the file in <code>&lt;filename/&gt;</code> is actually an executable program or script. If set to <code>0</code> (zero) <code>&lt;filename/&gt;</code> content is assumed to be a media file, playlist file or the keyword stdin (the default) </p>
<p> See the <code>SCRIPTING</code> section for details on how the playlist program must behave.</p>
<dt><code>&lt;shuffle&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set to <code>1</code> (one) to randomly shuffle the entries of the playlist specified in <code>&lt;filename/&gt;</code> Files are played sequentially if set to <code>0</code> (zero) or when the <code>&lt;shuffle/&gt;</code> element is absent. This option will be ignored if <code>&lt;playlist_program/&gt;</code> is set to 1 (one.)</p>
<dt><code>&lt;metadata_progname&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set the path and name of an executable program or script that should be used by to set the metadata of the stream. The program is automatically queried when a new track is streamed, or whenever the <code>SIGUSR2</code> signal is received. </p>
<p> If the <code>&lt;metadata_progname/&gt;</code> element is present in the configuration, no attempts will be made to read metadata from files that are being streamed. If this behavior is not desired, it should be removed or commented out in the configuration file. </p>
<p> See the <code>SCRIPTING</code> section for details on how the metadata program must behave.</p>
<dt><code>&lt;metadata_format&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set the format of the string that should be used for the `<code>@M@</code> &#8216; placeholder when setting metadata with an external program or script via <code>&lt;metadata_progname/&gt;</code> </p>
<p> See the <code>METADATA</code> section for details on how metadata is handled by <code>.</code></p>
<dt><code>&lt;metadata_refreshinterval&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Configures the time (in seconds) inbetween additional metadata updates via <code>&lt;metadata_progname/&gt;</code> A value of 0 (zero) triggers updates as fast as possible, while a value of -1 (minus one) or the absence of this configuration element disables this feature.</p>
<dt><code>&lt;stream_once&nbsp;<wbr>/&gt;</code></p>
<dd> Set to <code>1</code> (one) in order to stream the content of <code>&lt;filename/&gt;</code> only once, and to <code>0</code> (zero) for continuous streaming (the default)</p>
<dt><code>&lt;reconnect_tries&nbsp;<wbr>/&gt;</code></p>
<dd> Set how many attempts should be made to reconnect to the Icecast server in case the connection is interrupted. The default is to try indefinitely, which is equal to setting this configuration option to <code>0</code> (zero)</p>
<dt><code>&lt;svrinfoname&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set the name of the broadcast. Informational only.</p>
<dt><code>&lt;svrinfourl&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set the URL of the web site associated with the broadcast. Informational only.</p>
<dt><code>&lt;svrinfogenre&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set the genre of the broadcast. Informational only, used for YP.</p>
<dt><code>&lt;svrinfodescription&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set the description of the broadcast. Informational only, used for YP.</p>
<dt><code>&lt;svrinfobitrate&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set the bit rate of the broadcast. This setting is also purely informational and only used for YP. The value is set by the user and not <code>,</code> and should match the bit rate of the stream.</p>
<dt><code>&lt;svrinfoquality&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set the quality setting of an Ogg Vorbis broadcast. Informational only and needs to be set by the user, used for YP.</p>
<dt><code>&lt;svrinfochannels&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set the number of audio channels in the broadcast, e.g. <code>1</code> (one) for mono or <code>2</code> for stereo. Informational only and needs to be set by the user, used for YP.</p>
<dt><code>&lt;svrinfosamplerate&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set the sample rate of the broadcast. Informational only and needs to be set by the user, used for YP.</p>
<dt><code>&lt;svrinfopublic&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Set to <code>1</code> (one) if the broadcast may be listed in a public YP directory. If set to <code>0</code> (zero) the Icecast server will not submit this stream to a YP directory, which is also the default if the <code>&lt;svrinfopublic/&gt;</code> element is absent.</p>
<dt><code>&lt;reencode&nbsp;<wbr>/&gt;</code></p>
<dd> (Optional.) Element that contains child elements, which specify if and how re-encoding should be done.</dl>
<h3>Re-encoding settings</h3>
<p> Each of the re-encoding configuration elements have the <code>&lt;reencode/&gt;</code> element as their parent.</p>
<dl>
<dt><code>&lt;enable&nbsp;<wbr>/&gt;</code></p>
<dd> Set to <code>1</code> (one) to enable re-encoding. If set to <code>0</code> (zero) no re-encoding will be done, which is also the default if the <code>&lt;enable/&gt;</code> element is absent.</p>
<dt><code>&lt;encdec&nbsp;<wbr>/&gt;</code></p>
<dd> Element that contains child elements, which specify how to decode and encode a certain media file format for streaming. Each format is described by a separate <code>&lt;encdec/&gt;</code> element.</dl>
<h3>Decoder/Encoder settings</h3>
<p> Each of the decoder/encoder configuration elements have the <code>&lt;encdec/&gt;</code> element as their parent.</p>
<dl>
<dt><code>&lt;format&nbsp;<wbr>/&gt;</code></p>
<dd> This element is used by to find the appropriate encoder for the output stream format specified in the <code>&lt;format/&gt;</code> element inside the global configuration. For consistency reasons, it is recommended that this element is always supplied, even for currently unsupported output formats, with content such as <code>VORBIS</code> <code>MP3</code> <code>THEORA</code> <code>FLAC</code> et cetera.</p>
<dt><code>&lt;match&nbsp;<wbr>/&gt;</code></p>
<dd> Set the filename extension used to identify a given media file format. This allows to find the appropriate decoder for a given file. Should be set to <i>.mp3</i> for MP3, <i>.flac</i> for FLAC, <i>.ogg</i> for Ogg Vorbis, and so on.</p>
<dt><code>&lt;decode&nbsp;<wbr>/&gt;</code></p>
<dd> Set the command to decode the specified media file format to raw data and send it to standard output. During runtime, the placeholder `<code>@T@</code> &#8216; is replaced with the name of the media file, as it is specified in the <code>&lt;filename/&gt;</code> element or contained in a playlist file. It should always be enclosed in quotes, to prevent problems with filenames that contain whitespaces. </p>
<p> Metadata placeholders can be used in the <code>&lt;decode/&gt;</code> element as well, for combined de-/encoder programs that produce data that can be streamed. See the <code>METADATA</code> section for details on how metadata is handled by <code>.</code> </p>
<p> For example, to decode Ogg Vorbis files using the <code>oggdec</code> utility: </p>
<blockquote><p><tt>&lt;decode&gt;oggdec -R -o - @T@&lt;/decode&gt;</tt></p></blockquote>
<dt><code>&lt;encode&nbsp;<wbr>/&gt;</code></p>
<dd> Set the command to encode raw data, received from standard input, to the specified stream format. </p>
<p> Metadata placeholders can be used in the <code>&lt;encode/&gt;</code> element. For details about using metadata in <code>,</code> see below in the <code>METADATA</code> section. </p>
<p> For example, to encode an Ogg Vorbis stream using the quality setting 1.5 with the <code>oggenc</code> utility: </p>
<blockquote><p><tt>&lt;encode&gt;oggenc -r -q 1.5 -t @M@ -&lt;/encode&gt;</tt></p></blockquote>
</dl>
<h2>SCRIPTING</h2>
<p> The utility provides hooks for externally controlled playlist and metadata management. This is done by running external programs or scripts that need to behave in ways explained here.</p>
<h3>Common Rules</h3>
<dl>
<dt><code>The program must be an executable file.</code></p>
<dd>
<dt><code>The program must write one line to standard output and exit.</code></p>
<dd>
<dt><code>The program must not require arbitrary command line options to function.</code></p>
<dd> A wrapper script must be used if there is no other way.</dl>
<h3>Playlist Programs</h3>
<dl>
<dt><code>The program must return only filenames, with one filename per execution.</code></p>
<dd>
<dt><code>The program should not return an empty line unless</code></p>
<dd> is supposed to know that the end of the playlist has been reached. This is significant when the <code>&lt;stream_once/&gt;</code> option is enabled.</dl>
<h3>Metadata Programs</h3>
<dl>
<dt><code>The program must not return anything (just a newline character is okay) if it</code></p>
<dd> is called by with a command line parameter that the program does not support.</p>
<dt><code>When called without command line parameters, the program should return a</code></p>
<dd> complete string that should be used for metadata.</p>
<dt><code>When called with the command line parameter</code></p>
<dd> Qq Li artist , the program should return only the artist information of the metadata. (Optional.)</p>
<dt><code>When called with the command line parameter</code></p>
<dd> Qq Li title , the program should return only the title information of the metadata. (Optional.)</p>
<dt><code>The supplied metadata must be encoded in UTF-8.</code></p>
<dd></dl>
<h2>METADATA</h2>
<p> The main tool for handling metadata with is placeholders in decoder and encoder commands that are replaced with real content during runtime. </p>
<p> <i>Note:</i> To prevent malicious shell script in metadata (such as artist and title tags) from being executed, all metadata content is automatically enclosed in single quotes, with escaped single quote and backslash characters inbetween. To prevent this from causing unwanted side-effects (or introducting security risk) placeholders <i>must not</i> be quoted any further.</p>
<h3>Metadata Placeholders</h3>
<dl>
<dt><code>@T@</code></p>
<dd> Replaced with the media file name. Required in <code>&lt;decode/&gt;</code> and is available in <code>&lt;metadata_format/&gt;</code></p>
<dt><code>@M@</code></p>
<dd> Replaced with a metadata string. See below for a detailed explanation. Available in <code>&lt;decode/&gt;</code> and <code>&lt;encode/&gt;</code></p>
<dt><code>@a@</code></p>
<dd> Replaced with the artist information. Available in <code>&lt;decode/&gt;</code> <code>&lt;encode/&gt;</code> and <code>&lt;metadata_format/&gt;</code></p>
<dt><code>@t@</code></p>
<dd> Replaced with the title information. Available in <code>&lt;decode/&gt;</code> <code>&lt;encode/&gt;</code> and <code>&lt;metadata_format/&gt;</code></p>
<dt><code>@s@</code></p>
<dd> Replaced with the string returned by <code>&lt;metadata_progname/&gt;</code> when called without any command line parameters. Available only in <code>&lt;metadata_format/&gt;</code></dl>
<h3>The @M@ Placeholder</h3>
<p> While all other placeholders are simply replaced with whatever data they are associated with, `<code>@M@</code> &#8216; is context-sensitive. The logic used by is the following: </p>
<blockquote>
<pre>
If ('@M@ is present')
    If ('&lt;metadata_progname/&gt;' AND '&lt;metadata_format/&gt;')
        Replace with format string result.
    Else
        If (NOT '&lt;metadata_progname/&gt;' AND '@t@ is present')
            Replace with empty string.
        else
            Replace with generated metadata string.
        Endif
    Endif
Endif
</pre>
</blockquote>
<p> The generated metadata string for `<code>@M@</code> &#8216; is of the format &#8220;<i>Artist &#8211; Title</i> &#8221; if both artist and title information is available. If one of the two is missing, the available one is displayed without a leading or trailing dash, e.g. just &#8220;<i>Artist</i> &#8221; If neither artist nor title are available, the name of the media file &#8212; without its file extension &#8212; is used.</p>
<h3>Metadata Caveats</h3>
<p> It is possible to generate strange results with odd combinations of placeholders, external metadata programs and updates during runtime via <code>SIGUSR2</code> If things start to become just confusing, simplify. </p>
<p> Metadata updates during runtime are done with a relatively broken feature of libshout. Additional metadata information that is already present in the stream sent via is usually destroyed and replaced with the new data. It is not possible to properly discern between artist and title information, which means that anything set with the <code>SIGUSR2</code> feature will continue to end up entirely in the Qq Em Title field of a stream. </p>
<p> Of all possible Ogg-based streams, only Ogg Vorbis can have its metadata manipulated by Icecast. Any attempt of to update other Ogg metadata is actually a no-op. </p>
<p> While tries to do its best with relaying metadata accurately to Icecast, and subsequently the listeners, different codesets and locales can pose a problem. Especially when streaming MP3 files, it may help to explicitly set a codeset to work with via the <code>LC_CTYPE</code> environment variable, as assumes ID3v1 tags to be in the user&#8217;s current locale. Note that, even though support for different locales is provided by <code>,</code> Icecast itself and the listening clients also have a say in the matter. The only way to ensure consistent results with metadata in non-Ogg streams is to use the characters available in the ISO-8859-1 codeset. </p>
<p> External encoders may put additional, and possibly artificial, restrictions on valid characters in metadata.</p>
<h2>FILES</h2>
<dl>
<dt><code>/usr/share/examples/ezstream </code></p>
<dd> Directory containing example configuration files for various uses of <code>,</code> as well as example playlist and metadata scripts.</dl>
<h2>SEE ALSO</h2>
<p> ezstream-file.sh1</p>
<h2>AUTHORS</h2>
<p> was written by: </p>
<p> An Ed Zaleski Aq oddsock [at] oddsock.org An Moritz Grimm Aq mgrimm [at] mrsserver.net </p>
<p> An -nosplit This manual was written by An Moritz Grimm . </p>
<h2>Index</h2>
