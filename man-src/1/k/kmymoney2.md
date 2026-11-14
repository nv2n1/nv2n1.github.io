---
title: "kmymoney2(1)"
name: "kmymoney2"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kmymoney2/"
description: "KMyMoney – the personal finances manager for KDE"
---

<h2>NAME</h2>
<p> KMyMoney &#8211; the personal finances manager for KDE</p>
<h2>SYNOPSIS</h2>
<p> <code>kmymoney2</code> [<i>Qt-options</i>] [<i>KDE-options</i>] [<i>File</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>KMyMoney</code> KDE Application. This manual page was written for the Debian GNU/Linux distribution because the original program does not have a manual page. </p>
<p> <code>KMyMoney</code> is the Personal Finance Manager for the KDE environment. It provides the functions required to balance your checkbooks, manage your personal loans and categorise your incomes and expenses using a checkbook style graphical user interface.</p>
<h2>OPTIONS</h2>
<h3>Arguments:</h3>
<dl>
<dt>File</p>
<dd> file to open</dl>
<h3>Generic options:</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show help about options</p>
<dt><code>&#8211;help-qt</code></p>
<dd> Show Qt specific options</p>
<dt><code>&#8211;help-kde</code></p>
<dd> Show KDE specific options</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all options</p>
<dt><code>&#8211;author</code></p>
<dd> Show author information</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Show version information</p>
<dt><code>&#8211;license</code></p>
<dd> Show license information</p>
<dt><code>&#8212;</code></p>
<dd> End of options</dl>
<h3>KDE options</h3>
<dl>
<dt><code>&#8211;caption</code><i>&nbsp;<wbr>caption</i></p>
<dd> Use <i>caption</i> as name in the titlebar.</p>
<dt><code>&#8211;icon</code><i>&nbsp;<wbr>icon</i></p>
<dd> Use <i>icon</i> as the application icon. <i>icon</i> is the name of the icon, which can either be an absolute filename path, or otherwise the icon is sought for in places according to the normal KDE rules.</p>
<dt><code>&#8211;miniicon</code><i>&nbsp;<wbr>icon</i></p>
<dd> Use <i>icon</i> as the icon in the titlebar. <i>icon</i> is the filename of the icon, according to the same rules as for the &#8211;icon parameter.</p>
<dt><code>&#8211;config</code><i>&nbsp;<wbr>filename</i></p>
<dd> Use an alternative configuration file, instead of the default, which is normally located in <i>/usr/share/config</i> or in $<code>KDEHOME</code><i>/share/config</i></p>
<dt><code>&#8211;dcopserver</code><i>&nbsp;<wbr>server</i></p>
<dd> Set the address of the DCOP server to attach to.</p>
<dt><code>&#8211;nocrashhandler</code></p>
<dd> Disable crash handler, to get core dumps. This option has the same effect as definiting the environment variable KDE_DEBUG.</p>
<dt><code>&#8211;waitforwm</code></p>
<dd> Waits for a WM_NET compatible windowmanager.</p>
<dt><code>&#8211;style</code><i>&nbsp;<wbr>style</i></p>
<dd> sets the application GUI style.</p>
<dt><code>&#8211;geometry</code><i>&nbsp;<wbr>geometry</i></p>
<dd> sets the client geometry of the main widget. The geometry parameter follows the normal X convention for geometry, which is on the form:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> [<i>width</i><code>x</code><i>height</i>][{<code>+-</code>}<i>xpos</i>{<code>+-</code>}<i>ypos</i>] Where <i>width</i> and <i>height</i> gives the desired minimum width and height, of the main application window. Both in pixels. A value of 0 specifies the default size. The optional <i>xpos</i> and <i>ypos</i> specifies the x,y-position that which is desired for the application window. Specifying negative values for x or y implies that the x or y position is to be measured from the left or bottom screen edge, instead of as in the normal case, with positive values, from the left and top edges.</dl>
</dl>
</dl>
<h3>Qt options</h3>
<dl>
<dt><code>&#8211;display</code><i>&nbsp;<wbr>displayname</i></p>
<dd> Use the X-server display <i>displayname</i>.</p>
<dt><code>&#8211;session</code><i>&nbsp;<wbr>sessionId</i></p>
<dd> Restore the application for the given <i>sessionId</i>.</p>
<dt><code>&#8211;cmap</code></p>
<dd> Causes the application to install a private color map on an 8-bit display.</p>
<dt><code>&#8211;ncols</code><i>&nbsp;<wbr>count</i></p>
<dd> Limits the number of colors allocated in the color cube on an 8-bit display, if the application is using the QApplication::ManyColor color specification.</p>
<dt><code>&#8211;nograb</code></p>
<dd> Tells Qt to never grab the mouse or the keyboard.</p>
<dt><code>&#8211;dograb</code></p>
<dd> Running under a debugger can cause an implicit <code>-nograb</code>, use <code>-dograb</code> to override.</p>
<dt><code>&#8211;sync</code></p>
<dd> switches to synchronous mode for debugging.</p>
<dt><code>&#8211;fn</code>, &#8211;font<i>&nbsp;<wbr>fontname</i></p>
<dd> Defines the default application font. The <i>fontname</i> should be in the X logical font name description format XLFD. For a full description of the format see <i>/usr/X11R6/lib/X11/doc/xlfd.TXT</i> Note that the application might override the font specified with its own font.</p>
<dt><code>&#8211;bg</code>, <code>&#8211;background</code><i>&nbsp;<wbr>color</i></p>
<dd> Sets the default background color and an application palette (light and dark shades are calculated).</p>
<dt><code>&#8211;fg</code>, <code>&#8211;foreground</code><i>&nbsp;<wbr>color</i></p>
<dd> Sets the default foreground color.</p>
<dt><code>&#8211;btn</code>,<i></i><code>&#8211;button color</code></p>
<dd> Sets the default button color.</p>
<dt><code>&#8211;name</code><i>&nbsp;<wbr>name</i></p>
<dd> Sets the application name.</p>
<dt><code>&#8211;title</code><i>&nbsp;<wbr>title</i></p>
<dd> Sets the application title. This option might, or might not appear in the title bar caption, depending on the application. To change the caption, use the <code>&#8211;caption</code> option instead.</p>
<dt><code>&#8211;visual TrueColor</code></p>
<dd> Forces the application to use a TrueColor visual on an 8-bit display.</p>
<dt><code>&#8211;inputstyle</code><i>&nbsp;<wbr>inputstyle</i></p>
<dd> Sets XIM (X Input Method) input style. Possible values are <code>onthespot</code>, <code>overthespot</code>, <code>offthespot</code>and<code>root</code>.</p>
<dt><code>&#8211;im</code><i> XIM-server</i></p>
<dd> Set XIM server.</p>
<dt><code>&#8211;noxim</code></p>
<dd> Disable XIM.</p>
<dt><code>&#8211;reverse</code></p>
<dd> Mirror reverses the whole layout of widgets. This means that menus will go in the opposite direction, the scroll bar will be on the opposite side, etc. For a normal western layout that means that menus and tool bars will go from the right edge to the left, the vertical scroll bar will be on the left side and so on. </p>
</dl>
<h2>ENVIRONMENT</h2>
<h3>standard KDE environment variables</h3>
<dl>
<dt>KDE_LANG</p>
<dd> Language locale setting to use. This option makes it possible to set another language environment for a program than what is the default. The correct language pack for this language has to be installed for this option to work. The default language when there is none set is en_US. When deciding upon a language, the following resources are looked up, in order: KDE_LANG, configuration file, LC_CTYPE, LC_MESSAGES, LC_ALL, LANG.</p>
<dt>KDE_UTF8_FILENAMES</p>
<dd> Assume that all filenames are in UTF-8 format regardless of the current language setting. Otherwise the filename format is defined by the language.</p>
<dt>KDE_MULTIHEAD</p>
<dd> If this variable has the value <code>true</code> multihead multiple display mode is enabled. The KDE display will be shared over more than one screen.</p>
<dt>DISPLAY</p>
<dd> Specifies the X display to run KDE on.</p>
<dt>KDESYCOCA</p>
<dd> Specifies and alternative path for the <i>ksycoca</i> KDE system configuration cache file. The default path is /tmp/kde-$USER/ksycoca</p>
<dt>DCOPSERVER</p>
<dd> Specifies an alternative path for the DCOP server file. The default file is $HOME/.DCOPserver_<i>hostname</i>_<i>displayname</i></p>
<dt>SESSION_MANAGER</p>
<dd> The session manager to use. This option is set automatically by KDE and is a network path to the session manager socket.</p>
<dt>HOME</p>
<dd> Path to the home directory for the current user.</p>
<dt>KDEHOME</p>
<dd> The KDE per-user setting directory. Default if not specified is <i>$HOME/.kde</i></dl>
<h2>AUTHOR</h2>
<p> <code>KMyMoney</code> was written by </p>
<p> Michael Edwardes &lt;mte [at] users.sourceforge.net&gt;,<br />
 Felix Rodriguez &lt;frodriguez [at] users.sourceforge.net&gt;,<br />
 John C &lt;tacoturtle [at] users.sourceforge.net&gt;,<br />
 Thomas Baumgart &lt;ipwizard [at] users.sourceforge.net&gt;,<br />
 Kevin Tambascio &lt;ktambascio [at] users.sourceforge.net&gt; and<br />
 Arni Ingimundarson &lt;arniing [at] users.sourceforge.net&gt;. </p>
<p> Please use</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://sourceforge.net/tracker/?group_id=4708">http://sourceforge.net/tracker/?group_id=4708</a></code></dl>
<p> to report bugs and post support or feature requests.<br />
 <code>Do not mail the authors directly.</code> </p>
<p> This manual page was prepared by Karolina Lindqvist &lt;pgd-karolinali [at] algonet.se&gt; for the Debian GNU/Linux system (but may be used by others) and has been enhanced by Thomas Baumgart &lt;ipwizard [at] users.sourceforge.net&gt; to reflect the latest changes in development.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>KMyMoney</code> is maintained as a docbook manual. If the <code>khelpcenter</code> program is properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>khelpcenter help:/kmymoney2</code></dl>
<p> should give you access to the complete manual. Alternatively the manual can be browsed in <code>konqueror</code> giving it the URL <code>help:/kmymoney2</code> </p>
<h2>Index</h2>
