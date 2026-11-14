---
title: "defaults(1)"
name: "defaults"
section: "1"
letter: "d"
url: "/docs/linux/man/1-defaults/"
description: "defaults – read or modify GNUstep user defaults"
---

<h2>NAME</h2>
<p> defaults &#8211; read or modify GNUstep user defaults </p>
<h2>SYNOPSIS</h2>
<p> <code>defaults [ action ]</code> </p>
<h2>DESCRIPTION</h2>
<p> The &#8216;defaults&#8217; command lets you to read and modify a user&#8217;s defaults. </p>
<p> This program replaces the old NeXTstep style dread, dwrite, and dremove programs. </p>
<p> If you have access to another user&#8217;s defaults database, you may include &#8216;-u username&#8217; before any other options to use that user&#8217;s database rather than your own. </p>
<p> defaults read [ domain [ key] ]</p>
<dl>
<dt>
<dd> read the named default from the specified domain. If no &#8216;key&#8217; is given &#8211; read all defaults from the domain. If no &#8216;domain&#8217; is given &#8211; read all defaults from all domains. A domain is either an application name, or &quot;NSGlobalDomain&quot;, for system level defauts. (Running programs can access two other domains, &quot;NSArgumentDomain&quot;, for command line arguments, &quot;NSRegistrationDomain&quot;, a second-chance domain in which &quot;defaults for defaults&quot; can be registered, and possibly domains for specific locales.)</dl>
<p> defaults readkey key</p>
<dl>
<dt>
<dd> read the named default from all domains.</dl>
<p> defaults write domain key value</p>
<dl>
<dt>
<dd> write &#8216;value&#8217; as default &#8216;key&#8217; in the specified domain. &#8216;value&#8217; must be a property list in single quotes.</dl>
<p> defaults write domain dictionary</p>
<dl>
<dt>
<dd> write &#8216;dictionary&#8217; as a replacement for the specified domain. &#8216;dictionary&#8217; must be a property list in single quotes.</dl>
<p> defaults write</p>
<dl>
<dt>
<dd> reads standard input for defaults in the format produced by &#8216;defaults read&#8217; and writes them to the database.</dl>
<p> defaults delete [ domain [ key] ]</p>
<dl>
<dt>
<dd> remove the specified default(s) from the domain. If no &#8216;key&#8217; is given &#8211; delete the entire domain.</dl>
<p> defaults delete</p>
<dl>
<dt>
<dd> read standard input for a series of lines containing pairs of domains and keys for defaults to be deleted.</dl>
<p> defaults domains</p>
<dl>
<dt>
<dd> lists the domains in the database (one per line)</dl>
<p> defaults find word</p>
<dl>
<dt>
<dd> searches domain names, default names, and default value strings for those equal to the specified word and lists them on standard output.</dl>
<p> defaults plist</p>
<dl>
<dt>
<dd> output some information about property lists</dl>
<p> defaults help</p>
<dl>
<dt>
<dd> list options for the defaults command. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>~/GNUstep/Defaults/.GNUstepDefaults</p>
<dd> holds defaults for a user </p>
</dl>
<h2>BUGS</h2>
<p> None known. </p>
<h2>DIAGNOSTICS</h2>
<p> Hopefully self-explanatory. </p>
<h2>HISTORY</h2>
<p> The &#8216;defaults&#8217; command appeared in OpenStep and combined the capabilities of the earlier NeXTstep commands &#8216;dread&#8217;, &#8216;dwrite&#8217;, and &#8216;dremove&#8217;.</p>
<dl>
<dt>
<dd> The GNUstep version was written in 1998. </p>
<p> This manual page first appeared in gnustep-base 1.9.2 (March 2004). </p>
</dl>
<h2>AUTHORS</h2>
<p> <code>defaults</code> was written by Richard Frith-Macdonald &lt;rfm [at] gnu.org&gt; </p>
<h2>Index</h2>
