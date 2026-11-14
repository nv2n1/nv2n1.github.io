---
title: "finch(1)"
name: "finch"
section: "1"
letter: "f"
url: "/docs/linux/man/1-finch/"
description: "Finch – A Pimpin’ Penguin console frontend to libpurple. Instant Messaging client."
---

<h2>NAME</h2>
<p> Finch &#8211; A Pimpin&#8217; Penguin console frontend to libpurple. Instant Messaging client.</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>finch </code><i>[options]</i></p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>finch</code> is a console-based modular messaging client based on libpurple which is capable of connecting to AIM, MSN, Yahoo!, XMPP, ICQ, IRC, SILC, Novell GroupWise, Lotus Sametime, Zephyr, Gadu-Gadu, and QQ all at once. It has many common features found in other clients, as well as many unique features. Finch is not endorsed by or affiliated with America Online, ICQ, Microsoft, or Yahoo. </p>
<h2>OPTIONS</h2>
<p> The following options are provided by <code>finch</code> using the standard GNU command line syntax:</p>
<dl>
<dt><code>-c, &#8211;config=</code><i>DIR</i></p>
<dd> Use <i>DIR</i> as the directory for config files instead of <i>~/.purple</i>.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Print debugging messages to stderr and start with the <code>Debug</code> window. The messages shown in the <code>Debug</code> window are the same as the ones printed in stderr.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print this help and exit.</p>
<dt><code>-n, &#8211;nologin</code></p>
<dd> Don&#8217;t automatically login when <code>finch</code> starts. Sets all accounts to Offline.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display the version information window. </p>
</dl>
<h2>GNT Shortcuts</h2>
<p> You can use the following shortcuts (see the &quot;Widget Actions&quot; section for a more complete list):</p>
<dl>
<dt><code>Alt + a</code></p>
<dd> Bring up a list of available actions. You can use this list to access the accounts window, plugins window, preference window etc.</p>
<dt><code>Alt + n</code></p>
<dd> Go to the next window.</p>
<dt><code>Alt + p</code></p>
<dd> Go to the previous window.</p>
<dt><code>Alt + w</code></p>
<dd> Show the list of windows. You can select and jump to any window from the list.</p>
<dt><code>Alt + c</code></p>
<dd> Close the current window.</p>
<dt><code>Alt + q</code></p>
<dd> Quit.</p>
<dt><code>Alt + m</code></p>
<dd> Start moving a window. Press the cursor keys to move the window. When you are done, press <code>Enter</code> or <code>Escape</code>.</p>
<dt><code>Alt + r</code></p>
<dd> Start resizing a window. Press the cursor keys to resize the window. When you are done, press <code>Enter</code> or <code>Escape</code>.</p>
<dt><code>Alt + D</code></p>
<dd> Dump the contents of the screen in HTML format.</p>
<dt><code>Alt + .</code></p>
<dd> Move the position of the current window in the window list one place to the right.</p>
<dt><code>Alt + ,</code></p>
<dd> Move the position of the current window in the window list one place to the left.</p>
<dt><code>Alt + l</code></p>
<dd> Refresh the windows. This is useful after resizing the terminal window.</p>
<dt><code>Alt + 1 2 &#8230; 0</code></p>
<dd> Jump to the 1st, 2nd &#8230; 10th window.</p>
<dt><code>Alt + Tab</code></p>
<dd> Jump to the next URGENT (highlighted) window.</p>
<dt><code>Alt + Shift + Tab</code></p>
<dd> Jump to the previous URGENT (highlighted) window.</p>
<dt><code>Ctrl + o </code> or <code> F10</code></p>
<dd> Bring up the menu (if there is one) for a window.</p>
<dt><code>F11 </code> or <code> Ctrl + x</code></p>
<dd> Popup the context menu (if there is one) for the selected widget.</p>
<dt><code>Alt + /</code></p>
<dd> Show a list of available key-bindings for the current widget in focus.</p>
<dt><code>Alt + &gt;</code></p>
<dd> Switch to the next workspace</p>
<dt><code>Alt + &lt;</code></p>
<dd> Switch to the previous workspace</p>
<dt><code>Alt + t</code></p>
<dd> Tag (or untag) the current window</p>
<dt><code>Alt + T</code></p>
<dd> Attached all the tagged windows to the current workspace</p>
<dt><code>Alt + s</code></p>
<dd> Show the workspace list</p>
<dt><code>F9</code></p>
<dd> Create a new workspace and switch to it </p>
</dl>
<h2>FILES</h2>
<p> <i>~/.gntrc</i>: configuration file for gnt applications. </p>
<dl>
<dt>A sample file looks like:</p>
<dd>
 [Finch]<br />
 color-available = green; black<br />
 color-away = blue; black<br />
 color-idle = gray; black<br />
 color-offline = red; black<br />
 color-message-sent = cyan; default<br />
 color-message-received = red; default<br />
 color-message-highlight = black; green<br />
 color-message-action = yellow; default<br />
 color-timestamp = blue; default<br />
 #See below for details on color </p>
