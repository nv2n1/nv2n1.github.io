---
title: "oscap-chroot(8)"
name: "oscap-chroot"
section: "8"
letter: "o"
url: "/docs/linux/man/8-oscap-chroot/"
---

oscap-chroot - Tool for offline SCAP evaluation of filesystems mounted at arbitrary paths.

<h2>Description</h2>

oscap-chroot runs oscap tool on it in a filesystem mounted at given path. Usage of the tool mimics usage and options of <a HREF="/docs/linux/man/8-oscap/">oscap</a>(8) tool. 

<h2>Usage</h2>

<h3>Evaluation of XCCDF content</h3>

$ oscap-chroot CHROOT_PATH xccdf eval [options] INPUT_CONTENT 

 supported oscap xccdf eval options are: 
&nbsp;<wbr>&nbsp;<wbr>--profile 
&nbsp;<wbr>&nbsp;<wbr>--tailoring-file 
&nbsp;<wbr>&nbsp;<wbr>--tailoring-id 
&nbsp;<wbr>&nbsp;<wbr>--cpe&nbsp;<wbr>(external OVAL dependencies are not supported yet!) 
&nbsp;<wbr>&nbsp;<wbr>--oval-results 
&nbsp;<wbr>&nbsp;<wbr>--sce-results 
&nbsp;<wbr>&nbsp;<wbr>--check-engine-results 
&nbsp;<wbr>&nbsp;<wbr>--results 
&nbsp;<wbr>&nbsp;<wbr>--results-arf 
&nbsp;<wbr>&nbsp;<wbr>--report 
&nbsp;<wbr>&nbsp;<wbr>--skip-valid 
&nbsp;<wbr>&nbsp;<wbr>--fetch-remote-resources 
&nbsp;<wbr>&nbsp;<wbr>--progress 
&nbsp;<wbr>&nbsp;<wbr>--datastream-id 
&nbsp;<wbr>&nbsp;<wbr>--xccdf-id 
&nbsp;<wbr>&nbsp;<wbr>--benchmark-id

<h3>Evaluation of OVAL content</h3>

$ oscap-chroot image CHROOT_PATH oval eval [options] INPUT_CONTENT 

 supported oscap oval eval options are: 
&nbsp;<wbr>&nbsp;<wbr>--id 
&nbsp;<wbr>&nbsp;<wbr>--variables 
&nbsp;<wbr>&nbsp;<wbr>--directives 
&nbsp;<wbr>&nbsp;<wbr>--results 
&nbsp;<wbr>&nbsp;<wbr>--report 
&nbsp;<wbr>&nbsp;<wbr>--skip-valid 
&nbsp;<wbr>&nbsp;<wbr>--datastream-id 
&nbsp;<wbr>&nbsp;<wbr>--oval-id 
&nbsp;<wbr>&nbsp;<wbr>--probe-root

<h3>Collection of OVAL System Characteristic</h3>

$ oscap-chroot CHROOT_PATH oval collect [options] INPUT_CONTENT 

 supported oscap oval collect options are: 
&nbsp;<wbr>&nbsp;<wbr>--id 
&nbsp;<wbr>&nbsp;<wbr>--syschar 
&nbsp;<wbr>&nbsp;<wbr>--variables 
&nbsp;<wbr>&nbsp;<wbr>--skip-valid

<h2>Reporting Bugs</h2>

<pre>Please report bugs using <a rel="nofollow" HREF="https://github.com/OpenSCAP/openscap/issues">https://github.com/OpenSCAP/openscap/issues</a></pre>

<h2>Authors</h2>

<pre>Martin Preisler &lt;mpreisle [at] redhat.com&gt;</pre>
