---
title: "xmms2(1)"
name: "xmms2"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmms2/"
description: "xmms2 – offers a simple command-line interface to the XMMS2 daemon"
---

<h2>NAME</h2>
<p> xmms2 &#8211; offers a simple command-line interface to the XMMS2 daemon</p>
<h2>SYNOPSIS</h2>
<p> <i>xmms2</i> <code>command</code> <i>xmms2</i> <code>mlib</code> <code>command</code> <i>xmms2</i> <code>playlist</code> <code>command</code> <i>xmms2</i> <code>coll</code> <code>command </code></p>
<h2>DESCRIPTION</h2>
<p> <code>XMMS2 </code> is a redesign of the XMMS (<a rel="nofollow" href="http://www.xmms.org)">http://www.xmms.org)</a> music player. It features a client-server model, allowing multiple (even simultaneous!) user interfaces, both textual and graphical. All common audio formats are supported using plugins. On top of this, there is a flexible media library to organize your music. </p>
<p> <i>xmms2</i> is the official command-line interface client for <code>XMMS2</code> and acts as a reference implementation for the development of new clients. <i>xmms2</i> is able to issue commands to control the active playlist and playback as well as commands to control the media library. </p>
<p> The following commands effect the current <code>XMMS2</code> playlist. </p>
<p> <i>xmms2</i> includes many commands that allow the user to execute actions on <i>xmms2d.</i></p>
<dl>
<dt><code>These</code>commands<code>are</code>currently<code>recognized:</code></p>
<dd>
<dt><i>add  url&#8230;</i></p>
<dd> Adds URL(s) to <i>playlist</i> or the active playlist.</p>
<dt><i>addarg  url arguments</i></p>
<dd> Adds an URL to <i>playlist</i> or the active playlist, with arguments.</p>
<dt><i>addid  medialib_id&#8230;</i></p>
<dd> Adds song(s) to <i>playlist</i> or the active playlist using its Media Library ID.</p>
<dt><i>addpls  url</i></p>
<dd> Adds a playlist in a file to <i>playlist</i> or the active playlist.</p>
<dt><i>insert  pos url</i></p>
<dd> Adds a URL to <i>playlist</i> or the active playlist at a specific position.</p>
<dt><i>insertid  pos medialib_id</i></p>
<dd> Adds a song to <i>playlist</i> or the active playlist at a specific position using its Media Library ID.</p>
<dt><i>radd  directory</i></p>
<dd> Adds a directory of songs recursively to <i>playlist</i> or the active playlist.</p>
<dt><i>clear </i></p>
<dd> Clears all entries from <i>playlist</i> or the active playlist.</p>
<dt><i>shuffle </i></p>
<dd> Places the songs in <i>playlist</i> or the active playlist in a random order.</p>
<dt><i>sort property</i></p>
<dd> Sort the active playlist based on metadata from the Media Library. The metadata which is used for the sorting is based on what was given for <i>property.</i> An overview of the media library, and the potential properties, can be found in the <code>MEDIA LIBRARY</code> section of this manual page.</p>
<dt><i>sort playlist properties</i></p>
<dd> Sort <i>playlist</i> based on metadata from the Media Library. Separate the properties with a spaces.</p>
<dt><i>remove  playlist_position</i></p>
<dd> Removes a song from <i>playlist </i> or the active playlist at the position given by <i>playlist_position.</i></p>
<dt><i>list </i></p>
<dd> Lists the contents of <i>playlist</i> or the active playlist. An explanation of how to change the output format can be found in the <code>FILES</code> section of this manual page.</p>
<dt><i>play</i></p>
<dd> Starts playback of the playlist.</p>
<dt><i>stop</i></p>
<dd> Stops playback of the playlist.</p>
<dt><i>toggleplay</i></p>
<dd> Toggles playback status between play/pause</p>
<dt><i>pause</i></p>
<dd> Pauses playback of the playlist.</p>
<dt><i>next</i></p>
<dd> Skips to the next song in the playlist.</p>
<dt><i>prev</i></p>
<dd> Skips to the previous song in the playlist.</p>
<dt><i>seek [+ / -]seconds</i></p>
<dd> Seeks to a specific position in the currently playing song. The way in which <i>seek</i> moves in the file is based on the arguments passed to it. If + is used <i>xmms2</i> will seek <i>seconds</i> forward in the song. If &#8211; is used <i>xmms2</i> will seek <i>seconds</i> backwards in the song. If merely a number of seconds is given <i>xmms2</i> will seek to that absolute position in the song.</p>
<dt><i>jump [+ / -]playlist_position</i></p>
<dd> Jumps to <i>playlist_position</i> in the playlist or <i>playlist_position</i> forward/backward if + or &#8211; is specified.</p>
<dt><i>move  playlist_position new_position</i></p>
<dd> Moves the song at <i>playlist position</i> to the position denoted by <i>new_position in</i> <i>playlist</i> or the active playlist.</p>
<dt><i>volume channel volume</i></p>
<dd> Sets the volume of <i>channel</i> to <i>volume.</i></p>
<dt><i>volume_list</i></p>
<dd> Lists the volume for each channel.</p>
<dt><i>mlib</i></p>
<dd> Allows for the manipulation of the Media Library. The significance of the sub-commands of <i>mlib</i> can be found in the <code>MEDIA LIBRARY</code> section of this manual page.</p>
<dt><i>playlist</i></p>
<dd> Allows for the manipulation of playlists. The significance of the sub-commands of <i>playlist</i> can be found in the <code>PLAYLIST</code> section of this manual page.</p>
<dt><i>coll</i></p>
<dd> Allows for the manipulation of collections. The significance of this sub-commands of <i>coll</i> can be found in the <code>COLLECTIONS</code> section of this manual page.</p>
<dt><i>browse url</i></p>
<dd> Lists the contents of <i>url</i> in a list of encoded urls.</p>
<dt><i>status</i></p>
<dd> Gives a live status of the currently playing song.</p>
<dt><i>info [id]</i></p>
<dd> Gives the metadata archived by the Media Library for Media Library id <i>id</i> or the currently playing song.</p>
<dt><i>current [pattern]</i></p>
<dd> Gives some summary of the currently playing song&#8217;s meta data. A pattern can be specified in the form &quot;${album} &#8211; ${tracknr}&quot;. Please be aware of your shells substitution features.</p>
<dt><i>config config_key [=] value</i></p>
<dd> Sets <i>config_key</i> to <i>value</i> on <i><a href="/docs/linux/man/8-xmms2d/">xmms2d</a>(8).</i></p>
<dt><i>config_list</i></p>
<dd> Lists all the configuration values of <code>XMMS2.</code></p>
<dt><i>plugin_list</i></p>
<dd> Prints a list of the plugins being used by <code>XMMS2.</code></p>
<dt><i>stats</i></p>
<dd> Retrieves the uptime and version from <code>XMMS2.</code></p>
<dt><i>quit</i></p>
<dd> Makes <i><a href="/docs/linux/man/8-xmms2d/">xmms2d</a>(8)</i> quit.</p>
<dt><i>help</i></p>
<dd> Prints a concise overview of all commands offered by <i>xmms2.</i></dl>
<h2>MEDIA LIBRARY</h2>
<p> <code>XMMS2</code> stores metadata about every song in the Media Library. One can retrieve data from the Media Library using the <i>mlib </i> command of <i>xmms2.</i> The Media Library is an SQL database which is created and accessed by use of the sqlite library. <i>xmms2 mlib</i> includes many commands for manipulating and retrieving data from the Media Library.</p>
<dl>
<dt><code>The</code>following</p>
<dd> <i>mlib </i> commands are currently recognized:</p>
<dt><i>add url</i></p>
<dd> Adds a URL to the Media Library but not to the current playlist. The Media Library also fetches associated metadata for the added song.</p>
<dt><i>loadall</i></p>
<dd> Load all songs in the Media Library into the current playlist.</p>
<dt><i>searchadd pattern</i></p>
<dd> Searches the Media Library for songs that match <i>pattern</i> criteria and adds them to the current playlist.</p>
<dt><i>search pattern</i></p>
<dd> Searches and returns a list of songs in the Media Library that match <i>pattern.</i></p>
<dt>
<dd> For example one could execute:</p>
<dt>
<dd> <i>xmms2 mlib search artist:Dismantled</i></p>
<dt>
<dd> The result of which would be that all songs by Dismantled in the Media Library would be listed.</p>
<dt><i>addpath path</i></p>
<dd> Adds all songs in directory <i>path</i> into the Media Library.</p>
<dt><i>rehash</i></p>
<dd> Force the Media Library to check whether its data is up to date.</p>
<dt><i>remove id</i></p>
<dd> Removes a song from the Media Library with the id <i>id.</i></p>
<dt><i>setstr id key value [source]</i></p>
<dd> sets a string Media Library property with key <i>key</i> and value <i>value</i> for song with ID <i>id.</i> Optionally a source can be supplied with the <i>source</i> argument. If no source is defined client/xmms2-cli will be used.</p>
<dt><i>setint id key value [source]</i></p>
<dd> Sets a string Media Library property with key <i>key</i> and value <i>value</i> for song with ID <i>id.</i> Optionally a source can be supplied with the <i>source</i> argument. If no source is defined client/xmms2-cli will be used.</p>
<dt><i>rmprop id key [source]</i></p>
<dd> Removes properties from the Media Library entry with <i>id</i> and with key <i>key</i> and optionally source <i>source.</i></p>
<dt><i>addcover file id</i></p>
<dd> Add a cover image for id(s) <i>id.</i></dl>
<p> The Media Library allows for any variety of keys (sometimes called properties) to be stored within. There is no set list of available keys but rather the Media Library can store any variety of different values. For this reason it is difficult to give a complete list of available keys but some examples are:</p>
<dl>
<dt><i>url</i></p>
<dd> The path to the song in url</p>
<dt><i>added</i></p>
<dd> The time in seconds since UTC 00:00:00, 1 Jan 1970 that the song was added to the Media Library</p>
<dt><i>mime</i></p>
<dd> The MIME type of the song in the Media Library</p>
<dt><i>lmod</i></p>
<dd> The last time in seconds since UTC 00:00:00, 1 Jan 1970 that the song was modified</p>
<dt><i>laststarted</i></p>
<dd> The last time the song was played</p>
<dt><i>timesplayed</i></p>
<dd> The number of times the song was played</p>
<dt><i>duration</i></p>
<dd> The length of the song in milliseconds</p>
<dt><i>bitrate</i></p>
<dd> The bitrate of the song in bps</p>
<dt><i>album</i></p>
<dd> The name of the album the song is on</p>
<dt><i>artist</i></p>
<dd> The name of the artist that produced the song</p>
<dt><i>title</i></p>
<dd> The title of the song</p>
<dt><i>tracknr</i></p>
<dd> The track number of the song</p>
<dt><i>{album, artist, track}_id</i></p>
<dd> MusicBrainz ID numbers for the song</dl>
<h2>PLAYLIST</h2>
<p> <code>XMMS2</code> has support for playlists which is tightly coupled with <code>XMMS2&#8217;s</code> Collections system. Playlist manipulation is accessible with the <i>playlist</i> command of <i>xmms2.</i> <i>xmms2 playlist</i> includes many commands for manipulating and retrieving data about playlists.</p>
<dl>
<dt><code>The</code>following</p>
<dd> <i>playlist</i> commands are currently recognized:</p>
<dt><i>list</i></p>
<dd> Lists all currently available playlists.</p>
<dt><i>create [playlistname]</i></p>
<dd> Create a new playlist named <i>playlistname.</i></p>
<dt><i>type [playlistname] [type]</i></p>
<dd> Sets type of the playlist named <i>playlistname</i> to type <i>type.</i> Descriptions of the available types can be found later in the <code>PLAYLIST</code> section of this manual page.</p>
<dt><i>load [playlistname]</i></p>
<dd> Load a playlist specified by <i>playlistname</i> from the Media Library</p>
<dt><i>remove [playlistname]</i></p>
<dd> Remove a playlist specified by <i>playlistname</i> from the Media Library</dl>
<p> <code>XMMS2</code> currently supports three types of playlists, each of these playlists has a number of attributes which can be set using the <i>coll attr</i> command described in the <code>COLLECTIONS</code> section of this manual page. The available playlist types are:</p>
<dl>
<dt><i>list</i></p>
<dd> A simple list of medialib ids. The <i>list</i> has one attribute: <i>jumplist</i> which is the name of a playlist to jump to when the list is finished.</p>
<dt><i>queue</i></p>
<dd> A static playlist which supports a fixed length playlist where songs are removed as they are played. The <i>queue</i> has two attributes: <i>jumplist</i> which is the name of a playlist to jump to when the queue is finished <i>history</i> which is the number of played entries to keep before beginning to remove them</p>
<dt><i>pshuffle</i></p>
<dd> A playlist which picks a configurable number of songs from a collection at random. The <i>pshuffle</i> has three attributes: <i>jumplist</i> which is the name of a playlist to jump to when the pshuffle is finished. A pshuffle playlist only finishes when the collection from which new songs are pulled dries up, for instance when filtering on timesplayed &lt; 1 <i>history</i> which is the number of played entries to keep before beginning to remove them <i>upcoming</i> which is the number of unplayed entries to show in the playlist</dl>
<h2>COLLECTIONS</h2>
<p> <code>XMMS2</code> includes an extremely powerful method for querying and selecting music from the Media Library called Collections. Some of the features of collections are made accessible via the <i>xmms2</i> client. <i>xmms2 coll</i> includes many commands for manipulating and retrieving data about Collections.</p>
<dl>
<dt><code>The</code>following</p>
<dd> <i>coll </i> commands are currently recognized:</p>
<dt><i>save [collname] [pattern]</i></p>
<dd> Save the pattern <i>pattern</i> as a Collection named <i>collname</i></p>
<dt><i>rename [oldname] [newname]</i></p>
<dd> Rename a Collection from <i>oldname</i> to <i>newname.</i></p>
<dt><i>list [namespace]</i></p>
<dd> List all Collections, or if <i>namespace</i> is specified list only collections in the Collections or Playlists namespace.</p>
<dt><i>query [collname] [order]</i></p>
<dd> Retrieve information about all media in the Collection named <i>collname</i> ordered by <i>order</i></p>
<dt><i>queryadd [collname] [order]</i></p>
<dd> Add all media from the Collection <i>collname</i> ordered by <i>order</i> to the active playlist</p>
<dt><i>find [mid] [namespace]</i></p>
<dd> Find all collections in <i>namespace</i> that include the media referenced by <i>mid</i></p>
<dt><i>get [collname]</i></p>
<dd> Display information about the Collection <i>collname</i></p>
<dt><i>remove [collname]</i></p>
<dd> Remove the collection referenced by <i>collname</i></p>
<dt><i>attr [collname] [attr] [val]</i></p>
<dd> Set or get an attribute of name <i>attr</i> to value <i>val</i> on Collection <i>collname</i></dl>
<p> <i>xmms2</i> sometimes requires that the namespace of a Collection be specified in <i>collname.</i> This is done by prepending either <i>Playlists/</i> or <i>Collections/</i> to the beginning of the Collection name. If not specified the namespace defaults to <i>Collections.</i></p>
<h2>FILES</h2>
<dl>
<dt><i>$XDG_CONFIG_HOME/xmms2/clients/cli.conf or $HOME/Library/xmms2/clients/cli.conf or $HOME/.config/xmms2/clients/cli.conf</i></p>
<dd> A configuration file containing basic configuration values for <i>xmms2,</i> including the output format used by the <i>list</i> and <i>status</i> commands.</dl>
<h2>ENVIRONMENTAL VARIABLES</h2>
<dl>
<dt><i>XMMS_PATH</i></p>
<dd> The URL path to <i>xmms2d.</i></p>
<dt><i>XDG_CONFIG_HOME</i></p>
<dd> The path where the xmms2 configuration files are located See <code>IPC SOCKET</code> in <i><a href="/docs/linux/man/8-xmms2d/">xmms2d</a>(8)</i> for details of possible values for this variable </p>
</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/8-xmms2d/">xmms2d</a>(8), <a rel="nofollow" href="http://xmms2.xmms.org">http://xmms2.xmms.org</a></p>
<h2>HISTORY</h2>
<p> The <code>XMMS2</code> Project was started by Tobias Rundström and Anders Gustafsson. It is developed with their lead by a small group of contributors from all over the world.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Alexander Botero-Lowry &lt;alex [at] foxybanana.com&gt; </p>
<h2>Index</h2>
