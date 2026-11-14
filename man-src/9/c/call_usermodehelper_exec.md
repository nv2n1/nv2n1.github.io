---
title: "call_usermodehelper_exec(9)"
name: "call_usermodehelper_exec"
section: "9"
letter: "c"
url: "/docs/linux/man/9-call_usermodehelper_exec/"
---

call_usermodehelper_exec - start a usermode application

<h2>Synopsis</h2>

<pre><code>int call_usermodehelper_exec(struct subprocess_info *sub_info, int wait);</code></pre>

<h2>Arguments</h2>

<i>sub_info</i>
<dl><dd><dd>information about the subprocessa</dl>
 

 <i>wait</i>
<dl><dd>wait for the application to finish and return status. when UMH_NO_WAIT don't wait at all, but you get no useful error back when the program couldn't be exec'ed. This makes it safe to call from interrupt context.</dl>

<h2>Description</h2>

Runs a user-space application. The application is started asynchronously if wait is not set, and runs as a child of system workqueues. (ie. it runs with full root capabilities and optimized affinity).

<h2>Copyright</h2>


