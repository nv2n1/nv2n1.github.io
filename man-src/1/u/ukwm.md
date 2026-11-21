---

title: "ukwm(1)"
name: "ukwm"
section: "1"
letter: "u"
url: "/docs/linux/man/1-ukwm/"
description: "Ukwm – Clutter based compositing GTK2 Window Manager"
---

<p> <code>ukwm</code> [&#8211;display=<i>DISPLAY</i>] [&#8211;replace] [&#8211;sm-client-id=<i>ID</i>] [&#8211;sm-disable] [&#8211;sm-save-file=<i>FILENAME</i>] [&#8211;version] [&#8211;help]</p>
<p> This manual page documents briefly <code>ukwm</code>. </p>
<p> <code>ukwm</code> is a minimal X window manager aimed at nontechnical users and is designed to integrate well with the GNOME desktop. <code>ukwm</code> lacks some features that may be expected by traditional UNIX or other technical users; these users may want to investigate other available window managers for use with GNOME or standalone.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;display=DISPLAY</code></dt>
<dd> Connect to X display <i>DISPLAY</i>.</dd>
<dt><code>&#8211;replace</code></dt>
<dd> a window manager which is running is replaced by <code>ukwm</code>. Users are encouraged to change the GNOME window manager by running the new WM with the &#8211;replace or -replace option, and subsequently saving the session.</dd>
<dt><code>&#8211;sm-client-id=ID</code></dt>
<dd> Specify a session management <i>ID</i>.</dd>
<dt><code>&#8211;sm-disable</code></dt>
<dd> Disable the session management.</dd>
<dt><code>&#8211;sm-save-file=FILENAME</code></dt>
<dd> Load a session from <i>FILENAME</i>.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print the version number.</dd>
<dt><code>-?, &#8211;help</code></dt>
<dd> Show summary of options.</dd></dl>
<h2>CONFIGURATION</h2>
<p> <code>ukwm</code> configuration can be found under <i>Preferences</i>-&gt;<i>Windows</i> and <i>Preferences</i>-&gt;<i>Keyboard Shortcuts</i> on the menu-panel. Advanced configuration can be achieved directly through gsettings.</p>
<h2>SEE ALSO</h2>
<p> <code>ukwm-message</code>(1)</p>
<h2>AUTHOR</h2>
<p> The original manual page was written by Thom May &lt;thom [at] debian.org&gt;. It was updated by Akira TAGOH &lt;tagoh [at] debian.org&gt; for the Debian GNU/Linux system (with permission to use by others), and then updated by Luke Morton and Philip O&#8217;Brien for inclusion in ukwm. </p>
