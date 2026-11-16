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
<dt><code>&#8211;next</code></dt>
<dd> Play the next track, optionally restarting if the &#8216;restart&#8217; value is set</dd>
<dt><code>&#8211;previous</code></dt>
<dd> Play the previous track, optionally restarting if the &#8216;restart value is set</dd>
<dt><code>&#8211;restart-or-previous</code></dt>
<dd> If the current song has been played longer than 4 seconds then restart it, otherwise the same as <code>&#8211;previous</code></dd>
<dt><code>&#8211;play-enqueued</code></dt>
<dd> Automatically start playing any tracks enqueued on the command line</dd>
<dt><code>&#8211;play</code></dt>
<dd> Start playback</dd>
<dt><code>&#8211;pause</code></dt>
<dd> Pause playback</dd>
<dt><code>&#8211;toggle-playing</code></dt>
<dd> Toggle playback</dd>
<dt><code>&#8211;stop</code></dt>
<dd> Completely stop playback</dd>
<dt><code>&#8211;stop-when-finished</code></dt>
<dd> Enable or disable playback stopping after the currently playing track (value should be either &#8216;true&#8217; or &#8216;false&#8217;)</dd>
<dt><code>&#8211;set-volume</code>=<i>LEVEL</i></dt>
<dd> Set the playback volume (0-100), prefix with +/- for relative values</dd>
<dt><code>&#8211;set-position</code>=<i>POS</i></dt>
<dd> Seek to a specific point (seconds, float)</dd>
<dt><code>&#8211;set-rating</code>=<i>RATING</i></dt>
<dd> Set the currently played track&#8217;s rating (0 to 5)</dd>
<dt><code>&#8211;query-current-state</code></dt>
<dd> Current player state</dd>
<dt><code>&#8211;query-last-state</code></dt>
<dd> Last player state</dd>
<dt><code>&#8211;query-can-pause</code></dt>
<dd> Query whether the player can be paused</dd>
<dt><code>&#8211;query-can-seek</code></dt>
<dd> Query whether the player can seek</dd>
<dt><code>&#8211;query-volume</code></dt>
<dd> Player volume</dd>
<dt><code>&#8211;query-position</code></dt>
<dd> Player position in currently playing track</dd>
<dt><code>&#8211;query-uri</code></dt>
<dd> URI</dd>
<dt><code>&#8211;query-artist</code></dt>
<dd> Artist Name</dd>
<dt><code>&#8211;query-album</code></dt>
<dd> Album Title</dd>
<dt><code>&#8211;query-title</code></dt>
<dd> Track Title</dd>
<dt><code>&#8211;query-duration</code></dt>
<dd> Duration</dd>
<dt><code>&#8211;query-track-number</code></dt>
<dd> Track Number</dd>
<dt><code>&#8211;query-track-count</code></dt>
<dd> Track Count</dd>
<dt><code>&#8211;query-disc</code></dt>
<dd> Disc Number</dd>
<dt><code>&#8211;query-year</code></dt>
<dd> Year</dd>
<dt><code>&#8211;query-rating</code></dt>
<dd> Rating</dd>
<dt><code>&#8211;query-score</code></dt>
<dd> Score</dd>
<dt><code>&#8211;query-bit-rate</code></dt>
<dd> Bit Rate</dd>
<dt><code>&#8211;show</code>|&#8211;present</dt>
<dd> Present the user interface on the active workspace</dd>
<dt><code>&#8211;fullscreen</code></dt>
<dd> Enter the full-screen mode</dd>
<dt><code>&#8211;hide</code></dt>
<dd> Hide the user interface</dd>
<dt><code>&#8211;no-present</code></dt>
<dd> Do not present the user interface, regardless of any other options</dd>
<dt><code>&#8211;show-import-media</code></dt>
<dd> Present the import media dialog box</dd>
<dt><code>&#8211;show-about</code></dt>
<dd> Present the about dialog</dd>
<dt><code>&#8211;show-open-location</code></dt>
<dd> Present the open location dialog</dd>
<dt><code>&#8211;show-preferences</code></dt>
<dd> Present the preferences dialog</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Enable general debugging features</dd>
<dt><code>&#8211;debug-sql</code></dt>
<dd> Enable debugging output of SQL queries</dd>
<dt><code>&#8211;debug-addins</code></dt>
<dd> Enable debugging output of Mono.Addins</dd>
<dt><code>&#8211;db</code>=<i>FILE</i></dt>
<dd> Specify an alternate database to use</dd>
<dt><code>&#8211;gconf-base-key</code>=<i>KEY</i></dt>
<dd> Specify an alternate key, default is /apps/banshee-1/</dd>
<dt><code>&#8211;uninstalled</code></dt>
<dd> Optimize instance for running uninstalled; most notably, this will create an alternate Mono.Addins database in the working directory</dd>
<dt><code>&#8211;disable-dbus</code></dt>
<dd> Disable DBus support completely</dd>
<dt><code>&#8211;no-gtkrc</code></dt>
<dd> Skip loading a custom gtkrc file (~/.config/banshee-1/gtkrc) if it exists</dd>
<dt><code>&#8211;help</code></dt>
<dd> Show this help</dd>
<dt><code>&#8211;help-playback</code></dt>
<dd> Show options for controlling playback</dd>
<dt><code>&#8211;help-query-track</code></dt>
<dd> Show options for querying the playing track</dd>
<dt><code>&#8211;help-query-player</code></dt>
<dd> Show options for querying the playing engine</dd>
<dt><code>&#8211;help-ui</code></dt>
<dd> Show options for the user interface</dd>
<dt><code>&#8211;help-debug</code></dt>
<dd> Show options for developers and debugging</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all option groups</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version information</dd></dl>
<p> Copyright 2005-2009 Novell, Inc. and Contributors. </p>
<h2>Index</h2>
