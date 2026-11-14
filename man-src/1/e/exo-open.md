---
title: "exo-open(1)"
name: "exo-open"
section: "1"
letter: "e"
url: "/docs/linux/man/1-exo-open/"
description: "exo-open – Open URLs and launch preferred applications"
---

<h2 class="name">NAME</h2>
<p> exo-open &#8211; Open URLs and launch preferred applications </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>exo-open</code> [[url]&#8230;]</p>
<dt> <code>exo-open</code> &#8211;launch [category] [[parameter]&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>exo-open</code></p>
<dd>is a command line frontend to the <code>Xfce Preferred Applications</code> framework. It can either be used to open a list of <i>url</i>s with the default URL handler or launch the preferred application for a certain category.</p>
<h2>INVOCATION</h2>
<p> <code>exo-open</code> either takes a list of URLs and tries to open each of them using the default handler, or, when using the <code>&#8211;launch</code> tries to launch the preferred application for a certain category, optionally passing any number of <i>parameter</i>s to the application.</p>
<h3>Options</h3>
<p> <code>-?</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print brief help and exit.</dl>
<p> <code>-v</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print version information and exit.</dl>
<p> <code>&#8211;working-directory</code> <i>directory</i></p>
<dl>
<dt>
<dd> When using the <code>&#8211;launch</code> option and this option is specified as well, the application will be run in the given <i>directory</i>. This is primarily useful when running the preferred <code>TerminalEmulator</code> from another application and you want the command in the terminal window to be run in a specific directory.</dl>
<p> <code>&#8211;launch</code> <i>category</i> <i>parameters&#8230;</i></p>
<dl>
<dt>
<dd> Launch the preferred application for the given <i>category</i> with the optional <i>parameters&#8230;</i>, where <i>category</i> is either <code>WebBrowser</code>, <code>MailReader</code>, <code>TerminalEmulator</code> or <code>FileManager</code>.</dl>
<p> If you do not specify the <code>&#8211;launch</code> option, <code>exo-open</code> will open all specified URLs with their preferred URL handlers. Else, if you specify the <code>&#8211;launch</code> option, you can select which preferred application you want to run, and pass additional <i>parameters</i> to the application (i.e. for <code>TerminalEmulator</code> you can pass the command line that should be run in the terminal).</p>
<h2>COMPOSING EMAILS</h2>
<p> <code>exo-open</code> allows users and developers to open the preferred email composer from the command line by simply invoking <code>exo-open mailto:USER [at] HOST.TLD</code>. This will open the composer window with <i>USER [at] HOST.TLD</i> as the recipient. This syntax is supported by all <code>MailReader</code>s. In addition the <code>MailReader</code>s that ship as part of libexo also support extended mailto:-URIs (but be aware that user-defined mailers do not necessarily support this), which allows you to also specify default values for the subject and the body of the mail, add additional recipients (both Cc: and To:) and attach files to emails. For example <i>mailto:foo [at] foo.org?cc=bar [at] bar.org&amp;subject=Foo&amp;attach=/foo/bar.txt</i> tells the composer to start an email to foo [at] foo.org and bar [at] bar.org with Foo in the subject and the file /foo/bar.txt attached to the message.</p>
<h2>AUTHOR</h2>
<p> <code>exo-open</code> was written by Benedikt Meurer &lt;benny [at] xfce.org&gt;. </p>
<p> This manual page was provided by Benedikt Meurer &lt;benny [at] xfce.org&gt;. </p>
<h2>Index</h2>
