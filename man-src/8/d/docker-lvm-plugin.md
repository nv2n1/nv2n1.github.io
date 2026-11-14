---
title: "docker-lvm-plugin(8)"
name: "docker-lvm-plugin"
section: "8"
letter: "d"
url: "/docs/linux/man/8-docker-lvm-plugin/"
description: "docker-lvm-plugin – Docker Volume Driver for lvm volumes"
---

<p>docker-lvm-plugin &#8211; Docker Volume Driver for lvm volumes </p>
<h2>Synopsis</h2>
<p><code>docker-lvm-plugin</code> [<code>-debug</code>] [<code>-version</code>] </p>
<h2>Description</h2>
<p>This plugin can be used to create lvm volumes of specified size, which can then be bind mounted into the container using docker run command. </p>
<h2>Usage</h2>
<p>Start the docker daemon before starting the docker-lvm-plugin daemon. You can start docker daemon using command: </p>
<dl>
<dd>
<pre>systemctl start docker </pre>
</dl>
<p> Once docker daemon is up and running, you can start docker-lvm-plugin daemon using command: </p>
<dl>
<dd>
<pre>systemctl start docker-lvm-plugin</pre>
</dl>
<p> docker-lvm-plugin daemon is on-demand socket activated. Running docker volume ls command will automatically start the daemon. </p>
<p> Since logical volumes (lv&#8217;s) are based on a volume group, it is the responsibility of the user (administrator) to provide a volume group name. You can choose an existing volume group name by listing volume groups on your system using vgs command OR create a new volume group using vgcreate command. e.g. </p>
<dl>
<dd>
<pre>vgcreate vg1 /dev/hda </pre>
</dl>
<p> where /dev/hda is your partition or whole disk on which physical volumes were created. </p>
<p> Add this volume group name in the config file. </p>
<dl>
<dd>
<pre>/etc/docker/docker-lvm-plugin</pre>
</dl>
<p> The docker-lvm-plugin also supports the creation of thinly-provisioned volumes. To create a thinly-provisioned volume, a user (administrator) must first create a thin pool using the lvcreate command. </p>
<dl>
<dd>
<pre>lvcreate -L 10G -T vg1/mythinpool</pre>
</dl>
<p> This will create a thinpool named mythinpool of size 10G under volume group vg1. NOTE: thinpools are special kind of logical volumes carved out of the volume group. Hence in the above example, to create the thinpool mythinpool you must have atleast 10G of freespace in volume group vg1.</p>
<h2>Options</h2>
<p><code>-debug</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>Enable debug logging. Default is false. <code>-version</code>=<i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>Print version information and quit. Default is false.</p>
<h2>Examples</h2>
<p><code>Volume Creation</code>  </p>
<pre>docker volume create -d lvm --opt size=0.2G foobar</pre>
</dl>
<p> This will create a lvm volume named foobar of size 208 MB (0.2 GB).  </p>
<pre>docker volume create -d lvm --opt size=0.2G --opt thinpool=mythinpool thin_vol</pre>
</dl>
<p> This will create a thinly-provisioned lvm volume named thin_vol in mythinpool.  </p>
<pre>docker volume create -d lvm --opt snapshot=foobar --opt size=100M foobar_snapshot</pre>
</dl>
<p> This will create a snapshot volume of foobar named foobar_snapshot. For thin snapshots, use the same command above but don&#8217;t specify a size.  </p>
<pre>docker volume create -d lvm --opt size=0.2G --opt keyfile=/root/key.bin crypt_vol</pre>
</dl>
<p> This will create a LUKS encrypted lvm volume named crypt_vol with the contents of /root/key.bin as a binary passphrase. Snapshots of encrypted volumes use the same key file. The key file must be present when the volume is created, and when it is mounted to a container. <code>Volume List</code>  </p>
<pre>docker volume ls</pre>
</dl>
<p> This will list volumes created by all docker drivers including the default driver (local). <code>Volume Inspect</code>  </p>
<pre>docker volume inspect foobar</pre>
</dl>
<p> This will inspect foobar and return a JSON. [<br />
&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;Driver&quot;:&nbsp;<wbr>&quot;lvm&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;Labels&quot;:&nbsp;<wbr>{},<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;Mountpoint&quot;:&nbsp;<wbr>&quot;/var/lib/docker-lvm-plugin/foobar&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;Name&quot;:&nbsp;<wbr>&quot;foobar&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;Options&quot;:&nbsp;<wbr>{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;size&quot;:&nbsp;<wbr>&quot;0.2G&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>},<br />
&nbsp;<wbr>&nbsp;<wbr>&quot;Scope&quot;:&nbsp;<wbr>&quot;local&quot;<br />
&nbsp;<wbr>} ] <code>Volume Removal</code>  </p>
<pre>docker volume rm foobar</pre>
</dl>
<p> This will remove lvm volume foobar. <code>Bind Mount lvm volume inside the container</code>  </p>
<pre>docker run -it -v foobar:/home fedora /bin/bash</pre>
</dl>
<p> This will bind mount the logical volume foobar into the home directory of the container. </p>
