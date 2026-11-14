---
title: "oscap-vm(8)"
name: "oscap-vm"
section: "8"
letter: "o"
url: "/docs/linux/man/8-oscap-vm/"
---

oscap-vm - Tool for offline SCAP evaluation of virtual machines.

<h2>Description</h2>

oscap-vm mounts given virtual machine and runs oscap tool on it. The tool requires bash, guestmount, mktemp and umount to perform OVAL and XCCDF evaluation of virtual machines. Usage of the tool mimics usage and options of <a HREF="/docs/linux/man/8-oscap/">oscap</a>(8) tool. 

<h2>Usage</h2>

<h3>Evaluation of XCCDF content</h3>

$ oscap-vm image VM_STORAGE_IMAGE xccdf eval [options] INPUT_CONTENT 

 $ oscap-vm domain VM_DOMAIN xccdf eval [options] INPUT_CONTENT 

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

$ oscap-vm image VM_STORAGE_IMAGE oval eval [options] INPUT_CONTENT 

 $ oscap-vm domain VM_DOMAIN oval eval [options] INPUT_CONTENT 

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

$ oscap-vm image VM_STORAGE_IMAGE oval collect [options] INPUT_CONTENT 

 $ oscap-vm domain VM_DOMAIN oval collect [options] INPUT_CONTENT 

 supported oscap oval collect options are: 
&nbsp;<wbr>&nbsp;<wbr>--id 
&nbsp;<wbr>&nbsp;<wbr>--syschar 
&nbsp;<wbr>&nbsp;<wbr>--variables 
&nbsp;<wbr>&nbsp;<wbr>--skip-valid

<h2>Reporting Bugs</h2>

<pre>Please report bugs using <a rel="nofollow" HREF="https://github.com/OpenSCAP/openscap/issues">https://github.com/OpenSCAP/openscap/issues</a></pre>

<h2>Authors</h2>

<pre>Martin Preisler &lt;mpreisle [at] redhat.com&gt;</pre>
