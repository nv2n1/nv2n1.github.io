---
title: "gstream-save_input_approver(3)"
name: "gstream-save_input_approver"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gstream-save_input_approver/"
description: "save_input_approver"
---

<h2>NAME</h2>
<p> save_input_approver</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/gstream.h">gstream.h</a>&gt;</code> </p>
<p> <code>void save_input_approver();</code></p>
<h2>DESCRIPTION</h2>
<p> A typical use of the input approver system is to temporarily set a home-made approver, launch an input and then get the original settings back. Consequently there is a pair of functions to help you with that, save_input_approver and restore_input_approver. </p>
<p> Saving will backup the currently used approver, so you can continue using it. </p>
<pre><code>
gs.save_input_approver();
gs &gt;&gt; my_string; // uses still default approver
gs.set_input_approver(ia_my_own);
gs &gt;&gt; my_string; // uses ia_my_own approver
gs.restore_input_approver();
gs &gt;&gt; my_string; // uses default approver again
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-gstream-restore_input_approver/">gstream-restore_input_approver</a></code>(3), <code><a href="/docs/linux/man/3-gstream-set_input_approver/">gstream-set_input_approver</a></code>(3), <code><a href="/docs/linux/man/3-gstream-get_input_approver/">gstream-get_input_approver</a></code>(3) </p>
<h2>Index</h2>
