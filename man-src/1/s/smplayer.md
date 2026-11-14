---
title: "smplayer(1)"
name: "smplayer"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smplayer/"
description: "SMPlayer – The best GUI frontend for MPlayer"
---

<h2 class="name">NAME</h2>
<p> SMPlayer &#8211; The best GUI frontend for MPlayer </p>
<h2>SYNOPSIS</h2>
<p> <code>smplayer</code> <i>[-minigui</i>] [<i>-mpcgui</i>] [<i>-defaultgui</i>] [<i>-config-path &lt;directory&gt;</i>] [<i>-send-action &lt;action_name&gt;</i>] [<i>-actions &lt;action_list&gt;</i>] [<i>[-no]-close-at-end</i>] [<i>[-no]-fullscreen</i>] [<i>-sub &lt;subtitle_file&gt;</i>] [<i>-pos &lt;x&gt; &lt;y&gt;</i>] [<i>-size &lt;width&gt; &lt;height&gt;</i>] [<i>-add-to-playlist</i>] [<i>-disable-server] [-help|&#8211;help|-h|-?</i>] [<i>&lt;media1&gt;</i>] [<i>&lt;media2&gt;</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<dl>
<dt>SMPlayer is a GUI media player based on Qt, using <code><a href="/docs/linux/man/1-mplayer/">mplayer</a></code>(1) as its backend.</p>
<dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-minigui</code></p>
<dd> Open the mini GUI instead of the default one.</p>
<dt><code>-mpcgui</code></p>
<dd> Open the mpc GUI instead of the default one.</p>
<dt><code>-defaultgui</code></p>
<dd> Open the default gui.</p>
<dt><code>-config-path &lt;directory&gt;</code></p>
<dd> Specify the directory for the configuration files (smplayer.ini, smplayer_files.ini&#8230;).</p>
<dt><code>-send-action &lt;action_name&gt;</code></p>
<dd> Try to make a connection to another running instance and send to it the specified action.</p>
<dt>
<dd> <i>Example</i>: smplayer -send-action pause</p>
<dt>
<dd> The rest of options (if any) will be ignored and the application will exit. It will return 0 on success or -1 on failure.</p>
<dt><code>-actions &lt;action_list&gt;</code></p>
<dd> &lt;action_list&gt; is a list of actions separated by spaces. The actions will be executed just after loading the file (if any) in the same order as input. For switchable actions you can pass true or false as parameter.</p>
<dt>
<dd> <i>Example</i>: smplayer -actions.br &quot;fullscreen compact true&quot;</p>
<dt>
<dd> Quotes are necessary in case you pass more than one action.</p>
<dt><code>-close-at-end</code></p>
<dd> Close the main window when the file/playlist finishes.</p>
<dt><code>-no-close-at-end</code></p>
<dd> Do not close the main window when the file/playlist finishes.</p>
<dt><code>-fullscreen</code></p>
<dd> Play the video in fullscreen mode.</p>
<dt><code>-no-fullscreen</code></p>
<dd> Play the video in windowed mode.</p>
<dt><code>-sub</code></p>
<dd> Specify the subtitle file to be loaded (for the first video only).</p>
<dt><code>-pos &lt;x&gt; &lt;y&gt;</code></p>
<dd> Specify the coordinates where the main window will be displayed.</p>
<dt><code>-size &lt;width&gt; &lt;height&gt;</code></p>
<dd> Specify the size of the main window.</p>
<dt><code>-h, -help, &#8211;help, -?</code></p>
<dd> Show the help message and then exit.</p>
<dt><code>-add-to-playlist</code></p>
<dd> If there is another instance running, the media will be added to that instance&#8217;s playlist. If there is no other instance, this option will be ignored and the files will be opened in a new instance.</p>
<dt><code>-disable-server</code></p>
<dd> Disables the server used to communicate with other instances. This also disables the possibility to use a single instance.</p>
<dt><code>&lt;media1&gt; &lt;media2&gt; &#8230;</code></p>
<dd> Any kind of file that SMPlayer can open. It can be a local file, a DVD (e.g. <a href="dvd://1">dvd://1</a>), an Internet stream (e.g. <a href="mms://....)">mms://&#8230;.)</a> or a local playlist in format m3u or pls.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mplayer/">mplayer</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> The author of SMPlayer is Ricardo Villalba &lt;ricardo [at] smplayer.info&gt;. </p>
<p> This manual page was written by Matvey Kozhev &lt;sikon [at] lucidfox.org&gt; for the Ubuntu project (but may be used by others). Has been updated by greengreat &lt;gmeildeno [at] gmail.com&gt; for the SMPlayer project (July 2009). </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. On Debian systems, the complete text of the GNU General Public License can be found in <code>/usr/share/common-licenses/GPL</code>. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt> </p>
<h2>BUGS</h2>
<p> Please submit bugs to <code><a rel="nofollow" href="http://sourceforge.net/projects/smplayer">http://sourceforge.net/projects/smplayer</a></code>. </p>
<h2>Index</h2>
