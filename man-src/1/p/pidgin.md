---
title: "pidgin(1)"
name: "pidgin"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pidgin/"
description: "pidgin – Instant Messaging client"
---

<h2>NAME</h2>
<p> pidgin &#8211; Instant Messaging client</p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>pidgin </code><i>[options]</i></p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>pidgin</code> is a graphical modular messaging client based on libpurple which is capable of connecting to AIM, MSN, Yahoo!, XMPP, ICQ, IRC, SILC, Novell GroupWise, Lotus Sametime, Zephyr, Gadu-Gadu, and QQ all at once. It has many common features found in other clients, as well as many unique features. Pidgin is not endorsed by or affiliated with America Online, ICQ, Microsoft, or Yahoo. </p>
<p> Pidgin can be extended by plugins written in multiple programming languages and controlled through DBus or <code>purple-remote</code>. </p>
<h2>OPTIONS</h2>
<p> The following options are provided by Pidgin using the standard GNU command line syntax:</p>
<dl>
<dt><code>-c, &#8211;config=</code><i>DIR</i></p>
<dd> Use <i>DIR</i> as the directory for config files instead of <i>~/.purple</i>.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Print debugging messages to stdout. These are the same debugging messages that are displayed in the <code>Debug Window</code>.</p>
<dt><code>-f, &#8211;force-online</code></p>
<dd> Try to be online even if the network is reported (by Windows, or NetworkManager on Linux) to be unavailable.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print a summary of command line options and exit.</p>
<dt><code>-m, &#8211;multiple</code></p>
<dd> Allow multiple instances of Pidgin to run.</p>
<dt><code>-n, &#8211;nologin</code></p>
<dd> Don&#8217;t automatically login when Pidgin starts. Sets the global status to <code>Offline</code>.</p>
<dt><code>-l, &#8211;login[=</code><i>NAME</i>,<i>NAME</i>,&#8230;]</p>
<dd> Enable the comma-separated list of accounts provided, disabling all other accounts. If the user does not specify such a comma-separated list, the first account in accounts.xml will be enabled.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Print the current version and exit. </p>
</dl>
<h2>TERMS</h2>
<p> Pidgin uses a few terms differently from other applications. For convenience they are defined here:</p>
<dl>
<dt><code>Buddy List</code></p>
<dd> The list of other users who the user wants to see status information for and have quick access to for messaging.</p>
<dt><code>Buddy</code></p>
<dd> A user who has been added to the Buddy List.</p>
<dt><code>Contact</code></p>
<dd> A grouping of more than one buddy who are all the same person. A contact may contain buddies from any protocol and may contain as many buddies as the user desires. Contact arrangements are stored locally only.</p>
<dt><code>Alias</code></p>
<dd> A private &quot;nickname&quot; that may be set for Buddies or the user himself. On some protocols, aliases are saved on the server but not visible to other users. On other protocols, aliases are saved only locally.</p>
<dt><code>Protocol</code></p>
<dd> A messaging service. AIM, XMPP, MSN, Zephyr, etc. are protocols. Others may call these &quot;service types,&quot; &quot;account types,&quot; &quot;services,&quot; and so on. </p>
</dl>
<h2>BUDDY LIST</h2>
<p> The <code>Buddy List</code> window is Pidgin&#8217;s main interface window. Using this window a user can see which of his/her buddies is online, away, idle, etc. The user can also add buddies to and remove buddies from the buddy list. </p>
<p> The <code>Buddy List</code> window contains a list of the user&#8217;s buddies who are online and have allowed the user to be notified of their presence. The icon to the left of each buddy indicates the buddy&#8217;s current status. Double clicking a buddy will open a new <code>Conversation</code> window. Right clicking will pop up a menu:</p>
<dl>
<dt><code>Get Info</code></p>
<dd> Retrieves and displays information about the buddy. This information is also known as a Profile.</p>
<dt><code>IM</code></p>
<dd> Opens a new <code>Conversation</code> window to the selected buddy.</p>
<dt><code>Send File</code></p>
<dd> Sends a file to the selected buddy (only available on protocols that support file transfer).</p>
<dt><code>Add Buddy Pounce</code></p>
<dd> A Buddy Pounce is a configurable automated action to be performed when the buddy&#8217;s state changes. This will open the <code>Buddy Pounce</code> dialog, which will be discussed later.</p>
<dt><code>View Log</code></p>
<dd> Pidgin is capable of automatically logging messages. These logs are either plain text files (with a .txt extension) or html files (with a .html extension) located under the <i>~/.purple/logs</i> directory. This menu command will display Pidgin&#8217;s log viewer with logs loaded for that buddy or chat.</p>
<dt><code>Alias</code></p>
<dd> Create an alias for this buddy. This will show an editable text field where the buddy&#8217;s name was displayed. In this field one can give this buddy an alternate, more friendly name to appear on the buddy list and in conversations. </p>
<p> For example, if a buddy&#8217;s name was jsmith1281xx and his real name was &#8216;John Q. Smith,&#8217; one could create an alias as to identify the buddy by his common name.</dl>
<p> The remainder of the menu will consist of protocol specific commands. These commands vary depending on the protocol.</p>
<dl>
<dt><code>Status Selector</code></p>
<dd> At the bottom of the <code>Buddy List</code> is a status selector which allows one to change his/her status. This will be discussed further in the <code>STATUS MESSAGES</code> section below. </p>
</dl>
<h2>ACCOUNT EDITOR</h2>
<p> The account editor consists of a list of accounts and information about them. It can be accessed by selecting <code>Manage</code> from the Accounts menu. Clicking <i>Delete</i> will delete the currently selected account. Clicking <i>Add</i> or <i>Modify</i> will invoke a <code>Modify Account</code> window. Here, the user can add or alter account information. When creating a new account, the user will submit a username and password. The user will also choose the protocol for the account. </p>
<p> If <i>Remember Password</i> is chosen, the password will be saved in Pidgin&#8217;s <i>~/.purple/accounts.xml</i> configuration file. </p>
<p> If <i>Enabled</i> is checked in the accounts dialog, this account will follow the status currently selected in the status selector. If it is not checked, the account will always be offline. </p>
<p> Each protocol has its own specific options that can be found in the modify screen. </p>
<h2>PREFERENCES</h2>
<p> All options take effect immediately. </p>
<h2>Interface</h2>
<dl>
<dt><code>Show system tray icon</code></p>
<dd> Specifies when to show a Pidgin icon in the notification area of the user&#8217;s panel (commonly referred to as the System Tray). </p>
<dt><code>Hide new IM conversations</code></p>
<dd> Specifies when to hide new IM messages. Messages will queue under the specified condition until shown. Clicking the Pidgin icon in the notification area or system tray will display the queued messages. An icon also appears in the buddy list&#8217;s menu bar; this icon may also be used to display queued messages. </p>
<dt><code>Show IMs and chats in tabbed windows</code></p>
<dd> When checked, this option will cause IM and chat sessions to appear in windows with multiple tabs. One tab will represent one conversation or chat. Where tabs are placed will be dictated by the preferences below. </p>
<dt><code>Show close buttons on tabs</code></p>
<dd> When checked, this option will cause a clickable &quot;U+2715 MULTIPLICATION X&quot; unicode character to appear at the right edge of each tab. Clicking this will cause the tab to be closed. </p>
<dt><code>Placement</code></p>
<dd> Specifies where to place tabs in the window. Some tab orientations may allow some users to fit more tabs into a single window comfortably. </p>
<dt><code>New conversations</code></p>
<dd> Specifies under which conditions tabs are placed into existing windows or into new windows. For a single window, select <i>Last created window</i> here. </p>
</dl>
<h2>Conversations</h2>
<dl>
<dt><code>Enable buddy icon animation</code></p>
<dd> If a buddy&#8217;s icon happens to be animated, this option will enable the animation, otherwise only the first frame will be displayed. </p>
<dt><code>Notify buddies that you are typing to them</code></p>
<dd> Some protocols allow clients to tell their buddies when they are typing. This option enables this feature for protocols that supports it. </p>
<dt><code>Default Formatting</code></p>
<dd> Allows specifying the default formatting to apply to all outgoing messages (only applicable to protocols that support formatting in messages). </p>
</dl>
<h2>Smiley Themes</h2>
<p> Allows the user to choose between different smiley themes. The &quot;none&quot; theme will disable graphical emoticons &#8211; they will be displayed as text instead. The <code>Add</code> and <code>Remove</code> buttons may be used to install or uninstall smiley themes. Themes may also be installed by dragging and dropping them onto the list of themes. </p>
<h2>Sounds</h2>
<dl>
<dt><code>Method</code></p>
<dd> Lets the user choose between different playback methods. The user can also manually enter a command to be executed when a sound is to be played(<i>%s</i> expands to the full path to the file name). </p>
<dt><code>Sounds when conversation has focus</code></p>
<dd> When checked, sounds will play for events in the active conversation if the window is focused. When unchecked, sounds will not play for the active conversation when the window is focused. </p>
<dt><code>Enable Sounds</code></p>
<dd> Determines when to play sounds. </p>
<dt><code>Sound Events</code></p>
<dd> Lets the user choose when and what sounds are to be played. </p>
</dl>
<h2>Network</h2>
<dl>
<dt><code>STUN server</code></p>
<dd> This allows specifying a server which uses the STUN protocol to determine a host&#8217;s public IP address. This can be particularly useful for some protocols. </p>
<dt><code>Autodetect IP address</code></p>
<dd> When checked, causes Pidign to attempt to determine the public IP address of the host on which Pidgin is running and disables the <code>Public IP</code> text field listed below. </p>
<dt><code>Public IP</code></p>
<dd> If <code>Autodetect IP address</code> is disabled, this field allows manually specifying the public IP address for the host on which Pidgin is running. This is mainly useful for users with multiple network interfaces or behind NATs. </p>
<dt><code>Manually specify range of ports to listen on</code></p>
<dd> Specify a range ports to listen on, overriding any defaults. This is sometimes useful for file transfers and Direct IM. </p>
<dt><code>Proxy Server</code></p>
<dd> The configuration section to enable Pidgin to operate through a proxy server. Pidgin currently supports SOCKS 4/5 and HTTP proxies. </p>
</dl>
<h2>Browser</h2>
<dl>
<dt><code>Browser</code></p>
<dd> Allows the user to select Pidgin&#8217;s default web browser. Firefox, Galeon, Konqueror, Mozilla, Netscape and Opera are supported natively. The user can also manually enter a command to be executed when a link is clicked (<i>%s</i> expands to the URL). For example, <i>xterm -e lynx &quot;%s&quot;</i> will open the link with lynx. </p>
<dt><code>Open link in</code></p>
<dd> Allows the user to specify whether to use an existing window, a new tab, a new window, or to let the browser to decide what to do when calling the browser to open a link. Which options are available will depend on which browser is selected. </p>
</dl>
<h2>Logging</h2>
<dl>
<dt><code>Log format</code></p>
<dd> Specifies how to log. Pidgin supports HTML and plain text, but plugins can provide other logging methods. </p>
<dt><code>Log all instant messages</code></p>
<dd> When enabled, all IM conversations are logged. This can be overridden on a per-conversation basis in the conversation window. </p>
<dt><code>Log all chats</code></p>
<dd> When enabled, all chat conversations are logged. This can be overridden on a per-conversation basis in the conversation window. </p>
<dt><code>Log all status changes to system log</code></p>
<dd> When enabled, status changes are logged. </p>
</dl>
<h2>Status / Idle</h2>
<dl>
<dt><code>Report idle time</code></p>
<dd> Determines under which conditions to report idle time. <code>Based on keyboard and mouse use</code> uses keyboard and mouse activity to determine idle time. <code>From last sent message</code> uses the time at which the user last sent a message in Pidgin to determine idle. <code>Never</code> disables idle reporting. </p>
<dt><code>Auto-reply</code></p>
<dd> Determines when to send an auto-reply on protocols which support it (currently only AIM). </p>
<dt><code>Change status when idle</code></p>
<dd> When enabled, this uses the <code>Minutes before becoming idle</code> and <code>Change status to</code> preferences described below to set status on idle. </p>
<dt><code>Minutes before becoming idle</code></p>
<dd> Specifies how many minutes of inactivity are required before considering the user to be idle. </p>
<dt><code>Change status to</code></p>
<dd> Specifies which &quot;primitive&quot; or &quot;saved&quot; status to use when setting status on idle. </p>
<dt><code>Use status from last exit at startup</code></p>
<dd> If this is checked, Pidgin will remember what status was active when the user closed Pidgin and restore it at the next run. When disabled, Pidgin will always set the status selected in <code>Status to apply at startup</code> at startup. </p>
<dt><code>Status to apply at startup</code></p>
<dd> When <code>Use status from last exit at startup</code> is disabled, this specifies which &quot;primitive&quot; or &quot;saved&quot; status to use at startup. </p>
</dl>
<h2>CONVERSATIONS</h2>
<p> When starting a new conversation, the user is presented with the <code>Conversation</code> window. The conversation appears in the upper text box and the user types his/her message in the lower text box. Between the two is a row of options, represented by icons. Some or all buttons may not be active if the protocol does not support the specific formatting. From left to right:</p>
<dl>
<dt><code>Font</code></p>
<dd> This menu provides font control options for the current conversation. Size, style, and face may be configured here.</p>
<dt><code>Insert</code></p>
<dd> This menu provides the ability to insert images, horizontal rules, and links where the protocol supports each of these features.</p>
<dt><code>Smile!</code></p>
<dd> Allows the insertion of graphical smileys via the mouse. This button shows the user a dialog with the available smileys for the current conversation. </p>
</dl>
<h2>CHATS</h2>
<p> For protocols that allow it, <code>Chats</code> can be entered through the <i>Buddies</i> menu. </p>
<p> Additional features available in chat, depending on the protocol are:</p>
<dl>
<dt><code>Whisper</code></p>
<dd> The text will appear in the chat conversation, but it will only be visible to the sender and the receiver.</p>
<dt><code>Invite</code></p>
<dd> Invite other people to join the chat room.</p>
<dt><code>Ignore</code></p>
<dd> Ignore anything said by the chosen person</p>
<dt><code>Set Topic</code></p>
<dd> Set the topic of the chat room. This is usually a brief sentence describing the nature of the chat&#8211;an explanation of the chat room&#8217;s name.</p>
<dt><code>Private Message (IM)</code></p>
<dd> Send a message to a specific person in the chat. Messages sent this way will not appear in the chat window, but instead open a new IM conversation. </p>
</dl>
<h2>STATUS MESSAGES</h2>
<p> Most protocols allow for status messages. By using status messages, a user can leave an informative message for others to see. Status and status messages are configured via the status selector at the bottom of the Buddy List window. By default the menu shown here is divided into sections for &quot;primitive&quot; status types, such as <i>Available</i>, <i>Away</i>, etc.; a few &quot;popular&quot; statuses (including &quot;transient&quot; statuses) which have been recently used, and a section which shows <code>New Status&#8230;</code> and <code>Saved Statuses&#8230;</code> options for more advanced status manipulation. </p>
<dl>
<dt><code>Primitive Statuses</code></p>
<dd> A primitive status is a basic status supported by the protocol. Examples of primitive statuses would be Available, Away, Invisible, etc. A primitive status can be used to create a <code>Transient Status or a Saved Status</code>, both explained below. Essentially, primitive statuses are building blocks of more complicated statuses. </p>
<dt><code>Transient Statuses</code></p>
<dd> When one of the statuses from the topmost section of the status selector&#8217;s menu is selected, this creates a transient, or temporary, status. The status will show in the &quot;popular statuses&quot; section in the menu until it has not been used for a sufficiently long time. A transient status may also be created by selecting <i>New Status&#8230;</i> from the status selector&#8217;s menu, then clicking <i>Use</i> once the user has entered the message. </p>
<dt><code>Saved Statuses</code></p>
<dd> Saved statuses are permanent&#8211;once created, they will exist until deleted. Saved statuses are useful for statuses and status messages that will be used on a regular basis. They are also useful for creating complex statuses in which some accounts should always have a different status from others. For example, one might wish to create a status called &quot;Sleeping&quot; that has all accounts set to &quot;Away&quot;, then create another status called &quot;Working&quot; that has three accounts set to &quot;Away&quot; and another account set to &quot;Available.&quot; </p>
<dt><code>New Status Window</code></p>
<dd> When the user selects <i>New Status&#8230;</i> from the status selector menu, Pidgin presents the user with a dialog asking for status-related information. That information is discussed below: </p>
<p> <i>Title</i> &#8211; The name of the status that will appear in the status selctor&#8217;s menu. If the user clicks the <i>Save</i> or <i>Save &amp; Use</i> button, this name will also be shown in the <code>Saved Status Window</code>. The title should be a short description of the status. </p>
<p> <i>Status</i> &#8211; The type of status being created, such as Available, Away, etc. </p>
<p> <i>Message</i> &#8211; The content of the status message. This is what is visible to other users. Some protocols will allow formatting in some status messages; where formatting is not supported it will be stripped to the bare text entered. </p>
<p> <i>Use a different status for some accounts</i> &#8211; This allows the creation of complex statuses in which some accounts&#8217; status differs from that of other accounts. To use this, the user will click the expander to the left of the text, then select individual accounts which will have a different status and/or status message. When the user selects an account, Pidgin will present another status dialog asking for a status and a message just for the selected account. </p>
<dt><code>Saved Status Window</code></p>
<dd> When the user selects <i>Saved Statuses&#8230;</i> from the status selector&#8217;s menu, Pidgin presents a dialog that lists all saved statuses. &quot;Transient&quot; statuses, discussed above, are <i>NOT</i> shown here. This window provides the ability to manage saved statuses by allowing the creation, modification, and deletion of saved statuses. The <i>Use</i>, <i>Modify</i>, and <i>Delete</i> buttons here allow operation on the status selected from the list; the dd button allows creation of a new saved status, and the <i>Close</i> button closes the window. </p>
</dl>
<h2>BUDDY POUNCE</h2>
<p> A Buddy Pounce is an automated trigger that occurs when a buddy returns to a normal state from an away state. The <code>Buddy Pounce</code> dialog box can be activated by selecting the <i>Buddy Pounce</i> option from the <code>Tools</code> menu. From this dialog, new pounces can be created with the <code>Add</code> button and existing pounces can be removed with the <code>Delete</code> button. A pounce can be set to occur on any combination of the events listed, and any combination of actions can result. If <i>Pounce only when my status is not Available</i> is checked, the pounce will occur only if the user is set to a non-available status, such as invisible, do not disturb, away, etc. If <i>Recurring</i> is checked, the pounce will remain until removed by the <code>Delete</code> button. </p>
<h2>CUSTOM SMILIES</h2>
<p> Pidgin 2.5.0 introduced support for custom smilies on those protocols for which interested contributors have developed support. The custom smiley manager can be accessed by selecting <i>Smiley</i> from the <i>Tools</i> menu. From here, custom smilies may be added, edited, or deleted by clicking the <i>Add</i>, <i>Edit</i>, or <i>Delete</i> buttons, respectively. </p>
<p> During a conversation with another user, that user&#8217;s custom smileys may be added to the user&#8217;s own custom smiley list directly from the conversation window by right-clicking the new custom smiley and selecting <i>Add Custom Smiley&#8230;</i> </p>
<h2>PLUGINS</h2>
<p> Pidgin allows for dynamic loading of plugins to add extra functionality to Pidgin. See <i>plugins/HOWTO</i> or <i><a rel="nofollow" href="http://developer.pidgin.im/wiki/CHowTo">http://developer.pidgin.im/wiki/CHowTo</a></i> for information on writing plugins. </p>
<p> The plugins dialog can be accessed by selecting <i>Plugins</i> from the <i>Tools</i> menu. Each plugin available appears in this dialog with its name, version, and a short summary of its functionality. Plugins can be enabled with the checkbox beside the name and short description. More information on the currently selected plugin is available by clicking the expander beside the text <i>Plugin Details</i>. If the selected plugin has preferences or configuration options, the <i>Configure Plugin</i> button will present the plugin&#8217;s preferences dialog. </p>
<h2>PERL</h2>
<p> Pidgin allows for plugins to be written in the perl scripting language. See <i>Perl Scripting HOWTO</i> in the Pidgin documentation for more information about perl scripting. </p>
<h2>TCL</h2>
<p> Pidgin allows for plugins to be written in the Tcl scripting language. See <i>plugins/tcl/TCL-HOWTO</i> for more information about Tcl scripting. </p>
<h2>D-Bus</h2>
<p> Pidgin allows for interaction via D-Bus. Currently very little documentation about this interaction exists. </p>
<h2>FILES</h2>
<p>&nbsp;<wbr>&nbsp;<wbr><i>/usr/bin/pidgin</i>: Pidgin&#8217;s location. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>~/.purple/blist.xml</i>: the buddy list. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>~/.purple/accounts.xml</i>: information about the user&#8217;s accounts. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>~/.purple/pounces.xml</i>: stores the user&#8217;s buddy pounces. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>~/.purple/prefs.xml</i>: Pidgin&#8217;s configuration file. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>~/.purple/status.xml</i>: stores the user&#8217;s away messages. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>~/.purple/logs/PROTOCOL/ACCOUNT/BUDDYNAME/DATE.{html,txt}</i>: conversation logs. </p>
<h2>DIRECTORIES</h2>
<p>&nbsp;<wbr>&nbsp;<wbr><i>/usr/lib/pidgin/</i>: Pidgin&#8217;s plugins directory. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>/usr/lib/purple-2/</i>: libpurple&#8217;s plugins directory. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>~/.purple</i>: users&#8217;&nbsp;<wbr>local settings </p>
<p>&nbsp;<wbr>&nbsp;<wbr><i>~/.purple/plugins/</i>: users&#8217;&nbsp;<wbr>local plugins </p>
<h2>BUGS</h2>
<p> The bug tracker can be reached by visiting <i><a rel="nofollow" href="http://developer.pidgin.im/query">http://developer.pidgin.im/query</a></i> </p>
<p> Before sending a bug report, please verify that you have the latest version of Pidgin. Many bugs (major and minor) are fixed at each release, and if yours is out of date, the problem may already have been solved. </p>
<h2>PATCHES</h2>
<p> If you fix a bug in Pidgin (or otherwise enhance it), please submit a patch (using <code>mtn diff &gt; my.diff</code> against the latest version from the Monotone repository) at <i><a rel="nofollow" href="http://developer.pidgin.im/simpleticket">http://developer.pidgin.im/simpleticket</a></i> </p>
<p> You are also encouraged to drop by at <code>#pidgin</code> on <i>irc.freenode.net</i> to discuss development. </p>
<h2>SEE ALSO</h2>
<p> <i><a rel="nofollow" href="http://pidgin.im/">http://pidgin.im/</a></i><br />
 <i><a rel="nofollow" href="http://developer.pidgin.im/">http://developer.pidgin.im/</a></i><br />
 <code><a href="/docs/linux/man/1-purple-remote/">purple-remote</a></code>(1)<br />
 <code><a href="/docs/linux/man/1-finch/">finch</a></code>(1) </p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <code>WITHOUT ANY WARRANTY</code>; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02111-1301 USA </p>
