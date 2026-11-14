---
title: "krb-equiv(5)"
name: "krb-equiv"
section: "5"
letter: "k"
url: "/docs/linux/man/5-krb-equiv/"
description: "/etc/krb.equiv – Kerberos equivalences"
---

<p>&nbsp;<wbr>*</p>
<h2>Name</h2>
<p><code>/etc/krb.equiv</code> &#8211; Kerberos equivalences</p>
<h2>Description</h2>
<p><i>krb.equiv</i> contains zero or more lines, each of which describes a mapping of a kerberos principal (<i>userid [at] host</i>) to a local user (<i>userid</i> or alias). Each line of the file consists of two fields, separated by at least one whitespace character; other blanks are ignored. The first field is the kerberos principal name to remap, and the second is the name of the corresponding local user.</p>
<h2>Sample File</h2>
<pre>tyq4 [at] ANDY.CMU.EDU tyq4
tyq4 [at] DEANNA.ORG tyq4
ty347 [at] ECE.CMU.EDU tyq4
jj12 [at] ANDY.CMU.EDU tick
tick [at] DEANNA.ORG tick
jy9o [at] ANDY.CMU.EDU jyager
jyager [at] CS.CMU.EDU jyager</pre>
