---
title: "ispell-autobuildhash(8)"
name: "ispell-autobuildhash"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ispell-autobuildhash/"
description: "ispell-autobuildhash – Autobuilding the ispell hash file for some dicts"
---

<p>ispell-autobuildhash &#8211; Autobuilding the ispell hash file for some dicts</p>
<h2>Synopsis</h2>
<pre> ispell-autobuildhash [--force]
 Options:
 --debug Show some extra ispell-autobuildhash information.
 --dry-run Show what would be done, but do nothing real.
 --force Rebuild the hash file for all dicts providing a
 compat file skipping the test.
 --triggered Tell the script that is run in the triggers stage.</pre>
<h2>Description</h2>
<p><code>ispell-autobuildhash</code> is a script that will manage ispell hash files autobuild, intended to be called from the dictionaries-common tools. Depending on the ispell compatibility level and on the compatibility level used for the hash file if present, will decide whether it must be rebuilt or not. This script will only work on ispell packages prepared to use it, it will do nothing for other ispell dict packages.</p>
<h2>Options</h2>
<pre> --debug Show some extra ispell-autobuildhash information.
 --dry-run Show what would be done, but do nothing real.
 --force Rebuild the hash file for all dicts providing a compat
 file regardless of the compatibility levels found.
 --triggered Tell the script that is run in the triggers stage. When
 run under dpkg control, do not try to set the
 'ispell-autobuildhash' trigger, but run real
 B&lt;ispell-autobuildhash&gt; code. When not run under dpkg
 control, real code will always be run and '--triggered'
 option has no real effect.</pre>
<h2>Package Maintainers</h2>
<p>To use this system, <code>ispell-autobuildhash</code> expects a <i></i>$dict<i>.compat</i> file in <i>/var/lib/ispell</i> (<i></i>$dict<i></i> stands for the hash or affix file basename) containing ispell major or compatibility version for last successful build or &#8220;0&#8221; or en empty file if hash is to be rebuild, as is for dictionary installation and upgrades. </p>
<p> When upgrading <code>ispell</code>, script will check if version in <i></i>$dict<i>.compat</i> is different from <i>ispell.compat</i> and rebuild if so, updating <i></i>$dict<i>.compat</i> with the new value. The particular way things are done depends on whether your dict has a single source or a multiple source like ipolish has. </p>
<p> The most common case is having a single source. In this case you must put the <i></i>$dict<i>.aff</i> file at <i>/usr/lib/ispell/$dict.aff</i> as usual and the munched wordlist compressed with gzip at <i>/usr/share/ispell/$dict.mwl.gz</i>. </p>
<p> This script supports the way ipolish allows selection of subdictionaries to be put in the hash file. It will detect the presence of the main language .desc file and call update-ipolish-hash as appropriate. </p>
<p> Although this script looks for the existence of a update-ispell-hash script with supposedly similar functionality to update-ipolish-hash, this latter does not really exists, although it might be added at some time to ispell or to the dictionaries-common system, if enough demand is found. </p>
<p> If your package provides more than one ispell dictionary you will need to do the steps above for each dictionary. </p>
<p> Dictionaries-common scripts will call internally this script and create a hash file at <i>/var/lib/ispell/$dict.hash</i>. You must set a symlink to that file from <i>/usr/lib/ispell/$dict.hash</i>. </p>
<p> Ispell dictionary packages using this script must make sure that <i></i>$dict<i>.compat</i> is reset on every new install/upgrade, so hash is rebuilt. They must also make sure that <i></i>$dict<i>.compat</i> and <i>/var/lib/ispell/$dict.hash</i> are removed on package removal </p>
<p> As of version <tt>1.10</tt>, <code>installdeb-ispell</code> script will understand <tt>'auto-compat'</tt> field in <i></i>$dict<i>.info-ispell</i> file to help with this by adding needed debhelper snippets. Put in that entry the base name(s) of your compat file(s) and check resulting maintainer scripts after build. </p>
<p> Note that you are no longer suggested to ship empty files at <i>/var/lib/ispell/$dict.compat</i> and <i>/var/lib/ispell/$dict.hash</i> to help with reset/removal of those files, but explicitly create/update them on install and explicitly remove them on removal. </p>
<p> <code>ispell</code> maintainer should also call this script from package postinst. When comparing versions it will get the ispell version from file <i>/usr/share/ispell/ispell.compat</i>, or if it does not exists, from the upstream version as given in the first line of &#8216;<code>ispell -vv</code> output.</p>
<h2>Author</h2>
<p>Agustin Martin &lt;agmartin [at] debian.org&gt;</p>
<h2>Copyright</h2>
<p>Copyright (C) 2003-2013 Agustin Martin &lt;agmartin [at] debian.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
