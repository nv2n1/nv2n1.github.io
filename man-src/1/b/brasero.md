---
title: "brasero(1)"
name: "brasero"
section: "1"
letter: "b"
url: "/docs/linux/man/1-brasero/"
description: "brasero – Simple and easy to use CD/DVD burning application for the GNOME Desktop"
---

<h2>NAME</h2>
<p> brasero &#8211; Simple and easy to use CD/DVD burning application for the GNOME Desktop</p>
<h2>SYNOPSIS</h2>
<p> <code>brasero</code> [<i>options</i>] [<i>uri</i>] [<i>uri</i>] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>Brasero</code> is an easy-to-use application for burning CD-R/Ws and DVD-R/Ws. With Brasero you can create data, audio, or video CDs, DVDs, and SVCDs. You can copy existing disks, use image files, or create new projects. Brasero includes tools such as a media previewer, integrity checker and a cover creator.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all help options </p>
</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-p</code>, <code>&#8211;project</code>=<i>PROJECT</i></p>
<dd> Open the specified project</p>
<dt><code>-l</code>, <code>&#8211;playlist</code>=<i>PLAYLIST</i></p>
<dd> Open the specified playlist as an audio project</p>
<dt><code>&#8211;device</code>=<i>DEVICE</i> PATH</p>
<dd> Set the drive to be used for burning</p>
<dt><code>&#8211;image-file</code></p>
<dd> Create an image file instead of burning</p>
<dt><code>-a</code>, <code>&#8211;audio</code></p>
<dd> Open an audio project adding the URIs given on the command line</p>
<dt><code>-d</code>, <code>&#8211;data</code></p>
<dd> Open a data project adding the URIs given on the command line</p>
<dt><code>-c</code>, <code>&#8211;copy</code>=<i>PATH</i> TO DEVICE</p>
<dd> Copy a disc</p>
<dt><code>-j</code>, <code>&#8211;cover</code>=<i>PATH</i> TO COVER</p>
<dd> Cover to use</p>
<dt><code>-o</code>, <code>&#8211;video</code></p>
<dd> Open a video project adding the URIs given on the command line</p>
<dt><code>-i</code>, <code>&#8211;image</code>=<i>PATH</i> TO IMAGE</p>
<dd> URI of an image file to burn (autodetected)</p>
<dt><code>-e</code>, <code>&#8211;empty</code></p>
<dd> Force Brasero to display the project selection page</p>
<dt><code>-b</code>, <code>&#8211;blank</code>=<i>PATH</i> TO DEVICE</p>
<dd> Open the blank disc dialog</p>
<dt><code>-k</code>, <code>&#8211;check</code>=<i>PATH</i> TO DEVICE</p>
<dd> Open the check disc dialog</p>
<dt><code>-n</code>, <code>&#8211;ncb</code></p>
<dd> Burn the contents of the burn:// URI</p>
<dt><code>&#8211;immediately</code></p>
<dd> Start burning immediately</p>
<dt><code>&#8211;no-existing-session</code></p>
<dd> Don&#8217;t connect to an already-running instance</p>
<dt><code>-r</code>, <code>&#8211;burn-and-remove-project</code>=<i>PATH</i></p>
<dd> Burn the specified project and remove it (mainly useful for integration with other applications)</p>
<dt><code>-x</code>, <code>&#8211;transient-for</code></p>
<dd> The XID of the parent window</p>
<dt><code>&#8211;display</code>=<i>DISPLAY</i></p>
<dd> X display to use</dl>
<h3>Debugging Options:</h3>
<dl>
<dt><code>&#8211;brasero-media-debug</code></p>
<dd> Display debug messages for Brasero media library</p>
<dt><code>-g</code>, <code>&#8211;brasero-burn-debug</code></p>
<dd> Display debug messages for Brasero burn library</dl>
<h2>BUGS</h2>
<p> Please report any <code>brasero</code> bugs you find to <a rel="nofollow" href="https://bugzilla.gnome.org.">https://bugzilla.gnome.org.</a></p>
<h2>AUTHOR</h2>
<p> Brasero&#8217;s manual page was written by Jeremy Bicha &lt;jeremy [at] bicha.net&gt;. </p>
<h2>Index</h2>
