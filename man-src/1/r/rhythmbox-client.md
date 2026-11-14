---
title: "rhythmbox-client(1)"
name: "rhythmbox-client"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rhythmbox-client/"
description: "rhythmbox-client – controls a running instance of rhythmbox"
---

<h2 class="name">NAME</h2>
<p> rhythmbox-client &#8211; controls a running instance of rhythmbox </p>
<h2>SYNOPSIS</h2>
<p> <code>rhythmbox-client</code> [<i>option&#8230;</i>]<i>[</i>file&#8230;<i>]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>rhythmbox-client</code> is a tool for controlling an already running instance of <code>rhythmbox. </code> It&#8217;s useful for remote control scripting, adding specific files to the library from the shell, or printing details of what&#8217;s playing. It also has an interactive mode, useful for controlling playback remotely via ssh. Any files specified after the option arguments will be added to the library. If the <code>&#8211;enqueue</code> option is given, the files will also be added to the play queue.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?,&#8211;help</code></p>
<dd> Show help options</p>
<dt><code>&#8211;debug</code></p>
<dd> Enable debug output</p>
<dt><code>&#8211;no-start</code></p>
<dd> Do not start a new instance of rhythmbox</p>
<dt><code>&#8211;quit</code></p>
<dd> Quit rhythmbox</p>
<dt><code>-i,&#8211;interactive</code></p>
<dd> Start interactive mode <code>&#8211;no-present</code> Don&#8217;t present an existing rhythmbox window</p>
<dt><code>&#8211;next</code></p>
<dd> Jump to next song</p>
<dt><code>&#8211;previous</code></p>
<dd> Jump to previous song</p>
<dt><code>&#8211;play</code></p>
<dd> Resume playback if currently paused</p>
<dt><code>&#8211;pause</code></p>
<dd> Pause playback if currently playing</p>
<dt><code>&#8211;play-pause</code></p>
<dd> Toggle play/pause mode</p>
<dt><code>&#8211;stop</code></p>
<dd> Stop playback if currently playing</p>
<dt><code>&#8211;play-uri=URI</code></p>
<dd> Play a specified URI, importing it if necessary</p>
<dt><code>&#8211;enqueue</code></p>
<dd> Add specified tracks already in the library to the play queue</p>
<dt><code>&#8211;clear-queue</code></p>
<dd> Empty the play queue before adding new tracks</p>
<dt><code>&#8211;print-playing</code></p>
<dd> Print the title and artist of the playing song</p>
<dt><code>&#8211;print-playing-format=format</code></p>
<dd> Print formatted details of the song (see <font SIZE="-1"><code>FORMAT OPTIONS</code> </font> below).</p>
<dt><code>&#8211;set-volume</code></p>
<dd> Set the playback volume</p>
<dt><code>&#8211;volume-up</code></p>
<dd> Increase the playback volume</p>
<dt><code>&#8211;volume-down</code></p>
<dd> Decrease the playback volume</p>
<dt><code>&#8211;print-volume</code></p>
<dd> Print the current playback volume</p>
<dt><code>&#8211;select-source=URI</code></p>
<dd> Select the source corresponding to a URI (device or mount point)</p>
<dt><code>&#8211;activate-source=URI</code></p>
<dd> Select the source corresponding to a URI (device or mount point) and start playing from it if not already playing.</p>
<dt><code>&#8211;play-source=URI</code></p>
<dd> Select the source corresponding to a URI (device or mount point) and start playing from it.</dl>
<h2>FORMAT OPTIONS</h2>
<dl>
<dt>%at</p>
<dd> album title</p>
<dt>%aa</p>
<dd> album artist</p>
<dt>%aA</p>
<dd> album artist (lowercase)</p>
<dt>%as</p>
<dd> album artist sortname</p>
<dt>%aS</p>
<dd> album artist sortname (lowercase)</p>
<dt>%ay</p>
<dd> album year</p>
<dt>%ag</p>
<dd> album genre</p>
<dt>%aG</p>
<dd> album genre (lowercase)</p>
<dt>%an</p>
<dd> album disc number</p>
<dt>%aN</p>
<dd> album disc number, zero padded</p>
<dt>%st</p>
<dd> stream title</p>
<dt>%tn</p>
<dd> track number (i.e 8)</p>
<dt>%tN</p>
<dd> track number, zero padded (i.e 08)</p>
<dt>%tt</p>
<dd> track title</p>
<dt>%ta</p>
<dd> track artist</p>
<dt>%tA</p>
<dd> track artist (lowercase)</p>
<dt>%ts</p>
<dd> track artist sortname</p>
<dt>%tS</p>
<dd> track artist sortname (lowercase)</p>
<dt>%td</p>
<dd> track duration</p>
<dt>%te</p>
<dd> track elapsed time</p>
<dt>Variables can be combined using quotes. For example &quot;%tn %aa %tt&quot;, will print the track number followed by the artist and the title of the track.</p>
<dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Sven Arvidsson &lt;sa [at] whiz.se&gt;, for the Debian system (but may be used by others).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rhythmbox/">rhythmbox</a></code>(1). </p>
<h2>Index</h2>
