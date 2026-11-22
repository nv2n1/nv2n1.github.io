---

title: "yum-aliases(1)"
name: "yum-aliases"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-aliases/"
description: "yum aliases plugin"
---

<p> yum aliases plugin  </p>
<h2>SYNOPSIS</h2>
<p> <code>yum</code> [options] alias  </p>
<h2>DESCRIPTION</h2>
<p> This plugin changes other commands in <code>yum</code>, much like the alias command in bash. There are a couple of notable differences from shell style aliases though. The alias command has three forms: <br/>
 <i></i> * alias <br/>
 <i></i> * alias command <br/>
 <i></i> * alias command result <br/>
 </p>
<p> The first form lists all current aliases with their final result, the second form looks up a &quot;command&quot; and shows it&#8217;s final result or an error message. The last form creates a new alias. </p>
<p> <br/>
 <br/>
 </p>
<h2>Explanation of alias to final result conversion</h2>
<p> When you type an aliased command, like &quot;yum --disableexcludes UPT lsu&quot; using the default aliases, the yum-aliases plugin first takes the first &quot;command&quot;, by skipping over any options, and then looks up the result (in this case &quot;UPT&quot; is converted to &quot;--enablerepo=updates-testing&quot;). If there is a match, then it will replace the aliased &quot;command&quot; in the argument list and try again (again skipping over any options). By convention, in the default aliases list, alias &quot;commands&quot; that are in all CAPS only add options so you can join together a chain of them before any real command or aliased command. <br/>
 </p>
<p> There are two things that can alter the above, if you have the &quot;recursive&quot; configuration option set to off then alias processing will stop after the first alias to command substitution. Also, like in shell aliases, if the result starts with \ then alias processing will stop. <br/>
  </p>
<h2>EXAMPLES</h2>
<p> To create a new alias command called &quot;rm&quot; which does the same thing as the command &quot;remove&quot; use: </p>
<dl>
<dd> <p> yum <code>alias</code> rm remove </p>
 </dd></dl>
<p> To always add the --skip-broken --disableexcludes=all --obsoletes options to the update command (but leaving the upgrade option alone), you could use: </p>
<dl>
<dd> <p> yum <code>alias</code> update \update --skip-broken --disableexcludes=all --obsoletes </p>
 </dd></dl>
<p> To override the default &quot;up&quot; alias to use the above update command, and never ask for confirmation, you could use: </p>
<dl>
<dd> <p> yum <code>alias</code> up update -y <br/>
 </p>
 </dd></dl>
<h2>AUTHORS</h2>
<dl>
<dd> <p> James Antill &lt;james [at] and.org&gt; </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-yum-utils/">yum-utils</a>(1)</code> <code>yum(1)</code> </p>
