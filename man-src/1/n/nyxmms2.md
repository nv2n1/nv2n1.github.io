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
<dt><code>play</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Start playback.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>pause</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Pause playback.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>stop</code> [-n &lt;tracks&gt; | -t &lt;time&gt;]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Stop playback.</dd></dl>
<dl>
<dt>
</dt><dd> -n | &#8211;tracks</dd></dl>
<dl>
<dt>
</dt><dd> Number of tracks after which to stop playback.</dd></dl>
<dl>
<dt>
</dt><dd> -t | &#8211;time</dd></dl>
<dl>
<dt>
</dt><dd> Duration after which to stop playback.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>toggle</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Toggle playback.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>seek</code> &lt;time|offset&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Seek to a relative or absolute position.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>status</code> [-r &lt;time&gt;] [-f &lt;format&gt;]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Display playback status, either continuously or once.</dd></dl>
<dl>
<dt>
</dt><dd> -r | &#8211;refresh</dd></dl>
<dl>
<dt>
</dt><dd> Delay between each refresh of the status. If 0, the status is only printed once (default).</dd></dl>
<dl>
<dt>
</dt><dd> -f | &#8211;format</dd></dl>
<dl>
<dt>
</dt><dd> Format string used to display status.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>prev</code> [offset]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Jump to previous song.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>next</code> [offset]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Jump to next song.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>jump</code> [-b] &lt;pattern|positions&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Jump to the first media maching the pattern.</dd></dl>
<dl>
<dt>
</dt><dd> -b | &#8211;backward</dd></dl>
<dl>
<dt>
</dt><dd> Jump backward to the first media matching the pattern</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>info</code> &lt;pattern|positions&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Display all the properties for all media matching the pattern.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>search</code> [-p &lt;name&gt; | -c &lt;name&gt;] [-o &lt;prop1[,prop2&#8230;]&gt;] [-l &lt;prop1[,prop2&#8230;]&gt;] &lt;pattern&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Search and print all media matching the pattern. Search can be restricted to a collection or a playlist by using the corresponding flag.</dd></dl>
<dl>
<dt>
</dt><dd> -p | &#8211;playlist</dd></dl>
<dl>
<dt>
</dt><dd> Search in the given playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -c | &#8211;collection</dd></dl>
<dl>
<dt>
</dt><dd> Search in the given collection.</dd></dl>
<dl>
<dt>
</dt><dd> -o | &#8211;order</dd></dl>
<dl>
<dt>
</dt><dd> List of properties to order by (prefix by &#8216;-&#8216; for reverse ordering).</dd></dl>
<dl>
<dt>
</dt><dd> -l | &#8211;columns</dd></dl>
<dl>
<dt>
</dt><dd> List of properties to use as columns.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>list</code> [-p &lt;name&gt;] [pattern]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> List the contents of a playlist (the active playlist by default). If a pattern is provided, contents are further filtered and only the matching media are displayed.</dd></dl>
<dl>
<dt>
</dt><dd> -p | &#8211;playlist</dd></dl>
<dl>
<dt>
</dt><dd> List the given playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>add</code> [-f [-N] [-P]] [-p &lt;playlist&gt; | -c &lt;collection&gt;] [-n | -a &lt;pos|offset&gt;] [pattern | paths]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Add the matching media or files to a playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -f | &#8211;file</dd></dl>
<dl>
<dt>
</dt><dd> Treat the arguments as file paths instead of a pattern.</dd></dl>
<dl>
<dt>
</dt><dd> -P | &#8211;pls</dd></dl>
<dl>
<dt>
</dt><dd> Treat the files as playlist files (implies &#8211;file.)</dd></dl>
<dl>
<dt>
</dt><dd> -t | &#8211;pattern</dd></dl>
<dl>
<dt>
</dt><dd> Force treating arguments as pattern.</dd></dl>
<dl>
<dt>
</dt><dd> -N | &#8211;non-recursive</dd></dl>
<dl>
<dt>
</dt><dd> Do not add directories recursively.</dd></dl>
<dl>
<dt>
</dt><dd> -p | &#8211;playlist</dd></dl>
<dl>
<dt>
</dt><dd> Add to the given playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -n | &#8211;next</dd></dl>
<dl>
<dt>
</dt><dd> Add after the current track.</dd></dl>
<dl>
<dt>
</dt><dd> -a | &#8211;at</dd></dl>
<dl>
<dt>
</dt><dd> Add media at a given position in the playlist, or at a given offset from the current track.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>remove</code> [-p &lt;playlist&gt;] &lt;pattern|positions&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Remove the matching media from a playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -p | &#8211;playlist</dd></dl>
<dl>
<dt>
</dt><dd> Remove from the given playlist, instead of the active playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>move</code> [-p &lt;playlist&gt;] [-n | -a &lt;pos|offset&gt;] &lt;pattern|positions&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Move entries inside a playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -p | &#8211;playlist</dd></dl>
<dl>
<dt>
</dt><dd> Playlist to act on.</dd></dl>
<dl>
<dt>
</dt><dd> -n | &#8211;next</dd></dl>
<dl>
<dt>
</dt><dd> Move the matching tracks after the current track.</dd></dl>
<dl>
<dt>
</dt><dd> -a | &#8211;at</dd></dl>
<dl>
<dt>
</dt><dd> Move the matching tracks by an offset or to a position.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>exit</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Exit the shell-like interface.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>help</code> [-a] [command]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> List all commands, or help on one command.</dd></dl>
<dl>
<dt>
</dt><dd> -a | &#8211;alias</dd></dl>
<dl>
<dt>
</dt><dd> List aliases, or alias definition.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<h2>PLAYLIST COMMANDS</h2>
<dl>
<dt><code>playlist list</code> [-a] [pattern]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> List all playlists.</dd></dl>
<dl>
<dt>
</dt><dd> -a | &#8211;all</dd></dl>
<dl>
<dt>
</dt><dd> Include hidden playlists.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>playlist</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> No description</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>playlist switch</code> &lt;playlist&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Change the active playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>playlist create</code> [-p &lt;playlist&gt;] &lt;name&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Change the active playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -p | &#8211;playlist</dd></dl>
<dl>
<dt>
</dt><dd> Copy the content of the playlist into the new playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>playlist rename</code> [-f] [-p &lt;playlist&gt;] &lt;newname&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Rename a playlist. By default, rename the active playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -f | &#8211;force</dd></dl>
<dl>
<dt>
</dt><dd> Force the rename of the collection, overwrite an existing collection if needed.</dd></dl>
<dl>
<dt>
</dt><dd> -p | &#8211;playlist</dd></dl>
<dl>
<dt>
</dt><dd> Rename the given playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>playlist remove</code> &lt;playlist&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Remove the given playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>playlist clear</code> </dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Clear a playlist. By default, clear the active playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>playlist shuffle</code> </dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Shuffle a playlist. By default, shuffle the active playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>playlist sort</code> [-o &lt;order&gt;] </dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Sort a playlist. By default, sort the active playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -o | &#8211;order</dd></dl>
<dl>
<dt>
</dt><dd> List of properties to sort by (prefix by &#8216;-&#8216; for reverse sorting).</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>playlist config</code> [-t &lt;type&gt;] [-s &lt;history&gt;] [-u &lt;upcoming&gt;] [-i &lt;coll&gt;] </dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Configure a playlist by changing its type, attributes, etc. By default, configure the active playlist.</dd></dl>
<dl>
<dt>
</dt><dd> -t | &#8211;type</dd></dl>
<dl>
<dt>
</dt><dd> Change the type of the playlist: list, queue, pshuffle.</dd></dl>
<dl>
<dt>
</dt><dd> -s | &#8211;history</dd></dl>
<dl>
<dt>
</dt><dd> Size of the history of played tracks (for queue, pshuffle).</dd></dl>
<dl>
<dt>
</dt><dd> -u | &#8211;upcoming</dd></dl>
<dl>
<dt>
</dt><dd> Number of upcoming tracks to maintain (for pshuffle).</dd></dl>
<dl>
<dt>
</dt><dd> -i | &#8211;input</dd></dl>
<dl>
<dt>
</dt><dd> Input collection for the playlist (for pshuffle). Default to &#8216;All Media&#8217;.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<h2>COLLECTION COMMANDS</h2>
<dl>
<dt><code>collection list</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> List all collections.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>collection</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> No description</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>collection show</code> &lt;collection&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Display a human-readable description of a collection.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>collection create</code> [-f] [-a | -e] [-c &lt;collection&gt;] &lt;name&gt; [pattern]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Create a new collection. If pattern is provided, it is used to define the collection. Otherwise, the new collection contains the whole media library.</dd></dl>
<dl>
<dt>
</dt><dd> -f | &#8211;force</dd></dl>
<dl>
<dt>
</dt><dd> Force creating of the collection, overwrite an existing collection if needed.</dd></dl>
<dl>
<dt>
</dt><dd> -c | &#8211;collection</dd></dl>
<dl>
<dt>
</dt><dd> Copy an existing collection to the new one.</dd></dl>
<dl>
<dt>
</dt><dd> -e | &#8211;empty</dd></dl>
<dl>
<dt>
</dt><dd> Initialize an empty collection.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>collection rename</code> [-f] &lt;oldname&gt; &lt;newname&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Rename a collection.</dd></dl>
<dl>
<dt>
</dt><dd> -f | &#8211;force</dd></dl>
<dl>
<dt>
</dt><dd> Force renaming of the collection, overwrite an existing collection if needed.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>collection remove</code> &lt;collection&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Remove a collection.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>collection config</code> &lt;collection&gt; [attrname [attrvalue]]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Get or set attributes for the given collection. If no attribute name is provided, list all attributes. If only an attribute name is provided, display the value of the attribute. If both attribute name and value are provided, set the new value of the attribute.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<h2>SERVER COMMANDS</h2>
<dl>
<dt><code>server import</code> [-N] &lt;path&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Import new files into the media library. By default, directories are imported recursively.</dd></dl>
<dl>
<dt>
</dt><dd> -N | &#8211;non-recursive</dd></dl>
<dl>
<dt>
</dt><dd> Do not import directories recursively.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>server</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> No description</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>server remove</code> &lt;pattern&gt;</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Remove the matching media from the media library.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>server rehash</code> [pattern]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Rehash the media matched by the pattern, or the whole media library if no pattern is provided</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>server config</code> [name [value]]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Get or set configuration values. If no name or value is provided, list all configuration values. If only a name is provided, display the content of the corresponding configuration value. If both name and a value are provided, set the new content of the configuration value.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>server property</code> [-i | -s | -D] [-S] &lt;mid&gt; [name [value]]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Get or set properties for a given media. If no name or value is provided, list all properties. If only a name is provided, display the value of the property. If both a name and a value are provided, set the new value of the property. </dd>
<p> By default, set operations use client specific source and list, display operations use source-preference. Use the &#8211;source option to override this behaviour. </p>
<p> By default, the value will be used to determine whether it should be saved as a string or an integer. Use the &#8211;int or &#8211;string flag to override this behaviour.</dl>
<dl>
<dt>
</dt><dd> -i | &#8211;int</dd></dl>
<dl>
<dt>
</dt><dd> Force the value to be treated as integer.</dd></dl>
<dl>
<dt>
</dt><dd> -s | &#8211;string</dd></dl>
<dl>
<dt>
</dt><dd> Force the value to be treated as a string.</dd></dl>
<dl>
<dt>
</dt><dd> -D | &#8211;delete</dd></dl>
<dl>
<dt>
</dt><dd> Delete the selected property.</dd></dl>
<dl>
<dt>
</dt><dd> -S | &#8211;source</dd></dl>
<dl>
<dt>
</dt><dd> Property source.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>server plugins</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> List the plugins loaded in the server.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>server volume</code> [-c &lt;name&gt;] [value]</dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Get or set the audio volume (in a range of 0-100). If a value is provided, set the new value of the volume. Otherwise, display the current volume. By default, the command applies to all audio channels. Use the &#8211;channel flag to override this behaviour.</dd></dl>
<dl>
<dt>
</dt><dd> -c | &#8211;channel</dd></dl>
<dl>
<dt>
</dt><dd> Get or set the volume only for one channel.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>server stats</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Display statistics about the server: uptime, version, size of the medialib, etc</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>server sync</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Force the saving of collections to the disk (otherwise only performed on shutdown)</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>server shutdown</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> Shutdown the server.</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<h2>ALIASES</h2>
<p> A list of command aliases are read from the configuration file in the section [alias] at runtime. The syntax of <code>nycli</code> aliases are somewhat similar to bash and other shells. An alias is defined by a list of semi-colon separated commands and arguments. Parameter expansion is supported (see <code>EXPANSION</code> below). </p>
<dl>
<dt>The default configuration includes the following aliases:</dt>
<dd></dd></dl>
<dl>
<dt><code>addpls</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> add -f -P $@</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>current</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> status -f $1</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>server kill</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> server shutdown</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>mute</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> server volume 0</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>repeat</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> seek 0</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>ls</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> list</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>quit</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> exit</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>clear</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> playlist clear</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<dl>
<dt><code>scap</code></dt>
<dd></dd></dl>
<dl>
<dt>
</dt><dd> stop ; playlist clear ; add $@ ; play</dd></dl>
<dl>
<dt>
</dt><dd> -h | &#8211;help</dd></dl>
<dl>
<dt>
</dt><dd> Display command help.</dd></dl>
<h3>EXPANSION</h3>
<dl>
<dt>
</dt><dd> <code>Positional Parameters</code></dd></dl>
<dl>
<dt>
</dt><dd> An alias can use positional parameters, for example: </dd>
<p> foo = add -f $1 $3 </p>
<p> foo ctkoz.ogg and slre.ogg </p>
<p> Will result in: </p>
<p> add -f ctkoz.ogg slre.ogg </p>
</dl>
<dl>
<dt>
</dt><dd> <code>Special Parameters</code></dd></dl>
<dl>
<dt>
</dt><dd> <code>$@</code></dd>
<dl>
<dt>
</dt><dd> This expands to all parameters passed to the alias.</dd></dl>
</dl>
<h2>CONFIGURATION</h2>
<p> PROMPT</p>
<dl>
<dt>
</dt><dd> String to use as a prompt in <code>INTERACTIVE MODE</code></dd></dl>
<p> SERVER_AUTOSTART</p>
<dl>
<dt>
</dt><dd> Boolean, if true nycli will attempt to start <code><a href="/docs/linux/man/1-xmms2d/">xmms2d</a></code>(1) if it&#8217;s not running already.</dd></dl>
<p> AUTO_UNIQUE_COMPLETE</p>
<dl>
<dt>
</dt><dd> Boolean</dd></dl>
<p> PLAYLIST_MARKER</p>
<dl>
<dt>
</dt><dd> String to use to mark the current active entry in the playlist</dd></dl>
<p> GUESS_PLS</p>
<dl>
<dt>
</dt><dd> Boolean, try to guess if the URL is a playlist and add accordingly. (Not reliable)</dd></dl>
<p> CLASSIC_LIST</p>
<dl>
<dt>
</dt><dd> Boolean, format <code>list</code> output similar to the classic cli.</dd></dl>
<p> CLASSIC_LIST_FORMAT</p>
<dl>
<dt>
</dt><dd> String to format classic <code>list</code> output with.</dd></dl>
<p> STATUS_FORMAT</p>
<dl>
<dt>
</dt><dd> String to format <code>status</code> output with.</dd></dl>
<h2>FILES</h2>
<p> $XDG_CONFIG_HOME/xmms2/clients/nycli.conf</p>
<dl>
<dt>
</dt><dd> The configuration file for <code>nycli</code></dd></dl>
<h2>BUGS</h2>
<p> Please report all bugs at <a rel="nofollow" href="http://bugs.xmms2.xmms.se">http://bugs.xmms2.xmms.se</a></p>
<h2>AUTHORS</h2>
<p> Igor Assis, Anders Waldenborg, Anthony Garcia, Sebastien Cevey, and Jonne Lehtinen </p>
<p> See the <code>AUTHORS</code> file in the XMMS2 source distribution for more info. </p>
<p> The blame for this man page is on Anthony. </p>
<p> If you contributed and feel you should be listed here please send me a mail. </p>
<h2>Index</h2>
