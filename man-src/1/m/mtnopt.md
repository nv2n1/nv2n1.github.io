---
title: "mtnopt(1)"
name: "mtnopt"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mtnopt/"
description: "mtnopt – generate shell variables from monotone workspace options"
---

<h2>NAME</h2>
<p> mtnopt &#8211; generate shell variables from monotone workspace options</p>
<h2>SYNOPSIS</h2>
<p> <code>mtnopt</code> [<code>-s</code>|<code>-c</code>|<code>-v</code>] [<code>-d</code> <i>dir</i>] [<code>-k</code> <i>keys</i>]<br />
 <code>mtnopt -h</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>mtnopt</code> prints shell variable assignments for each value in the file of monotone workspace options, <i>_MTN/options</i>, in the current directory. For instance, if <i>_MTN/options</i> contained this text:</p>
<dl>
<dt>
<dd> <tt>database &quot;/home/user/src/monotone.mtn&quot;</tt><br />
 <tt> branch &quot;net.venge.monotone&quot;</tt><br />
 <tt> keydir &quot;/home/user/.monotone/keys&quot;</tt></dl>
<p> <code>mtnopt</code> would print:</p>
<dl>
<dt>
<dd> <tt>MTN_database=&quot;/home/user/src/monotone.mtn&quot;;</tt><br />
 <tt>MTN_branch=&quot;net.venge.monotone&quot;;</tt><br />
 <tt>MTN_keydir=&quot;/home/user/.monotone/keys&quot;;</tt></dl>
<p> By default, <code>mtnopt </code> attempts to guess appropriate syntax from the value of the <code>SHELL</code> environment variable. This can be overridden with the <code>-s</code> and <code>-c</code> command-line options.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code></p>
<dd> Print variable assignments in <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1) syntax.</p>
<dt><code>-c</code></p>
<dd> Print variable assignments in <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1) syntax.</p>
<dt><code>-v</code></p>
<dd> Print only the values, with no indication of the corresponding option keys.</p>
<dt><code>-d&nbsp;<wbr></code><i>directory</i></p>
<dd> Look for <i>_MTN/options</i> in <i>directory</i>, rather than in the current directory.</p>
<dt><code>-k&nbsp;<wbr></code><i>keys</i></p>
<dd> Print assignments for only those options that match the <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1) regular expression <i>keys</i>.</p>
<dt><code>-h</code></p>
<dd> Print a help message and exit.</dl>
<h2>BUGS</h2>
<p> <code>mtnopt</code> only looks in the current directory for the <i>_MTN</i> directory, so it will fail in a subdirectory of a workspace. </p>
<p> <code>mtnopt</code> should be aware of the set of possible options, rather than blindly printing whatever is in <i>_MTN/options</i>. </p>
<p> The behavior when there is no <i>_MTN/options</i> file to be found is less than helpful.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mtn/">mtn</a></code>(1), <code><a href="/docs/linux/man/1-egrep/">egrep</a></code>(1), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/1-csh/">csh</a></code>(1) </p>
<h2>Index</h2>
