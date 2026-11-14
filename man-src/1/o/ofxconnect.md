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
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Print version and exit</p>
<dt><code>&#8211;fipid</code>=<i>STRING</i></p>
<dd> FI partner identifier (looks up fid, org &amp; url from partner server)</p>
<dt><code>&#8211;fid</code>=<i>STRING</i></p>
<dd> FI identifier</p>
<dt><code>&#8211;org</code>=<i>STRING</i></p>
<dd> FI org tag</p>
<dt><code>&#8211;bank</code>=<i>STRING</i></p>
<dd> IBAN bank identifier</p>
<dt><code>&#8211;broker</code>=<i>STRING</i></p>
<dd> Broker identifier</p>
<dt><code>&#8211;user</code>=<i>STRING</i></p>
<dd> User name</p>
<dt><code>&#8211;pass</code>=<i>STRING</i></p>
<dd> Password</p>
<dt><code>&#8211;acct</code>=<i>STRING</i></p>
<dd> Account ID</p>
<dt><code>&#8211;type</code>=<i>INT</i></p>
<dd> Account Type 1=checking 2=invest 3=ccard</p>
<dt><code>&#8211;past</code>=<i>LONG</i></p>
<dd> How far back to look from today (in days)</p>
<dt><code>&#8211;url</code>=<i>STRING</i></p>
<dd> Url to POST the data to (otherwise goes to stdout)</p>
<dt><code>&#8211;trid</code>=<i>INT</i></p>
<dd> Transaction id</p>
<dt>
<dd> Group: command</p>
<dt><code>-s</code>, <code>&#8211;statement-req</code></p>
<dd> Request for a statement</p>
<dt><code>-a</code>, <code>&#8211;accountinfo-req</code></p>
<dd> Request for a list of accounts</p>
<dt><code>-p</code>, <code>&#8211;payment-req</code></p>
<dd> Request to make a payment</p>
<dt><code>-i</code>, <code>&#8211;paymentinquiry-req</code></p>
<dd> Request to inquire about the status of a payment</p>
<dt><code>-b</code>, <code>&#8211;bank-list</code></p>
<dd> List all known banks</p>
<dt><code>-f</code>, <code>&#8211;bank-fipid</code></p>
<dd> List all fipids for a given bank</p>
<dt><code>-v</code>, <code>&#8211;bank-services</code></p>
<dd> List supported services for a given fipid</p>
<dt><code>&#8211;allsupport</code></p>
<dd> List all banks which support online banking </p>
</dl>
<h2>Index</h2>
