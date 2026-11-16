---
title: "ofxconnect(1)"
name: "ofxconnect"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ofxconnect/"
description: "ofxconnect – Create a statement request file"
---

<h2>NAME</h2>
<p> ofxconnect &#8211; Create a statement request file</p>
<h2>SYNOPSIS</h2>
<p> <code>ofxconnect</code> [<i>OPTIONS</i>]&#8230; [<i>FILES</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> ofxconnect 0.9.9 </p>
<p> prints to stdout the created OFX file based on the options you pass it. currently it will only create a statement request file. you can POST this to an OFX server to request a statement from that financial institution for that account.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print version and exit</dd>
<dt><code>&#8211;fipid</code>=<i>STRING</i></dt>
<dd> FI partner identifier (looks up fid, org &amp; url from partner server)</dd>
<dt><code>&#8211;fid</code>=<i>STRING</i></dt>
<dd> FI identifier</dd>
<dt><code>&#8211;org</code>=<i>STRING</i></dt>
<dd> FI org tag</dd>
<dt><code>&#8211;bank</code>=<i>STRING</i></dt>
<dd> IBAN bank identifier</dd>
<dt><code>&#8211;broker</code>=<i>STRING</i></dt>
<dd> Broker identifier</dd>
<dt><code>&#8211;user</code>=<i>STRING</i></dt>
<dd> User name</dd>
<dt><code>&#8211;pass</code>=<i>STRING</i></dt>
<dd> Password</dd>
<dt><code>&#8211;acct</code>=<i>STRING</i></dt>
<dd> Account ID</dd>
<dt><code>&#8211;type</code>=<i>INT</i></dt>
<dd> Account Type 1=checking 2=invest 3=ccard</dd>
<dt><code>&#8211;past</code>=<i>LONG</i></dt>
<dd> How far back to look from today (in days)</dd>
<dt><code>&#8211;url</code>=<i>STRING</i></dt>
<dd> Url to POST the data to (otherwise goes to stdout)</dd>
<dt><code>&#8211;trid</code>=<i>INT</i></dt>
<dd> Transaction id</dd>
<dt>
</dt><dd> Group: command</dd>
<dt><code>-s</code>, <code>&#8211;statement-req</code></dt>
<dd> Request for a statement</dd>
<dt><code>-a</code>, <code>&#8211;accountinfo-req</code></dt>
<dd> Request for a list of accounts</dd>
<dt><code>-p</code>, <code>&#8211;payment-req</code></dt>
<dd> Request to make a payment</dd>
<dt><code>-i</code>, <code>&#8211;paymentinquiry-req</code></dt>
<dd> Request to inquire about the status of a payment</dd>
<dt><code>-b</code>, <code>&#8211;bank-list</code></dt>
<dd> List all known banks</dd>
<dt><code>-f</code>, <code>&#8211;bank-fipid</code></dt>
<dd> List all fipids for a given bank</dd>
<dt><code>-v</code>, <code>&#8211;bank-services</code></dt>
<dd> List supported services for a given fipid</dd>
<dt><code>&#8211;allsupport</code></dt>
<dd> List all banks which support online banking </dd>
</dl>
<h2>Index</h2>
