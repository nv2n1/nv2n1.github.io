---
title: "mirmon-pm(1)"
name: "mirmon-pm"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mirmon-pm/"
description: "Mirmon – OO interface for mirmon objects"
---

<p>Mirmon &#8211; OO interface for mirmon objects</p>
<h2>Synopsis</h2>
<pre> use Mirmon ;</pre>
<pre> $m = Mirmon -&gt; new ( [ $path-to-config ] )</pre>
<pre> $conf = $m -&gt; conf ; # a Mirmon::Conf object
 $state = $m -&gt; state ; # the mirmon state</pre>
<pre> for my $url ( keys %$state )
 { $mirror = $state -&gt; { $url } ; # a Mirmon::Mirror object
 $mail = $mirror -&gt; mail ; # contact address
 $mirror -&gt; age ( time ) ; # set mirror age
 }</pre>
<p>Many class and object methods can be used to get or set attributes : </p>
<pre> $object -&gt; attribute # get an atttibute
 $object -&gt; attribute ( $attr ) # set an atttibute</pre>
<h2>Mirmon class methods</h2>
<dl COMPACT>
<dt><code>new ( [$path] )</code></p>
<dd>Create a Mirmon object from a config file found in <tt>$path</tt>, or (by default) in the default list of possible config files. Related objects (config, state) are created and initialised.</p>
<dt>verbosity</p>
<dd>Mirmon always reports errors. Normally it only reports changes (inserts/deletes) found in the mirror_list ; in <i>quiet</i> mode, it doesn&#8217;t. In <i>verbose</i> mode, it reports progress: the startup and finishing of probes. </p>
<pre> Mirmon::verbose ( [ $bool ] ) # get/set verbose
 Mirmon::quiet ( [ $bool ] ) # get/set quiet
 Mirmon::debug ( [ $bool ] ) # get/set debug</pre>
