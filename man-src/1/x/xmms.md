---

title: "xmms(1)"
name: "xmms"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmms/"
description: "XMMS – an audio player for X."
---

<h2>NAME</h2>
<p> XMMS &#8211; an audio player for X.</p>
<p> <code>xmms</code> [-h] [&#8211;help] [-n <i>&lt;session&gt;</i>] [&#8211;session=<i>&lt;session&gt;</i>] [-r] [&#8211;rew] [-p] [&#8211;play] [-u] [&#8211;pause] [-s] [&#8211;stop] [-t] [&#8211;play-pause] [-f] [&#8211;fwd] [-e] [&#8211;enqueue] [-S] [&#8211;toggle-shuffle] [-R] [&#8211;toggle-repeat] [-A] [&#8211;toggle-advance] [-m] [&#8211;show-main-window] [-q] [&#8211;quit] [-i <i>&lt;session id&gt;</i>] [&#8211;sm-client-id=<i>&lt;session id&gt;</i>] [-v] [&#8211;version] [<i>filename</i>]&#8230;</p>
<p> <i>XMMS</i> is the X Multimedia System. It is used to play audio and other kinds of media files. By default XMMS can play MPEG audio, Ogg Vorbis, RIFF wav, most module formats and a few other formats. XMMS can be extended through plugins to play a number of other audio and video formats.</p>
<h2>OPTIONS</h2>
<p> XMMS accepts the following options:</p>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>-n, &#8211;session</code></dt>
<dd> Select XMMS session (Default: 0).</dd>
<dt><code>-r, &#8211;rew</code></dt>
<dd> Skip backwards in playlist.</dd>
<dt><code>-p, &#8211;play</code></dt>
<dd> Start playing current playlist.</dd>
<dt><code>-u, &#8211;pause</code></dt>
<dd> Pause current song.</dd>
<dt><code>-s, &#8211;stop</code></dt>
<dd> Stop current song.</dd>
<dt><code>-t, &#8211;play-pause</code></dt>
<dd> Pause if playing, play otherwise.</dd>
<dt><code>-f, &#8211;fwd</code></dt>
<dd> Skip forward in playlist.</dd>
<dt><code>-e, &#8211;enqueue</code></dt>
<dd> Don&#8217;t clear the playlist.</dd>
<dt><code>-Q, &#8211;queue</code></dt>
<dd> Add file(s) to playlist and queue</dd>
<dt><code>-S, &#8211;toggle-shuffle</code>[=<i>SWITCH</i>]</dt>
<dd> Toggle the &#8216;shuffle&#8217; flag. </dd>
<p> Optional argument SWITCH may be either &#8216;on&#8217; or &#8216;off&#8217;</p>
<dt><code>-R, &#8211;toggle-repeat</code>[=<i>SWITCH</i>]</dt>
<dd> Toggle the &#8216;repeat&#8217; flag. </dd>
<p> Optional argument SWITCH may be either &#8216;on&#8217; or &#8216;off&#8217;</p>
<dt><code>-A, &#8211;toggle-advance</code>[=<i>SWITCH</i>]</dt>
<dd> Toggle the &#8216;no playlist advance&#8217; flag. </dd>
<p> Optional argument SWITCH may be either &#8216;on&#8217; or &#8216;off&#8217;</p>
<dt><code>-m, &#8211;show-main-window</code></dt>
<dd> Show the main window.</dd>
<dt><code>-i, &#8211;sm-client-id</code></dt>
<dd> Set session manager identification.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Print version number and exit.</dd>
<dt><code>-q, &#8211;quit</code></dt>
<dd> Close remote session.</dd></dl>
<h2>SKINS</h2>
<p> XMMS supports WinAmp style skins. Skins may be stored in either archived (<i>.zip</i>, <i>.wsz</i>, <i>.tgz</i>, <i>.tar.gz</i>, or <i>.tar.bz2</i>) or unarchived format. XMMS looks for skinfiles in /usr/share/xmms/Skins, ~/.xmms/Skins, and locations specified by the <code>SKINSDIR</code> variable.</p>
<h2>KEYBINDINGS</h2>
<p> Global keybindings for XMMS: </p>
<p> z<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Previous song</p>
<p> x<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Play</p>
<p> c<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Pause</p>
<p> v<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Stop</p>
<p> b<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Next song</p>
<p> l<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Play file</p>
<p> j<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Jump to file</p>
<p> r<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle Repeat</p>
<p> s<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle Shuffle</p>
<p> Shift + l<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Play directory</p>
<p> Control + l<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Play location</p>
<p> Control + p<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Preferences dialog</p>
<p> Control + v<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Visualization plugin dialog</p>
<p> Control + r<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Time remaining</p>
<p> Control + a<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Always on top</p>
<p> Control + w<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Winshade mode</p>
<p> Control + d<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Doublesize mode</p>
<p> Control + e<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Easy move</p>
<p> Control + j<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Jump to time</p>
<p> Control + z<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Start of list</p>
<p> Control + n<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>No Playlist Advance</p>
<p> Control + 3<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>File info dialog</p>
<p> Control + Alt + w<tt>&nbsp;<wbr>&nbsp;<wbr></tt>Toggle Equalizer winshade mode</p>
<p> Shift + Control + wPlaylist winshade mode</p>
<p> Alt + w<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Hide/show mainwindow</p>
<p> Alt + e<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Hide/show playlistwindow</p>
<p> Alt + g<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Hide/show Equalizer</p>
<p> Alt + s<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Skin selecting window</p>
<p> Main window specific: </p>
<p> Arrow key up<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Volume up 2%</p>
<p> Arrow key down<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Volume down 2%</p>
<p> Arrow key right<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Skip 5 seconds forward in song</p>
<p> Arrow key left<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Skip 5 seconds back in song</p>
<p> Playlist window specific: </p>
<p> Arrow key up<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Up one step in playlist</p>
<p> Arrow key down<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Down one step in playlist</p>
<p> Delete<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Remove selected songs from playlist</p>
<p> Control + Delete<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Keeps the selected tracks and removes the rest</p>
<p> Q<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Queue/Dequeue the tracks selected</p>
<p> Shift + Q<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Clear the queue list</p>
<p> Alt + Q<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Queue manager</p>
<p> Page Up<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Move one page up</p>
<p> Page Down<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Move one page down</p>
<p> Home<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>First page in playlist</p>
<p> End<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Last page in playlist</p>
<p> Enter<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Play selected song</p>
<p> Insert<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Add file dialog</p>
<p> Shift + Insert<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Add directory dialog</p>
<p> Alt + Insert<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Add url dialog</p>
<p> Equalizer shade mode specific: </p>
<p> Arrow key up<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Volume up 2%</p>
<p> Arrow key down<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Volume down 2%</p>
<p> Arrow key right<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Balance 4% to right</p>
<p> Arrow key left<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Balance 4% to left</p>
<h2>FILES</h2>
<dl>
<dt>~/.xmms/config</dt>
<dd> Users xmms configuration.</dd>
<dt>~/.xmms/xmms.m3u</dt>
<dd> Default playlist usually loaded on startup.</dd>
<dt>~/.xmms/gtkrc</dt>
<dd> Users set of xmms-specific GTK config settings. Options such as widget color and fonts sizes can be set here.</dd>
<dt>~/.xmms/menurc</dt>
<dd> Users set of keybindings.</dd>
<dt>~/.xmms/Skins, /usr/share/xmms/Skins</dt>
<dd> Default locations where XMMS should look for skinfiles.</dd>
<dt>~/.xmms/Plugins</dt>
<dd> Location of user installed plugins.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>SKINSDIR</code></dt>
<dd> Colon separated list of paths where XMMS should look for skinfiles.</dd>
<dt><code>TARCMD</code></dt>
<dd> Tar command supporting GNU tar style decompression. Used for unpacking gzip and bzip2 compressed skins. Default is <i>tar</i>.</dd>
<dt><code>UNZIPCMD</code></dt>
<dd> Command for decompressing zip files (skins). Default is <i>unzip</i>.</dd></dl>
<h2>OTHER INFO</h2>
<p> The webpage for XMMS is at <a rel="nofollow" href="http://www.xmms.org.">http://www.xmms.org.</a> Here you can find info about XMMS, download the latest version, plugins, and skins.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wmxmms/">wmxmms</a></code>(1) </p>
