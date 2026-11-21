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
<dt><code>-h, &#8211;help</code></dt>
<dd> show this help message and exit </dd>
<dt><code>-V</code></dt>
<dd> show program&#8217;s version number and exit </dd>
</dl>
<h2>REQUIRED ARGUMENTS:</h2>
<dl>
<dt><code>-p STRING, &#8211;product=STRING</code></dt>
<dd> product name </dd>
<dt><code>-v STRING, &#8211;version=STRING</code></dt>
<dd> version identifier </dd>
<dt><code>-r STRING, &#8211;release=STRING</code></dt>
<dd> release information </dd>
<dt><code>-s REPOSITORY, &#8211;source=REPOSITORY</code></dt>
<dd> source repository (may be listed multiple times) </dd>
</dl>
<h2>OPTIONAL ARGUMENTS:</h2>
<dl>
<dt><code>-m REPOSITORY, &#8211;mirrorlist=REPOSITORY</code></dt>
<dd> mirrorlist repository (may be listed multiple times) </dd>
<dt><code>-t STRING, &#8211;variant=STRING</code></dt>
<dd> variant name </dd>
<dt><code>-b URL, &#8211;bugurl=URL</code></dt>
<dd> bug reporting URL for the product </dd>
<dt><code>&#8211;isfinal</code></dt>
<dd>
</dd><dt><code>-c STRING, &#8211;config=STRING</code></dt>
<dd> config file </dd>
<dt><code>&#8211;proxy=STRING</code></dt>
<dd> repo proxy url:port </dd>
<dt><code>-e STRING, &#8211;excludepkgs=STRING</code></dt>
<dd> package glob to exclude (may be listed multiple times) </dd>
<dt><code>&#8211;buildarch=STRING</code></dt>
<dd> build architecture </dd>
<dt><code>&#8211;volid=STRING</code></dt>
<dd> volume id </dd>
<dt><code>&#8211;nomacboot</code></dt>
<dd>
</dd><dt><code>&#8211;noupgrade</code></dt>
<dd>
</dd><dt><code>&#8211;logfile=LOGFILE</code></dt>
<dd> Path to logfile </dd>
<dt><code>&#8211;tmp=TMP</code></dt>
<dd> Top level temporary directory </dd>
</dl>
<h2>AUTHORS</h2>
<pre>
Martin Gracik
Will Woods
Brian C. Lane
</pre>
