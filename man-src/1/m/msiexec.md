---
title: "msiexec(1)"
name: "msiexec"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msiexec/"
description: "msiexec – Wine MSI Installer"
---

<h2>SYNOPSIS</h2>
<p> <code>msiexec</code> <i>command</i> {<i>required parameter</i>} [<i>optional parameter</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>msiexec</code> is the Wine MSI installer, which is command line compatible with its Microsoft Windows counterpart.</p>
<h2>INSTALL OPTIONS</h2>
<dl>
<dt><code>/i&nbsp;</code>{<i>package</i>|<i>productcode</i>}&nbsp;[<i>property</i>=<i>foobar</i>]</dt>
<dd> Install {package|productcode} with property=foobar.</dd>
<dt><code>/a&nbsp;</code>{<i>package</i>|<i>productcode</i>}&nbsp;[<i>property</i>=<i>foobar</i>]</dt>
<dd> Install {package|productcode} in administrator (network) mode.</dd>
<dt><code>/x&nbsp;</code>{<i>package</i>|<i>productcode</i>}&nbsp;[<i>property</i>=<i>foobar</i>]</dt>
<dd> Uninstall {package|productcode} with property=foobar.</dd>
<dt><code>/uninstall&nbsp;</code>{<i>package</i>|<i>productcode</i>}&nbsp;[<i>property</i>=<i>foobar</i>]</dt>
<dd> Same as <code>/x</code>.</dd></dl>
<h2>REPAIR OPTIONS</h2>
<dl>
<dt><code>/f</code>&nbsp;[<code>p</code>|<code>o</code>|<code>e</code>|<code>d</code>|<code>c</code>|<code>a</code>|<code>u</code>|<code>m</code>|<code>s</code>|<code>v</code>]&nbsp;{<i>package</i>|<i>productcode</i>}</dt>
<dd> Repair an installation. Default options are &#8216;omus&#8217;</dd>
<dt><code>p</code></dt>
<dd> Reinstall the file if it is missing.</dd>
<dt><code>o</code></dt>
<dd> Reinstall the file if it is missing or if any older version is installed.</dd>
<dt><code>e</code></dt>
<dd> Reinstall the file if it is missing, or if the installed version is equal or older.</dd>
<dt><code>d</code></dt>
<dd> Reinstall the file if it is missing or a different version is installed.</dd>
<dt><code>c</code></dt>
<dd> Reinstall the file if it is missing or the checksum does not match.</dd>
<dt><code>a</code></dt>
<dd> Reinstall all files.</dd>
<dt><code>u</code></dt>
<dd> Rewrite all required user registry entries.</dd>
<dt><code>m</code></dt>
<dd> Rewrite all required machine registry entries.</dd>
<dt><code>s</code></dt>
<dd> Overwrite any conflicting shortcuts.</dd>
<dt><code>v</code></dt>
<dd> Recache the local installation package from the source installation package.</dd></dl>
<h2>PATCHING</h2>
<dl>
<dt><code>/p&nbsp;</code>{<i>patch</i>}&nbsp;[<i>property</i>=<i>foobar</i>]</dt>
<dd> Apply <i>patch</i>. This should not be used with any of the above options.</dd></dl>
<h2>UI CONTROL</h2>
<dl>
<dt><code>/q</code>[<code>n</code>|<code>b</code>|<code>r</code>|<code>f</code>]</dt>
<dd> These options allow changing the behavior of the UI when installing MSI packages.</dd>
<dt><code>/q</code></dt>
<dd> Show no UI.</dd>
<dt><code>/qn</dt>
<dd> Same as /q</code>.</dd>
<dt><code>/qb</dt>
<dd> Show a basic UI.</dd>
<dt>/qr</dt>
<dd> Shows a reduced user UI.</dd>
<dt>/qf</dt>
<dd> Shows a full UI.</dd></dl>
<p> </code></p>
<h2>LOGGING</h2>
<dl>
<dt><code>/l</code>[<code>*</code>][<code>i</code>|<code>w</code>|<code>e</code>|<code>a</code>|<code>r</code>|<code>u</code>|<code>c</code>|<code>m</code>|<code>o</code>|<code>p</code>|<code>v</code>][<code>+</code>|<code>!</code>]&nbsp;{<i>logfile</i>}</dt>
<dd> Enable logging to <i>logfile</i>. Defaults are &#8216;iwearmo&#8217;.</dd>
<dt><code>*</code></dt>
<dd> Enable all logging options except &#8216;v&#8217; and &#8216;x&#8217;.</dd>
<dt><code>i</code></dt>
<dd> Log status messages.</dd>
<dt><code>w</code></dt>
<dd> Log nonfatal warnings.</dd>
<dt><code>e</code></dt>
<dd> Log all error messages.</dd>
<dt><code>a</code></dt>
<dd> Log start of actions.</dd>
<dt><code>r</code></dt>
<dd> Log action specific records.</dd>
<dt><code>u</code></dt>
<dd> Log user requests.</dd>
<dt><code>c</code></dt>
<dd> Log initial UI parameters.</dd>
<dt><code>m</code></dt>
<dd> Log out of memory errors.</dd>
<dt><code>o</code></dt>
<dd> Log out of diskspace messages.</dd>
<dt><code>p </code></dt>
<dd> Log terminal properties.</dd>
<dt><code>v </code></dt>
<dd> Verbose logging.</dd>
<dt><code>x </code></dt>
<dd> Log extra debugging messages.</dd>
<dt><code>+ </code></dt>
<dd> Append logging to existing file.</dd>
<dt><code>! </code></dt>
<dd> Flush each line to log.</dd></dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>/h</dt>
<dd> Show help.</dd>
<dt>/j</code>[<code>u</code>|<code>m</code>] {<i>package</i>|<i>productcode</i>} [<code>/t </code><i>transform</i>] [<code>/g </code><i>languageid</i>]</dt>
<dd> Advertise <i>package</i> optionally with <code>/t </code><i>transform</i> and <code>/g </code><i>languageid</i>.</dd>
<dt><code>/y</dt>
<dd> Register MSI service.</dd>
<dt>/z</dt>
<dd> Unregister MSI service.</dd>
<dt>/?</dt>
<dd> Same as /h</code>. </dd>
</dl>
<h2>BUGS</h2>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AVAILABILITY</h2>
<p> <code>msiexec</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1),<br />
 <code>Wine documentation and support</code> </p>
