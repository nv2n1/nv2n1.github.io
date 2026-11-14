---
title: "update_dialog(3)"
name: "update_dialog"
section: "3"
letter: "u"
url: "/docs/linux/man/3-update_dialog/"
description: "update_dialog – Low level function to update a dialog player. Allegro game programming library."
---

<p>update_dialog &#8211; Low level function to update a dialog player. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int update_dialog(DIALOG_PLAYER *player);</code></pre>
<h2>Description</h2>
<p>Updates the status of a dialog object returned by init_dialog(). Returns TRUE if the dialog is still active, or FALSE if it has terminated. Upon a return value of FALSE, it is up to you whether to call shutdown_dialog() or to continue execution. The object that requested the exit can be determined from the player-&gt;obj field. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-init_dialog/">init_dialog</a></code>(3) </p>