<p> [general]<br />
 shadow = 0<br />
 # There is experimental mouse support<br />
 mouse = 1<br />
 # To use some custom window-manager<br />
 wm = /usr/local/lib/gnt/s.so<br />
 # There&#8217;s also a custom window manager called irssi.so<br />
 # Remember window-positions based on the titles (on by default)<br />
 remember_position = 1<br />
 # Use borderless one-line high buttons<br />
 small-button = true </p>
<p> # Workspaces are created simply by adding Workspace-X groups as follows:<br />
 [Workspace-1]<br />
 name = blist<br />
 # window-names specifies that windows with these semi-colon separated names are placed into this workspace<br />
 window-names = buddylist;debug-window </p>
<p> [Workspace-2]<br />
 name = IM<br />
 window-names = conversation-window<br />
 # window-titles specifies that windows with these semi-colon separated titles are placed into this workspace. These are matched as substrings. Window titles take precedence over names.<br />
 window-titles = Preferences;Pounce </p>
<p> [colors]<br />
 # The RGB values range in [0, 1000]<br />
 black = 0; 0; 0<br />
 red = 1000; 0; 0<br />
 green = 0; 1000; 0<br />
 blue = 250; 250; 700<br />
 white = 1000; 1000; 1000<br />
 gray = 700; 700; 700<br />
 darkgray = 256; 256; 256 </p>
<p> [colorpairs]<br />
 normal = white; black<br />
 highlight = white; blue<br />
 highlightd = black; gray<br />
 shadow = black; darkgray<br />
 title = white; blue<br />
 titled = white; gray<br />
 text = white; blue<br />
 disabled = gray; black<br />
 urgent = green; black </p>
