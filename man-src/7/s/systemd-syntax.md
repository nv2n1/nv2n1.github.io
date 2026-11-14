---
title: "systemd-syntax(7)"
name: "systemd-syntax"
section: "7"
letter: "s"
url: "/docs/linux/man/7-systemd-syntax/"
description: "systemd.syntax – General syntax of systemd configuration files"
---

<p>systemd.syntax &#8211; General syntax of systemd configuration files</p>
<h2>Introduction</h2>
<p>This page describes the basic principles of configuration files used by <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) and related programs for: </p>
<dl>
<dd>&bull; systemd unit files, see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-device/">systemd.device</a></code>(5), <code><a href="/docs/linux/man/5-systemd-mount/">systemd.mount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-automount/">systemd.automount</a></code>(5), <code><a href="/docs/linux/man/5-systemd-swap/">systemd.swap</a></code>(5), <code><a href="/docs/linux/man/5-systemd-target/">systemd.target</a></code>(5), <code><a href="/docs/linux/man/5-systemd-path/">systemd.path</a></code>(5), <code><a href="/docs/linux/man/5-systemd-timer/">systemd.timer</a></code>(5), <code><a href="/docs/linux/man/5-systemd-slice/">systemd.slice</a></code>(5), <code><a href="/docs/linux/man/5-systemd-scope/">systemd.scope</a></code>(5), <code><a href="/docs/linux/man/5-systemd-nspawn/">systemd.nspawn</a></code>(5)</dl>
<dl>
<dd>&bull; link files, see <code><a href="/docs/linux/man/5-systemd-link/">systemd.link</a></code>(5)</dl>
<dl>
<dd>&bull; netdev and network files, see <code><a href="/docs/linux/man/5-systemd-netdev/">systemd.netdev</a></code>(5), <code><a href="/docs/linux/man/5-systemd-network/">systemd.network</a></code>(5)</dl>
<dl>
<dd>&bull; daemon config files, see <code><a href="/docs/linux/man/5-systemd-system-conf/">systemd-system.conf</a></code>(5), <code><a href="/docs/linux/man/5-systemd-user-conf/">systemd-user.conf</a></code>(5), <code><a href="/docs/linux/man/5-logind-conf/">logind.conf</a></code>(5), <code><a href="/docs/linux/man/5-journald-conf/">journald.conf</a></code>(5), <code><a href="/docs/linux/man/5-journal-remote-conf/">journal-remote.conf</a></code>(5), <code><a href="/docs/linux/man/5-journal-upload-conf/">journal-upload.conf</a></code>(5), <code><a href="/docs/linux/man/5-systemd-sleep-conf/">systemd-sleep.conf</a></code>(5), <code><a href="/docs/linux/man/5-timesyncd-conf/">timesyncd.conf</a></code>(5)</dl>
<p> The syntax is inspired by m[blue]<code>XDG Desktop Entry Specification</code>m[]<font SIZE="-2">[1]</font> .desktop files, which are in turn inspired by Microsoft Windows .ini files. </p>
<p> Each file is a plain text file divided into sections, with configuration entries in the style <i>key</i>=<i>value</i>. Whitespace immediately before or after the &quot;=&quot; is ignored. Empty lines and lines starting with &quot;#&quot; or &quot;;&quot; are ignored, which may be used for commenting. </p>
<p> Lines ending in a backslash are concatenated with the following line while reading and the backslash is replaced by a space character. This may be used to wrap long lines. The limit on line length is very large (currently 1 MB), but it is recommended to avoid such long lines and use multiple directives, variable substitution, or other mechanism as appropriate for the given file type. When a comment line or lines follow a line ending with a backslash, the comment block is ignored, so the continued line is concatenated with whatever follows the comment block. </p>
<p> <code>Example 1.&nbsp;</code> </p>
<dl>
<dd>
<pre>[Section A]
KeyOne=value 1
KeyTwo=value 2
# a comment
[Section B]
Setting=&quot;something&quot; &quot;some thing&quot; &quot;...&quot;
KeyTwo=value 2 \
 value 2 continued
