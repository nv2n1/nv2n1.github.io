---
title: "aspell-autobuildhash(8)"
name: "aspell-autobuildhash"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aspell-autobuildhash/"
description: "aspell-autobuildhash – Autobuilding aspell hash files for some dicts"
---

<p>aspell-autobuildhash &#8211; Autobuilding aspell hash files for some dicts</p>
<h2>Synopsis</h2>
<pre> aspell-autobuildhash [--force]
 Options:
 --debug Show extra info about aspell-autobuildhash internal
 work. Will also enable aspell affix validation.
 --dry-run Show what would be done, but do nothing real.
 --force Rebuild the hash file for all dicts providing a
 compat file skipping the test.
 --triggered Tell the script that is run in the triggers stage.</pre>
<h2>Description</h2>
<p><code>aspell-autobuildhash</code> is a script that will manage aspell hash files autobuild, intended to be called from the dictionaries-common tools. Depending on the aspell compatibility level and on the compatibility level used for the hash file if present, will decide whether it must be rebuilt or not. This script will only work on aspell packages prepared to use it, it will do nothing for other aspell dict packages.</p>
<h2>Options</h2>
<pre> --debug Show some extra information about aspell-autobuildhash
 internal work. Will also enable aspell affix validation.
 --dry-run Show what would be done, but do nothing real.
 --force Rebuild the hash file for all dicts providing a compat
 file regardless of the compatibility levels found.
 --triggered Tell the script that is run in the triggers stage. When
 run under dpkg control, do not try to set the
 'aspell-autobuildhash' trigger, but run real
 B&lt;aspell-autobuildhash&gt; code. When not run under dpkg
 control, real code will always be run and '--triggered'
 option has no real effect.</pre>
<h2>Package Maintainers</h2>
<p>To use this system, <code>aspell-autobuildhash</code> expects a <i></i>$lang<i>.compat</i> file in <i>/var/lib/aspell</i> (<i></i>$lang<i></i> stands for the lang basename with variant if any, e.g. <i></i>$lang<i></i> is something like <i>gl-minimos</i> or <i>en</i>)) containing aspell compatibility version for last successful build or &#8220;0&#8221; or en empty file if hash is to be rebuild, as is for dictionary installation and upgrades. </p>
<p> When upgrading <code>aspell</code>, script will check if version in <i></i>$lang<i>.compat</i> is different from <i>aspell.compat</i> and rebuild if so, updating <i></i>$lang<i>.compat</i> with the new value. </p>
<p> Wordlists should previously be compressed either with gzip (and their extensions set as <i>.mwl.gz</i> or <i>.wl.gz</i>) or preferably first with aspell prezip and then gzipped (with <i>.cwl.gz</i> extension). This applies both for plain wordlists and munched wordlists (in the ispell way) if you use affix compression. </p>
<p> If your package will provide a single hash, install prezipped+gzipped wordlist as <i>/usr/share/aspell/$lang.cwl.gz</i> or, if prezip is not used, as <i>/usr/share/aspell/$lang.mwl.gz</i>. </p>
<p> If your package will provide more than one aspell hash for the same <tt>$lang</tt>, you will need to place each compressed wordlist as e.g. <i>/usr/share/aspell/$subdict.cwl.gz</i>, and the common <i></i>$lang<i>.compat</i> as above. Then create a <i>/usr/share/aspell/$lang.contents</i> file with the base names of the subdicts, one in a line. For English that will contain, amongst other possible lines </p>
<pre> en-common
 en-variant_0
 en-variant_1
 en-variant_2
 en_CA-w_accents-only</pre>
<p>No need to use this file if a single hash is being created. </p>
<p> Dictionaries-common scripts will call internally this script and create a single hash file at <i>/var/lib/ispell/$lang.rws</i>, or hash files at <i>/var/lib/ispell/$subdict.rws</i>. You must set a symlink to that files from <i>/usr/lib/aspell/$lang.rws</i> or <i>/usr/lib/aspell/$subdict.rws</i> as appropriate. </p>
<p> Aspell dictionary packages using this script must make sure that <i></i>$lang<i>.compat</i> is reset on every new install/upgrade, so hash is rebuilt. They must also make sure that <i></i>$lang<i>.compat</i> and all of <i>/var/lib/aspell/$lang.rws</i> or <i>/var/lib/aspell/$subdict.rws</i> are removed on package removal. </p>
<p> As of version <tt>1.10</tt>, <code>installdeb-aspell</code> script will understand <tt>'auto-compat'</tt> and <tt>'auto-contents'</tt> fields in <i></i>$dict<i>.info-aspell</i> file to help with this by adding needed debhelper snippets. Put in that entry the base name(s) of your compat and contents file(s) and carefully check resulting maintainer scripts after build. </p>
<p> Note that you are no longer suggested to ship empty files at any of <i>/var/lib/aspell/$lang.compat</i>, <i>/var/lib/aspell/$lang.rws</i> or <i>/var/lib/aspell/$subdict.rws</i>, but explicitly create/update them on install and explicitly remove them on removal. </p>
<p> <code>aspell</code> maintainer should also call this script from package postinst. When comparing versions it will get the aspell version from file <i>/usr/share/aspell/aspell.compat</i>.</p>
<h2>Authors</h2>
<p>Agustin Martin &lt;agmartin [at] debian.org&gt;</p>
<h2>Copyright</h2>
<p>Copyright (C) 2004-2013 Agustin Martin &lt;agmartin [at] debian.org&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.</p>
