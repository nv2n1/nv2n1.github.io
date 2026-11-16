---
title: "wpg2svgbatch-pl(1)"
name: "wpg2svgbatch-pl"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wpg2svgbatch-pl/"
description: "wpg2svgbatch.pl – batch convert WordPerfect Graphics files into SVG"
---

<p>wpg2svgbatch.pl &#8211; batch convert WordPerfect Graphics files into SVG</p>
<h2>Description</h2>
<dl COMPACT>
<dd>Usage: wpg2svgbatch.pl [-hruv] [-d dir] [-o dir]</dd>
<dd>wpg2svgbatch.pl uses wpg2svg to convert batches of WordPerfect word processor files (WPG) to the Scalable Vector Graphics (SVG) format. The SVG files are generated anew and do not replace the original wpg files.</dd>
<dd>Running wpg2svgbatch.pl more than once on the same directory will cause the existing SVG file to be replaced with a new one.</dd>
<dt> <code>-d</code> &lt;dir&gt;</dt>
<dd>
</dd><dd>begins the conversion process in directory &quot;dir&quot; instead of the current directory. Use this switch separately from the other switches, (<code>-vr</code> <code>-d</code> <i>/home/robin</i>) or at the end of a switch string (<code>-rvd</code> <i>/home/robin</i>).</dd>
<dt><code>-h</code></dt>
<dd>displays this help text.</dd>
<dt> <code>-o</code> &lt;dir&gt;</dt>
<dd>
</dd><dd>causes all the generated SVG files to be deposited in this single specified output directory. When not used, the generated SVG files are deposited in the same directory in which the original WPG file was found. Use this switch separately from the other switches, (<code>-vr</code> <code>-o</code> <i>/home/robin</i>)</dd>
<dt><code>-r</code></dt>
<dd>converts files in either the current directory or the directory specified by the <code>-d</code> switch (see below) and all the wpg files in all the subdirectories.</dd>
<dt><code>-u</code></dt>
<dd>replaces spaces with underscores in the target filename(s).</dd>
<dt><code>-v</code></dt>
<dd>Displays statistics and the progress of the conversion.</dd></dl>
<p> running under Perl version 5.16.3.</p>
<dl COMPACT>
<dd>[Now continuing due to backward compatibility and excessive paranoia.</dd>
<dd>See &#8216;perldoc Getopt::Std&#8217; about $Getopt::Std::STANDARD_HELP_VERSION.] </dd>
</dl>
