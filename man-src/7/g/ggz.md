---
title: "ggz(7)"
name: "ggz"
section: "7"
letter: "g"
url: "/docs/linux/man/7-ggz/"
description: "ggz – The GGZ Gaming Zone"
---

<p>ggz &#8211; The GGZ Gaming Zone</p>
<h2>Description</h2>
<p>The GGZ Gaming Zone is a standards-conforming free online gaming infrastructure which provides many applications and games to people who like to play on the internet or in local networks. GGZ, how the (recursive) acronym is called, is available for many computer systems. This document focuses on the installations on Linux, BSD and Unix. On such systems, GGZ-powered games often ship with the KDE and GNOME games packages, and most distributors also include all components as released by the GGZ project.</p>
<h2>Applications</h2>
<p>GGZ is available on several platforms. A multitude of programs is available to the user, and even more which operate on the system level or are used by developers and administrators. Users will most likely want to connect to a GGZ server on the internet, such as <i><a href="ggz://live.ggzgamingzone.org">ggz://live.ggzgamingzone.org</a></i>, to play games against other people. <i>Core clients</i> are used to perform this task. Functional clients exist in the form of <code>kggz</code> for the K Desktop Environment (KDE), <code>ggz-gtk</code> for GNOME or XFCE users, and <code>ggz-txt</code> for people who prefer command-line applications. Of course, the clients are not bound to a specific desktop, but the choices above will likely be influenced by the level of integration. In particular, the GNOME client is often found embedded in GGZ-enabled games of the GNOME project. A client under development is the SDL-based <code>víbora</code>. Furthermore, a Java-based client and applet exists as well. Running <code>ggz</code> will automatically select a suitable core client depending on the desktop environment. </p>
<p> Special clients exist in the form of <code>ggzap</code>, a quick-launcher for the KDE panel, and <code>ggz-wrapper</code> which is used for launching GGZ games from the command line and instant messenger applications.</p>
<h2>Games</h2>
<p>Games are usually launched by the GGZ server, with corresponding game clients running on the user&#8217;s desktop. Plenty of games are available for GGZ, most of them coming from the GGZ project itself but several independent game projects do now provide GGZ support. Game clients are implemented using multiple toolkits, some of which stem from certain desktop environments. However, all games work equally well under all desktops, it&#8217;s just a matter of personal choice which of them are to be installed &#8211; having all of them is just fine. </p>
<p> While some GGZ game clients are suited for online gaming only, others also run locally like normal games happen to do. Those will be found in the desktop&#8217;s application menu.</p>
<h2>Files</h2>
<p>The following layout can vary from site to site, depending on the completeness of a GGZ installation and the operating system distribution in use. It adheres to the File Hierarchy Standard (FHS) as much as possible.</p>
<dl>
<dt>/usr/bin</p>
<dd>GGZ applications, tools, and the games which provide single player mode.</p>
<dt>/usr/lib/ggz(d)</p>
<dd>GGZ game clients and servers.</p>
<dt>/usr/share/ggz(d)</p>
<dd>Data files for game clients and servers.</p>
<dt>/etc/ggz.modules</p>
<dd>Game module registry for game clients.</p>
<dt>/etc/ggzd</p>
<dd>Configuration for the GGZ server, including rooms and game types.</dl>
<h2>Conforming To</h2>
<p><i>GGZ Design Document</i>, available at <i><a rel="nofollow" href="http://www.ggzgamingzone.org/docs/design/">http://www.ggzgamingzone.org/docs/design/</a></i> </p>
<p> <i>GGZ Main Client-Server Protocol Reference</i>, available at <i><a rel="nofollow" href="http://www.ggzgamingzone.org/docs/design/mainspec/">http://www.ggzgamingzone.org/docs/design/mainspec/</a></i> </p>
<p> <i>GGZ Client-Client Protocol Reference</i>, available at <i><a rel="nofollow" href="http://www.ggzgamingzone.org/docs/design/clientspec/">http://www.ggzgamingzone.org/docs/design/clientspec/</a></i> </p>
<p> <i>GGZ Server-Server Protocol Reference</i>, available at <i><a rel="nofollow" href="http://www.ggzgamingzone.org/docs/design/serverspec/">http://www.ggzgamingzone.org/docs/design/serverspec/</a></i> </p>
<p> <i>GGZ URI specification</i> </p>
<p> Freedesktop.org specifications for desktop integration of games and applications, more information at <i><a rel="nofollow" href="http://www.freedesktop.org/">http://www.freedesktop.org/</a></i> </p>
<p> File Hierarchy Standard for unix-derived operating systems, at <i><a rel="nofollow" href="http://www.pathname.com/fhs/">http://www.pathname.com/fhs/</a></i></p>
<h2>Authors</h2>
<p>The GGZ Development Team &lt;ggz-dev [at] mail.ggzgamingzone.org&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/6-kggz/">kggz</a>(6), <a href="/docs/linux/man/6-ggz-gtk/">ggz-gtk</a>(6), <a href="/docs/linux/man/6-ggz-txt/">ggz-txt</a>(6), <a href="/docs/linux/man/6-ggz-java/">ggz-java</a>(6) </p>