<h2>AUTHORS</h2>
<p> Pidgin&#8217;s active developers are: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Daniel&nbsp;<wbr>&#8216;datallah&#8217;&nbsp;<wbr>Atallah&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Paul&nbsp;<wbr>&#8216;darkrain42&#8217;&nbsp;<wbr>Aurich&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>John&nbsp;<wbr>&#8216;rekkanoryo&#8217;&nbsp;<wbr>Bailey&nbsp;<wbr>(developer and bugmaster) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Ethan&nbsp;<wbr>&#8216;Paco-Paco&#8217;&nbsp;<wbr>Blanton&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Thomas Butter&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Ka-Hing Cheung&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Sadrul Habib Chowdhury&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Mark&nbsp;<wbr>&#8216;KingAnt&#8217;&nbsp;<wbr>Doliner&nbsp;<wbr>(developer)&nbsp;<wbr>&lt;<i>thekingant [at] users.sourceforge.net</i>&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Sean Egan&nbsp;<wbr>(developer)&nbsp;<wbr>&lt;<i>seanegan [at] gmail.com</i>&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Casey Harkins&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Ivan Komarov </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Gary&nbsp;<wbr>&#8216;grim&#8217;&nbsp;<wbr>Kramlich&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Richard&nbsp;<wbr>&#8216;rlaager&#8217;&nbsp;<wbr>Laager&nbsp;<wbr>(developer)&nbsp;<wbr>&lt;<i>rlaager [at] pidgin.im</i>&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Sulabh&nbsp;<wbr>&#8216;sulabh_m&#8217;&nbsp;<wbr>Mahajan&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Richard&nbsp;<wbr>&#8216;wabz&#8217;&nbsp;<wbr>Nelson&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Christopher&nbsp;<wbr>&#8216;siege&#8217;&nbsp;<wbr>O&#8217;Brien&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Bartosz Oler&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Etan&nbsp;<wbr>&#8216;deryni&#8217;&nbsp;<wbr>Reisner&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Tim&nbsp;<wbr>&#8216;marv&#8217;&nbsp;<wbr>Ringenbach&nbsp;<wbr>(developer)&nbsp;<wbr>&lt;<i>marv_sf [at] users.sf.net</i>&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Michael&nbsp;<wbr>&#8216;Maiku&#8217;&nbsp;<wbr>Ruprecht&nbsp;<wbr>(developer, voice and video) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Elliott&nbsp;<wbr>&#8216;QuLogic&#8217;&nbsp;<wbr>Sales de Andrade&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Luke&nbsp;<wbr>&#8216;LSchiere&#8217;&nbsp;<wbr>Schierer&nbsp;<wbr>(support) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Megan&nbsp;<wbr>&#8216;Cae&#8217;&nbsp;<wbr>Schneider&nbsp;<wbr>(support/QA) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Evan Schoenberg&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Kevin&nbsp;<wbr>&#8216;SimGuy&#8217;&nbsp;<wbr>Stange&nbsp;<wbr>(developer and webmaster) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Will&nbsp;<wbr>&#8216;resiak&#8217;&nbsp;<wbr>Thompson&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Stu&nbsp;<wbr>&#8216;nosnilmot&#8217;&nbsp;<wbr>Tomlinson&nbsp;<wbr>(developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Nathan&nbsp;<wbr>&#8216;faceprint&#8217;&nbsp;<wbr>Walp&nbsp;<wbr>(developer) </p>
<p> Our crazy patch writers include: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Marcus&nbsp;<wbr>&#8216;malu&#8217;&nbsp;<wbr>Lundblad </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Dennis&nbsp;<wbr>&#8216;EvilDennisR&#8217;&nbsp;<wbr>Ristuccia </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Peter&nbsp;<wbr>&#8216;fmoo&#8217;&nbsp;<wbr>Ruibal </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Gabriel&nbsp;<wbr>&#8216;Nix&#8217;&nbsp;<wbr>Schulhof </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Jorge&nbsp;<wbr>&#8216;Masca&#8217;&nbsp;<wbr>Villaseñor </p>
<p> Our artists are: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Hylke Bons&nbsp;<wbr>&lt;<i>h.bons [at] student.rug.nl</i>&gt; </p>
<p> Our retired developers are: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Herman Bloggs&nbsp;<wbr>(win32 port)&nbsp;<wbr>&lt;<i>herman [at] bluedigits.com</i>&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Jim Duchek&nbsp;<wbr>&lt;<i>jim [at] linuxpimps.com</i>&gt;&nbsp;<wbr>(maintainer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Rob Flynn&nbsp;<wbr>&lt;<i>gaim [at] robflynn.com</i>&gt;&nbsp;<wbr>(maintainer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Adam Fritzler&nbsp;<wbr>(libfaim maintainer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Christian&nbsp;<wbr>&#8216;ChipX86&#8217;&nbsp;<wbr>Hammond&nbsp;<wbr>(developer&nbsp;<wbr>&amp;&nbsp;<wbr>webmaster)&nbsp;<wbr>&lt;<i>chipx86 [at] chipx86.com</i>&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Syd Logan&nbsp;<wbr>(hacker and designated driver&nbsp;<wbr>[lazy bum]) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Jim Seymour&nbsp;<wbr>(XMPP developer) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Mark Spencer&nbsp;<wbr>(original author)&nbsp;<wbr>&lt;<i>markster [at] marko.net</i>&gt; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Eric Warmenhoven&nbsp;<wbr>(former lead developer)&nbsp;<wbr>&lt;<i>eric [at] warmenhoven.org</i>&gt; </p>
<p> Our retired crazy patch writers include: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Felipe&nbsp;<wbr>&#8216;shx&#8217;&nbsp;<wbr>Contreras </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Decklin Foster </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Peter&nbsp;<wbr>&#8216;Bleeter&#8217;&nbsp;<wbr>Lawler </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Robert&nbsp;<wbr>&#8216;Robot101&#8217;&nbsp;<wbr>McQueen </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Benjamin Miller </p>
<p> This manpage was originally written by Dennis Ristuccia &lt;<i>dennis [at] dennisr.net</i>&gt;. It has been updated and largely rewritten by Sean Egan &lt;<i>seanegan [at] gmail.com</i>&gt;, Ben Tegarden &lt;<i>tegarden [at] uclink.berkeley.edu</i>&gt;, and John Bailey &lt;<i>rekkanoryo [at] pidgin.im</i>&gt;. </p>
<h2>Index</h2>
