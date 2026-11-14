---
title: "foomatic-kitload(8)"
name: "foomatic-kitload"
section: "8"
letter: "f"
url: "/docs/linux/man/8-foomatic-kitload/"
description: "foomatic-kitload – installs a data kit into the foomatic database."
---

<p>foomatic-kitload &#8211; installs a data kit into the foomatic database.</p>
<h2>Synopsis</h2>
<p><code>foomatic-kitload</code> [<i> -k kit-dir</i>] [<i> -d dest-dir</i>]&#8230;</p>
<h2>Description</h2>
<p><code>foomatic-kitload</code> installs a foomatic data kit into the local data library. It takes a <i>-k</i> <i>dirname</i> option, where <i>dirname</i> is the toplevel directory of a foomatic driver &quot;kit&quot;. A &quot;kit&quot; is a selection of XML source files arranged exactly as in the source/section of the master database (ie, opt/driver/printer/ subdirs). Gimp-Print&#8217;s foomatic-generator produces exactly such a kit. Foomatic-kitload is moderately paranoid about kits: the kit must contain at least one of <i>printer</i>, <i>driver</i> or <i>opt</i>; the kit must contain only files ending in <i>.xml</i>, the kit cannot be the local library itself, etc. But it does not inspect the contents of the kit files in any way.</p>
<h3>Options</h3>
<dl>
<dt><code>-k</code><i>&nbsp;<wbr>dirname</i></p>
<dd>dirname is the toplevel directory of a foomatic driver &quot;kit&quot;.</p>
<dt><code>-d</code><i>&nbsp;<wbr>destdir</i></p>
<dd>destdir is a prefix to prepend to the install path. This will not normally be required, but is useful if installing into a temporary `staging area&#8217; prior to installing in the final destination. </p>
<h2>Exit Status</h2>
<p><code>foomatic-kitload</code> returns 0 on success, 255 or something else when an error occurs.</p>
<h2>Author</h2>
<p>Manfred Wassmann &lt;<i>manolo [at] NCC-1701.B.Shuttle.de</i>&gt; for the foomatic project using output from the associated binary.</p>
<h2>Bugs</h2>
<p>Please post bug reports on <a rel="nofollow" href="http://lists.freestandards.org/mailman/listinfo/printing-foomatic">http://lists.freestandards.org/mailman/listinfo/printing-foomatic</a> </p>
