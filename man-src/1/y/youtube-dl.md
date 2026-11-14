---
title: "youtube-dl(1)"
name: "youtube-dl"
section: "1"
letter: "y"
url: "/docs/linux/man/1-youtube-dl/"
---

<h2 class="name">NAME</h2>
 

 

 youtube-dl - download videos from youtube.com or other video platforms 

<h2>SYNOPSIS</h2>

 

 youtube-dl [OPTIONS] URL [URL...]

<h2>DESCRIPTION</h2>

 

 youtube-dl is a command-line program to download videos from YouTube.com and a few more sites. It requires the Python interpreter, version 2.6, 2.7, or 3.2+, and it is not platform specific. It should work on your Unix box, on Windows or on macOS. It is released to the public domain, which means you can modify it, redistribute it or use it however you like.

<h2>OPTIONS</h2>

<dl>
<dt>-h, --help
<dd> Print this help text and exit
<dt>--version
<dd> Print program version and exit
<dt>-i, --ignore-errors
<dd> Continue on download errors, for example to skip unavailable videos in a playlist
<dt>--abort-on-error
<dd> Abort downloading of further videos (in the playlist or the command line) if an error occurs
<dt>--dump-user-agent
<dd> Display the current browser identification
<dt>--list-extractors
<dd> List all supported extractors
<dt>--extractor-descriptions
<dd> Output descriptions of all supported extractors
<dt>--force-generic-extractor
<dd> Force extraction to use the generic extractor
<dt>--default-search PREFIX
<dd> Use this prefix for unqualified URLs. For example &quot;gvsearch2:&quot; downloads two videos from google videos for youtube- dl &quot;large apple&quot;. Use the value &quot;auto&quot; to let youtube-dl guess (&quot;auto_warning&quot; to emit a warning when guessing). &quot;error&quot; just throws an error. The default value &quot;fixup_error&quot; repairs broken URLs, but emits an error if this is not possible instead of searching.
<dt>--ignore-config
<dd> Do not read configuration files. When given in the global configuration file /etc/youtube-dl.conf: Do not read the user configuration in ~/.config/youtube-dl/config (%APPDATA%/youtube-dl/config.txt on Windows)
<dt>--config-location PATH
<dd> Location of the configuration file; either the path to the config or its containing directory.
<dt>--flat-playlist
<dd> Do not extract the videos of a playlist, only list them.
<dt>--mark-watched
<dd> Mark videos watched (YouTube only)
<dt>--no-mark-watched
<dd> Do not mark videos watched (YouTube only)
<dt>--no-color
<dd> Do not emit color codes in output</dl>

<h3>Network Options:</h3>

<dl>
<dt>--proxy URL
<dd> Use the specified HTTP/HTTPS/SOCKS proxy. To enable SOCKS proxy, specify a proper scheme. For example socks5://127.0.0.1:1080/. Pass in an empty string (--proxy &quot;&quot;) for direct connection
<dt>--socket-timeout SECONDS
<dd> Time to wait before giving up, in seconds
<dt>--source-address IP
<dd> Client-side IP address to bind to
<dt>-4, --force-ipv4
<dd> Make all connections via IPv4
<dt>-6, --force-ipv6
<dd> Make all connections via IPv6</dl>

<h3>Geo Restriction:</h3>

<dl>
<dt>--geo-verification-proxy URL
<dd> Use this proxy to verify the IP address for some geo-restricted sites. The default proxy specified by --proxy (or none, if the option is not present) is used for the actual downloading.
<dt>--geo-bypass
<dd> Bypass geographic restriction via faking X-Forwarded-For HTTP header
<dt>--no-geo-bypass
<dd> Do not bypass geographic restriction via faking X-Forwarded-For HTTP header
<dt>--geo-bypass-country CODE
<dd> Force bypass geographic restriction with explicitly provided two-letter ISO 3166-2 country code
<dt>--geo-bypass-ip-block IP_BLOCK
<dd> Force bypass geographic restriction with explicitly provided IP block in CIDR notation</dl>

<h3>Video Selection:</h3>

<dl>
<dt>--playlist-start NUMBER
<dd> Playlist video to start at (default is 1)
<dt>--playlist-end NUMBER
<dd> Playlist video to end at (default is last)
<dt>--playlist-items ITEM_SPEC
<dd> Playlist video items to download. Specify indices of the videos in the playlist separated by commas like: &quot;-- playlist-items 1,2,5,8&quot; if you want to download videos indexed 1, 2, 5, 8 in the playlist. You can specify range: &quot; --playlist-items 1-3,7,10-13&quot;, it will download the videos at index 1, 2, 3, 7, 10, 11, 12 and 13.
<dt>--match-title REGEX
<dd> Download only matching titles (regex or caseless sub-string)
<dt>--reject-title REGEX
<dd> Skip download for matching titles (regex or caseless sub-string)
<dt>--max-downloads NUMBER
<dd> Abort after downloading NUMBER files
<dt>--min-filesize SIZE
<dd> Do not download any videos smaller than SIZE (e.g. 50k or 44.6m)
<dt>--max-filesize SIZE
<dd> Do not download any videos larger than SIZE (e.g. 50k or 44.6m)
<dt>--date DATE
<dd> Download only videos uploaded in this date
<dt>--datebefore DATE
<dd> Download only videos uploaded on or before this date (i.e. inclusive)
<dt>--dateafter DATE
<dd> Download only videos uploaded on or after this date (i.e. inclusive)
<dt>--min-views COUNT
<dd> Do not download any videos with less than COUNT views
<dt>--max-views COUNT
<dd> Do not download any videos with more than COUNT views
<dt>--match-filter FILTER
<dd> Generic video filter. Specify any key (see the &quot;OUTPUT TEMPLATE&quot; for a list of available keys) to match if the key is present, !key to check if the key is not present, key &gt; NUMBER (like &quot;comment_count &gt; 12&quot;, also works with &gt;=, &lt;, &lt;=, !=, =) to compare against a number, key = 'LITERAL' (like &quot;uploader = 'Mike Smith'&quot;, also works with !=) to match against a string literal and &amp; to require multiple matches. Values which are not known are excluded unless you put a question mark (?) after the operator. For example, to only match videos that have been liked more than 100 times and disliked less than 50 times (or the dislike functionality is not available at the given service), but who also have a description, use --match-filter &quot;like_count &gt; 100 &amp; dislike_count &lt;? 50 &amp; description&quot; .
<dt>--no-playlist
<dd> Download only the video, if the URL refers to a video and a playlist.
<dt>--yes-playlist
<dd> Download the playlist, if the URL refers to a video and a playlist.
<dt>--age-limit YEARS
<dd> Download only videos suitable for the given age
<dt>--download-archive FILE
<dd> Download only videos not listed in the archive file. Record the IDs of all downloaded videos in it.
<dt>--include-ads
<dd> Download advertisements as well (experimental)</dl>

<h3>Download Options:</h3>

<dl>
<dt>-r, --limit-rate RATE
<dd> Maximum download rate in bytes per second (e.g. 50K or 4.2M)
<dt>-R, --retries RETRIES
<dd> Number of retries (default is 10), or &quot;infinite&quot;.
<dt>--fragment-retries RETRIES
<dd> Number of retries for a fragment (default is 10), or &quot;infinite&quot; (DASH, hlsnative and ISM)
<dt>--skip-unavailable-fragments
<dd> Skip unavailable fragments (DASH, hlsnative and ISM)
<dt>--abort-on-unavailable-fragment
<dd> Abort downloading when some fragment is not available
<dt>--keep-fragments
<dd> Keep downloaded fragments on disk after downloading is finished; fragments are erased by default
<dt>--buffer-size SIZE
<dd> Size of download buffer (e.g. 1024 or 16K) (default is 1024)
<dt>--no-resize-buffer
<dd> Do not automatically adjust the buffer size. By default, the buffer size is automatically resized from an initial value of SIZE.
<dt>--http-chunk-size SIZE
<dd> Size of a chunk for chunk-based HTTP downloading (e.g. 10485760 or 10M) (default is disabled). May be useful for bypassing bandwidth throttling imposed by a webserver (experimental)
<dt>--playlist-reverse
<dd> Download playlist videos in reverse order
<dt>--playlist-random
<dd> Download playlist videos in random order
<dt>--xattr-set-filesize
<dd> Set file xattribute ytdl.filesize with expected file size
<dt>--hls-prefer-native
<dd> Use the native HLS downloader instead of ffmpeg
<dt>--hls-prefer-ffmpeg
<dd> Use ffmpeg instead of the native HLS downloader
<dt>--hls-use-mpegts
<dd> Use the mpegts container for HLS videos, allowing to play the video while downloading (some players may not be able to play it)
<dt>--external-downloader COMMAND
<dd> Use the specified external downloader. Currently supports aria2c,avconv,axel,c url,ffmpeg,httpie,wget
<dt>--external-downloader-args ARGS
<dd> Give these arguments to the external downloader</dl>

<h3>Filesystem Options:</h3>

<dl>
<dt>-a, --batch-file FILE
<dd> File containing URLs to download ('-' for stdin), one URL per line. Lines starting with '#', ';' or ']' are considered as comments and ignored.
<dt>--id
<dd> Use only video ID in file name
<dt>-o, --output TEMPLATE
<dd> Output filename template, see the &quot;OUTPUT TEMPLATE&quot; for all the info
<dt>--output-na-placeholder PLACEHOLDER
<dd> Placeholder value for unavailable meta fields in output filename template (default is &quot;NA&quot;)
<dt>--autonumber-start NUMBER
<dd> Specify the start value for %(autonumber)s (default is 1)
<dt>--restrict-filenames
<dd> Restrict filenames to only ASCII characters, and avoid &quot;&amp;&quot; and spaces in filenames
<dt>-w, --no-overwrites
<dd> Do not overwrite files
<dt>-c, --continue
<dd> Force resume of partially downloaded files. By default, youtube-dl will resume downloads if possible.
<dt>--no-continue
<dd> Do not resume partially downloaded files (restart from beginning)
<dt>--no-part
<dd> Do not use .part files - write directly into output file
<dt>--no-mtime
<dd> Do not use the Last-modified header to set the file modification time
<dt>--write-description
<dd> Write video description to a .description file
<dt>--write-info-json
<dd> Write video metadata to a .info.json file
<dt>--write-annotations
<dd> Write video annotations to a .annotations.xml file
<dt>--load-info-json FILE
<dd> JSON file containing the video information (created with the &quot;--write- info-json&quot; option)
<dt>--cookies FILE
<dd> File to read cookies from and dump cookie jar in
<dt>--cache-dir DIR
<dd> Location in the filesystem where youtube-dl can store some downloaded information permanently. By default $XDG_CACHE_HOME/youtube-dl or ~/.cache/youtube-dl . At the moment, only YouTube player files (for videos with obfuscated signatures) are cached, but that may change.
<dt>--no-cache-dir
<dd> Disable filesystem caching
<dt>--rm-cache-dir
<dd> Delete all filesystem cache files</dl>

<h3>Thumbnail Options:</h3>

