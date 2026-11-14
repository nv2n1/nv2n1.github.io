---
title: "nyxmms2(1)"
name: "nyxmms2"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nyxmms2/"
description: "nycli – New Korving CLI"
---

<h2>NAME</h2>
<p> nycli &#8211; New Korving CLI</p>
<h2>SYNOPSIS</h2>
<p> <code>nyxmms2</code> [command] [arguments]</p>
<h2>DESCRIPTION</h2>
<p> <code>nycli</code> is the new official CLI XMMS2 client, replacing <code><a href="/docs/linux/man/1-xmms2/">xmms2</a></code>(1).</p>
<h2>INVOCATION</h2>
<h3>INLINE MODE</h3>
<p> If <code>nycli</code> is passed a command as an argument, that command will be interpreted and <code>nycli</code> will exit after it is finished.</p>
<h3>INTERACTIVE MODE</h3>
<p> <code>nycli</code> features a powerful shell-like environment via readline that allows the user to enter commands at a prompt and have the usual cool features such as pathname expansion and line editing.</p>
<h2>GENERAL COMMANDS</h2>
<dl>
<dt><code>play</code></p>
<dd></dl>
<dl>
<dt>
<dd> Start playback.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>pause</code></p>
<dd></dl>
<dl>
<dt>
<dd> Pause playback.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>stop</code> [-n &lt;tracks&gt; | -t &lt;time&gt;]</p>
<dd></dl>
<dl>
<dt>
<dd> Stop playback.</dl>
<dl>
<dt>
<dd> -n | &#8211;tracks</dl>
<dl>
<dt>
<dd> Number of tracks after which to stop playback.</dl>
<dl>
<dt>
<dd> -t | &#8211;time</dl>
<dl>
<dt>
<dd> Duration after which to stop playback.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>toggle</code></p>
<dd></dl>
<dl>
<dt>
<dd> Toggle playback.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>seek</code> &lt;time|offset&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Seek to a relative or absolute position.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>status</code> [-r &lt;time&gt;] [-f &lt;format&gt;]</p>
<dd></dl>
<dl>
<dt>
<dd> Display playback status, either continuously or once.</dl>
<dl>
<dt>
<dd> -r | &#8211;refresh</dl>
<dl>
<dt>
<dd> Delay between each refresh of the status. If 0, the status is only printed once (default).</dl>
<dl>
<dt>
<dd> -f | &#8211;format</dl>
<dl>
<dt>
<dd> Format string used to display status.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>prev</code> [offset]</p>
<dd></dl>
<dl>
<dt>
<dd> Jump to previous song.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>next</code> [offset]</p>
<dd></dl>
<dl>
<dt>
<dd> Jump to next song.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>jump</code> [-b] &lt;pattern|positions&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Jump to the first media maching the pattern.</dl>
<dl>
<dt>
<dd> -b | &#8211;backward</dl>
<dl>
<dt>
<dd> Jump backward to the first media matching the pattern</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>info</code> &lt;pattern|positions&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Display all the properties for all media matching the pattern.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>search</code> [-p &lt;name&gt; | -c &lt;name&gt;] [-o &lt;prop1[,prop2&#8230;]&gt;] [-l &lt;prop1[,prop2&#8230;]&gt;] &lt;pattern&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Search and print all media matching the pattern. Search can be restricted to a collection or a playlist by using the corresponding flag.</dl>
<dl>
<dt>
<dd> -p | &#8211;playlist</dl>
<dl>
<dt>
<dd> Search in the given playlist.</dl>
<dl>
<dt>
<dd> -c | &#8211;collection</dl>
<dl>
<dt>
<dd> Search in the given collection.</dl>
<dl>
<dt>
<dd> -o | &#8211;order</dl>
<dl>
<dt>
<dd> List of properties to order by (prefix by &#8216;-&#8216; for reverse ordering).</dl>
<dl>
<dt>
<dd> -l | &#8211;columns</dl>
<dl>
<dt>
<dd> List of properties to use as columns.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>list</code> [-p &lt;name&gt;] [pattern]</p>
<dd></dl>
<dl>
<dt>
<dd> List the contents of a playlist (the active playlist by default). If a pattern is provided, contents are further filtered and only the matching media are displayed.</dl>
<dl>
<dt>
<dd> -p | &#8211;playlist</dl>
<dl>
<dt>
<dd> List the given playlist.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>add</code> [-f [-N] [-P]] [-p &lt;playlist&gt; | -c &lt;collection&gt;] [-n | -a &lt;pos|offset&gt;] [pattern | paths]</p>
<dd></dl>
<dl>
<dt>
<dd> Add the matching media or files to a playlist.</dl>
<dl>
<dt>
<dd> -f | &#8211;file</dl>
<dl>
<dt>
<dd> Treat the arguments as file paths instead of a pattern.</dl>
<dl>
<dt>
<dd> -P | &#8211;pls</dl>
<dl>
<dt>
<dd> Treat the files as playlist files (implies &#8211;file.)</dl>
<dl>
<dt>
<dd> -t | &#8211;pattern</dl>
<dl>
<dt>
<dd> Force treating arguments as pattern.</dl>
<dl>
<dt>
<dd> -N | &#8211;non-recursive</dl>
<dl>
<dt>
<dd> Do not add directories recursively.</dl>
<dl>
<dt>
<dd> -p | &#8211;playlist</dl>
<dl>
<dt>
<dd> Add to the given playlist.</dl>
<dl>
<dt>
<dd> -n | &#8211;next</dl>
<dl>
<dt>
<dd> Add after the current track.</dl>
<dl>
<dt>
<dd> -a | &#8211;at</dl>
<dl>
<dt>
<dd> Add media at a given position in the playlist, or at a given offset from the current track.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>remove</code> [-p &lt;playlist&gt;] &lt;pattern|positions&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Remove the matching media from a playlist.</dl>
<dl>
<dt>
<dd> -p | &#8211;playlist</dl>
<dl>
<dt>
<dd> Remove from the given playlist, instead of the active playlist.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>move</code> [-p &lt;playlist&gt;] [-n | -a &lt;pos|offset&gt;] &lt;pattern|positions&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Move entries inside a playlist.</dl>
<dl>
<dt>
<dd> -p | &#8211;playlist</dl>
<dl>
<dt>
<dd> Playlist to act on.</dl>
<dl>
<dt>
<dd> -n | &#8211;next</dl>
<dl>
<dt>
<dd> Move the matching tracks after the current track.</dl>
<dl>
<dt>
<dd> -a | &#8211;at</dl>
<dl>
<dt>
<dd> Move the matching tracks by an offset or to a position.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>exit</code></p>
<dd></dl>
<dl>
<dt>
<dd> Exit the shell-like interface.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>help</code> [-a] [command]</p>
<dd></dl>
<dl>
<dt>
<dd> List all commands, or help on one command.</dl>
<dl>
<dt>
<dd> -a | &#8211;alias</dl>
<dl>
<dt>
<dd> List aliases, or alias definition.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<h2>PLAYLIST COMMANDS</h2>
<dl>
<dt><code>playlist list</code> [-a] [pattern]</p>
<dd></dl>
<dl>
<dt>
<dd> List all playlists.</dl>
<dl>
<dt>
<dd> -a | &#8211;all</dl>
<dl>
<dt>
<dd> Include hidden playlists.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>playlist</code></p>
<dd></dl>
<dl>
<dt>
<dd> No description</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>playlist switch</code> &lt;playlist&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Change the active playlist.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>playlist create</code> [-p &lt;playlist&gt;] &lt;name&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Change the active playlist.</dl>
<dl>
<dt>
<dd> -p | &#8211;playlist</dl>
<dl>
<dt>
<dd> Copy the content of the playlist into the new playlist.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>playlist rename</code> [-f] [-p &lt;playlist&gt;] &lt;newname&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Rename a playlist. By default, rename the active playlist.</dl>
<dl>
<dt>
<dd> -f | &#8211;force</dl>
<dl>
<dt>
<dd> Force the rename of the collection, overwrite an existing collection if needed.</dl>
<dl>
<dt>
<dd> -p | &#8211;playlist</dl>
<dl>
<dt>
<dd> Rename the given playlist.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>playlist remove</code> &lt;playlist&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Remove the given playlist.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>playlist clear</code> </p>
<dd></dl>
<dl>
<dt>
<dd> Clear a playlist. By default, clear the active playlist.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>playlist shuffle</code> </p>
<dd></dl>
<dl>
<dt>
<dd> Shuffle a playlist. By default, shuffle the active playlist.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>playlist sort</code> [-o &lt;order&gt;] </p>
<dd></dl>
<dl>
<dt>
<dd> Sort a playlist. By default, sort the active playlist.</dl>
<dl>
<dt>
<dd> -o | &#8211;order</dl>
<dl>
<dt>
<dd> List of properties to sort by (prefix by &#8216;-&#8216; for reverse sorting).</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>playlist config</code> [-t &lt;type&gt;] [-s &lt;history&gt;] [-u &lt;upcoming&gt;] [-i &lt;coll&gt;] </p>
<dd></dl>
<dl>
<dt>
<dd> Configure a playlist by changing its type, attributes, etc. By default, configure the active playlist.</dl>
<dl>
<dt>
<dd> -t | &#8211;type</dl>
<dl>
<dt>
<dd> Change the type of the playlist: list, queue, pshuffle.</dl>
<dl>
<dt>
<dd> -s | &#8211;history</dl>
<dl>
<dt>
<dd> Size of the history of played tracks (for queue, pshuffle).</dl>
<dl>
<dt>
<dd> -u | &#8211;upcoming</dl>
<dl>
<dt>
<dd> Number of upcoming tracks to maintain (for pshuffle).</dl>
<dl>
<dt>
<dd> -i | &#8211;input</dl>
<dl>
<dt>
<dd> Input collection for the playlist (for pshuffle). Default to &#8216;All Media&#8217;.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<h2>COLLECTION COMMANDS</h2>
<dl>
<dt><code>collection list</code></p>
<dd></dl>
<dl>
<dt>
<dd> List all collections.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>collection</code></p>
<dd></dl>
<dl>
<dt>
<dd> No description</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>collection show</code> &lt;collection&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Display a human-readable description of a collection.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>collection create</code> [-f] [-a | -e] [-c &lt;collection&gt;] &lt;name&gt; [pattern]</p>
<dd></dl>
<dl>
<dt>
<dd> Create a new collection. If pattern is provided, it is used to define the collection. Otherwise, the new collection contains the whole media library.</dl>
<dl>
<dt>
<dd> -f | &#8211;force</dl>
<dl>
<dt>
<dd> Force creating of the collection, overwrite an existing collection if needed.</dl>
<dl>
<dt>
<dd> -c | &#8211;collection</dl>
<dl>
<dt>
<dd> Copy an existing collection to the new one.</dl>
<dl>
<dt>
<dd> -e | &#8211;empty</dl>
<dl>
<dt>
<dd> Initialize an empty collection.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>collection rename</code> [-f] &lt;oldname&gt; &lt;newname&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Rename a collection.</dl>
<dl>
<dt>
<dd> -f | &#8211;force</dl>
<dl>
<dt>
<dd> Force renaming of the collection, overwrite an existing collection if needed.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>collection remove</code> &lt;collection&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Remove a collection.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>collection config</code> &lt;collection&gt; [attrname [attrvalue]]</p>
<dd></dl>
<dl>
<dt>
<dd> Get or set attributes for the given collection. If no attribute name is provided, list all attributes. If only an attribute name is provided, display the value of the attribute. If both attribute name and value are provided, set the new value of the attribute.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<h2>SERVER COMMANDS</h2>
<dl>
<dt><code>server import</code> [-N] &lt;path&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Import new files into the media library. By default, directories are imported recursively.</dl>
<dl>
<dt>
<dd> -N | &#8211;non-recursive</dl>
<dl>
<dt>
<dd> Do not import directories recursively.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>server</code></p>
<dd></dl>
<dl>
<dt>
<dd> No description</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>server remove</code> &lt;pattern&gt;</p>
<dd></dl>
<dl>
<dt>
<dd> Remove the matching media from the media library.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>server rehash</code> [pattern]</p>
<dd></dl>
<dl>
<dt>
<dd> Rehash the media matched by the pattern, or the whole media library if no pattern is provided</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>server config</code> [name [value]]</p>
<dd></dl>
<dl>
<dt>
<dd> Get or set configuration values. If no name or value is provided, list all configuration values. If only a name is provided, display the content of the corresponding configuration value. If both name and a value are provided, set the new content of the configuration value.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>server property</code> [-i | -s | -D] [-S] &lt;mid&gt; [name [value]]</p>
<dd></dl>
<dl>
<dt>
<dd> Get or set properties for a given media. If no name or value is provided, list all properties. If only a name is provided, display the value of the property. If both a name and a value are provided, set the new value of the property. </p>
<p> By default, set operations use client specific source and list, display operations use source-preference. Use the &#8211;source option to override this behaviour. </p>
<p> By default, the value will be used to determine whether it should be saved as a string or an integer. Use the &#8211;int or &#8211;string flag to override this behaviour.</dl>
<dl>
<dt>
<dd> -i | &#8211;int</dl>
<dl>
<dt>
<dd> Force the value to be treated as integer.</dl>
<dl>
<dt>
<dd> -s | &#8211;string</dl>
<dl>
<dt>
<dd> Force the value to be treated as a string.</dl>
<dl>
<dt>
<dd> -D | &#8211;delete</dl>
<dl>
<dt>
<dd> Delete the selected property.</dl>
<dl>
<dt>
<dd> -S | &#8211;source</dl>
<dl>
<dt>
<dd> Property source.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>server plugins</code></p>
<dd></dl>
<dl>
<dt>
<dd> List the plugins loaded in the server.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>server volume</code> [-c &lt;name&gt;] [value]</p>
<dd></dl>
<dl>
<dt>
<dd> Get or set the audio volume (in a range of 0-100). If a value is provided, set the new value of the volume. Otherwise, display the current volume. By default, the command applies to all audio channels. Use the &#8211;channel flag to override this behaviour.</dl>
<dl>
<dt>
<dd> -c | &#8211;channel</dl>
<dl>
<dt>
<dd> Get or set the volume only for one channel.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>server stats</code></p>
<dd></dl>
<dl>
<dt>
<dd> Display statistics about the server: uptime, version, size of the medialib, etc</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>server sync</code></p>
<dd></dl>
<dl>
<dt>
<dd> Force the saving of collections to the disk (otherwise only performed on shutdown)</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>server shutdown</code></p>
<dd></dl>
<dl>
<dt>
<dd> Shutdown the server.</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<h2>ALIASES</h2>
<p> A list of command aliases are read from the configuration file in the section [alias] at runtime. The syntax of <code>nycli</code> aliases are somewhat similar to bash and other shells. An alias is defined by a list of semi-colon separated commands and arguments. Parameter expansion is supported (see <code>EXPANSION</code> below). </p>
<dl>
<dt>The default configuration includes the following aliases:</p>
<dd></dl>
<dl>
<dt><code>addpls</code></p>
<dd></dl>
<dl>
<dt>
<dd> add -f -P $@</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>current</code></p>
<dd></dl>
<dl>
<dt>
<dd> status -f $1</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>server kill</code></p>
<dd></dl>
<dl>
<dt>
<dd> server shutdown</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>mute</code></p>
<dd></dl>
<dl>
<dt>
<dd> server volume 0</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>repeat</code></p>
<dd></dl>
<dl>
<dt>
<dd> seek 0</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>ls</code></p>
<dd></dl>
<dl>
<dt>
<dd> list</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>quit</code></p>
<dd></dl>
<dl>
<dt>
<dd> exit</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>clear</code></p>
<dd></dl>
<dl>
<dt>
<dd> playlist clear</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<dl>
<dt><code>scap</code></p>
<dd></dl>
<dl>
<dt>
<dd> stop ; playlist clear ; add $@ ; play</dl>
<dl>
<dt>
<dd> -h | &#8211;help</dl>
<dl>
<dt>
<dd> Display command help.</dl>
<h3>EXPANSION</h3>
<dl>
<dt>
<dd> <code>Positional Parameters</code></dl>
<dl>
<dt>
<dd> An alias can use positional parameters, for example: </p>
<p> foo = add -f $1 $3 </p>
<p> foo ctkoz.ogg and slre.ogg </p>
<p> Will result in: </p>
<p> add -f ctkoz.ogg slre.ogg </p>
</dl>
<dl>
<dt>
<dd> <code>Special Parameters</code></dl>
<dl>
<dt>
<dd> <code>$@</code></p>
<dl>
<dt>
<dd> This expands to all parameters passed to the alias.</dl>
</dl>
<h2>CONFIGURATION</h2>
<p> PROMPT</p>
<dl>
<dt>
<dd> String to use as a prompt in <code>INTERACTIVE MODE</code></dl>
<p> SERVER_AUTOSTART</p>
<dl>
<dt>
<dd> Boolean, if true nycli will attempt to start <code><a href="/docs/linux/man/1-xmms2d/">xmms2d</a></code>(1) if it&#8217;s not running already.</dl>
<p> AUTO_UNIQUE_COMPLETE</p>
<dl>
<dt>
<dd> Boolean</dl>
<p> PLAYLIST_MARKER</p>
<dl>
<dt>
<dd> String to use to mark the current active entry in the playlist</dl>
<p> GUESS_PLS</p>
<dl>
<dt>
<dd> Boolean, try to guess if the URL is a playlist and add accordingly. (Not reliable)</dl>
<p> CLASSIC_LIST</p>
<dl>
<dt>
<dd> Boolean, format <code>list</code> output similar to the classic cli.</dl>
<p> CLASSIC_LIST_FORMAT</p>
<dl>
<dt>
<dd> String to format classic <code>list</code> output with.</dl>
<p> STATUS_FORMAT</p>
<dl>
<dt>
<dd> String to format <code>status</code> output with.</dl>
<h2>FILES</h2>
<p> $XDG_CONFIG_HOME/xmms2/clients/nycli.conf</p>
<dl>
<dt>
<dd> The configuration file for <code>nycli</code></dl>
<h2>BUGS</h2>
<p> Please report all bugs at <a rel="nofollow" href="http://bugs.xmms2.xmms.se">http://bugs.xmms2.xmms.se</a></p>
<h2>AUTHORS</h2>
<p> Igor Assis, Anders Waldenborg, Anthony Garcia, Sebastien Cevey, and Jonne Lehtinen </p>
<p> See the <code>AUTHORS</code> file in the XMMS2 source distribution for more info. </p>
<p> The blame for this man page is on Anthony. </p>
<p> If you contributed and feel you should be listed here please send me a mail. </p>
<h2>Index</h2>
