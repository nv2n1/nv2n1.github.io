---

title: "xmms2(1)"
name: "xmms2"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmms2/"
description: "xmms2 – offers a simple command-line interface to the XMMS2 daemon"
---

<p> xmms2 &#8211; offers a simple command-line interface to the XMMS2 daemon</p>
<h2>SYNOPSIS</h2>
<p> <i>xmms2</i> <code>command</code> <i>xmms2</i> <code>mlib</code> <code>command</code> <i>xmms2</i> <code>playlist</code> <code>command</code> <i>xmms2</i> <code>coll</code> <code>command </code></p>
<h2>DESCRIPTION</h2>
<p> <code>XMMS2 </code> is a redesign of the XMMS (<a rel="nofollow" href="http://www.xmms.org)">http://www.xmms.org)</a> music player. It features a client-server model, allowing multiple (even simultaneous!) user interfaces, both textual and graphical. All common audio formats are supported using plugins. On top of this, there is a flexible media library to organize your music. </p>
<p> <i>xmms2</i> is the official command-line interface client for <code>XMMS2</code> and acts as a reference implementation for the development of new clients. <i>xmms2</i> is able to issue commands to control the active playlist and playback as well as commands to control the media library. </p>
<p> The following commands effect the current <code>XMMS2</code> playlist. </p>
<p> <i>xmms2</i> includes many commands that allow the user to execute actions on <i>xmms2d.</i></p>
<dl>
<dt><code>These</code>commands<code>are</code>currently<code>recognized:</code></dt>
<dd>
</dd><dt><i>add  url&#8230;</i></dt>
<dd> Adds URL(s) to <i>playlist</i> or the active playlist.</dd>
<dt><i>addarg  url arguments</i></dt>
<dd> Adds an URL to <i>playlist</i> or the active playlist, with arguments.</dd>
<dt><i>addid  medialib_id&#8230;</i></dt>
<dd> Adds song(s) to <i>playlist</i> or the active playlist using its Media Library ID.</dd>
<dt><i>addpls  url</i></dt>
<dd> Adds a playlist in a file to <i>playlist</i> or the active playlist.</dd>
<dt><i>insert  pos url</i></dt>
<dd> Adds a URL to <i>playlist</i> or the active playlist at a specific position.</dd>
<dt><i>insertid  pos medialib_id</i></dt>
<dd> Adds a song to <i>playlist</i> or the active playlist at a specific position using its Media Library ID.</dd>
<dt><i>radd  directory</i></dt>
<dd> Adds a directory of songs recursively to <i>playlist</i> or the active playlist.</dd>
<dt><i>clear </i></dt>
<dd> Clears all entries from <i>playlist</i> or the active playlist.</dd>
<dt><i>shuffle </i></dt>
<dd> Places the songs in <i>playlist</i> or the active playlist in a random order.</dd>
<dt><i>sort property</i></dt>
<dd> Sort the active playlist based on metadata from the Media Library. The metadata which is used for the sorting is based on what was given for <i>property.</i> An overview of the media library, and the potential properties, can be found in the <code>MEDIA LIBRARY</code> section of this manual page.</dd>
<dt><i>sort playlist properties</i></dt>
<dd> Sort <i>playlist</i> based on metadata from the Media Library. Separate the properties with a spaces.</dd>
<dt><i>remove  playlist_position</i></dt>
<dd> Removes a song from <i>playlist </i> or the active playlist at the position given by <i>playlist_position.</i></dd>
<dt><i>list </i></dt>
<dd> Lists the contents of <i>playlist</i> or the active playlist. An explanation of how to change the output format can be found in the <code>FILES</code> section of this manual page.</dd>
<dt><i>play</i></dt>
<dd> Starts playback of the playlist.</dd>
<dt><i>stop</i></dt>
<dd> Stops playback of the playlist.</dd>
<dt><i>toggleplay</i></dt>
<dd> Toggles playback status between play/pause</dd>
<dt><i>pause</i></dt>
<dd> Pauses playback of the playlist.</dd>
<dt><i>next</i></dt>
<dd> Skips to the next song in the playlist.</dd>
<dt><i>prev</i></dt>
<dd> Skips to the previous song in the playlist.</dd>
<dt><i>seek [+ / -]seconds</i></dt>
<dd> Seeks to a specific position in the currently playing song. The way in which <i>seek</i> moves in the file is based on the arguments passed to it. If + is used <i>xmms2</i> will seek <i>seconds</i> forward in the song. If &#8211; is used <i>xmms2</i> will seek <i>seconds</i> backwards in the song. If merely a number of seconds is given <i>xmms2</i> will seek to that absolute position in the song.</dd>
<dt><i>jump [+ / -]playlist_position</i></dt>
<dd> Jumps to <i>playlist_position</i> in the playlist or <i>playlist_position</i> forward/backward if + or &#8211; is specified.</dd>
<dt><i>move  playlist_position new_position</i></dt>
<dd> Moves the song at <i>playlist position</i> to the position denoted by <i>new_position in</i> <i>playlist</i> or the active playlist.</dd>
<dt><i>volume channel volume</i></dt>
<dd> Sets the volume of <i>channel</i> to <i>volume.</i></dd>
<dt><i>volume_list</i></dt>
<dd> Lists the volume for each channel.</dd>
<dt><i>mlib</i></dt>
<dd> Allows for the manipulation of the Media Library. The significance of the sub-commands of <i>mlib</i> can be found in the <code>MEDIA LIBRARY</code> section of this manual page.</dd>
<dt><i>playlist</i></dt>
<dd> Allows for the manipulation of playlists. The significance of the sub-commands of <i>playlist</i> can be found in the <code>PLAYLIST</code> section of this manual page.</dd>
<dt><i>coll</i></dt>
<dd> Allows for the manipulation of collections. The significance of this sub-commands of <i>coll</i> can be found in the <code>COLLECTIONS</code> section of this manual page.</dd>
<dt><i>browse url</i></dt>
<dd> Lists the contents of <i>url</i> in a list of encoded urls.</dd>
<dt><i>status</i></dt>
<dd> Gives a live status of the currently playing song.</dd>
<dt><i>info [id]</i></dt>
<dd> Gives the metadata archived by the Media Library for Media Library id <i>id</i> or the currently playing song.</dd>
<dt><i>current [pattern]</i></dt>
<dd> Gives some summary of the currently playing song&#8217;s meta data. A pattern can be specified in the form &quot;${album} &#8211; ${tracknr}&quot;. Please be aware of your shells substitution features.</dd>
<dt><i>config config_key [=] value</i></dt>
<dd> Sets <i>config_key</i> to <i>value</i> on <i>xmms2d(8).</i></dd>
<dt><i>config_list</i></dt>
<dd> Lists all the configuration values of <code>XMMS2.</code></dd>
<dt><i>plugin_list</i></dt>
<dd> Prints a list of the plugins being used by <code>XMMS2.</code></dd>
<dt><i>stats</i></dt>
<dd> Retrieves the uptime and version from <code>XMMS2.</code></dd>
<dt><i>quit</i></dt>
<dd> Makes <i>xmms2d(8)</i> quit.</dd>
<dt><i>help</i></dt>
<dd> Prints a concise overview of all commands offered by <i>xmms2.</i></dd></dl>
<h2>MEDIA LIBRARY</h2>
<p> <code>XMMS2</code> stores metadata about every song in the Media Library. One can retrieve data from the Media Library using the <i>mlib </i> command of <i>xmms2.</i> The Media Library is an SQL database which is created and accessed by use of the sqlite library. <i>xmms2 mlib</i> includes many commands for manipulating and retrieving data from the Media Library.</p>
<dl>
<dt><code>The</code>following</dt>
<dd> <i>mlib </i> commands are currently recognized:</dd>
<dt><i>add url</i></dt>
<dd> Adds a URL to the Media Library but not to the current playlist. The Media Library also fetches associated metadata for the added song.</dd>
<dt><i>loadall</i></dt>
<dd> Load all songs in the Media Library into the current playlist.</dd>
<dt><i>searchadd pattern</i></dt>
<dd> Searches the Media Library for songs that match <i>pattern</i> criteria and adds them to the current playlist.</dd>
<dt><i>search pattern</i></dt>
<dd> Searches and returns a list of songs in the Media Library that match <i>pattern.</i></dd>
<dt>
</dt><dd> For example one could execute:</dd>
<dt>
</dt><dd> <i>xmms2 mlib search artist:Dismantled</i></dd>
<dt>
</dt><dd> The result of which would be that all songs by Dismantled in the Media Library would be listed.</dd>
<dt><i>addpath path</i></dt>
<dd> Adds all songs in directory <i>path</i> into the Media Library.</dd>
<dt><i>rehash</i></dt>
<dd> Force the Media Library to check whether its data is up to date.</dd>
<dt><i>remove id</i></dt>
<dd> Removes a song from the Media Library with the id <i>id.</i></dd>
<dt><i>setstr id key value [source]</i></dt>
<dd> sets a string Media Library property with key <i>key</i> and value <i>value</i> for song with ID <i>id.</i> Optionally a source can be supplied with the <i>source</i> argument. If no source is defined client/xmms2-cli will be used.</dd>
<dt><i>setint id key value [source]</i></dt>
<dd> Sets a string Media Library property with key <i>key</i> and value <i>value</i> for song with ID <i>id.</i> Optionally a source can be supplied with the <i>source</i> argument. If no source is defined client/xmms2-cli will be used.</dd>
<dt><i>rmprop id key [source]</i></dt>
<dd> Removes properties from the Media Library entry with <i>id</i> and with key <i>key</i> and optionally source <i>source.</i></dd>
<dt><i>addcover file id</i></dt>
<dd> Add a cover image for id(s) <i>id.</i></dd></dl>
<p> The Media Library allows for any variety of keys (sometimes called properties) to be stored within. There is no set list of available keys but rather the Media Library can store any variety of different values. For this reason it is difficult to give a complete list of available keys but some examples are:</p>
<dl>
<dt><i>url</i></dt>
<dd> The path to the song in url</dd>
<dt><i>added</i></dt>
<dd> The time in seconds since UTC 00:00:00, 1 Jan 1970 that the song was added to the Media Library</dd>
<dt><i>mime</i></dt>
<dd> The MIME type of the song in the Media Library</dd>
<dt><i>lmod</i></dt>
<dd> The last time in seconds since UTC 00:00:00, 1 Jan 1970 that the song was modified</dd>
<dt><i>laststarted</i></dt>
<dd> The last time the song was played</dd>
<dt><i>timesplayed</i></dt>
<dd> The number of times the song was played</dd>
<dt><i>duration</i></dt>
<dd> The length of the song in milliseconds</dd>
<dt><i>bitrate</i></dt>
<dd> The bitrate of the song in bps</dd>
<dt><i>album</i></dt>
<dd> The name of the album the song is on</dd>
<dt><i>artist</i></dt>
<dd> The name of the artist that produced the song</dd>
<dt><i>title</i></dt>
<dd> The title of the song</dd>
<dt><i>tracknr</i></dt>
<dd> The track number of the song</dd>
<dt><i>{album, artist, track}_id</i></dt>
<dd> MusicBrainz ID numbers for the song</dd></dl>
<h2>PLAYLIST</h2>
<p> <code>XMMS2</code> has support for playlists which is tightly coupled with <code>XMMS2&#8217;s</code> Collections system. Playlist manipulation is accessible with the <i>playlist</i> command of <i>xmms2.</i> <i>xmms2 playlist</i> includes many commands for manipulating and retrieving data about playlists.</p>
<dl>
<dt><code>The</code>following</dt>
<dd> <i>playlist</i> commands are currently recognized:</dd>
<dt><i>list</i></dt>
<dd> Lists all currently available playlists.</dd>
<dt><i>create [playlistname]</i></dt>
<dd> Create a new playlist named <i>playlistname.</i></dd>
<dt><i>type [playlistname] [type]</i></dt>
<dd> Sets type of the playlist named <i>playlistname</i> to type <i>type.</i> Descriptions of the available types can be found later in the <code>PLAYLIST</code> section of this manual page.</dd>
<dt><i>load [playlistname]</i></dt>
<dd> Load a playlist specified by <i>playlistname</i> from the Media Library</dd>
<dt><i>remove [playlistname]</i></dt>
<dd> Remove a playlist specified by <i>playlistname</i> from the Media Library</dd></dl>
<p> <code>XMMS2</code> currently supports three types of playlists, each of these playlists has a number of attributes which can be set using the <i>coll attr</i> command described in the <code>COLLECTIONS</code> section of this manual page. The available playlist types are:</p>
<dl>
<dt><i>list</i></dt>
<dd> A simple list of medialib ids. The <i>list</i> has one attribute: <i>jumplist</i> which is the name of a playlist to jump to when the list is finished.</dd>
<dt><i>queue</i></dt>
<dd> A static playlist which supports a fixed length playlist where songs are removed as they are played. The <i>queue</i> has two attributes: <i>jumplist</i> which is the name of a playlist to jump to when the queue is finished <i>history</i> which is the number of played entries to keep before beginning to remove them</dd>
<dt><i>pshuffle</i></dt>
<dd> A playlist which picks a configurable number of songs from a collection at random. The <i>pshuffle</i> has three attributes: <i>jumplist</i> which is the name of a playlist to jump to when the pshuffle is finished. A pshuffle playlist only finishes when the collection from which new songs are pulled dries up, for instance when filtering on timesplayed &lt; 1 <i>history</i> which is the number of played entries to keep before beginning to remove them <i>upcoming</i> which is the number of unplayed entries to show in the playlist</dd></dl>
<h2>COLLECTIONS</h2>
<p> <code>XMMS2</code> includes an extremely powerful method for querying and selecting music from the Media Library called Collections. Some of the features of collections are made accessible via the <i>xmms2</i> client. <i>xmms2 coll</i> includes many commands for manipulating and retrieving data about Collections.</p>
<dl>
<dt><code>The</code>following</dt>
<dd> <i>coll </i> commands are currently recognized:</dd>
<dt><i>save [collname] [pattern]</i></dt>
<dd> Save the pattern <i>pattern</i> as a Collection named <i>collname</i></dd>
<dt><i>rename [oldname] [newname]</i></dt>
<dd> Rename a Collection from <i>oldname</i> to <i>newname.</i></dd>
<dt><i>list [namespace]</i></dt>
<dd> List all Collections, or if <i>namespace</i> is specified list only collections in the Collections or Playlists namespace.</dd>
<dt><i>query [collname] [order]</i></dt>
<dd> Retrieve information about all media in the Collection named <i>collname</i> ordered by <i>order</i></dd>
<dt><i>queryadd [collname] [order]</i></dt>
<dd> Add all media from the Collection <i>collname</i> ordered by <i>order</i> to the active playlist</dd>
<dt><i>find [mid] [namespace]</i></dt>
<dd> Find all collections in <i>namespace</i> that include the media referenced by <i>mid</i></dd>
<dt><i>get [collname]</i></dt>
<dd> Display information about the Collection <i>collname</i></dd>
<dt><i>remove [collname]</i></dt>
<dd> Remove the collection referenced by <i>collname</i></dd>
<dt><i>attr [collname] [attr] [val]</i></dt>
<dd> Set or get an attribute of name <i>attr</i> to value <i>val</i> on Collection <i>collname</i></dd></dl>
<p> <i>xmms2</i> sometimes requires that the namespace of a Collection be specified in <i>collname.</i> This is done by prepending either <i>Playlists/</i> or <i>Collections/</i> to the beginning of the Collection name. If not specified the namespace defaults to <i>Collections.</i></p>
<h2>FILES</h2>
<dl>
<dt><i>$XDG_CONFIG_HOME/xmms2/clients/cli.conf or $HOME/Library/xmms2/clients/cli.conf or $HOME/.config/xmms2/clients/cli.conf</i></dt>
<dd> A configuration file containing basic configuration values for <i>xmms2,</i> including the output format used by the <i>list</i> and <i>status</i> commands.</dd></dl>
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><i>XMMS_PATH</i></dt>
<dd> The URL path to <i>xmms2d.</i></dd>
<dt><i>XDG_CONFIG_HOME</i></dt>
<dd> The path where the xmms2 configuration files are located See <code>IPC SOCKET</code> in <i>xmms2d(8)</i> for details of possible values for this variable </dd>
</dl>
<h2>SEE ALSO</h2>
<p> xmms2d(8), <a rel="nofollow" href="http://xmms2.xmms.org">http://xmms2.xmms.org</a></p>
<h2>HISTORY</h2>
<p> The <code>XMMS2</code> Project was started by Tobias Rundström and Anders Gustafsson. It is developed with their lead by a small group of contributors from all over the world.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Alexander Botero-Lowry &lt;alex [at] foxybanana.com&gt; </p>
