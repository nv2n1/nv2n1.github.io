---
title: "mailcap-order(5)"
name: "mailcap-order"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mailcap-order/"
description: "/etc/mailcap.order – the mailcap ordering specifications"
---

<p>/etc/mailcap.order &#8211; the mailcap ordering specifications</p>
<h2>Description</h2>
<p>The order of entries in the <i>/etc/mailcap</i> file can be altered by editing the <i>/etc/mailcap.order</i> file. Each line of that file specifies a package and an optional mime type. Mailcap entries that match will be placed in the order of this file. Entries that don&#8217;t match will be placed later.</p>
<h3>Example</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mime-support:*/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gv:application/postscript<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;netscape:text/html<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;less:text/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;emacs:text/* </p>
<p> The above would make any entries provided by the <code>mime-support</code> package (as found in the <i>/usr/lib/mime/packages</i> directory) take priority over everything else. The <code>gv</code> package will be used over anything else when it comes to postscript documents. <code>Netscape</code> will be used for any html documents and <code>less</code> will be used for any remaining text documents. However, since neither netscape or less provide for editing documents, any edit or compose actions will fall through to the <code>emacs</code> rules. </p>
<p> After modifying this file, be sure to run <i>/usr/sbin/update-mime</i> (as root) to propagate the changes into the <i>/etc/mailcap</i> file. </p>
<p> Remember that this files takes <i>package</i> names and not <i>executable</i> names. If you want to define rules that reference specific programs, the best way is to include them in <i>~/.mailcap</i> or the user section of the <i>/etc/mailcap</i> file.</p>
<h2>Limitations</h2>
<p>There is currently no way to break out a certain type from a wildcard rule. If, for example, both xv and gimp were to specify &quot;image/*&quot; rules, it isn&#8217;t possible to use xv for <i>gif</i> images but use gimp for <i>jpeg</i> images. </p>
<p> Also, I would like to add the ability to specify certain actions in the rules. For example, if netscape were to have an <i>edit</i> rule but I wanted to use emacs for editing/creating html documents, I could place a line like </p>
<p>&nbsp;<wbr>&nbsp;emacs:text/*&nbsp;action=edit|compose </p>
<p> before the netscape entry. The <code>update-mime</code> program would then spit out entries such that netscape <i>view</i> rule comes <code>before</code> the emacs <i>view</i> rule but have the netscape <i>edit</i> rule comes <code>after</code> the emacs <i>edit</i> rule.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-mailcap/">mailcap</a></code>(5) <code><a href="/docs/linux/man/1-run-mailcap/">run-mailcap</a></code>(1) <code><a href="/docs/linux/man/8-update-mime/">update-mime</a></code>(8)</p>
<h2>Author</h2>
<p>The <code>mailcap.order</code> specification was written by Brian White &lt;bcwhite [at] pobox.com&gt;</p>
