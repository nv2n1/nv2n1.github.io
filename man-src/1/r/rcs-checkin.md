---
title: "rcs-checkin(1)"
name: "rcs-checkin"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rcs-checkin/"
description: "rcs-checkin – check files into RCS"
---

<h2>NAME</h2>
<p> rcs-checkin &#8211; check files into RCS</p>
<h2>SYNOPSIS</h2>
<p> <code>rcs-checkin</code> [<i>FILE</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>rcs-checkin</code> is a helper script for checking files into RCS. This program is distributed with <code>GNU Emacs</code>. </p>
<p> This program converts files with an old <code>Emacs</code>-style version history for use with the <code>Emacs 19</code> version control interface <code>VC</code>, which likes to use RCS as its back end. </p>
<p> For each file to be processed, the script looks for <code>Emacs</code> version files related to it. These files are checked in as deltas, oldest first, so that the contents of the file itself becomes the latest revision in the master. </p>
<p> The first line of each file is used as its description. The file itself is not deleted, as under <code>VC</code> with <code>vc-keep-workfiles</code> at its default of <code>t</code>, but all the version files are. </p>
<p> If an argument file is already version-controlled under RCS, any version files are added to the list of deltas and deleted, and then the workfile is checked in again as the latest version. This is probably not quite what was wanted, and is the main reason VC doesn&#8217;t simply call this to do checkins. </p>
<p> In order to make it easier to use <code>rcs-checkin *</code>, files which are detectably either RCS masters (with names ending in <code>,v</code>) or Emacs version files (with names containing <code>~</code>) are ignored. </p>
<h2>OPTIONS</h2>
<p> The program accepts no options.</p>
<h2>SEE ALSO</h2>
<p> The Emacs version control interface is documented in the GNU Emacs manual, which you can read using <code>Info</code>, either from Emacs or as a standalone program.</p>
<h2>AUTHORS</h2>
<p> <i>rcs-checkin</i> was originally written by Paul Eggert. It was revised for use with <code>GNU Emacs</code> <code>VC</code> by Eric S. Raymond.</p>
<h2>COPYING</h2>
<p> Copyright (C) 2008-2012 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this document provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this document under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this document into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by the Free Software Foundation. </p>
<h2>Index</h2>
