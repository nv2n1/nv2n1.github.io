---
title: "cobbler-register(1)"
name: "cobbler-register"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cobbler-register/"
---

<h2 class="name">NAME</h2>
 

 cobbler-register - create a cobbler system record 

<h2>SYNOPSIS</h2>

 cobbler-register [--server=&lt;cobbler.example.org&gt;] --profile=&lt;cobbler-profile-name&gt; [--fqdn=&lt;hostname&gt;]

<h2>DESCRIPTION</h2>

 Running cobbler-register on a system will create a cobbler system record for that system on a remote cobbler server. No changes will be made on the system itself.

<h2>DETAILS</h2>

 When installing new machines into a cobbler managed datacenter/lab, it helps to not have to manually enter in the network information for those systems. Using cobbler register either from a kickstart or a live environment (or even <font SIZE="-1">SSH</font>) can help seed the cobbler database. 

 Network information is discovered automatically for all physical interfaces. cobbler-register will attempt to discover the hostname, though if 'localhost.localdomain' is found, it will have to use some other data for the cobbler system record. This is probably not what you want, so specify --fqdn in this instance to override that registration value. 

 For this to work, the ``register_new_installs'' setting must be enabled on the remote cobbler server. 

 When the remote system record is created, for safety reasons, it will be set in Cobbler to be ``netboot disabled''. Use ``cobbler system edit --name=foo --netboot-enabled=1'' to set the machine to reinstall, where ``foo'' is the name of the new system record.

<h2>ENVIRONMENT VARIABLES</h2>

 cobbler-register respects the <font SIZE="-1">COBBLER_SERVER</font> variable to specify the cobbler server to use. This is a convenient way to avoid using the --server option. This variable is set automatically on systems installed via cobbler, assuming standard kickstart templates are used. If you need to change this on an installed system, edit /etc/profile.d/cobbler.{csh,sh}.

<h2>ADDITIONAL</h2>

 Reading the cobbler manpage, the koan manpage, and cobbler.github.io is highly recommended. 

 The mailing list is cobbler [at] lists.fedorahosted.org. 

 Subscribe at <a rel="nofollow" HREF="https://fedorahosted.org/mailman/listinfo/cobbler">https://fedorahosted.org/mailman/listinfo/cobbler</a>

<h2>AUTHOR</h2>

 Michael DeHaan &lt;michael.dehaan <font SIZE="-1">AT</font> gmail&gt; 

<h2>Index</h2>


