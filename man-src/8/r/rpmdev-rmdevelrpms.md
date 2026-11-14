---
title: "rpmdev-rmdevelrpms(8)"
name: "rpmdev-rmdevelrpms"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpmdev-rmdevelrpms/"
description: "rpmdev-rmdevelrpms – manual page for rpmdev-rmdevelrpms version 1.13"
---

<p>rpmdev-rmdevelrpms &#8211; manual page for rpmdev-rmdevelrpms version 1.13</p>
<h2>Synopsis</h2>
<p><code>rpmdev-rmdevelrpms</code> [<i>options</i>]</p>
<h2>Description</h2>
<p>rpmdev-rmdevelrpms is a script for finding and optionally removing &quot;development&quot; packages, for example for cleanup purposes before starting to build a new package. </p>
<p> By default, the following packages are treated as development ones and are thus candidates for removal: any package whose name matches &quot;-devel&quot;, &quot;-debuginfo&quot;, &quot;-sdk&quot;, or &quot;-static&quot; (case insensitively) except gcc requirements; any package whose name starts with &quot;perl-(Devel|ExtUtils|Test)-&quot;; any package whose name starts with &quot;compat-gcc&quot;; packages in the internal list of known development oriented packages (see def_devpkgs in the source code); packages determined to be development ones based on some basic heuristic checks on the package&#8217;s contents. </p>
<p> The default set of packages above is not intended to not reduce a system into a minimal clean build root, but to keep it usable for general purposes while getting rid of a reasonably large set of development packages. The package set operated on can be configured to meet various scenarios. </p>
<p> To include additional packages in the list of ones treated as development packages, use the &quot;devpkgs&quot; option in the configuration file. To exclude packages from the list use &quot;nondevpkgs&quot; in it. Exclusion overrides inclusion. </p>
<p> The system wide configuration file is <i>/etc/rpmdevtools/rmdevelrpms.conf</i>, and per user settings (which override system ones) can be specified in ~/.config/rpmdevtools/rmdevelrpms.conf or ~/.rmdevelrpmsrc (deprecated). These files are written in Python.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>-l</code>, <code>&#8211;list-only</code></p>
<dd>Output condensed list of packages, do not remove.</p>
<dt><code>&#8211;qf</code>=<i>QF</i>, <code>&#8211;queryformat</code>=<i>QF</i></p>
<dd>Query format to use for output.</p>
<dt><code>-y</code>, <code>&#8211;yes</code></p>
<dd>Root only: remove without prompting; ignored with <code>-l</code>.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>Print program version and exit.</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com/">http://bugzilla.redhat.com/</a>&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2009 Ville Skyttä &lt;ville.skytta [at] iki.fi&gt; This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version.</p>
