---

title: "gfal-legacy-unregister(1)"
name: "gfal-legacy-unregister"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfal-legacy-unregister/"
description: "gfal-legacy-unregister – register a replica"
---

<p> gfal-legacy-unregister &#8211; register a replica</p>
<h2>SYNOPSIS</h2>
<p> <code>gfal-legacy-unregister</code> [ <code>-h</code> ] [ <code>-V</code> ] [ <code>-v</code> ] [ <code>-D</code> <i>DEFINITION</i> ] [ <code>-C</code> <i>CLIENT-INFO</i> ] [ <code>-t</code> <i>TIMEOUT</i> ] <i> lfc surl</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>gfal-legacy-unregister</code> Removes a replica from a catalog </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> show help about the command.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> output version information and exit.</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> verbose mode. Repeat up to 3 times for the most verbose mode.</dd>
<dt><code>-D, &#8211;definition</code></dt>
<dd> define properties for gfal2.</dd>
<dt><code>-C, &#8211;client-info</code></dt>
<dd> provide custom client-side information</dd>
<dt><code>-t, &#8211;timeout</code></dt>
<dd> global timeout for the execution of the command. Command is interrupted if time expires before it finishes.</dd>
<dt><code>lfc</code></dt>
<dd> LFC entry (lfc:// or guid:)</dd>
<dt><code>surl</code></dt>
<dd> Site URL </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gfal-legacy-unregister</code></dt>
<dd> guid:12345-678-abcdef <a href="srm://endpoint.cern.ch/path/group">srm://endpoint.cern.ch/path/group</a> </dd>
</dl>
<h2>FILES</h2>
<p> <i>/etc/gfal2.d/*</i></p>
<dl>
<dt>
</dt><dd> All configuration files in this directory affect the behavior of the underlying gfal2. </dd>
</dl>
<h2>AUTHORS</h2>
<p> Duarte Meneses &lt;duarte.meneses [at] cern.ch&gt;<br/>
 Adrien Devresse &lt;adrien.devresse [at] cern.ch&gt;<br/>
 Alejandro Alvarez Ayllon &lt;alejandro.alvarez.ayllon [at] cern.ch&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gfal-legacy-replicas/">gfal-legacy-replicas</a></code>(1), <code><a href="/docs/linux/man/1-gfal-legacy-register/">gfal-legacy-register</a></code>(1) </p>
