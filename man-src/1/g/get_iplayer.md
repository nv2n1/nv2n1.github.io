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
<dt><code>&#8211;before</p>
<dd> Limit search to programmes added to the cache before N hours ago</p>
<dt>&#8211;category &lt;string&gt;</p>
<dd> Narrow search to matched categories (regex or comma separated values). Supported only for podcasts (not tv or radio programmes).</p>
<dt>&#8211;channel &lt;string&gt;</p>
<dd> Narrow search to matched channel(s) (regex or comma separated values)</p>
<dt>&#8211;exclude &lt;string&gt;</p>
<dd> Narrow search to exclude matched programme names (regex or comma separated values)</p>
<dt>&#8211;exclude-category &lt;string&gt;</p>
<dd> Narrow search to exclude matched categories (regex or comma separated values). Supported only for podcasts (not tv or radio programmes).</p>
<dt>&#8211;exclude-channel &lt;string&gt;</p>
<dd> Narrow search to exclude matched channel(s) (regex or comma separated values)</p>
<dt>&#8211;fields &lt;field1&gt;,&lt;field2&gt;,..</p>
<dd> Searches only in the specified comma separated fields</p>
<dt>&#8211;future</p>
<dd> Additionally search future programme schedule if it has been indexed (refresh cache with: &#8211;refresh &#8211;refresh-future).</p>
<dt>&#8211;history</p>
<dd> Search/show recordings history</p>
<dt>&#8211;long, -l</p>
<dd> Additionally search in programme descriptions and episode names (same as &#8211;fields=name,episode,desc )</p>
<dt>&#8211;search &lt;search term&gt;</p>
<dd> GetOpt compliant way of specifying search args</p>
<dt>&#8211;since</p>
<dd> Limit search to programmes added to the cache in the last N hours</p>
<dt>&#8211;type &lt;type&gt;</p>
<dd> Only search in these types of programmes: liveradio,livetv,radio,tv,all (tv is default)</p>
<dt>&#8211;versions &lt;versions&gt;</p>
<dd> Version of programme to search or record. List is processed from left to right and first version found is downloaded. Example: &#8216;&#8211;versions signed,audiodescribed,default&#8217; will prefer signed and audiodescribed programmes if available. Default: &#8216;default,signed,audiodescribed&#8217;</dl>
<p> </code></p>
<h3>Display Options:</h3>
<dl>
<dt><code>&#8211;conditions</p>
<dd> Shows GPLv3 conditions</p>
<dt>&#8211;debug</p>
<dd> Debug output</p>
<dt>&#8211;dump-options</p>
<dd> Dumps all options with their internal option key names</p>
<dt>&#8211;help, -h</p>
<dd> Intermediate help text</p>
<dt>&#8211;helpbasic, &#8211;usage</p>
<dd> Basic help text</p>
<dt>&#8211;helplong</p>
<dd> Advanced help text</p>
<dt>&#8211;hide</p>
<dd> Hide previously recorded programmes</p>
<dt>&#8211;info, -i</p>
<dd> Show full programme metadata and availability of modes and subtitles (max 50 matches)</p>
<dt>&#8211;list &lt;categories|channel&gt;</p>
<dd> Show a list of available categories/channels for the selected type and exit</p>
<dt>&#8211;listformat &lt;format&gt;</p>
<dd> Display programme data based on a user-defined format string (such as &lt;pid&gt;, &lt;name&gt; etc)</p>
<dt>&#8211;listplugins</p>
<dd> Display a list of currently available plugins or programme types</p>
<dt>&#8211;long, -l</p>
<dd> Show long programme info</p>
<dt>&#8211;manpage &lt;file&gt;</p>
<dd> Create man page based on current help text</p>
<dt>&#8211;nocopyright</p>
<dd> Don&#8217;t display copyright header</p>
<dt>&#8211;page &lt;number&gt;</p>
<dd> Page number to display for multipage output</p>
<dt>&#8211;pagesize &lt;number&gt;</p>
<dd> Number of matches displayed on a page for multipage output</p>
<dt>&#8211;quiet, -q</p>
<dd> Reduce logging output</p>
<dt>&#8211;series</p>
<dd> Display Programme series names only with number of episodes</p>
<dt>&#8211;show-cache-age</p>
<dd> Displays the age of the selected programme caches then exit</p>
<dt>&#8211;show-options</p>
<dd> Shows options which are set and where they are defined</p>
<dt>&#8211;silent</p>
<dd> No logging output except PVR download report. Cannot be saved in preferences or PVR searches.</p>
<dt>&#8211;sort &lt;fieldname&gt;</p>
<dd> Field to use to sort displayed matches</p>
<dt>&#8211;sortreverse</p>
<dd> Reverse order of sorted matches</p>
<dt>&#8211;streaminfo</p>
<dd> Returns all of the media stream urls of the programme(s)</p>
<dt>&#8211;terse</p>
<dd> Only show terse programme info (does not affect searching)</p>
<dt>&#8211;tree</p>
<dd> Display Programme listings in a tree view</p>
<dt>&#8211;verbose, -v</p>
<dd> Verbose</p>
<dt>&#8211;warranty</p>
<dd> Displays warranty section of GPLv3</p>
<dt>-V</p>
<dd> Show get_iplayer version and exit.</dl>
<p> </code></p>
<h3>Recording Options:</h3>
<dl>
<dt><code>&#8211;attempts &lt;number&gt;</p>
<dd> Number of attempts to make or resume a failed connection. &#8211;attempts is applied per-stream, per-mode. TV modes typically have two streams available.</p>
<dt>&#8211;bandwidth</p>
<dd> In radio realaudio mode specify the link bandwidth in bps for rtsp streaming (default 512000)</p>
<dt>&#8211;check-duration</p>
<dd> Print message showing recorded duration, expected duration and difference between them.</p>
<dt>&#8211;ddl-radio-opts &lt;options&gt;</p>
<dd> Add custom options to ffmpeg DDL download re-muxing for radio</p>
<dt>&#8211;exclude-supplier &lt;suppliers&gt;</p>
<dd> Comma-delimited list of media stream suppliers to skip. Possible values: akamai,limelight,level3,bidi</p>
<dt>&#8211;ffmpeg-liveradio-opts &lt;options&gt;</p>
<dd> Add custom options to ffmpeg re-muxing for liveradio</p>
<dt>&#8211;ffmpeg-livetv-opts &lt;options&gt;</p>
<dd> Add custom options to ffmpeg re-muxing for livetv</p>
<dt>&#8211;ffmpeg-radio-opts &lt;options&gt;</p>
<dd> Add custom options to ffmpeg re-muxing for radio</p>
<dt>&#8211;ffmpeg-tv-opts &lt;options&gt;</p>
<dd> Add custom options to ffmpeg re-muxing for tv</p>
<dt>&#8211;force</p>
<dd> Ignore programme history (unsets &#8211;hide option also). Forces a script update if used with -u</p>
<dt>&#8211;get, -g</p>
<dd> Start recording matching programmes. Search terms required unless &#8211;pid specified. Use &#8211;search=.* to force download of all available programmes.</p>
<dt>&#8211;hash</p>
<dd> Show recording progress as hashes</p>
<dt>&#8211;hls-liveradio-opts &lt;options&gt;</p>
<dd> Add custom options to ffmpeg HLS download re-muxing for liveradio</p>
<dt>&#8211;hls-livetv-opts &lt;options&gt;</p>
<dd> Add custom options to ffmpeg HLS download encoding for livetv</p>
<dt>&#8211;hls-radio-opts &lt;options&gt;</p>
<dd> Add custom options to ffmpeg HLS download re-muxing for radio</p>
<dt>&#8211;hls-tv-opts &lt;options&gt;</p>
<dd> Add custom options to ffmpeg HLS download re-muxing for tv</p>
<dt>&#8211;liveradio-intl</p>
<dd> Force use of hard-coded international streams for HLS live radio. Ignored for World Service</p>
<dt>&#8211;liveradio-uk</p>
<dd> Force use of hard-coded UK streams for HLS live radio (overrides &#8211;liveradio-intl). Ignored for World Service</p>
<dt>&#8211;liveradiomode &lt;mode&gt;,&lt;mode&gt;,..</p>
<dd> Live Radio recording modes: hlsaachigh,hlsaacstd,hlsaacmed,hlsaaclow,shoutcastmp3std,shoutcastaachigh(R3 only, UK only). Shortcuts: default,good,better(=default),best,hls. (&#8216;default&#8217;=hlsaachigh,hlsaacstd,hlsaacmed,hlsaaclow)</p>
<dt>&#8211;livetv-uk</p>
<dd> Force use of hard-coded UK streams for HLS live tv</p>
<dt>&#8211;livetvmode &lt;mode&gt;,&lt;mode&gt;,&#8230;</p>
<dd> Live TV recording modes: hlshd,hlssd,hlsvhigh,hlshigh,hlsstd,hlslow. Shortcuts: default,good,better(=default),vbetter,best,hls. (&#8216;default&#8217;=hlsvhigh,hlshigh,hlsstd,hlslow)</p>
<dt>&#8211;mediaselector &lt;identifier&gt;</p>
<dd> Identifier of mediaselector API to use when searching for media streams. One of: 4,5 Default: 5</p>
<dt>&#8211;metadata-only</p>
<dd> Create specified metadata info file without any recording or streaming (can also be used with thumbnail option).</p>
<dt>&#8211;mmsnothread</p>
<dd> Disable parallel threaded recording for mms</p>
<dt>&#8211;modes &lt;mode&gt;,&lt;mode&gt;,&#8230;</p>
<dd> Recording modes. See &#8211;tvmode and &#8211;radiomode for available modes and defaults. Shortcuts: default,good,better(=default),best. Use &#8211;modes=best to select highest quality available (incl. HD TV).</p>
<dt>&#8211;multimode</p>
<dd> Allow the recording of more than one mode for the same programme &#8211; WARNING: will record all specified/default modes!!</p>
<dt>&#8211;no-proxy</p>
<dd> Ignore &#8211;proxy setting in preferences</p>
<dt>&#8211;overwrite</p>
<dd> Overwrite recordings if they already exist</p>
<dt>&#8211;partial-proxy</p>
<dd> Only uses web proxy where absolutely required (try this extra option if your proxy fails). If specified, value of http_proxy environment variable (if any) in parent process is retained and passed to child processes.</p>
<dt>&#8211;pid &lt;pid&gt;</p>
<dd> Record an arbitrary pid that does not necessarily appear in the index.</p>
<dt>&#8211;pid-recursive</p>
<dd> When used with &#8211;pid record all the embedded pids if the pid is a series or brand pid.</p>
<dt>&#8211;proxy, -p &lt;url&gt;</p>
<dd> Web proxy URL e.g. &#8216;<a rel="nofollow" href="http://USERNAME:PASSWORD@SERVER:PORT'">http://USERNAME:PASSWORD@SERVER:PORT&#8217;</a> or &#8216;<a href="http://SERVER:PORT'.">http://SERVER:PORT&#8217;.</a> Sets http_proxy environment variable for child processes (e.g., ffmpeg) unless &#8211;partial-proxy is specified.</p>
<dt>&#8211;radiomode &lt;mode&gt;,&lt;mode&gt;,&#8230;</p>
<dd> Radio recording modes: flashaachigh,flashaacstd,flashaudio,flashaaclow,wma. Shortcuts: default,good,better(=default),best,rtmp,flash,flashaac. (&#8216;default&#8217;=flashaachigh,flashaacstd,flashaudio,flashaaclow)</p>
<dt>&#8211;raw</p>
<dd> Don&#8217;t transcode or change the recording/stream in any way (i.e. radio/realaudio, rtmp/flv)</p>
<dt>&#8211;rtmp-liveradio-opts &lt;options&gt;</p>
<dd> Add custom options to rtmpdump for liveradio</p>
<dt>&#8211;rtmp-livetv-opts &lt;options&gt;</p>
<dd> Add custom options to rtmpdump for livetv</p>
<dt>&#8211;rtmp-radio-opts &lt;options&gt;</p>
<dd> Add custom options to rtmpdump for radio</p>
<dt>&#8211;rtmp-tv-opts &lt;options&gt;</p>
<dd> Add custom options to rtmpdump for tv</p>
<dt>&#8211;rtmpport &lt;port&gt;</p>
<dd> Override the RTMP port (e.g. 443)</p>
<dt>&#8211;shoutcast-liveradio-opts &lt;options&gt;</p>
<dd> Add custom options to ffmpeg Shoutcast download re-muxing for liveradio</p>
<dt>&#8211;start &lt;secs|hh:mm:ss&gt;</p>
<dd> Recording/streaming start offset (rtmp and realaudio only)</p>
<dt>&#8211;stop &lt;secs|hh:mm:ss&gt;</p>
<dd> Recording/streaming stop offset (can be used to limit live rtmp recording length) rtmp and realaudio only</p>
<dt>&#8211;suboffset &lt;offset&gt;</p>
<dd> Offset the subtitle timestamps by the specified number of milliseconds</p>
<dt>&#8211;subsfmt &lt;format&gt;</p>
<dd> Subtitles format. One of: default, compact. Default: &#8216;default&#8217;</p>
<dt>&#8211;subsraw</p>
<dd> Additionally save the raw subtitles file</p>
<dt>&#8211;subtitles</p>
<dd> Download subtitles into srt/SubRip format if available and supported</p>
<dt>&#8211;subtitles-only</p>
<dd> Only download the subtitles, not the programme</p>
<dt>&#8211;subtitles-required</p>
<dd> Do not download TV programme if subtitles are not available.</p>
<dt>&#8211;swfurl &lt;URL&gt;</p>
<dd> URL of Flash player used by rtmpdump for verification. Only use if default Flash player URL is not working.</p>
<dt>&#8211;tag-only</p>
<dd> Only update the programme tag and not download the programme (can also be used with &#8211;history)</p>
<dt>&#8211;test, -t</p>
<dd> Test only &#8211; no recording (will show programme type)</p>
<dt>&#8211;thumb</p>
<dd> Download Thumbnail image if available</p>
<dt>&#8211;thumbnail-only</p>
<dd> Only Download Thumbnail image if available, not the programme</p>
<dt>&#8211;tvmode &lt;mode&gt;,&lt;mode&gt;,&#8230;</p>
<dd> TV recording modes: flashhd,flashvhigh,flashhigh,flashstd,flashnormal,flashlow. Shortcuts: default,good,better(=default),best,rtmp,flash. (Use &#8216;best&#8217; for HD TV. &#8216;default&#8217;=flashvhigh,flashhigh,flashstd,flashnormal,flashlow)</p>
<dt>&#8211;url &quot;&lt;url&gt;&quot;</p>
<dd> Record the embedded media player in the specified URL. Use with &#8211;type=&lt;type&gt;.</p>
<dt>&#8211;wav</p>
<dd> In radio realaudio mode output as wav and don&#8217;t transcode to mp3</dl>
<p> </code></p>
<h3>Output Options:</h3>
<dl>
<dt><code>&#8211;aactomp3</p>
<dd> Transcode AAC audio to MP3 with ffmpeg/avconv (CBR 128k unless &#8211;mp3vbr is specified). Applied only to radio programmes. (Synonyms: &#8211;mp3)</p>
<dt>&#8211;avi</p>
<dd> Output video in AVI container instead of MP4. There is no metadata tagging support for AVI output.</p>
<dt>&#8211;command, -c &lt;command&gt;</p>
<dd> Run user command after successful recording using args such as &lt;pid&gt;, &lt;name&gt; etc</p>
<dt>&#8211;email &lt;address&gt;</p>
<dd> Email HTML index of matching programmes to specified address</p>
<dt>&#8211;email-password &lt;password&gt;</p>
<dd> Email password</p>
<dt>&#8211;email-port &lt;port number&gt;</p>
<dd> Email port number (default: appropriate port for &#8211;email-security)</p>
<dt>&#8211;email-security &lt;TLS|SSL&gt;</p>
<dd> Email security TLS, SSL (default: none)</p>
<dt>&#8211;email-sender &lt;address&gt;</p>
<dd> Optional email sender address</p>
<dt>&#8211;email-smtp &lt;hostname&gt;</p>
<dd> SMTP server IP address to use to send email (default: localhost)</p>
<dt>&#8211;email-user &lt;username&gt;</p>
<dd> Email username</p>
<dt>&#8211;fatfilename</p>
<dd> Remove FAT forbidden characters in file and directory names. Always applied on Windows. Overrides &#8211;punctuation.</p>
<dt>&#8211;file-prefix &lt;format&gt;</p>
<dd> The filename prefix (excluding dir and extension) using formatting fields. e.g. &#8216;&lt;name&gt;-&lt;episode&gt;-&lt;pid&gt;&#8217;</p>
<dt>&#8211;fxd &lt;file&gt;</p>
<dd> Create Freevo FXD XML of matching programmes in specified file</p>
<dt>&#8211;hfsfilename</p>
<dd> Remove colons in file and directory names. Prevents OS X Finder displaying colon as forward slash. Always applied on OS X. Overrides &#8211;punctuation.</p>
<dt>&#8211;html &lt;file&gt;</p>
<dd> Create basic HTML index of matching programmes in specified file</p>
<dt>&#8211;isodate</p>
<dd> Use ISO8601 dates (YYYY-MM-DD) in filenames and subdirectory paths</p>
<dt>&#8211;keep-all</p>
<dd> Keep whitespace, all possible punctuation and non-ASCII characters in file and directory names. Shortcut for: &#8211;whitespace &#8211;non-ascii &#8211;punctuation.</p>
<dt>&#8211;metadata &lt;type&gt;</p>
<dd> Create metadata info file after recording. Valid types are: xbmc (or kodi), xbmc_movie (or kodi_movie), freevo, generic</p>
<dt>&#8211;mkv</p>
<dd> Output video in MKV container instead of MP4. There is no metadata tagging support for MKV output.</p>
<dt>&#8211;mp3vbr</p>
<dd> Set LAME VBR mode to N (0 to 9) for AAC transcoding. 0 = target bitrate 245 Kbit/s, 9 = target bitrate 65 Kbit/s (requires &#8211;aactomp3). Applied only to radio programmes.</p>
<dt>&#8211;mythtv &lt;file&gt;</p>
<dd> Create Mythtv streams XML of matching programmes in specified file</p>
<dt>&#8211;non-ascii, &#8211;na</p>
<dd> Keep non-ASCII characters in file and directory names. Default behaviour is to remove all non-ASCII characters.</p>
<dt>&#8211;nowrite, -n</p>
<dd> No writing of file to disk (use with -x to prevent a copy being stored on disk)</p>
<dt>&#8211;output, -o &lt;dir&gt;</p>
<dd> Recording output directory</p>
<dt>&#8211;outputliveradio &lt;dir&gt;</p>
<dd> Output directory for live radio recordings (overrides &#8211;output)</p>
<dt>&#8211;outputlivetv &lt;dir&gt;</p>
<dd> Output directory for live tv recordings (overrides &#8211;output)</p>
<dt>&#8211;outputradio &lt;dir&gt;</p>
<dd> Output directory for radio recordings (overrides &#8211;output)</p>
<dt>&#8211;outputtv &lt;dir&gt;</p>
<dd> Output directory for tv recordings (overrides &#8211;output)</p>
<dt>&#8211;player &#8216;&lt;command&gt; &lt;options&gt;&#8217;</p>
<dd> Use specified command to directly play the stream</p>
<dt>&#8211;punctuation, &#8211;pu</p>
<dd> Keep punctuation characters and symbols in file and directory names, with ellipsis always replaced by underscore. Default behaviour is to remove all punctuation and symbols except underscore, hyphen and full stop. Overridden by &#8211;fatfilename and &#8211;hfsfilename.</p>
<dt>&#8211;stdout, -x</p>
<dd> Additionally stream to STDOUT (so you can pipe output to a player)</p>
<dt>&#8211;stream</p>
<dd> Stream to STDOUT (so you can pipe output to a player)</p>
<dt>&#8211;subdir, -s</p>
<dd> Put Recorded files into Programme name subdirectory</p>
<dt>&#8211;subdir-format &lt;format&gt;</p>
<dd> The format to be used for the subdirectory naming using formatting fields. e.g. &#8216;&lt;nameshort&gt;-&lt;seriesnum&gt;&#8217;</p>
<dt>&#8211;symlink &lt;file&gt;</p>
<dd> Create symlink to &lt;file&gt; once we have the header of the recording</p>
<dt>&#8211;thumb-ext &lt;ext&gt;</p>
<dd> Thumbnail filename extension to use</p>
<dt>&#8211;thumbsize &lt;index|width&gt;</p>
<dd> Default thumbnail size/index to use for the current recording and metadata. index: 1-11 or width: 86,150,178,512,528,640,832,1024,1280,1600,1920</p>
<dt>&#8211;thumbsizecache &lt;index|width&gt;</p>
<dd> Default thumbnail size/index to use when building cache. index: 1-11 or width: 86,150,178,512,528,640,832,1024,1280,1600,1920</p>
<dt>&#8211;whitespace, -w</p>
<dd> Keep whitespace in file and directory names. Default behaviour is to replace whitespace with underscores.</p>
<dt>&#8211;xml-alpha</p>
<dd> Create freevo/Mythtv menu sorted alphabetically by programme name</p>
<dt>&#8211;xml-channels</p>
<dd> Create freevo/Mythtv menu of channels -&gt; programme names -&gt; episodes</p>
<dt>&#8211;xml-names</p>
<dd> Create freevo/Mythtv menu of programme names -&gt; episodes</dl>
<p> </code></p>
<h3>PVR Options:</h3>
<dl>
<dt><code>&#8211;comment &lt;string&gt;</p>
<dd> Adds a comment to a PVR search</p>
<dt>&#8211;pvr [pvr search name]</p>
<dd> Runs the PVR using all saved PVR searches (intended to be run every hour from cron etc). The list can be limited by adding a regex to the command. Synonyms: &#8211;pvrrun, &#8211;pvr-run</p>
<dt>&#8211;pvr-add &lt;search name&gt;</p>
<dd> Save the named PVR search with the specified search terms. Search terms required. Use &#8211;search=.* to force download of all available programmes. Synonyms: &#8211;pvradd</p>
<dt>&#8211;pvr-del &lt;search name&gt;</p>
<dd> Remove the named search from the PVR searches. Synonyms: &#8211;pvrdel</p>
<dt>&#8211;pvr-disable &lt;search name&gt;</p>
<dd> Disable (not delete) a named PVR search. Synonyms: &#8211;pvrdisable</p>
<dt>&#8211;pvr-enable &lt;search name&gt;</p>
<dd> Enable a previously disabled named PVR search. Synonyms: &#8211;pvrenable</p>
<dt>&#8211;pvr-exclude &lt;string&gt;</p>
<dd> Exclude the PVR searches to run by search name (regex or comma separated values). Synonyms: &#8211;pvrexclude</p>
<dt>&#8211;pvr-list</p>
<dd> Show the PVR search list. Synonyms: &#8211;pvrlist</p>
<dt>&#8211;pvr-queue</p>
<dd> Add currently matched programmes to queue for later one-off recording using the &#8211;pvr option. Search terms required unless &#8211;pid specified. Use &#8211;search=.* to force download of all available programmes. Synonyms: &#8211;pvrqueue</p>
<dt>&#8211;pvr-scheduler &lt;seconds&gt;</p>
<dd> Runs the PVR using all saved PVR searches every &lt;seconds&gt;. Synonyms: &#8211;pvrscheduler</p>
<dt>&#8211;pvr-single &lt;search name&gt;</p>
<dd> Runs a named PVR search. Synonyms: &#8211;pvrsingle</dl>
<p> </code></p>
<h3>Config Options:</h3>
<dl>
<dt><code>&#8211;expiry, -e &lt;secs&gt;</p>
<dd> Cache expiry in seconds (default 4hrs)</p>
<dt>&#8211;limit-matches &lt;number&gt;</p>
<dd> Limits the number of matching results for any search (and for every PVR search)</p>
<dt>&#8211;nopurge</p>
<dd> Don&#8217;t ask to delete programmes recorded over 30 days ago</p>
<dt>&#8211;packagemanager &lt;string&gt;</p>
<dd> Tell the updater that we were installed using a package manager and don&#8217;t update (use either: apt,rpm,deb,yum,disable)</p>
<dt>&#8211;plugins-update</p>
<dd> Update get_iplayer plugins to the latest versions. get_iplayer main script also will be updated if a newer version is available.)</p>
<dt>&#8211;prefs-add</p>
<dd> Add/Change specified saved user or preset options</p>
<dt>&#8211;prefs-clear</p>
<dd> Remove *ALL* saved user or preset options</p>
<dt>&#8211;prefs-del</p>
<dd> Remove specified saved user or preset options</p>
<dt>&#8211;prefs-show</p>
<dd> Show saved user or preset options</p>
<dt>&#8211;preset, -z &lt;name&gt;</p>
<dd> Use specified user options preset</p>
<dt>&#8211;preset-list</p>
<dd> Show all valid presets</p>
<dt>&#8211;profile-dir &lt;dir&gt;</p>
<dd> Override the user profile directory/folder</p>
<dt>&#8211;refresh, &#8211;flush, -f</p>
<dd> Refresh cache</p>
<dt>&#8211;refresh-abortonerror</p>
<dd> Abort cache refresh for programme type if data for any channel fails to download. Use &#8211;refresh-exclude to temporarily skip failing channels.</p>
<dt>&#8211;refresh-exclude &lt;string&gt;</p>
<dd> Exclude matched channel(s) when refreshing cache (regex or comma separated values)</p>
<dt>&#8211;refresh-exclude-groups</p>
<dd> Exclude channel groups when refreshing radio or tv cache (comma-separated values). Valid values: &#8216;national&#8217;, &#8216;regional&#8217;, &#8216;local&#8217;</p>
<dt>&#8211;refresh-exclude-groups-radio</p>
<dd> Exclude channel groups when refreshing radio cache (comma-separated values). Valid values: &#8216;national&#8217;, &#8216;regional&#8217;, &#8216;local&#8217;</p>
<dt>&#8211;refresh-exclude-groups-tv</p>
<dd> Exclude channel groups when refreshing tv cache (comma-separated values). Valid values: &#8216;national&#8217;, &#8216;regional&#8217;, &#8216;local&#8217;</p>
<dt>&#8211;refresh-feeds &lt;string&gt;</p>
<dd> Alternate source for programme data. Valid values: &#8216;ion&#8217;,&#8217;ion2&#8242;,&#8217;schedule&#8217;</p>
<dt>&#8211;refresh-feeds-radio &lt;string&gt;</p>
<dd> Alternate source for radio programme data. Valid values: &#8216;ion&#8217;,&#8217;ion2&#8242;,&#8217;schedule&#8217;</p>
<dt>&#8211;refresh-feeds-tv &lt;string&gt;</p>
<dd> Alternate source for TV programme data. Valid values: &#8216;ion&#8217;,&#8217;ion2&#8242;,&#8217;schedule&#8217;</p>
<dt>&#8211;refresh-future</p>
<dd> Obtain future programme schedule when refreshing cache (between 7-14 days)</p>
<dt>&#8211;refresh-include &lt;string&gt;</p>
<dd> Include matched channel(s) when refreshing cache (regex or comma separated values)</p>
<dt>&#8211;refresh-limit &lt;integer&gt;</p>
<dd> Number of days of programmes to cache. Only applied with &#8211;refresh-feeds=schedule. Makes cache updates VERY slow. Default: 7 Min: 1 Max: 30</p>
<dt>&#8211;refresh-limit-radio &lt;integer&gt;</p>
<dd> Number of days of radio programmes to cache. Only applied with &#8211;refresh-feeds=schedule. Makes cache updates VERY slow. Default: 7 Min: 1 Max: 30</p>
<dt>&#8211;refresh-limit-tv &lt;integer&gt;</p>
<dd> Number of days of TV programmes to cache. Only applied with &#8211;refresh-feeds=schedule. Makes cache updates VERY slow. Default: 7 Min: 1 Max: 30</p>
<dt>&#8211;skipdeleted</p>
<dd> Skip the download of metadata/thumbs/subs if the media file no longer exists. Use with &#8211;history &amp; &#8211;metadataonly/subsonly/thumbonly.</p>
<dt>&#8211;update, -u</p>
<dd> Update get_iplayer if a newer version is available. If so, plugins also will be updated if newer versions available.</p>
<dt>&#8211;webrequest &lt;urlencoded string&gt;</p>
<dd> Specify all options as a urlencoded string of &quot;name=val&amp;name=val&amp;&#8230;&quot;</dl>
<p> </code></p>
<h3>External Program Options:</h3>
<dl>
<dt><code>&#8211;atomicparsley &lt;path&gt;</p>
<dd> Location of AtomicParsley tagger binary</p>
<dt>&#8211;ffmpeg &lt;path&gt;</p>
<dd> Location of ffmpeg or avconv binary. Synonyms: &#8211;avconv</p>
<dt>&#8211;ffmpeg-obsolete</p>
<dd> Indicates you are using an obsolete version of ffmpeg (&lt;0.7) that does not support the -loglevel option, so &#8211;quiet, &#8211;verbose and &#8211;debug will not be applied to ffmpeg. Synonym: &#8211;avconv-obsolete</p>
<dt>&#8211;id3v2 &lt;path&gt;</p>
<dd> Location of id3v2 or id3tag binary</p>
<dt>&#8211;lame &lt;path&gt;</p>
<dd> Location of lame binary</p>
<dt>&#8211;mplayer &lt;path&gt;</p>
<dd> Location of mplayer binary</p>
<dt>&#8211;rtmpdump &lt;path&gt;</p>
<dd> Location of rtmpdump binary. Synonyms: &#8211;flvstreamer</p>
<dt>&#8211;vlc &lt;path&gt;</p>
<dd> Location of vlc or cvlc binary</dl>
<p> </code></p>
<h3>Tagging Options:</h3>
<dl>
<dt><code>&#8211;no-artwork</p>
<dd> Do not embed thumbnail image in output file. All other metadata values will be written.</p>
<dt>&#8211;no-tag</p>
<dd> Do not tag downloaded programmes</p>
<dt>&#8211;tag-cnid</p>
<dd> Use AtomicParsley &#8211;cnID argument (if supported) to add catalog ID used for combining HD and SD versions in iTunes</p>
<dt>&#8211;tag-fulltitle</p>
<dd> Prepend album/show title to track title</p>
<dt>&#8211;tag-hdvideo</p>
<dd> AtomicParsley accepts &#8211;hdvideo argument for HD video flag</p>
<dt>&#8211;tag-id3sync</p>
<dd> Save ID3 tags for MP3 files in synchronised form. Provides workaround for corruption of thumbnail images in Windows. Has no effect unless using MP3::Tag Perl module.</p>
<dt>&#8211;tag-isodate</p>
<dd> Use ISO8601 dates (YYYY-MM-DD) in album/show names and track titles</p>
<dt>&#8211;tag-longdesc</p>
<dd> AtomicParsley accepts &#8211;longdesc argument for long description text</p>
<dt>&#8211;tag-longdescription</p>
<dd> AtomicParsley accepts &#8211;longDescription argument for long description text</p>
<dt>&#8211;tag-longepisode</p>
<dd> Use &lt;episode&gt; (incl. episode number) instead of &lt;episodeshort&gt; for track title</p>
<dt>&#8211;tag-longtitle</p>
<dd> Prepend &lt;series&gt; (if available) to track title. Ignored with &#8211;tag-fulltitle.</p>
<dt>&#8211;tag-podcast</p>
<dd> Tag downloaded radio and tv programmes as iTunes podcasts (requires MP3::Tag module for AAC/MP3 files)</p>
<dt>&#8211;tag-podcast-radio</p>
<dd> Tag only downloaded radio programmes as iTunes podcasts (requires MP3::Tag module for AAC/MP3 files)</p>
<dt>&#8211;tag-podcast-tv</p>
<dd> Tag only downloaded tv programmes as iTunes podcasts</p>
<dt>&#8211;tag-shortname</p>
<dd> Use &lt;nameshort&gt; instead of &lt;name&gt; for album/show title</p>
<dt>&#8211;tag-utf8</p>
<dd> AtomicParsley accepts UTF-8 input</dl>
<p> </code></p>
<h3>Misc Options:</h3>
<dl>
<dt><code>&#8211;encoding-console-in &lt;name&gt;</p>
<dd> Character encoding for standard input (currently unused). Encoding name must be known to Perl Encode module. Default (only if auto-detect fails): Linux/Unix/OSX = UTF-8, Windows = cp850</p>
<dt>&#8211;encoding-console-out &lt;name&gt;</p>
<dd> Character encoding used to encode search results and other output. Encoding name must be known to Perl Encode module. Default (only if auto-detect fails): Linux/Unix/OSX = UTF-8, Windows = cp850</p>
<dt>&#8211;encoding-locale &lt;name&gt;</p>
<dd> Character encoding used to decode command-line arguments. Encoding name must be known to Perl Encode module. Default (only if auto-detect fails): Linux/Unix/OSX = UTF-8, Windows = cp1252</p>
<dt>&#8211;encoding-locale-fs &lt;name&gt;</p>
<dd> Character encoding used to encode file and directory names. Encoding name must be known to Perl Encode module. Default (only if auto-detect fails): Linux/Unix/OSX = UTF-8, Windows = cp1252</p>
<dt>&#8211;no-scrape-versions</p>
<dd> Do not scrape episode web pages as extra measure to find audiodescribed/signed versions (only applies with &#8211;playlist-metadata).</p>
<dt>&#8211;playlist-metadata (IGNORED)</p>
<dd> Force use of playlists (XML and JSON) for programme metadata instead of /programmes data endpoints.</p>
<dt>&#8211;trim-history &lt;# days to retain&gt;</p>
<dd> Remove download history entries older than number of days specified in option value. Cannot specify 0 &#8211; use &#8216;all&#8217; to completely delete download history</dl>
<p> </code></p>
<h2>AUTHOR</h2>
<p> get_iplayer was written by Phil Lewis &lt;iplayer2 (at sign) linuxcentre.net&gt; and is now maintained by the contributors at <a rel="nofollow" href="http://www.infradead.org/get_iplayer/html/get_iplayer.html">http://www.infradead.org/get_iplayer/html/get_iplayer.html</a> </p>
<p> This manual page was originally written by Jonathan Wiltshire &lt;jmw [at] debian.org&gt; for the Debian project (but may be used by others).</p>
<h2>COPYRIGHT NOTICE</h2>
<p> get_iplayer v2.94, Copyright (C) 2008-2010 Phil Lewis<br />
&nbsp;<wbr>&nbsp;<wbr>This program comes with ABSOLUTELY NO WARRANTY;&nbsp;<wbr>for details use &#8211;warranty.<br />
&nbsp;<wbr>&nbsp;<wbr>This is free software, and you are welcome to redistribute it under certain<br />
&nbsp;<wbr>&nbsp;<wbr>conditions;&nbsp;<wbr>use &#8211;conditions for details. </p>
<h2>Index</h2>
