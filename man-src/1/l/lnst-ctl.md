---
title: "lnst-ctl(1)"
name: "lnst-ctl"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lnst-ctl/"
description: "lnst-ctl – Linux Network Stack Test controller"
---

<h2 class="name">NAME</h2>
<p> lnst-ctl &#8211; Linux Network Stack Test controller </p>
<h2>SYNOPSIS</h2>
<p> <code>lnst-ctl</code> [<i>OPTION</i>]&#8230; <i>ACTION</i> <i>RECIPE</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Linux Network Stack Test is a tool that supports development and execution of automated and portable network tests. For detailed description of the architecture of LNST please refer to project website (link listed on <code>INTERNET RESOURCES</code> bellow). </p>
<p> <code>lnst-ctl</code> is a script used for managing slaves. It reads a recipe XML file as an input and executes tests on the specified slave machines.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A, &#8211;override-alias name=value</code></p>
<dd> Define top-level alias that will override any other definitions in the recipe</p>
<dt><code>-a, &#8211;define-alias name=value</code></p>
<dd> Define top-level alias</p>
<dt><code>-c, &#8211;config</code><i>=file</i></p>
<dd> Load a custom configuration file in addition to <i>/etc/lnst-ctl.conf</i> and <i>~/lnst/lnst-ctl.conf</i> that are loaded by default.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Toggle emitting debugging messages.</p>
<dt><code>&#8211;dump-config</code></p>
<dd> Dumps the join of all loaded configuration files on stdout and exits</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display usage of this command.</p>
<dt><code>-m, &#8211;no-colours</code></p>
<dd> Disable coloured terminal output.</p>
<dt><code>-o, &#8211;disable-pool-checks</code></p>
<dd> Skip the pool machine availability checks.</p>
<dt><code>-p, &#8211;packet-capture</code></p>
<dd> Capture and log all ongoing network communication between the slaves during the test.</p>
<dt><code>&#8211;pools</code><i>=name[,&#8230;]</i></p>
<dd> Restricts which pools to use for matching, value is a comma separated list of values</p>
<dt><code>&#8211;pools=</code><i>path</i></p>
<dd> Restrict which pool to use for matching, value is single path to a pool directory</p>
<dt><code>-r, &#8211;reduce-sync</code></p>
<dd> Disable synchronization of module and tool resources to slave machines, when python tasks are used in the recipe. Instead the user can manually synchronize resources from the python task itself. This option has no effect if the recipe only contains xml tasks.</p>
<dt><code>-s, &#8211;xslt-url</code><i>=URL</i></p>
<dd> URL to a XSLT document that will be used when transforming the xml result file, only useful when -t is used as well</p>
<dt><code>-t, &#8211;html</code><i>=file</i></p>
<dd> Generate a formatted result html</p>
<dt><code>-u, &#8211;multi-match</code></p>
<dd> Run each recipe with every pool match possible</p>
<dt><code>-x, &#8211;result</code><i>=file</i></p>
<dd> Write results in XML format to the specified <i>file</i>.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Extends output of list_pools action</dl>
<p> <i>RECIPE</i> can be either a LNST recipe file or a directory containing recipe files. One or more files/directories can be passed at the same time. Each recipe is a XML file. The format is described in detail in the online documentation available at LNST wiki (link is listed on <code>INTERNET RESOURCES</code> bellow). </p>
<p> <i>ACTION</i> can be one of <code>run,</code> <code>config_only,</code> <code>deconfigure</code>, <code>match_setup, and</code> <code>list_pools.</code> </p>
<p> When it is set to <code>run,</code> all provided recipe files will be sequentially executed. The network will be configured accordingly to each recipe file and clean up afterwards. </p>
<p> In case of <code>config_only,</code> the recipes provided are processed up to the point where all the machines are prepared and properly configured. No tests will be executed and the cleanup phase is omitted as well. This mode of operation is useful if you want to perform some specific actions or tests outside of LNST using the configuration specified in a recipe file. </p>
<p> In case of <code>deconfigure,</code> the configuration from a previous config_only run will be removed, including dynamically created devices on virtual machines. There is no need to specify a recipe for this action. </p>
<p> In case of <code>list_pools,</code> lnst-ctl looks up all the pools entered in configs and dumps info about them. When used without <code>-v</code> or <code>&#8211;verbose</code> option, only pool names and paths are printed. With verbose option, all viable slave machine configs are printed in more human readable format. </p>
<p> At last, when the <i>ACTION</i> is set to <code>match_setup,</code> <code>lnst-ctl</code> will only try to match the configuration in the recipe with its local pools and print the resulting match, in case it was successful or an appropriate error message, in case it was not. </p>
<h2>CONFIGURATION</h2>
<p> <code>lnst-ctl</code> will look for configuration in the following locations: </p>
<p> <i>/etc/lnst-ctl.conf</i><br />
 <i>~/.lnst/lnst-ctl.conf</i> </p>
<p> For further description of file format or configuration options available, please refer to the configuration file itself, where each option is documented. </p>
<h2>EXIT STATUS</h2>
<p> <code>lnst-ctl</code> will terminate with one of the following statuses: </p>
<p>&nbsp;<wbr>0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>All tests passed, no errors encountered<br />
&nbsp;<wbr>1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>At least one test failed<br />
&nbsp;<wbr>2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>There was an error during the execution </p>
<h2>INTERNET RESOURCES</h2>
<p> Project Homepage: <a rel="nofollow" href="http://lnst-project.org/">http://lnst-project.org/</a><br />
 Online Documentation: <a rel="nofollow" href="https://github.com/jpirko/lnst/wiki#learn">https://github.com/jpirko/lnst/wiki#learn</a><br />
 Git Source Tree: <a rel="nofollow" href="https://github.com/jpirko/lnst">https://github.com/jpirko/lnst</a><br />
 Mailing List: &lt;lnst-developers [at] lists.fedorahosted.org&gt; </p>
<h2>AUTHORS</h2>
<p> <code>Jiri Pirko</code> &lt;jiri [at] resnulli.us&gt;<br />
 <code>Jan Tluka</code> &lt;jtluka [at] redhat.com&gt;<br />
 <code>Ondrej Lichtner</code> &lt;olichtne [at] redhat.com&gt;<br />
 <code>Jiri Prochazka</code> &lt;jprochaz [at] redhat.com&gt;<br />
 <code>Jiri Zupka</code> &lt;jzupka [at] redhat.com&gt;<br />
 <code>Radek Pazdera</code> &lt;radek [at] pazdera.co.uk&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2011-2015 Red Hat, Inc. </p>
<p> LNST is distributed under the GNU General Public License version 2. See the file &quot;COPYING&quot; in the source distribution for information on terms &amp; conditions for accessing and otherwise using LNST. </p>
<h2>Index</h2>
