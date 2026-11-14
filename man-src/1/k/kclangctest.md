---
title: "kclangctest(1)"
name: "kclangctest"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kclangctest/"
description: "kclangctest – command line interface to test the C language binding"
---

<h2 class="name">NAME</h2>
<p> kclangctest &#8211; command line interface to test the C language binding</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>kclangctest</code>&#8216; is a utility for facility test and performance test of the C language binding. This command is used in the following format. `<i>path</i>&#8216; specifies the path of a database file. `<i>rnum</i>&#8216; specifies the number of iterations. </p>
<dl>
<dt>
<dd>
 <code>kclangctest order </code>[<code>-rnd</code>][<code>-etc</code>][<code>-tran</code>][<code>-oat</code>|<code>-onl</code>|<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs in-order tests.</dl>
<p> <code>kclangctest index </code>[<code>-rnd</code>][<code>-etc</code>][<code>-oat</code>|<code>-onl</code>|<code>-onl</code>|<code>-otl</code>|<code>-onr</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs indexing operations.</dl>
<p> <code>kclangctest map </code>[<code>-rnd</code>][<code>-etc</code>][<code>-bnum </code><i>num</i>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of memory-saving hash map.</dl>
<p> <code>kclangctest list </code>[<code>-rnd</code>][<code>-etc</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of memory-saving array list.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-rnd</code> : performs random test.<br />
 <code>-etc</code> : performs miscellaneous operations.<br />
 <code>-tran</code> : performs transaction.<br />
 <code>-oat</code> : opens the database with the auto transaction option.<br />
 <code>-oas</code> : opens the database with the auto synchronization option.<br />
 <code>-onl</code> : opens the database with the no locking option.<br />
 <code>-otl</code> : opens the database with the try locking option.<br />
 <code>-onr</code> : opens the database with the no auto repair option.<br />
 <code>-bnum </code><i>num</i> : specifies the number of buckets of the hash table.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kcpolymgr/">kcpolymgr</a></code>(1), <code><a href="/docs/linux/man/1-kcpolytest/">kcpolytest</a></code>(1) </p>
<h2>Index</h2>
