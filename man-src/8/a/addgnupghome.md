---
title: "addgnupghome(8)"
name: "addgnupghome"
section: "8"
letter: "a"
url: "/docs/linux/man/8-addgnupghome/"
description: "addgnupghome – Create .gnupg home directories"
---

<p><code>addgnupghome</code> &#8211; Create .gnupg home directories</p>
<h2>Synopsis</h2>
<p><code>addgnupghome</code> <i>account_1</i> <i>account_2</i>&#8230;<i>account_n</i> </p>
<h2>Description</h2>
<p>If GnuPG is installed on a system with existing user accounts, it is sometimes required to populate the GnuPG home directory with existing files. Especially a &#8216;<i>trustlist.txt</i>&#8216; and a keybox with some initial certificates are often desired. This script helps to do this by copying all files from &#8216;<i>/etc/skel/.gnupg</i>&#8216; to the home directories of the accounts given on the command line. It takes care not to overwrite existing GnuPG home directories. <code>addgnupghome</code> is invoked by root as:</p>
<dl>
<dd>
<pre>addgnupghome account1 account2 ... accountn</pre>
</dl>
