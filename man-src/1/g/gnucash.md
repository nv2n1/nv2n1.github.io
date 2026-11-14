---
title: "gnucash(1)"
name: "gnucash"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnucash/"
description: "gnucash – personal finance manager"
---

<h2>NAME</h2>
<p> gnucash &#8211; personal finance manager</p>
<h2>SYNOPSIS</h2>
<p> <code>gnucash [options] [</code> <i>accounts.gnc</i> <code>]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>GnuCash</code> is a personal accounting package that allows you to record and track income, expenses, assets, and investments. It supports reconciliation, has substantial reporting capabilities, and is extensible using guile. It can import QIF data from Quicken(TM) and many other commercial accounting packages. It uses GTK+ and GNOME to provide an attractive user interface, and has extensive online help. </p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;version</p>
<dd> Show <code>GnuCash</code> version</p>
<dt>&#8211;help</p>
<dd> Show this help message</p>
<dt>&#8211;debug</p>
<dd> Enable debugging mode: increasing logging to provide deep detail.</p>
<dt>&#8211;extra</p>
<dd> Enable extra/development/debugging features.</p>
<dt>&#8211;log</p>
<dd> Log level overrides, of the form &quot;log.ger.path={debug,info,warn,crit,error}&quot;</p>
<dt>&#8211;logto</p>
<dd> File to log into; defaults to &quot;/tmp/gnucash.trace&quot;; can be &quot;stderr&quot; or &quot;stdout&quot;.</p>
<dt>&#8211;nofile</p>
<dd> Do not load the last file opened</p>
<dt>&#8211;add-price-quotes FILE</p>
<dd> Add price quotes to the given data file</p>
<dt>&#8211;namespace=REGEXP</p>
<dd> Regular expression determining which namespace commodities will be retrieved.</dl>
<h2>FILES</h2>
<p> <i>~/.gnucash/config.auto</i></p>
<dl>
<dt>
<dd> Automatically generated per-user configuration file. DO NOT EDIT MANUALLY!</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>GNC_DEBUG</p>
<dd> Enable debugging output. This allows you to turn on the debugging earlier in the startup process than you can with <code>&#8211;debug.</code></p>
<dt>GUILE_LOAD_PATH</p>
<dd> An override for the <code>GnuCash</code> scheme load path. You shouldn&#8217;t need to alter this. For more information see the README file.</p>
<dt>GNC_MODULE_PATH</p>
<dd> An override for the <code>GnuCash</code> scheme load path for <code>Gnucash</code> modules. You shouldn&#8217;t need to alter this. For more information see the README file.</dl>
<h2>BUGS</h2>
<p> <code>Please report any bugs using the bug reporting form on the</code> <code>GnuCash</code> web site. </p>
<h2>SEE ALSO</h2>
<p> <code>GnuCash</code> has extensive on-line help available from the &quot;help&quot; menu. </p>
<p> Additional information and the latest version is available at the web site: <code><a rel="nofollow" href="http://www.gnucash.org">http://www.gnucash.org</a></code> </p>
<h2>AUTHOR</h2>
<p> Robert Merkel &lt;rgmerk [at] mira.net&gt; wrote this manpage. </p>
<p> <code>GnuCash</code> was written by Robin Clark, Linas Vepstas, and a cast of thousands. </p>
<h2>Index</h2>
