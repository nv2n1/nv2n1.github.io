---
title: "getcap(8)"
name: "getcap"
section: "8"
letter: "g"
url: "/docs/linux/man/8-getcap/"
description: "getcap – examine file capabilities"
---

<p>getcap &#8211; examine file capabilities</p>
<h2>Synopsis</h2>
<p><code>getcap</code> [-v] [-n] [-r] [-h] <i>filename</i> [ &#8230; ]</p>
<h2>Description</h2>
<p><code>getcap</code> displays the name and capabilities of each specified file.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></dt>
<dd>prints quick usage.</dd>
<dt><code>-n</code></dt>
<dd>prints any non-zero user namespace root user ID value found to be associated with a file&#8217;s capabilities.</dd>
<dt><code>-r</code></dt>
<dd>enables recursive search.</dd>
<dt><code>-v</code></dt>
<dd>display all searched entries, even if the have no file-capabilities.</dd>
<dt><i>filename</i></dt>
<dd>One file per line.</dd></dl>
<h2>Reporting Bugs</h2>
<p>Please report bugs via:</p>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.kernel.org/buglist.cgi?component=libcap">https://bugzilla.kernel.org/buglist.cgi?component=libcap</a>&amp;list_id=1047723&amp;product=Tools&amp;resolution=&#8212;</dt>
<dd></dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-cap_get_file/">cap_get_file</a></code>(3), <code><a href="/docs/linux/man/3-cap_to_text/">cap_to_text</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7), <code><a href="/docs/linux/man/8-setcap/">setcap</a></code>(8) </p>
