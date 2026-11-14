---
title: "alsa-info-sh(1)"
name: "alsa-info-sh"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alsa-info-sh/"
description: "alsa-info.sh – command-line utility to gather information about the ALSA subsystem"
---

<p>alsa-info.sh &#8211; command-line utility to gather information about the ALSA subsystem </p>
<h2>Synopsis</h2>
<p><code>alsa-info.sh</code> [<i>options</i>] </p>
<h2>Description</h2>
<p><code>alsa-info.sh</code> is a command-line utility gathering information about the ALSA subsystem. It is used mostly for debugging purposes. </p>
<h2>Options</h2>
<dl>
<dt><i>&#8211;upload</i></p>
<dd>Upload contents to the server (<a rel="nofollow" href="http://www.alsa-project.org">www.alsa-project.org</a> or pastebin.ca).</p>
<dt><i>&#8211;no-upload</i></p>
<dd>Do not upload contents to the remote server.</p>
<dt><i>&#8211;stdout</i></p>
<dd>Print information to standard output.</p>
<dt><i>&#8211;output FILE</i></p>
<dd>Specify file for output in no-upload mode.</p>
<dt><i>&#8211;debug</i></p>
<dd>Run utility as normal, but will not delete file (usually /tmp/alsa-info.txt).</p>
<dt><i>&#8211;with-aplay</i></p>
<dd>Includes output from <i>aplay -l</i>.</p>
<dt><i>&#8211;with-amixer</i></p>
<dd>Includes output from <i>amixer</i>.</p>
<dt><i>&#8211;with-alsactl</i></p>
<dd>Includes output from <i>alsactl</i>.</p>
<dt><i>&#8211;with-configs</i></p>
<dd>Includes output from ~/.asoundrc and /etc/asound.conf if they exist.</p>
<dt><i>&#8211;update</i></p>
<dd>Check server for updates.</p>
<dt><i>&#8211;about</i></p>
<dd>Print information about authors. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt><code>alsa-info.sh &#8211;no-upload</code></p>
<dd>Will gather all information and show the output file. </p>
</dl>
<h2>See Also</h2>
<p><code> <a href="/docs/linux/man/1-aplay/">aplay</a>(1) <a href="/docs/linux/man/1-amixer/">amixer</a>(1) <a href="/docs/linux/man/1-alsactl/">alsactl</a>(1) </code> </p>
<h2>Author</h2>
<p><code>alsa-info.sh</code> was created by the ALSA team, see <i>&#8211;about</i> .</p>
