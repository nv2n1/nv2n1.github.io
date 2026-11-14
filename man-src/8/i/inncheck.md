---
title: "inncheck(8)"
name: "inncheck"
section: "8"
letter: "i"
url: "/docs/linux/man/8-inncheck/"
description: "inncheck – Check INN configuration and database files"
---

<p>inncheck &#8211; Check INN configuration and database files</p>
<h2>Synopsis</h2>
<p><code>inncheck</code> [<code>-afqv</code>] [<code>&#8211;noperm</code> | <code>&#8211;perm</code>] [<code>&#8211;pedantic</code>] [<i>file</i> | <i>file</i><code>=</code><i>path</i> &#8230;]</p>
<h2>Description</h2>
<p><code>inncheck</code> examines various configuration files and databases and verifies things about them. Things verified depend on the file being checked, but generally are things like permissions, ownership, syntax errors in config files, etc. </p>
<p> <code>inncheck</code> does not make changes to any files &#8212; it just reports what it thinks may be wrong, and it is up to the operator to fix the problem </p>
<p> The set of files checked may be restricted by using <i>file</i> or <i>file</i><code>=</code><i>path</i> arguments. For example, putting <tt>&quot;incoming.conf&quot;</tt> causes only the <i>incoming.conf</i> file to be checked. Using <tt>&quot;incoming.conf=/tmp/incoming.conf&quot;</tt> on the command line will cause <code>inncheck</code> to only verify the <i>incoming.conf</i> file, and it will perform the checks on the <i>/tmp/incoming.conf</i> file instead of the default one. Setting a file path to an empty value like <tt>&quot;incoming.conf=&quot;</tt> will skip the check for that file (this only makes sense with <code>-a</code>, or no files will be checked at all). </p>
<p> Valid values for <i>file</i> are: </p>
<pre> active
 control.ctl
 control.ctl.local
 expire.ctl
 incoming.conf
 inn.conf
 innfeed.conf
 moderators
 newsfeeds
 nntpsend.ctl
 passwd.nntp
 readers.conf
 storage.conf</pre>
<h2>Options</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd>If any <i>file</i> value or <i>file</i><code>=</code><i>path</i> pairs (see below) are given, then normally only the files they refer to are checked. Use the <code>-a</code> (or <code>&#8211;all</code>) flag to specify that <i>all</i> files should be checked regardless. In this case the form <i>file</i><code>=</code><i>path</i> will be the more useful.</p>
<dt><code>-f</code>, <code>&#8211;fix</code></p>
<dd>Use the <code>-f</code> flag (or <code>&#8211;fix</code>) to have <code>inncheck</code> print the appropriate <code>chown</code>/<code>chgrp</code>/<code>chmod</code> command necessary to fix a problem that it reports. Any other output lines will be prefixed with a hash sign (<tt>&quot;#&quot;</tt>) to make the output be valid input for a shell. Note that the <code>&#8211;perm</code> flag must be used as well when using this flag.</p>
<dt><code>&#8211;noperm</code></p>
<dd>To avoid doing any checking of file permissions or ownership, use the <code>&#8211;noperm</code> option.</p>
<dt><code>&#8211;pedantic</code></p>
<dd>Use the <code>&#8211;pedantic</code> option to get reports on things that are not necessarily wrong, but may indicate a bad configuration, such as <i>inn.conf</i> missing a key.</p>
<dt><code>&#8211;perm</code></p>
<dd><code>inncheck</code> checks all files for permission problems. If the <code>&#8211;perm</code> flag is used, then <i>only</i> the files specified by the <i>file</i> or <i>file</i><code>=</code><i>path</i> command line arguments will be checked for problems other than permission problems.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>Use the <code>-q</code> option (or <code>&#8211;quiet</code>) to get less output.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Use the <code>-v</code> option (or <code>&#8211;verbose</code>) to get more verbose output.</dl>
<h2>Examples</h2>
<p>To have <code>inncheck</code> check all files for syntax and permission problems simply run: </p>
<pre> inncheck</pre>
<p>It is recommended to run the following command to be aware of all the potential problems <code>inncheck</code> can detect: </p>
<pre> inncheck -a --perm --pedantic</pre>
<p>To have <code>inncheck</code> check all files for permission problems and to verify the syntax of the <i>active</i> and <i>incoming.conf</i> files, do: </p>
<pre> inncheck --perm active incoming.conf</pre>
<p>To fix the permissions problems noted in the output of the above command, modify it as follows: </p>
<pre> inncheck -f --perm | sh</pre>
<p>(Note that it is useless to mention the name of the two files since permission problems are checked on all files.) </p>
<p> To have <code>inncheck</code> check the test <i>newsfeeds</i> file in <i>/var/tmp/newsfeeds.testing</i>, do: </p>
<pre> inncheck newsfeeds=/var/tmp/newsfeeds.testing</pre>
<p>To have <code>inncheck</code> check all the files as it normally does, but to specify a different location for the <i>newsfeeds</i> file and omit checking of the <i>innfeed.conf</i> file, do: </p>
<pre> inncheck -a newsfeeds=/var/tmp/newsfeeds.testing innfeed.conf=</pre>
<h2>Bugs</h2>
<p>If the <code>-f</code> and <code>&#8211;perm</code> options are used together, along with <code>-a</code> or some <i>file</i> or <i>file</i><code>=</code><i>path</i> arguments that refer to a file with a syntax problem, then the output will no longer be valid input for a shell. </p>
<p> In most cases, <code>inncheck</code> currently does not correctly understand option values spanning multiple lines. If you get error messages about runaway quotes, you either have to ignore them and check the correctness of the relevant lines yourself, or merge the value into a single line.</p>
<h2>History</h2>
<p>Written by Brendan Kehoe &lt;brendan [at] cygnus.com&gt; and Rich Salz &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Converted to <font SIZE="-1">POD</font> by Julien Elie. </p>
<p> <tt>$Id:</tt> inncheck.pod 9429 2012-06-15 18:21:26Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-active/">active</a></i>(5), <i><a href="/docs/linux/man/5-control-ctl/">control.ctl</a></i>(5), <i><a href="/docs/linux/man/5-expire-ctl/">expire.ctl</a></i>(5), <i><a href="/docs/linux/man/5-history/">history</a></i>(5), <i><a href="/docs/linux/man/5-incoming-conf/">incoming.conf</a></i>(5), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-innfeed-conf/">innfeed.conf</a></i>(5), <i><a href="/docs/linux/man/5-moderators/">moderators</a></i>(5), <i><a href="/docs/linux/man/5-newsfeeds/">newsfeeds</a></i>(5), <i><a href="/docs/linux/man/5-nntpsend-ctl/">nntpsend.ctl</a></i>(5), <i><a href="/docs/linux/man/5-passwd-nntp/">passwd.nntp</a></i>(5), <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5), <i><a href="/docs/linux/man/5-storage-conf/">storage.conf</a></i>(5). </p>
