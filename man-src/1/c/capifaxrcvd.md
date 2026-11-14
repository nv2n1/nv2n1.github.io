---
title: "capifaxrcvd(1)"
name: "capifaxrcvd"
section: "1"
letter: "c"
url: "/docs/linux/man/1-capifaxrcvd/"
---

<h2>NAME</h2>

 capifaxrcvd — a FAX receive daemon for CAPI

<h2>SYNOPSIS</h2>

 capifaxrcvd [-i stationID] [-h header] [-l listenNumber] [-n notifyCmd] rcvDirectory

<h2>DESCRIPTION</h2>

 capifaxrcvd is a daemon to receive faxes via CAPI; you need a CAPI capable ISDN card with the appropriate drivers. 

 The final argument must be the directory in which the received faxes are to be placed. The filenames of the received faxes are of the form: f[fn]xxxtttttttt [fn] indicates the resolution (fine or normal), xxx indicated the number of pages, tttttttt is the (hexadecimal) timestamp of the fax (seconds since the Unix epoch, 00:00 on January 1st, 1970 UTC). 

 The daemon will fork itself into the background. 

 This stuff is based heavily on AVM's CAPI-adk for linux.

<h2>OPTIONS</h2>

<dl>
<dt>-i station_ID
<dd> 
&nbsp;<wbr>the station ID. Typically the company name or similar.
<dt>-h headline
<dd> 
&nbsp;<wbr>title of sent document.&nbsp;<wbr>(?)
<dt>-l listenNumber
<dd> 
&nbsp;<wbr>the phone number on which to receive faxes, i.e. the number to listen on.
<dt>-n notifyCmd
<dd> 
&nbsp;<wbr>command to execute when a fax has been received. It will be called with one argument, namely the filename of the received fax&nbsp;<wbr>(without the directory name).</dl>

<h2>AUTHOR</h2>

 manpage written from C source by Paul Slootman &lt;paul [at] debian.org&gt;. 

<h2>Index</h2>


