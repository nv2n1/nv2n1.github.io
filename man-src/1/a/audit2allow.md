---
title: "audit2allow(1)"
name: "audit2allow"
section: "1"
letter: "a"
url: "/docs/linux/man/1-audit2allow/"
description: "audit2allow – generate SELinux policy allow/dontaudit rules from logs of denied operations"
---

<h2>NAME</h2>
<p> <code>audit2allow</code> &#8211; generate SELinux policy allow/dontaudit rules from logs of denied operations </p>
<p> <code>audit2why</code> &#8211; translates SELinux audit messages into a description of why the access was denied (audit2allow -w) </p>
<h2>SYNOPSIS</h2>
<p> <code>audit2allow</code> [<i>options</i>]</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a | &#8211;all</code></p>
<dd> Read input from audit and message log, conflicts with -i</p>
<dt><code>-b | &#8211;boot</code></p>
<dd> Read input from audit messages since last boot conflicts with -i</p>
<dt><code>-d | &#8211;dmesg</code></p>
<dd> Read input from output of <i>/bin/dmesg.</i> Note that all audit messages are not available via dmesg when auditd is running; use &quot;ausearch -m avc | audit2allow&quot; or &quot;-a&quot; instead.</p>
<dt><code>-D | &#8211;dontaudit</code></p>
<dd> Generate dontaudit rules (Default: allow)</p>
<dt><code>-h | &#8211;help</code></p>
<dd> Print a short usage message</p>
<dt><code>-i &lt;inputfile&gt; | &#8211;input &lt;inputfile&gt;</code></p>
<dd> read input from <i>&lt;inputfile&gt;</i></p>
<dt><code>-l | &#8211;lastreload</code></p>
<dd> read input only after last policy reload</p>
<dt><code>-m &lt;modulename&gt; | &#8211;module &lt;modulename&gt;</code></p>
<dd> Generate module/require output &lt;modulename&gt;</p>
<dt><code>-M &lt;modulename&gt; </code></p>
<dd> Generate loadable module package, conflicts with -o</p>
<dt><code>-p &lt;policyfile&gt; | &#8211;policy &lt;policyfile&gt;</code></p>
<dd> Policy file to use for analysis</p>
<dt><code>-o &lt;outputfile&gt; | &#8211;output &lt;outputfile&gt;</code></p>
<dd> append output to <i>&lt;outputfile&gt;</i></p>
<dt><code>-r | &#8211;requires</code></p>
<dd> Generate require output syntax for loadable modules.</p>
<dt><code>-N | &#8211;noreference</code></p>
<dd> Do not generate reference policy, traditional style allow rules. This is the default behavior.</p>
<dt><code>-R | &#8211;reference</code></p>
<dd> Generate reference policy using installed macros. This attempts to match denials against interfaces and may be inaccurate.</p>
<dt><code>-w | &#8211;why</code></p>
<dd> Translates SELinux audit messages into a description of why the access was denied </p>
<dt><code>-v | &#8211;verbose</code></p>
<dd> Turn on verbose output </p>
</dl>
<h2>DESCRIPTION</h2>
<p> This utility scans the logs for messages logged when the system denied permission for operations, and generates a snippet of policy rules which, if loaded into policy, might have allowed those operations to succeed. However, this utility only generates Type Enforcement (TE) allow rules. Certain permission denials may require other kinds of policy changes, e.g. adding an attribute to a type declaration to satisfy an existing constraint, adding a role allow rule, or modifying a constraint. The <code><a href="/docs/linux/man/8-audit2why/">audit2why</a></code>(8) utility may be used to diagnose the reason when it is unclear. </p>
<p> Care must be exercised while acting on the output of this utility to ensure that the operations being permitted do not pose a security threat. Often it is better to define new domains and/or types, or make other structural changes to narrowly allow an optimal set of operations to succeed, as opposed to blindly implementing the sometimes broad changes recommended by this utility. Certain permission denials are not fatal to the application, in which case it may be preferable to simply suppress logging of the denial via a &#8216;dontaudit&#8217; rule rather than an &#8216;allow&#8217; rule. </p>
<h2>EXAMPLE</h2>
<pre><code>
NOTE: These examples are for systems using the audit package.  If you do 
not use the audit package,  the AVC messages will be in /var/log/messages.
Please substitute /var/log/messages for /var/log/audit/audit.log in the 
examples.
Using audit2allow to generate module policy
$ cat /var/log/audit/audit.log | audit2allow -m local &gt; local.te
$ cat local.te
module local 1.0;
require
{
    class file
    {
        getattr open read
    };
    type myapp_t;
    type etc_t;
};
allow myapp_t etc_t : file{getattr open read};
&lt;review local.te and customize as desired&gt;
Using audit2allow to generate module policy using reference policy
$ cat /var/log/audit/audit.log | audit2allow -R -m local &gt; local.te
$ cat local.te
policy_module(local, 1.0)
gen_require(`
        type myapp_t;
        type etc_t;
}
;
files_read_etc_files(myapp_t)&lt;review local.te and customize as desired&gt; Building module policy using Makefile
#SELinux provides a policy devel environment under
#/ usr / share / selinux / devel including all of the shipped
#interface files.
#You can create a te file and compile it by executing
        $ make
        - f / usr / share / selinux / devel / Makefile local.pp
#This make command will compile a local.te file in the current
#directory.If you did not specify a "pp" file, the make file
#will compile all "te" files in the current directory.After
#you compile your te file into a "pp" file, you need to install
#it using the semodule command.
                                              $ semodule
        - i local.pp Building module policy manually
#Compile the module
          $ checkmodule
        - M - m - o local.mod local.te
#Create the package
                  $ semodule_package
        - o local.pp - m local.mod
#Load the module into the kernel
                       $ semodule
        - i local.pp Using audit2allow to generate and build module policy $ cat / var / log / audit / audit.log
    | audit2allow - M local Generating type enforcement file : local.te Compiling policy : checkmodule - M - m - o local.mod local.te Building package : semodule_package - o local.pp - m local.mod ********************IMPORTANT ***********************In order to load this newly created policy package into the kernel,
    you are required to execute
            semodule
            - i local.pp
                  Using audit2allow to generate monolithic(non - module) policy
                  $ cd
                  / etc / selinux / $SELINUXTYPE / src / policy $ cat / var / log / audit / audit.log
        | audit2allow &gt;&gt; domains / misc / local.te $ cat domains / misc / local.te allow cupsd_config_t unconfined_t : fifo_file{getattr ioctl};
&lt;review domains / misc / local.te and customize as desired&gt; $ make load
</code></pre>
<h2>AUTHOR</h2>
<p> This manual page was written by <i>Manoj Srivastava &lt;srivasta [at] debian.org&gt;,</i> for the Debian GNU/Linux system. It was updated by Dan Walsh &lt;dwalsh [at] redhat.com&gt; </p>
<p> The <code>audit2allow</code> utility has contributions from several people, including <i>Justin R. Smith </i> and <i>Yuichi Nakamura.</i> and <i>Dan Walsh</i> </p>
<h2>Index</h2>
