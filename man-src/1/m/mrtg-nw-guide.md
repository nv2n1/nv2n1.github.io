---
title: "mrtg-nw-guide(1)"
name: "mrtg-nw-guide"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-nw-guide/"
description: "mrtg-nw-guide – MRTG for NetWare"
---

<h2 class="name">NAME</h2>
<p> mrtg-nw-guide &#8211; MRTG for NetWare </p>
<h2>SYNOPSIS</h2>
<p> This guide is intended to aid in the installation and configuration of <font SIZE="-1">MRTG</font> on a NetWare server.</p>
<h2>OVERVIEW</h2>
<p> <font SIZE="-1">MRTG</font> is a relative newcomer to the NetWare platform. Earlier versions of NetWare could not run <font SIZE="-1">MRTG</font> natively for several reasons:</p>
<dl>
<dt>&bull;</p>
<dd> Absence of NetWare <font SIZE="-1">OS</font> support in the <font SIZE="-1">MRTG</font> package.</p>
<dt>&bull;</p>
<dd> A NetWare server commandline length limitation.</p>
<dt>&bull;</p>
<dd> Absence of the Rateup executable (Rateup.nlm).</p>
<dt>&bull;</p>
<dd> A standard installation method.</p>
<dt>&bull;</p>
<dd> Problems with NetWare&#8217;s implementation of Perl.</dl>
<p> Support for the NetWare <font SIZE="-1">OS</font> has now been fully added into <font SIZE="-1">MRTG</font>, beginning with <font SIZE="-1">MRTG</font> release 2.12.2. </p>
<p> Liberallly minded operating systems support a commandline length approaching 1000 characters. In such environments it was an easy matter to pass the sometimes high number of parameters used by <font SIZE="-1">MRTG</font>&#8216;s Rateup executable directly on the commandline. Until NetWare 6.5, NetWare had a commandline limit of 512 characters. This limitation was also removed for NetWare 6.0 by Service Pack 5. For other NetWare versions and earlier Service Packs, this limitation remains. To permit a &#8216;standard&#8217; interface for NetWare, the Rateup executable has been modified to also read its parameters from a file, and the <font SIZE="-1">MRTG</font> script has been modified to support this method on a NetWare platform. (See New Rateup Switch) </p>
<p> A Rateup <font SIZE="-1">NLM</font> is now available, along with the necessary scripts to build it if required. See the NetWare Support section of this document for further details. Additionally, mrtg.pl has been revised because of the unique (to NetWare) name of executables (<font SIZE="-1">NLM</font>). </p>
<p> The absence of a specific installation procedure has caused <font SIZE="-1">MRTG</font> to fail in the past because the Perl script could not find or load the Rateup executable. The installation method supplied here will solve this problem for now. </p>
<p> The <font SIZE="-1">MRTG</font>.pl script in the 2.12.2 (or later) version of <font SIZE="-1">MRTG</font> has been configured to suit all likely versions of NetWare able to use Perl5, and bypasses all of the known problems with NetWare Perl running <font SIZE="-1">MRTG</font>.</p>
<h2>PREREQUISITES</h2>
<p> You will need the following:</p>
<dl>
<dt>&bull;</p>
<dd> Perl 5.8.0 for NetWare with latest Perl Updates (February, 2005 or later; previous versions <font SIZE="-1">MAY</font> work)</p>
<dt>&bull;</p>
<dd> NetWare 5.1 w/ <font SIZE="-1">SP8</font>, NetWare 6.0 w/ <font SIZE="-1">SP5</font> or NetWare 6.5 w/ <font SIZE="-1">SP2</font>.</p>
<dt>&bull;</p>
<dd> A copy of the <font SIZE="-1">MRTG</font> Package (v2.12.2 at time of writting)</p>
<dt>&bull;</p>
<dd> Three .ncf files to execute the Perl scripts at the NetWare server console.</p>
<dt>&bull;</p>
<dd> A copy of the Rateup <font SIZE="-1">NLM</font> (Pre-built or compiled)</p>
<dt>&bull;</p>
<dd> Optionally, any NetWare supported Web Server (Netscape, Apache 1.3 or 2.0)</dl>
<p> For copies of the .ncf files and Rateup <font SIZE="-1">NLM</font>, see NetWare Support in this document.</p>
<h2>INSTALLING MRTG</h2>
<dl>
<dt>1.</p>
<dd> Install the latest Perl 5.8.x release on your server. See the Perl documentation for details.</p>
<dt>2.</p>
<dd> Create the following directories: </p>
<pre>
         SYS:/Mrtg
         SYS:/Mrtg/bin
         SYS:/Mrtg/contrib    (Optional for this document)
         SYS:/Mrtg/doc        (Optional for this document)
         SYS:/Mrtg/html
         SYS:/Mrtg/html/images
         SYS:/Mrtg/html/work
         SYS:/Mrtg/lib
         SYS:/Mrtg/logs
         SYS:/Mrtg/translate
</pre>
<dt>3.</p>
<dd> Copy from the <font SIZE="-1">MRTG</font> package the following files: </p>
<pre>
 in\*        to  SYS:/Mrtg/bin              All files. See Note 1.
</pre>
<p> Note 1: Add a .pl extension to the mrtg, cfgmaker and indexmaker files. The rateup.exe will <font SIZE="-1">NOT</font> be needed on the NetWare server. </p>
<pre>
 
