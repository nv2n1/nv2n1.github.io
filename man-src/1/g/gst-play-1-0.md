---
title: "gst-play-1-0(1)"
name: "gst-play-1-0"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gst-play-1-0/"
description: "gst-play-1.0 – Simple command line playback testing tool"
---

<p>gst-play-1.0 &#8211; Simple command line playback testing tool </p>
<h2>Synopsis</h2>
<p><code>gst-play-1.0</code> <i>FILE|DIRECTORY|URI [FILE2|DIRECTORY2|URI2]</i></p>
<h2>Description</h2>
<p><i>gst-play-1.0</i> is a command line tool that can be used to test basic playback using the playbin element. You can pass it individual files, URIs or whole directories (in which case it will recurse into sub-directories as well). </p>
<h2>Options</h2>
<p><i>gst-play-1.0</i> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd>Print help synopsis and available command line options</p>
<dt><code>&#8211;version</code></p>
<dd>Print version and exit</p>
<dt><code>&#8211;audiosink=SOMESINK</code></p>
<dd>Use the SOMESINK element as audio sink instead of autoaudiosink</p>
<dt><code>&#8211;videosink=SOMESINK</code></p>
<dd>Use the SOMESINK element as video sink instead of autovideosink</p>
<dt><code>&#8211;volume=VOLUME</code></p>
<dd>Set initial playback volume to VOLUME, where 0.0=silent and 1.0=unchanged</p>
<dt><code>&#8211;shuffle</code></p>
<dd>Shuffle playlist (play files in random order)</p>
<dt><code>&#8211;no-interactive</code></p>
<dd>Disable control through keyboard interaction in terminal (see below)</p>
<dt><code>&#8211;gapless</code></p>
<dd>Enable gapless playback</p>
<dt><code>-v, &#8211;flags</code></p>
<dd>Control playback behaviour setting playbin &#8216;flags&#8217; property</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Output status information and property notifications</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd>Do not print any output (apart from errors)</p>
<dt><code>&#8211;use-playbin3</code></p>
<dd>Use playbin3 pipeline (default varies depending on &#8216;USE_PLAYBIN&#8217; env variable)</p>
<dt><code>&#8211;wait-on-eos</code></p>
<dd>Keep showing the last frame on EOS until quit or playlist change command (gapless is ignored) </p>
</dl>
<h2>Interactive Keyboard Control</h2>
<dl>
<dt><code>SPACE</code></p>
<dd>Pause/Resume playback</p>
<dt><code>ARROW UP/DOWN</code></p>
<dd>Volume up/down</p>
<dt><code>ARROW LEFT/RIGHT</code></p>
<dd>Seek back/forward</p>
<dt><code>+/-</code></p>
<dd>Increase/decrease playback rate</p>
<dt><code>d</code></p>
<dd>Reverse playback direction</p>
<dt><code>t</code></p>
<dd>Cycle through trick modes</p>
<dt><code>a</code></p>
<dd>Switch audio track</p>
<dt><code>s</code></p>
<dd>Switch subtitle track</p>
<dt><code>v</code></p>
<dd>Switch video track</p>
<dt><code>&gt; or n</code></p>
<dd>Skip to next item in playlist</p>
<dt><code>&lt; or b</code></p>
<dd>Go back to previous item in playlist</p>
<dt><code>0</code></p>
<dd>Seek back to beginning of current track</p>
<dt><code>Q, ESC</code></p>
<dd>Quit </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gst-inspect-1-0/">gst-inspect-1.0</a></code>(1), <code><a href="/docs/linux/man/1-gst-launch-1-0/">gst-launch-1.0</a></code>(1), <code><a href="/docs/linux/man/1-gst-discoverer-1-0/">gst-discoverer-1.0</a></code>(1),</p>
<h2>Author</h2>
<p>The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a></p>
