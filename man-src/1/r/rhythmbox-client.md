---
title: "rhythmbox-client(1)"
name: "rhythmbox-client"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rhythmbox-client/"
description: "rhythmbox-client – controls a running instance of rhythmbox"
---

<h2>SYNOPSIS</h2>
<p> <code>rhythmbox-client</code> [<i>option&#8230;</i>]<i>[</i>file&#8230;<i>]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>rhythmbox-client</code> is a tool for controlling an already running instance of <code>rhythmbox. </code> It&#8217;s useful for remote control scripting, adding specific files to the library from the shell, or printing details of what&#8217;s playing. It also has an interactive mode, useful for controlling playback remotely via ssh. Any files specified after the option arguments will be added to the library. If the <code>&#8211;enqueue</code> option is given, the files will also be added to the play queue.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?,&#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;debug</code></dt>
<dd> Enable debug output</dd>
<dt><code>&#8211;no-start</code></dt>
<dd> Do not start a new instance of rhythmbox</dd>
<dt><code>&#8211;quit</code></dt>
<dd> Quit rhythmbox</dd>
<dt><code>-i,&#8211;interactive</code></dt>
<dd> Start interactive mode <code>&#8211;no-present</code> Don&#8217;t present an existing rhythmbox window</dd>
<dt><code>&#8211;next</code></dt>
<dd> Jump to next song</dd>
<dt><code>&#8211;previous</code></dt>
<dd> Jump to previous song</dd>
<dt><code>&#8211;play</code></dt>
<dd> Resume playback if currently paused</dd>
<dt><code>&#8211;pause</code></dt>
<dd> Pause playback if currently playing</dd>
<dt><code>&#8211;play-pause</code></dt>
<dd> Toggle play/pause mode</dd>
<dt><code>&#8211;stop</code></dt>
<dd> Stop playback if currently playing</dd>
<dt><code>&#8211;play-uri=URI</code></dt>
<dd> Play a specified URI, importing it if necessary</dd>
<dt><code>&#8211;enqueue</code></dt>
<dd> Add specified tracks already in the library to the play queue</dd>
<dt><code>&#8211;clear-queue</code></dt>
<dd> Empty the play queue before adding new tracks</dd>
<dt><code>&#8211;print-playing</code></dt>
<dd> Print the title and artist of the playing song</dd>
<dt><code>&#8211;print-playing-format=format</code></dt>
<dd> Print formatted details of the song (see <font SIZE="-1"><code>FORMAT OPTIONS</code> </font> below).</dd>
<dt><code>&#8211;set-volume</code></dt>
<dd> Set the playback volume</dd>
<dt><code>&#8211;volume-up</code></dt>
<dd> Increase the playback volume</dd>
<dt><code>&#8211;volume-down</code></dt>
<dd> Decrease the playback volume</dd>
<dt><code>&#8211;print-volume</code></dt>
<dd> Print the current playback volume</dd>
<dt><code>&#8211;select-source=URI</code></dt>
<dd> Select the source corresponding to a URI (device or mount point)</dd>
<dt><code>&#8211;activate-source=URI</code></dt>
<dd> Select the source corresponding to a URI (device or mount point) and start playing from it if not already playing.</dd>
<dt><code>&#8211;play-source=URI</code></dt>
<dd> Select the source corresponding to a URI (device or mount point) and start playing from it.</dd></dl>
<h2>FORMAT OPTIONS</h2>
<dl>
<dt>%at</dt>
<dd> album title</dd>
<dt>%aa</dt>
<dd> album artist</dd>
<dt>%aA</dt>
<dd> album artist (lowercase)</dd>
<dt>%as</dt>
<dd> album artist sortname</dd>
<dt>%aS</dt>
<dd> album artist sortname (lowercase)</dd>
<dt>%ay</dt>
<dd> album year</dd>
<dt>%ag</dt>
<dd> album genre</dd>
<dt>%aG</dt>
<dd> album genre (lowercase)</dd>
<dt>%an</dt>
<dd> album disc number</dd>
<dt>%aN</dt>
<dd> album disc number, zero padded</dd>
<dt>%st</dt>
<dd> stream title</dd>
<dt>%tn</dt>
<dd> track number (i.e 8)</dd>
<dt>%tN</dt>
<dd> track number, zero padded (i.e 08)</dd>
<dt>%tt</dt>
<dd> track title</dd>
<dt>%ta</dt>
<dd> track artist</dd>
<dt>%tA</dt>
<dd> track artist (lowercase)</dd>
<dt>%ts</dt>
<dd> track artist sortname</dd>
<dt>%tS</dt>
<dd> track artist sortname (lowercase)</dd>
<dt>%td</dt>
<dd> track duration</dd>
<dt>%te</dt>
<dd> track elapsed time</dd>
<dt>Variables can be combined using quotes. For example &quot;%tn %aa %tt&quot;, will print the track number followed by the artist and the title of the track.</dt>
<dd></dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Sven Arvidsson &lt;sa [at] whiz.se&gt;, for the Debian system (but may be used by others).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rhythmbox/">rhythmbox</a></code>(1). </p>
