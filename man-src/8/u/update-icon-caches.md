---
title: "update-icon-caches(8)"
name: "update-icon-caches"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-icon-caches/"
description: "update-icon-caches – Update wrapper script for the icon caches"
---

<p>update-icon-caches &#8211; Update wrapper script for the icon caches</p>
<h2>Synopsis</h2>
<p><code>update-icon-caches</code> <i>directory</i> [ <i>&#8230;</i> ]</p>
<h2>Description</h2>
<p><code>update-icon-caches</code> is a wrapper script for updating the icon caches in a list of directories. </p>
<p> In each of the directories passed as arguments, the icon cache is updated if it is already present. It is not created if it does not already exist. </p>
<p> If the theme index file is not present, the icon cache is removed.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gtk-update-icon-cache/">gtk-update-icon-cache</a></code>(1)</p>
<h2>Author</h2>
<p>This manual page was written by Josselin Mouette &lt;joss [at] debian.org&gt;, for the Debian GNU/Linux system.</p>
