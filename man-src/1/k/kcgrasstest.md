---
title: "kcgrasstest(1)"
name: "kcgrasstest"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kcgrasstest/"
description: "kcgrasstest – command line interface to test the cache tree database"
---

<h2 class="name">NAME</h2>
<p> kcgrasstest &#8211; command line interface to test the cache tree database</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>kcgrasstest</code>&#8216; is a utility for facility test and performance test of the cache tree database. This command is used in the following format. `<i>rnum</i>&#8216; specifies the number of iterations. </p>
<dl>
<dt>
<dd>
 <code>kcgrasstest order </code>[<code>-th </code><i>num</i>][<code>-rnd</code>][<code>-etc</code>][<code>-tran</code>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-psiz </code><i>num</i>][<code>-pccap </code><i>num</i>][<code>-rcd</code>|<code>-rcld</code>|<code>-rcdd</code>][<code>-lv</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs in-order tests.</dl>
<p> <code>kcgrasstest queue </code>[<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-rnd</code>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-psiz </code><i>num</i>][<code>-pccap </code><i>num</i>][<code>-rcd</code>|<code>-rcld</code>|<code>-rcdd</code>][<code>-lv</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs queuing operations.</dl>
<p> <code>kcgrasstest wicked </code>[<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-psiz </code><i>num</i>][<code>-pccap </code><i>num</i>][<code>-rcd</code>|<code>-rcld</code>|<code>-rcdd</code>][<code>-lv</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs mixed operations selected at random.</dl>
<p> <code>kcgrasstest tran </code>[<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-tc</code>][<code>-bnum </code><i>num</i>][<code>-psiz </code><i>num</i>][<code>-pccap </code><i>num</i>][<code>-rcd</code>|<code>-rcld</code>|<code>-rcdd</code>][<code>-lv</code>]<i>rnum</i></p>
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
 <code>-psiz </code><i>num</i> : specifies the size of each page.<br />
 <code>-pccap </code><i>num</i> : specifies the capacity size of the page cache.<br />
 <code>-rcd</code> : use the decimal comparator instead of the lexical one.<br />
 <code>-rcld</code> : use the lexical descending comparator instead of the ascending one.<br />
 <code>-rcdd</code> : use the decimal descending comparator instead of the lexical one.<br />
 <code>-lv</code> : reports all errors.<br />
 <code>-it </code><i>num</i> : specifies the number of repetition.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>Index</h2>
