---
title: "call_usermodehelper(9)"
name: "call_usermodehelper"
section: "9"
letter: "c"
url: "/docs/linux/man/9-call_usermodehelper/"
description: "call_usermodehelper – prepare and start a usermode application"
---

<p>call_usermodehelper &#8211; prepare and start a usermode application</p>
<h2>Synopsis</h2>
<pre><code>int call_usermodehelper(char *path, char **argv, char **envp, int wait);</code></pre>
<h2>Arguments</h2>
<p><i>path</i></p>
<dl>
<dd>
<dd>path to usermode executable</dl>
<p> <i>argv</i></p>
<dl>
<dd>arg vector for process</dl>
<p> <i>envp</i></p>
<dl>
<dd>environment for process</dl>
<p> <i>wait</i></p>
<dl>
<dd>wait for the application to finish and return status. when UMH_NO_WAIT don&#8217;t wait at all, but you get no useful error back when the program couldn&#8217;t be exec&#8217;ed. This makes it safe to call from interrupt context.</dl>
<h2>Description</h2>
<p>This function is the equivalent to use <code>call_usermodehelper_setup</code> and <code>call_usermodehelper_exec</code>.</p>
<h2>Copyright</h2>
