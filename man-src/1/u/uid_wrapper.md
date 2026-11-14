---
title: "uid_wrapper(1)"
name: "uid_wrapper"
section: "1"
letter: "u"
url: "/docs/linux/man/1-uid_wrapper/"
description: "uid_wrapper – A wrapper to fake privilege separation"
---

<h2 class="name">NAME</h2>
<p> uid_wrapper &#8211; A wrapper to fake privilege separation </p>
<h2>SYNOPSIS</h2>
<p> LD_PRELOAD=libuid_wrapper.so UID_WRAPPER=1 UID_WRAPPER_ROOT=1 <code>./myapplication</code></p>
<h2>DESCRIPTION</h2>
<dl>
<dt>
<dd> &bull; Allows uid switching as a normal user.</dl>
<dl>
<dt>
<dd> &bull; Start any application making it believe it is running as root.</dl>
<dl>
<dt>
<dd> &bull; Support for user/group changing in the local thread using the syscalls (like glibc).</dl>
<dl>
<dt>
<dd> &bull; More precisely this library intercepts seteuid and related calls, and simulates them in a manner similar to the nss_wrapper and socket_wrapper libraries.</dl>
<p> Some projects like a file server need privilege separation to be able to switch to the connection user and do file operations. uid_wrapper convincingly lies to the application letting it believe it is operating as root and even switching between UIDs and GIDs as needed.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <code>UID_WRAPPER</code></p>
<dl>
<dt>
<dd> If you load the uid_wrapper and enable it with setting UID_WRAPPER=1 all setuid and setgid will work, even as a normal user.</dl>
<p> <code>UID_WRAPPER_ROOT</code></p>
<dl>
<dt>
<dd> It is possible to start your application as fake root with setting UID_WRAPPER_ROOT=1.</dl>
<p> <code>UID_WRAPPER_DEBUGLEVEL</code></p>
<dl>
<dt>
<dd> If you need to see what is going on in uid_wrapper itself or try to find a bug, you can enable logging support in uid_wrapper if you built it with debug symbols. </p>
<dl>
<dt>
<dd> &bull; 0 = ERROR</dl>
<dl>
<dt>
<dd> &bull; 1 = WARNING</dl>
<dl>
<dt>
<dd> &bull; 2 = DEBUG</dl>
<dl>
<dt>
<dd> &bull; 3 = TRACE</dl>
</dl>
<p> <code>UID_WRAPPER_MYUID</code></p>
<dl>
<dt>
<dd> This environment variable can be used to tell uid_wrapper to let geteuid() return the real (instead of the faked) UID of the user who started the process with uid_wrapper.</dl>
<dl>
<dt>
<dd>
<pre><code>
uid_t uid;
setenv("UID_WRAPPER_MYUID", "1", 1);
uid = geteuid();
unsetenv("UID_WRAPPER_MYUID");
</code></pre>
</dl>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre>
$ LD_PRELOAD=libuid_wrapper.so UID_WRAPPER=1 UID_WRAPPER_ROOT=1 id
uid=0(root) gid=0(root) 0(root)
</pre>
</dl>
<h2>WORKAROUNDS</h2>
<p> If you need to write code that behaves differently depending on whether uid_wrapper is enabled or not, for example in cases where you have to file permissions, you can predefine the uid_wrapper_enabled() function in your project as follows: </p>
<dl>
<dt>
<dd>
<pre><code>
bool uid_wrapper_enabled(void)
{
    return false;
}
</code></pre>
</dl>
<p> Since uid_wrapper overloads this function if enabled, you can use it in your code to detect uid_wrapper. </p>
<h2>Index</h2>
