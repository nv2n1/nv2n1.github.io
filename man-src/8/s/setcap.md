---
title: "setcap(8)"
name: "setcap"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setcap/"
description: "setcap – set file capabilities"
---

<p>setcap &#8211; set file capabilities</p>
<h2>Synopsis</h2>
<p><code>setcap</code> [-q] [-n &lt;rootuid&gt;] [-v] {<i>capabilities|-|-r} filename</i> [ &#8230; <i>capabilitiesN</i> <i>fileN</i> ]</p>
<h2>Description</h2>
<p>In the absence of the <code>-v</code> (verify) option <code>setcap</code> sets the capabilities of each specified <i>filename</i> to the <i>capabilities</i> specified. The optional <code>-n &lt;rootuid&gt;</code> argument can be used to set the file capability for use only in a user namespace with this root user ID owner. The <code>-v</code> option is used to verify that the specified capabilities are currently associated with the file. If -v and -n are supplied, the <code>-n &lt;rootuid&gt;</code> argument is also verified. </p>
<p> The <i>capabilities</i> are specified in the form described in <code><a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a></code>(3). </p>
<p> The special capability string, <code>&#8216;-&#8216;</code>, can be used to indicate that capabilities are read from the standard input. In such cases, the capability set is terminated with a blank line. </p>
<p> The special capability string, <code>&#8216;-r&#8217;</code>, is used to remove a capability set from a file. Note, setting an empty capability set is <code>not the same</code> as removing it. An empty set can be used to guarantee a file is not executed with privilege in spite of the fact that the prevailing ambient+inheritable sets would otherwise bestow capabilities on executed binaries. </p>
<p> The <code>-q</code> flag is used to make the program less verbose in its output.</p>
<h2>Exit Code</h2>
<p>The <code>setcap</code> program will exit with a 0 exit code if successful. On failure, the exit code is 1.</p>
<h2>Reporting Bugs</h2>
<p>Please report bugs via:</p>
<dl>
<dt><a rel="nofollow" href="https://bugzilla.kernel.org/buglist.cgi?component=libcap">https://bugzilla.kernel.org/buglist.cgi?component=libcap</a>&amp;list_id=1047723&amp;product=Tools&amp;resolution=&#8212;</p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a></code>(3), <code><a href="/docs/linux/man/3-cap_get_file/">cap_get_file</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-user_namespaces/">user_namespaces</a></code>(7), <code><a href="/docs/linux/man/8-getcap/">getcap</a></code>(8) </p>
