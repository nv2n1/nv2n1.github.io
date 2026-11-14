---
title: "lorax(1)"
name: "lorax"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lorax/"
description: "lorax – Create installer boot iso"
---

<h2>NAME</h2>
<p> lorax &#8211; Create installer boot iso </p>
<h2>SYNOPSIS</h2>
<p> lorax -p PRODUCT -v VERSION -r RELEASE -s REPOSITORY OUTPUTDIR </p>
<h2>DESCRIPTION</h2>
<p> lorax is used to create the installer boot iso. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> show this help message and exit </p>
<dt><code>-V</code></p>
<dd> show program&#8217;s version number and exit </p>
</dl>
<h2>REQUIRED ARGUMENTS:</h2>
<dl>
<dt><code>-p STRING, &#8211;product=STRING</code></p>
<dd> product name </p>
<dt><code>-v STRING, &#8211;version=STRING</code></p>
<dd> version identifier </p>
<dt><code>-r STRING, &#8211;release=STRING</code></p>
<dd> release information </p>
<dt><code>-s REPOSITORY, &#8211;source=REPOSITORY</code></p>
<dd> source repository (may be listed multiple times) </p>
</dl>
<h2>OPTIONAL ARGUMENTS:</h2>
<dl>
<dt><code>-m REPOSITORY, &#8211;mirrorlist=REPOSITORY</code></p>
<dd> mirrorlist repository (may be listed multiple times) </p>
<dt><code>-t STRING, &#8211;variant=STRING</code></p>
<dd> variant name </p>
<dt><code>-b URL, &#8211;bugurl=URL</code></p>
<dd> bug reporting URL for the product </p>
<dt><code>&#8211;isfinal</code></p>
<dd>
<dt><code>-c STRING, &#8211;config=STRING</code></p>
<dd> config file </p>
<dt><code>&#8211;proxy=STRING</code></p>
<dd> repo proxy url:port </p>
<dt><code>-e STRING, &#8211;excludepkgs=STRING</code></p>
<dd> package glob to exclude (may be listed multiple times) </p>
<dt><code>&#8211;buildarch=STRING</code></p>
<dd> build architecture </p>
<dt><code>&#8211;volid=STRING</code></p>
<dd> volume id </p>
<dt><code>&#8211;nomacboot</code></p>
<dd>
<dt><code>&#8211;noupgrade</code></p>
<dd>
<dt><code>&#8211;logfile=LOGFILE</code></p>
<dd> Path to logfile </p>
<dt><code>&#8211;tmp=TMP</code></p>
<dd> Top level temporary directory </p>
</dl>
<h2>AUTHORS</h2>
<pre>
Martin Gracik
Will Woods
Brian C. Lane
</pre>
<h2>Index</h2>
