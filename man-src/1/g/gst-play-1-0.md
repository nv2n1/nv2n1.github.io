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
<dt><code>&#8211;help</code></dt>
<dd>Print help synopsis and available command line options</dd>
<dt><code>&#8211;version</code></dt>
<dd>Print version and exit</dd>
<dt><code>&#8211;audiosink=SOMESINK</code></dt>
<dd>Use the SOMESINK element as audio sink instead of autoaudiosink</dd>
<dt><code>&#8211;videosink=SOMESINK</code></dt>
<dd>Use the SOMESINK element as video sink instead of autovideosink</dd>
<dt><code>&#8211;volume=VOLUME</code></dt>
<dd>Set initial playback volume to VOLUME, where 0.0=silent and 1.0=unchanged</dd>
<dt><code>&#8211;shuffle</code></dt>
<dd>Shuffle playlist (play files in random order)</dd>
<dt><code>&#8211;no-interactive</code></dt>
<dd>Disable control through keyboard interaction in terminal (see below)</dd>
<dt><code>&#8211;gapless</code></dt>
<dd>Enable gapless playback</dd>
<dt><code>-v, &#8211;flags</code></dt>
<dd>Control playback behaviour setting playbin &#8216;flags&#8217; property</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd>Output status information and property notifications</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd>Do not print any output (apart from errors)</dd>
<dt><code>&#8211;use-playbin3</code></dt>
<dd>Use playbin3 pipeline (default varies depending on &#8216;USE_PLAYBIN&#8217; env variable)</dd>
<dt><code>&#8211;wait-on-eos</code></dt>
<dd>Keep showing the last frame on EOS until quit or playlist change command (gapless is ignored) </dd>
</dl>
<h2>Interactive Keyboard Control</h2>
<dl>
<dt><code>SPACE</code></dt>
<dd>Pause/Resume playback</dd>
<dt><code>ARROW UP/DOWN</code></dt>
<dd>Volume up/down</dd>
<dt><code>ARROW LEFT/RIGHT</code></dt>
<dd>Seek back/forward</dd>
<dt><code>+/-</code></dt>
<dd>Increase/decrease playback rate</dd>
<dt><code>d</code></dt>
<dd>Reverse playback direction</dd>
<dt><code>t</code></dt>
<dd>Cycle through trick modes</dd>
<dt><code>a</code></dt>
<dd>Switch audio track</dd>
<dt><code>s</code></dt>
<dd>Switch subtitle track</dd>
<dt><code>v</code></dt>
<dd>Switch video track</dd>
<dt><code>&gt; or n</code></dt>
<dd>Skip to next item in playlist</dd>
<dt><code>&lt; or b</code></dt>
<dd>Go back to previous item in playlist</dd>
<dt><code>0</code></dt>
<dd>Seek back to beginning of current track</dd>
<dt><code>Q, ESC</code></dt>
<dd>Quit </dd>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gst-inspect-1-0/">gst-inspect-1.0</a></code>(1), <code><a href="/docs/linux/man/1-gst-launch-1-0/">gst-launch-1.0</a></code>(1), <code><a href="/docs/linux/man/1-gst-discoverer-1-0/">gst-discoverer-1.0</a></code>(1),</p>
<h2>Author</h2>
<p>The GStreamer team at <a rel="nofollow" href="http://gstreamer.freedesktop.org/">http://gstreamer.freedesktop.org/</a></p>
