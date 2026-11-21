---

title: "kconfig_compiler(1)"
name: "kconfig_compiler"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kconfig_compiler/"
description: "kconfig_compiler – KDE configuration compiler"
---

<dl>
<dt> <code>kconfig_compiler</code> [Qt-options] [KDE-options] [options] <i>file.kcfg</i> <i>file.kcfgc</i></dt></dl>
<p> <code>kconfig_compiler</code></p>
<dd>generates C++ source code from two files. The first file (.kcfg) contains information about configuration options and the second file (.kcfgc) provides the code generation options. </dd>
<p> The generated source code contains a class based on <code>KConfigSkeleton</code> that provides an API to access the applications configuration data.</p>
<h2>OPTIONS</h2>
<p> <code>Arguments:</code> </p>
<p> <i>file.kcfg</i></p>
<dl>
<dt>
</dt><dd> Input kcfg XML file</dd></dl>
<p> <i>file.kcfgc</i></p>
<dl>
<dt>
</dt><dd> Code generation options file</dd></dl>
<p> <code>Options:</code> </p>
<p> <code>-d, &#8211;directory &lt;dir&gt;</code></p>
<dl>
<dt>
</dt><dd> Directory to generate files in [.]</dd></dl>
<p> <code>Generic options:</code> </p>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show help about options</dd></dl>
<p> <code>&#8211;help-qt</code></p>
<dl>
<dt>
</dt><dd> Show Qt specific options</dd></dl>
<p> <code>&#8211;help-kde</code></p>
<dl>
<dt>
</dt><dd> Show KDE specific options</dd></dl>
<p> <code>&#8211;help-all</code></p>
<dl>
<dt>
</dt><dd> Show all options</dd></dl>
<p> <code>&#8211;author</code></p>
<dl>
<dt>
</dt><dd> Show author information</dd></dl>
<p> <code>-v, &#8211;version</code></p>
<dl>
<dt>
</dt><dd> Show version information</dd></dl>
<p> <code>&#8211;license</code></p>
<dl>
<dt>
</dt><dd> Show license information</dd></dl>
<p> <code>KDE Options:</code> </p>
<p> <code>&#8211;caption &lt;caption&gt;</code></p>
<dl>
<dt>
</dt><dd> Use &#8216;caption&#8217; as name in the titlebar</dd></dl>
<p> <code>&#8211;icon &lt;icon&gt;</code></p>
<dl>
<dt>
</dt><dd> Use &#8216;icon&#8217; as the application icon</dd></dl>
<p> <code>&#8211;miniicon &lt;icon&gt;</code></p>
<dl>
<dt>
</dt><dd> Use &#8216;icon&#8217; as the application icon</dd></dl>
<p> <code>&#8211;config &lt;filename&gt;</code></p>
<dl>
<dt>
</dt><dd> Use alternative configuration file</dd></dl>
<p> <code>&#8211;dcopserver &lt;server&gt;</code></p>
<dl>
<dt>
</dt><dd> Use the DCOP server specified by &#8216;server&#8217;</dd></dl>
<p> <code>&#8211;nocrashhandler</code></p>
<dl>
<dt>
</dt><dd> Disable crash handler to get core dumps</dd></dl>
<p> <code>&#8211;waitforwm</code></p>
<dl>
<dt>
</dt><dd> Waits for a WM_NET compatible windowmanager</dd></dl>
<p> <code>&#8211;style &lt;style&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the application GUI style</dd></dl>
<p> <code>&#8211;geometry &lt;geometry&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the client geometry of the main widget &#8211; see man X for the argument format</dd></dl>
<p> <code>Qt options:</code> </p>
<p> <code>&#8211;display &lt;displayname&gt;</code></p>
<dl>
<dt>
</dt><dd> Use the X-server display &#8216;displayname&#8217;</dd></dl>
<p> <code>&#8211;session &lt;sessionId&gt;</code></p>
<dl>
<dt>
</dt><dd> Restore the application for the given &#8216;sessionId&#8217;</dd></dl>
<p> <code>&#8211;cmap</code></p>
<dl>
<dt>
</dt><dd> Causes the application to install a private color map on an 8-bit display</dd></dl>
<p> <code>&#8211;ncols &lt;count&gt;</code></p>
<dl>
<dt>
</dt><dd> Limits the number of colors allocated in the color cube on an 8-bit display, if the application is using the QApplication::ManyColor color specification</dd></dl>
<p> <code>&#8211;nograb</code></p>
<dl>
<dt>
</dt><dd> Tells Qt to never grab the mouse or the keyboard</dd></dl>
<p> <code>&#8211;sync</code></p>
<dl>
<dt>
</dt><dd> Switches to synchronous mode for debugging</dd></dl>
<p> <code>&#8211;fn, &#8211;font &lt;fontname&gt;</code></p>
<dl>
<dt>
</dt><dd> Defines the application font</dd></dl>
<p> <code>&#8211;bg, &#8211;background &lt;color&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the default background color and an application palette (light and dark shades are calculated)</dd></dl>
<p> <code>&#8211;fg, &#8211;foreground &lt;color&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the default foreground color</dd></dl>
<p> <code>&#8211;btn, &#8211;button &lt;color&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the default button color</dd></dl>
<p> <code>&#8211;name &lt;name&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the application name</dd></dl>
<p> <code>&#8211;title &lt;title&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets the application title (caption)</dd></dl>
<p> <code>&#8211;visual TrueColor</code></p>
<dl>
<dt>
</dt><dd> Forces the application to use a TrueColor visual on an 8-bit display</dd></dl>
<p> <code>&#8211;inputstyle &lt;inputstyle&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets XIM (X Input Method) input style. Possible values are onthespot, overthespot, offthespot, and root</dd></dl>
<p> <code>&#8211;im &lt;XIM server&gt;</code></p>
<dl>
<dt>
</dt><dd> Sets XIM server</dd></dl>
<p> <code>&#8211;noxim</code></p>
<dl>
<dt>
</dt><dd> Disable XIM</dd></dl>
<p> <code>&#8211;reverse</code></p>
<dl>
<dt>
</dt><dd> Mirrors the whole layout of widgets</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a rel="nofollow" href="http://developer.kde.org">http://developer.kde.org</a></code></p>
<dl>
<dt>
</dt><dd> KDE Developer&#8217;s Corner website</dd></dl>
<h2>BUGS</h2>
<p> Please use m[blue]<code>bugs.kde.org</code>m[]<font SIZE="-2">[1]</font> to report bugs, do not mail the authors directly.</p>
<h2>AUTHORS</h2>
<p> <code>Cornelius Schumacher</code> &lt;schumacher [at] kde.org&gt;</p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<p> <code>Waldo Bastian</code> &lt;bastian [at] kde.org&gt;</p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<p> <code>Zack Rusin</code> &lt;zack [at] kde.org&gt;</p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> bugs.kde.org</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://bugs.kde.org">http://bugs.kde.org</a></dd></dl>
</dl>
