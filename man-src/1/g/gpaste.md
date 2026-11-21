---

title: "gpaste(1)"
name: "gpaste"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpaste/"
description: "GPaste – A lightweight clipboard manager for the Gnome desktop"
---

<h2>NAME</h2>
<p> GPaste &#8211; A lightweight clipboard manager for the Gnome desktop </p>
<p> <code>[command |] gpaste [options&#8230;]</code> </p>
<p> GPaste is a modular clipboard management system with a fully DBus-based daemon, a <font SIZE="-1">CLI</font> client and a gtk+ tray icon. </p>
<h2>COMMANDS</h2>
<dl>
<dt><code>gpaste [history]</code></dt>
<dd> Display the history with indexes </dd>
<dt><code>gpaste history-size</code></dt>
<dd> Display this size of the history </dd>
<dt><code>gpaste backup-history</code></dt>
<dd> Backup the current history </dd>
<dt><code>gpaste switch-history</code></dt>
<dd> Switch to another history </dd>
<dt><code>gpaste delete-history</code></dt>
<dd> Delete a history </dd>
<dt><code>gpaste list-histories</code></dt>
<dd> List available histories </dd>
<dt><code>gpaste add &lt;text&gt;</code></dt>
<dd> Add the text into the history </dd>
<dt><code>gpaste add-password &lt;name&gt; &lt;password&gt;</code></dt>
<dd> Add the name &#8211; password couple to the history </dd>
<dt><code>gpaste delete-password &lt;name&gt;</code></dt>
<dd> Delete the password &lt;name&gt; </dd>
<dt><code>gpaste set-password &lt;number&gt; &lt;name&gt;</code></dt>
<dd> Mark the &lt;number&gt;th item of the history as being a password named &lt;name&gt; </dd>
<dt><code>gpaste rename-password &lt;old name&gt; &lt;new name&gt;</code></dt>
<dd> Rename the password </dd>
<dt><code>gpaste get &lt;number&gt;</code></dt>
<dd> Get the &lt;number&gt;th item from the history </dd>
<dt><code>gpaste select &lt;number&gt;</code></dt>
<dd> Put the &lt;number&gt;th item of the history into the clipboard </dd>
<dt><code>gpaste delete &lt;number&gt;</code></dt>
<dd> Delete the &lt;number&gt;th item of the history </dd>
<dt><code>gpaste file &lt;path&gt;</code></dt>
<dd> Put the content of the file at &lt;path&gt; into the clipboard </dd>
<dt><code>command | gpaste</code></dt>
<dd> Put the output of the command into the history </dd>
<dt><code>gpaste empty</code></dt>
<dd> Empty the history </dd>
<dt><code>gpaste start</code></dt>
<dd> Start tracking clipboard changes </dd>
<dt><code>gpaste stop</code></dt>
<dd> Stop tracking clipboard changes </dd>
<dt><code>gpaste daemon-reexec</code></dt>
<dd> Reexecute the daemon, for example after upgrading GPaste </dd>
<dt><code>gpaste settings</code></dt>
<dd> Launch the configuration tool </dd>
<dt><code>gpaste version</code></dt>
<dd> Display the version </dd>
<dt><code>gpaste daemon-version</code></dt>
<dd> Display the daemon version </dd>
<dt><code>gpaste help</code></dt>
<dd> Display the help </dd>
<dt><code>gpaste about</code></dt>
<dd> Display the about dialog </dd>
<dt><code>gpaste show-history</code></dt>
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
