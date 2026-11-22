---

title: "gpaste-client(1)"
name: "gpaste-client"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpaste-client/"
description: "GPaste – A lightweight clipboard manager for the Gnome desktop"
---

<p> GPaste &#8211; A lightweight clipboard manager for the Gnome desktop </p>
<h2>SYNOPSIS</h2>
<p> <code>[command |] gpaste-client [options&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> GPaste is a modular clipboard management system with a fully DBus-based daemon, a CLI client and a gtk+ tray icon. </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>gpaste-client [history]</code></dt>
<dd> Display the history with indexes </dd>
<dt><code>gpaste-client history-size</code></dt>
<dd> Display this size of the history </dd>
<dt><code>gpaste-client get-history</code></dt>
<dd> Get the name of the current history </dd>
<dt><code>gpaste-client backup-history</code></dt>
<dd> Backup the current history </dd>
<dt><code>gpaste-client switch-history</code></dt>
<dd> Switch to another history </dd>
<dt><code>gpaste-client delete-history</code></dt>
<dd> Delete a history </dd>
<dt><code>gpaste-client list-histories</code></dt>
<dd> List available histories </dd>
<dt><code>gpaste-client add &lt;text&gt;</code></dt>
<dd> Add the text into the history </dd>
<dt><code>gpaste-client add-password &lt;name&gt; &lt;password&gt;</code></dt>
<dd> Add the name &#8211; password couple to the history </dd>
<dt><code>gpaste-client delete-password &lt;name&gt;</code></dt>
<dd> Delete the password &lt;name&gt; </dd>
<dt><code>gpaste-client set-password &lt;number&gt; &lt;name&gt;</code></dt>
<dd> Mark the &lt;number&gt;th item of the history as being a password named &lt;name&gt; </dd>
<dt><code>gpaste-client rename-password &lt;old name&gt; &lt;new name&gt;</code></dt>
<dd> Rename the password </dd>
<dt><code>gpaste-client get &lt;number&gt;</code></dt>
<dd> Get the &lt;number&gt;th item from the history </dd>
<dt><code>gpaste-client select &lt;number&gt;</code></dt>
<dd> Put the &lt;number&gt;th item of the history into the clipboard </dd>
<dt><code>gpaste-client replace &lt;number&gt; &lt;contents&gt;</code></dt>
<dd> Replace the contents of the &lt;number&gt;th item of the history with the provided one </dd>
<dt><code>gpaste-client merge [&#8211;decoration|-d &lt;string&gt;] [&#8211;separator|-s &lt;string&gt;] &lt;number&gt; … &lt;number&gt;</code></dt>
<dd> Merge the &lt;number&gt;th items of the history and put the result in the clipboard<br/>
 If foo bar and baz are respectively index 1 3 and 4 in history and you run<br/>
 gpaste-client merge -d &#8216;&quot;&#8217; -s &#8216;,&#8217; 1 3 4<br/>
 You will end up with &quot;foo&quot;,&quot;bar&quot;,&quot;baz&quot; in your clipboard </dd>
<dt><code>gpaste-client delete &lt;number&gt;</code></dt>
<dd> Delete the &lt;number&gt;th item of the history </dd>
<dt><code>gpaste-client file &lt;path&gt;</code></dt>
<dd> Put the content of the file at &lt;path&gt; into the clipboard </dd>
<dt><code>command | gpaste-client</code></dt>
<dd> Put the output of the command into the history </dd>
<dt><code>gpaste-client empty</code></dt>
<dd> Empty the history </dd>
<dt><code>gpaste-client start</code></dt>
<dd> Start tracking clipboard changes </dd>
<dt><code>gpaste-client stop</code></dt>
<dd> Stop tracking clipboard changes </dd>
<dt><code>gpaste-client upload &lt;number&gt;</code></dt>
<dd> Upload the &lt;number&gt;th item to a pastebin service </dd>
<dt><code>gpaste-client ui</code></dt>
<dd> Launch the graphical tool </dd>
<dt><code>gpaste-client daemon-reexec</code></dt>
<dd> Reexecute the daemon, for example after upgrading GPaste </dd>
<dt><code>gpaste-client settings</code></dt>
<dd> Launch the configuration tool </dd>
<dt><code>gpaste-client version</code></dt>
<dd> Display the version </dd>
<dt><code>gpaste-client daemon-version</code></dt>
<dd> Display the daemon version </dd>
<dt><code>gpaste-client help</code></dt>
<dd> Display the help </dd>
<dt><code>gpaste-client about</code></dt>
<dd> Display the about dialog </dd>
<dt><code>gpaste-client show-history</code></dt>
<dd> Make the applet or extension display the history </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;oneline</code></dt>
<dd> Display each item on one line, without new lines </dd>
<dt><code>&#8211;raw</code></dt>
<dd> Display the item raw (without index) </dd>
<dt><code>&#8211;zero</code></dt>
<dd> Use NUL character instead of new lines between each item </dd>
</dl>
