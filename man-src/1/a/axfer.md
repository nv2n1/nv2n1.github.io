---
title: "axfer(1)"
name: "axfer"
section: "1"
letter: "a"
url: "/docs/linux/man/1-axfer/"
description: "axfer – command-line sound recorder and player for sound devices and nodes supported by Linux sound subsystem (Advanced Linux Sound Architecture, also known as ALSA)."
---

<h2 class="name">NAME</h2>
<p> axfer &#8211; command-line sound recorder and player for sound devices and nodes supported by Linux sound subsystem (Advanced Linux Sound Architecture, also known as ALSA).</p>
<h2>SYNOPSYS</h2>
<p> <code>axfer</code> <i>subcommand direction options</i> </p>
<p> subcommand = <code>transfer</code> | <code>list</code> | <code>version</code> | <code>help</code> </p>
<p> direction = <code>capture</code> | <code>playback</code> </p>
<p> options = ( depends on <i>subcommand</i> ) </p>
<h2>DESCRIPTION</h2>
<p> The <code>axfer</code> is a command-line recorder and player to transfer audio data frame between sound devices/nodes and files/stdin/stdout. </p>
<h2>OPTIONS</h2>
<h3>Subcommand</h3>
<dl>
<dt><code>transfer</code></p>
<dd> Performs transmission of audio data frame. Its detail is described in <code><a href="/docs/linux/man/1-axfer-transfer/">axfer-transfer</a>(1)</code> manual. </p>
<dt><code>list</code></p>
<dd> Dumps lists of available sound devices and nodes. Its detail is described in <code><a href="/docs/linux/man/1-axfer-list/">axfer-list</a>(1)</code> manual. </p>
<dt><code>version</code></p>
<dd> Prints version of this application (as the same version as alsa-utils package). </p>
<dt><code>help</code></p>
<dd> Prints a short message about subcommands for users to enter this application. </p>
</dl>
<h3>Direction</h3>
<dl>
<dt><code>capture</code></p>
<dd> Operates for capture transmission. </p>
<dt><code>playback</code></p>
<dd> Operates for playback transmission. </p>
</dl>
<h2>EXIT STATUS</h2>
<p> <i>EXIT_SUCCESS</i> (0) if run time successfully finished, else <i>EXIT_FAILURE</i> (1). </p>
<h2>UNIT TEST</h2>
<p> This program has unit tests for internal implementation. Please refer to the manual of <i>axfer-transfer</i> for details. </p>
<h2>COMPATIBILITY TO APLAY</h2>
<p> The <i>axfer</i> is designed to be compatible to <a href="/docs/linux/man/1-aplay/">aplay</a>(1) as much as possible. In command line, executions of aplay/arecord files under $PATH runs axfer with compatibility mode if filesystem has symbolic link from the aplay/arecord to axfer. </p>
<p> $ ln -s aplay axfer $ ln -s arecord axfer </p>
<h3>A string to which arg[0] points</h3>
<p> When args[0] in run time points to string ended with &#8216;aplay&#8217;, it has the same meaning of <i>playback</i> direction. When it points to string ended with &#8216;arecord&#8217;, it has the same meaning of <i>capture</i> direction. </p>
<h3>Options acknowledged as list subcommand</h3>
<p> Options of <i>-l</i> , <i>&#8211;list-devices</i> , <i>-L</i> , <i>&#8211;list-pcms</i> are acknowledged as <i>list</i> subcommand. Without them, the run time performs <i>transfer</i> subcommand. </p>
<h2>REPORTING BUGS</h2>
<p> Report any bugs to mailing list of ALSA community &lt;alsa-devel [at] alsa-project.org&gt; where the development and maintenance is primarily done. Bug tracking service of alsa-utils repository on github.com is also available. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-axfer-transfer/">axfer-transfer</a>(1),</code> <code><a href="/docs/linux/man/1-axfer-list/">axfer-list</a>(1),</code> <code><a href="/docs/linux/man/1-alsamixer/">alsamixer</a>(1),</code> <code><a href="/docs/linux/man/1-amixer/">amixer</a>(1)</code> </p>
<h2>AUTHOR</h2>
<p> Takashi Sakamoto &lt;o-takashi [at] sakamocchi.jp&gt; </p>
<h2>Index</h2>
