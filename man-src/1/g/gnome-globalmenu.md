---
title: "gnome-globalmenu(1)"
name: "gnome-globalmenu"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-globalmenu/"
description: "gnome-globalmenu – Global Menu for GNOME"
---

<h2 class="name">NAME</h2>
<p> gnome-globalmenu &#8211; Global Menu for GNOME </p>
<h2>SYNOPSIS</h2>
<p> Global Menu is the globally-shared menu bar of all applications launched in your desktop session.<br />
 Global Menu consists two components:<br />
 &#8211; GTK Plugin (libglobalmenu-gnome.so)<br />
 &#8211; gnome-panel applet (GlobalMenu.PanelApplet). The applet also acts as a window selector.<br />
 On XFCE, a minimal applet (GlobalMenu.XfcePlugin) is also implemented.</p>
<h2>INSTALLATION</h2>
<p> After installation, Add to applet &quot;Global Menu Panel Applet&quot; to the panel, and enable the GTK plugin from the preference dialog of the applet. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The behavior of the applet is fully controlled via the preference dialog. The GTK plugin is affected by </p>
<p> <code>GLOBALMENU_GNOME_ARGS</code><br />
 <code>&#8211;verbose</code> produce a verbose log.<br />
 <code>&#8211;log-file=&lt;file&gt;</code> write the log into &lt;file&gt;.<br />
 <code>&#8211;disable</code> disable Global Menu. </p>
<p> <code>GTK_MENUBAR_NO_MAC</code><br />
 This environment variable constains binary names of the applications for whom the GTK plugin module should be disabled.</p>
<h2>SEE ALSO</h2>
<p> For the complete and up-to-date documentation, please visit <i><a rel="nofollow" href="http://code.google.com/p/gnome2-globalmenu">http://code.google.com/p/gnome2-globalmenu</a></i>. </p>
<p> This manual page was origninal written by Benjamin Marwell &lt;b.marwell [at] gmx.de&gt;, for the Debian project (but may be used by others). Rewritten by Yu Feng &lt;rainwoodman [at] gmail.com&gt; on Feb 22 2009, before integrated into the project. </p>
<h2>Index</h2>
