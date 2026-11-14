---
title: "globus_logging_update_pid(3)"
name: "globus_logging_update_pid"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_logging_update_pid/"
description: "globus_logging.h –"
---

<h2 class="name">NAME</h2>
<p> globus_logging.h &#8211; </p>
<p> Debug Logging.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_common_include.h&#8217;<br />
 #include &#8216;globus_time.h&#8217; </p>
<h3>Functions</h3>
<p> void <code>globus_logging_update_pid</code> (void) </p>
<h2>Detailed Description</h2>
<p> Debug Logging. </p>
<h2>Function Documentation</h2>
<h3>void globus_logging_update_pid (void)</h3>
<p> Reset the cached version of the pid used for logging. Call this after fork() to keep logging working in a child process</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
