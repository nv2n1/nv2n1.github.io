---
title: "ecore_x_flush_group(3)"
name: "ecore_x_flush_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_x_flush_group/"
description: "X Synchronization Functions – Functions that ensure that all commands that have been issued by the Ecore X library have been sent to the server."
---

<p>X Synchronization Functions &#8211; Functions that ensure that all commands that have been issued by the Ecore X library have been sent to the server. </p>
<h3>Functions</h3>
<p>EAPI void <code>ecore_x_flush</code> (void)<br />
 <i>Sends all X commands in the X Display buffer. </i><br />
 EAPI void <code>ecore_x_sync</code> (void)<br />
 <i>Flushes the command buffer and waits until all requests have been processed by the server. </i></p>
<h2>Detailed Description</h2>
<p>Functions that ensure that all commands that have been issued by the Ecore X library have been sent to the server.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
