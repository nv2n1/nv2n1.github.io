---
title: "gmediaserver(1)"
name: "gmediaserver"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gmediaserver/"
description: "GMediaServer – A UPnP compatible media server"
---

<h2>NAME</h2>
<p> GMediaServer &#8211; A UPnP compatible media server</p>
<h2>SYNOPSIS</h2>
<p> <code>gmediaserver</code> [<i>OPTIONS</i>]&#8230; <i>DIRECTORIES</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Run the UPnP compatible media server. The directories arguments specify where audio files are located. </p>
<p> <code>GMediaServer</code> is a UPnP music media server. It implements the server component that provides UPnP media devices with information on available audio files. GMediaServer uses the built-in http server of libupnp to stream the audio files to clients. </p>
<p> When the main process receives the <code>USR1</code> signal, all directories specified on the command line will be rescanned. This functionality is currently quite crude in that all files are rescanned even if they were not changed.</p>
<h2>OPTIONS</h2>
<p> This program follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;).</p>
<dl>
<dt><code>&#8211;friendly-name</code>=<i>NAME</i></p>
<dd> Set display name for media server.</p>
<dt><code>&#8211;disable-tags</code></p>
<dd> Do not scan files for tags.</p>
<dt><code>&#8211;fs-charset</code>=<i>CHARSET</i></p>
<dd> Specify character set used in file names. If the environment variable `G_BROKEN_FILENAMES&#8217; (1) is set, this is if possible identified automaticly from the current locale (usually the environment variable `LC_CTYPE&#8217; affects this). Otherwise UTF-8 is assumed. Use this option to specify character set manually. </p>
<p> Run `iconv &#8211;list&#8217; for a list of accepted character encoding names.</p>
<dt><code>&#8211;device-charset</code>=<i>CHARSET</i></p>
<dd> Specify character set used in the data passed to the control point (the player device). If this option is not specified, no translation will occur. </p>
<p> Run `iconv &#8211;list&#8217; for a list of accepted character encoding set names.</p>
<dt><code>&#8211;log-charset</code>=<i>CHARSET</i></p>
<dd> Specify character set used in messages printed to standard out and to the log file (if applicable). If this option is not specified, it is if possible identified automaticly from the current locale.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code>[=<i>LEVEL</i>]</p>
<dd> Set verbosity level (0-4).</p>
<dt><code>&#8211;pid-file</code>=<i>FILE</i></p>
<dd> Write pid to FILE when up and running.</p>
<dt><code>-i</code>, <code>&#8211;interface</code>=<i>NAME</i></p>
<dd> Listen on a specific interface. NAME can be either an IP address (IPv4) or the name of a network device.</p>
<dt><code>-p</code>, <code>&#8211;port</code>=<i>PORT</i></p>
<dd> Listen on a specific port.</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>LOGFILE</i></p>
<dd> File for logging.</p>
<dt><code>-b</code>, <code>&#8211;background</code></p>
<dd> Go to background (detach).</p>
<dt><code>&#8211;no-timestamp</code></p>
<dd> Do not prepend timestamp to log entries. See <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for description of the timestamp format.</p>
<dt><code>&#8211;timestamp</code>[=<i>FORMAT</i>]</p>
<dd> Prepend timestamp with optional time format.</p>
<dt><code>&#8211;profile</code>=<i>NAME</i></p>
<dd> Specify which profile to use. Profiles control what settings are enabled for a certain control point (the player device). See <code>PROFILES</code> below for a list of valid values for &#8211;profile. The default is &quot;generic&quot;.</p>
<dt><code>&#8211;expire-time</code>=<i>SECONDS</i></p>
<dd> Set UPnP advertisement expire time. This may be necessary for some devices. The default is 100 seconds.</p>
<dt><code>&#8211;file-types</code>=<i>TYPE</i>[,..]</p>
<dd> Specify which types of files are accepted by the control point. The argument is a comma separated list of accepted types. File types are identified by contents and not file name (i.e. the extension). See <code>FILE TYPES</code> below for a list of valid types for &#8211;file-types. The default is &quot;mp3,wma,m3u,pls&quot;.</p>
<dt><code>&#8211;help</code></p>
<dd> Display this help and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version information and exit.</dl>
<h2>PROFILES</h2>
<p> The following values are valid for &#8211;profile:</p>
<dl>
<dt><code>mp101</code></p>
<dd> Netgear MP101. Implies &#8211;file-types=mp3,wma,m3u,pls.</p>
<dt><code>dms1</code></p>
<dd> Omnify DMS1. Implies &#8211;expire-time=600 &#8211;file-types=mp3,wma,m3u,pls.</p>
<dt><code>generic</code></p>
<dd> All other devices. Implies no custom settings.</dl>
<h2>FILE TYPES</h2>
<p> The following types can be specified for &#8211;file-types:</p>
<dl>
<dt><code>mp3</code></p>
<dd> The regular MP3 files, or to be more specific `MPEG ADTS, layer III, v1&#8242;. At the moment this does also include MP3 files beginning with an ID3 tag.</p>
<dt><code>wma</code></p>
<dd> `Windows Media Audio&#8217; data encapsulated in Microsoft ASF files.</p>
<dt><code>wav</code></p>
<dd> Wave sound data encapsulated in RIFF files.</p>
<dt><code>m4a</code></p>
<dd> `iTunes AAC-LC&#8217; data encapsulated in an ISO Media MPEG v4 system file.</p>
<dt><code>ogg</code></p>
<dd> Vorbis audio data encapsulated in an Ogg file.</p>
<dt><code>pls</code></p>
<dd> A playlist format used by Winamp and other programs.</p>
<dt><code>m3u</code></p>
<dd> Simple and extended M3U playlists used by Winamp and other programs. Extended M3U playlists start with `#EXTM3U&#8217;.</p>
<dt><code>unknown</code></p>
<dd> Unidentified files (all other). Normally these files are not served, but when unknown is included in the file types list they will be.</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;<i>oskar [at] osk.mine.nu</i>&gt;.</p>
<h2>AUTHOR</h2>
<p> GMediaServer was written by Oskar Liljeblad &lt;oskar [at] osk.mine.nu&gt;.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-kill/">kill</a>(2)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005, 2006 Oskar Liljeblad </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