</dl>
<h2>Mirmon object methods</h2>
<dl COMPACT>
<dt><code>conf</code></p>
<dd>Returns Mirmon&#8217;s Mirmon::Conf object.</p>
<dt><code>state</code></p>
<dd>Returns a hashref <tt>&quot;{ url =&gt; mirror, ... }&quot;</tt>, where <i>url</i> is as specified in the mirror list and <i>mirror</i> is a Mirmon::Mirror object.</p>
<dt><code>regions</code></p>
<dd>Returns a hashref <tt>&quot;{ country_code =&gt; country_name, ... }&quot;</tt>.</p>
<dt><code>config_list</code></p>
<dd>Returns the list of default locations for config files.</p>
<dt><code>get_dates ( $get [, </code>$URL<code>] )</code></p>
<dd>Probes all mirrors if <tt>$get</tt> is <tt>&quot;all&quot;</tt> ; or a subset if <tt>$get</tt> is <tt>&quot;update&quot;</tt> ; or only <i>$URL</i> if <tt>$get</tt> is <tt>&quot;url&quot;</tt>.</dl>
<h2>Mirmon::Conf object methods</h2>
<p>A Mirmon::Conf object represents a mirmon conguration. It is normaly created by <i>Mirmon::new()</i>. A specified (or default) config file is read and interpreted.</p>
<dl COMPACT>
<dt>attribute methods</p>
<dd>For every config file entry, there is an attribute method : <code>web_page</code>, <code>state</code>, <code>countries</code>, <code>mirror_list</code>, <code>probe</code>, <code>project_name</code>, <code>project_url</code>, <code>icons</code>, <code>project_logo</code>, <code>timeout</code>, <code>max_probes</code>, <code>min_poll</code>, <code>max_poll</code>, <code>min_sync</code>, <code>max_sync</code>, <code>list_style</code>, <code>put_histo</code>, <code>randomize</code>, <code>add_slash</code>.</p>
<dt><code>root</code></p>
<dd>Returns the file name of (the root of) the configuration file(s).</p>
<dt><code>site_url</code></p>
<dd>Returns a hashref <tt>&quot;{ site =&gt; url, ... }&quot;</tt>, as specified in the mirmon config file.</dl>
<h2>Mirmon::Mirror object methods</h2>
<p>A Mirmon::Mirror object represents the last known state of a mirror. It is normaly created by <i>Mirmon::new()</i> from the state file, as specified in the mirmon config file. Mirmon::Mirror objects can be used to probe mirrors. </p>
<p> <code>attribute methods</code> </p>
<dl COMPACT>
<dt><code>url</code></p>
<dd>The url as given in the mirror list.</p>
<dt><code>age</code></p>
<dd>The mirror&#8217;s timestamp found by the last successful probe, or &#8216;undef&#8217; if no probe was ever successful.</p>
<dt><code>last_status</code></p>
<dd>The status of the last probe, or &#8216;undef&#8217; if the mirror was never probed.</p>
<dt><code>last_ok_probe</code></p>
<dd>The timestamp of the last successful probe or &#8216;undef&#8217; if the mirror was never successfully probed.</p>
<dt><code>probe_history</code></p>
<dd>The probe history is a list of &#8216;s&#8217; (for success) and &#8216;f&#8217; (for failure) characters indicating the result of the probe. New results are appended whenever the mirror is probed.</p>
<dt><code>state_history</code></p>
<dd>The state history consists of a timestamp, a &#8216;-&#8216; char, and a list of chars indicating a past status: &#8216;s&#8217; (fresh), &#8216;b&#8217; (oldish), &#8216;f&#8217; (old), &#8216;z&#8217; (bad) or &#8216;x&#8217; (skip). The timestamp indicates when the state history was last updated. The current status of the mirror is determined by the mirror&#8217;s age and a few configuration parameters (min_sync, max_sync, max_poll). The state history is updated when the mirror is probed. If the last update of the history was less than 24 hours ago, the last status is replaced by the current status. If the last update of the history was more than 24 hours ago, the current status is appended to the history. One or more &#8216;skip&#8217;s are inserted, if the timestamp is two or more days old (when mirmon hasn&#8217;t run for more than two days).</p>
<dt><code>last_probe</code></p>
<dd>The timestamp of the last probe, or &#8216;undef&#8217; if the mirror was never probed.
</dl>
<p> <code>object methods</code> </p>
<dl COMPACT>
<dt><code>mirmon</code></p>
<dd>Returns the parent Mirmon object.</p>
<dt><code>state_history_time</code></p>
<dd>Returns the <i>time</i> part of the state_history attribute.</p>
<dt><code>state_history_hist</code></p>
<dd>Returns the <i>history</i> part of the state_history attribute.</p>
<dt><code>type</code>, <code>site</code>, <code>home</code></p>
<dd>For an url like <i><a href="ftp://www.some.org/path/to/home">ftp://www.some.org/path/to/home</a></i>, the <code>type</code> is <i>ftp</i>, the <code>site</code> is <i><a rel="nofollow" href="http://www.some.org">www.some.org</a></i>, and <code>home</code> is <i><a href="ftp://www.some.org/">ftp://www.some.org/</a></i>.</p>
<dt><code>age_in_days</code></p>
<dd>Returns the mirror&#8217;s age (in fractional days), based on the mirror&#8217;s timestamp as found by the last successful probe ; or based on the length of the state history if no probe was ever successful. Returns &#8216;undef&#8217; if the mirror was never probed.</p>
<dt><code>mail</code></p>
<dd>Returns the mirror&#8217;s contact address as specified in the mirror list.</p>
<dt><code>region</code></p>
<dd>Returns the mirror&#8217;s country code as specified in the mirror list.</p>
<dt><code>start_probe</code></p>
<dd>Start a probe for the mirror in non-blocking mode ; returns the associated (IO::Handle) file handle. The caller must maintain an association between the handles and the mirror objects.</p>
<dt><code>finish_probe ( $handle )</code></p>
<dd>Sets the (IO::Handle) <code>$handle</code> to blocking <font SIZE="-1">IO</font> ; reads a result from the handle, and updates the state of the mirror.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-mirmon/">mirmon</a>(1) </p>
<h2>Author</h2>
<pre> (c) 2003-2016 Henk P. Penning
 Faculty of Science, Utrecht University
 <a rel="nofollow" href="http://www.staff.science.uu.nl/~penni101/">http://www.staff.science.uu.nl/~penni101/</a> -- penning [at] uu.nl
 mirmon-2.11 - Sat Jul 23 09:12:31 2016 ; henkp</pre>
