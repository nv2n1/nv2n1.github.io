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
<dt>Automated Default. -a, &#8211;auto</dt>
<dd> This mode runs all the plugins that firstaidkit can detect in the paths (The paths can be set in the config file). It will run the flow denomintated &quot;diagnose&quot; for all these plugins. When a plugin does not have a diagnose flow (Some plugins like passwd don&#8217;t have it), it will be ignored. The general idea with this mode is to see what is going on in different parts of the system. The behavior of this mode can be modified by passing on of two parameters: The flow name or &quot;fix&quot;. </dd>
<p> When fix is specified, it will run the fix flow of all the plugins. This is *not* the default behavior because this might not be what the user wants. A more sensible approach is to list the possible problems and then for the user to run individual plugins to address all of the listed problems or a subset of them. </p>
<p> When FLOW is specified, the flow named FLOW is run in each plugin. As with the default behavior, the plugin is ignored when the flow is not there. </p>
<dt>Flow Selection. -f PLUGIN FLOW, &#8211;flow PLUGIN FLOW</dt>
<dd> Basically lets you specify the plugin to run and the flow that you want to run on that plugin. This implies &#8211;nodeps. </dd>
<dt>Print Configuration. &#8211;print-config</dt>
<dd> Lists the resulting configuration. Firstaidkit allows you to specify configuration elements in a lot of places. This options just lests you see what firstaidkit ends up with after analyzing all the configuration elements. </dd>
<dt>List Plugins. &#8211;list</dt>
<dd> Make a list of all the plugins. </dd>
<dt>Individual Plugin Info. &#8211;info PLUGIN</dt>
<dd> Get information fro a specific plugin. </dd>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt>-c PATH, &#8211;config=PATH</dt>
<dd> Location of configuration file.</dd>
<dt>-r PATH, &#8211;root=PATH</dt>
<dd> Location of the root directory.</dd>
<dt>-P PATH</dt>
<dd> Location of different plugin path. This option can be used more than once. firstaidkit will look for plugins in all the paths specified by this option.</dd>
<dt>-v, &#8211;verbose</dt>
<dd> Verbose mode.</dd>
<dt>-l METHOD, &#8211;log=METHOD</dt>
<dd> Select METHOD as a log method.</dd>
<dt>-x PLUGIN, &#8211;exclude=PLUGIN</dt>
<dd> Exclude PLUGIN from the run.</dd>
<dt>-g GUI, &#8211;gui=GUI</dt>
<dd> Select GUI as front end to show results.</dd>
<dt>-h, &#8211;help</dt>
<dd> Show help.</dd>
<dt>-F FLAG, &#8211;flag=FLAG</dt>
<dd> Setup startup flags.</dd>
<dt>&#8211;nodeps</dt>
<dd> This makes firstaidkit ingore dependency between plugins.</dd>
<dt>&#8211;plugin-args=ARGS</dt>
<dd> This is the way firstaidkit passes arguments to plugins. You can actually specify plugin and flow. Although flow is not necessary. The arguments and their meaning are defined by the plugin. Where ARGS is a space separated string that begins with the plugin name and/or the flow name. </dd>
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
<dt>firstaidkit -f xserver diagnose</dt>
<dd> Execute the diagnose flow in a specific plugin. This line will execute the xserver plugin in diagnose mode.</dd>
<dt>firstaidkit -a &#8211;nodeps</dt>
<dd> Execute all plugins without dependencies. This will execute all plugins without looking at the dependencies between them. This is good if you want a general diagnose of the system.</dd>
<dt>firstaidkit &#8211;print-config</dt>
<dd> List the configuration.</dd>
<dt>firstaidkit &#8211;list</dt>
<dd> List of plugins.</dd>
<dt>firstaidkit &#8211;info xserver</dt>
<dd> Request a specific info from a plugin.</dd>
<dt>firstaidkit -a -e xserver</dt>
<dd> Exclude a plugin from an action. This will execute every plugin except the xserver.</dd>
<dt>firstaidkit &#8211;plugin-args=&#8217;grub/fix recover-devs=/dev/sda&#8217; -f grub fix</dt>
<dd> Runs the plugin plugin in the fix flow and passes it the &quot;recover-devs=/dev/sda&quot; argument. </dd>
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
