---
title: "dprofpp(1)"
name: "dprofpp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dprofpp/"
description: "dprofpp – display perl profile data"
---

<h2 class="name">NAME</h2>
<p> dprofpp &#8211; display perl profile data </p>
<h2>SYNOPSIS</h2>
<p> dprofpp [<code>-a</code>|<code>-z</code>|<code>-l</code>|<code>-v</code>|<code>-U</code>] [<code>-d</code>] [<code>-s</code>|<code>-r</code>|<code>-u</code>] [<code>-q</code>] [<code>-F</code>] [<code>-I|-E</code>] [<code>-O cnt</code>] [<code>-A</code>] [<code>-R</code>] [<code>-S</code>] [<code>-g subroutine</code>] [<code>-G</code> &lt;regexp&gt; [<code>-P</code>]] [<code>-f</code> &lt;regexp&gt;] [profile] </p>
<p> dprofpp <code>-T</code> [<code>-F</code>] [<code>-g subroutine</code>] [profile] </p>
<p> dprofpp <code>-t</code> [<code>-F</code>] [<code>-g subroutine</code>] [profile] </p>
<p> dprofpp <code>-G</code> &lt;regexp&gt; [<code>-P</code>] [profile] </p>
<p> dprofpp <code>-p script</code> [<code>-Q</code>] [other opts] </p>
<p> dprofpp <code>-V</code> [profile]</p>
<h2>DESCRIPTION</h2>
<p> The <i>dprofpp</i> command interprets profile data produced by a profiler, such as the Devel::DProf profiler. Dprofpp will read the file <i>tmon.out</i> and display the 15 subroutines which are using the most time. By default the times for each subroutine are given exclusive of the times of their child subroutines. </p>
<p> To profile a Perl script run the perl interpreter with the <code>-d</code> switch. So to profile script <i>test.pl</i> with Devel::DProf use the following: </p>
<pre>
        $ perl5 -d:DProf test.pl
</pre>
<p> Then run dprofpp to analyze the profile. The output of dprofpp depends on the flags to the program and the version of Perl you&#8217;re using. </p>
<pre>
        $ dprofpp -u
        Total Elapsed Time =    1.67 Seconds
                 User Time =    0.61 Seconds
        Exclusive Times
        %Time Seconds     #Calls sec/call Name
         52.4   0.320          2   0.1600 main::foo
         45.9   0.280        200   0.0014 main::bar
         0.00   0.000          1   0.0000 DynaLoader::import
         0.00   0.000          1   0.0000 main::baz
</pre>
<p> The dprofpp tool can also run the profiler before analyzing the profile data. The above two commands can be executed with one dprofpp command. </p>
<pre>
        $ dprofpp -u -p test.pl
