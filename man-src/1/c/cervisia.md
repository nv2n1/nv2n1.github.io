---

title: "cervisia(1)"
name: "cervisia"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cervisia/"
description: "Cervisia – Graphical CVS frontend"
---

<p> Cervisia &#8211; Graphical CVS frontend</p>
<h2>SYNOPSIS</h2>
<p> <code>cervisia</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;display</code>&nbsp;<wbr><i>display</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;caption</code>&nbsp;<wbr><i>caption</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;icon</code>&nbsp;<wbr><i>icon</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;miniicon</code>&nbsp;<wbr><i>miniicon</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;config</code>&nbsp;<wbr><i>filename</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;dcopserver</code>&nbsp;<wbr><i>server</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;nocrashhandler</code>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;waitforwm</code>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;style</code>&nbsp;<wbr><i>style</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;geometry</code>&nbsp;<wbr><i>geometry</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;resolve</code>&nbsp;<wbr><i>filename</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;log</code>&nbsp;<wbr><i>filename</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><code>&#8211;annotate</code>&nbsp;<wbr><i>filename</i>&nbsp;<wbr>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[&nbsp;<wbr><i>directory</i>&nbsp;<wbr>]</p>
<h2>DESCRIPTION</h2>
<p> Cervisia is a graphical user interface for the Concurrent Versions System. It is based on the <font SIZE="-1">KDE</font> libraries and therefore shares their Look&#8217;n&#8217;Feel, configuration and help system.</p>
<h2>OPTIONS</h2>
<p> Cervisia accepts the following options:</p>
<dl>
<dt><i>directory</i></dt>
<dd> Tells Cervisia to open the sandbox in <i>directory</i> at startup</dd>
<dt><code>&#8211;resolve</code> <i>filename</i></dt>
<dd> Shows a resolve dialog for the given file</dd>
<dt><code>&#8211;log</code> <i>filename</i></dt>
<dd> Shows a log dialog for the given file</dd>
<dt><code>&#8211;annotate</code> <i>filename</i></dt>
<dd> Shows a annotation dialog for the given file</dd>
<dt><code>&#8211;caption</code> <i>caption</i></dt>
<dd> Sets the caption, i. e. what is shown in the title bar</dd>
<dt><code>&#8211;icon</code> <i>icon</i></dt>
<dd> Sets the program&#8217;s icon (used by window managers and panels)</dd>
<dt><code>&#8211;miniicon</code> <i>miniicon</i></dt>
<dd> Sets the program&#8217;s mini icon (used by window managers and panels)</dd>
<dt><code>&#8211;config</code> <i>filename</i></dt>
<dd> Uses the given file for the configuration</dd>
<dt><code>&#8211;dcopserver</code> <i>server</i></dt>
<dd> Sets the dcopserver the program should use</dd>
<dt><code>&#8211;nocrashhandler</code></dt>
<dd> Disables the crash handler. Use this to get core dumps</dd>
<dt><code>&#8211;waitforwm</code></dt>
<dd> Waits for a <font SIZE="-1">WM_NET</font> compatible windowmanager</dd>
<dt><code>&#8211;style</code> <i>style</i></dt>
<dd> Sets the application <font SIZE="-1">GUI</font> style</dd>
<dt><code>&#8211;geometry</code> <i>geometry</i></dt>
<dd> Sets the geometry of the main window</dd></dl>
<h2>FILES</h2>
<p> <i>_KDECONFDIR_/cervisiarc</i> &#8211; global configuration file </p>
<p> <i>$HOME/.kde/share/config/cervisiarc</i> &#8211; user-specific configuration file</p>
<h2>SEE ALSO</h2>
<p> <i>_KDEHTMLDIR_/en/cervisia/index.html</i> </p>
<p> <i><a href="/docs/linux/man/1-cvs/">cvs</a></i>(1) </p>
<p> <i><a rel="nofollow" href="http://cervisia.kde.org/">http://cervisia.kde.org/</a></i></p>
<h2>AUTHOR</h2>
<p> Cervisia was originally developed by Bernd Gehrmann and is now maintained by Christian Loose &lt;christian.loose [at] kdemail.net&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs at <a rel="nofollow" href="http://bugs.kde.org.">http://bugs.kde.org.</a> </p>
