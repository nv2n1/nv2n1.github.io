---
title: "fts-set-blacklist(1)"
name: "fts-set-blacklist"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fts-set-blacklist/"
---

<h2>NAME</h2>

 fts-set-blacklist

<h2>SYNOPSIS</h2>

 fts-set-blacklist [options] TYPE SUBJECT MODE

<h2>DESCRIPTION</h2>

 fts-set-blacklist is a tool for blacklisting SEs and DNs. Accepted values for TYPE are: 'se', and 'dn', subject is either the DN or SE name, MODE is either 'on' (blacklisted) or 'off' (unblacklisted)

<h2>OPTIONS</h2>

 
&nbsp;<wbr>&nbsp;<wbr>-h&nbsp;<wbr>[&nbsp;<wbr>--help&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print this help text and exit. 
&nbsp;<wbr>&nbsp;<wbr>-q&nbsp;<wbr>[&nbsp;<wbr>--quite&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Quiet operation. 
&nbsp;<wbr>&nbsp;<wbr>-v&nbsp;<wbr>[&nbsp;<wbr>--verbose&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Be more verbose. 
&nbsp;<wbr>&nbsp;<wbr>-s&nbsp;<wbr>[&nbsp;<wbr>--service&nbsp;<wbr>]&nbsp;<wbr>arg&nbsp;<wbr>&nbsp;<wbr>Use the transfer service at the specified URL. 
&nbsp;<wbr>&nbsp;<wbr>-V&nbsp;<wbr>[&nbsp;<wbr>--version&nbsp;<wbr>]&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print the version number and exit.

<h2>EXAMPLE</h2>

 
&nbsp;<wbr>&nbsp;<wbr>- To blacklist a SE: 
&nbsp;<wbr>fts-set-blacklist -s&nbsp;<wbr>$FTSENDPOINT se&nbsp;<wbr>$SE on 
&nbsp;<wbr>&nbsp;<wbr>- To blacklist a SE for given VO: 
&nbsp;<wbr>fts-set-blacklist -s&nbsp;<wbr>$FTSENDPOINT se&nbsp;<wbr>$SE on --vo&nbsp;<wbr>$VO 
&nbsp;<wbr>&nbsp;<wbr>- To blacklist a SE but still accept transfer-jobs: 
&nbsp;<wbr>fts-set-blacklist -s&nbsp;<wbr>$FTSENDPOINT se&nbsp;<wbr>$SE on --allow-submit 
&nbsp;<wbr>&nbsp;<wbr>- To remove a SE from blacklist: 
&nbsp;<wbr>fts-set-blacklist -s&nbsp;<wbr>$FTSENDPOINT se&nbsp;<wbr>$SE off 
&nbsp;<wbr>&nbsp;<wbr>- To blacklist a DN: 
&nbsp;<wbr>fts-set-blacklist -s&nbsp;<wbr>$FTSENDPOINT dn&nbsp;<wbr>$DN on 
&nbsp;<wbr>&nbsp;<wbr>- To remove a DN from blacklist: 
&nbsp;<wbr>fts-set-blacklist -s&nbsp;<wbr>$FTSENDPOINT dn&nbsp;<wbr>$DN off

<h2>SEE ALSO</h2>

 <a rel="nofollow" HREF="http://fts3-service.web.cern.ch/">http://fts3-service.web.cern.ch/</a> 

<h2>Index</h2>


