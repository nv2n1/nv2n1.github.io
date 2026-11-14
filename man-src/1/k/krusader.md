---
title: "krusader(1)"
name: "krusader"
section: "1"
letter: "k"
url: "/docs/linux/man/1-krusader/"
description: "krusader – advanced twin-panel file manager and FTP client for KDE"
---

<h2 class="name">NAME</h2>
<p> krusader &#8211; advanced twin-panel file manager and FTP client for KDE </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>krusader</code> [KDE Generic Options] [Qt Generic Options] [Options] url</dl>
<h2>DESCRIPTION</h2>
<dd>Krusader is an advanced twin panel (commander style) file manager for KDE and other desktops in the *nix world, similar to Midnight or Total Commander. It provides all the file management features you could possibly want. Plus: extensive archive handling, mounted filesystem support, FTP, advanced search module, viewer/editor, directory synchronisation, file content comparisons, powerful batch renaming and much much more. It supports the following archive formats: ace, arj, bzip2, deb, gzip, iso, lha, rar, rpm, tar, xz, zip, and 7-zip and can handle other KIOSlaves such as smb:// or fish:// It is (almost) completely customizable, very user friendly, fast and looks great on your desktop! :-) You should give it a try.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;left</code> <i>&lt;path&gt;</i></p>
<dl>
<dt>
<dd> start left panel at <i>&lt;path&gt;</i></dl>
<p> <code>&#8211;right</code> <i>&lt;path&gt;</i></p>
<dl>
<dt>
<dd> start right panel at <i>&lt;path&gt;</i></dl>
<p> <code>&#8211;profile </code><i>&lt;panel-profile&gt;</i></p>
<dl>
<dt>
<dd> Load <i>&lt;panel-profile&gt;</i> on startup</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> show the general options</dl>
<p> <code>&#8211;help-all</code></p>
<dl>
<dt>
<dd> show all options</dl>
<p> <code>&#8211;author</code></p>
<dl>
<dt>
<dd> show the authors</dl>
<p> <code>-v, &#8211;version</code></p>
<dl>
<dt>
<dd> show the version</dl>
<p> <code>&#8211;license</code></p>
<dl>
<dt>
<dd> show the license</dl>
<p> <code>url</code></p>
<dl>
<dt>
<dd> if there is already a tab open with that url, it is activated, otherwise a new tab is opened in the active panel</dl>
<h2>QT-OPTIONS</h2>
<p> &quot;$ krusader &#8211;help-qt&quot; shows all Qt-options</p>
<h2>KDE-OPTIONS</h2>
<p> &quot;$ krusader &#8211;help-kde&quot; shows all KDE-options</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> &bull; $ krusader &#8211;left=/mnt/cdrom &#8211;right=<a href="ftp://downloads@myserver.net">ftp://downloads@myserver.net</a></dl>
<dl>
<dt>
<dd> &bull; $ krusader &#8211;left=/home,/usr,<a href="smb://workgroup.net">smb://workgroup.net</a> &#8211;right=<a href="fish://myserver.net">fish://myserver.net</a></dl>
<dl>
<dt>
<dd> &bull; $ krusader &#8211;profile=ftp_managment</dl>
<h2>FILES</h2>
<p> Configuration files: </p>
<p> ~/.kde/share/config/krusaderrc </p>
<p> ~/.kde/share/apps/krusader/krbookmarks.xml </p>
<p> $KDEDIR/share/apps/krusader/krusaderui.rc or </p>
<p> ~/.kde/share/apps/krusader/krusaderui.rc</p>
<h2>PLATFORMS</h2>
<p> All POSIX: Linux, Solaris, All BSD Platforms: FreeBSD, MacOS-X </p>
<p> <i>KDE 2.x</i> </p>
<p> krusader v1.01 stable but there are no planned changes. </p>
<p> <i>KDE 3.x</i> </p>
<p> Krusader v1.01 needs KDElibs 2 </p>
<p> Krusader v1.02 &#8211; 1.40 needs KDElibs 3 </p>
<p> Krusader 1.40 prefers &gt;= KDE 3.2 </p>
<p> Krusader v1.50 &#8211; v1.51: KDE 3.2 &#8211; KDE 3.3 </p>
<p> Krusader v1.60.0- v1.70.0: KDE 3.3 &#8211; KDE 3.4 </p>
<p> Krusader 1.70.x-1.80.x: KDE 3.4 &#8211; KDE 3.5 </p>
<p> <i>KDE 4.x</i> </p>
<p> Krusader 2.xx.x: KDE 4 </p>
<p> The latest version of Krusader can be found at the Krusader website.</p>
<h2>FEATURES</h2>
<p> OFM filemanager features. </p>
<p> Strong keyboard orientation. </p>
<p> Powerful internal viewer and editor. </p>
<p> Advanced search module that can search in archives. Supports: ace, arj, bzip2, deb, gzip, iso, lha, rar, rpm, tar, xz, zip, and 7-zip. </p>
<p> Directory comparison and filtering. </p>
<p> FTP/Samba client with a connection manager with SFTP/SCP support. </p>
<p> Synchronizer, UserActions, Embedded console. </p>
<p> Compare files by content. Easy editing of file permissions. </p>
<p> Diskusage, Calculate occupied space. Checksum creation-verification. </p>
<p> Fully MIME type-aware (with or without magic!). </p>
<p> Mountmanager, Locate, Krename support. </p>
<p> Root mode, Tabbed panels, PopUp Panel. Mouse selection modes. </p>
<p> Profiles for: Panels, Key-bindings, Colors. </p>
<p> For more features read m[blue]<code><a rel="nofollow" href="http://docs.kde.org/development/en/extragear-utils/krusader/features.html">http://docs.kde.org/development/en/extragear-utils/krusader/features.html</a></code>m[]</p>
<h2>LICENSE</h2>
<p> Krusader is distributed under the terms of the GNU General Public License. </p>
<p> License version 2 as published by the Free Software Foundation. </p>
<p> See the built-in help for details on the License and the lack of warranty. </p>
<p> The copyright for the project and its name are still held by Shie Erlich and Rafi Yanai.</p>
<h2>I18N</h2>
<p> Krusader is translated into many languages. </p>
<p> m[blue]<code><a rel="nofollow" href="http://l10n.kde.org/stats/gui/trunk-kde4/po/krusader.po/">http://l10n.kde.org/stats/gui/trunk-kde4/po/krusader.po/</a></code>m[] </p>
<p> Read the m[blue]<code>KDE translation howto</code>m[]<font SIZE="-2">[1]</font> if you want translate Krusader in your native language.</p>
<h2>FAQ</h2>
<p> The latest version of the KRUSADER FAQ can be found m[blue]<code>here</code>m[]<font SIZE="-2">[2]</font>.</p>
<h2>SEE ALSO</h2>
<p> The Krusader Handbook, at the krusader help menu. </p>
<p> The Krusader homepage on the World Wide Web: </p>
<p> m[blue]<code><a rel="nofollow" href="http://krusader.org">http://krusader.org</a></code>m[]</p>
<h2>AUTHORS</h2>
<p> Krusader is developed by a dedicated team of individuals, known as the Krusader Krew. </p>
<p> Shie Erlich, author [erlich {*} users {.} sourceforge {.} net] </p>
<p> Rafi Yanai, author [yanai {*} users {.} sourceforge {.} net] </p>
<p> Dirk Eschler, Webmaster and i18n coordinator [deschler {*} users {.} sourceforge {.} net] </p>
<p> Csaba Karai, Developer [ckarai {*} users {.} sourceforge {.} net] </p>
<p> Heiner Eichmann, Developer [h {.} eichmann {*} gmx.de] </p>
<p> Jonas Baehr, Developer [jonas.baehr {*} web.de] </p>
<p> Vaclav Juza, Developer [vaclavjuza {*} seznam {.} cz] </p>
<p> Jan Lepper, Developer [jan_lepper {*} gmx{.} de] </p>
<p> Frank Schoolmeesters, Documentation &amp; Marketing Coordinator [frank_schoolmeesters {*} yahoo {.} com] </p>
<p> Richard Holt, Documentation &amp; Proofing [richard {.} holt {*} gmail {.} com] </p>
<p> Matej Urbancic, Marketing &amp; Product Research [matej {*} amis {.} net] </p>
<p> The project is written using KDevelop and Qt Designer.</p>
<h2>BUGS</h2>
<p> See the TODO file in the distribution for information on what remains to be done. </p>
<p> For fixes, patches and comments use the krusader forum or mail to </p>
<p> [krusader-devel {*} googlegroups {.} com]. </p>
<p> Krusader Krew</p>
<h2>AUTHOR</h2>
<p> <code>Krusader Krew</code> &lt;krusader-devel [at] googlegroups.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> KDE translation howto</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://l10n.kde.org/docs/translation-howto/">http://l10n.kde.org/docs/translation-howto/</a></dl>
<dt> 2.</p>
<dd> here</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://docs.kde.org/development/en/extragear-utils/krusader/faq.html">http://docs.kde.org/development/en/extragear-utils/krusader/faq.html</a></dl>
</dl>
<h2>Index</h2>
