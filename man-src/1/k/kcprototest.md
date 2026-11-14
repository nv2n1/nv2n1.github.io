---
title: "kcprototest(1)"
name: "kcprototest"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kcprototest/"
description: "kcprototest – command line interface to test the prototype database"
---

<h2 class="name">NAME</h2>
<p> kcprototest &#8211; command line interface to test the prototype database</p>
<h2>DESCRIPTION</h2>
<p> The command `<code>kcprototest</code>&#8216; is a utility for facility test and performance test of the prototype database. This command is used in the following format. `<i>rnum</i>&#8216; specifies the number of iterations. </p>
<dl>
<dt>
<dd>
 <code>kcprototest order </code>[<code>-tree</code>][<code>-th </code><i>num</i>][<code>-rnd</code>][<code>-etc</code>][<code>-tran</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs in-order tests.</dl>
<p> <code>kcprototest queue </code>[<code>-tree</code>][<code>-th </code><i>num</i>][<code>-it </code><i>num</i>][<code>-rnd</code>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs queuing operations.</dl>
<p> <code>kcprototest wicked </code>[<code>-tree</code>][<code>-th </code><i>num</i>][<code>-it </code><i>num</i>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs mixed operations selected at random.</dl>
<p> <code>kcprototest tran </code>[<code>-tree</code>][<code>-th </code><i>num</i>][<code>-it </code><i>num</i>]<i>rnum</i></p>
<dl>
<dt>
<dd> Performs test of transaction.</dl>
</dl>
<p> Options feature the following. </p>
<dl>
<dt>
<dd> <code>-tree</code> : test the prototype tree database instead of the prototype hash database.<br />
 <code>-th </code><i>num</i> : specifies the number of worker threads.<br />
 <code>-rnd</code> : performs random test.<br />
 <code>-etc</code> : performs miscellaneous operations.<br />
 <code>-tran</code> : performs transaction.<br />
 <code>-it </code><i>num</i> : specifies the number of repetition.
</dl>
<p> This command returns 0 on success, another on failure. </p>
<h2>Index</h2>
