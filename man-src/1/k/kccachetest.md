---
title: "kccachetest(1)"
name: "kccachetest"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kccachetest/"
description: "kccachetest – command line interface to test the cache hash database"
---

<h2 class="name">NAME</h2>
<p> kccachetest &#8211; command line interface to test the cache hash database</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>kccachetest</code>&#8216; is a utility for facility test and performance test of the cache hash database. This command is used in the following format. `<i>rnum</i>&#8216; specifies the number of iterations. </p>
<dl>
<dt>
<dd>
 <code>kccachetest order </code>[<code>-th </code><i>num</i>][<code>-rnd</code>][<code>-etc</code>][<code>-tran</code>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-capcnt </code><i>num</i>][<code>-capsiz </code><i>num</i>][<code>-lv</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs in-order tests.</dl>
<p> <code>kccachetest queue </code>[<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-rnd</code>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-capcnt </code><i>num</i>][<code>-capsiz </code><i>num</i>][<code>-lv</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs queuing operations.</dl>
<p> <code>kccachetest wicked </code>[<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-capcnt </code><i>num</i>][<code>-capsiz </code><i>num</i>][<code>-lv</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs mixed operations selected at random.</dl>
<p> <code>kccachetest tran </code>[<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-capcnt </code><i>num</i>][<code>-capsiz </code><i>num</i>][<code>-lv</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of transaction.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-th </code><i>num</i> : specifies the number of worker threads.<br />
 <code>-rnd</code> : performs random test.<br />
 <code>-etc</code> : performs miscellaneous operations.<br />
 <code>-tran</code> : performs transaction.<br />
 <code>-tc</code> : tunes the database with the compression option.<br />
 <code>-bnum </code><i>num</i> : specifies the number of buckets of the hash table.<br />
 <code>-capcnt </code><i>num</i> : specifies the maximum number of records.<br />
 <code>-capsiz </code><i>num</i> : specifies the maximum size of memory usage.<br />
 <code>-lv</code> : reports all errors.<br />
 <code>-it </code><i>num</i> : specifies the number of repetition.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>Index</h2>
