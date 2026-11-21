---
title: "plymouth(1)"
name: "plymouth"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plymouth/"
description: "plymouth – Send commands to plymouthd"
---

<h2 class="name">NAME</h2>
<p> plymouth &#8211; Send commands to plymouthd </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>plymouth </code><code>[OPTION&#8230;]</code></dt>
<dt> <code>plymouth </code><code>COMMAND&nbsp;[OPTION&#8230;] </code></dt></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>plymouth</code> sends commands to a running <code>plymouthd</code>. This is used during the boot process to control the display of the graphical boot splash.</dd>
<h2>OPTIONS</h2>
<p> The following options are understood. These options are supported for compatibility with the old <code>rhgb-client</code> interface, and have been replaced by the commands that are described in the next section. </p>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show summary of options.</dd></dl>
<p> <code>&#8211;debug</code></p>
<dl>
<dt>
</dt><dd> Enable verbose debug logging.</dd></dl>
<p> <code>&#8211;get-splash-plugin-path</code></p>
<dl>
<dt>
</dt><dd> Get directory where splash plugins are installed.</dd></dl>
<p> <code>&#8211;newroot=</code><code>[STRING]</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd that the new root filesystem is mounted.</dd></dl>
<p> <code>&#8211;quit</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd to quit.</dd></dl>
<p> <code>&#8211;ping</code></p>
<dl>
<dt>
</dt><dd> Check if plymouthd is running.</dd></dl>
<p> <code>&#8211;has-active-vt</code></p>
<dl>
<dt>
</dt><dd> Check if plymouthd has an active vt.</dd></dl>
<p> <code>&#8211;sysinit</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd root filesystem is mounted read-write.</dd></dl>
<p> <code>&#8211;show-splash</code></p>
<dl>
<dt>
</dt><dd> Show the splash screen.</dd></dl>
<p> <code>&#8211;hide-splash</code></p>
<dl>
<dt>
</dt><dd> Hide the splash screen.</dd></dl>
<p> <code>&#8211;ask-for-password</code></p>
<dl>
<dt>
</dt><dd> Ask the user for a password.</dd></dl>
<p> <code>&#8211;ignore-keystroke=</code><code>[STRING]</code></p>
<dl>
<dt>
</dt><dd> Remove sensitivity to a keystroke.</dd></dl>
<p> <code>&#8211;update=</code><code>[STRING]</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd an update about boot progress.</dd></dl>
<p> <code>&#8211;details</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd there were errors during boot.</dd></dl>
<p> <code>&#8211;wait</code></p>
<dl>
<dt>
</dt><dd> Wait for plymouthd to quit.</dd></dl>
<h2>COMMANDS</h2>
<p> The following commands are understood: </p>
<p> <code>change-mode </code><code>OPTION</code></p>
<dl>
<dt>
</dt><dd> Change the operation mode. </dd>
<p> <code>&#8211;boot-up</code></p>
<dl>
<dt>
</dt><dd> Start the system up</dd></dl>
<p> <code>&#8211;shutdown</code></p>
<dl>
<dt>
</dt><dd> Shutting the system up</dd></dl>
<p> <code>&#8211;updates</code></p>
<dl>
<dt>
</dt><dd> Applying updates</dd></dl>
</dl>
<p> <code>system-update </code><code>OPTION</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd about boot progress. </dd>
<p> <code>&#8211;progress=INTEGER</code></p>
<dl>
<dt>
</dt><dd> The percentage progress of the updates</dd></dl>
</dl>
<p> <code>update </code><code>OPTION</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd about boot status changes. </dd>
<p> <code>&#8211;status=STRING</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd the current boot status</dd></dl>
</dl>
<p> <code>update-root-fs </code><code>OPTION</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd about root filesystem changes. </dd>
<p> <code>&#8211;new-root-dir=STRING</code></p>
<dl>
<dt>
</dt><dd> Root filesystem is about to change</dd></dl>
<p> <code>&#8211;read-write</code></p>
<dl>
<dt>
</dt><dd> Root filesystem is no longer read-only</dd></dl>
</dl>
<p> <code>show-splash</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd to show splash screen.</dd></dl>
<p> <code>hide-splash</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd to hide splash screen.</dd></dl>
<p> <code>ask-for-password </code><code>OPTION</code></p>
<dl>
<dt>
</dt><dd> Ask the user for a password. </dd>
<p> <code>&#8211;command=STRING</code></p>
<dl>
<dt>
</dt><dd> Command to send password to via standard input</dd></dl>
<p> <code>&#8211;prompt=STRING</code></p>
<dl>
<dt>
</dt><dd> Message to display when asking for password</dd></dl>
<p> <code>&#8211;number-of-tries=INTEGER</code></p>
<dl>
<dt>
</dt><dd> Number of times to ask before giving up (requires <code>&#8211;command</code>)</dd></dl>
<p> <code>&#8211;dont-pause-progress</code></p>
<dl>
<dt>
</dt><dd> Don&#8217;t pause boot progress bar while asking</dd></dl>
</dl>
<p> <code>ask-question</code></p>
<dl>
<dt>
</dt><dd> Ask the user a question. </dd>
<p> <code>&#8211;command=STRING</code></p>
<dl>
<dt>
</dt><dd> Command to send the answer to via standard input</dd></dl>
<p> <code>&#8211;prompt=STRING</code></p>
<dl>
<dt>
</dt><dd> Message to display when asking the question</dd></dl>
<p> <code>&#8211;dont-pause-progress</code></p>
<dl>
<dt>
</dt><dd> Don&#8217;t pause boot progress bar while asking</dd></dl>
</dl>
<p> <code>display-message </code><code>OPTION</code></p>
<dl>
<dt>
</dt><dd> Display a message. </dd>
<p> <code>&#8211;text=STRING</code></p>
<dl>
<dt>
</dt><dd> The message text</dd></dl>
</dl>
<p> <code>hide-message </code><code>OPTION</code></p>
<dl>
<dt>
</dt><dd> Hide a message. </dd>
<p> <code>&#8211;text=STRING</code></p>
<dl>
<dt>
</dt><dd> The message text</dd></dl>
</dl>
<p> <code>watch-keystroke </code><code>OPTION</code></p>
<dl>
<dt>
</dt><dd> Become sensitive to a keystroke. </dd>
<p> <code>&#8211;command=STRING</code></p>
<dl>
<dt>
</dt><dd> Command to send keystroke to via standard input</dd></dl>
<p> <code>&#8211;keys=STRING</code></p>
<dl>
<dt>
</dt><dd> Keys to become sensitive to</dd></dl>
</dl>
<p> <code>ignore-keystroke </code><code>OPTION</code></p>
<dl>
<dt>
</dt><dd> Remove sensitivity to a keystroke. </dd>
<p> <code>&#8211;keys=STRING</code></p>
<dl>
<dt>
</dt><dd> Keys to remove sensitivity from</dd></dl>
</dl>
<p> <code>pause-progress</code></p>
<dl>
<dt>
</dt><dd> Pause boot progress bar.</dd></dl>
<p> <code>unpause-progress</code></p>
<dl>
<dt>
</dt><dd> Unpause boot progress bar.</dd></dl>
<p> <code>report-error</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd there were errors during boot.</dd></dl>
<p> <code>deactivate</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd to deactivate.</dd></dl>
<p> <code>reactivate</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd to reactivate.</dd></dl>
<p> <code>quit </code><code>OPTION</code></p>
<dl>
<dt>
</dt><dd> Tell plymouthd to quit. </dd>
<p> <code>&#8211;retain-splash</code></p>
<dl>
<dt>
</dt><dd> Don&#8217;t explicitly hide boot splash on exit</dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-grub/">grub</a></code>(8), <code><a href="/docs/linux/man/8-plymouth/">plymouth</a></code>(8), <code><a href="/docs/linux/man/8-plymouthd/">plymouthd</a></code>(8), m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/wiki/Software/Plymouth">http://www.freedesktop.org/wiki/Software/Plymouth</a></code>m[] </p>
