---
title: "getfattr(1)"
name: "getfattr"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getfattr/"
description: "getfattr – get extended attributes of filesystem objects"
---

<h2 class="name">NAME</h2>
<p> getfattr &#8211; get extended attributes of filesystem objects </p>
<h2>SYNOPSIS</h2>
<pre><code>
getfattr[-hRLP] - n name[-e en] pathname... getfattr[-hRLP] - d[-e en][-m pattern] pathname...
</code></pre>
<h2>DESCRIPTION</h2>
<p> For each file, <code>getfattr</code> displays the file name, and the set of extended attribute names (and optionally values) which are associated with that file. Per default only attributes in the user namespace are displayed, see <code>-m</code>. </p>
<p> The output format of <code>getfattr -d</code> is as follows:</p>
<dl>
<dt>
<dd>
<pre>
 1:  # file: somedir/
 2:  user.name0=&quot;value0&quot;
 3:  user.name1=&quot;value1&quot;
 4:  user.name2=&quot;value2&quot;
 5:  ...
</pre>
</dl>
<p> Line 1 identifies the file name for which the following lines are being reported. The remaining lines (lines 2 to 4 above) show the <i>name</i> and <i>value</i> pairs associated with the specified file.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code> <i>name</i>, <code>&#8211;name</code>=<i>name</i></p>
<dd> Dump the value of the named extended attribute.</p>
<dt><code>-d</code>, <code>&#8211;dump</code></p>
<dd> Dump the values of all matched extended attributes.</p>
<dt><code>-e</code> <i>en</i>, <code>&#8211;encoding</code>=<i>en</i></p>
<dd> Encode values after retrieving them. Valid values of <i>en</i> are &quot;text&quot;, &quot;hex&quot;, and &quot;base64&quot;. Values encoded as text strings are enclosed in double quotes (&quot;), while strings encoded as hexadecimal and base64 are prefixed with 0x and 0s, respectively.</p>
<dt><code>-h</code>, <code>&#8211;no-dereference</code></p>
<dd> Do not dereference symlinks. Instead of the file a symlink refers to, the symlink itself is examined. Unless doing a logical (-L) traversal, do not traverse symlinks to directories.</p>
<dt><code>-m</code> <i>pattern</i>, <code>&#8211;match</code>=<i>pattern</i></p>
<dd> Only include attributes with names matching the regular expression <i>pattern</i>. The default value for <i>pattern</i> is &quot;^user\.&quot;, which includes all the attributes in the user namespace. Specify &quot;-&quot; for including all attributes. Refer to <code><a href="/docs/linux/man/5-attr/">attr</a></code>(5) for a more detailed discussion of namespaces.</p>
<dt><code>&#8211;absolute-names</code></p>
<dd> Do not strip leading slash characters (&#8216;/&#8217;). The default behaviour is to strip leading slash characters.</p>
<dt><code>&#8211;only-values</code></p>
<dd> Dump out the raw extended attribute value(s) without encoding them.</p>
<dt><code>-R</code>, <code>&#8211;recursive</code></p>
<dd> List the attributes of all files and directories recursively.</p>
<dt><code>-L</code>, <code>&#8211;logical</code></p>
<dd> Logical walk, follow symbolic links to directories. The default behaviour is to follow symbolic link arguments unless &#8211;no-dereference is given, and to skip symbolic links encountered in subdirectories. Only effective in combination with -R.</p>
<dt><code>-P</code>, <code>&#8211;physical</code></p>
<dd> Physical walk, do not follow symbolic links to directories. This also skips symbolic link arguments. Only effective in combination with -R.</p>
<dt><code>&#8211;version</code></p>
<dd> Print the version of <code>getfattr</code> and exit.</p>
<dt><code>&#8211;help</code></p>
<dd> Print help explaining the command line options.</p>
<dt><code>&#8212;</code></p>
<dd> End of command line options. All remaining parameters are interpreted as file names, even if they start with a dash character.</dl>
<h2>AUTHOR</h2>
<p> Andreas Gruenbacher, &lt;<i>a.gruenbacher [at] bestbits.at</i>&gt; and the SGI XFS development team, &lt;<i>linux-xfs [at] oss.sgi.com</i>&gt;. </p>
<p> Please send your bug reports or comments to &lt;<i><a rel="nofollow" href="https://savannah.nongnu.org/bugs/?group=attr">https://savannah.nongnu.org/bugs/?group=attr</a></i>&gt; or &lt;<i>acl-devel [at] nongnu.org</i>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-setfattr/">setfattr</a></code>(1), <code><a href="/docs/linux/man/5-attr/">attr</a></code>(5) </p>
<h2>Index</h2>