<p> # Remap some keys for GntEntry<br />
 [GntEntry::remap]<br />
 # Remap the up-arrow to the left-arrow<br />
 ^[[A = ^[[D<br />
 # Remap the down-arrow to the right-arrow<br />
 ^[[B = ^[[C<br />
 # Remap &#8216;a&#8217; to &#8216;bcd&#8217;<br />
 a = bcd<br />
 # Completely ignore the key &#8216;q&#8217;<br />
 q =<br />
 # But the following will NOT work<br />
 #abc = bcd </p>
<p> # Hitting &#8216;space&#8217; will activate a button<br />
 [GntButton::remap]<br />
 \ =  </p>
</dl>
<h2>Widget Actions</h2>
<p> You can specifiy key-bindings for specific widgets. The following entries in <i>~/.gntrc</i> correspond to the default keybindings for the actions: </p>
<p> [GntBox::binding]<br />
 tab = focus-next<br />
 right = focus-next<br />
 left = focus-prev </p>
<p> [GntComboBox::binding]<br />
 down = dropdown<br />
 up = dropdown </p>
<p> [GntEntry::binding]<br />
 c-a = cursor-home<br />
 home = cursor-home<br />
 c-e = cursor-end<br />
 end = cursor-end<br />
 backspace = delete-prev<br />
 del = delete-next<br />
 c-d = delete-next<br />
 c-u = delete-start<br />
 c-k = delete-end<br />
 c-b = cursor-prev<br />
 left = cursor-prev<br />
 c-f = cursor-next<br />
 right = cursor-next<br />
 tab = suggest-show<br />
 down = suggest-next<br />
 up = suggest-prev<br />
 page-down = suggest-next-page<br />
 page-up = suggest-prev-page<br />
 c-w = delete-prev-word<br />
 a-b = cursor-prev-word<br />
 a-f = cursor-next-word<br />
 a-d = delete-next-word<br />
 c-v = clipboard-paste<br />
 c-p = history-prev<br />
 c-n = history-next<br />
 c-r = history-search<br />
 c-up = history-prev<br />
 c-down = history-next </p>
<p> [GntTree::binding]<br />
 up = move-up<br />
 down = move-down<br />
 c-n = move-down<br />
 c-p = move-up<br />
 pageup = page-up<br />
 pagedown = page-down<br />
 backspace = move-parent<br />
 home = move-first<br />
 end = move-last<br />
 # Following is the default binding for the context-menu<br />
 menu = context-menu<br />
 # The following will let you open the context-menu in the buddylist with c-b<br />
 # c-b = context-menu </p>
<p> [GntWidget::binding]<br />
 f11 = context-menu<br />
 c-x = context-menu </p>
<p> [GntWindow::binding]<br />
 c-o = show-menu<br />
 f10 = show-menu </p>
<p> The <code>c-</code> corresponds to the <code>Control</code> key. You can also use <code>ctrl-</code> or <code>ctr-</code> or <code>ctl-</code> to indicate a combination. For alt-keys, you can use one of <code>a-</code>, <code>alt-</code>, <code>m-</code> or <code>meta-</code>. You can also use <code>home</code>, <code>end</code>, <code>left</code>, <code>right</code> etc. keys. </p>
<p> To unbind a key which has a default binding, you simply bind it to the empty string. For example, to unbind <code>Alt + q</code> from the Quit function, you would use: </p>
<p> [GntWM::binding]<br />
 a-q = </p>
<h2>Menus</h2>
<p> You can also specify key-bindings to trigger specific menuitems in windows. For example, the following entry in <i>~/.gntrc</i> will bind <code>Ctrl + t</code> to the &#8216;Send IM&#8230;&#8217; item in the buddylist: </p>
<p> [buddylist::menu]<br />
 c-t = send-im </p>
<p> The following is the list of IDs of the current menuitems in the buddylist: </p>
<p> send-im<br />
 join-chat<br />
 show-empty-groups<br />
 show-offline-buddies<br />
 sort-status<br />
 sort-alpha<br />
 sort-log<br />
 add-buddy<br />
 add-chat<br />
 add-group </p>
<h2>Mouse Support</h2>
<p> There is experimental mouse support. You can focus windows, activate buttons, select rows in a list, scroll using the wheel-scroll etc. Selecting text in a text-view copies it to the gnt clipboard. Mouse support is disabled by default, so you need to enable it in <i>~/.gntrc</i> (see the sample above). </p>
<h2>Window Management</h2>
<p> The default window management is very limited. But it is possible to write custom window managers to suit your needs. There is a sample window-manager included (named <i>s.so</i>) which adds a little &#8216;close-button&#8217; for the windows, removes the borders from the buddylist and pops up new windows in the middle of the screen, instead of at the upper-left corder. It is provided as a sample simple manager, but it should be possible to write more complex managers, and it&#8217;s very possible that the window-manager API will need to be enhanced. Look at the sample <i>~/.gntrc</i> file above to see how to select a window-manager. </p>
<p> It is also possible to rebind the window-manager actions in <i>~/.gntrc</i>, eg: </p>
<p> [GntWM::binding]<br />
 a-n = window-next<br />
 a-p = window-prev<br />
 a-c = window-close<br />
 a-w = window-list<br />
 a-d = dump-screen<br />
 a-, = shift-left<br />
 a-. = shift-right<br />
 a-a = action-list<br />
 a-m = start-move<br />
 a-r = start-resize<br />
 a-q = wm-quit<br />
 a-l = refresh-screen<br />
 a-s = workspace-list<br />
 a-t = window-tag<br />
 a-T = place-tagged<br />
 a-C = toggle-clipboard<br />
 a-/ = help-for-widget<br />
 a-c-j = window-scroll-down<br />
 a-c-k = window-scroll-up<br />
 # The following action is still incomplete, and doesn&#8217;t have a default binding<br />
 # switch-window-n<br />
 # Other actions: window-next-urgent, window-prev-urgent </p>
<p> # For the sample custom window manager<br />
 [GntS::binding]<br />
 a-b = toggle-buddylist </p>
<p> # For the irssi window manager<br />
 [Irssi::binding]<br />
 a-L = move-right<br />
 a-H = move-left<br />
 a-J = move-down<br />
 a-K = move-up </p>
<h2>Conversation Commands</h2>
<p> There are a few helpful commands in addition to the regular commands. You can use these from any conversation to access other windows. </p>
<dl>
<dt><code>accounts</code></p>
<dd> for the accounts window. </p>
<dt><code>buddylist</code></p>
<dd> for the buddylist. </p>
<dt><code>debugwin</code></p>
<dd> for the debug window. </p>
<dt><code>plugins</code></p>
<dd> for the plugins window. </p>
<dt><code>prefs</code></p>
<dd> for the preferences window. </p>
<dt><code>status</code></p>
<dd> for the status window. </p>
</dl>
<h2>FAQ</h2>
<p> FAQ for <code>finch</code> is located at<br />
 <i><a rel="nofollow" href="http://developer.pidgin.im/wiki/Using%20Finch">http://developer.pidgin.im/wiki/Using%20Finch</a></i> </p>
<h2>BUGS</h2>
<p> Known bugs are listed at<br />
 <i><a rel="nofollow" href="http://developer.pidgin.im/query?status=new">http://developer.pidgin.im/query?status=new</a>&amp;status=assigned&amp;status=reopened&amp;component=finch+%28gnt%2Fncurses%29&amp;order=priority</i> </p>
<p> Before sending a bug report, please verify that you have the latest version of <code>finch</code> and libpurple. Many bugs (major and minor) are fixed at each release, and if yours is out of date, the problem may already have been solved. </p>
<h2>PATCHES</h2>
<p> If you fix a bug in <code>finch</code> (or otherwise enhance it), please submit a patch (using <code>mtn diff &gt; my.diff</code> against the latest version from the Monotone repository) at <i><a rel="nofollow" href="http://developer.pidgin.im/simpleticket">http://developer.pidgin.im/simpleticket</a></i> </p>
<p> You are also encouraged to drop by at <code>#pidgin</code> on <i>irc.freenode.net</i> to discuss development. </p>
<h2>SEE ALSO</h2>
<p> <i><a rel="nofollow" href="http://pidgin.im/">http://pidgin.im/</a></i><br />
 <i><a rel="nofollow" href="http://developer.pidgin.im/">http://developer.pidgin.im/</a></i><br />
 <code><a href="/docs/linux/man/1-purple-remote/">purple-remote</a></code>(1)<br />
 <code><a href="/docs/linux/man/1-pidgin/">pidgin</a></code>(1) </p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <code>WITHOUT ANY WARRANTY</code>; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02111-1301 USA </p>
<h2>AUTHORS</h2>
<p> Sadrul Habib Chowdhury &lt;<i>sadrul [at] users.sourceforge.net</i>&gt; </p>
<p> This manpage was written by Sadrul Habib Chowdhury &lt;<i>sadrul [at] users.sourceforge.net</i>&gt; and Dennis Ristuccia &lt;<i>dennis [at] dennisr.net</i>&gt;. </p>
<h2>Index</h2>