[Section C]
KeyThree=value 3\
# this line is ignored
; this line is ignored too
 value 3 continued</pre>
</dl>
<p> Boolean arguments used in configuration files can be written in various formats. For positive settings the strings <code>1</code>, <code>yes</code>, <code>true</code> and <code>on</code> are equivalent. For negative settings, the strings <code>0</code>, <code>no</code>, <code>false</code> and <code>off</code> are equivalent. </p>
<p> Time span values encoded in configuration files can be written in various formats. A stand-alone number specifies a time in seconds. If suffixed with a time unit, the unit is honored. A concatenation of multiple values with units is supported, in which case the values are added up. Example: &quot;50&quot; refers to 50 seconds; &quot;2min 200ms&quot; refers to 2 minutes and 200 milliseconds, i.e. 120200 ms. The following time units are understood: &quot;s&quot;, &quot;min&quot;, &quot;h&quot;, &quot;d&quot;, &quot;w&quot;, &quot;ms&quot;, &quot;us&quot;. For details see <code><a href="/docs/linux/man/7-systemd-time/">systemd.time</a></code>(7). </p>
<p> Various settings are allowed to be specified more than once, in which case the interpretation depends on the setting. Often, multiple settings form a list, and setting to an empty value &quot;resets&quot;, which means that previous assignments are ignored. When this is allowed, it is mentioned in the description of the setting. Note that using multiple assignments to the same value makes the file incompatible with parsers for the XDG .desktop file format.</p>
<h2>Quoting</h2>
<p>For settings where quoting is allowed, the following general rules apply: double quotes (&quot;&#8230;&quot;) and single quotes (&#8216;&#8230;&#8217;) may be used to wrap a whole item (the opening quote may appear only at the beginning or after whitespace that is not quoted, and the closing quote must be followed by whitespace or the end of line), in which case everything until the next matching quote becomes part of the same item. Quotes themselves are removed. C-style escapes are supported. The table below contains the list of known escape patterns. Only escape patterns which match the syntax in the table are allowed; other patterns may be added in the future and unknown patterns will result in a warning. In particular, any backslashes should be doubled. Finally, a trailing backslash (&quot;\&quot;) may be used to merge lines, as described above. UTF-8 is accepted, and hence typical unicode characters do not need to be escaped. </p>
<p> <code>Table 1. Supported escapes</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Literal </code></td>
<td><code> Actual value </code>
</td>
</tr>
<tr VALIGN=top>
<td> &quot;&quot; </td>
<td> bell
</td>
</tr>
<tr VALIGN=top>
<td> &quot;&quot; </td>
<td> backspace
</td>
</tr>
<tr VALIGN=top>
<td> &quot;&quot; </td>
<td> form feed
</td>
</tr>
<tr VALIGN=top>
<td> &quot;
&quot; </td>
<td> newline
</td>
</tr>
<tr VALIGN=top>
<td> &quot;&quot; </td>
<td> carriage return
</td>
</tr>
<tr VALIGN=top>
<td> &quot;	&quot; </td>
<td> tab
</td>
</tr>
<tr VALIGN=top>
<td> &quot;&quot; </td>
<td> vertical tab
</td>
</tr>
<tr VALIGN=top>
<td> &quot;\&quot; </td>
<td> backslash
</td>
</tr>
<tr VALIGN=top>
<td> &quot;\&quot;&quot; </td>
<td> double quotation mark
</td>
</tr>
<tr VALIGN=top>
<td> &quot;\&#8217;&quot; </td>
<td> single quotation mark
</td>
</tr>
<tr VALIGN=top>
<td> &quot;\s&quot; </td>
<td> space
</td>
</tr>
<tr VALIGN=top>
<td> &quot;
