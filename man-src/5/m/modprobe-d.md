---
title: "modprobe-d(5)"
name: "modprobe-d"
section: "5"
letter: "m"
url: "/docs/linux/man/5-modprobe-d/"
description: "modprobe.d – Configuration directory for modprobe"
---

<p>modprobe.d &#8211; Configuration directory for modprobe</p>
<h2>Synopsis</h2>
<p>/lib/modprobe.d/*.conf </p>
<p> /usr/local/lib/modprobe.d/*.conf </p>
<p> /run/modprobe.d/*.conf </p>
<p> /etc/modprobe.d/*.conf</p>
<h2>Description</h2>
<p>Because the <code>modprobe</code> command can add or remove more than one module, due to modules having dependencies, we need a method of specifying what options are to be used with those modules. All files underneath the /etc/modprobe.d directory which end with the .conf extension specify those options as required. They can also be used to create convenient aliases: alternate names for a module, or they can override the normal <code>modprobe</code> behavior altogether for those with special requirements (such as inserting more than one module). </p>
<p> Note that module and alias names (like other module names) can have &#8211; or _ in them: both are interchangeable throughout all the module commands as underscore conversion happens automatically. </p>
<p> The format of files under modprobe.d is simple: one command per line, with blank lines and lines starting with &#8216;#&#8217; ignored (useful for adding comments). A &#8216;\&#8217; at the end of a line causes it to continue on the next line, which makes the file a bit neater.</p>
<h2>Commands</h2>
<p>alias <i>wildcard</i> <i>modulename</i></p>
<dl>
<dd>This allows you to give alternate names for a module. For example: &quot;alias my-mod really_long_modulename&quot; means you can use &quot;modprobe my-mod&quot; instead of &quot;modprobe really_long_modulename&quot;. You can also use shell-style wildcards, so &quot;alias my-mod* really_long_modulename&quot; means that &quot;modprobe my-mod-something&quot; has the same effect. You can&#8217;t have aliases to other aliases (that way lies madness), but aliases can have options, which will be added to any other options. </p>
<p> Note that modules can also contain their own aliases, which you can see using <code>modinfo</code>. These aliases are used as a last resort (ie. if there is no real module, <code>install</code>, <code>remove</code>, or <code>alias</code> command in the configuration).</dl>
<p> blacklist <i>modulename</i></p>
<dl>
<dd>Modules can contain their own aliases: usually these are aliases describing the devices they support, such as &quot;pci:123&#8230;&quot;. These &quot;internal&quot; aliases can be overridden by normal &quot;alias&quot; keywords, but there are cases where two or more modules both support the same devices, or a module invalidly claims to support a device that it does not: the <code>blacklist</code> keyword indicates that all of that particular module&#8217;s internal aliases are to be ignored.</dl>
<p> install <i>modulename</i> <i>command&#8230;</i></p>
<dl>
<dd>This command instructs <code>modprobe</code> to run your command instead of inserting the module in the kernel as normal. The command can be any shell command: this allows you to do any kind of complex processing you might wish. For example, if the module &quot;fred&quot; works better with the module &quot;barney&quot; already installed (but it doesn&#8217;t depend on it, so <code>modprobe</code> won&#8217;t automatically load it), you could say &quot;install fred /sbin/modprobe barney; /sbin/modprobe &#8211;ignore-install fred&quot;, which would do what you wanted. Note the <code>&#8211;ignore-install</code>, which stops the second <code>modprobe</code> from running the same <code>install</code> command again. See also <code>remove</code> below. </p>
<p> The long term future of this command as a solution to the problem of providing additional module dependencies is not assured and it is intended to replace this command with a warning about its eventual removal or deprecation at some point in a future release. Its use complicates the automated determination of module dependencies by distribution utilities, such as mkinitrd (because these now need to somehow interpret what the <code>install</code> commands might be doing. In a perfect world, modules would provide all dependency information without the use of this command and work is underway to implement soft dependency support within the Linux kernel. </p>
<p> If you use the string &quot;$CMDLINE_OPTS&quot; in the command, it will be replaced by any options specified on the modprobe command line. This can be useful because users expect &quot;modprobe fred opt=1&quot; to pass the &quot;opt=1&quot; arg to the module, even if there&#8217;s an install command in the configuration file. So our above example becomes &quot;install fred /sbin/modprobe barney; /sbin/modprobe &#8211;ignore-install fred $CMDLINE_OPTS&quot;</dl>
<p> options <i>modulename</i> <i>option&#8230;</i></p>
<dl>
<dd>This command allows you to add options to the module <i>modulename</i> (which might be an alias) every time it is inserted into the kernel: whether directly (using <code>modprobe </code> <i>modulename</i>) or because the module being inserted depends on this module. </p>
<p> All options are added together: they can come from an <code>option</code> for the module itself, for an alias, and on the command line.</dl>
<p> remove <i>modulename</i> <i>command&#8230;</i></p>
<dl>
<dd>This is similar to the <code>install</code> command above, except it is invoked when &quot;modprobe -r&quot; is run.</dl>
<p> softdep <i>modulename</i> pre: <i>modules&#8230;</i> post: <i>modules&#8230;</i></p>
<dl>
<dd>The <code>softdep</code> command allows you to specify soft, or optional, module dependencies. <i>modulename</i> can be used without these optional modules installed, but usually with some features missing. For example, a driver for a storage HBA might require another module be loaded in order to use management features. </p>
<p> pre-deps and post-deps modules are lists of names and/or aliases of other modules that modprobe will attempt to install (or remove) in order before and after the main module given in the <i>modulename</i> argument. </p>
<p> Example: Assume &quot;softdep c pre: a b post: d e&quot; is provided in the configuration. Running &quot;modprobe c&quot; is now equivalent to &quot;modprobe a b c d e&quot; without the softdep. Flags such as &#8211;use-blacklist are applied to all the specified modules, while module parameters only apply to module c. </p>
<p> Note: if there are <code>install</code> or <code>remove</code> commands with the same <i>modulename</i> argument, <code>softdep</code> takes precedence.</dl>
<h2>Compatibility</h2>
<p>A future version of kmod will come with a strong warning to avoid use of the <code>install</code> as explained above. This will happen once support for soft dependencies in the kernel is complete. That support will complement the existing softdep support within this utility by providing such dependencies directly within the modules.</p>
<h2>Copyright</h2>
<p>This manual page originally Copyright 2004, Rusty Russell, IBM Corporation. Maintained by Jon Masters and others.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-modprobe/">modprobe</a></code>(8), <code><a href="/docs/linux/man/5-modules-dep/">modules.dep</a></code>(5)</p>
<h2>Authors</h2>
<p><code>Jon Masters</code> &lt;jcm [at] jonmasters.org&gt;</p>
<dl>
<dd>Developer</dl>
<p> <code>Robby Workman</code> &lt;rworkman [at] slackware.com&gt;</p>
<dl>
<dd>Developer</dl>
<p> <code>Lucas De Marchi</code> &lt;lucas.de.marchi [at] gmail.com&gt;</p>
<dl>
<dd>Developer</dl>
