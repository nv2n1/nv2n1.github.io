---
title: "shell-quote(1)"
name: "shell-quote"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shell-quote/"
description: "shell-quote – quote arguments for safe use, unmodified in a shell command"
---

<h2 class="name">NAME</h2>
<p> shell-quote &#8211; quote arguments for safe use, unmodified in a shell command </p>
<h2>SYNOPSIS</h2>
<p> <code>shell-quote</code> [<i>switch</i>]&#8230; <i>arg</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>shell-quote</code> lets you pass arbitrary strings through the shell so that they won&#8217;t be changed by the shell. This lets you process commands or files with embedded white space or shell globbing characters safely. Here are a few examples.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>ssh preserving args</code></p>
<dd> When running a remote command with ssh, ssh doesn&#8217;t preserve the separate arguments it receives. It just joins them with spaces and passes them to <tt>&quot;$SHELL -c&quot;</tt>. This doesn&#8217;t work as intended: </p>
<pre>
    ssh host touch 'hi there'           # fails
</pre>
<p> It creates 2 files, <i>hi</i> and <i>there</i>. Instead, do this: </p>
<pre>
    cmd=`shell-quote touch 'hi there'`
    ssh host &quot;$cmd&quot;
</pre>
<p> This gives you just 1 file, <i>hi there</i>.</p>
<dt><code>process find output</code></p>
<dd> It&#8217;s not ordinarily possible to process an arbitrary list of files output by <code>find</code> with a shell script. Anything you put in <tt>$IFS</tt> to split up the output could legitimately be in a file&#8217;s name. Here&#8217;s how you can do it using <code>shell-quote</code>: </p>
<pre>
    eval set -- `find -type f -print0 | xargs -0 shell-quote --`
</pre>
<dt><code>debug shell scripts</code></p>
<dd> <code>shell-quote</code> is better than <code>echo</code> for debugging shell scripts. </p>
<pre><code>
debug()
{
    [-z "$debug"] || shell - quote "debug:"
                                   "$@"
}
</code></pre>
<p> With <code>echo</code> you can&#8217;t tell the difference between <tt>&quot;debug 'foo bar'&quot;</tt> and <tt>&quot;debug foo bar&quot;</tt>, but with <code>shell-quote</code> you can.</p>
<dt><code>save a command for later</code></p>
<dd> <code>shell-quote</code> can be used to build up a shell command to run later. Say you want the user to be able to give you switches for a command you&#8217;re going to run. If you don&#8217;t want the switches to be re-evaluated by the shell (which is usually a good idea, else there are things the user can&#8217;t pass through), you can do something like this: </p>
<pre><code>
    user_switches=
    while [ $# != 0 ]
    do
        case x$1 in
            x--pass-through)
                [ $# -gt 1 ] || die "need an argument for $1"
                user_switches="$user_switches "`shell-quote -- "$2"`
                shift;
    ;
#process other switches
    esac
        shift
            done
#later
                eval "shell-quote some-command $user_switches my args"
</code></pre>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;debug</code></p>
<dd> Turn debugging on.</p>
<dt><code>&#8211;help</code></p>
<dd> Show the usage message and die.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version number and exit.</dl>
<h2>AVAILABILITY</h2>
<p> The code is licensed under the <font SIZE="-1">GNU GPL. </font> Check <a rel="nofollow" href="http://www.argon.org/~roderick/">http://www.argon.org/~roderick/</a> or <font SIZE="-1">CPAN</font> for updated versions.</p>
<h2>AUTHOR</h2>
<p> Roderick Schertler &lt;roderick [at] argon.org&gt; </p>
<h2>Index</h2>
