---
title: "capifax(1)"
name: "capifax"
section: "1"
letter: "c"
url: "/docs/linux/man/1-capifax/"
---

<h2>NAME</h2>

 capifax - a FAX send application for CAPI

<h2>SYNOPSIS</h2>

 capifax [-v] [-i stationID] [-h header] [-c callerNumber] phone file

<h2>DESCRIPTION</h2>

 

 capifax is an application to send faxes via CAPI; you need a CAPI capable ISDN card with the appropriate drivers. The final argument must be the phone number of the receiving fax machine. This stuff is based heavily on AVM’s CAPI-adk for linux.

<h2>OPTIONS</h2>

<dl>
<dt>-v
<dd> Be verbose.
<dt>-c<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>callerNumber
<dd> the phone number used as the sender.

<dt>-i station_ID
<dd> the sender’s station ID. Typically the company name or similar.
<dt>-h header
<dd> title of sent document.</dl>

<h2>AUTHOR</h2>

 This manual page was written by Paul Slootman &lt;paul [at] tdebian.org&gt;, Than Ngo &lt;than [at] redhat.com&gt; 

 

<h2>Index</h2>


