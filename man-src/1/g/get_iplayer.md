---
title: "get_iplayer(1)"
name: "get_iplayer"
section: "1"
letter: "g"
url: "/docs/linux/man/1-get_iplayer/"
description: "get_iplayer – Stream Recording tool and PVR for BBC iPlayer, BBC Podcasts and more"
---

<h2>NAME</h2>
<p> get_iplayer &#8211; Stream Recording tool and PVR for BBC iPlayer, BBC Podcasts and more</p>
<h2>SYNOPSIS</h2>
<p> <code>get_iplayer</code> [&lt;options&gt;] [&lt;regex|index&gt; &#8230;] </p>
<p> <code>get_iplayer</code> <code>&#8211;get</code> [&lt;options&gt;] &lt;regex|index&gt; &#8230;<br />
 <code>get_iplayer</code> &lt;url&gt; <code>&#8211;type</code>=&lt;type&gt; [&lt;options&gt;] </p>
<p> <code>get_iplayer</code> &lt;pid|url&gt; [<code>&#8211;type</code>=&lt;type&gt; &lt;options&gt;] </p>
<p> <code>get_iplayer</code> <code>&#8211;stream</code> [&lt;options&gt;] &lt;regex|index&gt; | mplayer <code>-cache</code> 3072 &#8211; </p>
<p> <code>get_iplayer</code> <code>&#8211;stream</code> [&lt;options&gt;] <code>&#8211;type</code>=&lt;type&gt; &lt;pid|url&gt; | mplayer <code>-cache</code> 3072 &#8211; </p>
<p> <code>get_iplayer</code> <code>&#8211;stream</code> [&lt;options&gt;] <code>&#8211;type</code>=livetv,liveradio &lt;regex|index&gt; <code>&#8211;player</code>=&quot;mplayer -cache 128 -&quot; </p>
<p> <code>get_iplayer</code> <code>&#8211;refresh</code></p>
<h2>DESCRIPTION</h2>
<p> <code>get_iplayer</code> lists, searches and records BBC iPlayer TV/Radio, BBC Podcast programmes. Other 3rd-Party plugins may be available. </p>
<p> <code>get_iplayer</code> has three modes: recording a complete programme for later playback, streaming a programme directly to a playback application, such as mplayer; and as a Personal Video Recorder (PVR), subscribing to search terms and recording programmes automatically. It can also stream or record live BBC iPlayer output </p>
<p> If given no arguments, <code>get_iplayer</code> updates and displays the list of currently available programmes. Each available programme has a numerical identifier, <code>pid</code>. <code>get_iplayer</code> utilises the <code>rtmpdump</code> tool to record BBC iPlayer programmes from RTMP flash streams at various qualities. </p>
<p> In PVR mode, <code>get_iplayer</code> can be called from cron to record programmes to a schedule.</p>
<h2>OPTIONS</h2>
<h3>Search Options:</h3>
<dl>
<dt><code>&#8211;before</dt>
<dd> Limit search to programmes added to the cache before N hours ago</dd>
<dt>&#8211;category &lt;string&gt;</dt>
<dd> Narrow search to matched categories (regex or comma separated values). Supported only for podcasts (not tv or radio programmes).</dd>
<dt>&#8211;channel &lt;string&gt;</dt>
<dd> Narrow search to matched channel(s) (regex or comma separated values)</dd>
<dt>&#8211;exclude &lt;string&gt;</dt>
<dd> Narrow search to exclude matched programme names (regex or comma separated values)</dd>
<dt>&#8211;exclude-category &lt;string&gt;</dt>
<dd> Narrow search to exclude matched categories (regex or comma separated values). Supported only for podcasts (not tv or radio programmes).</dd>
<dt>&#8211;exclude-channel &lt;string&gt;</dt>
<dd> Narrow search to exclude matched channel(s) (regex or comma separated values)</dd>
<dt>&#8211;fields &lt;field1&gt;,&lt;field2&gt;,..</dt>
<dd> Searches only in the specified comma separated fields</dd>
<dt>&#8211;future</dt>
<dd> Additionally search future programme schedule if it has been indexed (refresh cache with: &#8211;refresh &#8211;refresh-future).</dd>
<dt>&#8211;history</dt>
<dd> Search/show recordings history</dd>
<dt>&#8211;long, -l</dt>
<dd> Additionally search in programme descriptions and episode names (same as &#8211;fields=name,episode,desc )</dd>
<dt>&#8211;search &lt;search term&gt;</dt>
<dd> GetOpt compliant way of specifying search args</dd>
<dt>&#8211;since</dt>
<dd> Limit search to programmes added to the cache in the last N hours</dd>
<dt>&#8211;type &lt;type&gt;</dt>
<dd> Only search in these types of programmes: liveradio,livetv,radio,tv,all (tv is default)</dd>
<dt>&#8211;versions &lt;versions&gt;</dt>
<dd> Version of programme to search or record. List is processed from left to right and first version found is downloaded. Example: &#8216;&#8211;versions signed,audiodescribed,default&#8217; will prefer signed and audiodescribed programmes if available. Default: &#8216;default,signed,audiodescribed&#8217;</dd></dl>
<p> </code></p>
<h3>Display Options:</h3>
<dl>
<dt><code>&#8211;conditions</dt>
<dd> Shows GPLv3 conditions</dd>
<dt>&#8211;debug</dt>
<dd> Debug output</dd>
<dt>&#8211;dump-options</dt>
<dd> Dumps all options with their internal option key names</dd>
<dt>&#8211;help, -h</dt>
<dd> Intermediate help text</dd>
<dt>&#8211;helpbasic, &#8211;usage</dt>
<dd> Basic help text</dd>
<dt>&#8211;helplong</dt>
<dd> Advanced help text</dd>
<dt>&#8211;hide</dt>
<dd> Hide previously recorded programmes</dd>
<dt>&#8211;info, -i</dt>
<dd> Show full programme metadata and availability of modes and subtitles (max 50 matches)</dd>
<dt>&#8211;list &lt;categories|channel&gt;</dt>
<dd> Show a list of available categories/channels for the selected type and exit</dd>
<dt>&#8211;listformat &lt;format&gt;</dt>
<dd> Display programme data based on a user-defined format string (such as &lt;pid&gt;, &lt;name&gt; etc)</dd>
<dt>&#8211;listplugins</dt>
<dd> Display a list of currently available plugins or programme types</dd>
<dt>&#8211;long, -l</dt>
<dd> Show long programme info</dd>
<dt>&#8211;manpage &lt;file&gt;</dt>
<dd> Create man page based on current help text</dd>
<dt>&#8211;nocopyright</dt>
<dd> Don&#8217;t display copyright header</dd>
<dt>&#8211;page &lt;number&gt;</dt>
<dd> Page number to display for multipage output</dd>
<dt>&#8211;pagesize &lt;number&gt;</dt>
<dd> Number of matches displayed on a page for multipage output</dd>
<dt>&#8211;quiet, -q</dt>
<dd> Reduce logging output</dd>
<dt>&#8211;series</dt>
<dd> Display Programme series names only with number of episodes</dd>
<dt>&#8211;show-cache-age</dt>
<dd> Displays the age of the selected programme caches then exit</dd>
<dt>&#8211;show-options</dt>
<dd> Shows options which are set and where they are defined</dd>
<dt>&#8211;silent</dt>
<dd> No logging output except PVR download report. Cannot be saved in preferences or PVR searches.</dd>
<dt>&#8211;sort &lt;fieldname&gt;</dt>
<dd> Field to use to sort displayed matches</dd>
<dt>&#8211;sortreverse</dt>
<dd> Reverse order of sorted matches</dd>
<dt>&#8211;streaminfo</dt>
<dd> Returns all of the media stream urls of the programme(s)</dd>
<dt>&#8211;terse</dt>
<dd> Only show terse programme info (does not affect searching)</dd>
<dt>&#8211;tree</dt>
<dd> Display Programme listings in a tree view</dd>
<dt>&#8211;verbose, -v</dt>
<dd> Verbose</dd>
<dt>&#8211;warranty</dt>
<dd> Displays warranty section of GPLv3</dd>
<dt>-V</dt>
<dd> Show get_iplayer version and exit.</dd></dl>
<p> </code></p>
<h3>Recording Options:</h3>
<dl>
<dt><code>&#8211;attempts &lt;number&gt;</dt>
<dd> Number of attempts to make or resume a failed connection. &#8211;attempts is applied per-stream, per-mode. TV modes typically have two streams available.</dd>
<dt>&#8211;bandwidth</dt>
<dd> In radio realaudio mode specify the link bandwidth in bps for rtsp streaming (default 512000)</dd>
<dt>&#8211;check-duration</dt>
<dd> Print message showing recorded duration, expected duration and difference between them.</dd>
<dt>&#8211;ddl-radio-opts &lt;options&gt;</dt>
<dd> Add custom options to ffmpeg DDL download re-muxing for radio</dd>
<dt>&#8211;exclude-supplier &lt;suppliers&gt;</dt>
<dd> Comma-delimited list of media stream suppliers to skip. Possible values: akamai,limelight,level3,bidi</dd>
<dt>&#8211;ffmpeg-liveradio-opts &lt;options&gt;</dt>
<dd> Add custom options to ffmpeg re-muxing for liveradio</dd>
<dt>&#8211;ffmpeg-livetv-opts &lt;options&gt;</dt>
<dd> Add custom options to ffmpeg re-muxing for livetv</dd>
<dt>&#8211;ffmpeg-radio-opts &lt;options&gt;</dt>
<dd> Add custom options to ffmpeg re-muxing for radio</dd>
<dt>&#8211;ffmpeg-tv-opts &lt;options&gt;</dt>
<dd> Add custom options to ffmpeg re-muxing for tv</dd>
<dt>&#8211;force</dt>
<dd> Ignore programme history (unsets &#8211;hide option also). Forces a script update if used with -u</dd>
<dt>&#8211;get, -g</dt>
<dd> Start recording matching programmes. Search terms required unless &#8211;pid specified. Use &#8211;search=.* to force download of all available programmes.</dd>
<dt>&#8211;hash</dt>
<dd> Show recording progress as hashes</dd>
<dt>&#8211;hls-liveradio-opts &lt;options&gt;</dt>
<dd> Add custom options to ffmpeg HLS download re-muxing for liveradio</dd>
<dt>&#8211;hls-livetv-opts &lt;options&gt;</dt>
<dd> Add custom options to ffmpeg HLS download encoding for livetv</dd>
<dt>&#8211;hls-radio-opts &lt;options&gt;</dt>
<dd> Add custom options to ffmpeg HLS download re-muxing for radio</dd>
<dt>&#8211;hls-tv-opts &lt;options&gt;</dt>
<dd> Add custom options to ffmpeg HLS download re-muxing for tv</dd>
<dt>&#8211;liveradio-intl</dt>
<dd> Force use of hard-coded international streams for HLS live radio. Ignored for World Service</dd>
<dt>&#8211;liveradio-uk</dt>
<dd> Force use of hard-coded UK streams for HLS live radio (overrides &#8211;liveradio-intl). Ignored for World Service</dd>
<dt>&#8211;liveradiomode &lt;mode&gt;,&lt;mode&gt;,..</dt>
<dd> Live Radio recording modes: hlsaachigh,hlsaacstd,hlsaacmed,hlsaaclow,shoutcastmp3std,shoutcastaachigh(R3 only, UK only). Shortcuts: default,good,better(=default),best,hls. (&#8216;default&#8217;=hlsaachigh,hlsaacstd,hlsaacmed,hlsaaclow)</dd>
<dt>&#8211;livetv-uk</dt>
<dd> Force use of hard-coded UK streams for HLS live tv</dd>
<dt>&#8211;livetvmode &lt;mode&gt;,&lt;mode&gt;,&#8230;</dt>
<dd> Live TV recording modes: hlshd,hlssd,hlsvhigh,hlshigh,hlsstd,hlslow. Shortcuts: default,good,better(=default),vbetter,best,hls. (&#8216;default&#8217;=hlsvhigh,hlshigh,hlsstd,hlslow)</dd>
<dt>&#8211;mediaselector &lt;identifier&gt;</dt>
<dd> Identifier of mediaselector API to use when searching for media streams. One of: 4,5 Default: 5</dd>
<dt>&#8211;metadata-only</dt>
<dd> Create specified metadata info file without any recording or streaming (can also be used with thumbnail option).</dd>
<dt>&#8211;mmsnothread</dt>
<dd> Disable parallel threaded recording for mms</dd>
<dt>&#8211;modes &lt;mode&gt;,&lt;mode&gt;,&#8230;</dt>
<dd> Recording modes. See &#8211;tvmode and &#8211;radiomode for available modes and defaults. Shortcuts: default,good,better(=default),best. Use &#8211;modes=best to select highest quality available (incl. HD TV).</dd>
<dt>&#8211;multimode</dt>
<dd> Allow the recording of more than one mode for the same programme &#8211; WARNING: will record all specified/default modes!!</dd>
<dt>&#8211;no-proxy</dt>
<dd> Ignore &#8211;proxy setting in preferences</dd>
<dt>&#8211;overwrite</dt>
<dd> Overwrite recordings if they already exist</dd>
<dt>&#8211;partial-proxy</dt>
<dd> Only uses web proxy where absolutely required (try this extra option if your proxy fails). If specified, value of http_proxy environment variable (if any) in parent process is retained and passed to child processes.</dd>
<dt>&#8211;pid &lt;pid&gt;</dt>
<dd> Record an arbitrary pid that does not necessarily appear in the index.</dd>
<dt>&#8211;pid-recursive</dt>
<dd> When used with &#8211;pid record all the embedded pids if the pid is a series or brand pid.</dd>
<dt>&#8211;proxy, -p &lt;url&gt;</dt>
<dd> Web proxy URL e.g. &#8216;<a rel="nofollow" href="http://USERNAME:PASSWORD@SERVER:PORT'">http://USERNAME:PASSWORD@SERVER:PORT&#8217;</a> or &#8216;<a href="http://SERVER:PORT'.">http://SERVER:PORT&#8217;.</a> Sets http_proxy environment variable for child processes (e.g., ffmpeg) unless &#8211;partial-proxy is specified.</dd>
<dt>&#8211;radiomode &lt;mode&gt;,&lt;mode&gt;,&#8230;</dt>
<dd> Radio recording modes: flashaachigh,flashaacstd,flashaudio,flashaaclow,wma. Shortcuts: default,good,better(=default),best,rtmp,flash,flashaac. (&#8216;default&#8217;=flashaachigh,flashaacstd,flashaudio,flashaaclow)</dd>
<dt>&#8211;raw</dt>
<dd> Don&#8217;t transcode or change the recording/stream in any way (i.e. radio/realaudio, rtmp/flv)</dd>
<dt>&#8211;rtmp-liveradio-opts &lt;options&gt;</dt>
<dd> Add custom options to rtmpdump for liveradio</dd>
<dt>&#8211;rtmp-livetv-opts &lt;options&gt;</dt>
<dd> Add custom options to rtmpdump for livetv</dd>
<dt>&#8211;rtmp-radio-opts &lt;options&gt;</dt>
<dd> Add custom options to rtmpdump for radio</dd>
<dt>&#8211;rtmp-tv-opts &lt;options&gt;</dt>
<dd> Add custom options to rtmpdump for tv</dd>
<dt>&#8211;rtmpport &lt;port&gt;</dt>
<dd> Override the RTMP port (e.g. 443)</dd>
<dt>&#8211;shoutcast-liveradio-opts &lt;options&gt;</dt>
<dd> Add custom options to ffmpeg Shoutcast download re-muxing for liveradio</dd>
<dt>&#8211;start &lt;secs|hh:mm:ss&gt;</dt>
<dd> Recording/streaming start offset (rtmp and realaudio only)</dd>
<dt>&#8211;stop &lt;secs|hh:mm:ss&gt;</dt>
<dd> Recording/streaming stop offset (can be used to limit live rtmp recording length) rtmp and realaudio only</dd>
<dt>&#8211;suboffset &lt;offset&gt;</dt>
<dd> Offset the subtitle timestamps by the specified number of milliseconds</dd>
<dt>&#8211;subsfmt &lt;format&gt;</dt>
<dd> Subtitles format. One of: default, compact. Default: &#8216;default&#8217;</dd>
<dt>&#8211;subsraw</dt>
<dd> Additionally save the raw subtitles file</dd>
<dt>&#8211;subtitles</dt>
<dd> Download subtitles into srt/SubRip format if available and supported</dd>
<dt>&#8211;subtitles-only</dt>
<dd> Only download the subtitles, not the programme</dd>
<dt>&#8211;subtitles-required</dt>
<dd> Do not download TV programme if subtitles are not available.</dd>
<dt>&#8211;swfurl &lt;URL&gt;</dt>
<dd> URL of Flash player used by rtmpdump for verification. Only use if default Flash player URL is not working.</dd>
<dt>&#8211;tag-only</dt>
<dd> Only update the programme tag and not download the programme (can also be used with &#8211;history)</dd>
<dt>&#8211;test, -t</dt>
<dd> Test only &#8211; no recording (will show programme type)</dd>
<dt>&#8211;thumb</dt>
<dd> Download Thumbnail image if available</dd>
<dt>&#8211;thumbnail-only</dt>
<dd> Only Download Thumbnail image if available, not the programme</dd>
<dt>&#8211;tvmode &lt;mode&gt;,&lt;mode&gt;,&#8230;</dt>
<dd> TV recording modes: flashhd,flashvhigh,flashhigh,flashstd,flashnormal,flashlow. Shortcuts: default,good,better(=default),best,rtmp,flash. (Use &#8216;best&#8217; for HD TV. &#8216;default&#8217;=flashvhigh,flashhigh,flashstd,flashnormal,flashlow)</dd>
<dt>&#8211;url &quot;&lt;url&gt;&quot;</dt>
<dd> Record the embedded media player in the specified URL. Use with &#8211;type=&lt;type&gt;.</dd>
<dt>&#8211;wav</dt>
<dd> In radio realaudio mode output as wav and don&#8217;t transcode to mp3</dd></dl>
<p> </code></p>
<h3>Output Options:</h3>
<dl>
<dt><code>&#8211;aactomp3</dt>
<dd> Transcode AAC audio to MP3 with ffmpeg/avconv (CBR 128k unless &#8211;mp3vbr is specified). Applied only to radio programmes. (Synonyms: &#8211;mp3)</dd>
<dt>&#8211;avi</dt>
<dd> Output video in AVI container instead of MP4. There is no metadata tagging support for AVI output.</dd>
<dt>&#8211;command, -c &lt;command&gt;</dt>
<dd> Run user command after successful recording using args such as &lt;pid&gt;, &lt;name&gt; etc</dd>
<dt>&#8211;email &lt;address&gt;</dt>
<dd> Email HTML index of matching programmes to specified address</dd>
<dt>&#8211;email-password &lt;password&gt;</dt>
<dd> Email password</dd>
<dt>&#8211;email-port &lt;port number&gt;</dt>
<dd> Email port number (default: appropriate port for &#8211;email-security)</dd>
<dt>&#8211;email-security &lt;TLS|SSL&gt;</dt>
<dd> Email security TLS, SSL (default: none)</dd>
<dt>&#8211;email-sender &lt;address&gt;</dt>
<dd> Optional email sender address</dd>
<dt>&#8211;email-smtp &lt;hostname&gt;</dt>
<dd> SMTP server IP address to use to send email (default: localhost)</dd>
<dt>&#8211;email-user &lt;username&gt;</dt>
<dd> Email username</dd>
<dt>&#8211;fatfilename</dt>
<dd> Remove FAT forbidden characters in file and directory names. Always applied on Windows. Overrides &#8211;punctuation.</dd>
<dt>&#8211;file-prefix &lt;format&gt;</dt>
<dd> The filename prefix (excluding dir and extension) using formatting fields. e.g. &#8216;&lt;name&gt;-&lt;episode&gt;-&lt;pid&gt;&#8217;</dd>
<dt>&#8211;fxd &lt;file&gt;</dt>
<dd> Create Freevo FXD XML of matching programmes in specified file</dd>
<dt>&#8211;hfsfilename</dt>
<dd> Remove colons in file and directory names. Prevents OS X Finder displaying colon as forward slash. Always applied on OS X. Overrides &#8211;punctuation.</dd>
<dt>&#8211;html &lt;file&gt;</dt>
<dd> Create basic HTML index of matching programmes in specified file</dd>
<dt>&#8211;isodate</dt>
<dd> Use ISO8601 dates (YYYY-MM-DD) in filenames and subdirectory paths</dd>
<dt>&#8211;keep-all</dt>
<dd> Keep whitespace, all possible punctuation and non-ASCII characters in file and directory names. Shortcut for: &#8211;whitespace &#8211;non-ascii &#8211;punctuation.</dd>
<dt>&#8211;metadata &lt;type&gt;</dt>
<dd> Create metadata info file after recording. Valid types are: xbmc (or kodi), xbmc_movie (or kodi_movie), freevo, generic</dd>
<dt>&#8211;mkv</dt>
<dd> Output video in MKV container instead of MP4. There is no metadata tagging support for MKV output.</dd>
<dt>&#8211;mp3vbr</dt>
<dd> Set LAME VBR mode to N (0 to 9) for AAC transcoding. 0 = target bitrate 245 Kbit/s, 9 = target bitrate 65 Kbit/s (requires &#8211;aactomp3). Applied only to radio programmes.</dd>
<dt>&#8211;mythtv &lt;file&gt;</dt>
<dd> Create Mythtv streams XML of matching programmes in specified file</dd>
<dt>&#8211;non-ascii, &#8211;na</dt>
<dd> Keep non-ASCII characters in file and directory names. Default behaviour is to remove all non-ASCII characters.</dd>
<dt>&#8211;nowrite, -n</dt>
<dd> No writing of file to disk (use with -x to prevent a copy being stored on disk)</dd>
<dt>&#8211;output, -o &lt;dir&gt;</dt>
<dd> Recording output directory</dd>
<dt>&#8211;outputliveradio &lt;dir&gt;</dt>
<dd> Output directory for live radio recordings (overrides &#8211;output)</dd>
<dt>&#8211;outputlivetv &lt;dir&gt;</dt>
<dd> Output directory for live tv recordings (overrides &#8211;output)</dd>
<dt>&#8211;outputradio &lt;dir&gt;</dt>
<dd> Output directory for radio recordings (overrides &#8211;output)</dd>
<dt>&#8211;outputtv &lt;dir&gt;</dt>
<dd> Output directory for tv recordings (overrides &#8211;output)</dd>
<dt>&#8211;player &#8216;&lt;command&gt; &lt;options&gt;&#8217;</dt>
<dd> Use specified command to directly play the stream</dd>
<dt>&#8211;punctuation, &#8211;pu</dt>
<dd> Keep punctuation characters and symbols in file and directory names, with ellipsis always replaced by underscore. Default behaviour is to remove all punctuation and symbols except underscore, hyphen and full stop. Overridden by &#8211;fatfilename and &#8211;hfsfilename.</dd>
<dt>&#8211;stdout, -x</dt>
<dd> Additionally stream to STDOUT (so you can pipe output to a player)</dd>
<dt>&#8211;stream</dt>
<dd> Stream to STDOUT (so you can pipe output to a player)</dd>
<dt>&#8211;subdir, -s</dt>
<dd> Put Recorded files into Programme name subdirectory</dd>
<dt>&#8211;subdir-format &lt;format&gt;</dt>
<dd> The format to be used for the subdirectory naming using formatting fields. e.g. &#8216;&lt;nameshort&gt;-&lt;seriesnum&gt;&#8217;</dd>
<dt>&#8211;symlink &lt;file&gt;</dt>
<dd> Create symlink to &lt;file&gt; once we have the header of the recording</dd>
<dt>&#8211;thumb-ext &lt;ext&gt;</dt>
<dd> Thumbnail filename extension to use</dd>
<dt>&#8211;thumbsize &lt;index|width&gt;</dt>
<dd> Default thumbnail size/index to use for the current recording and metadata. index: 1-11 or width: 86,150,178,512,528,640,832,1024,1280,1600,1920</dd>
<dt>&#8211;thumbsizecache &lt;index|width&gt;</dt>
<dd> Default thumbnail size/index to use when building cache. index: 1-11 or width: 86,150,178,512,528,640,832,1024,1280,1600,1920</dd>
<dt>&#8211;whitespace, -w</dt>
<dd> Keep whitespace in file and directory names. Default behaviour is to replace whitespace with underscores.</dd>
<dt>&#8211;xml-alpha</dt>
<dd> Create freevo/Mythtv menu sorted alphabetically by programme name</dd>
<dt>&#8211;xml-channels</dt>
<dd> Create freevo/Mythtv menu of channels -&gt; programme names -&gt; episodes</dd>
<dt>&#8211;xml-names</dt>
<dd> Create freevo/Mythtv menu of programme names -&gt; episodes</dd></dl>
<p> </code></p>
<h3>PVR Options:</h3>
<dl>
<dt><code>&#8211;comment &lt;string&gt;</dt>
<dd> Adds a comment to a PVR search</dd>
<dt>&#8211;pvr [pvr search name]</dt>
<dd> Runs the PVR using all saved PVR searches (intended to be run every hour from cron etc). The list can be limited by adding a regex to the command. Synonyms: &#8211;pvrrun, &#8211;pvr-run</dd>
<dt>&#8211;pvr-add &lt;search name&gt;</dt>
<dd> Save the named PVR search with the specified search terms. Search terms required. Use &#8211;search=.* to force download of all available programmes. Synonyms: &#8211;pvradd</dd>
<dt>&#8211;pvr-del &lt;search name&gt;</dt>
<dd> Remove the named search from the PVR searches. Synonyms: &#8211;pvrdel</dd>
<dt>&#8211;pvr-disable &lt;search name&gt;</dt>
<dd> Disable (not delete) a named PVR search. Synonyms: &#8211;pvrdisable</dd>
<dt>&#8211;pvr-enable &lt;search name&gt;</dt>
<dd> Enable a previously disabled named PVR search. Synonyms: &#8211;pvrenable</dd>
<dt>&#8211;pvr-exclude &lt;string&gt;</dt>
<dd> Exclude the PVR searches to run by search name (regex or comma separated values). Synonyms: &#8211;pvrexclude</dd>
<dt>&#8211;pvr-list</dt>
<dd> Show the PVR search list. Synonyms: &#8211;pvrlist</dd>
<dt>&#8211;pvr-queue</dt>
<dd> Add currently matched programmes to queue for later one-off recording using the &#8211;pvr option. Search terms required unless &#8211;pid specified. Use &#8211;search=.* to force download of all available programmes. Synonyms: &#8211;pvrqueue</dd>
<dt>&#8211;pvr-scheduler &lt;seconds&gt;</dt>
<dd> Runs the PVR using all saved PVR searches every &lt;seconds&gt;. Synonyms: &#8211;pvrscheduler</dd>
<dt>&#8211;pvr-single &lt;search name&gt;</dt>
<dd> Runs a named PVR search. Synonyms: &#8211;pvrsingle</dd></dl>
<p> </code></p>
<h3>Config Options:</h3>
<dl>
<dt><code>&#8211;expiry, -e &lt;secs&gt;</dt>
<dd> Cache expiry in seconds (default 4hrs)</dd>
<dt>&#8211;limit-matches &lt;number&gt;</dt>
<dd> Limits the number of matching results for any search (and for every PVR search)</dd>
<dt>&#8211;nopurge</dt>
<dd> Don&#8217;t ask to delete programmes recorded over 30 days ago</dd>
<dt>&#8211;packagemanager &lt;string&gt;</dt>
<dd> Tell the updater that we were installed using a package manager and don&#8217;t update (use either: apt,rpm,deb,yum,disable)</dd>
<dt>&#8211;plugins-update</dt>
<dd> Update get_iplayer plugins to the latest versions. get_iplayer main script also will be updated if a newer version is available.)</dd>
<dt>&#8211;prefs-add</dt>
<dd> Add/Change specified saved user or preset options</dd>
<dt>&#8211;prefs-clear</dt>
<dd> Remove *ALL* saved user or preset options</dd>
<dt>&#8211;prefs-del</dt>
<dd> Remove specified saved user or preset options</dd>
<dt>&#8211;prefs-show</dt>
<dd> Show saved user or preset options</dd>
<dt>&#8211;preset, -z &lt;name&gt;</dt>
<dd> Use specified user options preset</dd>
<dt>&#8211;preset-list</dt>
<dd> Show all valid presets</dd>
<dt>&#8211;profile-dir &lt;dir&gt;</dt>
<dd> Override the user profile directory/folder</dd>
<dt>&#8211;refresh, &#8211;flush, -f</dt>
<dd> Refresh cache</dd>
<dt>&#8211;refresh-abortonerror</dt>
<dd> Abort cache refresh for programme type if data for any channel fails to download. Use &#8211;refresh-exclude to temporarily skip failing channels.</dd>
<dt>&#8211;refresh-exclude &lt;string&gt;</dt>
<dd> Exclude matched channel(s) when refreshing cache (regex or comma separated values)</dd>
<dt>&#8211;refresh-exclude-groups</dt>
<dd> Exclude channel groups when refreshing radio or tv cache (comma-separated values). Valid values: &#8216;national&#8217;, &#8216;regional&#8217;, &#8216;local&#8217;</dd>
<dt>&#8211;refresh-exclude-groups-radio</dt>
<dd> Exclude channel groups when refreshing radio cache (comma-separated values). Valid values: &#8216;national&#8217;, &#8216;regional&#8217;, &#8216;local&#8217;</dd>
<dt>&#8211;refresh-exclude-groups-tv</dt>
<dd> Exclude channel groups when refreshing tv cache (comma-separated values). Valid values: &#8216;national&#8217;, &#8216;regional&#8217;, &#8216;local&#8217;</dd>
<dt>&#8211;refresh-feeds &lt;string&gt;</dt>
<dd> Alternate source for programme data. Valid values: &#8216;ion&#8217;,&#8217;ion2&#8242;,&#8217;schedule&#8217;</dd>
<dt>&#8211;refresh-feeds-radio &lt;string&gt;</dt>
<dd> Alternate source for radio programme data. Valid values: &#8216;ion&#8217;,&#8217;ion2&#8242;,&#8217;schedule&#8217;</dd>
<dt>&#8211;refresh-feeds-tv &lt;string&gt;</dt>
<dd> Alternate source for TV programme data. Valid values: &#8216;ion&#8217;,&#8217;ion2&#8242;,&#8217;schedule&#8217;</dd>
<dt>&#8211;refresh-future</dt>
<dd> Obtain future programme schedule when refreshing cache (between 7-14 days)</dd>
<dt>&#8211;refresh-include &lt;string&gt;</dt>
<dd> Include matched channel(s) when refreshing cache (regex or comma separated values)</dd>
<dt>&#8211;refresh-limit &lt;integer&gt;</dt>
<dd> Number of days of programmes to cache. Only applied with &#8211;refresh-feeds=schedule. Makes cache updates VERY slow. Default: 7 Min: 1 Max: 30</dd>
<dt>&#8211;refresh-limit-radio &lt;integer&gt;</dt>
<dd> Number of days of radio programmes to cache. Only applied with &#8211;refresh-feeds=schedule. Makes cache updates VERY slow. Default: 7 Min: 1 Max: 30</dd>
<dt>&#8211;refresh-limit-tv &lt;integer&gt;</dt>
<dd> Number of days of TV programmes to cache. Only applied with &#8211;refresh-feeds=schedule. Makes cache updates VERY slow. Default: 7 Min: 1 Max: 30</dd>
<dt>&#8211;skipdeleted</dt>
<dd> Skip the download of metadata/thumbs/subs if the media file no longer exists. Use with &#8211;history &amp; &#8211;metadataonly/subsonly/thumbonly.</dd>
<dt>&#8211;update, -u</dt>
<dd> Update get_iplayer if a newer version is available. If so, plugins also will be updated if newer versions available.</dd>
<dt>&#8211;webrequest &lt;urlencoded string&gt;</dt>
<dd> Specify all options as a urlencoded string of &quot;name=val&amp;name=val&amp;&#8230;&quot;</dd></dl>
<p> </code></p>
<h3>External Program Options:</h3>
<dl>
<dt><code>&#8211;atomicparsley &lt;path&gt;</dt>
<dd> Location of AtomicParsley tagger binary</dd>
<dt>&#8211;ffmpeg &lt;path&gt;</dt>
<dd> Location of ffmpeg or avconv binary. Synonyms: &#8211;avconv</dd>
<dt>&#8211;ffmpeg-obsolete</dt>
<dd> Indicates you are using an obsolete version of ffmpeg (&lt;0.7) that does not support the -loglevel option, so &#8211;quiet, &#8211;verbose and &#8211;debug will not be applied to ffmpeg. Synonym: &#8211;avconv-obsolete</dd>
<dt>&#8211;id3v2 &lt;path&gt;</dt>
<dd> Location of id3v2 or id3tag binary</dd>
<dt>&#8211;lame &lt;path&gt;</dt>
<dd> Location of lame binary</dd>
<dt>&#8211;mplayer &lt;path&gt;</dt>
<dd> Location of mplayer binary</dd>
<dt>&#8211;rtmpdump &lt;path&gt;</dt>
<dd> Location of rtmpdump binary. Synonyms: &#8211;flvstreamer</dd>
<dt>&#8211;vlc &lt;path&gt;</dt>
<dd> Location of vlc or cvlc binary</dd></dl>
<p> </code></p>
<h3>Tagging Options:</h3>
<dl>
<dt><code>&#8211;no-artwork</dt>
<dd> Do not embed thumbnail image in output file. All other metadata values will be written.</dd>
<dt>&#8211;no-tag</dt>
<dd> Do not tag downloaded programmes</dd>
<dt>&#8211;tag-cnid</dt>
<dd> Use AtomicParsley &#8211;cnID argument (if supported) to add catalog ID used for combining HD and SD versions in iTunes</dd>
<dt>&#8211;tag-fulltitle</dt>
<dd> Prepend album/show title to track title</dd>
<dt>&#8211;tag-hdvideo</dt>
<dd> AtomicParsley accepts &#8211;hdvideo argument for HD video flag</dd>
<dt>&#8211;tag-id3sync</dt>
<dd> Save ID3 tags for MP3 files in synchronised form. Provides workaround for corruption of thumbnail images in Windows. Has no effect unless using MP3::Tag Perl module.</dd>
<dt>&#8211;tag-isodate</dt>
<dd> Use ISO8601 dates (YYYY-MM-DD) in album/show names and track titles</dd>
<dt>&#8211;tag-longdesc</dt>
<dd> AtomicParsley accepts &#8211;longdesc argument for long description text</dd>
<dt>&#8211;tag-longdescription</dt>
<dd> AtomicParsley accepts &#8211;longDescription argument for long description text</dd>
<dt>&#8211;tag-longepisode</dt>
<dd> Use &lt;episode&gt; (incl. episode number) instead of &lt;episodeshort&gt; for track title</dd>
<dt>&#8211;tag-longtitle</dt>
<dd> Prepend &lt;series&gt; (if available) to track title. Ignored with &#8211;tag-fulltitle.</dd>
<dt>&#8211;tag-podcast</dt>
<dd> Tag downloaded radio and tv programmes as iTunes podcasts (requires MP3::Tag module for AAC/MP3 files)</dd>
<dt>&#8211;tag-podcast-radio</dt>
<dd> Tag only downloaded radio programmes as iTunes podcasts (requires MP3::Tag module for AAC/MP3 files)</dd>
<dt>&#8211;tag-podcast-tv</dt>
<dd> Tag only downloaded tv programmes as iTunes podcasts</dd>
<dt>&#8211;tag-shortname</dt>
<dd> Use &lt;nameshort&gt; instead of &lt;name&gt; for album/show title</dd>
<dt>&#8211;tag-utf8</dt>
<dd> AtomicParsley accepts UTF-8 input</dd></dl>
<p> </code></p>
<h3>Misc Options:</h3>
<dl>
<dt><code>&#8211;encoding-console-in &lt;name&gt;</dt>
<dd> Character encoding for standard input (currently unused). Encoding name must be known to Perl Encode module. Default (only if auto-detect fails): Linux/Unix/OSX = UTF-8, Windows = cp850</dd>
<dt>&#8211;encoding-console-out &lt;name&gt;</dt>
<dd> Character encoding used to encode search results and other output. Encoding name must be known to Perl Encode module. Default (only if auto-detect fails): Linux/Unix/OSX = UTF-8, Windows = cp850</dd>
<dt>&#8211;encoding-locale &lt;name&gt;</dt>
<dd> Character encoding used to decode command-line arguments. Encoding name must be known to Perl Encode module. Default (only if auto-detect fails): Linux/Unix/OSX = UTF-8, Windows = cp1252</dd>
<dt>&#8211;encoding-locale-fs &lt;name&gt;</dt>
<dd> Character encoding used to encode file and directory names. Encoding name must be known to Perl Encode module. Default (only if auto-detect fails): Linux/Unix/OSX = UTF-8, Windows = cp1252</dd>
<dt>&#8211;no-scrape-versions</dt>
<dd> Do not scrape episode web pages as extra measure to find audiodescribed/signed versions (only applies with &#8211;playlist-metadata).</dd>
<dt>&#8211;playlist-metadata (IGNORED)</dt>
<dd> Force use of playlists (XML and JSON) for programme metadata instead of /programmes data endpoints.</dd>
<dt>&#8211;trim-history &lt;# days to retain&gt;</dt>
<dd> Remove download history entries older than number of days specified in option value. Cannot specify 0 &#8211; use &#8216;all&#8217; to completely delete download history</dd></dl>
<p> </code></p>
<h2>AUTHOR</h2>
<p> get_iplayer was written by Phil Lewis &lt;iplayer2 (at sign) linuxcentre.net&gt; and is now maintained by the contributors at <a rel="nofollow" href="http://www.infradead.org/get_iplayer/html/get_iplayer.html">http://www.infradead.org/get_iplayer/html/get_iplayer.html</a> </p>
<p> This manual page was originally written by Jonathan Wiltshire &lt;jmw [at] debian.org&gt; for the Debian project (but may be used by others).</p>
<h2>COPYRIGHT NOTICE</h2>
<p> get_iplayer v2.94, Copyright (C) 2008-2010 Phil Lewis<br />
&nbsp;<wbr>&nbsp;<wbr>This program comes with ABSOLUTELY NO WARRANTY;&nbsp;<wbr>for details use &#8211;warranty.<br />
&nbsp;<wbr>&nbsp;<wbr>This is free software, and you are welcome to redistribute it under certain<br />
&nbsp;<wbr>&nbsp;<wbr>conditions;&nbsp;<wbr>use &#8211;conditions for details. </p>
