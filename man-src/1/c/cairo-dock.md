---
title: "cairo-dock(1)"
name: "cairo-dock"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cairo-dock/"
description: "cairo-dock – A dock to launch your programs easily."
---

<h2 class="name">NAME</h2>
<p> cairo-dock &#8211; A dock to launch your programs easily.</p>
<h2>SYNOPSIS</h2>
<p> <code>cairo-dock</code> [options] </p>
<h2>DESCRIPTION</h2>
<p> <code>Cairo-Dock</code> is a pretty, light and convenient interface to your desktop, able to replace advantageously your system panel! </p>
<p> It features <code>multi-docks, taskbar, launchers</code> and a lot of useful <code>applets.</code><br />
 <code>Applets</code> can be detached from the dock to act as desktop <code>widgets.</code><br />
 Numerous ready-to-use <code>themes</code> are downloadable in 1 click, and can be easily customized at your convenience.<br />
 It can use <code>hardware acceleration</code> (OpenGL) to be very fast and low on CPU. </p>
<p> It&#8217;s recommended to install the PLUG-INS package ( <code>cairo-dock-plug-ins</code> ) to have access to more views, dialogues and many plug-ins and applets. </p>
<p> Some <code>screenshots</code> are available : </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://pics.glx-dock.org">http://pics.glx-dock.org</a> </p>
<p> <code>Development site:</code> </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://launchpad.net/cairo-dock">https://launchpad.net/cairo-dock</a> </p>
<h2>OPTIONS</h2>
<p> You can launch <code>Cairo-Dock</code> with several options :<br />
 (Note : you can use these options in one block. For example : cairo-dock -oia )</p>
