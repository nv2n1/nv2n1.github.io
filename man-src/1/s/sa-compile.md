---
title: "sa-compile(1)"
name: "sa-compile"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sa-compile/"
description: "sa-compile – compile SpamAssassin ruleset into native code"
---

<h2 class="name">NAME</h2>
<p> sa-compile &#8211; compile SpamAssassin ruleset into native code </p>
<h2>SYNOPSIS</h2>
<p> <code>sa-compile</code> [options] </p>
<p> Options: </p>
<pre><code>
  --list                        Output base string list to STDOUT
  --sudo                        Use 'sudo' for privilege escalation
  --keep-tmps                   Keep temporary files instead of deleting
  -C path, --configpath=path, --config-file=path
                                Path to standard configuration dir
  -p prefs, --prefspath=file, --prefs-file=file
                                Set user preferences file
  --siteconfigpath=path         Path for site configs
                                (default: /etc/mail/spamassassin)
  --updatedir=path              Directory to place updates
          (default: /var/lib/spamassassin/compiled/&lt;perlversion&gt;/3.004000)
  --cf='config line'            Additional line of configuration
  -D, --debug [area=n,...]      Print debugging messages
  -V, --version                 Print version
  -h, --help                    Print usage message
</code></pre>
<h2>DESCRIPTION</h2>
<p> sa-compile uses <tt>&quot;re2c&quot;</tt> to compile the site-wide parts of the SpamAssassin ruleset. No part of user_prefs or any files included from user_prefs can be built into the compiled set. </p>
<p> This compiled set is then used by the <tt>&quot;Mail::SpamAssassin::Plugin::Rule2XSBody&quot;</tt> plugin to speed up SpamAssassin&#8217;s operation, where possible, and when that plugin is loaded. </p>
<p> <tt>&quot;re2c&quot;</tt> can match strings much faster than perl code, by constructing a <font SIZE="-1">DFA</font> to match many simple strings in parallel, and compiling that to native object code. Not all SpamAssassin rules are amenable to this conversion, however. </p>
<p> This requires <tt>&quot;re2c&quot;</tt> (see <tt>&quot;<a rel="nofollow" href="http://re2c.org/">http://re2c.org/</a>&quot;</tt>), and the C compiler used to build Perl <font SIZE="-1">XS</font> modules, be installed. </p>
<p> Note that running this, and creating a compiled ruleset, will have no effect on SpamAssassin scanning speeds unless you also edit your <tt>&quot;v320.pre&quot;</tt> file and ensure this line is uncommented: </p>
<pre>
  loadplugin Mail::SpamAssassin::Plugin::Rule2XSBody
</pre>
<p> Additionally, &#8220;sa-compile&#8221; will not restart &#8220;spamd&#8221; or otherwise cause a scanner to reload the now-compiled ruleset automatically.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;list</code></p>
<dd> Output the extracted base strings to <font SIZE="-1">STDOUT,</font> instead of generating the C extension code.</p>
<dt><code>&#8211;sudo</code></p>
<dd> Use <tt><a href="/docs/linux/man/8-sudo/">sudo</a>(8)</tt> to run code as &#8216;root&#8217; when writing files to the compiled-rules storage area (which is <tt>&quot;/var/lib/spamassassin/compiled/5.016/3.004000&quot;</tt> by default).</p>
<dt><code>&#8211;quiet</code></p>
<dd> Produce less diagnostic output. Errors will still be displayed.</p>
<dt><code>&#8211;keep-tmps</code></p>
<dd> Keep temporary files after the script completes, instead of deleting them.</p>
<dt><code>-C</code> <i>path</i>, <code>&#8211;configpath</code>=<i>path</i>, <code>&#8211;config-file</code>=<i>path</i></p>
<dd> Use the specified path for locating the distributed configuration files. Ignore the default directories (usually <tt>&quot;/usr/share/spamassassin&quot;</tt> or similar).</p>
<dt><code>&#8211;siteconfigpath</code>=<i>path</i></p>
<dd> Use the specified path for locating site-specific configuration files. Ignore the default directories (usually <tt>&quot;/etc/mail/spamassassin&quot;</tt> or similar).</p>
<dt><code>&#8211;updatedir</code></p>
<dd> By default, <tt>&quot;sa-compile&quot;</tt> will use the system-wide rules update directory: </p>
<pre>
        /var/lib/spamassassin/compiled/5.016/3.004000
</pre>
<p> If the updates should be stored in another location, specify it here. </p>
<p> Note that use of this option is not recommended; if sa-compile is placing the compiled rules the wrong directory, you probably need to rebuild SpamAssassin with different <tt>&quot;Makefile.PL&quot;</tt> arguments, instead of overriding sa-compile&#8217;s runtime behaviour.</p>
<dt><code>&#8211;cf=&#8217;config line&#8217;</code></p>
<dd> Add additional lines of configuration directly from the command-line, parsed after the configuration files are read. Multiple <code>&#8211;cf</code> arguments can be used, and each will be considered a separate line of configuration.</p>
<dt><code>-p</code> <i>prefs</i>, <code>&#8211;prefspath</code>=<i>prefs</i>, <code>&#8211;prefs-file</code>=<i>prefs</i></p>
<dd> Read user score preferences from <i>prefs</i> (usually <tt>&quot;$HOME/.spamassassin/user_prefs&quot;</tt>) .</p>
<dt><code>-D</code> [<i>area,&#8230;</i>], <code>&#8211;debug</code> [<i>area,&#8230;</i>]</p>
<dd> Produce debugging output. If no areas are listed, all debugging information is printed. Diagnostic output can also be enabled for each area individually; <i>area</i> is the area of the code to instrument. </p>
<p> For more information about which areas (also known as channels) are available, please see the documentation at &lt;<a rel="nofollow" href="http://wiki.apache.org/spamassassin/DebugChannels">http://wiki.apache.org/spamassassin/DebugChannels</a>&gt;.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help message and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print sa-compile version and exit.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-mail--spamassassin/">Mail::SpamAssassin</a></i>(3) <i><a href="/docs/linux/man/1-spamassassin/">spamassassin</a></i>(1) <i><a href="/docs/linux/man/1-spamd/">spamd</a></i>(1)</p>
<h2>PREREQUESITES</h2>
<p> <tt>&quot;Mail::SpamAssassin&quot;</tt> <tt>&quot;re2c&quot;</tt> <tt>&quot;Mail::SpamAssassin::Plugin::Rule2XSBody&quot;</tt></p>
<h2>BUGS</h2>
<p> See &lt;<a rel="nofollow" href="http://issues.apache.org/SpamAssassin/">http://issues.apache.org/SpamAssassin/</a>&gt;</p>
<h2>AUTHORS</h2>
<p> The Apache SpamAssassin(tm) Project &lt;<a rel="nofollow" href="http://spamassassin.apache.org/">http://spamassassin.apache.org/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> SpamAssassin is distributed under the Apache License, Version 2.0, as described in the file <tt>&quot;LICENSE&quot;</tt> included with the distribution. </p>
<h2>Index</h2>
