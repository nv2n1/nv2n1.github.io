---
title: "oscap-ssh(8)"
name: "oscap-ssh"
section: "8"
letter: "o"
url: "/docs/linux/man/8-oscap-ssh/"
---

oscap-ssh - Tool for running oscap over SSH and collecting results.

<h2>Description</h2>

oscap-ssh runs oscap tool on a remote system through SSH connection. The input files are transfered to the target system and after the scan finishes result files are transfered back. No temporary data remains on the remote machine. The tool requires bash, ssh, scp and mktemp to perform OVAL and XCCDF evaluation of remote machines. The remote machine also has to have oscap installed and in $PATH. This can be accomplished by installing openscap-scanner. Usage of the tool mimics usage and options of <a HREF="/docs/linux/man/8-oscap/">oscap</a>(8) tool. 

<h2>Usage</h2>

<h3>Evaluation of XCCDF content</h3>

$ oscap-ssh user [at] host 22 xccdf eval [options] INPUT_CONTENT 

 Only source datastreams are supported as INPUT_CONTENT! 

 Supported options are: 
&nbsp;<wbr>&nbsp;<wbr>--profile 
&nbsp;<wbr>&nbsp;<wbr>--tailoring-file 
&nbsp;<wbr>&nbsp;<wbr>--tailoring-id 
&nbsp;<wbr>&nbsp;<wbr>--cpe 
&nbsp;<wbr>&nbsp;<wbr>--results 
&nbsp;<wbr>&nbsp;<wbr>--results-arf 
&nbsp;<wbr>&nbsp;<wbr>--report 
&nbsp;<wbr>&nbsp;<wbr>--skip-valid 
&nbsp;<wbr>&nbsp;<wbr>--fetch-remote-resources 
&nbsp;<wbr>&nbsp;<wbr>--progress 
&nbsp;<wbr>&nbsp;<wbr>--datastream-id 
&nbsp;<wbr>&nbsp;<wbr>--xccdf-id 
&nbsp;<wbr>&nbsp;<wbr>--benchmark-id 
&nbsp;<wbr>&nbsp;<wbr>--remediate

<h3>Evaluation of OVAL content</h3>

$ oscap-ssh user [at] host 22 oval eval [options] INPUT_CONTENT 

 Supported options are: 
&nbsp;<wbr>&nbsp;<wbr>--id 
&nbsp;<wbr>&nbsp;<wbr>--variables 
&nbsp;<wbr>&nbsp;<wbr>--directives 
&nbsp;<wbr>&nbsp;<wbr>--results 
&nbsp;<wbr>&nbsp;<wbr>--report 
&nbsp;<wbr>&nbsp;<wbr>--skip-valid 
&nbsp;<wbr>&nbsp;<wbr>--datastream-id 
&nbsp;<wbr>&nbsp;<wbr>--oval-id 
&nbsp;<wbr>&nbsp;<wbr>--probe-root&nbsp;<wbr>(has to be remote path)

<h3>Collection of OVAL System Characteristic</h3>

$ oscap-ssh user [at] host 22 oval collect [options] INPUT_CONTENT 

 Supported options are: 
&nbsp;<wbr>&nbsp;<wbr>--id 
&nbsp;<wbr>&nbsp;<wbr>--syschar 
&nbsp;<wbr>&nbsp;<wbr>--variables 
&nbsp;<wbr>&nbsp;<wbr>--skip-valid 

 Specific option for oscap-ssh (must be first argument): 
&nbsp;<wbr>&nbsp;<wbr>--sudo

<h2>Exemplary Usage</h2>

<h3>Simple XCCDF evaluation</h3>

The following command evaluates a remote Fedora machine as root. HTML report is written out as report.html on the local machine. Can be executed from any machine that has ssh, scp and bash. The local machine does not need to have openscap installed. 

 $ oscap-ssh root [at] 192.168.1.13 22 xccdf eval --profile xccdf_org.ssgproject.content_profile_common --report report.html /usr/share/xml/scap/ssg/content/ssg-fedora-ds.xml

<h3>XCCDF Evaluation with tailoring file</h3>

The following command uses a tailoring file and also copies back ARF and XCCDF results. The tailoring file is automatically copied from local machine to remote. 

 $ oscap-ssh --sudo oscap-user [at] 192.168.1.13 22 xccdf eval --profile xccdf_org.ssgproject.content_profile_common --report report.html --results results.xml --results-arf arf.xml --tailoring-file ssg-fedora-ds-tailoring.xml /usr/share/xml/scap/ssg/content/ssg-fedora-ds.xml

<h3>Running remotely as root</h3>

Note that the openscap scanner is best run by the 'root' user as in the first example above. To do this, the &quot;PermitRootLogin&quot; directive must be enabled in /etc/ssh/sshd_config, which is itself a security violation. A safer approach is to enable a non-privileged user ('oscap-user' in the second example above) to run only the oscap binary as root (with the '--sudo' flag) by updating the remote machine's 'sudoers' file or adding a file like /etc/sudoers.d/99-oscap-user: 
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>allow oscap-user to run openscap scanner 
&nbsp;<wbr>&nbsp;<wbr>Defaults!/usr/bin/oscap&nbsp;<wbr>!requiretty 
&nbsp;<wbr>&nbsp;<wbr>oscap-user ALL=(root)&nbsp;<wbr>NOPASSWD:&nbsp;<wbr>/usr/bin/oscap

<h2>Reporting Bugs</h2>

<pre>Please report bugs using <a rel="nofollow" HREF="https://github.com/OpenSCAP/openscap/issues">https://github.com/OpenSCAP/openscap/issues</a></pre>

<h2>Authors</h2>

<pre>Martin Preisler &lt;mpreisle [at] redhat.com&gt;
Šimon Lukašík &lt;slukasik [at] redhat.com&gt;</pre>
