---
title: "libquvi-scripts-0-9(7)"
name: "libquvi-scripts-0-9"
section: "7"
letter: "l"
url: "/docs/linux/man/7-libquvi-scripts-0-9/"
description: "libquvi-scripts – Overview of the library scripts"
---

<p>libquvi-scripts &#8211; Overview of the library scripts</p>
<h2>Description</h2>
<p>libquvi-scripts contains the Lua scripts for libquvi that it uses to parse the different properties, such as the media properties.</p>
<h2>Types</h2>
<h3>Common scripts</h3>
<p>The common scripts are modules that may be loaded from other scripts, e.g. the <i><a href="/docs/linux/man/7-quvi-modules/">quvi-modules</a>(7)</i>. </p>
<p> These scripts are typically installed at</p>
<dl>
<dd>$prefix/share/libquvi-scripts/$major_ver.$minor_ver/common/</dl>
<h3>Media scripts</h3>
<p>The media scripts are responsible for parsing the media properties, e.g. the media stream URLs. There is usually a media script for each supported website. </p>
<p> These scripts are typically installed at</p>
<dl>
<dd>$prefix/share/libquvi-scripts/$major_ver.$minor_ver/media/</dl>
<h3>Playlist scripts</h3>
<p>The playlist scripts are responsible for parsing the playlist properties. There is usually a playlist script for each supported website. </p>
<p> These scripts are typically installed at</p>
<dl>
<dd>$prefix/share/libquvi-scripts/$major_ver.$minor_ver/playlist/</dl>
<h3>Scan scripts</h3>
<p>The scan scripts are used to scan an URL for embedded media URLs. </p>
<p> These scripts are typically installed at</p>
<dl>
<dd>$prefix/share/libquvi-scripts/$major_ver.$minor_ver/scan/</dl>
<h3>Subtitlte scripts</h3>
<p>The subtitle scripts are responsible for retrieving subtitle data for the media as well as exporting the data to another format, e.g. SubRip. </p>
<p> These scripts are typically installed at</p>
<dl>
<dd>$prefix/share/libquvi-scripts/$major_ver.$minor_ver/subtitle/ $prefix/share/libquvi-scripts/$major_ver.$minor_ver/subtitle/export/</dl>
<h3>Utility scripts</h3>
<p>The utility scripts are used by libquvi to perform misc. tasks, such as parsing file extension from a content-type, or converting HTML entities to UTF-8 characters. </p>
<p> These scripts are typically installed at</p>
<dl>
<dd>$prefix/share/libquvi-scripts/$major_ver.$minor_ver/util/</dl>
<h2>Environment</h2>
<p>LIBQUVI_SCRIPTS_VERBOSE</p>
<dl>
<dd>When defined, enables the output from any libquvi scripts using the debug facility (<i>quvi/debug</i> module).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-libquvi/">libquvi</a></code>(3), <code><a href="/docs/linux/man/1-quvi/">quvi</a></code>(1)</p>
<h2>Further Resources</h2>
<p>Home</p>
<dl>
<dd><a rel="nofollow" href="http://quvi.sourceforge.net/">http://quvi.sourceforge.net/</a></dl>
<p> Development code</p>
<dl>
<dd><a href="git://repo.or.cz/libquvi-scripts.git">git://repo.or.cz/libquvi-scripts.git</a></dl>
<p> gitweb</p>
<dl>
<dd><a rel="nofollow" href="http://repo.or.cz/w/libquvi-scripts.git">http://repo.or.cz/w/libquvi-scripts.git</a></dl>
<h2>Authors</h2>
<p>Toni Gundogdu &lt;legatvs [at] gmail.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to the quvi-devel mailing list &lt;quvi-devel [at] lists.sourceforge.net&gt; where the development and the maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>License</h2>
<p>libquvi-scripts is Free Software licensed under the GNU Affero GPLv3+</p>
<h2>Libquvi-Scripts</h2>
<p>Part of the <i><a href="/docs/linux/man/7-libquvi-scripts/">libquvi-scripts</a>(7)</i> suite</p>
