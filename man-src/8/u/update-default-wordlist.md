---
title: "update-default-wordlist(8)"
name: "update-default-wordlist"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-default-wordlist/"
description: "update-default-wordlist – update default wordlist"
---

<p>update-default-wordlist &#8211; update default wordlist</p>
<h2>Synopsis</h2>
<pre> update-default-wordlist [--skip-symlinks] [--triggered]</pre>
<h2>Description</h2>
<p><font SIZE="-1">WARNING:</font> Not to be used from the command line unless you know very well what you are doing. </p>
<p> This program is intended to be called from wordlist package postinst, from <code>select-default-wordlist</code> or from dictionaries-common postinst. </p>
<p> When called under dpkg control with the <code>&#8211;trigger</code> option the script is run normally, otherwise the dictionaries-common <code>update-default-wordlist</code> trigger is enabled for later run. </p>
<p> With the <code>&#8211;skip-symlinks</code> option the symlinks setting is skipped. </p>
<p> When run normally (from the command line or with <code>&#8211;trigger</code>) this script rebuilds the info at <i>/var/cache/dictionaries-common/wordlist.db</i> after files under <i>/var/lib/dictionaries-common/wordlist</i>, reads the system default from the debconf database and unless disabled, set default symlinks in <i>/etc/dictionaries-common</i> pointing to the appropriate files in <i>/usr/share/dict/</i>.</p>
<h2>Options</h2>
<pre> --skip-symlinks Do not try to set symlinks at /etc/dictionaries-common dir.
 --triggered Run all the code instead of trying to enable
 update-default-wordlist trigger</pre>
<h2>See Also</h2>
<p>The dictionaries-common policy document</p>
<h2>Authors</h2>
<p>Rafael Laboissiere, Agustin Martin Domingo</p>
