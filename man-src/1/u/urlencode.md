---
title: "urlencode(1)"
name: "urlencode"
section: "1"
letter: "u"
url: "/docs/linux/man/1-urlencode/"
description: "urlencode – convert strings to or from URL-encoded form"
---

<h2>NAME</h2>
<p> <code>urlencode</code> &#8211; convert strings to or from URL-encoded form</p>
<h2>SYNOPSIS</h2>
<p> <code>urlencode </code> [-m|-d] <i>string [string &#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>urlencode</code> encodes strings according to RFC 1738. </p>
<p> That is, characters A-Z a-z 0-9 . _ and &#8211; are passed through unmodified, but all other characters are represented as %HH, where HH is their two-digit upper-case hexadecimal ASCII representation. For example, the URL <a rel="nofollow" href="http://www.gridpp.ac.uk/">http://www.gridpp.ac.uk/</a> becomes http%3A%2F%2F<a rel="nofollow" href="http://www.gridpp.ac.uk">www.gridpp.ac.uk</a>%2F </p>
<p> <code>urlencode</code> converts each character in all the strings given on the command line. If multiple strings are given, they are concatenated with separating spaces before conversion. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-m</p>
<dd> Instead of full conversion, do GridSite &quot;mild URL encoding&quot; in which A-Z a-z 0-9 . = &#8211; _ @ and / are passed through unmodified. This results in slightly more human-readable strings but the application must be prepared to create or simulate the directories implied by any slashes. </p>
<dt>-d</p>
<dd> Do URL-decoding rather than encoding, according to RFC 1738. %HH and %hh strings are converted and other characters are passed through unmodified, with the exception that + is converted to space. </p>
</dl>
<h2>EXIT CODES</h2>
<p> 0 is always returned. </p>
<h2>AUTHOR</h2>
<p> Andrew McNab &lt;Andrew.McNab [at] manchester.ac.uk&gt; </p>
<p> urlencode is part of GridSite: <a rel="nofollow" href="http://www.gridsite.org/">http://www.gridsite.org/</a> </p>
<h2>Index</h2>
