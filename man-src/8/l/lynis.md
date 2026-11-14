---
title: "lynis(8)"
name: "lynis"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lynis/"
description: "Lynis – System and security auditing tool"
---

<p><code> Lynis </code>&#8211; System and security auditing tool</p>
<h2>Synopsis</h2>
<pre><code>lynis</code> [scan mode] [other options]</pre>
<h2>Description</h2>
<p><code>Lynis</code> is a security auditing tool for Linux, Mac OSX, and UNIX systems. It checks the system and the software configuration, to see if there is any room for improvement the security defenses. All details are stored in a log file. Findings and other discovered data is stored in a report file. This can be used to compare differences between audits. <code>Lynis</code> can run interactively or as a cronjob. Root permissions (e.g. sudo) are not required, however provide more details during the audit. The following system areas may be checked:</p>
<dl>
<dd>&#8211; Boot loader files</p>
<dd>&#8211; Configuration files</p>
<dd>&#8211; Software packages</p>
<dd>&#8211; Directories and files related to logging and auditing</p>
<dd>
<h2>First Time Usage</h2>
<p>When running <code>Lynis</code> for the first time, run: lynis audit system</p>
<h2>Commands</h2>
<dl>
<dt>audit &lt;type&gt;</p>
<dd>Perform an audit of the selected type</p>
<dt>show &lt;parameter&gt;</p>
<dd>Show varies information details like configuration and paths</p>
<dt>update &lt;parameter&gt;</p>
<dd>Perform activities regarding updating</p>
<dt>upload-only</p>
<dd>Upload the available report data file </p>
</dl>
<h2>Scan Types</h2>
<dl>
<dt>audit system</p>
<dd>Performs a system audit, which is the most common audit.</p>
<dt>audit system remote &lt;host&gt;</p>
<dd>Provide commands to do a remote scan.</dl>
<p> For more scan modes, see the helper utilities.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;auditor &lt;full name&gt;</code></p>
<dd>Define the name of the auditor/pen-tester. When a full name is used, add double quotes, like &quot;Your Name&quot;.</p>
<dt><code>&#8211;checkall (or -c)</code></p>
<dd><code>Lynis</code> performs a full check of the system, printing out the results of each test to stdout. Additional information will be saved into a log file (default is /var/log/lynis.log). This option invokes scan mode &quot;audit system&quot;.</p>
<dd>In case the outcome of a scan needs to be automated, use the report file.</p>
<dt><code>&#8211;config</code></p>
<dd>Show which settings file or profile is being used, then quit.</p>
<dt><code>&#8211;cronjob</code></p>
<dd>Perform automatic scan with cron safe options (no colors, no questions, no breaks).</p>
<dt><code>&#8211;debug</code></p>
<dd>Display debug information to screen for troubleshooting purposes.</p>
<dt><code>&#8211;developer</code></p>
<dd>Display developer information when creating tests.</p>
<dt><code>&#8211;dump-options</code></p>
<dd>Show all available parameters.</p>
<dt><code>&#8211;logfile &lt;/path/to/logfile&gt;</code></p>
<dd>Defines location and name of log file, instead of default /var/log/lynis.log.</p>
<dt><code>&#8211;no-colors</code></p>
<dd>Do not use colors for messages, warnings and sections.</p>
<dt><code>&#8211;no-log</code></p>
<dd>Redirect all logging information to /dev/null, prevent sensitive information to be written to disk.</p>
<dt><code>&#8211;pentest</code></p>
<dd>Run a non-privileged scan, usually for penetration testing. Some of the tests will be skipped if they require root permissions.</p>
<dt><code>&#8211;plugin-dir &lt;/path/to/plugins&gt;</code></p>
<dd>Define location where plugins can be found.</p>
<dt><code>&#8211;profile &lt;file&gt;</code></p>
<dd>Provide alternative profile to perform the scan.</p>
<dt><code>&#8211;quick (-Q)</code></p>
<dd>Do a quick scan (don&#8217;t wait for user input).</p>
<dt><code>&#8211;quiet (-q)</code></p>
<dd>Run quietly and do not show anything to the screen. Will also enable quick mode.</p>
<dt><code>&#8211;report-file &lt;file&gt;</code></p>
<dd>Provide an alternative name for report file.</p>
<dt><code>&#8211;reverse-colors</code></p>
<dd>Optimize screen output for light backgrounds.</p>
<dt><code>&#8211;skip-plugins</code></p>
<dd>Do not run plugins.</p>
<dt><code>&#8211;tests TEST-IDs</code></p>
<dd>Only run the specific test(s). When using multiple tests, add quotes around the line.</p>
<dt><code>&#8211;tests-from-group &lt;group&gt;</code></p>
<dd>Only perform tests from particular group of tests. Use &#8216;show groups&#8217; to determine valid options.</p>
<dt><code>&#8211;upload</code></p>
<dd>Upload data to Lynis Enterprise server.</p>
<dt><code>&#8211;wait</code></p>
<dd>Wait for user to continue. This adds a break after each section (opposed of &#8211;quick).</p>
<dt><code>&#8211;warnings-only</code></p>
<dd>Run quietly, except warnings.</dl>
<dl>
<dd>Multiple parameters are allowed, though some parameters can only be used together with others. When running Lynis without any parameters, help will be shown and the program will exit.</dl>
<h2>Helpers</h2>
<p>Lynis has special helpers to do certain tasks. This way the framework of Lynis is used, while at the same time storing most of the functionality in a separated file. This speeds up execution and keeps the code clean. </p>
<dl>
<dt>audit</p>
<dd>Run audit on the system or on other targets</p>
<dt>show</p>
<dd>Provide details about Lynis</p>
<dt>update</p>
<dd>Run updater utility</dl>
<p> To use a helper, run Lynis followed by the helper name.</p>
<h2>Exit Codes</h2>
<p>Lynis uses exit codes to signal any invoking script. Currently the following codes are used:</p>
<dl>
<dt>0</p>
<dd>Program exited normally</p>
<dt>1</p>
<dd>Fatal error</p>
<dt>64</p>
<dd>An unknown parameter is used, or incomplete</p>
<dt>65</p>
<dd>Incorrect data encountered</p>
<dt>66</p>
<dd>Can&#8217;t open file or directory</p>
<dt>78</p>
<dd>Lynis found 1 or more warnings or configurations errors (with error-on-warnings=yes) </p>
</dl>
<h2>Bugs</h2>
<p>Bugs can be reported via GitHub at <a rel="nofollow" href="https://github.com/CISOfy/lynis">https://github.com/CISOfy/lynis</a> </p>
<h2>Documentation</h2>
<p>Supporting documentation can be found via <a rel="nofollow" href="https://cisofy.com/support/">https://cisofy.com/support/</a></p>
<h2>Licensing</h2>
<p>Lynis is licensed as GPL v3. It was created by Michael Boelen in 2007. Development has been taken over by CISOfy. Plugins may have a different license.</p>
<h2>Contact Information</h2>
<p>Support requests and project related questions can be addressed via e-mail: lynis-dev [at] cisofy.com.</p>
