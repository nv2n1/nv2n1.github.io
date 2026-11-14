---
title: "mhparam(1)"
name: "mhparam"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mhparam/"
description: "mhparam – print nmh profile and context components"
---

<h2 class="name">NAME</h2>
<p> mhparam &#8211; print nmh profile and context components </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>mhparam</code> [<i>components</i>] [<code>-all</code>] [<code>-component</code> | <code>-nocomponent</code>] [<code>-version</code>] [<code>-help</code>] [<code>-debug</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>mhparam</code></p>
<dd>writes the value of the specified profile component to the standard output separated by newlines. Component name matching is case-insensitive. If the profile component is not present, the default value (or nothing if there is no default) is printed. </p>
<p> If the switch <code>-component</code> is given, then the component name is displayed along with the profile components value. This can be disabled with the switch <code>-nocomponent</code>. </p>
<p> If more than one component is specified in the <i>components</i> list, then the switch <code>-component</code> is on by default. If only one component is specified, then the switch <code>-nocomponent</code> is on by default. </p>
<p> If <code>-all</code> is specified, then all components in the nmh profile are displayed and other arguments are ignored. </p>
<p> <code>mhparam</code> can provide other information, such as the <code>nmh</code> version identifier, the locations of the nmh <i>etcdir</i> and <i>libdir</i> install directories, all <i>proc</i> settings, and the <i>datalocking</i> method described in the <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5) man page. Information about the configuration of the <code>nmh</code> installation is also available, including the default mail spool locking method. To test whether the configuration includes support for SASL, TLS, and <i><a href="/docs/linux/man/3-iconv/">iconv</a></i>(3), the following commands, respectively, will output a non-null string to indicate support: </p>
<dl>
<dt>
<dd>
<pre>
mhparam sasl
mhparam tls
mhparam iconv
</pre>
</dl>
<p> Conversely, no output means that the specified support is not included. The <code>-debug</code> switch displays all such other information available from <code>mhparam</code>. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
% mhparam path
Mail
% mhparam mhlproc
/usr/libexec/nmh/mhl
% mhparam -component Path
Path: Mail
% mhparam AliasFile rmmproc
AliasFile: aliases
rmmproc: rmmproc
% mhparam -nocomponent AliasFile rmmproc
aliases
rmmproc
% mhparam path nonexistent context
Path: Mail
context: context
% mhparam version
nmh-1.6
% mhparam etcdir
/etc/nmh
% mhparam libdir
/usr/libexec/nmh
% mhparam spoollocking
fcntl
% mhparam datalocking
fcntl
% mhparam sasl
cyrus_sasl
% mhparam tls
tls
% mhparam iconv
iconv
</pre>
</dl>
<p> <code>mhparam</code> is also useful in backquoted operations: </p>
<dl>
<dt>
<dd>
<pre>
% fgrep cornell.edu `mhpath +`/`mhparam aliasfile`
</pre>
</dl>
<h2>EXIT STATUS</h2>
<p> <code>mhparam</code> returns the number of components that were not found.</p>
<h2>FILES</h2>
<pre>
^$HOME/.mh_profile~^The user profile
^or $MH~^Rather than the standard profile
^&lt;mh-dir&gt;/context~^The user context
^or $MHCONTEXT~^Rather than the standard context
</pre>
<h2>PROFILE COMPONENTS</h2>
<pre>
^context:~^To determine the context file
</pre>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/5-mh-profile/">mh-profile</a></i>(5)</p>
<h2>DEFAULTS</h2>
<pre>
`<code>-nocomponent</code>' if only one component is specified
`<code>-component</code>' if more than one component is specified
`<code>components</code>' defaults to none
</pre>
<h2>CONTEXT</h2>
<p> None </p>
<h2>Index</h2>
