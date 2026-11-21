---
title: "findcon(1)"
name: "findcon"
section: "1"
letter: "f"
url: "/docs/linux/man/1-findcon/"
description: "findcon – SELinux file context search tool"
---

<h2>NAME</h2>
<p> findcon &#8211; SELinux file context search tool</p>
<h2>SYNOPSIS</h2>
<p> <code>findcon</code> FCLIST [OPTIONS] [EXPRESSION]</p>
<h2>DESCRIPTION</h2>
<p> <code>findcon</code> allows the user to search for files with a specified context. Results can be filtered by object class as described below.</p>
<h2>FCLIST</h2>
<p> The <code>findcon</code> tool operates upon a file context list source. There are three valid file context lists.</p>
<dl>
<dt>directory</dt>
<dd> If <code>FCLIST</code> is a name of a directory then begin the search at that directory and recurse within it. Be sure there are no circular mounts within it.</dd>
<dt>file_contexts</dt>
<dd> If <code>FCLIST</code> is the name of a file_contexts file (e.g., /etc/selinux/strict/contexts/files/file_contexts) then open that file and find matching entries.</dd>
<dt>database</dt>
<dd> If <code>FCLIST</code> is the name of a database as created by a previous run of <code>indexcon</code> or <code>apol</code> then open the database and execute queries into it.</dd></dl>
<h2>EXPRESSION</h2>
<p> The following options allow the user to specify which files to print. A file must meet all specified criteria. If no expression is provided, all files are printed.</p>
<dl>
<dt>-t TYPE, &#8211;type=TYPE</dt>
<dd> Search for files with a context containing the type TYPE.</dd>
<dt>-u USER, &#8211;user=USER</dt>
<dd> Search for files with a context containing the user USER.</dd>
<dt>-r ROLE, &#8211;role=ROLE</dt>
<dd> Search for files with a context containing the role ROLE.</dd>
<dt>-m RANGE, &#8211;mls-range=RANGE</dt>
<dd> Search for files with a context with the MLS range of RANGE. Note that <code>findcon</code> ignores the SELinux translation library, if present. In addition, this flag is ignored if the <code>FCLIST</code> has no MLS information.</dd>
<dt>&#8211;context=CONTEXT</dt>
<dd> Search for files matching this partial context. This flag overrides -t, -u, -r, and -m.</dd>
<dt>-p PATH, &#8211;path=PATH</dt>
<dd> Search for files which include PATH.</dd>
<dt>-c CLASS, &#8211;class=CLASS</dt>
<dd> Search only files of object class CLASS.</dd></dl>
<h2>OPTIONS</h2>
<p> The following additional options are available.</p>
<dl>
<dt>-R, &#8211;regex</dt>
<dd> Search using regular expressions instead of exact string matching. This option does not affect the &#8211;class flag.</dd>
<dt>-h, &#8211;help</dt>
<dd> Print help information and exit.</dd>
<dt>-V, &#8211;version</dt>
<dd> Print version information and exit.</dd></dl>
<h2>PARTIAL CONTEXT</h2>
<p> The <code>&#8211;context</code> flag specifies a partial context, which is a a colon separated list of user, role, and type. If the system supports MLS, the context may have a fourth field that gives the range. If a field is not specified or is the literal asterisk, then the query will always match the field.</p>
<h2>OBJECT CLASSES</h2>
<p> Valid object class strings are </p>
<p> block, char, dir, fifo, file, link, or sock.</p>
<h2>NOTE</h2>
<p> The findcon utility always operates on &quot;raw&quot; SELinux file contexts. If the system has an installed translation library (i.e., libsetrans), those translations are ignored in favor of reading the original contexts from the filesystem (if FCFILE is a directory).</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>findcon .</code></dt>
<dd> Find every context in the current directory and all of its subdirectories.</dd>
<dt><code>findcon -u user_u .</code></dt>
<dd> Find every context whose user is user_u in the current directory and all subdirectories.</dd>
<dt><code>findcon -u system_u -t bin_t file_contexts</code></dt>
<dd> Find entries user system_u and type bin_t within a file_contexts file, assuming that file_contexts is a file contexts file.</dd>
<dt><code>findcon &#8211;context=system_u::bin_t file_contexts</code></dt>
<dd> This is equivalent to the previous example.</dd>
<dt><code>findcon &#8211;context=system_u:*:bin_t:* file_contexts</code></dt>
<dd> This is also equivalent to the above example.</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Jeremy A. Mowery &lt;jmowery [at] tresys.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright(C) 2003-2007 Tresys Technology, LLC</p>
<h2>BUGS</h2>
<p> Please report bugs via an email to setools-bugs [at] tresys.com.</p>
<h2>SEE ALSO</h2>
<p> replcon(1), indexcon(1) </p>
