---
title: "dvcont(1)"
name: "dvcont"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dvcont/"
description: "dvcont – send control commands to DV cameras"
---

<h2>NAME</h2>
<p> dvcont &#8211; send control commands to DV cameras</p>
<h2>SYNOPSIS</h2>
<p> <code>dvcont</code> <i>&lt;command1&gt; </i><code>[ </code><i>&lt;command2&gt; </i>&#8230; <code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>dvcont</code> is a command line tool to send control commands via an IEEE1394 link to a device that implements the AV/C specifications by the 1394 Trade Association. Or for the non-techies: <code>dvcont</code> lets you remote control your DV camera via a Firewire cable. The following <i>command</i>s are understood:</p>
<dl>
<dt><code>dev </code><i>&lt;number&gt;</i></p>
<dd> Select device <i>number</i> on chain to use. (dvcont tries to automatically detect the camera. Use the <code>dev</code> command BEFORE any other commands for manual control.)</p>
<dt><code>play</code></p>
<dd> Tell the camera to play. If already playing, it toggles slow-motion.</p>
<dt><code>reverse</code></p>
<dd> Tell the camera to play in reverse. If already playing, it toggles slow-motion.</p>
<dt><code>trickplay &lt; -14 to +14 &gt;</code></p>
<dd> Tell the camera to play at various speeds. 0 = forward play, -14 = fastest reverse, -8 = 1X reverse, -1 = slowest reverse, 1 = slowest forward, 8 = 1X forward, 14 = fastest forward. (Not supported by all cameras.)</p>
<dt><code>stop</code></p>
<dd> Tell the camera to stop playing.</p>
<dt><code>rewind</code></p>
<dd> Tell the camera to rewind. (Use in stop or play mode.)</p>
<dt><code>ff</code></p>
<dd> Tell the camera to fast forward. (Use in stop or play mode.)</p>
<dt><code>pause</code></p>
<dd> Tell the camera to toggle pause play.</p>
<dt><code>next</code></p>
<dd> Tell the camera to go to the next frame. (Use in pause mode.)</p>
<dt><code>nextindex</code></p>
<dd> Tell the camera to search for the next scene. (Use in pause or play mode.)</p>
<dt><code>prev</code></p>
<dd> Tell the camera to go to the previous frame. (Use in pause mode)</p>
<dt><code>previndex</code></p>
<dd> Tell the camera to search for the previous scene. (Use in pause or play mode)</p>
<dt><code>record</code></p>
<dd> Tell the camera to record. (Use with caution!)</p>
<dt><code>eject</code></p>
<dd> Tell the camera to eject the tape. (Not supported by all cameras.)</p>
<dt><code>timecode</code></p>
<dd> Report the timecode on tape in the format HH:MM:SS:FF (hours, minutes, seconds, intra-second frames).</p>
<dt><code>seek </code><i>&lt;timecode&gt;</i></p>
<dd> Tell the camera to go to the <i>timecode</i>, given in format HH:MM:SS:FF as above.</p>
<dt><code>status</code></p>
<dd> Report the status of the device.</p>
<dt><code>pluginfo</code></p>
<dd> Report available plugs.</p>
<dt><code>verbose</code></p>
<dd> Tell the program to tell you debug info.</p>
<dt><code>version</code></p>
<dd> Tell the program to tell you the program version.</p>
<dt><code>help</code></p>
<dd> Tell the program to show you a help screen.</dl>
<h2>AUTHORS</h2>
<p> <code>dvcont</code> was written by Jason Howard &lt;jason [at] spectsoft.com&gt; and Dan Dennedy &lt;dan [at] dennedy.org&gt;. This man page was written with the help of <code>help2man</code> by Daniel Kobras &lt;kobras [at] debian.org&gt; for the Debian GNU/Linux distribution (but may be used by others). Updated by Dan Dennedy &lt;dan [at] dennedy.org&gt;. </p>
<h2>Index</h2>
