---
title: "yum-complete-transaction(8)"
name: "yum-complete-transaction"
section: "8"
letter: "y"
url: "/docs/linux/man/8-yum-complete-transaction/"
description: "yum-complete-transaction – attempt to complete failed or aborted Yum transactions"
---

<p>yum-complete-transaction &#8211; attempt to complete failed or aborted Yum transactions</p>
<h2>Synopsis</h2>
<p><code>yum-complete-transaction</code> [options]</p>
<h2>General Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Help; display a help message and then quit.</p>
<dt><code>&#8211;cleanup-only</code></p>
<dd>Only clean up only transaction journal files and exit. </p>
</dl>
<h2>Description</h2>
<p><code>yum-complete-transaction</code> is a program which finds incomplete or aborted yum transactions on a system and attempts to complete them. It looks at the transaction-all* and transaction-done* files which can normally be found in /var/lib/yum if a yum transaction aborted in the middle of execution. If it finds more than one unfinished transaction it will attempt to complete the most recent one first. You can run it more than once to clean up all unfinished transactions. </p>
<h2>Files</h2>
<p>As yum-complete-transaction uses YUM libraries for retrieving all the information, it relies on YUM configuration for its default values like which repositories to use. Consult YUM documentation for details: </p>
<pre>/etc/yum.conf
/etc/yum/repos.d/
/var/cache/yum/</pre>
<h2>See Also</h2>
<pre><i>yum.conf (5)</i>
<a rel="nofollow" href="http://yum.baseurl.org/">http://yum.baseurl.org/</a></pre>
<h2>Authors</h2>
<pre>See the Authors file included with this program.</pre>
<h2>Bugs</h2>
<p>There are of course no bugs, but should you find any, you should first consult the FAQ section on <a rel="nofollow" href="http://yum.baseurl.org/wiki/Faq">http://yum.baseurl.org/wiki/Faq</a> and if unsuccessful in finding a resolution contact the mailing list: yum-devel [at] lists.baseurl.org. To file a bug use <a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a> for Fedora/RHEL/Centos related bugs and <a rel="nofollow" href="http://yum.baseurl.org/report">http://yum.baseurl.org/report</a> for all other bugs. </p>
