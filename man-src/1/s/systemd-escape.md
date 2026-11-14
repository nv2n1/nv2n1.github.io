---
title: "systemd-escape(1)"
name: "systemd-escape"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-escape/"
description: "systemd-escape – Escape strings for usage in systemd unit names"
---

<h2 class="name">NAME</h2>
<p> systemd-escape &#8211; Escape strings for usage in systemd unit names </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-escape</code> [OPTIONS&#8230;] [STRING&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-escape</code></p>
<dd>may be used to escape strings for inclusion in systemd unit names. The command may be used to escape and to undo escaping of strings. </p>
<p> The command takes any number of strings on the command line, and will process them individually, one after another. It will output them separated by spaces to stdout. </p>
<p> By default, this command will escape the strings passed, unless <code>&#8211;unescape</code> is passed which results in the inverse operation being applied. If <code>&#8211;mangle</code> is given, a special mode of escaping is applied instead, which assumes the string is already escaped but will escape everything that appears obviously non-escaped. </p>
<p> For details on the escaping and unescaping algorithms see the relevant section in <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5).</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;suffix=</code></p>
<dl>
<dt>
<dd> Appends the specified unit type suffix to the escaped string. Takes one of the unit types supported by systemd, such as &quot;service&quot; or &quot;mount&quot;. May not be used in conjunction with <code>&#8211;template=</code>, <code>&#8211;unescape</code> or <code>&#8211;mangle</code>.</dl>
<p> <code>&#8211;template=</code></p>
<dl>
<dt>
<dd> Inserts the escaped strings in a unit name template. Takes a unit name template such as foobar [at] .service. With <code>&#8211;unescape</code>, expects instantiated unit names for this template and extracts and unescapes just the instance part. May not be used in conjunction with <code>&#8211;suffix=</code>, <code>&#8211;instance</code> or <code>&#8211;mangle</code>.</dl>
<p> <code>&#8211;path</code>, <code>-p</code></p>
<dl>
<dt>
<dd> When escaping or unescaping a string, assume it refers to a file system path. This eliminates leading, trailing or duplicate &quot;/&quot; characters and rejects &quot;.&quot; and &quot;..&quot; path components. This is particularly useful for generating strings suitable for unescaping with the &quot;%f&quot; specifier in unit files, see <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5).</dl>
<p> <code>&#8211;unescape</code>, <code>-u</code></p>
<dl>
<dt>
<dd> Instead of escaping the specified strings, undo the escaping, reversing the operation. May not be used in conjunction with <code>&#8211;suffix=</code> or <code>&#8211;mangle</code>.</dl>
<p> <code>&#8211;mangle</code>, <code>-m</code></p>
<dl>
<dt>
<dd> Like <code>&#8211;escape</code>, but only escape characters that are obviously not escaped yet, and possibly automatically append an appropriate unit type suffix to the string. May not be used in conjunction with <code>&#8211;suffix=</code>, <code>&#8211;template=</code> or <code>&#8211;unescape</code>.</dl>
<p> <code>&#8211;instance</code></p>
<dl>
<dt>
<dd> With <code>&#8211;unescape</code>, unescape and print only the instance part of an instantiated unit name template. Results in an error for an uninstantiated template like ssh [at] .service or a non-template name like ssh.service. Must be used in conjunction with <code>&#8211;unescape</code> and may not be used in conjunction with <code>&#8211;template</code>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>EXAMPLES</h2>
<p> To escape a single string: </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-escape 'Hallöchen, Meister'
Hallöchen, Meister
</pre>
</dl>
<p> To undo escaping on a single string: </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-escape -u 'Hallöchen, Meister'
Hallöchen, Meister
</pre>
</dl>
<p> To generate the mount unit for a path: </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-escape -p --suffix=mount &quot;/tmp//waldi/foobar/&quot;
tmp-waldi-foobar.mount
</pre>
</dl>
<p> To generate instance names of three strings: </p>
<dl>
<dt>
<dd>
<pre><code>
$ systemd - escape-- template = systemd - nspawn[at].service 'My Container 1' 'containerb' 'container/III' systemd - nspawn @My Container 1.service systemd - nspawn[at] containerb.service systemd - nspawn[at] container - III.service
</code></pre>
</dl>
<p> To extract the instance part of an instantiated unit: </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-escape -u --instance 'systemd-nspawn@My Container 1.service'
My Container 1
</pre>
</dl>
<p> To extract the instance part of an instance of a particular template: </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-escape -u --template=systemd-nspawn [at] .service 'systemd-nspawn@My Container 1.service'
My Container 1
</pre>
</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-unit/">systemd.unit</a></code>(5), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) </p>
<h2>Index</h2>
