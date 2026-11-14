---
title: "kcpolytest(1)"
name: "kcpolytest"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kcpolytest/"
description: "kcpolytest – command line interface to test the polymorphic database"
---

<h2 class="name">NAME</h2>
<p> kcpolytest &#8211; command line interface to test the polymorphic database</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>kcpolytest</code>&#8216; is a utility for facility test and performance test of the polymorphic database. This command is used in the following format. `<i>path</i>&#8216; specifies the path of a database file. `<i>rnum</i>&#8216; specifies the number of iterations. </p>
<dl>
<dt>
<dd>
 <code>kcpolytest order </code>[<code>-th </code><i>num</i>][<code>-rnd</code>][<code>-set</code>|<code>-get</code>|<code>-getw</code>|<code>-rem</code>|<code>-etc</code>][<code>-tran</code>][<code>-oat</code>|<code>-onl</code>|<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-lv</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs in-order tests.</dl>
<p> <code>kcpolytest queue </code>[<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-rnd</code>][<code>-oat</code>|<code>-onl</code>|<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-lv</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs queuing operations.</dl>
<p> <code>kcpolytest wicked </code>[<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-oat</code>|<code>-onl</code>|<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-lv</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs mixed operations selected at random.</dl>
<p> <code>kcpolytest tran </code>[<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-hard</code>][<code>-oat</code>|<code>-onl</code>|<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-lv</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of transaction.</dl>
<p> <code>kcpolytest mapred </code>[<code>-rnd</code>][<code>-ru</code>][<code>-oat</code>|<code>-onl</code>|<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-lv</code>][<code>-tmp </code><i>str</i>][<code>-dbnum </code><i>num</i>][<code>-clim </code><i>num</i>][<code>-cbnum </code><i>num</i>][<code>-xnl</code>][<code>-xpm</code>][<code>-xpr</code>][<code>-xpf</code>][<code>-xnc</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs MapReduce operations.</dl>
<p> <code>kcpolytest index </code>[<code>-th </code><i>num</i>][<code>-rnd</code>][<code>-set</code>|<code>-get</code>|<code>-rem</code>|<code>-etc</code>][<code>-tran</code>][<code>-oat</code>|<code>-onl</code>|<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-lv</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs indexing operations.</dl>
<p> <code>kcpolytest misc </code><i>path</i></p>
<dl>
<dt>
<dd> Performs miscellaneous tests.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-th </code><i>num</i> : specifies the number of worker threads.<br />
 <code>-rnd</code> : performs random test.<br />
 <code>-set</code> : performs setting operation only.<br />
 <code>-get</code> : performs getting operation only.<br />
 <code>-getw</code> : performs getting with a buffer operation only.<br />
 <code>-rem</code> : performs removing operation only.<br />
 <code>-etc</code> : performs miscellaneous operations.<br />
 <code>-tran</code> : performs transaction.<br />
 <code>-oat</code> : opens the database with the auto transaction option.<br />
 <code>-oas</code> : opens the database with the auto synchronization option.<br />
 <code>-onl</code> : opens the database with the no locking option.<br />
 <code>-otl</code> : opens the database with the try locking option.<br />
 <code>-onr</code> : opens the database with the no auto repair option.<br />
 <code>-lv</code> : reports all errors.<br />
 <code>-it </code><i>num</i> : specifies the number of repetition.<br />
 <code>-hard</code> : performs physical synchronization.<br />
 <code>-ru</code> : reuses the existing database.<br />
 <code>-tmp </code><i>str</i> : specifies the path of a directory for temporary storage.<br />
 <code>-dbnum </code><i>num</i> : specifies the number of temporary databases.<br />
 <code>-clim </code><i>num</i> : specifies the limit size of cache memory.<br />
 <code>-cbnum </code><i>num</i> : specifies the bucket number of cache memory.<br />
 <code>-xnl</code> : executes with the no locking option.<br />
 <code>-xpm</code> : executes with the parallel mapper option.<br />
 <code>-xpr</code> : executes with the parallel reducer option.<br />
 <code>-xpf</code> : executes with the parallel flusher option.<br />
 <code>-xnc</code> : executes with the no compression option.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kcpolymgr/">kcpolymgr</a></code>(1), <code><a href="/docs/linux/man/1-kclangctest/">kclangctest</a></code>(1) </p>
<h2>Index</h2>