<dl>
<dt>--write-thumbnail
<dd> Write thumbnail image to disk
<dt>--write-all-thumbnails
<dd> Write all thumbnail image formats to disk
<dt>--list-thumbnails
<dd> Simulate and list all available thumbnail formats</dl>

<h3>Verbosity / Simulation Options:</h3>

<dl>
<dt>-q, --quiet
<dd> Activate quiet mode
<dt>--no-warnings
<dd> Ignore warnings
<dt>-s, --simulate
<dd> Do not download the video and do not write anything to disk
<dt>--skip-download
<dd> Do not download the video
<dt>-g, --get-url
<dd> Simulate, quiet but print URL
<dt>-e, --get-title
<dd> Simulate, quiet but print title
<dt>--get-id
<dd> Simulate, quiet but print id
<dt>--get-thumbnail
<dd> Simulate, quiet but print thumbnail URL
<dt>--get-description
<dd> Simulate, quiet but print video description
<dt>--get-duration
<dd> Simulate, quiet but print video length
<dt>--get-filename
<dd> Simulate, quiet but print output filename
<dt>--get-format
<dd> Simulate, quiet but print output format
<dt>-j, --dump-json
<dd> Simulate, quiet but print JSON information. See the &quot;OUTPUT TEMPLATE&quot; for a description of available keys.
<dt>-J, --dump-single-json
<dd> Simulate, quiet but print JSON information for each command-line argument. If the URL refers to a playlist, dump the whole playlist information in a single line.
<dt>--print-json
<dd> Be quiet and print the video information as JSON (video is still being downloaded).
<dt>--newline
<dd> Output progress bar as new lines
<dt>--no-progress
<dd> Do not print progress bar
<dt>--console-title
<dd> Display progress in console titlebar
<dt>-v, --verbose
<dd> Print various debugging information
<dt>--dump-pages
<dd> Print downloaded pages encoded using base64 to debug problems (very verbose)
<dt>--write-pages
<dd> Write downloaded intermediary pages to files in the current directory to debug problems
<dt>--print-traffic
<dd> Display sent and read HTTP traffic
<dt>-C, --call-home
<dd> Contact the youtube-dl server for debugging
<dt>--no-call-home
<dd> Do NOT contact the youtube-dl server for debugging</dl>

<h3>Workarounds:</h3>

<dl>
<dt>--encoding ENCODING
<dd> Force the specified encoding (experimental)
<dt>--no-check-certificate
<dd> Suppress HTTPS certificate validation
<dt>--prefer-insecure
<dd> Use an unencrypted connection to retrieve information about the video. (Currently supported only for YouTube)
<dt>--user-agent UA
<dd> Specify a custom user agent
<dt>--referer URL
<dd> Specify a custom referer, use if the video access is restricted to one domain
<dt>--add-header FIELD:VALUE
<dd> Specify a custom HTTP header and its value, separated by a colon ':'. You can use this option multiple times
<dt>--bidi-workaround
<dd> Work around terminals that lack bidirectional text support. Requires bidiv or fribidi executable in PATH
<dt>--sleep-interval SECONDS
<dd> Number of seconds to sleep before each download when used alone or a lower bound of a range for randomized sleep before each download (minimum possible number of seconds to sleep) when used along with --max-sleep-interval.
<dt>--max-sleep-interval SECONDS
<dd> Upper bound of a range for randomized sleep before each download (maximum possible number of seconds to sleep). Must only be used along with --min- sleep-interval.</dl>

<h3>Video Format Options:</h3>

<dl>
<dt>-f, --format FORMAT
<dd> Video format code, see the &quot;FORMAT SELECTION&quot; for all the info
<dt>--all-formats
<dd> Download all available video formats
<dt>--prefer-free-formats
<dd> Prefer free video formats unless a specific one is requested
<dt>-F, --list-formats
<dd> List all available formats of requested videos
<dt>--youtube-skip-dash-manifest
<dd> Do not download the DASH manifests and related data on YouTube videos
<dt>--merge-output-format FORMAT
<dd> If a merge is required (e.g. bestvideo+bestaudio), output to given container format. One of mkv, mp4, ogg, webm, flv. Ignored if no merge is required</dl>

<h3>Subtitle Options:</h3>

<dl>
<dt>--write-sub
<dd> Write subtitle file
<dt>--write-auto-sub
<dd> Write automatically generated subtitle file (YouTube only)
<dt>--all-subs
<dd> Download all the available subtitles of the video
<dt>--list-subs
<dd> List all available subtitles for the video
<dt>--sub-format FORMAT
<dd> Subtitle format, accepts formats preference, for example: &quot;srt&quot; or &quot;ass/srt/best&quot;
<dt>--sub-lang LANGS
<dd> Languages of the subtitles to download (optional) separated by commas, use --list-subs for available language tags</dl>

<h3>Authentication Options:</h3>

<dl>
<dt>-u, --username USERNAME
<dd> Login with this account ID
<dt>-p, --password PASSWORD
<dd> Account password. If this option is left out, youtube-dl will ask interactively.
<dt>-2, --twofactor TWOFACTOR
<dd> Two-factor authentication code
<dt>-n, --netrc
<dd> Use .netrc authentication data
<dt>--video-password PASSWORD
<dd> Video password (vimeo, youku)</dl>

<h3>Adobe Pass Options:</h3>

<dl>
<dt>--ap-mso MSO
<dd> Adobe Pass multiple-system operator (TV provider) identifier, use --ap-list-mso for a list of available MSOs
<dt>--ap-username USERNAME
<dd> Multiple-system operator account login
<dt>--ap-password PASSWORD
<dd> Multiple-system operator account password. If this option is left out, youtube-dl will ask interactively.
<dt>--ap-list-mso
<dd> List all supported multiple-system operators</dl>

<h3>Post-processing Options:</h3>

<dl>
<dt>-x, --extract-audio
<dd> Convert video files to audio-only files (requires ffmpeg/avconv and ffprobe/avprobe)
<dt>--audio-format FORMAT
<dd> Specify audio format: &quot;best&quot;, &quot;aac&quot;, &quot;flac&quot;, &quot;mp3&quot;, &quot;m4a&quot;, &quot;opus&quot;, &quot;vorbis&quot;, or &quot;wav&quot;; &quot;best&quot; by default; No effect without -x
<dt>--audio-quality QUALITY
<dd> Specify ffmpeg/avconv audio quality, insert a value between 0 (better) and 9 (worse) for VBR or a specific bitrate like 128K (default 5)
<dt>--recode-video FORMAT
<dd> Encode the video to another format if necessary (currently supported: mp4|flv|ogg|webm|mkv|avi)
<dt>--postprocessor-args ARGS
<dd> Give these arguments to the postprocessor
<dt>-k, --keep-video
<dd> Keep the video file on disk after the post-processing; the video is erased by default
<dt>--no-post-overwrites
<dd> Do not overwrite post-processed files; the post-processed files are overwritten by default
<dt>--embed-subs
<dd> Embed subtitles in the video (only for mp4, webm and mkv videos)
<dt>--embed-thumbnail
<dd> Embed thumbnail in the audio as cover art
<dt>--add-metadata
<dd> Write metadata to the video file
<dt>--metadata-from-title FORMAT
<dd> Parse additional metadata like song title / artist from the video title. The format syntax is the same as --output. Regular expression with named capture groups may also be used. The parsed parameters replace existing values. Example: --metadata-from-title &quot;%(artist)s - %(title)s&quot; matches a title like &quot;Coldplay - Paradise&quot;. Example (regex): --metadata-from-title &quot;(?P.+?) - (?P
<dl>
<dt>
<dd> .+)&quot;</dl>

<dt>--xattrs
<dd> Write metadata to the video file's xattrs (using dublin core and xdg standards)
<dt>--fixup POLICY
<dd> Automatically correct known faults of the file. One of never (do nothing), warn (only emit a warning), detect_or_warn (the default; fix file if we can, warn otherwise)
<dt>--prefer-avconv
<dd> Prefer avconv over ffmpeg for running the postprocessors
<dt>--prefer-ffmpeg
<dd> Prefer ffmpeg over avconv for running the postprocessors (default)
<dt>--ffmpeg-location PATH
<dd> Location of the ffmpeg/avconv binary; either the path to the binary or its containing directory.
<dt>--exec CMD
<dd> Execute a command on the file after downloading and post-processing, similar to find's -exec syntax. Example: --exec 'adb push {} /sdcard/Music/ &amp;&amp; rm {}'
<dt>--convert-subs FORMAT
<dd> Convert the subtitles to other format (currently supported: srt|ass|vtt|lrc)</dl>

<h2>CONFIGURATION</h2>

 

 You can configure youtube-dl by placing any supported command line option to a configuration file. On Linux and macOS, the system wide configuration file is located at /etc/youtube-dl.conf and the user wide configuration file at ~/.config/youtube-dl/config. On Windows, the user wide configuration file locations are %APPDATA%\youtube-dl\config.txt or C:\Users\&lt;user name&gt;\youtube-dl.conf. Note that by default configuration file may not exist so you may need to create it yourself. 

 For example, with the following configuration file youtube-dl will always extract the audio, not copy the mtime, use a proxy and save all videos under Movies directory in your home directory:
<dl>
<dt>
<dd> <pre>
# Lines starting with # are comments
# Always extract audio
-x
# Do not copy the mtime
--no-mtime
# Use this proxy
--proxy 127.0.0.1:3128
# Save all videos under Movies directory in your home directory
-o ~/Movies/%(title)s.%(ext)s
</pre></dl>
 

 Note that options in configuration file are just the same options aka switches used in regular command line calls thus there must be no whitespace after - or --, e.g. -o or --proxy but not - o or -- proxy. 

 You can use --ignore-config if you want to disable the configuration file for a particular youtube-dl run. 

 You can also use --config-location if you want to use custom configuration file for a particular youtube-dl run.