<dl>
<dt><code>-c, &#8211;cairo</code></p>
<dd> Force Cairo backend. Use this option if you have issue with the OpenGL mode.</p>
<dt><code>-o, &#8211;opengl</code></p>
<dd> Force OpenGL backend. Cairo-Dock with OpenGL/Hardware acceleration.</p>
<dt><code>-O, &#8211;indirect-opengl</code></p>
<dd> Use OpenGL backend with indirect rendering. There are very few case where this option should be used.</p>
<dt><code>-A, &#8211;ask-backend</code></p>
<dd> Ask again on startup which backend to use.</p>
<dt><code>-l, &#8211;log [option]</code></p>
<dd> Log verbosity (options : debug, message, warning, critical, error &#8211; default is &#8216;warning&#8217;).<br />
 For example : cairo-dock -l debug</p>
<dt><code>-F, &#8211;colors</code></p>
<dd> Force to display some output messages with colors even if these messages are not displayed into a tty.</p>
<dt><code>-w, &#8211;wait</code></p>
<dd> Wait for N seconds before starting. This is useful if you notice some problems when the dock starts with the session.</p>
<dt><code>-a, &#8211;keep-above</code></p>
<dd> Force to keep the dock above other windows.</p>
<dt><code>-s, &#8211;no-sticky</code></p>
<dd> Don&#8217;t make the dock appear on all desktops.</p>
<dt><code>-e, &#8211;env</code></p>
<dd> Force the dock to consider this environment (gnome, xfce, etc.) &#8211; it may crash the dock if not set properly.</p>
<dt><code>-d, &#8211;dir</code></p>
<dd> Force the dock to load the configuration in this directory (default is ~/.config/cairo-dock).</p>
<dt><code>-m, &#8211;maintenance</code></p>
<dd> Allow to edit the config before the dock is started and show the config panel on startup.</p>
<dt><code>-x, &#8211;exclude</code></p>
<dd> Exclude a given plug-in from activating (it is still loaded though).</p>
<dt><code>-f, &#8211;safe-mode</code></p>
<dd> Don&#8217;t load any plug-ins and show the theme manager on startup.</p>
<dt><code>-W, &#8211;metacity-workaround</code></p>
<dd> Work around some bugs in Metacity Window-Manager (invisible dialogs or sub-docks)</p>
<dt><code>-M, &#8211;modules-dir</code></p>
<dd> Ask the dock to load additional modules contained in this directory (though it is unsafe for your dock to load unofficial modules).</p>
<dt><code>-T, &#8211;testing</code></p>
<dd> For debugging purpose only. The crash manager will not be started to hunt down the bugs.</p>
<dt><code>-E, &#8211;easter-eggs</code></p>
<dd> For debugging purpose only. Some hidden and still unstable options will be activated.</p>
<dt><code>-S, &#8211;server</code></p>
<dd> Address of a server containing additional themes. This will overwrite the default server address.</p>
<dt><code>-k, &#8211;locked</code></p>
<dd> Lock the dock so that any modification is impossible for users. </p>
</dl>
<h2>OTHER</h2>
<p> Some other options with an output in the terminal :</p>
<dl>
<dt><code>-v, &#8211;version</code></p>
<dd> Print version and quit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show the help and quit.</p>
<dt><code>-C, &#8211;capuccino</code></p>
<dd> Cairo-Dock makes anything, including coffee ! </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.config/cairo-dock/</code></p>
<dd> Your config files are saved in this repertory. You can use &#8216;-d&#8217; option to change it.</p>
<dt><code>/usr/share/cairo-dock/</code></p>
<dd> Data files for Cairo-Dock.</p>
<dt><code>/usr/lib/cairo-dock/</code></p>
<dd> Binary files for Cairo-Dock and its plug-ins. </p>
</dl>
<h2>AUTHOR</h2>
<p> Most of the <code>Cairo-Dock</code> project was written by <code>Fabrice Rey</code> (fabounet) &lt;fabounet [at] glx-dock.org&gt;. </p>
<p> The <code>Cairo-Dock Team</code> is currently formed by <code>Fabounet</code> (Fabrice Rey) and <code>Matttbe</code> (Matthieu Baerts).<br />
 With the help of <code>Eduardo Mucelli</code> for our third-party applets. </p>
<p> Thanks to our former developers: <code>Mav</code> (Yann Sladek), <code>Tofe</code> (Christophe Chapuis), <code>Nochka85</code> (Yann Dulieu), <code>ChanGFu</code> (Rémy Robertson), <code>Paradoxxx Zero</code> (Florian Mounier), <code>Necropotame</code> (Adrien Pilleboue), <code>Rom1</code> (Romain Perol), <code>Ctaf</code> , <code>Augur</code> and <code>SQP</code> as well as numerous beta testers and contributors: lylambda, taiebot65, Franksuse64, ppmt, etc. see the &#8216;About&#8217; menu in the dock and this web page. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://glx-dock.org/userlist_messages.php">http://glx-dock.org/userlist_messages.php</a> </p>
<p> Don&#8217;t hesitate to contribute to this project ;)<br />
 Please have a look at this wiki page: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://glx-dock.org/ww_page.php?p=How%20to%20help%20us">http://glx-dock.org/ww_page.php?p=How%20to%20help%20us</a> </p>
<p> This manual page was started by Julien Lavergne &lt;julien.lavergne [at] gmail.com&gt;, for the Debian project (but may be used by others).<br />
 Updated by Matthieu Baerts (matttbe) &lt;matttbe [at] gmail.com&gt;. </p>
<h2>BUGS</h2>
<p> Your bug is maybe a <code>recurrent problem</code> (black background, window at startup (use -c or -o), problem with OpenGL, etc.). Please go to: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://www.glx-dock.org/ww_page.php?p=Recurrents%20problems">http://www.glx-dock.org/ww_page.php?p=Recurrents%20problems</a> </p>
<p> For any other bugs, you can post them on Cairo-Dock forum: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="http://forum.glx-dock.org">http://forum.glx-dock.org</a><br />
 or on Launchpad </p>
<p>&nbsp;<wbr>&nbsp;<wbr><a rel="nofollow" href="https://bugs.launchpad.net/cairo-dock">https://bugs.launchpad.net/cairo-dock</a> </p>
<h2>WEBSITE</h2>
<p> &lt; <code><a rel="nofollow" href="http://glx-dock.org">http://glx-dock.org</a></code> &gt; </p>
<h2>Index</h2>
