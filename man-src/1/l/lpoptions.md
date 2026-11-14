---
title: "lpoptions(1)"
name: "lpoptions"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lpoptions/"
description: "lpoptions – display or set printer options and defaults"
---

<h2 class="name">NAME</h2>
<p> lpoptions &#8211; display or set printer options and defaults </p>
<h2>SYNOPSIS</h2>
<p> <code>lpoptions</code> [ <code>-E</code> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] <code>-d </code><i>destination</i>[<code>/</code><i>instance</i>] [ <code>-l</code> ]<br />
 <code>lpoptions</code> [ <code>-E</code> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] [ <code>-p </code><i>destination</i>[<code>/</code><i>instance</i>] ] <code>-o </code><i>option</i>[<code>=</code><i>value</i>] &#8230;<br />
 <code>lpoptions</code> [ <code>-E</code> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] [ <code>-p </code><i>destination</i>[<code>/</code><i>instance</i>] ] <code>-r</code> <i>option</i><br />
 <code>lpoptions</code> [ <code>-E</code> ] [ <code>-h </code><i>server</i>[<code>:</code><i>port</i>] ] <code>-x </code><i>destination</i>[<code>/</code><i>instance</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>lpoptions</code> displays or sets printer options and defaults. If no printer is specified using the <i>-p</i> option, the default printer is used as described in <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1). </p>
<p> If no <i>-l</i>, <i>-o</i>, or <i>-r</i> options are specified, the current options are reported on the standard output. </p>
<p> Options set with the <code>lpoptions</code> command are used by the <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1) and <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1) commands when submitting jobs. </p>
<p> When run by the root user, <code>lpoptions</code> gets and sets default options and instances for all users in the <i>/etc/cups/lpoptions</i> file. Otherwise, the per-user defaults are managed in the <i>~/.cups/lpoptions</i> file.</p>
<h2>OPTIONS</h2>
<p> <code>lpoptions</code> supports the following options:</p>
<dl>
<dt><code>-E</code></p>
<dd> Enables encryption when communicating with the CUPS server.</p>
<dt><code>-d </code><i>destination</i>[<code>/</code><i>instance</i>]</p>
<dd> Sets the user default printer to <i>destination</i>. If <i>instance</i> is supplied then that particular instance is used. This option overrides the system default printer for the current user.</p>
<dt><code>-h </code><i>server</i>[<code>:</code><i>port</i>]</p>
<dd> Uses an alternate server.</p>
<dt><code>-l</code></p>
<dd> Lists the printer specific options and their current settings.</p>
<dt><code>-o </code><i>option</i>[<code>=</code><i>value</i>]</p>
<dd> Specifies a new option for the named destination.</p>
<dt><code>-p </code><i>destination</i>[<code>/</code><i>instance</i>]</p>
<dd> Sets the destination and instance, if specified, for any options that follow. If the named instance does not exist then it is created. Destinations can only be created using the <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8) program.</p>
<dt><code>-r </code><i>option</i></p>
<dd> Removes the specified option from the named destination.</p>
<dt><code>-x </code><i>destination</i>[<code>/</code><i>instance</i>]</p>
<dd> Removes the options for the named destination and instance, if specified. If the named instance does not exist then this does nothing. Destinations can only be removed using the <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8) command.</dl>
<h2>FILES</h2>
<p> <i>~/.cups/lpoptions</i> &#8211; user defaults and instances created by non-root users.<br />
 <i>/etc/cups/lpoptions</i> &#8211; system-wide defaults and instances created by the root user.</p>
<h2>CONFORMING TO</h2>
<p> The <code>lpoptions</code> command is unique to CUPS.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-cancel/">cancel</a></code>(1), <code><a href="/docs/linux/man/1-lp/">lp</a></code>(1), <code><a href="/docs/linux/man/8-lpadmin/">lpadmin</a></code>(8), <code><a href="/docs/linux/man/1-lpr/">lpr</a></code>(1), <code><a href="/docs/linux/man/1-lprm/">lprm</a></code>(1), CUPS Online Help (<a rel="nofollow" href="http://localhost:631/help)">http://localhost:631/help)</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021-2022 by OpenPrinting. </p>
<h2>Index</h2>
