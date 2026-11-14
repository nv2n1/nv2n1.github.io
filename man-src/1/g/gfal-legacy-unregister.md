---
title: "gfal-legacy-unregister(1)"
name: "gfal-legacy-unregister"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfal-legacy-unregister/"
description: "gfal-legacy-unregister – register a replica"
---

<h2>NAME</h2>
<p> gfal-legacy-unregister &#8211; register a replica</p>
<h2>SYNOPSIS</h2>
<p> <code>gfal-legacy-unregister</code> [ <code>-h</code> ] [ <code>-V</code> ] [ <code>-v</code> ] [ <code>-D</code> <i>DEFINITION</i> ] [ <code>-C</code> <i>CLIENT-INFO</i> ] [ <code>-t</code> <i>TIMEOUT</i> ] <i> lfc surl</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>gfal-legacy-unregister</code> Removes a replica from a catalog </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> show help about the command.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> output version information and exit.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> verbose mode. Repeat up to 3 times for the most verbose mode.</p>
<dt><code>-D, &#8211;definition</code></p>
<dd> define properties for gfal2.</p>
<dt><code>-C, &#8211;client-info</code></p>
<dd> provide custom client-side information</p>
<dt><code>-t, &#8211;timeout</code></p>
<dd> global timeout for the execution of the command. Command is interrupted if time expires before it finishes.</p>
<dt><code>lfc</code></p>
<dd> LFC entry (lfc:// or guid:)</p>
<dt><code>surl</code></p>
<dd> Site URL </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gfal-legacy-unregister</code></p>
<dd> guid:12345-678-abcdef <a href="srm://endpoint.cern.ch/path/group">srm://endpoint.cern.ch/path/group</a> </p>
</dl>
<h2>FILES</h2>
<p> <i>/etc/gfal2.d/*</i></p>
<dl>
<dt>
<dd> All configuration files in this directory affect the behavior of the underlying gfal2. </p>
</dl>
<h2>AUTHORS</h2>
<p> Duarte Meneses &lt;duarte.meneses [at] cern.ch&gt;<br />
 Adrien Devresse &lt;adrien.devresse [at] cern.ch&gt;<br />
 Alejandro Alvarez Ayllon &lt;alejandro.alvarez.ayllon [at] cern.ch&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gfal-legacy-replicas/">gfal-legacy-replicas</a></code>(1), <code><a href="/docs/linux/man/1-gfal-legacy-register/">gfal-legacy-register</a></code>(1) </p>
<h2>Index</h2>
