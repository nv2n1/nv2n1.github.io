---
title: "afppasswd(1)"
name: "afppasswd"
section: "1"
letter: "a"
url: "/docs/linux/man/1-afppasswd/"
description: "afppasswd – netatalk password maintenance utility"
---

<h2 class="name">NAME</h2>
<p> afppasswd &#8211; netatalk password maintenance utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>afppasswd</code> [-acfn] [-p&nbsp;<wbr><i>passwd</i>&nbsp;<wbr><i>file</i>] [-u&nbsp;<wbr><i>minimum</i>&nbsp;<wbr><i>uid</i>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>afppasswd</code></p>
<dd>allows the maintenance of afppasswd files created by netatalk for use by the uams_randnum.so UAM (providing the &quot;Randnum exchange&quot; and &quot;2-Way Randnum exchange&quot; User Authentication Modules). </p>
<p> <code>afppasswd</code> can either be called by root with parameters, or can be called by local system users with no parameters to change their AFP passwords. </p>
<dl>
<dt>
<dd>
 <font SIZE="+1"> <code>Note</code> </font> </p>
<p> With this utility you can only change the passwords used by two specific UAMs. As they provide only weak password encryption, the use of the &quot;Randnum exchange&quot; and &quot;2-Way Randnum exchange&quot; UAMs is deprecated unless one has to support very old AFP clients, that can not deal with the more secure &quot;DHCAST128&quot; UAM instead. Please compare with the Authentication chapter inside Netatalk&#8217;s documentation. </p>
</dl>
<h2>EXAMPLE</h2>
<p> Local user changing their own password: </p>
<dl>
<dt>
<dd>
<pre>
example% <code>afppasswd</code>
Enter NEW AFP password: <code>(hidden)</code>
Enter NEW AFP password again: <code>(hidden)</code>
afppasswd: updated password.
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> Add a new user to the <code>afppasswd</code> file.</dl>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> Create and/or initialize <code>afppasswd</code> file or specific user.</dl>
<p> <code>-f</code></p>
<dl>
<dt>
<dd> Force the current action.</dl>
<p> <code>-p</code><i> path</i></p>
<dl>
<dt>
<dd> Path to <code>afppasswd</code> file.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> If cracklib support is built into <code>netatalk</code> this option will cause cracklib checking to be disabled, if the superuser does not want to have the password run against the cracklib dictionary.</dl>
<p> <code>-u</code><i> minimum uid</i></p>
<dl>
<dt>
<dd> This is the minimum <i>user id</i> (uid) that <code>afppasswd</code> will use when creating users.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-afpd/">afpd</a></code>(8), <code><a href="/docs/linux/man/8-atalkd/">atalkd</a></code>(8). </p>
<h2>Index</h2>
