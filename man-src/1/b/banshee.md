---
title: "banshee(1)"
name: "banshee"
section: "1"
letter: "b"
url: "/docs/linux/man/1-banshee/"
description: "Banshee – Media Management and Playback application Muinshee – Media Management and Playback application"
---

<h2 class="name">NAME</h2>
<p> Banshee &#8211; Media Management and Playback application<br />
 Muinshee &#8211; Media Management and Playback application </p>
<h2>SYNOPSIS</h2>
<p> <code>banshee</code> [<i>options</i>&#8230;] [<i>files|URIs</i>&#8230;]<br />
 <code>muinshee</code> [<i>options</i>&#8230;] [<i>files|URIs</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Banshee is an media management and playback application for the GNOME desktop, allowing users to import audio from CDs, search their library, create playlists of selections of their library, sync music to/from iPods and other media devices, play and manage video files and burn selections to a CD.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;next</code></p>
<dd> Play the next track, optionally restarting if the &#8216;restart&#8217; value is set</p>
<dt><code>&#8211;previous</code></p>
<dd> Play the previous track, optionally restarting if the &#8216;restart value is set</p>
<dt><code>&#8211;restart-or-previous</code></p>
<dd> If the current song has been played longer than 4 seconds then restart it, otherwise the same as <code>&#8211;previous</code></p>
<dt><code>&#8211;play-enqueued</code></p>
<dd> Automatically start playing any tracks enqueued on the command line</p>
<dt><code>&#8211;play</code></p>
<dd> Start playback</p>
<dt><code>&#8211;pause</code></p>
<dd> Pause playback</p>
<dt><code>&#8211;toggle-playing</code></p>
<dd> Toggle playback</p>
<dt><code>&#8211;stop</code></p>
<dd> Completely stop playback</p>
<dt><code>&#8211;stop-when-finished</code></p>
<dd> Enable or disable playback stopping after the currently playing track (value should be either &#8216;true&#8217; or &#8216;false&#8217;)</p>
<dt><code>&#8211;set-volume</code>=<i>LEVEL</i></p>
<dd> Set the playback volume (0-100), prefix with +/- for relative values</p>
<dt><code>&#8211;set-position</code>=<i>POS</i></p>
<dd> Seek to a specific point (seconds, float)</p>
<dt><code>&#8211;set-rating</code>=<i>RATING</i></p>
<dd> Set the currently played track&#8217;s rating (0 to 5)</p>
<dt><code>&#8211;query-current-state</code></p>
<dd> Current player state</p>
<dt><code>&#8211;query-last-state</code></p>
<dd> Last player state</p>
<dt><code>&#8211;query-can-pause</code></p>
<dd> Query whether the player can be paused</p>
<dt><code>&#8211;query-can-seek</code></p>
<dd> Query whether the player can seek</p>
<dt><code>&#8211;query-volume</code></p>
<dd> Player volume</p>
<dt><code>&#8211;query-position</code></p>
<dd> Player position in currently playing track</p>
<dt><code>&#8211;query-uri</code></p>
<dd> URI</p>
<dt><code>&#8211;query-artist</code></p>
<dd> Artist Name</p>
<dt><code>&#8211;query-album</code></p>
<dd> Album Title</p>
<dt><code>&#8211;query-title</code></p>
<dd> Track Title</p>
<dt><code>&#8211;query-duration</code></p>
<dd> Duration</p>
<dt><code>&#8211;query-track-number</code></p>
<dd> Track Number</p>
<dt><code>&#8211;query-track-count</code></p>
<dd> Track Count</p>
<dt><code>&#8211;query-disc</code></p>
<dd> Disc Number</p>
<dt><code>&#8211;query-year</code></p>
<dd> Year</p>
<dt><code>&#8211;query-rating</code></p>
<dd> Rating</p>
<dt><code>&#8211;query-score</code></p>
<dd> Score</p>
<dt><code>&#8211;query-bit-rate</code></p>
<dd> Bit Rate</p>
<dt><code>&#8211;show</code>|&#8211;present</p>
<dd> Present the user interface on the active workspace</p>
<dt><code>&#8211;fullscreen</code></p>
<dd> Enter the full-screen mode</p>
<dt><code>&#8211;hide</code></p>
<dd> Hide the user interface</p>
<dt><code>&#8211;no-present</code></p>
<dd> Do not present the user interface, regardless of any other options</p>
<dt><code>&#8211;show-import-media</code></p>
<dd> Present the import media dialog box</p>
<dt><code>&#8211;show-about</code></p>
<dd> Present the about dialog</p>
<dt><code>&#8211;show-open-location</code></p>
<dd> Present the open location dialog</p>
<dt><code>&#8211;show-preferences</code></p>
<dd> Present the preferences dialog</p>
<dt><code>&#8211;debug</code></p>
<dd> Enable general debugging features</p>
<dt><code>&#8211;debug-sql</code></p>
<dd> Enable debugging output of SQL queries</p>
<dt><code>&#8211;debug-addins</code></p>
<dd> Enable debugging output of Mono.Addins</p>
<dt><code>&#8211;db</code>=<i>FILE</i></p>
<dd> Specify an alternate database to use</p>
<dt><code>&#8211;gconf-base-key</code>=<i>KEY</i></p>
<dd> Specify an alternate key, default is /apps/banshee-1/</p>
<dt><code>&#8211;uninstalled</code></p>
<dd> Optimize instance for running uninstalled; most notably, this will create an alternate Mono.Addins database in the working directory</p>
<dt><code>&#8211;disable-dbus</code></p>
<dd> Disable DBus support completely</p>
<dt><code>&#8211;no-gtkrc</code></p>
<dd> Skip loading a custom gtkrc file (~/.config/banshee-1/gtkrc) if it exists</p>
<dt><code>&#8211;help</code></p>
<dd> Show this help</p>
<dt><code>&#8211;help-playback</code></p>
<dd> Show options for controlling playback</p>
<dt><code>&#8211;help-query-track</code></p>
<dd> Show options for querying the playing track</p>
<dt><code>&#8211;help-query-player</code></p>
<dd> Show options for querying the playing engine</p>
<dt><code>&#8211;help-ui</code></p>
<dd> Show options for the user interface</p>
<dt><code>&#8211;help-debug</code></p>
<dd> Show options for developers and debugging</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all option groups</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information</dl>
<p> Copyright 2005-2009 Novell, Inc. and Contributors. </p>
<h2>Index</h2>
