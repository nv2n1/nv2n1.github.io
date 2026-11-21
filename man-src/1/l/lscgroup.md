---

title: "lscgroup(1)"
name: "lscgroup"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lscgroup/"
description: "lscgroup – list all cgroups"
---

<h2>NAME</h2>
<p> lscgroup &#8211; list all cgroups </p>
<p> <code>lscgroup</code> [[<code>-g</code>] &lt;<i>controllers&gt;:&lt;path</i>&gt;] [&#8230;]<br />
 <code>lscgroup</code> [<code>-h|&#8211;help</code>] </p>
<p> List all/chosen cgroups. </p>
<dl>
<dt><code>&lt;controllers&gt;:&lt;path&gt;</code></dt>
<dd> defines the control groups whose subgroups will be shown. If this parameter is not used, the command will list all existing cgroups. </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CGROUP_LOGLEVEL</code></dt>
<dd> controls verbosity of the tool. Allowed values are <code>DEBUG</code>, <code>INFO</code>, <code>WARNING</code> or <code>ERROR</code>. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt><code>lscgroup -g cpu:/</code></dt>
<dd> list all cgroups which are in hierarchy containing cpu controller </dd>
<dt><code>lscgroup -g cpu:/student</code></dt>
<dd> list all cgroups which are in hierarchy containing cpu controller in subgroup student </dd>
<dt><code>lscgroup</code></dt>
<dd> list all cgroups which in all hierarchies </dd>
</dl>
<h2>SEE ALSO</h2>
<p> lssubsys (1), cgcreate (1), cgdelete (1), cgconfig.conf (5) </p>
