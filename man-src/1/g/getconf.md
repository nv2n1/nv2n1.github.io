---
title: "getconf(1)"
name: "getconf"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getconf/"
description: "getconf – Query system configuration variables"
---

<h2 class="name">NAME</h2>
<p> getconf &#8211; Query system configuration variables </p>
<h2>SYNOPSIS</h2>
<p> <code>getconf</code> -a </p>
<p> <code>getconf</code> [<code>-v specification</code>] system_var </p>
<p> <code>getconf</code> [<code>-v specification</code>] path_var pathname</p>
<h2>DESCRIPTION</h2>
<p> <code>-a</code> </p>
<pre>
        Displays all configuration variables for the current system
        and their values.
</pre>
<p> <code>-v</code> </p>
<pre>
        Indicate the specification and version for which to obtain
        configuration variables.
</pre>
<p> <code>system_var</code> </p>
<pre>
        A system configuration variable, as defined by <a href="//www.systutorials.com/docs/linux/man/3-sysconf/">sysconf</a>(3) or
        <a href="//www.systutorials.com/docs/linux/man/3-confstr/">confstr</a>(3).
</pre>
<p> <code>path_var</code> </p>
<pre>
        A system configuration variable as defined by <a href="//www.systutorials.com/docs/linux/man/3-pathconf/">pathconf</a>(3). This
        must be used with a pathname.
</pre>
<h2>AUTHOR</h2>
<p> <i>getconf</i> was written by Roland McGrath for the GNU C Library </p>
<p> This man page was written by Ben Collins &lt;bcollins [at] debian.org&gt; for the Debian GNU/Linux system.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3), <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3), <code><a href="/docs/linux/man/3-confstr/">confstr</a></code>(3) </p>
<h2>Index</h2>
