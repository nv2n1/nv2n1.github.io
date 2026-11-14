---
title: "clamsubmit(1)"
name: "clamsubmit"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clamsubmit/"
description: "clamsubmit – File submission utility for ClamAV"
---

<h2>NAME</h2>
<p> clamsubmit &#8211; File submission utility for ClamAV</p>
<h2>SYNOPSIS</h2>
<p> clamsubmit [options]</p>
<h2>DESCRIPTION</h2>
<p> clamsubmit submits files to Sourcefire for further analysis.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, -?</code></p>
<dd> Display help to stderr and exit.</p>
<dt><code>-e EMAIL</code></p>
<dd> Required option for setting the email address for the submission.</p>
<dt><code>-n FILE</code></p>
<dd> Submit a file that reports as a false negative (ClamAV reports CLEAN). FILE can be &#8211; to specify stdin. Mutually exclusive with -p.</p>
<dt><code>-N NAME</code></p>
<dd> Required option for setting the name of the sender for the submission.</p>
<dt><code>-p FILE</code></p>
<dd> Submit a file that reports as a false positive (ClamAV flags the file as virus). FILE can be &#8211; to specify stdin. Mutually exclusive with -n.</dl>
<h2>AUTHOR</h2>
<p> Shawn Webb &lt;swebb [at] sourcefire.com&gt; </p>
<h2>Index</h2>
