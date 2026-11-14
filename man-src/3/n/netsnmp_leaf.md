---
title: "netsnmp_leaf(3)"
name: "netsnmp_leaf"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_leaf/"
description: "leaf_handlers – Process individual leaf objects A group of handlers to implement individual leaf objects and instances (both scalar objects, and individual objects and instances within a table)."
---

<p>leaf_handlers &#8211; Process individual leaf objects A group of handlers to implement individual leaf objects and instances (both scalar objects, and individual objects and instances within a table).</p>
<h3>Modules</h3>
<p><code>instance</code><br />
 <i>Process individual MIB instances easily. </i><br />
 <code>scalar</code><br />
 <i>Process scalars easily. </i><br />
 <code>scalar_group</code><br />
 <i>Process groups of scalars. </i><br />
 <code>watcher</code><br />
 <i>Watch a specified variable and process it as an instance or scalar object. </i> </p>
<h2>Detailed Description</h2>
<p>Process individual leaf objects A group of handlers to implement individual leaf objects and instances (both scalar objects, and individual objects and instances within a table). </p>
<p> These handlers will typically allow control to be passed down to a lower level, user-provided handler, but this is (usually) optional.</p>
