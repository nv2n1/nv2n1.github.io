---
title: "kchashtest(1)"
name: "kchashtest"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kchashtest/"
description: "kchashtest – command line interface to test the file hash database"
---

<h2 class="name">NAME</h2>
<p> kchashtest &#8211; command line interface to test the file hash database</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>kchashtest</code>&#8216; is a utility for facility test and performance test of the file hash database. This command is used in the following format. `<i>path</i>&#8216; specifies the path of a database file. `<i>rnum</i>&#8216; specifies the number of iterations. </p>
<dl>
<dt>
<dd>
 <code>kchashtest order </code>[<code>-th </code><i>num</i>][<code>-rnd</code>][<code>-set</code>|<code>-get</code>|<code>-getw</code>|<code>-rem</code>|<code>-etc</code>][<code>-tran</code>][<code>-oat</code>|<code>-onl</code>|<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-apow </code><i>num</i>][<code>-fpow </code><i>num</i>][<code>-ts</code>][<code>-tl</code>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-msiz </code><i>num</i>][<code>-dfunit </code><i>num</i>][<code>-lv</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs in-order tests.</dl>
<p> <code>kchashtest queue </code>[<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-rnd</code>][<code>-oat</code>|<code>-onl</code>|<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-apow </code><i>num</i>][<code>-fpow </code><i>num</i>][<code>-ts</code>][<code>-tl</code>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-msiz </code><i>num</i>][<code>-dfunit </code><i>num</i>][<code>-lv</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs queuing operations.</dl>
<p> <code>kchashtest wicked </code>[<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-oat</code>|<code>-onl</code>|<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-apow </code><i>num</i>][<code>-fpow </code><i>num</i>][<code>-ts</code>][<code>-tl</code>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-msiz </code><i>num</i>][<code>-dfunit </code><i>num</i>][<code>-lv</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs mixed operations selected at random.</dl>
<p> <code>kchashtest tran </code>[<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-hard</code>][<code>-oat</code>|<code>-onl</code>|<code>-onl</code>|<code>-otl</code>|<code>-onr</code>][<code>-apow </code><i>num</i>][<code>-fpow </code><i>num</i>][<code>-ts</code>][<code>-tl</code>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-msiz </code><i>num</i>][<code>-dfunit </code><i>num</i>][<code>-lv</code>]<i>path</i><i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of transaction.</dl>
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
 <code>-apow </code><i>num</i> : specifies the power of the alignment of record size.<br />
 <code>-fpow </code><i>num</i> : specifies the power of the capacity of the free block pool.<br />
 <code>-ts</code> : tunes the database with the small option.<br />
 <code>-tl</code> : tunes the database with the linear option.<br />
 <code>-tc</code> : tunes the database with the compression option.<br />
 <code>-bnum </code><i>num</i> : specifies the number of buckets of the hash table.<br />
 <code>-msiz </code><i>num</i> : specifies the size of the memory-mapped region.<br />
 <code>-dfunit </code><i>num</i> : specifies the unit step number of auto defragmentation.<br />
 <code>-lv</code> : reports all errors.<br />
 <code>-it </code><i>num</i> : specifies the number of repetition.<br />
 <code>-hard</code> : performs physical synchronization.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kchashmgr/">kchashmgr</a></code>(1) </p>
<h2>Index</h2>
