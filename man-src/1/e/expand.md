---
title: "expand(1)"
name: "expand"
section: "1"
letter: "e"
url: "/docs/linux/man/1-expand/"
description: "expand – convert tabs to spaces"
---

<h2>SYNOPSIS</h2>
<p> <code>expand</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Convert tabs in each FILE to spaces, writing to standard output. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-i</code>, <code>&#8211;initial</code></dt>
<dd> do not convert tabs after non blanks</dd>
<dt><code>-t</code>, <code>&#8211;tabs</code>=<i>,N/</i></dt>
<dd> have tabs N characters apart, not 8</dd>
<dt><code>-t</code>, <code>&#8211;tabs</code>=<i>,LIST/</i></dt>
<dd> use comma separated list of tab positions The last specified position can be prefixed with &#8216;/&#8217; to specify a tab size to use after the last explicitly specified tab stop. Also a prefix of &#8216;+&#8217; can be used to align remaining tab stops relative to the last specified tab stop instead of the first column</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-unexpand/">unexpand</a>(1) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/expand">https://www.gnu.org/software/coreutils/expand</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) expand invocation&#8217; </p>
