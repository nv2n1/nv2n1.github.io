---
title: "dpkg-trigger(1)"
name: "dpkg-trigger"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-trigger/"
description: "dpkg-trigger – a package trigger utility"
---

<h2 class="name">NAME</h2>
<p> dpkg-trigger &#8211; a package trigger utility </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-trigger</code> [<i>option</i>&#8230;] <i>trigger-name</i> </p>
<p> <code>dpkg-trigger</code> [<i>option</i>&#8230;] <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-trigger</code> is a tool to explicitly activate triggers and check for its support on the running <code>dpkg</code>. </p>
<p> This can be used by maintainer scripts in complex and conditional situations where the file triggers, or the declarative <code>activate</code> triggers control file directive, are insufficiently rich. It can also be used for testing and by system administrators (but note that the triggers won&#8217;t actually be run by <code>dpkg-trigger</code>). </p>
<p> Unrecognized trigger name syntaxes are an error for <code>dpkg-trigger</code>.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>&#8211;check-supported</code></p>
<dd> Check if the running <code>dpkg</code> supports triggers (usually called from a postinst). Will exit <code>0</code> if a triggers-capable <code>dpkg</code> has run, or <code>1</code> with an error message to stderr if not. Normally, however, it is better just to activate the desired trigger with <code>dpkg-trigger</code>.</p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;admindir=</code><i>dir</i></p>
<dd> Change the location of the <code>dpkg</code> database. The default location is <i>/var/lib/dpkg</i>.</p>
<dt><code>&#8211;root=</code><i>directory</i></p>
<dd> Set the root directory to <i>directory</i>, which sets the administrative directory to &laquo;<i>directory</i>/var/lib/dpkg&raquo; (since dpkg 1.21.0).</p>
<dt><code>&#8211;by-package=</code><i>package</i></p>
<dd> Override trigger awaiter (normally set by <code>dpkg</code> through the <font SIZE="-1"><code>DPKG_MAINTSCRIPT_PACKAGE</code></font> environment variable of the maintainer scripts, naming the package to which the script belongs, and this will be used by default).</p>
<dt><code>&#8211;no-await</code></p>
<dd> This option arranges that the calling package <i>T</i> (if any) need not await the processing of this trigger; the interested package(s) <i>I</i>, will not be added to <i>T</i>&#8216;s trigger processing awaited list and <i>T</i>&#8216;s status is unchanged. <i>T</i> may be considered installed even though <i>I</i> may not yet have processed the trigger.</p>
<dt><code>&#8211;await</code></p>
<dd> This option does the inverse of <code>&#8211;no-await</code> (since dpkg 1.17.21). If the interested package has declared a &#8220;noawait&#8221; directive, then this option will not be effective. It is currently the default behavior.</p>
<dt><code>&#8211;no-act</code></p>
<dd> Just test, do not actually change anything.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> The requested action was successfully performed. Or a check or assertion command returned true.</p>
<dt><code>1</code></p>
<dd> A check or assertion command returned false.</p>
<dt><code>2</code></p>
<dd> Fatal or unrecoverable error due to invalid command-line usage, or interactions with the system, such as accesses to the database, memory allocations, etc.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DPKG_ROOT</code></font></p>
<dd> If set and the <code>&#8211;root</code> option has not been specified, it will be used as the filesystem root directory (since dpkg 1.21.0).</p>
<dt><font SIZE="-1"><code>DPKG_ADMINDIR</code></font></p>
<dd> If set and the <code>&#8211;admindir</code> option has not been specified, it will be used as the <code>dpkg</code> data directory.</p>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1), <code><a href="/docs/linux/man/5-deb-triggers/">deb-triggers</a></code>(5), <code>/usr/share/doc/dpkg/triggers.txt.gz</code>. </p>
<h2>Index</h2>
