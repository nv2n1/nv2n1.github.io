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
<p> <code>brasero</code> [<i>options</i>] [<i>uri</i>] [<i>uri</i>] &#8230; </p>
<p> <code>Brasero</code> is an easy-to-use application for burning CD-R/Ws and DVD-R/Ws. With Brasero you can create data, audio, or video CDs, DVDs, and SVCDs. You can copy existing disks, use image files, or create new projects. Brasero includes tools such as a media previewer, integrity checker and a cover creator.</p>
<h2>OPTIONS</h2>
<p> The following options are supported:</p>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all help options </dd>
</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-p</code>, <code>&#8211;project</code>=<i>PROJECT</i></dt>
<dd> Open the specified project</dd>
<dt><code>-l</code>, <code>&#8211;playlist</code>=<i>PLAYLIST</i></dt>
<dd> Open the specified playlist as an audio project</dd>
<dt><code>&#8211;device</code>=<i>DEVICE</i> PATH</dt>
<dd> Set the drive to be used for burning</dd>
<dt><code>&#8211;image-file</code></dt>
<dd> Create an image file instead of burning</dd>
<dt><code>-a</code>, <code>&#8211;audio</code></dt>
<dd> Open an audio project adding the URIs given on the command line</dd>
<dt><code>-d</code>, <code>&#8211;data</code></dt>
<dd> Open a data project adding the URIs given on the command line</dd>
<dt><code>-c</code>, <code>&#8211;copy</code>=<i>PATH</i> TO DEVICE</dt>
<dd> Copy a disc</dd>
<dt><code>-j</code>, <code>&#8211;cover</code>=<i>PATH</i> TO COVER</dt>
<dd> Cover to use</dd>
<dt><code>-o</code>, <code>&#8211;video</code></dt>
<dd> Open a video project adding the URIs given on the command line</dd>
<dt><code>-i</code>, <code>&#8211;image</code>=<i>PATH</i> TO IMAGE</dt>
<dd> URI of an image file to burn (autodetected)</dd>
<dt><code>-e</code>, <code>&#8211;empty</code></dt>
<dd> Force Brasero to display the project selection page</dd>
<dt><code>-b</code>, <code>&#8211;blank</code>=<i>PATH</i> TO DEVICE</dt>
<dd> Open the blank disc dialog</dd>
<dt><code>-k</code>, <code>&#8211;check</code>=<i>PATH</i> TO DEVICE</dt>
<dd> Open the check disc dialog</dd>
<dt><code>-n</code>, <code>&#8211;ncb</code></dt>
<dd> Burn the contents of the burn:// URI</dd>
<dt><code>&#8211;immediately</code></dt>
<dd> Start burning immediately</dd>
<dt><code>&#8211;no-existing-session</code></dt>
<dd> Don&#8217;t connect to an already-running instance</dd>
<dt><code>-r</code>, <code>&#8211;burn-and-remove-project</code>=<i>PATH</i></dt>
<dd> Burn the specified project and remove it (mainly useful for integration with other applications)</dd>
<dt><code>-x</code>, <code>&#8211;transient-for</code></dt>
<dd> The XID of the parent window</dd>
<dt><code>&#8211;display</code>=<i>DISPLAY</i></dt>
<dd> X display to use</dd></dl>
<h3>Debugging Options:</h3>
<dl>
<dt><code>&#8211;brasero-media-debug</code></dt>
<dd> Display debug messages for Brasero media library</dd>
<dt><code>-g</code>, <code>&#8211;brasero-burn-debug</code></dt>
<dd> Display debug messages for Brasero burn library</dd></dl>
<h2>BUGS</h2>
<p> Please report any <code>brasero</code> bugs you find to <a rel="nofollow" href="https://bugzilla.gnome.org.">https://bugzilla.gnome.org.</a></p>
<h2>AUTHOR</h2>
<p> Brasero&#8217;s manual page was written by Jeremy Bicha &lt;jeremy [at] bicha.net&gt;. </p>
