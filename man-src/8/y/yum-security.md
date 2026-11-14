---
title: "yum-security(8)"
name: "yum-security"
section: "8"
letter: "y"
url: "/docs/linux/man/8-yum-security/"
description: "yum security plugin"
---

<p>yum security plugin</p>
<h2>Synopsis</h2>
<p><code>yum</code> [options] [command] [package &#8230;]</p>
<h2>Description</h2>
<p>This plugin extends <code>yum</code> to allow lists and updates to be limited using security relevant criteria added yum <i>command</i>s are:<br />
 <i></i> * update-minimal This works like the update command, but if you have the the package foo-1 installed and have foo-2 and foo-3 available with updateinfo.xml then update-minimal will update you to foo-3.<br />
 <i></i> * info-updateinfo<br />
 <i></i> * list-updateinfo both of the last two take these <i>sub-commands</i>s:<br />
 <i></i> * * &lt;advisory&gt; [advisory&#8230;]<br />
 <i></i> * * bugzillas<br />
 <i></i> * * cves<br />
 <i></i> * * security<br />
 <i></i> * * new-packages </p>
<dl>
<dt><code>&lt;advisory&gt; [advisory&#8230;]</code></p>
<dd>Is used to display information about one or more advisories.</dl>
<dl>
<dt><code>list-updateinfo</code></p>
<dd>Is used to list all of the relevant errata notice information, from the updateinfo.xml data in yum. This includes bugzillas, CVEs, security updates and new.</p>
<dd>
<dt><code>bugzillas / bzs</code></p>
<dd>Is the subset of the updateinfo information, pertaining to the bugzillas.</p>
<dd>
<dt><code>cves</code></p>
<dd>Is the subset of the updateinfo information, pertaining to the CVEs.</p>
<dd>
<dt><code>security / sec</code></p>
<dd>Is the subset of the updateinfo information, pertaining to security.</p>
<dt><code>bugfix</code></p>
<dd>Is the subset of the updateinfo information, pertaining to bugfixes.</p>
<dt><code>enhancement</code></p>
<dd>Is the subset of the updateinfo information, pertaining to enhancements.</p>
<dt><code>recommended</code></p>
<dd>Is the subset of the updateinfo information, pertaining to recommended updates.</p>
<dt><code>new-packages</code></p>
<dd>Is the subset of the updateinfo information, pertaining to new packages. These are packages which weren&#8217;t available at the initial release of your distribution.</p>
<dd></dl>
<h2>General Options</h2>
<p>There are four options added to yum that are available in the &quot;list updates&quot;, &quot;info updates&quot;, &quot;check-update&quot; and &quot;update&quot; commands. They are: </p>
<dl>
<dt><code>&#8211;advisory</code></p>
<dd>This option includes packages coresponding to the advisory ID, Eg. FEDORA-2201-123.</p>
<dt><code>&#8211;bz</code></p>
<dd>This option includes packages that say they fix a Bugzilla ID, Eg. 123.</p>
<dt><code>&#8211;cve</code></p>
<dd>This option includes packages that say they fix a CVE &#8211; Common Vulnerabilities and Exposures ID (<a rel="nofollow" href="http://cve.mitre.org/about/">http://cve.mitre.org/about/</a>), Eg. CVE-2201-0123.</p>
<dt><code>&#8211;bugfixes</code></p>
<dd>This option includes packages that say they fix a bugfix issue.</p>
<dt><code>&#8211;security</code></p>
<dd>This option includes packages that say they fix a security issue.</dl>
<h2>Examples</h2>
<p>To list all updates that are security relevant, and get a reutrn code on whether there are security updates use:</p>
<dl>
<dd>yum &#8211;security check-update</dl>
<p> To upgrade packages that have security errata (upgrades to the latest available package) use:</p>
<dl>
<dd>yum &#8211;security update</dl>
<p> To upgrade packages that have security errata (upgrades to the last security errata package) use:</p>
<dl>
<dd>yum &#8211;security update-minimal</dl>
<p> To get a list of all BZs that are fixed for packages you have installed use:</p>
<dl>
<dd>yum list-updateinfo bugzillas</dl>
<p> To get the information on advisory FEDORA-2707-4567 use:</p>
<dl>
<dd>yum info-updateinfo FEDORA-2707-4567</dl>
<p> To update packages to the latest version which contain fixes for Bugzillas 123, 456 and 789; and all security updates use:</p>
<dl>
<dd>yum &#8211;bz 123 &#8211;bz 456 &#8211;bz 789 &#8211;security update</dl>
<p> To update to the packages which just update Bugzillas 123, 456 and 789; and all security updates use:</p>
<dl>
<dd>yum &#8211;bz 123 &#8211;bz 456 &#8211;bz 789 &#8211;security update-minimal</dl>
<p> To get an info list of the latest packages which contain fixes for Bugzilla 123; CVEs CVE-2207-0123 and CVE-2207-3210; and Fedora advisories FEDORA-2707-4567 and FEDORA-2707-7654 use:</p>
<dl>
<dd>yum &#8211;bz 123 &#8211;cve CVE-2207-0123 &#8211;cve CVE-2207-3210 &#8211;advisory FEDORA-2707-4567 &#8211;advisory FEDORA-2707-7654 info updates</dl>
<p> To get a list of packages which are &quot;new&quot;.</p>
<dl>
<dd>yum list-updateinfo new </p>
<h2>See Also</h2>
<pre><i>yum (8)</i>
<i>yum.conf (5)</i></pre>
<h2>Authors</h2>
<pre>James Antill &lt;james.antill [at] redhat.com&gt;.</pre>
<h2>Bugs</h2>
<p>The update-minimal command ignores the &#8211;obsoletes flag. The update-minimal command can only directly affect things atm., so if you update pkgA minimally but that requires an update to pkgB then pkgB will be updated to the newest version by the depsolver. Also the above will happen even if you&#8217;ve also minimally updated pkgB, if either the direct (minimal) update for pkgB happens after or if the minimal update for pkgB doesn&#8217;t satisy the requirements of pkgA. The main &quot;problem&quot; is that if the data is not correct the plugin cannot work correctly. For instance &quot;&#8211;bz 123&quot; will not fix BZ 123 if a package is updated to fix that BZ without referencing that it does so in the updateinfo.xml. </p>
