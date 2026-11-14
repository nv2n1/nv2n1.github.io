---
title: "deb-version(7)"
name: "deb-version"
section: "7"
letter: "d"
url: "/docs/linux/man/7-deb-version/"
description: "deb-version – Debian package version number format"
---

<p>deb-version &#8211; Debian package version number format</p>
<h2>Synopsis</h2>
<p>[<i>epoch</i><code>:</code>]<i>upstream-version</i>[<code>&#8211;</code><i>debian-revision</i>]</p>
<h2>Description</h2>
<p>Version numbers as used for Debian binary and source packages consist of three components. These are:</p>
<dl>
<dt><i>epoch</i></p>
<dd>This is a single (generally small) unsigned integer. It may be omitted, in which case zero is assumed. If it is omitted then the <i>upstream-version</i> may not contain any colons. </p>
<p> It is provided to allow mistakes in the version numbers of older versions of a package, and also a package&#8217;s previous version numbering schemes, to be left behind.</p>
<dt><i>upstream-version</i></p>
<dd>This is the main part of the version number. It is usually the version number of the original (&#8220;upstream&#8221;) package from which the <i>.deb</i> file has been made, if this is applicable. Usually this will be in the same format as that specified by the upstream author(s); however, it may need to be reformatted to fit into the package management system&#8217;s format and comparison scheme. </p>
<p> The comparison behavior of the package management system with respect to the <i>upstream-version</i> is described below. The <i>upstream-version</i> portion of the version number is mandatory. </p>
<p> The <i>upstream-version</i> may contain only alphanumerics (&#8220;A-Za-z0-9&#8221;) and the characters <code>.</code> <code>+</code> <code>&#8211;</code> <code>:</code> <code>~</code> (full stop, plus, hyphen, colon, tilde) and should start with a digit. If there is no <i>debian-revision</i> then hyphens are not allowed; if there is no <i>epoch</i> then colons are not allowed.</p>
<dt><i>debian-revision</i></p>
<dd>This part of the version number specifies the version of the Debian package based on the upstream version. It may contain only alphanumerics and the characters <code>+</code> <code>.</code> <code>~</code> (plus, full stop, tilde) and is compared in the same way as the <i>upstream-version</i> is. </p>
<p> It is optional; if it isn&#8217;t present then the <i>upstream-version</i> may not contain a hyphen. This format represents the case where a piece of software was written specifically to be turned into a Debian package, and so there is only one &#8220;debianization&#8221; of it and therefore no revision indication is required. </p>
<p> It is conventional to restart the <i>debian-revision</i> at &#8216;1&#8217; each time the <i>upstream-version</i> is increased. </p>
<p> Dpkg will break the version number apart at the last hyphen in the string (if there is one) to determine the <i>upstream-version</i> and <i>debian-revision</i>. The absence of a <i>debian-revision</i> compares earlier than the presence of one (but note that the <i>debian-revision</i> is the least significant part of the version number).</dl>
<h3>Sorting algorithm</h3>
<p>The <i>upstream-version</i> and <i>debian-revision</i> parts are compared by the package management system using the same algorithm: </p>
<p> The strings are compared from left to right. </p>
<p> First the initial part of each string consisting entirely of non-digit characters is determined. These two parts (one of which may be empty) are compared lexically. If a difference is found it is returned. The lexical comparison is a comparison of <font SIZE="-1">ASCII</font> values modified so that all the letters sort earlier than all the non-letters and so that a tilde sorts before anything, even the end of a part. For example, the following parts are in sorted order: &#8216;~~&#8217;, &#8216;~~a&#8217;, &#8216;~&#8217;, the empty part, &#8216;a&#8217;. </p>
<p> Then the initial part of the remainder of each string which consists entirely of digit characters is determined. The numerical values of these two parts are compared, and any difference found is returned as the result of the comparison. For these purposes an empty string (which can only occur at the end of one or both version strings being compared) counts as zero. </p>
<p> These two steps (comparing and removing initial non-digit strings and initial digit strings) are repeated until a difference is found or both strings are exhausted. </p>
<p> Note that the purpose of epochs is to allow us to leave behind mistakes in version numbering, and to cope with situations where the version numbering scheme changes. It is <code>not</code> intended to cope with version numbers containing strings of letters which the package management system cannot interpret (such as &#8216;ALPHA&#8217; or &#8216;pre-&#8216;), or with silly orderings.</p>
<h2>Notes</h2>
<p>The tilde character and its special sorting properties were introduced in dpkg 1.10 and some parts of the dpkg build scripts only gained support for it later in the 1.10.x series.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5), <code><a href="/docs/linux/man/5-deb/">deb</a></code>(5), <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) </p>
