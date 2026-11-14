---
title: "inadyn(5)"
name: "inadyn"
section: "5"
letter: "i"
url: "/docs/linux/man/5-inadyn/"
description: "inadyn.conf – configuration for the inadyn client for open DNS servers."
---

<p>inadyn.conf &#8211; configuration for the inadyn client for open DNS servers.</p>
<h2>Description</h2>
<p><code>inadyn</code> can read the very same options which can be present in the command line from a configuration file. This feature allows the user to write the options only once, and avoids frequent retyping. </p>
<p> The format of the file follows the *NIX tradition:</p>
<dl>
<dd>a &#8216;#&#8217; character denotes a comment.</p>
<dd>The long options (those with &#8216;&#8211;&#8216; in front) can also be placed at the beginning of the line without &#8216;&#8211;&#8216; signs.</p>
<dd>a \ can be used as an escape character.</dl>
<h2>Examples</h2>
<h3>1.</h3>
<p>#Some comment about inadyn cfg file &#8211;username test &#8211;password test &#8211;update_period 60000 &#8211;alias test.homeip.net &#8211;alias my.second.domain<br />
&nbsp;<wbr></p>
<h3>2.</h3>
<p>&#8211;username test # user &#8211;password test update_period 60000 # some other param without &#8216;&#8211;&#8216; alias test.homeip.net </p>
<h2>See Also</h2>
<h3>Other manual pages</h3>
<p><a href="/docs/linux/man/8-inadyn/">inadyn</a>(8).</p>
<h3>Internet resources</h3>
<p><code>Inadyn</code> &#8216;s home page is <a rel="nofollow" href="http://inadyn.ina-tech.net.">http://inadyn.ina-tech.net.</a></p>
<h2>Author</h2>
<p><code>inadyn</code> was written by Narcis Ilisei, &lt;inarcis2002 [at] hotpop.com&gt;. </p>
<p> This manual page was written by Shaul Karl, &lt;shaul [at] debian.org&gt;, for the <code>Debian GNU/Linux</code> system, based on the readme.html file that is found in the source.</p>