</pre>
<p> Consult &#8220;<font SIZE="-1">PROFILE</font> <font SIZE="-1">FORMAT</font>&#8221; in Devel::DProf for a description of the raw profile.</p>
<h2>OUTPUT</h2>
<p> Columns are:</p>
<dl>
<dt>%Time</p>
<dd> Percentage of time spent in this routine.</p>
<dt>#Calls</p>
<dd> Number of calls to this routine.</p>
<dt>sec/call</p>
<dd> Average number of seconds per call to this routine.</p>
<dt>Name</p>
<dd> Name of routine.</p>
<dt>CumulS</p>
<dd> Time (in seconds) spent in this routine and routines called from it.</p>
<dt>ExclSec</p>
<dd> Time (in seconds) spent in this routine (not including those called from it).</p>
<dt>Csec/c</p>
<dd> Average time (in seconds) spent in each call of this routine (including those called from it).</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Sort alphabetically by subroutine names.</p>
<dt><code>-d</code></p>
<dd> Reverse whatever sort is used</p>
<dt><code>-A</code></p>
<dd> Count timing for autoloaded subroutine as timing for <tt>*::AUTOLOAD</tt>. Otherwise the time to autoload it is counted as time of the subroutine itself (there is no way to separate autoload time from run time). </p>
<p> This is going to be irrelevant with newer Perls. They will inform <tt>&quot;Devel::DProf&quot;</tt> <i>when</i> the <tt>&quot;AUTOLOAD&quot;</tt> switches to actual subroutine, so a separate statistics for <tt>&quot;AUTOLOAD&quot;</tt> will be collected no matter whether this option is set.</p>
<dt><code>-R</code></p>
<dd> Count anonymous subroutines defined in the same package separately.</p>
<dt><code>-E</code></p>
<dd> (default) Display all subroutine times exclusive of child subroutine times.</p>
<dt><code>-F</code></p>
<dd> Force the generation of fake exit timestamps if dprofpp reports that the profile is garbled. This is only useful if dprofpp determines that the profile is garbled due to missing exit timestamps. You&#8217;re on your own if you do this. Consult the <font SIZE="-1">BUGS</font> section.</p>
<dt><code>-I</code></p>
<dd> Display all subroutine times inclusive of child subroutine times.</p>
<dt><code>-l</code></p>
<dd> Sort by number of calls to the subroutines. This may help identify candidates for inlining.</p>
<dt><code>-O cnt</code></p>
<dd> Show only <i>cnt</i> subroutines. The default is 15.</p>
<dt><code>-p script</code></p>
<dd> Tells dprofpp that it should profile the given script and then interpret its profile data. See <code>-Q</code>.</p>
<dt><code>-Q</code></p>
<dd> Used with <code>-p</code> to tell dprofpp to quit after profiling the script, without interpreting the data.</p>
<dt><code>-q</code></p>
<dd> Do not display column headers.</p>
<dt><code>-r</code></p>
<dd> Display elapsed real times rather than user+system times.</p>
<dt><code>-s</code></p>
<dd> Display system times rather than user+system times.</p>
<dt><code>-T</code></p>
<dd> Display subroutine call tree to stdout. Subroutine statistics are not displayed.</p>
<dt><code>-t</code></p>
<dd> Display subroutine call tree to stdout. Subroutine statistics are not displayed. When a function is called multiple consecutive times at the same calling level then it is displayed once with a repeat count.</p>
<dt><code>-S</code></p>
<dd> Display <i>merged</i> subroutine call tree to stdout. Statistics are displayed for each branch of the tree. </p>
<p> When a function is called multiple (<i>not necessarily consecutive</i>) times in the same branch then all these calls go into one branch of the next level. A repeat count is output together with combined inclusive, exclusive and kids time. </p>
<p> Branches are sorted with regard to inclusive time.</p>
<dt><code>-U</code></p>
<dd> Do not sort. Display in the order found in the raw profile.</p>
<dt><code>-u</code></p>
<dd> Display user times rather than user+system times.</p>
<dt><code>-V</code></p>
<dd> Print dprofpp&#8217;s version number and exit. If a raw profile is found then its <font SIZE="-1">XS_VERSION</font> variable will be displayed, too.</p>
<dt><code>-v</code></p>
<dd> Sort by average time spent in subroutines during each call. This may help identify candidates for inlining.</p>
<dt><code>-z</code></p>
<dd> (default) Sort by amount of user+system time used. The first few lines should show you which subroutines are using the most time.</p>
<dt><code>-g</code> &quot;subroutine&quot;</p>
<dd> Ignore subroutines except <tt>&quot;subroutine&quot;</tt> and whatever is called from it.</p>
<dt><code>-G</code> &lt;regexp&gt;</p>
<dd> Aggregate &#8220;Group&#8221; all calls matching the pattern together. For example this can be used to group all calls of a set of packages </p>
<pre>
  -G &quot;(package1::)|(package2::)|(package3::)&quot;
</pre>
<p> or to group subroutines by name: </p>
<pre>
  -G &quot;getNum&quot;
</pre>
<dt><code>-P</code></p>
<dd> Used with -G to aggregate &#8220;Pull&#8221; together all calls that did not match -G.</p>
<dt><code>-f</code> &lt;regexp&gt;</p>
<dd> Filter all calls matching the pattern.</p>
<dt><code>-h</code></p>
<dd> Display brief help and exit.</p>
<dt><code>-H</code></p>
<dd> Display long help and exit.</dl>
<h2>ENVIRONMENT</h2>
<p> The environment variable <font SIZE="-1"><code>DPROFPP_OPTS</code></font> can be set to a string containing options for dprofpp. You might use this if you prefer <code>-I</code> over <code>-E</code> or if you want <code>-F</code> on all the time. </p>
<p> This was added fairly lazily, so there are some undesirable side effects. Options on the commandline should override options in DPROFPP_OPTS&#8211;but don&#8217;t count on that in this version.</p>
<h2>BUGS</h2>
<p> Applications which call <i>_exit()</i> or <i>exec()</i> from within a subroutine will leave an incomplete profile. See the <code>-F</code> option. </p>
<p> Any bugs in Devel::DProf, or any profiler generating the profile data, could be visible here. See &#8220;<font SIZE="-1">BUGS</font>&#8221; in Devel::DProf. </p>
<p> Mail bug reports and feature requests to the perl5-porters mailing list at <i>&lt;perl5-porters [at] perl.org&gt;</i>. Bug reports should include the output of the <code>-V</code> option.</p>
<h2>FILES</h2>
<pre>
        dprofpp         - profile processor
        tmon.out        - raw profile
</pre>
<h2>SEE ALSO</h2>
<p> perl, Devel::DProf, <i><a href="/docs/linux/man/2-times/">times</a></i>(2) </p>
<h2>Index</h2>
