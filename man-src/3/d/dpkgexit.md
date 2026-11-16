---
title: "dpkgexit(3)"
name: "dpkgexit"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgexit/"
---

Dpkg::Exit - program exit handlers 

<h2>Description</h2>The Dpkg::Exit module provides support functions to run handlers on exit.
<h2>Functions</h2><dl COMPACT><dt>push_exit_handler($func)
</dt><dd>Register a code reference into the exit function handlers stack.
</dd><dt><i>pop_exit_handler()</i>
</dt><dd>Pop the last registered exit handler from the handlers stack.
</dd><dt><i>run_exit_handlers()</i>
</dt><dd>Run the registered exit handlers.</dd></dl><h2>Changes</h2><h3>Version 1.01</h3>New functions: <i>push_exit_handler()</i>, <i>pop_exit_handler()</i>, <i>run_exit_handlers()</i> 

 Deprecated variable: <tt>@handlers</tt>
<h3>Version 1.00</h3>Mark the module as public.
