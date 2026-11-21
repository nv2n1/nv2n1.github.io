---

title: "clamsubmit(1)"
name: "clamsubmit"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clamsubmit/"
description: "clamsubmit – File submission utility for ClamAV"
---

<p> clamsubmit &#8211; File submission utility for ClamAV</p>
<h2>SYNOPSIS</h2>
<p> clamsubmit [options]</p>
<h2>DESCRIPTION</h2>
<p> clamsubmit submits files to Sourcefire for further analysis.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, -?</code></dt>
<dd> Display help to stderr and exit.</dd>
<dt><code>-e EMAIL</code></dt>
<dd> Required option for setting the email address for the submission.</dd>
<dt><code>-n FILE</code></dt>
<dd> Submit a file that reports as a false negative (ClamAV reports CLEAN). FILE can be &#8211; to specify stdin. Mutually exclusive with -p.</dd>
<dt><code>-N NAME</code></dt>
<dd> Required option for setting the name of the sender for the submission.</dd>
<dt><code>-p FILE</code></dt>
<dd> Submit a file that reports as a false positive (ClamAV flags the file as virus). FILE can be &#8211; to specify stdin. Mutually exclusive with -n.</dd></dl>
<h2>AUTHOR</h2>
<p> Shawn Webb &lt;swebb [at] sourcefire.com&gt; </p>
