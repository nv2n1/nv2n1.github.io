---

title: "ncmpcpp(1)"
name: "ncmpcpp"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncmpcpp/"
description: "ncmpcpp – An ncurses Music Player Daemon (MPD) client."
---

<p> ncmpcpp &#8211; An ncurses Music Player Daemon (MPD) client.</p>
<h2>SYNOPSIS</h2>
<p> <code>ncmpcpp</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> ncmpcpp is an ncurses client for MPD (Music Player Daemon), inspired by ncmpc. </p>
<p> Read more about MPD at <a rel="nofollow" href="http://www.musicpd.org">http://www.musicpd.org</a></p>
<h2>OPTIONS</h2>
<p> <code>-h, &#8211;host</code> Connect to server at host [localhost]</p>
<dl>
<dt><code>-p, &#8211;port</code></dt>
<dd> Connect to server at port [6600]</dd>
<dt><code>-c, &#8211;config</code></dt>
<dd> Use alternative configuration file</dd>
<dt><code>-s, &#8211;screen &lt;name&gt;</code></dt>
<dd> Specify the startup screen (&lt;name&gt; may be: help, playlist, browser, search-engine, media-library, playlist-editor, tag-editor, outputs, visualizer, clock)</dd>
<dt><code>-?, &#8211;help</code></dt>
<dd> Display help.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Display version information.</dd>
<dt><code>&#8211;now-playing</code></dt>
<dd> Display now playing song [&#123;&#123;(%l) }&#123;&#123;%a &#8211; }%t}}|{%f}}]</dd>
<dt><code>play</code></dt>
<dd> Start playing and exit.</dd>
<dt><code>pause</code></dt>
<dd> Pause and exit.</dd>
<dt><code>toggle</code></dt>
<dd> Toggle playing and exit.</dd>
<dt><code>stop</code></dt>
<dd> Stop playing and exit.</dd>
<dt><code>next</code></dt>
<dd> Switch to next song and exit.</dd>
<dt><code>prev</code></dt>
<dd> Switch to previous song and exit.</dd>
<dt><code>volume [+-]&lt;number&gt;</code></dt>
<dd> Raise/lower volume by given number of percents and exit.</dd>
<dt></dt></dl>
<h2>CONFIGURATION</h2>
<dd> When ncmpcpp starts, it tries to read user&#8217;s settings from the ~/.ncmpcpp/config file. If no user&#8217;s configuration is found, ncmpcpp uses its default configuration. An example configuration file containing all default values is provided with ncmpcpp and can be found usually in /usr/share/doc/ncmpcpp (exact location may depend on used distribution/OS/configure prefix). </dd>
<p> Note: Each config option value must be enclosed in quotation marks (var = &quot;example&quot;). If you want to use quotation mark inside config option, prepend character &#8216;\&#8217; to it. </p>
<p> Note: COLOR has to be the name (not a number) of one of colors 1-8 from SONG FORMAT section. </p>
<p> Supported configuration options:</p>
<dl>
<dt><code>ncmpcpp_directory = PATH</code></dt>
<dd> Directory for storing ncmpcpp related files. Changing it is useful if you want to store everything somewhere else and provide command line setting for alternative location to config file which defines that while launching ncmpcpp.</dd>
<dt><code>lyrics_directory = PATH</code></dt>
<dd> Directory for storing downloaded lyrics. It defaults to ~/.lyrics since other MPD clients (eg. ncmpc) also use that location.</dd>
<dt><code>mpd_host = HOST</code></dt>
<dd> Connect to MPD running on specified host/unix socket. When HOST starts with a &#8216;/&#8217;, it is assumed to be a unix socket.</dd>
<dt><code>mpd_music_dir = PATH</code></dt>
<dd> Search for files in specified directory. This is needed for tag editor to work.</dd>
<dt><code>mpd_port = PORT</code></dt>
<dd> Connect to MPD on the specified port.</dd>
<dt><code>mpd_connection_timeout = SECONDS</code></dt>
<dd> Set connection timeout to MPD to given value.</dd>
<dt><code>mpd_crossfade_time = SECONDS</code></dt>
<dd> Default number of seconds to crossfade, if enabled by ncmpcpp.</dd>
<dt><code>mpd_communication_mode = MODE</code></dt>
<dd> If set to &#8216;polling&#8217;, ncmpcpp will constantly poll mpd for its status. If set to &#8216;notifications&#8217;, ncmppcp will make use of &#8216;idle&#8217; command and wait for events. This is more efficient and responsive, but may cause some trouble with &lt;mpd-0.15, so if you run such version and encounter strange bugs (e.g. current track time not being updated), you will either have to use &#8216;polling&#8217; or upgrade your mpd.</dd>
<dt><code>visualizer_in_stereo = yes/no</code></dt>
<dd> Should be set to &#8216;yes&#8217;, if fifo output&#8217;s format was set to 44100:16:2.</dd>
<dt><code>visualizer_fifo_path = PATH</code></dt>
<dd> Path to mpd fifo output. This is needed to make music visualizer work (note that output sound format of this fifo has to be either 44100:16:1 or 44100:16:2, depending on whether you want mono or stereo visualization)</dd>
<dt><code>visualizer_output_name = NAME</code></dt>
<dd> Name of output that provides data for visualizer. Needed to keep sound and visualization in sync.</dd>
<dt><code>visualizer_sync_interval = SECONDS</code></dt>
<dd> Defines interval between syncing visualizer and audio outputs.</dd>
<dt><code>visualizer_type = spectrum/wave</code></dt>
<dd> Defines default visualizer type (spectrum is available only if ncmpcpp was compiled with fftw support).</dd>
<dt><code>visualizer_look = STRING</code></dt>
<dd> Defines visualizer&#8217;s look (string has to be exactly 2 characters long: first one is for wave whereas second for frequency spectrum).</dd>
<dt><code>system_encoding = ENCODING</code></dt>
<dd> If you use encoding other than utf8, set it in order to handle utf8 encoded strings properly.</dd>
<dt><code>seek_time = SECONDS</code></dt>
<dd> Base seek time to begin with.</dd>
<dt><code>playlist_disable_highlight_delay = SECONDS</code></dt>
<dd> Delay for highlighting playlist since the last key was pressed. If set to 0, highlighting never fades away.</dd>
<dt><code>message_delay_time = SECONDS</code></dt>
<dd> Delay for displayed messages to remain visible.</dd>
<dt><code>song_list_format</code></dt>
<dd> Format for songs&#8217; list.</dd>
<dt><code>song_columns_list_format</code></dt>
<dd> Format for songs&#8217; list displayed in columns.</dd>
<dt><code>song_status_format</code></dt>
<dd> Song&#8217;s format for statusbar.</dd>
<dt><code>song_library_format</code></dt>
<dd> Format for songs in Media library.</dd>
<dt><code>tag_editor_album_format</code></dt>
<dd> Format for albums&#8217; list in Tag editor.</dd>
<dt><code>song_window_title_format</code></dt>
<dd> Song format for window title.</dd>
<dt><code>external_editor = PATH</code></dt>
<dd> Path to external editor used to edit lyrics.</dd>
<dt><code>browser_playlist_prefix = TEXT</code></dt>
<dd> Prefix for playlists in Browser.</dd>
<dt><code>default_tag_editor_pattern = TEXT</code></dt>
<dd> Default pattern used by Tag editor&#8217;s parser.</dd>
<dt><code>now_playing_prefix = TEXT</code></dt>
<dd> Prefix for currently playing song.</dd>
<dt><code>now_playing_suffix = TEXT</code></dt>
<dd> Suffix for currently playing song.</dd>
<dt><code>selected_item_prefix = TEXT</code></dt>
<dd> Prefix for selected items.</dd>
<dt><code>selected_item_suffix = TEXT</code></dt>
<dd> Suffix for selected items.</dd>
<dt><code>alternative_header_first_line_format = TEXT</code></dt>
<dd> Now playing song format for the first line in alternative user interface header window.</dd>
<dt><code>alternative_header_second_line_format = TEXT</code></dt>
<dd> Now playing song format for the second line in alternative user interface header window.</dd>
<dt><code>color1 = COLOR</code></dt>
<dd> One of colors used in Song info, Tiny tag editor and Search engine.</dd>
<dt><code>color2 = COLOR</code></dt>
<dd> One of colors used in Song info, Tiny tag editor and Search engine.</dd>
<dt><code>colors_enabled = yes/no</code></dt>
<dd> No need to describe it, huh?</dd>
<dt><code>header_text_scrolling = yes/no</code></dt>
<dd> If enabled, text in header window will scroll if its length is longer then actual screen width, otherwise it won&#8217;t.</dd>
<dt><code>fancy_scrolling = yes/no</code></dt>
<dd> If enabled, content of other columns will be updated immediately while scrolling, otherwise only after you stop scrolling.</dd>
<dt><code>cyclic_scrolling = yes/no</code></dt>
<dd> If enabled, cyclic scrolling is used (e.g. if you press down arrow being at the end of list, it&#8217;ll take you to the beginning)</dd>
<dt><code>mouse_list_scroll_whole_page = yes/no</code></dt>
<dd> If enabled, mouse wheel will scroll the whole page of item list at a time, otherwise the number of lines specified by lines_scrolled variable.</dd>
<dt><code>lines_scrolled = NUMBER</code></dt>
<dd> Number of lines that are scrolled with mouse wheel.</dd>
<dt><code>search_engine_default_search_mode = MODE_NUMBER</code></dt>
<dd> Number of default mode used in search engine.</dd>
<dt><code>playlist_show_remaining_time = yes/no</code></dt>
<dd> If enabled, time remaining to end of playlist will be shown after playlist&#8217;s statistics.</dd>
<dt><code>playlist_shorten_total_times = yes/no</code></dt>
<dd> If enabled, total/remaining playlist time displayed in statusbar will be shown using shortened units&#8217; names (d:h:m:s instead of days:hours:minutes:seconds).</dd>
<dt><code>playlist_separate_albums = yes/no</code></dt>
<dd> If enabled, separators will be placed between albums.</dd>
<dt><code>playlist_display_mode = classic/columns</code></dt>
<dd> Default display mode for Playlist.</dd>
<dt><code>browser_display_mode = classic/columns</code></dt>
<dd> Default display mode for Browser.</dd>
<dt><code>search_engine_display_mode = classic/columns</code></dt>
<dd> Default display mode for Search engine.</dd>
<dt><code>playlist_editor_display_mode = classic/columns</code></dt>
<dd> Default display mode for Playlist editor.</dd>
<dt><code>discard_colors_if_item_is_selected = yes/no</code></dt>
<dd> Indicates whether custom colors of tags have to be discarded if item is selected or not.</dd>
<dt><code>header_visibility = yes/no</code></dt>
<dd> If enabled, header window will be displayed, otherwise hidden.</dd>
<dt><code>statusbar_visibility = yes/no</code></dt>
<dd> If enabled, statusbar will be displayed, otherwise hidden.</dd>
<dt><code>titles_visibility = yes/no</code></dt>
<dd> If enabled, column titles will be displayed, otherwise hidden.</dd>
<dt><code>autocenter_mode = yes/no</code></dt>
<dd> Default state for autocenter mode at start.</dd>
<dt><code>centered_cursor = yes/no</code></dt>
<dd> If enabled, currently highlighted position in the list will be always centered.</dd>
<dt><code>progressbar_look = TEXT</code></dt>
<dd> This variable defines the look of progressbar. Note that it has to be exactly two or three characters long.</dd>
<dt><code>default_find_mode = wrapped/normal</code></dt>
<dd> If set to &quot;wrapped&quot;, going from last found position to next will take you to the first one (same goes for the first position and going to previous one), otherwise no actions will be performed.</dd>
<dt><code>default_space_mode = select/add</code></dt>
<dd> If set to &quot;select&quot;, space will select items instead of adding them to playlist (although selecting by space is default and the only one action for space in Playlist).</dd>
<dt><code>default_tag_editor_left_col = albums/dirs</code></dt>
<dd> If set to &quot;albums&quot;, tag editor will display list of all albums from database, otherwise it&#8217;ll allow you to browse the database.</dd>
<dt><code>incremental_seeking = yes/no</code></dt>
<dd> If enabled, seek time will increment by one each second of seeking.</dd>
<dt><code>follow_now_playing_lyrics = yes/no</code></dt>
<dd> If enabled, lyrics will be switched at song&#8217;s change to currently playing one&#8217;s (Note: this works only if you are viewing lyrics of item from Playlist).</dd>
<dt><code>fetch_lyrics_for_current_song_in_background = yes/no</code></dt>
<dd> If enabled, each time song changes lyrics fetcher will be automatically run in background in attempt to download lyrics for currently playing song.</dd>
<dt><code>store_lyrics_in_song_dir = yes/no</code></dt>
<dd> If enabled, lyrics will be saved in song&#8217;s directory, otherwise in ~/.lyrics. Note that it needs properly set mpd_music_dir.</dd>
<dt><code>lastfm_preferred_language = ISO 639 alpha-2 language code</code></dt>
<dd> If set, ncmpcpp will try to get info from last.fm in language you set and if it fails, it will fall back to english. Otherwise it will use english the first time.</dd>
<dt><code>ncmpc_like_songs_adding = yes/no</code></dt>
<dd> If enabled, pressing space on item, which is already in playlist will remove it, otherwise add it again.</dd>
<dt><code>show_hidden_files_in_local_browser = yes/no</code></dt>
<dd> Trigger for displaying in local browser files and directories that begin with &#8216;.&#8217;</dd>
<dt><code>default_place_to_search_in = database/playlist</code></dt>
<dd> If set to &quot;playlist&quot;, Search engine will perform searching in current MPD playlist rather than in music database.</dd>
<dt><code>display_screens_numbers_on_start = yes/no</code></dt>
<dd> If enabled, screens&#8217; names and their keybindings will be shown in header window until key is pressed, otherwise they won&#8217;t be displayed at all.</dd>
<dt><code>screen_switcher_mode = SWITCHER_MODE</code></dt>
<dd> If set to &quot;previous&quot;, key_screen_switcher will switch between current and last used screen. If set to &quot;sequence: user_defined_sequence&quot;, it will switch between given sequence of screens. Syntax clarification can be found in example config file.</dd>
<dt><code>locked_screen_width_part = 20-80</code></dt>
<dd> If you want to lock a screen, ncmpcpp asks for % of locked screen&#8217;s width to be reserved before that and provides a default value, which is the one you can set here.</dd>
<dt><code>ask_for_locked_screen_width_part = yes/no</code></dt>
<dd> If enabled, ncmpcpp will ask for % of locked screen&#8217;s width each time you want to lock a screen. If you disable that, it&#8217;ll silently attempt to use default value.</dd>
<dt><code>startup_screen = SCREEN_NUMBER</code></dt>
<dd> Screen that has to be displayed at start (playlist by default).</dd>
<dt><code>jump_to_now_playing_song_at_start = yes/no</code></dt>
<dd> If enabled, ncmpcpp will jump at start to now playing song if mpd is playing or paused.</dd>
<dt><code>ask_before_clearing_main_playlist = yes/no</code></dt>
<dd> If enabled, user will be asked if he really wants to clear the main playlist after pressing key responsible for that.</dd>
<dt><code>clock_display_seconds = yes/no</code></dt>
<dd> If enabled, clock will display time in format hh:mm:ss, otherwise hh:mm.</dd>
<dt><code>display_volume_level = yes/no</code></dt>
<dd> If enabled, volume level will be displayed in statusbar, otherwise not.</dd>
<dt><code>display_bitrate = yes/no</code></dt>
<dd> If enabled, bitrate of currently playing song will be displayed in statusbar.</dd>
<dt><code>display_remaining_time = yes/no</code></dt>
<dd> If enabled, remaining time of currently playing song will be be displayed in statusbar instead of elapsed time.</dd>
<dt><code>ignore_leading_the = yes/no</code></dt>
<dd> If enabled, word &quot;the&quot; at the beginning of tags/filenames will be ignored while sorting items.</dd>
<dt><code>use_console_editor = yes/no</code></dt>
<dd> If your external editor is console application, you need to enable it.</dd>
<dt><code>block_search_constraints_change_if_items_found = yes/no</code></dt>
<dd> If enabled, fields in Search engine above &quot;Reset&quot; button will be blocked after successful searching, otherwise they won&#8217;t.</dd>
<dt><code>mouse_support = yes/no</code></dt>
<dd> Self-descriptive, isn&#8217;t it?</dd>
<dt><code>allow_physical_files_deletion = yes/no</code></dt>
<dd> If enabled, ncmpcpp will be able to delete files using its browser screen.</dd>
<dt><code>allow_physical_directories_deletion = yes/no</code></dt>
<dd> If enabled, ncmpcpp will be able to delete directories using its browser screen.</dd>
<dt><code>tag_editor_extended_numeration = yes/no</code></dt>
<dd> If enabled, tag editor will number tracks using format xx/yy (where xx is the current track and yy is total amount of all numbered tracks), not plain xx.</dd>
<dt><code>media_library_display_date = yes/no</code></dt>
<dd> If enabled, dates of albums in media library will be displayed and respected in searching, otherwise not.</dd>
<dt><code>media_library_display_empty_tag = yes/no</code></dt>
<dd> If enabled, left column will contain entry for &#8217;empty&#8217; tag, otherwise not.</dd>
<dt><code>media_library_disable_two_column_mode = yes/no</code></dt>
<dd> If enabled, pressing the key for the media library twice won&#8217;t switch it to two column mode.</dd>
<dt><code>enable_window_title = yes/no</code></dt>
<dd> If enabled, ncmpcpp will override current window title with its own one.</dd>
<dt><code>regular_expressions = basic/extended</code></dt>
<dd> Type of currently used regular expressions.</dd>
<dt><code>user_interface = classic/alternative</code></dt>
<dd> Default user interface used by ncmpcpp at start.</dd>
<dt><code>media_library_left_column = a/y/g/c/p</code></dt>
<dd> Default tag type for left column in media library. Legend for possible letters is in SONG FORMAT section.</dd>
<dt><code>empty_tag_marker = TEXT</code></dt>
<dd> Text that will be displayed, if requested tag is not set.</dd>
<dt><code>empty_tag_color = COLOR</code></dt>
<dd> Color of empty tag marker.</dd>
<dt><code>header_window_color = COLOR</code></dt>
<dd> Color of header window.</dd>
<dt><code>volume_color = COLOR</code></dt>
<dd> Color of volume state.</dd>
<dt><code>state_line_color = COLOR</code></dt>
<dd> Color of lines separating header and statusbar from main window.</dd>
<dt><code>state_flags_color = COLOR</code></dt>
<dd> Color of MPD status flags.</dd>
<dt><code>main_window_color = COLOR</code></dt>
<dd> Color of main window.</dd>
<dt><code>main_window_highlight_color = COLOR</code></dt>
<dd> Color of main window&#8217;s highlight.</dd>
<dt><code>progressbar_color = COLOR</code></dt>
<dd> Color of progressbar.</dd>
<dt><code>statusbar_color = COLOR</code></dt>
<dd> Color of statusbar.</dd>
<dt><code>alternative_ui_separator_color = COLOR</code></dt>
<dd> Color of separators used in alternative user interface.</dd>
<dt><code>active_column_color = COLOR</code></dt>
<dd> Color of active column&#8217;s highlight.</dd>
<dt><code>visualizer_color = COLOR</code></dt>
<dd> Color of visualization.</dd>
<dt><code>active_window_border = COLOR</code></dt>
<dd> Color of active window&#8217;s border.</dd>
<dt></dt></dl>
<h2>KEYS</h2>
<dd> When ncmpcpp starts, it tries to read user&#8217;s keybindings from ~/.ncmpcpp/keys file. If no user&#8217;s keybindings is found, ncmpcpp uses its default keybindings. An example keybindings file containing all default values is provided with ncmpcpp and can be found usually in /usr/share/doc/ncmpcpp (exact location may depend on used distribution/OS/configure prefix). </dd>
<p> You can view current ncmpcpp&#8217;s keybindings by pressing &#8216;1&#8217; (Help).</p>
<h2>SONG FORMAT</h2>
<p> For song format you can use: </p>
<p>&nbsp;<wbr>%l &#8211; length<br />
&nbsp;<wbr>%f &#8211; filename<br />
&nbsp;<wbr>%D &#8211; directory<br />
&nbsp;<wbr>%a &#8211; artist<br />
&nbsp;<wbr>%A &#8211; album artist<br />
&nbsp;<wbr>%t &#8211; title<br />
&nbsp;<wbr>%b &#8211; album<br />
&nbsp;<wbr>%y &#8211; year<br />
&nbsp;<wbr>%n &#8211; track number&nbsp;<wbr>(01/12 -&gt;&nbsp;<wbr>01)<br />
&nbsp;<wbr>%N &#8211; full track info&nbsp;<wbr>(01/12 -&gt;&nbsp;<wbr>01/12)<br />
&nbsp;<wbr>%g &#8211; genre<br />
&nbsp;<wbr>%c &#8211; composer<br />
&nbsp;<wbr>%p &#8211; performer<br />
&nbsp;<wbr>%d &#8211; disc<br />
&nbsp;<wbr>%C &#8211; comment<br />
&nbsp;<wbr>$R &#8211; begin right alignment </p>
<p> You can also put them in { } and then they will be displayed only if all requested values are available and/or define alternate value with { }|{ } e.g. {%a &#8211; %t}|{%f} will check if artist and title tags are available and if they are, display them. Otherwise it&#8217;ll display filename. </p>
<p> <code>Note</code>: If you want to set limit on maximal length of a tag, just put the appropriate number between % and character that defines tag type, e.g. to make album take max. 20 terminal cells, use &#8216;%20b&#8217;. </p>
<p> <code>Note</code>: Format that is similar to &quot;%a &#8211; %t&quot; (i.e. without any additional braces) is equal to &quot;{%a &#8211; %t}&quot;, so if one of the tags is missing, you&#8217;ll get nothing. </p>
<p> Text can have different color than the main window, e.g. if you want length to be green, write $3%l$9. </p>
<p> Available values for colors: </p>
<p>&nbsp;<wbr>&#8211; 0 &#8211; default window color&nbsp;<wbr>(discards all other colors)<br />
&nbsp;<wbr>&#8211; 1 &#8211; black<br />
&nbsp;<wbr>&#8211; 2 &#8211; red<br />
&nbsp;<wbr>&#8211; 3 &#8211; green<br />
&nbsp;<wbr>&#8211; 4 &#8211; yellow<br />
&nbsp;<wbr>&#8211; 5 &#8211; blue<br />
&nbsp;<wbr>&#8211; 6 &#8211; magenta<br />
&nbsp;<wbr>&#8211; 7 &#8211; cyan<br />
&nbsp;<wbr>&#8211; 8 &#8211; white<br />
&nbsp;<wbr>&#8211; 9 &#8211; end of current color </p>
<p> <code>Note</code>: colors can be nested, so if you write $2some$5text$9, it&#8217;ll disable only usage of blue color and make red the current one. </p>
<h2>BUGS</h2>
<p> Report bugs on <a rel="nofollow" href="http://www.musicpd.org/mantis/">http://www.musicpd.org/mantis/</a></p>
<h2>NOTE</h2>
<p> Since MPD uses UTF-8, ncmpcpp needs to convert characters to the charset used by the local system. If you get character conversion errors while you are running ncmpcpp, you probably need to set up your locale. This is done by setting LANG and LC_ALL/LC_CTYPE environment variables (LC_CTYPE only affects character handling).</p>
<h2>HOMEPAGE</h2>
<p> -&gt; <a rel="nofollow" href="http://unkart.ovh.org/ncmpcpp">http://unkart.ovh.org/ncmpcpp</a> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-mpc/">mpc</a>(1), <a href="/docs/linux/man/1-mpd/">mpd</a>(1) </p>
