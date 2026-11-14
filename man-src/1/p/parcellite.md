---
title: "parcellite(1)"
name: "parcellite"
section: "1"
letter: "p"
url: "/docs/linux/man/1-parcellite/"
description: "Parcellite – Lightweight GTK+ Clipboard Manager"
---

<h2>NAME</h2>
<p> Parcellite &#8211; Lightweight GTK+ Clipboard Manager</p>
<h2>SYNOPSIS</h2>
<p> <code>parcellite</code> [<i>OPTION</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Parcellite</code> is a lightweight GTK+ clipboard manager. This is a stripped down, basic-features-only clipboard manager with a small memory footprint for those who like simplicity. </p>
<p> <code>Parcellite</code> features a clipboard CLI. Unrecognized options and the contents of your standard input get copied to your clipboard. See <code>CLI EXAMPLES</code>. </p>
<p> <code>Look at the tool tips by hovering over each item in the prefrences dialog.</code></p>
<h2><code>OPTIONS</code></h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show help options</p>
<dt><code>-d</code>, <code>&#8211;daemon</code></p>
<dd> Run as daemon. Use this mode if you just want <code>Parcellite</code> to keep your clipboard and primary contents safe. Daemon mode just restores clipboard contents if it is lost. It does nothing else, no clipboard history, no clipboard synchronization, no icon, no command line interface, or anything other than restoring clipboard content if it becomes empty. It must be run as the first instance, and will disable the command line interface and all other features of <code>parcellite</code>.</p>
<dt><code>-n</code>, <code>&#8211;no-icon</code></p>
<dd> Do not use status icon</p>
<dt><code>-c</code>, <code>&#8211;clipboard</code></p>
<dd> Print clipboard contents <code>-p</code>, <code>&#8211;primary</code> Print primary contents</dl>
<h2>ACTIONS</h2>
<p> <code>Parcellite&#8217;s</code> actions perform commands using the contents of your clipboard. &quot;<code>%s</code>&quot; in the command is replaced with the clipboard contents. Use double quotes &quot;<code>%s</code>&quot; to expand env variables like $HOME to /home/your_name Use single quotes &#8216;%s&#8217; to feed your action with env variables without shell expansion. Use %% if you want a literal %. See the man page for gnuC printf (man 2 printf) for more information.</p>
<h2>CLI EXAMPLES</h2>
<p>&nbsp;<wbr>echo&nbsp;<wbr>&quot;copied to clipboard&quot;&nbsp;<wbr>| parcellite<br />
&nbsp;<wbr>parcellite&nbsp;<wbr>&quot;copied to clipboard&quot;<br />
&nbsp;<wbr>echo&nbsp;<wbr>&quot;copied to clipboard&quot;&nbsp;<wbr>| parcellite -c</p>
<h2>Hotkeys</h2>
<p>&nbsp;<wbr>The available hotkey modifiers are&nbsp;<wbr>&lt;Ctrl&gt;,&nbsp;<wbr>&lt;Alt&gt;&nbsp;<wbr>&lt;Shift&gt;,&nbsp;<wbr>&lt;Release&gt;,&nbsp;<wbr>&lt;Meta&gt;,&nbsp;<wbr>&lt;Super&gt;,&nbsp;<wbr>&lt;Hyper&gt;,&nbsp;<wbr>&lt;Mod[1-5]&gt;</p>
<h2>Preferences</h2>
<p> Right-click on the parcellite icon in the systray to access the preferences. </p>
<h2>Behavior Tab</h2>
<dl>
<dt><code>Clipboards </code></p>
<dd> generally checking all these boxes is appropriate.</p>
<dt><code>History </code></p>
<dd>
&nbsp;<wbr>Check&nbsp;<wbr>&#8216;Save history&#8217;&nbsp;<wbr>to save history on close.<br />
&nbsp;<wbr>&#8216;Position history&#8217;&nbsp;<wbr>&#8211; Set the location where history appears. If unchecked, appears where the mouse is.<br />
&nbsp;<wbr>&#8216;X&#8217;&nbsp;<wbr>&#8211; X location in pixels. 0 is top of screen.<br />
&nbsp;<wbr>&#8216;Y&#8217;&nbsp;<wbr>&#8211; Y location in pixels. 0 is left of screen.<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&#8216;Max Data Size&nbsp;<wbr>(MB)&#8217;&nbsp;<wbr>&#8211; Set Maximum amount of data to copy for each entry in MBytes. 0 is no limit.</p>
<dt><code>Miscellaneous</code></p>
<dd>
&nbsp;<wbr>&#8216;Search As You Type&#8217;&nbsp;<wbr>&#8211; If checked, does a search-as-you-type. Turns red if not found. Goes to top&nbsp;<wbr>(Alt-E)&nbsp;<wbr>line when no chars are entered for search<br />
&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr>&#8216;Case Sensitive Search&#8217;&nbsp;<wbr>&#8211; If checked, does case sensitive search. </p>
<p>&nbsp;<wbr>&#8216;Ignore Whitespace Only&#8217;&nbsp;<wbr>&#8211; If checked, will ignore any clipboard additions that contain only whitespace. </p>
<p>&nbsp;<wbr>&#8216;Trim Whitespace&#8217;&nbsp;<wbr>&#8211; If checked, will trim whitespace from beginning and end of entry. </p>
<p>&nbsp;<wbr>&#8216;Trim Newlines&#8217;&nbsp;<wbr>&#8211; If checked, will replace newlines with spaces. </p>
</dl>
<h2>Display Tab</h2>
<dl>
<dt>
&nbsp;<wbr>&#8216;Show in Single line&#8217;&nbsp;<wbr>does nothing.</p>
<dd>
<dt>
&nbsp;<wbr>&#8216;Show in reverse order&#8217;&nbsp;<wbr>reverses the history so the first entry is last and the last is first.</p>
<dd>
<dt>
&nbsp;<wbr>&#8216;Omit items&#8217;&nbsp;<wbr>refers to omitting characters that don&#8217;t fit in the history window width. This is for display only.</p>
<dd>
</dl>
<h2>History Dialog Behavior</h2>
<dl>
<dt>Use the Ctrl or Shift key in conjunction with right-click.</p>
<dd>
<dt>If you hold Ctrl, then it toggles the delete on a single item.</p>
<dd>
<dt>If you hold Shift while holding down right-click (this is like a right-drag), then it toggles each item as it enters the item.</p>
<dd>
<dt>To complete the delete, hit enter.</p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> Website: <a rel="nofollow" href="http://parcellite.sourceforge.net">http://parcellite.sourceforge.net</a></p>
<h2>AUTHOR</h2>
<p> Written by Gilberto &quot;Xyhthyx&quot; Miralla &lt;xyhthyx [at] gmail.com&gt;. Gilberto is no longer maintaining the project. &#8216;Rickyrockrat&#8217; is his replacement.</p>
<h2>BUGS</h2>
<p> Please include your ~/.config/parcellite/parcelliterc file when filing a bug. This will give me your preferences.<br />
&nbsp;<wbr>Please report any bugs to the bug tracker via this web page:<br />
&nbsp;<wbr><a rel="nofollow" href="http://sourceforge.net/projects/parcellite/support">http://sourceforge.net/projects/parcellite/support</a><br />
&nbsp;<wbr>Click on&nbsp;<wbr>&#8216;Bugs&#8217;&nbsp;<wbr>under&nbsp;<wbr>&#8216;Project Trackers&#8217;&nbsp;<wbr>to file a bug if you are registered with Source Forge. If not, email rickyrockrat (rickyrockrat at users.sourceforge.net), or click the &#8216;project administers&#8217; in the link above. </p>
<h2>Index</h2>
