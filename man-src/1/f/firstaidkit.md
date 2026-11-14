---
title: "firstaidkit(1)"
name: "firstaidkit"
section: "1"
letter: "f"
url: "/docs/linux/man/1-firstaidkit/"
---

<h2>NAME FirstAidKit</h2>
<p> <code>.SH</code>SYNOPSIS firstaidkit [options] [-a | &#8211;auto] [fix | FLOW ]<br />
 firstaidkit [options] [-f | &#8211;flow ] PLUGIN FLOW<br />
 firstaidkit [options] &#8211;print-config<br />
 firstaidkit [options] &#8211;list<br />
 firstaidkit [options] &#8211;info &lt;plugin&gt; </p>
<p> <code>.SH</code>DESCRIPTION Firstaidkit executes simple and common recovery tasks in an automated way. The basic elements in the system are: backend plugin system, the plugins and the plugin flows. The plugins can be thought of as individual recovery units. Each unit having the possibility of holding varioius types of processes, but still focused on one specific subsystem. There can be a plugin for password recovery for example. This plugin would take care of all the possible processes related to password recovery. In the password recovery plugin there would only be one process: to recover the password. But other plugins might need to executing more than one process. Like if you would like to diagnose before actually fixing something. </p>
<p> Plugin flows are structures that represent the different processes. You will usually find two default flows in a plugin (with known exceptions): The diagnose flow and the fix flow. When in diagnose no changes to the system should be done. Only information should be taken from the system and output through the firstaidkit reporting system (this basically means a log file or stdout. It all depends on the configuration parameters when executing firstaidkit). When in fix mode an attempt will be made to modify the system to fix whatever was found to be missconfigured. </p>
<p> Currently firstaidkit has 6 modes of operation: </p>
<dl>
<dt>Automated Default. -a, &#8211;auto</p>
<dd> This mode runs all the plugins that firstaidkit can detect in the paths (The paths can be set in the config file). It will run the flow denomintated &quot;diagnose&quot; for all these plugins. When a plugin does not have a diagnose flow (Some plugins like passwd don&#8217;t have it), it will be ignored. The general idea with this mode is to see what is going on in different parts of the system. The behavior of this mode can be modified by passing on of two parameters: The flow name or &quot;fix&quot;. </p>
<p> When fix is specified, it will run the fix flow of all the plugins. This is *not* the default behavior because this might not be what the user wants. A more sensible approach is to list the possible problems and then for the user to run individual plugins to address all of the listed problems or a subset of them. </p>
<p> When FLOW is specified, the flow named FLOW is run in each plugin. As with the default behavior, the plugin is ignored when the flow is not there. </p>
<dt>Flow Selection. -f PLUGIN FLOW, &#8211;flow PLUGIN FLOW</p>
<dd> Basically lets you specify the plugin to run and the flow that you want to run on that plugin. This implies &#8211;nodeps. </p>
<dt>Print Configuration. &#8211;print-config</p>
<dd> Lists the resulting configuration. Firstaidkit allows you to specify configuration elements in a lot of places. This options just lests you see what firstaidkit ends up with after analyzing all the configuration elements. </p>
<dt>List Plugins. &#8211;list</p>
<dd> Make a list of all the plugins. </p>
<dt>Individual Plugin Info. &#8211;info PLUGIN</p>
<dd> Get information fro a specific plugin. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-c PATH, &#8211;config=PATH</p>
<dd> Location of configuration file.</p>
<dt>-r PATH, &#8211;root=PATH</p>
<dd> Location of the root directory.</p>
<dt>-P PATH</p>
<dd> Location of different plugin path. This option can be used more than once. firstaidkit will look for plugins in all the paths specified by this option.</p>
<dt>-v, &#8211;verbose</p>
<dd> Verbose mode.</p>
<dt>-l METHOD, &#8211;log=METHOD</p>
<dd> Select METHOD as a log method.</p>
<dt>-x PLUGIN, &#8211;exclude=PLUGIN</p>
<dd> Exclude PLUGIN from the run.</p>
<dt>-g GUI, &#8211;gui=GUI</p>
<dd> Select GUI as front end to show results.</p>
<dt>-h, &#8211;help</p>
<dd> Show help.</p>
<dt>-F FLAG, &#8211;flag=FLAG</p>
<dd> Setup startup flags.</p>
<dt>&#8211;nodeps</p>
<dd> This makes firstaidkit ingore dependency between plugins.</p>
<dt>&#8211;plugin-args=ARGS</p>
<dd> This is the way firstaidkit passes arguments to plugins. You can actually specify plugin and flow. Although flow is not necessary. The arguments and their meaning are defined by the plugin. Where ARGS is a space separated string that begins with the plugin name and/or the flow name. </p>
<p> ARGS=&quot;plugin_name[/flow_name] arg1 arg2 arg3&quot; </p>
<p> So if you wanted to pass &quot;&#8211;installto-devs=/dev/sda&quot; to the grub plugin in the fix flow, you would pass the following arg to firstaidkit: </p>
<p> &#8211;plugin-args=&quot;grub/fix &#8211;installto-devs=/dev/sda&quot; </p>
</dl>
<h2>EXAMPLES</h2>
<pre>
For most of the situations its probably better to execute
the plugins individually.  You manage this by using the -f
option.
</pre>
<dl>
<dt>firstaidkit -f xserver diagnose</p>
<dd> Execute the diagnose flow in a specific plugin. This line will execute the xserver plugin in diagnose mode.</p>
<dt>firstaidkit -a &#8211;nodeps</p>
<dd> Execute all plugins without dependencies. This will execute all plugins without looking at the dependencies between them. This is good if you want a general diagnose of the system.</p>
<dt>firstaidkit &#8211;print-config</p>
<dd> List the configuration.</p>
<dt>firstaidkit &#8211;list</p>
<dd> List of plugins.</p>
<dt>firstaidkit &#8211;info xserver</p>
<dd> Request a specific info from a plugin.</p>
<dt>firstaidkit -a -e xserver</p>
<dd> Exclude a plugin from an action. This will execute every plugin except the xserver.</p>
<dt>firstaidkit &#8211;plugin-args=&#8217;grub/fix recover-devs=/dev/sda&#8217; -f grub fix</p>
<dd> Runs the plugin plugin in the fix flow and passes it the &quot;recover-devs=/dev/sda&quot; argument. </p>
</dl>
<h2>BUGS</h2>
<pre>
Please report bugs at <a rel="nofollow" href="http://fedorahosted.org/firstaidkit/newticket">http://fedorahosted.org/firstaidkit/newticket</a>
</pre>
<h2>AUTHORS</h2>
<pre><code>
Martin Sivak&lt;msivak[at] redhat.com&gt;
    Joel Granados&lt;jgranado[at] redhat.com&gt;
</code></pre>
<h2>FILES</h2>
<pre>
/etc/firstaidkit.conf
</pre>
<h2>SEE ALSO</h2>
<pre>
<a rel="nofollow" href="http://fedorahosted.org/firstaidkit">http://fedorahosted.org/firstaidkit</a>
</pre>
<h2>Index</h2>
