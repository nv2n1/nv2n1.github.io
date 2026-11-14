---
title: "docker-build(1)"
name: "docker-build"
section: "1"
letter: "d"
url: "/docs/linux/man/1-docker-build/"
description: "docker-build – Build an image from a Dockerfile"
---

<h2 class="name">NAME</h2>
<p> docker-build &#8211; Build an image from a Dockerfile </p>
<h2>SYNOPSIS</h2>
<p> <code>docker build</code> [<code>&#8211;add-host</code>[=<i>[]</i>]] [<code>&#8211;build-arg</code>[=<i>[]</i>]] [<code>&#8211;cache-from</code>[=<i>[]</i>]] [<code>&#8211;cpu-shares</code>[=<i>0</i>]] [<code>&#8211;cgroup-parent</code>[=<i>CGROUP-PARENT</i>]] [<code>&#8211;help</code>] [<code>&#8211;iidfile</code>[=<i>CIDFILE</i>]] [<code>-f</code>|<code>&#8211;file</code>[=<i>PATH/Dockerfile</i>]] [<code>-squash</code>] <i>Experimental</i> [<code>&#8211;force-rm</code>] [<code>&#8211;isolation</code>[=<i>default</i>]] [<code>&#8211;label</code>[=<i>[]</i>]] [<code>&#8211;no-cache</code>] [<code>&#8211;pull</code>] [<code>&#8211;compress</code>] [<code>-q</code>|<code>&#8211;quiet</code>] [<code>&#8211;rm</code>[=<i>true</i>]] [<code>-t</code>|<code>&#8211;tag</code>[=<i>[]</i>]] [<code>-m</code>|<code>&#8211;memory</code>[=<i>MEMORY</i>]] [<code>&#8211;memory-swap</code>[=<i>LIMIT</i>]] [<code>&#8211;network</code>[=<i>&quot;default&quot;</i>]] [<code>&#8211;shm-size</code>[=<i>SHM-SIZE</i>]] [<code>&#8211;cpu-period</code>[=<i>0</i>]] [<code>&#8211;cpu-quota</code>[=<i>0</i>]] [<code>&#8211;cpuset-cpus</code>[=<i>CPUSET-CPUS</i>]] [<code>&#8211;cpuset-mems</code>[=<i>CPUSET-MEMS</i>]] [<code>&#8211;target</code>[=<i>[]</i>]] [<code>&#8211;ulimit</code>[=<i>[]</i>]] PATH | URL | &#8211; </p>
<h2>DESCRIPTION</h2>
<p> This will read the Dockerfile from the directory specified in <code>PATH</code>. It also sends any other files and directories found in the current directory to the Docker daemon. The contents of this directory would be used by <code>ADD</code> commands found within the Dockerfile. </p>
<p> Warning, this will send a lot of data to the Docker daemon depending on the contents of the current directory. The build is run by the Docker daemon, not by the CLI, so the whole context must be transferred to the daemon. The Docker CLI reports &quot;Sending build context to Docker daemon&quot; when the context is sent to the daemon. </p>
<p> When the URL to a tarball archive or to a single Dockerfile is given, no context is sent from the client to the Docker daemon. In this case, the Dockerfile at the root of the archive and the rest of the archive will get used as the context of the build. When a Git repository is set as the <code>URL</code>, the repository is cloned locally and then sent as the context. </p>
<h2>OPTIONS</h2>
<p> <code>-f</code>, <code>&#8211;file</code> <i>PATH/Dockerfile</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Path to the Dockerfile to use. If the path is a relative path and you are<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;building from a local directory, then the path must be relative to that<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;directory. If you are building from a remote URL pointing to either a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;tarball or a Git repository, then the path must be relative to the root of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;the remote context. In all cases, the file must be within the build context.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;The default is&nbsp;<i>Dockerfile</i>. </p>
<p> <code>&#8211;squash</code> <i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>Experimental Only</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Once the image is built, squash the new layers into a new image with a single<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;new layer. Squashing does not destroy any existing image, rather it creates a new<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;image with the content of the squashed layers. This effectively makes it look<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;like all Dockerfile commands were created with a single layer. The build<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;cache is preserved with this method. </p>
<p> <code>Note</code>: using this option means the new image will not be able to take<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;advantage of layer sharing with other images and may use significantly more<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;space. </p>
<p> <code>Note</code>: using this option you may see significantly more space used due to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;storing two copies of the image, one for the build cache with all the cache<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;layers in tact, and one for the squashed version. </p>
<p> <code>&#8211;add-host</code> []<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Add a custom host-to-IP mapping&nbsp;(host:ip) </p>
<p> Add a line to /etc/hosts. The format is hostname:ip. The <code>&#8211;add-host</code> option can be set multiple times. </p>
<p> <code>&#8211;build-arg</code> <i>variable</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;name and value of a&nbsp;<code>buildarg</code>. </p>
<p> For example, if you want to pass a value for http_proxy, use<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;build-arg=http_proxy=&quot;<a rel="nofollow" href="http://some.proxy.url">http://some.proxy.url</a>&quot; </p>
<p> Users pass these values at build-time. Docker uses the buildargs as the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;environment context for command(s)&nbsp;run via the Dockerfile&#8217;s RUN instruction<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;or for variable expansion in other Dockerfile instructions. This is not meant<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;for passing secret values. Read more about the buildargs instruction &lt;<a rel="nofollow" href="https://docs.docker.com/engine/reference/builder/#arg">https://docs.docker.com/engine/reference/builder/#arg</a>&gt; </p>
<p> <code>&#8211;cache-from</code> &quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set image that will be used as a build cache source. </p>
<p> <code>&#8211;force-rm</code> <i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Always remove intermediate containers, even after unsuccessful builds. The default is&nbsp;<i>false</i>. </p>
<p> <code>&#8211;isolation</code> &quot;<i>default</i>&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Isolation specifies the type of isolation technology used by containers. </p>
<p> <code>&#8211;label</code> <i>label</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set metadata for an image </p>
<p> <code>&#8211;no-cache</code> <i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Do not use cache when building the image. The default is&nbsp;<i>false</i>. </p>
<p> <code>&#8211;iidfile</code> &quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Write the image ID to the file </p>
<p> <code>&#8211;help</code><br />
&nbsp;<wbr>&nbsp;Print usage statement </p>
<p> <code>&#8211;pull</code> <i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Always attempt to pull a newer version of the image. The default is&nbsp;<i>false</i>. </p>
<p> <code>&#8211;compress</code> <i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Compress the build context using gzip. The default is&nbsp;<i>false</i>. </p>
<p> <code>-q</code>, <code>&#8211;quiet</code> <i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Suppress the build output and print image ID on success. The default is&nbsp;<i>false</i>. </p>
<p> <code>&#8211;rm</code> <i>true</i>|<i>false</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Remove intermediate containers after a successful build. The default is&nbsp;<i>true</i>. </p>
<p> <code>-t</code>, <code>&#8211;tag</code> &quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Repository names&nbsp;(and optionally with tags)&nbsp;to be applied to the resulting<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;image in case of success. Refer to&nbsp;<code><a href="/docs/linux/man/1-docker-tag/">docker-tag</a>(1)</code>&nbsp;for more information<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;about valid tag names. </p>
<p> <code>-m</code>, <code>&#8211;memory</code> <i>MEMORY</i><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Memory limit </p>
<p> <code>&#8211;memory-swap</code> <i>number</i>[<i>S</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Combined memory plus swap limit;&nbsp;<i>S</i>&nbsp;is an optional suffix which can be one<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;of&nbsp;<code>b</code>&nbsp;(bytes),&nbsp;<code>k</code>&nbsp;(kilobytes),&nbsp;<code>m</code>&nbsp;(megabytes), or&nbsp;<code>g</code>&nbsp;(gigabytes). </p>
<p> This option can only be used together with <code>&#8211;memory</code>. The argument should always be larger than that of <code>&#8211;memory</code>. Default is double the value of <code>&#8211;memory</code>. Set to <code>-1</code> to enable unlimited swap. </p>
<p> <code>&#8211;network</code> <i>type</i><br />
&nbsp;<wbr>&nbsp;Set the networking mode for the RUN instructions during build. Supported standard<br />
&nbsp;<wbr>&nbsp;values are:&nbsp;<code>none</code>,&nbsp;<code>bridge</code>,&nbsp;<code>host</code>&nbsp;and&nbsp;<code>container:</code>&lt;<i>name</i>|<i>id</i>&gt;. Any other value<br />
&nbsp;<wbr>&nbsp;is taken as a custom network&#8217;s name or ID which this container should connect to. </p>
<p> In Linux, default is <code>bridge</code>. </p>
<p> <code>&#8211;shm-size</code> <i>SHM-SIZE</i><br />
&nbsp;<wbr>&nbsp;Size of&nbsp;/dev/shm. The format is&nbsp;&lt;number&gt;&lt;unit&gt;. number must be greater than 0.<br />
&nbsp;<wbr>&nbsp;Unit is optional and can be b&nbsp;(bytes), k&nbsp;(kilobytes), m&nbsp;(megabytes), or g&nbsp;(gigabytes). If you omit the unit, the system uses bytes.<br />
&nbsp;<wbr>&nbsp;If you omit the size entirely, the system uses 64m. </p>
<p> <code>&#8211;cpu-shares</code> <i>0</i><br />
&nbsp;<wbr>&nbsp;CPU shares&nbsp;(relative weight). </p>
<p> By default, all containers get the same proportion of CPU cycles.<br />
&nbsp;<wbr>&nbsp;CPU shares is a&nbsp;&#8216;relative weight&#8217;, relative to the default setting of 1024.<br />
&nbsp;<wbr>&nbsp;This default value is defined here: </p>
<dl>
<dt>
<dd>
<pre>
   cat /sys/fs/cgroup/cpu/cpu.shares
   1024
</pre>
</dl>
<p> You can change this proportion by adjusting the container&#8217;s CPU share<br />
&nbsp;<wbr>&nbsp;weighting relative to the weighting of all other running containers. </p>
<p> To modify the proportion from the default of 1024, use the <code>&#8211;cpu-shares</code><br />
&nbsp;<wbr>&nbsp;flag to set the weighting to 2 or higher. </p>
<dl>
<dt>
<dd>
<pre><code>
Container CPU share Flag
{
    C0
}
60 % of CPU-- cpu - shares 614(614 is 60 % of 1024)
{
    C1
}
40 % of CPU-- cpu - shares 410(410 is 40 % of 1024)
</code></pre>
</dl>
<p> The proportion is only applied when CPU-intensive processes are running.<br />
&nbsp;<wbr>&nbsp;When tasks in one container are idle, the other containers can use the<br />
&nbsp;<wbr>&nbsp;left-over CPU time. The actual amount of CPU time used varies depending on<br />
&nbsp;<wbr>&nbsp;the number of containers running on the system. </p>
<p> For example, consider three containers, where one has <code>&#8211;cpu-shares 1024</code> and<br />
&nbsp;<wbr>&nbsp;two others have&nbsp;<code>&#8211;cpu-shares 512</code>. When processes in all three<br />
&nbsp;<wbr>&nbsp;containers attempt to use 100%&nbsp;of CPU, the first container would receive<br />
&nbsp;<wbr>&nbsp;50%&nbsp;of the total CPU time. If you add a fourth container with&nbsp;<code>&#8211;cpu-shares 1024</code>,<br />
&nbsp;<wbr>&nbsp;the first container only gets 33%&nbsp;of the CPU. The remaining containers<br />
&nbsp;<wbr>&nbsp;receive 16.5%, 16.5%&nbsp;and 33%&nbsp;of the CPU. </p>
<dl>
<dt>
<dd>
<p>Container CPU share Flag CPU time<br />
{<br />
    C0<br />
}<br />
100 % &#8211;cpu &#8211; shares 1024 33 %<br />
{<br />
    C1<br />
}<br />
50 % &#8211;cpu &#8211; shares 512 16.5 %<br />
{<br />
    C2<br />
}<br />
50 % &#8211;cpu &#8211; shares 512 16.5 %<br />
{<br />
    C4<br />
}<br />
100 % &#8211;cpu &#8211; shares 1024 33 %
</dl>
<p> On a multi-core system, the shares of CPU time are distributed across the CPU<br />
&nbsp;<wbr>&nbsp;cores. Even if a container is limited to less than 100%&nbsp;of CPU time, it can<br />
&nbsp;<wbr>&nbsp;use 100%&nbsp;of each individual CPU core. </p>
<p> For example, consider a system with more than three cores. If you start one<br />
&nbsp;<wbr>&nbsp;container&nbsp;<code>{C0}</code>&nbsp;with&nbsp;<code>&#8211;cpu-shares 512</code>&nbsp;running one process, and another container<br />
&nbsp;<wbr>&nbsp;<code>{C1}</code>&nbsp;with&nbsp;<code>&#8211;cpu-shares 1024</code>&nbsp;running two processes, this can result in the following<br />
&nbsp;<wbr>&nbsp;division of CPU shares: </p>
<dl>
<dt>
<dd>
<pre><code>
PID container CPU CPU share 100
{
    C0
}
0 100 % of CPU0 101
{
    C1
}
1 100 % of CPU1 102
{
    C1
}
2 100 % of CPU2
</code></pre>
</dl>
<p> <code>&#8211;cpu-period</code> <i>0</i><br />
&nbsp;<wbr>&nbsp;Limit the CPU CFS&nbsp;(Completely Fair Scheduler)&nbsp;period. </p>
<p> Limit the container&#8217;s CPU usage. This flag causes the kernel to restrict the<br />
&nbsp;<wbr>&nbsp;container&#8217;s CPU usage to the period you specify. </p>
<p> <code>&#8211;cpu-quota</code> <i>0</i><br />
&nbsp;<wbr>&nbsp;Limit the CPU CFS&nbsp;(Completely Fair Scheduler)&nbsp;quota. </p>
<p> By default, containers run with the full CPU resource. This flag causes the kernel to restrict the container&#8217;s CPU usage to the quota you specify. </p>
<p> <code>&#8211;cpuset-cpus</code> <i>CPUSET-CPUS</i><br />
&nbsp;<wbr>&nbsp;CPUs in which to allow execution&nbsp;(0-3, 0,1). </p>
<p> <code>&#8211;cpuset-mems</code> <i>CPUSET-MEMS</i><br />
&nbsp;<wbr>&nbsp;Memory nodes&nbsp;(MEMs)&nbsp;in which to allow execution&nbsp;(0-3, 0,1). Only effective on<br />
&nbsp;<wbr>&nbsp;NUMA systems. </p>
<p> For example, if you have four memory nodes on your system (0-3), use &#8211;cpuset-mems 0,1 to ensure the processes in your Docker container only use memory from the first two memory nodes. </p>
<p> <code>&#8211;cgroup-parent</code> <i>CGROUP-PARENT</i><br />
&nbsp;<wbr>&nbsp;Path to cgroups under which the container&#8217;s cgroup are created. </p>
<p> If the path is not absolute, the path is considered relative to the cgroups path of the init process. Cgroups are created if they do not already exist. </p>
<p> <code>&#8211;target</code> &quot;&quot;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;Set the target build stage name. </p>
<p> <code>&#8211;ulimit</code> []<br />
&nbsp;<wbr>&nbsp;Ulimit options </p>
<p> For more information about ulimit see Setting ulimits in a container &lt;<a rel="nofollow" href="https://docs.docker.com/engine/reference/commandline/run/#set-ulimits-in-container---ulimit">https://docs.docker.com/engine/reference/commandline/run/#set-ulimits-in-container&#8212;ulimit</a>&gt; </p>
<h2>EXAMPLES</h2>
<h2>Building an image using a Dockerfile located inside the current directory</h2>
<p> Docker images can be built using the build command and a Dockerfile: </p>
<dl>
<dt>
<dd>
<pre>
docker build .
</pre>
</dl>
<p> During the build process Docker creates intermediate images. In order to keep them, you must explicitly set &#8211;rm false. </p>
<dl>
<dt>
<dd>
<pre>
docker build --rm false .
</pre>
</dl>
<p> A good practice is to make a sub-directory with a related name and create the Dockerfile in that directory. For example, a directory called mongo may contain a Dockerfile to create a Docker MongoDB image. Likewise, another directory called httpd may be used to store Dockerfiles for Apache web server images. </p>
<p> It is also a good practice to add the files required for the image to the sub-directory. These files will then be specified with the COPY or ADD instructions in the Dockerfile. </p>
<p> Note: If you include a tar file (a good practice), then Docker will automatically extract the contents of the tar file specified within the ADD instruction into the specified target. </p>
<h2>Building an image and naming that image</h2>
<p> A good practice is to give a name to the image you are building. Note that only a-z0-9-_. should be used for consistency. There are no hard rules here but it is best to give the names consideration. </p>
<p> The <code>-t</code>/<code>&#8211;tag</code> flag is used to rename an image. Here are some examples: </p>
<p> Though it is not a good practice, image names can be arbitrary: </p>
<dl>
<dt>
<dd>
<pre>
docker build -t myimage .
</pre>
</dl>
<p> A better approach is to provide a fully qualified and meaningful repository, name, and tag (where the tag in this context means the qualifier after the &quot;:&quot;). In this example we build a JBoss image for the Fedora repository and give it the version 1.0: </p>
<dl>
<dt>
<dd>
<pre>
docker build -t fedora/jboss:1.0 .
</pre>
</dl>
<p> The next example is for the &quot;whenry&quot; user repository and uses Fedora and JBoss and gives it the version 2.1 : </p>
<dl>
<dt>
<dd>
<pre>
docker build -t whenry/fedora-jboss:v2.1 .
</pre>
</dl>
<p> If you do not provide a version tag then Docker will assign latest: </p>
<dl>
<dt>
<dd>
<pre>
docker build -t whenry/fedora-jboss .
</pre>
</dl>
<p> When you list the images, the image above will have the tag latest. </p>
<p> You can apply multiple tags to an image. For example, you can apply the latest tag to a newly built image and add another tag that references a specific version. For example, to tag an image both as whenry/fedora-jboss:latest and whenry/fedora-jboss:v2.1, use the following: </p>
<dl>
<dt>
<dd>
<pre>
docker build -t whenry/fedora-jboss:latest -t whenry/fedora-jboss:v2.1 .
</pre>
</dl>
<p> So renaming an image is arbitrary but consideration should be given to a useful convention that makes sense for consumers and should also take into account Docker community conventions. </p>
<h2>Building an image using a URL</h2>
<p> This will clone the specified GitHub repository from the URL and use it as context. The Dockerfile at the root of the repository is used as Dockerfile. This only works if the GitHub repository is a dedicated repository. </p>
<dl>
<dt>
<dd>
<pre>
docker build github.com/scollier/purpletest
</pre>
</dl>
<p> Note: You can set an arbitrary Git repository via the git:// scheme. </p>
<h2>Building an image using a URL to a tarball&#8217;ed context</h2>
<p> This will send the URL itself to the Docker daemon. The daemon will fetch the tarball archive, decompress it and use its contents as the build context. The Dockerfile at the root of the archive and the rest of the archive will get used as the context of the build. If you pass an <code>-f PATH/Dockerfile</code> option as well, the system will look for that file inside the contents of the tarball. </p>
<dl>
<dt>
<dd>
<pre>
docker build -f dev/Dockerfile <a rel="nofollow" href="https://10.10.10.1/docker/context.tar.gz">https://10.10.10.1/docker/context.tar.gz</a>
</pre>
</dl>
<p> Note: supported compression formats are &#8216;xz&#8217;, &#8216;bzip2&#8217;, &#8216;gzip&#8217; and &#8216;identity&#8217; (no compression). </p>
<h2>Specify isolation technology for container (&#8211;isolation)</h2>
<p> This option is useful in situations where you are running Docker containers on Windows. The &#8211;isolation &lt;value&gt; option sets a container&#8217;s isolation technology. On Linux, the only supported is the default option which uses Linux namespaces. On Microsoft Windows, you can specify these values: </p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> default: Use the value specified by the Docker daemon&#8217;s &#8211;exec-opt . If the daemon does not specify an isolation technology, Microsoft Windows uses process as its default value.</p>
<dt>&bull;</p>
<dd> process: Namespace isolation only.</p>
<dt>&bull;</p>
<dd> hyperv: Hyper-V hypervisor partition-based isolation. </p>
</dl>
</dl>
<p> Specifying the &#8211;isolation flag without a value is the same as setting &#8211;isolation &quot;default&quot;. </p>
<h2>HISTORY</h2>
<p> March 2014, Originally compiled by William Henry (whenry at redhat dot com) based on docker.com source material and internal work. June 2014, updated by Sven Dowideit SvenDowideit [at] home.org.au &lt;mailto:SvenDowideit [at] home.org.au&gt; June 2015, updated by Sally O&#8217;Malley somalley [at] redhat.com &lt;mailto:somalley [at] redhat.com&gt; August 2020, Updated by Des Preston despreston [at] gmail.com &lt;mailto:despreston [at] gmail.com&gt; </p>
<h2>Index</h2>
