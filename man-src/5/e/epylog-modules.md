---
title: "epylog-modules(5)"
name: "epylog-modules"
section: "5"
letter: "e"
url: "/docs/linux/man/5-epylog-modules/"
description: "epylog-modules – epylog module cofiguration."
---

<p><code>epylog-modules</code> &#8211; epylog module cofiguration.</p>
<h2>Synopsis</h2>
<p><code>epylog</code> uses pluggable modules to perform analysis and report on syslog strings. This manpage explains the format of the module config files. </p>
<h2>modules.d</h2>
<p>Epylog config files are placed in the <code>modules.d</code> directory of the cfgdir specified in epylog.conf. Any file ending in .conf in that directory is considered a module config file. Most common location for modules.d directory is in /etc/epylog/modules.d.</p>
<h2>module.conf</h2>
<p>The name of the config file doesn&#8217;t carry much meaning, however it MUST end in .conf in order to be recognized as a module config file. </p>
<p> The config file for each module is separated into two parts: [module] and [conf].</p>
<h2>[module]</h2>
<dl>
<dt><code>desc</code></p>
<dd>The description of the module. It will be shown in the final report.</p>
<dt><code>exec</code></p>
<dd>This is where the &quot;body&quot; of the module is located. Most modules that come with the distribution will be placed in /usr/share/epylog/modules, but depending on your setup, you may place them elsewhere.</p>
<dt><code>files</code></p>
<dd>List the logfiles requested by this module in this field. Separate multiple entries by comma. Epylog will handle rotated files, but you need to specify the mask appropriately. E.g. the most common logrotate setup will place rotated files in the same directory and add .0, .1, .2, etc to the end of the file. Therefore, a file entry would look like so:<br />
 <code>/var/log/filename[.#]</code><br />
 If you have compression turned on, your entry will look like so:<br />
 <code>/var/log/filename[.#.gz]</code><br />
 Lastly, for advanced configurations, more complex entries may be required. E.g. if your logrotate saves rotated files in a subdirectory in /var/log, you can specify it like so:<br />
 <code>/var/log/[rotate/]filename[.#.gz]</code><br />
 This will work, too:<br />
 <code>/var/log/filename[/var/rotate/filename.#.gz]</code><br />
 In any case, &quot;#&quot; will be where the increments will go.</p>
<dt><code>enabled</code></p>
<dd>Can be either &quot;yes&quot; or &quot;no&quot;. If &quot;no&quot; is specified, Epylog will completely ignore this module.</p>
<dt><code>internal</code></p>
<dd>Can be either &quot;yes&quot; or &quot;no&quot;. If &quot;yes&quot;, then the module is handled as an internal module, and if &quot;no&quot;, then the external module API is used. See doc/modules.txt for more information about the module APIs.</p>
<dt><code>outhtml</code></p>
<dd>Specifies whether the output produced by the module is HTML or not. Can be either &quot;yes&quot; or &quot;no&quot;.</p>
<dt><code>priority</code></p>
<dd>An unsigned int. Most commonly a number from 0 to 10. Modules with the lowest number will be considered the highest prioroty and will be both invoked and presented in the final report before the others. </p>
</dl>
<h2>[conf]</h2>
<p>This is where per-module configuration directives go. Some modules have these, some don&#8217;t. Look in the module config file &#8212; the available values should be listed and described there.</p>
<h2>Comments</h2>
<p>Lines starting with &quot;#&quot; will be considered commented out.</p>
<h2>Authors</h2>
<p>Konstantin Ryabitsev &lt;icon [at] linux.duke.edu&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-epylog/">epylog</a>(8), <a href="/docs/linux/man/3-epylog/">Epylog</a>(3), <a href="/docs/linux/man/5-epylog-conf/">epylog.conf</a>(5) </p>
