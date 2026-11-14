---
title: "nova(1)"
name: "nova"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nova/"
---

<h2>NAME</h2>

 nova - OpenStack Nova command line client

<h2>SYNOPSIS</h2>

 <i>nova</i> [options] &lt;command&gt; [command-options] 

 <i>nova help</i> 

 <i>nova help</i> &lt;command&gt;

<h2>DESCRIPTION</h2>

 

 <i>nova</i> is a command line client for controlling OpenStack Nova, the cloud computing fabric controller. It implements 100% of the Nova API, allowing management of instances, images, quotas and much more. 

 Before you can issue commands with <i>nova</i>, you must ensure that your environment contains the necessary variables so that you can prove to the CLI who you are and what credentials you have to issue the commands. See <i>Getting Credentials for a CLI</i> section of <i>OpenStack CLI Guide</i> for more info. 

 See <i>OpenStack Nova CLI Guide</i> for a full-fledged guide.

<h2>OPTIONS</h2>

 

 To get a list of available commands and options run: 

 <pre>
nova help
</pre> 

 To get usage and options of a command run: 

 <pre>
nova help &lt;command&gt;
</pre>

<h2>EXAMPLES</h2>

 

 Get information about boot command: 

 <pre>
nova help boot
</pre> 

 List available images: 

 <pre>
nova image-list
</pre> 

 List available flavors: 

 <pre>
nova flavor-list
</pre> 

 Launch an instance: 

 <pre>
nova boot myserver --image some-image --flavor 2
</pre> 

 View instance information: 

 <pre>
nova show myserver
</pre> 

 List instances: 

 <pre>
nova list
</pre> 

 Terminate an instance: 

 <pre>
nova delete myserver
</pre>

<h2>SEE ALSO</h2>

 

 OpenStack Nova CLI Guide: <i><a rel="nofollow" HREF="http://docs.openstack.org/cli-reference/content/novaclient_commands.html">http://docs.openstack.org/cli-reference/content/novaclient_commands.html</a></i>

<h2>BUGS</h2>

 

 Nova client is hosted in Launchpad so you can view current bugs at <i><a rel="nofollow" HREF="https://bugs.launchpad.net/python-novaclient/">https://bugs.launchpad.net/python-novaclient/</a></i>.

<h2>AUTHOR</h2>

 OpenStack Contributors

<h2>COPYRIGHT</h2>

 OpenStack Contributors 

<h2>Index</h2>


