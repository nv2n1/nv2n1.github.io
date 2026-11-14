---
title: "lintianoutput(3)"
name: "lintianoutput"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianoutput/"
description: "Lintian::Output – Lintian messaging handling"
---

<p>Lintian::Output &#8211; Lintian messaging handling </p>
<h2>Synopsis</h2>
<pre> # non-OO
 use Lintian::Output qw(:messages);
 $Lintian::Output::GLOBAL-&gt;<a href="//www.systutorials.com/docs/linux/man/1-verbosity_level/">verbosity_level</a>(1);
 msg(&quot;Something interesting&quot;);
 v_msg(&quot;Something less interesting&quot;);
 debug_msg(3, &quot;Something very specific&quot;);
 # OO
 use Lintian::Output;
 my $out = Lintian::Output-&gt;new;
 $out-&gt;verbosity_level(-1);
 $out-&gt;msg(&quot;Something interesting&quot;);
 $out-&gt;v_msg(&quot;Something less interesting&quot;);
 $out-&gt;debug_msg(3, &quot;Something very specific&quot;);</pre>
<h2>Description</h2>
<p>Lintian::Output is used for all interaction between lintian and the user. It is designed to be easily extensible via subclassing. </p>
<p> To simplify usage in the most common cases, many Lintian::Output methods can be used as class methods and will therefore automatically use the object <tt>$Lintian::Output::GLOBAL</tt> unless their first argument <tt>&quot;isa('Lintian::Output')&quot;</tt>.</p>
<h2>Attributes</h2>
<p>The following fields impact the behavior of Lintian::Output.</p>
<dl COMPACT>
<dt>color</p>
<dd>Can take the values &#8220;never&#8221;, &#8220;always&#8221;, &#8220;auto&#8221; or &#8220;html&#8221;. </p>
<p> Whether to colorize tags based on their severity. The default is &#8220;never&#8221;, which never uses color. &#8220;always&#8221; will always use color, &#8220;auto&#8221; will use color only if the output is going to a terminal. </p>
<p> &#8220;html&#8221; will output <font SIZE="-1">HTML</font> &lt;span&gt; tags with a color style attribute (instead of <font SIZE="-1">ANSI</font> color escape sequences).</p>
<dt>colors</p>
<dd>
<dt>debug</p>
<dd>If set to a positive integer, will enable all debug messages issued with a level lower or equal to its value.</p>
<dt>issuedtags</p>
<dd>Hash containing the names of tags which have been issued.</p>
<dt>perf_debug</p>
<dd>
<dt>perf_log_fd</p>
<dd>
<dt>proc_id2tag_count</p>
<dd>
<dt>stdout</p>
<dd>I/O handle to use for output of messages and tags. Defaults to <tt>&quot;\*STDOUT&quot;</tt>.</p>
<dt>stderr</p>
<dd>I/O handle to use for warnings. Defaults to <tt>&quot;\*STDERR&quot;</tt>.</p>
<dt>showdescription</p>
<dd>Whether to show the description of a tag when printing it.</p>
<dt>tty_hyperlinks</p>
<dd>
<dt>tag_display_limit</p>
<dd>Get/Set the number of times a tag is emitted per processable.</p>
<dt>verbosity_level</p>
<dd>Determine how verbose the output should be. &#8220;0&#8221; is the default value (tags and msg only), &#8220;-1&#8221; is quiet (tags only) and &#8220;1&#8221; is verbose (tags, msg and v_msg).</dl>
<h2>Class/Instance Methods</h2>
<p>These methods can be used both with and without an object. If no object is given, they will fall back to the <tt>$Lintian::Output::GLOBAL</tt> object.</p>
<dl COMPACT>
<dt>&quot;msg(@args)&quot;</p>
<dd>Will output the strings given in <tt>@args</tt>, one per line, each line prefixed with &#8216;N: &#8216;. Will do nothing if verbosity_level is less than 0.</p>
<dt>&quot;v_msg(@args)&quot;</p>
<dd>Will output the strings given in <tt>@args</tt>, one per line, each line prefixed with &#8216;N: &#8216;. Will do nothing unless verbosity_level is greater than 0.</p>
<dt>&quot;debug_msg($level, @args)&quot;</p>
<dd><tt>$level</tt> should be a positive integer. </p>
<p> Will output the strings given in <tt>@args</tt>, one per line, each line prefixed with &#8216;N: &#8216;. Will do nothing unless debug is set to a positive integer &gt;= <tt>$level</tt>.</p>
<dt>&quot;warning(@args)&quot;</p>
<dd>Will output the strings given in <tt>@args</tt> on stderr, one per line, each line prefixed with &#8216;warning: &#8216;.</p>
<dt>&quot;perf_log(@args)&quot;</p>
<dd>Like &#8220;v_msg&#8221;, except output is possibly sent to a dedicated log file. </p>
<p> Will output the strings given in <tt>@args</tt>, one per line. The lines will not be prefixed. Will do nothing unless perf_debug is set to a positive integer.</p>
<dt>&quot;delimiter()&quot;</p>
<dd>Gives back a string that is usable for separating messages in the output. Note: This does not print anything, it just gives back the string, use with one of the methods above, e.g. </p>
<pre> v_msg('foo', delimiter(), 'bar');</pre>
<dt>&quot;issued_tag($tag_name)&quot;</p>
<dd>Indicate that the named tag has been issued. Returns a boolean value indicating whether the tag had previously been issued by the object.</p>
<dt>&quot;string($lead, @args)&quot;</p>
<dd><font SIZE="-1">TODO:</font> Is this part of the public interface?</dl>
<h2>Instance Methods For Subclassing</h2>
<p>The following methods are only intended for subclassing and are only available as instance methods. The methods mentioned in &#8220;<font SIZE="-1">CLASS/INSTANCE METHODS&#8221;</font> usually only check whether they should do anything at all (according to the values of verbosity_level and debug) and then call one of the following methods to do the actual printing. Almost all of them finally call <code>_print()</code> to do that. This convoluted scheme is necessary to be able to use the methods above as class methods and still make the behaviour overridable in subclasses.</p>
<dl COMPACT>
<dt>&quot;_message(@args)&quot;</p>
<dd>Called by <code>msg()</code>, <code>v_msg()</code>, and <code>debug_msg()</code> to print the message.</p>
<dt>&quot;_warning(@args)&quot;</p>
<dd>Called by <code>warning()</code> to print the warning.</p>
<dt>&quot;_print($stream, $lead, @args)&quot;</p>
<dd>Called by <code>_message()</code>, <code>_warning()</code>, and <code>print_tag()</code> to do the actual printing. </p>
<p> If you override these three methods, you can change the calling convention for this method to pretty much whatever you want. </p>
<p> The version in Lintian::Output prints the strings in <tt>@args</tt>, one per line, each line preceded by <tt>$lead</tt> to the I/O handle given in <tt>$stream</tt>.</p>
<dt>&quot;_delimiter()&quot;</p>
<dd>Called by <code>delimiter()</code>.</p>
<dt>&quot;_do_color()&quot;</p>
<dd>Called by <code>print_tag()</code> to determine whether to produce colored output.</dl>
<h2>Exports</h2>
<p>Lintian::Output exports nothing by default, but the following export tags are available:</p>
<dl COMPACT>
<dt>:messages</p>
<dd>Exports all the methods in &#8220;<font SIZE="-1">CLASS/INSTANCE METHODS&#8221;</font></p>
<dt>:util</p>
<dd>Exports all the methods in &#8220;<font SIZE="-1">CLASS METHODS&#8221;</font></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
