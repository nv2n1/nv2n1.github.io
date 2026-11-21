---

title: "appstream-compose(1)"
name: "appstream-compose"
section: "1"
letter: "a"
url: "/docs/linux/man/1-appstream-compose/"
description: "appstream-compose – Generate AppStream metadata"
---

<p> appstream-compose &#8211; Generate AppStream metadata </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>appstream-compose</code> [OPTION&#8230;]</dt></dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>appstream-compose</code> command. </dd>
<p> <code>appstream-compose</code> is a simple app that takes a prefix (default /usr) and a set of application names. It looks for appdata, metainfo, desktop and icon files with that basename in $prefix/share/[appdata|metainfo|applications|icons] and generates appstream xml files and icons in (by default) $prefix/share/app-info.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Richard Hughes &lt;richard [at] hughsie.com&gt;. </p>
