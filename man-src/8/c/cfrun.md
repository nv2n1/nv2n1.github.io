---
title: "cfrun(8)"
name: "cfrun"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfrun/"
description: "cfrun – Execute remote cfagents"
---

<p>cfrun &#8211; Execute remote cfagents</p>
<h2>Synopsis</h2>
<p>/usr/local/sbin/cfrun [options] </p>
<h2>Description</h2>
<p><code>cfengine</code> is a language based system specifically designed for testing and configuring unix-like systems attached to a TCP/IP network. cfrun is a tool for executing one or more remote agents; it contacts the cfservd daemon running on a remote host, which (in turn) starts an authorized agent. Cfrun cannot be used to send instructions to a remote agent, but it can be used to flag certain aspects to the agent&#8217;s existing policy for special attention.. The command line options for cfrun are slightly unusual. They are separated into three sections: options to the cfrun program, options to the remote cfagent (with some security restrictions) and finally classes or flags to the remote agent. </p>
<h2>Examples</h2>
<p>cfrun specialhost1 specialhost2 &#8212; &#8211;verbose &#8212; solaris In this example, we contact hosts specialhost1 specialhost2 by name, and ask them to execute cfagent with the &#8211;verbose flag, if the class solaris is not defined. cfrun specialhost1 &#8211;verbose &#8212; &#8212; solaris In this example the verbose flag is sent to cfrun rather than to the remote agent. No options are sent to the remote agents. The class specifier is sent to all the agents so that they may determine whether they fulfill the required class membership for execution. The default behaviour is to execute cfagent serially on all hosts listed in the cfrun.hosts file. </p>
<h2>Files</h2>
<p>cfrun read a configuration file cfrun.hosts which must contain a list of every potentially contactable host.</p>
<h2>Author</h2>
<p>Mark Burgess, Oslo University College</p>
<h2>Information</h2>
<p><a rel="nofollow" href="http://www.cfengine.org">http://www.cfengine.org</a></p>
