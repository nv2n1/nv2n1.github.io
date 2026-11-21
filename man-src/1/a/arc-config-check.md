---

title: "arc-config-check(1)"
name: "arc-config-check"
section: "1"
letter: "a"
url: "/docs/linux/man/1-arc-config-check/"
description: "arc-config-check – checks the arc.conf for inconsistencies, known problems or (in a future development) just general bad taste."
---

<p> arc-config-check &#8211;printall </p>
<p> The motivation behind this little script was to have a repository for automated tests on issues that came up on the NorduGrid developers mailing list. As such this script indicates directories that are not present, checks host certificates, CA certificates and CRLs, validates the sanity of ARC configuration and tests for clock skew. </p>
<p> BECAUSE EVERY INSTALLATION OF ARC IS DIFFERENT THIS UTILITY ONLY SUGGESTS WHAT COULD BE WRONG. SOMETIMES IT IS OVERRESTRICTIVE. AND SOMETIMES IT CAN MISS SOME MISCONFIGURATION. NEVER TREAT RESULTS PRODUCED BY IT AS ULTIMATE TRUTH. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;config &lt;string&gt;</code></dt>
<dd> Specifies the location of the config file, by default it is /etc/arc.conf</dd>
<dt><code>&#8211;printall</code></dt>
<dd> Lists all variable names of the config file together with their values.</dd>
<dt><code>&#8211;timeserver &lt;server&gt;</code></dt>
<dd> Allows the specification of a server against which to test the local system&#8217;s time.</dd>
<dt><code>&#8211;skip-warnings</code></dt>
<dd> Do not show warnings.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Quick summary of options</dd>
<dt><code>&#8211;man</code></dt>
<dd> Detailed man page. </dd>
</dl>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> ARC software is developed by the NorduGrid Collaboration (<a rel="nofollow" href="http://www.nordugrid.org">http://www.nordugrid.org</a>), please consult the AUTHORS file distributed with ARC. Please report bugs and feature requests to <a rel="nofollow" href="http://bugzilla.nordugrid.org">http://bugzilla.nordugrid.org</a> </p>
