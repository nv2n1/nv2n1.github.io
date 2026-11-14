---
title: "mmg(1)"
name: "mmg"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mmg/"
description: "mmg – a GUI for"
---

<h2 class="name">NAME</h2>
<p> mmg &#8211; a GUI for <code></p>
<p><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1) including a chapter and a header editor</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mmg</code> [[&#8211;edit-headers&nbsp;<wbr>{filename.mkv}] | [preferences-file.mmg] | [source-file.ext]]</dl>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-mmg/">mmg</a></code>(1)</p>
<dd>is a wxWindows(TM) based GUI for <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1). It offers easy access to all of <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1)&#8217;s options. All settings (e.g. source files, track options etc) can be saved and restored. Included is a chapter editor that can read OGM style and XML style chapter files, write XML style chapter files and even read chapters from Matroska(TM) files and write chapters directly to Matroska(TM) files. Included is also a header editor that can be used to quickly change properties of existing Matroska(TM) files without needing a complete remux. </p>
<p> <code><a href="/docs/linux/man/1-mmg/">mmg</a></code>(1) knows few options. The first possibility is to start it with a single file name. If that file name&#8217;s extenion is &#8216;.mmg&#8217; then it will be treated as a preferences file and <code><a href="/docs/linux/man/1-mmg/">mmg</a></code>(1) will load its setting when it starts. Otherwise the name is interpreted as being the name of an input file which will be added. </p>
<p> The second operation mode is invoked with the option <code>&#8211;edit-headers</code> and a file name. This lets <code><a href="/docs/linux/man/1-mmg/">mmg</a></code>(1) run its header editor and load the file. </p>
<p> The full documentation is available in HTML form (doc/mkvmerge-gui.html).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mkvmerge/">mkvmerge</a></code>(1), <code><a href="/docs/linux/man/1-mkvextract/">mkvextract</a></code>(1), <code><a href="/docs/linux/man/1-mkvinfo/">mkvinfo</a></code>(1), <code><a href="/docs/linux/man/1-mkvpropedit/">mkvpropedit</a></code>(1)</p>
<h2>WWW</h2>
<p> The latest version can always be found at m[blue]<code>the MKVToolNix homepage</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>AUTHOR</h2>
<p> <code>Moritz Bunkus</code> &lt;moritz [at] bunkus.org&gt;</p>
<dl>
<dt>
<dd> Developer</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> the MKVToolNix homepage</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.bunkus.org/videotools/mkvtoolnix/">http://www.bunkus.org/videotools/mkvtoolnix/</a></dl>
</dl>
<h2>Index</h2>
