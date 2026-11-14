---
title: "ibus(1)"
name: "ibus"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibus/"
description: "ibus – command line utility for ibus"
---

<h2 class="name">NAME</h2>
<p> <code>ibus</code> &#8211; command line utility for ibus</p>
<h2>SYNOPSIS</h2>
<p> <code>ibus</code> <i>COMMAND</i> [<i>OPTION</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> IBus is an Intelligent Input Bus. It is a new input framework for Linux OS. It provides full featured and user friendly input method user interface. It also may help developers to develop input method easily. </p>
<p> <code>ibus</code> is a command line utility which can restart or exit ibus-daemon, get or set the current ibus engine or list the ibus engines. </p>
<p> Homepage: <a rel="nofollow" href="https://github.com/ibus/ibus/wiki">https://github.com/ibus/ibus/wiki</a> </p>
<h2>COMMAND</h2>
<dl>
<dt><code>help</code></p>
<dd> Show the commands list.</p>
<dt><code>engine</code> [<code>ENGINE_NAME</code>]</p>
<dd> Show the curent ibus engine when <code>ENGINE_NAME</code> is not given. Set <code>ENGINE_NAME</code> to the current ibus engine.</p>
<dt><code>exit</code></p>
<dd> Exit ibus-daemon.</p>
<dt><code>list-engine</code></p>
<dd> Show ibus engines list.</p>
<dt><code>restart</code></p>
<dd> Restart ibus-daemon.</p>
<dt><code>version</code></p>
<dd> Show the ibus version.</p>
<dt><code>read-cache</code> [<code>&#8211;system|&#8211;file=FILE</code>]</p>
<dd> Show the content of the user registry cache if <code>&#8211;system</code> is not given. Show the content of the system registry cache if <code>&#8211;system</code> is given. Show the content of the custom registry cache <code>FILE</code> if <code>&#8211;file=FILE</code> is given.</p>
<dt><code>write-cache</code> [<code>&#8211;system|&#8211;file=FILE</code>]</p>
<dd> Save the user registry cache if <code>&#8211;system</code> is not given. Save the system registry cache if <code>&#8211;system</code> is given. Save the custom registry cache <code>FILE</code> if <code>&#8211;file=FILE</code> is given. </p>
<p> By default, it reads the component XML files from the standard component directory (<i>/usr/share/ibus/component</i>), you can set <i>IBUS_COMPONENT_PATH</i> environment variable for custom component directories, separated by &#8216;:&#8217;.</p>
<dt><code>address</code></p>
<dd> Show the D-Bus address of ibus-daemon.</p>
<dt><code>read-config</code></p>
<dd> Print the setting values in a gsettings configuration file.</p>
<dt><code>reset-config</code></p>
<dd> Reset the user setting values to the default ones in a gsettings configuration file.</p>
<dt><code>watch</code></p>
<dd> Under construction.</p>
<dt><code>emoji</code> [<code>&#8211;font=FONT|&#8211;lang=LANG|&#8211;help|&#8211;partial-match</code>]</p>
<dd> Launch IBus Emojier ( <code>ibus-emoji (1)</code> ) and save the selected emoji to your clipboard. Can choose an emoji font with <code>&#8211;font</code> option. Can choose a language of emoji annotations with <code>&#8211;lang</code> option. If LANG=&quot;en&quot;, IBus Emojier loads /usr/share/ibus/dicts/emoji-en.dict . <code>&#8211;partial-match</code> option enables to match annotations with a partial string. These settings are available with <code>ibus-setup (1)</code> utility. </p>
</dl>
<h2>BUGS</h2>
<p> If you find a bug, please report it at <a rel="nofollow" href="https://github.com/ibus/ibus/issues">https://github.com/ibus/ibus/issues</a> </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-ibus-emoji/">ibus-emoji</a></code>(7) </p>
<h2>Index</h2>
