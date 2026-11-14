---
title: "opafmconfigdiff(8)"
name: "opafmconfigdiff"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opafmconfigdiff/"
---

opafmconfigdiff 

 

 

 Performs a file difference between two configuration files corresponding to two FM instances described by <i>file1</i> and <i>file2</i>.

<h2>Syntax</h2>

opafmconfigdiff [-f] [-l] [-d '<i>diff_args</i>'] <i>file1 file2</i>

<h2>Options</h2>

<dl><dt>--help
<dd>Produces full help text. 

<dt>-f
<dd>Filters out FM parameters that are not part of the consistency check. Removes config tags that do not cause consistency checks on the FM to fail from diff. 

<dt>-l
<dd>Includes comments in XML to indicate original line numbers. 

<dt>-d '<i>diff_args</i>'
<dd>Specifies additional arguments to add to diff command. For example, enter uw for unified format ignoring whitespace. 

<dt>
&nbsp;<wbr><i>file1 file2</i>&nbsp;<wbr>
<dd>Names of the configuration files to be compared. 

</dl>

<h2>Example</h2>

opafmconfigdiff /etc/sysconfig/opafm.xml /usr/lib/opa-fm/etc/opafm.xml 
 opafmconfigdiff -f /etc/sysconfig/opafm.xml /usr/lib/opa-fm/etc/opafm.xml 
 opafmconfigdiff #8217#8211;d -uw /etc/sysconfig/opafm.xml /usr/lib/opa-fm/etc/ opafm.xml 
