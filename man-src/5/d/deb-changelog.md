---
title: "deb-changelog(5)"
name: "deb-changelog"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-changelog/"
description: "deb-changelog – dpkg source packages’ changelog file format"
---

<p>deb-changelog &#8211; dpkg source packages&#8217; changelog file format</p>
<h2>Synopsis</h2>
<p><code>debian/changelog</code></p>
<h2>Description</h2>
<p>Changes in the packaged version of a project are explained in the changelog file <i>debian/changelog</i>. This includes modifications made in the source package compared to the upstream one as well as other changes and updates to the package. </p>
<p> The format of the <i>debian/changelog</i> allows the package building tools to discover which version of the package is being built and find out other release-specific information. </p>
<p> That format is a series of entries like this: </p>
<p>&nbsp;<i>package</i>&nbsp;(<i>version</i>)&nbsp;<i>distributions</i>;&nbsp;<i>metadata</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[optional blank line(s), stripped]<br />
&nbsp;<wbr>&nbsp;*&nbsp;<i>change-details</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>more-change-details</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[blank line(s), included in&nbsp;<code><a href="/docs/linux/man/1-dpkg-parsechangelog/">dpkg-parsechangelog</a></code>(1)&nbsp;output]<br />
&nbsp;<wbr>&nbsp;*&nbsp;<i>even-more-change-details</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[optional blank line(s), stripped]<br />
&nbsp;<wbr>&nbsp;&#8212;&nbsp;<i>maintainer-name</i>&nbsp;&lt;<i>email-address</i>&gt;&nbsp;<wbr>&nbsp;<i>date</i> </p>
<p> <i>package</i> and <i>version</i> are the source package name and version number. <i>version</i> is delimited by parenthesis U+00028 &#8216;<code>(</code>&#8216; and U+0029 &#8216;<code>)</code>&#8216;. </p>
<p> <i>distributions</i> lists one or more space-separated distributions where this version should be installed when it is uploaded; it is copied to the <code>Distribution</code> field in the <i>.changes</i> file. <i>distributions</i> must be terminated by a semicolon (U+003B &#8216;<code>;</code>&#8216;). </p>
<p> <i>metadata</i> lists zero or more comma-separated <i>keyword</i>=<i>value</i> items. Each keyword can contain only minus and case insensitive alphanumeric characters, as they need to be mapped to <code><a href="/docs/linux/man/5-deb822/">deb822</a></code>(5) field names. The only <i>keyword</i>s currently supported by <code>dpkg</code> are <code>urgency</code> and <code>binary-only</code>. <code>urgency</code>&#8216;s value is used for the <code>Urgency</code> field in the <i>.changes</i> file for the upload. <code>binary-only</code> with a <code>yes</code> value, is used to denote that this changelog entry is for a binary-only non-maintainer upload (an automatic binary rebuild with the only change being the changelog entry). </p>
<p> The change details may in fact be any series of lines starting with at least two spaces (U+0020 <font SIZE="-1"><code>SPACE</code></font>), but conventionally each change starts with an asterisk and a separating space and continuation lines are indented so as to bring them in line with the start of the text above. Blank lines may be used here to separate groups of changes, if desired. </p>
<p> If this upload resolves bugs recorded in the distribution bug tracking system, they may be automatically closed on the inclusion of this package into the distribution archive by including the string: </p>
<dl>
<dd><code>Closes: Bug#</code><i>nnnnn</i></dl>
<p> in the change details (the exact Perl regular expression is <code>/closes:\s*(?:bug)?\#?\s?\d+(?:,\s*(?:bug)?\#?\s?\d+)*/i</code>). This information is conveyed via the <code>Closes</code> field in the <i>.changes</i> file. </p>
<p> The maintainer name and email address used in the changelog should be the details of the person who prepared this release of the package. They are <code>not</code> necessarily those of the uploader or usual package maintainer. The information here will be copied to the <code>Changed-By</code> field in the <i>.changes</i> file, and then later might be used to send an acknowledgment when the upload has been installed in the distribution archive. </p>
<p> The <i>date</i> has the following format (compatible and with the same semantics of <font SIZE="-1">RFC2822</font> and <font SIZE="-1">RFC5322,</font> or what &laquo;date -R&raquo; generates): </p>
<dl>
<dd><i>day-of-week</i><code>,</code> <i>dd</i> <i>month</i> <i>yyyy</i> <i>hh</i><code>:</code><i>mm</i><code>:</code><i>ss</i> <code>+</code><i>zzzz</i></dl>
<p> where:</p>
<dl>
<dt><i>day-of-week</i></p>
<dd>Is one of: <code>Mon</code>, <code>Tue</code>, <code>Wed</code>, <code>Thu</code>, <code>Fri</code>, <code>Sat</code>, <code>Sun</code>.</p>
<dt><i>dd</i></p>
<dd>Is a one- or two-digit day of the month (<code>01</code>&#8211;<code>31</code>), where the leading zero is optional, but conventionally does not get omitted.</p>
<dt><i>month</i></p>
<dd>Is one of: <code>Jan</code>, <code>Feb</code>, <code>Mar</code>, <code>Apr</code>, <code>May</code>, <code>Jun</code>, <code>Jul</code>, <code>Aug</code>, <code>Sep</code>, <code>Oct</code>, <code>Nov</code>, <code>Dec</code>.</p>
<dt><i>yyyy</i></p>
<dd>Is the four-digit year (e.g. 2010).</p>
<dt><i>hh</i></p>
<dd>Is the two-digit hour (<code>00</code>&#8211;<code>23</code>).</p>
<dt><i>mm</i></p>
<dd>Is the two-digit minutes (<code>00</code>&#8211;<code>59</code>).</p>
<dt><i>ss</i></p>
<dd>Is the two-digit seconds (<code>00</code>&#8211;<code>60</code>).</p>
<dt>[<code>+-</code>]<i>zzzz</i></p>
<dd>Is the time zone offset from Coordinated Universal Time (<font SIZE="-1">UTC</font>). &#8216;<code>+</code>&#8216; indicates that the time is ahead of (i.e., east of) <font SIZE="-1">UTC</font> and &#8216;<code>&#8211;</code>&#8216; indicates that the time is behind (i.e., west of) <font SIZE="-1">UTC.</font> The first two digits indicate the hour difference from <font SIZE="-1">UTC</font> and the last two digits indicate the number of additional minutes difference from <font SIZE="-1">UTC.</font> The last two digits must be in the range <code>00</code>&#8211;<code>59</code>.</dl>
<p> The first &#8220;title&#8221; line with the package name must start at the left hand margin. The &#8220;trailer&#8221; line with the maintainer and date details must be preceded by exactly one space (U+0020 <font SIZE="-1"><code>SPACE</code></font>). The maintainer details and the date must be separated by exactly two spaces (U+0020 <font SIZE="-1"><code>SPACE</code></font>). Each part of the <i>date</i> can be separated by one or more spaces (U+0020 <font SIZE="-1"><code>SPACE</code></font>), except after the comma where it can be separated by zero or more spaces (U+0020 <font SIZE="-1"><code>SPACE</code></font>). </p>
<p> Any line that consists entirely (i.e., no leading whitespace) of <code>#</code> or <code>/* */</code> style comments or <font SIZE="-1">RCS</font> keywords. </p>
<p> Vim modelines or Emacs local variables, and ancient changelog entries with other formats at the end of the file should be accepted and preserved on output, but their contents might be otherwise ignored and parsing stopped at that point. </p>
<p> The entire changelog must be encoded in <font SIZE="-1">UTF-8.</font></p>
<h2>Files</h2>
<dl>
<dt><i>debian/changelog</i></p>
<dd></dl>
<h2>Examples</h2>
<pre> dpkg (1.17.18) unstable; urgency=low
 [ Guillem Jover ]
 * Handle empty minimum versions when initializing dependency versions,
 as the code is mapping the minimum version 0 to '' to avoid outputting
 useless versions. Regression introduced in dpkg 1.17.17. Closes: #764929
 [ Updated programs translations ]
 * Catalan (Guillem Jover).
 [ Updated dselect translations ]
 * Catalan (Guillem Jover).
 * German (Sven Joachim).
 -- Guillem Jover &lt;guillem [at] debian.org&gt; Sun, 12 Oct 2014 15:47:44 +0200</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-deb822/">deb822</a></code>(5), <code><a href="/docs/linux/man/7-deb-version/">deb-version</a></code>(7), <code><a href="/docs/linux/man/5-deb-changes/">deb-changes</a></code>(5), <code><a href="/docs/linux/man/1-dpkg-parsechangelog/">dpkg-parsechangelog</a></code>(1). </p>
