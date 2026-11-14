---
title: "debhelper-obsolete-compat(7)"
name: "debhelper-obsolete-compat"
section: "7"
letter: "d"
url: "/docs/linux/man/7-debhelper-obsolete-compat/"
description: "debhelper-obsolete-compat – List of no longer supported compat levels"
---

<p>debhelper-obsolete-compat &#8211; List of no longer supported compat levels</p>
<h2>Synopsis</h2>
<p>This document contains the upgrade guidelines from all compat levels which are no longer supported. Accordingly it is mostly for historical purposes and to assist people upgrading from a non-supported compat level to a supported level. </p>
<p> For upgrades from supported compat levels, please see <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7).</p>
<h2>Upgrade List For Compat Levels</h2>
<p>The following is the list of now obsolete compat levels and their changes.</p>
<dl>
<dt>v1</p>
<dd>This is the original debhelper compatibility level, and so it is the default one. In this mode, debhelper will use <i>debian/tmp</i> as the package tree directory for the first binary package listed in the control file, while using debian/<i>package</i> for all other packages listed in the <i>control</i> file. </p>
<p> This mode is deprecated.</p>
<dt>v2</p>
<dd>In this mode, debhelper will consistently use debian/<i>package</i> as the package tree directory for every package that is built. </p>
<p> This mode is deprecated.</p>
<dt>v3</p>
<dd>This mode works like v2, with the following additions:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>Debhelper config files support globbing via <code>*</code> and <code>?</code>, when appropriate. To turn this off and use those characters raw, just prefix with a backslash.</p>
<dt>&#8211;</p>
<dd><code>dh_makeshlibs</code> makes the <i>postinst</i> and <i>postrm</i> scripts call <code>ldconfig</code>.</p>
<dt>&#8211;</p>
<dd>Every file in <i>etc/</i> is automatically flagged as a conffile by <code>dh_installdeb</code>.</dl>
</dl>
<dl>
<dd>This mode is deprecated.</dl>
<dt>v4</p>
<dd>Changes from v3 are:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd><code>dh_makeshlibs -V</code> will not include the Debian part of the version number in the generated dependency line in the shlibs file.</p>
<dt>&#8211;</p>
<dd>You are encouraged to put the new <code>${misc:Depends}</code> into <i>debian/control</i> to supplement the <code>${shlibs:Depends}</code> field.</p>
<dt>&#8211;</p>
<dd><code>dh_fixperms</code> will make all files in <i>bin/</i> directories and in <i>etc/init.d</i> executable.</p>
<dt>&#8211;</p>
<dd><code>dh_link</code> will correct existing links to conform with policy.</dl>
</dl>
<dl>
<dd>This mode is deprecated.</dl>
<dt>v5</p>
<dd>This is the lowest supported compatibility level. </p>
<p> Changes from v4 are:</p>
<dl>
<dd>
<dl>
<dt>&#8211;</p>
<dd>Comments are ignored in debhelper config files.</p>
<dt>&#8211;</p>
<dd><code>dh_strip &#8211;dbg-package</code> now specifies the name of a package to put debugging symbols in, not the packages to take the symbols from.</p>
<dt>&#8211;</p>
<dd><code>dh_installdocs</code> skips installing empty files.</p>
<dt>&#8211;</p>
<dd><code>dh_install</code> errors out if wildcards expand to nothing.</dl>
</dl>
<dl>
<dd></dl>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7)</p>
<h2>Authors</h2>
<p>Niels Thykier &lt;niels [at] thykier.net&gt; </p>
<p> Joey Hess</p>
