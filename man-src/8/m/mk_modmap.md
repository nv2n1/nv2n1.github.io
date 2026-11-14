---
title: "mk_modmap(8)"
name: "mk_modmap"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mk_modmap/"
description: "mk_modmap – translate a Linux keytable file into an xmodmap file"
---

<p>mk_modmap &#8211; translate a Linux keytable file into an xmodmap file</p>
<h2>Synopsis</h2>
<p><code>mk_modmap</code> [ <code>-v</code> ] keymap_file </p>
<h2>Description</h2>
<p>The <code>mk_modmap</code> command tries to translate a Linux console keytable file into a file that can be parsed by xmodmap, and used within X. It outputs the results to standard out. </p>
<p> If the <code>-v</code> flag is used, verbose output is given. </p>
<p> It requires the X header files to be installed. (In Debian, these are in the &quot;xlibs-dev&quot; package).</p>
<h2>Notes</h2>
<p>Since XFree version 2.1, X initialises its keymap using the Linux keymap, so xmodmap will often be superfluous. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dumpkeys/">dumpkeys</a></code>(1), <code><a href="/docs/linux/man/5-keymaps/">keymaps</a></code>(5), <code><a href="/docs/linux/man/1-xmodmap/">xmodmap</a></code>(1) </p>
