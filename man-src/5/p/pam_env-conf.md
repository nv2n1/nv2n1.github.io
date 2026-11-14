---
title: "pam_env-conf(5)"
name: "pam_env-conf"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pam_env-conf/"
description: "pam_env.conf, environment – the environment variables config files"
---

<p>pam_env.conf, environment &#8211; the environment variables config files</p>
<h2>Description</h2>
<p>The /etc/security/pam_env.conf file specifies the environment variables to be set, unset or modified by <code><a href="/docs/linux/man/8-pam_env/">pam_env</a></code>(8). When someone logs in, this file is read and the environment variables are set according. </p>
<p> Each line starts with the variable name, there are then two possible options for each variable DEFAULT and OVERRIDE. DEFAULT allows and administrator to set the value of the variable to some default value, if none is supplied then the empty string is assumed. The OVERRIDE option tells pam_env that it should enter in its value (overriding the default value) if there is one to use. OVERRIDE is not used, &quot;&quot; is assumed and no override will be done. </p>
<p> <i>VARIABLE</i> [<i>DEFAULT=[value]</i>] [<i>OVERRIDE=[value]</i>] </p>
<p> (Possibly non-existent) environment variables may be used in values using the ${string} syntax and (possibly non-existent) PAM_ITEMs as well as HOME and SHELL may be used in values using the @{string} syntax. Both the $ and @ characters can be backslash escaped to be used as literal values values can be delimited with &quot;&quot;, escaped &quot; not supported. Note that many environment variables that you would like to use may not be set by the time the module is called. For example, ${HOME} is used below several times, but many PAM applications don&#8217;t make it available by the time you need it. The special variables @{HOME} and @{SHELL} are expanded to the values for the user from his <i>passwd</i> entry. </p>
<p> The &quot;<i>#</i>&quot; character at start of line (no space at front) can be used to mark this line as a comment line. </p>
<p> The /etc/environment file specifies the environment variables to be set. The file must consist of simple <i>NAME=VALUE</i> pairs on separate lines. The <code><a href="/docs/linux/man/8-pam_env/">pam_env</a></code>(8) module will read the file after the pam_env.conf file.</p>
<h2>Examples</h2>
<p>These are some example lines which might be specified in /etc/security/pam_env.conf. Set the REMOTEHOST variable for any hosts that are remote, default to &quot;localhost&quot; rather than not being set at all </p>
<pre><code>REMOTEHOST     DEFAULT=localhost OVERRIDE=@{PAM_RHOST}</code></pre>
<p> Set the DISPLAY variable if it seems reasonable </p>
<pre><code>DISPLAY        DEFAULT=${REMOTEHOST}:0.0 OVERRIDE=${DISPLAY}</code></pre>
<p> Now some simple variables</p>
<dl>
<dd>
<pre> PAGER DEFAULT=less
 MANPAGER DEFAULT=less
 LESS DEFAULT=&quot;M q e h15 z23 b80&quot;
 NNTPSERVER DEFAULT=localhost
 PATH DEFAULT=${HOME}/bin:/usr/local/bin:/bin\
 :/usr/bin:/usr/local/bin/X11:/usr/bin/X11
 XDG_DATA_HOME @{HOME}/share/</pre>
</dl>
<p> Silly examples of escaped variables, just to show how they work.</p>
<dl>
<dd>
<pre> DOLLAR DEFAULT=\$
 DOLLARDOLLAR DEFAULT= OVERRIDE=\$${DOLLAR}
 DOLLARPLUS DEFAULT=\${REMOTEHOST}${REMOTEHOST}
 ATSIGN DEFAULT=&quot;&quot; OVERRIDE=\@</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam_env/">pam_env</a></code>(8), <code><a href="/docs/linux/man/5-pam-d/">pam.d</a></code>(5), <code><a href="/docs/linux/man/7-pam/">pam</a></code>(7), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7)</p>
<h2>Author</h2>
<p>pam_env was written by Dave Kinchlea &lt;kinch [at] kinch.ark.com&gt;.</p>
