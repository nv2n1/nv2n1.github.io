---
title: "pdcp(1)"
name: "pdcp"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdcp/"
description: "pdcp – copy files to groups of hosts in parallel rpdcp – (reverse pdcp) copy files from a group of hosts in parallel"
---

<h2 class="name">NAME</h2>
<p> pdcp &#8211; copy files to groups of hosts in parallel<br />
 rpdcp &#8211; (reverse pdcp) copy files from a group of hosts in parallel</p>
<h2>SYNOPSIS</h2>
<p> <code>pdcp</code> [<i>options</i>]&#8230; src [src2&#8230;] dest<br />
 <code>rpdcp</code> [<i>options</i>]&#8230; src [src2&#8230;] dir </p>
<h2>DESCRIPTION</h2>
<p> <code>pdcp</code> is a variant of the <a href="/docs/linux/man/1-rcp/">rcp</a>(1) command. Unlike <a href="/docs/linux/man/1-rcp/">rcp</a>(1), which copies files to a single remote host, <code>pdcp</code> can copy files to multiple remote hosts in parallel. However, <code>pdcp</code> does not recognize files in the format &#8220;rname [at] rhost:path,&#8221; therefore all source files must be on the local host machine. Destination nodes must be listed on the <code>pdcp</code> command line using a suitable target nodelist option (See the <i>OPTIONS</i> section below). Each destination node listed must have <code>pdcp</code> installed for the copy to succeed. </p>
<p> When <code>pdcp</code> receives SIGINT (ctrl-C), it lists the status of current threads. A second SIGINT within one second terminates the program. Pending threads may be canceled by issuing ctrl-Z within one second of ctrl-C. Pending threads are those that have not yet been initiated, or are still in the process of connecting to the remote host. </p>
<p> Like <a href="/docs/linux/man/1-pdsh/">pdsh</a>(1), the functionality of <code>pdcp</code> may be supplemented by dynamically loadable modules. In <code>pdcp</code>, the modules may provide a new connect protocol (replacing the standard <a href="/docs/linux/man/1-rsh/">rsh</a>(1) protocol), filtering options (e.g. excluding hosts that are down), and/or host selection options (e.g. <i>-a</i> selects all nodes from a local config file). By default, <code>pdcp</code> requires at least one &quot;rcmd&quot; module to be loaded (to provide the channel for remote copy). </p>
<h2>REVERSE PDCP</h2>
<p> <code>rpdcp</code> performs a reverse parallel copy. Rather than copying files to remote hosts, files are retrieved from remote hosts and stored locally. All directories or files retrieved will be stored with their remote hostname appended to the filename. The destination file must be a directory when this option is used. </p>
<p> In other respects, <code>rpdcp</code> is exactly like <code>pdcp</code>, and further statements regarding <code>pdcp</code> in this manual also apply to <code>rpdcp</code>. </p>
<h2>RCMD MODULES</h2>
<p> The method by which <code>pdcp</code> connects to remote hosts may be selected at runtime using the <i>-R</i> option (See <i>OPTIONS</i> below). This functionality is ultimately implemented via dynamically loadable modules, and so the list of available options may be different from installation to installation. A list of currently available rcmd modules is printed when using any of the <i>-h</i>, <i>-V</i>, or <i>-L</i> options. The default rcmd module will also be displayed with the <i>-h</i> and <i>-V</i> options. </p>
<p> A list of <i>rcmd</i> modules currently distributed with <code>pdcp</code> follows.</p>
<dl>
<dt>rsh</p>
<dd> Uses an internal, thread-safe implementation of BSD <a href="/docs/linux/man/3-rcmd/">rcmd</a>(3) to run commands using the standard <a href="/docs/linux/man/1-rsh/">rsh</a>(1) protocol.</p>
<dt>ssh</p>
<dd> Uses a variant of <a href="/docs/linux/man/3-popen/">popen</a>(3) to run multiple copies of the <a href="/docs/linux/man/1-ssh/">ssh</a>(1) command.</p>
<dt>mrsh</p>
<dd> This module uses the <a href="/docs/linux/man/1-mrsh/">mrsh</a>(1) protocol to execute jobs on remote hosts. The mrsh protocol uses a credential based authentication, forgoing the need to allocate reserved ports. In other aspects, it acts just like rsh.</p>
<dt>krb4</p>
<dd> The krb4 module allows users to execute remote commands after authenticating with kerberos. Of course, the remote rshd daemons must be kerberized.</p>
<dt>xcpu</p>
<dd> The xcpu module uses the xcpu service to execute remote commands. </p>
</dl>
<h2>OPTIONS</h2>
<p> The list of available <code>pdcp</code> options is determined at runtime by supplementing the list of standard <code>pdcp</code> options with any options provided by loaded <i>rcmd</i> and <i>misc</i> modules. In some cases, options provided by modules may conflict with each other. In these cases, the modules are incompatible and the first module loaded wins. </p>
<h2>Standard target nodelist options</h2>
<dl>
<dt><code>-w</code> <i>TARGETS,&#8230;</i></p>
<dd> Target and or filter the specified list of hosts. Do not use with any other node selection options (e.g. <i>-a</i>, <i>-g</i>, if they are available). No spaces are allowed in the comma-separated list. Arguments in the <i>TARGETS</i> list may include normal host names, a range of hosts in hostlist format (See <code>HOSTLIST EXPRESSIONS</code>), or a single `-&#8216; character to read the list of hosts on stdin. </p>
<p> If a host or hostlist is preceded by a `-&#8216; character, this causes those hosts to be explicitly excluded. If the argument is preceded by a single `^&#8217; character, it is taken to be the path to file containing a list of hosts, one per line. If the item begins with a `/&#8217; character, it is taken as a regular expression on which to filter the list of hosts (a regex argument may also be optionally trailed by another &#8216;/&#8217;, e.g. /node.*/). A regex or file name argument may also be preceeded by a minus `-&#8216; to exclude instead of include thoses hosts. </p>
<p> A list of hosts may also be preceded by &quot;user@&quot; to specify a remote username other than the default, or &quot;rcmd_type:&quot; to specify an alternate rcmd connection type for these hosts. When used together, the rcmd type must be specified first, e.g. &quot;ssh:user1 [at] host0&quot; would use ssh to connect to host0 as user &quot;user1.&quot; </p>
<dt><i></i><code>-x</code> <i>host,host,&#8230;</i></p>
<dd> Exclude the specified hosts. May be specified in conjunction with other target node list options such as <i>-a</i> and <i>-g</i> (when available). Hostlists may also be specified to the <i>-x</i> option (see the <code>HOSTLIST EXPRESSIONS</code> section below). Arguments to <i>-x</i> may also be preceeded by the filename (`^&#8217;) and regex (&#8216;/&#8217;) characters as described above, in which case the resulting hosts are excluded as if they had been given to <code>-w</code> and preceeded with the minus `-&#8216; character. </p>
</dl>
<h2>Standard pdcp options</h2>
<dl>
<dt><i>-h</i></p>
<dd> Output usage menu and quit. A list of available rcmd modules will be printed at the end of the usage message.</p>
<dt><i>-q</i></p>
<dd> List option values and the target nodelist and exit without action.</p>
<dt><i>-b</i></p>
<dd> Disable ctrl-C status feature so that a single ctrl-C kills parallel copy. (Batch Mode)</p>
<dt><i>-r</i></p>
<dd> Copy directories recursively.</p>
<dt><i>-p</i></p>
<dd> Preserve modification time and modes.</p>
<dt><i>-e PATH</i></p>
<dd> Explicitly specify path to remote <code>pdcp</code> binary instead of using the locally executed path. Can also be set via the environment variable PDSH_REMOTE_PDCP_PATH.</p>
<dt><i>-l user</i></p>
<dd> This option may be used to copy files as another user, subject to authorization. For BSD rcmd, this means the invoking user and system must be listed in the user&#8217;s .rhosts file (even for root).</p>
<dt><i>-t seconds</i></p>
<dd> Set the connect timeout. Default is 10 seconds.</p>
<dt><i>-f number</i></p>
<dd> Set the maximum number of simultaneous remote copies to <i>number</i>. The default is 32.</p>
<dt><i>-R name</i></p>
<dd> Set rcmd module to <i>name</i>. This option may also be set via the PDSH_RCMD_TYPE environment variable. A list of available rcmd modules may be obtained via either the <i>-h</i> or <i>-L</i> options.</p>
<dt><i>-M name,&#8230;</i></p>
<dd> When multiple <code>misc</code> modules provide the same options to <code>pdsh</code>, the first module initialized &quot;wins&quot; and subsequent modules are not loaded. The <i>-M</i> option allows a list of modules to be specified that will be force-initialized before all others, in-effect ensuring that they load without conflict (unless they conflict with eachother). This option may also be set via the PDSH_MISC_MODULES environment variable.</p>
<dt><i>-L</i></p>
<dd> List info on all loaded <code>pdcp</code> modules and quit.</p>
<dt><i>-d</i></p>
<dd> Include more complete thread status when SIGINT is received, and display connect and command time statistics on stderr when done.</p>
<dt><i>-V</i></p>
<dd> Output <code>pdcp</code> version information, along with list of currently loaded modules, and exit. </p>
</dl>
<h2>HOSTLIST EXPRESSIONS</h2>
<p> As noted in sections above, <code>pdcp </code> accepts ranges of hostnames in the general form: prefix[n-m,l-k,&#8230;], where n &lt; m and l &lt; k, etc., as an alternative to explicit lists of hosts. This form should not be confused with regular expression character classes (also denoted by &#8220;[]&#8221;). For example, foo[19] does not represent foo1 or foo9, but rather represents a degenerate range: foo19. </p>
<p> This range syntax is meant only as a convenience on clusters with a prefixNN naming convention and specification of ranges should not be considered necessary &#8212; the list foo1,foo9 could be specified as such, or by the range foo[1,9]. </p>
<p> Some examples of range usage follow: </p>
<pre><code>
Copy / etc / hosts to foo01, foo02, ..., foo05 pdcp - w foo[01 - 05] / etc / hosts / etc Copy / etc / hosts to foo7, foo9, foo10 pdcp - w foo[7, 9 - 10] / etc / hosts / etc Copy / etc / hosts to foo0, foo4, foo5 pdcp - w foo[0 - 5] - x foo[1 - 3] / etc / hosts / etc
</code></pre>
<p> As a reminder to the reader, some shells will interpret brackets (&#8216;[&#8216; and &#8216;]&#8217;) for pattern matching. Depending on your shell, it may be necessary to enclose ranged lists within quotes. For example, in tcsh, the first example above should be executed as: </p>
<p>&nbsp;<wbr>pdcp -w&nbsp;<wbr>&quot;foo[01-05]&quot;&nbsp;<wbr>/etc/hosts&nbsp;<wbr>/etc </p>
<h2>ORIGIN</h2>
<p> Pdsh/pdcp was originally a rewrite of IBM <a href="/docs/linux/man/1-dsh/">dsh</a>(1) by Jim Garlick &lt;garlick [at] llnl.gov&gt; on LLNL&#8217;s ASCI Blue-Pacific IBM SP system. It is now also used on Linux clusters at LLNL. </p>
<h2>LIMITATIONS</h2>
<p> When using <code>ssh </code> for remote execution, stderr of ssh to be folded in with that of the remote command. When invoked by pdcp, it is not possible for ssh to prompt for confirmation if a host key changes, prompt for passwords if RSA keys are not configured properly, etc.. Finally, the connect timeout is only adjustable with ssh when the underlying ssh implementation supports it, and pdsh has been built to use the correct option. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-pdsh/">pdsh</a>(1) </p>
<h2>Index</h2>
