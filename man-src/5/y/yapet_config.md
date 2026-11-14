---
title: "yapet_config(5)"
name: "yapet_config"
section: "5"
letter: "y"
url: "/docs/linux/man/5-yapet_config/"
description: "yapet_config – format of YAPET configuration file"
---

<p>yapet_config &#8211; format of YAPET configuration file</p>
<h2>Description</h2>
<p><code><a href="/docs/linux/man/1-yapet/">yapet</a></code>(1) reads the configuration file <code>$HOME</code>/.yapet if it exists unless a different file is specified by using the <code>-r</code> option (see <code><a href="/docs/linux/man/1-yapet/">yapet</a></code>(1)). Options given on the command line override options given in a configuration file. </p>
<p> The configuration file has the following syntax: </p>
<dl>
<dd>
<pre><i>option</i>=<i>value</i></pre>
</dl>
<p> where <i>option</i> can be any of the following: </p>
<p> <code>colors</code></p>
<dl>
<dd>(String) Set custom colors. See <code><a href="/docs/linux/man/5-yapet_colors/">yapet_colors</a></code>(5) for more information.</dl>
<p> <code>load</code></p>
<dl>
<dd>(String) The file to load upon start of <code>yapet</code>. </p>
<p> Equivalent to providing a <i>filename</i> when invoking <code>yapet</code>. </p>
<p> A <code>~</code> (tilde) sign as the first character of the pathname will be replaced by the home directory of the user running <code>yapet</code>. </p>
<p> Default: not set</dl>
<p> <code>locktimeout</code></p>
<dl>
<dd>(Integer) A positive integer specifying the time of inactivity in seconds until the screen is locked. </p>
<p> Equivalent to providing the <code>-t</code> option when invoking <code>yapet</code>. </p>
<p> Default: 600</dl>
<p> <code>pwinputtimeout</code></p>
<dl>
<dd>(Integer) A positive integer specifying the time of inactivity in seconds until the password prompt for unlocking the screen will disappear. </p>
<p> Default: 60</dl>
<p> <code>allowlockquit</code></p>
<dl>
<dd>(Boolean) A value of true allows the user to quit <code>yapet</code> from the locked screen (if no changes are pending). A value of false prevents the user from quitting <code>yapet</code> when the screen is locked. </p>
<p> Default: true</dl>
<p> <code>checkfsecurity</code></p>
<dl>
<dd>(Boolean) A value of true enables the verification of the file owner and permissions when loading a file. A value of false disables the verification of the file owner and permissions when loading a file. </p>
<p> Equivalent to providing the <code>-S</code> (same as true) or <code>-s</code> (same as false) options when invoking <code>yapet</code>. </p>
<p> Default: true</dl>
<p> <code>pwgen_rng</code></p>
<dl>
<dd>(String) The random number generator used to generate passwords. Possible values are </p>
<p> devrandom</p>
<dl>
<dd>Request using /dev/random. This is a high-quality random number generator. However, if the system lacks entropy, reading from this device may block, thus making <code>yapet</code> unresponsive.</dl>
<p> devurandom</p>
<dl>
<dd>Request using /dev/urandom. This is a quality random number generator similar to /dev/random but not of the same quality. </p>
<p> Using this random number generator will not block as opposite to /dev/random.</dl>
<p> lrand48</p>
<dl>
<dd>Request using lrand48. This is a low-quality random number generator and should be used only if none of the above two random number generators are available.</dl>
<p> rand</p>
<dl>
<dd>Request using rand. This is a last resort random number generator and should not be used.</dl>
<p> If the random number generator requested is not available on the system, <code>yapet</code> takes the next best random number generator. </p>
<p> Default: devurandom</dl>
<p> <code>pwgen_pwlen</code></p>
<dl>
<dd>(Integer) A positive integer greater than zero specifying the default password length used by the Password Generator Dialog. </p>
<p> Default: 15</dl>
<p> <code>pwgen_letters</code></p>
<dl>
<dd>(Boolean) A value of true will preselect the Letters check box of the Password Generator Dialog. false does not preselect the Letters check box. </p>
<p> Default: true</dl>
<p> <code>pwgen_digits</code></p>
<dl>
<dd>(Boolean) A value of true will preselect the Digits check box of the Password Generator Dialog. false does not preselect the Digits check box. </p>
<p> Default: true</dl>
<p> <code>pwgen_punct</code></p>
<dl>
<dd>(Boolean) A value of true will preselect the Punctuation check box of the Password Generator Dialog. false does not preselect the Punctuation check box. </p>
<p> Default: true</dl>
<p> <code>pwgen_special</code></p>
<dl>
<dd>(Boolean) A value of true will preselect the Special check box of the Password Generator Dialog. false does not preselect the Special check box. </p>
<p> Default: true</dl>
<p> <code>pwgen_other</code></p>
<dl>
<dd>(Boolean) A value of true will preselect Other check box of the Password Generator Dialog. false does not preselect the Other check box. </p>
<p> Default: false</dl>
<p> For Boolean values, 1, yes, true, enable, and enabled denote true. 0, false, no, disable, disabled denote false. Please note, Boolean values are case-sensitive. </p>
<p> See the section called &#8220;EXAMPLES&#8221; for examples of configuration files.</p>
<h2>Examples</h2>
<p><code>Example 1. Example of an yapet configuration file</code> </p>
<dl>
<dd>
<pre>load=/home/joe/passwords
locktimeout=300
checkfsecurity=0
pwgen_pwlen=8</pre>
</dl>
<p> In this example, the file /home/joe/passwords will be loaded upon invocation of <code>yapet</code>. The timeout until the screen is locked is set to 300 seconds. File permissions will not be verified. </p>
<p> The Password Generator Dialog will have preset the Password Length to 8 characters. </p>
<p> <code>Example 2. Example of an yapet configuration file</code> </p>
<dl>
<dd>
<pre>locktimeout=150
checkfsecurity=yes
pwgen_other=enable</pre>
</dl>
<p> In this example, no file will be automatically loaded upon invocation of <code>yapet</code>. The timeout until the screen is locked is set to 150 seconds. File permissions and owner will be verified. </p>
<p> The Password Generator Dialog will have preset the Other check box checked. </p>
<p> <code>Example 3. Example 1 revisited</code> </p>
<dl>
<dd>
<pre>load=~/passwords.pet
locktimeout=300
checkfsecurity=false
pwgen_pwlen=8</pre>
</dl>
<p> This example has the same effect as Example 1, &#8220;Example of an yapet configuration file&#8221;. But instead of specifying the full path to the home directory, the ~ (tilde) sign is used, which is expanded to the home directory automatically. The .pet suffix can be specified, but if omitted it will be appended automatically.</p>
<h2>Files</h2>
<p><code>$HOME</code>/.yapet</p>
<dl>
<dd>The per-user configuration file. If existing, options are read from this file but can be overridden by the command line options. </p>
<p> Processing of this file can be disabled by invoking <code>yapet</code> with the <code>-i</code> option.</dl>
<h2>Author</h2>
<p>Rafael Ostertag rafi [at] guengel.ch</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-yapet/">yapet</a></code>(1), <code><a href="/docs/linux/man/5-yapet_colors/">yapet_colors</a></code>(5)</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2008, 2009, 2010, 2011, 2013, 2014 Rafael Ostertag &lt;rafi [at] guengel.ch&gt;</p>
