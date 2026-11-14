---
title: "msiexec(1)"
name: "msiexec"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msiexec/"
description: "msiexec – Wine MSI Installer"
---

<h2 class="name">NAME</h2>
<p> msiexec &#8211; Wine MSI Installer </p>
<h2>SYNOPSIS</h2>
<p> <code>msiexec</code> <i>command</i> {<i>required parameter</i>} [<i>optional parameter</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>msiexec</code> is the Wine MSI installer, which is command line compatible with its Microsoft Windows counterpart.</p>
<h2>INSTALL OPTIONS</h2>
<dl>
<dt><code>/i&nbsp;</code>{<i>package</i>|<i>productcode</i>}&nbsp;[<i>property</i>=<i>foobar</i>]</p>
<dd> Install {package|productcode} with property=foobar.</p>
<dt><code>/a&nbsp;</code>{<i>package</i>|<i>productcode</i>}&nbsp;[<i>property</i>=<i>foobar</i>]</p>
<dd> Install {package|productcode} in administrator (network) mode.</p>
<dt><code>/x&nbsp;</code>{<i>package</i>|<i>productcode</i>}&nbsp;[<i>property</i>=<i>foobar</i>]</p>
<dd> Uninstall {package|productcode} with property=foobar.</p>
<dt><code>/uninstall&nbsp;</code>{<i>package</i>|<i>productcode</i>}&nbsp;[<i>property</i>=<i>foobar</i>]</p>
<dd> Same as <code>/x</code>.</dl>
<h2>REPAIR OPTIONS</h2>
<dl>
<dt><code>/f</code>&nbsp;[<code>p</code>|<code>o</code>|<code>e</code>|<code>d</code>|<code>c</code>|<code>a</code>|<code>u</code>|<code>m</code>|<code>s</code>|<code>v</code>]&nbsp;{<i>package</i>|<i>productcode</i>}</p>
<dd> Repair an installation. Default options are &#8216;omus&#8217;</p>
<dt><code>p</code></p>
<dd> Reinstall the file if it is missing.</p>
<dt><code>o</code></p>
<dd> Reinstall the file if it is missing or if any older version is installed.</p>
<dt><code>e</code></p>
<dd> Reinstall the file if it is missing, or if the installed version is equal or older.</p>
<dt><code>d</code></p>
<dd> Reinstall the file if it is missing or a different version is installed.</p>
<dt><code>c</code></p>
<dd> Reinstall the file if it is missing or the checksum does not match.</p>
<dt><code>a</code></p>
<dd> Reinstall all files.</p>
<dt><code>u</code></p>
<dd> Rewrite all required user registry entries.</p>
<dt><code>m</code></p>
<dd> Rewrite all required machine registry entries.</p>
<dt><code>s</code></p>
<dd> Overwrite any conflicting shortcuts.</p>
<dt><code>v</code></p>
<dd> Recache the local installation package from the source installation package.</dl>
<h2>PATCHING</h2>
<dl>
<dt><code>/p&nbsp;</code>{<i>patch</i>}&nbsp;[<i>property</i>=<i>foobar</i>]</p>
<dd> Apply <i>patch</i>. This should not be used with any of the above options.</dl>
<h2>UI CONTROL</h2>
<dl>
<dt><code>/q</code>[<code>n</code>|<code>b</code>|<code>r</code>|<code>f</code>]</p>
<dd> These options allow changing the behavior of the UI when installing MSI packages.</p>
<dt><code>/q</code></p>
<dd> Show no UI.</p>
<dt><code>/qn</p>
<dd> Same as /q</code>.</p>
<dt><code>/qb</p>
<dd> Show a basic UI.</p>
<dt>/qr</p>
<dd> Shows a reduced user UI.</p>
<dt>/qf</p>
<dd> Shows a full UI.</dl>
<p> </code></p>
<h2>LOGGING</h2>
<dl>
<dt><code>/l</code>[<code>*</code>][<code>i</code>|<code>w</code>|<code>e</code>|<code>a</code>|<code>r</code>|<code>u</code>|<code>c</code>|<code>m</code>|<code>o</code>|<code>p</code>|<code>v</code>][<code>+</code>|<code>!</code>]&nbsp;{<i>logfile</i>}</p>
<dd> Enable logging to <i>logfile</i>. Defaults are &#8216;iwearmo&#8217;.</p>
<dt><code>*</code></p>
<dd> Enable all logging options except &#8216;v&#8217; and &#8216;x&#8217;.</p>
<dt><code>i</code></p>
<dd> Log status messages.</p>
<dt><code>w</code></p>
<dd> Log nonfatal warnings.</p>
<dt><code>e</code></p>
<dd> Log all error messages.</p>
<dt><code>a</code></p>
<dd> Log start of actions.</p>
<dt><code>r</code></p>
<dd> Log action specific records.</p>
<dt><code>u</code></p>
<dd> Log user requests.</p>
<dt><code>c</code></p>
<dd> Log initial UI parameters.</p>
<dt><code>m</code></p>
<dd> Log out of memory errors.</p>
<dt><code>o</code></p>
<dd> Log out of diskspace messages.</p>
<dt><code>p </code></p>
<dd> Log terminal properties.</p>
<dt><code>v </code></p>
<dd> Verbose logging.</p>
<dt><code>x </code></p>
<dd> Log extra debugging messages.</p>
<dt><code>+ </code></p>
<dd> Append logging to existing file.</p>
<dt><code>! </code></p>
<dd> Flush each line to log.</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>/h</p>
<dd> Show help.</p>
<dt>/j</code>[<code>u</code>|<code>m</code>] {<i>package</i>|<i>productcode</i>} [<code>/t </code><i>transform</i>] [<code>/g </code><i>languageid</i>]</p>
<dd> Advertise <i>package</i> optionally with <code>/t </code><i>transform</i> and <code>/g </code><i>languageid</i>.</p>
<dt><code>/y</p>
<dd> Register MSI service.</p>
<dt>/z</p>
<dd> Unregister MSI service.</p>
<dt>/?</p>
<dd> Same as /h</code>. </p>
</dl>
<h2>BUGS</h2>
<p> Bugs can be reported on the <code>Wine bug tracker</code></p>
<h2>AVAILABILITY</h2>
<p> <code>msiexec</code> is part of the Wine distribution, which is available through WineHQ, the <code>Wine development headquarters</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wine/">wine</a></code>(1),<br />
 <code>Wine documentation and support</code> </p>
<h2>Index</h2>
