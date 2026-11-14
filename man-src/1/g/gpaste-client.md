---
title: "gpaste-client(1)"
name: "gpaste-client"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpaste-client/"
description: "GPaste – A lightweight clipboard manager for the Gnome desktop"
---

<h2>NAME</h2>
<p> GPaste &#8211; A lightweight clipboard manager for the Gnome desktop </p>
<h2>SYNOPSIS</h2>
<p> <code>[command |] gpaste-client [options&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> GPaste is a modular clipboard management system with a fully DBus-based daemon, a <font SIZE="-1">CLI</font> client and a gtk+ tray icon. </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>gpaste-client [history]</code></p>
<dd> Display the history with indexes </p>
<dt><code>gpaste-client history-size</code></p>
<dd> Display this size of the history </p>
<dt><code>gpaste-client get-history</code></p>
<dd> Get the name of the current history </p>
<dt><code>gpaste-client backup-history</code></p>
<dd> Backup the current history </p>
<dt><code>gpaste-client switch-history</code></p>
<dd> Switch to another history </p>
<dt><code>gpaste-client delete-history</code></p>
<dd> Delete a history </p>
<dt><code>gpaste-client list-histories</code></p>
<dd> List available histories </p>
<dt><code>gpaste-client add &lt;text&gt;</code></p>
<dd> Add the text into the history </p>
<dt><code>gpaste-client add-password &lt;name&gt; &lt;password&gt;</code></p>
<dd> Add the name &#8211; password couple to the history </p>
<dt><code>gpaste-client delete-password &lt;name&gt;</code></p>
<dd> Delete the password &lt;name&gt; </p>
<dt><code>gpaste-client set-password &lt;number&gt; &lt;name&gt;</code></p>
<dd> Mark the &lt;number&gt;th item of the history as being a password named &lt;name&gt; </p>
<dt><code>gpaste-client rename-password &lt;old name&gt; &lt;new name&gt;</code></p>
<dd> Rename the password </p>
<dt><code>gpaste-client get &lt;number&gt;</code></p>
<dd> Get the &lt;number&gt;th item from the history </p>
<dt><code>gpaste-client select &lt;number&gt;</code></p>
<dd> Put the &lt;number&gt;th item of the history into the clipboard </p>
<dt><code>gpaste-client replace &lt;number&gt; &lt;contents&gt;</code></p>
<dd> Replace the contents of the &lt;number&gt;th item of the history with the provided one </p>
<dt><code>gpaste-client merge [&#8211;decoration|-d &lt;string&gt;] [&#8211;separator|-s &lt;string&gt;] &lt;number&gt; … &lt;number&gt;</code></p>
<dd> Merge the &lt;number&gt;th items of the history and put the result in the clipboard<br />
 If foo bar and baz are respectively index 1 3 and 4 in history and you run<br />
 gpaste-client merge -d &#8216;&quot;&#8217; -s &#8216;,&#8217; 1 3 4<br />
 You will end up with &quot;foo&quot;,&quot;bar&quot;,&quot;baz&quot; in your clipboard </p>
<dt><code>gpaste-client delete &lt;number&gt;</code></p>
<dd> Delete the &lt;number&gt;th item of the history </p>
<dt><code>gpaste-client file &lt;path&gt;</code></p>
<dd> Put the content of the file at &lt;path&gt; into the clipboard </p>
<dt><code>command | gpaste-client</code></p>
<dd> Put the output of the command into the history </p>
<dt><code>gpaste-client empty</code></p>
<dd> Empty the history </p>
<dt><code>gpaste-client start</code></p>
<dd> Start tracking clipboard changes </p>
<dt><code>gpaste-client stop</code></p>
<dd> Stop tracking clipboard changes </p>
<dt><code>gpaste-client upload &lt;number&gt;</code></p>
<dd> Upload the &lt;number&gt;th item to a pastebin service </p>
<dt><code>gpaste-client ui</code></p>
<dd> Launch the graphical tool </p>
<dt><code>gpaste-client daemon-reexec</code></p>
<dd> Reexecute the daemon, for example after upgrading GPaste </p>
<dt><code>gpaste-client settings</code></p>
<dd> Launch the configuration tool </p>
<dt><code>gpaste-client version</code></p>
<dd> Display the version </p>
<dt><code>gpaste-client daemon-version</code></p>
<dd> Display the daemon version </p>
<dt><code>gpaste-client help</code></p>
<dd> Display the help </p>
<dt><code>gpaste-client about</code></p>
<dd> Display the about dialog </p>
<dt><code>gpaste-client show-history</code></p>
<dd> Make the applet or extension display the history </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;oneline</code></p>
<dd> Display each item on one line, without new lines </p>
<dt><code>&#8211;raw</code></p>
<dd> Display the item raw (without index) </p>
<dt><code>&#8211;zero</code></p>
<dd> Use NUL character instead of new lines between each item </p>
</dl>
<h2>Index</h2>
