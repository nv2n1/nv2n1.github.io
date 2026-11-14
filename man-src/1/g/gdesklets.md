---
title: "gdesklets(1)"
name: "gdesklets"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gdesklets/"
description: "gDesklets – provides an advanced architecture for desktop applets"
---

<h2 class="name">NAME</h2>
<p> <code>gDesklets</code> &#8211; provides an advanced architecture for desktop applets </p>
<h2>SYNOPSIS</h2>
<p> <code>gdesklets open [ display ]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>gDesklets</code> provides an advanced architecture for desktop applets &#8212; tiny displays sitting on your desktop in a symbiotic relationship of eye candy and usefulness. </p>
<p> Populate your desktop with status meters, icon bars, weather sensors, news tickers&#8230; whatever you can imagine! Virtually anything is possible and maybe even available some day. </p>
<h2>FIRST START</h2>
<p> You can find an entry in the GNOME menu after a successful installation. This will start the gDesklets Shell where you can install and run desktop applets. When you log out or quit &#8216;gDesklets&#8217;, the settings will be remembered for the next session. </p>
<h2>COMMAND LINE TOOL</h2>
<p> The command line tool <code>gdesklets</code> lets you perform all administration tasks from the command line. </p>
<p> Display files can be opened using </p>
<p> <code>$ gdesklets open &lt;displayfile&gt;</code> </p>
<p> If the gdesklets-daemon wasn&#8217;t running, this will start up the daemon as well. You can only have one daemon per X-display. The daemon can be stopped again by calling </p>
<p> <code>$ gdesklets stop</code> </p>
<p> Usage of the command line frontend: </p>
<p> <code>gdesklets [option] &lt;command&gt; [arguments&#8230;]</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&lt;command&gt;: open&nbsp;<wbr>&lt;files&gt;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Opens the given display files)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>start&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Runs the gDesklets daemon)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>stop&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Stops the gDesklets daemon)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Lists open displays)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>restart&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Restarts the gDesklets daemon)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>profile&nbsp;<wbr>&lt;profile&gt;&nbsp;<wbr>(Switches to the given profile)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>profile&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Shows the current and the available<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>profiles)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>shell&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Opens the graphical shell)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>slay&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Kills the daemon &#8212; use in emergency)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>status&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Checks daemon status)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>about&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Prints information about gDesklets)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Prints gDesklets version)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>configure&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Opens the configuration dialog)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Displays this text)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>check&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(Dependency check for python bindings) </p>
<p>&nbsp;<wbr>[option]: &#8211;no-tray-icon&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(disables the systray icon) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>If you don&#8217;t pass a command, the script will fall back to<br />
&nbsp;<wbr>&nbsp;<wbr><code>gdesklets start</code>&nbsp;<wbr>which is the default. </p>
<h2>GDESKLETS-SHELL</h2>
<p> The shell is a graphical frontend for managing your desklets. You can start it either by selecting it from the GNOME menu (Accessories -&gt; gDesklets), by selecting it from the tray icon popup menu, or by calling: </p>
<p> <code>$ gdesklets shell</code> </p>
<p> The shell currently lets you create and switch between profiles, install new desklets and search for desklets. New desklets can be installed by dragging links from your web browser or files from the file manager into its window, or by selecting the menu item <code>&quot;File -&gt; Install package&#8230;&quot;</code>. </p>
<p> Displays (as we call the applets) will usually appear in the top left corner of your screen when you first run them. You can move displays around by pressing and holding down the middle mouse button. &#8216;gDesklets&#8217; will remember the new position of the display for the future. </p>
<h2>USAGE</h2>
<p> If you press the right mouse button over a display, a popup menu will open. It depends on the display what you will see there, but the following items are always available: </p>
<dl>
<dt> <code>Configure desklet</code></p>
<dt>
<dd>
<dd>Opens the configuration dialog for this display. It depends on the display what you can configure.</p>
<dt> <code>Move desklet</code></p>
<dt>
<dd>
<dd>Attaches desklet to cursor for moving it around. Click to release it.</p>
<dt> <code>View Source</code></p>
<dt>
<dd>
<dd>Lets you view the desklet&#8217;s source file (.display).</p>
<dt> <code>Restart desklet</code></p>
<dt>
<dd>
<dd>Restarts this display. This menu item is mainly for sensor debugging.</p>
<dt> <code>Remove desklet</code></p>
<dt>
<dd>
<dd>Removes this display from your desktop.</p>
<dt> <code>About</code></p>
<dt>
<dd>
<dd>Lets you view desklet&#8217;s &quot;About&quot; information, license and readme file. </p>
</dl>
<h2>LOGFILE</h2>
<p> The gdesklets-daemon writes a log file. That file can be found in <code>~/.gdesklets/logs/gdesklets&lt;display&gt;.log</code> where <code>&lt;display&gt; is the name of the X-Display. </p>
<p> You can select the item View log</code> in the popup menu of the tray icon to view the log messages. </p>
<h2>SUPPORTED WINDOW MANAGERS</h2>
<p> In order to run on as many desktops as possible, gDesklets relies on the EWMH specification from freedesktop.org. This specification is respected among many window managers. We currently know of the following EWMH compliant window managers: </p>
<dl>
<dt> <code>* metacity</code></p>
<dt> <code>* xfwm4</code></p>
<dt> <code>* openbox</code></p>
<dt> <code>* enlightenment</code> (&gt;= 0.16.6)</p>
<dt> <code>* fvwm</code> (2.5.x, see <a rel="nofollow" href="http://www.fvwm.org/features.php)">http://www.fvwm.org/features.php)</a></p>
<dt> <code>* sawfish</code></p>
<dt> <code>* kwin</code></p>
<dt> <code>* evilwm</code></p>
<dt> <code>* fluxbox</code> (recent versions)</p>
<dt> <code>* waimea</code></p>
<dt> * &#8230;and certainly some others which we forgot here. </p>
</dl>
<h2>MEMORY CONSUMPTION</h2>
<dd>This is taken seriously. In every release we&#8217;re addressing these issues. Unfortunately, gDesklets is relying on libraries which contain their own bugs or leaks. In some places it&#8217;s possible to create a work-around. Sometimes, we </p>
<p> have to wait until an issue in bugzilla is fixed. gDesklets itself shouldn&#8217;t leak. We&#8217;ve checked the relevant C code to make sure of that. </p>
<p> At startup the program claims approximately 16 MB of RAM. In the future we&#8217;re going to decrease that number. Some people in the GNOME and GTK+ community are also addressing these problems at a lower level (gtk+ and gnome libraries). gDesklets will automatically benefit from these efforts. </p>
<h2>COMMUNITY</h2>
<p> The site &#8216;<a rel="nofollow" href="http://www.gdesklets.de'">http://www.gdesklets.de&#8217;</a> is the place where you can get new desklets or upload your own creations for sharing them with other users. </p>
<p> Discussion and Help <a rel="nofollow" href="http://mail.gnome.org/mailman/listinfo/gdesklets-list">http://mail.gnome.org/mailman/listinfo/gdesklets-list</a> </p>
<p> gDesklets Developer&#8217;s Book (for developing on the gDesklets platform) <a rel="nofollow" href="http://develbook.gdesklets.de">http://develbook.gdesklets.de</a> </p>
<p> A printed reference in German language is available from &#8216;Software &amp; Support Verlag GmbH&#8217;. The book &#8216;Exploring Python&#8217; covers desklet development on 34 pages. </p>
<p> You can meet the &#8216;gDesklets&#8217; developers and other fans on the IRC channel #gdesklets on GIMPnet (irc.gimp.org). </p>
<h2>AUTHOR</h2>
<p> <code>gDesklets</code> was written by </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Martin Grimme&nbsp;<wbr>&lt;martin [at] pycage.de&gt;. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Christian Meyer&nbsp;<wbr>&lt;chrisime [at] gnome.org&gt;. </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Jesse Andrews&nbsp;<wbr>&lt;jdandr2 [at] cs.uky.edu&gt;. </p>
<h2>THANKS</h2>
<p> I&#8217;d like to thank all people who supported (and are still supporting) me so well with &#8216;gDesklets&#8217;. Please complain if I forgot you&#8230; ;) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Christian Meyer &#8212; ideas and sensor programming </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Jesse Andrews &#8212; sensor programming </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Johannes&nbsp;<wbr>&quot;Waldgeist&quot;&nbsp;<wbr>Rebhan &#8212; artwork </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Christian Neumair &#8212; installation </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Sebastien Bacher &#8212; man page and lots of other stuff </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Luke Stroven &#8212; gdesklets.gnomedesktop.org and&nbsp;<wbr>&#8216;gDesklets&#8217;&nbsp;<wbr>forum </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>James Henstridge &#8212; excellent GTK bindings for Python </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Joe Sapp&nbsp;<wbr>&nbsp;<wbr>&#8212; documentation </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Bjoern Koch&nbsp;<wbr>&nbsp;<wbr>&#8212; additional programming, documentation </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Robert Pastierovic&nbsp;<wbr>&nbsp;<wbr>&#8212; additional programming, documentation </p>
<p>&nbsp;<wbr>&nbsp;<wbr>*&nbsp;<wbr>Lauri Kainulainen&nbsp;<wbr>&nbsp;<wbr>&#8212; additional programming, gdesklets website </p>
<h2>BUGS</h2>
<p> If you encounter bugs which are not listed here, please post a bug report at <a rel="nofollow" href="https://launchpad.net/gdesklets/+filebug">https://launchpad.net/gdesklets/+filebug</a> for <code>gDesklets</code>. Please don&#8217;t report useless bug reports, like &quot;gDesklets crashes&quot; without checking the log file first, because that doesn&#8217;t tell us much. Also make sure, that you have all the necessary dependencies installed. </p>
<p> If the log says: &quot;ImportError: No module named X&quot; then you clearly don&#8217;t have the python module &quot;X&quot; installed on your system. We are going to close useless bug reports immediately(!), so please save your time and ours and be smart! </p>
<h2>LICENCE AND DISCLAIMER</h2>
<p> This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the file &#8216;COPYING&#8217; for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this software; if not, write to the </p>
<p> Free Software Foundation, Inc., 59 Temple Place, Suite 390, Boston, MA 02111-1307 USA </p>
<p> This software is provided &quot;as is&quot; and the author is not and cannot be made responsible for any damage resulting from the use of this software. </p>
<h2>COPYRIGHT</h2>
<p> <code>gdesklets</code> is copyright (c) 2003 &#8211; 2007 by</p>
<dl>
<dt> * Martin Grimme &lt;martin [at] pycage.de&gt;,</p>
<dt> * Christian Meyer &lt;chrisime [at] gnome.org&gt;,</p>
<dt> * Jesse Andrews &lt;jdandr2 [at] cs.uky.edu&gt;</p>
<dt> * Benoît Dejean &lt;tazforever [at] dlfp.org&gt;</dl>
<p> <code>glibtop Python wrapper</code> in libdesklets is copyright (c) 2003 &#8211; 2005 by</p>
<dl>
<dt> * Benoît Dejean &lt;tazforever [at] dlfp.org&gt;</dl>
<dd>The latest version of <code>gDesklets</code> can be found at <a rel="nofollow" href="http://www.gdesklets.de/">http://www.gdesklets.de/</a> The <code>Desklets</code> bzr repository can be found at <a rel="nofollow" href="https://code.launchpad.net/gdesklets/">https://code.launchpad.net/gdesklets/</a> </p>
<h2>Index</h2>
