---
title: "zonetab2pot(1)"
name: "zonetab2pot"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zonetab2pot/"
description: "zonetab2pot.py – Converts a timezone list to a PO file template."
---

<h2>NAME</h2>
<p> zonetab2pot.py &#8211; Converts a timezone list to a PO file template.</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>zonetab2pot.py</code> [<i>timezone-list</i>] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>zonetab2pot.py</code> reads the timezone list given on the command-line and converts it to a gettext message file (PO-file) template containing the names of the individual timezones. </p>
<dd>The given timezone list should be in the same format as the system zone.tab. If no timezone list is specified on the command-line, <i>/usr/share/zoneinfo/zone.tab</i> will be used. </p>
<p> The new PO-file template will be written to standard output. </p>
<p> This utility is part of the KDE Software Development Kit. </p>
<h2>AUTHORS</h2>
<p> zonetab2pot.py was written by Lukas Tinkl&lt;lukas [at] kde.org&gt; </p>
<p> This manual page was prepared by Ben Burton&lt;bab [at] debian.org&gt; </p>
<h2>AUTHOR</h2>
<p> Ben Burton. </p>
<h2>Index</h2>
