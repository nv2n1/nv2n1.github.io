---
title: "ncidtools(1)"
name: "ncidtools"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncidtools/"
description: "cidlog – view Caller ID log file"
---

<h2>NAME</h2>
<p> <code>cidlog</code> &#8211; view Caller ID log file </p>
<p> <code>cidalias</code> &#8211; view Caller ID alias definitions </p>
<p> <code>cidupdate</code> &#8211; update Caller ID aliases in log file</p>
<h2>SYNOPSIS</h2>
<p> <code>cidcall</code> [-r | -m] [cidlog] </p>
<p> <code>cidalias</code> [-r] [aliasfile] </p>
<p> <code>cidupdate</code> [-a aliasfile] [-l cidlog] [newcidlog]</p>
<h2>DESCRIPTION</h2>
<p> The script, <code>cidcall</code>, displays the current CID call file. </p>
<p> The script, <code>cidalias</code>, displays the aliases in the ncidd.alias file. </p>
<p> The Script, <code>cidupdate</code>, updates the CID log file using the aliases found in the ncidd.alias file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r</code></p>
<dd> Display the raw log file or alias definition.<br />
 Default: format the log file or alias definition.</p>
<dt><code>-m</code></p>
<dd> Display messages sent.</p>
<dt><code>-a aliasfile</code></p>
<dd> Set the alias file to <i>aliasfile</i><br />
 Default: /etc/ncid/ncidd.alias</p>
<dt><code>-c cidlog</code></p>
<dd> Set the CID call file to <i>cidlog</i><br />
 Default: /var/log/cidcall.log</dl>
<h3>Arguments</h3>
<dl>
<dt><code>cidlog</code></p>
<dd> The CID call file.<br />
 Default: /var/log/cidcall.log</p>
<dt><code>configfile</code></p>
<dd> The ncidd configuration file.<br />
 Default: /etc/ncid/ncidd.conf</p>
<dt><code>newcidlog</code></p>
<dd> The updated CID log file.<br />
 Default: cidcall.log.new</dl>
<h2>SEE ALSO</h2>
<p> ncidd.conf.5, ncidd.alias.5 </p>
<h2>Index</h2>
