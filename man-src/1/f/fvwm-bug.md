---
title: "fvwm-bug(1)"
name: "fvwm-bug"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwm-bug/"
description: "fvwm-bug – report a bug in fvwm"
---

<h2>NAME</h2>
<p> fvwm-bug &#8211; report a bug in fvwm</p>
<h2>SYNOPSIS</h2>
<p> <code>fvwm-bug</code> [<i>&#8211;help</i>] [<i>&#8211;version</i>] [<i>address</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>fvwm-bug</code> is a shell script to help the user compose and mail bug reports concerning fvwm in a standard format. <code>fvwm-bug</code> invokes the editor specified by the environment variable <font SIZE="-1"><code>EDITOR</code> </font> on a temporary copy of the bug report format outline. The user must fill in the appropriate fields and exit the editor. <code>fvwm-bug</code> then mails the completed report to the local fvwm maintainer, the fvwm workers list <i>fvwm-workers [at] fvwm.org</i>, or <i>address</i>. If the report cannot be mailed, it is saved in the file <i>dead.fvwm-bug</i> in the invoking user&#8217;s home directory. </p>
<p> The bug report format outline consists of several sections. The first section provides information about the machine, operating system, the fvwm version, and the compilation environment. The second section should be filled in with a description of the bug. The third section should be a description of how to reproduce the bug. The optional fourth section is for a proposed fix. Fixes are encouraged.</p>
<h2>ENVIRONMENT</h2>
<p> <code>fvwm-bug</code> will utilize the following environment variables if they exist:</p>
<dl>
<dt><code>EDITOR</code></p>
<dd> Specifies the preferred editor. If <font SIZE="-1"><code>EDITOR</code> </font> is not set, <code>fvwm-bug</code> defaults to <code>emacs</code>.</p>
<dt><code>HOME</code></p>
<dd> Directory in which the failed bug report is saved if the mail fails. </p>
</dl>
<h2>Index</h2>
