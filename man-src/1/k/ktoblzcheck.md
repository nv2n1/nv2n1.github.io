---
title: "ktoblzcheck(1)"
name: "ktoblzcheck"
section: "1"
letter: "k"
url: "/docs/linux/man/1-ktoblzcheck/"
description: "ktoblzcheck – Check Account and BLZ (bank routing code)"
---

<h2 class="name">NAME</h2>
<p> ktoblzcheck &#8211; Check Account and BLZ (bank routing code) </p>
<h2>SYNOPSIS</h2>
<p> <code>ktoblzcheck [&#8211;returncode] [&#8211;file=&lt;datafile&gt;] &lt;bank-id&gt; &lt;account-id&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>ktoblzcheck</code> application. </p>
<p> <code>ktoblzcheck</code> is a program that will check a given account and blz for the bank being valid and the account being valid using some checksum calculations, if supported for that particular bank. The output is the clear-text name of the bank specified by &lt;bank-id&gt;, and whether the given &lt;account-id&gt; is a valid account number at this bank.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&lt;bank-id&gt;</code></p>
<dd> This is the Bankleitzahl (bank routing id), actually it is the account-id of that particular bank at the Deutsche Bundesbank.</p>
<dt><code>&lt;account-id&gt;</code></p>
<dd> This is the account number you wish to verify. If the checksum method of the bank specified by the &lt;bank-id&gt; is supported, you will get the account-id verified, i.e. if it is a valid account-id at that particular bank.</p>
<dt><code>&#8211;returncode</code></p>
<dd> If given, the result is returned via the returncode and no output on the terminal. The following returncodes are possible: 0: account and bank are ok 1: unknown, e.g. checksum not implemented or such 2: account and/or bank not ok 3: bank not found</p>
<dt><code>&#8211;file=&lt;datafile&gt;</code></p>
<dd> Specifies the file with the bankdata. This file can be obtained via the internet from the Deutsche Bundesbank on address </p>
<pre>
<a rel="nofollow" href="http://www.bundesbank.de/zahlungsverkehr/zahlungsverkehr_bankleitzahlen_download.php">http://www.bundesbank.de/zahlungsverkehr/zahlungsverkehr_bankleitzahlen_download.php</a>
</pre>
<p> Beware! This page is in German only.</dl>
<h2>BUGS</h2>
<p> No bugs are known at this time. Only certain checksum algorythms are supported as of now, so please don&#8217;t complain if you always get &quot;unknown&quot; as return value.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Jens Gecius &lt;jens [at] gecius.de&gt; for the Debian GNU/Linux system. Authors of ktoblzcheck are Fabian Kaiser &lt;fabian [at] openhbci.de&gt; and Christian Stimming &lt;stimming [at] tuhh.de&gt;. </p>
<h2>Index</h2>
