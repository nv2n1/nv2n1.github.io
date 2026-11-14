---
title: "ncftool(1)"
name: "ncftool"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncftool/"
description: "ncftool – Network configuration tool"
---

<h2 class="name">NAME</h2>
<p> ncftool &#8211; Network configuration tool </p>
<h2>SYNOPSIS</h2>
<p> ncftool [command [options]]</p>
<h2>DESCRIPTION</h2>
<p> ncftool is a command line utility to configure networking. It can be invoked with no arguments to bring up the interactive ncftool shell. Alternatively a command and optional arguments can be specified to have ncftool execute the command non-interactively.</p>
<h2>COMMANDS</h2>
<h3><code>list [&#8211;macs] [&#8211;all] [&#8211;inactive]</code></h3>
<p> List the currently configured toplevel network interfaces</p>
<dl>
<dt><code>[&#8211;macs]</code> &#8211; show <font SIZE="-1">MAC</font> addresses</p>
<dd>
<dt><code>[&#8211;all]</code> &#8211; show all (up &amp; down) interfaces</p>
<dd>
<dt><code>[&#8211;inactive]</code> &#8211; show only inactive (down) interfaces</p>
<dd></dl>
<h3><code>dumpxml [&#8211;mac] [&#8211;live] name</code></h3>
<p> Dump the <font SIZE="-1">XML</font> description of an interface</p>
<dl>
<dt><code>[&#8211;mac]</code> &#8211; interpret the name as <font SIZE="-1">MAC</font> address</p>
<dd>
<dt><code>[&#8211;live]</code> &#8211; include information about the live interface</p>
<dd>
<dt><code>name</code> &#8211; the name of the interface</p>
<dd></dl>
<h3><code>define xmlfile</code></h3>
<p> Define an interface from the specified <font SIZE="-1">XML</font> file.</p>
<h3><code>undefine iface</code></h3>
<p> Remove the configuration of the specified interface.</p>
<h3><code>ifup iface</code></h3>
<p> Bring up specified interface.</p>
<h3><code>ifdown iface</code></h3>
<p> Bring down specified interface.</p>
<h3><code>change-begin</code></h3>
<p> Mark the beginning of a set of revertible network configuration changes.</p>
<h3><code>change-commit</code></h3>
<p> Commit (make permanent) a set of network configuration changes begun with <code>change-begin</code>.</p>
<h3><code>change-rollback</code></h3>
<p> Rollback (revert) a set of network configuration changes begun with <code>change-begin</code>.</p>
<h3><code>help [command]</code></h3>
<p> Print details about command, if specified, or list all commands if command is not specified.</p>
<h3>quit</h3>
<p> Exit the program.</p>
<h2>SEE ALSO</h2>
<p> interfaces (5)</p>
<h2>AUTHORS</h2>
<p> Please refer to the <font SIZE="-1">AUTHORS</font> file distributed with netcf. </p>
<h2>Index</h2>
<dt><a href="#lbAQ">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAR">AUTHORS</a></p>
<dd></dl>