<h3>Authentication with .netrc file</h3>

 

 You may also want to configure automatic credentials storage for extractors that support authentication (by providing login and password with --username and --password) in order not to pass credentials as command line arguments on every youtube-dl execution and prevent tracking plain text passwords in the shell command history. You can achieve this using a .netrc file (<a rel="nofollow" HREF="https://stackoverflow.com/tags/.netrc/info)">https://stackoverflow.com/tags/.netrc/info)</a> on a per extractor basis. For that you will need to create a .netrc file in your $HOME and restrict permissions to read/write by only you:
<dl>
<dt>
<dd> <pre>
touch $HOME/.netrc
chmod a-rwx,u+rw $HOME/.netrc
</pre></dl>
 

 After that you can add credentials for an extractor in the following format, where extractor is the name of the extractor in lowercase:
<dl>
<dt>
<dd> <pre>
machine &lt;extractor&gt; login &lt;login&gt; password &lt;password&gt;
</pre></dl>
 

 For example:
<dl>
<dt>
<dd> <pre>
machine youtube login myaccount [at] gmail.com password my_youtube_password
machine twitch login my_twitch_account_name password my_twitch_password
</pre></dl>
 

 To activate authentication with the .netrc file you should pass --netrc to youtube-dl or place it in the configuration file. 

 On Windows you may also need to setup the %HOME% environment variable manually. For example:
<dl>
<dt>
<dd> <pre>
set HOME=%USERPROFILE%
</pre></dl>

<h2>OUTPUT TEMPLATE</h2>

 

 The -o option allows users to indicate a template for the output file names. 

 tl;dr: navigate me to examples. 

 The basic usage is not to set any template arguments when downloading a single file, like in youtube-dl -o funny_video.flv &quot;<a rel="nofollow" HREF="https://some/video">https://some/video</a>&quot;. However, it may contain special sequences that will be replaced when downloading each video. The special sequences may be formatted according to python string formatting operations (<a rel="nofollow" HREF="https://docs.python.org/2/library/stdtypes.html#string-formatting">https://docs.python.org/2/library/stdtypes.html#string-formatting</a>). For example, %(NAME)s or %(NAME)05d. To clarify, that is a percent symbol followed by a name in parentheses, followed by formatting operations. Allowed names along with sequence type are:
<dl>
<dt>&bull;
<dd> id (string): Video identifier
<dt>&bull;
<dd> title (string): Video title
<dt>&bull;
<dd> url (string): Video URL
<dt>&bull;
<dd> ext (string): Video filename extension
<dt>&bull;
<dd> alt_title (string): A secondary title of the video
<dt>&bull;
<dd> display_id (string): An alternative identifier for the video
<dt>&bull;
<dd> uploader (string): Full name of the video uploader
<dt>&bull;
<dd> license (string): License name the video is licensed under
<dt>&bull;
<dd> creator (string): The creator of the video
<dt>&bull;
<dd> release_date (string): The date (YYYYMMDD) when the video was released
<dt>&bull;
<dd> timestamp (numeric): UNIX timestamp of the moment the video became available
<dt>&bull;
<dd> upload_date (string): Video upload date (YYYYMMDD)
<dt>&bull;
<dd> uploader_id (string): Nickname or id of the video uploader
<dt>&bull;
<dd> channel (string): Full name of the channel the video is uploaded on
<dt>&bull;
<dd> channel_id (string): Id of the channel
<dt>&bull;
<dd> location (string): Physical location where the video was filmed
<dt>&bull;
<dd> duration (numeric): Length of the video in seconds
<dt>&bull;
<dd> view_count (numeric): How many users have watched the video on the platform
<dt>&bull;
<dd> like_count (numeric): Number of positive ratings of the video
<dt>&bull;
<dd> dislike_count (numeric): Number of negative ratings of the video
<dt>&bull;
<dd> repost_count (numeric): Number of reposts of the video
<dt>&bull;
<dd> average_rating (numeric): Average rating give by users, the scale used depends on the webpage
<dt>&bull;
<dd> comment_count (numeric): Number of comments on the video
<dt>&bull;
<dd> age_limit (numeric): Age restriction for the video (years)
<dt>&bull;
<dd> is_live (boolean): Whether this video is a live stream or a fixed-length video
<dt>&bull;
<dd> start_time (numeric): Time in seconds where the reproduction should start, as specified in the URL
<dt>&bull;
<dd> end_time (numeric): Time in seconds where the reproduction should end, as specified in the URL
<dt>&bull;
<dd> format (string): A human-readable description of the format
<dt>&bull;
<dd> format_id (string): Format code specified by --format
<dt>&bull;
<dd> format_note (string): Additional info about the format
<dt>&bull;
<dd> width (numeric): Width of the video
<dt>&bull;
<dd> height (numeric): Height of the video
<dt>&bull;
<dd> resolution (string): Textual description of width and height
<dt>&bull;
<dd> tbr (numeric): Average bitrate of audio and video in KBit/s
<dt>&bull;
<dd> abr (numeric): Average audio bitrate in KBit/s
<dt>&bull;
<dd> acodec (string): Name of the audio codec in use
<dt>&bull;
<dd> asr (numeric): Audio sampling rate in Hertz
<dt>&bull;
<dd> vbr (numeric): Average video bitrate in KBit/s
<dt>&bull;
<dd> fps (numeric): Frame rate
<dt>&bull;
<dd> vcodec (string): Name of the video codec in use
<dt>&bull;
<dd> container (string): Name of the container format
<dt>&bull;
<dd> filesize (numeric): The number of bytes, if known in advance
<dt>&bull;
<dd> filesize_approx (numeric): An estimate for the number of bytes
<dt>&bull;
<dd> protocol (string): The protocol that will be used for the actual download
<dt>&bull;
<dd> extractor (string): Name of the extractor
<dt>&bull;
<dd> extractor_key (string): Key name of the extractor
<dt>&bull;
<dd> epoch (numeric): Unix epoch when creating the file
<dt>&bull;
<dd> autonumber (numeric): Number that will be increased with each download, starting at --autonumber-start
<dt>&bull;
<dd> playlist (string): Name or id of the playlist that contains the video
<dt>&bull;
<dd> playlist_index (numeric): Index of the video in the playlist padded with leading zeros according to the total length of the playlist
<dt>&bull;
<dd> playlist_id (string): Playlist identifier
<dt>&bull;
<dd> playlist_title (string): Playlist title
<dt>&bull;
<dd> playlist_uploader (string): Full name of the playlist uploader
<dt>&bull;
<dd> playlist_uploader_id (string): Nickname or id of the playlist uploader</dl>
 

 Available for the video that belongs to some logical chapter or section:
<dl>
<dt>&bull;
<dd> chapter (string): Name or title of the chapter the video belongs to
<dt>&bull;
<dd> chapter_number (numeric): Number of the chapter the video belongs to
<dt>&bull;
<dd> chapter_id (string): Id of the chapter the video belongs to</dl>
 

 Available for the video that is an episode of some series or programme:
<dl>
<dt>&bull;
<dd> series (string): Title of the series or programme the video episode belongs to
<dt>&bull;
<dd> season (string): Title of the season the video episode belongs to
<dt>&bull;
<dd> season_number (numeric): Number of the season the video episode belongs to
<dt>&bull;
<dd> season_id (string): Id of the season the video episode belongs to
<dt>&bull;
<dd> episode (string): Title of the video episode
<dt>&bull;
<dd> episode_number (numeric): Number of the video episode within a season
<dt>&bull;
<dd> episode_id (string): Id of the video episode</dl>
 

 Available for the media that is a track or a part of a music album:
<dl>
<dt>&bull;
<dd> track (string): Title of the track
<dt>&bull;
<dd> track_number (numeric): Number of the track within an album or a disc
<dt>&bull;
<dd> track_id (string): Id of the track
<dt>&bull;
<dd> artist (string): Artist(s) of the track
<dt>&bull;
<dd> genre (string): Genre(s) of the track
<dt>&bull;
<dd> album (string): Title of the album the track belongs to
<dt>&bull;
<dd> album_type (string): Type of the album
<dt>&bull;
<dd> album_artist (string): List of all artists appeared on the album
<dt>&bull;
<dd> disc_number (numeric): Number of the disc or other physical medium the track belongs to
<dt>&bull;
<dd> release_year (numeric): Year (YYYY) when the album was released</dl>
 

 Each aforementioned sequence when referenced in an output template will be replaced by the actual value corresponding to the sequence name. Note that some of the sequences are not guaranteed to be present since they depend on the metadata obtained by a particular extractor. Such sequences will be replaced with placeholder value provided with --output-na-placeholder (NA by default). 

 For example for -o %(title)s-%(id)s.%(ext)s and an mp4 video with title youtube-dl test video and id BaW_jenozKcj, this will result in a youtube-dl test video-BaW_jenozKcj.mp4 file created in the current directory. 

 For numeric sequences you can use numeric related formatting, for example, %(view_count)05d will result in a string with view count padded with zeros up to 5 characters, like in 00042. 

 Output templates can also contain arbitrary hierarchical path, e.g. -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' which will result in downloading each video in a directory corresponding to this path template. Any missing directory will be automatically created for you. 

 To use percent literals in an output template use %%. To output to stdout use -o -. 

 The current default template is %(title)s-%(id)s.%(ext)s. 

 In some cases, you don't want special characters such as 2D, spaces, or &amp;, such as when transferring the downloaded filename to a Windows system or the filename through an 8bit-unsafe channel. In these cases, add the --restrict-filenames flag to get a shorter title:

<h3>Output template and Windows batch files</h3>

 

 If you are using an output template inside a Windows batch file then you must escape plain percent characters (%) by doubling, so that -o &quot;%(title)s-%(id)s.%(ext)s&quot; should become -o &quot;%%(title)s-%%(id)s.%%(ext)s&quot;. However you should not touch %'s that are not plain characters, e.g. environment variables for expansion should stay intact: -o &quot;C:\%HOMEPATH%\Desktop\%%(title)s.%%(ext)s&quot;.

<h3>Output template examples</h3>

 

 Note that on Windows you may need to use double quotes instead of single.
<dl>
<dt>
<dd> <pre><code>
$ youtube - dl-- get - filename - o '%(title)s.%(ext)s' BaW_jenozKc youtube - dl test video ''_ &amp;auml;
AD50.mp4 #All kinds of weird characters
        $ youtube -
    dl-- get - filename - o '%(title)s.%(ext)s' BaW_jenozKc-- restrict - filenames youtube - dl_test_video_.mp4 #A simple file name
#Download YouTube playlist videos in separate directory indexed by video order in a playlist
                                                                                                 $ youtube -
    dl - o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https : // www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re
#Download all playlists of YouTube channel / user keeping each playlist in separate directory:
                                                                         $ youtube -
                                                                         dl - o '%(uploader)s/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https : // www.youtube.com/user/TheLinuxFoundation/playlists
#Download Udemy course keeping each chapter in separate directory under MyVideos directory in your home
                                                                                                                                                           $ youtube -
                                                                                                                                                           dl - u user - p password - o '~/MyVideos/%(playlist)s/%(chapter_number)s - %(chapter)s/%(title)s.%(ext)s' https : // www.udemy.com/java-tutorial/
#Download entire series season keeping each series and each season in separate directory under C : / MyVideos
                                                                                                                                                                                                                                                                             $ youtube -
                                                                                                                                                                                                                                                                             dl - o "C:/MyVideos/%(series)s/%(season_number)s - %(season)s/%(episode_number)s - %(episode)s.%(ext)s" https : // videomore.ru/kino_v_detalayah/5_sezon/367617
#Stream the video being downloaded to stdout
                                                                                                                                                                                                                                                                                                                                                                                             $ youtube -
                                                                                                                                                                                                                                                                                                                                                                                             dl - o - BaW_jenozKc
</code></pre></dl>

<h2>FORMAT SELECTION</h2>

 

 By default youtube-dl tries to download the best available quality, i.e. if you want the best quality you don't need to pass any special options, youtube-dl will guess it for you by default. 

 But sometimes you may want to download in a different format, for example when you are on a slow or intermittent connection. The key mechanism for achieving this is so-called format selection based on which you can explicitly specify desired format, select formats based on some criterion or criteria, setup precedence and much more. 

 The general syntax for format selection is --format FORMAT or shorter -f FORMAT where FORMAT is a selector expression, i.e. an expression that describes format or formats you would like to download. 

 tl;dr: navigate me to examples. 

 The simplest case is requesting a specific format, for example with -f 22 you can download the format with format code equal to 22. You can get the list of available format codes for particular video using --list-formats or -F. Note that these format codes are extractor specific. 

 You can also use a file extension (currently 3gp, aac, flv, m4a, mp3, mp4, ogg, wav, webm are supported) to download the best quality format of a particular file extension served as a single file, e.g. -f webm will download the best quality format with the webm extension served as a single file. 

 You can also use special names to select particular edge case formats:
<dl>
<dt>&bull;
<dd> best: Select the best quality format represented by a single file with video and audio.
<dt>&bull;
<dd> worst: Select the worst quality format represented by a single file with video and audio.
<dt>&bull;
<dd> bestvideo: Select the best quality video-only format (e.g. DASH video). May not be available.
<dt>&bull;
<dd> worstvideo: Select the worst quality video-only format. May not be available.
<dt>&bull;
<dd> bestaudio: Select the best quality audio only-format. May not be available.
<dt>&bull;
<dd> worstaudio: Select the worst quality audio only-format. May not be available.</dl>
 

 For example, to download the worst quality video-only format you can use -f worstvideo. 

 If you want to download multiple videos and they don't have the same formats available, you can specify the order of preference using slashes. Note that slash is left-associative, i.e. formats on the left hand side are preferred, for example -f 22/17/18 will download format 22 if it's available, otherwise it will download format 17 if it's available, otherwise it will download format 18 if it's available, otherwise it will complain that no suitable formats are available for download. 

 If you want to download several formats of the same video use a comma as a separator, e.g. -f 22,17,18 will download all these three formats, of course if they are available. Or a more sophisticated example combined with the precedence feature: -f 136/137/mp4/bestvideo,140/m4a/bestaudio. 

 You can also filter the video formats by putting a condition in brackets, as in -f &quot;best[height=720]&quot; (or -f &quot;[filesize&gt;10M]&quot;). 

 The following numeric meta fields can be used with comparisons &lt;, &lt;=, &gt;, &gt;=, = (equals), != (not equals):
<dl>
<dt>&bull;
<dd> filesize: The number of bytes, if known in advance
<dt>&bull;
<dd> width: Width of the video, if known
<dt>&bull;
<dd> height: Height of the video, if known
<dt>&bull;
<dd> tbr: Average bitrate of audio and video in KBit/s
<dt>&bull;
<dd> abr: Average audio bitrate in KBit/s
<dt>&bull;
<dd> vbr: Average video bitrate in KBit/s
<dt>&bull;
<dd> asr: Audio sampling rate in Hertz
<dt>&bull;
<dd> fps: Frame rate</dl>
 

 Also filtering work for comparisons = (equals), ha= (starts with), $= (ends with), *= (contains) and following string meta fields:
<dl>
<dt>&bull;
<dd> ext: File extension
<dt>&bull;
<dd> acodec: Name of the audio codec in use
<dt>&bull;
<dd> vcodec: Name of the video codec in use
<dt>&bull;
<dd> container: Name of the container format
<dt>&bull;
<dd> protocol: The protocol that will be used for the actual download, lower-case (http, https, rtsp, rtmp, rtmpe, mms, f4m, ism, http_dash_segments, m3u8, or m3u8_native)
<dt>&bull;
<dd> format_id: A short description of the format
<dt>&bull;
<dd> language: Language code</dl>
 

 Any string comparison may be prefixed with negation ! in order to produce an opposite comparison, e.g. !*= (does not contain). 

 Note that none of the aforementioned meta fields are guaranteed to be present since this solely depends on the metadata obtained by particular extractor, i.e. the metadata offered by the video hoster. 

 Formats for which the value is not known are excluded unless you put a question mark (?) after the operator. You can combine format filters, so -f &quot;[height &lt;=? 720][tbr&gt;500]&quot; selects up to 720p videos (or videos where the height is not known) with a bitrate of at least 500 KBit/s. 

 You can merge the video and audio of two formats into a single file using -f &lt;video-format&gt;+&lt;audio-format&gt; (requires ffmpeg or avconv installed), for example -f bestvideo+bestaudio will download the best video-only format, the best audio-only format and mux them together with ffmpeg/avconv. 

 Format selectors can also be grouped using parentheses, for example if you want to download the best mp4 and webm formats with a height lower than 480 you can use -f '(mp4,webm)[height&lt;480]'. 

 Since the end of April 2015 and version 2015.04.26, youtube-dl uses -f bestvideo+bestaudio/best as the default format selection (see #5447 (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/issues/5447">https://github.com/ytdl-org/youtube-dl/issues/5447</a>), #5456 (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/issues/5456)">https://github.com/ytdl-org/youtube-dl/issues/5456)</a>). If ffmpeg or avconv are installed this results in downloading bestvideo and bestaudio separately and muxing them together into a single file giving the best overall quality available. Otherwise it falls back to best and results in downloading the best available quality served as a single file. best is also needed for videos that don't come from YouTube because they don't provide the audio and video in two different files. If you want to only download some DASH formats (for example if you are not interested in getting videos with a resolution higher than 1080p), you can add -f bestvideo[height&lt;=?1080]+bestaudio/best to your configuration file. Note that if you use youtube-dl to stream to stdout (and most likely to pipe it to your media player then), i.e. you explicitly specify output template as -o -, youtube-dl still uses -f best format selection in order to start content delivery immediately to your player and not to wait until bestvideo and bestaudio are downloaded and muxed. 

 If you want to preserve the old format selection behavior (prior to youtube-dl 2015.04.26), i.e. you want to download the best available quality media served as a single file, you should explicitly specify your choice with -f best. You may want to add it to the configuration file in order not to type it every time you run youtube-dl.

<h3>Format selection examples</h3>

 

 Note that on Windows you may need to use double quotes instead of single.
<dl>
<dt>
<dd> 
#Download best mp4 format available or any other best if no mp4 available
$ youtube - dl - f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
#Download best format available but no better than 480p
    $ youtube -
    dl - f 'bestvideo[height&lt;=480]+bestaudio/best[height&lt;=480]'
#Download best video only format but no bigger than 50 MB
    $ youtube -
    dl - f 'best[filesize&lt;50M]'
#Download best format available via direct link over HTTP / HTTPS protocol
    $ youtube -
    dl - f '(bestvideo+bestaudio/best)[protocolha=http]'
#Download the best video format and the best audio format without merging them
    $ youtube -
    dl - f 'bestvideo,bestaudio' - o '%(title)s.f%(format_id)s.%(ext)s'
</dl>
 

 Note that in the last example, an output template is recommended as bestvideo and bestaudio may have the same file name.

<h2>VIDEO SELECTION</h2>

 

 Videos can be filtered by their upload date using the options --date, --datebefore or --dateafter. They accept dates in two formats:
<dl>
<dt>&bull;
<dd> Absolute dates: Dates in the format YYYYMMDD.
<dt>&bull;
<dd> Relative dates: Dates in the format (now|today)[+-][0-9](day|week|month|year)(s)?</dl>
 

 Examples:
<dl>
<dt>
<dd> 
#Download only the videos uploaded in the last 6 months
$ youtube - dl-- dateafter now - 6months
#Download only the videos uploaded on January 1, 1970
    $ youtube -
    dl-- date 19700101 $ #Download only the videos uploaded in the 200x decade
        $ youtube -
    dl-- dateafter 20000101 --datebefore 20091231
</dl>

<h2>FAQ</h2>

<h3>How do I update youtube-dl?</h3>

 

 If you've followed our manual installation instructions (<a rel="nofollow" HREF="https://ytdl-org.github.io/youtube-dl/download.html">https://ytdl-org.github.io/youtube-dl/download.html</a>), you can simply run youtube-dl -U (or, on Linux, sudo youtube-dl -U). 

 If you have used pip, a simple sudo pip install -U youtube-dl is sufficient to update. 

 If you have installed youtube-dl using a package manager like apt-get or yum, use the standard system update mechanism to update. Note that distribution packages are often outdated. As a rule of thumb, youtube-dl releases at least once a month, and often weekly or even daily. Simply go to <a rel="nofollow" HREF="https://yt-dl.org">https://yt-dl.org</a> to find out the current version. Unfortunately, there is nothing we youtube-dl developers can do if your distribution serves a really outdated version. You can (and should) complain to your distribution in their bugtracker or support forum. 

 As a last resort, you can also uninstall the version installed by your package manager and follow our manual installation instructions. For that, remove the distribution's package, with a line like
<dl>
<dt>
<dd> <pre>
sudo apt-get remove -y youtube-dl
</pre></dl>
 

 Afterwards, simply follow our manual installation instructions (<a rel="nofollow" HREF="https://ytdl-org.github.io/youtube-dl/download.html">https://ytdl-org.github.io/youtube-dl/download.html</a>):
<dl>
<dt>
<dd> <pre>
sudo wget <a rel="nofollow" HREF="https://yt-dl.org/downloads/latest/youtube-dl">https://yt-dl.org/downloads/latest/youtube-dl</a> -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
hash -r
</pre></dl>
 

 Again, from then on you'll be able to update with sudo youtube-dl -U.

<h3>youtube-dl is extremely slow to start on Windows</h3>

 

 Add a file exclusion for youtube-dl.exe in Windows Defender settings.

<h3>I'm getting an error Unable to extract OpenGraph title on YouTube playlists</h3>

 

 YouTube changed their playlist format in March 2014 and later on, so you'll need at least youtube-dl 2014.07.25 to download all YouTube videos. 

 If you have installed youtube-dl with a package manager, pip, setup.py or a tarball, please use that to update. Note that Ubuntu packages do not seem to get updated anymore. Since we are not affiliated with Ubuntu, there is little we can do. Feel free to report bugs (<a rel="nofollow" HREF="https://bugs.launchpad.net/ubuntu/+source/youtube-dl/+filebug)">https://bugs.launchpad.net/ubuntu/+source/youtube-dl/+filebug)</a> to the Ubuntu packaging people (mailto:ubuntu-motu [at] lists.ubuntu.com?subject=outdated%20version%20of%20youtube-dl) - all they have to do is update the package to a somewhat recent version. See above for a way to update.

<h3>I'm getting an error when trying to use output template: error: using output template conflicts with using title, video ID or auto number</h3>

 

 Make sure you are not using -o with any of these options -t, --title, --id, -A or --auto-number set in command line or in a configuration file. Remove the latter if any.

<h3>Do I always have to pass -citw?</h3>

 

 By default, youtube-dl intends to have the best options (incidentally, if you have a convincing case that these should be different, please file an issue where you explain that (<a rel="nofollow" HREF="https://yt-dl.org/bug)">https://yt-dl.org/bug)</a>). Therefore, it is unnecessary and sometimes harmful to copy long option strings from webpages. In particular, the only option out of -citw that is regularly useful is -i.

<h3>Can you please put the -b option back?</h3>

 

 Most people asking this question are not aware that youtube-dl now defaults to downloading the highest available quality as reported by YouTube, which will be 1080p or 720p in some cases, so you no longer need the -b option. For some specific videos, maybe YouTube does not report them to be available in a specific high quality format you're interested in. In that case, simply request it with the -f option and youtube-dl will try to download it.

<h3>I get HTTP error 402 when trying to download a video. What's this?</h3>

 

 Apparently YouTube requires you to pass a CAPTCHA test if you download too much. We're considering to provide a way to let you solve the CAPTCHA (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/issues/154">https://github.com/ytdl-org/youtube-dl/issues/154</a>), but at the moment, your best course of action is pointing a web browser to the youtube URL, solving the CAPTCHA, and restart youtube-dl.

<h3>Do I need any other programs?</h3>

 

 youtube-dl works fine on its own on most sites. However, if you want to convert video/audio, you'll need avconv (<a rel="nofollow" HREF="https://libav.org/)">https://libav.org/)</a> or ffmpeg (<a rel="nofollow" HREF="https://www.ffmpeg.org/">https://www.ffmpeg.org/</a>). On some sites - most notably YouTube - videos can be retrieved in a higher quality format without sound. youtube-dl will detect whether avconv/ffmpeg is present and automatically pick the best option. 

 Videos or video formats streamed via RTMP protocol can only be downloaded when rtmpdump (<a rel="nofollow" HREF="https://rtmpdump.mplayerhq.hu/)">https://rtmpdump.mplayerhq.hu/)</a> is installed. Downloading MMS and RTSP videos requires either mplayer (<a rel="nofollow" HREF="https://mplayerhq.hu/)">https://mplayerhq.hu/)</a> or mpv (<a rel="nofollow" HREF="https://mpv.io/)">https://mpv.io/)</a> to be installed.

<h3>I have downloaded a video but how can I play it?</h3>

 

 Once the video is fully downloaded, use any video player, such as mpv (<a rel="nofollow" HREF="https://mpv.io/">https://mpv.io/</a>), vlc (<a rel="nofollow" HREF="https://www.videolan.org/)">https://www.videolan.org/)</a> or mplayer (<a rel="nofollow" HREF="https://www.mplayerhq.hu/">https://www.mplayerhq.hu/</a>).

<h3>I extracted a video URL with -g, but it does not play on another machine / in my web browser.</h3>

 

 It depends a lot on the service. In many cases, requests for the video (to download/play it) must come from the same IP address and with the same cookies and/or HTTP headers. Use the --cookies option to write the required cookies into a file, and advise your downloader to read cookies from that file. Some sites also require a common user agent to be used, use --dump-user-agent to see the one in use by youtube-dl. You can also get necessary cookies and HTTP headers from JSON output obtained with --dump-json. 

 It may be beneficial to use IPv6; in some cases, the restrictions are only applied to IPv4. Some services (sometimes only for a subset of videos) do not restrict the video URL by IP address, cookie, or user-agent, but these are the exception rather than the rule. 

 Please bear in mind that some URL protocols are not supported by browsers out of the box, including RTMP. If you are using -g, your own downloader must support these as well. 

 If you want to play the video on a machine that is not running youtube-dl, you can relay the video content from the machine that runs youtube-dl. You can use -o - to let youtube-dl stream a video to stdout, or simply allow the player to download the files written by youtube-dl in turn.

<h3>ERROR: no fmt_url_map or conn information found in video info</h3>

 

 YouTube has switched to a new video info format in July 2011 which is not supported by old versions of youtube-dl. See above for how to update youtube-dl.

<h3>ERROR: unable to download video</h3>

 

 YouTube requires an additional signature since September 2012 which is not supported by old versions of youtube-dl. See above for how to update youtube-dl.

<h3>Video URL contains an ampersand and I'm getting some strange output [1] 2839 or 'v' is not recognized as an internal or external command</h3>

 

 That's actually the output from your shell. Since ampersand is one of the special shell characters it's interpreted by the shell preventing you from passing the whole URL to youtube-dl. To disable your shell from interpreting the ampersands (or any other special characters) you have to either put the whole URL in quotes or escape them with a backslash (which approach will work depends on your shell). 

 For example if your URL is <a rel="nofollow" HREF="https://www.youtube.com/watch?t=4">https://www.youtube.com/watch?t=4</a>&amp;v=BaW_jenozKc you should end up with following command: 

 youtube-dl '<a rel="nofollow" HREF="https://www.youtube.com/watch?t=4">https://www.youtube.com/watch?t=4</a>&amp;v=BaW_jenozKc' 

 or 

 youtube-dl <a rel="nofollow" HREF="https://www.youtube.com/watch?t=4\">https://www.youtube.com/watch?t=4\</a>&amp;v=BaW_jenozKc 

 For Windows you have to use the double quotes: 

 youtube-dl &quot;<a rel="nofollow" HREF="https://www.youtube.com/watch?t=4">https://www.youtube.com/watch?t=4</a>&amp;v=BaW_jenozKc&quot;

<h3>ExtractorError: Could not find JS function u'OF'</h3>

 

 In February 2015, the new YouTube player contained a character sequence in a string that was misinterpreted by old versions of youtube-dl. See above for how to update youtube-dl.

<h3>HTTP Error 429: Too Many Requests or 402: Payment Required</h3>

 

 These two error codes indicate that the service is blocking your IP address because of overuse. Usually this is a soft block meaning that you can gain access again after solving CAPTCHA. Just open a browser and solve a CAPTCHA the service suggests you and after that pass cookies to youtube-dl. Note that if your machine has multiple external IPs then you should also pass exactly the same IP you've used for solving CAPTCHA with --source-address. Also you may need to pass a User-Agent HTTP header of your browser with --user-agent. 

 If this is not the case (no CAPTCHA suggested to solve by the service) then you can contact the service and ask them to unblock your IP address, or - if you have acquired a whitelisted IP address already - use the --proxy or --source-address options to select another IP address.

<h3>SyntaxError: Non-ASCII character</h3>

 

 The error
<dl>
<dt>
<dd> <pre>
File &quot;youtube-dl&quot;, line 2
SyntaxError: Non-ASCII character '\x93' ...
</pre></dl>
 

 means you're using an outdated version of Python. Please update to Python 2.6 or 2.7.

<h3>What is this binary file? Where has the code gone?</h3>

 

 Since June 2012 (#342 (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/issues/342))">https://github.com/ytdl-org/youtube-dl/issues/342))</a> youtube-dl is packed as an executable zipfile, simply unzip it (might need renaming to youtube-dl.zip first on some systems) or clone the git repository, as laid out above. If you modify the code, you can run it by executing the __main__.py file. To recompile the executable, run make youtube-dl.

<h3>The exe throws an error due to missing MSVCR100.dll</h3>

 

 To run the exe you need to install first the Microsoft Visual C++ 2010 Service Pack 1 Redistributable Package (x86) (<a rel="nofollow" HREF="https://download.microsoft.com/download/1/6/5/165255E7-1014-4D0A-B094-B6A430A6BFFC/vcredist_x86.exe">https://download.microsoft.com/download/1/6/5/165255E7-1014-4D0A-B094-B6A430A6BFFC/vcredist_x86.exe</a>).

<h3>On Windows, how should I set up ffmpeg and youtube-dl? Where should I put the exe files?</h3>

 

 If you put youtube-dl and ffmpeg in the same directory that you're running the command from, it will work, but that's rather cumbersome. 

 To make a different directory work - either for ffmpeg, or for youtube-dl, or for both - simply create the directory (say, C:\bin, or C:\Users\&lt;User name&gt;\bin), put all the executables directly in there, and then set your PATH environment variable (<a rel="nofollow" HREF="https://www.java.com/en/download/help/path.xml)">https://www.java.com/en/download/help/path.xml)</a> to include that directory. 

 From then on, after restarting your shell, you will be able to access both youtube-dl and ffmpeg (and youtube-dl will be able to find ffmpeg) by simply typing youtube-dl or ffmpeg, no matter what directory you're in.

<h3>How do I put downloads into a specific folder?</h3>

 

 Use the -o to specify an output template, for example -o &quot;/home/user/videos/%(title)s-%(id)s.%(ext)s&quot;. If you want this for all of your downloads, put the option into your configuration file.

<h3>How do I download a video starting with a -?</h3>

 

 Either prepend <a rel="nofollow" HREF="https://www.youtube.com/watch?v=">https://www.youtube.com/watch?v=</a> or separate the ID from the options with --:
<dl>
<dt>
<dd> <pre>
youtube-dl -- -wNyEUrxzFU
youtube-dl &quot;<a rel="nofollow" HREF="https://www.youtube.com/watch?v=-wNyEUrxzFU">https://www.youtube.com/watch?v=-wNyEUrxzFU</a>&quot;
</pre></dl>

<h3>How do I pass cookies to youtube-dl?</h3>

 

 Use the --cookies option, for example --cookies /path/to/cookies/file.txt. 

 In order to extract cookies from browser use any conforming browser extension for exporting cookies. For example, Get cookies.txt (<a rel="nofollow" HREF="https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid/)">https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid/)</a> (for Chrome) or cookies.txt (<a rel="nofollow" HREF="https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)">https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)</a> (for Firefox). 

 Note that the cookies file must be in Mozilla/Netscape format and the first line of the cookies file must be either # HTTP Cookie File or # Netscape HTTP Cookie File. Make sure you have correct newline format (<a rel="nofollow" HREF="https://en.wikipedia.org/wiki/Newline)">https://en.wikipedia.org/wiki/Newline)</a> in the cookies file and convert newlines if necessary to correspond with your OS, namely CRLF (\r\n) for Windows and LF (\n) for Unix and Unix-like systems (Linux, macOS, etc.). HTTP Error 400: Bad Request when using --cookies is a good sign of invalid newline format. 

 Passing cookies to youtube-dl is a good way to workaround login when a particular extractor does not implement it explicitly. Another use case is working around CAPTCHA (<a rel="nofollow" HREF="https://en.wikipedia.org/wiki/CAPTCHA)">https://en.wikipedia.org/wiki/CAPTCHA)</a> some websites require you to solve in particular cases in order to get access (e.g. YouTube, CloudFlare).

<h3>How do I stream directly to media player?</h3>

 

 You will first need to tell youtube-dl to stream media to stdout with -o -, and also tell your media player to read from stdin (it must be capable of this for streaming) and then pipe former to latter. For example, streaming to vlc (<a rel="nofollow" HREF="https://www.videolan.org/)">https://www.videolan.org/)</a> can be achieved with:
<dl>
<dt>
<dd> <pre>
youtube-dl -o - &quot;<a rel="nofollow" HREF="https://www.youtube.com/watch?v=BaW_jenozKcj">https://www.youtube.com/watch?v=BaW_jenozKcj</a>&quot; | vlc -
</pre></dl>

<h3>How do I download only new videos from a playlist?</h3>

 

 Use download-archive feature. With this feature you should initially download the complete playlist with --download-archive /path/to/download/archive/file.txt that will record identifiers of all the videos in a special file. Each subsequent run with the same --download-archive will download only new videos and skip all videos that have been downloaded before. Note that only successful downloads are recorded in the file. 

 For example, at first,
<dl>
<dt>
<dd> <pre>
youtube-dl --download-archive archive.txt &quot;<a rel="nofollow" HREF="https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re">https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re</a>&quot;
</pre></dl>
 

 will download the complete PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re playlist and create a file archive.txt. Each subsequent run will only download new videos if any:
<dl>
<dt>
<dd> <pre>
youtube-dl --download-archive archive.txt &quot;<a rel="nofollow" HREF="https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re">https://www.youtube.com/playlist?list=PLwiyx1dc3P2JR9N8gQaQN_BCvlSlap7re</a>&quot;
</pre></dl>

<h3>Should I add --hls-prefer-native into my config?</h3>

 

 When youtube-dl detects an HLS video, it can download it either with the built-in downloader or ffmpeg. Since many HLS streams are slightly invalid and ffmpeg/youtube-dl each handle some invalid cases better than the other, there is an option to switch the downloader if needed. 

 When youtube-dl knows that one particular downloader works better for a given website, that downloader will be picked. Otherwise, youtube-dl will pick the best downloader for general compatibility, which at the moment happens to be ffmpeg. This choice may change in future versions of youtube-dl, with improvements of the built-in downloader and/or ffmpeg. 

 In particular, the generic extractor (used when your website is not in the list of supported sites by youtube-dl (<a rel="nofollow" HREF="https://ytdl-org.github.io/youtube-dl/supportedsites.html)">https://ytdl-org.github.io/youtube-dl/supportedsites.html)</a> cannot mandate one specific downloader. 

 If you put either --hls-prefer-native or --hls-prefer-ffmpeg into your configuration, a different subset of videos will fail to download correctly. Instead, it is much better to file an issue (<a rel="nofollow" HREF="https://yt-dl.org/bug)">https://yt-dl.org/bug)</a> or a pull request which details why the native or the ffmpeg HLS downloader is a better choice for your use case.

<h3>Can you add support for this anime video site, or site which shows current movies for free?</h3>

 

 As a matter of policy (as well as legality), youtube-dl does not include support for services that specialize in infringing copyright. As a rule of thumb, if you cannot easily find a video that the service is quite obviously allowed to distribute (i.e. that has been uploaded by the creator, the creator's distributor, or is published under a free license), the service is probably unfit for inclusion to youtube-dl. 

 A note on the service that they don't host the infringing content, but just link to those who do, is evidence that the service should not be included into youtube-dl. The same goes for any DMCA note when the whole front page of the service is filled with videos they are not allowed to distribute. A &quot;fair use&quot; note is equally unconvincing if the service shows copyright-protected videos in full without authorization. 

 Support requests for services that do purchase the rights to distribute their content are perfectly fine though. If in doubt, you can simply include a source that mentions the legitimate purchase of content.

<h3>How can I speed up work on my issue?</h3>

 

 (Also known as: Help, my important issue not being solved!) The youtube-dl core developer team is quite small. While we do our best to solve as many issues as possible, sometimes that can take quite a while. To speed up your issue, here's what you can do: 

 First of all, please do report the issue at our issue tracker (<a rel="nofollow" HREF="https://yt-dl.org/bugs">https://yt-dl.org/bugs</a>). That allows us to coordinate all efforts by users and developers, and serves as a unified point. Unfortunately, the youtube-dl project has grown too large to use personal email as an effective communication channel. 

 Please read the bug reporting instructions below. A lot of bugs lack all the necessary information. If you can, offer proxy, VPN, or shell access to the youtube-dl developers. If you are able to, test the issue from multiple computers in multiple countries to exclude local censorship or misconfiguration issues. 

 If nobody is interested in solving your issue, you are welcome to take matters into your own hands and submit a pull request (or coerce/pay somebody else to do so). 

 Feel free to bump the issue from time to time by writing a small comment (&quot;Issue is still present in youtube-dl version ...from France, but fixed from Belgium&quot;), but please not more than once a month. Please do not declare your issue as important or urgent.

<h3>How can I detect whether a given URL is supported by youtube-dl?</h3>

 

 For one, have a look at the list of supported sites. Note that it can sometimes happen that the site changes its URL scheme (say, from <a rel="nofollow" HREF="https://example.com/video/1234567">https://example.com/video/1234567</a> to <a rel="nofollow" HREF="https://example.com/v/1234567">https://example.com/v/1234567</a> ) and youtube-dl reports an URL of a service in that list as unsupported. In that case, simply report a bug. 

 It is not possible to detect whether a URL is supported or not. That's because youtube-dl contains a generic extractor which matches all URLs. You may be tempted to disable, exclude, or remove the generic extractor, but the generic extractor not only allows users to extract videos from lots of websites that embed a video from another service, but may also be used to extract video from a service that it's hosting itself. Therefore, we neither recommend nor support disabling, excluding, or removing the generic extractor. 

 If you want to find out whether a given URL is supported, simply call youtube-dl with it. If you get no videos back, chances are the URL is either not referring to a video or unsupported. You can find out which by examining the output (if you run youtube-dl on the console) or catching an UnsupportedError exception if you run it from a Python program.

<h2>Why do I need to go through that much red tape when filing bugs?</h2>

 

 Before we had the issue template, despite our extensive bug reporting instructions, about 80% of the issue reports we got were useless, for instance because people used ancient versions hundreds of releases old, because of simple syntactic errors (not in youtube-dl but in general shell usage), because the problem was already reported multiple times before, because people did not actually read an error message, even if it said &quot;please install ffmpeg&quot;, because people did not mention the URL they were trying to download and many more simple, easy-to-avoid problems, many of whom were totally unrelated to youtube-dl. 

 youtube-dl is an open-source project manned by too few volunteers, so we'd rather spend time fixing bugs where we are certain none of those simple problems apply, and where we can be reasonably confident to be able to reproduce the issue without asking the reporter repeatedly. As such, the output of youtube-dl -v YOUR_URL_HERE is really all that's required to file an issue. The issue template also guides you through some basic steps you can do, such as checking that your version of youtube-dl is current.

<h2>DEVELOPER INSTRUCTIONS</h2>

 

 Most users do not need to build youtube-dl and can download the builds (<a rel="nofollow" HREF="https://ytdl-org.github.io/youtube-dl/download.html)">https://ytdl-org.github.io/youtube-dl/download.html)</a> or get them from their distribution. 

 To run youtube-dl as a developer, you don't need to build anything either. Simply execute
<dl>
<dt>
<dd> <pre>
python -m youtube_dl
</pre></dl>
 

 To run the test, simply invoke your favorite test runner, or execute a test file directly; any of the following work:
<dl>
<dt>
<dd> <pre>
python -m unittest discover
python test/test_download.py
nosetests
</pre></dl>
 

 See item 6 of new extractor tutorial for how to run extractor specific test cases. 

 If you want to create a build of youtube-dl yourself, you'll need
<dl>
<dt>&bull;
<dd> python
<dt>&bull;
<dd> make (only GNU make is supported)
<dt>&bull;
<dd> pandoc
<dt>&bull;
<dd> zip
<dt>&bull;
<dd> nosetests</dl>

<h3>Adding support for a new site</h3>

 

 If you want to add support for a new site, first of all make sure this site is not dedicated to copyright infringement. youtube-dl does not support such sites thus pull requests adding support for them will be rejected. 

 After you have ensured this site is distributing its content legally, you can follow this quick list (assuming your service is called yourextractor):
<dl>
<dt> 1.
<dd> Fork this repository (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/fork)">https://github.com/ytdl-org/youtube-dl/fork)</a>
<dt> 2.
<dd> Check out the source code with:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
 git clone git [at] github.com:YOUR_GITHUB_USERNAME/youtube-dl.git
</pre></dl>
</dl>

<dt> 3.
<dd> Start a new git branch with
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
 cd youtube-dl
 git checkout -b yourextractor
</pre></dl>
</dl>

<dt> 4.
<dd> Start with this simple template and save it to youtube_dl/extractor/yourextractor.py:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> 
#coding : utf - 8
from __future__ import unicode_literals
    from.common import InfoExtractor class YourExtractorIE(InfoExtractor)
    : _VALID_URL = r 'https?://(?:www\.)?yourextractor\.com/watch/(?P&lt;id&gt;[0-9]+)' _TEST = {
    'url' : 'https://yourextractor.com/watch/42',
    'md5' : 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
    'info_dict' : {
        'id' : '42',
        'ext' : 'mp4',
        'title' : 'Video title goes here',
        'thumbnail' : r 're:hahttps?://.*\.jpg$',
#TODO more properties, either as:
#* A value
#* MD5 checksum; start the string with md5:
#* A regular expression; start the string with re:
#* Any Python type(for example int or float)
    }
} def _real_extract(self, url)
    : video_id = self._match_id(url)
                     webpage = self._download_webpage(url, video_id)
#TODO more code goes here, for example...
                                   title = self._html_search_regex(r '&lt;h1&gt;(.+?)&lt;/h1&gt;', webpage, 'title') return
{
    'id' : video_id,
           'title' : title,
                     'description' : self._og_search_description(webpage),
                     'uploader' : self._search_regex(r '&lt;div[ha&gt;]+id="uploader"[ha&gt;]*&gt;([ha&lt;]+)&lt;', webpage, 'uploader', fatal = False),
#TODO more properties(see youtube_dl / extractor / common.py)
}
</dl>
</dl>

<dt> 5.
<dd> Add an import in youtube_dl/extractor/extractors.py (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/extractors.py">https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/extractors.py</a>).
<dt> 6.
<dd> Run python test/test_download.py TestDownload.test_YourExtractor. This should fail at first, but you can continually re-run it until you're done. If you decide to add more than one test, then rename _TEST to _TESTS and make it into a list of dictionaries. The tests will then be named TestDownload.test_YourExtractor, TestDownload.test_YourExtractor_1, TestDownload.test_YourExtractor_2, etc. Note that tests with only_matching key in test's dict are not counted in.
<dt> 7.
<dd> Have a look at youtube_dl/extractor/common.py (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/common.py)">https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/extractor/common.py)</a> for possible helper methods and a detailed description of what your extractor should and may return (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/blob/7f41a598b3fba1bcab2817de64a08941200aa3c8/youtube_dl/extractor/common.py#L94-L303">https://github.com/ytdl-org/youtube-dl/blob/7f41a598b3fba1bcab2817de64a08941200aa3c8/youtube_dl/extractor/common.py#L94-L303</a>). Add tests and code for as many as you want.
<dt> 8.
<dd> Make sure your code follows youtube-dl coding conventions and check the code with flake8 (<a rel="nofollow" HREF="https://flake8.pycqa.org/en/latest/index.html#quickstart">https://flake8.pycqa.org/en/latest/index.html#quickstart</a>):
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
 $ flake8 youtube_dl/extractor/yourextractor.py
</pre></dl>
</dl>

<dt> 9.
<dd> Make sure your code works under all Python (<a rel="nofollow" HREF="https://www.python.org/)">https://www.python.org/)</a> versions claimed supported by youtube-dl, namely 2.6, 2.7, and 3.2+.
<dt>10.
<dd> When the tests pass, add (<a rel="nofollow" HREF="https://git-scm.com/docs/git-add)">https://git-scm.com/docs/git-add)</a> the new files and commit (<a rel="nofollow" HREF="https://git-scm.com/docs/git-commit)">https://git-scm.com/docs/git-commit)</a> them and push (<a rel="nofollow" HREF="https://git-scm.com/docs/git-push)">https://git-scm.com/docs/git-push)</a> the result, like this:
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> <pre>
$ git add youtube_dl/extractor/extractors.py
$ git add youtube_dl/extractor/yourextractor.py
$ git commit -m '[yourextractor] Add new extractor'
$ git push origin yourextractor
</pre></dl>
</dl>

<dt>11.
<dd> Finally, create a pull request (<a rel="nofollow" HREF="https://help.github.com/articles/creating-a-pull-request">https://help.github.com/articles/creating-a-pull-request</a>). We'll then review and merge it.</dl>
 

 In any case, thank you very much for your contributions!

<h3>youtube-dl coding conventions</h3>

 

 This section introduces a guide lines for writing idiomatic, robust and future-proof extractor code. 

 Extractors are very fragile by nature since they depend on the layout of the source data provided by 3rd party media hosters out of your control and this layout tends to change. As an extractor implementer your task is not only to write code that will extract media links and metadata correctly but also to minimize dependency on the source's layout and even to make the code foresee potential future changes and be ready for that. This is important because it will allow the extractor not to break on minor layout changes thus keeping old youtube-dl versions working. Even though this breakage issue is easily fixed by emitting a new version of youtube-dl with a fix incorporated, all the previous versions become broken in all repositories and distros' packages that may not be so prompt in fetching the update from us. Needless to say, some non rolling release distros may never receive an update at all.

<h3>Mandatory and optional metafields</h3>

 

 For extraction to work youtube-dl relies on metadata your extractor extracts and provides to youtube-dl expressed by an information dictionary (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/blob/7f41a598b3fba1bcab2817de64a08941200aa3c8/youtube_dl/extractor/common.py#L94-L303)">https://github.com/ytdl-org/youtube-dl/blob/7f41a598b3fba1bcab2817de64a08941200aa3c8/youtube_dl/extractor/common.py#L94-L303)</a> or simply info dict. Only the following meta fields in the info dict are considered mandatory for a successful extraction process by youtube-dl:
<dl>
<dt>&bull;
<dd> id (media identifier)
<dt>&bull;
<dd> title (media title)
<dt>&bull;
<dd> url (media download URL) or formats</dl>
 

 In fact only the last option is technically mandatory (i.e. if you can't figure out the download location of the media the extraction does not make any sense). But by convention youtube-dl also treats id and title as mandatory. Thus the aforementioned metafields are the critical data that the extraction does not make any sense without and if any of them fail to be extracted then the extractor is considered completely broken. 

 Any field (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/blob/7f41a598b3fba1bcab2817de64a08941200aa3c8/youtube_dl/extractor/common.py#L188-L303)">https://github.com/ytdl-org/youtube-dl/blob/7f41a598b3fba1bcab2817de64a08941200aa3c8/youtube_dl/extractor/common.py#L188-L303)</a> apart from the aforementioned ones are considered optional. That means that extraction should be tolerant to situations when sources for these fields can potentially be unavailable (even if they are always available at the moment) and future-proof in order not to break the extraction of general purpose mandatory fields.

<h3>Example</h3>

 

 Say you have some source dictionary meta that you've fetched as JSON with HTTP request and it has a key summary:
<dl>
<dt>
<dd> <pre>
meta = self._download_json(url, video_id)
</pre></dl>
 

 Assume at this point meta's layout is:
<dl>
<dt>
<dd> <pre>
{
    ...
    &quot;summary&quot;: &quot;some fancy summary text&quot;,
    ...
}
</pre></dl>
 

 Assume you want to extract summary and put it into the resulting info dict as description. Since description is an optional meta field you should be ready that this key may be missing from the meta dict, so that you should extract it like:
<dl>
<dt>
<dd> <pre>
description = meta.get('summary')  # correct
</pre></dl>
 

 and not like:
<dl>
<dt>
<dd> <pre>
description = meta['summary']  # incorrect
</pre></dl>
 

 The latter will break extraction process with KeyError if summary disappears from meta at some later time but with the former approach extraction will just go ahead with description set to None which is perfectly fine (remember None is equivalent to the absence of data). 

 Similarly, you should pass fatal=False when extracting optional data from a webpage with _search_regex, _html_search_regex or similar methods, for instance:
<dl>
<dt>
<dd> 
description = self._search_regex(
    r '&lt;span[ha&gt;]+id="title"[ha&gt;]*&gt;([ha&lt;]+)&lt;',
    webpage, 'description', fatal = False)
</dl>
 

 With fatal set to False if _search_regex fails to extract description it will emit a warning and continue extraction. 

 You can also pass default=&lt;some fallback value&gt;, for example:
<dl>
<dt>
<dd> 
description = self._search_regex(
    r '&lt;span[ha&gt;]+id="title"[ha&gt;]*&gt;([ha&lt;]+)&lt;',
    webpage, 'description', default = None)
</dl>
 

 On failure this code will silently continue the extraction with description set to None. That is useful for metafields that may or may not be present.

<h3>Provide fallbacks</h3>

 

 When extracting metadata try to do so from multiple sources. For example if title is present in several places, try extracting from at least some of them. This makes it more future-proof in case some of the sources become unavailable.

<h3>Example</h3>

 

 Say meta from the previous example has a title and you are about to extract it. Since title is a mandatory meta field you should end up with something like:
<dl>
<dt>
<dd> <pre>
title = meta['title']
</pre></dl>
 

 If title disappears from meta in future due to some changes on the hoster's side the extraction would fail since title is mandatory. That's expected. 

 Assume that you have some another source you can extract title from, for example og:title HTML meta of a webpage. In this case you can provide a fallback scenario:
<dl>
<dt>
<dd> <pre>
title = meta.get('title') or self._og_search_title(webpage)
</pre></dl>
 

 This code will try to extract from meta first and if it fails it will try extracting og:title from a webpage.

<h3>Regular expressions</h3>

<h3>Don't capture groups you don't use</h3>

 

 Capturing group must be an indication that it's used somewhere in the code. Any group that is not used must be non capturing.

<h3>Example</h3>

 

 Don't capture id attribute name here since you can't use it for anything anyway. 

 Correct:
<dl>
<dt>
<dd> <pre>
r'(?:id|ID)=(?P&lt;id&gt;\d+)'
</pre></dl>
 

 Incorrect:
<dl>
<dt>
<dd> <pre>
r'(id|ID)=(?P&lt;id&gt;\d+)'
</pre></dl>

<h3>Make regular expressions relaxed and flexible</h3>

 

 When using regular expressions try to write them fuzzy, relaxed and flexible, skipping insignificant parts that are more likely to change, allowing both single and double quotes for quoted values and so on.

<h3>Example</h3>

 

 Say you need to extract title from the following HTML code:
<dl>
<dt>
<dd> 
&lt;span style="position: absolute; left: 910px; width: 90px; float: right; z-index: 9999;" class="title"&gt;some fancy title&lt;/span&gt;
</dl>
 

 The code for that task should look similar to:
<dl>
<dt>
<dd> 
title = self._search_regex(
    r '&lt;span[ha&gt;]+class="title"[ha&gt;]*&gt;([ha&lt;]+)', webpage, 'title')
</dl>
 

 Or even better:
<dl>
<dt>
<dd> 
title = self._search_regex(
    r '&lt;span[ha&gt;]+class=(["\'])title\1[ha&gt;]*&gt;(?P&lt;title&gt;[ha&lt;]+)',
    webpage, 'title', group = 'title')
</dl>
 

 Note how you tolerate potential changes in the style attribute's value or switch from using double quotes to single for class attribute: 

 The code definitely should not look like:
<dl>
<dt>
<dd> 
title = self._search_regex(
    r '&lt;span style="position: absolute; left: 910px; width: 90px; float: right; z-index: 9999;" class="title"&gt;(.*?)&lt;/span&gt;',
    webpage, 'title', group = 'title')
</dl>

<h3>Long lines policy</h3>

 

 There is a soft limit to keep lines of code under 80 characters long. This means it should be respected if possible and if it does not make readability and code maintenance worse. 

 For example, you should never split long string literals like URLs or some other often copied entities over multiple lines to fit this limit: 

 Correct:
<dl>
<dt>
<dd> <pre>
'<a rel="nofollow" HREF="https://www.youtube.com/watch?v=FqZTN594JQw">https://www.youtube.com/watch?v=FqZTN594JQw</a>&amp;list=PLMYEtVRpaqY00V9W81Cwmzp6N6vZqfUKD4'
</pre></dl>
 

 Incorrect:
<dl>
<dt>
<dd> <pre>
'<a rel="nofollow" HREF="https://www.youtube.com/watch?v=FqZTN594JQw">https://www.youtube.com/watch?v=FqZTN594JQw</a>&amp;list='
'PLMYEtVRpaqY00V9W81Cwmzp6N6vZqfUKD4'
</pre></dl>

<h3>Inline values</h3>

 

 Extracting variables is acceptable for reducing code duplication and improving readability of complex expressions. However, you should avoid extracting variables used only once and moving them to opposite parts of the extractor file, which makes reading the linear flow difficult.

<h3>Example</h3>

 

 Correct:
<dl>
<dt>
<dd> <pre>
title = self._html_search_regex(r'&lt;title&gt;([ha&lt;]+)&lt;/title&gt;', webpage, 'title')
</pre></dl>
 

 Incorrect:
<dl>
<dt>
<dd> <pre>
TITLE_RE = r'&lt;title&gt;([ha&lt;]+)&lt;/title&gt;'
# ...some lines of code...
title = self._html_search_regex(TITLE_RE, webpage, 'title')
</pre></dl>

<h3>Collapse fallbacks</h3>

 

 Multiple fallback values can quickly become unwieldy. Collapse multiple fallback values into a single expression via a list of patterns.

<h3>Example</h3>

 

 Good:
<dl>
<dt>
<dd> <pre>
description = self._html_search_meta(
    ['og:description', 'description', 'twitter:description'],
    webpage, 'description', default=None)
</pre></dl>
 

 Unwieldy:
<dl>
<dt>
<dd> <pre>
description = (
    self._og_search_description(webpage, default=None)
    or self._html_search_meta('description', webpage, default=None)
    or self._html_search_meta('twitter:description', webpage, default=None))
</pre></dl>
 

 Methods supporting list of patterns are: _search_regex, _html_search_regex, _og_search_property, _html_search_meta.

<h3>Trailing parentheses</h3>

 

 Always move trailing parentheses after the last argument.

<h3>Example</h3>

 

 Correct:
<dl>
<dt>
<dd> 
    lambda x: x['ResultSet']['Result'][0]['VideoUrlSet']['VideoUrl'],
    list)
</dl>
 

 Incorrect:
<dl>
<dt>
<dd> 
    lambda x: x['ResultSet']['Result'][0]['VideoUrlSet']['VideoUrl'],
    list,
)
</dl>

<h3>Use convenience conversion and parsing functions</h3>

 

 Wrap all extracted numeric data into safe functions from youtube_dl/utils.py (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/utils.py">https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/utils.py</a>): int_or_none, float_or_none. Use them for string to number conversions as well. 

 Use url_or_none for safe URL processing. 

 Use try_get for safe metadata extraction from parsed JSON. 

 Use unified_strdate for uniform upload_date or any YYYYMMDD meta field extraction, unified_timestamp for uniform timestamp extraction, parse_filesize for filesize extraction, parse_count for count meta fields extraction, parse_resolution, parse_duration for duration extraction, parse_age_limit for age_limit extraction. 

 Explore youtube_dl/utils.py (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/utils.py)">https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/utils.py)</a> for more useful convenience functions.

<h3>More examples</h3>

<h3>Safely extract optional description from parsed JSON</h3>

<dl>
<dt>
<dd> 
description = try_get(response, lambda x
                      : x['result']['video'][0]['summary'], compat_str)
</dl>

<h3>Safely extract more optional metadata</h3>

<dl>
<dt>
<dd> 
video = try_get(response, lambda x
                : x['result']['video'][0], dict) or
{
}
description = video.get('summary')
                  duration = float_or_none(video.get('durationMs'), scale = 1000)
    view_count = int_or_none(video.get('views'))
</dl>

<h2>EMBEDDING YOUTUBE-DL</h2>

 

 youtube-dl makes the best effort to be a good command-line program, and thus should be callable from any programming language. If you encounter any problems parsing its output, feel free to create a report (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/issues/new">https://github.com/ytdl-org/youtube-dl/issues/new</a>). 

 From a Python program, you can embed youtube-dl in a more powerful fashion, like this:
<dl>
<dt>
<dd> 
from __future__ import unicode_literals
    import youtube_dl
        ydl_opts = {} with youtube_dl.YoutubeDL(ydl_opts) as ydl : ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
</dl>
 

 Most likely, you'll want to use various options. For a list of options available, have a look at youtube_dl/YoutubeDL.py (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312">https://github.com/ytdl-org/youtube-dl/blob/3e4cedf9e8cd3157df2457df7274d0c842421945/youtube_dl/YoutubeDL.py#L137-L312</a>). For a start, if you want to intercept youtube-dl's output, set a logger object. 

 Here's a more complete example of a program that outputs only errors (and a short message after the download is finished), and downloads/converts the video to an mp3 file:
<dl>
<dt>
<dd> 
from __future__ import unicode_literals
        import youtube_dl class MyLogger(object)
    : def debug(self, msg)
    : pass
      def warning(self, msg)
    : pass
      def error(self, msg)
    : print(msg)
          def my_hook(d)
    : if d['status'] == 'finished' : print('Done downloading, now converting ...')
                                         ydl_opts = {
    'format' : 'bestaudio/best',
    'postprocessors' : [ {
        'key' : 'FFmpegExtractAudio',
        'preferredcodec' : 'mp3',
        'preferredquality' : '192',
    } ],
    'logger' : MyLogger(),
    'progress_hooks' : [my_hook],
} with youtube_dl.YoutubeDL(ydl_opts) as ydl : ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
</dl>

<h2>BUGS</h2>

 

 Bugs and suggestions should be reported at: &lt;<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/issues">https://github.com/ytdl-org/youtube-dl/issues</a>&gt;. Unless you were prompted to or there is another pertinent reason (e.g. GitHub fails to accept the bug report), please do not send bug reports via personal email. For discussions, join us in the IRC channel #youtube-dl (<a HREF="irc://chat.freenode.net/#youtube-dl)">irc://chat.freenode.net/#youtube-dl)</a> on freenode (webchat (<a rel="nofollow" HREF="https://webchat.freenode.net/?randomnick=1">https://webchat.freenode.net/?randomnick=1</a>&amp;channels=youtube-dl)). 

 Please include the full output of youtube-dl when run with -v, i.e. add -v flag to your command line, copy the whole output and post it in the issue body wrapped in ``` for better formatting. It should look similar to this:
<dl>
<dt>
<dd> <pre><code>
$ youtube - dl - v&lt;your command line&gt;[debug] System config : [][debug] User config : [][debug] Command - line args : [ u'-v', u'https://www.youtube.com/watch?v=BaW_jenozKcj' ][debug] Encodings : locale cp1251, fs mbcs, out cp866, pref cp1251[debug] youtube - dl version 2015.12.06 [debug] Git HEAD : 135392e [debug] Python version 2.6.6 - Windows - 2003Server - 5.2.3790 - SP2[debug] exe versions : ffmpeg N - 75573 - g1d0487f, ffprobe N - 75573 - g1d0487f, rtmpdump 2.4 [debug] Proxy map : {}...
</code></pre></dl>
 

 Do not post screenshots of verbose logs; only plain text is acceptable. 

 The output (including the first lines) contains important debugging information. Issues without the full output are often not reproducible and therefore do not get solved in short order, if ever. 

 Please re-read your issue once again to avoid a couple of common mistakes (you can and should use this as a checklist):

<h3>Is the description of the issue itself sufficient?</h3>

 

 We often get issue reports that we cannot really decipher. While in most cases we eventually get the required information after asking back multiple times, this poses an unnecessary drain on our resources. Many contributors, including myself, are also not native speakers, so we may misread some parts. 

 So please elaborate on what feature you are requesting, or what bug you want to be fixed. Make sure that it's obvious
<dl>
<dt>&bull;
<dd> What the problem is
<dt>&bull;
<dd> How it could be fixed
<dt>&bull;
<dd> How your proposed solution would look like</dl>
 

 If your report is shorter than two lines, it is almost certainly missing some of these, which makes it hard for us to respond to it. We're often too polite to close the issue outright, but the missing info makes misinterpretation likely. As a committer myself, I often get frustrated by these issues, since the only possible way for me to move forward on them is to ask for clarification over and over. 

 For bug reports, this means that your report should contain the complete output of youtube-dl when called with the -v flag. The error message you get for (most) bugs even says so, but you would not believe how many of our bug reports do not contain this information. 

 If your server has multiple IPs or you suspect censorship, adding --call-home may be a good idea to get more diagnostics. If the error is ERROR: Unable to extract ... and you cannot reproduce it from multiple countries, add --dump-pages (warning: this will yield a rather large output, redirect it to the file log.txt by adding &gt;log.txt 2&gt;&amp;1 to your command-line) or upload the .dump files you get when you add --write-pages somewhere (<a rel="nofollow" HREF="https://gist.github.com/">https://gist.github.com/</a>). 

 Site support requests must contain an example URL. An example URL is a URL you might want to download, like <a rel="nofollow" HREF="https://www.youtube.com/watch?v=BaW_jenozKc.">https://www.youtube.com/watch?v=BaW_jenozKc.</a> There should be an obvious video present. Except under very special circumstances, the main page of a video service (e.g. <a rel="nofollow" HREF="https://www.youtube.com/)">https://www.youtube.com/)</a> is not an example URL.

<h3>Are you using the latest version?</h3>

 

 Before reporting any issue, type youtube-dl -U. This should report that you're up-to-date. About 20% of the reports we receive are already fixed, but people are using outdated versions. This goes for feature requests as well.

<h3>Is the issue already documented?</h3>

 

 Make sure that someone has not already opened the issue you're trying to open. Search at the top of the window or browse the GitHub Issues (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/search?type=Issues)">https://github.com/ytdl-org/youtube-dl/search?type=Issues)</a> of this repository. If there is an issue, feel free to write something along the lines of &quot;This affects me as well, with version 2015.01.01. Here is some more information on the issue: ...&quot;. While some issues may be old, a new post into them often spurs rapid activity.

<h3>Why are existing options not enough?</h3>

 

 Before requesting a new feature, please have a quick peek at the list of supported options (<a rel="nofollow" HREF="https://github.com/ytdl-org/youtube-dl/blob/master/README.md#options">https://github.com/ytdl-org/youtube-dl/blob/master/README.md#options</a>). Many feature requests are for features that actually exist already! Please, absolutely do show off your work in the issue report and detail how the existing similar options do not solve your problem.

<h3>Is there enough context in your bug report?</h3>

 

 People want to solve problems, and often think they do us a favor by breaking down their larger problems (e.g. wanting to skip already downloaded files) to a specific request (e.g. requesting us to look whether the file exists before downloading the info page). However, what often happens is that they break down the problem into two steps: One simple, and one impossible (or extremely complicated one). 

 We are then presented with a very complicated request when the original problem could be solved far easier, e.g. by recording the downloaded video IDs in a separate file. To avoid this, you must include the greater context where it is non-obvious. In particular, every feature request that does not consist of adding support for a new site should contain a use case scenario that explains in what situation the missing feature would be useful.

<h3>Does the issue involve one problem, and one problem only?</h3>

 

 Some of our users seem to think there is a limit of issues they can or should open. There is no limit of issues they can or should open. While it may seem appealing to be able to dump all your issues into one ticket, that means that someone who solves one of your issues cannot mark the issue as closed. Typically, reporting a bunch of issues leads to the ticket lingering since nobody wants to attack that behemoth, until someone mercifully splits the issue into multiple ones. 

 In particular, every site support request issue should only pertain to services at one site (generally under a common domain, but always using the same backend technology). Do not request support for vimeo user videos, White house podcasts, and Google Plus pages in the same issue. Also, make sure that you don't post bug reports alongside feature requests. As a rule of thumb, a feature request does not include outputs of youtube-dl that are not immediately related to the feature at hand. Do not post reports of a network error alongside the request for a new video service.

<h3>Is anyone going to need the feature?</h3>

 

 Only post features that you (or an incapacitated friend you can personally talk to) require. Do not post features because they seem like a good idea. If they are really useful, they will be requested by someone who requires them.

<h3>Is your question about youtube-dl?</h3>

 

 It may sound strange, but some bug reports we receive are completely unrelated to youtube-dl and relate to a different, or even the reporter's own, application. Please make sure that you are actually using youtube-dl. If you are using a UI for youtube-dl, report the bug to the maintainer of the actual application providing the UI. On the other hand, if your UI for youtube-dl fails in some way you believe is related to youtube-dl, by all means, go ahead and report the bug.

<h2>COPYRIGHT</h2>

 

 youtube-dl is released into the public domain by the copyright holders. 

 This README file was originally written by Daniel Bolton (<a rel="nofollow" HREF="https://github.com/dbbolton)">https://github.com/dbbolton)</a> and is likewise released into the public domain. 

<h2>Index</h2>


